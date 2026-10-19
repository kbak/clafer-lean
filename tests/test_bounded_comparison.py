"""Actual paired compiler + Lean + hash-pinned Alloy regression/search/replay.

No missing-tool skips. Raw evidence is always retained outside the checkout.
"""
import copy
import json
from itertools import islice
import os
import shutil
from pathlib import Path
import sys
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT / "scripts/verification"))
import alloy_runtime
import candidates
import comparison as c
from capture import capture
import protocol as p
import relation
from runtime import prepare

FIXTURES=ROOT / "tests/fixtures/comparison"


def candidate(members, containment=(), references=(), garbage=()):
    rows=[["root",0]]+[[u,o] for u,objects in members.items() for o in objects]
    objects=sorted({0,*garbage,*(o for _,o in rows)})
    return dict(objects=objects,root=0,members=rows,containment=list(containment),references=list(references))


class RelationTests(unittest.TestCase):
    def test_interruption_preserves_observed_solver(self):
        runtime=dict(java=Path("java"),classes=Path("classes"),jar=Path("alloy.jar"),identity={})
        for stage,observed,expected in ((None,None,None),("original_parse",None,None),
                ("profile_validation",None,None),("solver",None,"timeout"),("witness","sat","sat")):
            with tempfile.TemporaryDirectory() as temporary:
                directory=Path(temporary)
                if stage:(directory/"execution.json").write_bytes(p.encoded(dict(stage=stage,outcome=observed)))
                with patch.object(subprocess,"run",side_effect=subprocess.TimeoutExpired("injected",1)):
                    result=alloy_runtime.solve(runtime,directory,{})
                self.assertEqual(expected,result["outcome"])
                self.assertEqual("timeout",result["status"])

    def test_malformed_backend_is_execution_failure(self):
        runtime=dict(java=Path("java"),classes=Path("classes"),jar=Path("alloy.jar"),identity={})
        for raw in (b'{broken',b'{"schema":"unknown"}',b'null'):
            with tempfile.TemporaryDirectory() as temporary:
                directory=Path(temporary)
                (directory/"solver.json").write_bytes(raw)
                with patch.object(subprocess,"run",return_value=subprocess.CompletedProcess([],0)):
                    result=alloy_runtime.solve(runtime,directory,{})
                self.assertIsNone(result["outcome"])
                self.assertEqual("error",result["status"])

    def test_outcome_algebra_and_boundaries(self):
        self.assertEqual("alloy_accepts_lean_rejects",c.category("violates","sat",True))
        self.assertEqual("lean_accepts_alloy_rejects",c.category("satisfies","unsat",None))
        self.assertEqual("pin_decode_failure",c.category("satisfies","sat",False))
        for state in ("unknown","timeout","resource_limit","error",None):
            self.assertEqual("inconclusive",c.category("violates",state,None))
        with self.assertRaisesRegex(p.Rejection,"arithmetic_range"):
            relation.range_argument("#a <= 8",{"root":1,"a":1},4)
        self.assertEqual(8,relation.range_argument("#a <= 8",{"root":1,"a":1},5)["maximum"])
        with self.assertRaisesRegex(p.Rejection,"bitwidth_profile"):
            relation.range_argument("",{"root":1},32)

    def test_search_counts_interruption_and_seed(self):
        core={"declarations":[dict(uid="x",parent="root",target=None)]};bounds={"root":1,"x":1}
        all_candidates=list(candidates.domain(core,bounds))
        self.assertEqual(4,len(all_candidates)) # empty; unused; member/no link; member/link
        for value in all_candidates: relation.validate_candidate(value,core,bounds)
        def ok(value,index):return dict(admission="admitted",complete=True,category="agree_violates")
        report=candidates.batch(all_candidates,ok,mode="exhaustive",expected=4)
        self.assertTrue(report["complete_domain"])
        report=candidates.batch(all_candidates,ok,mode="exhaustive",limit=2)
        self.assertFalse(report["complete_domain"]);self.assertEqual(2,report["completed"])
        def interrupted(value,index):raise KeyboardInterrupt
        self.assertEqual("interrupted",candidates.batch(all_candidates,interrupted,mode="exhaustive")["termination"])
        a=list(candidates.generated(core,bounds,52,20));b=list(candidates.generated(core,bounds,52,20))
        self.assertEqual(a,b)
        for value in a: relation.validate_candidate(value,core,bounds)
        abstract={"declarations":[dict(uid="Base",parent="clafer",target=None)]}
        for value in list(candidates.domain(abstract,{"root":1,"Base":1}))+list(candidates.generated(abstract,{"root":1,"Base":1},52,10)):
            relation.validate_candidate(value,abstract,{"root":1,"Base":1})
            self.assertEqual([],value["containment"])


class LiveComparisonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.exporter,cls.build=prepare()
        cls.runtime=alloy_runtime.prepare()
        evidence=Path(os.environ.get("CLAFER_COMPARISON_EVIDENCE",tempfile.gettempdir())).resolve()
        if evidence.is_relative_to(ROOT):raise RuntimeError("comparison evidence must be external")
        evidence.mkdir(parents=True,exist_ok=True)
        cls.evidence=Path(tempfile.mkdtemp(prefix="clafer-comparison-",dir=evidence))
        print(f"Bounded comparison evidence: {cls.evidence}",flush=True)
        cls.bundles={};cls.cores={};cls.metadata={};cls.serial=0
        maps={
          "bag":{"c0_Target":2,"c0_refs":3},"set":{"c0_Target":2,"c0_refs":3},
          "optional":{"c0_x":2},"overlap":{"c0_x":1,"c0_y":1},
          "nesting":{"c0_box":2,"c0_child":2},
          "inheritance":{"c0_Base":3,"c0_Middle":2,"c0_Unused":1,"c0_left":2,"c0_right":2},
          "bounds":{"c0_box":1,"c0_zero":0,"c0_optional":1,"c0_exact":2,"c0_bounded":3,"c0_unbounded":3},
          "groups":{"c0_Target":1,"c0_box":1,"c0_refs":4},
          "cycles":{"c0_a":2,"c0_child":1,"c0_b":2}}
        maps.update(parent_set={"c0_Target":1,"c0_box":2,"c0_refs":2},
            nested_inheritance={"c0_Base":1,"c0_box":1,"c0_child":1},
            abstract_bounds={"c0_Base":1,"c0_left":1,"c0_right":1},one={"c0_x":0},
            some={"c0_x":0},
            eight={"c0_x":8},keywords={**{f"c{i}_"+name:1 for i in range(4) for name in ("first","second")},
                **{"c0_"+name:1 for name in ("exclusive","inclusive","atMostOne","optionalGroup")}},
            identities={"c0_Base":2,"c0_Unused":0,"c0_left":1,"c0_right":1,"c0_same":2,"c1_same":2,"c0_links":2},
            spellings={"c0_box":2,"c0_links'":2,"c0_same'":2,"c0_Élément":2})
        for name,bounds in maps.items():
            path=cls.evidence / ("capture-"+name)
            fixture=(ROOT/"tests/fixtures/importer"/(name+".cfr")) if name in ("identities","spellings") else FIXTURES/(name+".cfr")
            core,meta=capture(fixture,cls.exporter,cls.build,dict(root=1,**bounds),path)
            cls.bundles[name]=path;cls.cores[name]=core;cls.metadata[name]=meta
        # Reuse the same generated pair with a second explicit manual vector.
        path=cls.evidence/"capture-bag-small";shutil.copytree(cls.bundles["bag"],path)
        manifest=p.loads((path/"manifest.json").read_bytes());manifest["bounds"]={"root":1,"c0_Target":1,"c0_refs":1}
        (path/"manifest.json").write_bytes(p.encoded(manifest))
        cls.cores["bag-small"],cls.metadata["bag-small"]=p.import_bundle(path);cls.bundles["bag-small"]=path

    def run_case(self,name,value,expected=None,**options):
        type(self).serial+=1
        output=self.evidence/f"case-{self.serial:05d}-{name}"
        r=c.compare(self.bundles[name],value,output,runtime=self.runtime,bitwidth=options.pop("bitwidth",8),
                    overall=options.pop("overall",10),**options)
        if expected:self.assertEqual(expected,r["category"],(output,r))
        return r,output

    def repeat(self,count=3):
        heads=list(range(2,2+count))
        return candidate({"c0_Target":[1],"c0_refs":heads},
            [["c0_Target",[0,1]]]+[["c0_refs",[0,h]] for h in heads],[["c0_refs",[h,1]] for h in heads])

    def test_01_repeated_targets_and_replay(self):
        for count in (0,1,3):
            value=self.repeat(count)
            r,path=self.run_case("bag",value,"agree_satisfies")
            self.assertEqual(count,len(p.loads((path/"command.json").read_bytes())["derived_occurrences"]))
            _,set_path=self.run_case("set",value,"agree_violates" if count>1 else "agree_satisfies")
            if count>1:self.assertIn("keys",p.loads((set_path/"lean.json").read_bytes())["failed_predicates"])
        replayed=c.replay(path,self.evidence/"first-replay",runtime=self.runtime)
        self.assertEqual(r["category"],replayed["category"])
        renamed=relation.rename(self.repeat(),{0:99,1:7,2:18,3:20,4:50})
        self.run_case("bag",renamed,"agree_satisfies")

    def test_02_nesting_groups_and_effective_bounds(self):
        nested=candidate({"c0_box":[1],"c0_child":[2]},[["c0_box",[0,1]],["c0_child",[1,2]]])
        self.run_case("nesting",nested,"agree_satisfies")
        bad=copy.deepcopy(nested);bad["containment"].pop();self.run_case("nesting",bad,"agree_violates")
        for count in (1,2,3,4):
            heads=list(range(3,3+count))
            value=candidate({"c0_Target":[1],"c0_box":[2],"c0_refs":heads},
                [["c0_Target",[0,1]],["c0_box",[0,2]]]+[["c0_refs",[2,h]] for h in heads],
                [["c0_refs",[h,1]] for h in heads])
            self.run_case("groups",value,"agree_satisfies" if count in (2,3) else "agree_violates")
        members={"c0_box":[1],"c0_exact":[2,3],"c0_bounded":[4,5],"c0_unbounded":[6,7]}
        links=[["c0_box",[0,1]]]+[[u,[1,o]] for u,os_ in members.items() if u!="c0_box" for o in os_]
        good=candidate(members,links);self.run_case("bounds",good,"agree_satisfies")
        bad=copy.deepcopy(good);bad["containment"].remove(["c0_exact",[1,3]])
        self.run_case("bounds",bad,"agree_violates")
        self.run_case("bounds",candidate({}),"agree_satisfies")

    def test_03_inheritance_overlap_and_root_negatives(self):
        good=candidate({"c0_Base":[1,2],"c0_Middle":[1],"c0_left":[1],"c0_right":[2]},
                       [["c0_left",[0,1]],["c0_right",[0,2]]])
        self.run_case("inheritance",good,"agree_satisfies")
        for members in ({"c0_Base":[1]}, {"c0_Unused":[1]},
                        {"c0_Base":[1],"c0_Middle":[1],"c0_left":[1],"c0_right":[1]}):
            links=[[u,[0,o]] for u,os_ in members.items() if u in ("c0_left","c0_right") for o in os_]
            self.run_case("inheritance",candidate(members,links),"agree_violates")
        overlap=candidate({"c0_x":[1],"c0_y":[1]},[["c0_x",[0,1]],["c0_y",[0,1]]])
        self.assertEqual(overlap,p.loads((FIXTURES/"unrelated-overlap.json").read_bytes()))
        self.run_case("overlap",overlap,"lean_accepts_alloy_rejects")
        value=candidate({"c0_x":[1]},[["c0_x",[0,1]]])
        for mutate in (lambda x:x["objects"].append(2),
                       lambda x:x["containment"].clear(),lambda x:x["members"].append(["c0_x",0])):
            bad=copy.deepcopy(value);mutate(bad);self.run_case("optional",bad,"agree_violates")
        too_many=candidate({"c0_x":[1,2]},[["c0_x",[0,1]],["c0_x",[0,2]]])
        self.run_case("optional",too_many,"agree_violates")
        bad=copy.deepcopy(value);bad["members"].append(["root",1])
        r,_=self.run_case("optional",bad,"unsupported");self.assertEqual("violates",r["lean"])
        self.run_case("optional",dict(value,members=[],containment=[]),"agree_violates")
        nested=candidate({"c0_Base":[2],"c0_box":[1],"c0_child":[2]},[["c0_box",[0,1]],["c0_child",[1,2]]])
        self.run_case("nested_inheritance",nested,"agree_satisfies")

    def test_04_cycles_nonfunctional_and_malformed(self):
        value=candidate({"c0_a":[1],"c0_b":[2],"c0_child":[3]},
                        [["c0_a",[0,1]],["c0_b",[0,2]],["c0_child",[1,3]]],
                        [["c0_a",[1,2]],["c0_b",[2,1]]])
        self.run_case("cycles",value,"agree_satisfies")
        bad=copy.deepcopy(value);bad["references"].pop();self.run_case("cycles",bad,"agree_violates")
        multi=candidate({"c0_Target":[1,2],"c0_refs":[3]},
            [["c0_Target",[0,1]],["c0_Target",[0,2]],["c0_refs",[0,3]]],[["c0_refs",[3,1]],["c0_refs",[3,2]]])
        self.run_case("bag",multi,"agree_violates")
        for mutate in (lambda x:x["objects"].append(0),lambda x:x["members"].append(["missing",1]),
                       lambda x:x["references"].append(["c0_a",[1,99]]),
                       lambda x:x["references"].append(["c0_a",[1,3]])):
            bad=copy.deepcopy(value);mutate(bad);r,_=self.run_case("cycles",bad,"malformed")
            self.assertIsNone(r["solver"])
        self.run_case("bag",None,"malformed")

    def test_05_unpinned_witnesses(self):
        for name in ("bag","set","groups","inheritance","cycles","identities"):
            r,_=self.run_case(name,None,unpinned=True)
            self.assertEqual("agree_satisfies",r["category"],r)
            self.assertTrue(r["faithful"])
        r,_=self.run_case("one",None,"witness_unsat",unpinned=True)
        self.assertIn(dict(stage="lean",reason="no SAT witness exists to decode/check"),r["not_run"])
        self.run_case("one",candidate({}),"agree_violates")
        self.run_case("some",None,"witness_unsat",unpinned=True)
        self.run_case("some",candidate({}),"agree_violates")
        self.run_case("abstract_bounds",None,"witness_unsat",unpinned=True)

    def test_06_exhaustive_and_seeded_tables(self):
        # Exactly this fixed fresh-root domain, without isomorphism reduction.
        # Bounds 1/1 give 35 labelled candidates, including unused objects,
        # unrelated overlap and missing typed root-containment links.
        for name,count in (("overlap",35),("bag-small",55)):
            core=self.cores[name];bounds=self.metadata[name]["bounds"]
            values=list(candidates.domain(core,bounds));self.assertEqual(count,len(values))
            report=candidates.batch(values,lambda value,i:self.run_case(name,value,search=dict(mode="exhaustive",index=i,domain="fresh-root-all-tables/v1"))[0],
                                    mode="exhaustive",expected=count)
            (self.evidence/(name+"-exhaustive.json")).write_bytes(p.encoded(report))
            self.assertTrue(report["complete_domain"],report)
            self.assertGreater(report["categories"].get("lean_accepts_alloy_rejects",0),0)
        for name in ("bag","nesting","inheritance"):
            core=self.cores[name];bounds=self.metadata[name]["bounds"]
            stream=candidates.generated(core,bounds,52,6)
            report=candidates.batch(stream,lambda value,i:self.run_case(name,value,search=dict(mode="seeded",seed=52,index=i,count=6))[0],mode="seeded",seed=52,expected=6)
            (self.evidence/(name+"-seeded.json")).write_bytes(p.encoded(report))
            self.assertEqual(6,report["completed"],report);self.assertFalse(report["complete_domain"])

    def test_07_mutations_shrink_and_deterministic_replay(self):
        cases=[("set","omit_set_uniqueness",self.repeat(),"alloy_accepts_lean_rejects"),
               ("bag","collapse_bag_heads",self.repeat(),"pin_decode_failure"),
               ("optional","drop_cardinality",candidate({"c0_x":[1,2]},[["c0_x",[0,1]],["c0_x",[0,2]]]),"alloy_accepts_lean_rejects")]
        for name,mutation,value,expected in cases:
            self.run_case(name,value,expected,mutation=mutation)
            def preserves(smaller):
                result=self.run_case(name,smaller,mutation=mutation)[0]
                self.assertIn(result["category"],c.CATEGORIES|{expected},result)
                return result["category"]==expected
            minimal,attempts=candidates.shrink(value,self.cores[name],self.metadata[name]["bounds"],
                preserves)
            r,path=self.run_case(name,minimal,expected,mutation=mutation)
            (self.evidence/(mutation+"-minimum.json")).write_bytes(p.encoded(dict(candidate=minimal,attempts=attempts,
                minimality="single object/row deletion fixed point",replay=str(path))))
            self.assertEqual(4 if name in ("set","bag") else 3,len(minimal["objects"]))
            self.assertEqual(relation.canonical(p.loads((FIXTURES/(mutation+".json")).read_bytes())),minimal)
            self.assertEqual(expected,c.replay(path,self.evidence/(mutation+"-replay"),runtime=self.runtime)["category"])

    def test_08_tampering_arithmetic_errors_and_unknown(self):
        self.run_case("bag",self.repeat(),"unsupported",bitwidth=4)
        eight=candidate({"c0_x":list(range(1,9))},[["c0_x",[0,h]] for h in range(1,9)])
        self.run_case("eight",eight,"agree_satisfies",bitwidth=8)
        self.run_case("eight",eight,"unsupported",bitwidth=4)
        self.run_case("keywords",None,"agree_satisfies",bitwidth=10,unpinned=True)
        with patch.object(alloy_runtime,"solve",return_value=dict(outcome="unknown",detail="injected unknown")):
            r,_=self.run_case("bag",self.repeat(),"inconclusive");self.assertFalse(r["complete"])
        with patch.object(alloy_runtime,"solve",return_value=dict(outcome="timeout",detail="injected timeout")):
            self.run_case("bag",self.repeat(),"inconclusive")
        real_command=c.command
        value=candidate({"c0_Target":[1,2],"c0_refs":[3,4,5]},
            [["c0_Target",[0,1]],["c0_Target",[0,2]]]+[["c0_refs",[0,h]] for h in (3,4,5)],
            [["c0_refs",[h,1]] for h in (3,4,5)])
        def wrong_relation(original,pin_text,*args,**kwargs):
            self.assertIn("ib_obj_2->ib_obj_0",pin_text)
            return real_command(original,pin_text.replace("ib_obj_2->ib_obj_0","ib_obj_2->ib_obj_1",1),*args,**kwargs)
        with patch.object(c,"command",side_effect=wrong_relation):
            self.run_case("bag",value,"pin_decode_failure")
        def auxiliary(original,pin_text,*args,**kwargs):
            model,command=real_command(original,pin_text,*args,**kwargs)
            return model+"sig unexpectedAuxiliary {}\n",command
        with patch.object(c,"command",side_effect=auxiliary):
            r,_=self.run_case("bag",self.repeat(),"unsupported");self.assertIsNone(r["solver"])
        def unknown_skolem(original,pin_text,*args,**kwargs):
            return real_command(original,pin_text.replace("ib_obj_","unexpected_obj_"),*args,**kwargs)
        with patch.object(c,"command",side_effect=unknown_skolem):
            r,_=self.run_case("bag",self.repeat(),"unsupported")
            self.assertEqual("sat",r["solver"])
            self.assertEqual("witness",r["diagnostics"][0]["stage"])
        r,path=self.run_case("bag",self.repeat(),"agree_satisfies")
        tampered=self.evidence/"tampered-replay-input";shutil.copytree(path,tampered);path=tampered
        manifest=p.loads((path/"manifest.json").read_bytes())
        manifest["inputs"].pop("candidate.json")
        (path/"manifest.json").write_bytes(p.encoded(manifest))
        with self.assertRaisesRegex(p.Rejection,"replay_input_inventory"):
            c.replay(path,self.evidence/"bad-replay",runtime=self.runtime)

    def test_10_original_parser_failure_retains_stage(self):
        # S admits this existing spelling fixture. The pinned compiler emits an
        # apostrophe UID rejected by the actual Alloy parser: no semantic verdict.
        r,path=self.run_case("spellings",None,"inconclusive",unpinned=True)
        self.assertEqual("admitted",r["admission"])
        self.assertIsNone(r["solver"]);self.assertIsNone(r["lean"])
        self.assertFalse(r["complete"])
        self.assertEqual("original_parse",r["diagnostics"][0]["stage"])
        self.assertEqual("error",r["diagnostics"][0]["status"])
        replayed=c.replay(path,self.evidence/"spellings-parser-replay",runtime=self.runtime)
        self.assertEqual("inconclusive",replayed["category"])
        self.assertEqual("original_parse",replayed["diagnostics"][0]["stage"])

    def test_11_raw_candidate_bytes_and_malformed_replay(self):
        raw=("\n  "+json.dumps(self.repeat(1),indent=3)+" \n").encode()
        r,path=self.run_case("bag",None,"agree_satisfies",candidate_bytes=raw)
        self.assertEqual(raw,(path/"candidate.json").read_bytes())
        self.assertEqual(p.digest(raw),p.loads((path/"manifest.json").read_bytes())["inputs"]["candidate.json"])
        replay_path=self.evidence/"raw-candidate-replay"
        self.assertEqual("agree_satisfies",c.replay(path,replay_path,runtime=self.runtime)["category"])
        self.assertEqual(raw,(replay_path/"candidate.json").read_bytes())
        for i,broken in enumerate((b'{"objects":[],"objects":[]}',b'{broken',b'\xff')):
            r,path=self.run_case("bag",None,"malformed",candidate_bytes=broken)
            self.assertIsNone(r["lean"]);self.assertIsNone(r["solver"])
            self.assertEqual(broken,(path/"candidate.json").read_bytes())
            replay_path=self.evidence/f"malformed-candidate-replay-{i}"
            self.assertEqual("malformed",c.replay(path,replay_path,runtime=self.runtime)["category"])
            self.assertEqual(broken,(replay_path/"candidate.json").read_bytes())

    def test_09_per_parent_keys_and_two_parents(self):
        value=candidate({"c0_Target":[1],"c0_box":[2,3],"c0_refs":[4,5]},
            [["c0_Target",[0,1]],["c0_box",[0,2]],["c0_box",[0,3]],["c0_refs",[2,4]],["c0_refs",[3,5]]],
            [["c0_refs",[4,1]],["c0_refs",[5,1]]])
        self.run_case("parent_set",value,"agree_satisfies")
        bad=copy.deepcopy(value);bad["containment"][-1]=["c0_refs",[2,5]]
        self.run_case("parent_set",bad,"agree_violates")
        both=candidate({"c0_box":[1,2],"c0_child":[3]},
            [["c0_box",[0,1]],["c0_box",[0,2]],["c0_child",[1,3]],["c0_child",[2,3]]])
        self.run_case("nesting",both,"agree_violates")


if __name__=="__main__":unittest.main()
