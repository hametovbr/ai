---
name: n8n-error-handling-official
description: Use for webhook, scheduled, production, unattended, or otherwise failure-prone n8n workflows where errors must be surfaced and handled.
---

# n8n Error Handling

## Invariants

- A production path must not silently discard failures or return success after a failed operation.
- In API workflows, wire every fallible node's error output and end both success and failure paths at Respond to Webhook. Map caller/input errors to 4xx and dependency/execution failures to 5xx.
- Retry only operations that are safe to repeat, with bounded attempts and backoff. Preserve idempotency for writes.
- Honor a valid upstream `Retry-After` as a minimum wait. If it exceeds the remaining execution or retry budget, stop or defer with an explicit outcome; never clamp it downward and retry earlier. Count retries in the same rate budget as initial requests.
- Error handlers must not expose credentials, tokens, or sensitive payloads.

## Workflow

1. Classify the workflow surface: synchronous API/webhook, scheduled/unattended, or interactive/manual.
2. List fallible nodes and classify their failures as caller, transient dependency, permanent dependency, or internal logic errors.
3. Configure node-level error outputs and bounded retries where safe.
4. For request/response workflows, validate input early and converge all branches to an explicit response shape and status.
5. For every unattended workflow, set a workflow-level error workflow. The target must be published and contain an active Error Trigger.
6. Test a success case and each material failure branch. Verify the actual response/output and execution state before publishing.

## Stop rules

- Do not publish while a fallible production path can end without an observable result.
- Do not add automatic recovery that can duplicate a send, charge, insert, or other non-idempotent side effect.
- Do not run live failure tests with real side effects unless already authorized.

## Selective references

- [references/API_WORKFLOWS.md](references/API_WORKFLOWS.md): webhook validation, convergence, and response design.
- [references/NODE_ERROR_OUTPUTS.md](references/NODE_ERROR_OUTPUTS.md): per-node settings and wiring.
- [references/RESPONSE_SHAPES.md](references/RESPONSE_SHAPES.md): status and body mapping.
- [references/ERROR_WORKFLOWS.md](references/ERROR_WORKFLOWS.md): workflow-level handlers.
- [references/DETAILED_GUIDE.md](references/DETAILED_GUIDE.md): original examples and anti-patterns.
