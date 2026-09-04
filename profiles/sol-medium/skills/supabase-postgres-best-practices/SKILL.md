---
name: supabase-postgres-best-practices
description: "Postgres best practices maintained by Supabase, for Postgres running anywhere. Load this skill BEFORE writing or changing anything that lives in a Postgres database: creating or altering tables and columns (including choosing column types), schema design, migrations and declarative schema files, RLS policies and the tests that verify them, indexes, triggers, database functions, queues and scheduled jobs (pg_cron, pgmq), vector/semantic search (pgvector), and restoring dumps (pg_restore) or importing data. Also load it when diagnosing slow queries, high CPU, timeouts, EXPLAIN plans, connection exhaustion, locking, bloat, or rows visible to the wrong user or tenant. This is not just a performance guide — schema, migration, security, and SQL authoring tasks need these rules too, even for a one-column change or a single query."
license: MIT
metadata:
  author: supabase
  version: "1.1.1"
  organization: Supabase
  date: January 2026
  abstract: Comprehensive Postgres performance optimization guide for developers using Supabase and Postgres. Contains performance rules across 8 categories, prioritized by impact from critical (query performance, connection management) to incremental (advanced features). Each rule includes detailed explanations, incorrect vs. correct SQL examples, query plan analysis, and specific performance metrics to guide automated optimization and code generation.
---

# Supabase Postgres Best Practices

Comprehensive performance optimization guide for Postgres, maintained by Supabase. Contains rules across 8 categories, prioritized by impact to guide automated query optimization and schema design.

## When to Apply

Reference these guidelines when:
- Writing SQL queries or designing schemas
- Implementing indexes or query optimization
- Reviewing database performance issues
- Configuring connection pooling or scaling
- Optimizing for Postgres-specific features
- Working with Row-Level Security (RLS)

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Query Performance | CRITICAL | `query-` |
| 2 | Connection Management | CRITICAL | `conn-` |
| 3 | Security & RLS | CRITICAL | `security-` |
| 4 | Schema Design | HIGH | `schema-` |
| 5 | Concurrency & Locking | MEDIUM-HIGH | `lock-` |
| 6 | Data Access Patterns | MEDIUM | `data-` |
| 7 | Monitoring & Diagnostics | LOW-MEDIUM | `monitor-` |
| 8 | Advanced Features | LOW | `advanced-` |

## How to Use

1. Identify the database version, deployment context, affected objects, workload, and whether the task is drafting SQL, reviewing it, or executing a change. Do not assume Supabase-specific functions or roles exist in Postgres running elsewhere.
2. Read [`references/_sections.md`](references/_sections.md) and load only the rule files relevant to the task. For example, use `query-*` for query plans and indexes, `schema-*` for DDL and migrations, `security-*` for privileges or RLS, and `conn-*` for pool or connection exhaustion.
3. Inspect the existing schema, constraints, indexes, policies, extensions, and migration conventions before proposing changes. For performance work, use representative `EXPLAIN (ANALYZE, BUFFERS)` evidence when safe and available; do not infer production gains from generic examples.
4. Apply the relevant rules together. Check interactions such as write cost from added indexes, locks caused by DDL, RLS semantics, transaction length, rollback behavior, and extension or version availability.
5. Produce the smallest safe SQL or configuration change. Separate Supabase-only advice from portable PostgreSQL advice and preserve project conventions unless they create a concrete defect.
6. Validate syntax and migration behavior in an appropriate non-production environment when available. Report checks performed, assumptions, rollout or rollback needs, and any claim that still requires production measurement.

Each rule file includes rationale, incorrect and corrected SQL, and primary references. Treat its metrics as examples rather than guaranteed results for a different workload.

## References

- https://www.postgresql.org/docs/current/
- https://supabase.com/docs
- https://wiki.postgresql.org/wiki/Performance_Optimization
- https://supabase.com/docs/guides/database/overview
- https://supabase.com/docs/guides/auth/row-level-security
