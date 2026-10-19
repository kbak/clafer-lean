"""Explicit injected defects for sensitivity experiments, never compiler claims."""
import copy

from protocol import unsupported
from relation import canonical

NAMES = {"omit_set_uniqueness", "collapse_bag_heads", "drop_cardinality"}


def inject(name, original, candidate, core, metadata):
    if name not in NAMES: unsupported("unknown_injected_mutation")
    if name == "omit_set_uniqueness":
        clauses = [s for o in metadata["observations"].values() for s in o["set_uniqueness"]]
        if len(clauses) != 1 or original.count(clauses[0]) != 1:
            unsupported("mutation_precondition", name)
        return original.replace(clauses[0], "no none", 1), candidate
    if name == "drop_cardinality":
        # A selected top-level optional declaration, identified by receipt.
        nodes = [n for n in core["declarations"] if n["parent"] == "root" and n["card"] == [0,1]]
        if len(nodes) != 1: unsupported("mutation_precondition", name)
        uid = nodes[0]["uid"]
        text = "lone sig " + metadata["observations"][uid]["signature"]
        if original.count(text) != 1: unsupported("mutation_precondition", name)
        return original.replace(text, text.removeprefix("lone "), 1), candidate
    bag_uids = {n["uid"] for n in core["declarations"] if n["mode"] == "bag"}
    groups = {}
    for uid, (p, h) in candidate["containment"]:
        if uid not in bag_uids: continue
        targets = [t for u,(head,t) in candidate["references"] if u==uid and head==h]
        if len(targets)==1: groups.setdefault((uid,p,targets[0]),[]).append(h)
    removed = {h for heads in groups.values() for h in sorted(set(heads))[1:]}
    c = copy.deepcopy(candidate)
    # This deliberate faulty representation drops occurrence identities. The
    # unchanged checker input and witness-isomorphism gate must expose it.
    c["objects"]=[o for o in c["objects"] if o not in removed]
    c["members"]=[row for row in c["members"] if row[1] not in removed]
    for table in ("containment","references"):
        c[table]=[row for row in c[table] if not removed.intersection(row[1])]
    return original, canonical(c)
