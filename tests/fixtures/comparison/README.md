# Bounded comparison fixtures

These small structural sources are original MIT-licensed repository fixtures.
They isolate the [comparison contract](../../../docs/resolved-ir-comparison.md)
E1–E14 obligations. Existing imported upstream examples retain their separate
[MIT notice](../importer/LICENSE-upstream). Compiler release notes motivate tests;
injected mutations are not allegations of compiler defects.

`bag.cfr` and `set.cfr` differ only in reference mode. Distinct reference heads
pointing at one target test occurrence identity. `overlap.cfr` permits the same
object in both Lean extents, exposing Alloy's intrinsic top-level-signature
disjointness in the reverse direction. No candidate admission rule removes it.
Runtime captures, hashes, seeds, witnesses and minimized replays are retained
outside the repository by the executable tests.
`predicate_name.cfr` checks that a supported name containing `ib_candidate`
compares and replays without being mistaken for the added predicate itself.

The JSON candidates are stable, original MIT-licensed regression inputs:
`unrelated-overlap.json` exposes the intrinsic representation restriction;
`omit_set_uniqueness.json`, `collapse_bag_heads.json` and `drop_cardinality.json`
are the deterministic deletion-minimal sensitivity cases paired respectively
with `set.cfr`, `bag.cfr` and `optional.cfr`. The live tests apply only the named
injected mutation, compare the original checker candidate, shrink, check equality
with these fixtures and replay the external result bundle. These fixtures contain
no execution logs or private paths.
