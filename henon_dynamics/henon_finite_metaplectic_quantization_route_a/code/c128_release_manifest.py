#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "C128_RELEASE_MANIFEST.json"


def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()


rows = []
for p in sorted(x for x in ROOT.rglob("*") if x.is_file()):
    rel = p.relative_to(ROOT).as_posix()
    if rel == OUT.name or "__pycache__" in p.parts or p.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk"}: continue
    rows.append({"path": rel, "bytes": p.stat().st_size, "sha256": sha(p)})
data = {
    "schema": "HCS-C128-release-v1", "candidate_id": "HCS-C128", "date_utc": "2026-08-24",
    "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
    "route_a_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
    "route_b_invocation_allowed": False, "file_count_excluding_manifest": len(rows),
    "evidence_sha256": sha(ROOT / "results" / "c128_metaplectic_evidence.json"),
    "paper_pdf_sha256": sha(ROOT / "paper" / "main.pdf"), "files": rows,
}
OUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
print(OUT)
