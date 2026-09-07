# Planning-rules maintenance — 2026-09-07

## Decision and scope

Apply the user's approved targeted changes to four existing skills in `skills/` and this profile: preparing-openspec-context, resolve-ambiguous-tasks, challenging-architecture-decisions and orchestrating-openspec-luna. No new skill, runner or test infrastructure. Source input: user-supplied screenshots of https://www.reddit.com/r/OpenaiCodex/comments/1w967sn/astras_plans_got_too_heavy_during_development_so/ . The separate quoted shared principle was not readable; no wording was inferred from it.

Counterfactual: repository 59eb3938fe529179f3da3871ab6744b24a1308d9. Candidate identity: the skill hashes in the adjacent current SOURCE_SNAPSHOT.tsv and PROFILE_SNAPSHOT.tsv. Original model-profile evidence is historical and has not been rerun wholesale.

Decision rule: the concrete Light reviewer blocker must disappear; material security/contract/evidence requirements and scope boundaries must remain; resolve material consistency findings before saving. Use the existing scripts and reviewed case records. No general reliability, latency, cost or skill-selection claim is sought.

## Method and limits

Fresh subagent threads with no conversation fork, existing runtime/model inherited (no explicit target-model override; provider snapshot not exposed). Baseline agent `baseline_cases` and candidate agent `candidate_cases` received the same six fixtures and read raw and profile versions; only file contents differed. Forced-loaded, read-only dry decisions, no real application code, credentials or external side effects. Six cases shared one thread per condition and raw/profile inspection, so they are dependent qualitative observations. One paired pass; no statistical inference or Sol-medium performance claim.

The primary agent manually assessed the responses against required scope, evidence, authorization and completion boundaries. The cases informed this maintenance and are validation-as-decision, not held-out tests. Baseline cases 3–6 already produced sound decisions; added explicit wording is not evidence of improved success rate. The additional review probe and consistency review below are separate non-paired checks.

## Fixed cases and observed decisions

| Case/input | Baseline response | Candidate response |
| --- | --- | --- |
| Verified sole UI-label location; Light; routine preparation authorized; no isolated reviewer; OpenSpec draft requested | Both trees block on mandatory isolated research/readiness reviews. | Both use compact note, direct scope/evidence check and current validator; reviewer unavailability no longer blocks. Actual context-pack approval remains a distinct existing gate before downstream authoring. |
| Same small Markdown task now changes deployment DB credentials/privileges | Escalate to High by security/production effect; retain reviews and evidence. | Same; small diff does not relax privilege verification, and unavailable required reviewer blocks. |
| Approved concurrent-save semantics; helper extraction merely suggested; existing focused test; optional 40-minute suite | Permit verified equivalent inline method and focused acceptance. | Same, now with explicit binding/method distinction and plan-linked check/rerun rationale. Profile still defaults material persistence changes to fresh review. |
| Full suite stops before assertions on expired credentials; no correction; two retries available | Classify BLOCKED/NOT_RUN; diagnose/restore access before repeat. | Same; explicitly refuses spending retries on unchanged conditions. |
| H1 pass; H2 changes shared transaction config; assertion checks only non-null | Reopen affected acceptance; correct duplicate-effect assertion and check H2. | Same; assesses shared config impact, broadens if unclear, rejects non-discriminating assertions. |
| Two clean architecture reviews; no new evidence for a third; optional dashboard proposed | Stop at supported sufficiency; omit dashboard and third review. | Same; explicitly reopens only on new evidence, changed requirements or concrete defects. |

Additional fresh `challenge_check` application: native scheduler configuration already satisfies requested run time; proposal adds dashboard, new end-to-end harness and a full suite after every edit. Response: revise to native configuration and focused firing-time/timezone checks, remove unsupported additions and duplicate review, retain binding project gates. New concrete privilege escalation reopens affected acceptance.

## Consistency review and correction

Fresh read-only `consistency_review` inspected the diff and references. It found one P2 regression: shortened OpenSpec review wording had removed the ban on interactive grilling fallback while inherited rules still referenced grilling. Restored the explicit compatible-isolated-reviewer requirement and exclusion of interactive fallback in both entrypoints. A focused follow-up confirmed resolution; no other material findings were reported. This textual correction preserves the already tested isolation contract; the entire six-case group was not repeated after this guard restoration.

## Deterministic checks

- Eight changed entrypoints parse as YAML and preserve name/description.
- Both editable installed personal skills pass the existing quick validator.
- Both existing workflow validators accept a concrete compact Light READY record and reject the same record with an open material unknown.
- No validator implementation was changed.
- Local Markdown links, whitespace and refreshed snapshot hashes are checked before save.

## Disposition

Accept as a bounded instruction-maintenance change with the observed Light gate improvement and retained case boundaries. General effectiveness remains INSUFFICIENT_EVIDENCE. Explicit context-pack approval was retained; this update does not claim to remove every approval-friction point.

Installed-copy scope: the editable personal copies of challenging-architecture-decisions and orchestrating-openspec-luna receive the raw-source update. preparing-openspec-context and resolve-ambiguous-tasks are supplied outside the editable personal checkout in this session; their GitHub raw/profile versions are updated, but their installed copies cannot be modified through the available supported ownership path.
