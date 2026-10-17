# Sources and open decisions

The [roadmap/source audit (#2)](https://github.com/kbak/clafer-lean/issues/2) and
[architecture design (#13)](https://github.com/kbak/clafer-lean/issues/13) remain
open. [Slice #14](https://github.com/kbak/clafer-lean/issues/14) and the
[abstract reduct #15](https://github.com/kbak/clafer-lean/issues/15), together with
[spans #4](https://github.com/kbak/clafer-lean/issues/4), select the
following bounded source; this is not a complete audit of the literature.

## Primary source

*Clafer: unifying class and feature modeling*, 2014 SoSyM author preprint,
[PDF](https://gsd.uwaterloo.ca/sites/default/files/2014-Bak-Clafer-Unifying-Class-Feature-Modeling%28SOSYM%29.pdf),
[DOI](https://doi.org/10.1007/s10270-014-0441-1). The inspected source is the
34-page preprint with SHA-256
`56b1c18e74807fb7646c0e89cb2fc306f4178affb41fee52fcebde09b031b2fb`.
Appendix B.1 Definitions 1–5 and Theorems 1–2, B.2.1–2 (with the adopted
correction below), B.4 Definitions 6–10 and the abstract restriction argument of
B.5 Theorem 3 ground this slice:

| Source | Lean correspondence |
| --- | --- |
| B.1 Definitions 1–5, mappings and equivalences | `Span`, `Span.Iso`, `IndexedFamily`, `IndexedFamily.Equivalence`, `Span.toFamily`, `IndexedFamily.toSpan`, `Span.red`, `Span.ofRelation` |
| B.1 Theorem 1, relation correspondence | `Span.red_toFamily`, `IndexedFamily.red_toSpan`, `Span.red_ofRelation` |
| B.1 Theorem 2, set-valuedness | `Span.jointlyInjective_iff_fiberwise`, `Span.jointlyInjective_iff_iso_relation` |
| B.2.1–2, mapping operations | `Span.comp`, `IndexedFamily.comp`, `Span.leftUnit`, `Span.rightUnit`, `Span.associator`, `Span.inverse`; corrected comparison is detailed below |
| Definition 6, graphs and graph morphisms | Mathlib `Quiver`, `Quiv`, `Prefunctor`; [representation](ARCHITECTURE.md) |
| Definition 7, signature | `DPGraph.Signature` |
| Definition 8, formula | `DPGraph.Formula` |
| Definition 9, DP-graph | `DPGraph` |
| Definition 10, DP morphism | `Formula.translate`, `Hom`, `Hom.id`, `Hom.comp`, their laws and `DPGraph.category` |
| B.5, satisfaction and Theorem 3 | `Interpretation.Satisfies`, `IsModel`, `isModel_reduct`, `Model`, `reduct` and its laws |

The finite arrow-list notation is shorthand, not a generic finiteness restriction.
Formula arguments are graph maps. The structural examples introduce syntax-only
names; `SemanticsExamples` separately supplies an illustrative interpretation.
The abstract interface for B.5 takes each symbol's meaning to be a set of its
arity diagrams in a fixed semantic graph. A formula holds when its binding
composed with a candidate model belongs to that set. A target model restricts along `F : S → T` because `F` sends every
source declaration to a target declaration; graph-map associativity identifies
the two evaluations. This proves the abstract reduct direction of Theorem 3,
without extra closure or invariance assumptions on predicate meanings. Concrete
span predicate interpretations and SetMap are not implemented. The formula-level
satisfaction equivalence does not assert whole-model reflection.
[Trace artifacts](dpgraph-trace.md) name the actual declarations and proofs.

## Supporting sources and licenses

Mathlib is pinned to [56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679)
(v4.35.0), with the same Lean v4.35.0 pin. Inspected APIs:
[Quiver.Basic](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean),
[Quiver.Prefunctor](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Prefunctor.lean),
[Category.Basic](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/CategoryTheory/Category/Basic.lean),
[Category.Quiv](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/CategoryTheory/Category/Quiv.lean),
and [Equiv.Basic](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Logic/Equiv/Basic.lean).
Mathlib's Apache-2.0 license was checked; it is consumed as a pinned dependency,
without vendoring its source. Paper definitions are independently formalized with
citations; publication text and figures are not reproduced.

The supporting comparison uses the inspected author-uploaded Diskin & Wolter (2008),
[DOI 10.1016/j.entcs.2008.10.041](https://doi.org/10.1016/j.entcs.2008.10.041),
§4.1 Definitions 4.1–4.5. Its signatures add dependency arrows and closure.
Those additions are deliberately absent from this SoSyM slice. Full 2003/2000
secondary papers were not obtained. The maintained Haskell compiler is
supplementary context, not evidence used for this slice; later use must pin a
commit and check licensing.

## Span composition: Q1 research for #4

[#4](https://github.com/kbak/clafer-lean/issues/4) covers SoSyM B.1 Definitions
1–5, Theorems 1–2 and B.2.1–2. Its accepted implementation scope adopts the
correction below. The [span library](../DPGraph/Span.lean) implements that law and
its exact stronger-isomorphism criterion. This is a selected correction, not a
verbatim paper theorem. The abstract B.4/B.5 interpretation interface remains
independent of concrete predicate meanings.

### Source comparison

SoSyM B.1 distinguishes link identity, span isomorphism and relation reduction.
B.2.1, printed p. 29, first defines set-valued composition by union, then defines
span composition by a pullback of links. Its assertion that these coincide up to
isomorphism for relational inputs conflicts with its immediately following
two-path example. B.2.2 defines inversion by swapping legs.

Supporting full texts inspected for this question:

- Bąk, *Modeling and Analysis of Software Product Line Variability in Clafer*
  (2013), [Waterloo record](https://hdl.handle.net/10012/8039),
  [PDF](https://uwspace.uwaterloo.ca/bitstreams/fe498b08-4ee2-4247-9f2e-c1b3fc67d0ee/download),
  Appendix A.2.2, printed pp. 120–121 (PDF pp. 134–135). It repeats both the
  coincidence assertion and counterexample; it supplies no correction.
  SHA-256: `c623e685481a777b3387b8feb5aff9f9f62f431936318fba1830a75b3105b689`.
- Diskin, Easterbrook & Dingel, *Engineering Associations: From Models to Code
  and Back through Semantics* (2008),
  [author-hosted PDF](https://www.cs.toronto.edu/~sme/papers/2008/zTOOLS-08.pdf),
  §3.2–3.4, printed pp. 7–8. Labeled links retain repeated endpoint pairs;
  set-valuedness is a constraint. Inverse association ends have isomorphic
  extensions. This supports preserving links but does not establish the disputed
  composition claim.
  SHA-256: `34ed4bf6c4014e58445605392f03c5e638950dac6be07f3f0e7d485215b0d4cd`.
- Diskin, *Model Synchronization, Mappings, Tile Algebra, and Categories* (2011),
  [author-hosted manuscript](https://gsd.uwaterloo.ca/sites/default/files/zGttse11_0.pdf),
  Appendix B, manuscript pp. 61–63, Figure 32. It composes spans by pullback and
  explains associativity up to canonical isomorphism, or on isomorphism classes.
  Its application restricts both legs to injections. That restriction is stronger
  than jointly injective endpoint pairs and must not be imported into general
  Clafer mappings. §7.1, manuscript p. 45, also warns that a relational treatment
  loses structure carried by matching links.
  SHA-256: `0fdfb6cd9b6ff5006c9f6726ea6f105ea975079b5ef5a70c15f6581c6608153c`.

These texts are cited and independently analyzed; no publication text, figures
or third-party implementation are incorporated. SoSyM remains the primary
authority. The older thesis and the synchronization tutorial do not override it.

### Adopted correction and exact assumptions

Write `q ⋆ r` for **span composition** in source-to-target order, and `R ; S` for
**relational composition**. For spans `q : A ↛ B` and `r : B ↛ C`, let

```text
P = { (l, m) : Lq × Lr | tq(l) = sr(m) }
e(l, m) = (sq(l), tr(m))
red(q)(a, b) ↔ ∃ l : Lq, sq(l) = a ∧ tq(l) = b.
```

The adopted compatibility theorem, proved as `Span.red_comp` for arbitrary spans, is

```text
red(q ⋆ r) = red(q) ; red(r).
```

Proof: a composable link pair supplies the intermediate object `tq(l) = sr(m)`.
Conversely, an intermediate object and witnesses for the two reduced relations
supply a composable pair. This equates endpoint membership, not link types.
It requires no finiteness, decidable equality or injectivity assumptions.

The map from `P` onto the head of the relation span for the right-hand side sends
`(l,m)` to `e(l,m)`. It is surjective by the same argument. It is a bijection
exactly when `e` is injective, equivalently when for every `(a,c)` there is at
most one composable **link pair** with those endpoints. This is also necessary
and sufficient for the composite span to be isomorphic to that relation span.

When both inputs are relations (their endpoint pairings are injective), this
condition simplifies to at most one intermediate `b` for each `(a,c)` satisfying
`red(q)(a,b) ∧ red(r)(b,c)`. Sufficient special cases are that `q` is single-valued
or that the converse of `r` is single-valued; neither needs totality. For arbitrary
spans, uniqueness of `b` alone is insufficient because parallel input links can
still yield several link pairs.

For the counterexample, take `A={a}`, `B={b₁,b₂}` with `b₁≠b₂`, `C={c}`,
`q={(a,b₁),(a,b₂)}`, `r={(b₁,c),(b₂,c)}`. The pullback head has two elements,
while the relational composite has one. There is no bijection and hence no span
isomorphism. Both inputs are relations; `r` is even a total single-valued function.
Relational inputs therefore do not suffice, nor does single-valuedness of the
second input. The adopted correction preserves this example and replaces the
unqualified coincidence assertion with equality after reduction.

### Delivered implementation boundary and proof references

The operations and equivalences are independently available through `import DPGraph`.
Names below are relative to `DPGraph`; the [trace artifacts](dpgraph-trace.md)
link their requirement and proof obligations.

| Construct | Implementation and proof references |
| --- | --- |
| Spans and isomorphisms | [Basic.lean](../DPGraph/Span/Basic.lean): `Span`, `Span.Iso`, `Span.Iso.refl`, `.symm`, `.trans`, `.red_eq` |
| Indexed families and conversions | [IndexedFamily.lean](../DPGraph/Span/IndexedFamily.lean): `IndexedFamily`, `.Equivalence`, `.toSpan`, `Span.toFamily`, `Span.familySpanIso`, `IndexedFamily.spanFamilyEquivalence` |
| Relation membership (Theorem 1) | [IndexedFamily.lean](../DPGraph/Span/IndexedFamily.lean): `Span.red_toFamily`, `IndexedFamily.red_toSpan`; [Relation.lean](../DPGraph/Span/Relation.lean): `Span.red_ofRelation` |
| Set-valuedness (Theorem 2) | [Relation.lean](../DPGraph/Span/Relation.lean): `Span.jointlyInjective_iff_fiberwise`, `.jointlyInjective_iff_iso_relation`, `.relationIso` |
| Composition and laws | [Composition.lean](../DPGraph/Span/Composition.lean): `Span.comp`, `.identity`, `.leftUnit`, `.rightUnit`, `.associator`, `IndexedFamily.compSpanIso`, `Span.compFamilyEquivalence` |
| Inversion | [Basic.lean](../DPGraph/Span/Basic.lean): `Span.inverse`, `.inverse_inverse`, `.red_inverse` |
| Adopted reduction law and exact criterion | [Relation.lean](../DPGraph/Span/Relation.lean): `Span.red_comp`, `.compToRelation_surjective`, `.comp_iso_relation_iff`, `.comp_jointlyInjective_iff_uniqueIntermediate`, `.relations_comp_jointlyInjective_iff` |
| Sufficient conditions, without totality | [Relation.lean](../DPGraph/Span/Relation.lean): `Span.relations_comp_injective_of_first_singleValued`, `.relations_comp_injective_of_converse_second_singleValued` |
| Counterexamples | [Examples.lean](../DPGraph/Span/Examples.lean): `Span.Examples.twoPaths`, `.oneReducedPair`, `.second_singleValued_not_sufficient`, `.parallel_uniqueIntermediate`, `.parallel_composite_not_iso` |

Universe bounds remain compatible with [#15](https://github.com/kbak/clafer-lean/issues/15):
the family-to-span head lies in the maximum of source and index universes, and
the relation head in the maximum of the endpoint universes. A roundtrip need not
return a head in the original syntactic universe. Explicit joins and the mixed-universe
examples track these bounds without imposing one global universe or a resizing axiom.

A bicategory, a quotient of all spans, global finiteness and executable object generation are unnecessary for #4.
The meaning of commutativity and inverse predicates in Table 3 remains a
separate review for [#16](https://github.com/kbak/clafer-lean/issues/16); equality
of reduced relations alone does not establish equality or isomorphism of spans.

## Open for later increments

Keep these questions open in #2/#13 before implementing the affected semantics:

- Table 3 versus Figure 21 disjointness arity.
- Figure 21 VC inequality direction.
- Appendix D intersection typo and Appendix E analogous clauses.
- Label/identity choices for gluing.

These remaining questions are not resolved by the span definitions or examples.
Q1 alone has the adopted correction and proof references above.
