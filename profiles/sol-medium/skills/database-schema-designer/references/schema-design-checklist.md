# Database Schema Design Checklist

Coverage checklist for designing and reviewing database schemas. The parent `SKILL.md` is authoritative. Mark an item applicable only after checking the target engine, version, workload, invariants, and deployment/recovery policy; this checklist does not make every foreign key, index, timestamp, rollback, or staging technique mandatory.

---

## Pre-Design

- [ ] **Requirements Gathered**: Understand data entities and relationships
- [ ] **Access Patterns Identified**: Know how data will be queried
- [ ] **SQL vs NoSQL Decision**: Chosen appropriate database type
- [ ] **Scale Estimate**: Expected data volume and growth rate
- [ ] **Read/Write Ratio**: Understand if read-heavy or write-heavy

---

## Normalization (SQL)

- [ ] **1NF**: Atomic values, no repeating groups
- [ ] **2NF**: No partial dependencies on composite keys
- [ ] **3NF**: No transitive dependencies
- [ ] **Denormalization Justified**: If denormalized, reason documented

---

## Table Design

### Primary Keys

- [ ] **Primary Key Defined**: Every table has primary key
- [ ] **Key Type Chosen**: Engine-supported key with suitable locality, distribution, exposure, and lifecycle properties
- [ ] **Meaningful Keys Avoided**: Not using email/username as PK

### Data Types

- [ ] **Appropriate Types**: Correct data types for each column
- [ ] **String Sizes**: VARCHAR sized appropriately
- [ ] **Numeric Semantics**: Exact engine-supported representation for money and other exact quantities; ranges fit expected values
- [ ] **Time Semantics**: Instants, local civil times, and time zones represented deliberately for the target engine

### Constraints

- [ ] **NOT NULL**: Required columns marked NOT NULL
- [ ] **Unique Constraints**: Unique columns (email, username)
- [ ] **Check Constraints**: Validation rules (price >= 0)
- [ ] **Default Values**: Sensible defaults where appropriate

---

## Relationships

### Foreign Keys

- [ ] **Relationship Integrity**: FK constraints used where supported and compatible with ownership/partitioning; alternatives document their enforcement
- [ ] **ON DELETE Strategy**: CASCADE, RESTRICT, SET NULL chosen
- [ ] **ON UPDATE Strategy**: Usually CASCADE
- [ ] **FK Indexes Evaluated**: Join and parent update/delete patterns justify each retained FK index

### Relationship Types

- [ ] **One-to-Many**: Modeled correctly
- [ ] **Many-to-Many**: Junction table created
- [ ] **Self-Referencing**: Parent-child relationships handled
- [ ] **Polymorphic**: Strategy chosen (separate FKs or type+id)

---

## Indexing

### Index Strategy

- [ ] **Primary Key Indexed**: Automatic, verify
- [ ] **Foreign Keys Evaluated**: Indexes retained for demonstrated join or constraint needs
- [ ] **Filter Indexes Evaluated**: Indexes match recurring predicates and selectivity
- [ ] **Ordering Indexes Evaluated**: Indexes match material ordering/query shapes
- [ ] **Composite Indexes**: Multi-column queries optimized
- [ ] **Column Order**: Leading columns match target-engine predicate and ordering behavior, verified with plans

### Index Limits

- [ ] **Not Over-Indexed**: Only necessary indexes
- [ ] **Index Maintenance**: Aware of write impact

---

## Performance

- [ ] **Joins Optimized**: N+1 queries avoided
- [ ] **SELECT * Avoided**: Only fetch needed columns
- [ ] **Pagination**: LIMIT/OFFSET or cursor-based
- [ ] **Aggregations**: Pre-calculated for expensive queries

---

## Migrations

- [ ] **Compatibility Sequence**: Expand/contract or another engine-appropriate sequence preserves required mixed-version behavior
- [ ] **Recovery Defined**: Tested rollback or forward-recovery path appropriate to data and deployment constraints
- [ ] **Data Migrations Separate**: Schema vs data separated
- [ ] **Representative Validation**: Migration tested on safe data/scale representative enough for its risk

---

## Security

- [ ] **Least Privilege**: Minimal database permissions
- [ ] **Separate Accounts**: Read-only vs read-write
- [ ] **Sensitive Data**: Passwords hashed, PII encrypted
- [ ] **Parameterized Queries**: SQL injection prevented

---

## Documentation

- [ ] **ERD Created**: Entity-relationship diagram
- [ ] **Schema Documented**: Column descriptions
- [ ] **Indexes Documented**: Why each index exists
- [ ] **Migration History**: Changelog of changes
