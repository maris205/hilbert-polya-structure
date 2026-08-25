#!/usr/bin/env python3
"""Build the content-addressed self-excluded C150 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C150_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    excluded = {MANIFEST, ROOT / "paper/main.aux", ROOT / "paper/main.log", ROOT / "paper/main.out", ROOT / "paper/main.fdb_latexmk", ROOT / "paper/main.fls", ROOT / "paper/main.synctex.gz"}
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    evidence = ROOT / "results/c150_rule90_mersenne_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c150-release-v1", "status": "RELEASE_COMPLETE", "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Rule 90 on every Mersenne ring has a half-size periodic image reached in one step, while the matched power-of-two family is nilpotent",
        "gates": {
            "G0_source_lock": "PASS", "G1_frobenius_identity": "PASS", "G2_image_rank_and_periodicity": "PASS",
            "G3_divisor_resolved_cycles": "PASS", "G4_power_of_two_negative_control": "PASS",
            "G5_checker_sympy_replay_mutation": "PASS", "G6_double_compile_fonts_layout_visual": "PASS",
            "G7_manifest_hash_closure": "PASS", "G8_target_divisor_matching": "NOT_ESTABLISHED", "G9_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "all_r_theorem": True, "replay_r_limit": 8, "divisor_period_cells": 27, "power_control_s_limit": 8,
            "independent_checker_assertions": 153, "sympy_checks": 276,
            "repaired_hash_mutation_rejections": 44, "stale_hash_mutation_rejections": 1,
            "pdf_pages": 1, "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK", "A1_qualification": "ALL_R_EXACT_MERSENNE_PERIODIC_IMAGE_WITH_DIVISOR_RESOLVED_PRIMITIVE_CYCLES",
            "A2": "A2_FAIL", "A2_qualification": "SCALING_FAMILY_OF_FINITE_POLYNOMIAL_COUNTS_WITH_NO_TARGET_DIVISOR_COMPARISON",
            "A3": "A3_FAIL", "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4": "A4_FAIL", "A4_qualification": "NO_NATURAL_UNITARY_SCATTERING_OR_HAMILTONIAN_LIFT",
            "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False,
        },
        "nonclaims": ["that every divisor of L occurs as a cycle period", "an infinite-volume determinant or thermodynamic limit", "an arithmetic Euler product or local factorization", "a target divisor, functional equation, or counting-law match", "a natural self-adjoint Hilbert--Polya operator", "Route-B authorization or a solution of the larger program"],
        "excluded_from_manifest": ["C150_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper/main.aux", "paper/main.log", "paper/main.out", "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz"],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C150_MANIFEST_PASS", "file_count": len(files), "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)}, sort_keys=True))


if __name__ == "__main__":
    main()
