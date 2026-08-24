#!/usr/bin/env python3
"""Build the content-addressed C119 pre-freeze release ledger."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C119_RELEASE_MANIFEST.json"


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
        if not path.is_file() or path in excluded or "__pycache__" in path.parts:
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    evidence = ROOT / "results/c119_fock_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c119-release-v1",
        "status": "PREFREEZE_COMPLETE_NOT_RELEASED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Trace-class bosonic Fock owner for a strict linear Henon-type contraction",
        "gates": {
            "G0_map_and_fock_space_freeze": "PASS",
            "G1_exact_euclidean_contraction": "PASS",
            "G2_trace_class_and_fredholm_product_theorem": "PASS",
            "G3_trace_coefficient_and_zero_divisor_certificate": "PASS",
            "G4_independent_checker_sympy_replay_and_mutation": "PASS",
            "G5_paper_double_isolated_compile_and_font_check": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_nontrivial_primitive_orbit_atlas": "FAIL",
            "G8_target_divisor_matching": "NOT_ESTABLISHED",
            "G9_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "trace_power_prefix_length": 8,
            "determinant_taylor_degree": 8,
            "zero_divisor_prefix_length": 9,
            "mutation_rejections": 12,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_FAIL",
            "A1_qualification": "CONTRACTION_HAS_ONLY_THE_ORIGIN_AS_A_PERIODIC_POINT",
            "A2": "A2_FAIL",
            "A2_qualification": "FOCK_DETERMINANT_IS_NOT_PRIMITIVE_ORBIT_OWNED_AND_HAS_NO_TARGET_DIVISOR_MATCH",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_GAMMA_COUNTING_OR_CONTINUATION_CHECKS",
            "A4": "A4_FAIL", "overall": "ROUTE_A_EXPLORATORY",
        },
        "nonclaims": [
            "a nontrivial primitive-orbit atlas or orbit-derived determinant",
            "matching of the source-defined Fock zero divisor to any target divisor",
            "arithmetic/local data, Euler factors, root numbers, or automorphy",
            "a self-adjoint Hilbert--Polya operator or Riemann-zero correspondence",
            "Route-B authorization or resolution of the larger program",
        ],
        "excluded_from_manifest": [
            "C119_RELEASE_MANIFEST.json", "code/__pycache__/", "paper/main.aux", "paper/main.log",
            "paper/main.out", "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 26, f"expected 26 manifest files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"manifest_sha256": digest(MANIFEST), "file_count": len(files), "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)}, sort_keys=True))


if __name__ == "__main__":
    main()
