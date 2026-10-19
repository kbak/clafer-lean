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
| MCS and `FormalCD` validity; Figures 22–23, Appendix E | `Small.compilation_gluing_valid`, `exact_declarations`, `typed_attachments` | Instantiate Compile validity, effective-default completeness and exact translated union. Generic gluing's incidence/metadata hypotheses are derived by Compile's injective referents. |
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

| Fixture | Included declarations | Omissions |
| --- | --- | --- |
| Structural projection | All d01–d26, plus root and int; seven super edges, inherited fields and generated xor groups | No printed declarations omitted; optional cache is absent in the positive configuration |
| Separate c02 compilation fragment | d08 comp, d09 version, d10 ECU, d11 display, d12 server, mapped to fragment IDs 2,3,4,5,6 respectively; int=1, root=0 | d01–d07 and d13–d26 |

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

| Conjuncts | Representative fixture | Complete fixture |
| --- | --- | --- |
| c02 | Typed unguarded `not (displayVersion < serverVersion)` attached and glued; operand definedness derived from local formulas plus integer domain | `AppendixF.Meaning.c02_all` / `c02_defined`, full attachment and source truth |
| c01, c03–c12 | All omitted, including the final three selections | Every body attached and proved by `AppendixF.source_holds` |

The [complete fixture](appendix-f.md) owns the combined satisfaction account;
its [proof index](clafer-trace.md#complete-appendix-f-model-proofs) names
the individual conjunct proofs. Meanings and navigation paths are defined once
in the constraint inventory linked above.

The structural configuration has one plaDisplay per ECU. Its displayed choices
must not be read as satisfaction of c06/c07 or the printed final model. The [complete fixture](appendix-f.md) separately proves all twelve conjuncts
together on a configuration with two displays per ECU and all integers, then
applies the selected semantic bridge to its actual generated/glued diagram.

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
* #68 supplies general expression meaning; [#69’s selected bridge](constraint-preservation.md)
  connects body-derived predicates to exact Compile/gluing bindings and
  depends on this structural milestone. #64 owns full Appendix F satisfaction.
  The full-model result has its own [requirements and proof artifacts](appendix-f.md);
  the representative integration keeps its narrower contract. Neither result
  claims that all of Clafer or all paper figures are complete.
