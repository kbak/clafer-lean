# Implementation plan — #17

Approved scope: first FormalCD representation, naming/declaration invariants,
name-preserving morphisms and checked witnesses. See this package's spec.md;
canonical intent and requirements remain docs/intent.md and docs/spec.md.

## Source and task identity

- Project/repository: clafer-lean / kbak/clafer-lean; one repository.
- Task: issue-17; link the resulting PR with Closes #17.
- Reviewed base: dccdc5d1c2d698d34a06bf279290cb8ebfe0d94f (merged #34).
- Source anchors: SoSyM §6.1.1 inclusion IDs/names; §6.1.2 typed predicates;
  §6.1.3 predefined name discipline, formula identity and defaults; Figure 21c's
  explicit bag-valued args. B.4 Definitions 6–10 supply reused DP infrastructure.
- The catalog is stale; plan/dispatch pin the live base. A changed base requires
  reviewing its delta and preparing the package again.

## Steps and likely affected files

1. Inspect the pinned base's DPGraph.Predicates.signature, Formula, Hom,
   Interpretation and existing trace conventions. Capture the exact starting
   commit. Confirm no collisions for the proposed requirement names.
2. Add FormalCD/Basic.lean (and Vocabulary.lean if useful) for predefined
   registry, metadata, raw diagram, explicit WellFormed conditions and bundled CD.
   Reuse the existing predicate signature and carrier without new graph identity.
   Choose minimal helper constructors for unary formula bindings and defaults.
3. Add FormalCD/Morphism.lean for the DP map plus name/annotation/mode
   preservation, forgetful projection, identity/composition, extensionality and
   laws. Use the source/target-independent well-formedness proofs and existing
   DPGraph laws. No global injectivity or declaration reflection.
4. Add FormalCD/Examples.lean for the accepted positive and negative witnesses.
   Exercise a genuine nonidentity map, composition, repeated isA names, reserved
   names, optional predefined identity, missing defaults, explicit bag maps and
   concrete model restriction. Keep examples out of FormalCD.lean.
5. Update FormalCD.lean and tests/public_imports.lean to exercise the reusable
   public API. Existing automatic module discovery should cover new modules;
   change the validation harness only if a concrete integration gap needs it.
6. Maintain docs/spec.md, new docs/formalcd-trace.md, docs/ARCHITECTURE.md,
   docs/SOURCES.md, docs/intent.md, README.md and AGENTS.md where affected.
   Preserve existing IDs and link new requirements to the canonical intent.
   Explain that the selected name/mode-preserving morphism is this library's
   contract and that primitive annotations do not implement primitive semantics.
   Keep the accepted package snapshots unchanged; update this plan with actual
   file organization and completed steps.
7. Run pinned IntentBond with the captured base and supplied scope, including
   bash scripts/check.sh. Retain source-bound evidence. Factory verification
   and independent semantic review must pass; repair in-scope failures. Produce
   the draft PR and return ticket updates to the coordinator.

## Key implementation risks and checks

- Confusing strings with identity: prove two distinct inclusion arrows can
  share isA; do not require all classifier names to be injective.
- Losing typed bindings: retain repeated arguments and isolated arity vertices.
- Weak or misplaced defaults: all ordinary maps require setValued declarations;
  bag mode must not inherit them automatically; inclusion mode requires inclusion.
  Check negative raw diagrams as well as successful construction.
- Overclaiming morphism behavior: show a DP map with a name/mode mismatch cannot
  lift, and separately prove all chosen preservation conditions compose.
- Overclaiming semantics: preserve generic model restriction, name the supplied
  interpretation and distinguish raw validity, bundled well-formedness and
  satisfaction. Do not equate a primitive class label with its semantic domain.
- Dependent edge equalities/universes: reuse Prefunctor and DPGraph.Hom
  extensionality; keep the generic graph/interpretation universes unrestricted.
- Trace artifacts must point to actual checked Lean declarations; passing OFT
  links alone does not establish their semantic correspondence.

## Verification and boundaries

The trusted check remains bash scripts/check.sh via ib check; it discovers,
builds, kernel replays and axiom audits every new module, and verifies layer
boundaries. Independent semantic review assesses source correspondence and
theorem statements. Preserve warning enforcement and all current coverage floors.
Do not alter scope or pins to pass.

This package does not encode Figure 21c, prove self-description, choose VC's
disputed inequality, add a name-renaming operation, or implement Clafer gluing.
No new semantic question was identified that prevents this bounded implementation.
Material contradictions discovered in execution require NEEDS_INPUT; routine
file organization, helper lemmas and proof choices are delegated to the worker.

