# Tracing Lean definitions and proofs

The pinned IntentBond/OpenFastTrace combination imports Markdown requirements
and artifacts, but OpenFastTrace 4.9.0 does not import `.lean` source tags.
Do not put OFT coverage annotations directly in Lean files and assume they are
checked. Lean files remain in `scope.json`: their contents are captured, their
modules are built and kernel checked, and their changes require review.

## Lean artifacts

Until native Lean tag support is adopted, declare named implementation and proof
artifacts in Markdown under `docs/`, beside explicit links to the corresponding
Lean file and declaration names. For example, when a real requirement exists:

```markdown
## Representation of model shape
`impl~model-shape-representation~1`

The `ModelShape` declaration in Clafer/Syntax.lean represents the selected
abstract syntax. Link the source file and explain the correspondence here.

Covers:
- `req~model-shape~1`
```

Proof artifacts can use the same structure with type `proof`, naming the actual
theorem and its source. State `Needs: impl, proof` on requirements that require
both, rather than labeling documentation as proof. Use `utest` for actual tests.
Maintain these artifact declarations, source links, theorem statements, and
requirements together. Keep source references precise as declarations move.

These are checked OFT artifacts whose locations are in Markdown. Review must
follow their links into the Lean implementation and proofs. Neither a source
link nor an artifact named `proof` establishes the theorem; Lean checks the
declaration, and review assesses whether its statement matches the requirement
and the cited paper. Command-level evidence records the configured check's
result; it does not associate individual theorem executions with artifacts.

## Scope selection

[CI](../.github/workflows/ci.yml) selects the PR base (or the previous commit for
pushes) and uses its scope. If that base has no scope, the initial-adoption check
uses the candidate as baseline and explicitly leaves adoption to PR review.

With an existing scope, [ci_scope.py](../scripts/ci_scope.py) accepts identical
baseline/candidate bytes, or the exact recognized public-root expansion. For
that expansion it derives `inputs: ["."]` and `review_paths: ["."]` from the
recognized historical baseline, requires the pinned resulting bytes, and retains
the actual Git baseline. These layout-independent paths capture both historical
and sibling-root sources. Specification/test paths, coverage floors,
revision/skipped-test policy, command and timeout remain baseline obligations.
For scope changes, unknown baselines, partial migrations, reversions and unrelated
policy edits are rejected by the selector and exercised in
[regression tests](../tests/test_ci_scope.py).
Candidate policy changes cannot authorize themselves; other changes need separate
review. Local checks against the historical baseline use the independently
approved expanded scope via `--scope`.

CI retains baseline, candidate and selected scope byte identities, canonical
policy identities and the transformation alongside check evidence. Byte hashes
identify exact files; canonical policy hashes identify parsed policy values.
Authorization history belongs in PR context and external factory evidence.
Frozen task snapshots retain historical paths and are not current architecture
or scope-selection guidance.
