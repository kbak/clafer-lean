# MCS structural inventory

The source is SoSyM §6.2.3/Figure 23 (pp.20–21) and Appendix E Tables 5–8
(p.33), in the [pinned preprint](SOURCES.md#primary-source). The inventory below
records the accepted Q2 expansion and Q4 representation boundary for
[#20](https://github.com/kbak/clafer-lean/issues/20). The
[existing Shape contract](spec.md#individual-clafer-shapes) controls exact presence.
These equations are a specification inventory; MCS definitions and proofs remain
pending the independent Figure 23 multiplicity decision below. No compiler,
gluing congruence or semantic model-existence result is claimed.

## Appendix E inventory

Write `H`, `S`, `T` for head/source/target class roles and `h`, `p`, `d`, `t`
for head/parent/dereference/target map roles. `P` means the clafer has a parent;
`R` means its kind is reference set or reference bag. A subscript `super`
denotes the selected super's corresponding role. A guard does not allow required
roles to be omitted: `H` always exists; `S` exists exactly when `P`; `T` exactly
when `R`; `h,p` exactly when `P`; `d` exactly when `R`; and `t` exactly when
`P ∧ R`. These are the existing `Roles.classPresent` and `Roles.mapPresent`
rules in [Shape.lean](../Clafer/Shape.lean).

| Source clause | Guard | Equation or obligation |
| --- | --- | --- |
| Table 5: head endpoints | `P` | `so(h) = S`, `ta(h) = H` |
| Table 5: analogous parent endpoints | `P` | `so(p) = H`, `ta(p) = S` |
| Table 5: analogous dereference endpoints | `R` | `so(d) = H`, `ta(d) = T` |
| Table 5: analogous target endpoints | `P ∧ R` | `so(t) = S`, `ta(t) = T` |
| Table 6: parent cojoining | `P` | `S = parent.H` |
| Table 6: target cojoining | `R` | `T = target.H` |
| Table 6: head inclusion | super exists | `so(super_h) = H`, `ta(super_h) = H_super` |
| Table 6: analogous source inclusion | super exists and both source roles exist | `so(super_s) = S`, `ta(super_s) = S_super` |
| Table 6: analogous target inclusion | super exists and both target roles exist | `so(super_t) = T`, `ta(super_t) = T_super` |
| Table 7: Sing/root | synthetic root | Basic, no parent, no source/target class, no ordinary maps and no super; the head remains |
| Table 7: Dom | any supported primitive domain | Basic, parent is root, source cojoins root's head, no target and no super |
| Table 7: basic | basic kind | No target/dereference/target-map; source/head-map/parent-map exist exactly when parented |
| Table 7: analogous reference set | reference-set kind | Target/dereference required; source/head-map/parent-map/target-map exist exactly when parented; ordinary target-map mode |
| Table 7: analogous reference bag | reference-bag kind | Same role presence as reference set; bag target-map mode |
| Table 7: parentless non-root | no parent and not root | Abstract; retains head; a reference also retains target/dereference |
| Table 8: head naming | `P` | `label(h) = label(H)` |
| Table 8: parent naming | `P` | `label(p) = "parent"` |
| Table 8: analogous dereference naming | `R` | `label(d) = "dref"` |
| Table 8: target naming | `P ∧ R` | `label(t) = label(h) ++ "*"`; equivalently `label(H) ++ "*"`, derived using the head equation |
| Table 8: Sing equivalence | every clafer | synthetic root iff head label is `"Sing"` |
| Table 8: int equivalence | every clafer | primitive int iff head label is `"int"` |
| Table 8: string equivalence | every clafer | primitive string iff head label is `"string"` |
| Table 8: bool equivalence | every clafer | primitive bool iff head label is `"bool"` |

No super means no inclusion slots; a selected super requires the head inclusion
and every shared-endpoint inclusion. Missing one of two source/target endpoints
forbids that inclusion slot rather than generating an equation with an undefined
side. `Shape.SharedClass` already describes this boundary. The root and
parentless basic exceptions use the [accepted #3 correction](SOURCES.md#resolved-2014-clafer-and-individual-shapes).
The supported primitive-domain vocabulary is `int`, `string`, `bool`, as in
`PrimitiveDomain`; the analogous expansion quantifies over all three. Both
implications of each canonical naming equivalence are required, including the
exclusion of reserved head names from ordinary user clafers.

Inclusion names are `"isA"` under the inherited §6.1.1/§6.1.3 naming discipline.
That obligation comes from the class-diagram foundation, not an additional
printed Table 8 row. Local inverse, triangle, multiplicity and reference-key
formulas remain those of [Shape/Diagram.lean](../Clafer/Shape/Diagram.lean).

## Identity and formula boundaries

Keep local role slots, graph role identities, resolved class/map referents, and
displayed strings distinguishable. Cojoining equalities must explicitly state
which identity level they compare. Equality of displayed `parent`, `dref` or
`isA` strings must not by itself identify arrows. Preserve endpoints and the
information needed for later intended identifications; #23 owns the gluing
congruence and its graph/DP-morphism proof. The accepted #20 representation
choice does not complete that policy.

Figure 23 also includes Role, ClassRole, MapRole, InclRole, String, PredefStr,
Formula and Signature, with the ClassRole/MapRole cover/disjoint partition,
inclusion roles, total labels/endpoints, formula ownership and diagram predicates.
Formula data must retain the symbol and complete graph binding, including
isolated vertices and repeated argument occurrences. The literal bag key on
`(args,pred)` and total `args` are separate conditions; neither follows just
from well-typed full bindings. Reuse the
[existing distinction and counterexamples](SOURCES.md#literal-key-total-args-and-the-19-obligation).
Do not weaken that key to indexed equality or suppress total args for zero-arrow
arities.

## Figure 23 source-multiplicity conflict

**Unresolved Q9, owned by #20.** Figure 23 prints `1` at the source of each
ordinary-map slot (head, parent, dref, target), as well as the three super slots,
head-class slot and formulas association. Table 3's `mult-src` semantics
counts the inverse fiber at a target. Consequently, a literal source `1` on
`parent_map : Clafer → MapRole` requires every map-role object to occur as a
parent map of exactly one clafer. The corresponding `1` on `dref_map` requires
every map-role object to occur as a dereference map of exactly one clafer.

For any map role `m`, choose those two clafers. Table 8's guarded equations apply
because the chosen roles exist. They give `label(m) = "parent"` and
`label(m) = "dref"`. Figure 23's label is single-valued, so the two distinct
strings would be equal. Thus the literal conjunction permits no map-role
objects. Any parented shape requires a map role under the accepted Shape rules,
so it cannot satisfy that conjunction. Only inverse **existence** was needed
for this contradiction; weakening uniqueness alone does not remove it.

Q2's optional-role guards do not resolve this conflict: they guard the naming
and incidence equations at a clafer, while source multiplicity constrains every
object in the common target MapRole set. Q4's separation of referents from role
identities does not resolve it either: the conflict already occurs at a single
role's displayed label, before gluing.

Two possible source treatments require explicit selection:

- Retain each printed source `1` literally over its common target and state the
  resulting lack of any MCS with map roles. This cannot meet #20's requested
  nonempty parented/reference witnesses.
- Correct the affected ownership annotation to uniqueness on the image of that
  particular slot (equivalently source upper bound `0..1` over the common target),
  leaving exact required/forbidden role presence to Shape. This removes the
  conflicting lower bounds but is a semantic departure from the printed `1`.

The decision must also specify its application to the three super-role slots.
The head-class and formulas annotations need their own literal/ownership
accounting; they are not automatically changed by a correction to map slots.
No multiplicity correction is adopted here. The publication, existing Shape
requirements and frozen task snapshots remain unchanged.
