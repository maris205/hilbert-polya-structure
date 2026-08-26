#!/usr/bin/env python3
"""Build the content-addressed self-excluded C173 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C173_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
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
        if not path.is_file() or path in excluded or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        files[str(path.relative_to(ROOT))] = digest(path)

    evidence = ROOT / "results/c173_lyness_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c173-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C173",
        "evaluation_date": "2026-08-26",
        "source_commit": "ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "The positive Lyness map has an exact global five-cycle law that obstructs both classical Artin--Mazur and ordinary trace-class Koopman determinants",
        "gates": {
            "G0_source_domain_clock_measure_lock": "PASS",
            "G1_exact_F1_through_F5_and_unique_fixed_point": "PASS",
            "G2_all_point_period_classification_and_zeta_obstruction": "PASS_WITH_OBSTRUCTION",
            "G3_invariant_density_inverse_and_reversor": "PASS",
            "G4_unitary_order_five_projection_decomposition": "PASS",
            "G5_infinite_multiplicity_compactness_schatten_fredholm_selfadjoint_audit": "PASS_WITH_OBSTRUCTION",
            "G6_checker_sympy_replay_mutation": "PASS",
            "G7_bilingual_double_compile_fonts_layout_visual": "PASS",
            "G8_manifest_hash_closure": "PASS",
            "G9_arithmetic_target_hilbert_polya_route_b": "NOT_CLAIMED",
        },
        "results": {
            "global_map_order": 5,
            "least_period_values": [1, 5],
            "first_infinite_fixed_set_n": 5,
            "koopman_eigenspaces": 5,
            "infinite_dimensional_koopman_eigenspaces": 5,
            "rational_grid_rows": 100,
            "fixed_set_n_max": 50,
            "independent_checker_assertions": 891,
            "sympy_checks": 207,
            "repaired_hash_mutation_rejections": 49,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": 2,
            "pivot_required": False,
            "evidence_payload_sha256": "f96c44000538c10fbd3928991b44bcb7f003b6deb890d81045fa358b8d5ec97b",
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A0": "A0_FAIL",
            "A0_qualification": "NO_INTRINSIC_ARITHMETIC_OR_PRIME_POWER_ORIGIN",
            "A1": "A1_FAIL",
            "A1_qualification": "EXACT_PERIOD_CLASSIFICATION_BUT_UNCOUNTABLE_NONARITHMETIC_PRIMITIVE_FIVE_CYCLES",
            "A2": "A2_FAIL",
            "A2_qualification": "CLASSICAL_ARTIN_MAZUR_SERIES_FAILS_AT_N_5_AND_KOOPMAN_IS_NOT_TRACE_CLASS",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_SOURCE_DETERMINANT_FOR_GLOBAL_ANALYTIC_OR_WEIL_COMPRESSION_TESTS",
            "A4": "A4_NATURAL_QUANTIZATION",
            "A4_qualification": "NATURAL_ORDER_FIVE_UNITARY_KOOPMAN_LIFT_AND_ANTIUNITARY_REVERSAL_ONLY",
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "a finite count for the uncountable fixed set Fix(F^5)",
            "a classical Artin--Mazur zeta or isolated primitive-orbit Euler product",
            "a regularized, Lefschetz, or distributional substitute determinant",
            "an ordinary trace-class Fredholm determinant of the Koopman operator",
            "a compact, finite-Schatten, self-adjoint, or target-spectrum Koopman operator",
            "a prime-like orbit correspondence or arithmetic local data",
            "a target divisor, functional equation, or counting-law match",
            "an arithmetic Euler product, local factor, or root number",
            "automorphy, a Hilbert--Polya construction, or Route-B authorization",
        ],
        "integrity": {
            "hard_gate": "global fifth-iterate and period theorem plus existence audit for classical orbit and ordinary Koopman determinants",
            "hard_gate_status": "PASS_WITH_OBSTRUCTION",
            "dynamics_pivot_used": False,
            "model_rejected_as_primary_route_a_candidate": True,
            "finite_ledgers_are_proof": False,
            "external_reviewer_simulated": False,
            "citation_population": 0,
        },
        "excluded_from_manifest": [
            "C173_RELEASE_MANIFEST.json",
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
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(
        json.dumps(
            {
                "status": "C173_MANIFEST_PASS",
                "file_count": len(files),
                "manifest_sha256": digest(MANIFEST),
                "evidence_sha256": digest(evidence),
                "pdf_sha256": digest(pdf),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
