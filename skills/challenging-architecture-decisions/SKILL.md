---
name: challenging-architecture-decisions
description: "Use when reviewing or stress-testing an existing architecture, ADR, integration or migration proposal, platform choice, or implementation plan for overengineering, unsupported assumptions, unnecessary components, lifecycle risks, or readiness before approval. Do not use for initial design, fact-finding only, or routine code review that preserves system boundaries."
---

# Challenging Architecture Decisions

## Core rule

Try to invalidate or simplify the proposed design before strengthening it. Require every retained element to protect a stated requirement, invariant, or credible material failure.

Review from the proposal, user constraints, and directly relevant artifacts. A formal context contract is not required. Do not load `gathering-architecture-context` merely because it is absent.

## Review

1. Reconstruct the minimum review basis: requested outcome, scope, non-goals, invariants, proposal, and assumptions. Let the latest explicit correction invalidate conflicting earlier rationale.
2. Check whether the proposal solves the stated problem rather than a proxy such as elegance, testability, theoretical scale, or feature breadth.
3. Apply subtraction to every added component, deployment unit, state store, abstraction, script, artifact, credential, process, retry, fallback, and compatibility layer: which current requirement, invariant, or named failure breaks if it is removed?
4. Check the lowest sufficient intervention: no change/manual handling → configuration → native extension → local change → existing module or adapter → service → platform. Reject escalation when a lower level satisfies current requirements.
5. Examine only applicable lifecycle effects. Name a concrete failure, evidence, and existing recovery gap before requiring reliability machinery.
6. For an implementation plan, justify each task and expensive check by a required outcome, necessary dependency, or concrete material risk. Prefer existing sufficient checks; identify the uncovered risk before adding a costly run or test infrastructure. Distinguish binding outcomes/contracts/project gates from suggested implementation methods. Permit a cheaper equivalent method within those constraints.
7. Verify decisive claims from current code, configuration, measurements, official documentation, or maintained examples. Mark inference and assumption explicitly.

Use `gathering-architecture-context` only when a missing, disputed, stale, or inaccessible fact can change the verdict. If the missing item is user-owned or inaccessible, material, and has no safe reversible default, return `insufficient context` with one decision hinge. Otherwise bound the assumption and finish the review.

## Verdict

Return only applicable fields:

- **Verdict:** `accept`, `revise`, `reject`, or `insufficient context`
- **Decisive reason**
- **Blocking findings**, limited to violated requirements or material lifecycle costs
- **Subtractions**
- **Required changes**, minimum needed for acceptance
- **Evidence gaps or deferred triggers**, only when material

Stop after the proposal is invalidated, simplified to sufficiency, or supported. Reopen settled decisions only for new material evidence, changed requirements, or a concrete defect; discovered security defects remain reviewable. Repeat review only on material corrections or new gaps, and remove duplicate or superseded tasks instead of adding another review round by default. Do not produce a generic risk catalogue, add optional improvements, or turn review findings into a larger design. “Production-ready,” “more testable,” and possible future growth are not evidence by themselves.
