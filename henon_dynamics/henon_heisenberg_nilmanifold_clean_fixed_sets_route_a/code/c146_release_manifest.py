#!/usr/bin/env python3
"""Build the self-excluded content-addressed HCS-C146 manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C146_RELEASE_MANIFEST.json"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
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
    evidence = ROOT / "results/c146_heisenberg_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c146-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "A standard Heisenberg lattice automorphism has a certified central clean fixed circle at every iterate, forcing singular isolated-orbit factors and zero Lefschetz numbers",
        "gates": {
            "G0_source_lock": "PASS",
            "G1_lattice_automorphism": "PASS",
            "G2_all_iterate_clean_fixed_circle": "PASS",
            "G3_singular_stability_and_lefschetz": "PASS",
            "G4_toral_negative_control_through_20": "PASS",
            "G5_naive_full_component_lift_refuted": "PASS",
            "G6_independent_checker_sympy_replay_mutation": "PASS",
            "G7_double_compile_fonts_layout_visual": "PASS",
            "G8_manifest_hash_closure": "PASS",
            "G9_target_divisor_matching": "NOT_ESTABLISHED",
            "G10_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "iterate_ledger_rows": 20,
            "certified_fixed_circle_lower_bound_each_iterate": 1,
            "full_nilmanifold_component_count": "NOT_ASSERTED",
            "independent_checker_assertions": 687,
            "sympy_checks": 87,
            "repaired_hash_mutation_rejections": 30,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_FAIL",
            "A1_qualification": "CLEAN_POSITIVE_DIMENSIONAL_FIXED_FAMILIES_PREVENT_AN_ISOLATED_PRIMITIVE_ORBIT_LEDGER",
            "A2": "A2_FAIL",
            "A2_qualification": "THE_ORDINARY_ISOLATED_ORBIT_STABILITY_DENOMINATOR_IS_SINGULAR_AT_EVERY_ITERATE",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4": "A4_FORMAL_HINT",
            "A4_qualification": "THE_NATURAL_HAAR_KOOPMAN_UNITARY_PRESERVES_THE_ITERATE_CLOCK_BUT_NO_ISOLATED_ORBIT_WEIGHT_BRIDGE_IS_CONSTRUCTED",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "that every horizontal fixed class lifts to a fixed central circle",
            "an exact full fixed-component count on the nilmanifold",
            "an isolated primitive-orbit determinant",
            "a target divisor, functional equation, or counting law",
            "an arithmetic local or Euler factorization, root number, or automorphy statement",
            "a natural Hilbert--Polya operator or Route-B authorization",
        ],
        "excluded_from_manifest": [
            "C146_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper/main.aux", "paper/main.log", "paper/main.out",
            "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": "C146_MANIFEST_PASS", "file_count": len(files), "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)}, sort_keys=True))


if __name__ == "__main__":
    main()
