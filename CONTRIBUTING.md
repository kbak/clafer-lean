# Contributing

<!-- [impl->req~public-foundation~1] -->

Start with an existing issue or propose a small, scoped one in the
[GitHub Project](https://github.com/users/kbak/projects/2). Semantic work should
identify the paper sections, intended definitions/theorems, ambiguities, and
acceptance criteria before implementation. See [AGENTS.md](AGENTS.md).

## Setup and checks

<!-- [impl->req~intentbond-workflow~1] -->

Install Lean with [elan](https://lean-lang.org/install/), Python 3.11+, Git,
Java 17+, and the [GitHub CLI](https://cli.github.com/). Then:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements/intentbond.txt
ib install-oft
bash scripts/check.sh
```

The shared check builds every library module, runs `leanchecker`, audits project
declarations with `tests/axiom_audit.lean`, and runs the Python ticket-helper tests.
The audit permits only Lean's standard logical axioms (`propext`, `Quot.sound`,
`Classical.choice`) and reports which are used; it rejects new axioms, unsafe or
partial project declarations. Mathlib is pinned in the Lake files. The check
first tries Mathlib's normal cache for the targeted imports, falling back to
source compilation if the cache is unavailable. Ordinary `lake build` also builds
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
ib check --repo "$PWD" --base BASE_COMMIT --candidate worktree
```

The check uses `scope.json` from that baseline and runs `scripts/check.sh` on a
captured source snapshot. Exit 0 passes automation; exit 4 passes automation with
semantic review pending. Other exits fail. Keep the reported evidence directory
outside the repository and summarize it in the PR. After committing, match the
commit against that evidence with `ib verify --base BASE_COMMIT --candidate HEAD
--evidence /path/to/evidence.json`. Use `--allow-pending-review` only when review
will be enforced before acceptance.

CI runs Lean validation and IntentBond on pull requests and main. For the first
infrastructure PR, whose base has no scope, CI checks the candidate baseline
against itself and explicitly leaves adoption to PR review. Later PRs always use
the base branch's scope; candidate scope edits do not select their own policy.

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
Use the [Lean trace-link convention](docs/traceability.md) for implementation and
proof artifacts; the pinned OFT does not import inline `.lean` tags.
Review must assess whether definitions match the intended semantics and whether
proofs establish the stated results; trace coverage and a successful build alone
do not establish that correspondence. The current slice adds DP-graph syntax
and morphism laws; predicate semantics remain future work.

Contributions use the existing [MIT license](LICENSE). Preserve attribution and
check licenses before incorporating upstream code or publication material.
