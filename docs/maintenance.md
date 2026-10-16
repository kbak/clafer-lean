# Repository maintenance

The repository and its [Project](https://github.com/users/kbak/projects/2) are
currently private. The MIT license is already in place; changing visibility
remains a maintainer decision.

Before making the repository public:

- Enable main-branch protection/rulesets: require PRs, a passing
  `Lean and IntentBond` check, resolved review conversations, and block force
  pushes/deletion. Choose review requirements appropriate to the contributor
  pool; keep IntentBond exit-4 semantic review mandatory before acceptance.
- Enable GitHub private vulnerability reporting, update [SECURITY.md](../SECURITY.md),
  and add the reporting link to the issue template configuration.
- Review tracked files and history for private data; check attribution for any
  imported publication material or upstream code.
- Decide when to make the Project public, separately from repository visibility.

GitHub rejected branch protection and private vulnerability reporting during
initial setup under the current private-repository plan. CI and contributor
instructions are configured, but they cannot enforce protected-branch rules
until GitHub makes those features available.

IntentBond updates must update both `requirements/intentbond.txt` and the pinned
skill link in `AGENTS.md`. Lean updates must update `lean-toolchain` and pass the
shared checks. Review checking-policy changes explicitly; IntentMade's trusted
scope pin must also be deliberately advanced when adopting a new policy.
