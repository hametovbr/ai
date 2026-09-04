---
name: n8n-code-nodes-official
description: Use when considering, writing, or reviewing custom JavaScript or Python in an n8n Code node.
---

# n8n Code Nodes

## Decision gate

Use the least complex supported surface:

1. A direct expression for one parameter.
2. Edit Fields with an expression or arrow-function IIFE for field shaping.
3. A native node for service, crypto, XML, parsing, or transformation capabilities it already provides.
4. A sub-workflow for reusable domain logic.
5. A Code node only for whole-dataset aggregation, stateful multi-step logic, or a required library/capability unavailable above.

## Invariants

- Default to JavaScript. Use Python only when the user requests it or the task specifically requires it.
- Choose “Run Once for Each Item” versus “Run Once for All Items” from the data contract; never rely on a remembered default.
- Return valid n8n items with the required JSON shape and preserve binary explicitly.
- Do not put credentials, secrets, or unbounded network/retry loops in code.
- Prefer the Crypto node for cryptographic operations and the XML node for XML/SOAP/RSS parsing.

## Workflow

1. State why expressions, Edit Fields, native nodes, and sub-workflows are insufficient.
2. Define input/output shapes and execution mode.
3. Write the smallest JavaScript implementation using available runtime libraries only after verifying availability.
4. Test empty, single-item, multi-item, malformed-input, and binary cases that apply.
5. Verify downstream expressions receive the intended item pairing and shape.

## Stop rules

- Stop and replace Code when a simpler native surface satisfies the requirement.
- Do not assume external modules are installed.
- Do not execute side-effecting code outside existing authorization.

## Selective references

Read [references/DECISION_TREE.md](references/DECISION_TREE.md) for the full choice matrix, [references/ARROW_FUNCTIONS_IN_EDIT_FIELDS.md](references/ARROW_FUNCTIONS_IN_EDIT_FIELDS.md) before choosing Code for mapping, and [references/JAVASCRIPT_PATTERNS.md](references/JAVASCRIPT_PATTERNS.md) once Code is justified. [references/DETAILED_GUIDE.md](references/DETAILED_GUIDE.md) preserves the original worked examples.
