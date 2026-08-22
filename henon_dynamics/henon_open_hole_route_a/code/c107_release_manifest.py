#!/usr/bin/env python3
from __future__ import annotations
from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C107_RELEASE_MANIFEST.json"
EXCLUDED = {MANIFEST, PROJECT / "paper/main.aux", PROJECT / "paper/main.log", PROJECT / "paper/main.out", PROJECT / "paper/main.fdb_latexmk", PROJECT / "paper/main.fls"}


def h(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    files = {}
    for path in sorted(PROJECT.rglob("*")):
        if path.is_file() and path not in EXCLUDED and "__pycache__" not in path.parts:
            files[str(path.relative_to(PROJECT))] = h(path)
    evidence = PROJECT / "results/c107_open_hole_evidence.json"
    pdf = PROJECT / "paper/main.pdf"
    doc = {
        "schema": "hcs-c107-release-v1",
        "status": "RELEASE_CANDIDATE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Frozen open Hénon survivor and exact escape determinant",
        "verdict": {"A1": "A1_PARTIAL_CERTIFIED", "A2": "A2_CERTIFIED_PREFIX", "A3": "A3_NOT_ADDRESSED", "A4": "A4_FAIL"},
        "results": {"hole_state": 3, "period_max": 12, "evidence_sha256": h(evidence), "pdf_sha256": h(pdf) if pdf.exists() else "", "pdf_pages": 1},
        "nonclaims": ["analytic open Fredholm determinant", "prime correspondence", "Riemann zeros", "Route B"],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(doc, sort_keys=True, indent=2) + "\n")
    print(h(MANIFEST))


if __name__ == "__main__":
    main()
