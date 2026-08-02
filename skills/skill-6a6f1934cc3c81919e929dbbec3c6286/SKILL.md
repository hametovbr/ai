---
name: challenging-architecture-decisions
description: Use when a proposed architecture, ADR, integration, migration, platform choice, or implementation plan needs an independent stress test before approval or implementation.
---

# Challenging Architecture Decisions

## Core rule

Try to invalidate the preferred design before strengthening it. Challenge the problem framing, evidence, boundaries, lifecycle, and necessity of every addition. Do not reward sunk cost or defend the author’s rationale.

Use the confirmed context contract as the test oracle. If it is missing or stale, stop and use `gathering-architecture-context` before reviewing.

## Review sequence

### 1. Reconstruct the claim

State in compact form:

- the decision and selected candidate;
- requirements and invariants it claims to satisfy;
- operating model and lifecycle priorities;
- assumptions on which it depends.

Flag any candidate behavior that is absent from the context contract. Do not let the proposal silently create requirements.

### 2. Attack the framing

Test whether:

- the stated problem is the actual problem;
- no change, configuration, or accepted manual work already satisfies it;
- the scope has drifted since context gathering;
- the design optimizes a proxy such as code elegance, development testability, component count, or feature breadth instead of the required outcome;
- facts, user decisions, assumptions, and theoretical possibilities remain distinguishable.

Research a disputed fact before asking the user. Ask one question only when the answer is a material user decision or unavailable boundary condition.

### 3. Run the subtraction and native-capability tests

For every component, deployment unit, state store, abstraction, script, artifact, credential, build step, compatibility layer, retry, fallback, staging area, manifest, and manual procedure, ask:

> Which verified requirement or invariant fails if this is removed?

Remove anything without a concrete answer.

Verify that the candidate considered:

1. no change or manual exception handling;
2. configuration;
3. native feature or embedded extension point;
4. direct local change;
5. existing module, script, or adapter;
6. new service or platform.

Reject escalation when a lower level is sufficient across the full lifecycle.

### 4. Simulate the lifecycle

Walk one concrete path through each applicable stage:

- install and initial deployment;
- configuration and secret rotation;
- normal operation and observability;
- invalid input, partial failure, retry, and concurrency;
- operator diagnosis and manual recovery;
- backup and restore;
- upgrade of the host platform and dependencies;
- rollback or removal;
- ownership transfer and routine modification.

Test system verification separately from development convenience. A design that is easy to unit-test but difficult to deploy, observe, recover, support, or upgrade is not maintainable.

Name the specific failure, detection signal, containment boundary, recovery action, and residual loss. Do not demand resilience machinery without a credible material failure.

### 5. Check evidence and change

Verify claims against current configuration, code, tests, logs, official documentation, source, and maintained examples. Mark inference explicitly. Treat a feature name or design intent as unproven until its relevant semantics are demonstrated.

Identify:

- evidence required before rollout;
- cheapest safe canary or dry run;
- rollback boundary;
- measurable triggers for future complexity;
- assumptions that require an ADR or later revalidation.

## Verdict contract

Return:

- **Verdict:** `accept`, `revise`, `reject`, or `insufficient context`.
- **Decisive reason:** the strongest evidence-backed reason.
- **Blocking findings:** only issues that violate a requirement, invariant, or lifecycle priority.
- **Subtractions:** elements that can be removed now.
- **Evidence gaps:** claims still requiring verification.
- **Required changes:** minimum changes needed for acceptance.
- **Deferred triggers:** conditions that justify later complexity, not work to implement now.

Do not produce a long catalogue of hypothetical risks. Rank findings by impact on correctness, data safety, deployment, recovery, support, and upgrades. Stop when the candidate is either invalidated or sufficiently supported.

## Red flags

- The preferred design is treated as the baseline instead of one candidate.
- “More testable” justifies another runtime or deployment unit without lifecycle evidence.
- Existing platform capabilities are listed but not verified.
- A large code block is called “one component” while its image, runtime, mounts, secrets, and upgrades are ignored.
- Reliability mechanisms are added without a named failure and recovery gap.
- Rare ambiguity is automated by guessing instead of visible quarantine.
- Review findings add more machinery than they remove.
