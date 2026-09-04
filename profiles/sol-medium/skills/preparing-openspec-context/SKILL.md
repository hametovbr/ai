---
name: preparing-openspec-context
description: Use when an OpenSpec change, proposal, design, spec, or tasks are requested from incomplete, ambiguous, stale, reference-derived, or weakly verified task and repository context, before any OpenSpec artifacts are written.
---

# Preparing OpenSpec Context

Build a reviewed, evidence-backed handoff before OpenSpec authoring. A plausible solution or task list is not proof that the current system has the assumed change points.

**REQUIRED SUB-SKILL:** Use `resolve-ambiguous-tasks` for the research contract, evidence ledger, unknowns, readiness, and independent review. Read its required references before investigating. Retain its terminal `Mode` (`implementation` for an OpenSpec delivery request) and add `Phase: pre-spec`. In this phase apply its research, ledger, review, hard-gate, and validation rules, but stop before its specification, planning, and execution steps. This skill owns that intentional early stop.

**CONDITIONAL SUB-SKILL:** Use `making-architecture-decisions` when the change selects or revises architecture. Use domain, source-search, documentation, or runtime skills only for the evidence gap they can actually close.

Read [the context-pack contract](references/context-pack-contract.md) completely before building the handoff.

## Boundary

This skill ends at a verified context pack and one status:

- `READY`: material context is verified, every proposed requirement and future task is traceable, review is reconciled, and the user has approved the pack.
- `PARTIAL`: useful findings exist, but material evidence, feasibility, ownership, or approval is missing.
- `NOT_READY`: the requested outcome cannot yet be scoped safely or rests on contradicted evidence.

At `PARTIAL` or `NOT_READY`, do not write or draft OpenSpec `proposal`, `spec`, `design`, `change`, or `tasks`. Do not disguise research steps as implementation tasks. A materially incomplete terminal response contains supported findings, blockers, `Next evidence`, and the re-evaluation condition only. The sole exception is `PARTIAL — awaiting context-pack approval`: every evidence/review/validation gate already passes, and the user may inspect the full non-normative traceability pack before approval; its candidate rows must remain mappings, never imperative task prose.

## Workflow

1. **Contract the investigation.** Record `Mode` as the terminal mode, `Phase: pre-spec`, rigor using the inherited `Light | Standard | High` scale, proof target, repositories and branch/worktree, scope, non-goals, authority, privacy constraints, inputs, and the decision the pack must enable. All inherited High-rigor requirements remain mandatory.
2. **Establish current state.** Inspect current code, tests, configuration, build/deploy wiring, history when relevant, existing OpenSpec state, and primary external contracts only as needed. Task prose, memories, plans, and reference implementations are inputs—not evidence about this repository until verified here. At High rigor, run the inherited source-map critique before expensive discovery.
3. **Decompose borrowed claims.** Separate upstream/native behavior, a local wrapper's behavior, and application-specific wiring. A working reference proves only what was inspected.
4. **Trace change paths.** Identify current lifecycle owners and exact change targets such as files, symbols, beans, tables, jobs, or API contracts. Inventory affected variants and consumers. For claims such as “all”, “default”, “automatic”, “single”, or “no behavior change”, run a bounded counterexample search and record its scope.
5. **Maintain two ledgers.** Keep evidence-backed facts separate from user decisions. Mark decisions `ACTIVE` or `SUPERSEDED`. For a scope change, inventory affected surfaces; preserve unaffected evidence; invalidate or reopen affected coverage, claims, decisions, requirement/task candidates, and review/readiness gates; reclassify mode/rigor; resume from the earliest invalid artifact. Keep assumptions and unknowns explicit. A risk or possible implementation detail stated in the request remains a `lead` or `unknown`, not a confirmed claim, until evidence supports it.
6. **Build the context pack.** Use the required contract as a working artifact. Requirement candidates describe supported behavior boundaries but are not yet normative OpenSpec text. A future task candidate is admissible only when it maps to evidence, the current lifecycle owner/change target, observable completion, verification, dependencies/order, and non-goals. For material `PARTIAL` or `NOT_READY`, keep change/requirement/task candidate sections internal and use the four-item terminal format. Show them only in an approval-ready pack after every non-approval gate passes, without imperative implementation wording.
7. **Review independently.** Follow `resolve-ambiguous-tasks` review isolation. After evidence synthesis, run and record an isolated research audit. Then give a fresh readiness reviewer a redacted packet containing context-pack sections 1–11, the contract, and the directly referenced evidence or locators needed to verify every material claim and task-admissibility mapping. Replace the header readiness value with `UNDER_REVIEW`; exclude section 12 findings, section 13 readiness conclusion/checklist, and every author or prior-review verdict. Reconcile both reviews into the master pack only afterward; material changes re-run the affected review. Use a compatible isolated reviewer agent; if an interactive grilling fallback would question the user or reveal conclusions, do not use it for this gate. Never substitute author self-review. If no compatible isolated reviewer is available, record that blocker and remain `PARTIAL` or `NOT_READY`.
8. **Validate and issue readiness.** Run `resolve-ambiguous-tasks/scripts/validate_workflow_artifacts.py <artifact-or-directory>` using the resolved installed path before the approval gate, including when accepting a supplied upstream pack; a recorded prior pass is not a substitute. `READY` requires no unresolved material unknown, no open blocker, admissible mapping for every future task candidate, both reviews reconciled, current validator success, and explicit user approval of the context pack. Otherwise remain `PARTIAL` or `NOT_READY`. Then hand the approved pack to the repository's applicable OpenSpec authoring workflow. Do not author OpenSpec within this skill.

## Existing Approved Packs

A supplied pack may skip rediscovery only when it is contract-complete and includes traceable provenance, evidence/claim IDs and locators, source scope and freshness, current OpenSpec state, review records, readiness, and explicit user approval. Confirm it only as an upstream handoff; state what this run did not independently re-verify. Lack of repository access in the current run is acceptable only when the upstream process verified a pinned revision, all material evidence remains traceable, the handoff targets that same revision, and no freshness signal contradicts it. Otherwise, downgrade readiness for stale, inaccessible, absent, or scope-inconsistent material evidence. Never promote a bare assertion that a pack was “verified” into repository evidence.

Ask the user only for preferences, authority, or facts that cannot be discovered safely. Repository facts should be researched.

## Stop Signals

Stop and lower readiness when any of these appears:

- an implementation task has no verified current owner or change target;
- a task is actually a discovery action needed to choose the solution;
- a universal claim lacks an inventory or counterexample search;
- an active requirement depends on a superseded decision;
- an absence claim is based on inaccessible or unsearched evidence;
- the terminal handoff contains OpenSpec-shaped content before approval.

## Rationalizations to Reject

| Rationalization | Required response |
|---|---|
| “The reference already works.” | Verify the target repository's contract, wrapper, and wiring. |
| “The plan was approved.” | Treat approval as a decision; verify implementation facts independently. |
| “The prompt mentions this risk, so it is confirmed.” | Classify it as a lead or unknown and verify it against the current scope. |
| “Discovery can be task one.” | Keep prerequisite research under `Next evidence`. Only an intentionally scoped proof-first implementation spike may become a task after its owner, acceptance, and verification are known. |
| “I remember this codebase.” | Re-check current source and branch state. |
| “A partial task draft is still useful.” | Return the pack and blockers; premature tasks harden assumptions. |
