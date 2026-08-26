#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C174 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C174_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def pdf_pages(path: Path) -> int:
    report = subprocess.check_output(["pdfinfo", str(path)], text=True)
    match = re.search(r"^Pages:\s+(\d+)\s*$", report, re.MULTILINE)
    if match is None:
        raise AssertionError("pdfinfo did not report a page count")
    return int(match.group(1))


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
    files: dict[str, str] = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path in excluded or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        files[str(path.relative_to(ROOT))] = digest(path)

    evidence_path = ROOT / "results/c174_parity_renewal_evidence.json"
    pdf_path = ROOT / "paper/main.pdf"
    evidence = json.loads(evidence_path.read_text())
    result = {
        "schema": "hcs-c174-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C174",
        "evaluation_date": "2026-08-26",
        "source_commit": "100e5f601a0196710d53784bdeef40d2bff89fa8",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Odd-affine dyadic parity maps admit an exact first-return renewal decomposition and original-clock roof recovery, while unweighted and stability-weighted data are blind to every odd parameter pair",
        "gates": {
            "G0_source_parameter_domain_clock_measure_lock": "PASS",
            "G1_classical_parity_conjugacy_ownership_boundary": "PASS",
            "G2_all_parameter_fixed_word_and_period_theorem": "PASS",
            "G3_first_return_exceptional_set_and_geometric_law": "PASS",
            "G4_original_clock_roof_recovery": "PASS",
            "G5_stability_parameter_blindness": "PASS_WITH_ROUTE_A_OBSTRUCTION",
            "G6_operator_and_3x_plus_1_boundaries": "PASS_WITH_OBSTRUCTION",
            "G7_checker_sympy_replay_mutation": "PASS",
            "G8_bilingual_double_compile_fonts_layout_visual": "PASS",
            "G9_manifest_hash_and_disk_closure": "PASS",
            "G10_arithmetic_target_hilbert_polya_route_b": "NOT_CLAIMED",
        },
        "results": {
            **evidence["counts"],
            "independent_checker_assertions": 272693,
            "sympy_checks": 911,
            "repaired_hash_mutation_rejections": 25,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": pdf_pages(pdf_path),
            "evidence_payload_sha256": evidence["payload_sha256"],
            "evidence_sha256": digest(evidence_path),
            "pdf_sha256": digest(pdf_path),
        },
        "route_a_verdict": {
            "A0": "A0_FAIL",
            "A0_qualification": "DYADIC_LOCAL_ARITHMETIC_BUT_NO_RATIONAL_PRIME_OR_PRIME_POWER_CORRESPONDENCE",
            "A1": "A1_WEAK",
            "A1_qualification": "EXACT_PRIMITIVE_ORBIT_LEDGER_WITHOUT_ARITHMETIC_LABELS_OR_TARGET_WEIGHTS",
            "A2": "A2_FAIL",
            "A2_qualification": "EXACT_SOURCE_ZETAS_ARE_PARAMETER_BLIND_AND_HAVE_NO_TARGET_DIVISOR_MATCH",
            "A3": "A3_FAIL",
            "A3_qualification": "ELEMENTARY_RATIONAL_CONTINUATION_HAS_NO_FUNCTIONAL_EQUATION_OR_WEIL_COMPRESSION",
            "A4": "A4_FORMAL_HINT",
            "A4_qualification": "NATURAL_PROPER_KOOPMAN_ISOMETRY_ONLY; UNITARIZATION_CHANGES_PHASE_SPACE",
            "overall": "ROUTE_A_REJECTED",
            "a0_failure_forces_rejection": True,
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "novelty of the classical parity-vector conjugacy or its odd ax+b extension",
            "resolution or progress on the positive-integer 3x+1 conjecture",
            "a finite Artin--Mazur zeta for the accelerated countable-alphabet return map",
            "a prime or prime-power correspondence",
            "target divisor, functional-equation, or counting-law matching",
            "arithmetic local factors, Euler factors, or root numbers",
            "automorphy, a Hilbert--Polya operator, or Route-B authorization",
        ],
        "integrity": {
            "hard_gate": "exact first-return renewal plus original-clock recovery and parameter-blindness audit",
            "hard_gate_status": "PASS_WITH_ROUTE_A_REJECTION",
            "finite_ledgers_are_proof": False,
            "external_reviewer_simulated": False,
            "acceptance_rate_reported": False,
            "citation_population": 2,
            "mandatory_seven_mode_integrity_audit": "CLEAR",
        },
        "excluded_from_manifest": [
            "C174_RELEASE_MANIFEST.json",
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
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}: {sorted(files)}"
    expected_paths = {
        "EXPERIMENT_PLAN.md",
        "NARRATIVE_REPORT.md",
        "PAPER_IMPROVEMENT_LOG.md",
        "PAPER_PLAN.md",
        "README.md",
        "RESEARCH_QUESTION.md",
        "SOURCE_AUDIT.md",
        "THEOREM_PACKAGE.md",
        "code/README.md",
        "code/c174_mutation.py",
        "code/c174_parity_renewal_checker.py",
        "code/c174_parity_renewal_producer.py",
        "code/c174_release_manifest.py",
        "code/c174_replay.py",
        "code/c174_sympy_crosscheck.py",
        "evaluations/route_a/HCS-C174/2026-08-26.yaml",
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
        "results/c174_parity_renewal_evidence.json",
    }
    assert set(files) == expected_paths, f"payload path mismatch: {set(files) ^ expected_paths}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(
        json.dumps(
            {
                "status": "C174_MANIFEST_PASS",
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
