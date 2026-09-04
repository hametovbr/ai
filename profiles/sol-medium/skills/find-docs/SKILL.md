---
name: find-docs
description: Retrieve current official documentation, API references, and code examples for a named developer library, framework, SDK, CLI, or cloud service. Use for version-sensitive syntax, configuration, migration, setup, debugging, and library-specific how-to questions. Prefer this workflow to memory or general web results; do not use it for questions that are independent of a particular technology.
---

# Documentation Lookup

Ground the answer in current, version-matched documentation. Never include secrets, private code, personal data, or internal identifiers in a remote documentation query.

## Procedure

1. Extract the technology, task, and requested version from the user or project files. Ask only when ambiguity would change the answer.
2. Prefer an available documentation retrieval tool. If Context7 is available, resolve a library ID and then query it:

   ```bash
   npx ctx7@latest library <name> "<focused query>"
   npx ctx7@latest docs <libraryId> "<focused query>"
   ```

   Skip resolution only when the user supplied a Context7 ID such as `/org/project` or `/org/project/version`.
3. Select an exact official match when possible. When a version was specified, use its versioned docs or the closest indexed version and disclose any mismatch.
4. Query one topic at a time. Use the user's intent and relevant error text, stripped of sensitive values, instead of vague keywords.
5. If the documentation tool or CLI is unavailable, blocked, or exhausted after at most three focused attempts, use the technology's official documentation or source repository. Use broader web sources only when primary documentation does not answer the question, and identify that limitation.
6. Reconcile the result with the user's installed version and surrounding code. Do not copy an example that relies on a different release or runtime without adapting it.

## Deliverable

Answer the user's question directly, include a minimal version-appropriate example when useful, and link or cite the exact documentation pages that support material API or configuration claims. State the assumed version and any unresolved documentation gap. Do not silently fall back to memory after a retrieval failure.
