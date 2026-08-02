# FileFlows media and metadata nodes

Generated from the current official FileFlows plugin documentation sitemap.
This is a discovery and authoring index, not a serialization schema. Use a target-version flow export for `FlowElementUid`, model field names, defaults, and JSON shape.
Field and branch labels are retained for exact lookup; prose is deliberately condensed. Open the linked source before relying on version-sensitive behavior.

## Audio (17)

### Album Art Embedder

- Shape: `FlowPart`; inputs: `0`; outputs: `0`
- Documented configuration/behavior sections: `How it Works`, `Configuration`
- Output branches: Embedded: Artwork was found and successfully written into the audio…; Not Embedded: No artwork was added. This happens if no…
- Documented literals/examples: `cover.jpg`, `folder.jpg`, `albumart.jpg`, `front.jpg`, `{audio.AlbumArtist}`, `{audio.Album}`, `/MyMusic/Covers/{audio.Artist}/`, `folder`, `front`, `cover`, `.jpg`, `.jpeg`, `.jpe`
- Source: https://fileflows.com/docs/plugins/audio-nodes/album-art-embedder

### Audio Bitrate Matches

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Check if an audio bitrate matches the constraints.
- Documented configuration/behavior sections: `Kilobytes`, `Match`
- Output branches: Does match; Does not match
- Documented literals/examples: `=`, `!=`, `<`, `>=`, `>`, `Name`, `Expression`, `Equals`, `Not Equals`, `Less Than`, `Less Than Or Equal`, `Greater Than`, `Greater Than Or Equal`
- Source: https://fileflows.com/docs/plugins/audio-nodes/audio-bitrate-matches

### Audio Duration Compare

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Compares the original duration of a audio file with its final duration.
- Documented configuration/behavior sections: `Allowed Difference`
- Output branches: Audio file is within allowed duration difference; Audio file is not within the allowed duration difference
- Source: https://fileflows.com/docs/plugins/audio-nodes/audio-duration-compare

### Audio File

- Shape: `Input`; inputs: `0`; outputs: `1`
- Purpose: Audio File is an input node which will scan a file and load the Audio Information…
- Documented literals/examples: `Variable`, `Description`, `Type`, `Example`, `AudioInfo`, `AudioInfo object`, `object`, `See Below`, `audio.Album`, `The album for the file`, `string`, `The Album`, `audio.Artist`, `The artist for the file`, `The Artist`, `audio.Bitrate`, `The bitrate in bytes per second (bps)`, `number`, `192000`, `audio.Channels`
- Source: https://fileflows.com/docs/plugins/audio-nodes/audio-file

### Audio File Normalization

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Normalizes an audio file using two passes of FFmpeg's loudnorm filter, implementing EBU R128 loudness normalization…
- Documented configuration/behavior sections: `How It Works`, `Target Integrated Loudness`, `Target Loudness Range`, `Maximum True Peak`, `Practical Tips`
- Output branches: Audio file normalized and saved to a temporary file. This…
- Documented literals/examples: `loudnorm`, `input_i`, `input_lra`, `input_tp`, `input_thresh`, `print_format=json`, `TargetLoudness`, `LoudnessRange`, `TruePeak`
- Source: https://fileflows.com/docs/plugins/audio-nodes/audio-file-normalization

### Audio Is Codec

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks whether an audio file uses a specific codec.
- Documented configuration/behavior sections: `Codec`
- Output branches: Audio file matches the specified codec.; Audio file does not match the specified codec.
- Source: https://fileflows.com/docs/plugins/audio-nodes/audio-is-codec

### Audio Tagger

- Shape: `Input`; inputs: `0`; outputs: `1`
- Purpose: Writes metadata tags to the working audio file.
- Documented configuration/behavior sections: `Title`, `Album`, `Album Artist`, `Artist`, `Genres`, `Track`, `Disc`, `Cover Art`
- Output branches: Audio tags written to file.; No audio tags were written.
- Source: https://fileflows.com/docs/plugins/audio-nodes/audio-tagger

### Convert Audio

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Convert an Audio file to the specified audio codec
- Documented configuration/behavior sections: `Codec`, `Bitrate`, `Sample Rate`, `Bit-Depth`, `Channels`, `Extension`, `Normalize`, `Skip If Codec Matches`, `AAC Codec`
- Output branches: Audio converted and saved to temporary file; Audio already in codec, no conversion done
- Documented literals/examples: `Automatic`, `Same as source`, `AAC_Codec`, `libfdk_aac`, `aac`
- Source: https://fileflows.com/docs/plugins/audio-nodes/convert-audio

### Convert to AAC

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Convert a Audio file to AAC
- Documented configuration/behavior sections: `Sample Rate`, `Channels`, `Extension`, `AAC Codec`
- Documented literals/examples: `AAC_Codec`, `libfdk_aac`, `aac`
- Source: https://fileflows.com/docs/plugins/audio-nodes/convert-to-aac

### Convert to ALAC

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Convert a Audio file to ALAC
- Documented configuration/behavior sections: `Sample Rate`, `Channels`, `Extension`
- Source: https://fileflows.com/docs/plugins/audio-nodes/convert-to-alac

### Convert to FLAC

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Convert a Audio file to FLAC
- Documented configuration/behavior sections: `Sample Rate`, `Bit-Depth`, `Channels`, `Extension`
- Source: https://fileflows.com/docs/plugins/audio-nodes/convert-to-flac

### Convert to MP3

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Convert a Audio file to MP3
- Documented configuration/behavior sections: `Sample Rate`, `Channels`, `Extension`
- Source: https://fileflows.com/docs/plugins/audio-nodes/convert-to-mp3

### Convert to OGG

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Convert a Audio file to OGG
- Documented configuration/behavior sections: `Sample Rate`, `Channels`, `Extension`
- Source: https://fileflows.com/docs/plugins/audio-nodes/convert-to-ogg

### Convert to WAV

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Convert a Audio file to WAV
- Documented configuration/behavior sections: `Sample Rate`, `Bit-Depth`, `Channels`, `Extension`
- Source: https://fileflows.com/docs/plugins/audio-nodes/convert-to-wav

### Create Audio Book

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Creates a audio book from audio files found in input directory
- Documented configuration/behavior sections: `Metadata`, `Destination Path`, `Delete Source Files`, `Update Working File`
- Source: https://fileflows.com/docs/plugins/audio-nodes/create-audio-book

### Embed Artwork

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Embeds artwork into an audio file.
- Documented configuration/behavior sections: `Supported containers`, `Supported Artwork Files`, `Supported Image Extensions`
- Documented literals/examples: `mysong.mp3`, `mysong.jpg`
- Source: https://fileflows.com/docs/plugins/audio-nodes/embed-artwork

### Tag Normalizer

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: This flow element is designed to normalize the metadata tags within an audio file. When run…
- Documented configuration/behavior sections: `Use Common`, `Use Library File`, `Tags To Keep`
- Output branches: The audio file was successfully updated, and its tags have…; The audio file was not modified.
- Documented literals/examples: `Tag`, `Description`, `Title`, `The name of the track.`, `Artist`, `The primary performing artist(s).`, `Album`, `The name of the album the track belongs to.`, `Album Artist`, `The main artist(s) for the entire album.`, `Cover Art`, `The embedded image metadata.`, `Track`, `The track number (e.g., 1/12).`, `Genres`, `The style or category of music.`, `Year`, `The year the track/album was released.`, `Disc`, `The disc number (e.g., 1/2).`
- Source: https://fileflows.com/docs/plugins/audio-nodes/tag-normalizer

## Book (5)

### Book

- Shape: `Input`; inputs: `0`; outputs: `1`
- Purpose: Input flow element for processing book files.
- Source: https://fileflows.com/docs/plugins/book/book-input

### Comic Converter

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Converts a comic to a different comic book format.
- Documented configuration/behavior sections: `Format`, `Ensure Top Directory`, `Delete Non Page Images`, `Codec`, `Quality`, `Max Width`, `Max Height`
- Output branches: Comic was converted and saved as temporary file; Comic was already in desired format
- Documented literals/examples: `CBZ`, `PDF`
- Source: https://fileflows.com/docs/plugins/book/comic-converter

### Comic Extractor

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Extracts all files from a comic book format and saves them to them to a specific…
- Source: https://fileflows.com/docs/plugins/book/comic-extractor

### Create Comic Info

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Parses the path of a comic and create a comicinfo.xml file inside the comic book archive.
- Documented configuration/behavior sections: `File Format`, `Volume`, `Publisher`, `Rename File`
- Output branches: ComicInfo added to comic archive; ComicInfo already in archive
- Documented literals/examples: `comicinfo.xml`, `-`, `1984`, `#num`, `Volume [Num]`, `v[Num]`, `Vol[Num]`, `DC`, `Batman (1939)`, `1939`, `1`, `Batman vs. Joker`, `He-Man and the Masters of the Universe (2013)`, `2013`, `Desperate Times`, `Marvel`, `Ultimate Spider-Man (2000)`, `Volume 5`, `Public Scrunity`, `/media/comics`
- Source: https://fileflows.com/docs/plugins/book/create-comic-info

### eBook Converter

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Converts an eBook to a different eBook format.
- Documented configuration/behavior sections: `Format`
- Output branches: eBook was converted and saved as temporary file; eBook was already in desired format
- Documented literals/examples: `Calibre`
- Source: https://fileflows.com/docs/plugins/book/ebook-converter

## Checksum (4)

### MD5

- Shape: `Logic`; inputs: `1`; outputs: `1`
- Purpose: Computes a MD5 checksum of the working file and stores it in the variable MD5 and…
- Documented literals/examples: `MD5`, `Checksum`
- Source: https://fileflows.com/docs/plugins/checksum-nodes/md5

### SHA1

- Shape: `Logic`; inputs: `1`; outputs: `1`
- Purpose: Computes a SHA1 checksum of the working file and stores it in the variable SHA1 and…
- Documented literals/examples: `SHA1`, `Checksum`
- Source: https://fileflows.com/docs/plugins/checksum-nodes/sha1

### SHA256

- Shape: `Logic`; inputs: `1`; outputs: `1`
- Purpose: Computes a SHA256 checksum of the working file and stores it in the variable SHA256 and…
- Documented literals/examples: `SHA256`, `Checksum`
- Source: https://fileflows.com/docs/plugins/checksum-nodes/sha256

### SHA512

- Shape: `Logic`; inputs: `1`; outputs: `1`
- Purpose: Computes a SHA512 checksum of the working file and stores it in the variable SHA512 and…
- Documented literals/examples: `SHA512`, `Checksum`
- Source: https://fileflows.com/docs/plugins/checksum-nodes/sha512

## Image (12)

### Auto Crop Image

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Automatically crops an image of any white/black borders.
- Documented configuration/behavior sections: `Threshold`, `Format`, `Quality`
- Output branches: Image cropped, saved to new temporary file; Image was not cropped
- Documented literals/examples: `JPG`, `WEBP`, `100`
- Source: https://fileflows.com/docs/plugins/image-nodes/auto-crop-image

### Image Convert

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Converts an image to the selected format and saves it to a new temporary file.
- Documented configuration/behavior sections: `Format`, `Quality`
- Output branches: Image resized and saved to new temporary file
- Documented literals/examples: `JPG`, `WEBP`, `100`
- Source: https://fileflows.com/docs/plugins/image-nodes/image-convert

### Image File

- Shape: `Input`; inputs: `0`; outputs: `1`
- Purpose: Image File is an input node which will scan a file and load the Image Information…
- Documented configuration/behavior sections: `Move Files Based On Dates`
- Documented literals/examples: `2020-04-23 12:00:23`, `D:\Pictures\Family Photos`, `D:\Pictures\Family Photos\{img.DateTaken.Year}\{img.DateTaken.Month}`, `DateTaken`, `return Variables.img?.DateTaken ? 1 : -1;`, `2`, `return Variables.img?.DateTaken ? 1 : 2;`, `Variable`, `Description`, `Type`, `Example`, `img.Width`, `Image width`, `number`, `1920`, `img.Height`, `Image height`, `1080`, `img.Format`, `Image format`
- Source: https://fileflows.com/docs/plugins/image-nodes/image-file

### Image Flip

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Flips an image and saves it to a new temporary file
- Documented configuration/behavior sections: `Vertical`, `Format`, `Quality`
- Output branches: Image resized and saved to new temporary file
- Documented literals/examples: `JPG`, `WEBP`, `100`
- Source: https://fileflows.com/docs/plugins/image-nodes/image-flip

### Image Is Landscape

- Shape: `Logic`; inputs: `1`; outputs: `1`
- Purpose: Tests if a image is landscape
- Output branches: Image is landscape; Image is not landscape
- Source: https://fileflows.com/docs/plugins/image-nodes/image-is-landscape

### Image Is Portrait

- Shape: `Logic`; inputs: `1`; outputs: `1`
- Purpose: Tests if a image is portrait
- Output branches: Image is portrait; Image is not portrait
- Source: https://fileflows.com/docs/plugins/image-nodes/image-is-portrait

### Image Resizer

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Resizes an image and creates a new temporary file.
- Documented configuration/behavior sections: `Mode`, `Width`, `Height`, `Format`, `Quality`
- Output branches: Image resized and saved to new temporary file
- Documented literals/examples: `JPG`, `WEBP`, `100`
- Source: https://fileflows.com/docs/plugins/image-nodes/image-resizer

### Image Rotate

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Rotates an image and creates a new temporary file.
- Documented configuration/behavior sections: `Angle`, `Format`, `Quality`
- Output branches: Image resized and saved to new temporary file
- Documented literals/examples: `JPG`, `WEBP`, `100`
- Source: https://fileflows.com/docs/plugins/image-nodes/image-rotate

### Image To Video

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Converts an image into a video file
- Documented configuration/behavior sections: `Codec`, `Container`
- Output branches: Image converted to video and saved as a new temporary…
- Source: https://fileflows.com/docs/plugins/image-nodes/image-to-video

### Is Image

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Tests if a file is an image file
- Documented configuration/behavior sections: `File`
- Output branches: File is a recognized image file; File is not a recognized image file
- Source: https://fileflows.com/docs/plugins/image-nodes/is-image

### Pixel Check

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: This flow element verifies if an image's total pixel count exceeds the specified threshold.
- Documented configuration/behavior sections: `Pixels`
- Output branches: Image has greater or equal to the number of pixels…; Image has fewer pixels than the required pixels specified
- Source: https://fileflows.com/docs/plugins/image-nodes/pixel-check

### Set Photo Date

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: The Set Photo Date flow element allows you to set the date a photo was taken…
- Documented configuration/behavior sections: `Fields`
- Output branches: Photo date successfully updated
- Documented literals/examples: `yyyy-MM-dd HH:mm:ss`, `{MyDateVariable}`, `brew install exiftool`, `apt install libimage-exiftool-perl`, `dnf install exiftool`
- Source: https://fileflows.com/docs/plugins/image-nodes/set-photo-date

## Meta (8)

### Anime Show Lookup

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Looks performs a search on AniList.co for a Anime TV Show
- Documented configuration/behavior sections: `Use Folder Name`
- Output branches: Anime Show found; Anime Show NOT found
- Documented literals/examples: `VideoMetadata`, `string`, `Attack on Titan`, `Shingeki no Kyojin`, `進撃の巨人`, `2016`, `Several hundred years ago, humans were nearly exterminated by titans.`, `84`, `Season`, `Staffel`, `Saison`, `Specials`, `Variable`, `Description`, `Type`, `Example`, `tvshow.Title`, `The title in English`, `tvshow.TitleRomaji`, `The title in Romaji`
- Source: https://fileflows.com/docs/plugins/meta-nodes/antime-show-lookup

### Genre Matches

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Matches the genre metadata against the specified genre(s).
- Documented configuration/behavior sections: `Genres`, `Match All`
- Output branches: Genre match; Genre does not match
- Source: https://fileflows.com/docs/plugins/meta-nodes/genre-matches

### Movie Keyword Matches

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks whether any keyword from the retrieved movie information matches one of the specified keywords.
- Documented configuration/behavior sections: `Keywords`
- Output branches: Keyword match found – At least one keyword matches the…; No keyword match found – None of the keywords matched.
- Source: https://fileflows.com/docs/plugins/meta-nodes/movie-keyword-matches

### Movie Lookup

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Performs a movie metadata lookup using TheMovieDB.org.
- Documented configuration/behavior sections: `Use Folder Name`, `Use Spoken Language`, `Language`, `MovieInfo`, `Example Function`
- Output branches: Movie found; Movie not found
- Documented literals/examples: `VideoMetadata`, `/Movies/Inception (2010)/movie.mkv`, `original language`, `en`, `fr`, `de`, `Batman Begins`, `2005`, `tt0372784`, `Variable`, `Description`, `Type`, `Example`, `movie.Title`, `The movie title`, `string`, `movie.Year`, `The movie year`, `number`, `movie.ImdbId`
- Source: https://fileflows.com/docs/plugins/meta-nodes/movie-lookup

### Music Meta

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Loads the metadata of a music file into the flow variables.
- Documented literals/examples: `Variable`, `Description`, `Type`, `Example`, `music.Artist`, `The artist`, `string`, `A Fine Frenzy`, `music.Album`, `The album`, `Pines`, `music.Year`, `The year the song was released`, `number`, `2012`, `music.Track.Number`, `The track number`, `6`, `music.Track.Name`, `The track name`
- Source: https://fileflows.com/docs/plugins/meta-nodes/music-meta

### NFO File Creator

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Creates a NFO file from the previously looked up Movie Lookup or TV Episode Lookup.
- Documented configuration/behavior sections: `Desitination Path`, `Destination File`
- Output branches: NFO File created; NFO failed to be created
- Source: https://fileflows.com/docs/plugins/meta-nodes/nfo-file-creator

### TV Episode Lookup

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Performs a search on TheMovieDB.org for a TV Episode
- Documented configuration/behavior sections: `Use Folder Name`, `Language`, `Use Folder Name`
- Output branches: TV Show found; TV Show not found
- Documented literals/examples: `Season`, `Staffel`, `Saison`, `Specials`, `Batman`, `Variable`, `Description`, `Type`, `Example`, `tvepisode.Title`, `The TV show title`, `string`, `The Batman`, `tvepisode.Subtitle`, `The name of the episode`, `The Man Who Laughs`, `tvepisode.Year`, `The year the episode aired`, `number`, `2004`
- Source: https://fileflows.com/docs/plugins/meta-nodes/tv-episode-lookup/

### TV Show Lookup

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Performs a search on TheMovieDB.org for a TV Show
- Documented configuration/behavior sections: `Use Folder Name`, `Language`, `Use Folder Name`, `VideoMetadata`, `Example Function`
- Output branches: TV Show found; TV Show not found
- Documented literals/examples: `VideoMetadata`, `Season`, `Staffel`, `Saison`, `Specials`, `Batman`, `Variable`, `Description`, `Type`, `Example`, `tvshow.Title`, `The TV show title`, `string`, `The Batman`, `tvshow.Year`, `The original year the show aired`, `number`, `2004`, `Object containing video metadata`, `object`
- Source: https://fileflows.com/docs/plugins/meta-nodes/tv-show-lookup

## PDF (3)

### PDF Contains Text

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Checks if a PDF contains the specified text.
- Documented configuration/behavior sections: `Text`
- Output branches: PDF contains the specified text.; PDF does not contain the specified text.
- Source: https://fileflows.com/docs/plugins/pdf/pdf-contains-text

### PDF Matches Text

- Shape: `Logic`; inputs: `1`; outputs: `2`
- Purpose: Tests if a PDF matches the specified text using String Operations.
- Documented configuration/behavior sections: `Text`
- Output branches: PDF matches the specified text.; PDF does not match the specified text.
- Source: https://fileflows.com/docs/plugins/pdf/pdf-matches-text

### PDF To Text File

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Extracts the contents of the PDF file to a text file and updates the working file…
- Documented configuration/behavior sections: `Text`
- Output branches: PDF successfully saved to text file.; No text content found to extract.
- Source: https://fileflows.com/docs/plugins/pdf/pdf-to-text-file
