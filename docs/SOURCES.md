# Sources and open decisions

The [roadmap/source audit (#2)](https://github.com/kbak/clafer-lean/issues/2) and
[architecture design (#13)](https://github.com/kbak/clafer-lean/issues/13) remain
open. [Slice #14](https://github.com/kbak/clafer-lean/issues/14) selects the following
bounded source; this is not a complete audit of the literature.

## Primary source

*Clafer: unifying class and feature modeling*, 2014 SoSyM author preprint,
[PDF](https://gsd.uwaterloo.ca/sites/default/files/2014-Bak-Clafer-Unifying-Class-Feature-Modeling%28SOSYM%29.pdf),
[DOI](https://doi.org/10.1007/s10270-014-0441-1). The accepted source audit inspected
34 pages with SHA-256
`56b1c18e74807fb7646c0e89cb2fc306f4178affb41fee52fcebde09b031b2fb`.
Appendix B.4 Definitions 6–10 suffice for this slice:

| Source | Lean correspondence |
| --- | --- |
| Definition 6, graphs and graph morphisms | Mathlib `Quiver`, `Quiv`, `Prefunctor`; [representation](ARCHITECTURE.md) |
| Definition 7, signature | `DPGraph.Signature` |
| Definition 8, formula | `DPGraph.Formula` |
| Definition 9, DP-graph | `DPGraph` |
| Definition 10, DP morphism | `Formula.translate`, `Hom`, `Hom.id`, `Hom.comp` and their laws |

The finite arrow-list notation is shorthand, not a generic finiteness restriction.
Formula arguments are graph maps. Predicate names in examples denote syntax only.
Theorems here concern translation and declared-formula preservation, not predicate
interpretations, SetMap or Theorem 3. [Trace artifacts](dpgraph-trace.md) name the
actual declarations and proofs.

## Supporting sources and licenses

Mathlib is pinned to [56a005855ea17e0b0958f73ec801ae140b0a1679](https://github.com/leanprover-community/mathlib4/tree/56a005855ea17e0b0958f73ec801ae140b0a1679)
(v4.35.0), with the same Lean v4.35.0 pin. Inspected APIs:
[Quiver.Basic](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Basic.lean),
[Quiver.Prefunctor](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/Combinatorics/Quiver/Prefunctor.lean),
and [Category.Quiv](https://github.com/leanprover-community/mathlib4/blob/56a005855ea17e0b0958f73ec801ae140b0a1679/Mathlib/CategoryTheory/Category/Quiv.lean).
Mathlib's Apache-2.0 license was checked; it is consumed as a pinned dependency,
without vendoring its source. Paper definitions are independently formalized with
citations; publication text and figures are not reproduced.

The accepted audit also inspected author-uploaded Diskin & Wolter (2008),
[DOI 10.1016/j.entcs.2008.10.041](https://doi.org/10.1016/j.entcs.2008.10.041),
§4.1 Definitions 4.1–4.5. Its signatures add dependency arrows and closure.
Those additions are deliberately absent from this SoSyM slice. Full 2003/2000
secondary papers were not obtained. The maintained Haskell compiler is
supplementary context, not evidence used for this slice; later use must pin a
commit and check licensing.

## Open for later increments

Keep these questions open in #2/#13 before implementing the affected semantics:

- B.2.1 relation/span composition.
- Table 3 versus Figure 21 disjointness arity.
- Figure 21 VC inequality direction.
- Appendix D intersection typo and Appendix E analogous clauses.
- Label/identity choices for gluing.

None is resolved by the definitions or examples in this slice.
