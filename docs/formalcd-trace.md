# FormalCD implementation and proof links

Follow the [Lean trace convention](traceability.md). These named artifacts link
the [requirements](spec.md) to actual declarations; review must assess the Lean
statements and [source correspondence](SOURCES.md#formalcd-structure-and-selected-morphisms).
All names below are in `FormalCD`. Examples remain outside the public entrypoint.

## Raw and bundled structure
`impl~formalcd-data~1`

[Basic.lean](../FormalCD/Basic.lean): `Registry`, `PredefinedKind`, `MapMode`,
`Raw`, `Raw.WellFormed`, `CD`, `arrowBinding`, `inclusionFormula` and
`setValuedFormula` reuse Quiv/Prefunctor, the existing signature and Formula Set.
[FormalCD.lean](../FormalCD.lean) exposes the reusable core.

Covers:
- `req~formalcd-structure~1`

## Structure witnesses and typed bindings
`proof~formalcd-data-witnesses~1`

[Examples.lean](../FormalCD/Examples.lean): `Examples.wellFormed`,
`.finite_vertices`, `.finite_arrows`, `.optional_primitives`, `.repeated_arguments`
and `.isolated_vertex` exercise valid data, optional entries and intact bindings.
[SemanticsExamples.lean](../FormalCD/SemanticsExamples.lean):
`Examples.wellFormed_does_not_certify_satisfaction` separates syntax and semantics.
[formalcd_imports.lean](../tests/formalcd_imports.lean) checks the independent public
API with independent carrier/semantic universes; the existing DPGraph public-import
test retains its separate root guard.

Covers:
- `req~formalcd-structure~1`

## Naming obligations
`impl~formalcd-name-obligations~1`

[Basic.lean](../FormalCD/Basic.lean): `Registry.Reserved` and
`Raw.WellFormed.predefined_name`, `.user_name`, `.unique_predefined`,
`.inclusion_name` specify the obligations on raw metadata.

Covers:
- `req~formalcd-naming~1`

## Naming acceptance and rejection
`proof~formalcd-name-witnesses~1`

[Examples.lean](../FormalCD/Examples.lean): `Examples.distinct_inclusions`,
`.shared_inclusion_name`, `.repeated_class_names`, `.reserved_user_invalid`,
`.wrong_predefined_invalid`, `.duplicate_predefined_invalid` and
`.wrong_inclusion_name_invalid` prove the selected naming boundaries.

Covers:
- `req~formalcd-naming~1`

## Effective declaration obligations
`impl~formalcd-effective-declarations~1`

[Basic.lean](../FormalCD/Basic.lean): `Raw.toDPGraph` retains the authoritative
declaration Set. `Raw.WellFormed.inclusion_decl` and `.ordinary_decl` require
typed default formulas. Bag mode has no membership obligation.

Covers:
- `req~formalcd-declarations~1`

## Default membership and exceptions
`proof~formalcd-default-witnesses~1`

[Basic.lean](../FormalCD/Basic.lean): `arrowBinding_comp`,
`inclusionFormula_translate`, `setValuedFormula_translate` preserve the actual
typed arrow binding. [Examples.lean](../FormalCD/Examples.lean):
`Examples.inclusion_endpoints`, `.required_inclusions`, `.ordinary_default`,
`.no_bag_default`, `.user_declaration_retained`, `.explicit_bag_wellFormed`,
`.missing_inclusion_invalid` and `.missing_ordinary_invalid` check required
membership, preserved authored declarations and the bag exception.

Covers:
- `req~formalcd-declarations~1`

## Specialized morphisms and forgetting
`impl~formalcd-hom~1`

[Morphism.lean](../FormalCD/Morphism.lean): `Hom`, `Hom.toDPHom`, `Hom.id` and
`Hom.comp` retain the existing DP map and prove preservation of class/map names,
optional identifiers and modes. [Semantics.lean](../FormalCD/Semantics.lean):
`Hom.reduct` applies the existing reduct with an explicit interpretation.

Covers:
- `req~formalcd-morphisms~1`

## Morphism laws and semantic interoperability
`proof~formalcd-hom-laws~1`

[Morphism.lean](../FormalCD/Morphism.lean): `Hom.ext`, `.ext_of_map`, `.id_comp`,
`.comp_id`, `.comp_assoc`, `.toDPHom_id` and `.toDPHom_comp` reuse the DP laws.
The metadata proof fields of `Hom.id`/`.comp` close all four equality obligations.
[Semantics.lean](../FormalCD/Semantics.lean): `Hom.reduct_val`, `.reduct_id` and
`.reduct_comp` reuse the generic contravariant reduct laws.
[Examples.lean](../FormalCD/Examples.lean): `Examples.collapse_nonidentity`,
`.collapse_identifies`, `.explicit_composite`, `.composition_law`, `.unit_laws`,
`.forget_composite`, `.extra_target_declaration` and `.mode_change_cannot_lift`
exercise the selected specialization and its limits.

Covers:
- `req~formalcd-morphisms~1`

## Acceptance example data
`impl~formalcd-example-data~1`

[Examples.lean](../FormalCD/Examples.lean): `Examples.registry`, `.raw`, `.diagram`,
the invalid raw diagrams, `.explicitBag`, `.collapseHom`, `.swapHom`,
`.bagModeDiagram` and `.modeChangingDP` supply the structural cases.
[SemanticsExamples.lean](../FormalCD/SemanticsExamples.lean): `Examples.modelMap`,
`.model`, `.restrictedModel`, `.duplicateLinks` and `.failingMap` use the delivered
concrete span interpretation.

Covers:
- `req~formalcd-examples~1`

## Checked acceptance boundaries
`proof~formalcd-acceptance-witnesses~1`

The naming/default/morphism witnesses listed above in
[Examples.lean](../FormalCD/Examples.lean) cover all structural acceptance cases.
[SemanticsExamples.lean](../FormalCD/SemanticsExamples.lean):
`Examples.model_condition`, `.restricted_model`, `.restriction_forgets`,
`.restriction_composition`, `.restriction_identity`, `.satisfaction_translation`,
`.duplicateLinks_not_setValued`, `.model_bag_not_setValued`,
`.extra_declaration_not_satisfied`, `.failing_satisfaction` and
`.wellFormed_does_not_certify_satisfaction` check actual models and failures.
The unchanged shared check discovers and kernel replays all these modules and
includes them in the axiom audit; trace links alone do not establish semantics.

Covers:
- `req~formalcd-examples~1`
