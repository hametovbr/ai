---
name: n8n-loops-official
description: Use for n8n multi-item processing, per-item versus all-items behavior, batching, API pagination, rate limits, or concurrency.
---

# n8n Loops

## Decision order

1. Default n8n iteration: most nodes already run once per input item. Use this for ordinary “do X for each item.”
2. `executeOnce`: use when a downstream node must fire once total.
3. Aggregate or all-items expression/code: use when one operation needs the complete array.
4. HTTP Request pagination: use for APIs that expose pages/cursors.
5. Loop Over Items: use only for real batching, delay/rate control, or cross-iteration state.
6. Sub-workflow dispatch: use `mode: 'each'` when each item requires an independent sub-execution. Use `waitForSubWorkflow: false` only with explicit completion/error tracking.

## Invariants

- Do not add Loop Over Items merely to make downstream nodes process each row; that is already the default.
- Set `executeOnce: true` for every once-per-run node, including dataset-wide `$input.all()` / `.all()` aggregation, single notifications, aggregate writes, responses, and summaries. Keep it off when `.all()` supports a real per-item lookup through another node's `.item`.
- n8n fan-out branches and ordinary item iteration are sequential. Do not promise concurrency from canvas shape.
- Nested Loop Over Items in one workflow is unsafe; move the inner loop to a sub-workflow.
- Bound pages, batches, retries, and polling with a clear termination condition.

## Verification

Use representative zero-, one-, and many-item inputs. Verify invocation count, final item count/order, pagination termination, rate behavior, and any completion tracking before publish.

## Stop rules

- Stop if the API's page/cursor termination rule is unknown.
- Do not launch fire-and-forget work without durable status/error tracking and a timeout.
- Do not run repeated side effects beyond existing authorization.

## Selective references

Read [references/LOOP_OVER_ITEMS.md](references/LOOP_OVER_ITEMS.md) for batching/state and [references/HTTP_PAGINATION.md](references/HTTP_PAGINATION.md) for page/cursor patterns. Read [references/DETAILED_GUIDE.md](references/DETAILED_GUIDE.md) for `executeOnce`, scenario examples, and anti-patterns.
