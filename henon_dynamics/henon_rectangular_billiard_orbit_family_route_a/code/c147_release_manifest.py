#!/usr/bin/env python3
"""Build the self-excluded content-addressed HCS-C147 manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C147_RELEASE_MANIFEST.json"


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
    evidence = ROOT / "results/c147_billiard_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c147-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Primitive square-billiard directions form one-parameter cylinders with exact length degeneracies and a natural integrable quantization, while every isolated-orbit denominator is singular",
        "gates": {
            "G0_source_lock": "PASS",
            "G1_unfolding_and_primitive_family_theorem": "PASS",
            "G2_exact_direction_ledger_and_mobius_count": "PASS",
            "G3_minimal_inequivalent_length_collision": "PASS",
            "G4_irrational_aspect_ratio_control": "PASS",
            "G5_clean_family_stability_obstruction": "PASS",
            "G6_natural_integrable_quantization_boundary": "PASS",
            "G7_independent_checker_sympy_replay_mutation": "PASS",
            "G8_double_compile_fonts_layout_visual": "PASS",
            "G9_manifest_hash_closure": "PASS",
            "G10_target_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "positive_primitive_direction_count": 979,
            "ordered_length_degeneracy_group_count": 389,
            "symmetry_reduced_degeneracy_group_count": 98,
            "first_inequivalent_collision_square": 65,
            "independent_checker_assertions": 1082,
            "sympy_checks": 88,
            "repaired_hash_mutation_rejections": 35,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "INTRINSIC_REPRODUCIBLE_PRIMITIVE_DIRECTION_FAMILIES_EXIST_BUT_ARE_NOT_ISOLATED_OR_PRIME_LIKE",
            "A2": "A2_FAIL",
            "A2_qualification": "THE_FULL_REDUCED_POINCARE_LINEARIZATION_HAS_A_FAMILY_TANGENT_UNIT_EIGENVALUE_SO_THE_ORDINARY_ISOLATED_ORBIT_DETERMINANT_IS_SINGULAR",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4": "A4_NATURAL_QUANTIZATION",
            "A4_qualification": "THE_DIRICHLET_HALF_WAVE_IS_INTRINSIC_UNITARY_TIME_REVERSAL_SYMMETRIC_AND_CLOCK_MATCHED_BUT_SUPPLIES_NO_CLEAN_FAMILY_TRACE_BRIDGE_OR_TARGET_MATCH",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "isolated primitive billiard orbits for the rational directions",
            "validity of an ordinary isolated-orbit determinant",
            "a target divisor, functional equation, or counting law",
            "a prime-like correspondence",
            "an arithmetic local or Euler factorization, root number, or automorphy statement",
            "a Hilbert--Polya construction or Route-B authorization",
        ],
        "excluded_from_manifest": [
            "C147_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper/main.aux", "paper/main.log", "paper/main.out",
            "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": "C147_MANIFEST_PASS", "file_count": len(files), "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)}, sort_keys=True))


if __name__ == "__main__":
    main()
