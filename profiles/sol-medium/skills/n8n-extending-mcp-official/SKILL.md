---
name: n8n-extending-mcp-official
description: Use to expose an n8n workflow as an agent-callable tool or to wrap an n8n API capability missing from the installed MCP.
---

# n8n Extending MCP

Use this only after confirming the installed MCP does not already provide the capability, or when the requested outcome is explicitly a reusable agent-callable workflow.

## Authorization and security

- Creating the wrapper or tool workflow requires user authorization because it mutates their n8n instance. Existing authorization for that exact build is sufficient; do not ask twice.
- Use n8n credentials for every secret. Return credential metadata only, never values.
- Name and describe every side effect so a caller can distinguish reads from sends, writes, deletes, or bulk actions.
- Destructive or bulk wrappers need per-call explicit opt-in and a dry-run that lists targets.

## Workflow

1. Search native MCP tools and existing workflows tagged `tool`; reuse a suitable one.
2. Define typed Execute Workflow Trigger inputs and a structured output contract. Prefer a stateless read-only wrapper for MCP gaps.
3. For an n8n API wrapper, verify the current official endpoint and use the `n8nApi` or appropriate credential.
4. Build, validate, test within authorized side effects, fetch the saved workflow to verify wiring, then publish.
5. Confirm MCP access is enabled. Future agents discover with `search_workflows` and invoke with `execute_workflow` after reading the workflow input schema.
6. Offer to document the tool in the user's agent context only when useful; editing that separate file requires authorization unless already included.

## Stop rules

- Stop if the native MCP already supports the operation.
- Do not build a surprise workflow, expose a secret, or hide a side effect.
- Do not publish until the callable contract and error behavior are tested.

## Selective reference

Read [references/DETAILED_GUIDE.md](references/DETAILED_GUIDE.md) for current gap examples, folder and instance wrappers, discovery mechanics, and anti-patterns. Re-check live MCP capabilities because this list can drift.
