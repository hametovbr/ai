---
name: using-n8n-skills-official
description: Use for any n8n workflow task to route to the relevant official n8n skills and apply the shared build, verification, credential, and execution rules.
---

# Using n8n Skills

Use this router before the first n8n design decision or MCP action. Load only the domain skills triggered by the current task; add another when its trigger appears.

## Required protocol

1. Route from the index below and read the primary skill before acting.
2. Before SDK code, read the live `get_sdk_reference`; before configuring a node, fetch its live shape with `get_node_types`. Live tool output wins when it conflicts with a skill; report the drift.
3. Search before creating reusable workflows. Use exact instance values from discovery tools rather than invented IDs or options.
4. Keep every secret in n8n credentials, never node text, expressions, SDK code, or output.
5. Before create/update, validate. After create/update, fetch `get_workflow_details` and inspect actual connections. Before publish, complete the lifecycle checklist and required testing.
6. Pass every skill used since the prior successful create/update in `skillsUsed`, preserving the exact skill name.

## Route by decision

| Need | Load |
|---|---|
| Plan, create, organize, review, test, or publish | `n8n-workflow-lifecycle-official` |
| Configure a node or connection | `n8n-node-configuration-official` |
| Expressions, mapping, dates, or transformation | `n8n-expressions-official`; add `n8n-code-nodes-official` only if expressions cannot do it |
| Reuse, modularity, or a workflow over about 10 nodes | `n8n-subworkflows-official` |
| Items, batching, pagination, or concurrency | `n8n-loops-official` |
| Webhook, scheduled, unattended, or failure-prone execution | `n8n-error-handling-official` |
| Auth, tokens, or third-party services | `n8n-credentials-and-security-official` |
| Files or binary | `n8n-binary-and-data-official` |
| Data Tables or persistent workflow state | `n8n-data-tables-official` |
| AI nodes, agents, tools, memory, RAG, or structured LLM output | `n8n-agents-official` |
| Failure investigation | `n8n-debugging-official` |
| Expose a workflow as an agent-callable tool or fill an MCP capability gap | `n8n-extending-mcp-official` |
| Choose an architecture pattern | `n8n-workflow-patterns` plus the relevant domain skill |

## Execution and authorization stop rules

- `test_workflow` mocks only specified surfaces; downstream sends, writes, commands, file operations, and sub-workflows may run for real. Inspect the test plan and obtain authorization when a real side effect is not already authorized.
- Use `execute_workflow` with `executionMode: "manual"` for deliberate testing and `"production"` only for an intentional live run. Poll the returned execution ID.
- Do not publish until validation, post-write verification, and the applicable runtime tests succeed.
- Do not treat a passed validator as proof that connections, item pairing, side effects, or business behavior are correct.
- Do not ask again for an action the user already authorized; keep within that authorization's scope.

## Selective references

Read [references/DETAILED_GUIDE.md](references/DETAILED_GUIDE.md) only when you need the full MCP tool catalog, red-flag examples, `skillsUsed` format, review routing, or MCP-access troubleshooting.
