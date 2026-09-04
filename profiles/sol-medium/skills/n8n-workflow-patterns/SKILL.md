---
name: n8n-workflow-patterns
description: Use when selecting or reviewing the architecture for a new n8n workflow, integration, automation, batch process, or performance-sensitive data flow.
---

# n8n Workflow Patterns

Choose one primary pattern, then add only the cross-cutting behavior the workflow needs.

## Pattern router

| Trigger or goal | Primary guide |
|---|---|
| Receive and respond to an inbound request | [webhook_processing.md](webhook_processing.md) |
| Call one or more external APIs | [http_api_integration.md](http_api_integration.md) |
| Query, synchronize, or update a database | [database_operations.md](database_operations.md) |
| Agent, LLM, tools, memory, or RAG | [ai_agent_workflow.md](ai_agent_workflow.md) |
| Cron, polling, reports, or maintenance | [scheduled_tasks.md](scheduled_tasks.md) |
| Large item sets, batching, or pagination | `n8n-loops-official` plus the relevant guide above |

## Selection workflow

1. Define the trigger, data volume, latency, side effects, retry/idempotency needs, and output contract.
2. Select the primary pattern from the table and read only that guide.
3. Load the applicable official domain skills for nodes, expressions, credentials, errors, loops, sub-workflows, binary, Data Tables, or AI.
4. Search for existing workflows and reusable sub-workflows.
5. Design the success path and failure paths together. Keep transforms near their consumers unless they form a reusable contract.
6. Validate, fetch the saved workflow to verify connections, and test success plus material failure/volume cases before publishing.

## Invariants and stop rules

- Use live SDK/node schemas rather than copied examples as configuration truth.
- Do not mistake fan-out branches for concurrency or add Loop Over Items for default per-item behavior.
- Bound pagination, polling, retries, and batches; preserve idempotency for repeatable writes.
- Do not publish with unhandled production failures or execute unauthorized side effects.
- Stop and re-evaluate the pattern when the data volume, response-time requirement, or side-effect model contradicts its assumptions.

## Selective reference

Read [references/DETAILED_GUIDE.md](references/DETAILED_GUIDE.md) for component catalogs, performance heuristics, integration gotchas, quick-start examples, template names, and the original checklists. Treat examples as patterns, then confirm current node parameters live.
