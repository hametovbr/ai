---
name: making-architecture-decisions
description: Use when selecting or revising a substantive software architecture that changes durable state, ownership, contracts, deployment units, aggregate writers, migration, recovery, or other costly system boundaries. Use the pragmatic architecture skill for smaller reversible boundary choices.
---

# Making Architecture Decisions

Choose the smallest complete architecture that satisfies verified requirements and protects explicit invariants across its lifecycle.

## Route by decision shape

- For a local, reversible, single-owner choice with no new durable state, contract, deployment unit, migration, or recovery duty, use `making-pragmatic-architecture-decisions`.
- For fact-finding only, or when one missing current-system fact could change the boundary, use `gathering-architecture-context`.
- For stress-testing an existing proposal, use `challenging-architecture-decisions`.
- Continue here for a substantive architecture selection or revision.

Do not turn architecture review into a mandatory ceremony for a local implementation detail. Re-enter this workflow when verified scope, invariants, ownership, or authority changes materially.

## Readiness gate

Classify material context as verified fact, user decision, assumption, or unknown. Research discoverable facts before asking the user.

If an unresolved item can change a system boundary, data safety, ownership, technology choice, recovery, or acceptance criteria, return:

- **Readiness:** `blocked`
- **Verified context**
- **Decision hinge:** the guarantee or boundary the unknown controls
- **Next action:** one research step or user-owned decision

Do not rank or conditionally select candidates while that hinge remains open. Otherwise state bounded assumptions and continue.

## Decision workflow

1. Define the outcome, observable success, invariants, scope, non-goals, accepted manual work, owners, current lifecycle, real scale, and operational constraints.
2. Inspect current code, configuration, state, contracts, deployment, recovery, and native extension points. Treat live behavior as evidence and documents as intent when they drift.
3. Separate required behavior from placement, packaging, and verification. Custom logic does not imply a new file, runtime, service, or platform.
4. Trace each changed aggregate through transformations to its canonical writer and side effects. Preserve one deliberate writer unless a verified atomicity, isolation, or ownership invariant requires another.
5. Start at the lowest sufficient intervention: manual/no change → configuration → native extension → local change → bounded adapter → module → service → platform or migration. Reject lower levels only with a specific requirement or invariant.
6. Compare at most two serious candidates on total lifecycle delta: state, contracts, artifacts, ownership, deployment, secrets, observability, recovery, upgrade, rollback, removal, and verification.
7. Challenge the preferred candidate by subtraction. Every component, state store, abstraction, credential, retry, fallback, and procedure must protect a verified requirement, invariant, or credible material failure.
8. When a prior decision is superseded, inventory its code paths, writers, state, migrations, contracts, flags, dependencies, tests, observability, and documentation as `retain`, `migrate`, or `remove`. Retention needs a current requirement; irreversible history needs a safe forward migration.
9. Name acceptance evidence and measurable triggers for later complexity. Stop when the decision is supported or invalidated.

For a costly decision, new state/service, cross-owner contract, difficult rollback, or high-consequence invariant, read [the full decision method](references/full-decision-method.md) before finalizing. It contains the detailed aggregate-write, supersession, failure, lifecycle, and complexity gates.

## Output

For a ready decision, lead with:

1. **Decision and scope**
2. **Smallest complete architecture**
3. **Decisive evidence and assumptions**
4. **Lifecycle/artifact delta**, including writer and supersession effects when applicable
5. **Strongest rejected alternative** and why it loses
6. **Verification, recovery, residual risk, and evolution triggers**

For a small decision that reaches this skill, compress these to **Verdict**, **Reason**, **Boundary**, and the narrowest verification. Create an ADR only when the decision is durable, cross-owner, costly to reverse, or needs later revalidation.
