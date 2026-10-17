# Issue #16 implementation specification

Issue: https://github.com/kbak/clafer-lean/issues/16
Canonical overview: [docs/intent.md](https://github.com/kbak/clafer-lean/blob/030340d9d8700c1d6d722d4f0efc18dc0eb86647/docs/intent.md).
Reviewed base: `030340d9d8700c1d6d722d4f0efc18dc0eb86647`.

Implement the complete #16 increment under the accepted plan. The maintainer explicitly confirmed the Q8 correction: Table 3 has the wrong disjointness shape; the intended meaning is §6.1.2/Figure 21's common-target maps with nonoverlapping images. The contracts below retain the discussed scope and existing APIs. Acceptance authorizes implementation and normal factory validation/review; this specification reports no completed implementation or proof results.

## Source and preserved obligations

Use the SoSyM 34-page author preprint, SHA-256 `56b1c18e74807fb7646c0e89cb2fc306f4178affb41fee52fcebde09b031b2fb`: Table 3 (printed p.12), §6.1.1–2/Figure 21 (pp.17–18), Appendix A.1 (p.28), B.1–3 (pp.28–30), and the delivered B.4/B.5 interfaces. Cite exact locators and record the selected interpretations in `docs/SOURCES.md`.

Preserve the existing intent IDs and continuing requirements in [docs/spec.md](https://github.com/kbak/clafer-lean/blob/030340d9d8700c1d6d722d4f0efc18dc0eb86647/docs/spec.md), including `req~dpgraph-core~1`, `req~dpgraph-interpretation~1`, `req~dpgraph-model-reduct~1`, every `req~span-*~1` obligation, and validation/IntentBond/tracking/public-documentation requirements. Preserve the Q1 correction: relational composition agrees after reduction, while span composition retains every composable link pair.

## Concrete semantic graph

Provide a graph parameterized by an ambient type `U : Type u` and a link-universe bound. Its vertices are subsets `A : Set U`; arrows from A to B are existing `DPGraph.Span` values on their subtype carriers. Choose an explicit link universe containing the object universe (for example `max u w`), and state the resulting graph universes. Keep the existing unrestricted Span and Interpretation universe parameters unchanged.

This representation allows two classes to share the same underlying object and makes inclusion mean identity on that object. Distinct subtype memberships are not distinct object identities. It is a bounded semantic graph, not an all-universes SetMap. Reuse existing quivers and prefunctors; do not add another graph formalism or impose a category structure on these arrows.

## Typed vocabulary and meanings

Separate arity declarations from interpretations. Build a signature using real arity quivers and graph-map bindings, with finite family arities parameterized by `n : Nat`. No global finite/decidable-equality restriction is introduced on objects, links or declaration sets. Preserve isolated central vertices for zero-member family arities and allow repeated argument bindings.

In the contracts below `q : A ↛ B` denotes an existing span; `q⁻¹` is leg-swapping inversion; `q ⋆ r` is the delivered pullback composition; `q ≅ r` means that `Span.Iso q r` is inhabited. These contracts compare fixed endpoint sets; their isomorphism-invariance claim concerns relabeling links while preserving endpoints.

| Predicate | Arity and required meaning | Source/disposition |
| --- | --- | --- |
| Inverse | Opposite arrows `q : A ↛ B`, `r : B ↛ A`; `q⁻¹ ≅ r`. This is not a categorical inverse equation. | Table 3 inv; B.1 Definition 2 and B.2.2 |
| Commutation (`=`) | Triangle `q : A ↛ B`, `r : B ↛ C`, `s : A ↛ C`; `q ⋆ r ≅ s`. | Table 3 equality interpreted with B.1's link-renaming equivalence; preserve Q1 |
| Key | Family `qᵢ : A ↛ Bᵢ`; if every source fiber at a is equivalent to its fiber at a′ by an equivalence preserving target values, then `a = a′`. | Table 3 key, generalized to finite families; bag comparison retains multiplicity |
| Cover | Family `qᵢ : Aᵢ ↛ B`; every b is the target of a link in at least one family member. | Table 3 cover; §6.1.2 |
| Disjointness — accepted Q8 correction | Same common-target family shape; for `i ≠ j`, no b occurs as a target in both `qᵢ` and `qⱼ`. | Accepted §6.1.2/Figure 21 meaning; document Table 3’s erroneous shape |
| Set-valued | One arrow; joint endpoint injectivity (`Span.JointlyInjective`). | B.1.4/Theorem 2 |
| Total | One arrow; source map is surjective. | A.1, Table 2, §6.1.1 |
| Single-valued | One arrow; every source fiber has at most one link, equivalently the source map is injective. | A.1's set-valued, possibly partial function; duplicate copies are excluded |
| Inclusion | One arrow between subsets of U; source map is bijective and the target and source of every link have equal underlying U values. | A.1 and §6.1.1 literal inclusion |
| Target/source multiplicity | One arrow plus lower `m : Nat` and finite upper `n : Nat` or unbounded `*`; bound the number of outgoing/incoming links at every source/target object respectively. | Table 3 mult-trg/mult-src; B.1 indexed families |

Multiplicities use cardinal bounds on the actual fiber, including repeated targets. An equivalent implementation uses an embedding `Fin m ↪ fiber` for the lower bound and `fiber ↪ Fin n` for a finite upper bound. `*` omits the upper condition; it does not introduce local finiteness. Do not use a natural-number cardinality function that turns infinite types into zero. For set-valued spans, prove that these link counts agree with the distinct-value counts in the fiber. Source bounds are target bounds of the inverse.

Do not replace span equations or bag equality with equality of reduced relations. Cover and disjointness intentionally use reachable endpoint values, so they may hold for bag-valued arrows. Key does not silently require total, single-valued or set-valued arguments: Figure 21c uses a bag-valued argument. No automatic set-valued default belongs in the generic signature; later diagram construction must declare it explicitly.

For zero-member families: key means the source is subsingleton; cover means the target is empty; disjointness is vacuous. These are documented consequences of the quantified contracts, not new finiteness requirements.

## Interpretation and proofs

Connect the signature to the concrete semantic graph using the existing `DPGraph.Interpretation`. Formula satisfaction and model restriction must use the delivered generic APIs. Demonstrate a concrete satisfying model and restriction along a nonidentity declaration-preserving DP morphism; include a rejected predicate instance. Do not claim whole-model reflection.

Prove endpoint-preserving link-isomorphism invariance for each predicate. Add the small reusable inverse/composition/fiber transport lemmas needed in the span modules, preserving their existing interfaces. Prove inverse symmetry, source/target multiplicity duality, the existing set-valued characterization as a predicate, total/single-valued fiber characterizations, and inclusion's subset/identity consequences. Existence of an arbitrary injective function does not imply inclusion.

## Acceptance examples

All examples must compile and be kernel checked. Include:

- Isomorphic relabelings satisfy inverse/commutation predicates; a triangle with two composite links and one direct link has equal reduced relations but fails commutation. Reuse #4's counterexample where helpful.
- A two-link fiber with one repeated target has multiplicity 2, fails set-valuedness and single-valuedness, and satisfies a suitable finite range; a one-link version distinguishes those predicates.
- Key detects different bags with the same support but different multiplicity; also exhibit a failing key whose complete bag tuple is equal at two distinct sources.
- Cover and disjointness have positive/negative cases, including repeated argument bindings and empty domains. Check the zero-family meanings and nonempty isolated central vertex.
- A literal inclusion and an empty inclusion succeed; an injective permutation moving an underlying object and duplicated identity links fail inclusion.
- Finite lower/upper boundaries, empty fibers, source/target reversal, and an infinite fiber accepted by an unbounded upper range but rejected by a finite one.
- The complete predicate interpretation interoperates with formula translation and model reduct, and explicit universe choices exercise a larger link universe without resizing.

Do not require an executable solver. The propositions and witnesses may be noncomputable where justified by Lean's existing allowed axioms.

## Requirements, documentation and completion

Add scoped requirements under `docs/spec.md`, using new stable names only after a collision check; suggested names are `setmap-semantic-graph`, `predicate-arities`, `predicate-inverse`, `predicate-commutation`, `predicate-key`, `predicate-cover`, `predicate-disjointness`, `predicate-unary-maps`, `predicate-multiplicity`, `predicate-interpretation`, and `predicate-examples`. New mathematical requirements cover the continuing foundation intent and require implementation and proof artifacts. Preserve continuing IDs/revisions and maintain named Markdown artifacts linked to actual Lean declarations in `docs/dpgraph-trace.md`.

Update the canonical intent, architecture, source map and public scope descriptions to reflect only delivered behavior. Document Table 3’s common-source disjointness shape as an error, not an additional predicate. Catalogue unsupported predicates: VC, name/arity disciplines, arbitrary path equations beyond the triangle, and later FormalCD/Clafer-specific predicates. Required historical task artifacts stay frozen; current plan stays concise.

Validate through the unchanged `scope.json` and `bash scripts/check.sh`, using pinned Lean/Mathlib and the repository-pinned IntentBond. Preserve `enableArtifactCache = false` for candidate libraries. Require complete module discovery, warning enforcement, kernel replay, axiom and layer audits, public imports, existing regressions, `ib check`, exported-source verification and independent semantic review. Exit 4 leaves semantic review pending. No sorry/admit, new axioms, disabled checks, relaxed coverage or changed dependency pins.

The factory opens a draft PR after its gates pass, with `Closes #16`; only acceptance and merge permit closing #16/marking Done. No merge or deployment is authorized.
