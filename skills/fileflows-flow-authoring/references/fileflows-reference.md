# FileFlows authoring reference

## Official sources

- Flow editor: https://fileflows.com/docs/webconsole/flows/editor
- Flow properties and template fields: https://fileflows.com/docs/webconsole/flows/properties
- Basic nodes: https://fileflows.com/docs/plugins/basic-nodes/
- All documented plugins and nodes: https://fileflows.com/docs/plugins/
- Input Folder: https://fileflows.com/docs/plugins/basic-nodes/input-folder
- JavaScript Function: https://fileflows.com/docs/plugins/basic-nodes/scripting/function
- C# Function: https://fileflows.com/docs/plugins/basic-nodes/scripting/csharp
- C# globals: https://fileflows.com/docs/scripting/csharp/globals
- Flow scripting object: https://fileflows.com/docs/scripting/javascript/flow/
- External process execution: https://fileflows.com/docs/scripting/javascript/flow/execute
- Variables: https://fileflows.com/docs/variables
- Libraries: https://fileflows.com/docs/webconsole/config/libraries
- Processing-node mappings and variables: https://fileflows.com/docs/webconsole/nodes

Check these pages again for current behavior when generating a flow for a newer FileFlows release.

## Documented node catalog

Start with `nodes-index.md` and load only the relevant catalog file. The catalog records every node page found in the official plugin documentation, its rendered input/output shape, documented configuration and behavior sections, branch labels, useful literals, and its primary-source URL.

The catalog is a selection and discovery aid. Public documentation does not define a stable import-JSON schema for every node. A flow export from the target FileFlows version remains authoritative for `FlowElementUid`, model property names and types, defaults, and serialization details.

## Current export envelope

Use a target-version export when available. A current minimal shape is:

```json
{
  "Name": "Flow name",
  "Uid": "uuid",
  "Type": 0,
  "Revision": 1,
  "Properties": {
    "Description": "Purpose",
    "Author": "Author",
    "Fields": [],
    "Variables": {}
  },
  "Parts": []
}
```

Each part contains a UUID, `FlowElementUid`, coordinates, input/output counts, connections, type, and model. Connection shape:

```json
{
  "Input": 1,
  "Output": 1,
  "InputNode": "target-node-uuid"
}
```

## Documented scripting contract

`Function` executes JavaScript through FileFlows and exposes `Variables`, `Logger`, and `Flow`. Use:

```javascript
if (!Flow.IsDirectory)
    return Flow.Fail('Folder input required');

let ffmpeg = Flow.GetToolPath('ffmpeg');
let result = Flow.Execute({
    command: ffmpeg,
    argumentList: ['-v', 'error', '-i', Variables.file.FullName]
});

if (result.standardError)
    Logger.ILog(result.standardError);
if (result.exitCode !== 0)
    return Flow.Fail('ffmpeg failed with exit code ' + result.exitCode);
return 1;
```

Prefer `argumentList` because FileFlows passes discrete arguments and avoids shell interpolation. `Flow.GetToolPath` resolves FileFlows-managed tools. `Flow.Execute` exposes completion, exit code, standard output, and standard error.

C# Function has near-full access to the same flow context and public plugin methods. Its JSON node identifier is version-specific and is not documented on the public C# page. Require a flow export containing a C# Function from the target installation before emitting that node type.

## Validation checklist

- Parse JSON successfully.
- Require unique flow and node UUIDs.
- Require exactly one input node for a simple flow.
- Resolve every `InputNode` reference.
- Validate connection indexes against source outputs and target inputs.
- Match declared script outputs with `Model.Outputs`.
- Reject literal API keys, passwords, bearer tokens, and private URLs when they should be variables.
- Reject shell command construction from media filenames.
- Require visible failure on ambiguity, collision, missing tools, failed mux, failed verification, and failed downstream import when these are task invariants.
- Confirm every host path has the required container mount and that paths passed to Arr are identical in both containers.
