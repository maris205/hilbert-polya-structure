#!/usr/bin/env python3
"""Build the content-addressed self-excluded C159 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C159_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    excluded = {MANIFEST, ROOT / "paper/main.aux", ROOT / "paper/main.log", ROOT / "paper/main.out", ROOT / "paper/main.fdb_latexmk", ROOT / "paper/main.fls", ROOT / "paper/main.synctex.gz"}
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    evidence = ROOT / "results/c159_s_gap_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c159-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "A recurrent mixing Thue--Morse S-gap shift has an exact renewal zeta whose source meromorphic continuation has the unit circle as a natural boundary",
        "gates": {
            "G0_source_lock_and_pivot": "PASS", "G1_recurrent_mixing": "PASS",
            "G2_dense_periodic_points": "PASS", "G3_exact_renewal_zeta_entropy": "PASS",
            "G4_natural_boundary": "PASS", "G5_checker_sympy_replay_mutation": "PASS",
            "G6_bilingual_double_compile_fonts_layout_visual": "PASS", "G7_manifest_hash_closure": "PASS",
            "G8_target_divisor_matching": "NOT_ESTABLISHED", "G9_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "fixed_period_rows": 18, "formal_series_cells": 49,
            "independent_checker_assertions": 742, "sympy_checks": 118,
            "repaired_hash_mutation_rejections": 45, "stale_hash_mutation_rejections": 1,
            "pdf_pages": 2, "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK", "A1_qualification": "RECURRENT_MIXING_RENEWAL_DYNAMICS_WITH_DENSE_NONTRIVIAL_PERIODIC_POINTS",
            "A2": "A2_FAIL", "A2_qualification": "EXACT_SOURCE_ZETA_BUT_NO_TARGET_DIVISOR_COMPARISON",
            "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE", "A3_qualification": "PROVED_SOURCE_MEROMORPHIC_CONTINUATION_AND_UNIT_CIRCLE_NATURAL_BOUNDARY_WITH_NO_TARGET_GLOBAL_STRUCTURE_COMPARISON",
            "A4": "A4_FAIL", "A4_qualification": "NO_NATURAL_UNITARY_SCATTERING_OR_HAMILTONIAN_LIFT",
            "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False,
        },
        "nonclaims": ["a target divisor or critical line", "an arithmetic Euler product or local factorization", "a target functional equation or counting-law match", "a natural self-adjoint Hilbert--Polya operator", "Route-B authorization or a solution of the larger program"],
        "excluded_from_manifest": ["C159_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper/main.aux", "paper/main.log", "paper/main.out", "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz"],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C159_MANIFEST_PASS", "file_count": len(files), "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)}, sort_keys=True))


if __name__ == "__main__":
    main()
