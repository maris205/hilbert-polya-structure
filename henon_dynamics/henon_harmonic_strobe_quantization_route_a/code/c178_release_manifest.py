#!/usr/bin/env python3
"""Build the content-addressed self-excluded C178 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C178_RELEASE_MANIFEST.json"


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
        if (
            not path.is_file()
            or path in excluded
            or "__pycache__" in path.parts
            or path.suffix == ".pyc"
        ):
            continue
        files[str(path.relative_to(ROOT))] = digest(path)

    evidence = ROOT / "results/c178_harmonic_strobe_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    rounds = [
        ROOT / "paper/main_round0_original.pdf",
        ROOT / "paper/main_round1.pdf",
        ROOT / "paper/main_round2.pdf",
    ]
    round_hashes = [digest(path) for path in rounds]
    assert len(set(round_hashes)) == 3, "paper rounds must be content-distinct"
    assert digest(pdf) == round_hashes[2], "main.pdf must equal round 2"

    result = {
        "schema": "hcs-c178-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C178",
        "evaluation_date": "2026-08-26",
        "source_commit": "100e5f601a0196710d53784bdeef40d2bff89fa8",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "The real-time harmonic strobe has an exact classical resonance transition, complete Gaussian Koopman ledger, and 4*pi-periodic metaplectic quantum lift with retained 2*pi sign, while both unitaries fail ordinary Fredholm ownership",
        "gates": {
            "G0_source_clock_measure_and_A0_lock": "PASS_WITH_A0_FAIL",
            "G1_all_angle_classical_fixed_set_dichotomy": "PASS",
            "G2_irrational_zeta_and_rational_continuum_obstruction": "PASS_WITH_OBSTRUCTION",
            "G3_gaussian_laguerre_angular_spectrum": "PASS",
            "G4_quantum_hermite_metaplectic_cover_egorov_and_reversal": "PASS",
            "G5_noncompact_schatten_fredholm_and_heat_clock_boundary": "PASS_WITH_OBSTRUCTION",
            "G6_checker_sympy_replay_mutation": "PASS",
            "G7_bilingual_three_round_double_compile_fonts_layout_visual": "PASS",
            "G8_manifest_hash_closure": "PASS",
            "G9_arithmetic_target_hilbert_polya_route_b": "NOT_CLAIMED",
        },
        "results": {
            "rational_fixed_rows": 1656,
            "irrational_fixed_rows": 108,
            "laguerre_rows": 209,
            "koopman_phase_rows": 874,
            "quantum_phase_rows": 736,
            "independent_checker_assertions": 26271,
            "sympy_checks": 10465,
            "repaired_hash_mutation_rejections": 64,
            "stale_hash_mutation_rejections": 1,
            "citation_registry_population": 0,
            "reference_registry_population": 0,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": {
            "A0": "A0_FAIL",
            "A0_qualification": "NO_INTRINSIC_ARITHMETIC_OR_PRIME_POWER_ORIGIN",
            "A1": "A1_FAIL",
            "A1_qualification": "ONLY_ONE_PERIODIC_POINT_AT_IRRATIONAL_ANGLES_AND_UNCOUNTABLE_CLEAN_FAMILIES_AT_RATIONAL_ANGLES",
            "A2": "A2_FAIL",
            "A2_qualification": "IRRATIONAL_SOURCE_ZETA_IS_ELEMENTARY_AND_RATIONAL_ANGLES_HAVE_NO_CLASSICAL_ARTIN_MAZUR_SERIES",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_DIVISOR_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_WEIL_COMPRESSION",
            "A4": "A4_NATURAL_QUANTIZATION",
            "A4_qualification": "NATURAL_REAL_TIME_METAPLECTIC_OSCILLATOR_PROPAGATOR_WITH_RETAINED_2PI_SIGN_EXACT_EGOROV_AND_TIME_REVERSAL",
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "finite fixed counts at rational resonant iterates",
            "ordinary Fredholm determinants for the Gaussian Koopman or quantum oscillator unitary",
            "heat or Wick regularization as the physical strobe clock",
            "a single-valued quantum unitary family on the classical 2*pi time quotient",
            "a prime correspondence, target divisor, functional equation, or counting law",
            "arithmetic local data, Euler factors, root numbers, automorphy, or Hilbert--Polya",
            "Route-B authorization, novelty priority, external peer review, or an acceptance score",
        ],
        "excluded_from_manifest": [
            "C178_RELEASE_MANIFEST.json",
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
    MANIFEST.write_text(
        json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    )
    print(
        json.dumps(
            {
                "status": "C178_MANIFEST_PASS",
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
