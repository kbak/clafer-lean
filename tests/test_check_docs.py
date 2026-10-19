"""Exercise link failures that formatting and document moves can introduce."""

from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import check_docs


# [itest->req~lean-validation~1]
class DocumentationTest(unittest.TestCase):
    def test_topic_filenames_and_conventional_or_frozen_exceptions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            for name in ("README.md", "CONTRIBUTING.md", "SECURITY.md", "AGENTS.md",
                         "CLAUDE.md", "tests/fixtures/README.md",
                         "docs/changes/frozen/OLD_NAME.md", "docs/architecture.md",
                         "docs/sources.md", "docs/nested/appendix-f.md"):
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("# Document\n")
            self.assertEqual(check_docs.check(root), (0, []))
            for name in ("Uppercase.md", "under_score.md", "upper-extension.MD",
                         "space name.md", "non-ascii-é.md", "double--hyphen.md"):
                with self.subTest(name=name):
                    path = root / "docs/nested" / name
                    path.write_text("# Document\n")
                    count, errors = check_docs.check(root)
                    self.assertEqual(count, 0)
                    self.assertEqual(len(errors), 1)
                    self.assertIn(f"docs/nested/{name}: topic filename", errors[0])
                    path.unlink()

    def test_local_files_anchors_images_and_frozen_records(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            (root / "docs/changes").mkdir(parents=True)
            (root / "docs/page.md").write_text("# A `code` heading\n\n# Repeated\n\n# Repeated\n")
            (root / "docs/picture.svg").write_text("<svg/>")
            (root / "docs/changes/frozen.md").write_text("[historical](gone.md)\n")
            readme = root / "README.md"
            readme.write_text("[page](docs/page.md#a-code-heading)\n\n"
                              "[repeat](docs/page.md#repeated-1)\n\n"
                              "![image](docs/picture.svg)\n\n"
                              "[remote](https://example.invalid/)\n\n"
                              "`[code](missing.md)`\n")
            self.assertEqual(check_docs.check(root), (3, []))
            readme.write_text("[broken](docs/page.md#absent)\n\n![missing](gone.svg)\n\n"
                              "[outside](../outside.md)\n")
            count, errors = check_docs.check(root)
            self.assertEqual(count, 3)
            self.assertEqual(len(errors), 3)
            self.assertIn("missing heading anchor", errors[0])
            self.assertIn("missing target", errors[1])
            self.assertIn("escapes repository", errors[2])


if __name__ == "__main__":
    unittest.main()
