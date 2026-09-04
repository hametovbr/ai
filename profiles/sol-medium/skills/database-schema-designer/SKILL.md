---
name: database-schema-designer
description: Use when designing, reviewing, or evolving SQL or NoSQL schemas, relationships, constraints, indexes, access patterns, and database migrations.
license: MIT
---

# Database Schema Designer

Design the smallest schema that preserves domain invariants and supports verified read/write patterns. Generate executable DDL only for a named database and version; otherwise state the assumed dialect.

## Workflow

1. Inspect existing schema, migrations, ORM models, queries, and database conventions when available. Extract entities, ownership, cardinality, lifecycle, access patterns, retention, consistency, scale, and compatibility constraints from the request.
2. Ask only when a missing domain invariant or destructive-lifecycle choice cannot be inferred safely. For reversible details, state a bounded assumption and continue.
3. Choose SQL or NoSQL from transaction, relationship, query, consistency, and scaling requirements. Do not default to a new database category when an existing platform can satisfy them.
4. Model authoritative facts and relationships. For SQL, normalize to remove update anomalies, then denormalize only for a measured or clearly dominant access pattern with a synchronization rule. For document stores, choose embedding or references from cardinality, update independence, document growth, and atomicity boundaries.
5. Specify keys, nullability, uniqueness, checks, foreign-key behavior, tenant boundaries, and ownership. Select data types from the target engine rather than generic examples.
6. Add indexes from concrete query shapes, ordering, selectivity, and write cost. An index on a foreign key is common but not automatic; justify it from joins, deletes/updates, or engine behavior.
7. For an existing system, produce an expand/migrate/contract path with backfill, compatibility window, verification, rollback or forward-recovery strategy, and lock/load considerations. Do not promise zero downtime without evidence from the engine and deployment path.
8. Verify the design against representative queries, integrity failures, concurrent writes, deletion/retention behavior, and the target engine's actual DDL semantics. Stop when the requested artifact and material risks are covered.

## Output contract

Return only the artifacts the user needs, selected from:

- assumptions and unresolved domain decisions;
- concise entity/relationship model;
- schema or migration in the correct dialect;
- constraint and index rationale tied to invariants and queries;
- migration sequence and recovery boundary;
- representative verification queries or checks;
- material trade-offs and limits.

If the request is a review, lead with correctness and data-loss findings, then performance and maintainability. If context is insufficient for safe DDL, return the model, the blocking decision, and one next action instead of inventing columns or destructive behavior.

## References

- Read [design patterns and examples](references/design-patterns.md) only for detailed normalization, type, index, relationship, NoSQL, migration, and query examples.
- Use [the schema design checklist](references/schema-design-checklist.md) as a coverage aid, not as a universal rule set. Database-specific behavior and measured access patterns take precedence.

## Non-negotiable checks

- Every authoritative fact has one clear owner and valid lifecycle.
- Monetary and exact quantities use exact numeric semantics.
- Constraints enforce material invariants where the database can do so safely.
- Deletes, updates, tenant isolation, sensitive data, and retention have explicit behavior.
- Indexes correspond to actual query or constraint needs and account for write cost.
- Migration steps preserve compatibility and provide observable validation and recovery.
- Examples never substitute for current engine documentation or production evidence.
