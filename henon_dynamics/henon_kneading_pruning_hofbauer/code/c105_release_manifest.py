#!/usr/bin/env python3
"""Create the C105 content-addressed release manifest."""
from __future__ import annotations
from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C105_RELEASE_MANIFEST.json"
EXCLUDED = {MANIFEST, PROJECT / "paper/main.aux", PROJECT / "paper/main.log", PROJECT / "paper/main.out", PROJECT / "paper/main.fdb_latexmk", PROJECT / "paper/main.fls"}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    files = {}
    for path in sorted(PROJECT.rglob("*")):
        if path.is_file() and path not in EXCLUDED and "__pycache__" not in path.parts:
            files[str(path.relative_to(PROJECT))] = digest(path)
    evidence = PROJECT / "results/c105_kneading_evidence.json"
    pdf = PROJECT / "paper/main.pdf"
    doc = {
        "schema": "hcs-c105-release-v1",
        "status": "RELEASE_CANDIDATE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Finite kneading/pruning language and Hofbauer determinant prefix",
        "verdict": {"A1": "A1_OPEN", "A2": "A2_CERTIFIED_PREFIX", "A3": "A3_NOT_ADDRESSED", "A4": "A4_FAIL"},
        "results": {"period_max": 12, "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf) if pdf.exists() else "", "pdf_pages": 2},
        "nonclaims": ["prime correspondence", "Riemann zeros", "global Hénon coding", "analytic Fredholm determinant", "Route B"],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(doc, sort_keys=True, indent=2) + "\n")
    print(digest(MANIFEST))


if __name__ == "__main__":
    main()
