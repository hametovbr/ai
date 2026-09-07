# Verified Context Pack Contract

Use the full structure for High-rigor preparation. At Standard, combine fields into compact ledgers; at Light, use one compact note with scope, current revision/evidence, verified target, observable completion, sufficient check, dependencies/non-goals, material gaps, direct review and approval status. Preserve the same evidence and task-admissibility meaning without requiring all headings, empty coverage rows or separate artifacts. Escalate on material risk. Preserve stable IDs from `resolve-ambiguous-tasks` where already used.

## 1. Header

```text
Mode: <research-only | decision | implementation | diagnosis>
Phase: pre-spec
Rigor: <Light | Standard | High>
Readiness: <READY | PARTIAL | NOT_READY>
Proof target: <decision this pack must enable>
Prepared from: <repository/worktree/branch/revision and relevant external systems>
Current as of: <timestamp or inspected revision>
```

For an OpenSpec delivery request, `Mode` remains `implementation`; `pre-spec` is the bounded current phase, not a replacement mode. Apply the rigor requirements inherited from `resolve-ambiguous-tasks`, including all High-rigor review gates.

`READY` is invalid until the user approves this pack. Before approval, use `PARTIAL — awaiting context-pack approval`, even if every evidence gate passes.

## 2. Investigation Contract

- In scope
- Non-goals
- Required decisions
- Evidence authority and permitted sources
- Privacy/security constraints
- Delivery constraints
- Supplied inputs and how each is classified: evidence, lead, reference, user decision, or unverified claim. Prompt-supplied risks and possible implementation details default to `lead` or `unknown`, never confirmed current-state claims.

For a supplied upstream context pack, also record its source location, preparer, repository revision, evidence/claim provenance and direct locators, source scope and freshness, current OpenSpec state, research/readiness reviews, approval record, and what the current run did not independently re-verify. A summary that merely says “verified” is not contract-complete. Current-run repository access is not required when the pack proves inspection of a pinned revision, targets that same revision, keeps every material source traceable, and has no conflicting freshness signal.

## 3. Current-State Baseline

Record what exists now, not the requested future narrative:

- repository, worktree/branch, revision, dirty-state relevance;
- current behavior and lifecycle;
- current owners and exact implementation targets;
- test coverage and verification entry points;
- configuration, runtime, deployment, migration, and compatibility paths when relevant;
- existing OpenSpec changes/specs and collision or dependency risk;
- evidence freshness and inaccessible surfaces.

## 4. Coverage Map

| Surface | Inspected evidence | Current finding | Gap or limitation |
|---|---|---|---|
| Behavior and domain rules | | | |
| Data and migrations | | | |
| API/events/integrations | | | |
| Lifecycle owners and wiring | | | |
| Error/failure paths | | | |
| Compatibility and rollout | | | |
| Operations/observability | | | |
| Privacy/security | | | |
| Ownership and delivery | | | |

For the full pack, mark irrelevant surfaces with a reason. Compact packs cover relevant surfaces and explicitly record material gaps.

## 5. Evidence and Claims

Use the evidence, claim, contradiction, and unknown ledgers from `resolve-ambiguous-tasks`. Each material conclusion below must cite claim IDs and their supporting evidence IDs. Separate direct observation from inference.

## 6. Decision Ledger

| Decision ID | User decision or constraint | Status | Feasibility evidence | Supersedes | Downstream impact |
|---|---|---|---|---|---|
| D-... | | ACTIVE / SUPERSEDED | | | |

User preference establishes intent, not repository feasibility. If a decision or scope changes, inventory affected surfaces, preserve unaffected evidence, mark replaced decisions `SUPERSEDED`, and invalidate or reopen affected coverage, claims, decisions, requirement/task candidates, and review/readiness gates. Record the earliest invalid artifact and resume there.

## 7. Universal-Claim Audit

Required for claims containing or implying complete coverage, default behavior, automatic behavior, one owner/path, or unchanged behavior.

| Claim ID | Claim | Inventory/counterexample search scope | Result | Residual limitation |
|---|---|---|---|---|
| C-... | | | | |

## 8. Change Inventory

| Capability or behavior | Current lifecycle owner/change target | Basis claims | Intended observable delta | Constraints and non-goals | Status |
|---|---|---|---|---|---|
| | exact file/symbol/bean/table/job/contract | C-... | | | VERIFIED / BLOCKED |

“Create a component” is not a current target. Name the existing seam it changes or prove that a new seam is required.

## 9. Requirement Candidates

These are research handoff entries, not normative OpenSpec requirements. Separate required outcomes/contracts from suggested local implementation methods; no suggestion silently becomes a binding requirement.

| Candidate | Supported behavior boundary | Basis claims/decisions | Current owner | Acceptance boundary | Status |
|---|---|---|---|---|---|
| RQ-... | | C-..., D-... | | observable outcome and exclusions | SUPPORTED / BLOCKED |

## 10. Future-Task Admissibility

Do not phrase blocked rows as implementation instructions. They expose internally why authoring must wait and are not included in a materially `PARTIAL` or `NOT_READY` terminal response.

| Candidate | Requirement | Evidence | Current owner/change target | Observable completion | Verification | Dependencies/order | Non-goals | Status |
|---|---|---|---|---|---|---|---|---|
| TC-... | RQ-... | E-..., C-... | exact current seam | | exact test/check | | | ADMISSIBLE / BLOCKED |

In Verification, name the behavior/risk, exact sufficient test/check and rerun trigger. An extra expensive run or new test infrastructure requires a concrete gap that cheaper existing checks do not cover. Include these decisions in the authoring handoff, not only the conversation.

A row is `ADMISSIBLE` only when every cell is supported. An unknown target, speculative file/symbol, vague “add tests”, or undiscovered dependency makes it `BLOCKED`.

Research needed to discover the solution belongs in `Next evidence`, not this matrix. A proof-first implementation spike is admissible only if the decision it resolves, bounded code surface, observable outcome, cleanup/disposition, and verification are already defined.

## 11. Unknowns, Contradictions, and Blockers

For each material item include:

- exact unknown or contradiction;
- why it changes scope, design, acceptance, or sequencing;
- who/what can resolve it;
- bounded next evidence action;
- fallback if the evidence is inaccessible.

## 12. Independent Review

Record the review required by rigor/project policy: Light direct scope/evidence check; Standard combined independent research/readiness audit when a material decision or contested evidence warrants it (otherwise direct check and rationale); High separate isolated research/readiness audits.

Record:

- applicable review findings;
- accepted/rejected/deferred status with rationale and evidence;
- claims or decisions reopened by review.

The researcher may not silently mark their own pack ready after a material review finding.

## 13. Readiness Decision

### READY checklist

- [ ] Scope and non-goals are stable.
- [ ] Current repository/OpenSpec state is identified and fresh enough.
- [ ] Material claims are supported and contradictions reconciled.
- [ ] No material unknown remains `OPEN` and no blocker remains open.
- [ ] Universal claims passed a bounded counterexample search.
- [ ] User decisions are feasible and active/superseded states propagated.
- [ ] Every material requirement candidate has a current owner and acceptance boundary.
- [ ] Every future task candidate is `ADMISSIBLE`.
- [ ] Reviews required by rigor/project policy have no unresolved material finding; unavailable required independent review is an open blocker. Light direct checks need no isolated reviewer.
- [ ] A current deterministic workflow-artifact validation run passes, including for an upstream pack.
- [ ] The user explicitly approved this context pack.

If every item passes, return `READY` and hand off:

- the approved scope and non-goals;
- evidence/claim and decision IDs;
- change inventory;
- supported requirement candidates;
- admissible future-task matrix;
- accepted non-material unknowns and limitations.

The subsequent OpenSpec authoring process converts this handoff into repository-native artifacts. It must not invent missing owners, files, symbols, requirements, or tasks.

When an isolated audit is required, provide the applicable content from sections 1–11 (or the compact equivalent), this contract and directly referenced evidence/locators. Set the header readiness value to `UNDER_REVIEW`; exclude sections 12–13 and every author/research-review verdict. Add review findings and the final readiness decision to the master pack only during reconciliation.

### PARTIAL or NOT_READY output

When any material evidence, feasibility, ownership, review, validation, or safety gate is open, sections 8–10 remain internal working state and are omitted from the terminal response. Return only:

1. strongest supported findings;
2. material blockers and affected downstream items;
3. `Next evidence` actions or a user decision request;
4. readiness status and the exact condition for re-evaluation.

Do not append sample OpenSpec prose, a provisional implementation plan, or a “supported tasks” list.

For `PARTIAL — awaiting context-pack approval`, every other READY checklist item already passes. Present the full pack so the user can approve its provenance, scope, requirement boundaries, and admissibility mappings. Candidate rows must use neutral IDs and traceability fields, not imperative task wording. Explicit approval changes the status to `READY`; only the downstream OpenSpec workflow may convert the mappings into tasks.
