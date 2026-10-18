# Clafer Lean

Formalizing [Clafer](https://www.clafer.org/)'s semantics in Lean 4.
The proven foundation provides link-preserving spans and mapping operations
from SoSyM B.1–B.2, plus DP-graphs, their fixed-signature category and abstract
model restriction from B.4–B.5, and selected Table 3/A.1 predicate meanings.
Formal class diagrams add naming/default obligations, name-preserving morphisms
and the Figure 21c metamodel with explicit name/arity disciplines and bounded
syntactic self-description. Figure 21b includes the corrected guarded version
constraint and checked concrete models.
Structural 2014 Clafer adds resolved syntax, individual Shapes and the structural
MCS discipline from Figure 23 and Appendix E, with structural Compile and gluing; start with
the [product overview](docs/intent.md).
Readers of the paper can consult the [corrections and clarifications](docs/sosym-errata.md).

Install [Lean via elan](https://lean-lang.org/install/), then run:

```sh
lake build
bash scripts/check.sh
```

The repository is `kbak/clafer-lean`; its single Lake package is `clafer`.
Use `import DPGraph` for this foundation and its bounded semantic graph of
subsets and spans. See the overview for supported predicates and future scope.
The sibling public roots follow `Clafer -> FormalCD -> DPGraph -> Mathlib`.
Use `import FormalCD` for class diagrams and `import Clafer` for resolved syntax, Shapes, MCS, Compile and gluing.
The toolchain is pinned in `lean-toolchain`.
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
