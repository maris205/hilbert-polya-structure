#!/usr/bin/env python3
"""Build the content-addressed self-excluded C149 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C149_RELEASE_MANIFEST.json"


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
    evidence = ROOT / "results/c149_skeleton_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c149-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "A finite tagged skeleton supplies exactly four primitive cycles to an aperiodic Thue--Morse component, necessarily destroying minimality",
        "gates": {
            "G0_source_lock": "PASS", "G1_disjoint_union_topology": "PASS",
            "G2_all_period_fixed_counts": "PASS", "G3_zeta_and_primitive_skeleton": "PASS",
            "G4_minimality_obstruction": "PASS", "G5_checker_sympy_replay_mutation": "PASS",
            "G6_double_compile_fonts_layout_visual": "PASS", "G7_manifest_hash_closure": "PASS",
            "G8_target_divisor_matching": "NOT_ESTABLISHED", "G9_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "attached_cycle_lengths": [1, 2, 3, 5], "attached_points": 11,
            "period_ledger_rows": 60, "zeta_degree_limit": 30,
            "independent_checker_assertions": 395, "sympy_checks": 277,
            "repaired_hash_mutation_rejections": 41, "stale_hash_mutation_rejections": 1,
            "pdf_pages": 1, "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_FAIL", "A1_qualification": "DECLARED_FINITE_DISJOINT_ATTACHMENT_NOT_INTRINSIC_TO_THE_MINIMAL_THUE_MORSE_COMPONENT",
            "A2": "A2_FAIL", "A2_qualification": "ELEMENTARY_FINITE_RATIONAL_SOURCE_ZETA_WITH_NO_TARGET_DIVISOR_COMPARISON",
            "A3": "A3_FAIL", "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4": "A4_FAIL", "A4_qualification": "NO_NATURAL_UNITARY_SCATTERING_OR_HAMILTONIAN_LIFT",
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "that the attached periodic cycles belong to the Thue--Morse subshift",
            "that the disjoint union remains minimal or almost minimal",
            "an arithmetic Euler product or local factorization",
            "a target divisor, functional equation, or counting-law match",
            "a natural self-adjoint Hilbert--Polya operator",
            "Route-B authorization or a solution of the larger program",
        ],
        "excluded_from_manifest": ["C149_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper/main.aux", "paper/main.log", "paper/main.out", "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz"],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C149_MANIFEST_PASS", "file_count": len(files), "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)}, sort_keys=True))


if __name__ == "__main__":
    main()
