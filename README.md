# Clafer Lean

Formalizing [Clafer](https://www.clafer.org/)'s semantics in Lean 4.
The first proven slice provides reusable DP-graphs from SoSyM Appendix B.4.
Formal class diagrams and structural 2014 Clafer are subsequent layers; see the
[architecture](docs/ARCHITECTURE.md) and [source map](docs/SOURCES.md).

Install [Lean via elan](https://lean-lang.org/install/), then run:

```sh
lake build
bash scripts/check.sh
```

The toolchain is pinned in `lean-toolchain`. The library lives in `ClaferLean/`.
Contributions, including agent work, use [IntentBond](https://github.com/kbak/intentbond);
see [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md).
Planning and tickets live in the [GitHub Project](https://github.com/users/kbak/projects/2).

Primary references:

- *Clafer: unifying class and feature modeling*, Software and Systems Modeling,
  [DOI: 10.1007/s10270-014-0441-1](https://doi.org/10.1007/s10270-014-0441-1)
  ([free preprint](https://gsd.uwaterloo.ca/sites/default/files/2014-Bak-Clafer-Unifying-Class-Feature-Modeling%28SOSYM%29.pdf)).
- The maintained [Haskell implementation](https://github.com/gsdlab/clafer/)
  provides supplementary implementation context.

[MIT licensed](LICENSE). Referenced publications and upstream code retain their
own licenses.
