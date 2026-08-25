#!/usr/bin/env python3
"""Build the content-addressed self-excluded C163 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C163_RELEASE_MANIFEST.json"


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

    evidence = ROOT / "results/c163_phase_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c163-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C163",
        "evaluation_date": "2026-08-25",
        "source_commit": "63f75cf476711de93e6096ef74ac16969e1127d0",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "The frozen full-cycle open Walsh gate has an unconditional Haar phase law and a joint Gaussian-Haar modulus-phase limit",
        "gates": {
            "G0_source_lock_clock_phase_convention": "PASS",
            "G1_exact_non_torsion_obstruction": "PASS",
            "G2_all_k_fourier_identity": "PASS",
            "G3_haar_phase_limit": "PASS",
            "G4_joint_gaussian_haar_limit": "PASS",
            "G5_torsion_dichotomy_and_moved_hole_control": "PASS",
            "G6_checker_sympy_replay_mutation": "PASS",
            "G7_bilingual_double_compile_fonts_layout_visual": "PASS",
            "G8_manifest_hash_closure": "PASS",
            "G9_self_adjoint_target_arithmetic_route_b": "NOT_CLAIMED",
        },
        "results": {
            "phase_k_max": 32,
            "fourier_m_max": 24,
            "moved_hole_residue_k_max": 32,
            "independent_checker_assertions": 646,
            "sympy_checks": 170,
            "repaired_hash_mutation_rejections": 94,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": 2,
            "pivot_required": False,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "ALL_K_HAAR_PHASE_EQUIDISTRIBUTION_AND_JOINT_GAUSSIAN_HAAR_SCALING",
            "A2": "A2_FAIL",
            "A2_qualification": "SOURCE_SIDE_PHASE_FOURIER_LAW_WITH_NO_TARGET_DIVISOR_COMPARISON",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4": "A4_UNITARY_OR_SCATTERING_CANDIDATE",
            "A4_qualification": "NATURAL_SUBUNITARY_SCATTERING_GATE_WITH_PHASE_RESOLVED_LIMIT_BUT_NO_SELF_ADJOINT_OR_ANTIUNITARY_LIMIT",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "a self-adjoint or antiunitary limiting operator",
            "a target divisor, functional equation, or counting-law match",
            "a prime-like orbit correspondence or arithmetic local data",
            "an arithmetic Euler product, local factor, or root number",
            "automorphy or a Hilbert--Polya construction",
            "Route-B authorization or a solution of the larger program",
        ],
        "integrity": {
            "hard_gate": "unconditional all-k phase theorem for the frozen gate",
            "hard_gate_status": "PASS",
            "dynamics_pivot_used": False,
            "finite_ledgers_are_proof": False,
            "external_reviewer_simulated": False,
        },
        "excluded_from_manifest": [
            "C163_RELEASE_MANIFEST.json",
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
    print(json.dumps({"status": "C163_MANIFEST_PASS", "file_count": len(files), "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)}, sort_keys=True))


if __name__ == "__main__":
    main()
