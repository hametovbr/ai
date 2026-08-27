# Portable skills backup manifest

Snapshot date: 2026-08-27  
Destination: `https://github.com/hametovbr/ai` (`main`)  
Base commit: `205ff8afd4c37b86bd3931966434c5658d482056`

This additive backup preserves 84 regular files (603,125 bytes) byte-for-byte
and mode-for-mode. `BACKUP_SNAPSHOT.tsv` is the source path/mode/SHA-256
baseline. Only `.DS_Store` is excluded.

## Included skills

`architecture-decision-records`, `code-review`, `create-rfc`,
`database-schema-designer`, `evaluating-agent-skills`, `find-docs`,
`find-skills`, `grill-me`, `grilling`, `making-architecture-decisions`,
`n8n-workflow-patterns`, `resolve-ambiguous-tasks`, `ru-text`,
`supabase-postgres-best-practices`, `synthesis-voice-profiler`.

## Portability exclusions

`camunda-read-only-api`, `dp-support-code-search`, `dp-support-gitlab`,
`dp-support-investigation`, `dp-support-jira`, `dp-support-logs`,
`dp-support-time`, `dp-support-tracker`, `dp-support-wixie`,
`factoring-development-review`, `factoring-read-only-api`,
`factoring-support-triage`, `using-dp-time`, `configuring-nessy-cli`,
`configuring-nessy-desktop`, `nessy-direct-llm`, `using-nessy-bridge`,
`nestor-search-api`, `using-codegraph-mcp`, `orchestration`, `context7-mcp`,
`using-spark-subagents`.

Separate explicit user exclusion: `write-b-khametov-work-chat`.

## External boundaries

- `find-docs` requires the public Context7 CLI; `find-skills` requires the
  public Skills CLI. Neither is vendored.
- `code-review` supports standalone use; its optional `../../CONNECTORS.md`
  is absent.
- `n8n-workflow-patterns` retains one unresolved
  `../../n8n-expression-syntax/SKILL.md` link. Full use expects the n8n MCP
  plus expression, node-configuration, validation, code, and error-handling
  companions; agent-specific material is delegated to `n8n-agents`.
- `resolve-ambiguous-tasks` names managed Superpowers prerequisites, which are
  provider-managed rather than vendored.

## Provenance and licenses

Skill trees are copied unchanged from the installed source. Their installed
content evidence and separately pinned public license/NOTICE evidence are
distinguished in `THIRD_PARTY_NOTICES.md`; a license-evidence revision is not
claimed to be an installed-content revision. Third-party attribution and
license artifacts are outside the preserved skill trees.

| Skill(s) | Public source and effective license |
|---|---|
| architecture-decision-records | wshobson/agents, MIT |
| code-review | anthropics/knowledge-work-plugins, Apache-2.0 |
| create-rfc | tech-leads-club/agent-skills, CC-BY-4.0 |
| database-schema-designer | softaworks/agent-toolkit, MIT |
| find-docs | upstash/context7, MIT |
| find-skills | vercel-labs/skills, MIT |
| grill-me; grilling | mattpocock/skills, MIT |
| n8n-workflow-patterns | czlonkowski/n8n-skills, MIT plus NOTICE |
| ru-text | talkstream/ru-text, MIT |
| supabase-postgres-best-practices | supabase/agent-skills, MIT |
| synthesis-voice-profiler | synthesisengineering/synthesis-skills, CC0-1.0 |
| evaluating-agent-skills; making-architecture-decisions; resolve-ambiguous-tasks | user-managed local material; direct user publication request; no implied public reuse license |
