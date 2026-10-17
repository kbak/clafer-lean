# First FormalCD structure and morphisms — #17

Deliver the first reusable FormalCD implementation above the completed DPGraph
foundation, so later metamodel and Clafer work can refer to checked class-diagram
structure and composable structure-preserving maps.

Canonical product overview: [docs/intent.md](https://github.com/kbak/clafer-lean/blob/dccdc5d1c2d698d34a06bf279290cb8ebfe0d94f/docs/intent.md).
Task: [#17](https://github.com/kbak/clafer-lean/issues/17).
Source: SoSyM §6.1.1–3 and Figure 21; B.4 Definitions 6–10.

The user accepted the preceding concrete proposal with “sounds great, let's do it”.
That proposal selects graph identities separate from names, predefined/reserved
names, inclusion declarations, explicit set-valued defaults with bag-valued
exceptions, and name-preserving FormalCD morphisms with identity/composition laws.
This package makes those contracts implementable within the approved scope.

The same underlying graph/formula API must serve all layers. Names are metadata:
two different inclusion arrows may both be named isA. Syntactic well-formedness
and semantic model satisfaction remain different notions. Predefined-class keys
identify optional built-in classifiers; this increment does not implement the
primitive-value semantics of a complete object-model interpreter.

#15, #4 and #16 are merged; the reviewed starting main is
dccdc5d1c2d698d34a06bf279290cb8ebfe0d94f (#34). The local catalog at
cabcf18abf231a4aac510d8f9996110ff2d8db09 is stale. Current guidance, affected
requirements, architecture and predicate signature were read from pinned GitHub
sources. Factory planning and dispatch must use the current main, not that catalog.

Figure 21c encoding, self-description, VC meaning, renaming morphisms, MCS and
Clafer compilation/gluing stay with their later increments (#18, #19, #20–#24).
No new object generation, solver, parser or rendering work is authorized.

