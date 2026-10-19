# Structural Compile

`Clafer.Compile.compile` implements SoSyM §6.2.4 (p.21), producing the
[Figure 23/Appendix E MCS](mcs-invariants.md) under `Compile.Input`.
See the [product intent](intent.md), [requirements](spec.md#structural-compile-input-contract)
and [source decisions](sources.md#structural-compile-contract).

## Accepted input

The AST is finite, resolved and defaulted, with unique `DeclId`s and the existing
`AST.WellFormed` hierarchy, reference, primitive, multiplicity and boundary
conditions. Compile additionally requires canonical `Sing` naming and rejects
user names reserved for `Sing`, `int`, `string` and `bool`. Primitive names remain
canonical and origins explicitly select predefined classification. Compile does
not infer primitive meaning from a user spelling.

Every attached constraint position supplies a body satisfying `Constraint.Input`
for that exact boundary. Owner and list position identify the attachment;
source boundary numbers and strings need not be globally unique. Compile's
additional `0 < support.mapCount` precondition supplies the MCS total-args
obligation. A Boolean literal with only its context vertex is therefore outside
this Compile contract, while remaining legal generic constraint input. An
accepted constraint may include isolated support vertices alongside its maps.
No minimal-support extraction, name resolution, default elaboration or binder
inference is performed.

## Construction and guarantees

The existing structural traversal lists declarations in preorder. Class role
identities are `Fin entries.length`; a terminating finite search resolves each
parent, super and target ID to its unique position. Reference cycles never
become recursive calls. The head of each declaration is its own position;
source and target slots cojoin at the resolved parent's and target's heads.
Ordinary map identities pair the owner position with the exact map role.
Inclusions retain their owner, selected super and shared class role.

The family retains the complete authored/effective group record without another
defaulting pass; `group_bounds_valid` derives effective interval validity from
the AST. `DirectChild` derives the finite own-child inventory from resolved
parent identity, and `directChildHead` supplies each child's typed head map,
including reference children. These data guarantees feed the separate interpreted group extension described in
the [group compilation contract](group-compilation.md). `compileAugmented` retains
this structural result and adds every concrete context's effective group predicate
over its own and inherited child heads, including vertex-only empty inventories.

Allocation is deterministic for the same ordered AST. Equal display names do
not coalesce identities. Repeated references to one uniquely declared `DeclId`
share its class, while reference heads and dereference maps remain distinct.
Reordering or inserting declarations can change preorder IDs; persistent IDs
across edits and aliasing between distinct declaration heads are not promised.
The class referent records the source `DeclId`; map referents retain the generated
slot identity, separately from display names. No string-based gluing occurs.

`family_wellFormed` derives the MCS hierarchy, kind, rank and bound conditions
from AST well-formedness. `naming` derives canonical naming and reserved-user-name
rejection. Typed arrows supply incidence and canonical roles supply cojoining;
`compile` bundles these with the formula-bank proof. The construction and its
finite lookup reduce in Lean's kernel. The AST traversal and dependent lookup are marked `noncomputable` to avoid
compiler-generated unsafe native helpers; they remain kernel-reducible. This
is a defined transformation, with no choice of an output,
existence axiom or native compiler executable.

## Generated declarations

The local bank generates ordinary set-valued defaults, effective multiplicities,
inverse, triangle and set-reference key predicates with exactly the existing
Shape guards, plus an inclusion predicate for every guarded super slot. Built-in
symbols retain their identity in `FormalCD.Vocabulary.extend`.

A constraint occurrence selects its existing syntax-only predicate symbol and
full support-graph arity. The compiler resolves every support vertex and map,
including isolated vertices and repeated occurrences. The current support
`inclusion` role addresses head inheritance; all shared source/target inclusion
slots still exist structurally. Its binding is constructed from input incidence,
not supplied by the caller. Context maps to the owner head.

`LocalId.key_unique` proves the literal bag key for generated local declarations:
permuting arguments cannot change the unique owner/role that generated the
predicate. Constraint symbols are indexed by source attachment, as in the
existing constraint signature; equal bodies at distinct attachments remain
separate symbols. `formulas_wellFormed` proves total args and the combined key.
`shape_declared`, `inclusion_declared` and `constraint_declared` state completeness
for this inventory. Full binding data is never replaced by a bag or a quotient.

The complete augmented bank contains both original and group declarations; it is
not asserted to satisfy MCS total args. `gluedGroups` preserves its exact translated
union with naming, metadata and effective-default completeness. Group satisfaction
is equivalent to the selected child-object bounds for typed configurations, with
explicit finite-count assumptions for numeric cardinalities.

## Limits and examples

[Examples](../Clafer/Compile/Examples.lean) compile a nonempty resolved AST with
nested repeated names, abstract declarations, inheritance, a reference cycle,
shared reference targets and repeated constraint/support occurrences. They check
explicit primitive classification and rejection of reserved user names and
zero-map Compile support. The output validity theorem quantifies over every
accepted input, beyond these finite witnesses.

The delivered typed-core limits remain in force. The [selected semantic extension](constraint-preservation.md) derives constraint
meanings from typed bodies and explicit external domains; the
[integer extraction interface](integer-extraction.md) supplies selected partial
singleton conversion and version-operand definedness. A fresh constraint symbol
does not
establish any meaning for its body.

The guarded constraint-free
[structural checker](structural-checker.md) supplies a whole-model interpretation
of the exact generated local bank plus explicit global root, abstract, group
and declaration-disjointness obligations. `compiled_bank_iff` and
`erasure_correspondence` prove this selected
structural connection; they do not assert source elaboration or user-expression
preservation.

The delivered
[MCS gluing](architecture.md#mcs-gluing) provides a label morphism and conditional
`FormalCD` validity under its explicit incidence, metadata and default-completeness
hypotheses. The group extension derives those hypotheses for Compile output.

The
[representative integration](representative-models.md) instantiates the two
constructions for nesting, inheritance, references, typed attachments and actual
generated xor predicates. Its selected version example derives operand
definedness from emitted local formulas plus explicit integer-domain realization;
the [selected bridge](constraint-preservation.md) supplies its separate semantic
correspondence under explicit admissibility assumptions.

## Selected inherited realization extension

[The Appendix F contract](inherited-realization.md) adds
`Compile.Realization.compileRealized`, retaining `compileAugmented` exactly.
The additional bank generates actual built-in cover/disjoint predicates for every
explicit abstract and group predicates for ordinary fields made effectively
abstract by containment. `whole_model` relates the generated/glued bank to the
independent extended structural conditions plus each original authored occurrence's
meaning, with typedness, root and declaration disjointness explicit on the model
side. Context views restrict the same interpreted links. This result does not
extend the #50 checker. The [constraint preservation extension](constraint-preservation.md)
fixes its authored-meaning parameter from #68’s typed denotation and explicit
external domains, retaining the selected model assumptions.
