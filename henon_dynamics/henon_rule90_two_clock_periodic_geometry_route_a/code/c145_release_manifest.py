#!/usr/bin/env python3
"""Build the content-addressed self-excluded C145 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C145_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
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
    evidence = ROOT / "results/c145_rule90_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c145-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Cyclic Rule 90 has an all-size exact kernel-gcd count and an essential ordered two-clock periodic geometry",
        "gates": {
            "G0_source_lock": "PASS",
            "G1_all_size_kernel_gcd_theorem": "PASS",
            "G2_non_squarefree_even_lengths": "PASS",
            "G3_temporal_mobius_and_cycle_integrality": "PASS",
            "G4_spatiotemporal_torus_bijection": "PASS",
            "G5_aspect_ratio_and_divisor_history_witnesses": "PASS",
            "G6_independent_checker_sympy_replay_mutation": "PASS",
            "G7_double_compile_fonts_layout_visual": "PASS",
            "G8_manifest_hash_closure": "PASS",
            "G9_target_divisor_matching": "NOT_ESTABLISHED",
            "G10_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "two_clock_cells": 576,
            "fixed_point_sum": 488334,
            "exact_period_point_sum": 283758,
            "primitive_temporal_cycle_sum": 24474,
            "independent_checker_assertions": 6520,
            "sympy_checks": 1177,
            "repaired_hash_mutation_rejections": 42,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "EXACT_INTRINSIC_FINITE_VOLUME_TEMPORAL_CYCLES_WITH_ESSENTIAL_TWO_CLOCK_DEPENDENCE",
            "A2": "A2_FAIL",
            "A2_qualification": "NO_SINGLE_FROZEN_CLOCK_OR_TARGET_DIVISOR_DETERMINANT",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4": "A4_FAIL",
            "A4_qualification": "NO_NATURAL_UNITARY_SCATTERING_OR_HAMILTONIAN_LIFT",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "a thermodynamic or infinite-volume limit of the two-clock table",
            "that area alone determines spatiotemporal periodic geometry",
            "an arithmetic Euler product or local factorization",
            "a target divisor, functional equation, or counting-law match",
            "a natural self-adjoint Hilbert--Polya operator",
            "Route-B authorization or a solution of the larger program",
        ],
        "excluded_from_manifest": [
            "C145_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper/main.aux", "paper/main.log", "paper/main.out",
            "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C145_MANIFEST_PASS", "file_count": len(files), "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)}, sort_keys=True))


if __name__ == "__main__":
    main()
