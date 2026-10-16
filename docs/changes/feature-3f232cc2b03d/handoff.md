# First proven DP-graph slice

Proposed PR title: `feat(dpgraph): prove typed formulas and declaration-preserving morphisms`

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
proofs/examples, living documentation and Markdown trace artifacts. The scope
and Lean pin are unchanged. The accepted task intent/spec/accepted.json are
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
the repository with the original exact base. Command-level evidence does not
associate each theorem with an independently executed test artifact.

The retention repair changes evidence handling only: fresh invocation directories
contain the wrapper's receipt, log and portable evidence bundle. Supplemental
impact, verification and review reports stay outside those directories. The
recorded unexpected-artifact failure is checked by replaying retention into a
separate scratch destination. Current validation, source verification and an
independent review must accompany the handoff; prior summaries do not supply
those results. The approved requirements and Lean implementation are preserved.

Automation, including an IntentBond exit 4, is not semantic approval. Independent
review must assess Definitions 6–10, all positive/negative witness statements,
trace links and the complete change before a draft PR. Publication, acceptance
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
  opening the draft PR; include `Closes #14`, relate #2/#13, and leave broader
  research/design work open. Do not mark Done or close tickets during implementation.
