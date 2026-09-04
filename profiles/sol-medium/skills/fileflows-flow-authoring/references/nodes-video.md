# FileFlows Video nodes

Generated from the current official FileFlows plugin documentation sitemap.
This is a discovery and authoring index, not a serialization schema. Use a target-version flow export for `FlowElementUid`, model field names, defaults, and JSON shape.
Field and branch labels are retained for exact lookup; prose is deliberately condensed. Open the linked source before relying on version-sensitive behavior.

## Video (110)

### Audio To Video

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Allows converting of audio files into a video file using one the visualizations.
- Documented configuration/behavior sections: `Fields`, `Visualisations`
- Source: https://fileflows.com/docs/plugins/video-nodes/audio-to-video

### Comskip Remove Ads

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: This flow element will attempt to remove ads from a video file using a file from…
- Documented configuration/behavior sections: `Run Comskip`, `Comskip.ini`
- Output branches: Ads removed; No ads found/removed
- Documented literals/examples: `comskip.ini`, `comskipini`
- Source: https://fileflows.com/docs/plugins/video-nodes/comskip-remove-ads

### Create Thumbnail

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Creates a thumbnail image from a video file.
- Documented configuration/behavior sections: `Output File`, `Width`, `Height`, `Mode`, `Time`, `Skip Black Frames`
- Output branches: Thumbnail created.; Failed to create thumbnail.
- Source: https://fileflows.com/docs/plugins/video-nodes/create-thumbnail

### Read Video Info

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Reads the video information from the current working file and updates the video information in the…
- Output branches: File was a video file and information read into flow; File was not a video file or failed to be…
- Documented literals/examples: `Variables`
- Source: https://fileflows.com/docs/plugins/video-nodes/read-video-info

### Subtitle Extractor

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Extracts subtitle tracks and saves them to the destination.
- Documented configuration/behavior sections: `Language`, `Title`, `Extract All`, `Output File`, `Forced Only`, `Only Text Subtitles`, `Extract as SRT/SUP`
- Output branches: Subtitle(s) extracted; No subtitles extracted
- Documented literals/examples: `en|jpn|deu`, `{folder.Orig.FullName}\{file.Orig.FileName}.srt`, `Variable`, `Description`, `Type`, `Example`, `sub.FileName`, `The full path of the extract subtitle file`, `string`, `/path/to/subtitle.sub`
- Source: https://fileflows.com/docs/plugins/video-nodes/subtitle-extractor

### Video Extract Audio

- Shape: `Input`; inputs: `1`; outputs: `2`
- Purpose: Extracts audio from a video file and saves it to a file
- Documented literals/examples: `{folder.Orig.FullName}\{file.Orig.FileName}.mp3`, `Variable`, `Description`, `Type`, `Example`, `ExtractedAudioFile`, `The full path of the extract audio file`, `string`, `/mnt/audio/extracted.mp3`
- Source: https://fileflows.com/docs/plugins/video-nodes/video-extract-audio

### Video File

- Shape: `Input`; inputs: `0`; outputs: `1`
- Purpose: Video File is an input node which will scan a file and load the Video Information…
- Documented configuration/behavior sections: `Probe Size`, `Analyze Duration`
- Documented literals/examples: `Variable`, `Description`, `Type`, `Example`, `video.VideoInfo`, `VideoInfo object`, `object`, `See Below`, `video.Width`, `Width of video`, `number`, `1920`, `video.Height`, `Height of video`, `1080`, `video.Duration`, `Duration of video in seconds`, `60`, `video.Video.Codec`, `Codec of video`
- Source: https://fileflows.com/docs/plugins/video-nodes/video-file

### Category: Ffmpeg Builder

#### Add Input File

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will search for matching files and add them as input files to FFmpeg…
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/add-input-file

#### Aspect Ratio

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: The Aspect Ratio flow element allows users to define and adjust the aspect ratio of a…
- Documented configuration/behavior sections: `Aspect Ratio`, `Adjustment Mode`, `Custom Width`, `Custom Height`
- Output branches: Aspect ratio was changed successfully; Video was already in the desired aspect ratio
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/aspect-ratio

#### Audio Add Track

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will add a new audio track to `FFmpeg Builder``.
- Documented configuration/behavior sections: `General`, `Quality`, `Title`, `The string separator used between format values, this is needed to ensure no empty values are kept.`, `Advanced`, `Codec Override`
- Output branches: Audio track added to FFmpeg Builder Model; No suitable source audio track found to create new audio…
- Documented literals/examples: `Language Helper`, `English`, `eng`, `lang / codec / channels`, `volume=2.0`, `volume=0.5`, `aecho=0.8:0.88:1000:0.4`, `acompressor=threshold=-12dB:ratio=3:attack=5:release=50`, `highpass=f=300`, `lowpass=f=3000`, `aformat=channel_layouts=stereo`, `afade=t=in:ss=0:d=5`, `treble=g=5`, `bass=g=-5`, `silenceremove=start_periods=-1:start_threshold=-50dB:detection=peak`, `atempo=1.5`, `asetrate=44100`, `dynaudnorm`, `earwax`, `CodecName_Codec`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/audio-add-track

#### Audio Adjust Volume

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: This flow element will update "FFmpeg Builder" and adjust the volume by percentage of all currently…
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/audio-adjust-volume

#### Audio Convert

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will convert audio to a the options selected.
- Documented configuration/behavior sections: `Convert`, `Matching`, `Codec`, `Channels`, `Bitrate`, `Bitrate Per Channel`, `Codec Override`
- Output branches: Audio tracks matched the parameters and will be converted; Audio tracks did not match and no conversion will occur
- Documented literals/examples: `Language Helper`, `English`, `eng`, `Codec`, `Channels`, `Same as source`, `Bitrate`, `Automatic`, `CodecName_Codec`, `libfdk_aac`, `AAC_Codec`, `Property`, `Description`, `Chanenls`, `Can use Math Operations or specific how many channels exactly z`, `Can use String Operations`, `Language`, `Title`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/audio-convert

#### Audio Converter

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will normalize audio against the matching tracks in the output file.
- Documented configuration/behavior sections: `Codec`, `Channels`, `Bitrate`, `Bitrate Per Channel`, `Field`, `Pattern`, `Not Matching`, `Codec Override`
- Output branches: Audio tracks matched the parameters and will be normalized; Audio tracks did not match and no normalizing will occur
- Documented literals/examples: `Codec`, `Channels`, `Same as source`, `Bitrate`, `Automatic`, `commentary`, `.*commentary.*`, `German`, `deu`, `CodecName_Codec`, `libfdk_aac`, `AAC_Codec`, `Field`, `Description`, `Convert All`, `All audio tracks will be converted`, `Title`, `Uses the title of the track to match against`, `Uses the codec of the track to match against`, `Language`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/audio-converter

#### Audio Detect Language

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element looks for any audio tracks that have no language code set, or are…
- Documented configuration/behavior sections: `How It Works`, `Sampling Strategy`, `Configuration`
- Output branches: Language detected for one or more audio tracks, and track(s)…; No tracks needed updating, or language detection failed for all…
- Documented literals/examples: `und`, `5`, `60`, `180`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/audio-detect-language

#### Audio Language Converter

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: The Audio Language Converter flow element adds new audio tracks for specified languages using your preferred…
- Documented configuration/behavior sections: `Configuration`
- Output branches: Audio tracks were successfully added to the FFmpeg model.; No audio tracks were added (e.g., matching languages were not…
- Documented literals/examples: `CodecName_Codec`, `libfdk_aac`, `AAC_Codec`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/audio-language-converter

#### Audio Normalization

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will normalize audio against the matching tracks in the output file.
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/audio-normalization

#### Auto Chapters

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element automatically generates chapters by analyzing the video for scene changes.
- Documented literals/examples: `{index}`, `Chapter {index}`, `Chapter 1`, `Chapter 2`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/auto-chapters

#### Bitrate Encode

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: This flow element will ALWAYS encode a video to the quality level and codec specific.
- Documented configuration/behavior sections: `Codec`, `Encoder`, `Bitrate`
- Documented literals/examples: `Name`, `Notes`, `H.264`, `Older codec, wide playback support, but larger files`, `HEVC (Automatic)`, `HEVC (8-Bit)`, `Forces 8-bit HEVC video, this has wider support than 10-bit`, `HEVC (10-Bit)`, `AV-1`, `New codec, smaller than HEVC, but not many devices support this codec yet`, `AV-1 (10-Bit)`, `10-bit color depth produces more colors and better quality`, `VP9`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/bitrate-encode

#### Change Language Code

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: The FFmpeg Builder: Change Language Code flow element modifies language codes on all video, audio, and…
- Documented configuration/behavior sections: `Purpose`, `Replacements`
- Output branches: One or more language replacements were made.; No replacements were performed.
- Documented literals/examples: `"eng"`, `"en"`, `"cn"`, `"zht"`, `Key`, `Value`, `eng`, `en`, `fre`, `fr`, `cn`, `zht`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/change-language-code

#### Comskip Chapters

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will look for a comskip .edl file matching the working file. eg /media/movies/mymovie.mkv…
- Documented configuration/behavior sections: `Run Comskip`, `Comskip.ini`
- Output branches: A .edl file was found with chapters and a metadata…; No .edl file or no chapters were found.
- Documented literals/examples: `/media/movies/mymovie.mkv /media/movies/mymovie.edl`, `comskip.ini`, `comskipini`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/comskip-chapters

#### Crop Black Bars

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will scan the video file when first called and detect if black bars…
- Documented configuration/behavior sections: `Threshold`
- Documented literals/examples: `FFmpeg Builder: Executor`, `Threshold`, `10`, `1920x1080`, `1920x1070`, `1920x1076`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/crop-black-bars

#### Crop Black Bars (Clustered)

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element scans the video file to detect black bars using a clustered approach, analyzing…
- Documented configuration/behavior sections: `Detection Mode`, `Custom Options`
- Output branches: Output 1: Black bars were detected and meet the threshold.; Output 2: No significant black bars detected, or not above…
- Documented literals/examples: `FFmpeg Builder: Executor`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/crop-black-bars-clustered

#### Custom Parameters

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: This flow element lets you add custom parameters to the FFmpeg Builder for execution.
- Documented configuration/behavior sections: `Parameters`, `Force Encode`, `Arguments`
- Documented literals/examples: `-metadata "title=Some Title"`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/custom-parameters

#### Custom Video Filter

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: Adds a single custom video filter to the FFmpeg Builder. This element is intended for advanced…
- Documented configuration/behavior sections: `Filter`, `Hardware Filter`
- Output branches: The filter was successfully added to the FFmpeg Builder model…
- Documented literals/examples: `scale=1920:1080`, `crop=1280:720`, `hqdn3d=1.5:1.5:6:6`, `eq=contrast=1.2:brightness=0.05`, `hue=s=0`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/custom-video-filter

#### Default Original Language

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will attempt to set the original language tracks as default. It will try…
- Documented configuration/behavior sections: `Type`, `Make First`
- Output branches: Tracks have been modified; No tracks have been changed
- Documented literals/examples: `OriginalLanguage`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/default-original-language

#### Deinterlace

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: Adds a deinterlace filter to the FFmpeg Builder command to deinterlace the video file.
- Documented configuration/behavior sections: `Mode`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/deinterlace

#### Denoise

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: Adds a denoise filter to the FFmpeg Builder command to reduce noise and grain in the…
- Documented configuration/behavior sections: `Strength`
- Output branches: Added denoise filter to the video stream
- Documented literals/examples: `nvdenoise`, `strength`, `vpp_qsv=denoise`, `denoise_vaapi=default`, `hqdn3d`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/denoise

#### Disable FileFlows Metadata

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: Disables the FileFlows metadata (the 'Created by FileFlows' comment) from being written to the output file.
- Documented configuration/behavior sections: `Disable`
- Output branches: FileFlows metadata disabled setting updated
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/disable-fileflows-metadata

#### Duration/Start

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This element lets users define a segment to extract from a video by specifying its starting…
- Documented configuration/behavior sections: `Start`, `Duration`
- Output branches: Duration and start point successfully configured.; An error occurred while setting duration or start point.
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/duration-start

#### GPU Selector

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: This flow element allows you to specify which GPU should be used for encoding and decoding…
- Documented configuration/behavior sections: `Index`
- Output branches: FFmpeg configuration updated to use the specified GPU
- Documented literals/examples: `1`, `2`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/gpu-selector

#### HDR to SDR

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will first check to see if the working file is HDR.
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/hdr-to-sdr

#### Image Subtitle Converter

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: Converts bitmap-based subtitle tracks to text-based subtitles.
- Documented configuration/behavior sections: `Convert All`, `Languages`
- Output branches: Image-based subtitle tracks found and will be converted; No image-based subtitle tracks found
- Documented literals/examples: `true`, `false`, `eng`, `deu`, `fra`, `spa`, `ita`, `rus`, `Value`, `Description`, `All image-based subtitle tracks will be converted to text-based`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/image-subtitle-converter

#### Keep Original Language

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will keep only the original language and any additional languages the user defines.
- Documented configuration/behavior sections: `Type`, `Additional Languages`, `Keep Only First`, `First If None`, `Treat Empty As Original`
- Output branches: Tracks have been modified; No tracks have been changed
- Documented literals/examples: `OriginalLanguage`, `eng`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/keep-original-language

#### Language Remover

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: A basic flow element that removes unwanted audio and/or subtitles from a video file based on…
- Documented configuration/behavior sections: `Track Type`, `Not Matching`, `Languages`
- Output branches: Tracks marked for removal; Tracks NOT marked for removal
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/language-remover

#### Metadata Remover

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: The Metadata Remover is an FFmpeg Builder flow element that removes selected metadata from media files…
- Documented configuration/behavior sections: `Use Cases`, `Fields`, `Behavior Details`, `Example Workflow`, `Technical Notes`
- Documented literals/examples: `-map_metadata -1`, `Field`, `Description`, `Video`, `Remove metadata from video tracks.`, `Audio`, `Remove metadata from audio tracks.`, `Subtitle`, `Remove metadata from subtitle tracks.`, `Remove Images`, `Remove Title`, `Remove titles set on any selected tracks.`, `Remove Language`, `Remove language tags from audio and subtitle tracks.`, `Remove Additional Metadata`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/metadata-remover

#### Parameter Replacer

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: The FFmpeg Builder: Parameter Replacer flow element modifies FFmpeg command-line parameters by applying configured string replacements…
- Documented configuration/behavior sections: `Purpose`, `Replacements`, `Use Cases`, `How to Set in JavaScript`
- Output branches: One or more parameter replacements or removals were applied.; No replacements or removals were made.
- Documented literals/examples: `args`, `-preset medium`, `-preset fast`, `-filter_complex oldval`, `-filter_complex "val1 val2"`, `-filter_complex val1 val2`, `val1`, `val2`, `-map`, `-filter_complex somevalue`, `-filter_complex "new value"`, `FfmpegBuilderModel`, `builder.AddParameterReplacement("-c:v libx264", "-c:v hevc_nvenc");`, `builder.ClearParameterReplacements();`, `-i`, `ffmpeg -hwaccel cuda -i input.mp4 ...`, `Key`, `Value`, `Resulting Arguments`, `Replaces -preset medium with -preset fast`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/parameter-replacer

#### Pre-Execute

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: This element lets you run custom code just prior to the FFmpeg Builder: Executor executes FFmpeg.
- Documented literals/examples: `for(let arg of FFmpeg.Args){ Logger.ILog('FFmpeg arg: ' + arg);}`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/pre-execute

#### Prores

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: Encodes the video to the Apple prores format.
- Documented configuration/behavior sections: `Profile`, `Pixel Format`, `Quality`
- Documented literals/examples: `Name`, `Value`, `Proxy`, `0`, `LT`, `1`, `SQ`, `2`, `HQ`, `3`, `4:2:2`, `yuva422p10le`, `4:4:4`, `yuva444p10le`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/prores

#### Remove Attachments

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: Removes any attachments from the video, if there are any.
- Documented literals/examples: `FFmpeg Builder: Executor`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/remove-attachments

#### Remux to MKV

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: This flow element updates the FFmpeg Builder to save the output file in a MKV container.
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/remux-to-mkv

#### Remux to MOV

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: This flow element updates the FFmpeg Builder to save the output file in a MOV container.
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/remux-to-mov

#### Remux to MP4

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: This flow element updates the FFmpeg Builder to save the output file in a MP4 container.
- Documented configuration/behavior sections: `Use HVC1`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/remux-to-mp4

#### Remux to MXF

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: This flow element updates the FFmpeg Builder to save the output file in a MXF container.
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/remux-to-mxf

#### Remux to TS

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: This flow element updates the FFmpeg Builder to save the output file in a TS container.
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/remux-to-ts

#### Remux to WEBM

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: This flow element updates the FFmpeg Builder to save the output file in a WEBM container.
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/remux-to-webm

#### Set Default Track

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will search for the given audio, subtitle track or both and set them…
- Documented configuration/behavior sections: `Type`, `Languages`, `Index`
- Documented literals/examples: `en|jp`, `Language`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/set-default-track

#### Set Device

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element sets the VAAPI render device path FFmpeg should use for hardware-accelerated encoding or…
- Documented configuration/behavior sections: `Device`
- Documented literals/examples: `/dev/dri/renderD128`, `/dev/dri/renderD129`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/set-device

#### Set Forced

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: Sets a specific subtitle track as forced and clears the forced flag from all other subtitle…
- Documented configuration/behavior sections: `Track Selection`
- Output branches: Subtitle found: Matching track was found and set to forced…; No match: No matching subtitle track was found to modify.
- Documented literals/examples: `Language Helper`, `en`, `English`, `eng`, `Property`, `Description`, `Codec`, `Filter by the subtitle format. Supports String Operations.`, `Language`, `Title`, `Filter by the track title metadata. Supports String Operations.`, `Index`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/set-forced

#### Set FPS

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will set the frames per second (FPS) in the FFmpeg Builder.
- Documented configuration/behavior sections: `FPS`, `Only If Higher`
- Documented literals/examples: `60`, `30`, `24`, `Current FPS`, `Desired FPS`, `Changed`, `✅`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/set-fps

#### Set Language

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will look for any tracks that have no language code set on them…
- Documented configuration/behavior sections: `Type`, `Languages`
- Output branches: Tracks found with no language codes, and have been updated…; No tracks with missing language codes found
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/set-language

#### Set Track Titles

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will set track titles based on a formatter in the FFmpeg builder
- Documented configuration/behavior sections: `Type`, `Formatter`
- Output branches: Track titles updated in FFmpeg Builder; No track titles were effected
- Documented literals/examples: `lang`, `lang-iso1`, `lang-iso2`, `lang!`, `lang-iso1!`, `lang-iso2!`, `!lang`, `!lang-iso1`, `!lang-iso2`, `codec`, `!codec`, `codec-cc`, `!codec-cc`, `codec-cc!`, `default`, `Default`, `forced`, `Forced`, `channels`, `Mono`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/set-track-titles

#### Strip Dolby Vision (DOVI)

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: Removes Dolby Vision (DOVI) metadata from the video stream by updating the FFmpeg Builder model.
- Documented configuration/behavior sections: `What it does`
- Output branches: Dolby Vision was detected and the FFmpeg Builder model was…; Dolby Vision was not detected; no changes were made to…
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/strip-dovi

#### Subtitle Burn-In

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: Burns subtitles into the video file.
- Documented configuration/behavior sections: `Track Selection`
- Output branches: Subtitle found and will be burnt into the video; No subtitle found to burn in
- Documented literals/examples: `Language Helper`, `English`, `eng`, `Property`, `Description`, `Codec`, `Can use String Operations`, `Language`, `Title`, `Index`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/subtitle-burn-in

#### Subtitle Detect Language

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element detects the language of subtitle tracks that do not already have a language…
- Documented configuration/behavior sections: `How It Works`, `Language Handling`
- Output branches: One or more subtitle tracks had their language metadata detected…; No subtitle tracks needed language detection, or all detection attempts…
- Documented literals/examples: `und`, `unknown`, `eng`, `fra`, `spa`, `deu`, `ita`, `jpn`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/subtitle-detect-language

#### Subtitle Format Remover

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will update the "FFmpeg Builder" to remove subtitles that are in the desired…
- Output branches: Subtitles were found and marked for removal; Subtitles were not found and not marked for removal
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/subtitle-format-remover

#### Subtitle Generator

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: The Subtitle Generator creates subtitle tracks from the source audio and adds them to the active…
- Documented configuration/behavior sections: `How It Works`, `Configuration`
- Output branches: Subtitle tracks were generated and added to FFmpeg Builder.; No subtitle tracks were generated or added.
- Documented literals/examples: `eng`, `deu`, `fra`, `spa`, `ita`, `rus`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/subtitle-generator

#### Subtitle Resolver

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: The Subtitle Resolver updates the FFmpeg Builder subtitle model so the output file contains the subtitle…
- Documented configuration/behavior sections: `How It Works`, `Configuration`, `Source Selection`
- Output branches: Subtitle tracks were resolved and the FFmpeg Builder model was…; No subtitle changes were needed, or no changes could be…
- Documented literals/examples: `eng`, `en`, `spa`, `es`, `deu`, `de`, `fra`, `fr`, `jpn`, `ja`, `true`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/subtitle-resolver

#### Subtitle Track Merge

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will search for external subtitles and add them as input files to the…
- Documented configuration/behavior sections: `Subtitles`, `Use Source Directory`, `Match Filename`, `Pattern`, `Title`, `Forced`, `Default`
- Output branches: Subtitles found and added; Subtitles not found
- Documented literals/examples: `Match Filename`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/subtitle-track-merge

#### Subtitle Translator

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: The Subtitle Translator translates an existing subtitle track from a source language into a target language…
- Documented configuration/behavior sections: `How It Works`, `Track Selection`, `Configuration`
- Output branches: A subtitle track was translated and added to the FFmpeg…; No subtitle track was translated or added.
- Documented literals/examples: `eng`, `deu`, `fra`, `spa`, `ita`, `rus`, `jpn`, `zho`, `kor`, `por`, `ara`, `hin`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/subtitle-translator

#### Track Remover

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will update "FFmpeg Builder" to remove all the matching tracks from the output…
- Documented configuration/behavior sections: `Type`, `Matching`
- Output branches: Tracks set to remove; Tracks NOT set to removed
- Documented literals/examples: `>=1`, `Language Helper`, `English`, `eng`, `Property`, `Description`, `Bitrate`, `Chanenls`, `Can use Math Operations or specific how many channels exactly`, `Codec`, `Can use String Operations`, `Language`, `Title`, `Index`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/track-remover

#### Track Remover (Obsolete)

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will update "FFmpeg Builder" to remove all the matching tracks from the output…
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/track-remover-obsolete

#### Track Sorter

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will sort the audio and subtitles tracks given the parameters and update the…
- Documented configuration/behavior sections: `Type`, `Set Default`, `Sorters`
- Output branches: Tracks have been reordered in FFmpeg Builder; Tracks have NOT been reordered
- Documented literals/examples: `Reversed`, `Bitrate Reversed`, `Default`, `Forced`, `true`, `1`, `false`, `0`, `Default = true`, `Default = false`, `Forced = true`, `Forced = false`, `FFmpeg Builder`, `>=5.1`, `5.1`, `orig`, `German`, `deu`, `100000`, `7.1`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/track-sorter

#### Trim End Credits

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element analyzes the end of a video to detect whether it contains an end…
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/trim-end-credits

#### Trim Silence

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element analyzes the end of a video to detect if there is a period…
- Documented literals/examples: `-60 dB`, `-10 dB`, `-30 dB`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/trim-silence

#### Video Bitrate

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: Sets FFmpeg Builder to encode the video given the bitrate
- Documented literals/examples: `Codec: h265|hevc|h264Video Codec Parameters: h265|hevc|h264`, `Codec: h265Video Codec Parameters: h265`, `Codec: hevcVideo Codec Parameters: hevc`, `Codec: h264Video Codec Parameters: h264`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/video-bitrate

#### Video Codec

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will set all video streams in the file to encode using the video…
- Documented configuration/behavior sections: `Video Codec`, `Video Codec Parameters`, `Force Encode`, `Only First`
- Output branches: The video was update and encoding was set on the…; The video was already in the required codec or no…
- Documented literals/examples: `Force Encode`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/video-codec

#### Video Encode

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: Sets the FFMPEG Builder to encode the video with simple-to-use presets.
- Documented configuration/behavior sections: `Codec`, `Encoder`, `Quality`, `Speed`
- Documented literals/examples: `Name`, `Notes`, `H.264`, `Older codec, wide playback support, but larger files`, `HEVC (Automatic)`, `HEVC (8-Bit)`, `Forces 8-bit HEVC video, this has wider support than 10-bit`, `HEVC (10-Bit)`, `AV-1`, `New codec, smaller than HEVC, but not many devices support this codec yet`, `AV-1 (10-Bit)`, `10-bit color depth produces more colors and better quality`, `VP9`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/video-encode

#### Video Encode

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: This flow element will ALWAYS encode a video to the quality level and codec specific.
- Documented configuration/behavior sections: `Codec`, `Encoder`, `Quality`, `Speed`, `Codecs`
- Documented literals/examples: `Slower`, `Slow`, `p0`, `p1`, `-rc constop -qp {QualityValue} -preset p6 -spatial-aq 1`, `-global_quality {QualityValue} -preset slower`, `-qp {QualityValue} -preset slower -spatial-aq 1`, `-qp {QualityValue} -preset slower`, `libx264 -preset slower -crf {QualityValue}`, `libx265 -preset slower -crf {QualityValue}`, `libsvtav1 -preset 4 -crf {QualityValue}`, `libvpx-vp9 -preset slower -crf {QualityValue}`, `Name`, `Notes`, `H.264`, `Older codec, wide playback support, but larger files`, `HEVC (Automatic)`, `HEVC (8-Bit)`, `Forces 8-bit HEVC video, this has wider support than 10-bit`, `HEVC (10-Bit)`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/video-encode-advanced

#### Video Encode Manual

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: This flow element configures FFmpeg to encode the main video stream using manually specified encoding parameters.
- Documented configuration/behavior sections: `Parameters`
- Output branches: The video stream will be encoded using the specified parameters.
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/video-encode-manual

#### Video Encode Optimized

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: Smartly finds the perfect balance between visual quality and file size—so you never waste space or…
- Documented configuration/behavior sections: `Overview`, `Setup`, `General`, `Bitrates`, `Quality`, `Limits`, `Sampling`, `Custom FFmpeg`
- Output branches: Encoded – Encoding quality settings were successfully optimized to preserve…; Skipped – Video already meets quality and size criteria; no…
- Documented literals/examples: `FFmpeg FileFlows Edition`, `FFmpeg`, `FFmpegVMAF`, `/usr/local/bin/ffmpeg`, `/opt/ffmpeg-vmaf/bin/ffmpeg`, `h264`, `hevc`, `av1`, `Automatic`, `90`, `OptimizedValue`, `OptimizedEstimate`, `OptimizedEstimatePerHour`, `Variable`, `Purpose`, `Example Path`, `Encoding`, `VMAF Scoring`, `Codec`, `Field Value`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/video-encode-optimized

#### Video Optimized Manual

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: Automatically finds the ideal balance between visual quality and file size—so you get efficient compression without…
- Documented configuration/behavior sections: `Parameters`
- Documented literals/examples: `{compression}`, `{preset}`, `hevc_videotoolbox -b:v {compression}k -x265-params pass=1`, `Parameter`, `Value`, `Bitrate Result`, `Compression Lower`, `14000`, `Higher Bitrate (Lower Compression)`, `Compression Upper`, `1000`, `Lower Bitrate (Higher Compression)`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/video-encode-optimized-manual

#### Video Scaler

- Shape: `BuildPart`; inputs: `1`; outputs: `2`
- Purpose: This flow element will rescale the video to the desired resolution.
- Documented configuration/behavior sections: `Resolution`
- Documented literals/examples: `Name`, `Field Value`, `480P`, `854:-2`, `720P`, `1280:-2`, `1080P`, `1920:-2`, `1440P`, `2560:-2`, `4K`, `3840:-2`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/video-scaler

#### Video Tag

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: This flow element will add a tag to the video file
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/video-tag

#### Watermark

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: This flow element allows you to apply a watermark to a video file.
- Documented configuration/behavior sections: `Image (PNG recommended)`, `Position`, `Opacity (0-100)`, `Width and Height`
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/watermark

#### x265 Pools

- Shape: `BuildPart`; inputs: `1`; outputs: `1`
- Purpose: Sets the x265 pools parameter for H.265 encoding in the FFMPEG Builder.
- Documented configuration/behavior sections: `Pool Size`, `Use Processor Count`
- Output branches: x265 pools parameter added to FFMPEG Builder
- Source: https://fileflows.com/docs/plugins/video-nodes/ffmpeg-builder/x265-pools

### Category: Hardware Encoders

#### Disable AMD

- Shape: `Logic`; inputs: `1`; outputs: `1`
- Purpose: This sets the variable NoAMD to true, which is used by FFmpeg Builder: Video Encode and…
- Documented literals/examples: `NoAMD`
- Source: https://fileflows.com/docs/plugins/video-nodes/hardware-encoders/disable-amd

#### Disable Intel QSV

- Shape: `Logic`; inputs: `1`; outputs: `1`
- Purpose: This sets the variable NoQSV to true, which is used by FFmpeg Builder: Video Encode and…
- Documented literals/examples: `NoQSV`
- Source: https://fileflows.com/docs/plugins/video-nodes/hardware-encoders/disable-intel-qsv

#### Disable NVIDIA

- Shape: `Logic`; inputs: `1`; outputs: `1`
- Purpose: This sets the variable NoNvidia to true, which is used by FFmpeg Builder: Video Encode and…
- Documented literals/examples: `NoNvidia`
- Source: https://fileflows.com/docs/plugins/video-nodes/hardware-encoders/disable-nvidia

#### Disable VAAPI

- Shape: `Logic`; inputs: `1`; outputs: `1`
- Purpose: This sets the variable NoVAAPI to true, which is used by FFmpeg Builder: Video Encode and…
- Documented literals/examples: `NoVAAPI`
- Source: https://fileflows.com/docs/plugins/video-nodes/hardware-encoders/disable-vaapi

### Category: Logical Nodes

#### Can Use Hardware Encoding

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the specified hardware encoder is currently available to the Flow.
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/can-use-hardware-encoding

#### Size Per Hour

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the file size is within an acceptable limit based on its duration, where the…
- Documented configuration/behavior sections: `Size`
- Output branches: File size is acceptable.; File size is too large.
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/size-per-hour

#### Video Already Processed

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: A flow element that tests if a video file has already been processed, this is done…
- Output branches: Video has already been processed; Video has not been processed
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-already-processed

#### Video Bit Check

- Shape: `Logic`; inputs: `1`; outputs: `4`
- Purpose: Checks if a video if 8-Bit, 10-Bit, 12-Bit or unknown.
- Output branches: Video is 8-Bit; Video is 10-Bit; Video is 12-Bit; Unknown
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-bit-check

#### Video Bitrate Greater Than

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Tests if a videos bitrate is greater than a given bitrate.
- Documented configuration/behavior sections: `Bitrate`
- Output branches: Bitrate is greater than; Bitrate is not greater than
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-bitrate-greater-than

#### Video Codec

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: This is a logic processing node that will check if a video contains a specific codec…
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-codec

#### Video Duration

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Tests whether or not the duration of the video matches the given parameters.
- Documented configuration/behavior sections: `Match`, `Duration`
- Output branches: Video duration matches; Video duration does not match
- Documented literals/examples: `=`, `!=`, `<`, `>=`, `>`, `Between`, `Not Between`, `Name`, `Expression`, `Equals`, `Not Equals`, `Less Than`, `Less Than Or Equal`, `Greater Than`, `Greater Than Or Equal`, ```
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-duration

#### Video Duration Compare

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Compares the original duration of a video with its final duration.
- Documented configuration/behavior sections: `Allowed Difference`
- Output branches: Video is within allowed duration difference; Video is not within the allowed duration difference
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-duration-compare

#### Video Has Audio

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Determines whether a video file contains one or more audio tracks.
- Documented configuration/behavior sections: `Usage Context`, `Parameters`, `Example Use Cases`
- Output branches: Output 1 – Has audio: One or more audio tracks…; Output 2 – Does not have audio: No audio tracks…
- Documented literals/examples: `FFmpeg Builder Start`, `FFmpeg Builder Executor`, `Check FFmpeg Model`
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-has-audio

#### Video Has Codec

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Tests if a video file has a specific codec.
- Documented configuration/behavior sections: `Codec`, `Include Deleted Tracks`
- Output branches: Has the codec; Does not have the codec
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-has-codec

#### Video Has Errors

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Performs a health check on a video file and tests if a video file contains any…
- Output branches: Contains an error; Did not detect any errors
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-has-errors

#### Video Has Stream

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Tests if a video file contains a stream.
- Documented configuration/behavior sections: `Type`, `Title`, `Codec`, `Language`, `Channels`, `Check Deleted`, `Forced`, `Default`, `Invert`
- Output branches: Contains a matching stream; Does not contain a matching stream
- Documented literals/examples: `Type`, `Audio`, `Video Does Not Have Stream`, `Value`, `Description`, `Any`, `Any value is accepted, i.e. this check is skipped`, `Forced`, `This stream must be marked forced`, `Not Forced`, `This sream must not be marked forced`, `Default`, `This stream must be marked default`, `Not Default`, `This sream must not be marked default`
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-has-stream

#### Video Is 10-Bit

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Tests if a video is 10-Bit or not.
- Output branches: Video is 10-Bit; Video is not 10-Bit
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-is-10-bit

#### Video Is 12-Bit

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Tests if a video is 12-Bit or not.
- Output branches: Video is 12-Bit; Video is not 12-Bit
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-is-12-bit

#### Video Is 8-Bit

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Tests if a video is 8-Bit or not.
- Output branches: Video is 8-Bit; Video is not 8-Bit
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-is-8-bit

#### Video Is AV1

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the video file is encoded in AV1 format.
- Output branches: The video is AV1.; The video is not AV1.
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-is-av1

#### Video Is AVI

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the video file is encoded in AVI (Audio Video Interleave) format. AVI is a…
- Output branches: The video is AVI.; The video is not AVI.
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-is-avi

#### Video Is Dolby Vision

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if a video file is Dolby Vision
- Output branches: The video is Dolby Vision.; The video is not Dolby Vision.
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-is-dolby-vision

#### Video Is H.264

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the video file is encoded in H.264 format.
- Output branches: The video is H.264.; The video is not H.264.
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-is-h264

#### Video Is HDR

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if a video file is HDR
- Output branches: The video is HDR.; The video is not HDR.
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-is-hdr

#### Video Is HEVC

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the video file is encoded in HEVC format.
- Output branches: The video is HEVC.; The video is not HEVC.
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-is-hevc

#### Video Is Interlaced

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Tests if a video is interlaced or not.
- Documented configuration/behavior sections: `Threshold`
- Output branches: Video is interlaced; Video is not interlaced
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-is-interlaced

#### Video Is MKV

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the video file is encoded in MKV (Matroska Video) format. MKV is a flexible…
- Output branches: The video is MKV.; The video is not MKV.
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-is-mkv

#### Video Is MOV

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the video file is encoded in MOV (QuickTime Movie) format. MOV is a multimedia…
- Output branches: The video is MOV.; The video is not MOV.
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-is-mov

#### Video Is MP4

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the video file is encoded in MP4 (MPEG-4 Part 14) format. MP4 is one…
- Output branches: The video is MP4.; The video is not MP4.
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-is-mp4

#### Video Is MPEG

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the video file is encoded in MPEG (Moving Picture Experts Group) format. MPEG is…
- Output branches: The video is MPEG.; The video is not MPEG.
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-is-mpeg

#### Video Is MXF

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the video file is encoded in MXF (Material Exchange Format) format. MXF is a…
- Output branches: The video is MXF.; The video is not MXF.
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-is-mxf

#### Video Is TS

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the video file is encoded in TS (Transport Stream) format. TS is a container…
- Output branches: The video is TS.; The video is not TS.
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-is-ts

#### Video Is WEBM

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the video file is encoded in WEBM format. WEBM is an open, royalty-free multimedia…
- Output branches: The video is WEBM.; The video is not WEBM.
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-is-webm

#### Video Is WMV

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if the video file is encoded in WMV (Windows Media Video) format. WMV is a…
- Output branches: The video is WMV.; The video is not WMV.
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-is-wmv

#### Video Resolution

- Shape: `Logic`; inputs: `1`; outputs: `4`
- Purpose: Determines a video's resolution and outputs accordingly.
- Output branches: Video Is 4K; Video is 1080p; Video is 720p; Video is SD
- Source: https://fileflows.com/docs/plugins/video-nodes/logical-nodes/video-resolution
