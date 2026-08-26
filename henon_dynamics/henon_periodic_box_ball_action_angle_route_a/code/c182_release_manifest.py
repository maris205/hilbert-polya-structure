#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C182 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C182_RELEASE_MANIFEST.json"

EXPECTED = {
    "EXPERIMENT_PLAN.md",
    "NARRATIVE_REPORT.md",
    "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md",
    "README.md",
    "RESEARCH_QUESTION.md",
    "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md",
    "code/README.md",
    "code/c182_mutation.py",
    "code/c182_periodic_bbs_checker.py",
    "code/c182_periodic_bbs_producer.py",
    "code/c182_release_manifest.py",
    "code/c182_replay.py",
    "code/c182_sympy_crosscheck.py",
    "evaluations/route_a/HCS-C182/2026-08-26.yaml",
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
    "results/c182_periodic_bbs_evidence.json",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def pages(path: Path) -> int:
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    line = next(row for row in output.splitlines() if row.startswith("Pages:"))
    return int(line.split(":", 1)[1].strip())


def main() -> None:
    forbidden_suffixes = {".aux", ".log", ".out", ".fls", ".fdb_latexmk", ".synctex.gz"}
    actual: set[str] = set()
    for path in ROOT.rglob("*"):
        if not path.is_file() or path == MANIFEST or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        relative = str(path.relative_to(ROOT))
        if any(relative.endswith(suffix) for suffix in forbidden_suffixes):
            raise AssertionError(f"build auxiliary remains on disk: {relative}")
        actual.add(relative)
    if actual != EXPECTED:
        raise AssertionError(
            f"payload closure mismatch; missing={sorted(EXPECTED-actual)}, extra={sorted(actual-EXPECTED)}"
        )

    files = {relative: digest(ROOT / relative) for relative in sorted(actual)}
    evidence_path = ROOT / "results/c182_periodic_bbs_evidence.json"
    evidence = json.loads(evidence_path.read_text())
    pdf = ROOT / "paper/main.pdf"
    rounds = [
        ROOT / "paper/main_round0_original.pdf",
        ROOT / "paper/main_round1.pdf",
        ROOT / "paper/main_round2.pdf",
    ]
    round_hashes = [digest(path) for path in rounds]
    if len(set(round_hashes)) != 3:
        raise AssertionError("paper rounds must be content-distinct")
    if digest(pdf) != round_hashes[2]:
        raise AssertionError("main.pdf must equal Round 2")
    if pages(pdf) != 4 or [pages(path) for path in rounds] != [3, 3, 4]:
        raise AssertionError("unexpected PDF page counts")

    coverage = evidence["finite_regression_sentinels"]["coverage"]
    result = {
        "schema": "hcs-c182-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C182",
        "evaluation_date": "2026-08-26",
        "source_commit": "bbb809ee198bc9ad5f196383baab1e3d9de38e43",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "KTT/Takagi internal-symmetry tori yield all-parameter Smith orders and exact component-to-global fixed-cycle-zeta-Koopman laws, while the intrinsic arithmetic clock gate fails",
        "gates": {
            "G0_source_KTT_Takagi_clock_scope_and_A0_lock": "PASS_WITH_A0_FAIL",
            "G1_all_L_M_content_internal_symmetry_component_theorem": "PASS",
            "G2_sector_multiplicity_and_full_state_cardinality_closure": "PASS",
            "G3_augmented_Smith_exact_order_and_all_T_l_saturation": "PASS",
            "G4_fixed_primitive_zeta_and_finite_Koopman_determinant": "PASS",
            "G5_vacuum_half_filling_and_carrier_boundaries": "PASS",
            "G6_checker_carrier_SymPy_replay_mutation": "PASS",
            "G7_bilingual_three_round_fresh_double_compile_fonts_logs_visual": "PASS",
            "G8_manifest_27_payload_and_disk_hash_closure": "PASS",
            "G9_arithmetic_target_Hilbert_Polya_Route_B": "NOT_CLAIMED",
        },
        "results": {
            **coverage,
            "independent_checker_assertions": 55907,
            "brute_carrier_states": 559,
            "brute_carrier_maps": 108,
            "brute_primitive_cycles": 437,
            "sympy_checks": 38979,
            "repaired_hash_mutation_rejections": 64,
            "stale_hash_mutation_rejections": 1,
            "citation_registry_population": 2,
            "verified_reference_population": 2,
            "pdf_pages": 4,
            "evidence_payload_sha256": evidence["payload_sha256"],
            "evidence_sha256": digest(evidence_path),
            "pdf_sha256": digest(pdf),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": {
            "A0": "A0_FAIL",
            "A0_qualification": "NO_INTRINSIC_RATIONAL_PRIME_OR_PRIME_POWER_ORIGIN_AND_NO_ARITHMETIC_CLOCK",
            "A1": "A1_WEAK",
            "A1_qualification": "COMPLETE_INTRINSIC_PRIMITIVE_CYCLES_WITHOUT_ARITHMETIC_INFORMATION_OR_STABILITY_WEIGHTS",
            "A2": "A2_FAIL",
            "A2_qualification": "EXACT_FINITE_SOURCE_ZETA_AND_KOOPMAN_DETERMINANT_WITH_NO_TARGET_DIVISOR_COMPARISON",
            "A3": "A3_FAIL",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_CONTINUATION_OR_WEIL_COMPRESSION",
            "A4": "A4_NATURAL_QUANTIZATION",
            "A4_qualification": "SAME_CLOCK_FINITE_COUNTING_MEASURE_KOOPMAN_PERMUTATION_UNITARY",
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": evidence["nonclaims"],
        "excluded_from_manifest": [
            "C182_RELEASE_MANIFEST.json",
            "code/__pycache__/",
            "*.pyc",
        ],
        "files": files,
    }
    if len(files) != 27:
        raise AssertionError(f"expected 27 payload files, found {len(files)}")
    MANIFEST.write_text(
        json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    )
    print(
        json.dumps(
            {
                "status": "C182_MANIFEST_PASS",
                "file_count": len(files),
                "manifest_sha256": digest(MANIFEST),
                "evidence_payload_sha256": evidence["payload_sha256"],
                "evidence_sha256": digest(evidence_path),
                "pdf_sha256": digest(pdf),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
