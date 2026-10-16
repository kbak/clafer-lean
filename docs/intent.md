# Intent

## A maintainable foundation for formal semantics
`intent~formalization-foundation~1`

Develop a Lean 4 formalization grounded in the 2014 SoSyM paper. The repository
`kbak/clafer-lean` contains one Lake package, `clafer`, with sibling public roots
`DPGraph`, `FormalCD` and `Clafer`. Dependencies flow
`Clafer -> FormalCD -> DPGraph -> Mathlib`: independently reusable foundations
support structural 2014 Clafer as their application. DPGraph supplies graphs, typed diagram
predicates and declaration-preserving maps; FormalCD will supply formal class
diagrams independently of Clafer. Abstract mathematical semantics remain in scope
for later, separately reviewed increments.

The delivered mathematical slice is SoSyM Appendix B.4, Definitions 6–10.
FormalCD and Clafer have public entrypoint scaffolding only; predicate semantics,
SetMap and Theorem 3 remain undelivered. The [architecture](ARCHITECTURE.md)
explains the mathematics and future layer boundaries; [requirements](spec.md),
[source citations and open questions](SOURCES.md), and
[Lean definitions and proofs](dpgraph-trace.md) describe the current promises.
Track subsequent work in the [live roadmap (#2)](https://github.com/kbak/clafer-lean/issues/2) and
[design (#13)](https://github.com/kbak/clafer-lean/issues/13).

Exclude instance/object generation, Alloy/SMT/SAT integration, runtime
configurations, Claferize, post-2014 extensions, a production parser and
visualization. Keep the foundation reproducible and reviewable and the README
focused on its purpose.

Needs: req

## Consistent work by people and agents
`intent~traceable-contributions~1`

Use IntentBond to maintain the relationship between intended outcomes,
requirements, implementation, and verification evidence as the project evolves.
Use GitHub issues and a Project for planning and tracking, including IntentMade
work, so work and outstanding semantic decisions remain visible.
Follow the [contribution instructions](../CONTRIBUTING.md) and
[documentation policy](../AGENTS.md#documentation).

Needs: req
