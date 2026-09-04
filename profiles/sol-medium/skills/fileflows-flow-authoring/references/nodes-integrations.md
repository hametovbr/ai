# FileFlows integration nodes

Generated from the current official FileFlows plugin documentation sitemap.
This is a discovery and authoring index, not a serialization schema. Use a target-version flow export for `FlowElementUid`, model field names, defaults, and JSON shape.
Field and branch labels are retained for exact lookup; prose is deliberately condensed. Open the linked source before relying on version-sensitive behavior.

## Apprise (1)

### Apprise

- Shape: `Communication`; inputs: `1`; outputs: `2`
- Purpose: Sends a message to a Apprise server.
- Documented configuration/behavior sections: `Tag`, `Type`, `Message`
- Output branches: Apprise message sent; Apprise message failed to send
- Source: https://fileflows.com/docs/plugins/apprise/

## Discord (1)

### Discord

- Shape: `Communication`; inputs: `1`; outputs: `2`
- Purpose: Sends a message to a Discord server.
- Source: https://fileflows.com/docs/plugins/discord/

## Docker (1)

### Docker Execute

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Launches a Docker container from an image and executes a specified command inside it.
- Documented configuration/behavior sections: `Image`, `Volumes`, `Additional Outputs`, `Command`
- Output branches: Exit Code was zero/successful; Matched additional output 1 etc
- Documented literals/examples: `/temp`
- Source: https://fileflows.com/docs/plugins/docker/docker-execute

## Email (1)

### Email

- Shape: `Communication`; inputs: `1`; outputs: `2`
- Purpose: Sends an email using the configured SMTP Server.
- Documented configuration/behavior sections: `Recipients`, `Subject`, `Body`
- Output branches: Email was sent; Email failed to send
- Source: https://fileflows.com/docs/plugins/email/

## Emby (1)

### Emby

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Sends a request to your Emby server to update its library.
- Documented configuration/behavior sections: `Server`, `Access Token`, `Mapping`
- Source: https://fileflows.com/docs/plugins/emby/

## Gotify (1)

### Gotify

- Shape: `Communication`; inputs: `1`; outputs: `2`
- Purpose: Sends a message to a Gotify server.
- Documented configuration/behavior sections: `Title`, `Priority`, `Message`
- Output branches: Message sent; Message failed to send
- Source: https://fileflows.com/docs/plugins/gotify/

## Jellyfin (1)

### Jellyfin

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Sends a request to your Jellyfin server to update its library.
- Documented configuration/behavior sections: `Server`, `Access Token`, `Mapping`
- Source: https://fileflows.com/docs/plugins/jellyfin/

## Nextcloud (1)

### Upload to Nextcloud

- Shape: `Process`; inputs: `1`; outputs: `1`
- Purpose: Uploads a file to Nextcloud
- Documented configuration/behavior sections: `File`, `Destination`
- Output branches: Was successfully uploaded to Nextcloud; Failed ot upload to Nextcloud
- Source: https://fileflows.com/docs/plugins/nextcloud/upload-to-nextcloud

## Plex (2)

### Plex Analyze

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Sends a message to a Plex server to analyze the working file.
- Documented configuration/behavior sections: `Server`, `Access Token`, `Priority`
- Output branches: Plex analyze request sent; Plex analyze request failed to send
- Source: https://fileflows.com/docs/plugins/plex/plex-analyze

### Plex Updater

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Sends a message to a Plex server to update the library.
- Documented configuration/behavior sections: `Server`, `Access Token`, `Priority`
- Output branches: Plex update request sent; Plex update request failed to send
- Source: https://fileflows.com/docs/plugins/plex/plex-updater

## Pushbullet (1)

### Pushbullet

- Shape: `Communication`; inputs: `1`; outputs: `2`
- Purpose: Sends a message via Pushbullet.
- Documented configuration/behavior sections: `Title`, `Message`
- Output branches: Message sent; Message failed to send
- Source: https://fileflows.com/docs/plugins/pushbullet/

## Pushover (1)

### Pushover

- Shape: `Communication`; inputs: `1`; outputs: `2`
- Purpose: Sends a message via Pushover.
- Documented configuration/behavior sections: `Priority`, `Message`, `Emergency Messages`
- Output branches: Message sent; Message failed to send
- Documented literals/examples: `Retry`, `Expire`, `Priority`, `Description`, `Lowest`, `Quiet notification, no sound or vibration`, `Normal`, `Normal priority`, `High`, `Generate sound and vibration`, `Emergency`, `Rrepeated sound and vibration, requires retry and expire parameters`
- Source: https://fileflows.com/docs/plugins/pushover/

## Telegram (1)

### Telegram

- Shape: `Communication`; inputs: `1`; outputs: `2`
- Purpose: Sends a Telegram messager.
- Documented configuration/behavior sections: `Message`
- Output branches: Message sent; Message failed to send
- Source: https://fileflows.com/docs/plugins/telegram/

## Web (5)

### Downloader

- Shape: `Communication`; inputs: `1`; outputs: `2`
- Purpose: Writes text to a file.
- Documented configuration/behavior sections: `URL`
- Output branches: URL was successfully downloaded; URL failed to download
- Documented literals/examples: `WorkingFile`
- Source: https://fileflows.com/docs/plugins/web/downloader

### HTML Image Parser

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Parses HTML text for images and creates a list of images found.
- Documented configuration/behavior sections: `File`, `Pattern`
- Output branches: Images were found and variables updated; No images found, variables left unmodified
- Documented literals/examples: `.jpg`, `ImageUrls`, `CurrentList`
- Source: https://fileflows.com/docs/plugins/web/html-image-parser

### HTML Link Parser

- Shape: `Process`; inputs: `1`; outputs: `2`
- Purpose: Parses HTML text for links creates a list of links found.
- Documented configuration/behavior sections: `File`, `Pattern`
- Output branches: Links were found and variables updated; No links found, variables left unmodified
- Documented literals/examples: `.jpg`, `Links`, `CurrentList`
- Source: https://fileflows.com/docs/plugins/web/html-link-parser

### Input URL

- Shape: `Input`; inputs: `0`; outputs: `1`
- Purpose: An input flow element for a URL. This is required and is the starting point of…
- Documented configuration/behavior sections: `Download`
- Documented literals/examples: `Url`
- Source: https://fileflows.com/docs/plugins/web/input-url

### Web Request

- Shape: `Communication`; inputs: `1`; outputs: `2`
- Purpose: Copies a file to the destination folder
- Variables: Set the content type to "JSON"; Choose the HTTP method, for example "POST"; Set the body
- Output branches: Successfully sent; Request returned a non-successful status code
- Documented literals/examples: `{file.Name}`, `Variable`, `Description`, `Type`, `Example`, `web.StatusCode`, `The status code from the response`, `number`, `200`, `web.Body`, `The body of the response`, `string`, `this is a sample body`
- Source: https://fileflows.com/docs/plugins/web/web-request
