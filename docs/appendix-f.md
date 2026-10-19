# Complete Appendix F Telematics model

The full fixture combines the [reviewed declaration and constraint inventory](inherited-realization.md#scoped-source-to-core-inventory)
with the [resolved expression meanings](constraint-denotation.md) and the
[selected Compile/gluing bridge](constraint-preservation.md). Its primary source
is SoSyM Appendix F p.34, with Appendix C, D and E and §5.3–5.5/§6.2.
The archived PDF SHA-256 is
`56b1c18e74807fb7646c0e89cb2fc306f4178affb41fee52fcebde09b031b2fb`.
The source indentation, repeated names and constraint scopes are checked manually.
The accepted Q1–Q9 and D2/D4/D6 decisions remain those of the
[source map](SOURCES.md) and [inherited realization contract](inherited-realization.md).

The authoritative acceptance requirements are [complete integration](spec.md#complete-resolved-appendix-f-integration)
and [rejection witnesses](spec.md#complete-appendix-f-rejection-witnesses).
They reuse the existing contracts for:

- [Group compilation](spec.md#interpreted-group-compilation-and-augmented-gluing),
  [inherited realization](spec.md#selected-inherited-field-and-explicit-abstract-realization)
  and [generated structural correspondence](spec.md#generated-inherited-realization-and-structural-correspondence).
- [Integer extraction](spec.md#integer-extraction-from-primitive-navigation) and
  [version operand definedness](spec.md#appendix-f-version-operand-well-definedness).
- [Model environments](spec.md#explicit-constraint-model-environments),
  [core denotation](spec.md#independent-core-denotation),
  [expression inventory](spec.md#appendix-f-resolved-expression-inventory),
  [predicate meanings](spec.md#derived-source-constraint-predicate-meanings),
  [Compile/gluing preservation](spec.md#selected-compile-and-gluing-constraint-correspondence)
  and [preservation sensitivity](spec.md#constraint-preservation-sensitivity-and-appendix-f-support).
- [Representative integration](spec.md#representative-compilation-and-gluing) and
  [paper coverage accounting](spec.md#representative-paper-coverage-accounting),
  whose narrower acceptance boundaries remain intact.

## Resolved input and generated diagrams

[AppendixF](../Clafer/Examples/AppendixF.lean) reuses `Inherited.decl` for all
26 printed declarations and attaches the exact `AppendixFConstraints.inventory`
bodies through `occurrence`. The source declaration IDs remain d01–d26,
with root=0 and int=27. Preorder occurrence positions remain distinct from
source IDs, displayed names and constraint positions. `sourceIndex_occurrence`
and `occurrence_sourceIndex` exhaust both directions of the attachment map;
`occurrence_owner` identifies the owner of each printed conjunct.

| Source conjunct | Owner ID | Preorder position | Position in owner |
| --- | --- | --- | --- |
| c01 | d01 options | 13 | 0 |
| c02 | d11 display | 23 | 0 |
| c03, c04 | d15 plaDisplay | 27 | 0, 1 |
| c05–c09 | d19 telematics | 4 | 0–4 |
| c10–c12 | root | 0 | 0–2 |

Each attachment retains the complete 28-vertex/34-map support. `wf`,
`inventory_input` and `input` establish resolved/defaulted syntax, scope,
typing and positive navigation support. `mcs_valid`, `gluing_compatible`,
`effective_defaults`, `formalcd_valid` and `exact_declarations` apply the existing
construction to this exact input. The structural MCS and the larger augmented
bank are distinct: the latter includes zero-arrow group/abstract declarations
and is not claimed to satisfy the former's positive-argument discipline.

## Concrete interpretation

[AppendixFConfiguration](../Clafer/Examples/AppendixFConfiguration.lean) uses
36 nonprimitive objects and all mathematical integers. ECU1 and ECU2 each own
two plaDisplay objects; ECU2.master targets ECU1. Every display's server targets
its owning ECU. Every options.size selects large; cache is absent. The telematics
selection is dual, extraDisplay and large. ECU versions are 2; display versions
are 3. Version and server field bounds remain mandatory 1..1.

The implicit integer head has explicit unrestricted 0..* bounds, and each
represented integer has the actual root as its unique parent. `integer_extent`
and `primitive_root_containment` expose this correction directly. Nonprimitive
extents and all expression count operands are finite; the integer extent and
the root's collection of children are infinite. Unrestricted structural bounds
use embeddings and do not assign zero cardinality to infinite collections.
The finite checker from #50 is not applied to this interpretation.

`structural_satisfaction` discharges typing, root, inheritance, parent,
reference, key, multiplicity, abstract-cover/disjoint and group obligations.
[AppendixFSatisfaction](../Clafer/Examples/AppendixFSatisfaction.lean) evaluates
all twelve bodies using navigation from these same objects and links.
`c02_defined` derives operand definedness from actual version/server head
multiplicities and dereference functionality; the inequality is proved separately.

[AppendixFCompiled](../Clafer/Examples/AppendixFCompiled.lean) compares every
arity vertex and map with the actual generated support reduct. `source_holds`
proves every attached body at every applicable context object.
`compiled_glued_model` applies `Compile.ConstraintMeaning.whole_model` to this
same configuration's canonical descent and the exact generated/glued bank.
Its selected-core, primitive-domain, typing/root and source-truth assumptions
are discharged; they are not premises of the final concrete theorem.

## Negative witnesses

[AppendixFRejections](../Clafer/Examples/AppendixFRejections.lean) ties count,
cache, server/parent and version failures to the exact full-input source symbols.
`generated_rejected` transports each symbol failure to the actual emitted formula
under equality of its complete arity reduct. These focused arity environments
are not asserted to satisfy the remaining structural bank. The channel xor
candidates are typed configurations for the full input: `xor_counts` accepts one
child, and `xor_generated_rejected`/`xor_glued_rejected` reject zero and two
in the actual declared channel predicate. Other obligations can fail as well.

The nonvacuous missing-fixed c01 candidate and mismatched c05/c08/c09 candidates
check operator sensitivity. The retained c07 vacuity theorem refers to the actual
attached c07 body; the one-display candidate also rejects it with ECU2 present.
These checks preserve the printed implication and equivalences even though
several branches are vacuous in the positive final selection.

## Boundaries

This is a concrete nonempty model-existence result for the manually elaborated
resolved input. It does not verify a parser or name resolver, infer coercions,
or establish correctness for all Clafer source texts. The source-to-core map,
accepted source corrections and selection of explicit binder domains remain
reviewed elaboration decisions. Closed c01–c12 use empty external binder lists.
The older structural projection and expression environments retain their own
narrower claims; neither is relabeled as this complete interpretation.
The external Haskell/Alloy comparison remains a separate workstream.
