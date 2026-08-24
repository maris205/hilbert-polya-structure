#!/usr/bin/env python3
"""Build the self-excluded 27-payload HCS-C136 release manifest."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "C136_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results" / "c136_crt_metaplectic_evidence.json"
PDF = ROOT / "paper" / "main.pdf"
EXCLUDED_SUFFIXES = {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".synctex.gz"}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


rows = []
for path in sorted(p for p in ROOT.rglob("*") if p.is_file()):
    rel = path.relative_to(ROOT).as_posix()
    if rel == OUT.name or "__pycache__" in path.parts or path.suffix in EXCLUDED_SUFFIXES:
        continue
    rows.append({"path": rel, "bytes": path.stat().st_size, "sha256": sha(path)})

assert EVIDENCE.is_file(), EVIDENCE
assert PDF.is_file(), PDF
assert len(rows) == 27, f"expected 27 payload files, found {len(rows)}"

data = {
    "schema": "HCS-C136-release-v1",
    "candidate_id": "HCS-C136",
    "date_utc": "2026-08-24",
    "release_status": "FINAL_RELEASE_READY",
    "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
    "route_a_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
    "overall_verdict": "ROUTE_A_EXPLORATORY",
    "route_b_invocation_allowed": False,
    "file_count_excluding_manifest": len(rows),
    "evidence_sha256": sha(EVIDENCE),
    "paper_pdf_sha256": sha(PDF),
    "files": rows,
}
OUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
print(OUT)
