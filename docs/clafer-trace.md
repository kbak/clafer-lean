# Clafer implementation and proof links

These artifacts follow [the Lean trace convention](traceability.md). Source
locators and the accepted top-level abstract correction are in
[SOURCES](SOURCES.md#resolved-2014-clafer-and-individual-shapes). All declarations
below are in namespace `Clafer`, with witnesses in `Clafer.Examples`. Kernel
checking establishes the Lean statements; independent review must assess their
correspondence to the paper and the selected input boundary.

## Deep resolved declarations
`impl~clafer-resolved-syntax~1`

[Syntax.lean](../Clafer/Syntax.lean): `Kind`, `Reference`, `Origin`,
`PrimitiveDomain`, `Declaration`, `Tree`, `Forest`, `Tree.branch`, `AST`, `Multiplicity`, `GroupCard`,
`GroupMultiplicity`, `Defaults`. [Context.lean](../Clafer/Context.lean) defines
`DeclId` separately from names. The forest stores containment; targets/supers
store IDs. Numeric groups and keywords retain distinct authored forms.

Covers:
- `req~clafer-resolved-syntax~1`

## Resolved syntax witnesses
`proof~clafer-resolved-syntax~1`

[Examples.lean](../Clafer/Examples.lean): `sample_wellFormed` constructs a mixed
model, including a primitive domain and an abstract reference; `repeated_names_distinct_ids`
checks identity separation. `keyword_default`, `explicit_overrides_keyword`,
`inherited_group_bounds`, `unbounded_range_valid` and `inverted_range_rejected`
exercise the resolved/defaulted multiplicity boundary. These are input validation
statements, not claims about a parser or resolver.

Covers:
- `req~clafer-resolved-syntax~1`

## Local input obligations
`impl~clafer-input-wellformedness~1`

[Syntax.lean](../Clafer/Syntax.lean): `AST.WellFormed`, `Kind.CanExtend`,
`ValidRange` and `Defaults` state resolved identity, root/domain, containment,
abstractness, inheritance, interval and constraint-context obligations. Rank is
proof data for inheritance acyclicity. Generic FormalCD/DPGraph contracts are reused.

Covers:
- `req~clafer-input-wellformedness~1`

## Input invariants and rejected cases
`proof~clafer-input-wellformedness~1`

[Syntax.lean](../Clafer/Syntax.lean): `AST.WellFormed.no_self_parent`,
`no_self_super`, `parent_wellFounded`, `super_wellFounded`. [Examples.lean](../Clafer/Examples.lean):
`sample_wellFormed`, `concrete_orphan_rejected`, `duplicate_ids_rejected`,
`different_inheritance_parents_rejected`, `self_inheritance_rejected`,
`primitive_reference_rejected`, `basic_reference_inheritance_rejected`,
`bag_set_inheritance_rejected`,
`set_bag_inheritance_allowed`, and `inverted_range_rejected` establish selected
positive/negative boundaries. These are not a complete decision procedure for
all AST validity conditions.

Covers:
- `req~clafer-input-wellformedness~1`

## Context and occurrence interface
`impl~clafer-constraint-boundary~1`

[Context.lean](../Clafer/Context.lean): `BinderId`, `Binder`,
`ConstraintBoundary`, `ConstraintBoundary.Resolved`, `Occurrence`, `referenced`.
The context and each occurrence are already resolved. Finite lists retain
repetitions; the constraint extension attaches typed bodies without a reverse
dependency from the boundary module.

Covers:
- `req~clafer-constraint-boundary~1`

## Context boundary witnesses
`proof~clafer-constraint-boundary~1`

[Examples.lean](../Clafer/Examples.lean): `repeated_scope_resolved`,
`repeated_scope_positions`, `dangling_scope_rejected`.
[Context.lean](../Clafer/Context.lean): `ConstraintBoundary.occurrences_finite`.
Different positions can name the same declaration; unknown IDs are rejected.
No expression typing or Appendix D semantic equation is asserted.

Covers:
- `req~clafer-constraint-boundary~1`

## Typed individual role graphs and local diagrams
`impl~clafer-individual-shapes~1`

[Shape.lean](../Clafer/Shape.lean): `Roles.classPresent`, `mapPresent`, `Class`,
`Map`, `Arrow`, `graph`, `mode`, `Shape`, `Located.shape`, `Shape.Realization`,
`SharedClass`, `Inclusions`, `OptionalInclusions`.
[Diagram.lean](../Clafer/Shape/Diagram.lean): `Shape.inverseBinding`,
`triangleBinding`, `keyBinding`, `declarations`, `raw`, `diagram`, `realization`.
These reuse graph-valued predicates and FormalCD's defaults. Optionality is
controlled by kind and endpoints. Inheritance's inclusion arrows are typed in
one shared carrier; this does not impose the remaining global MCS equations.

Covers:
- `req~clafer-individual-shapes~1`

## Shape incidence, kind and optionality
`proof~clafer-individual-shapes~1`

[Shape.lean](../Clafer/Shape.lean): `Roles.endpoints_present`, `incidence`,
`no_basic_target`, `no_parent_source`, `no_parent_maps`, `root_only_head`,
`root_no_maps`, `Located.shape_has_head`, `parentless_has_no_source`,
`Shape.no_source_inclusion`, `Shape.Inclusions.declared` (under FormalCD well-formedness).
[Diagram.lean](../Clafer/Shape/Diagram.lean): `Shape.raw_wellFormed`,
`inverse_declared`, `key_declared`, `key_conditions`.
[Examples.lean](../Clafer/Examples.lean): constructible `basicShape`, `setShape`,
`bagShape`, `abstractShape`, `abstractReferenceShape` and their map witnesses;
`abstract_basic_keeps_head`, `abstract_reference_incidence`, `reference_modes`,
`key_guard`, `wrong_head_incidence_uninhabitable`, `abstract_inclusion_has_head`,
`abstract_inclusion_has_target`, `abstract_reference_no_key`, `bag_no_key`, and
`inclusion_witness_no_source`. `inclusionWitness`, `withSuper` and `withoutSuper`
construct the optional inclusion data in a partial carrier. The local CD proof is syntactic, not satisfaction
or existence of an instance.

Covers:
- `req~clafer-individual-shapes~1`

## Structural traversal
`impl~clafer-finite-traversal~1`

[Syntax.lean](../Clafer/Syntax.lean): `Tree.fold`, `Forest.fold`, `Tree.entries`, `Forest.entries`, `AST.entries`,
`AST.Occurrence`, `AST.at` provide structural processing and finite indexing.
[Shape.lean](../Clafer/Shape.lean) restricts roles to finite enums/subtypes.
Reference and inheritance IDs remain data; neither is a recursive subtree.
The primitive-recursive folds/traversal are kernel-reducible and marked
`noncomputable` for native code generation; this is a mathematical compilation
basis, not an executable compiler. The AST constructors remain directly usable.

Covers:
- `req~clafer-finite-traversal~1`

## Finite representation and decreasing measures
`proof~clafer-finite-traversal~1`

[Syntax.lean](../Clafer/Syntax.lean): `Tree.child_smaller`,
`AST.occurrences_finite`, `AST.every_entry_indexed`, `AST.WellFormed.parent_wellFounded`.
[Shape.lean](../Clafer/Shape.lean): `Roles.classes_finite`, `arrows_finite`,
`Shape.inclusion_roles_finite`.
[Examples.lean](../Clafer/Examples.lean): `finite_reference_cycle` and `fold_counts_reference_cycle` count the
complete traversal despite cyclic reference edges. No compilation or parser
correctness theorem follows from these finite presentation results.

Covers:
- `req~clafer-finite-traversal~1`


## MCS metamodel
`impl~clafer-mcs-metamodel~1`

[MCS/Metamodel.lean](../Clafer/MCS/Metamodel.lean): `Metamodel.Node`, `Edge`,
`declarations`, `raw`, `diagram`, `corrected`, `isOwned`. [MCS/Basic.lean](../Clafer/MCS/Basic.lean):
`Family.MapId`, `Role`, `Roles.graph`, `Labels`, `predefinedStrings`,
`Roles.Cojoining.head_bijective`, `Formulas.owner`. These declarations separate
role identities, referents and strings and encode the accepted ownership bounds.

Covers:
- `req~clafer-mcs-metamodel~1`

## MCS metamodel boundaries
`proof~clafer-mcs-metamodel~1`

[MCS/Metamodel.lean](../Clafer/MCS/Metamodel.lean): `Metamodel.wellFormed`,
`twenty_edges`, `edges_complete`, `corrected_declared`, `ownership_declared`,
`correction_boundary`, `args_total_declared`, `literal_key_declared`.
[MCS/Laws.lean](../Clafer/MCS/Laws.lean): `role_cover`, `role_disjoint`,
`ordinary_owner_unique`, `inclusion_owner_unique`, `Family.canonical_cojoining`.
[MCS/Examples.lean](../Clafer/MCS/Examples.lean): `repeated_parent_names`,
`repeated_dref_names`, `repeated_inclusion_names`, `sample_valid`.
These are structural statements; no whole-metagraph semantic instantiation is claimed.

Covers:
- `req~clafer-mcs-metamodel~1`

## MCS Appendix E definitions
`impl~clafer-mcs-disciplines~1`

[MCS/Basic.lean](../Clafer/MCS/Basic.lean): `Family`, `Family.WellFormed`,
`Family.shape`, `Family.InclusionSlot`, `Roles.binding`, `Roles.Cojoining`,
`Labels.WellFormed`, `Valid`, `Model`. The [inventory](mcs-invariants.md#definition-and-proof-map)
expands every printed row and analogous case, with exact declarations and guards.

Covers:
- `req~clafer-mcs-disciplines~1`

## MCS structural laws and nonempty composition
`proof~clafer-mcs-disciplines~1`

[MCS/Laws.lean](../Clafer/MCS/Laws.lean): `Roles.incidence`, `Roles.inclusion_incidence`,
`Family.canonical_cojoining`, `no_super_no_inclusion`, `super_has_head`,
`missing_sub_source`, `missing_super_source`, `missing_sub_target`, `missing_super_target`,
`root_no_maps`, `root_has_head`, `primitive_no_target`, `primitive_cojoins_root`,
`reference_target_iff`, `Family.WellFormed.no_self_parent`, `.no_self_super`,
`target_name_via_head`, `reserved_names_exclude_users`.
[MCS/Examples.lean](../Clafer/MCS/Examples.lean): `family_valid`, `labels_valid`,
`sample_valid`, `shapes_compose`, `parentless_reference_retains_dref`,
`missing_inherited_source`, `shared_source_present`, `bag_mode`,
`wrong_cojoining_rejected`, `wrong_parent_cojoining_rejected`,
`wrong_target_cojoining_rejected`, `missing_parent_rejected`,
`primitive_reference_rejected`, `root_super_rejected`, `user_named_Sing_rejected`.
The eleven-owner example covers int/string/bool and basic/set/bag, parentless
abstracts, both shared-source and absent-source inheritance.

Covers:
- `req~clafer-mcs-disciplines~1`

## MCS formula representation
`impl~clafer-mcs-formulas~1`

[MCS/Basic.lean](../Clafer/MCS/Basic.lean): `Formulas`, `Formulas.Arg`, `.argument`,
`.SameBag`, `.WellFormed`, `.diagram`. [MCS/Laws.lean](../Clafer/MCS/Laws.lean):
`Roles.localDiagram`. Full bindings and indexed occurrences are retained; the
literal bag key and total arguments are additional, separately checked propositions.

Covers:
- `req~clafer-mcs-formulas~1`

## MCS formula boundary proofs
`proof~clafer-mcs-formulas~1`

[MCS/Laws.lean](../Clafer/MCS/Laws.lean): `Formulas.no_zero_arrow`,
`Formulas.formula_injective`, `Formulas.sameBag_iff_map_roles`,
`Roles.arrowData_ext`, `Roles.local_declared`.
[MCS/Examples.lean](../Clafer/MCS/Examples.lean): `formulas_valid`,
`duplicate_formulas_rejected`, `repeated_args_valid`, `repeated_occurrences_preserved`.
These establish structural formula-bank conditions, not generation of the complete
Compile output or semantic satisfaction of the declarations.

Covers:
- `req~clafer-mcs-formulas~1`

## Resolved core expression constructors
`impl~clafer-core-typing~1`

[Typing.lean](../Clafer/Constraints/Typing.lean): `Constraints.Collection`, `Ty`,
`SetOp`, `Arithmetic`, `Expr`, and `Expr.some/no/one/lone` implement the selected
D.1–D.3 forms. `Expr.widenObjects` and `widenRelation` carry explicit
`Constraints.Widen` paths from [Support.lean](../Clafer/Constraints/Support.lean).
No evaluator or semantic preservation theorem is implemented. Integer-only
arithmetic is an implementation boundary, not a claim that D.3 forbids other
primitive domains. The Q3 disposition is in [SOURCES](SOURCES.md#appendix-d-rule-dispositions-q3).

Covers:
- `req~clafer-core-typing~1`

## Core typing witnesses and rejection assertions
`proof~clafer-core-typing~1`

[Constraints/Examples.lean](../Clafer/Constraints/Examples.lean), namespace
`Clafer.Constraints.Examples`: `navigation`, `inheritedNavigation`, `composed`,
`inheritedJoin`, `compatibleUnion`, `numericConstraint`, `collectionConstraint`,
`relationConstraint`
and `duplicateIdentity` are actual indexed expression values. The named
`wrong_image_rejected`, `wrong_join_rejected`, `mixed_collection_rejected`,
`bare_set_is_not_boolean`, `boolean_arithmetic_rejected`,
`integer_cardinality_rejected` and `mixed_equality_rejected` assertions use
`fail_if_success` on construction of the invalid terms. They check elaboration
failure; their `True` conclusions are not semantic impossibility theorems.
`non_inclusion_cannot_widen` checks a non-inheritance map's kind;
`unrelated_widening_rejected` proves that a path to an unrelated class cannot exist.

Covers:
- `req~clafer-core-typing~1`

## Lexical binding and compiler assumptions
`impl~clafer-core-binding~1`

[Typing.lean](../Clafer/Constraints/Typing.lean): `Local`, `Var`, `Expr.all`,
`Domains`, `Constraint`, `Constraint.Input`, `ResolvedConstraint` retain lexical
scope, typed external
domains, AST validity and the resolved boundary assumptions. `Support.Boundary`
in [Support.lean](../Clafer/Constraints/Support.lean) maps each recorded scope
and domain occurrence separately. `Constraint.Input` does not claim that the
boundary bags were computed by traversing the expression.

Covers:
- `req~clafer-core-binding~1`

## Binder scope and resolved-input evidence
`proof~clafer-core-binding~1`

[Typing.lean](../Clafer/Constraints/Typing.lean): `Var.index_lt`, `Var.lookup`,
`Var.closed` establish valid lexical positions and the absence of a closed free
variable. `Var.index` and `Path.navigate` use kernel-reducible primitive recursors
with native code generation omitted, as for the existing tree folds. [Constraints/Examples.lean](../Clafer/Constraints/Examples.lean):
`quantified`, `nested`, `shadowed_name_keeps_ids`, `outer_variable_position`,
`externalDomains`, `constraint_input`, `resolvedConstraint`, `external_input`,
`repeated_scope_retained`
and `repeated_domain_retained` give positive
witnesses. `nonboolean_body_rejected`, `relation_domain_rejected`,
`out_of_scope_rejected` and `domain_cannot_use_own_binder` are failed-construction
assertions; `duplicate_binder_id_rejected` proves the freshness condition false.
The singleton meaning of a variable is documented, not proved by these statements.

Covers:
- `req~clafer-core-binding~1`

## Graph support and predicate seam
`impl~clafer-core-support~1`

[Support.lean](../Clafer/Constraints/Support.lean): `MapKind`, `MapRef`, `Support`,
`Support.Arrow`, `graph`, `arrow`, `MapResolved`, `Resolved`, `DirectSuper`,
`Extends`, `Widen`, `Support.Boundary`.
[Typing.lean](../Clafer/Constraints/Typing.lean): `Path`, `Path.navigate`,
`signature`, `Constraint.formula`. The signature records graph arity only;
semantic interpretation and actual compilation remain separate work.

Covers:
- `req~clafer-core-support~1`

## Navigation, inheritance and full binding evidence
`proof~clafer-core-support~1`

[Support.lean](../Clafer/Constraints/Support.lean): `Support.incidence` and
`Widen.resolved` prove incidence and actual inheritance ancestry;
`Extends.preserves` transports invariants along inheritance.
[Typing.lean](../Clafer/Constraints/Typing.lean): `Path.navigate` is an
endpoint-indexed construction of well-typed navigation; `Path.navigate_nil`
and `Constraint.formula_binding` preserve the supplied start/binding exactly.
[Constraints/Examples.lean](../Clafer/Constraints/Examples.lean):
`support_resolved`, `widening_follows_super`, `pathNavigation`,
`repeated_scope_retained`, `repeated_maps_retained`, `full_graph_binding`,
`wrong_map_incidence_rejected`.
None of these declarations asserts satisfaction of a constraint predicate.

Covers:
- `req~clafer-core-support~1`

## Compile input and finite identity allocation
`impl~clafer-compile-structure~1`

[Compile/Structure.lean](../Clafer/Compile/Structure.lean) defines `Compile.Input`,
`ConstraintId`, `find`, `resolve`, `family`, `roles` and `labels`.
[Compile/Basic.lean](../Clafer/Compile/Basic.lean) defines `compile` as the actual
MCS construction. The [contract](compile.md) states its assumptions and limits.

Covers:
- `req~clafer-compile-contract~1`
- `req~clafer-compile-structure~1`

## Compile structural preservation
`proof~clafer-compile-structure~1`

In [Structure](../Clafer/Compile/Structure.lean), `find_spec`, `sourceId_injective`,
`resolve_sourceId`, `parent_ids`, `super_ids`, `target_ids`, `shape_preserved`,
`family_wellFormed`, `naming`, `heads_bijective`, `names_preserved` and `referents_preserved` prove
finite resolution and structural preservation. In
[Basic](../Clafer/Compile/Basic.lean), `wellFormed`, `fresh_heads`, `fresh_maps`,
`shared_target` and `maps_finite` establish output validity, freshness, resolved
sharing and finite generated map carriers.
[Examples](../Clafer/Compile/Examples.lean) checks `output_valid`,
`nested_repeated_names`, `shared_reference_target`,
`shared_target_distinct_dereferences`, `inheritance_preserved`,
`primitive_identity`, `reserved_user_rejected`, `zero_map_rejected`,
`zero_generic_input` and `zero_not_compile_support`.
These are structural theorems; no expression interpretation is assumed.

Covers:
- `req~clafer-compile-contract~1`
- `req~clafer-compile-structure~1`

## Compile declarations and occurrence bindings
`impl~clafer-compile-formulas~1`

[Binding](../Clafer/Compile/Binding.lean) constructs `vertex`, `mapOwner`,
`boundArrow` and `binding` from resolved support.
[Local](../Clafer/Compile/Local.lean) defines `LocalId`, `LocalId.formula` and
`localFormulas`. [Basic](../Clafer/Compile/Basic.lean) combines these with typed
constraints using `vocabulary`, `FormulaId`, `formula` and `formulas`.

Covers:
- `req~clafer-compile-formulas~1`

## Compile formula validity and completeness
`proof~clafer-compile-formulas~1`

[Binding](../Clafer/Compile/Binding.lean): `map_spec`, `binding_vertices`,
`binding_maps` and `binding_context` establish incidence, complete support
mapping and owner context. [Local](../Clafer/Compile/Local.lean):
`LocalId.argument_owner`, `LocalId.key_unique`, `localFormulas_wellFormed` and
`local_complete` derive the local bag key and generation completeness.
[Basic](../Clafer/Compile/Basic.lean): `formulas_wellFormed`, `shape_declared`,
`inclusion_declared`, `constraint_declared`, `constraint_owner` and
`constraint_binding` establish the combined bank contract.
[Examples](../Clafer/Compile/Examples.lean): `repeated_support_maps`,
`repeated_support_vertices`, `isolated_vertex_retained`,
`repeated_constraint_boundaries` and
`compiled_constraint_present` exercise occurrence preservation in actual output.

Covers:
- `req~clafer-compile-formulas~1`

## MCS gluing representation
`impl~clafer-gluing-identity~1`

[Gluing.lean](../Clafer/MCS/Gluing.lean), namespace `Clafer.MCS.Gluing`:
`Class`, `Map`, `classLabel`, `mapLabel`, `Incidence`, `source`, `target`,
`Arrow`, `graph`, `label`, `labeledArrow`, `Compatible`. Used referents determine
identity; representative choice only defines functions on already chosen fibers.
Compatibility checks incidence, names, registry annotations and modes.

Covers:
- `req~clafer-gluing-identity~1`
- `req~clafer-mcs-metamodel~1`
- `req~clafer-mcs-disciplines~1`

## MCS gluing identification proofs
`proof~clafer-gluing-identity~1`

[Gluing.lean](../Clafer/MCS/Gluing.lean): `classLabel_eq_iff`, `mapLabel_eq_iff`,
`classRepresentative_spec`, `mapRepresentative_spec`, `source_label`,
`target_label`, `arrowData_ext`, `labeledArrow_eq_iff`, `label_obj_surjective`.
The total-arrow equality theorem includes endpoint agreement and ensures
that different map referents cannot collapse even at equal endpoints/names.

Covers:
- `req~clafer-gluing-identity~1`

## Exact declaration image
`impl~clafer-gluing-declarations~1`

[Gluing.lean](../Clafer/MCS/Gluing.lean): `diagram`, `labelHom`. Declarations
are a set image of complete translated formulas; the source bank's indexed
identity and key are not asserted for the target image.

Covers:
- `req~clafer-gluing-declarations~1`
- `req~clafer-mcs-formulas~1`
- `req~dpgraph-morphisms~1`

## Declaration and binding preservation
`proof~clafer-gluing-declarations~1`

[Gluing.lean](../Clafer/MCS/Gluing.lean): `declared_iff`, the `preserves` proof
in `labelHom`, `translated_vertex`, `translated_arrow`. `label` is the actual
incidence-checked Prefunctor used by every formula translation.

Covers:
- `req~clafer-gluing-declarations~1`

## Glued CD metadata and assumptions
`impl~clafer-gluing-formalcd~1`

[Gluing.lean](../Clafer/MCS/Gluing.lean): `raw`, `Naming`, `Defaults`, `cd`.
[Origins.lean](../Clafer/MCS/Gluing/Origins.lean): `Predefined`, `registry`,
`originAnnotation`, `annotations`, `ofValid`. Names are metadata; semantic
origins select registry identities and kinds. Defaults are source-bank
membership hypotheses over the compatible vocabulary embedding.

Covers:
- `req~clafer-gluing-formalcd~1`
- `req~formalcd-structure~1`
- `req~formalcd-naming~1`
- `req~formalcd-declarations~1`
- `req~formalcd-morphisms~1`

## Separate FormalCD well-formedness
`proof~clafer-gluing-formalcd~1`

[Gluing.lean](../Clafer/MCS/Gluing.lean): `className_label`, `mapName_label`,
`predefined_label`, `kind_label`, `mode_label`, `raw_wellFormed`.
[Origins.lean](../Clafer/MCS/Gluing/Origins.lean): `annotations_head`,
`naming_of_valid`. The latter derives naming and predefined uniqueness from
`MCS.Valid`, but neither it nor `labelHom` assumes effective-default completeness.
`raw_wellFormed` explicitly requires that separate hypothesis.

Covers:
- `req~clafer-gluing-formalcd~1`

## MCS gluing acceptance fixtures
`impl~clafer-gluing-examples~1`

[Examples.lean](../Clafer/MCS/Gluing/Examples.lean), namespace
`Clafer.MCS.Gluing.Examples`: `family`, `labels`, `predef`, `formulas`, `glued`,
`emptyBank`, `badEndpoints`, `badClassNames`, `badMapNames`, `badAnnotation`.
[Boundaries.lean](../Clafer/MCS/Gluing/Boundaries.lean), namespace
`Clafer.MCS.Gluing.Boundaries`: the existing eleven-owner MCS fixture,
`modeConflict`, `completeBank`, `completeCD`, `Isolated.binding`, `Isolated.bank`.

Covers:
- `req~clafer-gluing-examples~1`

## MCS gluing acceptance proofs
`proof~clafer-gluing-examples~1`

[Examples.lean](../Clafer/MCS/Gluing/Examples.lean): `compatible`, `valid`,
`defaults`, `intentional_class_merge`, `intentional_map_merge`,
`parallel_maps_distinct`, `translated_formulas_not_injective`,
`canonical_name_preserved`, `registry_kind_preserved`, `empty_valid`,
`empty_defaults_rejected`, `empty_cd_rejected`, `source_conflict_rejected`,
`target_conflict_rejected`, `class_name_conflict_rejected`,
`map_name_conflict_rejected`, `annotation_and_kind_conflict_rejected`.
The nonempty source bank satisfies the literal bag key even though its
translated formulas are not injective. `glued` carries the separate CD proof.

[Boundaries.lean](../Clafer/MCS/Gluing/Boundaries.lean):
`repeated_parent_not_identified`, `repeated_isA_not_identified`,
`bag_mode_preserved`, `bag_has_no_added_setValued`, `missing_default_rejected`,
`mode_conflict_rejected`, `spelling_does_not_create_marker`,
`reserved_spelling_rejected`, `primitive_identity_preserved`,
`complete_valid`, `complete_defaults`, `inclusion_default_preserved`,
`repeated_arguments_retained`,
`Isolated.bank_valid`, `Isolated.isolated_vertex_retained`,
`Isolated.isolated_declaration_preserved`. These are kernel-checked structural
claims, not model satisfaction or compiler correctness statements.

Covers:
- `req~clafer-gluing-examples~1`

## Effective structural core
`impl~clafer-effective-core~1`

[EffectiveCore.lean](../Clafer/Semantics/EffectiveCore.lean): `EffectiveCore`,
`WellFormed`, `Supported`, `erase`. [Admission.lean](../Clafer/Verification/Admission.lean):
`CoreCertificate`, `coreChecks`, `supportChecks`. The
[interface](structural-checker.md) explains effective fields and fragment guards.

Covers:
- `req~clafer-effective-core~1`

## Effective-core correspondence proofs
`proof~clafer-effective-core~1`

[EffectiveCore.lean](../Clafer/Semantics/EffectiveCore.lean): `erase_wellFormed`,
`erase_shape`. [Bridge.lean](../Clafer/Semantics/Bridge.lean): `ConstraintFree`,
`compiled_bank_iff`, `erasure_correspondence`, `equal_erasure_satisfaction`.
[Admission.lean](../Clafer/Verification/Admission.lean): `admitted_wellFormed`,
`admitted_supported`, `certificate_exists`. Erasure uses the existing
`Compile.Input` and its naming/default obligations; no authored AST is fabricated.

Covers:
- `req~clafer-effective-core~1`

## Whole-model structural meaning
`impl~clafer-structural-satisfaction~1`

[Structural.lean](../Clafer/Semantics/Structural.lean): `Configuration`,
`StructuralSatisfies`, `Typed`, `Rooted`, `Inherits`, `Abstracts`, `Parents`,
`References`, `Keys`, `Multiplicities`, `Child`, `Groups`.
[Interpretation.lean](../Clafer/Semantics/Interpretation.lean): `headMap`,
`derefMap`, `targetMap`, `ordinaryMap`, `inclusionMap`, `interpret`.
[Bridge.lean](../Clafer/Semantics/Bridge.lean): `LocalConditions`,
`GlobalConditions`, `structuralInterpretation`, `SatisfiesAST`.

Covers:
- `req~clafer-structural-satisfaction~1`

## Structural interpretation and representation proofs
`proof~clafer-structural-satisfaction~1`

[Bridge.lean](../Clafer/Semantics/Bridge.lean): `key_local_iff`, `local_model_iff`,
`structural_model_iff` connect independent clauses to the exact local compiled
bank plus explicit global obligations. [Abstracts.lean](../Clafer/Semantics/Abstracts.lean):
`abstracts_iff` gives the existing Cover/Q8 Disjoint meaning.
[Relational.lean](../Clafer/Semantics/Relational.lean): `inRange_one_iff`,
`one_iff_total_single`, `compositeFiber`, `composite_multiplicity`, `two_key_iff`,
`parent_one_iff`, `deref_one_iff`. [Interpretation.lean](../Clafer/Semantics/Interpretation.lean):
`headFiberEquiv`, `head_multiplicity_iff`, `ordinary_representation`.
[Normalization.lean](../Clafer/Semantics/Normalization.lean): `SpanModel.headIso`,
`derefIso`, `parentIso`, `targetIso`, `inheritedIso`, `normalize_satisfies` extract
simultaneous relational representatives from arbitrary local-bank models.
[Representation.lean](../Clafer/Verification/Representation.lean): `realize_encode`,
`representable`, `finite_model_representable` give finite completeness.
[Renaming.lean](../Clafer/Semantics/Renaming.lean): `structural_rename`.
[Reachability.lean](../Clafer/Semantics/Reachability.lean): `structural_reaches`,
`concrete_descendant`, `unused_abstract_empty`.

Covers:
- `req~clafer-structural-satisfaction~1`
- `req~predicate-key~1`
- `req~predicate-key-functional~1`
- `req~predicate-multiplicity~1`
- `req~predicate-interpretation~1`

## Finite structural checker
`impl~clafer-finite-checker~1`

[Finite.lean](../Clafer/Verification/Finite.lean): `Candidate`, `realize`,
`CountInRange`, `multiplicityChecks`, `groupChecks`, `Checks`, `check`.
[Protocol.lean](../Clafer/Verification/Protocol.lean): `RawCandidate`, `decode`,
`InputError`, `Result`, `verify`. [Admission.lean](../Clafer/Verification/Admission.lean):
`RunResult`, `run`. Ordinary tuples and reference-head occurrences retain distinct
identities; [protocol documentation](structural-checker.md#executable-interface)
states error priority and checked-certificate input requirements.

Covers:
- `req~clafer-finite-checker~1`

## Checker and protocol correctness
`proof~clafer-finite-checker~1`

[Finite.lean](../Clafer/Verification/Finite.lean): `inRange_card`, `checks_iff`,
`check_correct`, `malformed_rejected`. [ProtocolProofs.lean](../Clafer/Verification/ProtocolProofs.lean):
`decode_root`, `decode_members`, `decode_containment`, `decode_references`,
`objectLabels`, `member_row_preserved`, `link_row_indices`, `tuple_identity`,
`verify_correct`, `verify_violation`, `illTyped_rejected`, `success_tablesValid`,
`malformed_tables_rejected`, `run_correct`. [Protocol.lean](../Clafer/Verification/Protocol.lean):
`duplicate_objects_rejected`, `missing_root_rejected`.
[Admission.lean](../Clafer/Verification/Admission.lean): `unsupported_rejected`.
These are kernel proofs; no claim of fresh per-instance proof certificates is made
for native execution.

Covers:
- `req~clafer-finite-checker~1`

## Structural checker fixtures and mutation controls
`impl~clafer-checker-witnesses~1`

[Examples.lean](../Clafer/Verification/Examples.lean), namespace
`Clafer.Verification.Examples`: `refs`, `bag`, `collapsed`, `overlapping`,
`rawBag`, `inheritance`, `nested`, `siblingOverlap`, `uncovered`, `emptyClasses`,
`cyclic`, `cycle`, `noOccurrences`, `twoParents`, `sharedTarget`,
`multipleParents`, `multipleTargets`, `unusedChain`, `onlyRoot`,
`collapseMutant`, `upperBoundMutant`, `missingChild`, `relaxedGroup`, `executableTests`.

Covers:
- `req~clafer-checker-witnesses~1`

## Structural checker kernel witnesses
`proof~clafer-checker-witnesses~1`

[Examples.lean](../Clafer/Verification/Examples.lean): `bag_satisfies`,
`set_not_satisfies`, `set_rejects_repetition`, `exact_two_accepts`,
`optional_rejects_two`, `zero_rejects_two`, `lower_three_rejects`,
`unbounded_accepts`, `group_three_accepts`, `group_two_rejects`,
`unrelated_overlap_and_union`, `missing_target_violates`, `missing_target_typed`,
`nested_satisfies`, `nested_reachable`, `sibling_overlap_rejected`,
`uncovered_abstract_rejected`, `empty_classes_accept`, `reference_cycle_accepts`,
`zero_accepts_empty`, `optional_accepts_empty`, `optional_accepts_one`,
`missing_child_group_rejected`, `missing_child_locally_valid`,
`set_shared_target_accepts`, `multiple_parents_typed`, `multiple_parents_rejected`,
`multiple_targets_typed`, `multiple_targets_rejected`, `unused_chain_satisfies`,
`protocol_accepts`, `protocol_set_violates`, `duplicate_identity`,
`duplicate_tuple`, `duplicate_membership`, `missing_root`, `dangling_identity`,
`unknown_class`, `ill_typed_endpoint`, `empty_reference_table_violates`,
`collapse_mutant_killed`, `upper_bound_mutant_killed`. Reduction-based witnesses
exercise finite inputs without `native_decide` or new axioms.

Covers:
- `req~clafer-checker-witnesses~1`

## Structural checker native regression execution
`utest~clafer-structural-checker~1`

[structural_checker.lean](../tests/structural_checker.lean) executes
`Clafer.Verification.Examples.executableTests` from
[Examples.lean](../Clafer/Verification/Examples.lean), including mutation controls
on unchanged reference fixtures. `scripts/check.sh` discovers and runs this test
and builds/audits/replays all library witness modules. Command-level evidence
records the full command outcome, not a separate per-artifact certificate.

Covers:
- `req~clafer-finite-checker~1`
- `req~clafer-checker-witnesses~1`
