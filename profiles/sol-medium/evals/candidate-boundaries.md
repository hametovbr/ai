# LIGHT

**Execution decision:** Proceed with the requested one-line label change when execution is in scope. Replace the visible text `Save` with `Save changes`; keep the existing `onClick` behavior and `save()` call unchanged. No additional approval, architecture work, specification, or independent review is required.

**Mode:** implementation  
**Rigor:** Light  
**Readiness:** READY

The supplied evidence covers the full acceptance boundary: `ui/Button.tsx` line 8 contains only display text, and the string has no role as an API key, selector, persisted field, or translation key. The change is reversible, repository rules already authorize it, and there is no material unknown or contradiction. A direct claim-to-source and scope check is sufficient at Light rigor.

Acceptance is limited to an exact diff showing only the label replacement and a rendered button displaying **Save changes** while invoking the unchanged save behavior. Per the request, no file edit or execution is performed here.

# DB

**Correctness and recovery findings**

The proposed `source_note text NULL` addition is structurally compatible with existing rows and needs no backfill. That supports a low-work expansion, but it does **not** prove zero downtime on PostgreSQL 16. `ALTER TABLE` still needs a strong table lock. On a highly concurrent table, lock acquisition can wait behind existing transactions; once queued, it can also delay later traffic. The promise is therefore unsupported until lock behavior and transaction duration are measured on the actual deployment path.

Required checks before approval:

- Confirm old and new application versions tolerate the column's absence/presence during the deployment window.
- Inspect peak write rate, transaction duration, long-running transactions, and current lock contention on `orders`.
- Rehearse against production-representative schema, table size, concurrency, and migration tooling; record lock wait, lock hold time, blocked sessions, and application latency.
- Define bounded lock/statement timeouts, an abort condition, monitoring, and a retry window. Verify the migration remains transactional under the tool in use.
- Verify reads and writes after deployment, including `NULL` handling and any retention or sensitivity requirements for free-form notes.

A universal lossless down migration is not a valid requirement. Dropping `source_note` is lossless only while it contains no data. After writes begin, a down migration destroys those values. Choose recovery by phase: abort/rollback before use; afterward prefer a tested forward fix or first export/preserve the data under an explicit recovery procedure.

**Index finding**

Do not automatically index `archive_owner_id`. PostgreSQL does not require an index on the referencing column to enforce ordinary child inserts, and the known workload has no joins or filters on it. An index adds write and storage cost to an already write-heavy table. Parent update/delete checks may benefit, but their workload is unmeasured, so the decision is conditional. Measure table size, non-null row count, parent-operation frequency and latency, lock impact, and representative plans. If that path proves material, evaluate a targeted index, potentially partial on non-null values, and confirm the benefit with plans and concurrency tests.
