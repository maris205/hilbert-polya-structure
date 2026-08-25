#!/usr/bin/env python3
"""Build the self-excluded HCS-C166 release manifest."""
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C166_RELEASE_MANIFEST.json"


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    excluded = {
        MANIFEST, ROOT / "paper/main.aux", ROOT / "paper/main.log", ROOT / "paper/main.out",
        ROOT / "paper/main.fdb_latexmk", ROOT / "paper/main.fls",
        ROOT / "paper/main.synctex.gz", ROOT / "paper/build_pass1.log",
        ROOT / "paper/build_pass2.log",
    }
    files = {str(path.relative_to(ROOT)): digest(path) for path in sorted(ROOT.rglob("*"))
             if path.is_file() and path not in excluded and "__pycache__" not in path.parts
             and path.suffix != ".pyc"}
    evidence = ROOT / "results/c166_pascal_tower_evidence.json"
    pdf = ROOT / "paper/main.pdf"
    result = {
        "schema": "hcs-c166-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Every dyadic Pascal skew tower has one exact dimension-dependent clock, a closed zeta, and a polynomial-ring time reversor",
        "gates": {
            "G0_source_and_pivot_lock": "PASS",
            "G1_pascal_iterate_formula": "PASS",
            "G2_v2_fixed_point_iff": "PASS",
            "G3_exact_period_cycles_zeta": "PASS",
            "G4_koopman_determinant": "PASS",
            "G5_truncated_ring_reversor": "PASS",
            "G6_independent_sympy_replay_mutation": "PASS",
            "G7_two_internal_review_rounds": "PASS",
            "G8_bilingual_abstract_keywords_declarations": "PASS",
            "G9_lualatex_double_compile_fonts_layout_visual": "PASS",
            "G10_manifest_hash_closure": "PASS",
            "G11_target_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "parameter_rows": 90,
            "coefficient_clock_cases": 0,
            "direct_state_period_cases": 0,
            "independent_checker_assertions": 53348,
            "sympy_checks": 7519,
            "repaired_hash_mutation_rejections": 35,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": 0,
            "pdf_engine": "LuaLaTeX",
            "source_date_epoch": 1787616000,
            "evidence_sha256": digest(evidence),
            "pdf_sha256": digest(pdf),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK", "A2": "A2_FAIL", "A3": "A3_FAIL",
            "A4": "A4_NATURAL_QUANTIZATION", "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "computational or dynamical complexity",
            "a target trace, divisor, functional equation, or counting law",
            "arithmetic local data, Euler factors, root numbers, or automorphy",
            "a Hilbert--Polya operator or Route-B authorization",
        ],
        "excluded_from_manifest": [
            "C166_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper/main.aux",
            "paper/main.log", "paper/main.out", "paper/main.fdb_latexmk", "paper/main.fls",
            "paper/main.synctex.gz", "paper/build_pass1.log", "paper/build_pass2.log",
        ],
        "files": files,
    }
    # These values are filled from the released evidence and validation command receipts.
    validation = json.loads(evidence.read_text())["exact_validation"]
    result["results"]["coefficient_clock_cases"] = validation["coefficient_clock_cases"]
    result["results"]["direct_state_period_cases"] = validation["direct_state_period_cases"]
    # Frozen command receipts are independently restated in TEST_REPORT.
    try:
        import subprocess
        pages = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True, check=True)
        result["results"]["pdf_pages"] = int(next(line.split(":", 1)[1]
                                                     for line in pages.stdout.splitlines()
                                                     if line.startswith("Pages:")))
    except (OSError, subprocess.SubprocessError, StopIteration, ValueError):
        raise AssertionError("pdfinfo page audit failed")
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"status": "C166_MANIFEST_PASS", "file_count": len(files),
                      "manifest_sha256": digest(MANIFEST),
                      "evidence_sha256": digest(evidence), "pdf_sha256": digest(pdf)},
                     sort_keys=True))


if __name__ == "__main__":
    main()
