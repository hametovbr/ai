# N8N

Use this flow, subject to confirming the installed node schemas before implementation:

1. **Webhook** receives the 100 JSON items and performs up-front shape validation. Invalid caller data returns `400` with a structured `validation_error` body.
2. **Loop Over Items**, batch size 5, provides explicit rate control. Wire output 1 (loop) through the body and back to the loop; wire output 0 (done) only to the final response path.
3. In the loop body, use **Edit Fields** with an expression for the deterministic transform. A Code node is unnecessary, and the raw token must never be pasted into Code, headers, variables, or workflow JSON.
4. **HTTP Request** performs the read-only lookup once per item using the saved `vendorApi` credential. At implementation time, list credentials by the required type and bind the unique matching credential ID; if the label is ambiguous or its auth type is incompatible, stop for selection/correction rather than guessing. Do not expose or recreate the secret.
5. After each five-item batch, **Wait** one second, then feed back to Loop Over Items. This caps dispatch at five requests per second without relying on apparent branch parallelism.
6. For a 429, preserve the current item, parse a valid `Retry-After` value, wait that duration, and retry the lookup with a bounded attempt count (maximum 3). Reject malformed/negative delays and apply a documented ceiling. Other upstream failures, or exhausted 429 retries, leave the loop and reach one sanitized error responder. Because exact error/header output shapes vary, verify those against the installed HTTP node before configuring this branch.
7. The done output contains all successful per-item results. Build one aggregate object/array there and invoke **Respond to Webhook** once (`executeOnce` on any node that reads all inputs). Return `200` and JSON. No success responder is reachable from the loop output.

Set the HTTP node to `onError: continueErrorOutput`; wire output 1 to the retry/error handler. A terminal upstream error returns `502`, timeout `504`, and persistent upstream throttling `503`, using `{error, message}` without upstream bodies, stack traces, or credentials. For production, configure a published workflow-level error workflow as a catch-all.

Verification cases: 100 valid items produce exactly 100 transforms/lookups and one ordered aggregate response; boundary timing never starts more than five calls in any one-second window; 429 with seconds and HTTP-date `Retry-After` waits then succeeds; malformed `Retry-After` and a fourth 429 terminate predictably; non-429 upstream failure returns one sanitized 5xx; invalid input returns 400 before any lookup; credential binding contains only an ID/name reference. Finally inspect the saved graph for loop/done indexes, feedback edge, `onError`, error-output wiring, and absence of secret-shaped text. These are planned checks, not executed validation.

# ORCH

Do not dispatch implementation yet. The repository-to-endpoint contract is unsettled, code is unavailable, and the shared tree contains user work in `service.py`; those facts make repository and endpoint units unready and unsafe to parallelize.

The first wave is one bounded, read-only Luna discovery worker, leaving five slots free. Dispatch with `fork_turns: "none"`, model `gpt-5.6-luna`, reasoning effort `max`. Its brief should identify the repository signature and compatibility behavior from approved artifacts/current code, repository and endpoint test entry points, whether the `service.py` edit is relevant to the baseline, the exact SDK generation command and generated-file ownership, required checks, and the missing dependency. It must return evidence and make no edits or design choices.

After primary verification of that report, use one writer at a time in the shared tree. First assign repository behavior plus focused opaque-cursor and legacy-compatibility tests. Accept only after inspecting its attributable diff and running the decisive focused checks on the recorded candidate. Next assign endpoint behavior against the accepted repository signature, including compatibility/error cases. Only after the endpoint/source contract is accepted should one owner regenerate the SDK and run generated-output plus integration checks. Six slots are capacity, not a target.

Preserve the user's `service.py` change with a documented pre-work snapshot and explicit baseline decision. Workers may not reset, clean, stash, switch branches, stage everything, commit user work, or overwrite it. If `service.py` overlaps required endpoint edits, stop writers and create an isolated candidate that intentionally includes the snapshot, or serialize a narrowly attributed edit.

Reject the suggestion to replace cursor pagination with offset: it contradicts the approved opaque-cursor design and legacy-preservation constraint. A worker cannot redesign the change.

`PASS` on H1 does not accept H2. The later integration edit invalidates every affected check, and the missing-dependency `make check` is `NOT_RUN/BLOCKED`, never PASS. Assign semantic integration or conflict repair to a new bounded Luna fix unit after other writers stop; use the same worker only for a local correction within its original scope. The primary performs mechanical integration and final acceptance. Restore/install the dependency only if authorized by repository policy, then rerun `make check` and affected focused/integration checks on immutable H2 (or its repaired successor). If restoration is impossible, keep dependent units and the OpenSpec checkboxes blocked, record exact command/cwd/candidate/reason, and do not claim completion. After two failed corrections under the same brief, diagnose and revise/split the unit before any further dispatch.
