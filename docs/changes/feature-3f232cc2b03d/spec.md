# Specification: first proven DP-graph slice (#14)

## Accepted source and scope

Use the 2014 SoSyM author preprint, Appendix B.4, Definitions 6–10:
https://gsd.uwaterloo.ca/sites/default/files/2014-Bak-Clafer-Unifying-Class-Feature-Modeling%28SOSYM%29.pdf
The inspected 34-page file has SHA-256 56b1c18e74807fb7646c0e89cb2fc306f4178affb41fee52fcebde09b031b2fb.

Repository baseline for planning: 43d7f3fc326201c68a5da24bdd8aa613794d1d0d. Preserve the factory-provided exact base and authoritative scope. Read AGENTS.md, CLAUDE.md, CONTRIBUTING.md, docs/intent.md, docs/spec.md and docs/traceability.md. Use the pinned IntentBond skill. Implementation is in the factory worktree only.

## Representation and definitions

1. Reuse Mathlib Quiver and Prefunctor. Use CategoryTheory.Quiv when bundled graphs are needed, keeping vertex/arrow/symbol universe parameters explicit. A carrier graph is not required to carry categorical identity arrows or composition. Explain the correspondence between the paper's total edge set and the dependent sum of endpoint-indexed quiver arrows.
2. Pin Mathlib to 56a005855ea17e0b0958f73ec801ae140b0a1679 (v4.35.0); its lean-toolchain matches the existing Lean v4.35.0. Preserve the Lean pin. Use targeted imports and the existing Lake setup.
3. A signature has a symbol type and graph-valued arity. A formula pairs a symbol with a graph morphism from its arity to the carrier. Avoid untyped names/argument lists. Preserve repeated arguments and isolated arity vertices; the paper's finite arrow-list shorthand is not a restriction on the generic definition.
4. A DP-graph has a carrier graph and a Set of well-typed formulas. Do not impose global finiteness or DecidableEq. A DP morphism has an underlying graph morphism and a proof that translation sends each declared source formula to a declared target formula.
5. Define formula translation by postcomposition; identity and composition of DP morphisms. Keep the signature fixed for these operations. Do not add inference closure from Diskin/Wolter's dependency-enriched signatures to the SoSyM definition.

## Required proofs and examples

- Formula translation preserves identities and composition.
- DP-morphism composition preserves declarations. Identity, associativity, left/right unit laws and useful extensionality hold; reuse existing Prefunctor lemmas.
- Construct a finite arity with two distinct parallel arrows, a nonempty declared-formula source DP-graph, and a target DP-graph with an explicitly described declaration. Build a nonidentity morphism that identifies the two arrows. Prove source distinctness, image equality and declared-formula preservation. Exercise the formula-translation composition theorem on explicit composable maps.
- Include a graph morphism to a target with the necessary declaration absent, and prove that this underlying map cannot be equipped with the required DP-morphism preservation proof.
- Exercise at least one isolated arity vertex. Finite examples must not impose finiteness on the core.
- Syntax-only example predicate names carry no unproved semantic meaning. Do not claim this slice implements SetMap or Theorem 3.

## Living documentation and traceability

The canonical intent must state that DPGraph and FormalCD are independently reusable foundations, with structural 2014 Clafer as the application. Keep explicit exclusions from the user brief: no instance/object generation, Alloy/SMT/SAT integration, runtime configurations, Claferize, post-2014 extensions, production parser or visualization. Abstract mathematical semantics remain in scope for future increments.

Maintain docs/SOURCES.md and docs/ARCHITECTURE.md concisely; link the live roadmap #2 and design #13. Add only requirements for the delivered slice in docs/spec.md (proposed stable names: dpgraph-core, formula-translation, dpgraph-morphisms, dpgraph-examples). Search existing IDs before declaring them. Continuing intent and infrastructure IDs must be preserved. Requirements with advertised theorems should require impl and proof artifacts. Follow docs/traceability.md: use named Markdown artifacts linking actual Lean definitions/theorems, not unsupported inline Lean tags. No claims that future-phase promises already have implementations or proofs.

Record the requirement change summary: formalization-foundation intent expands to reusable three-layer scope; lean-validation and public-foundation status wording may need updating now that mathematical code begins, while their build/check/documentation promises remain. All other contribution and scope policies remain. Use the repository's revision policy; do not weaken coverage or tests. Task-package references are not duplicate canonical OFT declarations.

## Boundaries and unresolved later decisions

No span operations or predicate semantics are needed here. The source audit identified unresolved later questions: B.2.1 relation/span composition; Table 3 versus Figure 21 disjointness arity; Figure 21 VC inequality direction; Appendix D intersection typo; Appendix E analogous clauses; and label/identity choices for gluing. Record these as open and do not silently answer them. Full 2003/2000 secondary papers were not obtained; no claim of complete source audit is permitted. Definitions 6–10 and compatible Mathlib sources have been inspected and are sufficient for this slice.

## Acceptance and reporting

An independently importable ClaferLean.DPGraph entrypoint and all required proofs/examples compile without any FormalCD/Clafer imports. Run the full existing validation through IntentBond, retaining the exact base, logs, proof/axiom audit and verification evidence. Kernel proofs must contain no sorry/admit or escape axioms; no unsafe mathematical declarations. Report legitimate standard axioms separately from new assumptions.

Pass the configured Docker checks and independent review before creating a draft PR. Link Closes #14; relate #2 and #13 but do not close their broader research/design work prematurely. Workers return ticket updates to the coordinator; they receive no GitHub credentials. Keep all tickets open until acceptance and merge. Do not merge, mark ready, or deploy.
