# Architecture

The [canonical intent](intent.md) selects three layers. Spans and their mapping
operations, DPGraph syntax, its fixed-signature category and abstract model
restriction and the selected concrete predicate meanings are delivered. The [live roadmap (#2)](https://github.com/kbak/clafer-lean/issues/2)
and [design (#13)](https://github.com/kbak/clafer-lean/issues/13) track later work.
The repository `kbak/clafer-lean` contains one Lake package named `clafer`.
Its public libraries and module roots are siblings: `DPGraph`, `FormalCD`,
`Clafer`. Imports flow `Clafer -> FormalCD -> DPGraph -> Mathlib`.

| Layer | Responsibility and dependencies | Status |
| --- | --- | --- |
| DPGraph | Spans, indexed mappings, graphs, typed predicates, a fixed-signature category and abstract/concrete interpretation; Mathlib only | B.1 Definitions 1–5/Theorems 1–2, B.2.1–2 with the Q1 correction, B.4 Definitions 6–10 and the abstract B.5 reduct and selected Table 3/A.1 meanings in [DPGraph](../DPGraph.lean) |
| FormalCD | Independently reusable class-diagram vocabulary and reviewed naming/structural invariants; builds on DPGraph | [Entrypoint scaffold](../FormalCD.lean) only; future self-description aims at Figure 21c ([#17](https://github.com/kbak/clafer-lean/issues/17), [#18](https://github.com/kbak/clafer-lean/issues/18), [#19](https://github.com/kbak/clafer-lean/issues/19)) |
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

VC, name/arity disciplines, arbitrary path equations beyond the triangle,
FormalCD/Clafer-specific predicates, all-universes SetMap and computable finite
presentations remain future work. The source map distinguishes the accepted Q1
and Q8 corrections from the remaining open questions.
