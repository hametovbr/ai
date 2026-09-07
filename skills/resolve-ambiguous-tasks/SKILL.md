---
name: resolve-ambiguous-tasks
description: Use when a task begins with ambiguous, incomplete, conflicting, or weakly sourced input; when research must discover hidden context before decisions; or when implementation scope, constraints, ownership, success criteria, or boundaries are not yet reliable.
---

# Resolve Ambiguous Tasks

## Overview

Turn uncertainty into traceable state. Progress is not readiness: material conclusions connect to evidence, and implementation waits for gates.

## Classify First

Record both dimensions before broad discovery:

| Dimension | Choices |
|---|---|
| Mode | `research-only`, `decision`, `implementation`, `diagnosis` |
| Rigor | `Light`, `Standard`, `High` |

Mode is the requested terminal deliverable, not the next safe action. A blocked implementation remains `implementation` with `NOT_READY`.

- **Light:** reversible low-risk work; one scope check. Escalate when ambiguity or blast radius grows.
- **Standard:** incomplete context or multiple systems; compact ledgers; one independent audit when a material decision or contested evidence warrants it.
- **High:** architecture, production, privacy, money, irreversible change, or disputed evidence; full ledgers and fresh reviews.

Assess risk from behavior, data, authority and recovery consequences, not file extension or diff size. A deployment guide can change privileges or production behavior.

## Workflow

1. Write a context contract: deliverable, proof target, scope/non-scope, constraints, authority, privacy boundary, known inputs, and material unknowns.
2. Read [references/research-protocol.md](references/research-protocol.md) and [references/artifact-contracts.md](references/artifact-contracts.md). Inventory likely sources, choose narrowing keys, then run bounded reconnaissance.
3. Research by gap: convert observations into evidence and claims; search again only for an open material gap. At High rigor, critique the source map before expensive discovery.
4. Apply [references/review-contracts.md](references/review-contracts.md) by rigor: Light uses a direct scope/evidence check; Standard uses one independent audit for material decisions or contested evidence; High retains required isolated reviews. Give reviewers the artifact, contract and referenced evidence without author or prior-review verdicts. Reconcile material findings and check claim-to-source coverage.
5. For `research-only`, deliver the audited synthesis, confidence, limitations, and next evidence; stop here.
6. For implementation, require `Readiness: READY`, create a high-level specification, and obtain user approval. **REQUIRED SUB-SKILL for software architecture:** use `making-architecture-decisions`. Audit the specification at the selected rigor, resolve material findings, and obtain approval for the updated specification.
7. **REQUIRED SUB-SKILL:** use `superpowers:writing-plans`; obtain plan approval. Execute with applicable domain and repository workflows; select testing and delegation according to the approved plan, risk and project policy. Finish with `superpowers:verification-before-completion`.

If scope changes, invalidate only affected claims, decisions, and gates; reclassify mode/rigor and resume from the earliest invalid artifact.

## Hard Gates

- No implementation until readiness, specification approval, and plan approval are explicit.
- Missing or inaccessible evidence stays an unknown; it never becomes an assumption disguised as fact.
- A reviewer packet contains the contract and artifact only.
- Stop expanding source scope when no material gap justifies it.

Run `python scripts/validate_workflow_artifacts.py <artifact-or-directory>` before approval gates.

## Common Rationalizations

| Shortcut | Correction |
|---|---|
| “The patch already exists.” | Existing work is evidence, not readiness. |
| “This is tiny.” | Start Light; escalate only on observed risk. |
| “The reviewer needs my reasoning.” | It contaminates independent review; send artifact plus contract. |
| “We found enough facts.” | Check material claims against evidence and unresolved gaps. |

## Red Flags

Implementation with open material unknowns; research-only drifting into delivery; unbounded searching; conclusions included in reviewer context; or unchanged execution after scope expansion. Stop and reopen the affected gate.
