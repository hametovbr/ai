# Full Architecture Decision Method

Read this only for a substantive, costly, or hard-to-reverse decision. It preserves the source skill's detailed gates, comparison criteria, lifecycle checks, red flags, and example.

## Workflow

### 1. Establish the context contract

Capture:

- decision, outcome, trigger, and observable success;
- verified requirements, invariants, scope, non-goals, and accepted manual work;
- current owners, writers, state, contracts, boundaries, deployment, support, and recovery paths;
- for every changed aggregate, the current path from source through transformations and result models to its canonical writer and emitted side effects;
- real scale, lifetime, team capability, operational ownership, and change constraints;
- native configuration, built-ins, extension points, managed tools, and local patterns;
- priority decisions, evidence, assumptions, and unknowns;
- readiness: `ready for synthesis` or `blocked`.

Inspect current code and configuration before designing. Treat live behavior as evidence; treat ADRs and documents as intent and flag drift. When scope or priorities change, invalidate affected conclusions instead of patching the old design around them.

### 2. Separate behavior, placement, packaging, and verification

For each required custom behavior, decide independently:

1. **Behavior:** essential domain logic.
2. **Placement:** the existing lifecycle owner that should execute it.
3. **Packaging:** configuration, embedded code, source file, plugin, module, image, service, or platform.
4. **Verification:** evidence that proves functional and lifecycle behavior.

Required logic does not imply a separate file, runtime, container, or service. Count every artifact and obligation: source and generated files, images, runtimes, volumes, credentials, manifests, builds, contracts, backups, restore steps, upgrades, and operator documentation.

#### Aggregate write-path gate

Apply this gate before adding a repository/storage method, another writer, or a domain service that mutates an existing aggregate:

1. Trace the current path: `source -> transformations/strategies -> result model -> canonical writer -> side effects`.
2. Name the aggregate, canonical writer, every existing alternative writer, and the lifecycle event each writer owns.
3. Check whether the existing result or command model can carry the new facts to the canonical writer. If it can, extend that model and preserve the writer.
4. Add another writer only when the canonical path cannot protect a verified invariant such as atomic claiming, isolation, or distinct lifecycle ownership. Record the invariant and evidence.
5. Keep calculation and mapping services value-returning by default. Place persistence and event publication in the established lifecycle owner.

If the current write path or ownership cannot be established, readiness is `blocked`; do not infer a new boundary from nearby class names.

#### Decision supersession cleanup gate

When verified scope or an architecture decision changes, treat the previous design as superseded rather than layering the new design over it:

1. Inventory artifacts justified by the superseded decision: code paths, writers, state/schema, migrations, contracts, flags/configuration, dependencies, tests/fixtures, observability, and documentation.
2. Classify each artifact as `retain`, `migrate`, or `remove`. `Retain` needs a current verified requirement; sunk cost, compatibility speculation, and possible future reuse do not qualify.
3. Remove obsolete runtime paths and tests of intermediate specifications. Rewrite verification around the final target behavior and invariants.
4. Preserve irreversible history safely: do not edit an applied migration; use a forward migration and an explicit rollout/removal step. Delete an unapplied branch-local artifact when nothing depends on it.
5. Do not approve the replacement architecture while obsolete writers, state, or contracts remain unexplained. If cleanup must be deferred, name its owner, safety boundary, trigger, and exit condition.

### 3. Find the lowest sufficient intervention

Move right only when the preceding option demonstrably fails a verified requirement or invariant:

`no change/manual handling → configuration → native feature/extension point → direct local change → bounded script/adapter → module → service → platform/migration`

Record the specific reason and evidence for rejecting each lower level. Verify exact native behavior and version; do not infer capability from a feature name.

Prefer:

- specific code over a generic framework;
- temporary duplication over the wrong abstraction;
- one implementation over a provider interface with one provider;
- one authoritative owner and deliberate writer for each fact;
- visible manual review for rare ambiguity over automation that guesses;
- stateless behavior without a cross-event requirement;
- reversible incremental change over a rewrite;
- a rewrite only when the current model is incompatible and migration is acceptably cheap.

### 4. Compare complete candidates

Audit assumptions before ranking. If an unverified assumption materially selects or eliminates a candidate, discard the ranking and return to the readiness gate.

Compare at most two materially different serious candidates. Include requirements and invariants, added and removed responsibilities, state, contracts, dependencies, artifacts, manual procedures, ownership, deployment, secrets, observability, recovery, upgrade, rollback, removal, and verification.

Prefer the lowest justified total lifecycle cost—not the fewest lines, boxes, or repository files.

### 5. Challenge the preferred candidate

Try to invalidate it before strengthening it:

- For every component, state store, abstraction, deployment unit, credential, build step, retry, fallback, and procedure, ask: **Which verified requirement or invariant fails if this is removed?**
- For every new aggregate writer or persistence method, ask: **Why can the existing result model and canonical writer not carry this change?** Reject the new writer when no verified invariant answers this.
- For every artifact inherited from a superseded decision, ask: **Which current verified requirement fails if this is removed?** Remove it or record a bounded migration when none does.
- Walk one concrete path through deployment, normal operation, invalid input, partial failure, diagnosis, recovery, upgrade, rollback, removal, and ownership transfer where applicable.
- For each reliability mechanism, name the failure, detection signal, containment boundary, recovery action, and residual loss.
- Separate system verification from developer convenience.

Remove unsupported machinery. Stop when the candidate is invalidated or sufficiently supported; do not produce a catalogue of hypothetical risks.

## Complexity gate

Before adding an abstraction, interface, state, queue, service, broker, plugin system, telemetry, configuration, compatibility layer, migration framework, persistence method, or aggregate writer, answer:

> What observed defect, verified requirement, explicit invariant, or credible material failure cannot be handled sufficiently well without this element?

Add it only when its benefit exceeds implementation, cognitive, operational, migration, and carrying costs. Future possibility, elegance, generic “best practice,” and “we may need flexibility” do not pass.

## Principles and priorities

When qualities conflict, use this default order unless the user overrides it:

1. Correctness, data safety, and runtime reliability.
2. Deployment, rollback, recovery, observability, and security.
3. Operation, support, upgrades, compatibility, and operator burden.
4. Developer-local testability, implementation speed, and authoring convenience.

- **KISS:** Minimize total lifecycle concepts, not merely lines or components.
- **YAGNI:** Do not build presumptive capabilities; preserve cheap options with clear boundaries, tests, and observable evolution triggers.
- **DRY:** Deduplicate knowledge, not every repeated expression. Use the Rule of Three unless an external standard already defines the abstraction.
- **Surgical changes:** Every changed line and artifact must trace to the goal. Remove obsolete machinery when scope narrows.
- **Evidence:** Verify semantics with current configuration, code, tests, logs, primary documentation, dry runs, canaries, or recovery exercises.
- **Proportionate safety:** Add idempotency, atomicity, retries, quarantine, compatibility, and observability only for identified failures or invariants.

## Output contract

Lead with the outcome.

If readiness is blocked, return:

- **Readiness:** `blocked`.
- **Verified context.**
- **Decision hinge:** why the unknown changes the architecture.
- **Next action:** one question or research step.

For a small ready decision, return **Verdict**, **Reason**, **Boundary**, and the narrowest verification.

For a substantive ready decision, return:

1. Decision, scope, verified context, and priorities.
2. Smallest complete architecture.
3. Lifecycle and artifact delta, including canonical-writer and side-effect changes plus artifacts retained, migrated, and removed from superseded decisions.
4. Strongest rejected alternative and decisive reason.
5. Failure, recovery, upgrade, rollback, and removal handling.
6. Evidence, residual uncertainty, verification, and measurable evolution triggers.

Use an ADR only when the decision is costly to reverse, affects multiple owners, changes data ownership, introduces a durable dependency or contract, or rests on assumptions that require later revalidation.

## Red flags

Stop and simplify or return to context gathering when:

- architecture is emerging incrementally during coding without an explicit pre-implementation decision;
- a complex implementation plan, agent workflow, automation, test harness, or research platform is treated as “not architecture”;
- architecture review is deferred until after modules, state, contracts, or recovery machinery already exist;
- a material assumption selects the architecture;
- research begins after a candidate is chosen;
- a single-use abstraction or one-provider interface appears;
- required behavior is automatically externalized into a runtime or service;
- persistence exists without a current state requirement;
- a mapping or calculation service writes an aggregate already owned by the surrounding lifecycle;
- one flow can update the same aggregate through multiple writers or duplicate its domain-event publication without a verified invariant;
- a replacement design is added while obsolete state, writers, contracts, flags, dependencies, or intermediate-specification tests remain without a current requirement or migration exit;
- configuration or extensibility has no current consumer;
- “more testable” justifies another deployment unit without lifecycle evidence;
- “one component” hides images, credentials, builds, backups, or upgrade paths;
- reliability machinery lacks a named failure and inadequate existing recovery;
- rare ambiguity is automated by guessing;
- adjacent cleanup or retained sunk cost expands the change;
- review adds more machinery than it removes.

Do not add health endpoints, request IDs, telemetry, containers, graceful shutdown, load tests, or similar operational machinery merely because they are common. Require an existing convention or a current scale, SLA, invariant, or failure mode.

## Example

If a proposed classifier service adds a queue, container, credentials, and retries while the consequence of one misclassification and ownership of ambiguous cases are unknown, do not choose the service or a local module yet. Return `blocked`: those unknowns determine the required correctness, recovery, and ownership boundaries. Resolve them first; then start at manual handling or the existing platform’s native extension point and escalate only with evidence.
