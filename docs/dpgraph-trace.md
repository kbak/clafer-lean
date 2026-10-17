# DP-graph trace artifacts

Follow [the Lean trace convention](traceability.md): these are named Markdown
artifacts; their evidence is the linked Lean declarations, not inline Lean tags.
The [source map](SOURCES.md) records SoSyM B.1–B.2 spans, the adopted Q1
correction, B.4 Definitions 6–10 and the abstract restriction argument of
B.5 Theorem 3.
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
[scripts/check.sh](../scripts/check.sh) builds the complete inventory in one Lake
invocation and passes the three public roots to one verbose `leanchecker`, which
enumerates their compiled descendants without repeated overlapping targets.
It executes the audit after kernel checking,
with warnings treated as errors. This is a validation test, not a theorem
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

## Model reduct injectivity implementation
`impl~model-reduct-injective~1`

[ModelTransport.lean](../DPGraph/ModelTransport.lean):
`Interpretation.reduct_injective_of_comp_eq_id` states injectivity of `I.reduct F`
under `J.comp F = Hom.id T`, with independent signature, source/target carrier
and semantic universes. [DPGraph.lean](../DPGraph.lean) publicly imports it.
This is a derived consequence of the existing abstract reduct laws from SoSyM
B.4 Definitions 9–10 and B.5 Theorem 3, not a verbatim paper theorem.

Covers:
- `req~model-reduct-injective~1`

## Model reduct injectivity proof
`proof~model-reduct-injective~1`

[ModelTransport.lean](../DPGraph/ModelTransport.lean):
`Interpretation.reduct_injective_of_comp_eq_id` applies `I.reduct J` to equality
of reducts and recovers equality of the original models using `reduct_comp`,
`J.comp F = Hom.id T` and `reduct_id`.

Covers:
- `req~model-reduct-injective~1`

## Model reduct surjectivity implementation
`impl~model-reduct-surjective~1`

[ModelTransport.lean](../DPGraph/ModelTransport.lean):
`Interpretation.reduct_surjective_of_comp_eq_id` states surjectivity of `I.reduct F`
under `F.comp J = Hom.id S`, with independent signature, source/target carrier
and semantic universes. [DPGraph.lean](../DPGraph.lean) publicly imports it.
This is a derived consequence of the existing abstract reduct laws from SoSyM
B.4 Definitions 9–10 and B.5 Theorem 3, not a verbatim paper theorem.

Covers:
- `req~model-reduct-surjective~1`

## Model reduct surjectivity proof
`proof~model-reduct-surjective~1`

[ModelTransport.lean](../DPGraph/ModelTransport.lean):
`Interpretation.reduct_surjective_of_comp_eq_id` gives `I.reduct J m` as the
preimage of any source model `m`, using `reduct_comp`, `F.comp J = Hom.id S`
and `reduct_id`. Neither result adds assumptions on predicate meanings or claims
whole-model reflection for arbitrary DP morphisms.

Covers:
- `req~model-reduct-surjective~1`

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

## Span representation
`impl~span-representation~1`

[Span/Basic.lean](../DPGraph/Span/Basic.lean): `Span` has independent endpoint/head
universes and total legs, and `Span.Iso` requires a head equivalence preserving
both endpoints. It imposes no endpoint injectivity. SoSyM B.1 Definitions 1–5.

Covers:
- `req~span-representation~1`

## Span isomorphism operations
`proof~span-representation~1`

[Span/Basic.lean](../DPGraph/Span/Basic.lean): the equivalence and commuting proof
fields of `Span.Iso.refl`, `.symm` and `.trans` implement identity, symmetry and
transitivity across head universes. `Span.Iso.red_eq` proves preservation of
endpoint membership. [Span/Examples.lean](../DPGraph/Span/Examples.lean)'s
`Span.Examples.parallel_links` witnesses retained parallel links.

Covers:
- `req~span-representation~1`

## Indexed mapping implementation
`impl~span-family-correspondence~1`

[Span/IndexedFamily.lean](../DPGraph/Span/IndexedFamily.lean): `IndexedFamily`,
`.Equivalence`, `.toSpan`, `.red` and `Span.toFamily` implement indexed mappings,
fiber equivalences, sigma heads and source fibers. The source/index universe join
is explicit in `toSpan`. [Span/Basic.lean](../DPGraph/Span/Basic.lean)'s `Span.red`
is existential endpoint membership.

Covers:
- `req~span-family-correspondence~1`

## Indexed mapping roundtrips and membership proofs
`proof~span-family-correspondence~1`

[Span/IndexedFamily.lean](../DPGraph/Span/IndexedFamily.lean): the equivalence,
inverse and commuting proof fields in `Span.familySpanIso` and
`IndexedFamily.spanFamilyEquivalence` prove both roundtrips without resizing.
`Span.red_toFamily` and `IndexedFamily.red_toSpan` prove the endpoint-membership
correspondence of B.1 Theorem 1. [Span/Relation.lean](../DPGraph/Span/Relation.lean)'s
`Span.red_ofRelation` supplies the relation roundtrip.

Covers:
- `req~span-family-correspondence~1`

## Set-valuedness implementation
`impl~span-set-valuedness~1`

[Span/Basic.lean](../DPGraph/Span/Basic.lean): `Span.JointlyInjective` concerns the
pair of endpoints. [Span/Relation.lean](../DPGraph/Span/Relation.lean):
`Span.ofRelation` has the subtype of satisfying endpoint pairs as its head,
in the join of endpoint universes; `Span.toRelation` is the canonical endpoint map.

Covers:
- `req~span-set-valuedness~1`

## Set-valuedness proofs
`proof~span-set-valuedness~1`

[Span/Relation.lean](../DPGraph/Span/Relation.lean):
`Span.jointlyInjective_iff_fiberwise`, `.jointlyInjective_iff_iso_relation` and
`.relationIso` prove both equivalences in B.1 Theorem 2.
`Span.ofRelation_jointlyInjective`, `.red_ofRelation` and `.toRelation_surjective`
establish the relation representation and quotient properties. `relationIso` uses
standard classical choice to invert a bijection, with no additional axiom.

Covers:
- `req~span-set-valuedness~1`

## Span composition implementation
`impl~span-composition~1`

[Span/Composition.lean](../DPGraph/Span/Composition.lean): `Span.comp` uses a
subtype of link pairs, preserving all compatible pairs in source-to-target order.
`Span.identity` uses the endpoint type as its head. `IndexedFamily.comp` uses the
dependent sum of indices. Their result universe joins are explicit.

Covers:
- `req~span-composition~1`

## Span composition proofs
`proof~span-composition~1`

[Span/Composition.lean](../DPGraph/Span/Composition.lean): `Span.leftUnit`,
`.rightUnit` and `.associator` contain inverse and endpoint-commutation proofs for
the canonical head equivalences. `IndexedFamily.compSpanIso` and
`Span.compFamilyEquivalence` establish compatibility of composition under both
conversions. These are head/fiber equivalences, with no strict head equality or
extra finiteness or decidability assumption.

Covers:
- `req~span-composition~1`

## Inversion implementation
`impl~span-inversion~1`

[Span/Basic.lean](../DPGraph/Span/Basic.lean): `Span.inverse` retains the head and
swaps the legs, as in SoSyM B.2.2.

Covers:
- `req~span-inversion~1`

## Inversion proofs
`proof~span-inversion~1`

[Span/Basic.lean](../DPGraph/Span/Basic.lean): `Span.inverse_inverse` proves
involution and `Span.red_inverse` proves relational converse by endpoint
membership. Neither states categorical invertibility.

Covers:
- `req~span-inversion~1`

## Relation composition implementation
`impl~span-relation-composition~1`

[Span/Relation.lean](../DPGraph/Span/Relation.lean): `relationComp` is existential
composition, `Span.compToRelation` maps every link pair to its outer endpoints,
`SingleValued` imposes no totality, and `UniqueIntermediate` asserts at most one
intermediate object per outer endpoint pair. `Span.compRelationIso` constructs
an endpoint-preserving head equivalence under composite joint injectivity.

Covers:
- `req~span-relation-composition~1`

## Adopted Q1 correction proofs
`proof~span-relation-composition~1`

[Span/Relation.lean](../DPGraph/Span/Relation.lean): `Span.red_comp` and
`.compToRelation_surjective` have no injectivity, finiteness or decidability
hypothesis. `Span.comp_iso_relation_iff` states the exact stronger-isomorphism
criterion. `Span.comp_jointlyInjective_iff_uniqueIntermediate` assumes joint
injectivity of each input; `.relations_comp_jointlyInjective_iff` specializes to
canonical relation spans. `.relations_comp_injective_of_first_singleValued` and
`.relations_comp_injective_of_converse_second_singleValued` prove the sufficient
cases without totality, through `uniqueIntermediate_of_singleValued` and
`uniqueIntermediate_of_converse_singleValued`. The [source comparison](SOURCES.md#span-composition-q1-research-for-4)
identifies this as an adopted correction to B.2.1, not its verbatim claim.

Covers:
- `req~span-relation-composition~1`

## Span example constructions
`impl~span-examples~1`

[Span/Examples.lean](../DPGraph/Span/Examples.lean), under `Span.Examples`:
`parallel`, `empty`, `empty_family`, `empty_endpoints`, `first`, `second`, `path`,
`partialFirst`, `large`, `raisedSource` and `raisedFamily` construct the boundary
cases. `large` separates endpoint universes 1/2 and link universe 3;
`raisedSource` and `raisedFamily` exercise a small head/index lifted by a source
in universe 2. [public_imports.lean](../tests/public_imports.lean) exercises the
API through independent `import DPGraph` and rejects imports of the examples.

Covers:
- `req~span-examples~1`

## Span example proofs
`proof~span-examples~1`

[Span/Examples.lean](../DPGraph/Span/Examples.lean), under `Span.Examples`:
`parallel_links`, `parallel_not_jointlyInjective`, `parallel_reduction`,
`empty_fibers`, `empty_reduction`, the empty roundtrips and
`empty_endpoints_no_links` establish the basic boundary cases.
`twoPaths` is a head equivalence with `Bool`; `oneReducedPair` is an equivalence
with `Unit`. `paths_distinct`, `two_path_reduction`, `two_path_not_iso` and
`second_singleValued_not_sufficient` preserve the source counterexample.
`parallel_uniqueIntermediate` and `parallel_composite_not_iso` establish why the
intermediate-object criterion requires relational inputs. `partialFirst_not_total`
and the two `partial_*_composite_injective` proofs exercise partial relations.
`large_roundtrip`, `large_family_roundtrip`, `large_left_unit`, `large_right_unit`,
`large_associator`, `large_family_composition`, `large_relation_composition`,
`large_relation_iso`, `raisedSource_roundtrip` and `raisedFamily_roundtrip`
exercise conversions and laws across universes. These are all kernel-checked
declarations; examples do not replace the general theorems.

Covers:
- `req~span-examples~1`

## Carrier-cocone data implementation
`impl~dpgraph-pushout-data~1`

[Pushout/Basic.lean](../DPGraph/Pushout/Basic.lean): `Pushout.CarrierCocone` fixes
the bundled-quiver category explicitly. `Pushout.obj` uses exactly
the union of the two translated declaration images. `Pushout.inl`, `inr` and
`cocone` retain the supplied carrier maps and equation; `CompatibleModels` is
the subtype of component models with equal reducts. [DPGraph.lean](../DPGraph.lean)
exports these definitions without upper-layer imports.

Covers:
- `req~dpgraph-pushout-data~1`

## Carrier-cocone preservation proofs
`proof~dpgraph-pushout-data~1`

[Pushout/Basic.lean](../DPGraph/Pushout/Basic.lean): the `preserves` fields in
`Pushout.inl` and `inr` use the respective declaration-image membership witness.
`Pushout.cocone` proves commutation by `Hom.ext` and the supplied carrier
cocone equation. No universal-property or amalgamation proof is assumed here.

Covers:
- `req~dpgraph-pushout-data~1`

## Pushout universal property implementation
`impl~dpgraph-pushout-universal~1`

[Pushout/Universal.lean](../DPGraph/Pushout/Universal.lean): `Pushout.isColimit`
takes `F J c hc` in that order and constructs `IsColimit (Pushout.cocone F J c)`.
It imports only `Pushout.Basic`, retains the independent signature universes and
fixed carrier universes, and uses the supplied carrier colimit's mediator for
each target DP cocone. [DPGraph.lean](../DPGraph.lean) publicly exports the result.
The source basis is SoSyM B.4 Definitions 9–10 and the abstract B.5 representation;
the universal property is a derived result, not a verbatim theorem of the paper.

Covers:
- `req~dpgraph-pushout-universal~1`

## Pushout universal property proof
`proof~dpgraph-pushout-universal~1`

[Pushout/Universal.lean](../DPGraph/Pushout/Universal.lean): `Pushout.isColimit`
constructs a declaration-preserving mediator. Its preservation proof splits
membership in the declaration union, uses `Formula.translate_comp` and the
carrier factorization equations, then applies the corresponding target leg's
`Hom.preserves`. Its two DP factorization equations follow from `hc.fac` by
`Hom.ext`; uniqueness follows from `PushoutCocone.IsColimit.hom_ext hc` and
`Hom.ext`. These kernel-checked fields establish the full `IsColimit`, with no
additional axioms or model amalgamation assumption.

Covers:
- `req~dpgraph-pushout-universal~1`

## Model amalgamation implementation
`impl~dpgraph-model-amalgamation~1`

[Pushout/Models.lean](../DPGraph/Pushout/Models.lean): `Pushout.modelEquiv`
maps a model to exactly its two reducts and uses the private `Pushout.amalgamate`
for its inverse. That helper applies `PushoutCocone.IsColimit.desc` to the two
underlying component maps and their compatibility equation. The module imports
`Pushout.Basic` independently; [DPGraph.lean](../DPGraph.lean) publicly imports it.
Only this equivalence restricts `Ω` to the carrier universes. This is a derived
result over SoSyM B.4 Definitions 9–10 and abstract B.5 Theorem 3.

Covers:
- `req~dpgraph-model-amalgamation~1`

## Model amalgamation proofs
`proof~dpgraph-model-amalgamation~1`

[Pushout/Models.lean](../DPGraph/Pushout/Models.lean): the private
`Pushout.amalgamate` proves satisfaction by splitting membership in the union of
declaration images, applying `Interpretation.satisfies_translate`, and using the
appropriate carrier factorization equation and component model proof.
Private `Pushout.amalgamate_inl` and `Pushout.amalgamate_inr` prove the inverse's
reducts recover the component models. In `Pushout.modelEquiv`, the forward
compatibility proof uses the reduct composition law and cocone equation;
`left_inv` uses carrier-colimit uniqueness, while `right_inv` uses the two helper
equations and subtype/product extensionality. `Pushout.modelEquiv_fst` and
`Pushout.modelEquiv_snd` prove the required forward projection equations with
explicit argument order `F J c I hc m`. All proof obligations use the supplied
carrier colimit and existing satisfaction semantics, without additional axioms.

Covers:
- `req~dpgraph-model-amalgamation~1`

## Public pushout interfaces
`itest~dpgraph-pushout-public-api~1`

[public_imports.lean](../tests/public_imports.lean) imports only `DPGraph` and
checks the common cocone-data names. Its universe-polymorphic typed examples
exercise `Pushout.isColimit`, `modelEquiv`, `modelEquiv_fst` and `modelEquiv_snd`
with the required explicit argument order and exact projection equations. The
existing import-environment audit still rejects upper layers and examples. The
shared check compiles this test with warnings as errors.

Covers:
- `req~dpgraph-pushout-data~1`
- `req~dpgraph-pushout-universal~1`
- `req~dpgraph-model-amalgamation~1`
