# Foundation and DP-graph requirements

These requirements cover the repository infrastructure and the delivered
span operations, DP-graph category and abstract model reduct. FormalCD, structural Clafer and
concrete predicate semantics remain later work; future definitions and theorems
need scoped requirements and source links.

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
the full validation requirement.
Keep artifact caching disabled for the project package so each isolated check
rebuilds candidate modules. Deployment-managed dependency caches may reuse pinned
dependency artifacts without replacing any build, kernel or audit gate.
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
B.4 Definitions 6–10 foundation and abstract B.5 model reduct from future
concrete predicate interpretations, SetMap and
FormalCD/Clafer implementations and keeps private deployment
configuration and credentials outside the source repository. Keep
[intent](intent.md) as the canonical overview, linking current architecture,
mathematical explanations, source citations, requirements and trace artifacts.
Follow the [documentation policy](../AGENTS.md#documentation): change comparisons
belong in PR descriptions and acceptance/execution evidence in external factory
artifacts. Retain controller-required historical snapshots and a concise current
plan until the retention policy permits removal.

Covers:
- `intent~formalization-foundation~1`

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
