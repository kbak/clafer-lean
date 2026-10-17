# Issue #18 intent

Build the Figure 21c formal-CD metamodel on the delivered FormalCD library, with explicit name/arity meanings and faithful graph-shaped formula identity. This is the next bounded step toward the later self-description/example work in #19.

Canonical product direction: [docs/intent.md](https://github.com/kbak/clafer-lean/blob/5e4f13c8e1ba58e0b0c744c1aa0397909e20f79e/docs/intent.md). Issue: https://github.com/kbak/clafer-lean/issues/18. Keep the existing three layers and independent DPGraph/FormalCD imports.

The maintainer authorized proceeding with #18 after the complete-scope recommendation and explicitly cautioned against confusing Lean's type system in #19. Preserve that boundary: model-language metaclasses are ordinary mathematical data; syntax, instances and semantic universes are distinct. No Type : Type, recursive universal type, resizing axiom, universal self-instantiation or implicit identification of modeling levels with Lean universes.

The complete scope includes the metamodel construction, name/arity predicates and graph-binding identity, rather than postponing their meanings. The exact printed Figure 21c key/args constraints do not automatically characterize every generic DPGraph. Preserve their actual meanings and make the correspondence limits explicit. #19's final self-description statement, full Figure 21b/VC example and unresolved Q7 inequality are outside this task.

These are the accepted local outcomes. Implementation choices that preserve them are routine; a newly discovered contradiction requiring changed meanings must be reported through NEEDS_INPUT. Do not weaken checks or silently reinterpret a paper constraint.
