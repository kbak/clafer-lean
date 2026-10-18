# Architecture

The [canonical intent](intent.md) owns product scope and the documentation map.
This document explains representation choices and module boundaries; the
[source map](SOURCES.md) owns paper correspondence and the trace maps own
individual implementation/proof inventories.

The repository `kbak/clafer-lean` contains one Lake package, `clafer`, with sibling
public roots. Imports flow `Clafer -> FormalCD -> DPGraph -> Mathlib`.

| Layer | Responsibility | Public entrypoint |
| --- | --- | --- |
| DPGraph | Reusable graphs, spans, predicates, model restriction and conditional pushouts | [DPGraph](../DPGraph.lean), independently importable |
| FormalCD | Class-diagram metadata, morphisms, metamodel disciplines and bounded examples | [FormalCD](../FormalCD.lean), built on DPGraph |
| Clafer | Resolved syntax, Shapes, MCS, structural Compile and gluing | [Clafer](../Clafer.lean), built on FormalCD |

## DPGraph core and models

[Signature.lean](../DPGraph/Signature.lean), [Formula.lean](../DPGraph/Formula.lean)
and [Basic.lean](../DPGraph/Basic.lean) represent symbols with graph arities,
full `Prefunctor` bindings and declaration sets. A carrier is a directed
multigraph: `x ⟶ y` is an arrow type without identity/composition operations.
The category of bundled graphs supplies maps between carriers, not composition
inside a carrier. A binding retains vertex images, isolated arity vertices and
distinct arrow occurrences with equal images. Declarations require neither
global finiteness nor decidable equality or inference closure.

[Morphism.lean](../DPGraph/Morphism.lean) translates bindings by postcomposition
and proves declaration preservation. Maps can identify vertices/arrows, and a
target can have extra declarations. [Category.lean](../DPGraph/Category.lean)
uses these maps at a fixed signature and carrier universes. Syntax, arity,
carrier and semantic universes remain independent; see the
[representation decision](#dp-graph-representation-decision) for size and equality details.

[Semantics.lean](../DPGraph/Semantics.lean) interprets each predicate as a set
of satisfying arity maps into a fixed semantic graph Ω. A model map m satisfies
φ when `φ.binding ; m` belongs to that set. Associativity gives
`sat m (translate φ F) ↔ sat (F ; m) φ`; declaration preservation then restricts
models contravariantly along `F : S → T`. No closure/invariance axiom on meanings
is needed. The formula equivalence does not reflect whole-model satisfaction,
since T can declare more formulas. The derived split-map
[injectivity](spec.md#model-reduct-injectivity) and
[surjectivity](spec.md#model-reduct-surjectivity) results retain explicit composite
identity hypotheses. [SemanticsExamples.lean](../DPGraph/SemanticsExamples.lean)
checks small and larger semantic universes.

The concrete semantic graph uses subsets of one ambient U as vertices and spans
between their subtype carriers as arrows. Shared objects retain ambient identity.
For `U : Type u`, links in `Type (max u w)` give arrows in
`Type (max u w + 1)`; this is a bounded graph, not an all-universes SetMap.
[Supporting-source alternatives](SOURCES.md#generalized-sketches-and-model-reduct-coherence)
compare ordinary signatures with marked/dependency-enriched arities and typed
pullback instances. They do not establish a bridge or justify another dependency;
closure, consistency, size and coherence would require separate contracts.

[Pushout/Basic.lean](../DPGraph/Pushout/Basic.lean) places the
[union of translated declarations](spec.md#declaration-unions-on-carrier-cocones)
on a supplied carrier cocone and records compatible component models.
[Universal.lean](../DPGraph/Pushout/Universal.lean) lifts a supplied carrier
colimit to a [DP-graph colimit](spec.md#pushout-universal-property): the mediator
preserves the union and inherits factorization/uniqueness from the carrier.
[Models.lean](../DPGraph/Pushout/Models.lean) derives
[model amalgamation](spec.md#model-amalgamation-on-a-carrier-pushout) using that
same universal property and satisfaction under translation. Here Ω shares the
fixed carrier universes. No global pushout existence or concrete Clafer gluing
theorem follows. [Trace artifacts](dpgraph-trace.md) give the named declarations.

Examples, including [Examples.lean](../DPGraph/Examples.lean), are checked
separately from public imports. The [validation workflow](../CONTRIBUTING.md#setup-and-checks)
discovers every owned module, rejects reverse/unowned imports and audits all
project declarations, including unimported helpers.

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
witnesses; the final assessment is recorded in merged #39. The
[roadmap (#2)](https://github.com/kbak/clafer-lean/issues/2) links subsequent
source questions and Clafer increments. Bounded syntactic
self-description and the telematics example are delivered in
[#19 / #38](https://github.com/kbak/clafer-lean/pull/38), with the limitations
described below; neither semantic self-instantiation nor global pushout existence follows.

## Spans and indexed mappings

[Span.Basic](../DPGraph/Span/Basic.lean) keeps a link type and two endpoint
functions in independent universes. `Span.Iso` renames links while preserving
endpoints; inversion swaps the legs and is involutive, without supplying a
categorical inverse. [IndexedFamily](../DPGraph/Span/IndexedFamily.lean) uses
source-fiber indices and evaluation. Its sigma-head conversion and roundtrips
use equivalences across universes, not finite multisets or resizing.

[Composition](../DPGraph/Span/Composition.lean) retains every composable link
pair; family composition uses a dependent sum of indices. Units and associativity
are canonical span isomorphisms. [Relation](../DPGraph/Span/Relation.lean)
forgets link identity by existential endpoint membership. Joint endpoint
injectivity, fiberwise evaluation injectivity and isomorphism to the reduced
relation span characterize set-valuedness (B.1 Theorem 2).

The [Q1 derivation](SOURCES.md#span-composition-q1-research-for-4) states the exact
reduction/isomorphism criterion and sufficient hypotheses. The
[examples](../DPGraph/Span/Examples.lean) preserve two-path and parallel-link
counterexamples, empty heads and universe joins; the
[trace map](dpgraph-trace.md#span-representation) supplies the full proof inventory.

## Concrete predicates

[Predicates.Signature](../DPGraph/Predicates/Signature.lean) separates symbols
and real arity graphs from [Meaning](../DPGraph/Predicates/Meaning.lean).
Inverse has opposite arrows; commutation has a triangle; keys use a common source;
cover/disjointness use a common target. Family arities retain their center at
zero arity and permit repeated bindings. Generic DPGraph adds no set-valued default.

Inverse and triangle commutation compare spans up to link isomorphism; keys compare
source fibers as bags; cover and corrected disjointness inspect reachable values.
Inclusion fixes ambient object identity, and multiplicity bounds count links via
finite-type embeddings, with no finiteness requirement for an unbounded upper
limit. The [predicate contracts](SOURCES.md#predicate-contracts-and-the-accepted-q8-correction)
record exact meanings, empty-family cases, invariance and the Q8 correction.

[FunctionalKey](../DPGraph/Predicates/FunctionalKey.lean) derives the
[ordinary-key correspondence](spec.md#ordinary-key-correspondence-and-repeated-marriages)
under componentwise totality/single-valuedness. Its
[repeated-marriage witness](../DPGraph/Predicates/Examples/FunctionalKey.lean)
does not impose those hypotheses on general bag keys.
[Interpretation](../DPGraph/Predicates/Interpretation.lean) connects these meanings
to generic satisfaction and reduct. [Examples](../DPGraph/Predicates/Examples.lean)
and the [trace map](dpgraph-trace.md#typed-vocabulary-implementation) cover the
acceptance boundaries. VC belongs to the separate FormalCD extension; arbitrary
path equations beyond triangles and all-universes SetMap remain outside this slice.

## Formal class diagrams

[FormalCD.Basic](../FormalCD/Basic.lean) adds a shared `Registry`, class/map
names, predefined annotations and map modes to the authoritative DP declaration
set. `Raw` exposes data and invalid cases; `CD` bundles `Raw.WellFormed`.
Registry identifiers determine predefined identity/kind, independently of spelling.
Entries are optional; user names may repeat, and there is no global name-injectivity
or inheritance-acyclicity condition at this layer.

Declarations are effective: ordinary maps require setValued membership and
inclusions require inclusion membership. Bag mode adds no default, while authored
bag setValued declarations remain expressible. These syntactic obligations assert
neither satisfaction nor model existence; general primitive/object-diagram
semantics remain separate. Exact [source/default obligations](SOURCES.md#formalcd-structure-and-selected-morphisms)
and [naming requirements](spec.md#formalcd-naming-and-predefined-identity) retain
these distinctions.

[Morphism](../FormalCD/Morphism.lean) specializes DP morphisms by preserving
names, optional registry identities and modes. Source/target CDs independently
satisfy well-formedness; carrier maps may identify user vertices/arrows and targets
may declare more. [Semantics](../FormalCD/Semantics.lean) applies the existing
reduct after forgetting metadata. The [structural](../FormalCD/Examples.lean) and
[semantic](../FormalCD/SemanticsExamples.lean) fixtures and
[trace map](formalcd-trace.md) record the laws and counterexamples.

## Figure 21c and compatible vocabularies

[FormalCD.Signature](../FormalCD/Signature.lean) defines `Vocabulary` through
a built-in symbol embedding and inverse arity Prefunctors. `extend` adds disjoint
symbols; embedding commutes with translation and interpretation restriction.
`RawOver`, `CDOver` and `HomOver` generalize the original built-in wrappers without
changing their metadata/default obligations. General vocabularies retain independent
universes; the disjoint extension uses small arities.

[The metamodel](../FormalCD/Metamodel/Basic.lean) uses this API with explicit
naming/arity subgraphs. The [source inventory](SOURCES.md#figure-21c-metamodel)
owns nodes, arrows, declarations and inferred nd/ad attachments. Class, modeled
class and object identities stay separate; no node denotes all Lean types.

`Candidate` stores the symbol, every vertex image and indexed total-arrow images;
its endpoint-valid candidates are equivalent to `DPGraph.Formula`. `Context`
supplies embeddings/data, never validity. `ArityDiscipline` checks complete fiber
indexing, endpoints, argument values and selected symbols; `NameDiscipline` checks
names, registry identities/kinds and the predefined naming square. Their bounded
interpretations use the existing subset/span graph and independent syntax universes.

Full binding identity, literal bag-key satisfaction and total args are separate
obligations. The [projection witnesses](SOURCES.md#literal-key-total-args-and-the-19-obligation)
explain why positional/isolated bindings and zero-arrow arities prevent a universal
realizability inference. Fragment satisfaction and whole-metamodel satisfaction
remain distinct; see the [named discipline proofs](formalcd-trace.md#discipline-correspondence-and-identity-laws).

## Bounded self-description and Figure 21b

[SelfDescription.lean](../FormalCD/SelfDescription.lean) reuses `Metamodel.diagram`
in the small `CDOver` family with the nd/ad vocabulary and SING registry.
`bounded_self_description` combines representation, well-formedness and the
inventory; `metamodelFormulaRepresentation` reuses `Candidate.formulaEquiv`.
It establishes syntactic self-description, not semantic self-instantiation.

[Telematics/Basic.lean](../FormalCD/Telematics/Basic.lean) supplies Figure 21b's
four nodes, five arrows and twelve effective declarations.
[VC.lean](../FormalCD/Telematics/VC.lean) adds a four-arrow predicate with an
explicit integer-domain embedding/decoder. Its meaning follows actual server,
inclusion and version links; `builtins_unchanged` preserves generic meanings.
Under inclusion and 1..1(version), `satisfies_vc_iff_guarded` gives the corrected
comparison; 0..1(server) is single-valued without totality, and 0..5(display)
bounds its inverse. [Source locators and the Q7 decision](SOURCES.md#figure-21b-and-the-accepted-q7-correction)
retain the exact order, guard and drawn annotations.

[Examples.lean](../FormalCD/Telematics/Examples.lean) uses `Bool ⊕ Int`, all
integers and an optional server link with its inverse. `model_iff` characterizes
whole Figure 21b models: greater/equal versions pass, lower fails only VC, and
an unserved display passes. These are separate from Figure 21c fragments and
the bounded self-description result; the [trace map](formalcd-trace.md#figure-21b-satisfaction-and-counterexamples)
links the full witness inventory.

## Roadmap and validation accounting
`impl~formalization-roadmap-architecture~1`

The [Project](https://github.com/users/kbak/projects/2), its existing
[three phase milestones](https://github.com/kbak/clafer-lean/milestones?state=all),
and [#2](https://github.com/kbak/clafer-lean/issues/2) record the backlog.
[Merged #40](https://github.com/kbak/clafer-lean/pull/40) delivers #2's
documentation close-out; [#41](https://github.com/kbak/clafer-lean/issues/41)
records the bounded assessment delivered in [#43](https://github.com/kbak/clafer-lean/pull/43). The
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
| 3 — structural 2014 Clafer | [#3](https://github.com/kbak/clafer-lean/issues/3) → [#20](https://github.com/kbak/clafer-lean/issues/20) and [#21](https://github.com/kbak/clafer-lean/issues/21) → [#22](https://github.com/kbak/clafer-lean/issues/22)/[#23](https://github.com/kbak/clafer-lean/issues/23) → [#24](https://github.com/kbak/clafer-lean/issues/24) | Resolved syntax, the binder/context boundary and individual Shapes are implemented for #3. The structural MCS disciplines are implemented for #20; #21 adds typed core expressions and graph support. Structural Compile is implemented for #22 under its explicit contract. The approved Q4 gluing is implemented for #23 with separate default-completeness hypotheses; Compile-to-gluing integration remains on #24. Planning tickets alone authorize no further implementations. |

### Nine architectural decision areas

This cross-check consolidates the brief's representation and later-layer concerns
with the rationale in #13. A1–A9 are design areas, separate from the source
questions Q1–Q9 in [SOURCES](SOURCES.md#question-dispositions-and-validation-tasks).
“Proposed” marks a later design to validate within its own authorized increment.

| Area | Choice and alternatives | Evidence and remaining validation |
| --- | --- | --- |
| A1 — graph representation and Mathlib reuse | Retain `Quiver`/`Prefunctor`/`Quiv` over a second vertex/edge record or a category imposed on carrier arrows. Total edges are a dependent sum; loops and parallel arrows survive. | #14/#25 exercises isolated vertices and noninjective maps. #13/#39 assesses the wider Quiv imports; [cost decision](#dependency-cost-decision) states measurement limits and reassessment triggers. No new wrapper or dependency change is proposed. |
| A2 — signatures, arities and declarations | Graph-valued arities and full dependent bindings, with declaration sets. Untyped arrow lists lose incidence/isolated vertices; injective bindings lose repetitions. Dependency-enriched sketches are a separate extension. | #14/#25 proves translation and declaration preservation; #18/#36 checks full-binding/argument-projection limits. [#41](https://github.com/kbak/clafer-lean/issues/41) owns the [bounded library/closure/reduct assessment](SOURCES.md#generalized-sketches-and-model-reduct-coherence) against Diskin & Wolter §4.1–3. A future dependency-enriched extension needs its own scope and compatibility evidence. |
| A3 — morphisms and categorical structure | Fixed-signature DP category; preservation permits identification and extra target declarations. Requiring embeddings or reflection would change Definition 10. FormalCD specializes this with metadata preservation. | #15/#27 and #17/#35 supply category/morphism laws; #28/#29 and #30/#33 are conditional derived results. #23 proves the concrete label map preserves declarations and separately establishes CD well-formedness under explicit defaults; generic pushout existence or arbitrary-model reflection does not follow. |
| A4 — spans, identities and universes | Retain explicit links/fiber indices and pullback composition. Relations discard multiplicity; a graph of all Lean types needs an unjustified size principle. Use independent universes and explicit bounded ambient objects. | #4/#32 proves roundtrips, units/associativity up to isomorphism and corrected Q1; #16/#34 checks shared-object inclusion and bag counts. #20/#23 preserve these identities across role encodings without resizing or collapsing links. |
| A5 — predicate syntax and meaning | Separate symbols/arities from interpretations and model maps. Generic syntax imposes no default set-valuedness; FormalCD supplies effective defaults. Primitive domains and VC require explicit interpretations. | #15/#27 proves reduct by precomposition; #16/#34 interprets the selected vocabulary and Q8; #19/#38 handles VC separately. #21 resolves Q3 for the selected typed core and distinguishes typing from satisfaction; general evaluation remains deferred; #67 supplies the separate integer-extraction interface. |
| A6 — formal-CD metamodel and self-description | Reuse `CDOver` with explicit vocabulary/registry, nd/ad meanings and full-binding correspondence. Reject a Lean universe fixpoint and an inference from syntactic well-formedness to semantic self-instantiation. | #18/#36 and #19/#38 deliver the bounded result and Figure 21 example. Ordered/isolated bindings expose bag-key and total-args restrictions. Stronger realizability/self-instantiation is deferred and would require new accepted hypotheses and examples. |
| A7 — Clafer syntax, MCS and finiteness | Deep resolved AST and typed individual role graphs, with raw data plus explicit well-formedness propositions. A shallow Lean encoding would obscure source syntax/compilation; globally finite DPGraphs would restrict reusable semantics. Use finite data only at the executable boundary. | #3 accounts for Figure 16/22, Appendix C and the accepted top-level abstract correction in the [Clafer source map](SOURCES.md#resolved-2014-clafer-and-individual-shapes); #20 has an [accepted guarded inventory](mcs-invariants.md) of Appendix E clauses (Q2), with exact presence still enforced by Shape. Figure 23's accepted source-multiplicity correction (Q9) makes the seven map/inclusion associations uniquely owned on their images; nonempty examples validate this boundary. Compile validates these finite presentations through its input contract and derived structural proofs. |
| A8 — names, generated identity, Compile and gluing | Accepted #20 separation of role identities, resolved class/map referents and displayed names. Repeated parent/dref/isA strings do not identify arrows. Preserve the information needed for intended gluing; the approved Q4 congruence uses exactly resolved-referent equality and an exact declaration image. | #20 states the level of cojoining equality and covers repeated names. #22 implements generated identities, freshness and termination; #23 owns intended identifications and incidence/declaration preservation. The approved congruence is implemented in the used-referent graph. A DP-morphism proof and a CD-well-formedness proof are separate targets. |
| A9 — constraints and end-to-end claims | Resolved typed core expressions with explicit inheritance widening and graph support; semantic translation remains separate. Neither a production parser nor the current Haskell compiler defines the 2014 meaning. Structural Compile/glue correctness is distinct from full constraint-semantic preservation. | #21 resolves Appendix D discrepancies (Q3) and checks binders/navigation/types; #22/#23 state explicit well-formed-input assumptions; #24 enumerates supported Appendix F examples and unsupported constructs. Full constraint preservation remains deferred until both source and target meanings are specified. |

### Theorem statements and proof status

The roadmap assessment adds no Lean theorem. The existing named
[DPGraph](dpgraph-trace.md), [FormalCD](formalcd-trace.md) and [Clafer](clafer-trace.md) proof artifacts
link to the actual declarations; the statements below bound what may be inferred.

| Statement | Status and scope |
| --- | --- |
| Translation preserves identity/composition; declaration-preserving maps form a fixed-signature category. | Proved in #14/#25 and #15/#27, using `Formula.translate_id`, `translate_comp` and `Hom` laws; B.4 Definitions 6–10. |
| A model of T restricts to a model of S along F : S → T, contravariantly. | Proved as `Interpretation.isModel_reduct` and `reduct` laws (#15/#27); abstract B.5 Theorem 3. No whole-model reflection is claimed. |
| Restriction along F is injective if J.comp F = id T, and surjective if F.comp J = id S. | Derived and proved in `ModelTransport` (#28/#29), not verbatim paper theorems. |
| A supplied carrier pushout lifts to a DP pushout; its models correspond to compatible component models. | Derived and proved as `Pushout.isColimit`/`modelEquiv` (#30/#33). The equivalence fixes semantic and carrier universes together; no global existence or concrete Clafer gluing theorem. |
| Span reduction commutes with composition; isomorphism to the relational composite requires injective composite endpoint pairing. | Proved corrected Q1 statement (#4/#32), with counterexamples to the unqualified source assertion. |
| The metamodel has a bounded syntactic CD representation; guarded VC agrees with the selected integer comparison and the example models. | Proved as `bounded_self_description`, `satisfies_vc_iff_guarded` and `Examples.model_iff` (#19/#38); preserve their vocabulary/registry, integer-domain, inclusion and version hypotheses. No semantic self-instantiation. |
| A well-formed resolved AST compiles to an MCS satisfying the explicitly enumerated invariants. | Derived by `Compile.compile`/`wellFormed` under `Compile.Input`, including canonical naming and positive constraint support. Finite traversal/lookup and owner-role identities establish termination and freshness; see [the contract](compile.md). |
| The role-label map is a DP morphism, and the glued structure is a well-formed formal CD. | Proved separately in `Gluing.labelHom` and `raw_wellFormed`: approved referent incidence/metadata consistency, with naming and effective-default completeness additionally required for CD validity. |
| Compilation/gluing preserves all constraint meanings, or every CD semantically instantiates its metamodel. | Deferred; no accepted general statement or proof. Source resolution and explicit realizability/semantic hypotheses would be needed first. |

#40 delivers #2's cross-check and documentation close-out. Missing-source
limits and conditional acquisition remain recorded under Q6 / #41; acceptance of the roadmap does not
complete that research or later implementation tickets. The pinned build,
kernel/axiom/layer checks and IntentBond validate the candidate and existing
proofs; they do not certify the source interpretation or complete a deferred
task. Exit 4 leaves semantic review pending. Each continuing issue requires its
own accepted deliverables and any required documentation merge before closure.

## Resolved syntax and individual Shapes

[Clafer.Syntax](../Clafer/Syntax.lean) uses mutually inductive `Tree`/`Forest`
containment with resolved `DeclId` edges for references/inheritance. `Origin`
distinguishes root, primitive domains and users; strings are repeatable metadata.
Containment supplies structural recursion/depth, inheritance uses a rank witness,
and reference/super IDs are never recursive children. The recursors and finite
lookup remain kernel-reducible; `noncomputable` suppresses compiler-generated
partial native helpers rather than introducing choice or termination axioms.
No native compiler executable or finite-carrier restriction on lower layers follows.

Authored/effective multiplicities and abstractness remain inspectable. `Defaults`
validates supplied Appendix C data, including inherited keyword provenance and
explicit overrides; it does not elaborate defaults or realize primitive values.
The [syntax/source correspondence](SOURCES.md#resolved-2014-clafer-and-individual-shapes)
records the supported forms, traversal measures and accepted parentless-head rule.

[Clafer.Context](../Clafer/Context.lean) separates the syntax boundary from typed
expressions: context, scope/domain occurrences and binder IDs/names survive without
deduplication. [Constraints.Typing](../Clafer/Constraints/Typing.lean) supplies
Boolean/integer terms and unary/binary collections with lexical positions,
endpoint-checked joins and explicit inheritance paths for widening.
[Constraints.Support](../Clafer/Constraints/Support.lean) gives finite occurrence
graphs retaining isolated/repeated identities, used as constraint arities by
Compile. The [typing requirement](spec.md#resolved-core-constraint-typing) and
[Q3 disposition](SOURCES.md#appendix-d-rule-dispositions-q3) distinguish this
interface from resolution, general evaluation and preservation. The
[integer-extraction extension](#integer-extraction-boundary) supplies its separate
partial primitive bridge.

[Clafer.Shape](../Clafer/Shape.lean) uses finite role subtypes with both endpoint
equations in arrow types. Kind and parent presence determine availability;
`Located.shape` decodes a local inventory, `Realization` binds it to a CD and
`Inclusions` supplies shared-role inclusions for a selected super.
[Local diagrams](../Clafer/Shape/Diagram.lean) add inverse, triangle, multiplicity,
default and set-reference-key declarations. [MCS](../Clafer/MCS/Basic.lean) supplies
global cojoining/naming; [gluing](#mcs-gluing) uses referents. Local CD validity
asserts no model. [Clafer trace](clafer-trace.md) links the complete proof inventory.

## MCS structural representation

[MCS/Basic.lean](../Clafer/MCS/Basic.lean) represents a resolved structural
family with Shape-presence guards. Shared class-role vertices and distinct ordinary/
inclusion slot occurrences make cojoining and ownership inspectable.
`Family.canonicalRoles` constructs cojoining from resolved edges; it is not the
AST compiler. `Family.WellFormed`/`Labels.WellFormed` enforce the
[Appendix E inventory](mcs-invariants.md), and `Model` bundles those proofs.

`Formulas` retains the owner and full graph binding of every formula, with separate
literal-key and total-args obligations. [MCS/Metamodel.lean](../Clafer/MCS/Metamodel.lean)
encodes Figure 23, explicit nd/ad context and the accepted Q9 bounds; exact source
clauses and their proof map belong to the inventory. [Examples](../Clafer/MCS/Examples.lean)
exercise nonempty families, primitive domains, repeated names and guarded inclusions.
Local formulas transport through `Roles.localDiagram`; [Compile](../Clafer/Compile/Basic.lean)
generates the local/constraint bank. No semantic self-instantiation follows.

## Finite structural verification boundary

The accepted [#49 contract and compiler matrix](resolved-ir-comparison.md) under
#48 selects a guarded structural fragment and an effective input boundary for #50.
Whole-model semantics, representation and erasure bridges live under
`Clafer/Semantics/`; finite candidates and the verified executable checker live
under `Clafer/Verification/`. These remain in the single `clafer` package and
add no reverse dependency or finite-carrier condition to DPGraph or FormalCD.
The reusable local bank is the existing structural Compile bank. Global root,
abstract-cover/disjointness and group obligations must be stated and interpreted
in addition to that bank; local Shapes alone do not establish whole-model meaning.

Finite ordinary relation tables retain head objects as occurrence identities.
Derived reference-target spans retain composable links. Inheritance uses the same
ambient objects, and group counts use the union of child head fibers. Unrelated
classes may overlap; Alloy's implicit signature disjointness is not a Lean guard.
The [structural checker guide](structural-checker.md) identifies the domain,
compiled-bank and arbitrary-span normalization bridges, protocol and proof APIs.
The theorem checks the executable algorithm against independent satisfaction;
an ordinary native invocation supplies a verdict, not a fresh kernel proof.
No per-instance proof-certificate or solver theorem is claimed.

The #51–52 external harness location, importer, paired compiler receipts,
solver/search policy and generation remain deferred. JSON alone does not recover
authored/default provenance or backend state. Preserve the full pinned validation
and independent review gates for this executable increment.

## Structural Compile

[Compile/Structure.lean](../Clafer/Compile/Structure.lean) traverses resolved
entries in preorder, allocates class IDs and resolves finite edges.
[Binding.lean](../Clafer/Compile/Binding.lean) builds complete constraint bindings;
[Local.lean](../Clafer/Compile/Local.lean) generates Shape/inclusion declarations;
[Basic.lean](../Clafer/Compile/Basic.lean) combines banks and validity proofs.
[GroupSupport.lean](../Clafer/Compile/GroupSupport.lean),
[Groups.lean](../Clafer/Compile/Groups.lean) and
[GroupSemantics.lean](../Clafer/Compile/GroupSemantics.lean) add full inherited group
supports, a separate augmented declaration component, exact union gluing and
child-object counting correspondence. The old structural bank remains intact;
vertex-only groups do not claim its total-args discipline. See the
[group contract](group-compilation.md) for D6, empty inventories and #50/#66 boundaries.
The [Compile contract](compile.md) owns exact input assumptions, identity/sharing
rules, formula generation and guarantees. It derives structural MCS validity,
not constraint-semantic preservation; integration with gluing remains on #24.

## MCS gluing

[Gluing.lean](../Clafer/MCS/Gluing.lean) builds the graph of used class/map
referents. Representatives define endpoints/metadata, and `Incidence`/`Compatible`
make those choices independent of representatives. `classLabel_eq_iff` and
`labeledArrow_eq_iff` establish exactly referent equality as the identification
rule; different parallel-map referents remain distinct despite equal names/endpoints.

`labelHom` transports full formulas to their exact image. Translation retains
isolated vertices and repeated arguments, but may identify source formulas, so
the source bank's key does not imply injectivity of translated formulas.
`raw_wellFormed`/`cd` separately require naming and effective-default completeness;
[Origins.lean](../Clafer/MCS/Gluing/Origins.lean) derives naming from valid origins,
while `ofValid` still requires compatibility/defaults. No missing defaults are
silently added. The [gluing boundary](mcs-invariants.md#gluing-boundary),
[Q4 decision](SOURCES.md#mcs-gluing-and-the-approved-q4-rule) and
[requirements](spec.md#mcs-gluing-identity-and-incidence) own the precise contract.

[Examples](../Clafer/MCS/Gluing/Examples.lean) and
[Boundaries](../Clafer/MCS/Gluing/Boundaries.lean) exercise merges, parallel maps,
formula collisions, defaults and full-binding transport; the
[trace map](clafer-trace.md#mcs-gluing-representation) gives exact declarations.
DP preservation, CD validity and model satisfaction are distinct. Compiler
integration and global pushout existence are separate obligations.

## Integer extraction boundary

[Constraints/Integer.lean](../Clafer/Constraints/Integer.lean) assigns the partial
meaning of `Expr.integerOf`: exact singleton equality with an encoded mathematical
integer. `Support.integer` marks the operand class; `Support.Resolved.integers`
checks its resolved primitive origin. `IntegerBinding` supplies the integer domain,
equal-ID correspondence and inheritance inclusions. Typing does not certify
runtime uniqueness. The operation returns `none` for invalid collections.

[IntegerNavigation.lean](../Clafer/Constraints/IntegerNavigation.lean) supplies
the selected Appendix F resolved fragment, typed comparison and conditional
operand-definedness theorem. Head and dereference maps remain distinct;
1..1 version/server heads and functional dereferences derive singleton images.
The accompanying examples evaluate the actual navigation and comparison for
arbitrary integer versions. This extension reuses the explicit Figure 21 integer
realization, while its VC predicate and guarded optional-server semantics remain
separate. The [conversion contract](integer-extraction.md) owns detailed limits;
full expression interpretation, Compile semantic preservation and all inherited
whole-model constraints remain future work.
