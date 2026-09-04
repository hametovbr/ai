# Execution details

Read the relevant section for custom OpenSpec layouts, workspace isolation, disputed evidence, stuck workers, or recovery.

## 1. Establish executable inputs

1. Resolve the selected change from the request and repository. If several changes remain equally plausible, ask for the change identifier; do not choose by recency alone.
2. Read root and applicable nested `AGENTS.md`, the project's OpenSpec instructions and configuration, and required local skills. Inspect the installed CLI help/version before relying on command flags.
3. Where supported, run `openspec status --change <id> --json` and `openspec instructions apply --change <id> --json`. Read the returned context, operation guidance, artifact locations, and applicable artifacts. Resolve paths from the output rather than hardcoding `openspec/changes/<id>`; custom schemas and external stores may differ. With an older CLI, use the repository's documented apply workflow and actual artifacts. Do not install or upgrade OpenSpec to accommodate this skill.
4. Read the ready plan, requirements/scenarios, relevant current specs, approved design, and actual implementation entry points. Confirm the project's apply prerequisites, not a universal list of mandatory artifact filenames. CLI artifact completion alone is not authorization and is not implementation completion.
5. Record plan/spec revision or content hashes, implementation base, dirty/untracked files, required checks, known baseline failures, and execution authorization. Inspect nearby code and existing tests enough to make the first briefs accurate.

Preserve the repository's source-of-truth rules. A task brief cannot override a requirement. If artifacts contradict each other, report the concrete conflict and affected task; resolve it before assigning that behavior. Task-size refinement is in scope; new API semantics, ownership boundaries, migration strategy, or acceptance criteria are planning changes.

## 2. Decompose by acceptance boundary

Map each original OpenSpec task and relevant requirement/scenario to one or more execution units. Keep original task IDs; use child IDs such as `2.1/a` in the execution ledger. Do not replace the original plan with a competing plan.

A unit is ready when it has:

- one coherent observable outcome and explicit non-goals;
- fixed inputs and interface expectations from the plan or accepted prerequisites;
- bounded writable paths and identified read dependencies;
- behavioral acceptance evidence and concrete verification commands;
- a reviewable diff and no unresolved architecture/product choice.

Prefer a small vertical behavior with its tests. A handful of files is a useful starting point, not a hard cap. Split when the worker must hold unrelated domains, make several independent decisions, or cannot verify the result locally. Keep tightly coupled code together; batch repeated mechanical edits under one brief. Do not split production code and its necessary tests merely to use more agents.

Construct a dependency graph with two distinct edge types: **requires accepted output** and **must not run concurrently**. Include semantic dependencies even when paths do not overlap. For every candidate parallel pair check writable files, consumed interfaces, generators and lockfiles, shared fixtures, databases, ports, caches, and build outputs.

If an interface producer and consumer are not already constrained by an adequate contract, serialize them. Different files do not make them independent. A fixed approved interface permits parallel implementation only when isolated checks and integration criteria are specified. Generate clients after their source contract is accepted; give generated outputs a single owner and the actual generation command.

Example: for an approved cursor pagination change, assign repository behavior plus focused tests, then dependent endpoint behavior plus compatibility tests, then SDK regeneration and integration checks. Parallelize endpoint work with repository work only if the internal call contract is already fixed. Have the primary agent identify this fact from artifacts/code, not invent a signature to unlock parallelism.

## 3. Protect the workspace

Identify the actual sharing model; a new agent or branch does not provide filesystem isolation.

- **Separate worktrees/checkouts:** use explicit absolute paths and named bases; each worker stays in its assigned tree. Integrate accepted outputs in dependency order. Isolation prevents file races, not incompatible designs.
- **Shared tree:** default to one writer. Parallel writers require proven disjoint ownership, no shared generated/build/test resources, and attributable diffs. Serialize Git index/branch operations; workers do not switch branches, stage all files, reset, clean, stash, merge, or commit in a shared tree.
- **Dirty user work:** preserve it. Determine whether it is part of the execution baseline. A clean worktree from HEAD omits uncommitted changes; do not silently test the wrong baseline. Preserve relevant changes through a documented non-destructive snapshot/copy into an isolated candidate, or work serially with explicit before/after attribution. Do not commit, discard, or overwrite unrelated user work.

The primary agent performs clean mechanical integration. Send merge conflicts and all semantic integration edits to a Luna worker with a new bounded brief. Never resolve conflicts with wholesale `ours`/`theirs` selection. Freeze candidate files during review and verification, or review an immutable snapshot.

## 4. Dispatch and supervise

Use `gpt-5.6-luna` with reasoning effort `max` explicitly. Read the available tool schema: with `collaboration.spawn_agent`, use `fork_turns: "none"`, `model: "gpt-5.6-luna"`, and `reasoning_effort: "max"`. Supply task-local context through a brief and accessible paths. A full-history fork is inappropriate and may prevent model overrides. Verify selection where the runtime exposes it; do not claim a model was used from prompt wording alone.

If this model, effort, or subagent mechanism is unavailable, report the exact capability gap. Do not silently substitute another model, reduce effort, or implement the task in the primary agent. Continue useful read-only preparation.

Start with the smallest ready set. Increase parallelism only when independence and review capacity support it; reserve capacity for fixes/review rather than filling every slot. One fresh worker per coherent unit; resume the same worker for a local correction. Do not mix unrelated task histories in a reused worker.

Briefs must fit the task: outcome, original task/scenario references, exact contracts and constraints, minimum code entry points, ownership, baseline, checks, stop conditions, and report path. Provide exact requirement values once with authoritative references. Do not paste the full conversation, entire repo, or accumulated reports. Give workers access to necessary source artifacts; do not hide constraints to make prompts shorter.

Record agent ID, task ID, model/effort, workspace, base, and writable scope before scheduling another writer. Monitor reports and progress alongside useful local review. A long test is not a stuck agent. On inactivity, inspect observable state and request a progress/blocker report; interrupt if necessary. Before reassigning ownership, confirm the old agent and its background processes have stopped. Never run two replacement workers on the same scope.

## 5. Accept evidence, not completion claims

Worker `READY_FOR_REVIEW` is not task completion. The primary agent performs these gates:

1. **Scope and spec:** inspect the actual diff, including new/deleted/untracked files; map every required scenario to implementation and evidence. Check compatibility and prohibited scope changes. Inspect the actual source, not only the worker summary.
2. **Correctness and quality:** inspect boundary/error paths, test assertions, and changed interfaces. Apply risk-specific checks where relevant: authorization, transactions, concurrency, migrations, retries, generated code. Do not add a universal security/tooling program.
3. **Verification:** execute relevant checks against the exact candidate. Record command, cwd, version/snapshot, exit status, and outcome. Reuse worker logs only when independently inspected and attributable to the same immutable candidate; still run the decisive acceptance check under primary-agent control. Missing dependencies, skipped tests, or infrastructure failure are BLOCKED/NOT_RUN, not PASS.
4. **Integration:** inspect and test the combined state after integration, not just each worker branch. Confirm contract consumers, generated outputs, and preserved baseline changes still agree.

For material behavior changes, require tests that exercise the required behavior and credible failure paths; for bug fixes, reproduce the defect when feasible. Follow repository test policy. For reversible low-impact edits, use proportional inspection/build/validation instead of invented tests that mirror implementation. Never accept weakened assertions, skipped gates, changed expected values, or removed tests merely to make checks green.

Use a fresh read-only Luna reviewer when independent inspection adds value, especially for contracts, persistence, security-sensitive behavior, or a substantial diff. Give it raw requirements, fixed diff/base/head, and relevant test evidence without the implementer's verdict. Require separate spec and correctness findings with locations and impact. Reviewers do not edit. The primary agent adjudicates findings against evidence; agreement among agents is not proof.

Any change after a check invalidates affected evidence. Identify affected checks from the changed dependencies; rerun required final gates on the final integrated snapshot. Never carry PASS from H1 to modified H2 because the fix was small or time is short. If unrelated evidence remains reusable, record the reason.

## 6. Repair without looping blindly

- `NEEDS_CONTEXT`: answer from verified artifacts/code and amend the brief; retain the same task and worker when useful.
- `BLOCKED`: separate environment failure, scope conflict, ambiguous requirement, and implementation difficulty. Fix authorized environment issues or narrow/restructure execution; do not fabricate success.
- Review failure: send concrete findings, evidence, expected behavior, and affected checks to the worker. Re-review the correction and changed dependencies, rather than reopening unrelated areas.
- Default to two correction attempts per unchanged brief. Treat this as a circuit breaker, not a success threshold. At the cap or repeated identical failure, stop blind retries; the primary agent diagnoses and records why a smaller/revised unit or fresh Luna worker can succeed. Keep lineage and attempt counts across replacement workers. If no justified next attempt exists, block the affected unit.
- If the fix requires changing design or requirements, enter the external planning process. Do not promote the worker to architect or switch to a stronger implementer. After an authorized plan revision, invalidate affected briefs, dependent results, and acceptance evidence before resuming.

Required behavior and blocking defects cannot be waived to finish. Record unrelated observations without expanding scope. Resolve disputed findings with source evidence; user input is only needed when the resolution exceeds the existing authorization or plan.

## 7. Persist, resume, and finish

Maintain one change-scoped execution ledger and task briefs/reports in the repository's established location. If none exists, use a local execution directory outside formal OpenSpec artifacts; record its absolute path. Do not introduce a new OpenSpec schema or add orchestration files to a change's public deliverables by default. Retain enough evidence for resumption; do not delete it before handoff.

State transitions: `pending → ready → running → review → accepted`; rejection returns to `running` with findings; `blocked` records an explicit cause. `accepted` requires integration evidence appropriate to that unit. Reopen accepted work if a later change invalidates it.

After compaction/interruption, reconcile ledger identity and artifact hashes with Git/workspace state, live workers, and check logs. Do not blindly trust either checkboxes or memory. Recover existing outputs before dispatching replacements. A checked original task with no usable evidence is unverified; inspect and verify it rather than automatically reimplementing it.

Only the primary agent updates original OpenSpec task completion, after every child unit and its required integration checks are accepted. Preserve task text and IDs. Do not check all tasks at once because workers reported success.

Finish with a whole-change review against the original scenarios and scope, required project gates, and applicable OpenSpec validation. Validation of OpenSpec structure is separate from proof that code works. Report implemented scope, checks actually run, final candidate identity, and any remaining blockers. Do not describe partially verified work as complete. Archiving, publishing, deploying, or merging to a shared branch follows the existing request and repository lifecycle; this skill grants no additional authorization.

## OpenSpec compatibility reference

Consult the installed project first. CLI integration points above are documented in the official [OpenSpec CLI reference](https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md); operation guidance is described in [customization](https://github.com/Fission-AI/OpenSpec/blob/main/docs/customization.md). These describe discovery, not a fixed schema requirement.
