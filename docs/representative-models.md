# Representative models through compilation and gluing

The [product intent](intent.md) and [Compile contract](compile.md) bound this
integration of `Clafer`, `FormalCD` and `DPGraph`. The requirements are
[representative integration](spec.md#representative-compilation-and-gluing) and
[coverage accounting](spec.md#representative-paper-coverage-accounting).
The [named trace artifacts](clafer-trace.md#representative-model-integration)
link each claim below to Lean declarations.

Primary source: the [SoSyM author preprint](SOURCES.md#primary-source), SHA-256
`56b1c18e74807fb7646c0e89cb2fc306f4178affb41fee52fcebde09b031b2fb`:
§6.2.4–5, Appendix F p.34, Figures 16, 18, 21–23. Preserve the accepted
Q1/Q7/Q8 corrections and top-level abstract/ownership corrections in the
[source map](SOURCES.md). These examples reuse those decisions; they add no
new source interpretation. Figures 15, 17 and 19 have no new standalone fixture
here; their general representation context does not count as a checked copy of
those printed models.

## Feature and theorem coverage

| Feature/source | Concrete checked connection | Claim and limit |
| --- | --- | --- |
| Nesting and repeated names; Figure 16, §6.2.3–5 | `Integration.Small.nested_names_and_identity`, `nesting_incidence` | Equal names remain distinct glued classes; the nested head retains its parent/child endpoints. |
| Inheritance and references; Figure 18, §5.3–5.5 | `Small.inheritance_declared`, `shared_target_distinct_maps`; `Inherited.inherited_version`, `inherited_options_and_displays` | Inclusion is actually declared; two reference maps sharing a target remain distinct. Appendix F fields reuse ambient objects in inherited views. |
| MCS and FormalCD validity; Figures 22–23, Appendix E | `Small.compilation_gluing_valid`, `exact_declarations`, `typed_attachments` | Instantiate Compile validity, effective-default completeness and exact translated union. Generic gluing's incidence/metadata hypotheses are derived by Compile's injective referents. |
| Individual multiplicities and xor; Appendix C, §4.2.1 | `Integration.Xor.optional_declarations`, `boundaries` | The actual compiled and glued optional-head formulas pass for zero/one/two selected objects. The generated xor passes for one and fails separately on both sides for zero/two. |
| Typed constraint attachments; Appendix D, §6.2.2–5 | `Small.typed_attachments`, `repeated_binding_after_gluing`; `VersionCompilation.attachment`, `full_binding` | Positive support, context/owner, repeated occurrences and complete bindings survive. Fresh predicate symbols do not establish expression denotation. |
| Integer navigation; Appendix F c02 | `VersionCompilation.versionModel`, `operands_defined`, `comparison_defined` | The emitted local inclusion/multiplicity formulas, interpreted after gluing, supply the delivered navigation theorem's structural hypotheses. Integer realization/domain equality is explicit. Definedness does not assert comparison truth. |
| Concrete version values; Appendix F c02 | `IntegerExamples.comparison_value`, `greater`, `equal`, `lower`, `empty_server`, `multiple_server`, `wrong_domain_server` | Actual navigation and partial integer comparison have checked results. These are support-model witnesses, separate from whole-model satisfaction. |
| Appendix F inherited structural projection | `Integration.AppendixF.source_ids`, `exact_declarations`, `structural_model`, `version_and_server`; `Inherited.compiled_glued_model`, `realized_xor_glued` | All printed declarations compile/glue, with a nonempty model of the generated structural bank. The finite primitive token is not the full mathematical integer domain. |
| Figure 21b/c | `FormalCD.Telematics.Examples.model_iff`; `FormalCD.bounded_self_description` | Existing complete Figure 21b and bounded syntactic self-description remain separate. Guarded VC is never substituted for Appendix F c02. |
| Public layer boundary | `tests/public_imports.lean and tests/formalcd_imports.lean`, module discovery in `scripts/check.sh` | The pinned validation builds each public entrypoint and rejects imports from higher layers, including helpers/examples. |

The small integration fixture reuses `Compile.Examples.input`: its childless xor
makes it useful for structural validity and attachment checks, not a positive
whole-model witness. The xor boundary fixture reuses `Compile.GroupExamples`;
its typed configurations test generated predicates, not complete inherited
realizability. The Appendix F structural fixture supplies that separate positive
realization witness.

## Appendix F declaration accounting

Use the authoritative [d01–d26 inventory](inherited-realization.md#scoped-source-to-core-inventory)
for names, parent/super/target edges, abstractness and bounds. `Inherited.ast`
contains **every d01–d26 declaration**, plus synthetic root and implicit int;
no printed declaration is omitted from its structural projection. The source IDs
1–26 are retained exactly, although preorder occurrence indices differ.

| Declarations | Structural projection | Separate c02 compilation fragment |
| --- | --- | --- |
| d01 options, d02 size, d03 small, d04 large | Included, with inherited field realization and generated xor | Omitted |
| d05 cache, d06 cache.size, d07 fixed | Included; optional cache absent in the positive configuration | Omitted |
| d08 comp, d09 version, d10 ECU, d11 display, d12 server | Included, with mandatory version/server fields | Included; fragment IDs 2,3,4,5,6 respectively, int=1, root=0 |
| d13 display.options | Included with super d01 | Omitted |
| d14 plaECU, d15 plaDisplay | Included with seven-edge hierarchy and 1..2 display bound | Omitted |
| d16 ECU1, d17 ECU2, d18 master | Included with mandatory/optional instances and shared reference target | Omitted |
| d19 telematics, d20 channel, d21 single, d22 dual | Included with generated channel xor | Omitted |
| d23 extraDisplay, d24 size, d25 small, d26 large | Included with generated size xor | Omitted |

The two fixtures have explicit, different identity assignments. They are not
silently merged into one whole-model certificate. The c02 fragment changes the
delivered navigation fixture's synthetic root spelling to canonical `Sing` and
attaches the existing typed comparison at display; it preserves all resolved
support IDs and mandatory bounds.

## Appendix F constraint accounting

The [c01–c12 inventory](inherited-realization.md#constraint-scope-handoff) fixes
all twelve printed conjuncts and their exact navigation. The structural fixture
has **no authored expression bodies**. Only c02 has a separate compiled typed
attachment here; the following omissions remain visible.

| ID | Selected status | Remaining obligation |
| --- | --- | --- |
| c01 | Omitted: small size/cache implies fixed | Typed attachment, denotation and satisfaction in #68/#69/#64 |
| c02 | Typed unguarded `not (displayVersion < serverVersion)` attached and glued; operand definedness derived from local formulas plus integer domain | General expression-denotation connection and satisfaction in the complete fixture (#68/#69/#64) |
| c03 | Omitted: no inherited cache | Typed attachment, denotation and satisfaction |
| c04 | Omitted: server = parent at ECU | Typed attachment, denotation and satisfaction; current server navigation is not this equality proof |
| c05 | Omitted: dual iff ECU2 | Typed attachment, denotation and satisfaction |
| c06 | Omitted: extraDisplay iff two ECU1 displays | Typed attachment, denotation and satisfaction |
| c07 | Omitted: extraDisplay iff (ECU2 implies two ECU2 displays) | Preserve implication and absent-ECU2 vacuity in later interpretation |
| c08 | Omitted: large iff no small options on all plaECU displays | Typed attachment, denotation and satisfaction |
| c09 | Omitted: small iff no large options on all plaECU displays | Typed attachment, denotation and satisfaction |
| c10 | Omitted: final dual selection | Full-model selection and satisfaction (#64) |
| c11 | Omitted: final extraDisplay selection | Full-model selection and satisfaction (#64) |
| c12 | Omitted: final large selection | Full-model selection and satisfaction (#64) |

The structural configuration has one plaDisplay per ECU. Its displayed choices
must not be read as satisfaction of c06/c07 or the printed final model. Full
Appendix F completion requires all twelve conjuncts together and a nonempty
satisfying interpretation under #64.

## Assumptions and completion boundary

* Structural proofs consume the explicit resolved/defaulted `Compile.Input`;
  input validity, typed boundary support and positive user-constraint map support
  are proved for the concrete fixtures. No name resolver or parser is supplied.
* Generated groups use the existing same-parent union of own/inherited child
  objects. The zero/one/two witnesses prove actual predicate behavior; group
  metadata or individual optional bounds alone cannot provide that guarantee.
* `VersionCompilation.LocalHolds` requires satisfaction only of emitted built-in
  local formulas. `versionModel` derives inclusion and the four 1..1 hypotheses;
  the full integer-domain interpretation is an explicit additional assumption.
  The theorem assumes neither singleton operands nor the desired inequality.
  The separate concrete integer support examples demonstrate defined true and
  false results and rejection of missing/multiple/noninteger operands.
* The mathematical results are kernel-checked declarations linked in the trace.
  Command-level build/IntentBond evidence records the configured validation;
  trace coverage does not certify the source correspondence. Independent semantic
  review and acceptance remain separate gates.
* #68 owns general expression meaning; #69 owns the combined semantic bridge and
  depends on this structural milestone. #64 owns full Appendix F satisfaction.
  This integration does not close those obligations or claim that all of Clafer
  or all paper figures are complete. #24 remains open until acceptance and merge.
