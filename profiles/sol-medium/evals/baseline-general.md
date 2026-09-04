## RFC

# RFC: Idempotent Payment Webhooks

| Field | Value |
|---|---|
| RFC ID | Unassigned |
| Status | Draft |
| Author / Driver | Nina |
| Audience / Informed | Backend team |
| Approver / Contributors | TBD |
| Impact | HIGH — duplicate postings compromise financial correctness |
| Decision deadline | TBD |

### Background

Duplicate webhook deliveries can create duplicate ledger postings. The goal is one posting per event ID with retry-safe responses. Deployment is out of scope. No change preserves a financial-integrity risk.

### Assumptions

| Assumption | Confidence | Invalidation trigger |
|---|---|---|
| Every payment event has a stable event ID reused on redelivery. | Medium | A provider can reuse an ID for different logical events or change it on retry. |
| The ledger posting and idempotency record can share a PostgreSQL transaction. | Medium | They cannot be committed atomically. |
| PostgreSQL remains available; Redis is not deployed. | High | Platform dependencies change. |

### Decision criteria

| Criterion | Weight |
|---|---|
| Exactly one durable posting per event ID, including concurrent deliveries | Must-have |
| Retry-safe, deterministic response behavior | Must-have |
| Operational complexity | High |
| Failure recovery and auditability | High |

### Options

**1. PostgreSQL unique constraint — recommended.** Add a unique event ID key and deduplicate with the ledger write in one transaction. On conflict, return the defined retry response without another posting. This gives durable concurrency enforcement in the existing system and supports audit/recovery. Cost is small-to-medium; risk is medium until transaction and collision semantics are verified.

**2. Redis deduplication.** Claim the ID in Redis before posting. Redis adds deployment, persistence, expiry, and recovery concerns. Its claim and the PostgreSQL posting are not atomic, so crashes can cause skipped or duplicate work without further coordination. Cost and operational risk are higher.

**3. Do nothing.** No immediate effort, but duplicate ledger postings remain possible; this fails the must-have criterion.

### Recommendation and actions

Choose PostgreSQL for durable correctness at the authoritative write boundary with lower operational complexity. Before approval, Nina should define response/collision behavior, confirm transaction feasibility, and name the approver. After approval, design and test sequential retries, concurrent duplicates, rollback, and reused-ID mismatch.

### Unresolved questions

- What exact response should a repeated event receive?
- How long must idempotency history be retained?
- Can event IDs collide across providers or accounts, requiring a composite key?

### Outcome

Pending review; no decision date or approver assigned.

## ARCH

**Verdict: reject the proposal and revise to the existing scheduled import.**

The minimum adequate design is one nightly scheduled process that fetches at most 500 records, validates/transforms them locally, and UPSERTs them into the existing PostgreSQL database before exiting. Keep any provider-specific mapping as concrete code inside the job. Preserve a small function or module boundary around fetch/transform logic so another real provider can be added later without creating a plugin framework now.

**Decisive reason:** the workload is bounded, single-process, easy to rerun, and only needs completion by morning. PostgreSQL already owns durable state and the scheduler already owns execution. No supplied requirement calls for streaming, independent scaling, a separate lifecycle, or a new state authority.

**Subtractions:**

- Remove Kafka: there is no throughput, fan-out, latency, or isolation requirement that needs a broker.
- Remove the generic plugin framework: future providers are hypothetical and no stable variation axis has been demonstrated.
- Remove the checkpoint database: PostgreSQL UPSERTs plus rerunning the bounded import provide recovery without another durable state store.
- Remove the controller service: the existing scheduler can start and observe the job; a persistent deployment adds recovery, monitoring, and ownership work without changing the outcome.

**Required acceptance evidence:** run the job twice against the same fixture and verify the second run creates no duplicate rows and converges to the same PostgreSQL state. A failed run must surface as failed and be safe to rerun.

**Material assumption:** each fetched record has a stable key and UPSERT semantics are acceptable for updates. If this is false, define identity/conflict policy in PostgreSQL before importing.

**Specific fact that would change the design:** a demonstrated requirement to ingest continuously or at a volume/concurrency level that the nightly single process cannot finish by morning. That measured failure could justify partitioning or a queue. Adding another provider alone would justify a second concrete adapter first, not Kafka or a generic framework.

## DOCS

The pinned target is **`example-lib` 2.4.1**. No documentation result has been verified in this exercise because Context7 is unavailable, browser retrieval has not occurred, and installation is prohibited.

My next actions would be:

1. Use the browser to open the official package-registry entry for the exact package name and version (`example-lib@2.4.1`). Confirm that the page identifies version 2.4.1, then follow only its repository, homepage, or documentation links. This avoids guessing which similarly named project owns the package.
2. Look for a version selector or an official documentation URL explicitly labeled 2.4.1. I would reject an unversioned “latest” page unless it states that its content applies to 2.4.1.
3. If no versioned documentation site exists, open the official source repository at the release/tag corresponding to 2.4.1 and use that tag’s README, API reference, examples, and changelog. The version tag is the fallback documentation path because it preserves the pinned package state.
4. Verify any needed API detail against at least one artifact tied to 2.4.1, such as the tagged source declarations or published package contents exposed by the registry. Record the final canonical URL and note any gaps between the release tag and hosted docs.

Until those browser checks are complete, I would report the documentation path as **unresolved**, not infer APIs from current docs or memory.
