#!/usr/bin/env python3
"""Freeze Paper 33 result payload hashes."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
EXCLUDED = {"SHA256SUMS.txt", "aggregate_sha256.txt", "artifact_inventory.json", "integrity_audit.json"}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    files = [p for p in sorted(RESULTS.iterdir()) if p.is_file() and p.name not in EXCLUDED]
    lines = [f"{digest(path)}  {path.name}" for path in files]
    (RESULTS / "SHA256SUMS.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    aggregate = hashlib.sha256((RESULTS / "SHA256SUMS.txt").read_bytes()).hexdigest()
    (RESULTS / "aggregate_sha256.txt").write_text(aggregate + "\n", encoding="utf-8")
    inventory = {
        "candidate_id": "SD-C35",
        "result_files_hashed": len(files),
        "sha256sums_sha256": aggregate,
        "files": [{"path": path.name, "sha256": digest(path)} for path in files],
    }
    (RESULTS / "artifact_inventory.json").write_text(json.dumps(inventory, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"candidate_id": "SD-C35", "files": len(files), "sha256sums_sha256": aggregate}))


if __name__ == "__main__":
    main()
