---
name: resolve-ambiguous-tasks
description: Use when a task begins with ambiguous, incomplete, conflicting, or weakly sourced input; when research must discover hidden context before decisions; or when implementation scope, constraints, ownership, success criteria, or boundaries are not yet reliable.
---

# Resolve Ambiguous Tasks

Turn material uncertainty into traceable state, then continue toward the user's requested deliverable as soon as the evidence supports it.

## Classify first

Record the terminal **Mode**: `research-only`, `decision`, `implementation`, or `diagnosis`, and choose proportionate **Rigor**:

- `Light`: reversible, low-impact work; one scope and evidence check.
- `Standard`: incomplete context, multiple systems, or meaningful side effects; compact ledgers and one independent audit when it can change the result.
- `High`: architecture, production, privacy, money, irreversible change, or disputed evidence; full ledgers and fresh isolated reviews.

Mode describes the requested outcome, not the next safe action. Escalate rigor when discovered risk warrants it; do not impose High-rigor ceremony on Light work.

## Workflow

1. Write a compact context contract: requested deliverable, proof target, scope/non-scope, constraints, authority, privacy boundary, known inputs, and material unknowns.
2. Read [the research protocol](references/research-protocol.md) and [artifact contracts](references/artifact-contracts.md). Inventory likely sources, choose narrowing keys, and run bounded reconnaissance.
3. Research by gap. Convert observations into evidence and claims; mark inference, contradiction, and unknown explicitly. Search again only for an open material gap. At High rigor, critique the source map before expensive discovery.
4. Review proportionally using [review contracts](references/review-contracts.md):
   - Light: perform a direct claim-to-source and scope check.
   - Standard: use one fresh isolated reviewer when the decision is material or the evidence is contestable.
   - High: use the required independent research and readiness reviews with packets containing the contract, artifact, and necessary evidence, but no author verdict.
   Reconcile findings and reopen affected claims. If required isolation is unavailable, record the blocker rather than substituting author self-review.
5. For `research-only`, return the audited synthesis, confidence, limitations, and next evidence; stop.
6. For `decision` or `diagnosis`, continue once evidence satisfies the proof target. Use the applicable domain or architecture skill when the task crosses its boundary.
7. For `implementation`, require `Readiness: READY`, then create only the specification and plan needed for the work's risk and repository rules. Existing user authorization is sufficient for reversible work unless a governing workflow requires a separate approval; obtain explicit approval immediately before a consequential, irreversible, or externally mutating step that is not already authorized. Execute and verify with applicable domain skills.

If scope changes, invalidate dependent claims, decisions, and gates; preserve unaffected evidence; reclassify mode/rigor and resume from the earliest invalid artifact.

## Readiness and stop rules

`READY` requires that every material claim needed for action has admissible evidence, no unresolved contradiction or unknown can change the result, ownership and acceptance are clear, and required review/validation gates pass.

- Missing or inaccessible evidence remains an unknown; it never becomes fact by repetition.
- A supplied patch, plan, or “verified” pack is an input until its relevant claims are checked.
- Stop expanding source scope when no material gap justifies it.
- Do not implement with an open material unknown or let research-only work drift into delivery.
- Ask the user only for preferences, authority, or facts that cannot be discovered safely. Ask one focused question only when its answer blocks progress and no safe bounded default exists.

Run `python scripts/validate_workflow_artifacts.py <artifact-or-directory>` before a formal approval or readiness gate. A validator checks artifact shape; it does not replace evidence review.

## Output

Lead with the requested deliverable when ready. If blocked, return only:

- **Mode / Rigor / Readiness**
- **Strongest verified findings**
- **Material blocker and affected decision**
- **Next evidence or one user-owned decision**
- **Condition for re-evaluation**
