---
name: n8n-subworkflows-official
description: Use when n8n logic is reusable, independently testable, shared across workflows, used as an agent tool, or a larger workflow needs deliberate modular boundaries.
---

# n8n Sub-workflows

## Invariants

- Search before building using `subworkflow`, domain, and `tool` tags plus relevant keywords. Reuse a suitable workflow instead of duplicating it.
- Prefer stateless input-to-output behavior. If the workflow reads or writes state, make the side effect explicit in its name, description, contract, retry behavior, and output.
- Use Execute Workflow Trigger “Define Below” with typed fields. Use passthrough only for binary input or a genuine zero-input workflow; a binary passthrough workflow cannot be a direct parameterized agent tool.
- Treat inputs and outputs as an API. Document them, migrate all callers for breaking changes, and return natural domain shapes.
- Use a final Return/Edit Fields boundary when it clarifies or enforces the output contract.
- Split genuinely different input contracts such as binary versus JSON, sync versus async, or distinct auth schemes into separate outer sub-workflows with a shared normalized core.

## Workflow

1. Confirm the boundary earns a sub-workflow through reuse, isolation, independent testing, an agent-tool contract, or a coherent state operation. For canvas readability alone, use node groups.
2. Search existing workflows and tags.
3. Define typed inputs, outputs, errors, side effects, and idempotency.
4. Choose caller mode: `all` for one invocation with all items, `each` for one invocation per item. Keep waiting enabled unless deliberate async dispatch has durable completion/error tracking.
5. Build, tag, validate, test independently, then verify every caller's saved connections and input mappings.

## Stop rules

- Do not create an untagged duplicate or a vague “Helper” workflow.
- Do not use passthrough to avoid defining a real JSON contract.
- Do not change a shared contract until all callers are identified and included in the migration.
- Do not use fire-and-forget dispatch without status tracking, timeout, and failure handling.

## Selective references

Read [references/NAMING_AND_DISCOVERY.md](references/NAMING_AND_DISCOVERY.md) for search/tag/project rules and [references/SUBWORKFLOW_PATTERNS.md](references/SUBWORKFLOW_PATTERNS.md) for input-shape splitting, async dispatch, and completion tracking. Read [references/DETAILED_GUIDE.md](references/DETAILED_GUIDE.md) for extraction examples, stateless/stateful patterns, input details, and call modes.
