# Issue #16 implementation plan

Status: accepted implementation handoff. The maintainer confirmed the Q8 correction, resolving the only outstanding semantic choice. Submit through the factory; retain this acceptance and the original package. Refer to `spec.md` for the precise contracts and to the canonical [product overview](https://github.com/kbak/clafer-lean/blob/030340d9d8700c1d6d722d4f0efc18dc0eb86647/docs/intent.md) for product direction.

## Base and ownership

Selected repository: `kbak/clafer-lean` only. Reviewed main is `030340d9d8700c1d6d722d4f0efc18dc0eb86647`. The older mounted catalog is read-only; current source references and the #31 validation delta were inspected on GitHub. The factory must start from the reviewed remote base, not from the catalog commit. Recheck issue text and main before submission; review any intervening change and prepare the package again.

Use the existing issue #16 and a factory task identity tied to it. Keep #16 In Progress and remove its blocked label now that Q8 is resolved. Do not resubmit an existing failed task as unrelated work. The controller retains accepted snapshots and controls validation, review and publication.

## Steps and files

1. Record the selected Q8 disposition on #16 and in `docs/SOURCES.md` before semantic implementation. Preserve the distinction between the source text, the selected correction and derived library statements. Q8 is accepted: common-target family maps have pairwise nonoverlapping images. Preserve the error disposition without introducing a second common-source meaning.
2. Add narrowly scoped reusable isomorphism/fiber transport lemmas in `DPGraph/Span/Basic.lean`, `IndexedFamily.lean` and `Composition.lean` as required. Preserve the accepted #4 API and laws. Avoid importing predicate vocabulary back into generic span or DPGraph core modules.
3. Add `DPGraph/Predicates/Signature.lean` for symbols and arities, `SemanticGraph.lean` for the bounded graph of subsets and spans, and `Meaning.lean` for span-level predicates. Names/file splits are routine implementation choices; keep syntax and interpretation separable.
4. Add `DPGraph/Predicates/Interpretation.lean` to build the existing Interpretation value and establish the specified laws. Add `DPGraph/Predicates/Examples.lean` for positive, negative, empty, repeated-link and universe witnesses. Add `DPGraph/Predicates.lean` and expose the library through `DPGraph.lean`; examples remain separately checked.
5. Maintain `docs/spec.md`, `docs/dpgraph-trace.md`, `docs/SOURCES.md`, `docs/ARCHITECTURE.md`, and the canonical `docs/intent.md`. Adjust README/AGENTS/CONTRIBUTING scope statements only where the delivered boundary changes. Use named Markdown proof artifacts, not unsupported inline Lean OFT tags.
6. Extend `tests/public_imports.lean` to exercise the exported vocabulary without importing FormalCD/Clafer or examples. Extend only the expected module inventory in `tests/test_project_modules.py`; preserve all discovery, layer, axiom and cache rejection assertions. Keep toolchain, dependency pins, trusted scope, and full test command unchanged.
7. Run the full IntentBond check at the original base, assess requirements against actual declarations and witnesses, and verify committed/exported source against retained evidence. The factory's independent review must assess Q8, bag equality, multiplicity, inclusion identity and universe bounds explicitly. Publish a draft only after all required gates pass.

## Risks and verification focus

- Link identity versus multiplicity: isomorphism must preserve duplicate-link counts; reduced-relation equality alone is insufficient for inverse/commutation/key.
- Key on bag-valued arguments: equality of fibers is target-preserving equivalence, not literal equality of source-indexed link IDs or merely equality of supports.
- Inclusion: an arbitrary injection or bijection is insufficient; underlying ambient objects must be unchanged. The shared ambient type is a parameter, not a global resizing principle.
- Infinite cardinalities: finite upper bounds must reject infinite fibers. The `*` branch must not silently impose finiteness. Embedding formulations can avoid unnecessary cardinal-arithmetic imports.
- Dependent arities: retain isolated vertices when n=0 and handle repeated bindings. Family indices are syntax parameters; semantic sets/links stay unrestricted.
- Universe growth and import cost: account for the universe of the link type field; do not narrow the generic API. Keep added imports focused. #13's comparative build-cost study is separate.
- Catalog drift: current source has the #4 API and #31 cache guard absent from the mounted snapshot; the frozen remote base is authoritative.

## Handoff status

Source inspection and the accepted contracts are complete. The maintainer’s Q8 answer selects the recommended common-target meaning. No further approval is required for the specified implementation or its routine choices. Tests and proof validation remain worker/controller work; successful review gates permit a draft PR, while acceptance and merge remain separate.
