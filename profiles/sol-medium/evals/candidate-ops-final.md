## N8N

Use a synchronous webhook workflow with this shape:

1. **Webhook → validate input.** Require an array represented as 100 items (and validate the fields used by the transform/lookup). Invalid input goes to one Respond to Webhook node with `400` and a sanitized `validation_error` body.
2. **Edit Fields/Set transform.** Apply the deterministic transform before the loop; ordinary n8n item processing already runs it once per item. Do not use Code unless the transform cannot be expressed safely.
3. **Loop Over Items, batch size 1.** The loop output processes one transformed item; the done output alone goes to aggregation. Batch size 1 plus a Wait of 200 ms after every attempted lookup gives at most five starts per second and makes per-item retry behavior unambiguous. Route the successful HTTP result through a result-normalizer, then Wait, then back to the loop.
4. **HTTP Request lookup.** Use the saved `vendorApi` credential reference. Do not paste, request, log, pin, export, or place its token in Code/headers. In an implementation session, discover the actual credential ID/type and live node shape before binding; the label alone is insufficient.
5. **Errors/retries.** Route the HTTP node’s error output to a classifier. For 429, parse a valid `Retry-After`, wait at least that long, then retry the same item; every retry is also paced and counted. Retry only read-only transient failures, with a proposed cap of 3 attempts per item and an overall execution-time budget. If `Retry-After` exceeds the remaining budget, or the cap is exhausted, record a sanitized failure result and do not claim success. Treat auth/permanent 4xx as non-retryable; bound 5xx/timeouts with backoff. All branches rejoin the loop without losing the item’s input identity/order.
6. **Finish once.** On the loop’s done output, aggregate all normalized results with `executeOnce`, preserve input order, and use one `Respond to Webhook` with `executeOnce`. Return `200` only when all 100 lookups succeeded; otherwise return a project-consistent `502/503` aggregate error with per-item safe error codes and no upstream bodies or secrets.

Verification is design-only: zero, one, and 100 items; deterministic transform; exactly one final response; output count/order; request timestamps never exceed five starts in any second; successful 429 retry honoring integer/date `Retry-After`; malformed/missing `Retry-After`; retry cap and total-time cutoff; 401/403 no retry; timeout/5xx; mixed success/failure; credential reference present and no secret-shaped parameter text. Exact node fields, connections, and runtime behavior remain unvalidated until live node discovery and workflow inspection are available.

## ORCH

Do not dispatch implementation yet. The repository signature is a prerequisite contract, and the dirty shared tree means `HEAD` does not identify the candidate.

**First wave: two read-only Luna Max workers**, leaving four slots unused. Each brief specifies `model: gpt-5.6-luna`, `reasoning_effort: max`, `fork_turns: none`, no children, absolute workspace, approved change/scenario IDs, and report path.

- **D1, repository contract discovery:** inspect the repository interface, call sites, tests, legacy behavior, and expected opaque-cursor input/output/error contract. Report the narrow writable paths and decisive checks. Stop rather than invent the unspecified signature.
- **D2, endpoint/generator discovery:** inspect endpoint compatibility requirements, SDK generation source/command/output ownership, required gates, and the existing `service.py` user diff. Produce an attributable baseline (commit plus dirty/untracked snapshot) and identify collisions; make no edits.

Accept discovery only after primary inspection of the cited code/diffs confirms an implementable signature, preserved legacy cases, exact ownership, dependencies, and commands. A report is evidence, not acceptance.

Then serialize writers in the shared tree: repository implementation first; endpoint only after repository output is accepted; generated SDK only after the endpoint schema/contract is accepted. Prefer a separate clean worktree only if it can include an explicit snapshot of required user edits; otherwise keep one writer and narrowly protect `service.py`. Each unit must prove opaque-cursor progression/termination, malformed/stale cursor behavior, and legacy behavior. Reject the offset suggestion: it changes the approved design and invalidates dependent briefs; send any desired redesign back to planning.

H1’s PASS is stale after the integration edit created H2. Reopen affected units and assign the semantic integration fix to one bounded Luna worker after all other writers stop; the primary agent performs only mechanical integration. The fixer must preserve the recorded user edits and return an H2 snapshot plus targeted evidence.

Record `make check` as `BLOCKED/NOT_RUN`, never PASS. Identify the missing dependency and installation policy; restore it through the repository’s approved setup path, or report the capability gap. Then run targeted checks and the required `make check` under primary control against frozen H2 (or its successor), recording command, cwd, candidate identity, exit status, and logs. Do not accept repository, endpoint, SDK, integration, or close OpenSpec tasks until final integrated checks and scenario review pass on the same candidate.
