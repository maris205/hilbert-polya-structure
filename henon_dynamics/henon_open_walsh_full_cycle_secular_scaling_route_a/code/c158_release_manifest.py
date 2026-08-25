#!/usr/bin/env python3
"""Build the content-addressed self-excluded C158 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C158_RELEASE_MANIFEST.json"


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

    evidence = ROOT / "results/c158_full_cycle_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c158-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C158",
        "evaluation_date": "2026-08-25",
        "source_commit": "506dead810d67fa58fa7c42b2d9a09bfae161059",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": (
            "The full-cycle open Walsh propagator has an exact tensor secular "
            "factorization and a binomial-to-Gaussian surviving log-modulus law"
        ),
        "gates": {
            "G0_source_lock_and_clock": "PASS",
            "G1_full_cycle_tensor_identity": "PASS",
            "G2_complete_secular_factorization": "PASS",
            "G3_log_modulus_concentration_and_clt": "PASS",
            "G4_controls_and_scope_boundary": "PASS",
            "G5_checker_sympy_replay_mutation": "PASS",
            "G6_bilingual_double_compile_fonts_layout_visual": "PASS",
            "G7_manifest_hash_closure": "PASS",
            "G8_phase_or_self_adjoint_limit": "NOT_ESTABLISHED",
            "G9_target_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "field_polynomial_k_max": 5,
            "direct_kronecker_k_max": 3,
            "binomial_k_max": 24,
            "concentration_sentinel_rows": 4,
            "independent_checker_assertions": 439,
            "sympy_checks": 62,
            "repaired_hash_mutation_rejections": 85,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": (
                "ALL_K_FULL_CYCLE_TENSOR_SECULAR_FACTORIZATION_AND_"
                "BINOMIAL_GAUSSIAN_LOG_MODULUS_SCALING"
            ),
            "A2": "A2_FAIL",
            "A2_qualification": (
                "SOURCE_SIDE_SURVIVING_SPECTRAL_MEASURE_WITH_NO_TARGET_"
                "DIVISOR_COMPARISON"
            ),
            "A3": "A3_FAIL",
            "A3_qualification": (
                "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_"
                "CONTINUATION_COMPARISON"
            ),
            "A4": "A4_UNITARY_OR_SCATTERING_CANDIDATE",
            "A4_qualification": (
                "NATURAL_SUBUNITARY_SCATTERING_GATE_BUT_NO_PHASE_"
                "SELF_ADJOINT_OR_ANTIUNITARY_LIMIT"
            ),
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "a limiting phase law or inverse-secular-zero convention transfer",
            "a self-adjoint or antiunitary limiting operator",
            "a target divisor, functional equation, or counting-law match",
            "an arithmetic Euler product, local factor, or root number",
            "automorphy or a Hilbert--Polya construction",
            "Route-B authorization or a solution of the larger program",
        ],
        "excluded_from_manifest": [
            "C158_RELEASE_MANIFEST.json",
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
                "status": "C158_MANIFEST_PASS",
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
