# SoSyM paper corrections and clarifications

<!-- [impl->req~sosym-reader-companion~1] -->

A reading companion to *Clafer: unifying class and feature modeling*, using the
[34-page 2014 author preprint](SOURCES.md#primary-source). Page numbers refer to
that preprint. The corrections below are adopted by Clafer Lean; they are not
publisher-issued errata. Clarifications distinguish source explanations from
explicit choices made in the formalization.

## Corrections

### Disjointness uses a common target

**Table 3, p.12; §6.1.2 and Figure 21, pp.17–18.** Read disjointness for mappings
`fᵢ : Aᵢ ↛ B` into a common target: different family members must have disjoint
images in `B`. Table 3's common-source shape and source-inequality condition are
incorrect. Two inclusions containing the same ambient object overlap even when
their source values are equal; binding the same nonempty map twice also fails
disjointness. This agrees with the class partitions in Figure 21.
[Decision and meaning](SOURCES.md#predicate-contracts-and-the-accepted-q8-correction);
[implemented in #34](https://github.com/kbak/clafer-lean/pull/34).

### Top-level abstracts retain their head class

**§5.3.4, p.14; §6.2.3 and Figure 23, pp.20–21; Appendix E Table 7, p.33.**
Replace the exclusion of the head class in §5.3.4 with exclusion of the
**source** class and parent-dependent maps. The head always exists, as §6.2.3
and Figure 23 require. A top-level abstract reference retains its head, target
and dereference map; it has no source, head map, parent map or target map.
Table 7's source-present clause for basic clafers needs this parentless exception
and the separate synthetic-root exception.
[Accepted decision #3](https://github.com/kbak/clafer-lean/issues/3);
[implemented in #47](https://github.com/kbak/clafer-lean/pull/47).

### The version constraint compares display to server

**Figure 21a and adjacent prose, p.17; Figure 8 line 9 and §4.2.3, p.8;
Appendix F, p.34.** The intended condition is
`display.version ≥ server.version`. In Figure 21a it is guarded by the
presence of a server: equality passes, and a display without a server satisfies
VC vacuously. Appendix F instead has a default 1..1 server and an unguarded
comparison; its [operand-definedness contract](integer-extraction.md#appendix-f)
derives existence from the selected structural semantics. The adjacent p.17 prose
reverses the inequality; Figure 8, its explanation and Appendix F support the corrected direction. Preserve Figure
21a's nonempty-server guard rather than requiring every display to have a server.
[Decision and checked models](SOURCES.md#figure-21b-and-the-accepted-q7-correction);
[implemented in #38](https://github.com/kbak/clafer-lean/pull/38).

### Seven Figure 23 associations need optional source multiplicities

**Figure 23, p.21; Appendix E Table 8, p.33.** Change source multiplicity `1`
to `0..1` on the four ordinary-map associations (`head_map`, `parent_map`,
`dref_map`, `target_map`) and three super-inclusion associations (`super_s`,
`super_h`, `super_t`). Each role then has at most one owner within each
association's image. The printed lower bounds
force every MapRole into both the parent-map and dereference-map images, requiring
its single label to be both `parent` and `dref`. Exact role-presence rules still
apply. Keep source `1` for head-class and formula ownership.
[Correction and proof map](mcs-invariants.md#figure-23-source-multiplicity-correction);
[implemented in #56](https://github.com/kbak/clafer-lean/pull/56).

### Span composition agrees with relations after reduction

**Appendix B.2.1, p.29.** Relational inputs do not make pullback span composition
isomorphic to relational composition. Two paths `a → b₁ → c` and `a → b₂ → c`
produce two composite links, while the relational composite contains one pair
`(a,c)`. The correct general law is
`red(q ⋆ r) = red(q) ; red(r)`, where `red` forgets link identity and `;` is
relational composition. Isomorphism holds exactly when each outer endpoint pair
has at most one composable **link pair**. For relational inputs, this reduces to
uniqueness of the intermediate object; parallel links make that condition
insufficient for arbitrary spans.
[Derivation and counterexamples](SOURCES.md#span-composition-q1-research-for-4);
[implemented in #32](https://github.com/kbak/clafer-lean/pull/32).

## Clarifications

### Links and bag keys retain multiplicity

**Appendix B.1–B.3, pp.28–30; Table 3, p.12.** A mapping retains individual
links. Set-valuedness forbids duplicate links with the same endpoints;
single-valuedness permits at most one outgoing link per source. Multiplicities
count links, including repeated targets. The formalization reads inverse and
triangle equality up to link-preserving span isomorphism, and keys compare
tuples of output **bags**. Replacing bags by their supports changes key meaning.
For a finite family of total, single-valued maps, this key is exactly injectivity
of the tuple of target values.
[Predicate contracts](SOURCES.md#predicate-contracts-and-the-accepted-q8-correction);
[ordinary-key correspondence, #53](https://github.com/kbak/clafer-lean/pull/53).

### A formula needs its complete graph binding

**Appendix B.4 Definition 8, p.30; Figure 21c and its explanation, pp.17,19;
§6.2.2–3, p.20.** A formula consists of a predicate symbol and a graph morphism,
including all vertex and arrow images. The printed arrow-list shorthand assumes
finitely many arrows and no isolated vertices. An unordered argument bag can
lose occurrence assignments; it also cannot describe isolated vertex images.
Consequently, the literal key on `(args,pred)` is an additional instance condition,
not a characterization of equality of all full formulas. Repeated argument
values remain permitted. Total `args` separately excludes a realized formula
with zero arguments, although zero-arrow arities are valid under Definition 8.
[Checked projection and totality boundaries](SOURCES.md#literal-key-total-args-and-the-19-obligation).

### Metamodel representation and semantic instantiation differ

**§6.1.3 and Figure 21c, pp.17,19; §6.2.1, p.20.** Expressing the metamodel as
a formal class diagram establishes syntactic self-description. Establishing that
a diagram is a semantic instance additionally requires an interpretation and
satisfaction of every effective declaration, including naming, arity, key and
totality conditions. Clafer Lean proves bounded syntactic self-description and
selected instance fragments; these do not establish semantic self-instantiation
or that every formal CD is an instance of Figure 21c. The omitted dashed
attachments for `nd` and `ad` are supplied explicitly in the formalization.
[Bindings and scope](SOURCES.md#figure-21c-metamodel).

### Appendix E equations apply to roles that exist

**§5.5 and Figure 18, pp.14–16; Appendix E Tables 5–8, p.33.** Read analogous
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

**§6.1.1–3, pp.17–19; §6.2.5, p.21.** Distinguish role occurrences, the classes
or maps they denote, and displayed names. Repeated `parent`, `dref` or `isA`
strings do not identify maps. The adopted gluing rule identifies exactly equal
resolved referents, requiring matching endpoints and consistent names, predefined
annotations and map modes. This is an explicit interpretation of the paper's
labeling step. Transporting declarations proves a DP morphism; FormalCD validity
also needs complete effective defaults in the source bank. An exact image of
declarations does not silently add missing defaults. Ordinary non-bag maps require
set-valued defaults; bag maps have no such default.
[Adopted rule and proof boundaries](SOURCES.md#mcs-gluing-and-the-approved-q4-rule);
[implemented in #57](https://github.com/kbak/clafer-lean/pull/57).

### Appendix D intersection is not difference

**Appendix D.3–D.4, p.32.** The PDF prints `∩` in the intersection equation;
text extraction can misread the glyph. Ordinary common-element intersection
needs no correction. D.4.1 identifies `E` and `S` on set expressions, explaining
the mixed evaluator subscripts in D.4.2. D.3.1 lists addition and subtraction
although its displayed arithmetic conclusion shows only addition. These typing
rules and notation do not by themselves supply constraint interpretation or
primitive-value conversion.
[Visual-source disposition and selected typing scope](SOURCES.md#appendix-d-rule-dispositions-q3).

## Formalization boundary

Structural compilation and gluing establish structural results under their
[explicit contracts](compile.md), rather than full semantic preservation of
Clafer expressions. The compiler-comparison audit's remaining
[decision items](resolved-ir-comparison.md#decisions-location-proposal-and-prerequisites)
are proposals or compatibility limits, not additional accepted paper corrections.
The [source map](SOURCES.md) retains detailed citations and the
[product overview](intent.md) records the delivered scope.
