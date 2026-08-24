#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "C133_RELEASE_MANIFEST.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


rows = []
for path in sorted(p for p in ROOT.rglob("*") if p.is_file()):
    rel = path.relative_to(ROOT).as_posix()
    if rel == OUT.name or "__pycache__" in path.parts or path.suffix in {
        ".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk"
    }:
        continue
    rows.append({"path": rel, "bytes": path.stat().st_size, "sha256": sha(path)})

data = {
    "schema": "HCS-C133-release-v1",
    "candidate_id": "HCS-C133",
    "date_utc": "2026-08-24",
    "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
    "route_a_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_UNITARY_OR_SCATTERING_CANDIDATE"],
    "route_b_invocation_allowed": False,
    "file_count_excluding_manifest": len(rows),
    "evidence_sha256": sha(ROOT / "results" / "c133_quantum_graph_evidence.json"),
    "paper_pdf_sha256": sha(ROOT / "paper" / "main.pdf"),
    "files": rows,
}
OUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
print(OUT)
