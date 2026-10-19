"""Pinned live exports, strict rejection boundary and deterministic replay."""
import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts/verification"))
import protocol as p
from capture import capture

FIXTURES = ROOT / "tests/fixtures/importer"


def runtime():
    executable = os.environ.get("CLAFER_CAPTURE") or shutil.which("clafer-capture")
    if not executable:
        raise RuntimeError("Build the pinned exporter with scripts/verification/build.py and set CLAFER_CAPTURE; see docs/resolved-import.md")
    executable = Path(executable)
    build = Path(os.environ.get("CLAFER_CAPTURE_BUILD", str(executable.with_name("build.json"))))
    return executable, build


class PinnedImportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.exporter, cls.build = runtime()
        cls.scratch = tempfile.TemporaryDirectory()
        cls.directory = Path(cls.scratch.name)
        cls.receipts = {}
        cls.bundles = {}
        for fixture in sorted(FIXTURES.glob("*.cfr")):
            receipt = p.loads(subprocess.check_output([str(cls.exporter), str(fixture)], timeout=120))
            if receipt["status"] != "captured":
                raise AssertionError(receipt)
            cls.receipts[fixture.stem] = p.seal_receipt(receipt)
            nodes, _ = p.decode_ir(p.loads(receipt["json"]))
            # Explicit test bound, unrelated to compiler scope inference/global cards.
            bounds = {"root": 1, **{n["uid"]: 10 for n in nodes}}
            directory = cls.directory / fixture.stem
            capture(fixture, cls.exporter, cls.build, bounds, directory)
            cls.bundles[fixture.stem] = directory
        cls.bag = p.loads(cls.receipts["set_and_bag_references"]["json"])

    @classmethod
    def tearDownClass(cls):
        cls.scratch.cleanup()

    def rejected_ir(self, change, code=None, base=None):
        doc = copy.deepcopy(base or self.bag)
        change(doc)
        with self.assertRaises(p.Rejection) as error:
            p.decode_ir(doc)
        if code:
            self.assertEqual(code, error.exception.code)
        return error.exception

    def test_live_exports_and_replay(self):
        for name, directory in self.bundles.items():
            with self.subTest(name=name):
                core, metadata = p.import_bundle(directory)
                self.assertEqual((core, metadata), p.import_bundle(directory))
                self.assertEqual("clafer-import/1", core["schema"])
                self.assertEqual(1, metadata["bounds"]["root"])
                self.assertEqual((directory / "model.als").read_bytes(), self.receipts[name]["alloy"].encode())
                # The Lean-side normalization/admission is exercised on real exports.
                result = self.lean(core, None)
                self.assertEqual("admitted", result["status"], result)
        nodes, _ = p.decode_ir(p.loads(self.receipts["identities"]["json"]))
        repeats = [n for n in nodes if n["name"] == "same"]
        self.assertEqual(2, len(repeats))
        self.assertNotEqual(repeats[0]["uid"], repeats[1]["uid"])
        self.assertEqual("c0_Base", repeats[0]["super"])
        self.assertEqual([0, 0], next(n for n in nodes if n["name"] == "Unused")["card"])

    def lean(self, core, candidate):
        proc = subprocess.run(["lake", "env", "lean", "--run", "Clafer/Verification/ImportMain.lean"],
            cwd=ROOT, input=p.encoded(dict(core, candidate=candidate)), capture_output=True, timeout=120, check=True)
        return p.loads(proc.stdout)

    def test_duplicate_keys_and_non_json_numbers(self):
        for raw in ['{"x":0,"x":1}', '{"x":{"x":0,"x":1}}', '{"x":NaN}', '{"x":Infinity}', '{']:
            with self.subTest(raw=raw), self.assertRaises(p.Rejection):
                p.loads(raw)

    def test_ids_incidence_and_cards(self):
        def field(key, value, i=0):
            return lambda d: d["iModule"]["_mDecls"][i]["_iClafer"].__setitem__(key, value)
        for value in [None, [], [0], [0, -2], [-1, -1], [3, 2], [0.5, 1], [False, 1], [0, 1, 2]]:
            with self.subTest(value=value):
                self.rejected_ir(field("_card", value), "interval")
                self.rejected_ir(field("_glCard", value), "interval")
        for uid in ["root", "clafer", "int", "", "r!", "c0_a", "sig", "String", "seq"]:
            with self.subTest(uid=uid):
                self.rejected_ir(field("_uid", uid))
        self.rejected_ir(field("_parentUID", ""), "parent_incidence")
        self.rejected_ir(field("_parentUID", "c0_a"), "parent_incidence")
        self.rejected_ir(field("_gcard", None), "fields")
        self.rejected_ir(field("new_semantic_field", True), "fields")
        self.rejected_ir(field("_cinPos", [1, 2]), "position")
        self.rejected_ir(field("_ident", "invalid name"), "name_syntax")

    def test_all_excluded_expression_and_binding_tags(self):
        def ref(d):
            return d["iModule"]["_mDecls"][2]["_iClafer"]["_reference"]["_ref"]
        for tag in ["IDeclPExp", "IFunExp", "IInt", "IReal", "IDouble", "IStr", "Unknown"]:
            with self.subTest(tag=tag):
                self.rejected_ir(lambda d: ref(d).__setitem__("_exp", {"tag": tag}), "expression")
        for tag in ["LocalBind", "NoBind", "Unknown"]:
            with self.subTest(tag=tag):
                self.rejected_ir(lambda d: ref(d)["_exp"].__setitem__("_binding", {"tag": tag}), "binding")
        for tag in ["TBoolean", "TString", "TInteger", "TDouble", "TReal", "TMap", "TUnion", "Unknown"]:
            with self.subTest(tag=tag):
                self.rejected_ir(lambda d: ref(d).__setitem__("_iType", {"tag": tag}), "type_metadata")
        self.rejected_ir(lambda d: ref(d)["_exp"].__setitem__("_modName", "module"), "qualified_id")
        self.rejected_ir(lambda d: ref(d)["_exp"]["_binding"].__setitem__("contents", "c0_a"), "binding_identity")
        self.rejected_ir(lambda d: ref(d)["_iType"].__setitem__("_hi", ["c0_a"]), "type_hierarchy")
        self.rejected_ir(lambda d: ref(d)["_exp"].__setitem__("_isTop", False), "top_flag")
        for uid in ["missing", "integer"]:
            def change(d):
                ref(d)["_exp"]["_binding"]["contents"] = uid
                ref(d)["_exp"]["_sident"] = uid
            self.rejected_ir(change, "dangling_id" if uid == "missing" else "predefined_target")

    def test_excluded_elements_and_modifiers(self):
        for tag in ["IEConstraint", "IEGoal", "Unknown"]:
            for hard in [True, False]:
                with self.subTest(tag=tag, hard=hard):
                    self.rejected_ir(lambda d: d["iModule"]["_mDecls"].append({"tag": tag, "_isHard": hard}), "element")
        self.rejected_ir(lambda d: d.__setitem__("objectives", {"max": [1]}), "objectives")
        for modifier in ["_initial", "_final"]:
            self.rejected_ir(lambda d: d["iModule"]["_mDecls"][1]["_iClafer"]["_modifiers"].__setitem__(modifier, True), "temporal_modifier")
        for modifier in ["FinalRefTarget", "FinalRef", "FinalTarget", "Unknown"]:
            self.rejected_ir(lambda d: d["iModule"]["_mDecls"][2]["_iClafer"]["_reference"].__setitem__("_refModifier", modifier), "reference_modifier")

    def test_combination_guards(self):
        self.rejected_ir(lambda d: d["iModule"]["_mDecls"][0]["_iClafer"].__setitem__("_card", [0, 1]), "abstract_fragment")
        self.rejected_ir(lambda d: d["iModule"]["_mDecls"][0]["_iClafer"]["_gcard"].__setitem__("_interval", [0, 1]), "abstract_fragment")
        self.rejected_ir(lambda d: d["iModule"]["_mDecls"][1]["_iClafer"]["_gcard"].__setitem__("_interval", [1, 1]), "empty_positive_group")
        def cycle(d):
            c = d["iModule"]["_mDecls"][0]["_iClafer"]
            c["_super"] = copy.deepcopy(d["iModule"]["_mDecls"][1]["_iClafer"]["_super"])
        self.rejected_ir(cycle, "super_cycle")
        def reference_inheritance(d):
            d["iModule"]["_mDecls"][2]["_iClafer"]["_super"] = copy.deepcopy(d["iModule"]["_mDecls"][1]["_iClafer"]["_super"])
        self.rejected_ir(reference_inheritance, "inheritance_fragment")

    def test_source_audit_before_desugaring(self):
        cases = ["enum Color = red | blue\n", "x = 1\n", "x -> integer\n",
                 "x\n[ some x ]\n", "x\nassert [ some x ]\n", "x\n<< max #x >>\n",
                 "initial x\n", "final x\n", "x\n[alloy| fact { no univ } |]\n",
                 "x\n[choco| hello |]\n", "//# OPTIONS --keep_unused\nx\n",
                 "x\ny\nz -> x ++ y\n", "abstract A\n  x\n", "a\n  b\n  r -> b\n"]
        for index, text in enumerate(cases):
            with self.subTest(source=text):
                source = self.directory / f"rejected-{index}.cfr"
                source.write_text(text)
                result = p.loads(subprocess.check_output([str(self.exporter), str(source)], timeout=120))
                if result["status"] == "captured":
                    with self.assertRaises(p.Rejection):
                        p.validate_generation(p.seal_receipt(result), source.read_bytes(), result["json"].encode(), result["alloy"].encode())
                else:
                    self.assertIn(result["status"], ["unsupported", "compiler_rejected"])

    def test_receipts_versions_hashes_and_options(self):
        receipt = self.receipts["set_and_bag_references"]
        source = (FIXTURES / "set_and_bag_references.cfr").read_bytes()
        changes = [lambda g: g.__setitem__("schema", "unknown"),
            lambda g: g.__setitem__("backend", "tmp.als"),
            lambda g: g.__setitem__("scopes", [["c0_a", 4]]),
            lambda g: g.__setitem__("strings", [[0, "str"]]),
            lambda g: g.__setitem__("post_strings", {}),
            lambda g: g.__setitem__("consumed_map", g["consumed_map"][:-1]),
            lambda g: g.__setitem__("observations", []),
            lambda g: g["source_audit"].__setitem__("errors", ["enum"]),
            lambda g: g["consumed_map"][0][1].__setitem__("_ident", "changed")]
        for key, value in p.OPTIONS.items():
            changes.append(lambda g, k=key, v=value: g["effective_options"].__setitem__(k, not v if type(v) is bool else "bad"))
        for change in changes:
            g = copy.deepcopy(receipt)
            change(g)
            g = p.seal_receipt(g)
            with self.subTest(change=repr(change)), self.assertRaises(p.Rejection):
                p.validate_generation(g, source, receipt["json"].encode(), receipt["alloy"].encode())
        original = self.bundles["empty"]
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            for file in original.iterdir():
                shutil.copy(file, directory / file.name)
            manifest = p.loads((directory / "manifest.json").read_bytes())
            (directory / "manifest.json").write_bytes((FIXTURES / "malformed-version.json").read_bytes())
            with self.assertRaisesRegex(p.Rejection, "version"):
                p.import_bundle(directory)
            for key in ["schema", "compiler_commit", "compiler_version", "export_schema"]:
                altered = dict(manifest, **{key: "unknown"})
                (directory / "manifest.json").write_bytes(p.encoded(altered))
                with self.assertRaises(p.Rejection):
                    p.import_bundle(directory)
            (directory / "manifest.json").write_bytes(p.encoded(manifest))
            (directory / "model.als").write_bytes(b"tampered")
            with self.assertRaisesRegex(p.Rejection, "artifact_hash"):
                p.import_bundle(directory)

    def test_scalar_types_build_identity_and_injected_facts(self):
        source = (FIXTURES / "identities.cfr").read_bytes()
        base = self.receipts["identities"]
        mutations = [
            lambda g: g.__setitem__("json", None),
            lambda g: g.__setitem__("implicit_template", None),
            lambda g: g.__setitem__("observations", [None]),
            lambda g: g["source_audit"].__setitem__("ast", 1),
            lambda g: g["source_audit"].__setitem__("tokens", [{"T_PosLineComment": 1}]),
            lambda g: g["observations"][0].__setitem__("reference_refinement", []),
            lambda g: g["observations"][0].__setitem__("parent_fact", ["bad"]),
            lambda g: g["post_strings"]["_mDecls"][0]["_iClafer"]["_modifiers"].__setitem__("_abstract", 1),
            lambda g: next(row for row in g["consumed_map"] if row[0] == "int").__setitem__(1,
                list(dict(g["consumed_map"])["int"].items())),
        ]
        for mutate in mutations:
            receipt = copy.deepcopy(base)
            mutate(receipt)
            receipt = p.seal_receipt(receipt)
            with self.assertRaises(p.Rejection):
                p.validate_generation(receipt, source, base["json"].encode(), base["alloy"].encode())
        for slot in ["header", "extra_fragment", "inside_fragment"]:
            receipt = copy.deepcopy(base)
            injection = "fact { no univ }\n"
            if slot == "header":
                receipt["header"] += injection
            elif slot == "extra_fragment":
                receipt["top_fragments"].append(injection)
            else:
                receipt["top_fragments"][0] += injection
            receipt["alloy"] = receipt["header"] + "".join(receipt["top_fragments"])
            with self.assertRaises(p.Rejection):
                p.validate_generation(p.seal_receipt(receipt), source, receipt["json"].encode(), receipt["alloy"].encode())
        original = self.bundles["empty"]
        for field, value in [("source_tree_sha256", None), ("source_tree_sha256", "0" * 64),
                             ("compiler_sources_unchanged", 1), ("stack_lock", {"bytes": 0, "sha256": "0" * 64})]:
            with tempfile.TemporaryDirectory() as temp:
                directory = Path(temp)
                for file in original.iterdir():
                    shutil.copy(file, directory / file.name)
                build = p.loads((directory / "build.json").read_bytes())
                build[field] = value
                data = p.encoded(build)
                (directory / "build.json").write_bytes(data)
                manifest = p.loads((directory / "manifest.json").read_bytes())
                manifest["inputs"]["build.json"] = p.digest(data)
                (directory / "manifest.json").write_bytes(p.encoded(manifest))
                with self.assertRaises(p.Rejection):
                    p.import_bundle(directory)
        with self.assertRaisesRegex(p.Rejection, "candidate_scope"):
            p.check_candidate_bounds(dict(objects=[0, 1], root=0, members=[["root", 0], ["root", 1]], containment=[], references=[]), {"root": 1})

    def test_hash_scalar_types(self):
        original = self.bundles["empty"]
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            for file in original.iterdir():
                shutil.copy(file, directory / file.name)
            manifest = p.loads((directory / "manifest.json").read_bytes())
            # Boolean false compares equal to integer zero in Python, but is
            # not a valid byte count, even when the underlying file is empty.
            (directory / "input.cfr").write_bytes(b"")
            manifest["inputs"]["input.cfr"] = dict(p.digest(b""), bytes=False)
            (directory / "manifest.json").write_bytes(p.encoded(manifest))
            with self.assertRaisesRegex(p.Rejection, "artifact_hash"):
                p.import_bundle(directory)

    def test_capture_malformed_build_has_structured_error(self):
        build = self.directory / "malformed-build.json"
        bounds = self.directory / "bounds.json"
        bounds.write_text('{"root":1}')
        for value in [[], None, {}, {"exporter_binary": []}]:
            build.write_bytes(p.encoded(value))
            result = subprocess.run([sys.executable, str(ROOT / "scripts/verification/capture.py"),
                "capture", str(FIXTURES / "empty.cfr"), str(self.directory / "bad-output"),
                "--exporter", str(self.exporter), "--build", str(build), "--bounds", str(bounds)],
                capture_output=True, timeout=120)
            self.assertEqual(2, result.returncode, result.stderr)
            self.assertEqual("malformed", p.loads(result.stdout)["status"])

    def test_live_bound_combinations(self):
        # Bounded exhaustive receipt checks; this is not a semantic proof or solver search.
        for group in ["0..0", "0..1", "1..1", "2..3", "0..*", "1..*"]:
            for local in ["0..0", "0..1", "1..1", "2..3", "0..*", "1..*", "3..3"]:
                with self.subTest(group=group, local=local):
                    source = self.directory / "bounds.cfr"
                    source.write_text(f"Target 0..*\n{group} box\n  heads ->> Target {local}\n")
                    g = p.loads(subprocess.check_output([str(self.exporter), str(source)], timeout=120))
                    self.assertEqual("captured", g["status"], g)
                    nodes, _, _ = p.validate_generation(p.seal_receipt(g), source.read_bytes(), g["json"].encode(), g["alloy"].encode())
                    self.assertEqual(3, len(nodes))

    def test_bag_heads_are_not_collapsed(self):
        core, _ = p.import_bundle(self.bundles["cycles"])
        # Both cyclic reference classes can be empty, and root identity remains fresh.
        empty = dict(objects=[7], root=7, members=[["root", 7]], containment=[], references=[])
        self.assertEqual("satisfies", self.lean(core, empty)["status"])
        empty["objects"].append(7)
        self.assertEqual("malformed", self.lean(core, empty)["status"])
        # The detailed repeated-target bag/set witnesses also run in Lean tests.

    def test_live_candidate_identity_and_command_boundary(self):
        directory = self.bundles["set_and_bag_references"]
        core, _ = p.import_bundle(directory)
        # Three shared-identity subtype/supertype objects, three distinct set
        # targets, and three bag heads all dereferencing the first target.
        names = {n["name"]: n["uid"] for n in core["declarations"]}
        a, abstract, refs, bags = (names[k] for k in ["a", "A", "setRefToA", "multisetRefToA"])
        candidate = dict(objects=list(range(10)), root=0,
            members=[["root", 0]] + [[uid, obj] for uid, objs in
                [(a, range(1, 4)), (abstract, range(1, 4)), (refs, range(4, 7)), (bags, range(7, 10))] for obj in objs],
            containment=[[uid, [0, obj]] for uid, objs in
                [(a, range(1, 4)), (refs, range(4, 7)), (bags, range(7, 10))] for obj in objs],
            references=[[refs, [obj, obj - 3]] for obj in range(4, 7)] + [[bags, [obj, 1]] for obj in range(7, 10)])
        path = self.directory / "candidate.json"
        command = [sys.executable, str(ROOT / "scripts/verification/capture.py"), "import", str(directory), "--candidate", str(path)]
        def verdict(value):
            path.write_bytes(p.encoded(value))
            result = subprocess.run(command, capture_output=True, timeout=120)
            self.assertEqual(0, result.returncode, result.stderr)
            return p.loads(result.stdout)["status"]
        self.assertEqual("satisfies", verdict(candidate))
        candidate["references"][1][1][1] = 1
        self.assertEqual("violates", verdict(candidate))
        candidate["references"][1][1][1] = 2
        # An uncovered abstract object is a typed semantic violation.
        candidate["objects"].append(10)
        candidate["members"].append([abstract, 10])
        self.assertEqual("violates", verdict(candidate))
        candidate["objects"].remove(10)
        candidate["members"].remove([abstract, 10])
        # A reference endpoint outside its target extent is malformed.
        candidate["members"].remove([abstract, 1])
        self.assertEqual("malformed", verdict(candidate))
        # Duplicate fields are rejected at the supported external command,
        # before Lean's internal canonical-record parser is called.
        path.write_text('{"objects":[],"objects":[],"root":0,"members":[],"containment":[],"references":[]}')
        result = subprocess.run(command, capture_output=True, timeout=120)
        self.assertEqual(2, result.returncode)
        self.assertEqual("duplicate_json_key", p.loads(result.stdout)["code"])


if __name__ == "__main__":
    unittest.main()
