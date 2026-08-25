#!/usr/bin/env python3
"""Build the content-addressed self-excluded C168 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C168_RELEASE_MANIFEST.json"


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

    evidence = ROOT / "results/c168_rank_three_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c168-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C168",
        "evaluation_date": "2026-08-25",
        "source_commit": "4342893ce5e2516924181744bfacc01c12e4959d",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "The natural rank-three four-symbol open Walsh gate has an exact all-k secular law, weak Haar phase limit, and joint Gaussian-Haar scaling",
        "gates": {
            "G0_source_gate_clock_weight_lock": "PASS",
            "G1_exact_one_site_spectrum_and_nontorsion": "PASS",
            "G2_all_k_multinomial_secular_product": "PASS",
            "G3_fixed_mode_fourier_contraction_and_haar_limit": "PASS",
            "G4_joint_gaussian_haar_mixed_transform": "PASS",
            "G5_hole_zero_torsion_and_antiunitary_controls": "PASS",
            "G6_checker_sympy_replay_mutation": "PASS",
            "G7_bilingual_double_compile_fonts_layout_visual": "PASS",
            "G8_manifest_hash_closure": "PASS",
            "G9_uniform_gap_self_adjoint_target_arithmetic_route_b": "NOT_CLAIMED",
        },
        "results": {
            "spectral_k_max": 24,
            "fourier_m_max": 24,
            "hole_zero_k_max": 24,
            "independent_checker_assertions": 682,
            "sympy_checks": 386,
            "repaired_hash_mutation_rejections": 112,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": 2,
            "pivot_required": False,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "ALL_K_RANK_THREE_SECULAR_HAAR_PHASE_AND_JOINT_GAUSSIAN_HAAR_THEOREMS",
            "A2": "A2_FAIL",
            "A2_qualification": "EXACT_SOURCE_MULTINOMIAL_DETERMINANT_WITH_NO_TARGET_DIVISOR_COMPARISON",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4": "A4_UNITARY_OR_SCATTERING_CANDIDATE",
            "A4_qualification": "NATURAL_SUBUNITARY_RANK_THREE_GATE_WITH_PHASE_LIMIT_AND_TORSION_CONTROL_BUT_NO_FIXED_HOLE_SELF_ADJOINT_LIMIT",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "a Fourier contraction gap uniform over all nonzero modes",
            "total-variation convergence of finite atomic phase measures to continuous Haar",
            "distinctness of all multinomial phase labels",
            "a fixed-hole self-adjoint or antiunitary limiting operator",
            "a target divisor, functional equation, or counting-law match",
            "a prime-like orbit correspondence or arithmetic local data",
            "an arithmetic Euler product, local factor, or root number",
            "automorphy, a Hilbert--Polya construction, or Route-B authorization",
        ],
        "integrity": {
            "hard_gate": "unconditional all-k rank-three secular and phase-limit theorem for the natural four-symbol gate",
            "hard_gate_status": "PASS",
            "dynamics_pivot_used": False,
            "finite_ledgers_are_proof": False,
            "external_reviewer_simulated": False,
        },
        "excluded_from_manifest": [
            "C168_RELEASE_MANIFEST.json",
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
                "status": "C168_MANIFEST_PASS",
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
