# Tracing Lean definitions and proofs

The pinned IntentBond/OpenFastTrace combination imports Markdown requirements
and artifacts, but OpenFastTrace 4.9.0 does not import `.lean` source tags.
Do not put OFT coverage annotations directly in Lean files and assume they are
checked. Lean files remain in `scope.json`: their contents are captured, their
modules are built and kernel checked, and their changes require review.

Until native Lean tag support is adopted, declare named implementation and proof
artifacts in Markdown under `docs/`, beside explicit links to the corresponding
Lean file and declaration names. For example, when a real requirement exists:

```markdown
## Representation of model shape
`impl~model-shape-representation~1`

The `ModelShape` declaration in ClaferLean/Syntax.lean represents the selected
abstract syntax. Link the source file and explain the correspondence here.

Covers:
- `req~model-shape~1`
```

Proof artifacts can use the same structure with type `proof`, naming the actual
theorem and its source. State `Needs: impl, proof` on requirements that require
both, rather than labeling documentation as proof. Use `utest` for actual tests.
Maintain these artifact declarations, source links, theorem statements, and
requirements together. Keep source references precise as declarations move.

These are checked OFT artifacts whose locations are in Markdown. Review must
follow their links into the Lean implementation and proofs. Neither a source
link nor an artifact named `proof` establishes the theorem; Lean checks the
declaration, and review assesses whether its statement matches the requirement
and the cited paper. Command-level evidence records the configured check's
result; it does not associate individual theorem executions with artifacts.
