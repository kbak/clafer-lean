# Issue #19 implementation plan

Base: `bb2fe88c9ac060a0002ec8e503bcc5631f3be0ab`. Use the canonical intent and requirement links from spec.md; retain task identity `issue-19`. This plan implements the already authorized bounded scope.

1. Confirm the actual worktree base and repository guidance. Inspect FormalCD/Metamodel/Basic.lean, Binding.lean and Interpretation.lean; FormalCD/Basic.lean and Signature.lean; DPGraph predicate arities, meanings and semantic graph; the source figure and linked requirements. Reuse the delivered wellFormed and formula-representation results.
2. Add a focused self-description module under FormalCD (for example FormalCD/SelfDescription.lean) expressing the precise shared-syntax statement with explicit registry, vocabulary and universe bounds. Preserve the existing metamodel and its documented semantic limits.
3. Add source-linked telematics modules under FormalCD/Telematics (Basic.lean, VC.lean and Examples.lean). Define the four-node/five-arrow graph, VC extension, twelve effective declarations and well-formed CD. Keep demonstration modules separate from public imports.
4. Connect VC's actual four-arrow arity to a bounded integer interpretation. Reuse built-in span meanings. Prove the full nonempty example model and interpreted greater/equal/lower/no-server witnesses, with the negative model satisfying the other declarations.
5. Maintain docs/spec.md, docs/formalcd-trace.md, docs/SOURCES.md and affected overview/architecture guidance together. Name new requirements after checking existing IDs; preserve continuing obligations. Resolve Q7 wording while retaining the paper's discrepancy and original frozen artifacts.
6. Update FormalCD.lean only for reusable public API, plus tests/formalcd_imports.lean and tests/test_project_modules.py as required by discovery/import checks. Retain independent DPGraph imports, correct layer direction and existing witnesses.
7. Run the supplied traceability invocation on the captured base, including the unchanged complete scripts/check.sh workflow. Review the full diff and linked promises and preserve evidence. Leave changes uncommitted for the parent factory to verify the exported candidate, run its configured independent read-only review and publish a draft PR with Closes #19 only after all gates pass. This execution split follows the factory implementation workflow.

Main risks are reversing VC through the contradictory prose, accidentally requiring a server, asserting satisfaction from well-formedness, weakening bag-key/full-binding limits, and confusing model-language metaclasses with Lean universes. The concrete satisfaction witnesses and explicit theorem domains address those risks. Integer interpretation details are explicit local data, not a general object-diagram semantics expansion.

Implementation may adjust the proposed module split and proof techniques without changing scope. Keep this plan current while retaining intent/spec/acceptance snapshots. Return ticket updates and evidence links to the coordinator; workers receive no GitHub credentials.

Steps 1–6 are implemented in SelfDescription plus Telematics/Basic, VC and
Examples, with living documentation and trace artifacts. Step 7 retains the
factory validation, independent review and publication gates. The
semantic witnesses share a parameterized two-component model with an optional
server and arbitrary integer versions; this isolates VC failures while proving
the other eleven declarations together. No scope or accepted behavior changed.
