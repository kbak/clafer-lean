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
- Resumed from retained implementation HEAD
  `e48ed8bfb84d1db848c1e533d1bac2b712522a5f`, preserving the original review base,
  task branch and frozen scope. Rechecked the accepted intent/spec hashes and
  reviewed the complete change, including actual Lean statements and trace links.
  The factory package's skill differs from the repository pin, so the exact
  pinned skill and relevant reference differences were read from upstream.
  Current validation uses the supplied factory wrapper and its official Mathlib
  cache provisioning; the earlier local cache experiment is not reused.
  Retain fresh check and worktree-verification evidence outside the repository.

## Evidence-retention repair

- Repair starting HEAD: `eb5ab471e896fd7b62ab2b4f6a64d80257aec2e0`; retain
  review base `43d7f3fc326201c68a5da24bdd8aa613794d1d0d`, the accepted package,
  frozen scope and mathematical implementation. The recorded failure rejected
  an extra `impact.json` in an invocation directory; it does not authorize a
  semantic change.
- Revise step 6's evidence handling: create fresh checks only through the supplied
  wrapper. Leave each invocation with its generated `invocation.json`,
  `checker.log` and untouched `evidence/` bundle. Store impact, verification and
  independent-review reports separately, outside invocation directories. Preserve
  historical inputs. Exercise the retention routine on the fresh bundle using a
  separate scratch destination to check the failure directly.
- Finish these documents before validation, rerun the full configured check and
  source verification, and obtain a fresh independent review of the retained
  change. Earlier validation and implementation summaries remain reported work;
  current external evidence supplies the new results. Coordinator publication
  and ticket gates remain as described in step 7.

## Pinned review-guidance repair

- Repair starting HEAD: `0712c088b9726f5b80f4af492f584ea0c3d57868`; retain
  the original review base and accepted contract. The recorded blocker concerns
  unavailable pinned guidance during offline review, not the mathematical code.
- Revise steps 1 and 6 to use the test profile's retained
  `review-context/intentbond-a430efa8d82e2a88ed2607bfe838066bb9d73f3c/`
  source copy. Its skill, relevant references and upstream license are available
  locally. All 168 source files match the supplied provenance's byte counts,
  SHA-256 digests and Git blob identities. Supply that location and verification
  to the independent reviewer; the installed checker remains a separate runtime.
- Preserve the Lean implementation, requirements, scope and accepted package.
  Finish this record before fresh wrapper validation and source verification,
  then obtain a new independent review using the retained guidance. Keep all
  supplemental results outside invocation directories and leave publication
  and ticket updates to the coordinator.

## Current-base repair validation

- Repair starting HEAD: `51534de7c608ab749b929d549a46728f11fffaba`.
  It already incorporates the supplied current review base
  `4c6d03c5022b5f5f762cae4a6459bbe73c76a477`, including the checkout action
  update, with no unresolved conflicts. Use this exact base for fresh feedback
  and verification; the original planning base remains recorded above and in
  the unchanged accepted package.
- Rechecked the retained definitions, laws, positive/negative examples, named
  trace artifacts and validation script against the approved requirements.
  No CI diagnostics were supplied with this repair request, so identify any
  remaining failure through the full configured check before changing code.
- Preserve the existing branch, exact scope bytes, accepted documents, Lean and
  Mathlib pins, and all validation stages. The pinned guidance is available
  locally and its 168 files match the recorded provenance. Finish this record
  before invoking the required feedback wrapper; keep the fresh bundle intact
  and supplemental results outside its invocation directory. Independent
  review and publication remain coordinator gates.
- The first fresh check passed trace coverage but stopped before compilation
  because the release metadata endpoint returned HTTP 403. Provisioned the
  official Lean v4.35.0 archive outside the repository, verified its published
  SHA-256, and registered it with elan under the existing exact toolchain name.
  The profile's normal install command now recognizes that toolchain. Retain
  the failed bundle and rerun the complete check; no check or policy is bypassed.
