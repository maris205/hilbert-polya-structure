#!/usr/bin/env python3
"""Build the content-addressed C131 release manifest."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C131_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c131_odd_metaplectic_evidence.json"
PDF = ROOT / "paper/main.pdf"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


files = []
for path in sorted(p for p in ROOT.rglob("*") if p.is_file() and p != MANIFEST):
    rel = path.relative_to(ROOT).as_posix()
    if "__pycache__" in rel or path.suffix in {".pyc", ".aux", ".log", ".out", ".fls", ".fdb_latexmk"}:
        continue
    files.append({"path": rel, "bytes": path.stat().st_size, "sha256": sha(path)})
data = {
    "schema": "HCS-C131-release-v1",
    "candidate_id": "HCS-C131",
    "date_utc": "2026-08-24",
    "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
    "route_a_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
    "route_b_invocation_allowed": False,
    "file_count_excluding_manifest": len(files),
    "evidence_sha256": sha(EVIDENCE),
    "paper_pdf_sha256": sha(PDF),
    "files": files,
}
MANIFEST.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
print(json.dumps({"file_count": len(files), "evidence_sha256": data["evidence_sha256"], "pdf_sha256": data["paper_pdf_sha256"], "manifest_sha256": sha(MANIFEST)}, sort_keys=True))
