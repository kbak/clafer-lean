# Approved follow-up: sibling public libraries in PR #25

This record captures the maintainer-approved structural follow-up to #14 in
[PR #25](https://github.com/kbak/clafer-lean/pull/25). It supersedes only the
original package's packaging, namespace and path choices. All mathematical
obligations remain in force. Canonical promises remain in [intent](../../intent.md)
and [requirements](../../spec.md); this addendum declares no duplicate OFT items.

## Authorization and source identities

- Original Canvas conversation: `8658ea18-41c1-4de6-ac73-3c6ed3d0f67a`.
- 2026-10-16 16:56:00 UTC, event `6046f2c3-f455-4ab7-bf02-adc58838bf53`:
  proceed with the refactor and update AGENTS.md and canonical intent for future
  FormalCD work.
- 2026-10-16 17:00:22 UTC, event `edc67ecb-9f7e-4ca1-9529-2aa0cdd4b7ef`:
  incorporate the work into existing PR #25. The coordinator's approved follow-up
  dispatch explicitly confirms the scope and externally supplied scope migration.
- Starting reviewed PR head: `23b1647af679a06130bfb83ca5fb613c81e5de12`;
  review base: `4c6d03c5022b5f5f762cae4a6459bbe73c76a477`;
  original retained base: `43d7f3fc326201c68a5da24bdd8aa613794d1d0d`.
- Maintenance run `afee5e0c-f1f0-4580-9bb2-21144b2aa7be` passed tests and
  independent review before dispatch. Its checkout-action update and retained
  validation history remain incorporated; those results do not validate this refactor.
- Original work-package SHA-256:
  `5fc8970485ffcc55f199eff743cafb2353d3b73362190d485e802780062e35d9`.
  Frozen [intent.md](intent.md), [spec.md](spec.md) and [accepted.json](accepted.json)
  remain byte-identical. Their SHA-256 identities are respectively
  `268dc70fdbdda842beeb691ae90f9a5da05361cca876d406e6597f168527707d`,
  `db5d21fc5dcb4c3f0b17ac28451b5975d4a5078a24b33c7a55c7bd9de7b2bdda`,
  `c94a2c34edd811d3f3d292a6484c583f4c8a837947ecb42fdfdb30a9adc006ca`.

## Bounded outcome

Keep repository `kbak/clafer-lean` and one Lake package; rename only the package
from `claferLean` to `clafer`. Preserve Lean v4.35.0 and Mathlib
`56a005855ea17e0b0958f73ec801ae140b0a1679`, with its transitive manifest pins.
Expose sibling `DPGraph`, `FormalCD` and `Clafer` public roots, removing the old
`ClaferLean` umbrella. Move the five mathematical modules to `DPGraph/` and
remove only the old namespace/import prefix. Preserve every delivered universe,
hypothesis, definition, theorem, proof and example. No new mathematical increment
or predicate semantics is authorized. FormalCD and Clafer receive entrypoint
scaffolding only; their future boundaries are in [architecture](../../ARCHITECTURE.md).

Enforce `Clafer -> FormalCD -> DPGraph -> Mathlib`. Build and kernel-check all
modules, including examples and future unimported helpers; audit all originating
declarations with complete import-all coverage. Preserve warnings-as-errors,
fail-closed checks, the nonempty DPGraph audit and standard axiom allowlist.
Exercise public DPGraph imports independently and test rejection paths.

## Explicit scope expansion

The pinned checker requires tracing inputs to exist in both snapshots. Replace
only `inputs` and `review_paths` with `["."]` so historical and moved code remain
captured and reviewed. No dummy old modules or candidate-as-baseline workaround
is permitted. Specification/test paths, coverage floors, revision/skipped-test
policy, command and timeout remain unchanged. The controller supplied the
approved expanded policy independently of the candidate.

| Identity | SHA-256 |
| --- | --- |
| Original scope bytes (870 bytes) | `4a706e10262528a94a097a84dd8813c0dd9265eaa1f87c55cb77d01ab928ce7f` |
| Approved expanded scope bytes (628 bytes) | `76540699cdf6a6a3e57f7077b82d445cad0d325890b5f99bfa54de7a300ad6f5` |
| Expanded canonical policy (sorted compact ASCII JSON, no newline) | `4547b647f0892bd3c354c0c55ab4bd65f0ce54827fe810534206dd8a49448895` |

[CI selection](../../../scripts/ci_scope.py) derives the transformation from the
recognized baseline and accepts only the approved resulting bytes.
[Regression tests](../../../tests/test_ci_scope.py) cover both layouts and
reject unrelated changes. CI retains original/selected identities for independent
review. Candidate policy changes cannot authorize themselves.

## Continuing promises and handoff gates

The continuing names/revisions are unchanged: formalization-foundation,
dpgraph-core, lean-validation and public-foundation clarify public packaging,
independence and complete coverage. Formula-translation, dpgraph-morphisms and
dpgraph-examples retain their mathematical promises. Traceable-contributions,
intentbond-workflow and github-tracking retain their obligations. The adopted
revision policy allows these continuing IDs; it does not waive review.

Compare the moved mathematics to the starting head after names-only normalization.
Run the configured captured check with the supplied scope and actual review base,
retain failures, and verify current/exported source against fresh evidence.
IntentBond exit 4 leaves semantic review pending. Independent code/security,
intent and traceability review must use the exact provisioned guidance at
`a430efa8d82e2a88ed2607bfe838066bb9d73f3c` and cover the full move and scope change.
The coordinator updates existing PR #25 through the publication workflow only
after checks/review pass. Link `Closes #14` for eventual merge; keep #2/#13 and
future work open. No second PR, force push, merge, ready-state change or deployment.
