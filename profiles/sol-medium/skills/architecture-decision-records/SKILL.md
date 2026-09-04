---
name: architecture-decision-records
description: Use when writing, updating, superseding, or indexing an Architecture Decision Record (ADR) for a durable technical decision. Do not use an ADR as a substitute for making or reviewing the decision itself.
---

# Architecture Decision Records

Capture a durable decision so a future reader can understand the forces, choice, and consequences without reconstructing the discussion.

## Route first

- Use `making-architecture-decisions` when the choice is still being made.
- Use `challenging-architecture-decisions` when an existing proposal needs stress-testing.
- Use this skill when the decision is ready to record, or an ADR's status/index must be maintained.

Write an ADR for a choice that is costly to reverse, changes ownership or a durable contract, introduces a lasting dependency, or needs later revalidation. Skip routine maintenance and local implementation details unless they encode a durable boundary.

## Workflow

1. Inspect the repository's ADR location, numbering, template, status vocabulary, and index. Follow local convention when it exists.
2. Establish the evidence basis: current context, decision drivers, constraints, considered credible options, and who owns the decision. Do not invent missing facts. If the choice is unresolved, route back to decision-making instead of writing a conclusion-shaped ADR.
3. Draft the smallest format that preserves the decision. A useful ADR contains:
   - title, date, status, and deciders when known;
   - context and decision drivers;
   - credible options, including the status quo when material;
   - decision and rationale tied to the drivers;
   - positive and negative consequences, risks, and mitigations;
   - implementation or revalidation triggers only when they affect the decision;
   - related decisions and evidence references.
4. For a changed decision, create a new ADR that supersedes the old one. Preserve the accepted historical record; update status and cross-links rather than rewriting its rationale.
5. Update the index or related ADR links if the repository maintains them. Do not install ADR tooling unless the user requests it.
6. Check that claims are traceable, alternatives are honest, consequences include costs, and status matches reality. Then stop.

## Output

Return the ADR in the repository's format, plus only the status/index changes needed to keep the decision history coherent. When no repository format exists, use a lightweight Context / Decision / Consequences ADR unless the decision needs the fuller MADR fields.

Read [templates and management examples](references/templates-and-management.md) only when a concrete template, index pattern, supersession example, or `adr-tools` command is useful. Treat product versions and example estimates there as illustrative, not current evidence.
