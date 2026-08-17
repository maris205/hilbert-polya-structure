#!/usr/bin/env python3
"""Render the self-excluding C-sorted Paper 43 static-input manifest."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXCLUDED_ROOTS = ("results/", "evaluations/")
EXCLUDED_FILES = {
    "EXPERIMENT_REPORT.md", "PAPER_MANIFEST.sha256", "STATIC_INPUT_SHA256SUMS.txt",
}


def main() -> int:
    contract = json.loads(
        (ROOT / "code/contracts/INTEGRATION_CONTRACT.json").read_text(
            encoding="ascii"))
    overlay_paths = set(
        contract["authority_overlay"]["static_manifest_excluded_overlay_paths"])
    rows = []
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT).as_posix()
        if path.is_symlink():
            raise ValueError(f"symlink forbidden: {relative}")
        if not path.is_file() or relative in EXCLUDED_FILES \
                or relative in overlay_paths \
                or relative.startswith(EXCLUDED_ROOTS):
            continue
        if path.name == "__pycache__" or path.suffix == ".pyc":
            raise ValueError(f"cache forbidden: {relative}")
        rows.append((relative, hashlib.sha256(path.read_bytes()).hexdigest()))
    rows.sort()
    if len(rows) != len({relative for relative, _ in rows}):
        raise ValueError("static paths are not unique")
    sys.stdout.write("".join(f"{digest}  {relative}\n" for relative, digest in rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
