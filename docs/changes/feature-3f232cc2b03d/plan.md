# Documentation maintenance plan

The delivered foundation and future layer boundaries are described in the
[canonical intent](../../intent.md), [architecture](../../ARCHITECTURE.md),
[requirements](../../spec.md), [source map](../../SOURCES.md) and
[Lean trace artifacts](../../dpgraph-trace.md).

## Steps

1. Consolidate living documentation around those sources and the
   [contribution instructions](../../../CONTRIBUTING.md). Apply the durable
   [documentation policy](../../../AGENTS.md#documentation) to future work.
2. Remove redundant approval and handoff reports, keeping unique current
   explanations in living docs and change comparisons in the PR description.
   Preserve controller-required historical intent/spec/acceptance snapshots
   unchanged and retain this concise plan; their removal awaits a retention-policy
   change.
3. Audit maintained file and anchor links, including this plan; report historical
   snapshot exceptions separately. Explain current
   [scope-selection rules](../../traceability.md#scope-selection) without duplicating
   authorization history.
4. Compare the complete cleanup against its starting PR head, proving all Lean,
   validation, dependency, policy and frozen snapshot bytes unchanged. Run the
   configured captured check with the supplied trusted scope and review base;
   inspect impact and pending review requirements. Keep full check evidence and
   supplemental results outside the repository and separate from invocation bundles.
5. Obtain independent code/security, intent and traceability review of the full PR
   diff. Verify the exported commit against fresh evidence before the coordinator
   updates the existing PR. Keep the implementation issue open and In Progress
   pending acceptance and merge.

These steps replace the implementation diary with documentation maintenance and
verification; the mathematical scope and validation obligations are unchanged.

## Risks and verification

- Preserve graph-map, universe, declaration-preservation and syntax/meaning
  explanations, source identities, open semantic questions and every OFT ID,
  revision and Needs/Covers obligation.
- Follow the [Lean trace convention](../../traceability.md): coverage links and
  passing builds do not establish correspondence with the cited mathematics.
- IntentBond exit 4 means automation passed with semantic review pending.
  Source verification and independent review remain required before publication.
