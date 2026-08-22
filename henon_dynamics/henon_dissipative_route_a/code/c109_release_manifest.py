#!/usr/bin/env python3
"""Create the content-addressed C109 pre-freeze release ledger."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "C109_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    excluded = {
        MANIFEST,
        PROJECT / "paper/main.aux",
        PROJECT / "paper/main.log",
        PROJECT / "paper/main.out",
        PROJECT / "paper/main.fdb_latexmk",
        PROJECT / "paper/main.fls",
        PROJECT / "paper/main.synctex.gz",
    }
    files: dict[str, str] = {}
    for path in sorted(PROJECT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts:
            continue
        files[str(path.relative_to(PROJECT))] = digest(path)

    evidence = PROJECT / "results/c109_dissipative_evidence.json"
    pdf = PROJECT / "paper/main.pdf"
    result = {
        "schema": "hcs-c109-release-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Exact dissipative Hénon low-period cycles and a finite weighted transfer witness",
        "gates": {
            "G0_model_and_dissipation_parameter_freeze": "PASS",
            "G1_fixed_and_primitive_period_two_exact_elimination": "PASS",
            "G2_jacobian_weight_and_finite_transfer_prefix": "PASS",
            "G3_independent_checker_and_sympy_crosscheck": "PASS",
            "G4_replay_and_hostile_mutation_audit": "PASS",
            "G5_paper_double_isolated_compile_and_font_check": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_complete_real_coding_or_orbit_atlas": "NOT_ESTABLISHED",
            "G8_source_native_fredholm_operator_owner": "NOT_ESTABLISHED",
            "G9_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "fixed_point_count": 2,
            "primitive_period_two_orbit_count": 1,
            "witness_state_count": 4,
            "trace_max_n": 6,
            "mutation_rejections": 8,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_PARTIAL_CERTIFIED",
            "A1_qualification": "EXACT_FIXED_AND_PRIMITIVE_TWO_CYCLE_WITNESSES_ONLY",
            "A2": "A2_CERTIFIED_PREFIX",
            "A2_qualification": "FOUR_STATE_DISCRETE_WEIGHTED_CYCLE_GRAPH_ONLY",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
            "overall": "ROUTE_A_EXPLORATORY",
        },
        "nonclaims": [
            "complete real primitive-orbit atlas, Markov partition, or global coding",
            "Fredholm determinant, nuclearity, analytic continuation, or zero-count theorem",
            "arithmetic/local data, Euler factors, root numbers, automorphy",
            "Hilbert--Polya operator, Riemann-zero correspondence, or Route-B authorization",
        ],
        "excluded_from_manifest": [
            "C109_RELEASE_MANIFEST.json",
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
