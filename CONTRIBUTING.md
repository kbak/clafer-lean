# Contributing

<!-- [impl->req~public-foundation~1] -->

Start with an [existing issue](https://github.com/kbak/clafer-lean/issues) or
propose a small, scoped one. Maintainers also track issues in a
[private GitHub Project](https://github.com/users/kbak/projects/2); contributors
can use the public issues and pull requests without Project access. Semantic work should
identify the paper sections, intended definitions/theorems, ambiguities, and
acceptance criteria before implementation. See [AGENTS.md](AGENTS.md).

## Setup and checks

<!-- [impl->req~intentbond-workflow~1] -->

Repository `kbak/clafer-lean` contains the single Lake package `clafer`.
Place modules beneath their owning public root and preserve
`Clafer -> FormalCD -> DPGraph -> Mathlib`; `import DPGraph` remains independent.
The [product overview and documentation map](docs/intent.md) identify delivered
scope and authoritative documents; [architecture](docs/ARCHITECTURE.md) explains
module boundaries. Use those references when updating summaries, retaining
artifact IDs, trace links, source citations and existing link destinations.

Install Python 3.11+, Git, Java 17+, and the [GitHub CLI](https://cli.github.com/).
For full validation, also install Lean with [elan](https://lean-lang.org/install/)
and prepare the [pinned importer prerequisites](#pinned-import-validation-prerequisites).
Documentation-only checks do not need Lean, the Haskell compiler or Alloy. Then:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements/intentbond.txt -r requirements/documentation.txt
ib install-oft
```

For quick feedback while editing, run `bash scripts/check.sh --preflight`.
This checks module discovery and its Python regressions without requiring Lean;
it does not replace the full check. The full command runs this preflight before
toolchain/dependency setup and prints elapsed seconds for each validation step.
CI streams the retained test log during validation and includes stage timings in
the job summary, so compilation and kernel replay progress are visible while running.
The shared check defaults Lake artifact caching to disabled. CI and factory
profiles may enable native caching for project modules and pinned dependencies;
keep that cache outside captured source and preserve the complete validation
gates. Lake checks source, compiler-option and transitive-import traces before
reusing a module, rebuilding changed modules and their dependents. CI saves Lake
artifacts and Mathlib downloads after
successful checks, keyed by OS, architecture, toolchain and dependency manifest.
The commit suffix allows the cache to grow when later changes introduce imports.
`LAKE_CACHE_DIR` and `MATHLIB_CACHE_DIR` locate these caches outside the checkout
so IntentBond's fresh snapshots inherit them. `LAKE_ARTIFACT_CACHE=true` enables
incremental compilation; use `false` for fresh compilation in an isolated snapshot.
The shared check sets `LAKE_RESTORE_ARTIFACTS=true` so all outputs are restored to
the paths used by the audit, tests and kernel checker. A warm cache still runs
the complete module build, fresh kernel replay, axiom audit and regression tests.

The [validation wrapper](scripts/validation.py) and CI automatically select
documentation checks when only regular, nonexecutable `README.md` or Markdown
under `docs/` changed. They compare complete source contents and modes against the
frozen baseline, including additions, deletions and nonignored untracked files.
The shared check verifies the selection again inside IntentBond's captured snapshot.
Other source changes, missing or stale comparisons, and an empty diff select the
full check. This includes changes to scripts, tests, dependencies, workflows,
agent instructions and `scope.json`.

The documentation path checks module inventory, Python regressions for inventory
and selection, and local document links and heading anchors. It does not run Lean
examples, including Appendix F, or provision Haskell and Alloy. Frozen change
records remain under their retention policy; document-link checks cover living
docs. IntentBond coverage, source matching and independent read-only review still
apply, including review of mathematical claims. Evidence records the selected path
without claiming a new Lean build.

The shared check discovers every project module, rejects reverse dependencies
(including through root/helper modules), builds and runs `leanchecker` on each,
including examples. It batches library/module builds in one Lake invocation and
passes the three public roots to one verbose `leanchecker` invocation, which
enumerates their compiled descendants, including unimported helpers/examples.
This avoids repeated directory scans and overlapping module replay. The checker
thread pool defaults to four threads; set `LEAN_NUM_THREADS` to choose its size.
It generates an `import all` audit from
`tests/axiom_audit.lean`. After the build, it runs that audit, the independent public-import test, all Lean
validation tests and Python tests, including dependency/scope/audit rejection cases.
These gates precede the expensive kernel replay so failures return earlier.
Every successful full check still replays the complete discovered module inventory.
Unowned Lean sources are errors; keep validation harnesses under `tests/`.
The audit permits only Lean's standard logical axioms (`propext`, `Quot.sound`,
`Classical.choice`) and reports which are used; it rejects new axioms, unsafe or
partial project declarations, including private/generated declarations selected
by module origin. The audit rejects empty/missing DPGraph coverage; zero
FormalCD/Clafer declarations mean scaffolding only. Mathlib is pinned in the Lake files. The check
first tries Mathlib's normal cache for the imports discovered across every project
module and Lean test, including helpers/examples outside the public entrypoints.
Mathlib fetches their transitive dependencies; the generated inventory is
`.lake/validation/mathlib-imports.txt`. An empty inventory skips prefetch, and an
unavailable cache falls back to source compilation. Ordinary `lake build` also builds
from source. Cache availability never waives the build or kernel check.

The installed IntentBond skill is at `intentbond/skills/intentbond/SKILL.md`
inside the Python package. It can be located with:

```sh
python -c 'from importlib.resources import files; print(files("intentbond") / "skills/intentbond/SKILL.md")'
```

Before editing, retain the baseline commit (`git merge-base HEAD origin/main` on
a feature branch; the starting `HEAD` on main). Keep the affected intent,
requirements, source/proof references, and checks consistent. Run:

```sh
python3 scripts/validation.py check --base BASE_COMMIT --candidate worktree --out /tmp/clafer-check
```

Choose a fresh external output directory for each run. The wrapper invokes
`ib check`, using `scope.json` from that baseline and running `scripts/check.sh`
on a captured source snapshot. It retains `/tmp/clafer-check-selection.json`
beside the evidence directory, with both source manifests, baseline identity and
selection reason. Add `--full` to require all validation gates. Direct
`ib check` or `bash scripts/check.sh` without a selection plan also runs full validation.

Exit 0 passes automation; exit 4 passes automation with
semantic review pending. Other exits fail. Keep the reported evidence directory
outside the repository and summarize it in the PR. After committing, match the
commit against that evidence with `ib verify --base BASE_COMMIT --candidate HEAD
--evidence /path/to/evidence.json`. Use `--allow-pending-review` only when review
will be enforced before acceptance.

CI selects documentation or full validation before expensive toolchain setup,
and runs IntentBond on pull requests and main. Follow the
[scope-selection rules](docs/traceability.md#scope-selection) for baseline policy,
first adoption and the exact public-root expansion. Local checks against the
historical baseline require the independently approved scope via `--scope`.
Candidate policy changes cannot authorize themselves; other scope changes
require separate review.

## Tickets and pull requests

Authenticate `gh` with an account that can access this repository and Project
(classic tokens need `repo` and `project`; equivalent fine-grained permissions
also work). Example:

```sh
python3 scripts/tickets.py list
python3 scripts/tickets.py create --title 'Define the selected core syntax' --body-file /tmp/issue.md --label semantics
python3 scripts/tickets.py track 1 --status in-progress
python3 scripts/tickets.py comment 1 --body-file /tmp/progress.md
```

The helper adds issues to the Project and updates its Status field. It can also
edit issue bodies/labels and close completed issues. Use `track` to repair Project
membership after a partial creation failure. GitHub-hosted issue/PR status and
the Project should agree; link implementation PRs with `Closes #N`.

Use a topic branch, keep changes focused, and explain what changed and how it was
checked. Include paper references and affected requirement IDs for semantic work.
Follow the [documentation policy](AGENTS.md#documentation): keep living docs
current, change comparisons in the PR, and factory evidence outside the repository.
Use the [Lean trace-link convention](docs/traceability.md) for implementation and
proof artifacts; the pinned OFT does not import inline `.lean` tags.
Review must assess whether definitions match the intended semantics and whether
proofs establish the stated results; trace coverage and a successful build alone
do not establish that correspondence. The [source map](docs/SOURCES.md) owns exact
paper correspondences, accepted corrections and audit limits; the
[product overview](docs/intent.md) owns current scope. Keep focused contracts and
trace indexes separate from those summaries, and preserve frozen change records
under their retention policy.

Contributions use the existing [MIT license](LICENSE). Preserve attribution and
check licenses before incorporating upstream code or publication material.

## Pinned import validation prerequisites

The importer tests execute the pinned Haskell exporter as well as Lean. On Linux
x86_64, `bash scripts/check.sh` prepares it automatically in an external cache when
no exporter is configured. Install GMP headers (`libgmp-dev` on Debian/Ubuntu)
and allow the first build to download the pinned Stack, GHC and dependencies.
For explicit provisioning, build in external scratch and set `CLAFER_CAPTURE`
and `CLAFER_CAPTURE_BUILD` as described in
[the import guide](docs/resolved-import.md#build-and-replay).
Keep source archives, GHC/Stack caches, binaries and evidence outside the repository.
Setup failures fail the check; saved JSON fixtures do not substitute for compiler
execution. The shared check retains all existing module, kernel, axiom, layer and
independent-import checks.

The same Python suite runs [bounded comparison](docs/bounded-comparison.md) against
hash-pinned Alloy 6.2.0 with SAT4J and Java 17. Provisioning and bridge compilation
use an external cache; explicit tool settings are checked, with no missing-tool
skip. Comparison artifacts and minimized replays are retained externally under
`CLAFER_COMPARISON_EVIDENCE` (temporary directory by default). CI retains them
with validation evidence. Read the relation/domain and arithmetic limits before
interpreting a bounded solver result.
CI builds the same exporter from verified source/Stack archives before the check,
retaining its build identities and log with the validation evidence.
