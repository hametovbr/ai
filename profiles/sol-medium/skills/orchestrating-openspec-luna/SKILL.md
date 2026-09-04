---
name: orchestrating-openspec-luna
description: Use when executing an already planned OpenSpec change through Luna Max subagents, including decomposition, dispatch, verification, integration, and recovery. Planning and architecture decisions precede this skill.
---

# OpenSpec execution through Luna Max

## Roles and boundaries

The primary agent owns execution decomposition, scheduling, inspection, clean integration, verification and acceptance. Luna Max workers implement code, tests, configuration, generated outputs and fixes. Workers do not redesign, expand scope, spawn children or mark OpenSpec tasks complete. A fresh read-only Luna reviewer can add evidence; the primary agent still owns the verdict.

Keep product planning and architecture outside this skill. Resolve implementation details from approved artifacts and code. If requirements/design are missing or contradictory, block the affected unit and return that decision to planning; continue independent authorized work. Do not silently replace Luna with primary-agent implementation or a different model. Existing execution authorization covers routine work; do not add per-task approvals.

## Execution loop

1. **Establish inputs.** Resolve the exact change, read applicable `AGENTS.md`, project OpenSpec guidance, plan, requirements/scenarios, design and relevant code. Use installed CLI help and, where supported, `openspec status --change <id> --json` plus `openspec instructions apply --change <id> --json`. Resolve returned artifact paths; do not assume a fixed schema or install/upgrade the CLI. Artifact completion is not execution authorization or code completion. Record plan hashes, code baseline including dirty/untracked files, required checks and existing failures.
2. **Define ready units.** Map original OpenSpec task/scenario IDs to bounded units with one observable outcome, non-goals, fixed contracts, writable paths, accepted dependencies, verification commands and evidence. Include necessary tests with behavior. Preserve original IDs; use child IDs in the ledger. Do not invent a contract to make a unit ready: inspect first or serialize producer and consumer.
3. **Schedule.** Track both `requires accepted output` and `cannot run concurrently` edges. Check semantic contracts and shared files, generators, lockfiles, fixtures, databases, ports, caches and build outputs. Prioritize work that unlocks dependents; prepare the next ready briefs rather than every downstream brief. Integrate accepted increments immediately and refill capacity as dependencies clear.
4. **Dispatch.** Read [handoffs.md](references/handoffs.md) before first dispatch. Use a fresh worker for each coherent unit and resume it for local corrections. Provide task-local artifacts, exact constraints, ownership, baseline, checks and report location—not conversation history. Record agent ID, model/effort, workspace and write scope before another dispatch.
5. **Review and verify.** Inspect actual source and full diff, including untracked/deleted files. Map required scenarios to behavior and evidence; check compatibility, failure paths and assertions. Run decisive acceptance checks under primary-agent control against the exact candidate. Inspect combined behavior after integration. Only then accept the unit and update the parent task when all children and required integration checks pass.
6. **Handle failures.** Supply missing context or concrete review findings to the worker. After two corrections to an unchanged brief, diagnose before retrying: narrow/revise the unit or use a fresh Luna worker with a reason. Preserve attempt counts and lineage. Block if no justified next attempt exists. Design changes return to planning and invalidate affected briefs/results.
7. **Finish.** Review the whole change against original scenarios, run required project gates and applicable OpenSpec validation on the final integrated state, and report actual results and remaining blockers. Structural OpenSpec validation is not evidence that code works. Follow existing authorization for archive, publication, deployment and shared-branch merge.

## Choose the smallest adequate team

| Work | Default |
| --- | --- |
| Small coherent change | One worker plus primary review |
| Coupled changes/unknown interface | Read-only discovery, then dependent execution |
| Independent behavior and isolated resources | Small ready set, normally start with two workers |
| Repeated mechanical changes | One batch with a complete target list |
| Material contract/persistence/security change or substantial diff | Fresh read-only review, then primary acceptance |
| Semantic integration fix/merge conflict | One bounded Luna assignment after conflicting writers stop |

Do not create a standing planner/critic/tester/reviewer team for every task. Increase concurrency only when independence and review capacity support it. If reviews accumulate or collisions repeat, reduce concurrency or keep tightly coupled changes together. Different agents or branches alone do not isolate files.

## Runtime and workspace invariants

- Explicit worker settings: `model: "gpt-5.6-luna"`, `reasoning_effort: "max"`, `fork_turns: "none"` with `collaboration.spawn_agent`; adapt only to the actual exposed schema. Verify selection where observable. If unavailable, report the capability gap and continue read-only preparation; no silent substitution.
- Separate worktrees require explicit paths and bases. In a shared tree default to one writer; allow more only with verified disjoint ownership and resources. Serialize Git index/branch operations; shared-tree workers do not switch branches, stage all, reset, clean, stash, merge or commit.
- Preserve user work. HEAD alone does not identify a dirty candidate, and a new worktree from HEAD omits uncommitted changes. Establish an attributable baseline/snapshot without discarding or committing unrelated changes.
- Primary integration is mechanical only. Luna resolves conflicts and semantic fixes. Do not use wholesale `ours`/`theirs` to conceal conflicts. Freeze the candidate for review/checks or use an immutable snapshot.
- Before replacement, confirm the old worker and background processes stopped. A long test alone does not mean a worker is stuck.

## Evidence and recovery invariants

`READY_FOR_REVIEW` is a worker report, not completion. Record each check's command, cwd, candidate identity, exit status, outcome and log. Missing dependencies, skipped checks and infrastructure failure are `BLOCKED/NOT_RUN`, not PASS. H1 evidence does not verify changed H2; rerun affected checks and required final gates. Preserve unrelated evidence only with an explicit reason.

Use behavioral tests for material changes and credible failure paths; reproduce bug fixes when feasible. Follow repository policy. Use proportional inspection/build/validation for reversible low-impact edits. Never weaken assertions, remove tests or waive required behavior to finish. A reviewer needs requirements and actual diff/code, not just the author's report; reviewer agreement is not proof.

Maintain one change-scoped ledger with `pending → ready → running → review → accepted`, blockers, findings and reopening decisions. Use the established execution location; otherwise use a local directory outside formal OpenSpec artifacts and record its path. After interruption reconcile ledger hashes, workspace/Git state, active workers and logs before dispatching. Missing evidence means verify existing work, not automatically redo it. Retain evidence through handoff; never close all OpenSpec tasks based only on worker reports.

For custom layouts, dirty-work isolation, disputed findings or recovery details, read the relevant section of [execution-details.md](references/execution-details.md). Its detailed protocol preserves these same boundaries; it is not a second plan.
