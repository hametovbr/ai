---
name: n8n-expressions-official
description: Use when writing or reviewing n8n `{{...}}` expressions, field mappings, cross-node references, Luxon date logic, or expression errors.
---

# n8n Expressions

## Invariants

- Prefer a stable named-node reference such as `$('Lookup').item.json.id` when a value originates upstream; `$json.id` is safe only when the immediate input contract owns that field.
- Preserve item pairing. After Aggregate, Execute Once, Split Out, or ambiguous merges, `.item` may not resolve; use an explicit lookup or restore context with Merge.
- Use Luxon for date/time math and make the timezone explicit when it changes meaning.
- Return the type required by the target parameter. Distinguish UI `object` and `array` slots.
- Use valid n8n expression wrappers. Multi-step logic belongs in a readable IIFE; substantial or stateful logic may require Code.

## Workflow

1. Identify the target parameter's expected type and the source node/field.
2. Choose a direct reference, method chain, conditional, Luxon expression, or IIFE.
3. Make missing-value behavior explicit with nullish/default handling appropriate to the domain.
4. For arrays or objects, serialize only at a storage/text boundary; keep natural shapes elsewhere.
5. Validate with representative missing, empty, single, and multiple-item inputs. Inspect the actual downstream value.

## Scope boundary

Avoid a separate Edit Fields node when an expression can map the value directly for one consumer. Use Edit Fields when several consumers need a named normalized field, the mapping is a meaningful contract, or it shapes a sub-workflow return. Use Code only when expressions cannot express the required behavior clearly and safely.

## Stop rules

- Stop if the target type or item-pairing semantics are unknown; inspect the node and execution first.
- Do not use a DateTime node solely for date math an expression can perform.
- Do not hide side effects in expressions.

## Selective reference

Read [references/DETAILED_GUIDE.md](references/DETAILED_GUIDE.md) for full syntax, mapping decisions, method-chain formatting, IIFE patterns, JSON serialization rules, examples, and anti-patterns.
