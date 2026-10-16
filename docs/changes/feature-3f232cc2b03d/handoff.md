# Proven DP-graphs and sibling public libraries

Proposed PR #25 title: `feat(foundation): prove DP-graphs in sibling public libraries`

This change introduces the first reusable mathematical layer: SoSyM Appendix B.4
Definitions 6–10 over Mathlib quivers. Formulas bind a whole arity graph, preserving
parallel arrows, repeated arguments and isolated vertices. DP morphisms carry a
proof of declaration preservation. Translation and morphism laws hold with fixed
signature and independent universes. Finite witnesses include a nonidentity arrow
collapse between nonempty declaration sets, explicit composition, and the
impossibility of equipping a graph map with preservation when its declaration is
absent. Predicate semantics, SetMap and Theorem 3 remain future work.

The change includes the accepted task package retained since the review base,
the pinned Mathlib dependency and resolved manifest, the independent entrypoint,
proofs/examples, living documentation and Markdown trace artifacts. The Lean pin is unchanged. The approved scope expansion and public-root refactor
are recorded below. The accepted task intent/spec/accepted.json are
unchanged; plan.md explains the smaller file grouping and parent review/PR work.

Closes #14 (on eventual merge). Related: [roadmap #2](https://github.com/kbak/clafer-lean/issues/2)
and [design #13](https://github.com/kbak/clafer-lean/issues/13); their broader work
remains open.

## Requirement changes

Under the existing policy (`require_revision_increase: false`), continuing names
and revisions are retained:

| Requirement/intent | Change and acceptance impact |
| --- | --- |
| formalization-foundation | Infrastructure-first intent expands to the approved three-layer scope: reusable DPGraph, reusable FormalCD, structural 2014 Clafer. Explicit exclusions and future abstract semantics are retained. |
| lean-validation | Scaffold status now includes mathematical modules. Build-all-modules, warnings-as-errors, leanchecker and failure propagation remain. A declaration/axiom audit strengthens validation. |
| public-foundation | Status distinguishes delivered DPGraph from future FormalCD/Clafer. License, concise README, contribution/security guidance, source links and private-data exclusion remain. |
| dpgraph-core | New delivered representation and dependency requirement; named implementation artifacts. |
| formula-translation | New postcomposition requirement with implementation and identity/composition proof artifacts. |
| dpgraph-morphisms | New preservation, identity/composition, extensionality and law requirement with implementation and proof artifacts. |
| dpgraph-examples | New finite positive/negative witnesses with implementation and proof artifacts. |

The existing intentbond-workflow, github-tracking and contribution/scope policies
continue unchanged. No requirement or artifact claims implementation/proof of a
future phase. Task-package references are context, not duplicate canonical OFT
declarations. [dpgraph-trace.md](../../dpgraph-trace.md) follows the real Lean
symbols; review must assess their semantic correspondence, not just coverage.

## Validation and review contract

The retained implementation record reports successful local compilation,
leanchecker and declaration audit: 161 project declarations use only `propext`,
`Classical.choice` and `Quot.sound`, with no new assumptions. Fresh captured
validation and source verification are required for the completed candidate;
their authoritative results are the externally retained invocation bundles.
The shared command provisions targeted Mathlib caches (with source-build fallback)
and runs Lake, Lean's kernel checker, the declaration/axiom audit,
and existing Python tests. The audit permits only `propext`, `Classical.choice`
and `Quot.sound`, printing actual dependencies and rejecting new assumptions and
unsafe/partial project declarations. These standard axioms are not new domain
assumptions. Full feedback bundles and source verification are retained outside
the repository with the exact base selected for each handoff. The current repair
uses `4c6d03c5022b5f5f762cae4a6459bbe73c76a477`; the original planning base remains
in the accepted package. The current base's checkout-action update is incorporated
without conflicts. Command-level evidence does not
associate each theorem with an independently executed test artifact.

The retention repair changes evidence handling only: fresh invocation directories
contain the wrapper's receipt, log and portable evidence bundle. Supplemental
impact, verification and review reports stay outside those directories. The
recorded unexpected-artifact failure is checked by replaying retention into a
separate scratch destination. Current validation, source verification and an
independent review must accompany the handoff; prior summaries do not supply
those results. The approved requirements and Lean implementation are preserved.

The offline review prerequisite is now available in the test profile: the exact
pinned development skill, its reference source and upstream license. The 168
retained files match their supplied provenance's byte counts, SHA-256 digests and
Git blob identities. The fresh reviewer must read that copy, with its location
provided in the external review context. This resolves the missing-guidance
prerequisite without changing the implementation or substituting the installed
checker's guidance. Fresh validation and review results remain separate evidence.

Automation, including an IntentBond exit 4, is not semantic approval. Independent
review must assess Definitions 6–10, all positive/negative witness statements,
trace links and the complete change before updating PR #25. Publication, acceptance
and merge remain separate gates; no merge, ready status or deployment is requested.

## Coordinator ticket update

Issue listing through the repository helper returned HTTP 401; live issue
comments and Project status could not be inspected or updated in the worker.
The supplied accepted #14 package authorizes this bounded slice. Preserve the
following update for the credential-bearing coordinator instead of creating a
duplicate issue:

- Track #14 as In Progress; keep #14, #2 and #13 open until acceptance and merge.
- Scope/acceptance: the four new requirements in [the living spec](../../spec.md),
  SoSyM B.4 Definitions 6–10, pinned Mathlib/Lean, independent imports, positive
  noninjective and negative preservation proofs, full kernel/axiom/trace checks.
- Dependencies: source audit #2 and design #13. No additional semantic decisions
  were needed for this slice. Later ambiguities remain open in
  [SOURCES.md](../../SOURCES.md), including the unavailable full secondary papers.
- Attach the retained feedback/verification result and independent review before
  updating existing PR #25; include `Closes #14`, relate #2/#13, and leave broader
  research/design work open. Do not mark Done or close tickets during implementation.

## Approved public-root follow-up

The [addendum](approved-follow-up.md) records maintainer authorization and exact
source/package/scope identities. Starting head:
`23b1647af679a06130bfb83ca5fb613c81e5de12`; review base:
`4c6d03c5022b5f5f762cae4a6459bbe73c76a477`; original retained base:
`43d7f3fc326201c68a5da24bdd8aa613794d1d0d`. The candidate is the uncommitted
worktree; the parent supplies the exported commit and verifies it before publication.
The accepted intent/spec/accepted.json remain byte-identical, retaining original
package `5fc8970485ffcc55f199eff743cafb2353d3b73362190d485e802780062e35d9`.

| Historical module/path | Current module/path |
| --- | --- |
| `ClaferLean/DPGraph/{Signature,Formula,Basic,Morphism,Examples}.lean` | `DPGraph/{Signature,Formula,Basic,Morphism,Examples}.lean` |
| `ClaferLean/DPGraph.lean` | `DPGraph.lean` |
| `ClaferLean.lean`, empty `ClaferLean/Basic.lean` | Removed umbrella/scaffold; sibling roots `DPGraph.lean`, `FormalCD.lean`, `Clafer.lean` |
| Namespace prefix `ClaferLean.DPGraph` | `DPGraph` (including the carrier/declaration structure itself) |
| Lake package `claferLean` | `clafer`; repository remains `kbak/clafer-lean` |

All five mathematical files match the starting PR source byte-for-byte after
removing only the `ClaferLean.` prefix and the enclosing namespace in Basic.
Manifest dependencies and Lean toolchain bytes are unchanged. FormalCD/Clafer
are empty public entrypoint scaffolds importing their lower layer. Tracked
directory markers allow Lake's recursive globs before future modules are added. The
layout-independent scope covers moved and historical sources; the exact
transformation and unchanged obligations are detailed in the addendum.

Continuing OFT IDs and revisions are retained. Compared with the starting PR,
formalization-foundation/public-foundation clarify package/repository names,
sibling reuse and future boundaries; dpgraph-core changes its independent import
to DPGraph; lean-validation adds explicit layer checks and complete discovery for
build/kernel/audit coverage. Formula-translation, dpgraph-morphisms and
dpgraph-examples retain all mathematics. Contribution/tracking obligations remain.

Validation implementation: one discovered inventory covers all eight current
modules, including examples, in explicit builds, leanchecker and import-all
axiom inspection. The audit selects module origins and retains private/generated
coverage and the nonempty guard. Regression cases exercise allowed and forbidden
layer/helper/root imports, future unimported modules, uncovered sources, the
actual audit on private/generated and invalid fixtures, independent public names,
and exact scope migration/rejection. All 27 Python tests pass locally, including actual Lean audit rejection
cases; fresh complete captured validation and independent review remain separate
required evidence, with actual results retained outside the source tree.

The parent must review the full intended diff, including all new/moved files,
scope transformation and tests, using the retained pinned IntentBond guidance.
Exit 4 leaves semantic review pending. Source verification must match the fresh
evidence before updating existing PR #25. Keep #14 In Progress and all affected
tickets open pending acceptance/merge; relate #2/#13 and future #17–#19 without
closing them. The worker leaves source uncommitted and returns updates to the
coordinator. No direct publication, merge, ready-state change or deployment.
