---
name: n8n-agents-official
description: Use for n8n AI agents, LLM chains, classifiers, extractors, summarizers, embeddings, vector stores, tool calling, memory, RAG, structured output, or AI media nodes.
---

# n8n Agents

## Choose the surface

- Use a one-shot chain or task node for deterministic classify, extract, summarize, transform, or generate work that does not need tools.
- Use an Agent only when the model must choose among tools or plan across tool calls.
- Use RAG only when answers require retrieval from a corpus; use memory only for conversation state that must persist across turns.

## Invariants

- Connect model, memory, tools, and output parser through the correct AI sub-node ports. Fetch each live node type before configuring it.
- Treat tool names, descriptions, input schemas, and side effects as part of the agent prompt.
- Use typed sub-workflow tools for multi-step behavior. `fromAi()` descriptions must state meaning and constraints; do not expose binary directly through tool parameters.
- Keep secrets in credentials. Prevent prompt or tool output from exposing credentials or sensitive context.
- Wrap tools with user-visible side effects such as sends, payments, refunds, and account changes in human review. Existing conversational authorization avoids a duplicate build-time confirmation; it does not remove the workflow's runtime review unless the user explicitly changes that policy.
- Production structured output uses `outputParserStructured` with `autoFix: true` and a coding-capable fixer model. Validate the result at the boundary; do not assume the model always follows the schema.

## Workflow

1. Define the user-visible task, required output contract, allowed tools, side effects, and review policy.
2. Select agent versus one-shot node; add memory/RAG only when required.
3. Configure the model and sub-nodes from live types.
4. Write a focused system prompt and specific tool descriptions; separate agent-filled and workflow-supplied inputs.
5. Wire bounded error behavior for each tool and validate structured output.
6. Test happy path, ambiguous input, tool failure, forbidden/unauthorized action, and malformed model output before publish.

## Selective references

Read only what the design uses: [references/SYSTEM_PROMPT.md](references/SYSTEM_PROMPT.md), [references/TOOLS.md](references/TOOLS.md), [references/SUBWORKFLOW_AS_TOOL.md](references/SUBWORKFLOW_AS_TOOL.md), [references/STRUCTURED_OUTPUT.md](references/STRUCTURED_OUTPUT.md), [references/HUMAN_REVIEW.md](references/HUMAN_REVIEW.md), [references/MEMORY.md](references/MEMORY.md), [references/RAG.md](references/RAG.md), or [references/CHAT_AGENT_PATTERNS.md](references/CHAT_AGENT_PATTERNS.md). [references/DETAILED_GUIDE.md](references/DETAILED_GUIDE.md) preserves the original overview and examples.
