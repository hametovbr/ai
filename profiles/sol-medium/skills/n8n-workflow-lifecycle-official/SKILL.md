---
name: n8n-workflow-lifecycle-official
description: Use when planning, creating, organizing, reviewing, testing, updating, publishing, unpublishing, or archiving an n8n workflow.
---

# n8n Workflow Lifecycle

## Delivery workflow

1. **Plan:** capture trigger, inputs, outputs, side effects, credentials, error behavior, placement, and acceptance criteria. Search for existing workflows and sub-workflows first.
2. **Design:** choose native nodes and patterns, name nodes by purpose, define contracts, and annotate non-obvious decisions.
3. **Configure:** read live SDK and node types; resolve instance IDs and credential bindings from discovery tools.
4. **Validate:** validate node configs and the full workflow, then run the applicable validation checklist.
5. **Verify and test:** fetch the saved workflow after every create/update, inspect actual connections and settings, then test representative success and failure cases with controlled inputs.
6. **Ship:** publish only after prior gates pass; report what was tested, what was pinned, side effects exercised, and any remaining limits.

## Invariants

- Validation alone does not prove connection indices, item pairing, external behavior, or side-effect safety.
- n8n fan-out branches execute sequentially by canvas order. Use explicit sub-workflow dispatch for true concurrency.
- A project is not a folder. Search existing folders before building; the installed MCP may be unable to create or move folders.
- MCP access is per workflow. UI-created workflows may require the user to enable it.
- Every created workflow needs a concise description that states what it does and why.
- Do not publish, unpublish, archive, execute live, or change access outside the user's authorization.

## Stop rules

- Stop before testing when any unpinned downstream node can cause an unauthorized real side effect.
- Stop before publish if validation, post-write retrieval, connection inspection, or required behavior tests fail.
- Do not claim completion from a saved draft when the requested outcome requires publication.

## Selective references

- [references/VALIDATION_CHECKLIST.md](references/VALIDATION_CHECKLIST.md): pre-publish gates.
- [references/TESTING.md](references/TESTING.md): pinning and real-side-effect boundaries.
- [references/REVIEW_CHECKLIST.md](references/REVIEW_CHECKLIST.md): audits of existing workflows.
- [references/NAMING_CONVENTIONS.md](references/NAMING_CONVENTIONS.md): workflow/node names and tags.
- [references/FOLDER_LIMITATIONS.md](references/FOLDER_LIMITATIONS.md): placement constraints.
- [references/MCP_ACCESS_PER_WORKFLOW.md](references/MCP_ACCESS_PER_WORKFLOW.md): discovery visibility.
- [references/DETAILED_GUIDE.md](references/DETAILED_GUIDE.md): execution model, readability, handoff, and original examples.
