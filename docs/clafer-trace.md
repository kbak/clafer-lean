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
