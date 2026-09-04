# LIGHT

**Execution decision:** `Readiness: READY` for the requested one-line, reversible text change. If execution were in scope, change only the display literal in `ui/Button.tsx` line 8 from `Save` to `Save changes`. No separate approval, architecture work, or broader discovery is needed. This exercise explicitly excludes editing, so no change is performed.

**Compact readiness note**

- **Mode / rigor:** implementation / Light. The proposed change is local, reversible, and low risk.
- **Proof target:** the rendered button says **Save changes**, while its behavior remains the existing `save()` call.
- **Scope check:** verified evidence says the line contains only display text; the string is not an API key, selector, persisted field, or translation key. The handler already calls the unchanged `save()` function.
- **Authority:** the user requested this exact edit, and repository rules allow already-requested reversible changes without another approval.
- **Material unknowns or blockers:** none in the supplied scope. No independent review is required for this Light case, and none is available.
- **Acceptance:** inspect the exact diff and confirm it contains only the literal replacement; render the component and confirm the visible label is **Save changes** and clicking it still invokes the existing save behavior.

# DB

The proposal supports a **likely low-impact schema change**, but it does not support an unconditional zero-downtime promise. In PostgreSQL 16, adding a nullable `text` column with no default normally avoids a table rewrite. The `ALTER TABLE` still needs an `ACCESS EXCLUSIVE` lock. On a heavily written table, waiting for that lock—or blocking queued work after it is acquired—can cause an outage unless bounded and observed.

Before approval, verify the exact generated SQL and migration transaction behavior; inspect long-running transactions and lock contention during the intended window; test on a representative copy or staging workload; set a short `lock_timeout` so failure is safe; confirm old and new application versions tolerate the nullable column; and define monitoring, abort criteria, and retry procedure. Table size, write rate, transaction duration, and acceptable latency/interruption thresholds should be recorded. A successful staging run is evidence, not a guarantee, so production lock monitoring remains necessary.

A lossless down migration is **not unconditional**. `DROP COLUMN source_note` reverses the schema only while no meaningful values have been written. Once populated, it destroys data and is not lossless. Prefer a forward fix or stop application use first; if removal is required, preserve the values in an archival table/export and verify recovery. Backups/PITR are recovery controls, not proof that a down migration itself is lossless.

Do not index `archive_owner_id` automatically from the facts given. PostgreSQL does not automatically index the referencing FK column. Such an index can help joins, filters, and parent-key updates/deletes, but it also adds storage and write maintenance. Here, known queries neither join nor filter on it, writes are high, and parent mutations are rare. Measure child-table cardinality, actual parent update/delete behavior and latency, referential-action plans, and write overhead. Add the index only if those checks show a concrete query or FK-maintenance need; if needed in production, plan a nonblocking creation method such as `CREATE INDEX CONCURRENTLY`, with its transaction and failure-cleanup constraints reviewed.
