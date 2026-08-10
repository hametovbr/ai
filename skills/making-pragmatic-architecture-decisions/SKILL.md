---
name: making-pragmatic-architecture-decisions
description: "Use when choosing or revising software-system boundaries: where behavior or state belongs; configuration vs custom code; inline, plugin, module, service, or platform placement; integration, deployment, migration, ownership, or build-vs-buy shape. Do not use for local changes that preserve existing boundaries, fact-finding only, or review of an already proposed architecture or ADR."
---

# Making Pragmatic Architecture Decisions

## Core rule

Choose the smallest sufficient design. Treat every component, artifact, process, and reliability mechanism as a cost that needs evidence.

Use this skill as the normal architecture entrypoint. Do not load `gathering-architecture-context` or `challenging-architecture-decisions` merely because the task concerns architecture.

## Route proportionally

Use the **fast path** by default when the choice is reversible, stays with one owner, and does not add or change durable state, an external contract, a deployment unit, credentials, migration, or recovery responsibility:

1. Extract the requested outcome, invariants, scope, and non-goals from available context.
2. Inspect only directly relevant artifacts or facts.
3. Choose the first sufficient level: no change/manual handling → configuration → native extension → local change → bounded adapter → module → service → platform.
4. Name the decisive reason and one verification or material failure note.
5. Stop.

Use a deeper comparison only when the decision is costly to reverse or materially changes ownership, data guarantees, contracts, deployment, migration, security, recovery, or long-term operating cost. Compare only credible alternatives and only on differences that can change the verdict.

Use `gathering-architecture-context` only for an explicit investigation request or a genuinely missing, disputed, or stale fact that can change such a material choice. Use `challenging-architecture-decisions` only when the user requests review, stress-testing, or an independent check of an existing proposal.

Read [principles.md](references/principles.md) only for an explicit principles-based review, a substantive conflict between qualities, or a costly hard-to-reverse decision. Do not load it on the normal path.

## Decision discipline

- Let the latest explicit scope or correction replace conflicting earlier plans.
- Map each addition to a verified requirement, invariant, or credible failure not already handled. “Production-ready” alone does not justify retries, queues, alerts, dashboards, or runbooks.
- Separate required behavior from placement and packaging; custom logic does not imply a new file, runtime, service, or platform.
- Research discoverable facts. Ask one question only when an unavailable user-owned decision materially changes the result and no safe reversible default exists.
- Otherwise state a bounded assumption and its consequence if wrong, then continue.
- Mark facts, evidence-backed inferences, and assumptions distinctly. Do not invent certainty.
- Do not add optional refactors, documentation, governance, orchestration, or future-proofing outside the requested outcome.
- Stop when the requested decision is supported and its acceptance evidence is named.

## Output

For the fast path, return:

- **Verdict**
- **Reason**
- **Boundary**
- **Verification or material assumption**, only when needed

For a deeper decision, add only material context, credible rejected alternatives, lifecycle delta, residual risks, and measurable triggers for later complexity. Create an ADR only when the decision is durable, cross-owner, or costly to reverse.
