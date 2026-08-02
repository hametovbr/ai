# FileFlows Basic nodes

Generated from the current official FileFlows plugin documentation sitemap.
This is a discovery and authoring index, not a serialization schema. Use a target-version flow export for `FlowElementUid`, model field names, defaults, and JSON shape.
Field and branch labels are retained for exact lookup; prose is deliberately condensed. Open the linked source before relying on version-sensitive behavior.

## Basic (65)

### 7-Zip

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Allows you to 7-zip the input
- Documented literals/examples: `Method`, `Description`, `LZMA2`, `Improved LZMA Compression (Slower)`, `LZMA`, `Better Compression (Slower)`, `PPMd`, `Balanced Compression (Slower)`, `BZip2`, `Good Compression (Moderate)`, `Deflate`, `Standard ZIP Compression (Moderate)`, `Copy`, `No Compression (Fastest)`
- Source: https://fileflows.com/docs/plugins/basic-nodes/seven-zip

### Complete Flow

- Shape: `Logic`; inputs: `1`; outputs: `0`
- Purpose: A flow element that completes or ends the flow execution.
- Source: https://fileflows.com/docs/plugins/basic-nodes/complete-flow

### Copy File

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Copies a file to the destination folder
- Documented configuration/behavior sections: `File To Copy`, `Destination Folder`, `Destination File`, `Copy Folder`, `Additional Files`, `Original Directory`, `Preserve Dates`
- Source: https://fileflows.com/docs/plugins/basic-nodes/copy-file

### Create Folder

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Creates a folder at the specified absolute path on the system. This element ensures that a…
- Documented configuration/behavior sections: `Path`, `Behavior`
- Documented literals/examples: `C:\Media\Movies\NewFolder`, `/media/movies/NewFolder`, `{temp}\{MyVariable}`, `"Folder already exists."`, `"Folder created: [path]"`, `Path: D:\Media\Processed\{file.Name}`, `D:\Media\Processed\Movie1`
- Source: https://fileflows.com/docs/plugins/basic-nodes/create-folder

### Delete

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Deletes either a single file or a single directory.
- Source: https://fileflows.com/docs/plugins/basic-nodes/delete

### Delete Source Folder

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Deletes the source folder of the original library file.
- Documented configuration/behavior sections: `If Empty`, `Include Patterns`, `Top Most Only`
- Output branches: Source folder deleted; Folder was NOT deleted
- Documented literals/examples: `/mnt/library/sub/sub2/sub3/file.mkv`, `sub3`, `/mnt/library`
- Source: https://fileflows.com/docs/plugins/basic-nodes/delete-source-folder

### Executor

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Execute the following process against the file.
- Source: https://fileflows.com/docs/plugins/basic-nodes/executor

### Fail Flow

- Shape: `Logic`; inputs: `1`; outputs: `0`
- Purpose: Fails a flow immediately, useful if you want a certain path to just fail.
- Documented configuration/behavior sections: `Reason`
- Documented literals/examples: `Failure Reason`
- Source: https://fileflows.com/docs/plugins/basic-nodes/fail-flow

### Fail Reason Matches

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Evaluates whether the failure reason specified in the flow matches the provided input.
- Documented configuration/behavior sections: `Match Reason`
- Output branches: Reason matched — the provided reason was found in the…; Reason did not match — the provided reason was not…
- Documented literals/examples: `Contains`, `Failure Reason`
- Source: https://fileflows.com/docs/plugins/basic-nodes/fail-reason-matches

### File Date Compare

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the file creation or last write time matches the specified date constraint.
- Documented configuration/behavior sections: `File Name`, `Date`, `Comparison`
- Output branches: Matches the date constraint.; Does not match the date constraint.
- Source: https://fileflows.com/docs/plugins/basic-nodes/file-date-compare

### File Exists

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if a file exists
- Documented configuration/behavior sections: `File Name`
- Output branches: File exists; File does not exist
- Source: https://fileflows.com/docs/plugins/basic-nodes/file-exists

### File Extension

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the file has one of the configured extensions.
- Source: https://fileflows.com/docs/plugins/basic-nodes/file-extension

### File Name Matches

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the original file name (including the full path) matches the specified value using String…
- Documented configuration/behavior sections: `Match Value`
- Output branches: Matches; Does Not Match
- Source: https://fileflows.com/docs/plugins/basic-nodes/file-name-matches

### File Property Exists

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Tests if a property has been set on this file record. Properties are stored in the…
- Documented configuration/behavior sections: `Property`
- Output branches: The property exists for this file record.; The property does not exist for this file record.
- Source: https://fileflows.com/docs/plugins/basic-nodes/file-property-exists

### File Property Matches

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Tests if a property on this file record matches a given value. Properties are stored in…
- Documented configuration/behavior sections: `Property`, `Value`
- Output branches: The property matches the expected value.; The property does not match the expected value.
- Source: https://fileflows.com/docs/plugins/basic-nodes/file-property-matches

### File Size

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the file size falls within the specified range. File size values are measured in…
- Documented configuration/behavior sections: `Lower`, `Upper`
- Output branches: File size within range – The file size is greater…; File size not within range – The file size falls…
- Documented literals/examples: `0`
- Source: https://fileflows.com/docs/plugins/basic-nodes/file-size

### File Size Compare

- Shape: `Logic`; inputs: `1`; outputs: `3`
- Purpose: Compares the current file size to the original file size to determine if it has changed.
- Output branches: Smaller than original – The current file size is smaller…; Same size as original – The current file size is…; Larger than original – The current file size is larger…
- Source: https://fileflows.com/docs/plugins/basic-nodes/file-size-compare

### File Size Within

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Determines whether the current file size is within a specified difference from the original file size…
- Documented configuration/behavior sections: `Overview`, `Value`, `Example Use Cases`
- Output branches: Output 1 (Within Range): The size difference is within the…; Output 2 (Outside Range): The size difference exceeds the allowed…
- Source: https://fileflows.com/docs/plugins/basic-nodes/file-size-within

### Filename Pattern Replacer

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: This flow element lets you make replacements in the filename.
- Documented configuration/behavior sections: `Replacements`, `Use Working Filename`
- Output branches: Replacement done; No replacement done
- Documented literals/examples: `EMPTY`, `s([\d]+)e([\d]+)`, `$1x$2`, `0([1-9]+x[\d]+)`, `$1`, `\.h265`, `.h265`, `1080p`, `720p`, `Pattern`, `Value`, `Description`, `Trims a leading zero from 01x02 etc`, `Replaces .h265 with an empty string, ie removes that from the filename`, `Replaces 1080p with 720p`
- Source: https://fileflows.com/docs/plugins/basic-nodes/filename-pattern-replacer

### Folder Date Compare

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the folder creation or last write time matches the specified date constraint.
- Documented configuration/behavior sections: `Path`, `Date`, `Comparison`
- Output branches: Matches the date constraint.; Does not match the date constraint.
- Source: https://fileflows.com/docs/plugins/basic-nodes/folder-date-compare

### Folder Iterator

- Shape: `SubFlow`; inputs: `1`; outputs: `1`
- Purpose: Iterates all files in a given folder and executes those files against a sub flow.
- Documented configuration/behavior sections: `Flow`, `Folder`, `Pattern`, `Recursive`
- Variables: IterationIndex Passed into the subflow for each file. This represents the zero-based…; IterationTotal Passed into the subflow for each file. This represents the total…
- Output branches: Files have been iterated successfully.
- Failure branch: A return code from the sub flow was unexpected.
- Documented literals/examples: `Output`, `Output 1`, `*`, `IMAGES`, `\.(jpg|jpeg|jpe|png|gif|bmp|webp)$`, `VIDEOS`, `\.(ts|mp4|mkv|avi|mpe|mpeg|mov|mpv|flv|wmv|webm|avchd|h264|h265)$`, `AUDIO`, `\.(mp3|wav|ogg|aac|wma|flac|alac|m4a|m4p)$`
- Source: https://fileflows.com/docs/plugins/basic-nodes/folder-iterator

### Goto Flow

- Shape: `Logic`; inputs: `1`; outputs: `0`
- Purpose: Allows the flow to switch to a different flow for processing.
- Documented configuration/behavior sections: `Update Flow`, `Behavior`
- Source: https://fileflows.com/docs/plugins/basic-nodes/goto-flow

### Has Hard Links

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if a file has hard links to it.
- Documented configuration/behavior sections: `File Name`, `Count`
- Output branches: Hard links detected; No hard links detected
- Source: https://fileflows.com/docs/plugins/basic-nodes/has-hard-links

### Input File

- Shape: `Input`; inputs: `0`; outputs: `1`
- Purpose: An input flow element for a file.
- Documented configuration/behavior sections: `Behavior`
- Output branches: The selected file path is passed as the current working…
- Source: https://fileflows.com/docs/plugins/basic-nodes/input-file

### Input Folder

- Shape: `Input`; inputs: `1`; outputs: `1`
- Purpose: An input node for selecting a folder.
- Documented configuration/behavior sections: `Behavior`
- Output branches: The selected folder path is passed to the flow as…
- Source: https://fileflows.com/docs/plugins/basic-nodes/input-folder

### Is From Library

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the current file originates from the specified library.
- Documented configuration/behavior sections: `Library`
- Output branches: File is from the specified library – The file belongs…; File is not from the specified library – The file…
- Source: https://fileflows.com/docs/plugins/basic-nodes/is-from-library

### Is Processing On Node

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the flow is currently running on a specified processing node.
- Documented configuration/behavior sections: `Node`
- Output branches: Is processing on node – The flow is running on…; Is not processing on node – The flow is running…
- Source: https://fileflows.com/docs/plugins/basic-nodes/is-processing-on-node

### List Iterator

- Shape: `SubFlow`; inputs: `1`; outputs: `1`
- Purpose: Iterates all strings in a given list and executes those files against a sub flow.
- Documented configuration/behavior sections: `Flow`, `List`
- Variables: IterationIndex Passed into the subflow for each item. This represents the zero-based…; IterationTotal Passed into the subflow for each item. This represents the total…
- Output branches: Strings have been iterated successfully.
- Failure branch: A return code from the sub flow was unexpected.
- Documented literals/examples: `Output`, `Output 1`, `CurrentList`
- Source: https://fileflows.com/docs/plugins/basic-nodes/list-iterator

### Log

- Shape: `Logic`; inputs: `1`; outputs: `1`
- Purpose: Writes a message to the file log, which records log entries specifically for the current processing…
- Documented configuration/behavior sections: `Type`, `Message`
- Documented literals/examples: `Debug`, `Info`, `Warning`, `Error`, `{}`, `Processing file: {File.Name}`, `Finished processing {File.Name}`
- Source: https://fileflows.com/docs/plugins/basic-nodes/log

### Log Contains

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Searches the Flow Runner log for the specified text.
- Documented configuration/behavior sections: `Text`
- Output branches: Text found in log — The specified text was detected…; Text not found in log — The specified text was…
- Documented literals/examples: `Processing completed successfully`, `WARN:`, `{File.Name}`, `error`, `Scenario`, `Text Example`, `Description`, `Detect a specific success message`, `Matches if that phrase is found in the log (case-insensitive).`, `Check for any warning`, `Matches if any log line contains "WARN:" (case-insensitive).`, `Use a variable`, `Searches for the current file name in the log (case-insensitive).`, `Match partial text`, `Finds any line containing “error” (case-insensitive).`
- Source: https://fileflows.com/docs/plugins/basic-nodes/log-contains

### Log Image

- Shape: `Logic`; inputs: `1`; outputs: `1`
- Purpose: Logs an image to the file log associated with the current processing file.
- Documented configuration/behavior sections: `Image`
- Output branches: Image was logged – The image was successfully added to…; Image failed to be logged – There was an error…
- Source: https://fileflows.com/docs/plugins/basic-nodes/log-image

### Log Variables

- Shape: `Logic`; inputs: `1`; outputs: `1`
- Purpose: Logs all the variables in the flow to the file log for debugging purposes.
- Documented configuration/behavior sections: `Detailed Logging`
- Output branches: Variables have been logged successfully – Indicates that all variables…
- Source: https://fileflows.com/docs/plugins/basic-nodes/log-variables

### Matches

- Shape: `Logic`; inputs: `1`; outputs: `4`
- Purpose: Compares a set of values and matches conditions to see which output should be called.
- Documented configuration/behavior sections: `Matches`
- Source: https://fileflows.com/docs/plugins/basic-nodes/matches

### Matches All

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Compares a set of values and checks if all conditions match.
- Documented configuration/behavior sections: `Matches`
- Output branches: All conditions match; Not all conditions match
- Source: https://fileflows.com/docs/plugins/basic-nodes/matches-all

### Move File

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Moves a file to the destination folder
- Documented configuration/behavior sections: `File To Move`, `Destination Folder`, `Destination File`, `Copy Folder`, `Delete Original`, `Additional Files`, `Original Directory`, `Perserve Dates`
- Output branches: File was moved successfully; File was moved, however the original file failed to be…
- Source: https://fileflows.com/docs/plugins/basic-nodes/move-file

### Move Folder

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Moves a folder
- Documented configuration/behavior sections: `Source`, `Destination`, `Create Subfolder`, `If Destination Already Exists`
- Documented literals/examples: `Working File`, `/data/backup`, `/archive`, `/archive/backup`
- Source: https://fileflows.com/docs/plugins/basic-nodes/move-folder

### Original File

- Shape: `Logic`; inputs: `1`; outputs: `1`
- Purpose: Sets the current working file in the flow back to the original file that triggered the…
- Documented configuration/behavior sections: `Behavior`
- Source: https://fileflows.com/docs/plugins/basic-nodes/original-file

### Pattern

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Tests the working file and original file against a regular expression.
- Output branches: Matches expression; Does not match
- Documented literals/examples: `PatternMatch`
- Source: https://fileflows.com/docs/plugins/basic-nodes/pattern-match

### Random

- Shape: `Logic`; inputs: `1`; outputs: `4`
- Purpose: Allows you to configure between 2 and 10 outputs, and one of those outputs will be…
- Source: https://fileflows.com/docs/plugins/basic-nodes/random

### Renamer

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Renames the working file. Variables can be used by entering the key { inside the New…
- Documented literals/examples: `{`
- Source: https://fileflows.com/docs/plugins/basic-nodes/renamer

### Replace Original

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Replaces the original file with the working file.
- Documented configuration/behavior sections: `Perserve Dates`
- Source: https://fileflows.com/docs/plugins/basic-nodes/replace-original

### Reprocess

- Shape: `Process`; inputs: `1`; outputs: `0`
- Purpose: Requeues the original library file to be reprocessed, optionally on a different processing node and after…
- Documented configuration/behavior sections: `Node`, `Hold Minutes`
- Documented literals/examples: `0`, `Hold Minutes`
- Source: https://fileflows.com/docs/plugins/basic-nodes/reprocess

### Set File Property

- Shape: `Logic`; inputs: `1`; outputs: `1`
- Purpose: Sets a property on this file record. Properties are stored in the file's database record and…
- Documented configuration/behavior sections: `Property`, `Value`
- Output branches: The property was set on this file record.
- Source: https://fileflows.com/docs/plugins/basic-nodes/set-file-property

### Set Variable

- Shape: `Logic`; inputs: `1`; outputs: `1`
- Purpose: The Set Variable flow element creates or updates a variable that can be referenced later in…
- Documented configuration/behavior sections: `Variable`, `Value`
- Documented literals/examples: `{VariableName}`, `a-z`, `A-Z`, `_`, `.`, `flag`, `count.total`, `result_{StepNumber}`, `result_2`, `StepNumber=2`, `1start`, `.hidden`, `invalid name`, `^[a-zA-Z_][a-zA-Z0-9_\.]*$`, `true`, `false`, `123`, `12.34`, `Username = bob`, `user.{Username}`
- Source: https://fileflows.com/docs/plugins/basic-nodes/set-variable

### Set Working File

- Shape: `Process`; inputs: `0`; outputs: `1`
- Purpose: A flow element that updates the current working file to the one specified.
- Documented configuration/behavior sections: `File`, `Don't Delete Previous`
- Source: https://fileflows.com/docs/plugins/basic-nodes/set-working-file

### Sleep

- Shape: `Logic`; inputs: `1`; outputs: `1`
- Purpose: Pauses the flow execution for a specified duration in milliseconds.
- Documented configuration/behavior sections: `Milliseconds`
- Documented literals/examples: `5000`
- Source: https://fileflows.com/docs/plugins/basic-nodes/sleep

### Tag

- Shape: `Logic`; inputs: `1`; outputs: `1`
- Purpose: This allows you to attach one or more custom labels or tags to the file's database…
- Documented configuration/behavior sections: `Configuration Options`, `Usage Example`
- Documented literals/examples: `HDR`, `Atmos`, `Setting`, `Action`, `Description`, `Off (Append)`, `Adds the new tags.`, `On (Replace)`, `Overwrites existing tags.`
- Source: https://fileflows.com/docs/plugins/basic-nodes/tag

### Touch

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Updates the last write time (modified time) of a file or directory to the current time.
- Documented configuration/behavior sections: `File Name�`, `Behavior Notes`
- Documented literals/examples: `touch`, `processed.txt`, `/media/output/processed.txt`
- Source: https://fileflows.com/docs/plugins/basic-nodes/touch

### Unpack

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Allows you to unpack an archive, zip, rar, tar etc.
- Documented configuration/behavior sections: `Destination Folder`, `File`
- Documented literals/examples: `{folder.Orig.FullName}`
- Source: https://fileflows.com/docs/plugins/basic-nodes/unpack

### Variable Exists

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks whether a variable is defined and not null.
- Documented configuration/behavior sections: `Variable`
- Output branches: Variable exists – The variable is defined and its value…; Variable does not exist – The variable is either undefined…
- Documented literals/examples: `null`, `MyVariable`, `{}`, `Variables.`, `movie.Title`, `Title`, `movie`
- Source: https://fileflows.com/docs/plugins/basic-nodes/variable-exists

### Variable Match

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Tests if a variable matches the given value.
- Documented configuration/behavior sections: `Variable`, `Value`
- Output branches: Input matched variable – The variable matched the given value.; Input did not match variable – The variable did not…
- Documented literals/examples: `MyVariable`, `movie.Title`, `movie.Year`, `>123`, `<100`, `=456`, `456`, `abc`, `*abc*`, `abc*`, `*abc`, `>2000`
- Source: https://fileflows.com/docs/plugins/basic-nodes/variable-match

### Write Text

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Writes text to a file.
- Documented configuration/behavior sections: `File`, `Text`, `CSV Files`
- Output branches: Text written to file
- Documented literals/examples: `File`, `.csv`, `Text`, `;`, `,`, `{file.Name},{ext}`, `"file.mkv","mkv"`
- Source: https://fileflows.com/docs/plugins/basic-nodes/write-text

### Zip

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Allows you to zip the input
- Documented configuration/behavior sections: `Path`, `Destination Folder`, `Destination File`, `Set Working File`
- Output branches: Zip file created
- Source: https://fileflows.com/docs/plugins/basic-nodes/zip

### Category: Conditions

#### If Boolean

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Tests if a boolean variable is true
- Source: https://fileflows.com/docs/plugins/basic-nodes/conditions/if-boolean

#### If String

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Tests if a string matches a specified value and triggers the corresponding output if it does.
- Documented configuration/behavior sections: `Behavior`
- Output branches: String matches – The input string matched the specified value.; String does not match – The input string did not…
- Source: https://fileflows.com/docs/plugins/basic-nodes/conditions/if-string

### Category: Scripting

#### Batch Script (.bat)

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Allows you to execute a batch (.bat) script in a Windows environment.
- Documented configuration/behavior sections: `Code`, `Set Working File`, `Exit Codes`
- Documented literals/examples: `SetWorkingFile`, `echo "SETWORKINGFILE=..."`, `1+`, `Outputs`, `0`, `other`, `Number`, `Description`
- Source: https://fileflows.com/docs/plugins/basic-nodes/scripting/batch-script

#### C# Script

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Allows you to execute C# code in a flow. This has full access to the Flow…
- Documented configuration/behavior sections: `Return Codes`
- Documented literals/examples: `1+`, `Outputs`, `0`, `-1`, `FFmpeg Builder: Start`, `FFmpeg Builder: Executor`, `Number`, `Description`, `Indicates an error and stops the flow. This will mark the flow as unsuccessful.`
- Source: https://fileflows.com/docs/plugins/basic-nodes/scripting/csharp

#### Function

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: The function flow element allows you to use custom JavaScript code to process within the flow.
- Documented configuration/behavior sections: `Return Codes`
- Documented literals/examples: `1+`, `Outputs`, `0`, `-1`, `Number`, `Description`, `Indicates an error and stops the flow. This will mark the flow as unsuccessful.`
- Source: https://fileflows.com/docs/plugins/basic-nodes/scripting/function

#### PowerShell Script

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Allows you to execute a PowerShell (.ps1) script in a Windows environment.
- Documented configuration/behavior sections: `Code`, `Set Working File`, `Exit Codes`
- Documented literals/examples: `SetWorkingFile()`, `SetWorkingFile("C:\path\to\newfile.mp4")`, `Write-Output "SETWORKINGFILE=..."`, `1+`, `Outputs`, `0`, `other`, `Number`, `Description`
- Source: https://fileflows.com/docs/plugins/basic-nodes/scripting/powershell-script

#### Shell Script

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Allows you to execute a shell (.sh) script in a Unix-like environment.
- Documented configuration/behavior sections: `Code`, `Set Working File`, `Exit Codes`
- Documented literals/examples: `SetWorkingFile()`, `echo "SETWORKINGFILE=..."`, `1+`, `Outputs`, `0`, `other`, `Number`, `Description`
- Source: https://fileflows.com/docs/plugins/basic-nodes/scripting/shell-script

### Category: System

#### Is Docker

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Determines if the flow is running on Docker
- Output branches: Flow is running on Docker; Flow is not running on Docker
- Source: https://fileflows.com/docs/plugins/basic-nodes/system/is-docker

#### Is Linux

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Determines if the flow is running on Linux
- Output branches: Flow is running on Linux; Flow is not running on Linux
- Source: https://fileflows.com/docs/plugins/basic-nodes/system/is-linux

#### Is MacOS

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Determines if the flow is running on MacOS
- Output branches: Flow is running on MacOS; Flow is not running on MacOS
- Source: https://fileflows.com/docs/plugins/basic-nodes/system/is-mac-os

#### Is Windows

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Determines if the flow is running on Windows
- Output branches: Flow is running on Windows; Flow is not running on Windows
- Source: https://fileflows.com/docs/plugins/basic-nodes/system/is-windows

### Category: Templating

#### Output Path

- Shape: `Logic`; inputs: `1`; outputs: `0`
- Purpose: Special flow element that is only to be used in a template flow.
- Documented literals/examples: `Output Path`
- Source: https://fileflows.com/docs/plugins/basic-nodes/templating/output-path
