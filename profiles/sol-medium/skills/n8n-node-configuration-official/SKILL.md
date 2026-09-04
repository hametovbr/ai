---
name: n8n-node-configuration-official
description: Use whenever configuring or debugging an n8n node, its operation, parameters, settings, resource locators, or input connections.
---

# n8n Node Configuration

## Invariants

- Never configure a node from memory. Fetch its live type for the exact node, resource, operation, and mode.
- Set discriminators first, then only the fields active for that discriminator path. Do not copy stale parameters between operations.
- Discover resource-locator and load-option values from the instance; do not invent IDs.
- Treat credentials as credential bindings, never text parameters.
- Validation is necessary; post-write retrieval and runtime testing verify the saved behavior.

## Workflow

1. Identify the required capability and search for the best native node.
2. Read best practices for the technique when available.
3. Call `get_node_types` with the exact discriminators.
4. If parameters depend on remote values, call `explore_node_resources` with an accessible credential ID and current parent parameters.
5. Build the minimum operation-aware config. Set node settings such as retry, `onError`, and `executeOnce` deliberately.
6. Run `validate_node_config`, then full workflow validation.
7. After create/update, fetch the workflow and inspect saved parameters and connection indices. Test with representative data before publish.

## Stop rules

- Stop and re-fetch the type when validation reveals an unknown or inactive field; do not guess around it.
- Do not execute or publish merely because schema validation passes.
- Do not run a node with real external effects outside existing authorization.

## Selective references

Read only the relevant node-family file in `references/`: `HTTP_NODES.md`, `WEBHOOK_NODES.md`, `DATABASE_NODES.md`, `COMMS_NODES.md`, `AI_NODES.md`, `TRIGGER_NODES.md`, `MERGE_NODE.md`, or `SWITCH_FALLBACK.md`. Read [references/DETAILED_GUIDE.md](references/DETAILED_GUIDE.md) for the complete operation and dependency examples.
