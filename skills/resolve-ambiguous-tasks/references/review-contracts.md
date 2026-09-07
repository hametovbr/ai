# Review Contracts

## Contents

- Isolation rule
- Review stages
- Reviewer packets
- Reconciliation loop

## Isolation Rule

For independent reviews required by the selected rigor, use a fresh subagent. Light direct checks need no reviewer. Provide only:

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

Apply review stages proportionally. Light uses a direct scope and claim-to-source check. Standard uses one independent audit when a material decision or contested evidence warrants it; otherwise record the direct check and rationale. High requires source-map critique before expensive/sensitive discovery and isolated research and readiness reviews. Audit formal specifications/plans at the selected rigor; a planning/execution skill may satisfy an independent gate using the same isolation rule. Repository-mandated reviews remain binding. Review does not itself introduce approval checkpoints.

## Reviewer Packets

### Source-map critique

> Audit this context and source map against its proof target. Identify material blind spots, implicit assumptions, privacy or authority risks, and bounded searches with the highest information gain. Do not solve the task or invent missing facts. Return findings ordered by severity and reference artifact IDs.

### Research audit

> Audit the synthesis against the claim and evidence ledgers. For every material claim, verify cited support, contradicting evidence, source authority/currentness, confidence calibration, and plausible alternatives. Flag claims that are unsupported, stronger than evidence, or not needed for the proof target. Return a claim-to-source coverage verdict and material findings.

### Specification audit

> Audit this specification against the approved research pack. Look for missing scope boundaries, actors, invariants, error paths, compatibility constraints, nonfunctional requirements, observability, rollout/rollback, and testable acceptance criteria. Do not redesign unless a finding requires a minimal correction.

For plan reviews, identify duplicate/superseded tasks and checks whose cost has no distinct acceptance benefit. Preserve required behavior and project gates; omit optional additions with no concrete risk or requirement.

## Reconciliation Loop

1. Primary agent classifies every finding as accepted, rejected-with-evidence, or deferred-with-owner.
2. Update artifacts and invalidate dependent claims/decisions when needed.
3. Ask the user only about material preference, authority, or acceptance questions that evidence cannot answer.
4. Re-run a required review only when changed material affects its verdict.
5. Stop when no material finding remains. Reopen settled decisions only for new material evidence, changed requirements or a concrete defect, including security defects. At three unresolved cycles, diagnose the specific disagreement; ask the user only for a user-owned decision, otherwise report the evidence blocker. A cycle limit does not justify repeating an unchanged review.

Before a gate, check claim-to-source coverage. For Light this is the direct check; for higher rigor it complements required independent review.

