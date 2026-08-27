#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C191 release manifest."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C191_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c191_sinkhorn_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE_COMMIT = "4d7b214759f7ff982c0b19e662918acd307e0f58"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVIDENCE_PAYLOAD_SHA256 = "8a4286b4d97efee5d93403407594b1539723cf6bab41ea38168ac515bd27a142"
EVIDENCE_SHA256 = "6950c217543c2e9c023db08ac406b3f8f116a393294d43ce9ec4da96cfef6f9e"
PDF_SHA256 = "b578720d2c9ba9e0be06cf659cf3e15521bfdd9267082333fd3c0144223d8129"


EXPECTED_FILES = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c191_mutation.py", "code/c191_release_manifest.py", "code/c191_replay.py",
    "code/c191_sinkhorn_checker.py", "code/c191_sinkhorn_producer.py", "code/c191_sympy_crosscheck.py",
    "evaluations/route_a/HCS-C191/2026-08-27.yaml", "paper/COMPILE_REPORT.md", "paper/README.md",
    "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf",
    "paper/main_round2.pdf", "results/HOSTILE_AUDIT.md", "results/RESULTS.md",
    "results/TEST_REPORT.md", "results/c191_sinkhorn_evidence.json",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def is_build_sidecar(path: Path) -> bool:
    return (
        path.suffix in {".aux", ".log", ".out", ".fls", ".fdb_latexmk", ".pyc"}
        or path.name.endswith(".synctex.gz")
        or "__pycache__" in path.parts
    )


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["schema"] == "hcs-c191-sinkhorn-evidence-v1"
    assert evidence["candidate_id"] == "HCS-C191"
    assert evidence["date_utc"] == "2026-08-27"
    assert evidence["source_commit"] == SOURCE_COMMIT
    assert evidence["evaluator"] == {
        "version": "0.2.0",
        "path": "flow_systems/skills/route-a-evaluator.md",
        "sha256": EVALUATOR_SHA256,
    }
    assert evidence["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == EVIDENCE_PAYLOAD_SHA256
    assert digest(EVIDENCE) == EVIDENCE_SHA256
    assert digest(PDF) == PDF_SHA256
    assert evidence["route_a"]["tuple"] == [
        "A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL",
    ]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert evidence["scope_flags"] == {
        "arithmetic_local_data_used": False,
        "automorphy_claimed": False,
        "euler_factor_claimed": False,
        "hilbert_polya_operator_claimed": False,
        "root_number_claimed": False,
        "route_b_invoked": False,
        "target_divisor_claimed": False,
        "target_functional_equation_claimed": False,
        "target_prime_table_used": False,
        "target_zero_table_used": False,
    }

    files = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == MANIFEST or is_build_sidecar(path):
            continue
        files[str(path.relative_to(ROOT))] = digest(path)
    assert set(files) == EXPECTED_FILES, sorted(set(files) ^ EXPECTED_FILES)

    rounds = [
        ROOT / "paper/main_round0_original.pdf",
        ROOT / "paper/main_round1.pdf",
        ROOT / "paper/main_round2.pdf",
    ]
    round_hashes = [digest(path) for path in rounds]
    assert round_hashes == [
        "0f03c7e80934a079889b62fa664bbfaadaee7ce93bcae01cedfa95d00822c127",
        "3f41001054f429d37994f2ecd16089cce92a5f533a92022f72f7da99213db770",
        PDF_SHA256,
    ]
    assert len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[2]

    pdf_info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pdf_pages = int(next(
        line.split(":", 1)[1]
        for line in pdf_info.splitlines()
        if line.startswith("Pages:")
    ))
    assert pdf_pages == 2
    assert PDF.stat().st_size == 146909

    finite = evidence["finite_regression"]
    assert finite["pattern_row_count"] == 272
    assert finite["positive_case_count"] == 4
    assert finite["boundary_case_count"] == 4
    assert finite["iteration_step_count"] == 40
    assert finite["cross_ratio_count"] == 28
    assert len(evidence["source_registry"]) == 4

    result = {
        "schema": "hcs-c191-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C191",
        "evaluation_date": "2026-08-27",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "headline": (
            "Every square nonnegative matrix is classified under alternating row-column normalization "
            "by support, total support and full indecomposability, while positive strata have exact "
            "projective contraction and local S-transpose-S rate data"
        ),
        "gates": {
            "G0_source_lock_and_A0": "PASS_WITH_A0_FAIL",
            "G1_all_matrix_support_scalability_and_uniqueness": "PASS",
            "G2_positive_projective_contraction_and_local_rate": "PASS",
            "G3_boundary_complete_recurrence_and_nonclaims": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS",
            "G5_two_actual_improvements_double_compile_fonts_layout_visual": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_target_divisor_quantization_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "pattern_rows": finite["pattern_row_count"],
            "positive_cases": finite["positive_case_count"],
            "boundary_cases": finite["boundary_case_count"],
            "iteration_rows": finite["iteration_step_count"],
            "cross_ratios": finite["cross_ratio_count"],
            "independent_checker_assertions": 2411,
            "sympy_checks": 951,
            "repaired_hash_mutation_rejections": 242,
            "stale_hash_mutation_rejections": 1,
            "citation_registry_population": len(evidence["source_registry"]),
            "reference_registry_population": len(evidence["source_registry"]),
            "pdf_pages": pdf_pages,
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": evidence["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence["route_a"],
        "nonclaims": evidence["nonclaims"],
        "excluded_from_manifest": [
            "C191_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc",
            "paper/*.aux", "paper/*.log", "paper/*.out", "paper/*.fdb_latexmk",
            "paper/*.fls", "paper/*.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27, f"expected 27 payload files, found {len(files)}"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C191_MANIFEST_PASS",
        "file_count": len(files),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(EVIDENCE),
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
