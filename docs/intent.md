# Intent

## A maintainable foundation for formal semantics
`intent~formalization-foundation~1`

Develop a Lean 4 formalization grounded in the 2014 SoSyM paper. The repository
`kbak/clafer-lean` contains one Lake package, `clafer`, with sibling public roots
`DPGraph`, `FormalCD` and `Clafer`. Dependencies flow
`Clafer -> FormalCD -> DPGraph -> Mathlib`: independently reusable foundations
support structural 2014 Clafer as their application. DPGraph supplies link-preserving spans and indexed mappings, graphs,
typed diagram predicates, a fixed-signature category, abstract model
restriction and concrete predicate meanings over subsets and spans. FormalCD
supplies formal class diagrams and name-preserving morphisms independently of
Clafer, reusing the same graph identities and typed declarations.
The selected Table 3/A.1 vocabulary includes the accepted common-target
disjointness correction; later predicates require separately reviewed increments.

The delivered mathematical slice includes SoSyM B.1 Definitions 1–5 and
Theorems 1–2, B.2.1–2 span composition/inversion, and B.4 Definitions 6–10
with a fixed-signature category and the abstract model reduct of B.5 Theorem 3.
Span composition retains all composable link pairs; the adopted B.2.1 correction
proves agreement with relational composition after reduction, with isomorphism
exactly when the composite endpoint pairing is injective.
Interpretations select satisfying arity diagrams in a chosen semantic graph;
models restrict contravariantly along declaration-preserving maps. Derived
[model transport results](spec.md#model-reduct-injectivity) establish injectivity
or surjectivity of restriction under the respective composite identity equations.
[Carrier-cocone data](spec.md#declaration-unions-on-carrier-cocones) combines
translated declarations and records compatible component models. A supplied
carrier colimit [lifts to a DP-graph colimit](spec.md#pushout-universal-property),
and [model amalgamation](spec.md#model-amalgamation-on-a-carrier-pushout) identifies
models of the declaration union with compatible component models when the
semantic graph shares the fixed carrier universes.
Concrete inverse, triangle commutation, bag-sensitive keys, cover, disjointness,
map properties and cardinal multiplicities are delivered. Their bounded semantic
graph retains shared ambient objects and link multiplicity; it imposes no
automatic set-valued default. FormalCD adds inspectable class/map metadata, a
shared predefined registry, syntactic well-formedness and composable morphisms
preserving names, annotations and modes. Its ordinary maps require explicit
set-valued declarations; its inclusions require inclusion declarations. Bag mode
has no implicit set-valued declaration. Registry annotations identify optional
predefined classes without implementing their concrete domains, and syntactic
validity does not assert model existence or satisfaction. FormalCD self-description
and the Clafer implementation remain future work. An all-universes SetMap and the
unsupported predicates listed in the [source map](SOURCES.md#predicate-contracts-and-the-accepted-q8-correction)
remain outside the delivered slice. The [architecture](ARCHITECTURE.md)
explains the mathematics and future layer boundaries; [requirements](spec.md),
[source citations and open questions](SOURCES.md), and
[DPGraph definitions and proofs](dpgraph-trace.md) and
[FormalCD definitions and proofs](formalcd-trace.md) describe the current promises.
Track subsequent work in the [live roadmap (#2)](https://github.com/kbak/clafer-lean/issues/2) and
[design (#13)](https://github.com/kbak/clafer-lean/issues/13).

Exclude instance/object generation, Alloy/SMT/SAT integration, runtime
configurations, Claferize, post-2014 extensions, a production parser and
visualization. Keep the foundation reproducible and reviewable and the README
focused on its purpose.

Needs: req

## Consistent work by people and agents
`intent~traceable-contributions~1`

Use IntentBond to maintain the relationship between intended outcomes,
requirements, implementation, and verification evidence as the project evolves.
Use GitHub issues and a Project for planning and tracking, including IntentMade
work, so work and outstanding semantic decisions remain visible.
Follow the [contribution instructions](../CONTRIBUTING.md) and
[documentation policy](../AGENTS.md#documentation).

Needs: req
