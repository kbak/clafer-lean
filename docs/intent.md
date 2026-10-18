# Intent

## A maintainable foundation for formal semantics
`intent~formalization-foundation~1`

Develop a maintainable Lean 4 formalization grounded in the 2014 SoSyM paper,
with reusable foundations supporting structural Clafer. The repository
`kbak/clafer-lean` contains one Lake package, `clafer`, and sibling public roots
`DPGraph`, `FormalCD` and `Clafer`. Dependencies flow
`Clafer -> FormalCD -> DPGraph -> Mathlib`; DPGraph remains independently importable.

| Layer | Delivered scope | Boundary |
| --- | --- | --- |
| DPGraph | Link-preserving spans and indexed mappings (B.1–B.2), typed diagram predicates and their fixed-signature category (B.4), abstract model restriction (B.5), conditional model transport/pushout/amalgamation results, and selected Table 3/A.1 meanings over subsets and spans | Independent universes and shared object/link identities; no all-universes SetMap, inference closure or automatic set-valued defaults |
| FormalCD | Class diagrams with names, predefined identities, effective defaults and name-preserving morphisms; compatible signatures, Figure 21c naming/arity disciplines and bounded syntactic self-description; complete Figure 21b with twelve declarations and guarded integer VC models | Syntactic validity, fragment satisfaction and whole-model satisfaction are separate; no semantic self-instantiation or general primitive-domain realization |
| Clafer | Finite resolved deep syntax, typed core constraints with lexical binders and inheritance widening, partial integer extraction from navigation, graph support, individual Shapes, Figure 23/Appendix E MCS disciplines, structural Compile and resolved-referent gluing | Name resolution/default elaboration and general constraint meaning remain separate; the integer bridge proves selected Appendix F operand definedness; Compile-to-gluing integration is on [#24](https://github.com/kbak/clafer-lean/issues/24) |

Preserve the accepted [paper corrections and clarifications](sosym-errata.md):
composition retains links and agrees with relations after reduction;
disjointness uses a common target; VC keeps its corrected direction and guard;
top-level abstracts retain their heads; and seven Figure 23 associations have
corrected ownership bounds. Full formula bindings, the literal bag key and total
args remain distinct. The [source map](SOURCES.md) records the exact decisions,
source identities and applicability limits.

Role identities, resolved referents and display names remain separate. Gluing
uses equal referents under incidence/metadata consistency and preserves the exact
translated declarations; FormalCD validity additionally requires complete effective
defaults. Structural Compile derives MCS validity under its [resolved-input
contract](compile.md). Neither transformation establishes full constraint-semantic
preservation. Augmented Compile generates effective group predicates over the union of own and
inherited child heads at each concrete context, including empty inventories.
The [group compilation contract](group-compilation.md) explains the separate
declaration component, exact union gluing and conditional semantic correspondence.
The [requirements](spec.md) state the precise promises, including
ordinary-key correspondence under totality/single-valuedness and the bounded
metamodel/primitive-conversion limits.

The [three-phase roadmap](ARCHITECTURE.md#roadmap-and-validation-accounting)
separates delivered, proposed and deferred results. The source/design close-outs
for [#2](https://github.com/kbak/clafer-lean/issues/2) and
[#13](https://github.com/kbak/clafer-lean/issues/13) are documentation deliverables,
not completion of every layer. The bounded [supporting-source assessment](SOURCES.md#generalized-sketches-and-model-reduct-coherence)
for [#41](https://github.com/kbak/clafer-lean/issues/41) leaves unread pages
unaudited. The [source disposition](SOURCES.md#project-critical-source-disposition)
makes further acquisition conditional on a named necessary claim lacking adequate
primary evidence; accessible primary alternatives may establish that claim.
Ordinary signatures and precomposition reduct laws remain the delivered
contract; stronger representations and dependency-enriched extensions require
separate authorization. Planning later work does not authorize implementation.

The [resolved-IR comparison contract](resolved-ir-comparison.md) fixes the
accepted effective-core boundary and guarded version-1 structural fragment.
Whole-model structural semantics and finite candidate verification belong in
`Clafer/Semantics/` and `Clafer/Verification/` under
[#50](https://github.com/kbak/clafer-lean/issues/50). Preserve resolved identities
and effective bounds without reconstructing authored/default provenance. A supplied
finite candidate may violate constraints; the checker must distinguish that result
from malformed or unsupported input and prove agreement with the independent
structural meaning. Reference occurrences retain identity even at repeated targets.
The external comparison harness and its location remain deferred to #51–52.

The separate [inherited realization extension](inherited-realization.md) supplies
Appendix F's ordinary field instances, explicit abstract families, restrictions of
shared maps, and generated structural correspondence. Authored abstract types and
fields made effectively abstract by containment retain different realization rules.
The complete fixture and final selections remain #64; general expression meaning
and its combined bridge remain #68/#69.

Exclude instance/object generation, Alloy/SMT/SAT integration, production runtime
configuration management, Claferize, post-2014 extensions, a production parser and
visualization. Keep the foundation reproducible and reviewable and the README brief.

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

## Documentation map

Use each document for its specific role; link to authoritative detail when
updating summaries. Keep conditions needed to understand a claim beside it.

| Read or maintain | Purpose |
| --- | --- |
| This intent | Product goals, delivered scope and exclusions |
| [Requirements](spec.md) | Normative promises, acceptance obligations and stable OFT IDs |
| [Architecture](ARCHITECTURE.md) | Representation choices, module boundaries, roadmap and theorem status |
| [Source map](SOURCES.md) | Paper correspondence, immutable source citations, decisions and audit limits |
| [Paper companion](sosym-errata.md) | Concise corrections and clarifications for SoSyM readers |
| [DPGraph](dpgraph-trace.md), [FormalCD](formalcd-trace.md) and [Clafer](clafer-trace.md) traces | Named implementation/proof artifacts and actual Lean declarations |
| [Integer extraction](integer-extraction.md) | Primitive realization, partial extraction and Appendix F navigation assumptions |
| [MCS inventory](mcs-invariants.md) and [Compile contract](compile.md) | Detailed structural clauses and transformation assumptions |
| [IR comparison contract](resolved-ir-comparison.md) | Proposed comparison domain, compiler audit and remaining prerequisites |
| [Contributing](../CONTRIBUTING.md), [trace convention](traceability.md) and [maintenance](maintenance.md) | Setup/checks, evidence links and repository administration |
| [Historical change records](changes/) | Retained accepted scopes and plans; not current architecture or status |

Keep frozen change records unchanged until controller retention permits removal.
Do not merge normative requirements with proof indexes or treat historical
proposals as current promises. Preserve artifact IDs, trace relationships, source
citations and existing link destinations when consolidating living prose.
