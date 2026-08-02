---
name: making-pragmatic-architecture-decisions
description: Use when selecting, designing, reviewing, simplifying, or revising software and system architecture, including integrations, migrations, deployment shapes, automation boundaries, build-versus-buy choices, and responses to narrowed requirements.
---

# Making Pragmatic Architecture Decisions

## Core rule

Design the smallest complete system that satisfies verified requirements and protects explicit invariants across development, deployment, operation, support, recovery, upgrade, and removal.

Context collection precedes synthesis. Operational reliability and lifecycle simplicity take priority over implementation convenience unless the user explicitly chooses otherwise.

Assume the first proposal has positive complexity bias. Treat it as a candidate, not a baseline.

## Required skill sequence

1. **REQUIRED SUB-SKILL:** Use `gathering-architecture-context` before generating or selecting candidates.
2. Synthesize and compare only after its context contract is `ready for synthesis`.
3. **REQUIRED SUB-SKILL:** Use `challenging-architecture-decisions` on the preferred candidate before approval or implementation.

If the context contract is `blocked`, return it with its decision hinge and next single action. Express the hinge as the unresolved required guarantee or acceptance criterion, without mapping answers to candidates or conditionally eliminating technologies. Do not include a preferred, provisional, conservative, default, reversible, or conditional candidate. These labels do not bypass the readiness gate.

If a required sub-skill is unavailable, execute its installed workflow from the resolved personal skill rather than silently skipping the phase. If it cannot be resolved, report the missing gate and do not claim the architecture is complete.

## Lifecycle priority

Use this default order when qualities conflict:

1. Correctness, data safety, and runtime reliability.
2. Deployment, rollback, recovery, observability, and security.
3. Routine operation, support, upgrades, compatibility, and operator burden.
4. Development testability, implementation speed, and authoring convenience.

Testing that proves runtime behavior, deployment safety, recovery, compatibility, and upgrade correctness belongs to the higher lifecycle levels. Only developer-local convenience is lower priority.

Read [principles.md](references/principles.md) for substantive reviews or when principles conflict.

## Architecture workflow

### 1. Establish the context contract

Do not discuss a preferred topology before context gathering completes. Require verified:

- objective, trigger, invariants, success criteria, scope, non-goals, and accepted manual work;
- current components, owners, writers, state, contracts, deployment, support, and recovery paths;
- real scale, lifetime, team capability, operational ownership, and change constraints;
- native configuration, built-ins, embedded scripting, plugins, managed tools, and local patterns;
- current official capabilities and maintained examples of similar solutions;
- explicit priority decisions and material unknowns.

Research discoverable facts. Ask the user one material decision at a time. When scope or priorities change, invalidate affected conclusions and rebuild the context contract instead of patching the old design.

### 2. Separate behavior, placement, and packaging

For every required custom behavior, decide separately:

1. **Behavior:** what domain logic is essential.
2. **Placement:** which existing lifecycle owner should execute it.
3. **Packaging:** configuration, embedded code, source file, plugin, image, module, service, or platform.
4. **Verification:** how correctness and lifecycle behavior are proved.

Never infer placement from behavior. “A matcher is required” does not imply “a separate script or runtime is required.”

Count all deployable and support artifacts: source files, generated exports, images, runtimes, volumes, plugins, credentials, manifests, build steps, backups, restore procedures, version coupling, and operator documentation.

### 3. Find the lowest sufficient intervention

Evaluate in this order and stop at the first level that satisfies the full lifecycle:

1. no change or accepted manual handling;
2. configuration;
3. native feature or embedded extension point;
4. direct local change;
5. bounded script or adapter inside the existing lifecycle;
6. module;
7. new service;
8. platform or migration.

For each rejected lower level, record the specific unmet requirement or invariant and the evidence. Do not reject a built-in by name alone; verify its exact behavior and version.

Keep ambiguous low-frequency cases manual when deterministic automation would guess. Preserve one authoritative owner for each fact and one deliberate writer where concurrency threatens invariants.

### 4. Compare complete candidates

First audit the assumptions used to rank candidates. If an unverified assumption materially selects or eliminates one, discard the ranking and return to context gathering.

Compare only serious candidates. For each, record:

- requirements and invariants satisfied or missed;
- added and removed responsibilities, state, contracts, dependencies, artifacts, and manual procedures;
- deployment, configuration, secrets, observability, recovery, upgrade, rollback, and removal path;
- operator and ownership burden;
- evidence quality and unresolved assumptions;
- development and system-level verification.

Prefer the candidate with the lowest justified lifecycle cost, not the fewest boxes or lines. A large embedded function may be operationally simpler than an external runtime; a source file may be more maintainable when code changes often or has multiple consumers. Let verified context decide.

### 5. Add proportional safety

Name concrete failures before adding timeouts, retries, idempotency, staging, manifests, queues, fallbacks, observability, compatibility, or rollback machinery.

For each applicable failure, define detection, containment, recovery, and residual loss. Fail visibly and quarantine ambiguity when silent continuation could lose or corrupt data. Keep partial state invisible when atomic publication protects an invariant.

Use measured evidence before claiming success. Configuration, code, tests, logs, dry runs, canaries, recovery exercises, and observed behavior outrank design intent.

### 6. Challenge and finalize

Run `challenging-architecture-decisions` with the context contract, preferred candidate, alternatives, and evidence.

- `insufficient context` → return to context gathering.
- `reject` → discard the candidate; do not patch it around a structural failure.
- `revise` → make only required changes, then repeat the targeted challenge.
- `accept` → finalize the decision.

Do not begin implementation until the review accepts the design or the user explicitly accepts named residual gaps.

## Decision output

Scale the output to the decision.

For a small, reversible, single-owner decision, return:

- **Verdict**
- **Reason**
- **Boundary**
- one targeted verification or failure note when needed

For a substantive decision, return:

- **Decision and scope**
- **Verified context and priorities**
- **Minimum architecture**
- **Lifecycle/artifact delta**
- **Strongest rejected alternatives**
- **Failure, recovery, upgrade, and rollback handling**
- **Evidence and verification**
- **Residual assumptions and evolution triggers**

Use an ADR only when the decision is costly to reverse, affects multiple owners, changes data ownership, introduces a durable dependency or contract, or relies on assumptions that must be revisited.

## Mandatory stop checks

- Stop synthesis when a material context item is unknown.
- Stop and remove any candidate ranking derived from a material assumption; conditional selection is still selection.
- Stop escalation when an existing owner or extension point is sufficient.
- Stop adding elements that do not map to a verified requirement, invariant, or material failure.
- Stop automating rare ambiguity when visible manual review is cheaper and safer.
- Stop carrying components retained only by sunk cost or an earlier scope.
- Stop implementation when adversarial review has a blocking finding.
- Stop refining once the accepted candidate satisfies the context contract.

## Red flags

- Research begins after a candidate is chosen.
- Generic architecture patterns substitute for current-system inspection.
- Development testability justifies another deployment unit without lifecycle evidence.
- A logical responsibility is automatically externalized into a file, runtime, image, or service.
- Native capabilities are assumed absent or accepted without semantic verification.
- “One component” hides multiple artifacts, credentials, builds, backups, or upgrade paths.
- Reliability machinery lacks a named failure and inadequate existing recovery.
- A scope change disables old machinery instead of deleting its cost.
- Review adds more components than it removes.
