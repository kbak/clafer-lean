# First DP-graph increment

Local outcome: validate the reusable DP-graph architecture with a small compiling and proved library, before expanding to formal class diagrams or Clafer. Product direction belongs in [docs/intent.md](https://github.com/kbak/clafer-lean/blob/main/docs/intent.md); update that canonical overview to reflect the supplied three-layer project brief without duplicating it in task documents.

The user requested source research, architecture, GitHub milestones/issues, and then a small Phase 1 vertical slice in the supplied initial execution instructions, item 8. This package covers that first slice only. It does not authorize implementation of the whole backlog. Planning and repository review have established the B.4 source scope and the initial architecture. Implementation remains a factory task with normal verification and independent review; no merge or deployment is requested.

Primary ticket: [#14](https://github.com/kbak/clafer-lean/issues/14). Related design: [#13](https://github.com/kbak/clafer-lean/issues/13). Source audit/roadmap: [#2](https://github.com/kbak/clafer-lean/issues/2). Existing contribution/traceability requirements continue to apply.

A useful result must preserve arbitrary graph shapes and parallel arrows, enforce formula arity through types, and prove declaration-preserving morphism composition. Noninjective finite examples validate that the abstraction is reusable beyond Clafer. Concrete predicate meanings, span operations, formal CDs, Clafer syntax and compilers belong to later issues.
