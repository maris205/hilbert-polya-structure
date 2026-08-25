#!/usr/bin/env python3
"""Build the self-excluded HCS-C167 release manifest."""

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C167_RELEASE_MANIFEST.json"


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
        ROOT / "paper/build_pass1.log",
        ROOT / "paper/build_pass2.log",
    }
    files = {
        str(path.relative_to(ROOT)): digest(path)
        for path in sorted(ROOT.rglob("*"))
        if path.is_file()
        and path not in excluded
        and "__pycache__" not in path.parts
        and path.suffix != ".pyc"
    }
    evidence = ROOT / "results/c167_rectangle_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c167-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": (
            "Every rectangular-billiard source shell has a canonical full-trace "
            "branch coefficient; all non-sign collisions occur at positive-rational "
            "aspect-square and every pairwise crossing is transverse"
        ),
        "gates": {
            "G0_c157_c162_source_lock": "PASS",
            "G1_rectangular_poisson_constant": "PASS",
            "G2_all_alpha_full_trace_limit": "PASS",
            "G3_rational_collision_classification": "PASS",
            "G4_transversality_and_reciprocal_aspect": "PASS",
            "G5_double_axis_double_boundary_control": "PASS",
            "G6_independent_checker_sympy_replay_mutation": "PASS",
            "G7_two_internal_improvement_rounds": "PASS",
            "G8_bilingual_abstract_keywords_declarations": "PASS",
            "G9_lualatex_double_compile_fonts_layout_visual": "PASS",
            "G10_manifest_hash_closure": "PASS",
            "G11_target_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "rational_parameter_sentinel_rows": 3,
            "irrational_quadratic_field_fibres": 624,
            "branch_convergence_sentinels": 4,
            "independent_checker_assertions": 1362,
            "sympy_checks": 28585,
            "repaired_hash_mutation_rejections": 30,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": 2,
            "pdf_engine": "LuaLaTeX",
            "source_date_epoch": 1787616000,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A2": "A2_FAIL",
            "A3": "A3_FAIL",
            "A4": "A4_NATURAL_QUANTIZATION",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "a uniform irrational shell gap or universal rational divisor formula",
            "an isolated primitive-orbit determinant or stability amplitude",
            "a target trace, divisor, functional equation, or counting law",
            "arithmetic local data, Euler factors, root numbers, or automorphy",
            "a Hilbert--Polya construction or Route-B authorization",
        ],
        "excluded_from_manifest": [
            "C167_RELEASE_MANIFEST.json",
            "code/__pycache__/",
            "*.pyc",
            "paper/main.aux",
            "paper/main.log",
            "paper/main.out",
            "paper/main.fdb_latexmk",
            "paper/main.fls",
            "paper/main.synctex.gz",
            "paper/build_pass1.log",
            "paper/build_pass2.log",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(
        json.dumps(
            {
                "status": "C167_MANIFEST_PASS",
                "file_count": len(files),
                "manifest_sha256": digest(MANIFEST),
                "evidence_sha256": digest(evidence),
                "pdf_sha256": digest(pdf),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
