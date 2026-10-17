# Sources and open decisions

The [roadmap/source audit (#2)](https://github.com/kbak/clafer-lean/issues/2)
is delivered in [merged #40](https://github.com/kbak/clafer-lean/pull/40).
[Research #41](https://github.com/kbak/clafer-lean/issues/41) owns
the project-critical source and conditional sketch-extension assessment.
The representation assessment for
[design #13](https://github.com/kbak/clafer-lean/issues/13) is present in
[merged #39](https://github.com/kbak/clafer-lean/pull/39); the bounded
self-description and Figure 21b work for #19 is present in
[merged #38](https://github.com/kbak/clafer-lean/pull/38).
The [architecture](ARCHITECTURE.md#roadmap-and-validation-accounting) tracks
delivered increments and later work. The sources below support bounded claims;
they do not constitute a complete audit of the literature.

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
| Definition 6, graphs and graph morphisms | Mathlib `Quiver`, `Quiv`, `Prefunctor`; [representation decision and dependency tradeoff](ARCHITECTURE.md#dp-graph-representation-decision) |
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
span predicates use the selected contracts below in a bounded graph of subsets
and spans; no all-universes SetMap is asserted. The formula-level
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
[full-text rendering](https://www.researchgate.net/publication/220368840_A_Diagrammatic_Logic_for_Object-Oriented_Visual_Modeling).
The upload is headed ACCAT 2006; use its numbered statements rather than
assuming the journal's pagination. The comparison below identifies the relevant
syntax and semantics separately. A downloaded PDF identity for this upload has
not been established; browser section excerpts are distinct from a complete file.
The inspected Diskin, Easterbrook & Dingel (2008) §3 formal-CD/mapping discussion
and §5 association examples support retaining link identity and distinguishing
extensional and navigational views; the full-text identity is recorded below.

The audit limits for the other requested sources are specific:

| Source | Available evidence | Remaining audit |
| --- | --- | --- |
| Diskin & Kadish (2003), *Variable set semantics for keyed generalized sketches*, [DOI 10.1016/S0169-023X(03)00047-8](https://doi.org/10.1016/S0169-023X(03)00047-8), pp. 1–59 | Bibliographic record, abstract and publisher section snippets; inspected scholarly indexes supplied no downloadable copy | Full text not obtained; technical object-identity definitions remain unaudited. The criticality assessment below defers further acquisition unless an active claim needs them and no inspected primary alternative establishes it. The abstract does not select Clafer label identity. |
| Diskin, Kadish, Piessens & Johnson (2000), [Universal Arrow Foundations for Visual Modeling](https://researchers.mq.edu.au/en/publications/universal-arrow-foundations-for-visual-modeling/), pp. 345–360, [DOI 10.1007/3-540-44590-0_30](https://doi.org/10.1007/3-540-44590-0_30) | User-recovered Google Books previews: pp. 345–348, 350, 352–357 and 359, as a two-page PDF and ten page images. Page 345 identifies the title, authors and Diagrams 2000 / LNAI 1889 publication. | Partial source acquired: pp. 349, 351, 358 and 360 are missing. Only the recovered passages are assessed. Further acquisition is conditional on a necessary claim, as recorded below; this is not a complete-paper audit. |

The [bounded library assessment](#lean-library-assessment) identifies reusable
foundations, without establishing a ready-made generalized-sketch dependency or
proving that none exists. The maintained Haskell
compiler has not been used as semantic evidence; later use must pin a commit,
check licensing and distinguish post-2014 constructs. Acquired publications
remain outside the repository.

### Universal Arrow Foundations: partial-source assessment

Google Books previews provided a partial copy of *Universal Arrow Foundations
for Visual Modeling* after author links and other full-text searches did not
yield a complete copy. The available material covers pp. 345–348, 350, 352–357
and 359; pp. 349, 351, 358 and 360 remain unavailable.

The inspected passages inform the comparisons of keys, names and marked arities
below. Detailed provenance and file identities are retained with the research
evidence tracked by [#41](https://github.com/kbak/clafer-lean/issues/41).

| Inspected locator | Finding and applicability boundary |
| --- | --- |
| §2.1, p. 348 | The separating-family example uses an injective tuple map of ordinary functions. It motivates the derived `key_ofFunction_iff` and `key_total_singleValued_iff` in [FunctionalKey.lean](../DPGraph/Predicates/FunctionalKey.lean), whose span formulation explicitly assumes totality and single-valuedness. It does not identify the 2000 set-valued notation with unrestricted SoSyM bags. Table 1 is not among the recovered pages. |
| Predicate-declaration discussion, p. 350 | Bindings are incidence-preserving graph maps. Arity shapes may themselves carry predicate markers, and bindings must preserve them. This supports A2's hierarchical-arity alternative; it is not an identification with the 2008 predicate/dependency category or the delivered ordinary graph arities. |
| §3.1–3.2, pp. 352–353 | Class structure is expressed by outgoing arrows and constraints. Optional/multivalued references use pm-functions with separate single-valuedness and totality markers. The set-valued notation does not provide the multiplicity-bearing links of SoSyM B.1; these examples do not replace the span interpretation. |
| §3.3, pp. 353–354, Figure 1; §3.5, p. 356 | Repeated marriages motivate a key on `(wife, husb, mdate)` rather than the spouses alone. [Examples/FunctionalKey.lean](../DPGraph/Predicates/Examples/FunctionalKey.lean) checks two marriages with equal spouse values and distinct dates: `Remarriage.spouses_not_key` and `Remarriage.spouseDate_key`. This is a finite witness, not an unrestricted marriage identity theorem. Page 354 distinguishes unconstraining names from semantic markers for predefined domains, without choosing Clafer's same-label congruence (Q4). |
| §3.4, pp. 354–355, Figure 2; §3.5, pp. 356–357 | Association-class and qualification visualizations abbreviate explicit sketch structures. This supports preserving underlying bindings rather than inferring identity from a drawing; no general endpoint-based link identification follows. |

The missing pages interrupt Table 1 and the category-theory discussion in §2.3,
and omit part of the conclusion and references. The recovered material does not
complete a universal-arrow foundation or pullback-coherence audit. The broad
expressiveness discussion in §4, p. 357, is not a theorem delivered by this library.

### Additional Diskin sources and applicability

Accessible alternatives support particular questions; they do not establish the
unread 2003 definitions or missing 2000 passages, or settle Clafer's label congruence (Q4).

| Inspected source | Applicable statements and limits |
| --- | --- |
| Wolter & Diskin, *From Indexed to Fibred Semantics — The Generalized Sketch File*, Bergen report 361 (2007), [author-uploaded full-text rendering](https://www.researchgate.net/publication/264922657_From_Indexed_to_Fibred_Semantics_--_The_Generalized_Sketch_File) | §3 Definitions 6–7 use an ordinary signature; Remark 4 explicitly sets aside the dependency-category extension. §4 Definition 11 / Proposition 3 give models into a semantic universe and precomposition reduction. §7 Definitions 18–19 / Proposition 5 give isomorphism-closed meanings and pullback reduction, with canonical coherence at the section opening. §6 treats the graph semantic universe; Remark 13 flags additional identity loops in that construction. This is relevant background for A2, not a proved bridge for the delivered bounded span semantics. Browser-rendered statements were inspected; no complete PDF hash is claimed. |
| Diskin, Dingel & Liang, *Scenario Integration via Higher-Order Graphs*, Queen's report 2006-517, [PDF](https://research.cs.queensu.ca/TechReports/Reports/2006-517.pdf) | §3.1–3.3, printed pp. 9–13, separate names from denotations, specify correspondences by spans, merge by generated equivalence, and lift the construction to graphs. Correspondence discovery is an input, not a derived identity rule. The closing sketch/constraint caveat prevents treating graph merge alone as constrained-model integration. Useful for formulating Q4's alternatives, without selecting a Clafer congruence. Acquired 23-page PDF SHA-256: `7da666e6016f5c1c4d2b261922990ac009bce090d4bff10243e41402b2d704c7`. |
| Diskin, *Mappings, maps, atlases and tables: a formal semantics for associations in UML 2*, [Toronto report CSRG-566](https://ftp.cs.toronto.edu/pub/reports/csrg/566/TR-566-umlAssons.pdf) | The acquired 48-page version credits Diskin alone. Definition 5.1, p. 34, distinguishes role labels from class names and permits repeated classes in a context. Construction 5.2 fixes one common state; Definition 5.4, pp. 35–36, separates mapping schemas from their concrete names. Construction 5.6 separates duplicate elimination from the original mapping. These support explicit role/context data; they do not determine Clafer's gluing congruence or supply general dynamic identity semantics. SHA-256: `837e177f6fd7e7ce8dcdf6565edbe7c7bd9dd670391ddf89311c23030a33391b`. |
| Diskin, Easterbrook & Dingel, *Engineering Associations* (2008), and Diskin's *Model Synchronization* tutorial (2011) | The [Q1 source comparison](#span-composition-q1-research-for-4) records their PDF hashes and locators. They support link identity, association views and span composition; neither selects Clafer's label congruence. Both full PDFs were acquired and their recorded hashes verified. |

## Generalized sketches and model-reduct coherence
`impl~supporting-source-assessment~1`

The [partial-source assessment](#universal-arrow-foundations-partial-source-assessment) and
comparison below support the [research requirement](spec.md#supporting-source-and-coherence-research).
The missing 2003 full text and 2000 page gaps remain unaudited; the bounded
disposition below states when further acquisition is needed.
No mathematical implementation or new theorem is delivered by this comparison.

Covers:
- `req~supporting-source-research~1`

| Concern | SoSyM B.4–B.5 and the delivered API | Diskin & Wolter author upload |
| --- | --- | --- |
| Signature and consequences | Definition 7 / `Signature`: symbols with graph arities; Definition 9 / `DPGraph`: a declaration set without inference closure. | §4.1 Definition 4.1 uses a predicate/dependency category and an arity functor. Definition 4.5 (Inf) closes declarations: a dependency `r : Q → P` carries `P(d)` to `Q(α(r) ; d)`. |
| Models and satisfaction | A map from the carrier to fixed `Ω`; `Interpretation.meaning` selects satisfying arity maps. | §4.2 Definitions 4.7/4.9 use instances typed into a carrier and satisfaction by pullback. Meanings are isomorphism-closed and consistent with dependency pullbacks. |
| Restriction and its laws | B.5 Theorem 3 / `isModel_reduct` restricts by precomposition. `reduct_id` and `reduct_comp` prove equalities of model values. | §4.3 Lemma 4.13, Proposition 4.14 and Corollary 4.15 use chosen pullbacks, coherent natural isomorphisms and isomorphism-closed meanings. Theorem 4.19 packages the sketch instance pseudofunctor. |

The comparison does not identify these two model representations. A future
typed-instance bridge needs an explicit construction and correspondence theorem
with its size and semantic hypotheses. The existing precomposition laws require
neither pullback choices nor extra axioms on meanings; they do not establish
strict equality for arbitrary chosen pullback reducts. For a dependency-enriched
extension, separately specify dependency direction, arity functoriality,
declaration closure, interpretation consistency and the intended coherence laws.
That extension and its proofs require a new authorized scope.
The 2007 report above supplies an ordinary-signature comparison; generalized
sketch references do not all assume the 2008 dependency-enriched signature.

### Arity alternatives and semantic compatibility

| Representation | Obligations and present need |
| --- | --- |
| Ordinary graph arities | Delivered `Signature.arity` and `Formula.binding` retain incidence, isolated vertices and repeated arguments. `Hom.preserves` preserves declared formulas. This suffices for the selected SoSyM vocabulary and existing FormalCD construction; its explicit disciplines remain separate. |
| Marker-bearing arities, recovered 2000 p. 350 | A binding must preserve marks on the arity as well as its graph. A possible design keeps the ordinary signature and separately specifies prerequisite formulas on each arity, with translated prerequisites required in the carrier's declarations. Translation stability, closure and sound interpretation of those prerequisites would need proofs. No such extension is currently required or implemented. |
| Predicate/dependency category, 2008 §4.1–3 | Also specify dependency composition, an arity functor, inference closure and interpretation consistency. Typed pullback instances add isomorphism closure and coherence. This is a possible future framework, not an equivalence already established for the other two presentations. |

In the possible prerequisite design, let `Req(p)` be formulas on `arity p`.
For `P(d)` declared in `S`, require `ψ.translate d` in `S.declarations` for
each `ψ ∈ Req(P)`. Soundness would additionally require every
`d ∈ I.meaning P` to satisfy those `ψ`. Merely adding declarations does not
establish that entailment. This is a proposed encoding obligation, not a new
Lean declaration or a correspondence theorem attributed to the papers.

There is a concrete compatibility boundary: the 2008 author's Example 4.8
requires total single-valued legs for its binary key. Our `Key` permits bags;
`bagKey_key` and `bagKey_not_setValued`, together with
`singleValued_setValued`, rule out importing that prerequisite for every key
argument. The [ordinary-function special case](spec.md#ordinary-key-correspondence-and-repeated-marriages)
preserves that meaning and states the additional hypotheses explicitly (#44).
Precomposition reduct laws remain as
proved; any future inferred declarations need their own soundness argument.

### Project-critical source disposition

Research follows the claims needed by an increment, using accessible primary
alternatives when they establish the exact point. Further recovery of the
2003 paper and missing 2000 pages is deferred unless such a claim cannot be
supported otherwise. These texts are not treated as read or as replaced in full.

| Needed claim or decision | Evidence and remaining owner |
| --- | --- |
| Ordinary-key correspondence | SoSyM B.1 and the delivered `Key` supply the semantics of the derived [#44 result](spec.md#ordinary-key-correspondence-and-repeated-marriages); the recovered p. 348 example and the restricted 2008 key explain the comparison. Its proof and finite marriage witness need no further acquisition. |
| Resolved identities versus repeated names | SoSyM §6.2.4 explicitly adds indices for uniqueness; recovered p. 354 and CSRG-566 Definition 5.1 support separating names and roles. #3/#22 can use the reviewed resolved-input contract. No general theory of object persistence is needed for that contract. |
| Which MCS roles denote one class or map | SoSyM §6.2.5 requires a graph/DP morphism. CSRG-566 supplies useful role/context distinctions, not the missing Clafer congruence. #20/#23 still need an explicit label policy, incidence proof and positive/negative identification witnesses before gluing. This is a design decision, not a requirement to obtain one particular paper. |
| Closure or typed-instance coherence | The 2007 report and inspected 2008 definitions establish the relevant alternative frameworks. The present ordinary API needs neither extension. Reopen this design only for a concrete increment requiring marked arities or a typed-instance bridge, with size and interpretation hypotheses stated. |

The research assessment can be reviewed without completing the bibliography.
Revisit a deferred source when a named active claim depends on an unaudited
definition; record that claim, attempted alternatives and its issue owner.

### Lean library assessment

The bounded search inspected the full `Mathlib/` tree at the pin above for
`sketch`, `generalized/generalised sketch` and `institution`, followed relevant
category-theory modules, and checked GitHub repository queries
`sketch language:Lean` and `"generalized sketches"`, web/Reservoir discovery,
and the candidate README/manifests below. Keyword hits included proof outlines
and *Sketches of an Elephant* citations; they did not identify a sketch API.
Search results and compatibility are separate: none of the external candidates
was built against this project's Lean/Mathlib pins or added as a dependency.

| Inspected source | Relevant content and suitability limit |
| --- | --- |
| [Pinned Mathlib](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679) | `CategoryTheory/Limits/Shapes/Pullback/`, `FiberedCategory/`, `Grothendieck.lean` and `Bicategory/Functor/Pseudofunctor.lean` provide foundations. They do not supply the selected predicate/dependency signature, closure and satisfaction package together; those obligations remain to be specified. |
| [sinhp/LeanFibredCategories at a58604a](https://github.com/sinhp/LeanFibredCategories/tree/a58604a389544523aa171daf890386fb8317568b) | Fibers, Cartesian lifts and Grothendieck examples; README describes upstreaming foundations to Mathlib. Manifest pins Lean v4.4.0-rc1. Relevant background, without the required generalized-sketch layer. |
| [jacobneu/GeneralizedAlgebra at d2f4029](https://github.com/jacobneu/GeneralizedAlgebra/tree/d2f402944052f7d93d2f600ab1131c13d92d4351) | Generalized algebraic-theory signatures and generated algebra descriptions; Lean v4.13.0. A different specification language, without an inspected DP-sketch interpretation/reduct adapter. |
| [b-mehta/topos at c9032b1](https://github.com/b-mehta/topos/tree/c9032b11789e36038bc841a1e2b486972421b983) | Topos/pullback foundations; `leanpkg.toml` pins Lean 3.24.0. This is not a directly compatible Lean 4 dependency or a delivered diagram-predicate package. |

Retain the existing Mathlib dependency and ordinary DPGraph signature. Before
adopting an external library, check its license, exact API, maintained toolchain
compatibility and a compiling adapter with meaningful satisfaction/closure laws.
The scoped negative search cannot rule out other libraries or later versions.

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
The accepted [#16](https://github.com/kbak/clafer-lean/issues/16) contracts below
interpret Table 3 commutation and inverse using link-preserving isomorphism;
equality of reduced relations alone does not establish these predicates.

## Audit coverage and remaining decisions
`impl~formalization-roadmap-sources~1`

The table extends the exact DPGraph mapping above through the two upper layers.
Future representations and obligations are proposals for their owning increments,
not additional promises of implemented mathematics. Detailed delivered
declarations remain in [DPGraph trace artifacts](dpgraph-trace.md) and
[FormalCD trace artifacts](formalcd-trace.md).
The [supporting-source audit limits](#supporting-sources-and-licenses) and
[Q1–Q8 dispositions](#question-dispositions-and-validation-tasks) supply the
remaining research obligations for this source-map artifact.

Covers:
- `req~formalization-roadmap~1`

| Construct and exact SoSyM locator | Representation and obligations | Status / owner |
| --- | --- | --- |
| Predicate catalogue: B.3 Table 3, §6.1.1–2, A.1 Table 2 | Separate typed arities and span meanings; invariance, multiplicity and empty/repeated-family boundaries; Q8 correction | Selected vocabulary proved in #16 / [#34](https://github.com/kbak/clafer-lean/pull/34); unsupported predicates deferred |
| Formal CD: §6.1.1–3, Figure 21a–b | Raw/bundled CD, registry, naming and effective defaults; name-preserving morphisms are an explicit library specialization | #17 / [#35](https://github.com/kbak/clafer-lean/pull/35); whole Figure 21b/guarded VC models in #19 / [#38](https://github.com/kbak/clafer-lean/pull/38) |
| Metamodel: §6.1.3, Figure 21c | Compatible vocabulary, nd/ad disciplines, full graph bindings; separate syntactic self-description from semantic instantiation | #18 / [#36](https://github.com/kbak/clafer-lean/pull/36), bounded self-description #19 / #38; literal-key/total-args limits below |
| Syntax and individual Shapes: §5.2 Figure 16, §6.2.2 Figure 22, Appendix C | Resolved deep AST and individual Shapes; IDs, containment, inheritance, references, abstractness, root/domains and finite traversal | [#3](https://github.com/kbak/clafer-lean/issues/3), [implementation and proofs](clafer-trace.md) |
| MCS: §6.2.3 Figure 23, Appendix E Tables 5–8 | Proposed typed role graph plus explicit invariants; expand analogous clauses, optional roles, naming and cojoining before selecting proofs | [#20](https://github.com/kbak/clafer-lean/issues/20), Q2/Q4 pending |
| Constraints: Appendix D.1–D.4 | Proposed resolved expression syntax and checked typing; binders, navigation and set operations; meaning remains distinct from syntax | [#21](https://github.com/kbak/clafer-lean/issues/21), Q3 pending |
| Compile: §6.2.4 | Proposed finite resolved-AST-to-MCS transformation; termination, freshness, incidence, cojoining, kind/name preservation under explicit input well-formedness | [#22](https://github.com/kbak/clafer-lean/issues/22), depends on #3/#20/#21 |
| Gluing: §6.2.5 | Proposed role-label graph map and declaration image; endpoint congruence, label DP-morphism, then separate CD well-formedness | [#23](https://github.com/kbak/clafer-lean/issues/23), Q4 pending; generic pushout results alone do not prove this |
| Integration: Appendix F and selected earlier figures | Proposed finite AST/MCS/CD examples exercising compile/glue statements; enumerate unsupported constructs | [#24](https://github.com/kbak/clafer-lean/issues/24), after #22/#23 |

### Question dispositions and validation tasks

Q1–Q8 name source questions; A1–A9 in the architecture name design areas.
An accepted correction is a bounded decision, not permission to fill unrelated
source gaps. Keep the original issue discussions as the decision history.

| Question | Disposition and alternatives | Validation and owner |
| --- | --- | --- |
| Q1 — B.2.1 composition | Accepted: retain pullback links and prove equality after reduction. The unqualified relational-span isomorphism is false. | #4 / #32 delivered `Span.red_comp`, the exact endpoint-injectivity criterion and two-path/parallel-link counterexamples; [source comparison](#span-composition-q1-research-for-4). No remaining #4 implementation task. |
| Q2 — Appendix E analogous clauses | Unresolved: implementing only printed representatives would omit the prose obligations. No expansion is selected here. | #20 must enumerate source/target, reference, parent and super-role variants from Tables 5–8, record which endpoints may be undefined and each guard, visually cross-check Figure 23, and attach positive/negative incidence and optional-role witnesses to the accepted checklist. |
| Q3 — Appendix D notation | Unresolved: D.4.2 prints set difference in the intersection equation; some type-rule notation is inconsistent. Following the named intersection and D.1–D.3 is a proposal, not an accepted semantic equation. | #21 must locate each discrepant rule, record alternatives and obtain a reviewed disposition before semantics. Validate common-element versus difference examples, empty operands, and accepted/rejected typing/navigation/binder cases; no theorem of constraint meaning is claimed here. |
| Q4 — labels and identity | Unresolved for Clafer: §6.2.4 indices and §6.2.5 label identification require a precise congruence. Existing FormalCD names are metadata, not identity. | #20/#22/#23 must distinguish source names, generated IDs, class identities and endpoint-qualified map labels; show repeated parent/isA names do not merge incompatible endpoints, define the intended same-label identifications, and prove label incidence before declaration preservation. Use the inspected primary evidence above; relying on a particular unread 2003 definition would require obtaining it or an adequate primary alternative. |
| Q5 — self-description | Bounded syntactic result delivered. Semantic self-instantiation, a universal every-CD-is-an-instance claim and a universe fixpoint remain outside scope. | #19 / #38 proves representation/well-formedness in explicit `CDOver` parameters. Preserve the ordered/isolated/repeated binding witnesses and literal key/total-args limits below. Any stronger result needs a new scope and explicit realizability hypotheses. |
| Q6 — acquisition and visual completeness | Partial audit: 2003 full text missing; twelve recovered 2000 pages inspected with four page gaps. The criticality assessment above records alternate evidence and conditional acquisition. Figures 21 and 23 were visually inspected in planning; that does not complete the later construct-by-construct inventory. | [#41](https://github.com/kbak/clafer-lean/issues/41) owns the bounded assessment and reviewed source disposition; #3/#20/#24 must pair the relevant Figure 16/22/23 and Appendix F inventory with text, labels, incidence and examples. Reopen acquisition for a named necessary claim lacking adequate primary evidence; never mark unread definitions audited. |
| Q7 — VC order and guard | Accepted: display.version ≥ server.version, guarded by a nonempty server fiber. Contrary adjacent p.17 prose is the discrepancy. | #19 / #38 delivers the [guarded correspondence and whole models](#figure-21b-and-the-accepted-q7-correction): greater/equal pass, lower fails VC, absent server passes. No remaining implementation task for this correction. |
| Q8 — disjointness shape | Accepted: §6.1.2/Figure 21 common-target maps with nonoverlapping images; Table 3's common-source shape is erroneous. | #16 / #34 delivers typed arity, interpretation and overlap/repeated-nonempty-binding failures. [Contract below](#predicate-contracts-and-the-accepted-q8-correction); no second predicate or source-object inequality. |

The roadmap can be accepted with deferred work explicitly assigned; it cannot
claim that those tasks or missing-source research are completed. #40 delivers
#2's source/design cross-check; #41 retains the unfinished research. The architecture records
the existing #13 assessment and the separate proof-status boundaries.

## Predicate contracts and the accepted Q8 correction

Issue [#16](https://github.com/kbak/clafer-lean/issues/16) selects Table 3
(printed p.12), §6.1.1–2 and Figure 21 (pp.17–18), Appendix A.1 (p.28),
and B.1–3 (pp.28–30) of the hashed preprint above. The maintainer accepted
§6.1.2/Figure 21's common-target disjointness meaning: distinct family members
have nonoverlapping target images. Table 3's common-source shape and its
source-inequality condition are erroneous. In particular, two inclusions
containing the same ambient object overlap even at equal source values;
repeated nonempty bindings fail disjointness. No common-source alternative is
part of this vocabulary.

The selected interpretation of Table 3 inverse and equality uses B.1 Definition 2
link-renaming equivalence, B.2.2 leg-swapping inversion and B.2.1 pullback
composition. Equality is triangular commutation up to span isomorphism.
The Q1 correction continues to distinguish this from equality after reduction.
Key compares finite tuples of bags using target-preserving source-fiber
equivalences, including multiplicity; Figure 21c permits a bag-valued argument.
Cover and corrected disjointness compare reachable target values and require
no set-valuedness. Zero-member key requires a subsingleton source, cover an
empty target, and disjointness is vacuous; the central arity vertex remains.

B.1.4/Theorem 2 gives set-valuedness as joint endpoint injectivity. A.1,
Table 2 and §6.1.1 give totality and single-valuedness as source surjectivity
and injectivity respectively. Single-valuedness excludes duplicate copies.
Literal inclusion (A.1, §6.1.1) additionally fixes the underlying ambient
object and supplies exactly one link per source. An arbitrary injection,
or a permutation moving an object, is insufficient.

Table 3 mult-trg/mult-src and B.1 indexed families count actual outgoing/incoming
links. Finite bounds are embeddings to/from `Fin`; an unbounded upper limit
adds no finiteness condition. Under set-valuedness, fiber evaluation is a
bijection onto distinct reachable values. Source bounds are target bounds
of the inverse. These are bounded semantic graphs over subsets of a specified
ambient type, with an explicit link universe, not an all-universes SetMap.
No automatic set-valued default is imposed.

The generic built-in vocabulary excludes VC, arbitrary path equations beyond
the triangle, and FormalCD/Clafer-specific predicates. FormalCD supplies the
separate corrected VC extension described below.


| Source locator | Concrete declarations (namespace `DPGraph.Predicates`) |
| --- | --- |
| Table 3 inv/= (p.12); B.1 Definition 2, B.2.1–2 (pp.28–30) | `Inverse`, `Commutation`, `inverse_symmetry`, `inverse_iff`, `commutation_iff`; `Span.Iso.inverse`, `.comp` |
| Table 3 key (p.12); Figure 21c (p.17) | `BagEquiv`, `Key`, `BagEquiv.transport`, `key_iff`, `key_zero` |
| Derived from B.1 Definitions 1–5 / Theorems 1–2 (pp.28–29), Table 3 key and Figure 21c; comparison with Diskin et al. (2000) §2.1 p.348 | `Span.ofFunction`, `bagEquiv_ofFunction_iff`, `key_ofFunction_iff`, `targetValue`, `targetValue_eq_of_source`, `red_iff_targetValue_eq`, `functionalSpanIso`, `key_total_singleValued_iff`, `tuple_injective_zero_iff` |
| Finite witness motivated by Diskin et al. (2000) §3.3 pp.353–354 / Figure 1 and §3.5 p.356 | `Examples.Remarriage.same_spouses_different_dates`, `spouses_not_key`, `spouseDate_key` |
| Table 3 cover (p.12); §6.1.2 (p.18) | `Cover`, `cover_iff`, `cover_zero` |
| §6.1.2/Figure 21 (pp.17–18), accepted Q8 correction | `Disjoint`, `disjoint_iff`, `disjoint_zero` |
| A.1 (p.28), Table 2 (p.11), §6.1.1 (pp.17–18), B.1.4/Theorem 2 (p.29) | `SetValued`, `Total`, `SingleValued`, `Inclusion`; fiber characterizations and `inclusion_subset`, `inclusion_identity` |
| Table 3 mult-trg/mult-src (p.12), B.1 indexed families (pp.28–29) | `InRange`, `TargetMultiplicity`, `SourceMultiplicity`, `distinctValuesEquiv`, multiplicity invariance/duality/distinct-value theorems |
| B.4 Definitions 6–9 and B.5 (p.30) | `signature`, `semanticGraph`, `interpretation`; generic `Interpretation.Satisfies` and `.reduct` |

The [trace artifacts](dpgraph-trace.md) link implementations and checked
acceptance witnesses to the current mathematical requirements. Transport and
invariance results are derived library statements for these selected contracts,
not additional claims attributed verbatim to the paper.

## FormalCD structure and selected morphisms

Issue [#17](https://github.com/kbak/clafer-lean/issues/17) adopts the first
FormalCD increment from the same hashed SoSyM preprint, §6.1.1–3 and Figure
21b–c (pp.17–18), over B.4 Definitions 6–10. The correspondence is:

| Source / selected contract | FormalCD declarations |
| --- | --- |
| §6.1.1 classes, maps, inclusion identities/names | `Raw.className`, `Raw.mapName`, `MapMode`, `RawOver.WellFormed.inclusion_name` |
| §6.1.2 typed predicates; B.4 Definitions 6–9 | Existing `DPGraph`, `Formula`, `Predicates.signature`; `arrowBinding`, `inclusionFormula`, `setValuedFormula` |
| §6.1.3 predefined naming discipline | `Registry`, `PredefinedKind`, `Raw.predefined`, `RawOver.WellFormed.predefined_name`, `.user_name`, `.unique_predefined` |
| §6.1.1–3 defaults; Figure 21c explicit bag-valued args | `Raw.mode`, `RawOver.WellFormed.inclusion_decl`, `.ordinary_decl`; `Examples.no_bag_default`, `.explicit_bag_wellFormed` |
| Adopted name/annotation/mode-preserving specialization of B.4 Definition 10 | `Hom`, `.id`, `.comp`, `.ext`, `.comp_assoc`, `.id_comp`, `.comp_id`, `.toDPHom` |
| Existing abstract B.5 reduct after forgetting | `Hom.reduct`, `.reduct_id`, `.reduct_comp`; `Examples.restrictedModel` |

The extra metadata equalities are an accepted library contract, not a verbatim
theorem about arbitrary DP morphisms. Class identities are vertices and map
identities are arrows; strings need not be globally injective. Different inclusion
arrows may both be named isA. A selected predefined identifier has one realization
at most, but no predefined entry is compulsory. Registry kinds distinguish the
singleton vocabulary from primitive domains without implementing their object sets.

WellFormed requires default membership in the authoritative effective declaration
set; it adds no generic DPGraph defaults or inference closure. Inclusion and bag
are separate modes. Inclusion's semantic consequences come from its already delivered
literal span meaning. User declarations are retained, including explicit bag
setValued constraints. Structural validity alone implies neither satisfaction nor
model existence; an explicit interpretation and a model proof remain necessary.
This increment reuses the supported predicate vocabulary, preserving Q1 and Q8.
The metamodel extension below adds nd/ad and Figure 21c construction; a general
constraint language and complete primitive/object-diagram semantics remain open.
Figure 21b supplies a bounded integer realization for its separate VC extension.

The [FormalCD trace artifacts](formalcd-trace.md) link these independently
formalized contracts and acceptance witnesses to their Lean declarations.


## Figure 21c metamodel

Issue [#18](https://github.com/kbak/clafer-lean/issues/18) independently formalizes
§6.1.1–3, Figure 21c on printed p.17, the explanation on p.19 and B.4 Definition 8
on p.30 of the 34-page preprint with SHA-256
`56b1c18e74807fb7646c0e89cb2fc306f4178affb41fee52fcebde09b031b2fb`.
The figure and prose jointly determine the following inventory; no publication
images or text are vendored. Lean names below are in `FormalCD.Metamodel`.

The eleven distinct `Node` identities are Classifier, Class, Map, Incl, Predef,
SING, Dom, String, PredefStr, Formula and Signature. `SingletonClass.sing` describes
the modeled predefined class Sing, and `SingletonObject.star` its object; neither
is the metaclass `Node.sing`. The underlined SING node is the singleton annotation
in the metamodel's own small metadata registry. Concrete assignments to String,
PredefStr and Signature belong to interpretation context. Merely naming a node
Class or Signature supplies no universal collection of Lean types or signatures.

| Edge identity | Source → target | Displayed name and effective declarations |
| --- | --- | --- |
| predefStrIn | PredefStr → String | isA; inclusion |
| classIn | Class → Classifier | isA; inclusion |
| mapIn | Map → Classifier | isA; inclusion |
| predefIn | Predef → Class | isA; inclusion |
| singIn | SING → Predef | isA; inclusion |
| domIn | Dom → Predef | isA; inclusion |
| inclIn | Incl → Map | isA; inclusion |
| name | Classifier → String | name; ordinary setValued, total, singleValued |
| predefName | Predef → PredefStr | name; ordinary setValued, total, singleValued |
| so | Map → Class | so; ordinary setValued, total, singleValued |
| ta | Map → Class | ta; ordinary setValued, total, singleValued |
| args | Formula → Map | args; explicit bag, total; no setValued default |
| pred | Formula → Signature | pred; ordinary setValued, total, singleValued |

`classifiers` binds cover/disjoint to (classIn,mapIn), and `predefinedKinds` binds
them to (singIn,domIn), with the accepted common-target Q8 meaning. `keyBinding`
binds the literal key to (args,pred). The 30 `Declaration` cases enumerate seven
inclusions, five set defaults, six total and five single-valued annotations,
four cover/disjoint annotations, and key/nd/ad. Inclusion's existing meaning
already implies a total identity-valued function, without extra synthetic tokens.

The drawing omits dashed attachments for nd/ad. The following are **inferred
bindings**, justified by the selected constraint, not claims of hidden incidence:

- `nameShape` uses the nine left-hand nodes and exactly the seven inclusions and
  two name arrows. Canonical/user naming, optional predefined identity/kinds,
  inclusion naming and restriction along Predef→Class→Classifier and
  PredefStr→String need these nodes/maps. It omits so/ta, args and pred.
- `arityShape` has Formula, Signature, Map and Class and exactly args, pred, so, ta.
  Selecting a symbol, indexing its arguments and checking both endpoints requires
  this incidence. Extra arity vertices and occurrence labels are explicitly
  supplied data; they are not invented arrows in Figure 21c.

`NameContext` decodes names/identifiers and embeds strings into a bounded U.
`NameDiscipline` checks actual name links, reserved strings, realized optional
identifiers and kinds, unique identifier realization, isA names and the commuting
name-restriction square as a span isomorphism. It permits repeated classifier
names. The generic built-in inclusion declarations separately require identity
on the underlying ambient objects.

`ArityContext` supplies an independently bounded signature σ, graph G and explicit
embeddings of symbols, vertices and total arrows into U. `ArityDescriptor` provides
optional candidates for actual formula objects and optional occurrence indices.
`ArityDiscipline` checks domain sets, so/ta endpoints, a valid complete candidate,
a bijection from each actual args fiber to all arity arrows, the argument values,
and the selected pred value. Missing/invalid descriptions are rejected. Candidate
validity itself is equivalent to the existing typed Formula representation, by
`Candidate.formulaEquiv`; it is not supplied as a validity assumption by Context.
Every arity vertex remains in the candidate, including isolated ones. The graph
alone cannot recover this descriptor; interpretation is explicitly parameterized
by it. The bounded span links use `Type (max z w)` for `U : Type z`, with semantic
arrows in `Type (max z w + 1)`; signature/carrier universes remain independent.

### Literal key, total args and the #19 obligation

B.4 Definition 8 defines a formula as a symbol and a **full graph morphism**.
Its arrow-list shorthand explicitly assumes finitely many arrows and no isolated
nodes. The generic library does not impose those hypotheses. The p.19 prose uses
indexed families for arguments, while the accepted Table 3 key compares bags by
fiber equivalence. These are different observations of a formula. The accepted
#18 contract preserves both; it does not reinterpret the generic key as indexed
identity or quotient existing formulas. Symbol plus all vertex/arrow actions
characterizes formula equality; bag-key satisfaction is an additional condition.

| Checked witness | Literal key | Total args | Exact conclusion |
| --- | --- | --- | --- |
| `ordered` pair | fails | holds | Same symbol and equivalent arrow bags, different positions/full bindings |
| `isolated` pair | fails | fails | Same symbol and empty arrow projection, different isolated vertex images |
| `repeated` singleton formula | holds | holds | Two distinct occurrences have the same arrow value; not set-valued |
| `fragmentModel` | holds | holds | Actual extended-interpretation model of ad/key/total with repeated args |
| `nameDiagram false/true` | not a formula/key fragment | not an args fragment | nd holds for user/canonical predefined naming respectively |

The ordered/isolated span witnesses are projections of the displayed full
bindings. They are not asserted to be full Figure 21c models. `fragmentModel`
checks an explicit declaration fragment; the separate name witnesses check nd.
The metamodel `diagram` is syntactically well-formed, which does not assert its
own semantic satisfaction. No whole-metamodel or universal every-CD-is-an-instance
theorem is claimed.

The total bullet on args excludes an empty outgoing fiber for a realized formula.
Zero-arrow arities (with isolated vertices) remain valid generic formulas but
cannot satisfy that totality with their complete indexed argument representation.
This restriction is retained rather than erasing the figure annotation.

The bounded result in [SelfDescription.lean](../FormalCD/SelfDescription.lean)
reuses `Metamodel.diagram`, its well-formedness and inventory in the small
`CDOver` family with the concrete nd/ad vocabulary and SING registry. Its full
formula representation is the existing `Candidate.formulaEquiv`. This states
that MCD is representable as a formal CD; it claims no semantic self-instantiation,
universal realizability or self-containing universe. Literal key and total args
remain separate instance conditions, with the projection failures above intact.

## Figure 21b and the accepted Q7 correction

Issue [#19](https://github.com/kbak/clafer-lean/issues/19) selects the corrected
inequality **display.version ≥ server.version**. Figure 8 line 9 (p.8), its
accompanying §4.2.3 discussion and Appendix F (p.34) support this direction.
Section 4.3 (p.9) supplies the configuration context.
The paragraph accompanying Figure 8 describes the display's version as not lower
than the server's. Figure 21a (p.17) explicitly guards the comparison by
`self.server->notEmpty()`: a display without a server satisfies VC vacuously.
Equality passes. The nearby p.17 prose instead says the ECU's version is not
lower than the display's; that discrepancy is retained as a source error, not
an alternative interpretation. The rendering and original publication remain
reference inputs, not repository content.

The Figure 21b construction follows §6.1.1–3 and the exact twelve-formula list
on p.19, with B.4 Definitions 7–9 supplying signature/formula/DP-graph structure:

| Identity | Incidence | Name / declarations |
| --- | --- | --- |
| i1 | ECU → Comp | isA; inclusion |
| i2 | Display → Comp | isA; inclusion |
| server | Display → ECU | server; 0..1, setValued |
| display | ECU → Display | display; 0..5, setValued |
| version | Comp → Int | version; 1..1, setValued |

Together with disjoint(i1,i2), cover(i1,i2), inverse(server,display) and
VC(server,i1,i2,version), these are twelve effective formulas, proved distinct.
Class identities are exactly Comp, ECU, Display and Int. Int has the canonical
primitive registry annotation; the example selects no Sing class. The registry
API still permits optional entries. The italic Comp label adds no separate
constraint: cover/disjointness impose the partition. The bullet/open arrowheads
on version are accounted for by 1..1; server's open head is accounted for by
0..1 and does not imply totality. Display remains a general map bounded by 0..5.

`FormalCD.Telematics.vocabulary` adds VC through the compatible extension API,
leaving `DPGraph.Predicates` and its Q8 common-target/inverse/multiplicity meanings
unchanged. VC has a real four-arrow arity with all four vertex images. Its
interpretation checks an explicit integer-domain realization and follows the
inclusion/version links for every server link. The theorem
`satisfies_vc_iff_guarded` connects actual formula satisfaction to the selected
integer comparison under inclusion and 1..1 version hypotheses.

The example models in `FormalCD.Telematics.Examples` realize all integers in
`Bool ⊕ Int`. `model_iff` characterizes all twelve declarations for arbitrary
ECU/display integers and a present/absent server link. Greater and equal cases
pass, lower fails only VC, and an absent server passes with a faithful 0..1
multiplicity. These are whole Figure 21b model claims, distinct from the bounded
syntactic self-description theorem and the Figure 21c fragment witnesses.

## Resolved 2014 Clafer and individual Shapes

Issue [#3](https://github.com/kbak/clafer-lean/issues/3) implements the selected
constructs from the same 34-page preprint (SHA-256
`56b1c18e74807fb7646c0e89cb2fc306f4178affb41fee52fcebde09b031b2fb`).
Figures 16, 22 and 23 were visually cross-checked against their accompanying
text. The formalization is independent; no publication figures/text or compiler
implementation are vendored, and the Haskell compiler is not semantic evidence.

| Source locator | Selected contract and Lean correspondence |
| --- | --- |
| §5.3.1–3/Table 4 (p.13), Figure 22 (p.20) | `Reference`, `Kind`: basic, reference set and reference bag; resolved target IDs |
| §5.3.4–5/§5.4 (p.14), §6.2.2 (p.20) | `Origin`, `Declaration`, `Tree`, `AST.WellFormed`: distinguished root, selected int/string/bool domains, nested and top-level abstract declarations, deep containment |
| §5.5 (pp.14–16), Figure 18 | `Kind.CanExtend`, `inheritance_kind`, `inheritance_parent`: no basic-over-reference or bag-over-set; equal parents when super is parented; local inclusion roles |
| Appendix C/Figure 27 (pp.30–31) | `Multiplicity`, `GroupCard`, `GroupMultiplicity`, `Defaults`: authored/effective intervals, unbounded upper limit, xor/or/mux/opt, explicit child overrides, inherited group provenance |
| §6.2.2/Figure 22 (p.20), D.2 boundary (p.31) | `ConstraintBoundary`, `Binder`: resolved context, repeated scope/domain occurrences and separate binder identities; full expressions deferred |
| §5.2/Figure 16/Table 4 (pp.12–13), §6.2.3/Figure 23 (pp.20–21) | `Roles.Class`, `Roles.Arrow`, `Shape`, local `Shape.diagram`: typed optional roles, inverse/triangle/multiplicity/set/key declarations using FormalCD and DPGraph |
| §5.5/Figure 18, Table 6's local inclusion endpoints (p.33) | `Shape.SharedClass`, `Shape.Inclusions`, `Shape.OptionalInclusions`: head inclusion and source/target inclusions where both endpoints exist; full cojoining deferred |
| §5.4 and §6.2.4 traversal (pp.14,21) | `Tree.fold`, `Tree.child_smaller`, `AST.every_entry_indexed`, `parent_wellFounded`: derived finite representation/termination basis; no compilation correctness claim |

The resolved boundary accepts IDs, not textual resolution requests. `Defaults`
checks explicit values and the effective values supplied by an elaborator.
Clafer multiplicity sugar is already numeric at this boundary: `?` is 0..1,
`+` is 1..*, and `*` is 0..*. Authored values record whether an interval was
explicit, without preserving the original token spelling.
Group keywords retain their provenance through inheritance so their child-default
policy remains inspectable. Numeric group bounds alone do not induce keyword
optional defaults. Effective bounds must be valid; root/domain metadata is
separate from user defaulting. Acyclic inheritance uses an explicit rank witness
as a selected well-formed-input condition, not a theorem attributed verbatim to
Figure 22. Reference cycles are permitted and do not enter containment recursion.

**Accepted top-level abstract correction.** Section 5.3.4, printed p.14, says
that a parentless abstract's CS excludes the *head* class. Section 6.2.3, p.20,
says the head is always present, and Figure 23 gives the head-class role total
multiplicity. The maintainer's accepted #3 interpretation retains the head and
removes the source and parent-dependent maps. A top-level abstract reference
therefore has head, target and dereference, with no head map, parent map or
target map. The basic-source-present statement in Table 7 (p.33) is read with
this top-level abstract exception (and its separate synthetic-root rule).
Source/target inclusion roles are likewise omitted when either endpoint is
absent; head inclusion remains. This is an explicit correction, not a claim that
the conflicting sentence says the same thing. The publication and historical
accepted snapshots remain unchanged.

Full MCS invariants/analogous equations (#20), expressions and Appendix D's Q3
(#21), compilation (#22), label congruence/gluing (#23) and integration (#24)
remain separate. No new interpretation of those unresolved equations is adopted.
