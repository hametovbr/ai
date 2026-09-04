# RFC

# RFC: Idempotent Payment Webhooks

| Field | Value |
|---|---|
| RFC ID | Unassigned |
| Status | Draft |
| Impact | High |
| Driver | Nina |
| Audience | Backend team |
| Approver | TBD |
| Decision deadline | TBD |

## Background

Duplicate webhook deliveries can create duplicate ledger postings. This RFC decides how to guarantee exactly one posting per payment event ID and retry-safe responses. Without a decision, duplicate financial records remain possible. Deployment is out of scope.

## Assumptions

| Assumption | Confidence | Invalidation trigger |
|---|---|---|
| Each logical payment event has a stable event ID across retries. | Medium | A provider can resend one event under different IDs. |
| Posting and recording the processed event can occur in one PostgreSQL transaction. | Medium | The ledger write is outside that transaction boundary. |
| PostgreSQL is available on the webhook write path. | High | Current architecture shows otherwise. |

## Decision criteria

1. **Must-have:** exactly one committed posting per event ID under concurrency and process failure.
2. **Must-have:** repeat delivery receives a retry-safe response without another posting.
3. **High:** durable correctness across restarts and recovery.
4. **High:** low operational complexity with current infrastructure.

## Options

### 1. PostgreSQL unique constraint — recommended

Store the event ID under a PostgreSQL unique constraint and create the posting in the same transaction. A uniqueness conflict identifies an accepted event and returns the defined success response.

**Advantages:** database-enforced concurrency safety; durable with the ledger; no new service.  
**Costs/risks:** requires a correct transaction boundary and a defined response when a duplicate arrives while the first attempt is incomplete.

### 2. Redis deduplication

Claim each event ID in Redis before posting.

**Advantages:** fast deduplication and possible expiry controls.  
**Costs/risks:** introduces a datastore and recovery work; expiry or eviction can admit old duplicates; Redis and PostgreSQL can diverge without coordination. Durable correctness is harder to establish.

### 3. Status quo

No implementation cost, but it fails both must-haves and preserves duplicate-ledger risk.

## Recommendation

Choose the PostgreSQL constraint for durable concurrency control with existing infrastructure. The trade-off is coupling idempotency to the database transaction. Confidence is medium until the transaction boundary is confirmed.

## Action items

- Nina: confirm event-ID semantics and transaction boundary; due TBD.
- Approver TBD: review and decide by the deadline TBD.
- Backend team: define the response contract for completed and in-progress duplicate deliveries.

## Outcome

**Decision:** Pending.  
**Decision date / approver:** TBD.

## Unresolved questions

- Can all providers guarantee stable, globally scoped event IDs?
- What response should an overlapping retry receive before the first transaction completes?

# ARCH

**Verdict: reject the proposal and revise to a scheduled single-process job using PostgreSQL.**

**Decisive reason:** The stated workload is at most 500 records nightly, has no deadline tighter than the next morning, exits after completion, and is easy to rerun. The existing scheduler, process, and PostgreSQL already satisfy those requirements. Possible future providers do not establish a current need for new distributed infrastructure.

**Minimum adequate design:** Keep one scheduled import job. Fetch the provider’s records, validate them, and UPSERT them into the existing PostgreSQL database using a stable record key. Treat a failed run as failed, retain enough run/error information in the existing job or database facilities to diagnose it, and rerun the whole bounded import. Keep provider-specific mapping inside the job; introduce a small local interface only when a second provider actually requires differing behavior.

**Subtractions:**

- Remove Kafka: no stated throughput, decoupling, buffering, or independent-consumer requirement needs a broker.
- Remove the plugin framework: one provider does not justify a generic extension boundary.
- Remove the checkpoint database: a bounded, rerunnable import can restart from the beginning, while PostgreSQL already holds durable state.
- Remove the controller service: the existing scheduler already starts the job, and there is no continuous coordination requirement.

Each proposed component adds deployment, monitoring, credentials, recovery, and ownership work without protecting a named current invariant.

**Specific missing fact that would change the decision:** whether rerunning the full import can cause an irreversible external side effect that the PostgreSQL UPSERT cannot make idempotent. If yes, durable per-record checkpointing may be required; it should live in existing PostgreSQL unless a demonstrated constraint rules that out. More providers alone would justify a local adapter first, not Kafka or a controller service.

**Verification:** Confirm one complete failed-then-rerun execution produces the same PostgreSQL state as one successful run and causes no duplicate external effects. On the supplied facts, context is sufficient and the decision is ready.

# DOCS

The target is **example-lib 2.4.1**, exactly as pinned in `package.json`. No API or documentation result is verified yet.

My next actions would be:

1. Use the available browser to find the package’s official documentation or official source repository. I would identify the canonical project from its package-registry metadata if the name is ambiguous, while avoiding third-party tutorials.
2. Look for documentation explicitly versioned **2.4.1**: a version selector, `/2.4.1/` documentation path, release tag, or tagged source tree. I would navigate from the official project rather than guessing a URL.
3. If no 2.4.1 documentation site exists, inspect the official repository at tag `v2.4.1` or `2.4.1`, then use that tag’s README, API reference, examples, and release notes as the version-matched documentation path.
4. Query one focused topic at a time based on the user’s actual task or error. Before sending a query, I would remove secrets, private code, personal data, and internal identifiers.
5. Cross-check every proposed API or configuration example against the 2.4.1 material and the surrounding project runtime. I would cite the exact official pages or tagged files supporting each material claim.
6. If only nearby-version documentation is available, I would state the closest version found, disclose the mismatch, and avoid presenting syntax as valid for 2.4.1 until the tagged source or release notes confirm it.

Context7 is unavailable, and shell installation is prohibited, so I would not run or install `ctx7`, the package, or another CLI. Because browsing is also prohibited in this exercise, I cannot provide a verified URL or invent API details. The correct current deliverable is therefore this lookup procedure plus the unresolved gap: the official 2.4.1 documentation location has not yet been fetched.
