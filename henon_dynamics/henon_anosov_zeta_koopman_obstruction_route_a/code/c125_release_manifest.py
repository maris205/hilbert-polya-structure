#!/usr/bin/env python3
"""Build the content-addressed C125 pre-freeze release ledger."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C125_RELEASE_MANIFEST.json"


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
    files: dict[str, str] = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts:
            continue
        files[str(path.relative_to(ROOT))] = digest(path)

    evidence = ROOT / "results/c125_anosov_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c125-release-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "All-order Anosov orbit zeta and a natural Koopman determinant-class obstruction",
        "gates": {
            "G0_toral_automorphism_clock_and_zeta_convention_freeze": "PASS",
            "G1_all_order_fixed_point_kernel_count": "PASS",
            "G2_mobius_primitive_counts_and_exact_rational_zeta": "PASS",
            "G3_natural_koopman_unitarity_and_noncompactness_obstruction": "PASS",
            "G4_parabolic_sign_and_wraparound_controls": "PASS",
            "G5_independent_checker_sympy_and_canonical_replay": "PASS",
            "G6_hostile_mutation_audit": "PASS",
            "G7_paper_double_isolated_compile_font_and_visual_check": "PASS",
            "G8_manifest_hash_closure": "PASS",
            "G9_prime_like_correspondence_target_divisor_and_analytic_bridge": "NOT_ESTABLISHED",
            "G10_arithmetic_hilbert_polya_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "all_order_fixed_point_theorem": True,
            "maximum_replayed_period": 12,
            "fixed_point_count_at_period_12": 103680,
            "primitive_orbit_count_at_period_12": 8610,
            "exact_zeta": "(1-z)^2/(1-3*z+z^2)",
            "koopman_unitary": True,
            "koopman_noncompact": True,
            "mutation_rejections": 23,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "evaluator": "henon_dynamics/skills/route-a-evaluator.md",
            "canonical_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "canonical_tuple_text": "(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)",
            "A1": "A1_WEAK",
            "A1_qualification": "COMPLETE_INTRINSIC_PRIMITIVE_ORBIT_CENSUS_BUT_NO_PRIME_LIKE_TARGET_CORRESPONDENCE_OR_AMPLITUDE_LAW",
            "A2": "A2_FAIL",
            "A2_qualification": "EXACT_INTERNAL_ARTIN_MAZUR_ZETA_BUT_NO_TARGET_DIVISOR_OR_SEALED_ZERO_COMPARISON_AND_NATURAL_KOOPMAN_IS_NOT_DETERMINANT_CLASS",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_GAMMA_FACTOR_COUNTING_LAW_OR_CONTROLLED_TARGET_CONTINUATION",
            "A4": "A4_FORMAL_HINT",
            "A4_qualification": "NATURAL_UNITARY_KOOPMAN_ACTION_EXISTS_BUT_NO_TRACE_COMPATIBLE_QUANTIZATION_OR_ORBIT_PHASE_LIFT",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "prime-like orbit correspondence, logarithmic-prime clock, target amplitude law, or complete arithmetic labeling",
            "target divisor match, missing/extra target-zero census, sealed validation pass, or identification of the Artin-Mazur zeta with a target function",
            "ordinary operator trace or ordinary trace-class Fredholm determinant for the Koopman unitary",
            "functional equation, Gamma factor, trivial-zero treatment, Riemann-von Mangoldt law, or target analytic continuation",
            "arithmetic/local data, Euler factors, root numbers, automorphy, or an adelic assembly",
            "Hilbert--Polya operator, Riemann-zero correspondence, A4 natural quantization, or Route-B authorization",
        ],
        "excluded_from_manifest": [
            "C125_RELEASE_MANIFEST.json",
            "code/__pycache__/",
            "paper/main.aux",
            "paper/main.log",
            "paper/main.out",
            "paper/main.fdb_latexmk",
            "paper/main.fls",
            "paper/main.synctex.gz",
        ],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
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
