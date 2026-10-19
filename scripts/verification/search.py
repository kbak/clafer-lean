#!/usr/bin/env python3
"""Replayable labelled-table enumeration or seeded sampling (no LLM required)."""
import argparse
from pathlib import Path
import sys

from alloy_runtime import prepare
from candidates import batch, domain, generated
from comparison import compare, CATEGORIES, ROOT
from protocol import encoded, import_bundle, unsupported


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("bundle",type=Path);p.add_argument("output",type=Path)
    p.add_argument("--mode",choices=("exhaustive","seeded"),required=True)
    p.add_argument("--bitwidth",type=int,required=True);p.add_argument("--overall",type=int,required=True)
    p.add_argument("--seed",type=int);p.add_argument("--count",type=int);p.add_argument("--limit",type=int)
    args=p.parse_args()
    if args.output.resolve().is_relative_to(ROOT):unsupported("evidence_in_repository")
    if args.mode=="seeded" and (args.seed is None or args.count is None or args.count<0):
        p.error("seeded mode requires --seed and nonnegative --count")
    if args.limit is not None and args.limit<0:p.error("limit must be nonnegative")
    core,metadata=import_bundle(args.bundle);runtime=prepare()
    args.output.mkdir(parents=True,exist_ok=False)
    stream=domain(core,metadata["bounds"]) if args.mode=="exhaustive" else generated(core,metadata["bounds"],args.seed,args.count)
    spec=dict(mode=args.mode,domain="fresh-root-all-tables/v1",bounds=metadata["bounds"],seed=args.seed,count=args.count,
              symmetry_reduction=False,distribution="labelled exhaustive" if args.mode=="exhaustive" else "MT19937 sizes/subsets/fair tuple bits")
    (args.output/"search.json").write_bytes(encoded(spec))
    report=batch(stream,lambda value,i:compare(args.bundle,value,args.output/f"case-{i:08d}",
        bitwidth=args.bitwidth,overall=args.overall,runtime=runtime,search=dict(spec,index=i)),
        mode=args.mode,expected=args.count if args.mode=="seeded" else None,seed=args.seed,limit=args.limit)
    (args.output/"result.json").write_bytes(encoded(report))
    print(encoded(report).decode(),end="")
    return 0 if report["exhausted"] and report["requested"]==report["completed"] and not any(
        k not in ("agree_satisfies","agree_violates") for k in report["categories"]) else 1


if __name__=="__main__":sys.exit(main())
