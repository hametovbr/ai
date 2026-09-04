---
name: code-review
description: Review a supplied diff, pull request, commit, or set of files for actionable correctness, security, performance, and maintainability defects. Use when the user asks for review before merge or requests analysis of risks such as injection, authorization gaps, races, N+1 queries, or missing edge cases. Do not use for implementing an unspecified feature or summarizing code without review findings.
metadata:
  argument-hint: "<PR URL, diff, or file path>"
---

# Code Review

Review the requested change and report only defects supported by the code or available execution evidence.

## Procedure

1. Identify the review target and intended behavior. If neither the request nor repository context identifies a target, ask for it.
2. Read repository instructions and the complete changed code with enough surrounding context to understand callers, data flow, and existing conventions. For a PR or commit, inspect the actual diff and relevant test or CI results when accessible.
3. Trace correctness first: boundary cases, state transitions, error paths, concurrency, resource cleanup, and compatibility with callers.
4. Check security where relevant: trust boundaries, authentication and authorization, injection, secret exposure, path traversal, SSRF, unsafe deserialization, and sensitive-data handling.
5. Check performance where relevant: query count, missing or ineffective indexes, unbounded work, algorithmic cost on realistic inputs, allocation, I/O, and leaks.
6. Check maintainability only when it creates a concrete future defect risk. Do not elevate personal style preferences to findings.
7. Verify suspected issues with focused tests, static analysis, or a minimal reproduction when practical. Do not modify the reviewed code unless the user also asked for fixes.
8. Re-read every finding. Remove speculative claims, duplicates, and issues outside the change unless the change newly exposes them.

## Findings

Order findings by severity. For each finding include:

- severity and concise title;
- exact file and line or smallest useful code location;
- the condition that triggers the problem and its concrete impact;
- the shortest viable remediation;
- verification evidence, or an explicit note that the finding is based on static reasoning.

Use **critical** only for likely compromise, data loss, or system-wide failure; **high** for release-blocking defects; **medium** for meaningful but bounded defects; and **low** for minor concrete risks. If there are no actionable findings, say so directly and mention any important validation gap. End with a brief assessment of whether the change is ready to merge, and summarize tests or checks actually observed or run. Do not claim CI, runtime behavior, or requirements compliance without evidence.
