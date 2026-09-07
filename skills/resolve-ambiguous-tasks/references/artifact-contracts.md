# Artifact Contracts

## Contents

- Identity and status rules
- Context/research pack
- Research synthesis
- Readiness record
- High-level specification
- Implementation handoff
- Compact example

## Identity and Status Rules

Use stable IDs so artifacts survive compaction and can be reviewed independently:

- `E-###` evidence, `C-###` claim, `U-###` unknown, `B-###` blocker;
- `D-###` decision, `Q-###` user question, `R-###` requirement, `A-###` acceptance criterion.

Define an item as `- [E-001] ...`; reference it as `(E-001)`. Reference each ID separately: ranges such as `(E-001–E-003)` are invalid. Never recycle an ID. Mark changes as `ACTIVE`, `INVALID`, `SUPERSEDED`, `OPEN`, or `CLOSED` instead of deleting history.

The deterministic validator recognizes these conventions plus `Mode:`, `Rigor:`, and `Readiness:` fields.

## Context/Research Pack

```markdown
# Context map
Mode: research-only | decision | implementation | diagnosis
Rigor: Light | Standard | High
Readiness: NOT_READY | READY

## Contract
Deliverable: {requested output}
Proof target: {completion proposition}
In scope: {bounded scope}
Out of scope: {explicit exclusions}
Authority/privacy: {limits}
Constraints: {compatibility, risk, time, format}

## Coverage
- Behavior: covered | partial | missing | not-applicable
- Data: ...
- History: ...
- Operations: ...
- Ownership: ...
- Failure modes: ...

## Evidence
- [E-001] Source: {locator}; Scope/currentness: {value}; Observation: {fact}; Limitation: {value}

## Claims
- [C-001] Claim: {statement}; Evidence: (E-001); Contradicts: none; Confidence: medium; Status: ACTIVE

## Unknowns and blockers
- [U-001] Unknown: {gap}; Material: yes; Status: OPEN; Next evidence: {bounded step}
- [B-001] Blocker: {constraint}; Owner: {role}; Status: OPEN

## Decisions and questions
- [D-001] Decision: {choice}; Basis: (C-001); Status: ACTIVE
- [Q-001] Question: {preference/authority needed}; Blocks: (D-001); Status: OPEN
```

Light rigor may use a compact note containing only contract, one scope check, and any discovered material gap. Create full ledgers as soon as rigor escalates.

## Research Synthesis

The output contains, in order:

1. proof-target verdict and confidence;
2. confirmed findings, each citing claim/evidence IDs;
3. contradictions and viable alternatives;
4. limitations and inaccessible sources;
5. unresolved material and nonmaterial gaps;
6. smallest useful next evidence or explicit stopping rationale;
7. claim-to-source matrix for every material output statement.

Do not turn a research-only synthesis into a delivery proposal unless the user expands the mode.

## Readiness Record

`Readiness: READY` means:

- proof target and scope are stable enough for the selected mode;
- every material claim has supporting evidence and calibrated confidence;
- no `Material: yes; Status: OPEN` unknown remains;
- no `Status: OPEN` blocker remains;
- material tradeoffs, authority, and acceptance thresholds have owners;
- review required by the selected rigor has no unresolved material finding; Light uses a direct check, Standard uses one independent audit when warranted, and High retains isolated reviews.

Accepted nonmaterial unknowns stay visible with owner and consequence. READY is a gate verdict, not a claim of certainty.

## High-Level Specification

Create only for delivery/implementation modes:

```markdown
# Specification
Objective: {observable outcome}
Non-goals: {excluded outcomes}
Actors/systems: {boundaries and owners}

- [R-001] Requirement: {testable behavior}; Basis: (C-001)
- [A-001] Acceptance: {observable pass/fail}; Verifies: (R-001)

Invariants and constraints: {compatibility, security, privacy, performance}
Failure behavior: {errors, partial success, retries, recovery}
Observability: {signals and success thresholds}
Rollout/rollback: {boundary, abort conditions, reversibility}
Open nonmaterial unknowns: (U-001)
Approval: PENDING | APPROVED by {owner/date}
```

Use `making-architecture-decisions` when the specification selects or changes software/system architecture. User approval applies to the revised specification after the review required by the selected rigor, not merely the first draft.

## Implementation Handoff

The implementation plan maps every `R-###` to tasks, files/components, tests, verification commands, rollout checks, and an approval checkpoint. No requirement may disappear between specification and plan. Execution records evidence of verification and preserves deviations as new decisions.

Separate binding outcomes, contracts, invariants and project gates from suggested implementation methods. Allow equivalent cheaper local methods within those constraints; changes to public semantics, ownership, migration strategy or acceptance return to planning. For each planned check, state the behavior/risk, sufficient existing check and rerun trigger. Justify additional expensive checks or new test infrastructure by a concrete coverage gap. Put applicable rerun/diagnosis rules in the plan or linked authoritative contract so execution does not depend on chat history. Keep one concise mapping; reference existing evidence instead of duplicating reports.

## Compact Example

An initial “rename a UI label” request is Light. Discovery that the same term is an API field escalates rigor, invalidates the UI-only scope claim, and reopens compatibility research. The known UI location remains valid evidence; it is not discarded. Implementation waits for an approved compatibility specification and its mapped plan.
