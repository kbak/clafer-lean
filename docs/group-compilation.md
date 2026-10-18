# Compiling effective group cardinalities

[#65](https://github.com/kbak/clafer-lean/issues/65) extends the
[structural Compile contract](compile.md) with interpreted group declarations.
`Compile.compileAugmented` retains the original well-formed MCS, adds generated
group declarations and exposes their complete union. `Compile.gluedGroups`
preserves that exact union and derives FormalCD naming/default validity.

## Source and selected meaning

The [primary preprint](SOURCES.md#primary-source), SHA-256
`56b1c18e74807fb7646c0e89cb2fc306f4178affb41fee52fcebde09b031b2fb`, supplies:

| Locator | Meaning and boundary |
| --- | --- |
| §4.2.1 p.7; §6.2.2 p.20 | Group bounds constrain child instances per parent object. |
| §4.2.2 p.8; Appendix D.4 p.32 | Explicit constraints hold for every object of their context, including subtype objects. |
| §4.2.3 p.8; §5.5 pp.14–16; Appendix F p.34 | Inheritance shares objects and structure; map commutation/realization requires separate obligations. |
| Appendix C p.31 | xor = 1..1, or = 1..*, mux = 0..1, opt = 0..*. Effective bounds/defaults are supplied by resolved input. |
| B.4 Definitions 8–10 p.30; §6.2.3–5 pp.20–21 | Formulas retain full graph bindings; gluing translates declarations. Figure 23 total args is a separate MCS restriction. |

The selected group-inheritance behavior follows compiler commit
`15adb2216909421bcb5022174d2d84ef2b42307c`:

* [Generator/Alloy.hs, genGroupConst](https://github.com/gsdlab/clafer/blob/15adb2216909421bcb5022174d2d84ef2b42307c/src/Language/Clafer/Generator/Alloy.hs#L324)
  unions own and super-hierarchy child relations and skips abstract contexts.
* [Intermediate/ResolverInheritance.hs, analyzeGCard](https://github.com/gsdlab/clafer/blob/15adb2216909421bcb5022174d2d84ef2b42307c/src/Language/Clafer/Intermediate/ResolverInheritance.hs#L213)
  resolves the nearest authored group along the hierarchy.
* [Common.hs, findHierarchy](https://github.com/gsdlab/clafer/blob/15adb2216909421bcb5022174d2d84ef2b42307c/src/Language/Clafer/Common.hs#L171)
  includes self and successive supers.
* [groupCardInheritance.cfr](https://github.com/gsdlab/clafer/blob/15adb2216909421bcb5022174d2d84ef2b42307c/test/positive/groupCardInheritance.cfr),
  its [Alloy regression](https://github.com/gsdlab/clafer/blob/15adb2216909421bcb5022174d2d84ef2b42307c/test/regression/groupCardInheritance.als.reg),
  and [groupCardInheritance2.cfr](https://github.com/gsdlab/clafer/blob/15adb2216909421bcb5022174d2d84ef2b42307c/test/positive/groupCardInheritance2.cfr)
  distinguish inherited alternatives, newly added children and local overrides.

An abstract group supplies an inheritable bound. It does not additionally impose
an invariant over only the abstract declaration's original inventory. Every
concrete context enforces its resolved effective bound over the union of its own
children and children of every super. If abstract xor A has x/y and B : A adds z,
a B object with only z passes. An effective opt override on B can admit two
children. This special treatment of groups refines the paper's context-constraint
account; ordinary explicit constraints on abstracts retain that account unchanged.
Appendix C authored/effective provenance, override rules and child defaults are
preserved. D1 compiler/default discrepancies remain separate from D6.

An empty inventory counts zero. Bounds containing zero hold; a positive lower
bound forces the context extent empty. An empty context satisfies the universal
predicate vacuously. This deliberately differs from `genGroupConst`'s unconditional
empty-inventory skip. The [compiler license/source policy](SOURCES.md#pinned-compiler-compatibility-audit)
applies; no compiler source is incorporated.

## Representation and interpretation

`Groups.Ancestor` selects the reflexive transitive super hierarchy by resolved
identity. `Groups.Child` pairs an ancestor with each declaration whose resolved
parent is that ancestor. Finite ASTs therefore have finite inventories.
The arity has one vertex for each selected ancestor and child, a distinguished
context vertex, each selected child-head arrow, and the inclusion arrows between
selected ancestor heads. `Groups.binding` maps all vertices and arrows into the
canonical role graph, preserving incidence and ownership. A generated predicate
symbol identifies one concrete owner; its effective bound and inventory are fixed
by the compiled family. Reference children bind their heads, never their targets.

For each context object, `Groups.Objects` takes the **set union of ambient child
objects** reached by those head maps from that same parent identity. Distinct bag
heads with one reference target count separately. Multiple links or inherited
paths witnessing the same object count once. No sum of declaration cardinalities
or target deduplication is used. `InRange` gives the embedding-based meaning even
for infinite sets; finite specialization reuses #50's `inRange_card`, with explicit
finiteness of the counted subtype.

The extra component can contain vertex-only formulas. A childless context with
no super has its context vertex and no arrows. These are legal under B.4
Definition 8, but cannot satisfy Figure 23 total args. The original MCS bank, its
literal bag key, nonempty argument proof and the positive-support contract for
user constraints remain intact. No synthetic identity role is added. The complete
raw bank is not claimed to satisfy the old MCS total-args discipline.
`forget_augmented` recovers the existing structural result exactly.

## Gluing and semantic boundary

The complete source bank contains the union of original and generated
declarations, including ordinary/inclusion effective defaults. `glued_declarations`
proves exact image equality for both components, retaining full bindings under
labeling. Compile's referents are injective, so incidence, metadata compatibility
and a graph inverse to labeling are derived. `descendGroups` therefore constructs
an actual glued interpretation from a configuration and proves its reduct equality.
Generic noninjective MCS gluing still requires its existing consistency conditions.

`objects_interpret` proves that a typed #50 relational configuration realizes each
selected head fiber as containment at the same parent identity. `generated_group_iff`
and `descended_group_iff` identify source/glued formula satisfaction with the
selected bounds. `descended_model_iff` accounts for both declaration components;
satisfying a group alone does not establish the remaining structural obligations.
No user-expression interpreter is inferred from fresh predicate symbols.

#50's checker and guarded comparison fragment remain unchanged. `direct_child_iff`
relates inventories when strict ancestors have no children; effective-bound
agreement is also necessary when comparing to its `Configuration.Groups` (and
holds for `EffectiveCore.erase`). #50 does not depend on this extension.
[#66](https://github.com/kbak/clafer-lean/issues/66) owns realization of inherited
fields, nested child specialization and commuting map restrictions. Selecting an
inherited head map does not prove those obligations or copy any object. Tests of
an inherited abstract-child fiber are explicitly group-predicate tests under typed
relations, not proofs of complete inherited-family realizability. The zero-arrow example
uses only Sing; its empty-context case tests the group predicate vacuously and
does not assert the separate root singleton obligation.

Named implementation/proof and acceptance artifacts are in
[the Clafer trace](clafer-trace.md). #24's integration and #64's full Telematics
model retain their separate acceptance criteria.
