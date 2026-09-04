---
name: n8n-binary-and-data-official
description: Use when an n8n workflow uploads, downloads, transforms, stores, returns, or passes files, images, attachments, PDFs, or other binary data.
---

# n8n Binary and Data

## Invariants

- Binary lives in the item's binary slot under a named property; JSON expressions do not carry file bytes.
- Preserve both JSON metadata and binary properties through transformations and merges.
- Agent-tool inputs and outputs are JSON contracts. Stage files in accessible storage and pass a URL or storage key when binary must cross that boundary.
- A URL returned to a chat surface must be reachable by that client and have an appropriate lifetime and access policy.
- Never place secrets in file URLs, filenames, metadata, or node text.

## Workflow

1. Identify where bytes enter, their binary property name, MIME type, filename, and size constraints.
2. Fetch live types for each file-producing or file-consuming node and configure the expected binary property consistently.
3. When JSON context is lost, merge or explicitly restore it using stable item correspondence.
4. For agent tools, stage input or output binary and pass structured references; define cleanup and expiry when needed.
5. Test with a representative file and verify bytes, MIME type, filename, JSON context, and consumer accessibility.

## Stop rules

- Do not assume binary survives a node or sub-workflow boundary; inspect actual output.
- Do not return local or authenticated-only URLs to a client that cannot fetch them.
- Do not test uploads, sends, or storage writes beyond existing authorization.

## Selective references

- [references/BINARY_BASICS.md](references/BINARY_BASICS.md): item shape and binary operations.
- [references/MERGE_FOR_CONTEXT.md](references/MERGE_FOR_CONTEXT.md): preserving JSON with files.
- [references/AGENT_TOOL_BINARY.md](references/AGENT_TOOL_BINARY.md): staging across agent-tool boundaries.
- [references/CDN_REQUIREMENT.md](references/CDN_REQUIREMENT.md): chat-accessible downloads.
- [references/DETAILED_GUIDE.md](references/DETAILED_GUIDE.md): full examples and anti-patterns.
