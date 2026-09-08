#!/usr/bin/env python3
"""Read-only artifact audit; never executes UUC or any historical science."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--check-seal", action="store_true")
args = parser.parse_args()
base = Path(__file__).resolve().parent
workspace = base.parents[3]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

files = sorted(p for p in base.rglob("*") if p.is_file())
assert not any(p.is_symlink() for p in base.rglob("*")), "symlink in owned package"
assert sum(p.stat().st_size for p in files) < 2_000_000, "package exceeds compact cap"

history_rows = []
for row in (base / "HISTORY_INPUTS.sha256").read_text().splitlines():
    expected, relative = row.split("  ", 1)
    assert re.fullmatch(r"[0-9a-f]{64}", expected)
    target = workspace / relative
    assert target.is_file(), relative
    assert digest(target) == expected, relative
    history_rows.append(relative)
assert len(history_rows) == 17 and len(set(history_rows)) == 17

links = []
for path in sorted(base.glob("*.md")):
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
        if target.startswith(("https://", "http://", "mailto:", "#")):
            continue
        target = target.split("#", 1)[0]
        assert (path.parent / target).resolve().exists(), (str(path), target)
        links.append((str(path.relative_to(base)), target))

json_files = sorted(base.rglob("*.json"))
for path in json_files:
    json.loads(path.read_text())
discovery = json.loads((base / "evidence/DISCOVERY_NATIVE.json").read_text())
assert discovery["result"]["exit_code"] == 0
assert discovery["result"]["output"].endswith("\n")
source_access = json.loads((base / "evidence/SOURCE_ACCESS.json").read_text())
assert len(source_access["search_query_groups"]) == 3
assert len(source_access["primary_access"]) == 3

seal_count = None
if args.check_seal:
    rows = []
    for row in (base / "MANIFEST.sha256").read_text().splitlines():
        expected, relative = row.split("  ", 1)
        path = base / relative
        assert path.is_file() and relative != "MANIFEST.sha256", relative
        assert digest(path) == expected, relative
        rows.append(relative)
    actual = {str(p.relative_to(base)) for p in files if p.name != "MANIFEST.sha256"}
    assert len(rows) == len(set(rows)), "duplicate manifest key"
    assert set(rows) == actual, "manifest is not complete nonself coverage"
    seal_count = len(rows)

print(json.dumps({
    "status": "PASS_ARTIFACT_ONLY",
    "scientific_runs": 0,
    "history_pins_checked": len(history_rows),
    "local_markdown_links_checked": len(links),
    "json_files_parsed": len(json_files),
    "package_files_seen": len(files),
    "package_bytes_seen": sum(p.stat().st_size for p in files),
    "nonself_seal_entries_checked": seal_count,
    "python": sys.version,
    "limitations": [
        "No UUC or old scientific verifier is executed.",
        "Not an independent mathematical or source-owner review.",
        "Runtime dependencies are not a pinned hermetic execution capsule.",
        "History pins are post-reading identities, not complete corpus coverage."
    ]
}, indent=2))
