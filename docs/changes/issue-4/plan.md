# Implementation plan for issue #4

Status: proposed; semantic adoption awaits the user's decision. This package is a plan, not execution evidence.

## Baseline and dependencies

Selected repository: kbak/clafer-lean. Catalog and live main matched cabcf18abf231a4aac510d8f9996110ff2d8db09 during preparation. Configured scope comes from 0b9599e89417d9f9ea8c39170fff4af15cd02ab3:scope.json; current root scope has the same obligations. No prior factory report exists for issue-4. The issue is open, manually submitted, and still labeled blocked pending semantic adoption.

Read AGENTS.md, CLAUDE.md, CONTRIBUTING.md, canonical docs/intent.md, affected docs/spec.md, docs/ARCHITECTURE.md, docs/SOURCES.md, docs/traceability.md, and #2/#13/#16. #15's abstract interpretation is already delivered. #16 predicate choices are outside this task.

## Work order and affected files

1. Record the adopted Q1 correction and refine scoped mathematical requirements before compatibility theorems. Update docs/spec.md, docs/SOURCES.md and the coordinator's issue tracking as authorized; retain the issue body/comment identities in external evidence.
2. Add DPGraph/Span/Basic.lean for spans, cross-universe isomorphisms and inversion; DPGraph/Span/IndexedFamily.lean for families, equivalences and conversions. File subdivision may change if the same boundaries and acceptance criteria remain clear.
3. Add DPGraph/Span/Composition.lean for pullback heads, identity and canonical unit/associator equivalences, and the family-composition correspondence.
4. Add DPGraph/Span/Relation.lean for reduction, set-valuedness, the reduction/composition law and exact injectivity criterion. Avoid an import cycle between composition and relation modules. Document all assumptions explicitly.
5. Add DPGraph/Span/Examples.lean with the positive/negative and universe witnesses. Add DPGraph/Span.lean as the public facade and expose it through DPGraph.lean. Extend tests/public_imports.lean with actual independent API uses. Existing discovery should include all new modules without weakening scripts/check.sh or tests/axiom_audit.lean.
6. Extend docs/dpgraph-trace.md with named implementation and proof artifacts; link exact declarations. Update the delivered-scope statements in docs/intent.md, docs/ARCHITECTURE.md, docs/SOURCES.md, README.md and CONTRIBUTING.md only as needed. Keep source citations and the distinction from future predicate/SetMap semantics.
7. Run the full IntentBond check against the captured starting commit, inspect the complete diff and evidence, commit, and verify the committed candidate. The factory's configured tests and independent review must pass before publishing a draft with Closes #4.

## Risks and verification focus

- Fiber/sigma heads can raise universe bounds. Cross-universe head equivalences and compiled mixed-universe examples must demonstrate the intended generality.
- Proof irrelevance for equality witnesses must not erase actual link identity. Check the two-path and parallel-link counterexamples at the span level.
- Isomorphism must preserve endpoints, not merely head cardinality. The exact composite criterion and family roundtrips must state this.
- The source's unqualified relation-isomorphism claim is contradicted by its example. Preserve the correction and counterexample together; do not strengthen the theorem silently.
- General algebraic theorems are kernel-checked Lean proofs; finite examples supplement them. Source correspondence still requires semantic review.
- Existing abstract interpretation/reduct laws and dependency boundaries must continue to pass.

## Handoff

Freeze these three documents using configure.py plan with task issue-4. No implementation in the catalog or a temporary checkout. After explicit acceptance, use the factory submission workflow with this exact package and the existing issue identity; retain source specification and clarification, and update the existing Project through the coordinator ticket wrapper. Do not create a duplicate issue or unrelated task. Recheck the issue/comment and live base before submission; review and reprepare if they changed. Keep the issue open until merge, and leave unrelated roadmap/design work open.

The factory retains accepted snapshots and a concise current plan; full test/review evidence and handoff.md/handoff.json remain external artifacts. No implementation or validation result is claimed by this planning package.
