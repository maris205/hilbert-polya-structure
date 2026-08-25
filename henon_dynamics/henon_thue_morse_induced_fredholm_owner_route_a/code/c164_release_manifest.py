#!/usr/bin/env python3
"""Build the content-addressed self-excluded C164 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C164_RELEASE_MANIFEST.json"


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
    evidence = ROOT / "results/c164_fredholm_owner_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c164-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C164",
        "evaluation_date": "2026-08-25",
        "source_commit": "4342893ce5e2516924181744bfacc01c12e4959d",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "The C159 renewal zeta has a branch-resolved induced Fredholm owner while every bounded diagonal Hilbert realization of its uninduced adjacency is noncompact",
        "gates": {
            "G0_source_lock_clock_operator_separation": "PASS",
            "G1_trace_norm_holomorphic_first_return_family": "PASS",
            "G2_all_trace_powers_and_fredholm_identity": "PASS",
            "G3_uninduced_all_weight_compactness_no_go": "PASS",
            "G4_unit_circle_trace_class_extension_obstruction": "PASS",
            "G5_scalar_tautology_exclusion": "PASS",
            "G6_checker_sympy_replay_mutation": "PASS",
            "G7_bilingual_double_compile_fonts_layout_visual": "PASS",
            "G8_manifest_hash_closure": "PASS",
            "G9_target_arithmetic_self_adjoint_route_b": "NOT_CLAIMED",
        },
        "results": {
            "source_bits": 128,
            "formal_degree": 48,
            "trace_power_rows": 6,
            "branch_rows": 32,
            "independent_checker_assertions": 668,
            "sympy_checks": 197,
            "repaired_hash_mutation_rejections": 61,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": 2,
            "pivot_required": False,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "RECURRENT_THUE_MORSE_RENEWAL_DYNAMICS_WITH_A_SOURCE_BRANCH_TRANSFER_OWNER",
            "A2": "A2_FAIL",
            "A2_qualification": "EXACT_SOURCE_FREDHOLM_DETERMINANT_BUT_NO_TARGET_DIVISOR_COMPARISON",
            "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE",
            "A3_qualification": "SOURCE_TRACE_CLASS_DISK_DOMAIN_AND_PROVED_UNIT_CIRCLE_EXTENSION_OBSTRUCTION_ONLY",
            "A4": "A4_FAIL",
            "A4_qualification": "INDUCED_NONUNITARY_TRANSFER_FAMILY_AND_UNINDUCED_SCHATTEN_NO_GO_WITH_NO_SELF_ADJOINT_LIFT",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "that the induced first-return family is the uninduced time-one adjacency",
            "that a scalar determinant identity alone establishes operator ownership",
            "a target divisor, functional equation, counting-law match, or arithmetic local factorization",
            "a unitary, Hamiltonian, natural self-adjoint, or Hilbert--Polya operator",
            "Route-B authorization or a solution of the larger program",
        ],
        "integrity": {
            "hard_gate": "branch-resolved induced owner plus universal uninduced compactness obstruction",
            "hard_gate_status": "PASS",
            "dynamics_pivot_used": False,
            "finite_ledgers_are_proof": False,
            "external_reviewer_simulated": False,
        },
        "excluded_from_manifest": [
            "C164_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper/main.aux", "paper/main.log", "paper/main.out",
            "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C164_MANIFEST_PASS", "file_count": len(files), "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)}, sort_keys=True))


if __name__ == "__main__":
    main()
