# FileFlows documented node index

Validated against the current official sitemap. Total documented flow nodes: **242**.
Plugin settings pages and category indexes are excluded because they are not executable flow nodes.

## Reference routing

- [Basic nodes](nodes-basic.md): 65
- [Video and FFmpeg Builder nodes](nodes-video.md): 110
- [Audio, image, book, checksum, metadata, and PDF nodes](nodes-media.md): 49
- [Integration and web nodes](nodes-integrations.md): 18

## Counts by official plugin group

- Apprise: 1
- Audio: 17
- Basic: 65
- Book: 5
- Checksum: 4
- Discord: 1
- Docker: 1
- Email: 1
- Emby: 1
- Gotify: 1
- Image: 12
- Jellyfin: 1
- Meta: 8
- Nextcloud: 1
- PDF: 3
- Plex: 2
- Pushbullet: 1
- Pushover: 1
- Telegram: 1
- Video: 110
- Web: 5

## Maintenance

Run `python3 scripts/update_node_reference.py --check` to detect drift without writing files.
Run `python3 scripts/update_node_reference.py --write` to regenerate the catalog from official documentation.
