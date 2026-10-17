# Architecture

The [canonical intent](intent.md) selects three layers. Spans and their mapping
operations, DPGraph syntax, its fixed-signature category and abstract model
restriction, the selected concrete predicate meanings, and FormalCD
structure/morphisms, signature support, the Figure 21c metamodel, bounded syntactic
self-description and Figure 21b with its corrected VC interpretation are delivered. The [live roadmap (#2)](https://github.com/kbak/clafer-lean/issues/2)
and [design (#13)](https://github.com/kbak/clafer-lean/issues/13) track later work.
The repository `kbak/clafer-lean` contains one Lake package named `clafer`.
Its public libraries and module roots are siblings: `DPGraph`, `FormalCD`,
`Clafer`. Imports flow `Clafer -> FormalCD -> DPGraph -> Mathlib`.

| Layer | Responsibility and dependencies | Status |
| --- | --- | --- |
| DPGraph | Spans, indexed mappings, graphs, typed predicates, a fixed-signature category and abstract/concrete interpretation; Mathlib only | B.1 Definitions 1–5/Theorems 1–2, B.2.1–2 with the Q1 correction, B.4 Definitions 6–10 and the abstract B.5 reduct and selected Table 3/A.1 meanings in [DPGraph](../DPGraph.lean) |
| FormalCD | Class diagrams, naming/default obligations and name-preserving morphisms; builds on DPGraph | [Core API](../FormalCD.lean) delivered; Figure 21c and disciplines, bounded syntactic self-description, and Figure 21b/VC delivered |
| Clafer | Structural 2014 Clafer application over the foundations: resolved syntax, Shapes/MCS, eventually Compile/gluing | [Entrypoint scaffold](../Clafer.lean) only; name resolution and constraint meaning require review |

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

VC, arbitrary path equations
beyond the triangle, FormalCD/Clafer-specific predicates, all-universes SetMap and computable finite
presentations remain future work. The source map distinguishes the accepted Q1
and Q8 corrections from the remaining open questions.

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

[Figure21/Basic.lean](../FormalCD/Figure21/Basic.lean) constructs the four-node,
five-arrow diagram, Int registry metadata and twelve distinct effective formulas.
[VC.lean](../FormalCD/Figure21/VC.lean) adds one symbol through `Vocabulary.extend`.
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

[Examples.lean](../FormalCD/Figure21/Examples.lean), checked separately from public
imports, uses `Bool ⊕ Int`: two component objects, disjoint ECU/Display singleton
subsets, all integers, and an optional single server link with its actual inverse.
The parameterized `model_iff` proves whole Figure 21b satisfaction exactly when
the optional link respects the corrected order. The lower-version counterexample
satisfies all eleven other declarations; the unserved model keeps the 0..1 bound
while failing server totality. These are models of Figure 21b, not Figure 21c.
