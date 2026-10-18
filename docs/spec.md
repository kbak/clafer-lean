# Foundation, DP-graph, FormalCD and Clafer requirements

These requirements cover the repository infrastructure and the delivered
span operations, DP-graph category, abstract model reduct and concrete predicate
semantics over a bounded graph of subsets and spans, plus FormalCD
structure, name-preserving morphisms, the Figure 21c metamodel, bounded syntactic
self-description and the complete Figure 21b example with corrected VC. Structural
Clafer now includes resolved deep syntax and individual Shapes under the scoped
requirements below, including the MCS structural discipline. Full expressions, compilation, gluing and integration
remain separate increments. The source-audit roadmap alone authorizes no semantic work.

## Reproducible Lean validation
`req~lean-validation~1`

The project pins Lean 4 and builds every module in the sibling `DPGraph`,
`FormalCD` and `Clafer` libraries of the single `clafer` Lake package. It treats
warnings as errors and rechecks every compiled project module with Lean's bundled
`leanchecker`, including examples and helpers not imported by the entrypoints.
Enforce `Clafer -> FormalCD -> DPGraph -> Mathlib`, including transitive imports
through helpers and roots; exercise `import DPGraph` and its public names without
the upper layers. Reject uncovered project modules and reverse dependencies,
testing rejection as well as the permitted graph.
The shared check command must fail if any
validation stage fails. This includes the DP-graph definitions, proofs and examples.
Run module discovery and its Python regressions before toolchain/dependency setup;
make that preflight available separately for development feedback. Report elapsed
time for build, kernel-check and test stages, identifying every kernel-checked
module in the output. Batch module builds and deduplicate overlapping kernel-check
targets while retaining the complete discovered inventory. Preflight success does not satisfy
the full validation requirement for Lean, build, validation or other executable changes.
After building, run the declaration/axiom audit and Lean/Python regression tests
before the more expensive kernel replay. Any failed gate stops later stages;
successful validation still requires the complete kernel check.
An explicitly configured factory documentation check may instead run source-inventory
preflight, its Python regressions and changed-document checks when a complete
file-content and mode comparison with the frozen baseline proves that only
`README.md` or Markdown beneath `docs/` changed. Deletions and additions participate
in that comparison. Other paths, executable modes, symlinks, an unavailable baseline
or uncertain classification require full validation. Preserve the baseline identity
and selected check in evidence. This exception does not claim new Lean validation:
IntentBond tracing, source matching and independent read-only semantic review
remain required, including review of changed mathematical claims and requirements.
Keep artifact caching disabled for the project package so each isolated check
rebuilds candidate modules. Deployment-managed dependency caches may reuse pinned
dependency artifacts without replacing any build, kernel or audit gate.
Include the pushout-cocone dependency in the optional Mathlib cache prefetch;
cache failure must retain the complete pinned source-build fallback.
Audit declarations by their originating project modules, including private and
generated declarations regardless of namespace, with complete `import all`
coverage. Reject unsafe/partial definitions, new axioms and transitive axiom
dependencies outside `propext`, `Classical.choice` and `Quot.sound`; report these
standard axioms separately. Reject an empty audit or one missing actual DPGraph
declarations. Zero declarations in a future root only indicate scaffolding.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, itest

## IntentBond on every contribution
`req~intentbond-workflow~1`

Agent instructions require the pinned IntentBond development skill. The repository
maintains intent and requirements with OFT links and a nonempty scope. CI checks
pull requests using the base branch's scope and retains evidence; first adoption
explicitly checks the candidate baseline and requires review. Exit 4 retains
semantic review as pending. Failed checks block the CI job.
The explicitly approved public-root migration expands only baseline `inputs`
and `review_paths` to `["."]`, preserving every other policy field and the actual
baseline commit. CI recognizes the exact original and migrated scope identities,
derives the expansion from the baseline and rejects arbitrary candidate policy
changes. Retain both identities and the transformation for independent review.

Covers:
- `intent~traceable-contributions~1`

Needs: impl

## GitHub planning and tracking
`req~github-tracking~1`

Agents plan work as GitHub issues in the configured Project. The ticket helper
creates issues from body files, adds them to the Project, sets their status, and
supports later edits, comments, and closure. GitHub operation failures must be
reported as failures; if issue creation succeeds before Project tracking fails,
the helper reports the created URL so tracking can be retried without recreation.
Planning tickets do not authorize starting semantic implementation.

Covers:
- `intent~traceable-contributions~1`

Needs: impl, utest

## Focused public project documentation
`req~public-foundation~1`

The repository keeps its MIT license and provides contribution and
private security-reporting guidance, issue/PR templates, a brief README, and links
to the SoSyM publication, free preprint, and maintained Haskell implementation.
It distinguishes repository `kbak/clafer-lean` from its single Lake package
`clafer`, with sibling public `DPGraph`, `FormalCD` and `Clafer` roots and the
dependency direction above. It distinguishes the delivered B.1 Definitions 1–5,
Theorems 1–2 and B.2.1–2 span operations (with the adopted Q1 reduction law),
B.4 Definitions 6–10 foundation, abstract B.5 model reduct and selected
Table 3/A.1 predicates (including the Q8 correction) over a bounded semantic
graph, and the first FormalCD structure/name-preserving morphisms, from future
predicates, all-universes SetMap, semantic self-instantiation and the remaining
Clafer expression/compilation/gluing increments. It documents the delivered
resolved AST, constraint boundary, individual Shapes and MCS structural discipline.
It keeps private deployment configuration and credentials outside the source repository. Keep
[intent](intent.md) as the canonical overview, linking current architecture,
mathematical explanations, source citations, requirements and trace artifacts.
Follow the [documentation policy](../AGENTS.md#documentation): change comparisons
belong in PR descriptions and acceptance/execution evidence in external factory
artifacts. Retain controller-required historical snapshots and a concise current
plan until the retention policy permits removal.

Covers:
- `intent~formalization-foundation~1`

Needs: impl

## Source audit and three-layer roadmap
`req~formalization-roadmap~1`

Maintain the three reusable layers and explicit exclusions in [intent](intent.md),
the source-to-construct mapping in [SOURCES](SOURCES.md), and representation
alternatives, dependencies and validation tasks in [architecture](ARCHITECTURE.md).
SoSyM is the primary semantic authority; identify exact sections/definitions/figures,
the inspected preprint hash and Mathlib commit. Distinguish inspected full texts
and recovered-page subsets from abstracts, snippets and unavailable sources.
Record disagreements before selecting meanings; the compiler is supplementary
context and any use as evidence requires an immutable revision and a license check.

Acceptance of roadmap/source-audit issue [#2](https://github.com/kbak/clafer-lean/issues/2)
requires all of the following:

- Three phase milestones and a dependency-ordered backlog in the existing Project,
  linked from the maintained architecture.
- A source map with exact locators and the Mathlib pin, without compiler-driven semantics.
- A cross-check of all nine architectural decision areas, with alternatives,
  delivered evidence and explicit remaining validation tasks assigned to live issues.
- Honest available-source audit limits and dispositions of source disagreements,
  including gaps in 2003/2000 source coverage; recording a limit does not
  complete the missing-source research.
- PR review of maintained documentation, this scoped requirement and trace links.
  Research progress alone is not acceptance. Keep #2 Open / In Progress until
  its deliverables are accepted and the implementing PR is merged, preserving
  its earlier discussion.

Distinguish proposed, proved and deferred theorem statements. This research
requirement adds no Lean theorem or mathematical implementation obligation;
later semantic increments require their own authorized scope. The existing
validation, IntentBond and GitHub-tracking requirements continue to apply.
Project-critical source research and the conditional sketch-extension assessment
are tracked by [#41](https://github.com/kbak/clafer-lean/issues/41) after #2 closes.

Covers:
- `intent~formalization-foundation~1`
- `intent~traceable-contributions~1`

Needs: impl

## Supporting-source and coherence research
`req~supporting-source-research~1`

Maintain the bounded assessment authorized by
[#41](https://github.com/kbak/clafer-lean/issues/41), with SoSyM B.4 Definitions
7–10 and B.5 Theorem 3 as the semantic reference. Compare the inspected Diskin
& Wolter §4.1–3 signature dependencies, declaration closure, typed-instance
satisfaction and pullback coherence with the actual `Signature`, `Interpretation`
and reduct laws. Distinguish precomposition equalities from coherent
isomorphisms for chosen pullback reducts; assert no unproved equivalence of the
model representations and add no semantic or dependency change through this audit.

Record exact inspected statements, source/version identities and the limits of
browser excerpts, recovered-page subsets and acquired complete files. For partial
collections, record file/page hashes, page gaps and which claims are supported;
do not treat recovered passages as uninspected or missing passages as audited.
Bound acquisition by the claims required for an active increment. Use accessible
primary alternatives when they establish the exact needed statement, recording
its applicability limits. The unread 2003 keyed-sketch material and missing 2000
universal-arrow pages remain explicit audit limits; further acquisition is
deferred unless a named necessary claim lacks adequate primary evidence.
Review this disposition with #41's assessment. Record hashes and locators for acquired
files, and retain failed-route evidence outside living documentation. Abstracts,
snippets and indexed PDF results do not establish a technical audit.
Assess accessible alternative Diskin sources by their exact statements and
applicability limits, without treating them as the missing full texts or as an
implicit choice of Clafer label identity.

Bound the Lean-library search by queries, inspected source trees and immutable
candidate revisions. Distinguish relevant foundations from a ready-made sketch
package, and static inspection from compatibility verified by building. Preserve
the adopted pins and separately review any future extension, adapter and license.
Keep source limits, architecture, canonical intent and trace links consistent.
Compare ordinary graph arities, marker-bearing arities and dependency-category
signatures; state the extra closure, preservation and semantic-consistency
obligations without importing them into the delivered API. Check proposed
dependencies against the actual bag-sensitive key and existing counterexamples.
This documentation requirement adds no Lean proof obligation. Acceptance requires
the bounded assessment and a reviewed disposition of remaining necessary claims;
a missing paper alone does not block an independently justified increment.

Covers:
- `intent~formalization-foundation~1`
- `intent~traceable-contributions~1`

Needs: impl

## Graphs, signatures and typed declarations
`req~dpgraph-core~1`

Implement SoSyM Appendix B.4, Definitions 6–9, using Mathlib `Quiver`,
`Prefunctor` and bundled `CategoryTheory.Quiv`, with explicit independent symbol,
arity vertex/arrow and carrier vertex/arrow universe parameters. Pin Mathlib to
56a005855ea17e0b0958f73ec801ae140b0a1679 and preserve Lean v4.35.0. A signature
maps symbols to arity graphs; a formula pairs a symbol with a graph morphism from
its arity to the carrier; a DP-graph has a carrier and a `Set` of typed formulas.
Retain repeated arguments and isolated arity vertices. Do not impose categorical
structure on carrier arrows, global finiteness, decidable equality or dependency
closure. Explain the total-edge/dependent-sum correspondence. Provide the
independently importable `DPGraph` with no FormalCD/Clafer dependencies.

Covers:
- `intent~formalization-foundation~1`

Needs: impl

## Formula translation laws
`req~formula-translation~1`

For a fixed signature, translate a formula by postcomposing its arity-to-carrier
map with a graph morphism (SoSyM B.4, Definition 10). Prove translation preserves
identity and composition for arbitrary well-typed formulas and graph maps.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Declaration-preserving morphisms
`req~dpgraph-morphisms~1`

A DP morphism is a graph morphism with a proof that translation maps every
source declaration to a target declaration (SoSyM B.4, Definition 10).
For a fixed signature, provide identity and composition, prove their declaration
preservation, associativity and both unit laws, and provide extensionality from
the underlying graph map and its vertex/arrow actions. Reuse `Prefunctor` laws.
There is no injectivity requirement and no inference-closure condition.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Finite witnesses and failed preservation
`req~dpgraph-examples~1`

Construct a finite arity with two distinct parallel arrows and an isolated vertex,
a nonempty source declaration set and an explicitly described target declaration.
Give a nonidentity DP morphism identifying those arrows; prove distinctness,
equal images and declaration preservation. Apply the translation-composition
theorem to explicit composable maps. Exercise the isolated vertex's binding.
Provide a graph map to a carrier whose required declaration is absent and prove
that it cannot be equipped with a DP preservation proof. All these examples must
compile independently of FormalCD/Clafer. Their syntax-only predicate names carry
no unproved meaning; they do not implement SetMap or Theorem 3. Finiteness is
local to these examples, not a restriction on the core.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Fixed-signature category
`req~dpgraph-category~1`

For each signature and fixed carrier vertex/arrow universes, provide a Mathlib
`Category` instance on DP-graphs using exactly the existing `Hom`, identity and
composition from B.4 Definitions 9–10. Reuse their associativity, unit laws and
extensionality. Keep carrier arrows as arbitrary quiver arrows; the category
structure concerns maps between DP-graphs. Expose it through `import DPGraph`.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Abstract interpretation and satisfaction
`req~dpgraph-interpretation~1`

An interpretation for a fixed signature and semantic graph assigns each symbol
a set of graph maps from its arity to that semantic graph. Derive satisfaction
of a formula under a carrier-to-semantic-graph map by composing the formula's
binding with that map and testing membership in the symbol's meaning. Derive
the model predicate by requiring every declaration to be satisfied.
Prove the satisfaction condition under translation: for any graph map `F : G → H`,
formula `φ` on `G` and map `m : H → Ω`, satisfaction of `translate φ F` by `m`
is equivalent to satisfaction of `φ` by `F ; m`.

Keep semantic vertex and arrow universes independent of signature and carrier
universes. This abstract interface does not select concrete span predicate
interpretations. No all-universes SetMap object, resizing axioms, solver or
executable instance generation are included.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Contravariant model reduct
`req~dpgraph-model-reduct~1`

For a fixed interpretation, a declaration-preserving DP morphism `F : S → T`
and a `T`-model `m`, prove that precomposition `F ; m` is an `S`-model, the
abstract form of SoSyM B.5 Theorem 3. Provide restriction on models retaining
their underlying maps, and prove identity and composition laws:
`reduct (id S) m = m` and `reduct (F ; J) m = reduct F (reduct J m)`.

State the exact assumptions: a semantic graph, meanings on arity diagrams,
declaration preservation by `F`, and satisfaction of the target declarations.
No additional closure/invariance properties of meanings are assumed. Do not
claim reflection of whole-model satisfaction or preservation by arbitrary graph
maps, nor concrete SetMap semantics before those interpretations are supplied.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Model reduct injectivity
`req~model-reduct-injective~1`

For any `I : Interpretation σ Ω`, `F : Hom S T` and `J : Hom T S`, prove
`Function.Injective (I.reduct F)` from `J.comp F = Hom.id T`, with independent
signature, source/target carrier and semantic universes. Expose
`Interpretation.reduct_injective_of_comp_eq_id` through `import DPGraph`.
This is a derived library consequence of the existing reduct laws, grounded in
SoSyM B.4 Definitions 9–10 and the abstract B.5 Theorem 3, not a verbatim paper
theorem or concrete Clafer/span semantics. Require no finiteness, decidable
equality, interpretation invariance or injectivity assumptions, and assert no
whole-model reflection for arbitrary DP morphisms.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Model reduct surjectivity
`req~model-reduct-surjective~1`

For any `I : Interpretation σ Ω`, `F : Hom S T` and `J : Hom T S`, prove
`Function.Surjective (I.reduct F)` from `F.comp J = Hom.id S`, with independent
signature, source/target carrier and semantic universes. Expose
`Interpretation.reduct_surjective_of_comp_eq_id` through `import DPGraph`.
This is a derived library consequence of the existing reduct laws, grounded in
SoSyM B.4 Definitions 9–10 and the abstract B.5 Theorem 3, not a verbatim paper
theorem or concrete Clafer/span semantics. Require no finiteness, decidable
equality, interpretation invariance or injectivity assumptions, and assert no
whole-model reflection for arbitrary DP morphisms.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Interpreted witnesses
`req~dpgraph-semantics-examples~1`

Exercise a nonempty signature and declaration set with an explicit predicate
meaning that has both satisfying and failing diagrams. Construct a target model
and its reduct along a nonidentity DP morphism; exercise reduct identity and
composition through category notation. Exhibit the failure of restriction by a
bare graph map and the failure of whole-model reflection. Include an example
with semantic vertex and arrow universes larger than the syntax universes.
Example meanings are illustrative and do not claim the paper's concrete span
predicates. Keep all assertions kernel checked.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Link-preserving spans and isomorphisms
`req~span-representation~1`

Implement SoSyM B.1 Definitions 1–5 within DPGraph: a span from `A : Type u`
to `B : Type v` has a head `L : Type w` and total source/target functions.
The three universes are independent; distinct links may have equal endpoints.
An isomorphism is a head equivalence commuting with both legs, including across
head universes. Supply identity, symmetry and transitivity operations.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Span and indexed-family correspondence
`req~span-family-correspondence~1`

Represent indexed mappings by `I : A → Type w` and evaluation `∀ a, I a → B`.
Equivalence is fiberwise index equivalence preserving evaluation. Convert spans
to source fibers and families to heads `Σ a, I a`, in `Type (max u w)`.
Prove both roundtrips up to their respective equivalences, permitting the raised
head/index universes. Establish B.1 Theorem 1 through endpoint-membership equality:
span reduction is existence of a link with the given endpoints, and family
reduction is existence of an index evaluating to the target. Neither representation
requires finite indices or decidable equality.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Set-valued spans and relation reduction
`req~span-set-valuedness~1`

For SoSyM B.1 Theorem 2, a relation span has head
`{p : A × B // R p.1 p.2}` in `Type (max u v)`. Prove joint endpoint injectivity
iff every source fiber's target evaluation is injective, and iff a span is
isomorphic to the relation span of its existential reduction. Supply the
relation roundtrip by endpoint membership, preserving empty relations/fibers.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Pullback span composition and laws
`req~span-composition~1`

Implement SoSyM B.2.1 source-to-target composition with head
`{p : Lq × Lr // tq p.1 = sr p.2}`, in the join of the link universes.
Preserve every composable link pair. Prove compatibility with indexed-family
composition, whose indices at `a` are `Σ i : I a, J (f a i)`.
The identity has head `A` and identity legs. Supply endpoint-preserving left/right
unit isomorphisms and the canonical associator `((l,m),n) ↔ (l,(m,n))`, with
explicit universe joins; no strict equality of differently represented heads
is required. No finiteness or decidable equality is assumed.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Span inversion
`req~span-inversion~1`

Implement SoSyM B.2.2 inversion by retaining the head and swapping the legs.
Prove involution and that reduction is relational converse. This operation
asserts no categorical invertibility of arbitrary spans.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Relation composition: adopted Q1 correction
`req~span-relation-composition~1`

Adopt the [Q1 correction](SOURCES.md#span-composition-q1-research-for-4) to
SoSyM B.2.1: for arbitrary spans `red(q ⋆ r) = red(q) ; red(r)`, where `;`
is existential relational composition in source-to-target order. Require no
finiteness, decidable equality or injectivity. Prove the canonical map from
composite links to the right-hand relation span is surjective, and existence
of a span isomorphism to it iff the outer endpoint map is injective.
For relational inputs, characterize this injectivity by at most one intermediate
object per outer endpoint pair. Prove sufficient cases: the first relation is
single-valued, or the converse of the second is single-valued; neither requires
totality. Uniqueness of intermediate objects alone does not suffice for arbitrary
spans, nor does single-valuedness of the second relation for relational inputs.
This correction is selected semantics, not a verbatim paper theorem.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Span witnesses and universe boundaries
`req~span-examples~1`

Provide kernel-checked examples of parallel links with identical endpoints;
empty spans and fibers; and relational inputs with two intermediate objects,
two composite links and only one reduced endpoint pair. Prove that the latter
composite is not isomorphic to the reduced relation span, even though its second
relation is single-valued. Include a parallel-input-link example where uniqueness
of the intermediate object fails to imply the stronger isomorphism. Exercise
conversions, unit/associativity laws and relation criteria at differing universe
levels. Expose the generic API via independent `import DPGraph`; examples remain
separate modules covered by the full build, kernel and axiom audits.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Bounded semantic graph
`req~setmap-semantic-graph~1`

Provide a graph over an ambient `U : Type u` whose vertices are subsets `A : Set U`
and arrows are existing spans between subtype carriers. Links live in an explicit
universe containing u (chosen as `max u w`); state vertex universe u and arrow
universe `max u w + 1`. Shared underlying objects retain their identity across
subsets. Reuse Quiv/Prefunctor without a category on span arrows, resizing or an
all-universes SetMap. Preserve unrestricted Span and Interpretation universes.
Exercise a larger link universe through the concrete interpretation.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Separate typed predicate arities
`req~predicate-arities~1`

Declare the selected Table 3/A.1 symbols with real arity quivers, separately
from meanings. Inverse has opposite arrows, commutation a triangle, key an
n-member common-source family, and cover/disjointness an n-member common-target
family. Unary maps and multiplicities have one-arrow arities; multiplicity
symbols carry a natural lower bound and finite natural or unbounded upper bound.
Retain the isolated central vertex for n=0 and repeated graph-map argument
bindings. Impose no global finiteness, decidable equality or implicit set-valued
default. Catalogue VC, naming/arity disciplines, arbitrary path equations beyond
the triangle and later FormalCD/Clafer-specific predicates as outside this generic
built-in vocabulary. FormalCD extensions supply nd/ad and the selected VC.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Inverse predicate
`req~predicate-inverse~1`

Interpret Table 3 inverse using B.1 Definition 2 and B.2.2: for opposite spans
q and r, require inhabited `Span.Iso q.inverse r`. This is leg-swapping, not a
categorical inverse equation. Prove symmetry and invariance under independent
endpoint-preserving relabelings of both link types, including across universes.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Triangle commutation
`req~predicate-commutation~1`

Interpret Table 3 equality as inhabited `Span.Iso (q.comp r) s` for a typed
triangle. Preserve every composable link pair and the continuing Q1 reduction
law. Prove invariance under relabeling all three spans. Exhibit relabeled
satisfying triangles and a two-composite-link/one-direct-link triangle whose
reduced relations agree but which fails commutation.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Bag-sensitive finite-family keys
`req~predicate-key~1`

A common-source finite family is a key exactly when target-preserving
equivalences between every pair of corresponding source fibers imply equality
of the two source objects. Compare full bags, retaining repeated values, with
no implicit totality, single-valuedness or set-valuedness assumption (Figure 21c).
Prove endpoint-preserving link-isomorphism invariance. Prove zero-member key
is equivalent to a subsingleton source. Check a key distinguishing bags with
identical support but different multiplicities and a failing key with equal
complete bag tuples at distinct sources.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Ordinary-key correspondence and repeated marriages
`req~predicate-key-functional~1`

Derive an ordinary-function specialization of `req~predicate-key~1` without
changing its unrestricted `Key`/`BagEquiv` meaning. Represent each function
`f i : A → B i` by a span with exactly one outgoing link at every source.
For every finite arity `n`, prove both directions of
`Key (fun i => Span.ofFunction (f i)) ↔ Function.Injective (fun a i => f i a)`.
For arbitrary span families, assume `Total` and `SingleValued` componentwise,
define their unique target values and prove the corresponding tuple-injectivity
equivalence, with justified link-preserving functional-span isomorphisms.
Set-valuedness alone does not provide a unique total value. Preserve independent
source, target and link universes; impose no inhabitance, finiteness or decidable
equality on the source or targets. Include zero arity, consistently with
`key_zero`, and empty/subsingleton sources.

Check a finite witness with two distinct marriages sharing wife and husband
values but having different dates: the spouse pair fails `Key` and the
spouse/date triple satisfies it. This establishes only that finite predicate
witness, not an unrestricted real-world marriage identity rule. Preserve the
existing multiplicity-sensitive, identical-support and equal-bag counterexamples.
Keep results independently available through `import DPGraph`, with examples
built and kernel checked by the existing module-discovery runner.

Primary semantics: SoSyM B.1 Definitions 1–5 / Theorems 1–2, Table 3 key and
Figure 21c. Supporting comparison: Diskin, Kadish, Piessens & Johnson (2000),
*Universal Arrow Foundations for Visual Modeling*, DOI 10.1007/3-540-44590-0_30,
§2.1 p. 348 (separating family / injective tuple), §3.3 pp. 353–354 / Figure 1
and §3.5 p. 356 (marriage key). These are derived library results under explicit
hypotheses; the 2000 set-valued notation is not identified with all SoSyM spans.
See the [partial-source assessment](SOURCES.md#universal-arrow-foundations-partial-source-assessment)
and [#44](https://github.com/kbak/clafer-lean/issues/44).

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Covering common-target families
`req~predicate-cover~1`

Interpret Table 3 cover and §6.1.2 as every target object being reached by a
link in some family member. Permit bag-valued arrows. Prove invariance under
link isomorphisms and that zero-member cover is equivalent to an empty target.
Check positive and negative cover, repeated bindings and empty domains.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Disjoint images: accepted Q8 correction
`req~predicate-disjointness~1`

Use §6.1.2/Figure 21 common-target family maps: for distinct indices i and j,
no target value is reached by both maps. Table 3's common-source shape and
source-inequality condition are errors, not a second supported predicate.
Shared source objects do not exempt overlap. Permit bag-valued arguments and
prove link-isomorphism invariance and vacuity for zero-member families.
Check disjoint images, overlap, repeated nonempty inclusion bindings and empty
domains. Record the accepted interpretation and exact source locators.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Set-valued, total, single-valued and inclusion maps
`req~predicate-unary-maps~1`

Use B.1.4/Theorem 2 joint endpoint injectivity for set-valuedness; use A.1,
Table 2 and §6.1.1 source surjectivity for totality and source injectivity for
single-valuedness. Single-valuedness permits empty fibers and excludes duplicate
copies. Literal inclusion between subsets of U has a bijective source leg and
equal underlying source/target U values for every link. Prove each predicate
invariant under endpoint-preserving link isomorphism, the set-valued relation
characterization, total/nonempty-fiber and single-valued/subsingleton-fiber
characterizations, and inclusion's subset and identity consequences. Check a
literal and empty inclusion, a moving injective permutation and duplicate
identity links; existence of an injection alone does not imply inclusion.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Cardinal multiplicity bounds on links
`req~predicate-multiplicity~1`

Interpret Table 3 mult-trg/mult-src and B.1 indexed families by bounding each
outgoing/incoming link fiber, including repeated target/source values. Lower m
means an embedding from Fin m; finite upper n means an embedding into Fin n.
Unbounded upper * imposes no upper bound or local finiteness. Do not use a
natural cardinality that maps infinite types to zero. Prove isomorphism
invariance, source/target duality under inversion and agreement with distinct
reachable-value counts for set-valued spans. Check finite lower/upper boundaries,
empty fibers, repeated values, reversal and infinite fibers satisfying unbounded
ranges but failing every finite upper bound.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Concrete interpretation and generic model restriction
`req~predicate-interpretation~1`

Connect every symbol to its span meaning in the bounded semantic graph using
the existing Interpretation. Use delivered formula satisfaction, translation
and model reduct APIs. Demonstrate a satisfying concrete model, restriction
along a nonidentity declaration-preserving DP morphism, a rejected predicate
instance and explicit larger semantic link universes. Preserve the generic
interfaces and their lack of whole-model reflection.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Predicate acceptance witnesses
`req~predicate-examples~1`

Provide kernel-checked positive and negative witnesses for the complete selected
vocabulary: relabeled inverse/commutation; the Q1 two-path counterexample; one
versus two links with a repeated target; multiplicity-sensitive and failing
keys; cover/disjointness with repeated bindings, empty domains and zero-member
families whose central vertex survives; literal/empty inclusion and moving or
duplicated counterexamples; finite/empty/infinite ranges and reversal; concrete
formula translation and nonidentity model restriction; larger link universes.
Expose the reusable API through independent import DPGraph and keep examples
separate. The unchanged shared check must discover, build, kernel replay and
audit every added module; preserve warning enforcement, source export checks,
IntentBond coverage and independent semantic review. No solver is required.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Declaration unions on carrier cocones
`req~dpgraph-pushout-data~1`

For fixed-signature DP morphisms `F : Hom S T` and `J : Hom S U` at fixed
carrier vertex/arrow universes, a supplied carrier `PushoutCocone` determines a
DP-graph on its point. Declare exactly the union of the images of the left and
right declaration sets under formula translation by its two legs. Provide the
canonical declaration-preserving injections and their commuting DP-graph cocone.
Define compatible component models by equality of their reducts to `S`, keeping
semantic universes independent in that data type.

Expose `Pushout.CarrierCocone`, `obj`, `inl`, `inr`, `cocone` and `CompatibleModels` through
`import DPGraph`. These are derived constructions over SoSyM B.4 Definitions
9–10 and the abstract B.5 reduct, not concrete span, FormalCD or Clafer gluing.
Do not add finiteness, injectivity, inference closure or interpretation invariance.
The cocone data alone does not assert a universal property or model amalgamation.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof, itest

## Pushout universal property
`req~dpgraph-pushout-universal~1`

For `σ : Signature.{s, va, ua}`, `S T U : DPGraph.{s, va, ua, v, u} σ`,
`F : Hom S T`, `J : Hom S U`, `c : Pushout.CarrierCocone F J` and a supplied
`hc : CategoryTheory.Limits.IsColimit c`, provide
`noncomputable def Pushout.isColimit F J c hc : IsColimit (Pushout.cocone F J c)`.
Construct the DP mediator from the carrier universal property, prove preservation
of the union of translated declarations, both factorization equations and
uniqueness. Keep the explicit argument order `F J c hc` and expose the result
through `import DPGraph`. Its module `DPGraph.Pushout.Universal` independently
imports `DPGraph.Pushout.Basic`.

This is a derived result over the representation from SoSyM B.4 Definitions 9–10
and the abstract B.5 Theorem 3, not a verbatim paper claim. Keep signature
universes independent and carrier universes fixed; add no finiteness,
injectivity, semantic invariance, global pushout existence or model amalgamation
assumption. This requirement does not deliver a model equivalence.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof, itest

## Model amalgamation on a carrier pushout
`req~dpgraph-model-amalgamation~1`

For a signature in universes `s va ua`, fixed carrier universes `v u`,
`F : Hom S T`, `J : Hom S U`, `c : Pushout.CarrierCocone F J`,
`Ω : Quiv.{v,u}`, `I : Interpretation σ Ω` and `hc : IsColimit c`, provide
`Pushout.modelEquiv F J c I hc :
I.Model (Pushout.obj F J c) ≃ Pushout.CompatibleModels I F J`.
Its forward map must be exactly the pair of reducts along `Pushout.inl F J c`
and `Pushout.inr F J c`. Construct the inverse using the supplied carrier
colimit, prove that it satisfies the union of translated declarations, and
prove both inverse laws. Prove `Pushout.modelEquiv_fst F J c I hc m` and
`Pushout.modelEquiv_snd F J c I hc m`, with exactly that explicit argument order,
stating respectively
`(modelEquiv F J c I hc m).val.1 = I.reduct (Pushout.inl F J c) m` and
`(modelEquiv F J c I hc m).val.2 = I.reduct (Pushout.inr F J c) m`.

Implement this in `DPGraph/Pushout/Models.lean` importing `Pushout.Basic`
independently of any DP-graph universal-property proof, and expose it through
`import DPGraph`. The semantic universe restriction is local to this result;
preserve all existing interpretation and reduct declarations. This is a derived
result over SoSyM B.4 Definitions 9–10 and abstract B.5 Theorem 3, not a verbatim
paper claim. Require no finiteness, injectivity, semantic invariance or separate
model amalgamation assumption, and assert no global pushout existence or concrete
FormalCD/Clafer gluing.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof, itest

## FormalCD structure and semantic boundary
`req~formalcd-structure~1`

Expose reusable FormalCD modules through `import FormalCD`, depending on DPGraph
and never Clafer. Reuse Quiv/Prefunctor, DPGraph.Formula and a declaration Set
at a supported signature containing the built-in predicates, retaining
DPGraph.Predicates.signature as the original specialization. Annotate existing vertices/arrows with class/map
names, optional predefined identifiers and ordinary/bag/inclusion map modes.
Keep raw data independently inspectable from a WellFormed proposition and bundle
valid CDs with its proof. A shared registry provides stable identifiers, canonical
names and singleton/primitive kinds; entries are optional in each diagram.
Graph identities remain vertices/arrows, independent of their names. Preserve
typed bindings, repeated arguments and isolated arity vertices. Add no second
graph API, untyped arguments, formula identity tokens, dependency closure or
global finite/decidable assumptions.

WellFormed expresses syntactic/structural validity, not model existence or
satisfaction. Registry entries record identity/naming, not concrete primitive
or singleton domains. Generic models concern declared predicates under an explicit
interpretation. The metamodel-specific nd/ad meanings are specified below;
the selected VC extension is specified below. A general constraint language and
full object-diagram semantics remain future work.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## FormalCD naming and predefined identity
`req~formalcd-naming~1`

Require predefined classes to use their registry's canonical name and user-defined
class names to lie outside all registry-reserved names. Each selected predefined
identifier has at most one vertex realization. Inclusion arrows are named isA;
distinct inclusion arrows may share that name. Impose no global classifier-name
injectivity, inheritance acyclicity, compulsory predefined entries or map identity
based on names. Ground these obligations in SoSyM §6.1.1–3/Figure 21, distinguishing
the selected library representation from verbatim paper statements.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## FormalCD effective declarations
`req~formalcd-declarations~1`

Every inclusion-marked arrow must have its corresponding built-in inclusion
formula in the underlying DPGraph's effective declaration set. Every ordinary
map must have its corresponding setValued formula. Explicit bag mode adds no
implicit setValued obligation, but authors may explicitly declare it. Inclusion
is separate from bag mode and receives its semantic consequences from the existing
inclusion interpretation. Use the typed unary binding with the actual arrow and
its endpoints; do not replace typed formulas with a weaker arity predicate.
Preserve all authored declarations in one authoritative effective set. Membership
obligations in WellFormed suffice; generic DPGraph defaults/meanings are unchanged.
These are the accepted §6.1.1–3 defaults, with Figure 21c's bag exception.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## FormalCD name-preserving morphisms
`req~formalcd-morphisms~1`

At a shared registry and supported signature (including the original built-in
specialization), a morphism between independently
well-formed CDs is an existing declaration-preserving DPGraph.Hom together with
equality of class names, map names, optional predefined annotations and map modes
at mapped vertices/arrows. Preserve none versus some and ordinary versus bag versus
inclusion exactly. Require neither global carrier injectivity nor reflection of
extra target declarations. This is an adopted library specialization of B.4
Definition 10, not an extra theorem attributed verbatim to the paper.

Provide identity, composition, extensionality from the underlying DP map and graph
map, associativity and both units. Prove all metadata obligations close under
identity/composition and that forgetting to DPGraph.Hom respects both operations,
reusing DPGraph laws. Reuse the existing satisfaction/model reduct after forgetting,
with explicit interpretation, contravariant direction and its identity/composition
laws. Do not re-prove the general reduct or claim arbitrary DP maps preserve metadata.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## FormalCD acceptance witnesses
`req~formalcd-examples~1`

Keep examples separate from the public entrypoint and kernel check:

- A finite valid CD with two distinct isA inclusion arrows, their endpoints and
  required declarations; an ordinary map's set-valued default and an explicit bag
  without that default (also allowing an authored bag setValued declaration).
- Invalid reserved user naming, incorrect predefined naming, duplicate realization
  of a predefined identifier, missing inclusion/ordinary defaults and an invalid
  inclusion name.
- A nonidentity morphism, explicit composable maps and their laws; a declaration-
  preserving DP map between valid CDs that cannot lift because a name or mode changes.
- An actual concrete interpretation/model and restriction, plus failing satisfaction
  illustrating the separate semantic condition.

Preserve independent DPGraph import, module discovery, import-layer checks, warnings,
kernel replay, axiom audits and trace coverage. The Figure 21c acceptance
requirements below extend these witnesses, together with the complete Figure
21b and VC requirements. No sorry/admit, unchecked axioms, unsafe/partial mathematical declarations,
disabled warnings, skipped checks or weakened scope/coverage.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof


## Compatible signature extension
`req~formalcd-signature-extension~1`

Provide an injective inclusion of the built-in symbols with inverse arity graph
maps. Reuse DPGraph signatures, formulas and interpretations. Formula inclusion
must be injective and commute with translation; extension of interpretations must
restrict to the original meanings. Support independently bounded symbol, arity,
carrier, registry and semantic universes without narrowing DPGraph. Preserve the
original Raw/CD/Hom API and acceptance examples, ordinary/inclusion defaults,
bag behavior, optional registry metadata, forgetting, identity/composition and
model reduct laws at every supported common signature.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Figure 21c metamodel shape
`req~formalcd-metamodel-shape~1`

Construct the eleven-node, thirteen-arrow inventory in the source map as a typed
CD over an extended vocabulary. Retain distinct arrow identities despite equal
names. Include seven inclusions, five ordinary setValued defaults, total and
singleValued name/so/ta/pred annotations, total bag-valued args, two cover/disjoint
pairs and nd/ad/literal key declarations. Prove inventory, incidence and effective
declaration facts and local syntactic well-formedness. Distinguish the SING
metaclass, modeled class Sing and its object. Document inferred nd/ad bindings;
these must use existing figure incidence justified by the stated constraints.
No construction proof asserts semantic satisfaction or self-description.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Metamodel discipline meanings
`req~formalcd-metamodel-disciplines~1`

Give nd/ad mathematical meanings connected to the extended interpretation and
typed declarations. Name discipline checks canonical names of realized predefined
identifiers, user names outside the reserved set, optional-entry identity and kind
rules, inclusion names and compatible name restriction through the displayed
predefined inclusions. Impose no global classifier-name injectivity.

Arity discipline validates arbitrary candidate data against the selected symbol's
arity graph: every vertex image, both endpoints of every arrow, and a bijective
indexing of the actual args fiber by all arity arrows. Repeated argument values
are allowed. Explicit context supplies the signature, represented graph, registry,
name/identity interpretation, vertex images and occurrence indexing that the bare
graph does not recover. Missing, malformed and duplicated-index data can fail.
Derive the correspondence with existing typed Formula values in both directions.
The total args annotation separately excludes empty fibers; generic zero-arrow
arities remain legal. State the interpretation's bounded domain and universe joins.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Full graph-formula identity and projection limits
`req~formalcd-formula-identity~1`

Formula identity is the existing symbol and full binding. Prove extensionality
and a correspondence with valid raw binding data, including all vertex images
and indexed arrow actions. Distinct symbols, argument positions or isolated
vertex images can distinguish formulas. Retain repeated arguments.

Figure 21c's literal key(args,pred) uses the unchanged generic Key/BagEquiv meaning.
Its satisfaction is an additional instance condition. Check that bag projection
can forget positions and arrow-only projection can forget isolated vertices;
never quotient formulas by these projections or assert their injectivity without
hypotheses. Full-binding identity and the printed metamodel do not imply universal
realizability. The requirements below add the explicitly typed, signature/registry/universe-bounded
self-description statement, Figure 21b example and VC semantics. Add no self-containing
universe, resizing, unchecked casts or escape axioms.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Metamodel acceptance witnesses
`req~formalcd-metamodel-examples~1`

Kernel check the complete inventory/defaults, valid and invalid predefined/user
names and name restriction, invalid incidence and argument indexing, repeated
arguments, nontrivial symbol/binding identity, both projection failures, and the
zero-arrow/total-args boundary. Include a concrete nonempty extended interpretation
model. State which finite witnesses satisfy literal key and totality and which
fail, distinguishing fragments from whole metamodel instances. Preserve existing
examples, supported-signature morphism/reduct laws and independent public imports.
Run the unchanged shared validation and trusted trace checks without weakening
coverage, warnings, proofs or scope.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof


## Bounded syntactic self-description
`req~formalcd-bounded-self-description~1`

For SoSyM §6.1.3 / Figure 21c, provide a named checked representation and
well-formedness statement reusing Metamodel.diagram and wellFormed in
CDOver with its concrete built-in-plus-nd/ad vocabulary, SING registry and
explicit small syntax/registry universes. Reuse the inventory and full-binding
Candidate.formulaEquiv correspondence. Class, Map and Signature remain ordinary
data. Preserve indexed occurrences, isolated vertex images, zero-arrow formulas,
literal bag key and total-args limitations. This is a syntactic representation
result, not semantic self-instantiation or universal every-CD realizability;
it requires no new axiom or metamodel-instance assertion.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Complete Figure 21b example
`req~formalcd-figure21-example~1`

Construct Figure 21b / §6.1.1–3 with exactly Comp, ECU, Display, Int and five
arrow identities: i1:ECU→Comp, i2:Display→Comp, server:Display→ECU,
display:ECU→Display, version:Comp→Int. Both inclusions are named isA.
Register Int as a primitive with canonical name Int; do not require Sing or
other optional predefined entries. Preserve existing naming and map modes.
Use the compatible vocabulary extension for VC and full graph bindings.

The effective declaration set has exactly the twelve distinct formulas on p.19:
disjoint(i1,i2), cover(i1,i2), inverse(server,display), inclusion(i1), inclusion(i2),
0..5(display), 1..1(version), 0..1(server), VC(server,i1,i2,version), and
setValued(version), setValued(server), setValued(display). Multiplicities count
outgoing links. Explain total/single-valued notation via these bounds, retaining
Q8 common-target disjointness and existing span inverse meanings. Prove inventory,
incidence, declaration membership/distinctness, naming/default obligations and
syntactic well-formedness in the same CDOver family as the metamodel.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Corrected guarded VC semantics
`req~formalcd-vc-semantics~1`

Adopt Q7: display.version ≥ server.version, with equality allowed and an absent
server satisfying VC vacuously. Sources: Figure 8 line 9 and its accompanying
§4.2.3 discussion (p.8; §4.3 supplies configuration context on p.9), Figure 21a
OCL / §6.1.2, and Appendix F; retain the discrepancy with the adjacent reversed
prose in the source map. VC's arity has exactly the
server, i1, i2 and version arrows and all endpoints. Interpret its actual typed
formula through DPGraph.Interpretation over the existing bounded subset/span
graph, with an explicit integer realization/decoding and universe parameters.
Keep built-in meanings unchanged. Under inclusion and version 1..1 declarations,
prove correspondence with the guarded integer comparison. No True placeholder,
unconnected Boolean test, server-totality assumption, global primitive framework,
finiteness restriction or change to the generic predicate catalogue is allowed.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Figure 21b semantic witnesses
`req~formalcd-vc-witnesses~1`

Provide a concrete nonempty model satisfying all twelve effective declarations,
including inverse, cover/disjointness, multiplicities, defaults and VC, with
all integers explicitly realized. Kernel-check actual interpreted VC satisfaction
for a served display with a strictly greater version, equal versions, a strictly
lower version (failure), and an unserved display (success). Prove the eleven
other declarations still hold in the lower-version counterexample, isolating VC.
Show the unserved case satisfies 0..1 without falsely requiring totality.
Keep examples separate from public imports and distinguish whole Figure 21b
satisfaction from syntactic well-formedness and metamodel-instance claims.
Preserve all existing validation, trace coverage and dependency/toolchain pins.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Resolved 2014 Clafer syntax
`req~clafer-resolved-syntax~1`

Implement directly constructible deep containment syntax for the selected 2014
constructs in §5.3.1–5, §5.4–5, §6.2.2/Figure 22 and Appendix C/Figure 27.
Keep resolved declaration IDs separate from source/display names, preserving
identity when names repeat. Distinguish the synthetic root, selected predefined
primitive-domain declarations (int, string, bool), and user declarations. Include
basic/reference-set/reference-bag forms, optional super IDs, abstractness and
both clafer and group multiplicities, with natural lower bounds and finite or
unbounded upper bounds. Input is already resolved and defaulted: retain authored
values separately, validate explicit overrides, default 1..1 clafer bounds,
keyword-induced optional children, and default 0..* or inherited group bounds.
Retain inherited keyword provenance. No parser, name resolver or elaboration
correctness theorem is promised.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Selected Clafer input well-formedness
`req~clafer-input-wellformedness~1`

State and check Clafer-local conditions from §5.3.4–5, §5.4–5 and §6.2.2:
unique resolved IDs, a distinguished parentless basic synthetic root with no
super, resolved parent/target/super edges, parentless non-root declarations
abstract, and nested abstractness confined to abstract containment. Primitive
domains are unique predefined basic declarations parented by the root, with
canonical names and no super. Require valid effective intervals and consistency
of authored/defaulted values. Enforce §5.5's kind restrictions and equal parents
when the super has a parent. Rule out containment and inheritance cycles using
the deep containment representation and explicit depth/rank conditions. These
conditions do not strengthen FormalCD or DPGraph. Supply a well-formed mixed
model with basic, set, bag, top-level abstract basic/reference and nested abstract
cases, plus rejected malformed or uninhabitable witnesses for important boundaries.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Constraint and binder input boundary
`req~clafer-constraint-boundary~1`

Expose a resolved declaration context and a finite indexed bag of referenced
scope occurrences for each constraint (§6.2.2/Figure 22). Preserve repeated
references in different positions; context is recorded separately. Provide
separate binder IDs, display names and resolved domain occurrences as the input
interface for #21, validating known IDs and unique binder IDs per boundary.
Constraint bodies, expression typing, resolution rules and Appendix D semantic
equations remain on #21. The context module must not depend on that future
implementation. Check repeated-occurrence and dangling-reference examples.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Individual Clafer Shapes
`req~clafer-individual-shapes~1`

Represent Figure 16/Table 4 and §6.2.3's individual Shapes as typed role graphs
using the existing graph/CD foundations. The head class is always present;
source requires a parent and target requires a reference kind. Give head
(source→head), parent (head→source), dereference (head→target) and target
(source→target) maps exactly when their endpoints exist. Supply finite,
kind-indexed role inventories and incidence proofs. When a super is selected,
head inclusion is required and source/target inclusions exist exactly for shared
endpoints; absent supers supply no inclusion family.

Apply the accepted #3 source correction: §5.3.4 (p.14) incorrectly excludes the
head of a top-level abstract clafer, contrary to §6.2.3 (p.20) and Figure 23's
total head role. Retain the head and omit source/parent-dependent maps. An
abstract reference retains target and dereference. Read Table 7's basic-source
statement with this exception. Preserve publication and historical snapshots.

Use existing predicates for local inverse, triangle, effective multiplicities,
ordinary set defaults and the set-reference projection key when its endpoints
exist. Bag target maps have bag mode. Expose local diagrams as well-formed
FormalCDs without claiming model existence, full MCS invariants, global cojoining
or gluing. Include positive basic/set/bag/abstract examples and impossible
incidence/absent-role cases.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Finite syntax and compilation termination basis
`req~clafer-finite-traversal~1`

Keep finiteness local to the Clafer input and role presentation. Provide a finite
indexing of all traversed declarations and a structural fold on containment,
with a decreasing child measure and well-founded resolved parent traversal.
Reference IDs are not recursive children; cyclic references must not prevent
finite traversal. Prove finite class/map-role carriers. This is a basis for
future terminating compilation (#22), not a parser, compiler correctness or
full MCS theorem. Preserve independent generic DPGraph imports.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof


## MCS metamodel and ownership
`req~clafer-mcs-metamodel~1`

Encode SoSyM §6.2.3/Figure 23 with the existing graph/formula and FormalCD APIs:
Role, ClassRole, MapRole, InclRole, String, PredefStr, Formula, Signature and the
Clafer owner; the cover/disjoint partition; labels, endpoints, slots and formulas.
Preserve the accepted correction from source `1` to `0..1` on the four ordinary-map
and three inclusion-role associations, meaning unique ownership within each
association's image. Shape guards require exactly the applicable slots. Retain
literal head-class source `1` and formula source `1`. Distinguish local slots,
role-graph identities, resolved class/map referents and displayed names. Do not
identify parent/dref/isA arrows by repeated strings. Keep the head of every clafer,
including top-level abstracts. Gluing congruence remains on #23.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## Complete Appendix E structural discipline
`req~clafer-mcs-disciplines~1`

Implement the complete applicable Tables 5–8 inventory and accepted Q2 expansion
in [the MCS inventory](mcs-invariants.md). Use typed incidence and exact existing
Shape presence guards; express cojoining at role-graph vertex identity. Include
both endpoints of all four ordinary roles and three guarded super roles, root,
every supported primitive domain, basic/set/bag and parentless abstract cases.
Missing source/target endpoints forbid the corresponding inclusion slot. Enforce
head/parent/dref/target and inclusion naming, both directions of Sing and all
primitive naming equivalences, and the target-name equation derived via the head
map. Bundle each discipline once as a proposition, without inconsistent duplicate
invariant fields. Preserve resolved hierarchy/kind restrictions at the structural
family boundary. Supply nonempty composed shapes with proved obligations,
including inherited roles, absent roles and distinct same-name arrows.
This is a structural MCS representation, not an AST compiler or model-existence
claim; #22 owns conversion from the already resolved AST and formula generation.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof

## MCS formula bindings and literal constraints
`req~clafer-mcs-formulas~1`

Formula objects have one owner, a symbol and a complete well-typed graph binding,
retaining isolated vertices and repeated argument occurrences. Preserve the
literal bag key on `(args,pred)` separately from full binding identity and from
total args. Bag equality may permute occurrences; it is not indexed equality.
Zero-arrow arities remain legal in the generic formula API but cannot occur in
an MCS formula bank satisfying the printed total-args condition. Demonstrate
accepted repeated occurrences and rejection of duplicate-key formula objects.
Expose a DP-graph declaration set and transport existing local Shape declarations
without inventing a constraint language or asserting compiler completeness.
Keep those later obligations separate from structural validity.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, proof
