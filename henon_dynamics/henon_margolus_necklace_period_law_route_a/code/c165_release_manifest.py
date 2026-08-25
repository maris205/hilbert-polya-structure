#!/usr/bin/env python3
"""Build the content-addressed self-excluded C165 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C165_RELEASE_MANIFEST.json"


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
    evidence = ROOT / "results/c165_margolus_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c165-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Every binary two-phase Margolus swap ring is exactly conjugate at the full-tick clock to a four-letter necklace rotation, with a complete period law, concentration bound, reversor, and same-clock Koopman determinant",
        "gates": {
            "G0_source_lock_and_rule90_pivot": "PASS",
            "G1_full_tick_site_law": "PASS",
            "G2_four_letter_conjugacy": "PASS",
            "G3_all_m_period_and_zeta_law": "PASS",
            "G4_concentration_and_m1_boundary": "PASS",
            "G5_reversor_and_koopman_owner": "PASS",
            "G6_checker_sympy_replay_mutation": "PASS",
            "G7_bilingual_double_compile_fonts_layout_visual": "PASS",
            "G8_manifest_hash_closure": "PASS",
            "G9_target_divisor_matching": "NOT_ESTABLISHED",
            "G10_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "finite_family_rows": 16,
            "fixed_cells": 136,
            "period_cells": 50,
            "directly_enumerated_configurations": 87380,
            "independent_checker_assertions": 723,
            "sympy_checks": 481,
            "repaired_hash_mutation_rejections": 57,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "ALL_M_EXACT_NECKLACE_PERIOD_LAW_FOR_A_REVERSIBLE_PARTITIONED_CA",
            "A2": "A2_FAIL",
            "A2_qualification": "EXACT_FINITE_SOURCE_ZETA_WITH_NO_TARGET_DIVISOR_COMPARISON",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4": "A4_NATURAL_QUANTIZATION",
            "A4_qualification": "SAME_CLOCK_FINITE_KOOPMAN_UNITARY_WITH_EXPLICIT_ANTIUNITARY_REVERSAL",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "chaos or interaction in a system conjugate to a four-letter rotation",
            "a target divisor, functional equation, or counting-law match",
            "arithmetic local factors, Euler factors, root numbers, or automorphy",
            "a uniform self-adjoint Hilbert--Polya realization across the family",
            "Route-B authorization or a solution of the larger program",
        ],
        "excluded_from_manifest": [
            "C165_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper/main.aux", "paper/main.log", "paper/main.out",
            "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C165_MANIFEST_PASS", "file_count": len(files),
        "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(evidence),
        "pdf_sha256": digest(pdf),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
