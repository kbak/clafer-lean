# Issue #16 implementation plan

Status: implementation complete; validation evidence and semantic review outcomes
are retained externally. The accepted contracts in [spec.md](spec.md) and the
frozen intent/acceptance remain authoritative. Review baseline:
`030340d9d8700c1d6d722d4f0efc18dc0eb86647`.

## Implemented steps

1. Record the accepted Q8 correction and precise preprint locators in
   `docs/SOURCES.md`. The accepted issue snapshot already records the same decision.
2. Extend the existing span modules with inverse/composition isomorphism transport
   and target-preserving fiber equivalences, preserving their original APIs.
3. Add `DPGraph/Predicates/{Signature,SemanticGraph,Meaning,Interpretation}.lean`
   and the public `DPGraph.Predicates` entrypoint. Use the agreed ambient subsets,
   bounded link universe, bag equivalences and cardinal embedding contracts.
4. Add `DPGraph/Predicates/Examples.lean`, including Q1/Q8 counterexamples, zero
   families, infinite fibers, literal inclusion and generic model restriction.
5. Maintain the living intent/specification, source map, architecture, public scope
   statements and named Markdown trace artifacts. Preserve continuing requirement
   IDs and the frozen task intent/spec/acceptance.
6. Extend only the expected module inventory and independent public API tests.
   Keep scope, dependency/toolchain pins, cache policy and validation gates intact.

No semantic step changed. The small fiber transport addition fits the existing
indexed-family module; no extra graph API or global finiteness assumption is used.

## Handoff gates

Run the supplied IntentBond wrapper against the original review baseline; retain
build, warning, complete module discovery/kernel replay, axiom/layer/public-import
and regression evidence. Verify exported source against that evidence. Exit 4
leaves semantic review pending. Independent review must assess Q8, bag equality,
link multiplicities, inclusion identity and universe bounds before acceptance.
The coordinator retains issue #16 In Progress and handles a draft PR with
`Closes #16` after its gates. Keep changes uncommitted; do not merge, deploy, close
the issue or mark Done before acceptance and merge.
