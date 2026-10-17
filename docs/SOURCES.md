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
The accepted [#16](https://github.com/kbak/clafer-lean/issues/16) contracts below
interpret Table 3 commutation and inverse using link-preserving isomorphism;
equality of reduced relations alone does not establish these predicates.

## Open for later increments

Keep these questions open in #2/#13 before implementing the affected semantics:

- Appendix D intersection typo and Appendix E analogous clauses.
- Label/identity choices for gluing.

These remaining questions are not resolved by the span definitions or examples.
Q1, Q7 and Q8 have the adopted corrections recorded here.

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

`FormalCD.Figure21.vocabulary` adds VC through the compatible extension API,
leaving `DPGraph.Predicates` and its Q8 common-target/inverse/multiplicity meanings
unchanged. VC has a real four-arrow arity with all four vertex images. Its
interpretation checks an explicit integer-domain realization and follows the
inclusion/version links for every server link. The theorem
`satisfies_vc_iff_guarded` connects actual formula satisfaction to the selected
integer comparison under inclusion and 1..1 version hypotheses.

The example models in `FormalCD.Figure21.Examples` realize all integers in
`Bool ⊕ Int`. `model_iff` characterizes all twelve declarations for arbitrary
ECU/display integers and a present/absent server link. Greater and equal cases
pass, lower fails only VC, and an absent server passes with a faithful 0..1
multiplicity. These are whole Figure 21b model claims, distinct from the bounded
syntactic self-description theorem and the Figure 21c fragment witnesses.
