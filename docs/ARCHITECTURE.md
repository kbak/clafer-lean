# Architecture

The [canonical intent](intent.md) selects three layers. Only the first DPGraph
slice is delivered. The [live roadmap (#2)](https://github.com/kbak/clafer-lean/issues/2)
and [design (#13)](https://github.com/kbak/clafer-lean/issues/13) track later work.

| Layer | Responsibility and dependencies | Status |
| --- | --- | --- |
| DPGraph | Reusable graphs, signatures, typed formulas and declaration-preserving morphisms; Mathlib only | B.4 Definitions 6–10 implemented in [ClaferLean.DPGraph](../ClaferLean/DPGraph.lean) |
| FormalCD | Independently reusable class-diagram vocabulary and reviewed naming/structural invariants; builds on DPGraph | Future work; self-description aims at Figure 21c |
| Clafer | Structural 2014 Clafer application over the foundations: resolved syntax, Shapes/MCS, eventually Compile/gluing | Future work; name resolution and constraint meaning require review |

`Signature.lean` uses `CategoryTheory.Quiv.{arrowUniverse, vertexUniverse}` for
arity graphs; `Formula.lean` binds each symbol by a `Prefunctor` from that arity.
`Basic.lean` pairs a carrier with a `Set` of formulas. `Morphism.lean` supplies
preservation proofs, identity, composition, extensionality and laws. The signature
is fixed throughout these operations; arities and each carrier can occupy distinct
vertex/arrow universes. The separate `Examples.lean` uses finite types locally.
The root `ClaferLean.lean` imports both the independent entrypoint and examples
so the shared build and `leanchecker` check the delivered slice.

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

A fixed-signature Category instance, predicate interpretations, SetMap, Theorem 3,
span operations, and computable finite presentations are later increments. The
[source map](SOURCES.md) retains unresolved questions without choosing answers.
