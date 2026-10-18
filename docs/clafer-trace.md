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
repetitions; a future #21 implementation attaches expression bodies without a
reverse dependency from the boundary module.

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
