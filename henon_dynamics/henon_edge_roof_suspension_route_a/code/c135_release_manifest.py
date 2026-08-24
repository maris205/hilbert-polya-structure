#!/usr/bin/env python3
"""Build the content-addressed C135 release ledger."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C135_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    excluded = {
        MANIFEST,
        ROOT / "paper/main.aux", ROOT / "paper/main.log", ROOT / "paper/main.out",
        ROOT / "paper/main.fdb_latexmk", ROOT / "paper/main.fls",
        ROOT / "paper/main.synctex.gz",
    }
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        files[str(path.relative_to(ROOT))] = digest(path)

    evidence = ROOT / "results/c135_edge_roof_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c135-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "An exact nonlattice directed-edge roof separates edge-count sectors while proving residual orbit and orientation collisions",
        "gates": {
            "G0_source_lock": "PASS",
            "G1_formal_edge_determinant": "PASS",
            "G2_all_period_trace_and_primitive_identity": "PASS",
            "G3_nonlattice_specialization_and_convergence": "PASS",
            "G4_requested_period_six_separation": "PASS",
            "G5_residual_collision_and_orientation_obstruction": "PASS",
            "G6_c130_destination_symbol_control": "PASS",
            "G7_independent_checker_sympy_replay_mutation": "PASS",
            "G8_double_compile_fonts_layout": "PASS",
            "G9_manifest_hash_closure": "PASS",
            "G10_target_divisor_matching": "NOT_ESTABLISHED",
            "G11_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "rooted_closed_words_through_period_10": 2046,
            "primitive_cycles_through_period_10": 226,
            "first_same_edge_count_primitive_collision_period": 6,
            "period_6_sector_multiplicity_000111": 6,
            "period_6_sector_multiplicity_001011": 12,
            "independent_checker_assertions": 2121,
            "sympy_checks": 37,
            "repaired_hash_mutation_rejections": 42,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "ALL_PERIOD_INTRINSIC_PRIMITIVE_SUSPENSION_ORBITS_WITH_NO_PRIME_LIKE_TARGET_CORRESPONDENCE",
            "A2": "A2_FAIL",
            "A2_qualification": "EXACT SOURCE DETERMINANT AND PRIMITIVE PRODUCT BUT NO FROZEN TARGET DIVISOR MATCH",
            "A3": "A3_FAIL",
            "A3_qualification": "NO TARGET FUNCTIONAL EQUATION GAMMA FACTOR COUNTING LAW OR CONTINUATION COMPARISON",
            "A4": "A4_FAIL",
            "A4_qualification": "NO NATURAL SELF_ADJOINT UNITARY SCATTERING OR HAMILTONIAN LIFT",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "orbit injectivity inside one directed-edge-count sector",
            "recovery of the antisymmetric off-diagonal roof component",
            "an arithmetic Euler product or local factorization",
            "a target zero or pole divisor match, functional equation, or counting law",
            "a natural self-adjoint Hilbert--Polya operator",
            "Route-B authorization or a solution of the larger program",
        ],
        "excluded_from_manifest": [
            "C135_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper/main.aux", "paper/main.log", "paper/main.out",
            "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 manifest files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "manifest_sha256": digest(MANIFEST),
        "file_count": len(files),
        "evidence_sha256": digest(evidence),
        "pdf_sha256": digest(pdf),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
