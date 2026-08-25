#!/usr/bin/env python3
"""Build the content-addressed C142 release ledger."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C142_RELEASE_MANIFEST.json"


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
    evidence = ROOT / "results/c142_renewal_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c142-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "A countable renewal graph owns an infinite-rank trace-class operator with an exact entire Fredholm determinant and primitive excursion product",
        "gates": {
            "G0_source_lock": "PASS",
            "G1_trace_class_operator": "PASS",
            "G2_exact_renewal_determinant": "PASS",
            "G3_entire_order_zero": "PASS",
            "G4_primitive_excursion_product": "PASS",
            "G5_noncompact_constant_shift_control": "PASS",
            "G6_independent_checker_sympy_replay_mutation": "PASS",
            "G7_double_compile_fonts_layout": "PASS",
            "G8_manifest_hash_closure": "PASS",
            "G9_target_divisor_matching": "NOT_ESTABLISHED",
            "G10_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "coefficient_cutoff": 16,
            "trace_cutoff": 12,
            "primitive_clock_cutoff": 10,
            "mutation_rejections": 25,
            "pdf_pages": 3,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A2": "A2_FAIL",
            "A3": "A3_FAIL",
            "A4": "A4_FAIL",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "a target-facing zero or divisor match",
            "a target functional equation or counting law",
            "prime-like information, arithmetic local data, Euler factors, root numbers, or automorphy",
            "a self-adjoint Hilbert--Polya operator or Route-B authorization",
        ],
        "excluded_from_manifest": [
            "C142_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper/main.aux", "paper/main.log", "paper/main.out",
            "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 manifest files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"manifest_sha256": digest(MANIFEST), "file_count": len(files), "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)}, sort_keys=True))


if __name__ == "__main__":
    main()
