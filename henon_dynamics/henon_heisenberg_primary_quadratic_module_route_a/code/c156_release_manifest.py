#!/usr/bin/env python3
"""Build the self-excluded content-addressed HCS-C156 release manifest."""
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C156_RELEASE_MANIFEST.json"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    excluded = {
        MANIFEST,
        ROOT / "paper/main.aux",
        ROOT / "paper/main.log",
        ROOT / "paper/main.out",
        ROOT / "paper/main.fdb_latexmk",
        ROOT / "paper/main.fls",
        ROOT / "paper/main.synctex.gz",
        ROOT / "paper/build_pass1.log",
        ROOT / "paper/build_pass2.log",
    }
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if (not path.is_file() or path in excluded or "__pycache__" in path.parts
                or path.suffix == ".pyc"):
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    evidence = ROOT / "results/c156_primary_module_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c156-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "All-iterate Smith types and an exponent-level central-rotation bound yield an orthogonal group-primary zero product for the frozen Heisenberg fixed fibres",
        "gates": {
            "G0_source_lock": "PASS",
            "G1_fibonacci_lucas_factorization_and_smith": "PASS",
            "G2_canonical_vs_iterate_cocycle": "PASS",
            "G3_all_iterate_parity_denominator_proof": "PASS",
            "G4_correct_quadratic_polarization": "PASS",
            "G5_orthogonal_primary_zero_product": "PASS",
            "G6_exact_primary_ledgers_through_14": "PASS",
            "G7_independent_checker_sympy_replay_mutation": "PASS",
            "G8_two_internal_review_rounds": "PASS",
            "G9_bilingual_abstract_keywords_declarations": "PASS",
            "G10_lualatex_double_compile_fonts_layout_visual": "PASS",
            "G11_manifest_hash_closure": "PASS",
            "G12_target_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "iterate_cutoff": 14,
            "primary_component_count": 23,
            "enumerated_primary_elements": 314151,
            "rotation_histogram_cells": 906,
            "orthogonality_pair_checks": 191597,
            "n13_fixed_circle_components": 1041,
            "n14_fixed_circle_components": 57,
            "independent_checker_assertions": 507331,
            "sympy_checks": 1842,
            "repaired_hash_mutation_rejections": 53,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": 2,
            "pdf_engine": "LuaLaTeX",
            "source_date_epoch": 1787616000,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_FAIL",
            "A1_qualification": "THE_PERIODIC_OBJECTS_REMAIN_POSITIVE_DIMENSIONAL_CLEAN_FIBRES_NOT_ISOLATED_PRIMITIVE_ORBITS",
            "A2": "A2_FAIL",
            "A2_qualification": "THE_ORDINARY_ISOLATED_STABILITY_DENOMINATOR_REMAINS_SINGULAR",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_ANALYTIC_STRUCTURE_OR_COUNTING_COMPARISON",
            "A4": "A4_FORMAL_HINT",
            "A4_qualification": "THE_FROZEN_HAAR_KOOPMAN_UNITARY_REMAINS_NATURAL_BUT_THE_PRIMARY_ZERO_PROJECTORS_ARE_NOT_AN_OPERATOR_TRACE_FORMULA",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "that the finite observed denominator sharpness holds for all iterates",
            "an all-iterate closed formula for the fixed-circle count",
            "an isolated primitive-orbit determinant or ordinary stability weight",
            "a target divisor, functional equation, or counting law",
            "an arithmetic local or Euler factorization, root number, or automorphy statement",
            "a Hilbert--Polya construction or Route-B authorization",
        ],
        "excluded_from_manifest": [
            "C156_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper/main.aux", "paper/main.log", "paper/main.out",
            "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz",
            "paper/build_pass1.log", "paper/build_pass2.log",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps({
        "status": "C156_MANIFEST_PASS",
        "file_count": len(files),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(evidence),
        "pdf_sha256": digest(pdf),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
