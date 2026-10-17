# Working on Clafer Lean

The repository remains `kbak/clafer-lean`; its single Lake package is `clafer`.
The sibling public roots are `DPGraph`, `FormalCD` and `Clafer`, with permitted
dependencies `Clafer -> FormalCD -> DPGraph -> Mathlib`. Keep DPGraph independently
importable. Its delivered slice includes SoSyM B.1 Definitions 1–5, Theorems 1–2 and
B.2.1–2 link-preserving span operations with the adopted Q1 correction, B.4
Definitions 6–10, a fixed-signature category, the abstract B.5 model reduct and
selected Table 3/A.1 predicates in a bounded graph of subsets and spans, with the
accepted common-target Q8 disjointness correction.
FormalCD delivers raw/bundled class diagrams, naming/default obligations and
name-preserving morphisms, compatible signature support and the Figure 21c
metamodel with explicit disciplines, bounded syntactic self-description and
Figure 21b with its corrected guarded VC interpretation and concrete models.
Self-description does not assert semantic self-instantiation. VC remains a
FormalCD extension, separate from the generic built-in vocabulary.
Preserve full graph bindings separately from the literal bag key and total-args
conditions; see the source map before extending metamodel representation. Clafer currently
has entrypoint scaffolding only. Read the future layer boundaries in
[architecture](docs/ARCHITECTURE.md), the [requirements](docs/spec.md) and
[roadmap #2](https://github.com/kbak/clafer-lean/issues/2)/
[design #13](https://github.com/kbak/clafer-lean/issues/13) before those increments.

Every agent must use [IntentBond](https://github.com/kbak/intentbond) for planning,
implementation, and review. Read the development skill and its relevant references
from the revision pinned in [requirements/intentbond.txt](requirements/intentbond.txt):
[IntentBond skill](https://github.com/kbak/intentbond/blob/a430efa8d82e2a88ed2607bfe838066bb9d73f3c/intentbond/skills/intentbond/SKILL.md).
Use the installed package's matching skill when available. If tooling is missing,
follow [CONTRIBUTING.md](CONTRIBUTING.md); report a concrete blocker instead of
silently skipping IntentBond.

Read [intent](docs/intent.md), the affected [requirements](docs/spec.md), and
[scope.json](scope.json). Capture the starting Git commit before editing. Maintain
affected requirements, source references, implementation, proofs/tests, and trace
links together. Run `ib check` before handoff and retain its evidence. Exit 4
means automated checks passed with semantic review pending; it is not approval.
For Lean definitions and proofs, follow [the Lean trace-link convention](docs/traceability.md).
The pinned OFT does not import `.lean` tags: declare linked implementation/proof
artifacts in Markdown and review the actual Lean declarations they reference.
Do not weaken scope or coverage to make a change pass. Scope changes need explicit
review in the PR.

Plan and track work as issues in [the GitHub Project](https://github.com/users/kbak/projects/2).
Search existing issues before creating one. Use `python3 scripts/tickets.py` to
create, track, update, and comment on issues; `--help` lists commands. Record
scope, acceptance criteria, source sections, affected requirement IDs, dependencies,
and validation. Set In Progress when starting and link PRs with `Closes #N`.
Close tickets and mark Done only after their acceptance criteria are met.
In IntentMade, the credential-bearing coordinator uses its deployment ticket
wrapper. Workers return ticket updates to the coordinator; never copy GitHub
credentials into a worker.
If GitHub access is unavailable, preserve the proposed ticket locally and report
the blocker. A planning issue alone does not authorize semantic implementation.

The SoSyM paper is the primary semantic reference; cite section/definition numbers
when adding definitions and theorems. Record ambiguities and deliberate departures
in issues before choosing a meaning. The Haskell compiler is supplementary context;
pin a commit when using it as evidence. Do not copy third-party material without
checking its license. Keep the README brief.

Use the pinned Lean toolchain and `bash scripts/check.sh` for full validation.
A factory may use the explicitly configured documentation-only check described
in `req~lean-validation~1` after proving all other source contents and modes unchanged
from its frozen baseline. Do not select this exception by agent judgment or edit
scope to obtain it. Keep proofs kernel
checked. Do not introduce `sorry`, `admit`, disabled warning checks, or unchecked
axioms as completed proofs; discuss intentional additional axioms explicitly.
Keep private deployment paths, credentials, and runtime state outside this repo.
Place new Lean modules under their owning public root. The shared check discovers
all modules (including examples and helpers) for builds, kernel checks and
import-all audits, and rejects reverse layer imports or unowned source modules.

## Documentation

Maintain current product intent, architecture, mathematical explanations, source
citations, requirements and reusable agent guidance. Use [docs/intent.md](docs/intent.md)
as the canonical overview and link to authoritative documents rather than
duplicating them. Put before/after explanations in PR descriptions and acceptance
and execution evidence in external factory artifacts. Keep transcripts, conversation
and run IDs, execution diaries and handoff reports out of living docs; preserve
source commits and hashes used as citations. Obey controller retention requirements:
keep frozen package snapshots unchanged and required plans concise and current
until the retention policy permits removal.
