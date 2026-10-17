# Issue #19 intent

Implement [#19](https://github.com/kbak/clafer-lean/issues/19): finish the bounded formal-CD self-description statement and the Figure 21b example using the metamodel delivered by #18/#36. Product purpose and exclusions remain in the canonical [intent](https://github.com/kbak/clafer-lean/blob/bb2fe88c9ac060a0002ec8e503bcc5631f3be0ab/docs/intent.md).

The maintainer corrected VC to `display.version ≥ server.version`, agreeing with the Figure 8 Clafer model, Figure 21a and Appendix F. Figure 21a guards the comparison by the presence of a server. The contradictory nearby prose must not reverse the selected meaning. The outcome is an explicit checked example and honest theorem boundaries, with usable source citations and trace links.

Self-description means a precisely typed representation/well-formedness statement in the existing FormalCD syntax, with explicit signature, registry and universe bounds. It does not promise semantic self-instantiation or unrestricted realizability of every graph-shaped formula in the printed metamodel. Preserve #18's full bindings and its literal bag-key/total-args limits.

Authorization: the maintainer explicitly requested: “Implement #19 from latest main, including the corrected VC condition. Run the normal factory validation and independent read-only review, and confirm the submitted task/run ID.” This authorizes implementation and the normal draft-PR workflow. The preceding discussion resolved the inequality; inspection of Figure 21a resolved the absent-server guard. No further approval is needed for this scope. Merge and deployment are not included.
