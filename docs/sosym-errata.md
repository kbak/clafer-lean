# SoSyM paper corrections and clarifications

<!-- [impl->req~sosym-reader-companion~1] -->

A reading companion to *Clafer: unifying class and feature modeling*, using the
[published SoSyM article](sources.md#primary-source). PDF pages count from the
first cover sheet of the 37-page personal e-offprint; the article starts on PDF
page 3. The [edition crosswalk](sources.md#published-locators-and-legacy-aliases)
maps the preprint’s appendices and pages to the publication. All corrections below
remain necessary in the published text. They are adopted by Clafer Semantics, not
publisher-issued errata. Clarifications distinguish source explanations from
explicit choices made in the formalization.

## Corrections

### Disjointness uses a common target

**Table 3, PDF p.13; §6.1.2 and Figure 21, PDF pp.19–20.** Read disjointness for mappings
`fᵢ : Aᵢ ↛ B` into a common target: different family members must have disjoint
images in `B`. Table 3's common-source shape and source-inequality condition are
incorrect. Two inclusions containing the same ambient object overlap even when
their source values are equal; binding the same nonempty map twice also fails
disjointness. This agrees with the class partitions in Figure 21.
[Decision and meaning](sources.md#predicate-contracts-and-the-accepted-q8-correction);
[concrete predicate implementation PR](https://github.com/kbak/clafer-semantics/pull/34).

### Top-level abstracts retain their head class

**§5.3.4, PDF p.15; §6.2.3 and Figure 23, PDF p.22; Table 7, PDF p.23.**
Replace the exclusion of the head class in §5.3.4 with exclusion of the
**source** class and parent-dependent maps. The head always exists, as §6.2.3
and Figure 23 require. A top-level abstract reference retains its head, target
and dereference map; it has no source, head map, parent map or target map.
Table 7's source-present clause for basic clafers needs this parentless exception
and the separate synthetic-root exception.
[resolved syntax and Shapes issue](https://github.com/kbak/clafer-semantics/issues/3);
[resolved syntax and Shapes implementation PR](https://github.com/kbak/clafer-semantics/pull/47).

### The version constraint compares display to server

**Figure 21a, PDF p.19; §6.1 prose, PDF p.18; Figure 8 line 9 and §4.2.3, PDF p.10;
Appendix 6, PDF p.34.** The intended condition is
`display.version ≥ server.version`. In Figure 21a it is guarded by the
presence of a server: equality passes, and a display without a server satisfies
VC vacuously. Appendix 6 instead has a default 1..1 server and an unguarded
comparison; its [operand-definedness contract](integer-extraction.md#appendix-f)
derives existence from the selected structural semantics. The adjacent PDF p.18 prose
reverses the inequality; Figure 8, its explanation and Appendix 6 support the corrected direction. Preserve Figure
21a's nonempty-server guard rather than requiring every display to have a server.
[Decision and checked models](sources.md#figure-21b-and-the-accepted-q7-correction);
[self-description and telematics implementation PR](https://github.com/kbak/clafer-semantics/pull/38).

### Seven Figure 23 associations need optional source multiplicities

**Figure 23, PDF p.22; Table 8, PDF p.23.** Change source multiplicity `1`
to `0..1` on the four ordinary-map associations (`head_map`, `parent_map`,
`dref_map`, `target_map`) and three super-inclusion associations (`super_s`,
`super_h`, `super_t`). Each role then has at most one owner within each
association's image. The printed lower bounds
force every MapRole into both the parent-map and dereference-map images, requiring
its single label to be both `parent` and `dref`. Exact role-presence rules still
apply. Keep source `1` for head-class and formula ownership.
[Correction and proof map](mcs-invariants.md#figure-23-source-multiplicity-correction);
[MCS disciplines implementation PR](https://github.com/kbak/clafer-semantics/pull/56).

### Span composition agrees with relations after reduction

**Appendix 2, “(Sequential) Mapping composition”, PDF p.30.** Relational inputs do not make pullback span composition
isomorphic to relational composition. Two paths `a → b₁ → c` and `a → b₂ → c`
produce two composite links, while the relational composite contains one pair
`(a,c)`. The correct general law is
`red(q ⋆ r) = red(q) ; red(r)`, where `red` forgets link identity and `;` is
relational composition. Isomorphism holds exactly when each outer endpoint pair
has at most one composable **link pair**. For relational inputs, this reduces to
uniqueness of the intermediate object; parallel links make that condition
insufficient for arbitrary spans.
[Derivation and counterexamples](sources.md#span-composition-q1-research-for-4);
[span implementation and proofs PR](https://github.com/kbak/clafer-semantics/pull/32).

## Clarifications

### Incomparable Clafer declaration heads are disjoint

**§5.3–5.5, §6.1–6.2 and Appendices 5–6.** The adopted disjointness rule requires
super-edge comparability for two declaration heads to share an object. It covers
nested declarations and separate inheritance trees while preserving subtype
identity and inherited field views. Reference-target sharing remains permitted.
The paper supplies inclusion and explicit abstract-family partitions without
uniquely specifying this global rule. This is a maintainer-adopted clarification
consistent with the pinned static Alloy translation; generic subset/span models
remain unrestricted. [Source correspondence and limits](sources.md#declaration-disjointness-clarification).

### Links and bag keys retain multiplicity

**Appendix 2, mappings and operations, PDF pp.28–30; Table 3, PDF p.13.** A mapping retains individual
links. Set-valuedness forbids duplicate links with the same endpoints;
single-valuedness permits at most one outgoing link per source. Multiplicities
count links, including repeated targets. The formalization reads inverse and
triangle equality up to link-preserving span isomorphism, and keys compare
tuples of output **bags**. Replacing bags by their supports changes key meaning.
For a finite family of total, single-valued maps, this key is exactly injectivity
of the tuple of target values.
[Predicate contracts](sources.md#predicate-contracts-and-the-accepted-q8-correction);
[ordinary-key correspondence implementation PR](https://github.com/kbak/clafer-semantics/pull/53).

### A formula needs its complete graph binding

**Appendix 2 Definition 8, PDF p.31; Figure 21c and its explanation, PDF pp.19–21;
§6.2.2–3, PDF pp.21–23.** A formula consists of a predicate symbol and a graph morphism,
including all vertex and arrow images. The printed arrow-list shorthand assumes
finitely many arrows and no isolated vertices. An unordered argument bag can
lose occurrence assignments; it also cannot describe isolated vertex images.
Consequently, the literal key on `(args,pred)` is an additional instance condition,
not a characterization of equality of all full formulas. Repeated argument
values remain permitted. Total `args` separately excludes a realized formula
with zero arguments, although zero-arrow arities are valid under Definition 8.
[Checked projection and totality boundaries](sources.md#literal-key-total-args-and-the-19-obligation).

### Metamodel representation and semantic instantiation differ

**§6.1.3 and Figure 21c, PDF pp.19–21; §6.2.1, PDF p.21.** Expressing the metamodel as
a formal class diagram establishes syntactic self-description. Establishing that
a diagram is a semantic instance additionally requires an interpretation and
satisfaction of every effective declaration, including naming, arity, key and
totality conditions. Clafer Semantics proves bounded syntactic self-description and,
separately, a [semantic self-instance](metamodel-realization.md#assessment-for-the-particular-metamodel)
under a canonical bounded context after proving arrow support and bag separation.
This does not establish that every formal CD is an instance of Figure 21c or
supply a universe fixed point. The omitted dashed attachments for `nd` and `ad`
are supplied explicitly in the formalization.
[Bindings and scope](sources.md#figure-21c-metamodel).

<a id="appendix-e-equations-apply-to-roles-that-exist"></a>

### Appendix 5 equations apply to roles that exist

**§5.5 and Figure 18, PDF p.17; Tables 5–8 (see Appendix 5), PDF pp.22–23.** Read analogous
incidence and naming equations under the relevant role-presence guards. A parented
clafer has source/head-map/parent-map roles; a reference has target/dereference
roles; the target map exists exactly when both conditions hold. A selected super
requires a head inclusion, and source/target inclusions exactly when the
corresponding endpoints exist in both shapes. Guards do not permit required roles
to be omitted. Expand primitive
domain clauses over each supported domain, and canonical-name equivalences in
both directions.
[Complete clause inventory](mcs-invariants.md#appendix-e-inventory).

### Names do not determine gluing identity

**§6.1.1–3, PDF pp.18–21; §6.2.5, PDF p.23.** Distinguish role occurrences, the classes
or maps they denote, and displayed names. Repeated `parent`, `dref` or `isA`
strings do not identify maps. The adopted gluing rule identifies exactly equal
resolved referents, requiring matching endpoints and consistent names, predefined
annotations and map modes. This is an explicit interpretation of the paper's
labeling step. Transporting declarations proves a DP morphism; `FormalCD` validity
also needs complete effective defaults in the source bank. An exact image of
declarations does not silently add missing defaults. Ordinary non-bag maps require
set-valued defaults; bag maps have no such default.
[Adopted rule and proof boundaries](sources.md#mcs-gluing-and-the-approved-q4-rule);
[resolved-referent gluing implementation PR](https://github.com/kbak/clafer-semantics/pull/57).

<a id="appendix-d-intersection-is-not-difference"></a>

### Appendix 4 intersection is not difference

**Appendix 4, “Type rules” and “Semantics”, PDF pp.33–34.** The PDF prints `∩` in the intersection equation;
text extraction can misread the glyph. Ordinary common-element intersection
needs no correction. “Semantics of expressions” identifies `E` and `S` on set
expressions, explaining the mixed evaluator subscripts in “Semantics of set
expressions”. The arithmetic typing rule lists addition and subtraction
although its displayed arithmetic conclusion shows only addition. These typing
rules and notation do not by themselves supply constraint interpretation or
primitive-value conversion.
[Visual-source disposition and selected typing scope](sources.md#appendix-d-rule-dispositions-q3).

### Effective group inheritance and empty inventories

**§4.2.1–2, §6.2.2, Appendix 3 and Appendix 4 “Semantics”.** Groups on abstract declarations supply
inheritable bounds. Each concrete context enforces its effective bound over the
union of own and inherited child heads; no separate abstract original-child
invariant is added. This group-inheritance interpretation follows the pinned
compiler's inheritance regressions. Ordinary explicit abstract-context constraints remain
invariants. Empty inventories retain count zero, intentionally differing from
the compiler's unconditional skip. A positive lower bound forces an empty context
extent. [Source account, examples and representation boundary](group-compilation.md)
explain the complete arities and separate component needed for vertex-only formulas.

### Inherited ordinary fields and explicit abstract types

**§5.3.4–5, §5.5, Appendix 6.** The inherited-field clarification distinguishes
authored explicit abstract types from ordinary fields whose effective abstractness
comes from containment. Fields such as comp.version have the same occurrences
at the same realized parent across its super chain. Context views restrict the
existing containment/dereference links. They do not add declaration-level
unequal-parent inheritance. Explicit abstract coverage/disjointness remains a
separate obligation, including when a covering head is itself an inherited field.
See the [scoped inventory and combination policy](inherited-realization.md).
Realized `options.size` enforces its effective xor through the
[group-inheritance policy above](#effective-group-inheritance-and-empty-inventories).
This fills a specification gap; it is not attributed as a printed theorem.

## Formalization boundary

Structural compilation and gluing establish structural results under their
[explicit contracts](compile.md). The separate [constraint-preservation bridge](constraint-preservation.md)
connects resolved expression meanings to generated predicates under stated model
assumptions; the [complete Appendix 6 fixture](telematics.md) discharges those
assumptions for one concrete model. Neither establishes correctness for all
Clafer source texts. The compiler-comparison audit's
[decision table](resolved-ir-comparison.md#decisions-location-proposal-and-prerequisites)
also records compatibility limits and deferred extensions; these are not additional
accepted paper corrections. The [source map](sources.md) retains detailed citations
and the [product overview](intent.md) records the delivered scope.
