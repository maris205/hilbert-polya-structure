#!/usr/bin/env python3
"""Build the content-addressed self-excluded C140 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C140_RELEASE_MANIFEST.json"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    excluded = {
        MANIFEST,
        ROOT / "paper/main.aux", ROOT / "paper/main.log", ROOT / "paper/main.out",
        ROOT / "paper/main.fdb_latexmk", ROOT / "paper/main.fls", ROOT / "paper/main.synctex.gz",
    }
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    evidence = ROOT / "results/c140_sofic_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c140-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "A strictly sofic mod-three gap suspension has an exact intrinsic zeta obtained by correcting the unique exceptional cover orbit",
        "gates": {
            "G0_source_lock": "PASS",
            "G1_strict_soficity_and_minimal_cover": "PASS",
            "G2_exact_cover_determinant": "PASS",
            "G3_all_period_exceptional_orbit_correction": "PASS",
            "G4_intrinsic_zeta_and_primitive_product": "PASS",
            "G5_nonlattice_label_suspension": "PASS",
            "G6_independent_checker_sympy_replay_mutation": "PASS",
            "G7_double_compile_fonts_layout_visual": "PASS",
            "G8_manifest_hash_closure": "PASS",
            "G9_natural_fredholm_owner": "NOT_ESTABLISHED",
            "G10_target_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "admissible_rooted_points_through_period_15": 969,
            "primitive_label_cycles_through_period_15": 74,
            "rooted_feature_cells_through_period_15": 60,
            "primitive_feature_cells_through_period_15": 32,
            "independent_checker_assertions": 2028,
            "sympy_checks": 53,
            "repaired_hash_mutation_rejections": 53,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "ALL_PERIOD_INTRINSIC_PRIMITIVE_ORBITS_OF_A_STRICTLY_SOFIC_SUSPENSION_WITHOUT_A_PRIME_LIKE_TARGET_MAP",
            "A2": "A2_FAIL",
            "A2_qualification": "EXACT_INTRINSIC_RATIONAL_ZETA_AND_COVER_CORRECTION_WITHOUT_A_FROZEN_TARGET_DIVISOR_MATCH",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_GAMMA_FACTOR_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4": "A4_FAIL",
            "A4_qualification": "NO_NATURAL_SELF_ADJOINT_UNITARY_SCATTERING_OR_HAMILTONIAN_LIFT",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "that the three-state cover trace already equals the intrinsic label fixed-point trace",
            "a natural Fredholm determinant owner for the corrected rational inverse zeta",
            "an arithmetic Euler product or local factorization",
            "a target zero or pole divisor match, functional equation, or counting law",
            "a natural self-adjoint Hilbert--Polya operator",
            "Route-B authorization or a solution of the larger program",
        ],
        "excluded_from_manifest": [
            "C140_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper/main.aux", "paper/main.log", "paper/main.out",
            "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C140_MANIFEST_PASS", "file_count": len(files), "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)}, sort_keys=True))


if __name__ == "__main__":
    main()
