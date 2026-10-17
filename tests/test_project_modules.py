"""Regression checks for permitted/rejected dependencies and complete discovery."""

from pathlib import Path
import tempfile
import unittest

from scripts.project_modules import audit_source, imports, validate


REPO = Path(__file__).resolve().parent.parent


class PublicLibrariesTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        self.write("lakefile.toml", (REPO / "lakefile.toml").read_text())
        self.write("DPGraph.lean", "module\npublic import DPGraph.Core\n")
        self.write("DPGraph/Core.lean", "module\npublic import Mathlib.Data.Set.Defs\n")
        self.write("FormalCD.lean", "module\npublic import DPGraph\n")
        self.write("Clafer.lean", "module\npublic import FormalCD\n")
        self.write("FormalCD/.gitkeep", "")
        self.write("Clafer/.gitkeep", "")
        self.write("tests/axiom_audit.lean", (REPO / "tests/axiom_audit.lean").read_text())

    def write(self, path, content):
        file = self.repo / path
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text(content)

    def test_permitted_graph_and_unreachable_new_module_are_fully_enumerated(self):
        self.write("FormalCD/Internal/New.lean", "module\nimport DPGraph.Core\n")
        modules, _ = validate(self.repo)
        self.assertIn("FormalCD.Internal.New", modules)
        source = audit_source(self.repo, modules)
        for module in modules:
            self.assertIn(f"import all {module}\n", source)

    def test_repository_includes_every_delivered_module_and_examples(self):
        modules, tests = validate(REPO)
        self.assertEqual(set(modules), {
            "DPGraph", "DPGraph.Signature", "DPGraph.Formula", "DPGraph.Basic",
            "DPGraph.Morphism", "DPGraph.Examples", "FormalCD", "Clafer",
            "DPGraph.Category", "DPGraph.Semantics", "DPGraph.SemanticsExamples",
            "DPGraph.ModelTransport", "DPGraph.Pushout.Basic",
            "DPGraph.Pushout.Models",
        })
        self.assertIn(Path("tests/public_imports.lean"), tests)

    def test_reverse_edges_including_helper_and_root_imports_are_rejected(self):
        for path, dep in [("DPGraph/Core.lean", "FormalCD"),
                          ("DPGraph.lean", "Clafer"),
                          ("FormalCD/Helper.lean", "Clafer")]:
            with self.subTest(path=path, dep=dep):
                original = (self.repo / path).read_text() if (self.repo / path).exists() else None
                self.write(path, f"module\npublic import {dep}\n")
                with self.assertRaisesRegex(ValueError, "reverse layer import"):
                    validate(self.repo)
                if original is None:
                    (self.repo / path).unlink()
                else:
                    self.write(path, original)

    def test_transitive_helper_cannot_hide_reverse_dependency(self):
        self.write("DPGraph/Core.lean", "module\nimport DPGraph.Helper\n")
        self.write("DPGraph/Helper.lean", "module\nimport FormalCD\n")
        with self.assertRaisesRegex(ValueError, "DPGraph.Helper -> FormalCD"):
            validate(self.repo)

    def test_unknown_helpers_and_obsolete_roots_cannot_escape_coverage(self):
        for path in ["Helper.lean", "ClaferLean.lean", "Other/Unimported.lean"]:
            with self.subTest(path=path):
                self.write(path, "module\nimport Clafer\n")
                with self.assertRaisesRegex(ValueError, "outside public libraries"):
                    validate(self.repo)
                (self.repo / path).unlink()

    def test_import_of_unowned_or_missing_module_is_rejected(self):
        for dep in ["Helper", "ClaferLean.DPGraph", "DPGraph.Missing", "Mathlib"]:
            with self.subTest(dependency=dep):
                self.write("DPGraph/Core.lean", f"module\nimport {dep}\n")
                with self.assertRaises(ValueError):
                    validate(self.repo)

    def test_cycles_are_rejected(self):
        self.write("DPGraph/Core.lean", "module\nimport DPGraph\n")
        with self.assertRaisesRegex(ValueError, "cycle"):
            validate(self.repo)

    def test_empty_future_library_still_needs_directory_for_lake_glob(self):
        (self.repo / "FormalCD/.gitkeep").unlink()
        (self.repo / "FormalCD").rmdir()
        with self.assertRaisesRegex(ValueError, "missing library directory"):
            validate(self.repo)

    def test_headers_handle_comments_and_reject_unsupported_forms(self):
        self.assertEqual(imports("module\n/- import Clafer /- nested -/ -/\n"
                                 "public import DPGraph.Core -- comment\n"
                                 "meta import all Mathlib.Data.Set.Defs\n"),
                         ["DPGraph.Core", "Mathlib.Data.Set.Defs"])
        for source in ["import DPGraph Clafer", "import\n Clafer", "import «Clafer»",
                       "def x := 1\nimport Clafer", "/- unfinished"]:
            with self.subTest(source=source), self.assertRaises(ValueError):
                imports(source)

    def test_removed_glob_and_audit_marker_fail_closed(self):
        self.write("lakefile.toml", (REPO / "lakefile.toml").read_text().replace('"DPGraph.**"', '"DPGraph.Core"'))
        with self.assertRaisesRegex(ValueError, "every DPGraph module"):
            validate(self.repo)
        self.write("tests/axiom_audit.lean", "module\n")
        with self.assertRaisesRegex(ValueError, "import marker"):
            audit_source(self.repo, ["DPGraph"])

    def test_hidden_or_symlinked_source_is_rejected(self):
        self.write("DPGraph/.Hidden.lean", "module\n")
        with self.assertRaises(ValueError):
            validate(self.repo)
        (self.repo / "DPGraph/.Hidden.lean").unlink()
        (self.repo / "DPGraph/Alias.lean").symlink_to(self.repo / "DPGraph/Core.lean")
        with self.assertRaisesRegex(ValueError, "symlink"):
            validate(self.repo)


if __name__ == "__main__":
    unittest.main()
