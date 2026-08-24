#!/usr/bin/env python3
"""Content-addressed release ledger for C116."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C116_PREFREEZE_MANIFEST.json"


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    files = {}
    ignored_suffixes = {".aux", ".log", ".out", ".fls", ".fdb_latexmk"}
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and path != MANIFEST and "__pycache__" not in path.parts and path.suffix not in ignored_suffixes:
            files[str(path.relative_to(ROOT))] = digest(path)
    evidence = ROOT / "results/c116_lozi_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    payload = {
        "schema": "hcs-c116-lozi-nonsmooth-prefreeze-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Strict Lozi sign-itinerary pruning atlas and finite weighted cycle prefix",
        "route_a_verdict": {
            "A1": "A1_PARTIAL_CERTIFIED",
            "A2": "A2_CERTIFIED_PREFIX",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
        },
        "results": {
            "parameters": {"a": "2", "b": "1/2"},
            "max_period": 8,
            "primitive_necklaces": 37,
            "cycle_atlas_dimension": 240,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf) if pdf.exists() else "",
            "pdf_pages": 2,
            "mutation_rejections": 12,
        },
        "nonclaims": [
            "complete Lozi invariant set",
            "global Markov partition",
            "analytic Fredholm determinant",
            "arithmetic data",
            "Route B",
        ],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(digest(MANIFEST))


if __name__ == "__main__":
    main()
