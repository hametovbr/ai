---
name: fileflows-flow-authoring
description: Use when creating, reviewing, modifying, or validating importable FileFlows flow JSON, selecting documented FileFlows nodes, authoring inline JavaScript or C# nodes, integrating FFmpeg, mapping Docker paths, or handing files to Sonarr/Radarr.
---

# FileFlows Flow Authoring

Create the smallest importable flow that satisfies the current requirement. Prefer an existing FileFlows node over code. Prefer one inline `Function` when native nodes cannot express a bounded operation. Add reusable FileFlows Scripts only when more than one flow consumes the same behavior.

## Workflow

1. Read `references/fileflows-reference.md` before creating or changing a flow.
2. Read `references/nodes-index.md`, then load only the node catalog relevant to the task: Basic, Video, media/metadata, or integrations. The catalog covers every flow node detected in the current official plugin documentation and links each entry to its source.
3. Inspect a current export from the target FileFlows installation when available. Treat it as authoritative for envelope fields, node UIDs, model properties, defaults, and serialization shape. The node catalog is not a substitute for an export.
4. State input type, output effect, required invariants, mounted paths, variables, and failure behavior.
5. Use the first sufficient mechanism: native nodes, inline JavaScript `Function`, inline `C# Function`, then a plugin or external executable.
6. Keep secrets out of exported JSON. Read API keys and credentials from environment or node variables intended for secrets.
7. Use `Flow.GetToolPath('ffmpeg')` and `Flow.GetToolPath('ffprobe')` for FileFlows-managed tools. Execute with `Flow.Execute({ command, argumentList })`; never construct a shell command from filenames.
8. Use `Flow.Fail(reason)` or `-1` for unsafe or ambiguous input. Log decisions and external-process errors.
9. Build the complete operation plan before destructive writes. Use a temporary path and atomic rename when partial publication would violate correctness.
10. Generate stable UUIDs for the flow and every part. Ensure every connection references an existing node and valid output/input indexes.
11. Validate JSON parsing, graph integrity, forbidden embedded secrets, and inline-code syntax where a suitable compiler or parser is available.

## Authoring rules

- Start folder workflows with `FileFlows.BasicNodes.File.InputFolder`.
- Use `FileFlows.BasicNodes.Functions.Function` for documented JavaScript scripting. Do not guess a C# node UID; obtain it from a target-version export before generating a C# node.
- Set script-node `Type` to `3`, `Inputs` to `1`, and `Model.Outputs` equal to the node's declared outputs.
- Return `0` only to complete the entire flow. Return `1+` to follow the corresponding output. Return failure for out-of-range or unsafe states.
- Use `Variables.file.FullName` for the current input path and verify `Flow.IsDirectory` for folder workflows.
- Keep container paths identical across FileFlows, download client, and Arr services when a path is passed through an API.
- Never embed host-only paths in flow code when the processing node sees a mapped container path.
- Preserve the source on failure. Delete it only after downstream success is proven.
- Do not add retries, manifests, staging, or cleanup unless a named repeat/partial-failure mode requires them.
- Do not infer undocumented node UIDs, JSON model keys, defaults, or version availability from a documentation page title. Confirm them in a target-version export.

## Node reference maintenance

The generated catalog lives beside this skill in `references/nodes-*.md`. It excludes plugin Settings pages and category indexes. To detect documentation drift, run `python3 scripts/update_node_reference.py --check`. To refresh it from the official sitemap, run the same script with `--write`. This maintenance dependency is not needed to author or use flows.

## Deliverable

Produce one importable `.json` flow artifact plus only the deployment changes required for variables or mounts. Report target FileFlows version assumptions and validations performed. Do not claim UI import or runtime success without testing on the target installation.
