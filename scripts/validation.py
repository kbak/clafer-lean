"""Select documentation checks using the same source capture as pinned IntentBond.

The plan lives outside source. The shared check verifies it against the actual
IntentBond snapshot before taking the short path; a selection is not evidence
that tests passed. Without a usable plan the shared check runs full validation.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import stat
import subprocess
import sys
import tempfile


def digest(manifest):
    return hashlib.sha256(json.dumps(manifest, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=True).encode()).hexdigest()


def documentation(path):
    return path == "README.md" or (path.startswith("docs/") and path.endswith(".md"))


# [impl->req~lean-validation~1]
def classify(base, candidate):
    before = {entry["path"]: entry for entry in base}
    after = {entry["path"]: entry for entry in candidate}
    changed = sorted(path for path in before.keys() | after.keys()
                     if before.get(path) != after.get(path))
    if not changed:
        return "full", "No documentation changes to validate", changed
    for path in changed:
        if not documentation(path):
            return "full", f"Changed non-documentation source: {path}", changed
        entries = [items[path] for items in (before, after) if path in items]
        if any(entry["mode"] != "100644" for entry in entries):
            return "full", f"Changed executable or symlink: {path}", changed
    return "docs", "Only regular Markdown documentation changed", changed


def prepare(repo, base, candidate, force_full=False):
    # Use the pinned capture implementation: includes untracked source and
    # deletions, ignores build outputs, and does not apply export attributes.
    from intentbond.common import CheckError
    from intentbond.snapshot import repository, resolve_commit, snapshot

    plan = {"version": 1, "base_ref": base, "candidate_ref": candidate,
            "mode": "full", "reason": "No complete baseline comparison"}
    try:
        with tempfile.TemporaryDirectory(prefix="clafer-selection-") as directory:
            root = Path(directory)
            repo = repository(repo)
            before = snapshot(repo, resolve_commit(repo, base), root / "base")
            after = snapshot(repo, candidate, root / "candidate")
            mode, reason, changed = classify(before.manifest, after.manifest)
            plan.update(base=before.identity(), candidate=after.identity(),
                        base_manifest=before.manifest, candidate_manifest=after.manifest,
                        mode=mode, reason=reason, changed=changed)
    except (CheckError, OSError) as exc:
        plan["reason"] = f"Comparison unavailable: {exc}"
    if force_full:
        plan.update(mode="full", reason="Full validation requested")
    return plan


def validate_manifest(manifest):
    paths = set()
    for entry in manifest:
        path = entry["path"]
        parts = PurePosixPath(path).parts
        if (not parts or path != PurePosixPath(path).as_posix() or
                PurePosixPath(path).is_absolute() or ".." in parts or
                ".git" in parts or "\\" in path or path in paths):
            raise ValueError("Invalid source path")
        if entry["mode"] not in ("100644", "100755", "120000"):
            raise ValueError("Unsupported source mode")
        if len(entry["sha256"]) != 64 or any(c not in "0123456789abcdef" for c in entry["sha256"]):
            raise ValueError("Invalid source digest")
        paths.add(path)


def directory_manifest(root):
    entries = []
    for directory, dirs, files in os.walk(root, followlinks=False):
        for name in list(dirs):
            if (Path(directory) / name).is_symlink():
                dirs.remove(name)
                files.append(name)
        for name in files:
            path = Path(directory) / name
            info = path.lstat()
            if stat.S_ISLNK(info.st_mode):
                mode, data = "120000", os.fsencode(os.readlink(path))
            elif stat.S_ISREG(info.st_mode):
                mode = "100755" if info.st_mode & stat.S_IXUSR else "100644"
                data = path.read_bytes()
            else:
                raise ValueError("Unsupported source file")
            entries.append({"path": path.relative_to(root).as_posix(), "mode": mode,
                            "sha256": hashlib.sha256(data).hexdigest()})
    return sorted(entries, key=lambda entry: entry["path"])


def select_snapshot(root, plan_path):
    """Fail closed to full validation on absent, stale or malformed plans."""
    try:
        if plan_path.resolve().is_relative_to(root.resolve()):
            raise ValueError("Selection plan must be outside captured source")
        plan = json.loads(plan_path.read_text())
        if plan["version"] != 1 or plan["mode"] != "docs":
            return "full", plan.get("reason", "Full validation selected")
        for key in ("base", "candidate"):
            manifest = plan[key + "_manifest"]
            validate_manifest(manifest)
            if digest(manifest) != plan[key]["sha256"]:
                raise ValueError("Manifest identity mismatch")
        mode, reason, _ = classify(plan["base_manifest"], plan["candidate_manifest"])
        if mode != "docs":
            return mode, reason
        if directory_manifest(root) != plan["candidate_manifest"]:
            raise ValueError("Captured source differs from selection plan")
        return "docs", f"{reason}; baseline {plan['base']['commit']}"
    except (OSError, ValueError, KeyError, TypeError) as exc:
        return "full", f"Documentation selection unavailable: {exc}"


def write_plan(path, plan, repo):
    path = path.resolve()
    if path.is_relative_to(repo.resolve()):
        raise ValueError("Keep selection plans outside the repository")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x") as stream:
        json.dump(plan, stream, indent=2)
        stream.write("\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("prepare", "check"):
        command = commands.add_parser(name)
        command.add_argument("--repo", type=Path, default=Path.cwd())
        command.add_argument("--base", required=True)
        command.add_argument("--candidate", default="worktree")
        command.add_argument("--full", action="store_true")
        command.add_argument("--out", type=Path, required=True)
        if name == "check":
            command.add_argument("--scope", type=Path)
    command = commands.add_parser("select")
    command.add_argument("--plan", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "select":
        root = Path.cwd()
        if os.environ.get("PROJECT_DIR") != str(root) or (root / ".git").exists():
            mode, reason = "full", "No isolated IntentBond snapshot"
        else:
            mode, reason = select_snapshot(root, args.plan)
        print(f"[check] Selection: {mode}; {reason}", file=sys.stderr)
        print(mode)
        return 0
    plan = prepare(args.repo, args.base, args.candidate, args.full)
    plan_path = args.out if args.command == "prepare" else args.out.with_name(args.out.name + "-selection.json")
    write_plan(plan_path, plan, args.repo)
    print(f"Validation: {plan['mode']}; {plan['reason']}", flush=True)
    if args.command == "prepare":
        return 0
    # Freeze resolved refs, so a moving branch cannot change the comparison.
    base = plan.get("base", {}).get("commit", args.base)
    candidate = args.candidate if args.candidate == "worktree" else plan.get("candidate", {}).get("commit", args.candidate)
    command = [sys.executable, "-m", "intentbond", "check", "--repo", str(args.repo.resolve()),
               "--base", base, "--candidate", candidate, "--out", str(args.out.resolve())]
    if args.scope:
        command += ["--scope", str(args.scope.resolve())]
    return subprocess.call(command, env=dict(os.environ, CLAFER_VALIDATION_PLAN=str(plan_path.resolve())))


if __name__ == "__main__":
    sys.exit(main())
