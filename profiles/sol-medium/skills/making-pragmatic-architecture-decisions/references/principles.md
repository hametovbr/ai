# Architecture principles and decision lenses

Use this reference to resolve trade-offs. Do not maximize any principle independently.

## Table of contents

- [Foundational model](#foundational-model)
- [Context before synthesis](#context-before-synthesis)
- [LLM complexity bias](#llm-complexity-bias)
- [Core simplicity principles](#core-simplicity-principles)
- [Boundaries and dependencies](#boundaries-and-dependencies)
- [Evolution and reversibility](#evolution-and-reversibility)
- [Reliability and data safety](#reliability-and-data-safety)
- [Operational and human cost](#operational-and-human-cost)
- [Decision traps](#decision-traps)
- [Complexity escalation ladder](#complexity-escalation-ladder)
- [Architecture review checklist](#architecture-review-checklist)

## Foundational model

Architecture allocates responsibilities, state, authority, dependencies, and failure. Evaluate it through four views:

1. **Functional:** Does it deliver the verified outcome?
2. **Structural:** Are responsibilities cohesive and dependencies intentional?
3. **Operational:** Can it be deployed, observed, repaired, secured, and upgraded predictably?
4. **Evolutionary:** Can likely changes occur without premature infrastructure or irreversible migration?

Distinguish:

- **Essential complexity:** imposed by real domain rules, safety, scale, regulation, consistency, or integration constraints.
- **Accidental complexity:** introduced by tools, duplicated ownership, unnecessary distribution, generic abstractions, speculative flexibility, or mismatched processes.

Remove accidental complexity. Preserve essential complexity explicitly instead of hiding it.

## Context before synthesis

Architecture begins by reducing uncertainty, not generating candidates. Establish the actual objective, invariants, current owners, lifecycle, native capabilities, operational constraints, and accepted manual work before selecting patterns or technologies.

Separate:

- verified facts from source code, configuration, measurements, and authoritative documentation;
- user decisions and priority choices;
- assumptions that can be tested;
- unknowns that can materially change the design.

Research discoverable facts instead of asking the user. Ask one material decision at a time. A context phase is complete only when remaining unknowns cannot change system boundaries, safety, technology choice, operational responsibility, or acceptance criteria.

When the objective or constraints change, invalidate dependent conclusions. Do not preserve a topology merely because it was already designed or implemented.

## LLM complexity bias

Treat the initial generated proposal as a candidate, not a neutral baseline. Coding agents frequently produce plausible additions that are locally defensible but globally unnecessary:

- requirements inferred from generic “production quality” rather than the stated goal;
- defensive branches for increasingly remote possibilities;
- helpers, interfaces, factories, and compatibility layers for one current case;
- manifests, hashes, staging, retries, dry runs, wrappers, containers, services, or dashboards added without a required failure mode;
- adjacent cleanup or refactoring presented as part of the requested change;
- process disproportionate to scope, such as full ADRs, multi-agent decomposition, exhaustive test matrices, or repeated review loops for disposable or low-risk work.

Correct this bias with a subtraction pass. Trace every addition to a verified requirement, explicit invariant, observed failure, or mandatory external constraint. If removing an element does not cause one of those to fail, exclude it from the minimum architecture.

Do not replace this with a line-count target. Short code can hide unsafe behavior, while justified reliability may require state and coordination. The correction target is unsupported complexity, not complexity itself.

### Rationalization tests

| Claim | Required evidence |
|---|---|
| “It is safer or more robust” | Named failure, credible path, material impact, and why existing recovery is insufficient |
| “It is standard practice” | A current constraint or invariant that the practice protects |
| “It improves maintainability” | A present change axis, repeated change, or ownership boundary |
| “It is future-proof” | Put the condition in an evolution trigger; do not implement it now |
| “It is optional” | Exclude it from the minimum recommendation |
| “The full process is more rigorous” | Decision risk and reversibility justify its cost |

### Proportional review depth

| Decision shape | Required treatment |
|---|---|
| Local, reversible, one owner, no new state or contract | Verdict, minimal change, preserved boundary, targeted verification |
| Bounded script, adapter, or module with material failure behavior | Scope, minimal flow, concrete failure handling, rejected escalation |
| New state, service, cross-owner contract, difficult rollback, or high-consequence invariant | Full complexity ledger, lifecycle review, migration, rollback, and ADR when applicable |

## Core simplicity principles

### KISS

Minimize total lifecycle complexity, not local code length or container count.

Include implementation, deployment, state, observability, recovery, upgrades, security, documentation, and human coordination. A bounded script can be simpler than a new service. A managed platform can be simpler than several fragile scripts when it removes proven operational burden.

When trade-offs are otherwise comparable, prioritize runtime reliability, deployment, recovery, operation, support, and upgrades over development convenience. Count packaging and placement independently from the required logic: embedded code, mounted source, a derived image, a plugin, and a service can implement the same behavior while creating very different lifecycle costs.

Reject both premature distribution and an oversized monolith that hides unrelated ownership or failure domains.

### YAGNI

Do not implement capabilities justified only by hypothetical future requirements.

Preserve cheap options through clear boundaries, compatible schemas, tests, and documented extraction triggers. YAGNI does not permit ignoring known security, recovery, regulatory, capacity, or compatibility requirements.

When requirements narrow, remove no-longer-required processing and infrastructure. Do not merely disable it while retaining its operational cost.

### DRY

Remove duplicated knowledge, not superficial textual similarity.

Keep similar implementations separate when their policies, owners, rates of change, failure semantics, or audit rules differ. Extract only stable, demonstrably identical behavior. Prefer small pure utilities over a generic framework. Wait for repeated change or a third concrete use case before introducing a broad abstraction.

### Rule of Three

Treat two similar cases as evidence to observe, not proof of a general model. Generalize after repeated concrete use reveals the stable axis of variation. Override this only when an external standard or protocol already defines the abstraction.

### Least power and boring technology

Choose the least expressive mechanism that safely solves the problem: data before code, configuration before orchestration, a function before a framework, a module before a distributed service. Prefer mature technology when novelty provides no requirement-level advantage.

### Gall's law

Build a working simple system and evolve it. Do not design a complex working system from an untested blank slate. Preserve seams for extraction without pre-building the extracted topology.

## Boundaries and dependencies

### Single responsibility

Give a component one coherent reason to change. Do not equate responsibility with a single function or tiny service. Split only when change drivers, ownership, deployment, scaling, security, or failure isolation differ materially.

### Separation of concerns

Separate policy from mechanism and domain decisions from infrastructure details. Do not create a network boundary merely to demonstrate separation; modules and interfaces often provide the required boundary more cheaply.

### Cohesion and coupling

Keep behavior that changes together close. Minimize temporal, data, deployment, and organizational coupling. Network calls, shared databases, shared release trains, and cross-team approvals are coupling even when source code is separated.

### Information hiding

Expose stable intent and hide volatile implementation details. Prefer an existing extension point carrying authoritative metadata over reconstructing that metadata from filenames, logs, or duplicated inference.

### Dependency inversion

Place interfaces at proven volatility or ownership boundaries. Do not add interfaces, factories, adapters, or dependency injection solely for formal compliance when no alternate implementation or test seam is needed.

### Open/closed principle

Design for extension only along demonstrated axes of variation. A generic plugin system for one implementation is speculative complexity. A narrow adapter at an existing extension point is justified when it isolates a current integration.

### Data ownership and single writer

Assign one authoritative owner for every fact. Avoid shared writable databases and competing importers unless concurrency and conflict rules are explicit. Multiple readers are cheap; multiple writers multiply consistency and recovery complexity.

## Evolution and reversibility

### Reversible decisions

Prefer additive schemas, feature flags, adapters, dual-read validation, isolated root paths, dry runs, canaries, and atomic publication. Delay irreversible migrations until evidence makes their benefits exceed transition risk.

### Evolutionary architecture

Attach measurable fitness functions to important qualities: latency, failure rate, data-loss count, deployment frequency, recovery time, resource saturation, or manual intervention rate. Let observed threshold violations trigger architectural change.

### Compatibility

Preserve backward compatibility when consumers cannot migrate atomically. Make contract, schema, file-format, and API evolution explicit. Add integration tests around the compatibility boundary.

### Migration cost

Count coexistence, data conversion, rollback, retraining, temporary duplication, validation, cutover, and post-migration support. A cleaner target does not justify migration when the current defect has a bounded local repair.

## Reliability and data safety

### Explicit invariants

State what must never happen: data loss, duplicate payment, silent media omission, unauthorized access, invalid state transition. Let invariants determine required complexity.

### Idempotency

Make retries safe at boundaries where operations can repeat. Define the idempotency key, stored result, collision behavior, and retention. Do not add idempotency machinery where operations cannot repeat or side effects are harmless.

### Atomicity

Publish complete state or no state. Use temporary paths, transactions, compare-and-swap, or atomic rename as appropriate. Keep partial results invisible to downstream consumers.

### Fail fast, fail closed, and quarantine

- Fail fast on invalid configuration and broken invariants.
- Fail closed when continuing risks loss, corruption, security exposure, or incorrect financial action.
- Quarantine ambiguous inputs when manual resolution is safer than guessing.
- Permit best-effort continuation only when partial success is explicitly acceptable and observable.

### Observability

Require evidence sufficient to distinguish success, partial success, retries, ambiguity, and data loss. Logs alone are insufficient when metrics, traces, audit records, or reconciliation are needed. Verify behavior after rollout before declaring the decision successful.

### Blast radius and isolation

Introduce process or service isolation only when an actual failure domain, security boundary, scaling profile, or ownership boundary requires it. Distribution creates new failure modes; it does not automatically create resilience.

### Resilience mechanisms

Use timeouts, bounded retries, backoff, circuit breakers, bulkheads, backpressure, dead-letter handling, and reconciliation only against identified failure modes. Every retry policy must address duplication and retry storms.

## Operational and human cost

Count all of the following in a complexity ledger:

- runtime processes and deployment units;
- databases, queues, caches, object stores, and schemas;
- control planes, workers, schedulers, and external relays;
- credentials, backups, restores, migrations, and upgrade paths;
- dashboards, alerts, logs, runbooks, and on-call procedures;
- APIs, events, files, and versioned contracts;
- teams, approvals, handoffs, ownership transfers, and specialist knowledge;
- manual review, correction, and exception workflows.

### Manual versus automated

Manual work is acceptable when frequency, duration, risk, and variability are low. Automate when repeated manual cost and error risk exceed the lifetime cost of building, observing, repairing, and evolving the automation.

Prefer human-in-the-loop handling for rare ambiguous cases. Do not force deterministic automation to guess semantic intent.

### Build versus buy or reuse

Evaluate existing extension points, configured features, libraries, OSS services, managed services, and custom code. Compare fit, state ownership, lock-in, maintenance, migration, failure behavior, and unused capability. Feature count is not architectural fit.

Before externalizing custom behavior, inventory native configuration, embedded scripting, plugins, managed binaries, export/import behavior, secret injection, and existing lifecycle hooks. Verify exact semantics and versions. A logical responsibility does not determine its deployment shape.

## Decision traps

### Premature abstraction

Symptoms: generic names, conditional frameworks, DSLs, plugin systems, or shared services before stable common behavior exists. Keep concrete implementations and extract verified commonality.

### Premature distribution

Symptoms: queues, service discovery, schemas, separate databases, and orchestration introduced for hypothetical scale or visual modularity. Use in-process boundaries until independent lifecycle requirements are proven.

### Platform replacement bias

Do not replace a working stack because a new platform has a unified interface. Expand the dependency inventory: one application may conceal a database, relay, workers, migration, and less mature importer.

### Automation bias

Do not equate full automation with correctness. Rare ambiguous inputs often require visible quarantine and manual resolution.

### Sunk-cost fallacy

Past implementation or migration effort does not increase future value. Compare only future cost, risk, and benefit.

### Novelty and fashion bias

Modernity, popularity, microservices, event-driven design, Kubernetes, AI, or a new database are not requirements. Demand a current problem that the technology solves better than the lower-complexity alternative.

### Compromise architecture

Reject middle options that retain most operational costs of a complex design while omitting its isolation, scale, or ownership benefits.

### Local optimization

A locally elegant component can make the system worse through extra state, duplicated authority, or coordination. Review topology and lifecycle, not only source-code quality.

### Principle cargo cult

Do not use KISS to omit safety, YAGNI to ignore known requirements, DRY to merge distinct policies, SRP to create nanoservices, or decoupling to justify asynchronous integration without delivery semantics.

## Complexity escalation ladder

Choose the first level that satisfies the current requirement and invariants:

| Level | Use when | Escalate when |
|---|---|---|
| Configuration | Existing behavior only needs selection or parameters | Custom deterministic behavior is required |
| Script or adapter | Bounded transformation or integration fits one existing lifecycle | Logic becomes shared, stateful, or independently owned |
| Module | Cohesive domain behavior shares deployment and scaling | Independent lifecycle or isolation becomes measurable |
| Service | Independent deployment, ownership, scaling, security, or failure boundary is required | Multiple services need common platform capabilities |
| Platform | Repeated cross-service needs justify shared control and operations | Do not escalate speculatively |

A new service normally requires several aligned signals: stable contract, clear owner, independent lifecycle, explicit data ownership, failure isolation, operational capacity, and measured need.

## Architecture review checklist

### Scope

- What exact outcome is required now?
- What must never happen?
- What is explicitly out of scope?
- Which manual steps are accepted?
- Which facts are measured, and which are assumptions?
- What should be removed because scope narrowed?

### Current system

- Where is authoritative data and semantic knowledge already located?
- Which extension point can carry the change?
- Who writes each piece of state?
- Which existing component already owns the lifecycle?
- What are the current failure and operational boundaries?
- Which native configuration, built-ins, embedded extension points, managed tools, and maintained local examples exist?
- Which facts come from live behavior, which from historical intent, and where do they disagree?

### Proposed system

- Which responsibilities, stateful dependencies, contracts, and deployment units are added or removed?
- Does each new component solve a verified requirement?
- Which current requirement fails if each proposed abstraction, safety mechanism, or process step is removed?
- Has the proposal invented an invariant or treated a theoretical edge case as a requirement?
- Is policy duplicated or merely code?
- Can the same result be achieved one escalation level lower?
- Has behavior been separated from placement and packaging?
- Which source files, exports, images, runtimes, volumes, plugins, credentials, build steps, backup surfaces, and upgrade couplings are added?
- How does the change affect neighboring systems and owners?

### Safety and change

- What happens on retry, partial failure, ambiguity, collision, and rollback?
- Is publication atomic and processing idempotent where necessary?
- What evidence proves correct behavior?
- Can rollout be canaried or dry-run?
- How is the system deployed, diagnosed, recovered, upgraded, rolled back, removed, and transferred to another operator?
- Which measurable trigger justifies future extraction or migration?
