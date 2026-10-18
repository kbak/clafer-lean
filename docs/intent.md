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
map properties and cardinal multiplicities are delivered. The derived
[ordinary-key correspondence](spec.md#ordinary-key-correspondence-and-repeated-marriages)
identifies keys with injective tuples under explicit totality and single-valuedness,
and checks a finite repeated-marriage witness. The bounded semantic
graph retains shared ambient objects and link multiplicity; it imposes no
automatic set-valued default. FormalCD adds inspectable class/map metadata, a
shared predefined registry, syntactic well-formedness and composable morphisms
preserving names, annotations and modes. Its ordinary maps require explicit
set-valued declarations; its inclusions require inclusion declarations. Bag mode
has no implicit set-valued declaration. Registry annotations identify optional
predefined classes without implementing their concrete domains, and syntactic
validity does not assert model existence or satisfaction. FormalCD also supplies
compatible signature extension, the Figure 21c metamodel, explicit name/arity
disciplines and full graph-binding identity with checked projection limitations.
The printed key and total-args constraints impose additional conditions on
instances; no universal realizability follows. A bounded syntactic self-description
statement reuses that metamodel in CDOver. The complete Figure 21b diagram has
twelve effective declarations and an explicit integer/span interpretation of the
corrected guarded VC, with nonempty whole-model and boundary witnesses. These
results do not assert semantic self-instantiation. Clafer supplies finite resolved
deep syntax, typed core constraints with lexical binders, graph support and
explicit inheritance widening, and individual Shapes. Constraint meaning and
predicate translation remain separate from typing. Source
names remain metadata separate from resolved IDs. Top-level abstract clafers keep
their head class and omit parent-dependent roles under the accepted source
correction in [SOURCES](SOURCES.md#resolved-2014-clafer-and-individual-shapes).
The MCS structural discipline covers Figure 23 and the expanded Appendix E
inventory, using guarded Shape slots and the accepted map-role ownership
correction. Role identities, resolved referents and strings remain distinct;
full formula bindings retain separate total-args and literal bag-key obligations.
Resolved-referent gluing identifies precisely equal class/map referents under
explicit incidence and metadata consistency. Labeling preserves the exact
translated declarations; FormalCD validity additionally requires effective
default completeness. Predefined annotations come from semantic origins.
The selected [typed constraint core](spec.md#resolved-core-constraint-typing)
follows D.1–D.3 and the [Q3 disposition](SOURCES.md#appendix-d-rule-dispositions-q3);
primitive conversion and constraint evaluation remain unformalized.
[Structural Compile](compile.md) constructs well-formed MCS values from the
explicit resolved-input contract, preserving names separately from generated
identities and attaching complete constraint bindings. Compile-to-gluing integration
remains on issue #24. An all-universes SetMap and the
unsupported predicates listed in the [source map](SOURCES.md#predicate-contracts-and-the-accepted-q8-correction)
remain outside the delivered slice. The [architecture](ARCHITECTURE.md)
explains the mathematics and future layer boundaries; [requirements](spec.md),
[source citations and open questions](SOURCES.md), and
[DPGraph definitions and proofs](dpgraph-trace.md),
[FormalCD definitions and proofs](formalcd-trace.md), and
[Clafer definitions and proofs](clafer-trace.md) describe the current promises.
The [roadmap (#2)](https://github.com/kbak/clafer-lean/issues/2), delivered in
[merged #40](https://github.com/kbak/clafer-lean/pull/40), links the subsequent
increments; [design #13](https://github.com/kbak/clafer-lean/issues/13) records
the representation assessment.

The [three-phase roadmap](ARCHITECTURE.md#roadmap-and-validation-accounting)
separates delivered results from proposed theorem statements and deferred source
decisions. Its source/design close-out is a documentation deliverable: it requires
review of the architectural alternatives, remaining validation tasks and audit
limits, rather than completion of all three layers. Project-critical source research
and the [bounded sketch/coherence assessment](SOURCES.md#generalized-sketches-and-model-reduct-coherence)
belong to [#41](https://github.com/kbak/clafer-lean/issues/41). Recovered pages
support only the inspected source claims; missing portions remain unaudited.
Accessible primary alternatives can establish the necessary claims. Further
acquisition is conditional on a named active claim lacking adequate evidence,
as recorded in the [source disposition](SOURCES.md#project-critical-source-disposition).
The current ordinary signature and precomposition
reduct laws remain the delivered contract; stronger semantic representations
and dependency-enriched extensions require separate authorization.
Planning the later increments does not authorize their semantic implementation.

The [resolved-IR comparison audit](resolved-ir-comparison.md) specifies a proposed
bounded structural comparison with the pinned compiler's generated Alloy. It
records compatibility limits, an effective-data boundary and missing whole-model
interpretation obligations for #50. Its companion-harness recommendation requires
review before executable work; it adds no solver integration or new semantic
claim to the delivered libraries.

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
