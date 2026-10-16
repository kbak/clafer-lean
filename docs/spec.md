# Foundation requirements

These requirements describe the initial repository infrastructure. They do not
claim that any Clafer semantics have already been formalized. Future definitions
and theorems need their own requirements and paper references.

## Reproducible Lean validation
`req~lean-validation~1`

The project pins Lean 4, builds the `ClaferLean` library including all modules
under its namespace, treats warnings as errors, and rechecks the compiled library
with Lean's bundled `leanchecker`. The shared check command must fail if any
validation stage fails. The initial library contains no semantic declarations.

Covers:
- `intent~formalization-foundation~1`

Needs: impl, itest

## IntentBond on every contribution
`req~intentbond-workflow~1`

Agent instructions require the pinned IntentBond development skill. The repository
maintains intent and requirements with OFT links and a nonempty scope. CI checks
pull requests using the base branch's scope and retains evidence; first adoption
explicitly checks the candidate baseline and requires review. Exit 4 retains
semantic review as pending. Failed checks block the CI job.

Covers:
- `intent~traceable-contributions~1`

Needs: impl

## GitHub planning and tracking
`req~github-tracking~1`

Agents plan work as GitHub issues in the configured Project. The ticket helper
creates issues from body files, adds them to the Project, sets their status, and
supports later edits, comments, and closure. GitHub operation failures must be
reported as failures; if issue creation succeeds before Project tracking fails,
the helper reports the created URL so tracking can be retried without recreation.
Planning tickets do not authorize starting semantic implementation.

Covers:
- `intent~traceable-contributions~1`

Needs: impl, utest

## Focused public project documentation
`req~public-foundation~1`

The repository keeps its MIT license and provides contribution and
private security-reporting guidance, issue/PR templates, a brief README, and links
to the SoSyM publication, free preprint, and maintained Haskell implementation.
It identifies the formalization as future work and keeps private deployment
configuration and credentials outside the source repository.

Covers:
- `intent~formalization-foundation~1`

Needs: impl
