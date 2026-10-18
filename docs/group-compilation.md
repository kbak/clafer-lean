# Group compilation: D6 proposal

This is the semantic proposal for [#65](https://github.com/kbak/clafer-lean/issues/65),
supporting #24 and #64. The choices below remain open; they are not delivered
interpretation theorems or changes to the [Compile contract](compile.md).
Preserving group metadata and deriving direct-child maps do not select them.

## Source and settled meaning

The [primary preprint](SOURCES.md#primary-source), SHA-256
`56b1c18e74807fb7646c0e89cb2fc306f4178affb41fee52fcebde09b031b2fb`, supplies:

| Locator | Evidence and limit |
| --- | --- |
| §4.2.1 p.7 | A group bounds instances of children; xor allows exactly one small/large child instance. |
| §4.2.2 p.8; D.4 p.32 | Constraints hold for each object of their context class. |
| §4.2.3 p.8; §5.5 pp.14,16 | Subtyping shares objects and inherited structure; map commutation is required. This does not specify group override interaction. |
| §5.3.4 p.14; Appendix F p.34 | Abstract containment propagates abstractness; the reusable options example contains xor size. Abstract bodies cannot simply be discarded. Retain the accepted head-class correction. |
| §6.2.2 p.20 | A group is a constraint whose context is the parent and whose scope contains the children. |
| Appendix C p.31 | xor = 1..1, or = 1..*, mux = 0..1, opt = 0..*; omitted groups inherit the super's group or default to 0..*. Keyword child defaults remain unchanged. |
| §6.2.3–5 pp.20–21; B.4 Defs.8–10 p.30 | Generated predicates have complete graph bindings and gluing transports declarations. Figure 23's total args remains a separate obligation. |

For a parent object `p`, count the ambient objects in the **set union** of
child-head fibers. Distinct reference heads pointing to the same target count
separately. One object reached through two inherited paths counts once. A
declaration count, a target count, or a sum of fiber cardinalities is unsuitable.
Use the existing `DPGraph.Predicates.InRange` on that subtype; for a finite
union, prove equivalence to the lower bound and finite/unbounded upper bound on
its cardinality. Do not interpret an infinite set as having cardinality zero.

Supplementary evidence is
[`genGroupConst`, lines 324–334](https://github.com/gsdlab/clafer/blob/15adb2216909421bcb5022174d2d84ef2b42307c/src/Language/Clafer/Generator/Alloy.hs#L324)
at compiler commit `15adb2216909421bcb5022174d2d84ef2b42307c`.
It unions child relations over the super hierarchy and skips abstract and empty
groups. These skips do not decide paper meaning. The MIT license/source policy
is recorded in [SOURCES](SOURCES.md#pinned-compiler-compatibility-audit); no
compiler source is incorporated. D1's default-policy differences remain separate.

## Decision A: abstract applicability and inherited inventory

**Recommendation:** treat a group as an invariant of its declaring context,
including abstract contexts. Its inventory is the direct children of that
declaration and its transitive supers. Evaluate inherited head maps at the same
ambient parent object through identity inclusion paths. No subtype-only child
is added to the super's inventory. Apply each context's effective bound; an
explicit subtype group does not erase the super's invariant.

This follows the context-constraint reading of §6.2.2 and D.4. Appendix C fixes
effective metadata but does not explicitly settle whether replacing that
metadata suppresses an inherited invariant. **Alternative:** abstract groups
are templates, realized only at concrete contexts using each concrete context's
effective bound and full inherited inventory. That resembles the compiler's
skip but requires a reviewed account of the paper's constraint reading.

Discriminating examples (explicit optional child multiplicities):

* Abstract xor A has children x and y; B : A adds z with effective xor. An object
  with only z fails the recommendation (A counts zero), but passes the template
  alternative (B counts one).
* With explicit opt on B, an object with x and y fails A's invariant under the
  recommendation; the template alternative permits it. Appendix C defaults are
  unchanged in both alternatives.
* Abstract xor A has no children; B : A adds x. A B-object with x fails the
  recommendation but passes the template alternative. An empty abstract head
  satisfies universal group constraints vacuously.

For overlapping inherited paths, both alternatives must use union by ambient
object identity. Realizing inherited fields, commuting maps, and nested child
specialization belongs to #66; #65 must not assume arbitrary maps have those
properties or silently strengthen `AST.WellFormed.inheritance_parent`.

## Decision B: empty groups and total args

**Recommended meaning:** an empty inventory has count zero at each parent
object. Bounds containing zero pass; a positive lower bound forces the context
head to be empty. An absent optional parent passes vacuously. Never omit a
nontrivial bound because its inventory is empty.

The natural group arity has a context vertex, a vertex for each selected child
head, all child head arrows, and every intermediate vertex/inclusion arrow
needed for inherited navigation. Empty own-child inventories can have just the
context vertex and no arrows. Such a formula is legal in DPGraph but cannot
inhabit a valid `MCS.Formulas` bank under `req~clafer-mcs-formulas~1`.
The existing `Formulas.no_zero_arrow` theorem in
[MCS/Laws.lean](../Clafer/MCS/Laws.lean) proves that boundary.

This is not solved by choosing nonminimal support: an accepted AST containing
only Sing and a parentless, childless abstract xor A has **no map roles at all**.
Both heads remain present under the accepted correction. Any arrow in a
predicate arity would have to map to a nonexistent role. Nor can a dummy
identity be bound: the role graph is a quiver without identity arrows. Requiring
positive child support would exclude previously accepted input and would miss
the requested empty cases.

**Recommended representation extension, requiring review:** retain the existing
MCS formula bank and its total-args/key disciplines, and add an explicit component
of generated vertex-only declarations to the Compile result. The complete source
diagram is their union with the existing bank; gluing takes the exact image of
that complete diagram. Every vertex-only declaration retains its owner, unique
generated symbol and full binding. This changes the generated-output interface;
it is not already allowed by the current MCS-only formula contract.
An alternative is a reviewed extension of the MCS role vocabulary with genuine
identity-support arrows and their semantics. Silently weakening total args,
adding unrelated arrows, or rejecting empty groups is not proposed.

## Proposed interface and proof obligations

#65 owns a Clafer-specific signature extension, distinct from authored constraint
occurrences and built-in predicates. A generated symbol identifies its owner
occurrence, effective range and resolved support inventory. Its binding includes
every support vertex/arrow; `owner = parent occurrence`. Unique occurrence
symbols establish the literal bag key without replacing bag equality by ordered
arguments. Built-in defaults remain in the source bank for FormalCD validity.

#50 owns structural candidates, counting and representation lemmas and its
checker; it must not depend on this extension. Reuse its actual API when supplied.
The present baseline has no #50 implementation. The integration seam is a finite
set of ambient child-head objects per parent, with explicit finite-count and
structural correspondence proofs. #65 interprets its generated formula using
that seam and proves the bound equivalence; it does not duplicate a checker.
Existing [predicate lemmas](../DPGraph/Predicates/Meaning.lean)
`distinctValuesEquiv`, `targetMultiplicity_distinct` and `inRange_iff` can relate
an individual set-valued head-map fiber to its distinct child objects. They do
not justify summing overlapping fibers or counting dereferenced targets.
#66 supplies the inherited inventory and realization laws (including shared
object identity and commuting parent maps). Direct-child selection is derivable
now from resolved parent equality; it is not a substitute for that inventory.

For each generated declaration, prove source-bank membership, exact glued-image
membership, and satisfaction after gluing iff the same bounds hold after
precomposition with labeling. Use B.5's formula translation law; do not infer
whole-model reflection from reduct alone. Prove default completeness separately.

Required interpreted compile/glue witnesses remain: xor with zero/one/two
children while each child is individually optional; numeric 2..3; or/mux/opt;
two bag heads sharing one target; overlapping inherited paths; abstract-context
applicability; and empty inventories with both zero and positive lower bounds.
One child declaration with two instances must count two. The choices above must
be resolved before the affected witnesses are implemented or #24 reports group
compilation complete. The affected existing requirement IDs listed in #65 retain
their promises; new semantic requirements need actual implementation/proof
coverage, not this proposal as a substitute.
