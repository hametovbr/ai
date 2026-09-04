# Retry/response decision

Do **not** clamp `Retry-After` and do **not** retry during this webhook execution. The valid upstream minimum wait is 120 seconds, while only 30 seconds remain; waiting 10 seconds and retrying would violate the upstream instruction, and two retries would also consume the same rate budget.

End the lookup’s error branch at **Respond to Webhook** with an explicit dependency-failure response:

- HTTP status: **503 Service Unavailable**
- Header: **`Retry-After: 120`** (or the correctly recalculated remaining value if time has elapsed since receipt)
- Body: a stable, non-sensitive error such as `{"error":"dependency_rate_limited","retry_after_seconds":120}`
- Execution outcome: recorded as a handled failure, never success

If the workflow already supports durable asynchronous deferral, it may instead enqueue/defer the lookup until **no earlier than 120 seconds** and return the documented asynchronous acceptance response. It must not improvise that behavior inside this synchronous request.

Evidence still missing before enabling any later automatic retry:

- confirmation that the lookup is truly read-only and safe to repeat;
- the upstream rate-limit policy, including whether `Retry-After` is seconds or a date and how retries count;
- proof that the caller contract accepts the chosen 503 body/header, or documentation for an asynchronous 202 contract;
- proof that the node error output reaches Respond to Webhook and that logs omit credentials and sensitive payloads;
- success, 429, malformed-header, and exhausted-budget branch test results.
