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
`RawOver.WellFormed.predefined_name`, `.user_name`, `.unique_predefined`,
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
declaration Set. `RawOver.WellFormed.inclusion_decl` and `.ordinary_decl` require
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

## Supported signature data and compatible specialization
`impl~formalcd-supported-signature~1`

[Signature.lean](../FormalCD/Signature.lean): `Vocabulary`, `.builtins`, `.extend`,
`.embed`, `.restrict`, `.extendInterpretation` provide symbol inclusion and inverse
arity maps without identifying universes. [Basic.lean](../FormalCD/Basic.lean):
`RawOver`, `RawOver.WellFormed`, `CDOver` generalize metadata/default obligations;
`Raw`, `CD`, `CD.generalize` retain the original specialization.
[Morphism.lean](../FormalCD/Morphism.lean): `HomOver` and its identity/composition
operations preserve all metadata. [Semantics.lean](../FormalCD/Semantics.lean):
`HomOver.reduct` reuses DPGraph restriction at that signature.

Covers:
- `req~formalcd-signature-extension~1`
- `req~formalcd-structure~1`
- `req~formalcd-declarations~1`
- `req~formalcd-morphisms~1`

## Signature and morphism compatibility proofs
`proof~formalcd-supported-signature-laws~1`

[Signature.lean](../FormalCD/Signature.lean): `Vocabulary.embed_builtins`,
`.embed_injective`, `.embed_translate`, `.satisfies_embed`, `.restrict_extend`.
[Morphism.lean](../FormalCD/Morphism.lean): `HomOver.ext`, `.ext_of_map`,
`.id_comp`, `.comp_id`, `.comp_assoc`, `.toDPHom_id`, `.toDPHom_comp`.
[Semantics.lean](../FormalCD/Semantics.lean): `HomOver.reduct_val`, `.reduct_id`,
`.reduct_comp`. Existing examples remain checked; the extended universe-polymorphic
laws are also exercised in [formalcd_imports.lean](../tests/formalcd_imports.lean).

Covers:
- `req~formalcd-signature-extension~1`
- `req~formalcd-structure~1`
- `req~formalcd-declarations~1`
- `req~formalcd-morphisms~1`

## Metamodel inventory and typed declarations
`impl~formalcd-metamodel-construction~1`

[Shape.lean](../FormalCD/Metamodel/Shape.lean): `Metamodel.Node`, `.Edge`, `.graph`,
`.NameNode`, `.NameEdge`, `.ArityNode`, `.ArityEdge`, `.nameBinding`, `.arityBinding`,
`.vocabulary`, `.nd`, `.ad`, `.SingletonClass`, `.SingletonObject`.
[Basic.lean](../FormalCD/Metamodel/Basic.lean): `Metamodel.nodeName`, `.edgeName`,
`.edgeMode`, `.registry`, `.classifiers`, `.predefinedKinds`, `.keyBinding`,
`.literalKey`, `.Declaration`, `.declaration`, `.raw`, `.diagram`, `.edges`.

Covers:
- `req~formalcd-metamodel-shape~1`

## Metamodel construction facts
`proof~formalcd-metamodel-construction-laws~1`

[Basic.lean](../FormalCD/Metamodel/Basic.lean): `Metamodel.wellFormed`, `.declared`,
`.args_no_setValued`, `.args_bag_total`, `.discipline_declarations`,
`.cover_disjoint_declarations`, `.eleven_nodes`, `.thirteen_arrows`,
`.edges_complete`, `.edges_nodup`, `.sing_metadata`, `.drawn_totals`,
`.drawn_singleValued`, `.name_identities_distinct`, `.same_name`;
[Shape.lean](../FormalCD/Metamodel/Shape.lean): `star_has_sing_class`.
The typed constructors and binding equations expose every endpoint in the source
inventory. These are construction and local well-formedness facts, not satisfaction.

Covers:
- `req~formalcd-metamodel-shape~1`

## Discipline meanings and full binding representation
`impl~formalcd-metamodel-meaning~1`

[Binding.lean](../FormalCD/Metamodel/Binding.lean): `Metamodel.Candidate`,
`.Candidate.Valid`, `.Candidate.ofFormula`, `.Candidate.toFormula`,
`.Candidate.formulaEquiv` retain full symbol, vertex and indexed arrow data.
[Discipline.lean](../FormalCD/Metamodel/Discipline.lean): `NameContext`,
`NameDiscipline`, `ArityContext`, `ArityDescriptor`, `ArityDescriptor.ValidAt`,
`ArityDiscipline` (all in `FormalCD.Metamodel`) check actual spans and explicit
representation data. [Interpretation.lean](../FormalCD/Metamodel/Interpretation.lean):
`Context` and `interpretation` connect the two extra symbols to these predicates.
The literal key uses the existing DPGraph interpretation without changing it.

Covers:
- `req~formalcd-metamodel-disciplines~1`
- `req~formalcd-formula-identity~1`

## Discipline correspondence and identity laws
`proof~formalcd-metamodel-meaning-laws~1`

[Binding.lean](../FormalCD/Metamodel/Binding.lean): `Candidate.ofFormula_valid`,
`.to_ofFormula`, `.of_toFormula`, `.valid_iff_represents`, `formula_ext`,
`formula_binding_ext`, `full_binding_identity`.
[Discipline.lean](../FormalCD/Metamodel/Discipline.lean): `represented_formula`,
`zero_arrow_not_total`. [Interpretation.lean](../FormalCD/Metamodel/Interpretation.lean):
`builtins_unchanged`, `satisfies_nd`, `satisfies_ad`, `satisfies_literalKey`.
These declarations are in `FormalCD.Metamodel`.

Covers:
- `req~formalcd-metamodel-disciplines~1`
- `req~formalcd-formula-identity~1`

## Metamodel acceptance data
`impl~formalcd-metamodel-witness-data~1`

[Examples.lean](../FormalCD/Metamodel/Examples.lean): `ordered`, `repeated`,
`badIncidence`, `orderedArgs`, `orderedPred`, `repeatedArgs`, `isolated` and
`isolatedArgs`. [InterpretationExamples.lean](../FormalCD/Metamodel/InterpretationExamples.lean):
`repeatDiagram`, `repeatContext`, `repeatDescriptor`, `duplicateIndex`,
`fragment`, `fragmentModel`. [NameExamples.lean](../FormalCD/Metamodel/NameExamples.lean):
`nameDiagram`, `nameContext`, `reservedUser`, `wrongPredefined`.
All are in `FormalCD.Metamodel.Examples`, built separately from the public root.

Covers:
- `req~formalcd-metamodel-examples~1`

## Checked discipline and projection boundaries
`proof~formalcd-metamodel-witnesses~1`

[Examples.lean](../FormalCD/Metamodel/Examples.lean): `repeated_occurrences`,
`changed_position`, `changed_symbol`, `reconstructed_identity`,
`bad_incidence_rejected`, `bad_incidence_has_no_formula`,
`ordered_args_projection`, `ordered_pred_projection`,
`unindexed_bag_forgets_position`, `ordered_total`, `ordered_literal_key_fails`,
`repeated_total`, `repeated_literal_key`, `repeated_not_setValued`,
`changed_isolated_vertex`, `arrow_projection_forgets_isolated`, `empty_arity_valid`,
`isolated_not_total`, `isolated_literal_key_fails`.
[InterpretationExamples.lean](../FormalCD/Metamodel/InterpretationExamples.lean):
`repeat_discipline`, `duplicate_index_rejected`, `missing_candidate_rejected`,
`extended_ad_satisfied`, `extended_key_satisfied`, `extended_total_satisfied`,
`extended_args_not_setValued`, and the proof field of `fragmentModel`.
[NameExamples.lean](../FormalCD/Metamodel/NameExamples.lean): `name_square`,
`names_valid`, `valid_user_name`, `valid_predefined_name`, `reserved_user_rejected`,
`wrong_predefined_rejected`, `incompatible_name_span_rejected`, `extended_nd_satisfied`.
All names are in `FormalCD.Metamodel.Examples`. The source map states the exact
fragment/model boundary. Generic key, Q1 and Q8 are unchanged.

Covers:
- `req~formalcd-metamodel-disciplines~1`
- `req~formalcd-formula-identity~1`
- `req~formalcd-metamodel-examples~1`

## Bounded syntactic self-description data
`impl~formalcd-bounded-self-description-data~1`

[SelfDescription.lean](../FormalCD/SelfDescription.lean) reuses the existing
`Metamodel.diagram` in `CDOver.{0,0,0,0,0,0}` at `Metamodel.vocabulary` and
`Metamodel.registry`. `metamodelFormulaRepresentation` specializes the existing
`Candidate.formulaEquiv` without altering full binding or bag projection semantics.

Covers:
- `req~formalcd-bounded-self-description~1`

## Bounded syntactic self-description proof
`proof~formalcd-bounded-self-description-laws~1`

[SelfDescription.lean](../FormalCD/SelfDescription.lean):
`FormalCD.bounded_self_description` reuses the raw-data equality, `wellFormed`,
`eleven_nodes` and `thirteen_arrows`; `metamodel_formula_roundtrip` reuses the
full-binding equivalence. These are representation and syntactic validity results,
not proofs of semantic self-instantiation or universal realizability.

Covers:
- `req~formalcd-bounded-self-description~1`

## Figure 21b data and effective formulas
`impl~formalcd-figure21-construction~1`

[Figure21/Basic.lean](../FormalCD/Figure21/Basic.lean): `Node`, `Edge`, `graph`,
`VCEdge`, `vcShape`, `vcBinding`, `extraSignature`, `vocabulary`, `vc`, `registry`,
`nodeName`, `edgeName`, `edgeMode`, `inclusions`, `opposite`, `Declaration`,
`declaration`, `raw`, `diagram`, `edges`, `effectiveFormulasEquiv`.
Names are in `FormalCD.Figure21`. These reuse full typed Formula bindings and
the existing optional metadata/default framework. Sources: §6.1.1–3, Figure 21b,
p.19's twelve effective declarations, and B.4 Definitions 7–9.

Covers:
- `req~formalcd-figure21-example~1`

## Figure 21b syntax and inventory proofs
`proof~formalcd-figure21-construction-laws~1`

[Figure21/Basic.lean](../FormalCD/Figure21/Basic.lean): `wellFormed`, `declared`,
`four_classes`, `five_arrows`, `edges_complete`, `edges_nodup`,
`inclusion_identities_distinct`, `inclusion_names`, `int_metadata`,
`no_singleton_required`, `twelve_declarations`, `declaration_injective`,
`twelve_effective_formulas`, `four_vc_arrows`, `vc_edges_complete`, `vc_edges_nodup`.
`effectiveFormulasEquiv` proves exact correspondence between the twelve labels
and the effective formula set. Edge constructors and the complete list expose
all five incidences, with the four VC arrows bound by `vcBinding`.
[VC.lean](../FormalCD/Figure21/VC.lean): `one_one_total_single` and
`zero_one_single` explain the arrow notation through link multiplicities.

Covers:
- `req~formalcd-figure21-example~1`

## Guarded VC interpretation data
`impl~formalcd-vc-meaning~1`

[Figure21/VC.lean](../FormalCD/Figure21/VC.lean): `IntegerRealization`, `.domain`,
`InheritedVersion`, `VCMeaning`, `vcInterpretation`, `interpretation`,
`asComponent`, `versionValue`, `GuardedComparison`. All names are in
`FormalCD.Figure21`. VC checks the realized integer domain and compares decoded
version targets along actual inclusion/version links for each server link.
There is no comparison for an empty server fiber. Semantic universes retain
`U : Type u`, subset vertices and link bound `max u w`. The source correction
is Figure 8 line 9 / §4.2.3–4.3, Figure 21a / §6.1.2 and Appendix F, recorded as Q7
in the source map; the generic built-in catalogue remains separate.

Covers:
- `req~formalcd-vc-semantics~1`

## Guarded VC correspondence proofs
`proof~formalcd-vc-meaning-laws~1`

[Figure21/VC.lean](../FormalCD/Figure21/VC.lean): `builtins_unchanged`,
`satisfies_vc`, `one_one_total_single`, `zero_one_single`, `versionValue_link`,
`inherited_iff_value`, `satisfies_vc_iff_guarded`, `declared_vc_iff_guarded`. The
last two theorems assume the
explicit integer domain, both inclusions and version 1..1; it proves equivalence
with the guarded integer comparison for actual typed VC satisfaction. It assumes
neither server totality nor whole-model satisfaction.

Covers:
- `req~formalcd-vc-semantics~1`

## Figure 21b model and boundary data
`impl~formalcd-vc-witness-data~1`

[Figure21/Examples.lean](../FormalCD/Figure21/Examples.lean): `Universe`, `integers`,
`components`, `singletonObjects`, `component`, `singletonObject`, `inclusionSpan`,
`serverSpan`, `versionNumber`, `versionSpan`, `objects`, `modelMap`, `model`.
Names are in `FormalCD.Figure21.Examples`. The ambient type is `Bool ⊕ Int`;
component sets are finite but the integer domain realizes every integer.
The models are parameterized by server presence and arbitrary ECU/display versions.

Covers:
- `req~formalcd-vc-witnesses~1`

## Figure 21b satisfaction and counterexamples
`proof~formalcd-vc-witness-laws~1`

[Figure21/Examples.lean](../FormalCD/Figure21/Examples.lean): `inclusion_holds`,
`server_multiplicity`, `display_multiplicity`, `version_multiplicity`,
`server_set`, `display_set`, `version_set`, `inverse_holds`, `cover_holds`,
`disjoint_holds`, `other_declarations`, `inherited_version`, `vc_iff`, `model_iff`,
`component_classes_nonempty`, `every_integer_realized`, `served_link`, `greater_vc`, `equal_vc`,
`lower_not_vc`, `lower_other_declarations`, `unserved_vc`, `unserved_model`,
`unserved_no_link`, `unserved_multiplicity`, `unserved_not_total`.
`model_iff` characterizes whole-model satisfaction for all parameters; the actual
`model` supplies a nonempty satisfying witness. The lower-version witness fails
VC while satisfying the other eleven declarations. The unserved witness shows
both VC vacuity and 0..1 without totality. All are actual interpreted formulas,
with no claim that these models instantiate the Figure 21c metamodel.
The shared module discovery, kernel replay, axiom audit and independent import
checks include the new modules and preserve all existing regressions.

Covers:
- `req~formalcd-vc-witnesses~1`
