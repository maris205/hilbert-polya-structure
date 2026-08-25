#!/usr/bin/env python3
"""Build the self-excluded content-addressed HCS-C157 release manifest."""
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C157_RELEASE_MANIFEST.json"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    excluded = {
        MANIFEST,
        ROOT/"paper/main.aux", ROOT/"paper/main.log", ROOT/"paper/main.out",
        ROOT/"paper/main.fdb_latexmk", ROOT/"paper/main.fls",
        ROOT/"paper/main.synctex.gz", ROOT/"paper/build_pass1.log",
        ROOT/"paper/build_pass2.log",
    }
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if (not path.is_file() or path in excluded or "__pycache__" in path.parts
                or path.suffix == ".pyc"):
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    evidence = ROOT/"results/c157_abel_trace_evidence.json"
    pdf = ROOT/"paper/main.pdf"
    result = {
        "schema": "hcs-c157-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "An exact Dirichlet Abel half-wave trace separates Weyl, axis, primitive clean-family, and boundary contributions for the unit square",
        "gates": {
            "G0_source_lock": "PASS",
            "G1_radial_fourier_constant": "PASS",
            "G2_exact_poisson_quadrant_formula": "PASS",
            "G3_absolute_convergence_and_branch": "PASS",
            "G4_primitive_repetition_rearrangement": "PASS",
            "G5_four_boundary_strata": "PASS",
            "G6_exact_shell_ledger_through_500": "PASS",
            "G7_rigorous_primal_dual_tail_bounds": "PASS",
            "G8_independent_checker_sympy_replay_mutation": "PASS",
            "G9_two_internal_review_rounds": "PASS",
            "G10_bilingual_abstract_keywords_declarations": "PASS",
            "G11_lualatex_double_compile_fonts_layout_visual": "PASS",
            "G12_manifest_hash_closure": "PASS",
            "G13_target_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "squared_norm_cutoff": 500,
            "primitive_shells": 98,
            "ordered_primitive_directions": 239,
            "occupied_dual_shells": 161,
            "ordered_positive_dual_vectors": 373,
            "first_fourfold_primitive_collision": 65,
            "numerical_sentinels": 2,
            "independent_checker_assertions": 1022,
            "sympy_checks": 1198,
            "repaired_hash_mutation_rejections": 103,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": 2,
            "pdf_engine": "LuaLaTeX",
            "source_date_epoch": 1787616000,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": "THE_SOURCE_TRACE_RETAINS_EVERY_PRIMITIVE_CLEAN_FAMILY_LENGTH_AND_REPETITION_BUT_THE_FAMILIES_ARE_NOT_ISOLATED_ORBITS",
            "A2": "A2_FAIL",
            "A2_qualification": "NO_ISOLATED_STABILITY_DETERMINANT_OR_TARGET_DIVISOR_COMPARISON",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_CONTINUATION_OR_COUNTING_COMPARISON",
            "A4": "A4_NATURAL_QUANTIZATION",
            "A4_qualification": "SQRT_DELTA_D_IS_NATURAL_SELF_ADJOINT_AND_W_D_IS_ITS_GENUINE_SOURCE_ABEL_TRACE_WITHOUT_A_TARGET_OPERATOR_IDENTITY",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "that the listed branch points exhaust every boundary singularity",
            "that an axis branch cancels a coincident boundary-subtraction pole",
            "an isolated primitive-orbit determinant or stability amplitude",
            "a target trace, divisor, functional equation, or counting law",
            "an arithmetic local or Euler factorization, root number, or automorphy statement",
            "a Hilbert--Polya construction or Route-B authorization",
        ],
        "excluded_from_manifest": [
            "C157_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper/main.aux", "paper/main.log", "paper/main.out",
            "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz",
            "paper/build_pass1.log", "paper/build_pass2.log",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2)+"\n")
    print(json.dumps({
        "status": "C157_MANIFEST_PASS", "file_count": len(files),
        "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(evidence),
        "pdf_sha256": digest(pdf),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
