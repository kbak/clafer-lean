# Issue #18 implementation specification

Implement https://github.com/kbak/clafer-lean/issues/18 in kbak/clafer-lean.
Approved starting main: `5e4f13c8e1ba58e0b0c744c1aa0397909e20f79e` (merged #35).
Dependencies #16/#34 and #17/#35 are complete. Link the eventual draft PR with `Closes #18`; keep the issue open until acceptance and merge. #19 is not included.

## Sources and retained context

Use the canonical [intent](https://github.com/kbak/clafer-lean/blob/5e4f13c8e1ba58e0b0c744c1aa0397909e20f79e/docs/intent.md), [requirements](https://github.com/kbak/clafer-lean/blob/5e4f13c8e1ba58e0b0c744c1aa0397909e20f79e/docs/spec.md), architecture, source map and traceability guidance. Read AGENTS.md and CLAUDE.md at the actual task base; the coordinator catalog is stale and is not the implementation source.

Primary source: 34-page 2014 SoSyM author preprint, SHA-256 `56b1c18e74807fb7646c0e89cb2fc306f4178affb41fee52fcebde09b031b2fb`, §6.1.1–3, Figure 21c on printed p.17, explanatory p.19 and Appendix B.4 Definition 8 on p.30. The PDF and a reference rendering are supplied as read-only factory inputs for inspection; do not commit third-party papers or figures. Independently formalize the definitions and retain precise citations. Existing Q1/Q8 corrections and #16's meanings remain authoritative.

## Compatible signature support

Provide the minimal reusable extension of FormalCD needed for metamodel-specific predicates while retaining the existing built-in signature as a supported specialization. Reuse DPGraph.Signature, Formula, Quiv/Prefunctor and Interpretations; introduce no parallel graph/formula framework.

Specify an arity-preserving inclusion of built-in symbols into the extended vocabulary and prove the relevant formula/translation compatibility. Built-in interpretations, ordinary-map setValued defaults, inclusion defaults, bag behavior, registry metadata and optional predefined identifiers retain their accepted meanings. Existing name-preserving morphisms, forgetting, identity/composition and model-reduct laws must remain valid at the supported common signature. Keep the existing public API usable, by compatible specialization/aliases where necessary, and retain all existing acceptance examples. No parser or general constraint-expression language is required.

Use explicit universe parameters and account for any joins/lifts. Do not narrow the existing universe-polymorphic DPGraph APIs. Ordinary Lean data may describe a model-language class named Class or Signature; those names do not denote the collection of all Lean types/signatures.

## Figure 21c construction

Create a source-linked inventory and typed metamodel value with these eleven node identities: Classifier, Class, Map, Incl, Predef, SING, Dom, String, PredefStr, Formula and Signature. Distinguish the SING metaclass identity, its modeled predefined class, and an object of that class.

The figure's seven inclusion arrows are:
PredefStr to String; Class to Classifier; Map to Classifier; Predef to Class; SING to Predef; Dom to Predef; Incl to Map.
The other six arrows are:
name from Classifier to String; name from Predef to PredefStr; so and ta from Map to Class; args from Formula to Map; pred from Formula to Signature.
Arrow identities remain distinct even when their displayed names coincide.

Account explicitly for the two cover/disjoint pairs (Class/Map covering Classifier; SING/Dom covering Predef), inclusion/default declarations, the total/single-valued notation on name/so/ta/pred, the explicitly bag-valued args arrow and its drawn totality, and the nd/ad/key annotations. Recheck the reference image and prose before finalizing the inventory. Record inferred binding choices for annotations whose dashed attachment is omitted; justify their arities by the stated constraint, not by inventing hidden figure incidence.

Keep args as a bag with repeated argument occurrences. Do not impose an ordinary-map setValued default on it. The figure's total args annotation excludes empty argument fibers. Record that limitation; do not silently delete the annotation or make generic zero-arrow arities illegal.

Prove arity-correct construction, explicit incidence/declaration facts and the structural facts needed by the later #19 work. Local syntactic well-formedness may be proved when useful, but it neither proves semantic satisfaction nor closes #19.

## Name and arity meanings

nd and ad must have explicit mathematical predicates and an actual connection to their typed declarations/interpretation. Bare uninterpreted labels, True placeholders or simply pointing to Lean typechecking are insufficient.

Name discipline must express the selected registry/naming contract: canonical names for realized predefined identifiers, user class names outside the reserved set, and compatible name restriction along the displayed predefined inclusions. Preserve the existing optional-entry and identity rules. Do not impose global classifier-name injectivity; inclusion arrows can share isA.

Arity discipline must express that a formula selects a symbol and a complete incidence-preserving binding from its arity graph. Retain the indexing of argument occurrences and all vertex images, including isolated vertices. Define the required representation context explicitly: the symbol-to-arity assignment, interpretation of names/predefined values, and any extra vertex/index data not drawn in Figure 21c. Separate arbitrary candidate data from its validity condition so malformed incidence/arguments can be rejected. Show the stated relationship to the existing typed Formula representation; do not make the validity proof an unexplained input assumption.

The interpretation may be parameterized by the necessary explicit descriptor/registry context. State its exact domain, and give meaningful positive and negative witnesses. Do not claim the unaugmented graph alone can recover information it does not contain.

## Formula identity and the literal key constraint

The authoritative formula identity is the existing pair of symbol and full graph binding. Equal symbols and equal vertex/arrow actions determine equal formulas; changed argument positions or isolated-vertex images can distinguish formulas. Retain repeated arguments. Establish these claims with extensionality/correspondence results and witnesses.

Preserve the accepted generic `DPGraph.Predicates.Key`/BagEquiv semantics from #16. Figure 21c's literal [key](args,pred) must be represented with that documented meaning, not silently strengthened to an indexed key. Its satisfaction is an additional condition on instances; it is not automatic for arbitrary sets of graph-shaped formulas. Full binding data is retained separately when presenting the metamodel instance correspondence.

Include checked counterexamples/limitations showing that an unindexed arrow bag can forget argument positions, and that an arrow-only projection can forget isolated vertices. A source-faithful construction and a faithful full-binding identity API are both required; they do not establish a universal every-CD-is-an-instance theorem for the printed metamodel. Explain this exact boundary for #19 in the source map. Do not quotient existing formulas by bag equivalence, change generic key meanings, or claim these projections are injective without hypotheses.

## #19 and universe boundary

#18 delivers the metamodel and the selected meanings/construction facts. Leave #19's final self-description/example theorem and VC semantics open. Self-description must later be stated as an explicitly typed representation/well-formedness result with its signature, registry and universe bounds. It does not follow that a model is its own semantic instance or that Lean has a self-containing universe.

No recursive `Type : Type`, all-types SetMap, impredicative Type encoding, resizing/self-instantiation axiom, unchecked casts, or new escape axioms. Normal universe-polymorphic data and justified lifts are allowed. No proof may silently identify syntax-level Class/Map/Signature data with Lean types or semantic objects. Record any gap requiring a stronger theorem as a #19 obligation rather than solving it by changing the foundation.

## Requirements and checks

Preserve existing OFT IDs and trusted scope. Update continuing FormalCD structure/declaration/morphism requirements only to describe the compatible extension; retain the old specialization's obligations. The existing `req~predicate-key~1`, all generic DPGraph promises, Q1/Q8 and universe contracts remain unchanged.

Add independently meaningful requirements for signature extension, metamodel shape, discipline meanings, graph-formula identity and acceptance witnesses in docs/spec.md. Link them to `intent~formalization-foundation~1` and actual Lean declarations using named Markdown implementation/proof artifacts in docs/formalcd-trace.md. Update current intent, architecture, source map and reusable guidance only where the delivered increment changes them. Keep source/code/tests/requirements consistent; frozen task intent/spec/acceptance snapshots remain unchanged.

Required witnesses include the complete inventory/defaults, valid and invalid names, invalid arity/incidence data, repeated args, nontrivial symbol/binding identity cases, argument-position and isolated-vertex projection failures, the zero-arrow/total-args boundary, and a concrete nontrivial use of the extended interpretation. Check built-in specialization compatibility, morphism/reduct laws and independent public imports. State exactly which finite model witnesses satisfy the literal key/totality and which do not; no universal realizability claim.

Run pinned `ib check` against the captured base, including unchanged `bash scripts/check.sh`, all discovered module builds, kernel replay, axiom/layer/public-import audits and relevant regressions. Verify the exported commit against retained evidence; exit 4 is automation success with review pending. The factory's independent semantic/code/security review must pass before draft PR publication. No sorry/admit, unsafe/partial mathematics, unchecked axioms, skipped tests, scope weakening or dependency/toolchain updates.

Keep any material source contradiction or unauthorized narrowing visible and request NEEDS_INPUT before making that change. A theorem failure is not grounds to redefine the target promise.
