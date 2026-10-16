# DP-graph trace artifacts

Follow [the Lean trace convention](traceability.md): these are named Markdown
artifacts; their evidence is the linked Lean declarations, not inline Lean tags.
The [source map](SOURCES.md) records SoSyM B.4 Definitions 6–10 and the
abstract restriction argument of B.5 Theorem 3.
All declaration names below are relative to `DPGraph`, except the
carrier/declaration structure itself, `DPGraph`.

## Core representation
`impl~dpgraph-core~1`

[Signature.lean](../DPGraph/Signature.lean): `Signature`, with independent
symbol and arity universes and Mathlib bundled quivers.
[Formula.lean](../DPGraph/Formula.lean): `Formula`, retaining a typed
`Prefunctor` binding.
[Basic.lean](../DPGraph/Basic.lean): `DPGraph`, with a `Set`
of declarations over its carrier.
[DPGraph.lean](../DPGraph.lean) is the independent entrypoint.
The [architecture](ARCHITECTURE.md) explains total edges as a dependent sum.
[lakefile.toml](../lakefile.toml) and [lake-manifest.json](../lake-manifest.json)
record the exact Mathlib pin, compatible with the preserved Lean toolchain.

Covers:
- `req~dpgraph-core~1`

## Translation implementation
`impl~formula-translation~1`

[Formula.lean](../DPGraph/Formula.lean): `Formula.translate` postcomposes
the binding, retaining the symbol and signature.

Covers:
- `req~formula-translation~1`

## Translation proofs
`proof~formula-translation~1`

[Formula.lean](../DPGraph/Formula.lean): `Formula.translate_id` and
`Formula.translate_comp` quantify over arbitrary formulas and compatible graph
maps, using `Prefunctor.comp_id` and `Prefunctor.comp_assoc`.

Covers:
- `req~formula-translation~1`

## Morphism implementation
`impl~dpgraph-morphisms~1`

[Morphism.lean](../DPGraph/Morphism.lean): `Hom.toPrefunctor` and
`Hom.preserves` enforce Definition 10. `Hom.id` and `Hom.comp` construct
preservation proofs, with fixed signature and independent carrier universes.

Covers:
- `req~dpgraph-morphisms~1`

## Morphism proofs
`proof~dpgraph-morphisms~1`

[Morphism.lean](../DPGraph/Morphism.lean): the proof fields in `Hom.id`
and `Hom.comp` establish declaration preservation; `Hom.comp_preserves` exposes
the latter result. `Hom.id_comp`, `Hom.comp_id` and `Hom.comp_assoc` use the
corresponding `Prefunctor` laws. `Hom.ext` identifies morphisms with equal graph
maps, and `Hom.ext_of_obj_map` reuses `Prefunctor.ext` for pointwise equality.

Covers:
- `req~dpgraph-morphisms~1`

## Example constructions
`impl~dpgraph-examples~1`

[Examples.lean](../DPGraph/Examples.lean): `Examples.Vertex`, its finite
instances, `arity`, `firstArrow`, `secondArrow`, and `signature` give a finite
arity with an isolated vertex and a syntax-only symbol `mark`. `sourceFormula`
binds the arity by identity; `targetFormula` explicitly binds it by `collapse`,
which fixes vertices and sends both arrows to `firstArrow`. `sourceGraph` and
`targetGraph` each declare exactly the named formula. `collapseHom` proves
preservation. `swap`, `swapHom`, `finalFormula` and `finalGraph` supply a second
explicit composable map. `undeclaredGraph` has the same carrier and no declarations;
`unpreservedMap` gives the same collapse map to that carrier.

Covers:
- `req~dpgraph-examples~1`

## Example proofs
`proof~dpgraph-examples~1`

[Examples.lean](../DPGraph/Examples.lean), all under `Examples`:
`parallel_distinct`, `images_equal`, `collapse_ne_id`, `source_declared`,
`source_nonempty`, `translated_declaration` and `collapse_preserves` establish the
nonvacuous, nonidentity witness. `isolated_no_out`, `isolated_no_in`,
`isolated_binding` and `isolated_translation` exercise the isolated vertex.
`explicit_translation_comp` applies the generic composition theorem to `collapse`
and `swap`; `composed_preserves` applies the DP composition theorem.
`declaration_absent`, `no_preservation` and `no_dp_lift` prove the negative case,
including impossibility of a preservation proof for the specific underlying map.
These are structural results, with no predicate interpretation assumed.

Covers:
- `req~dpgraph-examples~1`

## Declaration and axiom audit
`itest~dpgraph-axiom-audit~1`

[tests/axiom_audit.lean](../tests/axiom_audit.lean) inspects declarations originating
in all `DPGraph`, `FormalCD` and `Clafer` modules, rejects unsafe/partial declarations and new axioms,
and checks transitive axiom dependencies against the three standard logical
axioms. It selects by module origin even for private/generated declarations
outside a root namespace, rejects an empty audit and prints dependencies and
totals per root. [project_modules.py](../scripts/project_modules.py) discovers
the complete module inventory and generates every `import all` in the audit.
[scripts/check.sh](../scripts/check.sh) executes it after the build and kernel
check, with warnings treated as errors. This is a validation test, not a theorem
about the intended semantics.

[public_imports.lean](../tests/public_imports.lean) exercises the public names
and rejects upper-layer/example imports in the independent entrypoint.
[test_project_modules.py](../tests/test_project_modules.py) exercises permitted
and reverse/helper/root dependencies, uncovered modules and future audit coverage.
[test_axiom_audit.py](../tests/test_axiom_audit.py) runs the production audit on
isolated Lean fixtures: private/generated names, axioms in every root,
unsafe/partial declarations, incomplete imports and an empty audit.

Covers:
- `req~lean-validation~1`

## Fixed-signature category implementation
`impl~dpgraph-category~1`

[Category.lean](../DPGraph/Category.lean): `category` uses the existing `Hom`,
`Hom.id` and `Hom.comp` directly, at fixed signature and carrier universes.
[DPGraph.lean](../DPGraph.lean) publicly imports it through `Semantics`.

Covers:
- `req~dpgraph-category~1`

## Category laws and extensionality
`proof~dpgraph-category~1`

[Category.lean](../DPGraph/Category.lean): `category` supplies its law fields
from [Morphism.lean](../DPGraph/Morphism.lean)'s `Hom.id_comp`, `Hom.comp_id`,
`Hom.comp_assoc`; `Hom.ext` and `Hom.ext_of_obj_map` apply unchanged to category
arrows. [SemanticsExamples.lean](../DPGraph/SemanticsExamples.lean)'s
`SemanticsExamples.category_units`, `category_assoc` and `category_ext` exercise
Mathlib notation and laws with the existing nonidentity maps.

Covers:
- `req~dpgraph-category~1`

## Interpretation implementation
`impl~dpgraph-interpretation~1`

[Semantics.lean](../DPGraph/Semantics.lean): `Interpretation.meaning` assigns a
set of arity diagrams in the chosen semantic graph. `Interpretation.Satisfies`
uses binding composition and membership; `Interpretation.IsModel` requires all
declarations. Semantic universes are independent of syntax universes.

Covers:
- `req~dpgraph-interpretation~1`

## Satisfaction composition proof
`proof~dpgraph-interpretation~1`

[Semantics.lean](../DPGraph/Semantics.lean): `Interpretation.satisfies_translate`
proves satisfaction of a translated formula equivalent to satisfaction after
precomposition, using `Prefunctor.comp_assoc`. It quantifies over arbitrary
interpretations and graph maps, with no closure/invariance assumptions.

Covers:
- `req~dpgraph-interpretation~1`

## Model restriction implementation
`impl~dpgraph-model-reduct~1`

[Semantics.lean](../DPGraph/Semantics.lean): `Interpretation.Model` retains the
map and its model proof. `Interpretation.reduct` precomposes that map with the
DP morphism, using `isModel_reduct` for satisfaction. Source, target and semantic
graph universes may differ.

Covers:
- `req~dpgraph-model-reduct~1`

## Model restriction proofs
`proof~dpgraph-model-reduct~1`

[Semantics.lean](../DPGraph/Semantics.lean): `Interpretation.isModel_reduct`
uses `Hom.preserves`, target-model satisfaction and `satisfies_translate` to prove
the B.5 reduct direction. `reduct_val`, `reduct_id` and `reduct_comp` identify the
underlying map and prove the identity and contravariant composition laws, using
subtype extensionality and the prefunctor laws. No additional semantic axiom is
assumed, and whole-model reflection is not asserted.

Covers:
- `req~dpgraph-model-reduct~1`

## Interpreted example constructions
`impl~dpgraph-semantics-examples~1`

[SemanticsExamples.lean](../DPGraph/SemanticsExamples.lean), all under
`SemanticsExamples`: `equalArrows` interprets the nonempty `Examples.signature`
by equality of the two parallel-arrow images. `targetModel`, `restrictedModel`
and `finalModel` retain maps satisfying nonempty declaration sets. `inclusion`
adds a declaration on the same carrier. `LargeVertex`, `largeQuiver`, `largeGraph`
and `liftDiagram` lift the example's vertices and arrows to `Type 1`;
`largeEqualArrows` and `largeTargetModel` interpret the original small syntax there.

Covers:
- `req~dpgraph-semantics-examples~1`

## Interpreted example proofs
`proof~dpgraph-semantics-examples~1`

[SemanticsExamples.lean](../DPGraph/SemanticsExamples.lean), all under
`SemanticsExamples`: `collapse_satisfies` and `identity_fails` prove that the
meaning has satisfying and failing diagrams. `restricted_map` and
`restricted_is_model` identify the nonidentity model reduct. `category_reduct_id`
and `category_reduct_comp` exercise its laws. `identity_not_source_model`,
together with `targetModel`, shows why bare graph maps do not suffice;
`model_not_reflected` disproves whole-model reflection even along a DP morphism.
`large_reduct_map` exercises restriction into larger semantic universes and
`large_identity_fails` checks that the larger interpretation is also nontrivial.
The existing `Examples.source_nonempty` establishes nonempty declarations.

Covers:
- `req~dpgraph-semantics-examples~1`
