# Review Contracts

## Contents

- Isolation rule
- Review stages
- Reviewer packets
- Reconciliation loop

## Isolation Rule

Use a fresh subagent. Provide only:

1. the artifact being reviewed;
2. the contract/rubric it must satisfy;
3. directly referenced evidence needed to verify it.

Do not provide the author’s conclusion, confidence pitch, chain of reasoning, preferred option, or prior reviewer verdict. If `grill-me` is available, explicitly invoke it in the reviewer prompt. Otherwise invoke `grilling`. The isolation contract remains authoritative.

The reviewer returns findings, not a replacement artifact. Each finding contains severity (`material` or `minor`), exact location/ID, violated contract field, evidence or counterexample, and the smallest corrective action.

## Review Stages

| Stage | Input | Required output |
|---|---|---|
| Source-map critique | Context contract, coverage map, gap ledger | Missing source classes, hidden assumptions, unsafe breadth, better narrowing keys |
| Research audit | Synthesis, claim ledger, evidence ledger | Unsupported/overstated claims, contradictions, missing alternatives, citation gaps |
| Specification audit | Approved research pack, draft specification | Missing boundaries, requirements, failure modes, acceptance criteria, rollout/rollback issues |
| Plan audit | Approved specification, implementation plan | Unmapped requirements, unsafe ordering, missing verification, unclear checkpoints |

Source-map critique is required only at High rigor or when discovery is expensive/sensitive. Research audit is required for Standard and High. Specification audit is required before final specification approval. Plan review may be satisfied by the planning/execution skill when it uses an independent reviewer with the same isolation rule.

## Reviewer Packets

### Source-map critique

> Audit this context and source map against its proof target. Identify material blind spots, implicit assumptions, privacy or authority risks, and bounded searches with the highest information gain. Do not solve the task or invent missing facts. Return findings ordered by severity and reference artifact IDs.

### Research audit

> Audit the synthesis against the claim and evidence ledgers. For every material claim, verify cited support, contradicting evidence, source authority/currentness, confidence calibration, and plausible alternatives. Flag claims that are unsupported, stronger than evidence, or not needed for the proof target. Return a claim-to-source coverage verdict and material findings.

### Specification audit

> Audit this specification against the approved research pack. Look for missing scope boundaries, actors, invariants, error paths, compatibility constraints, nonfunctional requirements, observability, rollout/rollback, and testable acceptance criteria. Do not redesign unless a finding requires a minimal correction.

## Reconciliation Loop

1. Primary agent classifies every finding as accepted, rejected-with-evidence, or deferred-with-owner.
2. Update artifacts and invalidate dependent claims/decisions when needed.
3. Ask the user only about material preference, authority, or acceptance questions that evidence cannot answer.
4. Re-run the same review on changed material.
5. Stop after no material findings or three cycles. At three unresolved cycles, report the disagreement and request a user decision; do not silently average conclusions.

Before a gate, run the claim-to-source audit even if a critic found no issue. Independence and citation coverage test different failure modes.

