---
name: n8n-data-tables-official
description: Use for n8n Data Table schema design, queries, inserts, updates, upserts, deduplication, lookup data, audit state, or persistence across executions.
---

# n8n Data Tables

## Invariants

- Treat `id`, `createdAt`, and `updatedAt` as managed default columns.
- Data Table cells support primitive values. Store objects/arrays as JSON strings in `string` columns with an `_object` suffix, then parse them at the ownership boundary.
- Data Tables do not enforce foreign keys. Store stable IDs and implement referential behavior explicitly.
- Choose a uniqueness key before using a table for deduplication or idempotency.
- Preserve natural shapes at sub-workflow outputs even when storage uses serialized text.

## Workflow

1. Search existing tables before creating one.
2. Define the row identity, column types, required fields, uniqueness/idempotency keys, retention, and expected query paths.
3. Choose the operation: insert for append-only facts, update for known rows, upsert for stable external identities, query/get for lookups, and delete only with explicit scope.
4. Fetch the live node/tool shape and map fields explicitly.
5. Test empty-table, duplicate, update, missing-row, and serialization paths that apply.
6. Verify saved rows and downstream natural-shape output before publishing.

## Stop rules

- Do not create a duplicate table or schema without searching.
- Do not rely on an unenforced foreign key or accidental UI mapping.
- Do not perform destructive or bulk row changes outside the user's authorization.

## Selective references

- [references/SCHEMA_DESIGN.md](references/SCHEMA_DESIGN.md): columns, relationships, and storage shapes.
- [references/OPERATIONS.md](references/OPERATIONS.md): node/tool operation details and UI quirks.
- [references/DEDUP_PATTERNS.md](references/DEDUP_PATTERNS.md): external IDs and idempotency.
- [references/DETAILED_GUIDE.md](references/DETAILED_GUIDE.md): lookup, audit, and verification examples.
