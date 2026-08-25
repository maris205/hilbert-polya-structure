#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C153 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C153_RELEASE_MANIFEST.json"
SOURCE_COMMIT = "2d4e6211a254ef49d87718569d23466f4c6dcf4c"

EXPECTED_PAYLOADS = {
    "EXPERIMENT_PLAN.md",
    "NARRATIVE_REPORT.md",
    "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md",
    "README.md",
    "RESEARCH_QUESTION.md",
    "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md",
    "code/README.md",
    "code/c153_mutation.py",
    "code/c153_release_manifest.py",
    "code/c153_replay.py",
    "code/c153_sympy_crosscheck.py",
    "code/c153_walsh_escape_checker.py",
    "code/c153_walsh_escape_producer.py",
    "evaluations/route_a/HCS-C153/2026-08-25.yaml",
    "paper/COMPILE_REPORT.md",
    "paper/README.md",
    "paper/main.pdf",
    "paper/main.tex",
    "paper/main_round0_original.pdf",
    "paper/main_round1.pdf",
    "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md",
    "results/RESULTS.md",
    "results/TEST_REPORT.md",
    "results/c153_walsh_escape_evidence.json",
}


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
    }
    files = {}
    for path in sorted(ROOT.rglob("*")):
        if (
            not path.is_file()
            or path in excluded
            or "__pycache__" in path.parts
            or path.suffix == ".pyc"
        ):
            continue
        files[str(path.relative_to(ROOT))] = digest(path)

    if set(files) != EXPECTED_PAYLOADS:
        missing = sorted(EXPECTED_PAYLOADS - set(files))
        unexpected = sorted(set(files) - EXPECTED_PAYLOADS)
        raise AssertionError(
            f"payload ledger mismatch: missing={missing}, unexpected={unexpected}"
        )

    evidence_path = ROOT / "results/c153_walsh_escape_evidence.json"
    pdf_path = ROOT / "paper/main.pdf"
    round2_path = ROOT / "paper/main_round2.pdf"
    evidence = json.loads(evidence_path.read_text())

    assert evidence["schema"] == "hcs-c153-walsh-growing-k-escape-v1"
    assert evidence["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert evidence["source_lock"]["source_commit"] == SOURCE_COMMIT
    assert len(evidence["all_parameter_rank_theorem"]["ledger_rows"]) == 624
    assert len(evidence["macroscopic_escape_theorem"]["finite_ratio_ledger"]) == 192
    assert len(evidence["fixed_period_trace_theorem"]["periods"]) == 20
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert digest(pdf_path) == digest(round2_path)

    result = {
        "schema": "hcs-c153-release-v1",
        "status": "RELEASE_COMPLETE",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_commit": SOURCE_COMMIT,
        "headline": (
            "A growing three-symbol open Walsh gate has an exact saturated "
            "image-rank law, a macroscopic escape exponent, and equality-merged "
            "fixed-period gcd trace clusters"
        ),
        "gates": {
            "G0_source_lock": "PASS",
            "G1_one_qutrit_simple_zero_and_power_rank": "PASS",
            "G2_all_parameter_tensor_normal_form_and_rank": "PASS",
            "G3_macroscopic_escape_rate_including_alpha_zero": "PASS",
            "G4_all_fixed_period_gcd_trace_clusters": "PASS",
            "G5_normalized_trace_limit_and_raw_nonlimit_witness": "PASS",
            "G6_closed_order_and_moved_hole_controls": "PASS",
            "G7_checker_sympy_replay_mutation": "PASS",
            "G8_double_compile_fonts_layout_visual": "PASS",
            "G9_manifest_hash_closure": "PASS",
            "G10_full_secular_or_target_divisor_matching": "NOT_ESTABLISHED",
            "G11_arithmetic_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "exact_rank_rows": 624,
            "macroscopic_ratio_rows": 192,
            "fixed_period_cluster_ledgers": 20,
            "independent_checker_assertions": 6193,
            "sympy_checks": 213,
            "repaired_hash_mutation_rejections": 52,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": 2,
            "evidence_sha256": digest(evidence_path),
            "pdf_sha256": digest(pdf_path),
            "main_tex_sha256": digest(ROOT / "paper/main.tex"),
            "round0_pdf_sha256": digest(ROOT / "paper/main_round0_original.pdf"),
            "round1_pdf_sha256": digest(ROOT / "paper/main_round1.pdf"),
            "round2_pdf_sha256": digest(round2_path),
        },
        "route_a_verdict": {
            "A1": "A1_WEAK",
            "A1_qualification": (
                "INTRINSIC_GROWING_SYSTEM_CLOCK_WITH_EXACT_GCD_TRACE_CLASSES_"
                "BUT_NO_PRIME_LIKE_TARGET_MAP"
            ),
            "A2": "A2_FAIL",
            "A2_qualification": (
                "EXACT_SOURCE_RANKS_AND_FIXED_PERIOD_TRACES_WITHOUT_A_FULL_"
                "SECULAR_OR_TARGET_DIVISOR_COMPARISON"
            ),
            "A3": "A3_FAIL",
            "A3_qualification": (
                "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_GLOBAL_"
                "TARGET_STRUCTURE"
            ),
            "A4": "A4_UNITARY_OR_SCATTERING_CANDIDATE",
            "A4_qualification": (
                "SOURCE_DERIVED_SUBUNITARY_GATES_WITH_A_SAME_CLOCK_CLOSED_"
                "UNITARY_PARENT_BUT_NO_SELF_ADJOINT_OR_TARGET_LIMIT"
            ),
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "convergence of every unnormalized fixed-period trace sequence",
            "a full growing-k secular determinant or resonance limit",
            "a self-adjoint or antiunitary quantization",
            "a target zero, divisor, functional equation, or counting-law match",
            "prime-like information, arithmetic local data, Euler factors, root numbers, or automorphy",
            "a Hilbert--Polya operator or Route-B authorization",
        ],
        "excluded_from_manifest": [
            "C153_RELEASE_MANIFEST.json",
            "code/__pycache__/",
            "*.pyc",
            "paper/main.aux",
            "paper/main.log",
            "paper/main.out",
            "paper/main.fdb_latexmk",
            "paper/main.fls",
            "paper/main.synctex.gz",
        ],
        "files": files,
    }
    MANIFEST.write_text(
        json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    )
    print(
        json.dumps(
            {
                "status": "C153_MANIFEST_PASS",
                "file_count": len(files),
                "manifest_sha256": digest(MANIFEST),
                "evidence_sha256": digest(evidence_path),
                "pdf_sha256": digest(pdf_path),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
