# Implement #17: formal class diagrams and name-preserving morphisms

Implement the approved first FormalCD increment for
https://github.com/kbak/clafer-lean/issues/17 in repository kbak/clafer-lean.
The PR must reference Closes #17. This is the initial manual task issue-17,
not a retry of another issue or a new unrelated feature.

## Authority and baseline

The user approved the immediately preceding scope and recommendation of
name-preserving morphisms: “sounds great, let's do it”.
Use the accepted intent.md and plan.md in this package. Canonical product intent:
[docs/intent.md](../../intent.md). Canonical requirements:
[docs/spec.md](../../spec.md). Follow AGENTS.md, CLAUDE.md, CONTRIBUTING.md,
docs/traceability.md and pinned IntentBond instructions at the approved base.

Reviewed main: dccdc5d1c2d698d34a06bf279290cb8ebfe0d94f, containing merged #34.
Dependencies #15/#27, #4/#32 and #16/#34 are delivered.
Do not derive the implementation from the stale coordinator catalog.

Primary semantic sources: SoSyM §6.1.1–3, Figure 21b–c, B.4 Definitions 6–10.
The inspected author PDF has SHA-256
56b1c18e74807fb7646c0e89cb2fc306f4178affb41fee52fcebde09b031b2fb.
Consult docs/SOURCES.md. Preserve accepted Q1 and Q8 meanings.
The name-preserving specialization below is an adopted library contract;
do not present its extra conditions as a verbatim theorem from the paper.

## Representation

1. Implement reusable FormalCD modules and expose the core through import FormalCD.
   Depend on DPGraph, never Clafer. Preserve independent import DPGraph.
2. Use the existing Quiv/Prefunctor carrier, DPGraph.Formula and declaration Set.
   The initial supported predicate vocabulary is DPGraph.Predicates.signature.
   Do not introduce a second graph API, untyped argument lists, formula identity
   tokens, predicate-dependency closure, or global finite/decidable assumptions.
   User-defined predicate syntax/VC and metamodel-specific nd/ad predicates can
   be added by their later increments; do not pretend they are supported here.
3. Add metadata on existing vertices and arrows: class and map names,
   optional predefined-class identifiers, and map modes distinguishing ordinary
   set-valued maps, explicitly bag-valued maps and inclusion maps.
   Keep data independently inspectable from a WellFormed proposition; a bundled
   valid CD carries a proof of that proposition. Equivalent minimal organization
   is acceptable if raw invalid data and the failed obligations can be expressed.
4. Use a shared predefined vocabulary/registry parameter with stable identifiers
   and canonical names, allowing singleton and primitive-domain entries to be
   distinguished. Entries are optional in a diagram. Each selected predefined
   identifier has at most one class realization; preserve its identifier through
   morphisms. A class's graph identity remains its carrier vertex. Do not equate
   arbitrary user classes or maps because their strings agree.

## Naming and declaration invariants

5. A predefined class has its registered canonical name; user-defined class
   names lie outside the registry's reserved names. Inclusion maps use isA.
   Different inclusion arrows may share that name. Do not impose global
   injectivity of classifier names, acyclic inheritance, compulsory presence of
   every primitive domain or singleton, or map identity based solely on names.
6. The existing typed formula binding enforces arity/incidence. Repeated
   arguments and isolated arity vertices remain valid. Declare no second,
   weaker arity predicate to replace it.
7. Every inclusion-marked arrow has the corresponding built-in inclusion
   formula in the underlying declaration set. Every ordinary set-valued arrow
   has its corresponding setValued formula. Explicit bag mode adds no implicit
   setValued requirement; an author can still explicitly declare it.
   Inclusion's semantic consequences come from the delivered inclusion meaning.
   Inclusions are a separate mode from bag maps.
8. These defaults are FormalCD obligations, visible in the effective declaration
   set used by its underlying DPGraph; they do not change generic DPGraph.
   It is sufficient to require membership as part of WellFormed; if a convenience
   constructor inserts defaults, prove its resulting membership obligations.
   Preserve all user declarations and use one authoritative effective set.

## Morphisms and proofs

9. At a shared predefined registry and supported predicate signature, a
   FormalCD morphism consists of an existing declaration-preserving DPGraph.Hom
   plus preservation of vertex names, arrow names, predefined-class annotations
   and map modes. Annotation/mode preservation is equality at mapped vertices
   and arrows (including user vs predefined and set/bag/inclusion modes).
   Source and target are independently well-formed CDs. Require no global
   injectivity of the carrier map and no reflection of extra target declarations.
10. Provide identity, composition, extensionality from the underlying DP map,
    associativity, and both unit laws. Prove every metadata-preservation
    obligation is closed under identity and composition; reuse the existing
    graph/DP morphism laws. Expose a forgetful projection to DPGraph.Hom and
    prove it respects identity/composition.
11. Demonstrate interoperability with existing satisfaction/model reduct by
    forgetting a FormalCD morphism. Retain the existing contravariant direction
    and explicit interpretation parameter. Do not re-prove the general reduct
    theorem or claim arbitrary DP morphisms preserve the added metadata.

## Semantic boundary and acceptance witnesses

12. WellFormed is syntactic/structural validity, not a proof of a model's
    existence or satisfaction. The registry records primitive identity/naming,
    not an implementation of the concrete Int/String/Bool/singleton domains.
    Generic models and the reduct concern declared predicates under a supplied
    interpretation. Document this boundary instead of silently claiming complete
    primitive-class or object-diagram semantics.
13. Provide kernel-checked witnesses for:
    - a finite valid CD with two distinct inclusion arrows both named isA,
      exercising their endpoints and required inclusion declarations;
    - an ordinary map's required set-valued declaration, and an explicit bag map
      without an automatically added set-valued declaration;
    - invalid reserved user-class naming, incorrect predefined naming and
      duplicate realization of a predefined identifier;
    - missing required inclusion/default declarations and an invalid inclusion name;
    - a nonidentity FormalCD morphism, explicit composable maps and the laws;
    - a declaration-preserving DP map between well-formed CDs that cannot lift
      to the chosen FormalCD morphism because it changes a name or mode;
    - one actual concrete interpretation/model and its restriction, plus a
      failing satisfaction example illustrating the separate semantic condition.
    Keep examples separate from the public entrypoint. No full Figure 21 or
    VC interpretation is required. Names of the witnesses are implementation choices.
14. Preserve all existing build, module-discovery, import-layer, kernel,
    warning, axiom and trace checks. No sorry/admit, unchecked escape axioms,
    unsafe/partial mathematical declarations, disabled warnings, skipped tests
    or weakened coverage/scope.

## Living requirements and documents

Add the new independently meaningful promises to docs/spec.md, with fresh IDs
after checking for collisions. Suggested stable names:
formalcd-structure, formalcd-naming, formalcd-declarations,
formalcd-morphisms, formalcd-examples. Use revision 1 for new items; link to
the existing intent~formalization-foundation~1, with impl and proof obligations
as appropriate. These names here are a work list, not duplicate declarations.
Use named Markdown artifacts in docs/formalcd-trace.md linking actual Lean
declarations, per docs/traceability.md.

Preserve continuing IDs/revisions, especially req~dpgraph-core~1,
req~dpgraph-morphisms~1, req~predicate-arities~1,
req~predicate-unary-maps~1, req~predicate-interpretation~1,
req~lean-validation~1, req~intentbond-workflow~1 and req~github-tracking~1.
Update the delivered-slice wording of req~public-foundation~1 and the maintained
overview/architecture/source map where affected, without duplicating the overview
or turning later phases into delivered promises. Generic predicate meanings,
scope.json, pin versions and accepted Q1/Q8 rules remain the baseline contracts.

Record source correspondence, selected specialization, semantic boundaries and
the accepted default/identity rules in current docs. Update scaffold status in
AGENTS.md/README.md as applicable. Frozen intent/spec/accepted.json remain
unchanged; keep the package's plan.md concise and current.

## Verification and completion

Run the approved check with pinned tooling and the captured base:
ib check --repo WORKTREE --base dccdc5d1c2d698d34a06bf279290cb8ebfe0d94f
--candidate worktree --out NEW_EXTERNAL_EVIDENCE_DIRECTORY
using the controller-supplied trusted scope when provided. Its test command is
bash scripts/check.sh. Retain complete evidence and verify the exported candidate
against the same baseline. Exit 4 requires the independent semantic review;
it does not constitute approval. Factory tests and independent review gate the
draft PR. Address in-scope findings through the normal bounded repair process.

The coordinator handles GitHub ticket/Project updates; workers return needed
updates without receiving GitHub credentials. Keep #17 open until acceptance and
merge. Return a draft PR with Closes #17 and concrete proof/validation evidence.
No merge, ready-for-review transition or deployment is authorized.
