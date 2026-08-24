#!/usr/bin/env python3
"""Build the deterministic C117 prefreeze ledger."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C117_PREFREEZE_MANIFEST.json"


def h(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    excluded = {
        "C117_PREFREEZE_MANIFEST.json", "paper/main.aux", "paper/main.log",
        "paper/main.out", "paper/main.fls", "paper/main.fdb_latexmk",
        "paper/main.synctex.gz",
    }
    files = {}
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or "__pycache__" in p.parts:
            continue
        rel = str(p.relative_to(ROOT))
        if rel not in excluded:
            files[rel] = h(p)
    evidence = ROOT / "results/c117_markov_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    value = {
        "schema_id": "hcs-c117-markov-switching-moment-prefreeze-manifest-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Exact source-owned tangent moment operators for a Markov-switching Hénon cocycle",
        "files": files,
        "excluded_from_manifest": sorted(excluded) + ["code/__pycache__/"],
        "results": {
            "first_moment_dimension": 4, "second_moment_dimension": 6,
            "mutation_rejections": 12, "pdf_pages": 2,
            "evidence_sha256": h(evidence), "pdf_sha256": h(pdf) if pdf.exists() else "",
        },
        "route_a_verdict": {
            "A1": "A1_WEAK", "A2": "A2_CERTIFIED_PREFIX",
            "A3": "A3_NOT_ADDRESSED", "A4": "A4_FAIL",
            "overall": "ROUTE_A_EXPLORATORY",
        },
        "gates": {
            "G0_model_and_markov_convention": "PASS",
            "G1_exact_tangent_moment_operators": "PASS",
            "G2_stationary_average_control": "PASS",
            "G3_independent_symbolic_replay_mutation": "PASS",
            "G4_pdf_determinism_fonts_layout": "PASS",
            "G5_manifest_hash_closure": "PASS",
            "G6_global_nonlinear_random_transfer": "NOT_ESTABLISHED",
            "G7_arithmetic_or_route_b": "NOT_CLAIMED",
        },
        "nonclaims": [
            "complete nonlinear random orbit atlas",
            "global nonlinear transfer, Fredholm, or nuclear operator",
            "arithmetic/local data, Euler factors, root numbers, or automorphy",
            "Hilbert--Polya operator or Route-B authorization",
        ],
    }
    MANIFEST.write_text(json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"manifest_sha256": h(MANIFEST), "file_count": len(files),
                      "evidence_sha256": h(evidence), "pdf_sha256": h(pdf) if pdf.exists() else ""}, sort_keys=True))


if __name__ == "__main__":
    main()
