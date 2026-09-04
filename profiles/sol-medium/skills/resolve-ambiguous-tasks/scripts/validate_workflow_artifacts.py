#!/usr/bin/env python3
"""Validate deterministic structural invariants in workflow artifacts.

Review applicability and authorization are judgment gates defined by the skill and
references; this validator intentionally does not infer or require them.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path


SUPPORTED_SUFFIXES = {".md", ".txt"}
DEFINITION = re.compile(r"^\s*-\s*\[([A-Z][A-Z0-9]*-\d{3})\](?:\s|$)")
REFERENCE = re.compile(r"\(([A-Z][A-Z0-9]*-\d{3})\)")
ID_RANGE = re.compile(
    r"\([A-Z][A-Z0-9]*-\d{3}\s*(?:-|–|—|\.\.)\s*[A-Z][A-Z0-9]*-\d{3}\)"
)
PLACEHOLDER = re.compile(
    r"\b(?:TODO|TBD|FIXME)\b|\?\?\?|\{(?:requested output|completion proposition|"
    r"bounded scope|explicit exclusions|limits|compatibility, risk, time, format|value|"
    r"locator|fact|statement|gap|bounded step|constraint|role|choice|preference/authority needed|"
    r"observable outcome|excluded outcomes|boundaries and owners|testable behavior|observable pass/fail|"
    r"compatibility, security, privacy, performance|errors, partial success, retries, recovery|"
    r"signals and success thresholds|boundary, abort conditions, reversibility|named action|owner/date)\}",
    re.IGNORECASE,
)
READY = re.compile(r"^\s*Readiness:\s*READY\s*$", re.IGNORECASE | re.MULTILINE)
OPEN_STATUS = re.compile(r"\bStatus:\s*OPEN\b", re.IGNORECASE)
MATERIAL_YES = re.compile(r"\bMaterial:\s*yes\b", re.IGNORECASE)
UNKNOWN_DEFINITION = re.compile(r"^\s*-\s*\[U-\d{3}\]", re.IGNORECASE)
BLOCKER_DEFINITION = re.compile(r"^\s*-\s*\[B-\d{3}\]", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Check placeholders, duplicate IDs, undefined references, and "
            "structural READY contradictions in workflow artifacts. Review and "
            "authorization gates remain risk-dependent checks outside this script."
        )
    )
    parser.add_argument("paths", nargs="+", type=Path, help="Artifact file or directory")
    return parser.parse_args()


def collect_files(paths: list[Path]) -> tuple[list[Path], list[str]]:
    files: set[Path] = set()
    errors: list[str] = []
    for path in paths:
        if not path.exists():
            errors.append(f"{path}: path does not exist")
        elif path.is_file():
            files.add(path)
        elif path.is_dir():
            files.update(
                candidate
                for candidate in path.rglob("*")
                if candidate.is_file() and candidate.suffix.lower() in SUPPORTED_SUFFIXES
            )
        else:
            errors.append(f"{path}: unsupported path type")
    if not files and not errors:
        errors.append("no .md or .txt artifact files found")
    return sorted(files), errors


def validate(files: list[Path]) -> tuple[list[str], int, int]:
    issues: list[str] = []
    definitions: dict[str, list[tuple[Path, int]]] = defaultdict(list)
    references: list[tuple[str, Path, int]] = []

    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            issues.append(f"{path}: cannot read UTF-8 text: {exc}")
            continue

        ready = bool(READY.search(text))
        for line_number, line in enumerate(text.splitlines(), start=1):
            definition = DEFINITION.search(line)
            if definition:
                definitions[definition.group(1).upper()].append((path, line_number))

            for reference in REFERENCE.finditer(line):
                references.append((reference.group(1).upper(), path, line_number))

            if ID_RANGE.search(line):
                issues.append(
                    f"{path}:{line_number}: invalid ID range; reference each ID separately"
                )

            if PLACEHOLDER.search(line):
                issues.append(f"{path}:{line_number}: unresolved placeholder")

            if ready and OPEN_STATUS.search(line):
                if UNKNOWN_DEFINITION.search(line) and MATERIAL_YES.search(line):
                    issues.append(
                        f"{path}:{line_number}: readiness contradiction: "
                        "READY with an open material unknown"
                    )
                if BLOCKER_DEFINITION.search(line):
                    issues.append(
                        f"{path}:{line_number}: readiness contradiction: "
                        "READY with an open blocker"
                    )

    for item_id, locations in definitions.items():
        if len(locations) > 1:
            rendered = ", ".join(f"{path}:{line}" for path, line in locations)
            issues.append(f"duplicate definition {item_id}: {rendered}")

    for item_id, path, line_number in references:
        if item_id not in definitions:
            issues.append(f"{path}:{line_number}: undefined reference {item_id}")

    return issues, len(definitions), len(references)


def main() -> int:
    args = parse_args()
    files, path_errors = collect_files(args.paths)
    issues, definition_count, reference_count = validate(files)
    issues = path_errors + issues

    if issues:
        for issue in issues:
            print(f"ERROR: {issue}")
        print(f"FAILED: {len(issues)} issue(s)")
        return 1

    print(
        f"OK: validated {len(files)} file(s), {definition_count} definition(s), "
        f"{reference_count} reference(s)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
