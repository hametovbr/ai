---
name: gathering-architecture-context
description: "Use when the user explicitly asks to investigate architecture context before deciding, or when a missing, disputed, stale, or inaccessible current-system fact could materially change ownership, a system boundary, data-safety guarantee, external contract, migration, deployment, or recovery. Do not use when supplied facts and bounded reversible assumptions are sufficient, for local implementation planning, or as a mandatory prelude to architecture work."
---

# Gathering Architecture Context

## Core rule

Collect only context that can change the pending architecture decision. Research discoverable facts; ask the user only for an inaccessible decision or boundary condition that has no safe reversible default.

Do not create a full context dossier merely because the task concerns architecture. If the available facts are sufficient, state that directly and stop.

## Workflow

1. Extract the decision hinge, supplied facts, scope, non-goals, and accepted manual work.
2. Identify only unknowns that can change ownership, a durable boundary, data guarantees, external contracts, deployment, migration, recovery, or acceptance criteria.
3. Inspect directly relevant code, configuration, manifests, documentation, incidents, measurements, and current official sources. Treat code and configuration as current behavior; mark documents as intent when they differ.
4. When a material unknown has no safe reversible default, ask one question if it is user-owned; otherwise name one action that can obtain the inaccessible decisive fact.
5. Otherwise label the assumption, bound the consequence if wrong, and continue. Unknown future scale or hypothetical reuse does not block a reversible present choice without evidence that it is a current requirement.

Do not propose candidates when the user requested fact-finding only. When the same request also asks for a decision and context is sufficient, use `making-pragmatic-architecture-decisions`; otherwise stop at the context result.

## Materiality test

An unknown is material only when different answers can change the decision now. Missing detail that affects only class names, exact file placement, optional optimization, or speculative future work is not an architecture blocker.

## Output

Return only applicable fields:

- **Decision hinge**
- **Verified decisive facts**, with source or artifact when relevant
- **Material assumptions or unknowns**, each with impact if wrong
- **Readiness:** `ready for decision` or `blocked`
- **Next action**, only when blocked

Mark `blocked` only when an unavailable user-owned decision or inaccessible decisive fact materially changes the result and no safe reversible default exists. Name the required guarantee or boundary and one next action; do not rank candidates.

## Stop rules

- Do not ask for searchable facts.
- Do not inventory unrelated lifecycle details.
- Do not turn context collection into design or implementation.
- Do not preserve conclusions invalidated by a later scope correction.
- Stop when all remaining uncertainty is bounded and non-decisive.
