# Skills for GPT-5.6 Sol · medium

This profile adapts the repository's backed-up skills for a primary agent using
`gpt-5.6-sol` with reasoning effort `medium`. It is a prompt profile, not a model
configuration: select the model and effort in the runtime. A SKILL.md or an
`agents/openai.yaml` display prompt cannot change the running model.

## Use

Use the complete desired directories under `profiles/sol-medium/skills/` as the
skill source. Keep each skill's references, scripts, assets and metadata together.
Install **one version per skill name** in an agent's discovery path: choose either
the original backup or this profile, not both. Repository-wide recursive discovery
must exclude the unselected tree. No skills in your installed ChatGPT collection
are replaced by this repository update.

For OpenSpec execution, use `orchestrating-openspec-luna` after the plan is ready.
The primary agent is Sol medium; implementation/fixes remain explicitly assigned
to Luna Max. The profile does not switch all model roles to Sol.

## What was optimized

Keep operational constraints in the entrypoint; make inputs, routing, actions,
evidence, output and stopping conditions easy to locate. Load detailed examples
and domain reference material only when the task needs them. Preserve useful
short skills rather than adding a universal model preamble. Preserve permission
boundaries and required behavior; use existing context instead of ceremonial
questions. Prefer available tools and explicit capability gaps over assumed CLI
or connector availability.

These are task-specific instruction changes, not proven model-wide improvements.
See [ANALYSIS.md](ANALYSIS.md) for every skill's disposition and
[evals/RESULTS.md](evals/RESULTS.md) for the limited behavioral evidence.

## Source and refresh policy

The raw source is `skills/` at commit
`a1002b8de222ee8d34f8fbf56dccb017fc11f796` (which adds the OpenSpec orchestration
backup). `SOURCE_SNAPSHOT.tsv` records raw source paths and SHA-256 hashes;
`PROFILE_SNAPSHOT.tsv` records this profile's skill files. The original dated
`BACKUP_SNAPSHOT.tsv` remains historical and is not regenerated.

A future backup from another device may update `skills/`. Do not mirror it over
this profile automatically. Compare its changes with `SOURCE_SNAPSHOT.tsv`,
review the affected adaptations, rerun relevant checks, and refresh the profile
explicitly. Do not delete a raw backup merely because it is absent on a device.
Original resources are retained in the profile; large instructional examples may
be moved from SKILL.md into linked references.

## Evidence and provenance

The live official GPT-5.6 model-guidance page could not be retrieved in this run.
The target model and effort were available through the actual subagent interface.
Adaptation used the supplied local OpenAI skill-authoring/model-migration guidance,
inspection of the backup contents, and explicitly configured Sol medium cases.
No new API capability, price, context limit or benchmark claim is inferred.

All original source and licensing notices continue to apply. See the root
[THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md) and
[third_party_licenses](../../third_party_licenses/). The files here are adaptations,
not verbatim upstream backups; names containing “official” are preserved source
names and do not imply endorsement of these local modifications.
