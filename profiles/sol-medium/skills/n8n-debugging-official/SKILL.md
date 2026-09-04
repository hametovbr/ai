---
name: n8n-debugging-official
description: Use when an n8n workflow errors, stops, produces unexpected output, or behaves differently from the user's expectation.
---

# n8n Debugging

Treat the user's expected behavior as the requirement and execution data as evidence of actual behavior. Do not dismiss a report because the workflow appears correct.

## Diagnostic order

1. Pin down expected versus actual behavior, the exact error, the failing execution, and what changed.
2. Fetch the execution with data and identify the first node whose output or status diverges.
3. Fetch the current workflow and inspect actual node parameters and the `connections` object.
4. Re-fetch live node types and run `validate_node_config` for the suspect node. Check discriminators, conditional fields, and value types.
5. Trace data shape and item pairing across Aggregate, Execute Once, Split Out, Merge, Code-all-items, binary extraction, and other shape-changing nodes. Prefer stable named-node references when intermediate `$json` no longer carries the field.
6. Reproduce with controlled pin data when safe. Compare each node's emitted data with the intended contract.
7. If configuration and data flow are correct, check upstream API documentation, n8n source, instance version, and skill/plugin drift.
8. State the confirmed cause and evidence. If only a workaround is available, label it as such and record the unresolved cause.

## Stop rules

- Do not randomly delete or rewrite nodes before locating the first divergence.
- Do not declare an n8n bug until configuration, current source/version, and drift have been checked.
- Do not call a workaround a fix.
- Do not rerun a side-effecting workflow merely to gather evidence unless that execution is authorized.

## Selective references

- Read [references/PARAMETER_VERIFICATION.md](references/PARAMETER_VERIFICATION.md) for deep conditional configurations.
- Read [references/FETCHING_N8N_SOURCE.md](references/FETCHING_N8N_SOURCE.md) when runtime behavior contradicts the live schema or documentation.
- Read [references/DETAILED_GUIDE.md](references/DETAILED_GUIDE.md) for detailed symptom classes, commands, drift checks, and reporting examples.
