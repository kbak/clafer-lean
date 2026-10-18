# Clafer Lean

<!-- [impl->req~public-foundation~1] -->

[![CI](https://github.com/kbak/clafer-lean/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/kbak/clafer-lean/actions/workflows/ci.yml)

**A Lean 4 formalization of Clafer's modeling semantics.**
[Clafer](https://www.clafer.org/) combines class modeling, feature modeling, and
constraints in one language for describing families of systems and their valid
configurations. This project turns the definitions in the 2014 Clafer paper into
precise mathematical objects and machine-checked proofs.

Use it to study the semantics, inspect worked models, or build on reusable graph
and class-diagram foundations. The focus is the connection between a model's
structure, its constraints, and the configurations that satisfy them.

[Overview and documentation](docs/intent.md) · [Contributing](CONTRIBUTING.md) ·
[Roadmap](docs/ARCHITECTURE.md#roadmap-and-validation-accounting) · [MIT license](LICENSE)

## What is here?

The `clafer` Lake package provides three public Lean libraries:

| Import | What it provides |
| --- | --- |
| `DPGraph` | Graphs with predicates, link-preserving spans, model restriction, and conditional model transport and amalgamation results |
| `FormalCD` | Class diagrams with names and defaults, structure-preserving mappings, and the paper's metamodel and telematics example |
| `Clafer` | Resolved syntax, typed constraints and their core meanings, structural compilation and gluing, and a verified finite structural candidate checker |

Dependencies flow `Clafer → FormalCD → DPGraph → Mathlib`; `DPGraph` is independently
importable. The [architecture](docs/ARCHITECTURE.md) explains these boundaries.

**Status: active research, with no stable API or supported releases.** The
[Appendix F case study](docs/appendix-f.md) connects a complete, manually resolved
telematics model to compilation and a concrete satisfying interpretation,
including all twelve constraint bodies. Its proof establishes that particular
model under the documented formalization choices. General source-text compiler
correctness, a production parser, configuration generation, and Alloy/SMT/SAT
integration are outside the delivered scope. See the [current scope](docs/intent.md)
and [finite checker's supported fragment](docs/structural-checker.md).

## Get started

Install Git and [Lean via elan](https://lean-lang.org/install/), then:

```sh
git clone https://github.com/kbak/clafer-lean.git
cd clafer-lean
lake build
```

Elan selects the pinned [Lean toolchain](lean-toolchain); Lake fetches the pinned
Mathlib dependency. The first build can take time to download and compile dependencies.
For editor support, open the checkout with the Lean 4 extension for VS Code.

Start with the [span examples](DPGraph/Span/Examples.lean), which show why two links
between the same endpoints carry more information than an ordinary relation.
After building, check that file with:

```sh
lake env lean DPGraph/Span/Examples.lean
```

Then explore [class diagrams](FormalCD/Examples.lean),
[compilation and gluing](docs/representative-models.md), or the
[complete telematics model](docs/appendix-f.md). The
[documentation map](docs/intent.md#documentation-map) leads to detailed contracts,
source citations, and proof indexes.

## Contribute

Questions, bug reports, documentation improvements, and small proof contributions
are welcome. Start with the [issues](https://github.com/kbak/clafer-lean/issues)
and [contribution guide](CONTRIBUTING.md). Discuss semantic changes in an issue
before implementation, identifying the relevant paper sections and acceptance criteria.

The full validation command is `bash scripts/check.sh`; follow the
[setup instructions](CONTRIBUTING.md#setup-and-checks) for its prerequisites and
the required [IntentBond](https://github.com/kbak/intentbond) check. Validation
builds every project module, replays proofs through Lean's kernel checker, audits
axioms, and runs regression tests. IntentBond connects requirements to artifacts
and retains evidence; semantic review remains necessary.

[AGENTS.md](AGENTS.md) also applies to agent contributions. Work is tracked in the
public issues; maintainers also use a
[private GitHub Project](https://github.com/users/kbak/projects/2).
For sensitive reports, follow the [security policy](SECURITY.md).

## References and license

The primary semantic reference is:

- *Clafer: unifying class and feature modeling*, Software and Systems Modeling,
  [DOI: 10.1007/s10270-014-0441-1](https://doi.org/10.1007/s10270-014-0441-1)
  ([free preprint](https://gsd.uwaterloo.ca/sites/default/files/2014-Bak-Clafer-Unifying-Class-Feature-Modeling%28SOSYM%29.pdf)).

Read the [paper corrections and clarifications](docs/sosym-errata.md) alongside it;
the [source map](docs/SOURCES.md) records exact correspondences and accepted choices.
The maintained [Haskell implementation](https://github.com/gsdlab/clafer/)
provides supplementary context and the existing Clafer toolchain.

[MIT licensed](LICENSE). Referenced publications and upstream code retain their
own licenses.
