# Sources and open decisions

The [roadmap/source audit (#2)](https://github.com/kbak/clafer-lean/issues/2) and
[architecture design (#13)](https://github.com/kbak/clafer-lean/issues/13) remain
open. [Slice #14](https://github.com/kbak/clafer-lean/issues/14) and the
[abstract reduct #15](https://github.com/kbak/clafer-lean/issues/15) select the
following bounded source; this is not a complete audit of the literature.

## Primary source

*Clafer: unifying class and feature modeling*, 2014 SoSyM author preprint,
[PDF](https://gsd.uwaterloo.ca/sites/default/files/2014-Bak-Clafer-Unifying-Class-Feature-Modeling%28SOSYM%29.pdf),
[DOI](https://doi.org/10.1007/s10270-014-0441-1). The inspected source is the
34-page preprint with SHA-256
`56b1c18e74807fb7646c0e89cb2fc306f4178affb41fee52fcebde09b031b2fb`.
Appendix B.4 Definitions 6–10 and the abstract restriction argument of B.5
Theorem 3 ground this slice:

| Source | Lean correspondence |
| --- | --- |
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
span meanings and SetMap are not implemented. In particular the formula-level
satisfaction equivalence does not assert whole-model reflection.
[Trace artifacts](dpgraph-trace.md) name the actual declarations and proofs.

## Supporting sources and licenses

Mathlib is pinned to [56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679)
(v4.35.0), with the same Lean v4.35.0 pin. Inspected APIs:
[Quiver.Basic](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean),
[Quiver.Prefunctor](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Prefunctor.lean),
[Category.Basic](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/CategoryTheory/Category/Basic.lean),
and [Category.Quiv](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/CategoryTheory/Category/Quiv.lean).
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
1–5, Theorems 1–2 and B.2.1–2. The following is a proposed source correction and
mathematical specification for review, not delivered Lean semantics or acceptance
of the increment. The delivered abstract interpretation interface does not select
span composition or any of these proposed concrete meanings.

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

### Derived correction and exact assumptions

Write `q ⋆ r` for **span composition** in source-to-target order, and `R ; S` for
**relational composition**. For spans `q : A ↛ B` and `r : B ↛ C`, let

```text
P = { (l, m) : Lq × Lr | tq(l) = sr(m) }
e(l, m) = (sq(l), tr(m))
red(q)(a, b) ↔ ∃ l : Lq, sq(l) = a ∧ tq(l) = b.
```

The proposed compatibility theorem, valid for arbitrary spans, is

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
second input. The proposed correction preserves this example and replaces the
unqualified coincidence assertion with equality after reduction.

### Proposed implementation boundary and proof targets

Retain separate operations and equivalences in the future DPGraph increment:

| Construct | Proposed representation or obligation |
| --- | --- |
| Span | A link type `L` with total endpoint functions `L → A`, `L → B`; allow equal endpoints for distinct links |
| Span isomorphism | A head equivalence commuting with both endpoint functions; permit different head universes |
| Indexed family | `I : A → Type` and evaluation `∀ a, I a → B`; arbitrary indices, not finite `Multiset` |
| Conversions | Span to source fibers; family to head `Σ a, I a`; both roundtrips by equivalences preserving endpoints/evaluation |
| Relation reduction | The existential endpoint relation `red`; its span uses the subtype of endpoint pairs |
| Set-valuedness | Jointly injective endpoints iff every source fiber's target evaluation is injective; equivalently isomorphic to the reduced relation span |
| Composition | The explicit type-level pullback `P`, preserving every composable pair; compatibility with family composition indexed by `Σ i : I a, J (f a i)` |
| Laws | Identity head `A` with two identity legs; left/right unit equivalences and associator `((l,m),n) ↔ (l,(m,n))` |
| Inversion | Preserve the head and swap legs; involution, not a claim that an arbitrary span has a categorical inverse |
| Compatibility | Prove reduction/composition equality and the exact injectivity criterion above; keep the two-path counterexample |

Coordinate universe bounds with [#15](https://github.com/kbak/clafer-lean/issues/15):
the family-to-span head lies in the maximum of source and index universes, and
the relation head in the maximum of the endpoint universes. A roundtrip need not
return a head in the original syntactic universe. Track these bounds or explicit
lifts rather than imposing one global universe or a resizing axiom.

Split work into representation/conversions, composition/laws, and reviewed
relation compatibility if useful. A bicategory, a quotient of all spans,
global finiteness and executable object generation are unnecessary for #4.
The meaning of commutativity and inverse predicates in Table 3 remains a
separate review for [#16](https://github.com/kbak/clafer-lean/issues/16); equality
of reduced relations alone does not establish equality or isomorphism of spans.

## Open for later increments

Keep these questions open in #2/#13 before implementing the affected semantics:

- B.2.1 relation/span composition: the [Q1 research above](#span-composition-q1-research-for-4)
  proposes the precise correction; semantic adoption remains subject to review in #4.
- Table 3 versus Figure 21 disjointness arity.
- Figure 21 VC inequality direction.
- Appendix D intersection typo and Appendix E analogous clauses.
- Label/identity choices for gluing.

None is resolved by the definitions or examples in this slice.
