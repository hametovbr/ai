# Sol medium behavioral and structural checks

Historical results for the original profile. Its exact skill hashes remain in the [snapshot at 59eb3938](https://github.com/hametovbr/ai/blob/59eb3938fe529179f3da3871ab6744b24a1308d9/profiles/sol-medium/PROFILE_SNAPSHOT.tsv). The current snapshot includes later changes; see [planning-rules-review.md](planning-rules-review.md) for their separate, limited checks.

## Decision and scope

Accept the profile as a reviewed instruction adaptation with bounded regression
coverage. Do **not** claim model-wide superiority, measured speed/cost improvement,
or production readiness. The source skills often already yielded correct behavior.

Configured model: `gpt-5.6-sol`, effort `medium`, fresh `fork_turns: none` threads.
The runtime accepted these explicit settings; a provider-resolved model snapshot
was not exposed. Cases force-loaded the named skills, so no natural skill-selection
claim is supported. Full settings, budgets, grouping and limitations are in
[run-config.json](run-config.json); task inputs and mandatory invariants are in
[cases.json](cases.json).

The primary agent manually assessed actual responses against the stated
invariants. This is reviewed fixed-case evidence, not a calibrated independent
human benchmark. Cases shared a thread within each group, in the same order for
baseline and candidate; they are not independent population samples.

## Paired observations

| Case | Source behavior | Final profile behavior | Supported conclusion |
| --- | --- | --- | --- |
| N8N | Used batching for throttling, credentials, explicit failures and one response. Delay-cap wording did not state what happens when a valid Retry-After exceeds the time budget. | Preserved those boundaries and explicitly stops retrying when the minimum wait exceeds the remaining budget; retries count toward pacing. | Required design decisions retained; retry-budget ambiguity resolved in this response. No actual timing/graph execution proof. |
| ORCH | Discovery before implementation, Luna Max role, dirty baseline protection, H1/H2 distinction, blocked check prevents completion. | Same invariants; chose two read-only discovery units instead of one, then serialized writers. | Mandatory execution boundaries retained; differing safe scheduling choices are not graded as failures. |
| RFC | Drafted immediately with honest unknown metadata, criteria, alternatives/status quo and pending outcome. | Same decision-document behavior with no blocking questionnaire or claimed approval. | No regression observed; baseline already met the case. |
| ARCH | Rejected unsupported distributed infrastructure and chose existing scheduler/PostgreSQL. | Same minimal design and evidence boundary; named an external-side-effect hinge. | No regression observed; no general architecture-quality uplift established. |
| DOCS | Preserved pinned version, official-source fallback, no installation or invented fetched result. | Same constraints and explicit unresolved documentation location. | No regression observed; baseline already handled unavailable Context7 correctly. |
| LIGHT | Used Light implementation readiness, no extra approval/review blocker, proportional inspection/render checks. | Same scope and authorization behavior. | No regression observed; runtime/user constraints already prevented original over-ceremony. |
| DB | Rejected unconditional zero-downtime, lossless-down and FK-index promises. | Same engine/workload-dependent conclusions and explicit validation needs. | No regression observed; shortened guidance is not evidence of better database expertise. |

Response artifacts:

- Baseline: [operations](baseline-ops.md), [general](baseline-general.md), [boundaries](baseline-boundaries.md).
- Final candidate: [operations](candidate-ops-final.md), [general](candidate-general.md), [boundaries](candidate-boundaries.md).
- Initial operations candidate: [candidate-ops-v1.md](candidate-ops-v1.md), retained to expose the refinement history.

## Disclosed refinement

The first operations candidate also used ambiguous “cap/validate unreasonable delay
values” language. After inspecting it, the n8n error-handling skill gained an
explicit rule: a valid Retry-After is a minimum, not a value to clamp downward;
when it exceeds budget, stop or defer with an explicit outcome. The final
operations group was rerun against the changed instructions.

An additional [retry-budget probe](retry-budget.md) supplied Retry-After 120 seconds
with only 30 seconds left. The response refused early retries, returned an explicit
503 design, and allowed asynchronous deferral only if that contract already
exists. This is targeted regression evidence after tuning, not an untouched
hold-out set or an extra paired baseline comparison.

## Deterministic checks

- All 36 skill entrypoints passed `quick_validate.py`.
- All original source resource paths remain present in the profile.
- Raw backup hashes still match `SOURCE_SNAPSHOT.tsv`.
- No unresolved substantive local Markdown links remain; fenced examples and URL placeholders were reviewed separately.
- One bundled script changed: `resolve-ambiguous-tasks/scripts/validate_workflow_artifacts.py`. Concrete Light readiness still passes; open material unknowns and undefined evidence still fail. The old script accepted the unresolved `{named action}` template, while the adapted script correctly rejects it.

See [structural-results.json](structural-results.json),
[validator-cases.json](validator-cases.json), and
[validator-results.json](validator-results.json). Candidate skill-file identity is
recorded in [PROFILE_SNAPSHOT.tsv](../PROFILE_SNAPSHOT.tsv).

## Verdict

**PASS — limited adaptation acceptance:** structural integrity, retained resources,
script regression checks, and sampled forced-loaded behavioral boundaries support
publishing this profile for use and further observation.

**INSUFFICIENT_EVIDENCE — general improvement:** no broad reliability, accuracy,
latency, cost, automatic selection, live n8n execution, database load, or end-to-end
OpenSpec implementation claim is established. Unchanged scripts and external
services were not executed. Seven original cases were used for low-risk
validation-as-decision; one case informed a disclosed refinement.
