# Pinned compiler import fixtures

`set_and_bag_references.cfr` is copied unchanged from
[gsdlab/clafer@15adb2216909421bcb5022174d2d84ef2b42307c](https://github.com/gsdlab/clafer/blob/15adb2216909421bcb5022174d2d84ef2b42307c/test/positive/set_and_bag_references.cfr).
Its MIT attribution is retained in `LICENSE-upstream`. Other source fixtures are
original examples for this repository. Tests execute the pinned exporter; saved
JSON files are schema/mutation examples, not substitutes for those executions.

`identities` combines duplicate display names, nesting, inheritance, an unused
abstract and a bag reference. `groups` counts child occurrences under effective
numeric bounds. `cycles` keeps reference cycles; `empty` imports only the root.
`spellings` retains Latin-1 letters and apostrophes admitted by the pinned lexer.
See [the import protocol](../../../docs/resolved-import.md) for replay and trust
boundaries. Malformed/unsupported cases are deterministic mutations in
`tests/test_resolved_import.py`, including every rejected tag/modifier family.
