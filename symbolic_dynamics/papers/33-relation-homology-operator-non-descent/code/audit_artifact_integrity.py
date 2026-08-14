#!/usr/bin/env python3
"""Verify Paper 33 frozen result hashes."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    failures: list[dict[str, str]] = []
    rows = []
    for line in (RESULTS / "SHA256SUMS.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        expected, name = line.split("  ", 1)
        actual = digest(RESULTS / name)
        rows.append({"path": name, "expected": expected, "actual": actual, "pass": expected == actual})
        if expected != actual:
            failures.append(rows[-1])
    payload = {
        "candidate_id": "SD-C35",
        "checked_files": len(rows),
        "failures": failures,
        "pass": not failures,
        "sha256sums_sha256": digest(RESULTS / "SHA256SUMS.txt"),
    }
    (RESULTS / "integrity_audit.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"candidate_id": "SD-C35", "checked_files": len(rows), "pass": not failures}))
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
