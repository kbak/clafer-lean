# DP-graph trace artifacts

Follow [the Lean trace convention](traceability.md): these are named Markdown
artifacts; their evidence is the linked Lean declarations, not inline Lean tags.
The [source map](SOURCES.md) records the meaning of SoSyM B.4 Definitions 6–10.
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
