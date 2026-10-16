# Implementation plan for #14

## Order and files

1. Recheck the captured baseline and selected requirements. Read the repository's required pinned guidance. Confirm the Mathlib commit and Lean compatibility before dependency resolution.
2. Add Mathlib in lakefile.toml and retain the resolved lake-manifest.json. Preserve default target behavior and warnings-as-errors. Use the normal cache/provisioning mechanism; do not bypass tests on a timeout or download failure.
3. Implement targeted modules under ClaferLean/DPGraph/: Signature.lean, Formula.lean, Basic.lean, Morphism.lean, and Examples.lean. The representation bridge is documented beside Signature and in ARCHITECTURE.md; no separate Graph API/file is needed. Add ClaferLean/DPGraph.lean as an independent entrypoint and import it from ClaferLean.lean so the existing leanchecker invocation sees the new library. Adapt filenames if a smaller natural grouping is clearer.
4. Prove laws incrementally and construct the noninjective example, composition example, isolated-node arity and failed-preservation example. Avoid vacuous formula sets as the sole demonstration. The fixed-signature Mathlib Category instance and abstract satisfaction remain the next issue (#15), unless a minimal instance naturally falls out without scope growth.
5. Update docs/intent.md, docs/spec.md and the brief README status as needed. Add concise docs/SOURCES.md and docs/ARCHITECTURE.md, using the source/decision facts below; add named Lean implementation/proof artifacts in a focused docs file or alongside the source map, following docs/traceability.md. Keep later work linked to issues rather than duplicating the entire backlog.
6. Inspect the complete change and the axioms of the public theorems. Run ib check against the supplied original baseline; this runs scripts/check.sh including Lake, leanchecker and the existing Python tests. Preserve evidence and run ib verify against the completed worktree; the parent repeats verification against the exported commit. Exit 4 retains review pending. Run the configured independent review and repair bounded findings. A validation failure remains a failure.
7. Produce handoff.md with source links, requirement changes, validation limits, Closes #14 and coordinator ticket updates. Per factory-implementation, leave changes uncommitted; the parent runs independent review and handles the draft PR after the gates pass. No GitHub credential access in the worker.

## Source/design facts to retain

The authority for this increment is SoSyM B.4 Definitions 6–10. The paper defines signature symbols with graph arities, formulas as a predicate plus an arity-to-carrier graph map, declarations as a set, and DP morphisms by declared-formula preservation. This does not require signature dependencies or closure. Diskin & Wolter (2008), DOI 10.1016/j.entcs.2008.10.041, §4.1 Definitions 4.1–4.5 adds dependency arrows and closure: document that difference instead of importing it accidentally. The author-uploaded full text was inspected for this comparison.

Mathlib pinned sources:
- https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean
- https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Prefunctor.lean
- https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/CategoryTheory/Category/Quiv.lean

Prefunctor supplies id, comp, id_comp, comp_id, comp_assoc and extensionality. Quiv bundles graph values. Reuse them. Quiver arrows are Type-valued, not propositions, so parallel arrows remain distinct. Explain total edges via Sigma endpoints without developing a second competing graph API. Using finite Set/Finset presentations and computable transformations is later work; avoid forcing decidable equality onto the arbitrary core.

FormalCD and Clafer remain future independent upper layers. FormalCD will add vocabulary and reviewed naming/structural invariants; the self-description target is a well-formed value representing Figure 21c. Clafer will use resolved syntax, Shapes/MCS and eventually Compile/gluing, with name resolution and constraint meaning made explicit. These are roadmap direction, not definitions or theorems to implement now.

## Risks and checks

- Dependent morphism/formula extensionality and universe inference: use explicit universe bounds and existing extensionality lemmas; do not collapse all types to Type 0 to make examples compile.
- Mathlib build footprint: verify the compatible pin and normal cache support. Preserve leanchecker and factory timeouts; report infrastructure limitations instead of silently reducing verification.
- Noninjectivity: graph maps may merge arrows; no injectivity assumption belongs in the generic morphism.
- Syntax vs meaning: proofs of declaration preservation must not be described as interpretation or semantic-equivalence proofs.
- Source ambiguities: preserve the listed open questions; they do not affect B.4. A newly found ambiguity affecting this slice requires a concrete maintainer decision, not an invented semantics.
- Traceability: named Markdown proof artifacts link checked Lean declarations. Coverage is not evidence that the theorem formalizes the right claim; independent review checks correspondence.


## Implementation record

- Review base: `43d7f3fc326201c68a5da24bdd8aa613794d1d0d`; starting worktree HEAD:
  `eff3fc5f7fb19879a1a06943e74c7357b2c1d40e`. The existing factory task branch
  and accepted intent/spec/accepted.json are retained. Scope bytes match the
  supplied SHA-256 `4a706e10262528a94a097a84dd8813c0dd9265eaa1f87c55cb77d01ab928ce7f`.
- Read the pinned IntentBond skill and relevant references from its exact source
  revision; use the factory-provided check wrapper for retained feedback bundles.
- Mathlib's release tag resolves to the accepted commit and matches Lean v4.35.0.
  The manifest pins all transitive dependencies. Normal elan provisioning hit a
  release metadata network restriction; the same official Lean release archive
  was installed after checking its GitHub-published SHA-256. Mathlib cache access
  is blocked by network policy, so dependencies were built from source and packed
  using Mathlib's normal local cache command. Cold source compilation approached
  the configured check budget; the shared check now attempts the targeted cache
  before building, with source compilation as fallback. Kernel checking still
  runs in full and no timeout or coverage policy is changed.
- The modules use Lean 4.35 public/exposed declarations, matching Mathlib's module system without disabling warnings. Core and finite witnesses follow B.4 Definitions 6–10. No Category instance or
  predicate semantics is added. The implementation uses five focused modules;
  this grouping avoids an unnecessary wrapper around Mathlib graphs.
- Add a declaration/axiom audit to the shared check, retaining the existing
  build, warnings-as-errors, leanchecker and Python tests. It checks all project
  declarations, including generated ones, and reports standard logical axioms
  separately from new assumptions.
- GitHub issue listing failed with HTTP 401. The worker has no coordinator
  credential access; proposed status/comments are retained in handoff.md.
  Existing #14 is the implementation ticket; no duplicate issue is proposed.
- Local compilation and leanchecker pass for the independent core and examples. The axiom audit
  checks 161 project declarations, including private/generated declarations, and
  reports only propext, Classical.choice and Quot.sound; no new assumptions.
- Full captured validation and source verification must follow the completed
  candidate. Independent review and publication remain parent workflow gates.
  These workflow adjustments do not change the approved mathematical scope.
