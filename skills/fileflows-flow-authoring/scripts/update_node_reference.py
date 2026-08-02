#!/usr/bin/env python3
"""Build and validate the FileFlows documented-node reference.

The script treats a plugin documentation page as a node page only when its
article contains exactly one rendered ``flow-part``.  Category indexes and
plugin settings pages therefore stay out of the catalog automatically.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import html as html_std
import re
import sys
import urllib.request
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlparse

from lxml import html


SITEMAP = "https://fileflows.com/sitemap.xml"
PLUGIN_PREFIX = "https://fileflows.com/docs/plugins/"
USER_AGENT = "FileFlows skill reference updater/1.0"
ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "references"

OUTPUTS = {
    "basic": REFERENCES / "nodes-basic.md",
    "video": REFERENCES / "nodes-video.md",
    "media": REFERENCES / "nodes-media.md",
    "integrations": REFERENCES / "nodes-integrations.md",
}
INDEX = REFERENCES / "nodes-index.md"

GROUP_NAMES = {
    "apprise": "Apprise",
    "audio-nodes": "Audio",
    "basic-nodes": "Basic",
    "book": "Book",
    "checksum-nodes": "Checksum",
    "discord": "Discord",
    "docker": "Docker",
    "email": "Email",
    "emby": "Emby",
    "gotify": "Gotify",
    "image-nodes": "Image",
    "jellyfin": "Jellyfin",
    "meta-nodes": "Meta",
    "nextcloud": "Nextcloud",
    "pdf": "PDF",
    "plex": "Plex",
    "pushbullet": "Pushbullet",
    "pushover": "Pushover",
    "telegram": "Telegram",
    "video-nodes": "Video",
    "web": "Web",
}

MEDIA_GROUPS = {"audio-nodes", "book", "checksum-nodes", "image-nodes", "meta-nodes", "pdf"}
INTEGRATION_GROUPS = {
    "apprise",
    "discord",
    "docker",
    "email",
    "emby",
    "gotify",
    "jellyfin",
    "nextcloud",
    "plex",
    "pushbullet",
    "pushover",
    "telegram",
    "web",
}

SPECIAL_SECTIONS = {
    "outputs",
    "failure output",
    "variables",
    "requirements",
    "notes",
    "examples",
    "example",
}

# This documented node currently lacks the visual flow-part widget used on
# every other node page. Keep the exception explicit so leaf guides (for
# example TV Episode Lookup/episode-renaming) are not misclassified as nodes.
NODE_PAGE_EXCEPTIONS = {
    "https://fileflows.com/docs/plugins/audio-nodes/album-art-embedder",
}


def fetch(url: str) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read()


def compact(value: str) -> str:
    return " ".join(value.split())


def truncate_words(value: str, limit: int) -> str:
    words = compact(value).split()
    if len(words) <= limit:
        return " ".join(words)
    return " ".join(words[:limit]).rstrip(".,;:") + "…"


def sitemap_urls() -> list[str]:
    text = fetch(SITEMAP).decode("utf-8", errors="replace")
    urls = re.findall(r"<loc>(.*?)</loc>", text)
    return sorted(
        html_std.unescape(url)
        for url in urls
        if url.startswith(PLUGIN_PREFIX) and url != PLUGIN_PREFIX and not url.rstrip("/").endswith("/settings")
    )


def node_from_page(url: str, payload: bytes) -> dict[str, object] | None:
    document = html.fromstring(payload)
    articles = document.xpath("//article")
    if not articles:
        return None
    article = articles[0]
    widgets = article.xpath(
        './/div[contains(concat(" ", normalize-space(@class), " "), " flow-part ")]'
    )
    # Most node pages contain one visual flow-part. Keep any missing-widget
    # exception explicit: not every leaf documentation page describes a node.
    if len(widgets) > 1 or (len(widgets) == 0 and url not in NODE_PAGE_EXCEPTIONS):
        return None

    widget = widgets[0] if widgets else None
    headings = article.xpath(".//h1")
    title = compact(headings[0].text_content()) if headings else url.rstrip("/").rsplit("/", 1)[-1]
    names = (
        widget.xpath('.//div[contains(concat(" ", normalize-space(@class), " "), " name ")]')
        if widget is not None
        else []
    )
    display_name = compact(names[0].text_content()) if names else title

    path = urlparse(url).path.strip("/").split("/")
    group = path[2]
    subgroup = path[3] if group in {"basic-nodes", "video-nodes", "meta-nodes"} and len(path) > 4 else ""

    input_numbers = {
        value
        for value in (widget.xpath('.//*[@x-input]/@x-input') if widget is not None else [])
        if str(value).isdigit()
    }
    output_numbers = {
        value
        for value in (widget.xpath('.//*[@x-output]/@x-output') if widget is not None else [])
        if str(value).isdigit()
    }
    widget_classes = (widget.get("class") or "").split() if widget is not None else []
    kind = next((x for x in widget_classes if x not in {"flow-part", "size-1", "size-2", "height-1"}), "FlowPart")

    purpose = ""
    purpose_anchor = widget if widget is not None else headings[0]
    for sibling in purpose_anchor.itersiblings():
        if sibling.tag in {"h2", "hr"}:
            break
        if sibling.tag == "p" and compact(sibling.text_content()):
            purpose = truncate_words(sibling.text_content(), 16)
            break

    section_headings: list[str] = []
    field_headings: list[str] = []
    variables: list[str] = []
    outputs: list[str] = []
    failure: list[str] = []
    literals: list[str] = []

    for heading in article.xpath(".//h2"):
        name = compact("".join(heading.itertext()).replace("​", ""))
        if not name:
            continue
        section_headings.append(name)
        lowered = name.casefold()
        if lowered not in SPECIAL_SECTIONS:
            field_headings.append(name)

        section_nodes = []
        for sibling in heading.itersiblings():
            if sibling.tag == "h2":
                break
            section_nodes.append(sibling)

        if lowered == "outputs":
            for item in section_nodes:
                outputs.extend(compact(x.text_content()) for x in item.xpath(".//li") if compact(x.text_content()))
        elif lowered == "failure output":
            for item in section_nodes:
                failure.extend(compact(x.text_content()) for x in item.xpath(".//li") if compact(x.text_content()))
            if not failure:
                text = compact(" ".join(x.text_content() for x in section_nodes))
                if text:
                    failure.append(truncate_words(text, 12))
        elif lowered == "variables":
            for item in section_nodes:
                variables.extend(compact(x.text_content()) for x in item.xpath(".//li") if compact(x.text_content()))

    # Literal values and table cells are useful authoring facts and are much
    # less error-prone than copied prose.  Keep the list deliberately bounded.
    for code in article.xpath(".//article//code | .//code"):
        value = compact(code.text_content())
        if value and len(value) <= 80 and "\n" not in value and value not in literals:
            literals.append(value)
    for cell in article.xpath(".//table//th | .//table//td"):
        value = compact(cell.text_content())
        if value and len(value) <= 80 and value not in literals:
            literals.append(value)

    return {
        "url": url,
        "group": group,
        "subgroup": subgroup,
        "title": title,
        "display_name": display_name,
        "kind": kind,
        "inputs": len(input_numbers),
        "outputs_count": len(output_numbers),
        "purpose": purpose,
        "fields": field_headings,
        "sections": section_headings,
        "variables": variables,
        "outputs": outputs,
        "failure": failure,
        "literals": literals[:20],
    }


def discover() -> list[dict[str, object]]:
    urls = sitemap_urls()
    nodes: list[dict[str, object]] = []
    errors: list[str] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        jobs = {executor.submit(fetch, url): url for url in urls}
        for job in concurrent.futures.as_completed(jobs):
            url = jobs[job]
            try:
                node = node_from_page(url, job.result())
                if node:
                    nodes.append(node)
            except Exception as error:  # noqa: BLE001 - report every failed source
                errors.append(f"{url}: {error}")
    if errors:
        raise RuntimeError("Could not inspect official documentation:\n" + "\n".join(sorted(errors)))
    return sorted(
        nodes,
        key=lambda x: (
            str(x["group"]),
            str(x["subgroup"]),
            str(x["title"]).casefold(),
            str(x["url"]),
        ),
    )


def bucket_for(group: str) -> str:
    if group == "basic-nodes":
        return "basic"
    if group == "video-nodes":
        return "video"
    if group in MEDIA_GROUPS:
        return "media"
    if group in INTEGRATION_GROUPS:
        return "integrations"
    raise ValueError(f"Unclassified plugin group: {group}")


def render_node(node: dict[str, object]) -> list[str]:
    lines = [f"### {node['title']}", ""]
    lines.append(
        f"- Shape: `{node['kind']}`; inputs: `{node['inputs']}`; outputs: `{node['outputs_count']}`"
    )
    if node["purpose"]:
        lines.append(f"- Purpose: {node['purpose']}")
    if node["fields"]:
        lines.append("- Documented configuration/behavior sections: " + ", ".join(f"`{x}`" for x in node["fields"]))
    if node["variables"]:
        lines.append("- Variables: " + "; ".join(truncate_words(str(x), 12) for x in node["variables"]))
    if node["outputs"]:
        lines.append("- Output branches: " + "; ".join(truncate_words(str(x), 10) for x in node["outputs"]))
    if node["failure"]:
        lines.append("- Failure branch: " + "; ".join(truncate_words(str(x), 10) for x in node["failure"]))
    if node["literals"]:
        lines.append("- Documented literals/examples: " + ", ".join(f"`{x}`" for x in node["literals"]))
    lines.append(f"- Source: {node['url']}")
    lines.append("")
    return lines


def render_reference(bucket: str, nodes: list[dict[str, object]]) -> str:
    titles = {
        "basic": "FileFlows Basic nodes",
        "video": "FileFlows Video nodes",
        "media": "FileFlows media and metadata nodes",
        "integrations": "FileFlows integration nodes",
    }
    lines = [
        f"# {titles[bucket]}",
        "",
        "Generated from the current official FileFlows plugin documentation sitemap.",
        "This is a discovery and authoring index, not a serialization schema. Use a target-version flow export for `FlowElementUid`, model field names, defaults, and JSON shape.",
        "Field and branch labels are retained for exact lookup; prose is deliberately condensed. Open the linked source before relying on version-sensitive behavior.",
        "",
    ]
    by_group: dict[str, list[dict[str, object]]] = defaultdict(list)
    for node in nodes:
        by_group[str(node["group"])].append(node)
    for group in sorted(by_group, key=lambda x: GROUP_NAMES[x].casefold()):
        group_nodes = by_group[group]
        lines.extend([f"## {GROUP_NAMES[group]} ({len(group_nodes)})", ""])
        by_subgroup: dict[str, list[dict[str, object]]] = defaultdict(list)
        for node in group_nodes:
            by_subgroup[str(node["subgroup"])].append(node)
        for subgroup in sorted(by_subgroup):
            subgroup_nodes = by_subgroup[subgroup]
            if subgroup:
                lines.extend([f"### Category: {subgroup.replace('-', ' ').title()}", ""])
                # One extra heading level keeps node names distinct inside nested categories.
                for node in subgroup_nodes:
                    card = render_node(node)
                    card[0] = "####" + card[0][3:]
                    lines.extend(card)
            else:
                for node in subgroup_nodes:
                    lines.extend(render_node(node))
    return "\n".join(lines).rstrip() + "\n"


def render_index(nodes: list[dict[str, object]]) -> str:
    by_group: dict[str, int] = defaultdict(int)
    by_bucket: dict[str, int] = defaultdict(int)
    for node in nodes:
        group = str(node["group"])
        by_group[group] += 1
        by_bucket[bucket_for(group)] += 1
    lines = [
        "# FileFlows documented node index",
        "",
        f"Validated against the current official sitemap. Total documented flow nodes: **{len(nodes)}**.",
        "Plugin settings pages and category indexes are excluded because they are not executable flow nodes.",
        "",
        "## Reference routing",
        "",
        f"- [Basic nodes](nodes-basic.md): {by_bucket['basic']}",
        f"- [Video and FFmpeg Builder nodes](nodes-video.md): {by_bucket['video']}",
        f"- [Audio, image, book, checksum, metadata, and PDF nodes](nodes-media.md): {by_bucket['media']}",
        f"- [Integration and web nodes](nodes-integrations.md): {by_bucket['integrations']}",
        "",
        "## Counts by official plugin group",
        "",
    ]
    for group in sorted(by_group, key=lambda x: GROUP_NAMES[x].casefold()):
        lines.append(f"- {GROUP_NAMES[group]}: {by_group[group]}")
    lines.extend(
        [
            "",
            "## Maintenance",
            "",
            "Run `python3 scripts/update_node_reference.py --check` to detect drift without writing files.",
            "Run `python3 scripts/update_node_reference.py --write` to regenerate the catalog from official documentation.",
        ]
    )
    return "\n".join(lines).rstrip() + "\n"


def expected_files(nodes: list[dict[str, object]]) -> dict[Path, str]:
    buckets: dict[str, list[dict[str, object]]] = defaultdict(list)
    for node in nodes:
        buckets[bucket_for(str(node["group"]))].append(node)
    files = {INDEX: render_index(nodes)}
    for bucket, path in OUTPUTS.items():
        files[path] = render_reference(bucket, buckets[bucket])
    return files


def check(files: dict[Path, str]) -> int:
    stale = []
    for path, expected in files.items():
        if not path.exists():
            stale.append(f"missing: {path.relative_to(ROOT)}")
        elif path.read_text(encoding="utf-8") != expected:
            stale.append(f"stale: {path.relative_to(ROOT)}")
    if stale:
        print("Node reference check failed:", file=sys.stderr)
        for item in stale:
            print(f"- {item}", file=sys.stderr)
        return 1
    print(f"Node reference is current: {len(files)} files")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--write", action="store_true")
    args = parser.parse_args()

    nodes = discover()
    if not nodes:
        raise RuntimeError("No documented flow nodes discovered")
    files = expected_files(nodes)
    if args.check:
        return check(files)
    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Wrote {len(files)} reference files for {len(nodes)} documented flow nodes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
