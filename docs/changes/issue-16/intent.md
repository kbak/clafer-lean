# Issue #16: reusable diagram-predicate interpretations

Canonical product overview: [docs/intent.md](https://github.com/kbak/clafer-lean/blob/030340d9d8700c1d6d722d4f0efc18dc0eb86647/docs/intent.md).
Tracker: [#16](https://github.com/kbak/clafer-lean/issues/16).

## Local outcome

Connect the delivered abstract interpretation interface and link-preserving span library to a reusable, source-grounded predicate vocabulary. This supplies the meanings required by the later FormalCD work without implementing FormalCD or Clafer here.

The user authorized proceeding with #16 after completing #4 and accepted the prepared plan. The remaining Q8 semantic choice is now explicitly resolved by the maintainer. Preserve the accepted Q1 correction and all existing mathematical and validation obligations. The audit uses current main `030340d9d8700c1d6d722d4f0efc18dc0eb86647`, containing both merged #32 and #31; the mounted catalog still points to `cabcf18abf231a4aac510d8f9996110ff2d8db09` and is not the implementation base.

## Accepted decisions

The accepted contracts distinguish link-preserving equations from predicates about endpoint membership. Link IDs may change under isomorphism; duplicate links remain observable. Multiplicities count fibers of links. Literal inclusion preserves the underlying object, which requires a shared ambient object type in the concrete semantic graph.

Q8 is resolved: the maintainer confirmed Table 3's disjointness shape is wrong. Use the common-target, disjoint-image predicate of §6.1.2 and Figure 21. For distinct family members, their target images must not overlap, including at the same underlying source object. Document the Table 3 error; do not introduce a separate common-source disjointness predicate. The earlier authorization to proceed and this explicit semantic answer authorize submission of the complete #16 package.

## Boundaries

Keep the generic signature, formula, DP-morphism and abstract reduct interfaces. The concrete vocabulary lives in dedicated DPGraph modules. A semantic graph over fixed universe bounds is sufficient; do not assert a graph containing all universes, add resizing axioms, generate instances, or implement later class-diagram syntax. #13's build-cost assessment and #26/#30's experiments remain separate tasks.
