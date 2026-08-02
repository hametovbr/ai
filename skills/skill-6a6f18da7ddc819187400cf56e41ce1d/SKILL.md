---
name: gathering-architecture-context
description: Use when a system design, integration, migration, platform choice, or technical plan is not yet grounded in verified requirements, current-system behavior, native capabilities, comparable prior art, and operational constraints.
---

# Gathering Architecture Context

## Core rule

Build a verified context contract before synthesizing architecture. Research discoverable facts; ask the user only for decisions, preferences, unavailable facts, and boundary conditions that can materially change the design.

Do not propose components, select technology, write a plan, or implement while a material context gap remains.

## Hard gate for material unknowns

When any unresolved fact or user decision could change a readiness criterion below:

- set **Readiness** to `blocked`;
- do not name, rank, recommend, default to, or conditionally select a candidate;
- do not draft or approve an ADR, authorize production use, or begin implementation;
- return the verified context, the decision hinge, and one next question or research action.

Calling a choice provisional, conservative, reversible, exploratory, or “not yet production-approved” does not make it context gathering. A conditional recommendation is still synthesis. Deadline, authority pressure, sunk cost, and a desire to preserve momentum do not waive this gate.

State a blocked decision hinge in this form: **the unknown determines a required guarantee, boundary, ownership rule, or acceptance criterion**. Do not map possible answers to named candidates, conditionally eliminate technologies, or outline branching architectures. Candidate names may appear only when restating what decision is blocked.

Use a conservative assumption only when being wrong cannot materially change boundaries, safety, ownership, technology choice, lifecycle ranking, or acceptance. Otherwise keep the item unknown and stop.

## Priority model

Treat architecture as the complete operating lifecycle. Unless the user explicitly overrides it, rank concerns in this order:

1. Correctness, data safety, and runtime reliability.
2. Deployment, rollback, recovery, observability, and security.
3. Routine operation, support, upgrades, compatibility, and operator burden.
4. Development testability, implementation speed, and authoring convenience.

Do not confuse development convenience with system testability. Verification in deployment, recovery rehearsal, and observable runtime behavior belong to the higher operational priorities.

Count packaging as architecture: source files, generated artifacts, images, runtimes, plugins, volumes, credentials, configuration, build steps, backup surfaces, and upgrade coupling.

## Workflow

### 1. Frame the decision

Extract what is already known. Establish:

- exact outcome and trigger;
- invariants and unacceptable outcomes;
- measurable success;
- scope, non-goals, and accepted manual work;
- likely lifetime, scale, reversibility, and decision deadline;
- who deploys, operates, supports, upgrades, and recovers the system;
- user priorities when lifecycle qualities conflict.

Label each statement as **verified fact**, **user decision**, **assumption**, or **unknown**. Never promote an assumption into a requirement.

### 2. Inspect the current system

Read directly mentioned artifacts fully before decomposing the research. Inspect only relevant:

- code, configuration, manifests, schemas, APIs, ADRs, runbooks, and recent changes;
- topology, data flow, state, authoritative owners, writers, and integration boundaries;
- deployment, upgrade, backup, restore, incident, and manual exception workflows;
- existing modules, scripts, plugins, embedded functions, managed tools, and extension points;
- logs, incidents, tests, and measurements that reveal actual behavior.

Treat live code and configuration as the primary description of current behavior. Treat ADRs and historical documents as intent and history; flag drift instead of silently choosing one source.

Document what exists before evaluating what should change.

### 3. Research available solutions

Research before inventing. Check, in order:

1. no change and accepted manual handling;
2. existing configuration;
3. native feature or embedded extension point;
4. established local pattern;
5. official platform or framework capability;
6. mature external component;
7. custom code or new deployment unit.

For current, niche, uncertain, or explicitly researched topics, use current primary sources. Search official documentation, source code, release notes, issue trackers, and maintained real examples. Use community reports to identify failure modes, not as sole proof of capability.

Verify exact semantics that affect the decision. Do not infer support from a feature name. Record source, version/date, demonstrated behavior, and remaining uncertainty.

### 4. Resolve gaps with the user

Look up discoverable facts instead of asking for them. Ask one material question at a time, building on prior answers. Include:

- why the answer changes the architecture;
- 2–3 concrete choices when possible;
- a recommended answer with its trade-off.

Do not ask questions already answered by visible context. Do not conduct an exhaustive interview for immaterial edge cases. If a missing answer would not change topology, safety, or lifecycle cost, state a conservative assumption and continue.

### 5. Produce the context contract

Return this compact artifact:

- **Decision:** what must be decided now.
- **Outcome and trigger:** why the decision exists.
- **Verified requirements:** functional and lifecycle requirements.
- **Invariants:** what must never happen.
- **Scope:** included work, non-goals, accepted manual handling.
- **Priority order:** explicit trade-off ordering.
- **Current system:** owners, state, writers, boundaries, deployment and support model.
- **Native capability inventory:** configuration, built-ins, extension points, managed tools, packaging options.
- **Evidence and prior art:** authoritative sources, local examples, measured behavior, relevant incidents.
- **Assumptions and unknowns:** with impact if wrong.
- **Readiness:** `ready for synthesis` or `blocked`, with the next single question or research action.

Before marking `ready for synthesis`, perform an assumption audit: list every assumption used to prefer or eliminate a candidate. If an unverified assumption materially determines that ranking, discard the ranking and return `blocked`.

## Readiness gate

Mark the contract ready only when no unresolved item could materially change:

- system boundaries or deployment units;
- data ownership, consistency, or safety;
- operational responsibility or recovery;
- technology or integration choice;
- lifecycle cost ranking;
- acceptance criteria.

When scope or priorities change, invalidate affected conclusions and refresh the contract. Do not patch the previous design around a changed objective.

## Common failures

| Failure | Correction |
|---|---|
| Start from a familiar pattern | Start from current owners, invariants, and evidence. |
| Ask the user for searchable facts | Research them and ask only for decisions or inaccessible context. |
| List built-ins without checking semantics | Verify the exact behavior and version. |
| Treat custom logic as an external component | Separate required logic from its placement and packaging. |
| Optimize for easy unit tests | Compare the full deployment, support, recovery, and upgrade lifecycle first. |
| Research only products, not examples | Find maintained implementations and documented failure reports. |
| Keep designing after a material unknown appears | Stop synthesis and resolve the unknown. |
| “Conditionally choose” under a conservative assumption | A material assumption cannot select architecture. Return `blocked` and resolve the decision hinge. |

## Regression example

Unknown: the consequence of losing one event may determine whether transactional coupling is required.

- Wrong: “Conditionally choose an outbox assuming loss is unacceptable; delay production approval.”
- Correct: “Readiness is blocked. The consequence of one lost event determines the required consistency guarantee. Obtain the accountable owner’s answer before comparing candidates.”
