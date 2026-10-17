# Issue #19 implementation specification

Implement [#19](https://github.com/kbak/clafer-lean/issues/19) in `kbak/clafer-lean` as task `issue-19`. Start from latest main `bb2fe88c9ac060a0002ec8e503bcc5631f3be0ab` (merged #36), rechecked when freezing/submitting this package. Dependencies #16/#34, #17/#35 and #18/#36 are complete. Link the resulting draft PR with `Closes #19`; keep the issue open until acceptance and merge.

## Context and sources

Use the canonical [intent](https://github.com/kbak/clafer-lean/blob/bb2fe88c9ac060a0002ec8e503bcc5631f3be0ab/docs/intent.md), [requirements](https://github.com/kbak/clafer-lean/blob/bb2fe88c9ac060a0002ec8e503bcc5631f3be0ab/docs/spec.md), architecture, source map, traceability convention and AGENTS.md/CLAUDE.md at the actual task base. The coordinator catalog is stale; it is not the implementation source. The inspected current-source checkout is for reading only; implementation belongs in the factory's native worktree.

Primary reference: the 34-page 2014 SoSyM author preprint, SHA-256 `56b1c18e74807fb7646c0e89cb2fc306f4178affb41fee52fcebde09b031b2fb`, §6.1.1–3 and Figure 21a–c, with B.4 Definitions 7–9 for signatures/formulas/DP-graphs. For the VC correction, also cite Figure 8 line 9, its §4.3 explanation and Appendix F. Supplied PDF and Figure 21 rendering are read-only reference inputs, not repository content. Preserve original publication material and frozen #18 artifacts.

## Bounded self-description

Reuse `FormalCD.Metamodel.diagram`, `wellFormed`, the existing inventory and the full-binding correspondence. Deliver a clearly named, documented checked statement that Figure 21c is representable and well formed in the same supported `CDOver` family used for ordinary formal CDs and the Figure 21b example. State the concrete signature/vocabulary, registry and universe parameters in that result. Build on the existing proof instead of reproducing the metamodel or replacing the formal-CD framework.

Model-language Class, Map and Signature are ordinary data. Distinguish syntactic validity, a representation result and satisfaction under an explicit interpretation. This task does not require a proof that MCD is its own semantic instance, a universal every-CD-is-an-instance theorem, or a new interpretation of Lean universes. If any narrower metamodel-instance claim is made, prove its explicit key/totality and descriptor hypotheses; do not infer them from well-formedness.

Preserve indexed argument occurrences, all arity-vertex images, generic zero-arrow formulas and the existing `Candidate.formulaEquiv` correspondence. The literal key still compares bags, and total args still excludes empty fibers. Do not quotient formulas by bag equivalence, silently strengthen key, narrow DPGraph universes, introduce Type : Type/resizing/self-instantiation axioms, or use unchecked casts.

## Complete Figure 21b construction

Encode exactly these class identities: Comp, ECU, Display and Int. Encode five distinct arrow identities with incidence:
- i1: ECU → Comp;
- i2: Display → Comp;
- server: Display → ECU;
- display: ECU → Display;
- version: Comp → Int.

Both inclusions have displayed name isA while remaining distinct identities. Register Int as a predefined primitive with its canonical name; preserve optional registry entries and do not insert a required Sing class. Retain the existing naming, inclusion and ordinary-map modes/default rules.

Account explicitly for the twelve effective formulas described on printed p.19: disjoint(i1,i2), cover(i1,i2), inverse(server,display), inclusion(i1), inclusion(i2), outgoing multiplicity 0..5 on display, 1..1 on version, 0..1 on server, VC(server,i1,i2,version), and the three ordinary-map setValued defaults on version/server/display. Explain the total/single-valued arrow notation through these multiplicities. Use the accepted Q8 common-target disjointness and existing span inverse/multiplicity meanings.

Prove inventory, incidence, declaration membership, naming/default obligations and syntactic well-formedness. Keep typed full graph bindings. Reuse #18's compatible vocabulary extension for the extra VC symbol without changing built-in meanings or forcing VC into the generic DPGraph catalogue.

## Corrected VC and its interpretation

The accepted direction is `display.version ≥ server.version`. For a display d with server e, compare d's integer version to e's integer version and require the former to be at least the latter. Equality passes. A display with no server satisfies VC vacuously, as in Figure 21a's `self.server->notEmpty() implies ...`. Do not adopt the reversed adjacent prose.

Give VC a real arity graph with the server, i1, i2 and version arrows and their endpoints, then bind it to the Figure 21b graph. Give it an explicit mathematical meaning connected to `DPGraph.Interpretation` and the actual typed formula. Use the existing bounded subset/span semantic graph, with an explicit integer-domain realization/decoding and universe bounds. Under the example's inclusion and version multiplicity declarations, relate this meaning to the guarded integer comparison. Do not satisfy VC by a True placeholder, a disconnected Boolean test, or merely by constructing the formula.

Provide a concrete nonempty model satisfying every effective declaration, including VC, the inverse mapping, cover/disjointness, defaults and multiplicities. Concrete examples may have finite component/link sets while the integer domain is explicitly realized. The general library must not gain a finiteness restriction or a global primitive-domain framework as a side effect.

Kernel-check witnesses for:
- a served display whose version is strictly greater than its server's: VC holds;
- equal versions: VC holds;
- a served display whose version is strictly lower: VC fails;
- an unserved display: VC holds and the 0..1 server multiplicity remains faithful.

Exercise actual interpreted formula satisfaction. For the reversed-inequality counterexample, demonstrate that other Figure 21b declarations can still hold, so the failure isolates VC. Keep the interpretation and model proof distinct from syntactic well-formedness. Document the exact scope of any whole-model or representation claim.

## Requirements, documentation and compatibility

Preserve trusted scope and existing OFT names/revisions, including `intent~formalization-foundation~1`, `intent~traceable-contributions~1`, `req~formalcd-structure~1`, `req~formalcd-naming~1`, `req~formalcd-declarations~1`, `req~formalcd-examples~1`, `req~formalcd-signature-extension~1`, `req~formalcd-metamodel-shape~1`, `req~formalcd-formula-identity~1`, `req~predicate-multiplicity~1`, and all generic predicate/validation contracts. Read their full promises and follow the existing trace links.

Add independently meaningful source-linked requirements for bounded self-description, the complete example and VC semantics/witnesses in docs/spec.md; search names before assigning IDs. Requirements promising theorems need actual implementation/proof artifacts in docs/formalcd-trace.md pointing to Lean declarations. Inline Lean tags are not supported by the pinned OFT.

Update affected living docs: docs/SOURCES.md must record Q7's accepted direction and guard, remove its unresolved-direction claims, and retain the source discrepancy. Reconcile docs/intent.md, docs/ARCHITECTURE.md, README.md and reusable guidance where the delivered scope changes. Keep VC's FormalCD-level extension distinct from the generic built-in vocabulary's boundary. Frozen task intent/spec/acceptance records stay snapshots; keep plan.md concise and current. Return any required issue/roadmap status updates to the credential-bearing coordinator.

## Validation and completion

Run the normal factory workflow on the captured base, using the pinned IntentBond toolchain and unchanged `bash scripts/check.sh`. Required checks include all discovered Lean modules, kernel replay, warnings-as-errors, axiom audit, dependency-layer audit, independent public imports, existing regression suites and the new assertions. Retain `ib check` evidence and verify the exported commit against it. IntentBond exit 4 means automated checks passed with semantic review pending, not approval.

The normal independent read-only review must assess mathematical/source correspondence, the exact theorem boundaries, VC direction/guard and counterexamples, traceability, compatibility and code/security concerns. Use the factory's configured Alibaba/OCR review procedure; preserve its evidence. Tests and review must pass before draft PR publication, with only the normal bounded repair path. No sorry/admit, unchecked axioms, unsafe/partial mathematics, skipped tests, weakened scope or validation bypasses; no dependency/toolchain upgrade.

A material contradiction or a need to strengthen the promised self-description beyond these bounds requires NEEDS_INPUT before adopting a new meaning. Routine proof/module choices need no further approval. The factory writes handoff.md/handoff.json and reports the task/run identity and final result. Do not merge, mark the PR ready or deploy.
