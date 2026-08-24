#!/usr/bin/env python3
"""Build the content-addressed C114 pre-freeze release ledger."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C114_RELEASE_MANIFEST.json"


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
    evidence = ROOT / "results/c114_jet_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c114-release-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Exact order-four local Koopman jet on a fifteen-dimensional quotient",
        "gates": {
            "G0_polynomial_germ_and_local_algebra_freeze": "PASS",
            "G1_exact_fifteen_by_fifteen_pullback_matrix": "PASS",
            "G2_graded_blocks_trace_determinant_and_characteristic_data": "PASS",
            "G3_independent_checker_and_sympy_crosscheck": "PASS",
            "G4_canonical_replay_and_hostile_mutation_audit": "PASS",
            "G5_paper_double_isolated_compile_and_font_check": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_global_koopman_or_primitive_orbit_owner": "NOT_ESTABLISHED",
            "G8_nuclear_fredholm_or_analytic_tail_theorem": "NOT_ESTABLISHED",
            "G9_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "quotient_dimension": 15,
            "maximum_total_degree": 4,
            "graded_block_count": 5,
            "trace_power_prefix_length": 8,
            "mutation_rejections": 13,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_PARTIAL_CERTIFIED",
            "A1_qualification": "LOCAL_FIXED_POINT_AND_ORDER_FOUR_JET_ONLY",
            "A2": "A2_CERTIFIED_PREFIX",
            "A2_qualification": "FIFTEEN_DIMENSIONAL_FINITE_LOCAL_QUOTIENT_ONLY",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
            "overall": "ROUTE_A_EXPLORATORY",
        },
        "nonclaims": [
            "global orbit classification, Markov partition, or complete primitive-orbit atlas",
            "global Koopman spectrum, invariant Banach space, nuclearity, or Fredholm determinant",
            "analytic continuation, zero-count theorem, or spectral correspondence",
            "arithmetic/local data, Euler factors, root numbers, or automorphy",
            "Hilbert--Polya operator, Riemann-zero correspondence, or Route-B authorization",
        ],
        "excluded_from_manifest": [
            "C114_RELEASE_MANIFEST.json",
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
    print(json.dumps({"manifest_sha256": digest(MANIFEST), "file_count": len(files), "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)}, sort_keys=True))


if __name__ == "__main__":
    main()
