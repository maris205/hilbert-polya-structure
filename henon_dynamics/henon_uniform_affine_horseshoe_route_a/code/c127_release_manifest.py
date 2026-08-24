#!/usr/bin/env python3
"""Generate the closed C127 release ledger."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "C127_RELEASE_MANIFEST.json"
EXCLUDE = {OUTPUT.name}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


files = []
for path in sorted(p for p in ROOT.rglob("*") if p.is_file()):
    rel = path.relative_to(ROOT).as_posix()
    if rel in EXCLUDE or any(part.startswith(".") or part == "__pycache__" for part in path.relative_to(ROOT).parts):
        continue
    if path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk"}:
        continue
    files.append({"path": rel, "bytes": path.stat().st_size, "sha256": sha(path)})

manifest = {
    "schema": "HCS-C127-release-v1",
    "candidate_id": "HCS-C127",
    "date_utc": "2026-08-24",
    "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
    "route_a_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
    "route_b_invocation_allowed": False,
    "file_count_excluding_manifest": len(files),
    "evidence_sha256": sha(ROOT / "results" / "c127_uniform_horseshoe_evidence.json"),
    "paper_pdf_sha256": sha(ROOT / "paper" / "main.pdf"),
    "files": files,
}
OUTPUT.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
print(OUTPUT)
