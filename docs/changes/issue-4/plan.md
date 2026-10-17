# Implementation plan for issue #4

Status: implementation complete. The submitted specification adopts the Q1
correction; the frozen intent/specification retain their historical proposal
wording. Candidate validation and independent semantic review remain handoff gates.

## Baseline and dependencies

Selected repository: kbak/clafer-lean. Catalog and live main matched cabcf18abf231a4aac510d8f9996110ff2d8db09 during preparation. Configured scope comes from 0b9599e89417d9f9ea8c39170fff4af15cd02ab3:scope.json; current root scope has the same obligations. Keep issue #4 open through acceptance and merge. The coordinator owns GitHub issue/Project updates.

Read AGENTS.md, CLAUDE.md, CONTRIBUTING.md, canonical docs/intent.md, affected docs/spec.md, docs/ARCHITECTURE.md, docs/SOURCES.md, docs/traceability.md, and #2/#13/#16. #15's abstract interpretation is already delivered. #16 predicate choices are outside this task.

## Work order and affected files

1. [x] Record the adopted Q1 correction and refine scoped mathematical requirements before compatibility theorems. Update docs/spec.md, docs/SOURCES.md and the coordinator's issue tracking as authorized; retain the issue body/comment identities in external evidence.
2. [x] Add DPGraph/Span/Basic.lean for spans, cross-universe isomorphisms, reduction and inversion; DPGraph/Span/IndexedFamily.lean for families, equivalences and conversions. Reduction is in Basic so the family correspondence can use it without a dependency cycle.
3. [x] Add DPGraph/Span/Composition.lean for pullback heads, identity and canonical unit/associator equivalences, and the family-composition correspondence.
4. [x] Add DPGraph/Span/Relation.lean for relation spans, set-valuedness, the reduction/composition law and exact injectivity criterion. Avoid an import cycle between composition and relation modules. Document all assumptions explicitly.
5. [x] Add DPGraph/Span/Examples.lean with the positive/negative and universe witnesses. Add DPGraph/Span.lean as the public facade and expose it through DPGraph.lean. Extend tests/public_imports.lean with actual independent API uses. Keep discovery and audit enforcement unchanged; extend the exact expected inventory in tests/test_project_modules.py to include the six new modules. This updates the regression fixture to the delivered module set.
6. [x] Extend docs/dpgraph-trace.md with named implementation and proof artifacts; link exact declarations. Update the delivered-scope statements in docs/intent.md, docs/ARCHITECTURE.md, docs/SOURCES.md, README.md and CONTRIBUTING.md only as needed. Keep source citations and the distinction from future predicate/SetMap semantics.
7. [ ] Run the supplied IntentBond feedback wrapper against review base cabcf18abf231a4aac510d8f9996110ff2d8db09 and inspect the complete diff and evidence. Leave changes uncommitted under the factory implementation workflow; the coordinator owns final commit verification, independent semantic review and draft publication with Closes #4. This updates the original commit/publication step to the dispatched worker boundary.

## Risks and verification focus

- Fiber/sigma heads can raise universe bounds. Cross-universe head equivalences and compiled mixed-universe examples must demonstrate the intended generality.
- Proof irrelevance for equality witnesses must not erase actual link identity. Check the two-path and parallel-link counterexamples at the span level.
- Isomorphism must preserve endpoints, not merely head cardinality. The exact composite criterion and family roundtrips must state this.
- The source's unqualified relation-isomorphism claim is contradicted by its example. Preserve the correction and counterexample together; do not strengthen the theorem silently.
- General algebraic theorems are kernel-checked Lean proofs; finite examples supplement them. Source correspondence still requires semantic review.
- Existing abstract interpretation/reduct laws and dependency boundaries must continue to pass.

## Handoff

Preserve the frozen intent.md, spec.md and accepted.json. Keep scope.json and
existing requirements/obligations unchanged except for the approved delivered-scope
updates. Retain validation and coordinator ticket updates outside the repository.
No ready transition, merge or deployment is authorized.
