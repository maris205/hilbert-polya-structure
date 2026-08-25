#!/usr/bin/env python3
"""Generate the self-excluded C148 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C148_RELEASE_MANIFEST.json"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    excluded = {
        MANIFEST,
        ROOT / "paper/main.aux",
        ROOT / "paper/main.log",
        ROOT / "paper/main.out",
        ROOT / "paper/main.fdb_latexmk",
        ROOT / "paper/main.fls",
        ROOT / "paper/main.synctex.gz",
    }
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if path.is_file() and path not in excluded and "__pycache__" not in path.parts and path.suffix != ".pyc":
            files[str(path.relative_to(ROOT))] = digest(path)
    evidence = ROOT / "results/c148_walsh_baker_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c148-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "A three-symbol open Walsh gate has exact projection defects, a corrected escape-rank ledger, an all-period gcd trace formula, and five exact secular polynomials",
        "gates": {
            "G0_source_lock": "PASS",
            "G1_contraction_and_corrected_one_step_rank": "PASS",
            "G2_k_step_tensor_identity_and_escape_rank": "PASS",
            "G3_all_period_gcd_trace_formula": "PASS",
            "G4_exact_k1_to_k5_characteristic_polynomials": "PASS",
            "G5_complex_primitive_path_product": "PASS",
            "G6_closed_order_and_hole_controls": "PASS",
            "G7_independent_checker_sympy_replay_mutation": "PASS",
            "G8_double_compile_fonts_layout_visual": "PASS",
            "G9_manifest_hash_closure": "PASS",
            "G10_target_divisor_matching": "NOT_ESTABLISHED",
            "G11_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "k_values_with_exact_polynomials": 5,
            "exact_coefficient_cells": 67,
            "nonzero_coefficient_cells": 50,
            "direct_trace_sentinels": 60,
            "direct_tensor_source_checks": 363,
            "independent_checker_assertions": 748,
            "sympy_checks": 141,
            "repaired_hash_mutation_rejections": 40,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "INTRINSIC_FIXED_BASIS_COMPLEX_PRIMITIVE_PATHS_WITHOUT_A_PRIME_LIKE_TARGET_MAP",
            "A2": "A2_FAIL",
            "A2_qualification": "EXACT_SOURCE_SECULAR_POLYNOMIALS_WITHOUT_A_FROZEN_TARGET_DIVISOR_COMPARISON",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_GLOBAL_TARGET_STRUCTURE",
            "A4": "A4_UNITARY_OR_SCATTERING_CANDIDATE",
            "A4_qualification": "SOURCE_DERIVED_SUBUNITARY_GATE_WITH_EXACT_DEFECTS_AND_A_CLOSED_UNITARY_PARENT_BUT_NO_SELF_ADJOINT_OR_SEMICLASSICAL_TARGET_LIMIT",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "rank(B_k)=2^k at one step",
            "a self-adjoint quantization or a semiclassical target match",
            "an antiunitary symmetry",
            "a target zero or divisor match, functional equation, or counting law",
            "prime-like information, arithmetic local data, Euler factors, root numbers, or automorphy",
            "a Hilbert--Polya operator or Route-B authorization",
        ],
        "excluded_from_manifest": [
            "C148_RELEASE_MANIFEST.json",
            "code/__pycache__/",
            "*.pyc",
            "paper/main.aux",
            "paper/main.log",
            "paper/main.out",
            "paper/main.fdb_latexmk",
            "paper/main.fls",
            "paper/main.synctex.gz",
        ],
        "files": files,
    }
    if len(files) != 27:
        raise AssertionError(f"expected 27 manifest files, found {len(files)}")
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(
        json.dumps(
            {
                "manifest_sha256": digest(MANIFEST),
                "file_count": len(files),
                "evidence_sha256": digest(evidence),
                "pdf_sha256": digest(pdf),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
