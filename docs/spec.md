# Foundation and DP-graph requirements

These requirements cover the repository infrastructure and the delivered
DP-graph slice. FormalCD, structural Clafer and predicate semantics remain later
work; future definitions and theorems need scoped requirements and source links.

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
dependency direction above. It distinguishes the delivered B.4 Definitions 6–10
foundation from future FormalCD/Clafer implementations and keeps private deployment configuration and credentials outside the
source repository.

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
