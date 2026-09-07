# Review Contracts

## Contents

- Isolation rule
- Review stages
- Reviewer packets
- Reconciliation loop

## Isolation Rule

Apply this rule whenever the selected rigor requires an independent review or a Standard-rigor review is justified by materiality or contested evidence. Light-rigor direct checks do not require a reviewer. Use a fresh isolated reviewer and provide only:

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
| Readiness audit | Context contract, candidate readiness record, material evidence | Open material gaps, unsupported acceptance/ownership, scope drift, invalid `READY` verdict |
| Specification audit | Evidence-ready research pack, draft specification | Missing boundaries, requirements, failure modes, acceptance criteria, rollout/rollback issues |
| Plan audit | Current specification, implementation plan | Unmapped requirements, unsafe ordering, missing verification, unclear checkpoints |

Apply stages by rigor and consequence:

| Rigor | Required review |
|---|---|
| Light | Direct claim-to-source and scope check by the working agent. Escalate if a material contradiction, broad blast radius, or disputed source appears. |
| Standard | One independent research audit when the decision is material or the evidence is contestable. Otherwise record the direct coverage check and why independent review would not change the result. |
| High | Independent source-map critique before expensive or sensitive discovery, independent research audit after synthesis, independent readiness audit before action, and an independent specification or plan audit for each such artifact required by the delivery risk. |

A specification audit is required only when a specification is required by risk, repository policy, or the applicable architecture workflow. A plan audit is required only when the work warrants a formal plan; an applicable planning/execution skill may satisfy it if it preserves this isolation rule. Existing user authorization remains valid for reversible work. Review does not create a new approval checkpoint; separate approval is needed only when a governing workflow requires it or immediately before a consequential, irreversible, or externally mutating action that is not already authorized.

## Reviewer Packets

### Source-map critique

> Audit this context and source map against its proof target. Identify material blind spots, implicit assumptions, privacy or authority risks, and bounded searches with the highest information gain. Do not solve the task or invent missing facts. Return findings ordered by severity and reference artifact IDs.

### Research audit

> Audit the synthesis against the claim and evidence ledgers. For every material claim, verify cited support, contradicting evidence, source authority/currentness, confidence calibration, and plausible alternatives. Flag claims that are unsupported, stronger than evidence, or not needed for the proof target. Return a claim-to-source coverage verdict and material findings.

### Readiness audit

> Audit the candidate readiness record against the context contract and directly referenced evidence. Check that scope and acceptance are stable, material claims and ownership are supported, contradictions are reconciled, no material unknown or blocker remains open, and the proposed next action stays within authority. Return findings and a `READY` or `NOT_READY` recommendation; do not design or execute the solution.

### Specification audit

> Audit this specification against the evidence-ready research pack. Look for missing scope boundaries, actors, invariants, error paths, compatibility constraints, nonfunctional requirements, observability, rollout/rollback, and testable acceptance criteria. Do not redesign unless a finding requires a minimal correction.

For plan reviews, identify duplicate/superseded tasks and checks whose cost has no distinct acceptance benefit. Preserve required behavior and project gates; omit optional additions with no concrete risk or requirement.

## Reconciliation Loop

1. Primary agent classifies every finding as accepted, rejected-with-evidence, or deferred-with-owner.
2. Update artifacts and invalidate dependent claims/decisions when needed.
3. Ask the user only about material preference, authority, or acceptance questions that evidence cannot answer.
4. Re-run a required review only when changed material affects its verdict.
5. Stop when no material finding remains. Reopen settled decisions only for new material evidence, changed requirements or a concrete defect, including security defects. At three unresolved cycles, diagnose the specific disagreement; ask the user only for a user-owned decision, otherwise report the evidence blocker. A cycle limit does not justify repeating an unchanged review.

Before a readiness gate, run the claim-to-source audit even if a critic found no issue. For Light work this is the direct review; at Standard or High it complements any required independent review.
