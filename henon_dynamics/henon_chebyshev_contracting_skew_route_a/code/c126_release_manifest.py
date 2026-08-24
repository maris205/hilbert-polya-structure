#!/usr/bin/env python3
"""Build the content-addressed C126 release ledger."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C126_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def main() -> None:
    excluded = {
        MANIFEST,
        ROOT/"paper/main.aux", ROOT/"paper/main.log", ROOT/"paper/main.out",
        ROOT/"paper/main.fdb_latexmk", ROOT/"paper/main.fls", ROOT/"paper/main.synctex.gz",
    }
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts:
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    evidence = ROOT/"results/c126_chebyshev_skew_evidence.json"
    pdf = ROOT/"paper/main.pdf"
    result = {
        "schema": "hcs-c126-release-v1",
        "status": "COMPLETE_NOT_COMMITTED",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "All-period real orbit, primitive, zeta, and stability laws for a Chebyshev contracting skew product",
        "gates": {
            "G0_source_clock_and_convention_freeze": "PASS",
            "G1_all_period_chebyshev_iterate_theorem": "PASS",
            "G2_complete_distinct_real_fixed_point_and_fiber_lift_theorem": "PASS",
            "G3_mobius_primitive_and_artin_mazur_zeta_theorem": "PASS",
            "G4_all_period_stability_orientation_and_repetition_law": "PASS",
            "G5_two_exact_negative_controls": "PASS",
            "G6_independent_checker_sympy_replay_and_mutation": "PASS",
            "G7_paper_double_isolated_compile_and_font_check": "PASS",
            "G8_manifest_hash_closure": "PASS",
            "G9_target_fredholm_divisor_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "theorem_orbit_cutoff": "none",
            "replay_prefix_period": 12,
            "primitive_prefix_rows": 12,
            "stability_prefix_rows": 12,
            "mutation_rejections": 18,
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
        "progress_over_prior_gate": "all-period complete orbit, primitive, orientation, stability, and repetition laws replace another finite low-period witness",
        "nonclaims": [
            "a prime-to-orbit correspondence or target divisor match",
            "a weighted nuclear transfer operator or Fredholm determinant",
            "a target analytic completion or counting law",
            "arithmetic/local data, Euler factors, root numbers, or automorphy",
            "a Hilbert--Polya operator, Riemann-zero statement, or Route-B authorization",
        ],
        "excluded_from_manifest": [
            "C126_RELEASE_MANIFEST.json", "code/__pycache__/", "paper/main.aux", "paper/main.log",
            "paper/main.out", "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 manifest files, found {len(files)}: {sorted(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    print(json.dumps({
        "manifest_sha256": digest(MANIFEST),
        "file_count": len(files),
        "evidence_sha256": digest(evidence),
        "pdf_sha256": digest(pdf),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
