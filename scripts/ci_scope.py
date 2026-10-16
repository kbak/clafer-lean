#!/usr/bin/env python3
"""Select baseline policy, allowing only the reviewed public-root expansion.

The baseline is never changed. Both byte identities are pinned to the approved
migration; every other field is derived from the original baseline. Candidate
policy is compared, never used to construct trusted policy.
"""

import argparse
import hashlib
import json
from pathlib import Path


ORIGINAL_SHA256 = "4a706e10262528a94a097a84dd8813c0dd9265eaa1f87c55cb77d01ab928ce7f"
MIGRATED_SHA256 = "76540699cdf6a6a3e57f7077b82d445cad0d325890b5f99bfa54de7a300ad6f5"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(data):
    return digest(json.dumps(json.loads(data), sort_keys=True, separators=(",", ":"),
                             ensure_ascii=True).encode())


def select_scope(baseline, candidate):
    if candidate == baseline:
        return baseline
    if digest(baseline) != ORIGINAL_SHA256:
        raise ValueError("unapproved scope change: baseline is not the approved migration source")
    policy = json.loads(baseline)
    policy["inputs"] = ["."]
    policy["review_paths"] = ["."]
    migrated = (json.dumps(policy, indent=2) + "\n").encode()
    if digest(migrated) != MIGRATED_SHA256 or candidate != migrated:
        raise ValueError("unapproved scope change: only the exact public-root expansion is permitted")
    return migrated


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path, required=True)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--record", type=Path, required=True)
    args = parser.parse_args()
    baseline, candidate = args.baseline.read_bytes(), args.candidate.read_bytes()
    selected = select_scope(baseline, candidate)
    args.output.write_bytes(selected)
    record = {
        "migration": "public-roots" if selected != baseline else None,
        "baseline_scope_sha256": digest(baseline),
        "candidate_scope_sha256": digest(candidate),
        "selected_scope_sha256": digest(selected),
        "baseline_canonical_policy_sha256": canonical(baseline),
        "selected_canonical_policy_sha256": canonical(selected),
        "changed_fields": ["inputs", "review_paths"] if selected != baseline else [],
    }
    args.record.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps(record, sort_keys=True))


if __name__ == "__main__":
    main()
