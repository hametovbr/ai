# Research Protocol

## Contents

- Entry contract
- Source and coverage map
- Evidence-first research loop
- Convergence and stopping
- Mode-specific handoff

## Entry Contract

Create the context contract before broad search:

1. **Request:** exact user intent and requested deliverable.
2. **Proof target:** what must be true, explained, chosen, or demonstrated for the task to be done.
3. **Mode and rigor:** chosen value plus one-sentence reason.
4. **Scope:** included systems, time range, entities, environments, and explicit non-scope.
5. **Authority:** read/write permissions, approval owner, and actions that need new permission.
6. **Constraints:** deadlines, compatibility, cost, safety, privacy, reversibility, and output format.
7. **Inputs:** supplied artifacts with provenance and currentness.
8. **Unknowns:** separate material blockers from useful-but-nonblocking gaps.

Do not ask the user for facts that safe read-only discovery can establish. Ask when the answer is preference, authority, acceptance threshold, irreversible tradeoff, or cannot be discovered reliably.

## Source and Coverage Map

Inventory source classes before querying them. Prefer the narrowest authoritative source that can close a named gap:

- request artifacts and linked records;
- current code, tests, configuration, schemas, and ownership;
- version history, reviews, delivery records, and prior related tasks;
- operational state, logs, metrics, traces, incidents, and audit history;
- documentation, decisions, contracts, and external primary sources;
- user or domain-owner clarification.

For each class record: availability, authority, freshness, narrowing key, privacy boundary, and the gap it could close. Domain-specific skills define source order and access guardrails when available.

Build a coverage map around the proof target, not around available tools. Typical dimensions are behavior, data, history, operations, ownership, constraints, alternatives, and failure modes. Mark each `covered`, `partial`, `missing`, or `not-applicable`.

## Evidence-First Research Loop

1. Select the highest-value open material gap.
2. Form the smallest query or inspection that could discriminate among competing explanations.
3. Record the source, exact scope, timestamp/currentness, observation, limitations, and confidence as evidence.
4. Update claims with supporting and contradicting evidence. Preserve alternatives; distinguish occurrence, correlation, and causation.
5. Update unknowns, blockers, and decisions. Negative results count only when source coverage, selector, time range, and retention are known.
6. Reassess the proof target. Continue only if another bounded step can materially change the answer or readiness.

At High rigor, send the context contract, coverage map, and current gaps to a fresh reviewer before expensive or privacy-sensitive discovery. Use its findings to narrow the next round, not to authorize broad fan-out.

## Convergence and Stopping

Stop research when one condition holds:

- the proof target is supported at the required confidence and no material gap remains;
- remaining gaps cannot be closed within authority, privacy, time, or access constraints;
- expected information gain is lower than the cost/risk of another round;
- a user decision is the only missing input;
- the agreed effort limit is reached.

Do not use “all sources searched” as a completion criterion. Record an inconclusive result when evidence is insufficient.

If new evidence changes scope, ownership, risk, or the proof target, mark affected claims and decisions invalid, reclassify rigor, and revisit the earliest affected artifact. Preserve unaffected evidence.

## Mode-Specific Handoff

- **research-only:** audited synthesis, confidence, contradictions, limitations, unresolved gaps, and smallest useful next evidence. No specification or implementation plan.
- **decision:** decision record with options, constraints, tradeoffs, evidence, unknowns, reversibility, and approval owner.
- **diagnosis:** reproducible symptom, competing hypotheses, eliminated causes, root-cause confidence, and verification target; then route to the applicable debugging skill.
- **implementation:** readiness verdict plus context pack for specification. Research findings do not themselves authorize changes.

