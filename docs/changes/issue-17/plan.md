# Implementation plan — #17

Approved scope: this package's frozen [specification](spec.md); current product
contracts: [intent](../../intent.md), [requirements](../../spec.md).
PR linkage: Closes #17. Keep #17 open until acceptance and merge.

Reviewed base: `dccdc5d1c2d698d34a06bf279290cb8ebfe0d94f` (#34).
Captured starting HEAD: `d9db1b318d37a812271fb5fa211e514ef6bbec9c`, which adds
this accepted package. Retain the supplied task branch and frozen snapshots.

1. Inspect DPGraph's typed signature, formulas, Hom and reduct, the pinned
   IntentBond guidance and trace conventions; check new requirement IDs for collisions.
2. Implement `FormalCD/Basic.lean`: shared registry/kinds, modes, raw data,
   explicit naming/default obligations and bundled valid CDs. Defaults are
   required membership in the authoritative set, with no insertion constructor.
3. Implement `FormalCD/Morphism.lean`: metadata-preserving DP maps, identity,
   composition, extensionality, laws and forgetful equations. Put the explicit
   interpretation/reduct adapter and inherited laws in `FormalCD/Semantics.lean`.
4. Implement structural positive/negative cases in `FormalCD/Examples.lean`
   and actual interpreted models/failures in `FormalCD/SemanticsExamples.lean`.
   This split keeps structural witnesses readable and the examples out of the
   public API. Add `tests/formalcd_imports.lean`; preserve the existing independent
   DPGraph import test instead of importing an upper layer into it. Extend the
   exact module-inventory regression to require all five new modules and the new
   import test, retaining its equality assertion and all rejection cases.
5. Maintain five new revision-1 requirements (`formalcd-structure`,
   `formalcd-naming`, `formalcd-declarations`, `formalcd-morphisms`,
   `formalcd-examples`) and named artifacts in `docs/formalcd-trace.md`.
   Update the delivered-slice overview, architecture, source map and scaffold
   guidance; preserve existing IDs, generic predicate meanings, scope and pins.
6. Compile the new modules and inspect the complete change against the reviewed
   base. Apply the authorized whitespace-only reflow of the frozen specification's
   continuing-ID paragraph so references are not parsed as declarations; preserve
   every word, ID, revision and the original acceptance hashes.
   Run the controller-provided feedback wrapper for IntentBond, including
   `bash scripts/check.sh`, with trusted scope and that same base. Retain external
   evidence and verify the exported candidate. Resolve in-scope failures before
   handoff; exit 4 leaves independent semantic review pending.
7. Return implementation/validation and ticket updates for coordinator review and
   draft publication. Leave changes uncommitted; do not publish, merge, mark ready,
   close the issue or mark Done in the worker.

Implementation organization follows steps 1–5; compilation, source review and
validation complete step 6. The only organization changes are separating semantic
examples and the reduct adapter, and adding a dedicated FormalCD import test.
The inventory assertion must grow with the delivered module set. No behavior
change from the approved specification is intended. Figure 21c
encoding/self-description, VC, nd/ad predicates, primitive-domain implementation,
renaming, MCS and Clafer compilation/gluing remain outside scope.
