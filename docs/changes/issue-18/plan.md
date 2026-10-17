# Issue #18 plan

Base: `5e4f13c8e1ba58e0b0c744c1aa0397909e20f79e`. Use the actual factory worktree at this base; the coordinator catalog is older. Accepted task: complete #18 with the explicit #19/universe boundary in spec.md. Read the canonical product intent and affected living requirements, then the retained source inputs.

1. Confirm the source inventory against Figure 21c and §6.1.3/B.4 Definition 8. Record all 11 nodes, 13 arrows, constraints/defaults, the full-binding versus bag projection distinction, and the total-args/zero-arrow boundary in docs/SOURCES.md. Keep unresolved universal representation claims for #19.
2. Add the minimal compatible signature extension in FormalCD (proposed FormalCD/Signature.lean plus adaptations to Basic/Morphism/Semantics). Preserve the built-in specialization and old examples. Reuse DPGraph graph/formula APIs and prove the symbol/arity embedding and translation compatibility.
3. Add metamodel inventory/definitions under FormalCD/Metamodel/ (suggested Basic.lean). Construct the typed carrier, metadata and effective declarations, with all displayed modes and default facts. No Clafer dependency.
4. Implement explicit discipline meanings and full graph-formula identity/correspondence under FormalCD/Metamodel/ (suggested Discipline.lean, Interpretation.lean). Make representation context and universe bounds visible. Retain literal generic bag-key meaning separately from full-binding equality.
5. Add positive/negative and projection-loss witnesses (suggested FormalCD/Metamodel/Examples.lean). Preserve nonempty, repeated-argument, isolated-vertex, ordering, empty-arity and invalid-data cases. Strengthen tests/formalcd_imports.lean for supported specialization and universe signatures; extend the exact inventory in tests/test_project_modules.py without weakening rejection assertions.
6. Export the intended public API from FormalCD.lean while keeping acceptance examples separate. Update docs/spec.md and docs/formalcd-trace.md together with actual declarations; update concise current docs/intent.md, docs/ARCHITECTURE.md, docs/SOURCES.md, README/AGENTS/CONTRIBUTING only as affected. Add minimal DPGraph generic helpers only if necessary for the embedding/correspondence; preserve all existing meanings and boundaries.
7. Run the full pinned IntentBond/Lean checks and ib impact on the retained evidence, inspect requirement/assertion correspondence and the complete diff, verify exported source, and retain evidence. Keep this plan concise and current. Independent factory review must inspect source fidelity, predicate meaning, missing-information counterexamples, unchanged key semantics and universe bounds. Publish a draft with Closes #18 only after all gates pass; no merge, ready-for-review transition or deployment.

Expected affected files: FormalCD/Basic.lean, Morphism.lean, Semantics.lean, new signature/metamodel modules, FormalCD.lean, tests/formalcd_imports.lean, tests/test_project_modules.py and affected living docs. Existing examples may need compatible elaboration updates but must retain their assertions. New requirement names must be checked for uniqueness. Suggested independent names: formalcd-signature-extension, formalcd-metamodel-shape, formalcd-metamodel-disciplines, formalcd-formula-identity, formalcd-metamodel-examples.

Primary risks: silently conflating full bindings with bags; hiding the figure's empty-args restriction; vacuous nd/ad meanings; breaking the old specialization; and interpreting model-language metaclasses as Lean universes. The accepted specification addresses these explicitly. Further semantic choices that change these contracts require NEEDS_INPUT; ordinary file/API organization does not.

Implementation organization: signature-independent wrappers preserve the existing
Raw/CD/Hom API while RawOver/CDOver/HomOver carry arbitrary supported vocabularies.
The metamodel is split into Shape, Basic, Binding, Discipline and Interpretation;
Examples, InterpretationExamples and NameExamples keep acceptance witnesses out
of public imports. Candidate validity is proved equivalent to typed Formula.
Concrete interpretation acceptance uses an ad/key/total fragment and separate nd
witnesses; whole-metamodel self-description remains outside the accepted scope.
Validation uses the unchanged full trace/Lean command and full diff review, with
results retained in external evidence rather than this plan.
The factory owns export verification and independent review before publication. #19 stays open; any handoff must separate proved construction facts, structural validity, concrete satisfaction and remaining self-description obligations.
