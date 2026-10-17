# Architecture

The [canonical intent](intent.md) selects three layers. Spans and their mapping
operations, DPGraph syntax, its fixed-signature category and abstract model
restriction, the selected concrete predicate meanings, and FormalCD
structure/morphisms, signature support, the Figure 21c metamodel, bounded syntactic
self-description and Figure 21b with its corrected VC interpretation are delivered.
Clafer adds resolved deep syntax, a constraint boundary and individual Shapes.
The [roadmap (#2)](https://github.com/kbak/clafer-lean/issues/2) is delivered in
[merged #40](https://github.com/kbak/clafer-lean/pull/40); its later increments
retain their own tickets. [Research #41](https://github.com/kbak/clafer-lean/issues/41)
owns the project-critical source and sketch-extension assessment.
[Design #13](https://github.com/kbak/clafer-lean/issues/13)
records the representation assessment delivered in
[merged #39](https://github.com/kbak/clafer-lean/pull/39).
The repository `kbak/clafer-lean` contains one Lake package named `clafer`.
Its public libraries and module roots are siblings: `DPGraph`, `FormalCD`,
`Clafer`. Imports flow `Clafer -> FormalCD -> DPGraph -> Mathlib`.

| Layer | Responsibility and dependencies | Status |
| --- | --- | --- |
| DPGraph | Spans, indexed mappings, graphs, typed predicates, a fixed-signature category and abstract/concrete interpretation; Mathlib only | B.1 Definitions 1–5/Theorems 1–2, B.2.1–2 with the Q1 correction, B.4 Definitions 6–10 and the abstract B.5 reduct and selected Table 3/A.1 meanings in [DPGraph](../DPGraph.lean) |
| FormalCD | Class diagrams, naming/default obligations and name-preserving morphisms; builds on DPGraph | [Core API](../FormalCD.lean) delivered; Figure 21c and disciplines, bounded syntactic self-description, and Figure 21b/VC delivered |
| Clafer | Structural 2014 Clafer application over the foundations: resolved syntax, Shapes/MCS, eventually Compile/gluing | [Resolved syntax and individual Shapes](../Clafer.lean) delivered; name resolution, full MCS and constraint meaning remain separate |

[Signature.lean](../DPGraph/Signature.lean) uses
`CategoryTheory.Quiv.{arrowUniverse, vertexUniverse}` for arity graphs;
[Formula.lean](../DPGraph/Formula.lean) binds each symbol by a `Prefunctor` from
that arity. [Basic.lean](../DPGraph/Basic.lean) pairs a carrier with a `Set` of
formulas. [Morphism.lean](../DPGraph/Morphism.lean) supplies
preservation proofs, identity, composition, extensionality and laws. The signature
is fixed throughout these operations; arities and each carrier can occupy distinct
vertex/arrow universes. [Examples.lean](../DPGraph/Examples.lean) uses finite types locally.
`import DPGraph` exposes the generic foundation without importing examples or
upper layers. `DPGraph.Examples`, `DPGraph.SemanticsExamples`,
`DPGraph.Span.Examples` and `DPGraph.Predicates.Examples` are built and checked
separately. Library globs and the shared check's discovered module inventory
cover all project modules,
including future helpers that no entrypoint imports. That same inventory drives
explicit builds, `leanchecker` and the generated `import all` axiom audit.
Dependency checks reject reverse imports through root/helper modules and reject
Lean sources outside the owned roots (apart from validation harnesses in `tests/`).

A carrier is a directed multigraph: `x ⟶ y` is a type of arrows and need not
have an identity or composition. In the paper's presentation, total edges are
`Σ x y : G, (x ⟶ y)` with source and target given by projections. Conversely,
the fibers of an edge set over its source/target functions give these hom types.
The category structure on *bundled graphs* supplies morphisms between graphs;
it does not give categorical operations to a carrier's arrows.

A formula binding records vertex images as well as arrow images. Consequently,
isolated arity vertices and two distinct arity arrows with equal images survive
the representation; an arrow list alone would lose that information. Declarations
have no global finiteness, decidable equality or inference-closure requirement.
No second graph API is introduced.

Translation postcomposes a formula's binding with a graph map, retaining its
symbol. A DP morphism carries a proof that every translated source declaration
belongs to the target's declaration set. Identity and composition preserve that
condition; their laws and the finite positive/negative witnesses are linked in
the [trace artifacts](dpgraph-trace.md). [Category.lean](../DPGraph/Category.lean)
equips DP-graphs at fixed signature and carrier universes with a Mathlib category
using exactly these morphisms.

[Semantics.lean](../DPGraph/Semantics.lean) takes a semantic graph `Ω` and a set
of satisfying maps `arity p → Ω` for every symbol `p`. A candidate model
`m : S.carrier → Ω` satisfies `φ` precisely when `φ.binding ; m` belongs to that
set. It is a model when all declarations are satisfied. Associativity gives
`sat m (translate φ F) ↔ sat (F ; m) φ`. Declaration preservation then gives
`Model T → Model S` for `F : S → T`; restriction is precomposition, with identity
and reversed-order composition laws. This is the abstract argument of B.5
Theorem 3. It needs no closure or invariance axiom on the predicate meanings.
The formula-level equivalence does not reflect whole-model satisfaction: the
target may have additional declarations.

The [supporting-source comparison](SOURCES.md#generalized-sketches-and-model-reduct-coherence)
separates these laws from pullback restriction of typed instances. Retain the
ordinary signature and fixed semantic graph. Dependency-enriched sketches and a
typed-instance correspondence would need separately specified closure,
consistency, size and coherence obligations; the bounded library assessment
does not justify adding another dependency. The
[inspected 2000 passages](SOURCES.md#universal-arrow-foundations-partial-source-assessment)
support a bounded comparison of keys, names and hierarchical arities. The
[criticality assessment](SOURCES.md#project-critical-source-disposition) uses
accessible primary alternatives and makes further acquisition conditional on
a necessary claim. Keep ordinary graph arities; importing the 2008 key's
functional prerequisites would conflict with the delivered bag-sensitive key.
Clafer label identity still needs the #20/#23 congruence and incidence decision.

Semantic vertex/arrow universes are independent of all syntax universes, and
`Hom` and reduct still support source and target carriers in different universes.
The concrete semantic graph has vertices `Set U` in `Type u` for
`U : Type u`, and spans between their subtype carriers as arrows. Links in
`Type (max u w)` give arrows in `Type (max u w + 1)`. The shared ambient type
lets two subsets contain the same object; subtype membership does not change
its identity. The generic interface remains unrestricted and imposes no resizing
or all-universes SetMap. [SemanticsExamples.lean](../DPGraph/SemanticsExamples.lean) interprets a
small signature in both a small graph and a graph with vertices/arrows in
`Type 1`, and proves positive and negative satisfaction cases.

[Pushout/Basic.lean](../DPGraph/Pushout/Basic.lean) puts the union of translated
component declarations on a supplied carrier cocone point. Its two injections
preserve declarations by construction, and the supplied graph equation gives
the DP-graph cocone. `CompatibleModels` records equality of component reducts.

[Pushout/Universal.lean](../DPGraph/Pushout/Universal.lean) independently imports
the basic data and lifts a supplied carrier `IsColimit` to the DP-graph cocone
at fixed carrier universes. For any target DP cocone, its carrier mediator
preserves declarations: each declaration comes from one component, and translation
composition plus that component's factorization equation reduces preservation
to its DP map. Carrier factorization and uniqueness lift through `Hom.ext`.

[Pushout/Models.lean](../DPGraph/Pushout/Models.lean) independently imports the
same data and derives `Pushout.modelEquiv` from the supplied carrier colimit.
Its forward map is exactly the two reducts. Compatibility gives a cocone into the
semantic graph; its mediator satisfies the declaration union by satisfaction
under translation and the two component model proofs. Carrier factorization
recovers both component models, and uniqueness recovers the original model.
`modelEquiv_fst` and `modelEquiv_snd` expose the forward projection equations.
Here `Ω : Quiv.{v,u}` shares the fixed carrier universes so that the supplied
universal property applies. This restriction is local to the equivalence;
interpretations, reducts and compatible-model data retain their independent
semantic universes. Both results are derived over SoSyM B.4 Definitions 9–10
and abstract B.5 Theorem 3. They add no predicate-meaning or amalgamation axiom,
assert no global pushout existence, and supply no concrete CD or Clafer gluing.


## DP-graph representation decision

Keep Mathlib `Quiver`, `Prefunctor` and bundled `Quiv` for SoSyM B.4
Definitions 6–10. The [design assessment (#13)](https://github.com/kbak/clafer-lean/issues/13)
records the acceptance evidence and dependency-cost comparison. The delivered
[core requirements](spec.md#graphs-signatures-and-typed-declarations) and
[trace artifacts](dpgraph-trace.md#core-representation) state the checked contract.

| Choice | Reason and alternative |
| --- | --- |
| Endpoint-indexed arrows | A `Quiver` permits loops and parallel arrows. An explicit vertex/edge/source/target record is mathematically equivalent: take the total edge type `Σ x y, (x ⟶ y)` in one direction and the fiber `{e // source e = x ∧ target e = y}` in the other. Reusing `Prefunctor` avoids a second incidence-preserving map API. The correspondence is explanatory here; no new Lean equivalence theorem is claimed. |
| Graph-valued arities and full bindings | `Signature.arity` and `Formula.binding` retain every arity vertex and arrow. An untyped arrow list loses endpoint checking and isolated vertices; requiring injective bindings loses repeated arguments. |
| Sets of declarations | `Set (Formula σ G)` matches Definition 9 without global finiteness or decidable equality. Finite lists, `Finset` and executable maps belong at later algorithmic boundaries. |
| Fixed-signature morphisms | `Hom` combines a graph map with declaration preservation. Neither injectivity, reflection of extra target declarations nor predicate-dependency closure is required. The dependency-enriched sketches in the secondary source are a separate possible extension. |
| Separate interpretations | `Interpretation` selects meanings in an explicit semantic graph. Satisfaction and the contravariant reduct are derived from composition; the syntax does not prescribe a solver, primitive domains or a graph of all types. |
| Mathlib graph category | `Quiv` reuses the category of graphs and its existing colimit interfaces. A local bundle with only Quiver/Prefunctor imports could reduce the syntax-only import closure, but would require adapters for the delivered carrier cocones and conditional pushout/model-amalgamation API. |

The independent universes in `Signature.{s,va,ua}` bound symbols, arity arrows
and arity vertices. `DPGraph.{s,va,ua,v,u}` adds carrier arrow and vertex bounds;
`Interpretation` adds independent semantic bounds. `Hom` supports different
source and target bounds, while each category fixes its carrier bounds. A
dependent binding's arrow action has endpoints determined by its vertex action:
`Hom.ext_of_obj_map` therefore uses the endpoint transports of `Prefunctor.ext`,
and `Hom.ext` removes only the proof-field distinction. Translation and morphism
laws reuse `Prefunctor.comp_id`, `id_comp` and `comp_assoc`. These obligations are
exercised by the existing [structural](../DPGraph/Examples.lean) and
[semantic](../DPGraph/SemanticsExamples.lean) witnesses, including noninjective
arrow maps, repeated arguments, isolated vertices, failed declaration
preservation and larger semantic universes.

### Dependency-cost decision

Retain the current `Mathlib.CategoryTheory.Category.Quiv` import and both
dependency pins. That module includes category, adjunction and path-category
machinery beyond the smaller `Mathlib.Combinatorics.Quiver.Prefunctor` import.
The comparison in #13 measures the exact imported environments, cached import
processes and rebuilding each named Mathlib module with cached prerequisites.
Retained and fresh full validation runs assess a fresh project build with pinned
dependencies already provisioned against the baseline scope's 900-second test
limit; CI separately has a 20-minute job limit. This evidence supports the
existing design in that environment. It does not measure rebuilding the whole
dependency closure from source or a machine with cold filesystem caches, nor
guarantee the same timing on another runner. The unchanged check retains its
source-build fallback when the optional Mathlib cache is unavailable.

The larger import closure alone does not justify a local wrapper: the public
foundation already uses graph-category colimits, so such a change needs an
end-to-end comparison including adapters, build/kernel checks and public API
compatibility. Reassess if supported-runner validation approaches its budget or
a separately scoped syntax-only consumer needs smaller imports. Measurements,
commands, source identities and review results belong in #13 and its PR/evidence,
rather than in the maintained mathematical contract.

The original representation criteria are met by the delivered core and its
witnesses; the final assessment is recorded in merged #39. Later source
questions and Clafer meanings remain on the
[roadmap (#2)](https://github.com/kbak/clafer-lean/issues/2). Bounded syntactic
self-description and the telematics example are delivered in
[#19 / #38](https://github.com/kbak/clafer-lean/pull/38), with the limitations
described below; neither semantic self-instantiation nor Clafer gluing follows.

## Spans and indexed mappings

[Span.Basic](../DPGraph/Span/Basic.lean) defines `Span A B` with a head `Link`
and total `source`/`target` legs. Their universes `u`, `v`, `w` are independent.
`Span.Iso` is an equivalence of heads preserving both endpoints; parallel links
remain distinct. Inversion swaps the legs and is involutive. It supplies no
categorical inverse for arbitrary spans.

[IndexedFamily](../DPGraph/Span/IndexedFamily.lean) uses `Index : A → Type w`
and `eval : ∀ a, Index a → B`. A span gives source fibers in `Type w`; a family
gives a sigma head in `Type (max u w)`. The roundtrips use head or fiberwise
equivalences, including across universes. Family reduction and span reduction
agree by endpoint membership (B.1 Theorem 1). No resizing or finite multiset
representation is needed.

[Composition](../DPGraph/Span/Composition.lean) uses all pairs `(l,m)` with
`target l = source m`, in `Type (max w w')`, with the outer legs. Family
composition uses all indices `Σ i, J (eval a i)` and corresponds by equivalence.
The identity has head `A`; units and reassociation of three links are canonical
span isomorphisms, not strict equality of differently represented heads.

[Relation](../DPGraph/Span/Relation.lean) reduces a span to existence of a link
with given endpoints. A relation span's head is the subtype of satisfying pairs,
in `Type (max u v)`. Joint endpoint injectivity, fiberwise evaluation injectivity
and isomorphism to the reduced relation span are equivalent (B.1 Theorem 2).

The adopted Q1 law is `red(q.comp r) = relationComp q.red r.red`. Its canonical
endpoint map is always surjective and yields an isomorphism exactly when it is
injective. For relational inputs this is equivalent to at most one intermediate
object per outer pair. The first relation being single-valued, or the converse
of the second being single-valued, suffices without totality. The
[examples](../DPGraph/Span/Examples.lean) retain two paths through distinct
intermediates even when the second relation is single-valued, and retain parallel
input links even when the intermediate is unique. They also exercise empty heads
and the universe joins.

## Concrete predicates

[Predicates.Signature](../DPGraph/Predicates/Signature.lean) declares the vocabulary
and real arity quivers, independently of meanings. The two-arrow inverse shape
has opposite arrows; commutation has a triangle; key has a common source;
cover and disjointness have a common target. Family arities are parameterized by
n, retain a central vertex at n=0, and allow repeated graph-map bindings.
Unary predicates and range bounds are explicit symbols. There is no automatic
set-valued declaration.

[Predicates.Meaning](../DPGraph/Predicates/Meaning.lean) compares inverse and
composite spans by inhabited `Span.Iso`, preserving multiplicity. Keys compare
source fibers by target-preserving equivalence, so different bags with the same
support remain distinguishable. Cover and disjointness intentionally inspect
reachable target values. Q8 selects §6.1.2/Figure 21's common-target disjoint
images and records Table 3's shape as erroneous in the [source map](SOURCES.md).

Set-valuedness is joint endpoint injectivity; totality and single-valuedness are
source surjectivity and injectivity. Inclusion requires a bijective source and
identical underlying ambient objects at both ends. It implies subset membership
and a unique identity-valued link per source; a moving permutation fails.
Multiplicities bound actual link fibers by embeddings from/to finite types.
The unbounded branch has no local finiteness requirement. For set-valued spans,
fiber evaluation gives an equivalence onto distinct reachable values, proving
agreement of the two counts. Inversion exchanges outgoing and incoming bounds.
Each predicate is invariant under endpoint-preserving link isomorphisms,
including relabelings into different universes. These statements do not relabel
the endpoints themselves.

[Predicates.Interpretation](../DPGraph/Predicates/Interpretation.lean) connects every
symbol to the existing `Interpretation` interface. Satisfaction, translation and
model restriction retain the generic definitions and proofs. Concrete witnesses
in [Predicates.Examples](../DPGraph/Predicates/Examples.lean) include a nonidentity
map preserving declarations, its restricted model and a rejected overlapping
binding. Zero-member key means a subsingleton source, cover an empty target,
and disjointness is vacuous, while each central arity vertex survives.

The generic built-in vocabulary excludes VC and FormalCD/Clafer-specific
predicates; the telematics example below supplies VC as a FormalCD extension.
Arbitrary path equations beyond the triangle, all-universes SetMap and computable
finite presentations remain future work. The source map records the accepted
Q1, Q7 and Q8 corrections and the remaining open questions.

## Formal class diagrams

[FormalCD.Basic](../FormalCD/Basic.lean) layers metadata on the existing
`DPGraph Predicates.signature`. `Raw` retains the carrier and a single effective
declaration set, plus `className`, `mapName`, `predefined` and `mode`. The shared
`Registry` maps stable identifiers to canonical names and singleton/primitive
kinds. `Raw.WellFormed` checks canonical predefined names, exclusion of reserved
names for user classes, uniqueness of each realized predefined identifier, the
isA name for inclusions, and the required inclusion/setValued declarations.
`CD` bundles raw data with that proof. Failed obligations remain expressible on
raw data; all data projections remain inspectable.

Strings do not define vertex or arrow equality. User classes can share names;
distinct inclusion arrows share isA. Registry entries are optional, and no global
name injectivity or acyclic inheritance condition is imposed. The registry's
identifier, rather than the spelling of a name, determines predefined identity.
Typed `Formula` bindings continue to enforce arity/incidence, including repeated
arguments and isolated vertices. The metamodel validates separately supplied candidate data and relates it to
these existing typed bindings; it does not replace their representation.

Declarations are already effective: ordinary arrows require setValued membership,
inclusions require inclusion membership, and explicit bags add no default.
Authors may explicitly declare a bag set-valued. No constructor drops declarations
or silently creates another set. Inclusion's object-preserving span meaning and
the Q1/Q8 contracts remain in DPGraph unchanged. These syntactic obligations do
not assert existence of a model or satisfaction by a proposed interpretation map.
Primitive annotations do not constrain that map to concrete Int/String/Bool or
singleton domains; complete primitive and object-diagram semantics remain later work.

[FormalCD.Morphism](../FormalCD/Morphism.lean) defines `Hom` as an existing
`DPGraph.Hom` plus equalities preserving every metadata field at mapped identities.
The registry and supported signature are shared; source and target carry independent
well-formedness proofs. Equality of optional annotations preserves user/predefined
status as well as each identifier, and equality of modes distinguishes all three
cases. Carrier maps may identify user vertices/arrows, and target declarations
may be stronger. The chosen name-preserving specialization is a library contract
over B.4 Definition 10; it is not the paper's generic morphism definition.
Identity and composition close each metadata obligation; extensionality and laws
reuse DPGraph. Forgetting is `Hom.toDPHom`, with identity/composition equations.

[FormalCD.Semantics](../FormalCD/Semantics.lean) simply applies the existing
contravariant reduct to that projection, retaining an explicit interpretation and
independent semantic universes. [Structural witnesses](../FormalCD/Examples.lean)
and [concrete models](../FormalCD/SemanticsExamples.lean) are separate from the
public entrypoint. Their declarations and obligations are linked in
[formalcd-trace.md](formalcd-trace.md). Metamodel-specific nd/ad predicates use
the compatible extension below; Figure 21b adds a separate VC extension. A general
constraint language and semantic self-instantiation remain outside this slice.


## Figure 21c and compatible vocabularies

[FormalCD.Signature](../FormalCD/Signature.lean) contains `Vocabulary`: an explicit
built-in symbol embedding and two inverse arity Prefunctors. Its signature can
have independent symbol/vertex/arrow universes. The disjoint `extend` constructor
joins the built-in symbol universe 0 with the extra symbol universe and uses
small arities; the general interface imposes no such bound. Formula embedding
precomposes with the arity projection and commutes with carrier translation.
`RawOver`, `CDOver` and `HomOver` use that vocabulary. The original `Raw`/`CD`
structures wrap the built-in specialization and retain its public projections;
`CD.generalize` forgets only this wrapper. Both morphism APIs use the same DPGraph
laws, declarations, registry obligations and interpretations.

[The metamodel](../FormalCD/Metamodel/Basic.lean) is a small typed CD with a single
effective declaration set, whose source inventory is in [SOURCES](SOURCES.md#figure-21c-metamodel).
The two extra symbols use explicit naming and incidence subgraphs. The metadata
registry marks the underlined SING metaclass as singleton; assignments of concrete
String/PredefStr/Signature domains belong to the interpretation context. Model
metaclass identities, modeled classes and their objects remain ordinary separate
data; no syntax node denotes the collection of all Lean types.

`Candidate` retains a symbol, every vertex image and an indexed map of total
arity arrows to total carrier arrows. Its `Valid` proposition checks both endpoint
equations. Valid candidates are equivalent to the existing `DPGraph.Formula`.
An `ArityDescriptor` adds optional candidates and optional index data to an actual
span diagram. `ArityDiscipline` checks candidate validity, complete bijective
fiber indexing, actual argument values, selected symbols and source/target maps.
`NameDiscipline` checks actual names, optional registry identities/kinds and the
predefined naming square by a span isomorphism. `Context` supplies data, never a
validity assumption. The interpretation is over `semanticGraph U`, with the
existing link universe `max z w` for `U : Type z`; candidate data retains the
independent signature/carrier universes and their ordinary joins. Encodings into
U are explicit embeddings; no resizing or all-universes semantic graph is used.

The repeated-argument acceptance model concerns the ad/key/total fragment. Name
witnesses separately satisfy nd. Construction well-formedness, fragment satisfaction
and whole-metamodel satisfaction are distinct. The literal key compares unindexed
bags, so it can identify projections of distinct positional bindings; arrow-only
projection also loses isolated vertices. Total args excludes empty argument fibers
although those formulas are legal in DPGraph. These facts bound self-description
to an explicit syntactic representation/well-formedness result with signature,
registry and universes. They do not prove that every CD is a semantic instance
of the printed metamodel, nor that a model is its own
semantic instance.


## Bounded self-description and Figure 21b

[SelfDescription.lean](../FormalCD/SelfDescription.lean) reuses `Metamodel.diagram`
in `CDOver.{0,0,0,0,0,0}` with `Metamodel.vocabulary` (built-ins plus nd/ad) and
`Metamodel.registry` (SING). `bounded_self_description` combines exact raw-data
representation, existing well-formedness and the eleven-node/thirteen-arrow
inventory. `metamodelFormulaRepresentation` specializes `Candidate.formulaEquiv`;
its roundtrip retains all vertex images and indexed arrows. This is the same
CDOver family used by the built-in specialization and Figure 21b, with different
explicit vocabulary/registry parameters. No metamodel-instance result is inferred,
so no literal-key/totality hypotheses are silently discharged by this theorem.

[Telematics/Basic.lean](../FormalCD/Telematics/Basic.lean) formalizes the telematics
example (§2) as the four-node, five-arrow diagram in Figure 21b, with Int registry
metadata and twelve distinct effective formulas.
[VC.lean](../FormalCD/Telematics/VC.lean) adds one symbol through `Vocabulary.extend`.
Its four-arrow arity retains both inheritance paths to Comp and version to Int.
`IntegerRealization` embeds every integer in an ambient U and supplies a decoder
with a roundtrip law. VC requires the Int vertex to equal this image and compares
the decoded targets reached through actual inclusion and version links for each
actual server link. `builtins_unchanged` preserves the existing span meanings.

For `U : Type u`, semantic vertices are subsets of U and links live in
`Type (max u w)`; semantic arrows inhabit `Type (max u w + 1)`. Syntax remains
small; neither DPGraph nor the interpretation acquires a finiteness assumption.
Under inclusion and 1..1(version), `satisfies_vc_iff_guarded` derives the functional
integer comparison. 0..1(server) gives single-valuedness without totality;
0..5(display) bounds the inverse's outgoing links. Equality passes and an empty
server fiber contributes no comparison.

[Examples.lean](../FormalCD/Telematics/Examples.lean), checked separately from public
imports, uses `Bool ⊕ Int`: two component objects, disjoint ECU/Display singleton
subsets, all integers, and an optional single server link with its actual inverse.
The parameterized `model_iff` proves whole Figure 21b satisfaction exactly when
the optional link respects the corrected order. The lower-version counterexample
satisfies all eleven other declarations; the unserved model keeps the 0..1 bound
while failing server totality. These are models of Figure 21b, not Figure 21c.

## Roadmap and validation accounting
`impl~formalization-roadmap-architecture~1`

The [Project](https://github.com/users/kbak/projects/2), its existing
[three phase milestones](https://github.com/kbak/clafer-lean/milestones?state=all),
and [#2](https://github.com/kbak/clafer-lean/issues/2) record the backlog.
[Merged #40](https://github.com/kbak/clafer-lean/pull/40) delivers #2's
documentation close-out; [#41](https://github.com/kbak/clafer-lean/issues/41)
owns the deferred source research. The
milestones organize increments; completion of the research issue does not
require implementation of every milestone. Earlier issue discussion remains the
decision history. The table records delivered merge references rather than
inferring live Project status from the presence of code.
The [nine design areas](#nine-architectural-decision-areas) and
[proof-status accounting](#theorem-statements-and-proof-status) below supply
the alternatives and validation boundaries for this roadmap artifact.

Covers:
- `req~formalization-roadmap~1`

| Phase | Dependency-ordered increments | Delivery boundary |
| --- | --- | --- |
| 1 — reusable DP-graphs | [#13](https://github.com/kbak/clafer-lean/issues/13) representation; [#14](https://github.com/kbak/clafer-lean/issues/14) → [#15](https://github.com/kbak/clafer-lean/issues/15), with derived [#28](https://github.com/kbak/clafer-lean/issues/28)/[#30](https://github.com/kbak/clafer-lean/issues/30); [#4](https://github.com/kbak/clafer-lean/issues/4) → [#16](https://github.com/kbak/clafer-lean/issues/16) | #14/#25, #15/#27, #28/#29, #4/#32, #30/#33 and #16/#34 delivered. #13's final representation/dependency assessment is in #39. Generic DPGraph remains independently importable. |
| 2 — reusable formal CDs | #16 → [#17](https://github.com/kbak/clafer-lean/issues/17) → [#18](https://github.com/kbak/clafer-lean/issues/18) → [#19](https://github.com/kbak/clafer-lean/issues/19) | #17/#35, #18/#36 and #19/#38 delivered: structure, morphisms, compatible vocabulary, Figure 21c, bounded syntactic self-description and Figure 21b/VC. Semantic self-instantiation remains outside scope. |
| 3 — structural 2014 Clafer | [#3](https://github.com/kbak/clafer-lean/issues/3) → [#20](https://github.com/kbak/clafer-lean/issues/20) and [#21](https://github.com/kbak/clafer-lean/issues/21) → [#22](https://github.com/kbak/clafer-lean/issues/22)/[#23](https://github.com/kbak/clafer-lean/issues/23) → [#24](https://github.com/kbak/clafer-lean/issues/24) | Resolved syntax, the binder/context boundary and individual Shapes are implemented for #3. Full MCS invariants, expression typing and label identity precede Compile/gluing; integration requires both. Planning tickets alone authorize no further implementations. |

### Nine architectural decision areas

This cross-check consolidates the brief's representation and later-layer concerns
with the rationale in #13. A1–A9 are design areas, separate from the source
questions Q1–Q8 in [SOURCES](SOURCES.md#question-dispositions-and-validation-tasks).
“Proposed” marks a later design to validate within its own authorized increment.

| Area | Choice and alternatives | Evidence and remaining validation |
| --- | --- | --- |
| A1 — graph representation and Mathlib reuse | Retain `Quiver`/`Prefunctor`/`Quiv` over a second vertex/edge record or a category imposed on carrier arrows. Total edges are a dependent sum; loops and parallel arrows survive. | #14/#25 exercises isolated vertices and noninjective maps. #13/#39 assesses the wider Quiv imports; [cost decision](#dependency-cost-decision) states measurement limits and reassessment triggers. No new wrapper or dependency change is proposed. |
| A2 — signatures, arities and declarations | Graph-valued arities and full dependent bindings, with declaration sets. Untyped arrow lists lose incidence/isolated vertices; injective bindings lose repetitions. Dependency-enriched sketches are a separate extension. | #14/#25 proves translation and declaration preservation; #18/#36 checks full-binding/argument-projection limits. [#41](https://github.com/kbak/clafer-lean/issues/41) owns the [bounded library/closure/reduct assessment](SOURCES.md#generalized-sketches-and-model-reduct-coherence) against Diskin & Wolter §4.1–3. A future dependency-enriched extension needs its own scope and compatibility evidence. |
| A3 — morphisms and categorical structure | Fixed-signature DP category; preservation permits identification and extra target declarations. Requiring embeddings or reflection would change Definition 10. FormalCD specializes this with metadata preservation. | #15/#27 and #17/#35 supply category/morphism laws; #28/#29 and #30/#33 are conditional derived results. #23 must prove the concrete label map preserves declarations and separately establish CD well-formedness; generic pushout existence or arbitrary-model reflection does not follow. |
| A4 — spans, identities and universes | Retain explicit links/fiber indices and pullback composition. Relations discard multiplicity; a graph of all Lean types needs an unjustified size principle. Use independent universes and explicit bounded ambient objects. | #4/#32 proves roundtrips, units/associativity up to isomorphism and corrected Q1; #16/#34 checks shared-object inclusion and bag counts. #20/#23 must preserve these identities across role encodings without resizing or collapsing links. |
| A5 — predicate syntax and meaning | Separate symbols/arities from interpretations and model maps. Generic syntax imposes no default set-valuedness; FormalCD supplies effective defaults. Primitive domains and VC require explicit interpretations. | #15/#27 proves reduct by precomposition; #16/#34 interprets the selected vocabulary and Q8; #19/#38 handles VC separately. #21 must distinguish typing from satisfaction, resolve Q3 before semantic equations and state each domain/interpretation assumption. |
| A6 — formal-CD metamodel and self-description | Reuse `CDOver` with explicit vocabulary/registry, nd/ad meanings and full-binding correspondence. Reject a Lean universe fixpoint and an inference from syntactic well-formedness to semantic self-instantiation. | #18/#36 and #19/#38 deliver the bounded result and Figure 21 example. Ordered/isolated bindings expose bag-key and total-args restrictions. Stronger realizability/self-instantiation is deferred and would require new accepted hypotheses and examples. |
| A7 — Clafer syntax, MCS and finiteness | Deep resolved AST and typed individual role graphs, with raw data plus explicit well-formedness propositions. A shallow Lean encoding would obscure source syntax/compilation; globally finite DPGraphs would restrict reusable semantics. Use finite data only at the executable boundary. | #3 accounts for Figure 16/22, Appendix C and the accepted top-level abstract correction in the [Clafer source map](SOURCES.md#resolved-2014-clafer-and-individual-shapes); #20 must enumerate Appendix E's implicit/optional-role clauses (Q2). Validate finite presentations against the generic graph API, with positive and malformed role examples, before promising a compiler. |
| A8 — names, generated identity, Compile and gluing | Proposed separation of names and generated IDs, followed by an explicit endpoint-compatible label congruence and declaration image. Textual names alone can collapse unrelated parent/isA arrows; replacing labels by arbitrary injective IDs would omit intended gluing. The congruence remains unresolved. | #20/#22/#23 own Q4: repeated-name and intended-identification cases, freshness and termination, incidence/cojoining and kind/name preservation. Review label equality before defining the quotient/map. A DP-morphism proof and a CD-well-formedness proof are separate targets. |
| A9 — constraints and end-to-end claims | Proposed resolved typed expressions, with syntax/typing first and semantic translation only after source dispositions. Neither a production parser nor the current Haskell compiler defines the 2014 meaning. Structural Compile/glue correctness is distinct from full constraint-semantic preservation. | #21 resolves Appendix D discrepancies (Q3) and checks binders/navigation/types; #22/#23 state explicit well-formed-input assumptions; #24 enumerates supported Appendix F examples and unsupported constructs. Full constraint preservation remains deferred until both source and target meanings are specified. |

### Theorem statements and proof status

This research increment advertises no new Lean theorem. The existing named
[DPGraph](dpgraph-trace.md) and [FormalCD](formalcd-trace.md) proof artifacts
link to the actual declarations; the statements below bound what may be inferred.

| Statement | Status and scope |
| --- | --- |
| Translation preserves identity/composition; declaration-preserving maps form a fixed-signature category. | Proved in #14/#25 and #15/#27, using `Formula.translate_id`, `translate_comp` and `Hom` laws; B.4 Definitions 6–10. |
| A model of T restricts to a model of S along F : S → T, contravariantly. | Proved as `Interpretation.isModel_reduct` and `reduct` laws (#15/#27); abstract B.5 Theorem 3. No whole-model reflection is claimed. |
| Restriction along F is injective if J.comp F = id T, and surjective if F.comp J = id S. | Derived and proved in `ModelTransport` (#28/#29), not verbatim paper theorems. |
| A supplied carrier pushout lifts to a DP pushout; its models correspond to compatible component models. | Derived and proved as `Pushout.isColimit`/`modelEquiv` (#30/#33). The equivalence fixes semantic and carrier universes together; no global existence or concrete Clafer gluing theorem. |
| Span reduction commutes with composition; isomorphism to the relational composite requires injective composite endpoint pairing. | Proved corrected Q1 statement (#4/#32), with counterexamples to the unqualified source assertion. |
| The metamodel has a bounded syntactic CD representation; guarded VC agrees with the selected integer comparison and the example models. | Proved as `bounded_self_description`, `satisfies_vc_iff_guarded` and `Examples.model_iff` (#19/#38); preserve their vocabulary/registry, integer-domain, inclusion and version hypotheses. No semantic self-instantiation. |
| A well-formed resolved AST compiles to an MCS satisfying the explicitly enumerated invariants. | Proposed #22 target, after #3/#20/#21 establish input typing and Q2/Q3/Q4 dispositions. Termination and freshness are additional obligations; no implementation yet. |
| The role-label map is a DP morphism, and the glued structure is a well-formed formal CD. | Proposed separate #23 targets after label congruence/incidence is settled. Neither follows solely from declaration-image construction. |
| Compilation/gluing preserves all constraint meanings, or every CD semantically instantiates its metamodel. | Deferred; no accepted general statement or proof. Source resolution and explicit realizability/semantic hypotheses would be needed first. |

#40 delivers #2's cross-check and documentation close-out. Missing-source
limits and conditional acquisition remain recorded under Q6 / #41; acceptance of the roadmap does not
complete that research or later implementation tickets. The pinned build,
kernel/axiom/layer checks and IntentBond validate the candidate and existing
proofs; they do not certify the source interpretation or complete a deferred
task. Exit 4 leaves semantic review pending. Each continuing issue requires its
own accepted deliverables and any required documentation merge before closure.

## Resolved syntax and individual Shapes

[Clafer.Syntax](../Clafer/Syntax.lean) uses mutually inductive `Tree`/`Forest` containment with a list of roots and
`Declaration` records, with `DeclId` edges for inheritance and references.
`Origin` distinguishes synthetic root, primitive domains and users. A distinguished
root ID is checked against the forest; parent links and depths come from traversal.
Top-level abstracts occupy other forest roots. `Tree.branch` accepts ordinary
finite lists of children; `Forest.ofList` constructs the mutual forest. Both folds
and traversal use primitive structural recursors. They are kernel-reducible;
`noncomputable` suppresses native code generation for these recursors, avoiding
compiler-generated partial helpers. This supplies a mathematical termination
basis, with native compilation remaining on #22. No choice or termination axiom
is added. Strings are metadata and may repeat.
A rank witness in `AST.WellFormed` excludes inheritance cycles, while containment
has structural recursion and a depth measure. No finite-carrier restriction is
added to DPGraph or FormalCD.

Input retains authored and effective multiplicities/abstractness. `Defaults`
checks the Appendix C boundary: ordinary 1..1 bounds, keyword-induced optional
children, explicit overrides, and inherited/default group bounds. An inherited
group retains its keyword provenance. This validates supplied resolved data;
it is not an elaborator. Primitive domains select identities/names, not sets of
runtime values. `Tree.fold`, `Tree.child_smaller`, `AST.every_entry_indexed` and
`AST.WellFormed.parent_wellFounded` provide a finite traversal/termination basis.
References and super IDs are never followed by the containment fold.

[Clafer.Context](../Clafer/Context.lean) is the dependency boundary for #21.
`ConstraintBoundary` stores a context ID, occurrence-indexed referenced-scope
list, and binder IDs/names/domain occurrences. Distinct positions can reference
the same declaration; no deduplication occurs. A later expression module can
associate a body with a boundary ID and validate its occurrences. Neither expression
syntax nor Appendix D's disputed equations are selected here.

[Clafer.Shape](../Clafer/Shape.lean) uses subtypes of finite class/map role enums
and the existing `Quiver`/`Quiv` API. Hom types contain both endpoint equations;
incorrect incidence cannot inhabit an arrow type. Kind and parent presence
control role availability. `Located.shape` decodes only that local inventory;
it does not recursively compile a model. `Shape.Realization` binds a role graph
to an existing FormalCD; `Shape.Inclusions` supplies inclusion-mode arrows for
all shared class roles when a super is selected. Full MCS equations remain #20.

[Local diagrams](../Clafer/Shape/Diagram.lean) instantiate the delivered predicate
vocabulary: inverse head/parent, triangle commutation, multiplicities, ordinary
set-valued defaults and the set-reference key. Source/target names in this local
CD are role labels; global naming/cojoining/gluing is deliberately left to
#20/#22/#23. These are syntactically well-formed CDs, with no assertion of a model.
The [accepted source correction](SOURCES.md#resolved-2014-clafer-and-individual-shapes)
keeps the head of every top-level abstract and removes its parent-dependent roles.
The [Clafer trace artifacts](clafer-trace.md) link these boundaries to checked
positive and rejected examples.

## Proposed bounded structural comparison boundary

The [#49 contract and compiler matrix](resolved-ir-comparison.md) are a
documentation proposal under #48. They recommend a separate `clafer-compare`
companion with a pinned dependency on `clafer`, an effective-core adapter and
finite candidates retaining shared object identity and bag link occurrences.
JSON/Alloy pairing requires a same-generation state receipt; JSON alone loses
authored/default provenance and backend state. Current `AST.WellFormed` and
local `Shape.diagram` proofs do not supply the proposed satisfaction bridge.

The contract assigns missing whole-model structural interpretation, finite
representation/checker correctness and the effective-core bridge to #50, with
explicit interfaces from #20/#22/#23. It preserves #21 and the existing roadmap
dependencies until a structural-only disposition is reviewed. Unrelated deferred
language features need not block an accepted structural slice. The detailed
[location and decision proposal](resolved-ir-comparison.md#decisions-location-proposal-and-prerequisites)
identifies the companion paths, possible reusable `Clafer/Semantics/` additions
and the alternative in-project verification extension. Each requires its
implementing requirements and architecture review first. This proposal leaves
the current intent exclusions, public layers and validation policy in force.
