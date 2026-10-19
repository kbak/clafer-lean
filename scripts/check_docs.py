"""Check local links and heading anchors in living Markdown documentation."""

from functools import lru_cache
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

from markdown_it import MarkdownIt


PARSER = MarkdownIt("commonmark").enable(["table", "strikethrough"])


@lru_cache(maxsize=None)
def anchors(path):
    text = path.read_text(encoding="utf-8")
    tokens = PARSER.parse(text)
    result = set()
    for i, token in enumerate(tokens):
        if token.type != "inline" or not i or tokens[i - 1].type != "heading_open":
            continue
        title = "".join(child.content for child in token.children or []
                        if child.type in ("text", "code_inline", "softbreak"))
        slug = re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")
        anchor, n = slug, 0
        while anchor in result:
            n += 1
            anchor = f"{slug}-{n}"
        result.add(anchor)
    result.update(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', text))
    return result


def living_documents(root):
    return sorted([*root.glob("*.md"),
                   *(path for path in (root / "docs").rglob("*.md")
                     if not path.is_relative_to(root / "docs/changes"))])


# [impl->req~lean-validation~1]
def check(root):
    errors, count = [], 0
    anchors.cache_clear()
    for path in living_documents(root):
        for token in PARSER.parse(path.read_text(encoding="utf-8")):
            for child in token.children or []:
                target = (child.attrGet("href") if child.type == "link_open" else
                          child.attrGet("src") if child.type == "image" else None)
                if target is None:
                    continue
                parts = urlsplit(target)
                if parts.scheme or parts.netloc:
                    continue
                destination = (path.parent / unquote(parts.path)).resolve() if parts.path else path
                count += 1
                problem = None
                if not destination.is_relative_to(root):
                    problem = "link escapes repository"
                elif not destination.exists():
                    problem = "missing target"
                elif (parts.fragment and destination.suffix == ".md" and
                      unquote(parts.fragment) not in anchors(destination)):
                    problem = "missing heading anchor"
                if problem:
                    errors.append(f"{path.relative_to(root)}: {problem}: {target}")
    return count, errors


if __name__ == "__main__":
    count, errors = check(Path.cwd().resolve())
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Checked {count} local documentation links; {len(errors)} errors")
    sys.exit(bool(errors))
