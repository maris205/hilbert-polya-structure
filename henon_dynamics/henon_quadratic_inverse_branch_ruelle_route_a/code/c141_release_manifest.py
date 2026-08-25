#!/usr/bin/env python3
"""Build the self-excluded, content-addressed C141 release manifest."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C141_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    excluded = {MANIFEST, ROOT / "paper/main.aux", ROOT / "paper/main.log", ROOT / "paper/main.out", ROOT / "paper/main.fdb_latexmk", ROOT / "paper/main.fls", ROOT / "paper/main.synctex.gz"}
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        files[str(path.relative_to(ROOT))] = {"bytes": path.stat().st_size, "sha256": digest(path)}
    evidence = ROOT / "results/c141_quadratic_ruelle_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c141-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "A quadratic inverse-branch Hardy operator gives an all-period trace formula and a nontrivial m=2 primitive stability product",
        "gates": {
            "G0_source_lock": "PASS", "G1_strict_inverse_branch_geometry": "PASS",
            "G2_trace_class_nuclear_decomposition": "PASS", "G3_all_period_exhaustion": "PASS",
            "G4_weighted_trace_formula": "PASS", "G5_m0_m1_control_ladder": "PASS",
            "G6_m2_exact_prefix_and_primitive_product": "PASS_IN_PROVED_DISK",
            "G7_independent_checker_sympy_replay_mutation": "PASS",
            "G8_double_compile_fonts_layout": "PASS", "G9_manifest_hash_closure": "PASS",
            "G10_target_divisor_matching": "NOT_ESTABLISHED", "G11_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "trace_prefix_length": 6, "fredholm_taylor_degree": 6,
            "rooted_periodic_points_through_6": 126, "primitive_orbits_through_6": 23,
            "independent_checker_assertions": 82, "sympy_checks": 38,
            "repaired_hash_mutation_rejections": 36, "stale_hash_mutation_rejections": 1,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK", "A1_qualification": "ALL_PERIOD_INTRINSIC_PRIMITIVE_ORBITS_WITH_NO_PRIME_LIKE_TARGET_CORRESPONDENCE",
            "A2": "A2_FAIL", "A2_qualification": "EXACT_SOURCE FREDHOLM DETERMINANT BUT NO FROZEN TARGET DIVISOR MATCH",
            "A3": "A3_FAIL", "A3_qualification": "NO TARGET FUNCTIONAL EQUATION GAMMA FACTOR COUNTING LAW OR CONTINUATION COMPARISON",
            "A4": "A4_FAIL", "A4_qualification": "NUCLEAR TRANSFER OPERATOR IS NOT A NATURAL UNITARY OR SELF_ADJOINT QUANTIZATION",
            "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "prime-like target correspondence or target zero census", "target functional equation or divisor match",
            "arithmetic/local data, Euler factors, root numbers, or automorphy",
            "natural unitary, self-adjoint, metaplectic, or Hilbert--Polya operator",
            "raw primitive-product convergence outside |u|<4", "novelty of general Ruelle theory",
        ],
        "excluded_from_manifest": ["C141_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper/main.aux", "paper/main.log", "paper/main.out", "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz"],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"manifest_sha256": digest(MANIFEST), "file_count": len(files), "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)}, sort_keys=True))


if __name__ == "__main__":
    main()
