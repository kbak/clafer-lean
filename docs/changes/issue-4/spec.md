# Issue #4 implementation specification

This proposed package refines [issue #4](https://github.com/kbak/clafer-lean/issues/4) using its [Q1 research comment](https://github.com/kbak/clafer-lean/issues/4#issuecomment-6224179327). Submission for implementation adopts the correction below. The comment's old research-only status is historical context, not an instruction to omit these deliverables.

## Source and scope

Implement SoSyM B.1 Definitions 1–5, Theorems 1–2 and B.2.1–2 within DPGraph. Use the source comparison, citations and hashes in [docs/SOURCES.md](https://github.com/kbak/clafer-lean/blob/cabcf18abf231a4aac510d8f9996110ff2d8db09/docs/SOURCES.md#span-composition-q1-research-for-4). The B.2.1 correction below is an explicitly selected correction to the source, not a verbatim paper theorem. Keep the existing abstract B.4/B.5 interface and separate public roots.

## Definitions and acceptance criteria

1. Represent a span from A to B by a link type L with total source and target functions. Independent endpoint/link universes are required. Distinct links with equal endpoints must remain distinct.
2. A span isomorphism is a head equivalence commuting with both legs, allowing different head universes. Supply the basic identity, symmetry and transitivity operations needed by the proofs.
3. Represent indexed mappings by I : A → Type and evaluation ∀ a, I a → B. Their equivalence consists of fiberwise index equivalences preserving evaluation. Convert spans to source fibers and families to dependent-sum heads. Prove both roundtrips up to the respective equivalence, with explicit universe joins. Establish the relation-reduction correspondence in B.1 Theorem 1 using endpoint-membership equality.
4. Define red(q)(a,b) iff there exists a q-link with endpoints (a,b). A relation span has the subtype of satisfying endpoint pairs as its head. Prove joint endpoint injectivity iff target evaluation is injective in every source fiber, and iff the span is isomorphic to its reduced relation span (B.1 Theorem 2).
5. Define source-to-target composition q ⋆ r using the head {(l,m) | tq(l)=sr(m)} and outer endpoint functions. Prove compatibility with indexed-family composition, whose indices at a are Σ i : I a, J (f a i). Preserve all link pairs.
6. Define the identity span using head A and identity legs. Construct left/right unit isomorphisms and the canonical associator ((l,m),n) ↔ (l,(m,n)). State these as span isomorphisms, with universe joins; no strict equality between differently represented heads is promised.
7. Inversion retains the head and swaps its legs. Prove involution and that reduction gives relational converse. This operation does not make arbitrary spans categorically invertible.
8. Adopt and prove red(q ⋆ r) = red(q) ; red(r) for arbitrary spans, where ; is existential relational composition in source-to-target order. Prove the canonical composite-to-relation-span map is surjective, and that span isomorphism to this relation span holds exactly when (l,m) ↦ (sq(l),tr(m)) is injective. No finiteness, decidable equality or injectivity assumptions belong on the general reduction theorem.
9. For relational inputs, characterize this injectivity by at most one intermediate object for each pair of outer endpoints. Prove the sufficient cases from the comment: the first relation is single-valued, or the converse of the second is single-valued. Neither requires totality.
10. Supply kernel-checked examples: parallel links with identical endpoints; empty spans/fibers; the two-intermediate-object example with two composite links and only one reduced endpoint pair; a parallel-input-link example showing uniqueness of the intermediate object alone does not suffice for arbitrary spans; and conversions/laws with differing universe levels. In the two-path example the second relation is single-valued, so demonstrate that this alone does not imply the stronger isomorphism.

## Requirements and documentation

Preserve existing IDs/revisions and obligations in docs/spec.md, especially intent~formalization-foundation~1, intent~traceable-contributions~1, req~lean-validation~1, req~intentbond-workflow~1 and req~github-tracking~1. Add separately reviewable mathematical requirements in docs/spec.md, covering the existing foundation intent, with implementation/proof obligations. Suggested unique names, subject to a fresh collision search: span-representation, span-family-correspondence, span-set-valuedness, span-composition, span-inversion, span-relation-composition and span-examples. Use revision 1 initially and the existing Markdown trace convention.

Update req~public-foundation~1 and living documentation from “concrete spans undelivered” to the exact delivered scope. Update the Q1 source map from proposed correction to the adopted law and actual proof references. Keep other source questions open. Do not redeclare canonical OFT items in frozen change documents. Maintain named Markdown implementation/proof artifacts linked to actual Lean declarations.

## Validation and delivery

Use pinned Lean v4.35.0 and Mathlib 56a005855ea17e0b0958f73ec801ae140b0a1679, and the pinned IntentBond workflow. Run ib check against the captured base; its configured bash scripts/check.sh must pass the full build, kernel checks, axiom/layer audits, public-import and regression checks. No sorry/admit, new escape axioms, unsafe mathematics or weakened scope/coverage. Verify evidence against the final commit and retain independent semantic review of statements and source correspondence. Exit 4 means review remains pending.

Publish a draft PR with Closes #4 only after factory gates pass. Keep the issue open until acceptance and merge. No merge, ready-for-review transition or deployment is authorized by this package.
