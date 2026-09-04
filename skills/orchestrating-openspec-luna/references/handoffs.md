# Execution handoffs

## Worker brief

Populate these fields from inspected sources; omit no required field. Keep paths absolute when workers can have different working directories. Use concise excerpts plus links to actual artifacts, not duplicated specifications.

```text
Role: Luna Max implementation worker; no child agents.
Task: <execution ID>; OpenSpec parent IDs: <IDs>.
Outcome: <one observable behavior>.
Requirements: <artifact path + section/scenario; exact constraints>.
Non-goals: <explicit excluded behavior and decisions>.
Workspace: <absolute path>; base: <commit + dirty snapshot if any>.
Accepted prerequisites: <IDs + relevant fixed interfaces/output versions>.
Read first: <applicable AGENTS/local skills; selected code/test entry points>.
May edit: <paths/precise ownership>; must preserve: <baseline/user work>.
Contract: <inputs, outputs, errors, compatibility/invariants from approved sources>.
Acceptance: <observable cases including material edge/error paths>.
Checks: <exact commands, cwd, required resources; baseline known failures>.
Coordination: <shared resources, permitted Git actions, report path>.
Stop and report: missing contract, out-of-scope file/decision, unexpected user
changes, unverifiable baseline, or unavailable required check.
Return READY_FOR_REVIEW, NEEDS_CONTEXT, or BLOCKED with the report below.
Do not mark OpenSpec tasks complete, change the design, weaken gates, publish,
or perform semantic integration outside this assignment.
```

Do not use broad ownership such as `src/**` when a narrower boundary is known. If file scope cannot be known until inspection, dispatch a bounded read-only discovery unit first; use its evidence to complete the implementation brief.

## Worker report

```text
Status and task ID:
Workspace and starting base/snapshot:
Final commit or snapshot identity, including dirty/new files:
Changed files and observable behavior:
Requirement/scenario → implementation location → check evidence:
Checks: exact command | cwd | candidate identity | exit code | outcome | log path
Not run/blocked checks and reasons:
Remaining concerns or required decisions:
```

Store detailed evidence at the assigned report path; return a short status plus pointers. Record facts rather than “all tests pass.” A report is a review input, never permission to accept.

## Reviewer brief and report

Supply the original requirement/scenario pointers, immutable base and candidate diff, actual relevant code, and check evidence. Request a read-only assessment of scope/spec compliance and correctness. Do not supply an intended verdict or ask the reviewer to endorse the worker.

For each finding require: requirement/invariant, location, concrete failure condition, consequence, and suggested verification. Distinguish blocking defects from unrelated observations. A clean review must say what was inspected and what could not be verified. The primary agent resolves findings and owns acceptance.

## Minimal execution ledger

Keep one ledger per exact change identity, including repo/store location. Record:

- Plan/spec paths and revisions/hashes; implementation baseline and user changes.
- Original task/scenario → execution units → required evidence.
- Each unit's outcome, dependencies, write ownership, shared resources, and status.
- Agent ID, requested/observed model and effort, workspace, base/candidate version.
- Check commands/results/log locations and review findings tied to that version.
- Integration version, acceptance/reopening decision, and original checkbox update.
- Corrections with attempt count and parent task lineage; blockers and decisions.
- Active workers/processes and exact next action for resumption.

For a small change use one compact table plus evidence links. Do not maintain duplicate boards, copy reports into the ledger, or invent metrics. Store candidate identity as commit plus dirty/untracked content snapshot when necessary: HEAD alone does not identify an uncommitted worktree.
