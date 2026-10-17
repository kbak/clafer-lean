# Issue #4: spans and mapping operations

Status: proposal for semantic adoption and implementation; no worker dispatched.

Canonical product overview: [docs/intent.md](https://github.com/kbak/clafer-lean/blob/cabcf18abf231a4aac510d8f9996110ff2d8db09/docs/intent.md).
Local outcome: deliver reusable mapping semantics that preserve distinct links, supporting future FormalCD semantics within the independent DPGraph layer.

Sources: [issue #4](https://github.com/kbak/clafer-lean/issues/4) and its [Q1 clarification](https://github.com/kbak/clafer-lean/issues/4#issuecomment-6224179327); [current source analysis](https://github.com/kbak/clafer-lean/blob/cabcf18abf231a4aac510d8f9996110ff2d8db09/docs/SOURCES.md#span-composition-q1-research-for-4). The user asks whether the clarification makes #4 ready to start. The issue and comment explicitly leave semantic adoption pending.

Decision proposed for adoption: retain pullback span composition and distinct composable link pairs. Prove agreement with relational composition after existential relation reduction. Stronger span isomorphism requires injectivity of the composite endpoint pairing. Preserve the two-path counterexample.

The proposed scope implements the issue's representations, conversions, operations and proofs. Predicate meanings in #16, FormalCD/Clafer implementation, global SetMap, quotient/bicategory machinery and executable instance generation remain separate work. #15 is delivered. Remaining #2/#13 research stays open; this proposal adopts only the source/design decisions needed for #4.

An explicit instruction to implement this package accepts this precise Q1 correction and scope. It does not assert that proofs or review have already passed.
