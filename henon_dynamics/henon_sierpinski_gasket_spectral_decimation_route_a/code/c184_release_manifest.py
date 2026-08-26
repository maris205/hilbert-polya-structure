#!/usr/bin/env python3
"""Build the exact content-addressed, self-excluded C184 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

import yaml


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C184_RELEASE_MANIFEST.json"
SOURCE_COMMIT = "908a6818caedb0c46195a591873a2ac9c685b55e"
EVALUATOR_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
PATH_BASE = "henon_dynamics/henon_sierpinski_gasket_spectral_decimation_route_a"
EVIDENCE_PAYLOAD_SHA = "6501f85d491d61e224772aef24bb94f317219044bbc03864ebcffd3ed394a14e"
EVIDENCE_SHA = "9955cf03d3acd4c240569d0138348f78f58c69ebddb517b6b588d3dd74fd7bb9"
PDF_SHA = "3ae96a32319b2af57b72b73ab3085cfbe38c88b24f5fc0a831107ed44274230d"
ROUND_SHAS = [
    "e9c07ef24ebcc021cb2bc154daa56a4019adf2a0f44b620f0e06d52b070cc68e",
    "6f2971b373b08684017749ed070df171a7d0a4ab3a9be7a88bb31787fb7698f9",
    PDF_SHA,
]

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
    "code/c184_mutation.py",
    "code/c184_release_manifest.py",
    "code/c184_replay.py",
    "code/c184_spectral_decimation_checker.py",
    "code/c184_spectral_decimation_producer.py",
    "code/c184_sympy_crosscheck.py",
    "evaluations/route_a/HCS-C184/2026-08-26.yaml",
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
    "results/c184_spectral_decimation_evidence.json",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def canonical_payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def pdf_pages(path: Path) -> int:
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    match = re.search(r"^Pages:\s+(\d+)\s*$", output, re.MULTILINE)
    if not match:
        raise AssertionError("pdfinfo page count unavailable")
    return int(match.group(1))


def validate_route_evaluation(path: Path, evidence: dict) -> None:
    evaluation = yaml.safe_load(path.read_text())
    required_inputs = {
        "candidate_id", "candidate_definition", "family", "phase_space",
        "dynamics", "parameters", "parameter_provenance", "arithmetic_origin",
        "clock", "normalization", "determinant_convention", "orbit_cutoff",
        "precision", "training_data", "forbidden_data", "code_commit",
        "artifact_paths",
    }
    if not required_inputs <= evaluation.keys():
        raise AssertionError("Route-A v0.2 required inputs missing")
    assert evaluation["skill"] == "route-a-evaluator"
    assert evaluation["skill_version"] == "0.2.0"
    assert evaluation["candidate_id"] == "HCS-C184"
    assert evaluation["source_commit"] == evaluation["code_commit"] == evidence["source_commit"] == SOURCE_COMMIT
    assert str(evaluation["evaluation_date"]) == evidence["date_utc"] == "2026-08-26"
    assert evaluation["evaluator_authority_path"] == evidence["evaluator"]["authority_path"]
    assert evaluation["evaluator_authority_sha256"] == evidence["evaluator"]["authority_sha256"] == EVALUATOR_SHA
    assert evaluation["artifact_path_base"] == evidence["artifact_path_base"] == PATH_BASE
    assert evaluation["scope_literal"] == evidence["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert "no intrinsic rational-prime" in evaluation["arithmetic_origin"]
    assert "not physical time" in evaluation["clock"]
    assert evaluation["training_data"] == "none"

    artifacts = evaluation["artifact_paths"]
    assert isinstance(artifacts, list) and len(artifacts) == 3
    assert all((ROOT / artifact).is_file() for artifact in artifacts)
    required_lock = {
        "object", "family", "arithmetic_origin", "clock", "normalization",
        "determinant_convention", "cutoff", "precision", "allowed_data",
        "forbidden_data",
    }
    assert required_lock <= evaluation["source_lock"].keys()
    assert evaluation["source_lock"] == evidence["source_lock"]

    axis_map = {"a0": "A0", "a1": "A1", "a2": "A2", "a3": "A3", "a4": "A4"}
    for axis, evidence_axis in axis_map.items():
        record = evaluation[axis]
        assert record["verdict"] == evidence["route_a_verdict"][evidence_axis]
        assert record["evidence_status"] == "PROVED"
        axis_artifacts = record.get("artifacts")
        assert isinstance(axis_artifacts, list) and axis_artifacts
        assert all((ROOT / artifact).is_file() for artifact in axis_artifacts)
    assert evaluation["a0"]["verdict"] == "A0_FAIL"
    assert evaluation["a3"]["analytic_structure"]
    assert evaluation["a3"]["weil_compression"]
    assert evaluation["integrity_modes"] == evidence["integrity_modes"]
    assert evaluation["overall_verdict"] == evidence["route_a_verdict"]["overall"] == "ROUTE_A_REJECTED"
    assert evaluation["route_b_invocation_allowed"] is evidence["route_a_verdict"]["route_b_invocation_allowed"] is False


def validate_evidence(evidence: dict) -> None:
    assert evidence["schema"] == "HCS-C184-v1"
    assert evidence["candidate_id"] == "HCS-C184"
    assert evidence["payload_sha256"] == canonical_payload_hash(evidence) == EVIDENCE_PAYLOAD_SHA
    assert evidence["source_registry"] == [{
        "key": "fukushima_shima_1992_sierpinski",
        "title": "On a spectral analysis for the Sierpiński gasket",
        "authors": "Masatoshi Fukushima and Tadashi Shima",
        "journal": "Potential Analysis", "volume": 1, "issue": 1,
        "pages": "1-35", "year": 1992, "doi": "10.1007/BF00249784",
        "role": "classical ownership of the finite-gasket spectral-decimation method and complete spectrum",
    }]
    assert evidence["integrity_modes"] == {
        "implementation_bug": "CLEAR", "hallucinated_citation": "CLEAR",
        "hallucinated_result": "CLEAR", "shortcut_reliance": "CLEAR",
        "bug_reframed_as_insight": "CLEAR", "methodology_fabrication": "CLEAR",
        "frame_lock": "CLEAR",
    }
    assert evidence["scope_flags"] == {
        "used_target_zero_table": False, "used_target_prime_table": False,
        "used_arithmetic_local_data": False, "claimed_target_divisor_match": False,
        "claimed_target_functional_equation": False,
        "claimed_infinite_gasket_spectral_zeta": False,
        "claimed_level_as_physical_time": False, "claimed_hilbert_polya": False,
        "route_b_invocation_allowed": False,
    }
    route = evidence["route_a_verdict"]
    assert route == {
        "A0": "A0_FAIL",
        "A0_qualification": "LEVEL_AND_SPECTRAL_BRANCH_DATA_HAVE_NO_INTRINSIC_RATIONAL_PRIME_ORIGIN",
        "A1": "A1_FAIL",
        "A1_qualification": "THE_INVERSE_BRANCH_TREE_IS_LEVEL_RENORMALIZATION_NOT_A_PHYSICAL_TIME_PRIMITIVE_ORBIT_OWNER",
        "A2": "A2_FAIL",
        "A2_qualification": "FINITE_LAPLACIAN_DETERMINANTS_HAVE_NO_TARGET_DIVISOR_MATCH",
        "A3": "A3_PARTIAL_ANALYTIC_STRUCTURE",
        "A3_qualification": "EXACT_FINITE_SPECTRAL_ZETA_AND_DETERMINANT_STRUCTURE_ONLY_WITH_NO_TARGET_FUNCTIONAL_EQUATION",
        "A4": "A4_FORMAL_HINT",
        "A4_qualification": "THE_SELF_ADJOINT_LAPLACIAN_HAS_A_CANONICAL_UNITARY_EXPONENTIAL_BUT_REFINEMENT_LEVEL_IS_NOT_ITS_TIME_CLOCK",
        "overall": "ROUTE_A_REJECTED", "a0_failure_forces_rejection": True,
        "route_b_invocation_allowed": False,
    }
    regression = evidence["finite_regression"]
    assert regression["level_min"] == 1 and regression["level_max"] == 5
    assert regression["level_row_count"] == len(regression["level_rows"]) == 5
    assert regression["lineage_row_count"] == len(regression["lineage_rows"]) == 103
    assert regression["characteristic_coefficient_cells"] == 542
    assert regression["graph_eigenvalue_cells"] == 537
    assert evidence["all_level_theorem"]["renormalization_map"] == "R(t)=t(5-t)"
    assert evidence["all_level_theorem"]["exceptional_values"] == [2, 5, 6]
    assert "forced to 3" in evidence["all_level_theorem"]["six_series"]
    assert "not an autonomous physical-time map" in evidence["all_level_theorem"]["owner_boundary"]
    assert len(evidence["nonclaims"]) == 6
    assert "external peer review" in evidence["nonclaims"][-1]


def main() -> None:
    actual: set[str] = set()
    forbidden_endings = (".aux", ".log", ".out", ".fls", ".fdb_latexmk", ".synctex.gz")
    for path in ROOT.rglob("*"):
        if not path.is_file() or path == MANIFEST:
            continue
        relative = str(path.relative_to(ROOT))
        if "__pycache__" in path.parts or path.suffix == ".pyc":
            raise AssertionError(f"Python cache remains on disk: {relative}")
        if relative.endswith(forbidden_endings):
            raise AssertionError(f"build auxiliary remains on disk: {relative}")
        actual.add(relative)
    if actual != EXPECTED:
        raise AssertionError(
            f"payload closure mismatch; missing={sorted(EXPECTED-actual)}, extra={sorted(actual-EXPECTED)}"
        )

    evidence_path = ROOT / "results/c184_spectral_decimation_evidence.json"
    evidence = json.loads(evidence_path.read_text())
    validate_evidence(evidence)
    validate_route_evaluation(ROOT / "evaluations/route_a/HCS-C184/2026-08-26.yaml", evidence)
    assert digest(evidence_path) == EVIDENCE_SHA

    pdf = ROOT / "paper/main.pdf"
    rounds = [
        ROOT / "paper/main_round0_original.pdf",
        ROOT / "paper/main_round1.pdf",
        ROOT / "paper/main_round2.pdf",
    ]
    round_hashes = [digest(path) for path in rounds]
    assert round_hashes == ROUND_SHAS and len(set(round_hashes)) == 3
    assert digest(pdf) == PDF_SHA == round_hashes[-1]
    assert pdf_pages(pdf) == 2 and [pdf_pages(path) for path in rounds] == [2, 2, 2]
    compile_report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    assert PDF_SHA in compile_report and "Two new temporary directories" in compile_report
    assert "no LaTeX/package warning" in compile_report and "Visual inspection" in compile_report

    files = {relative: digest(ROOT / relative) for relative in sorted(actual)}
    result = {
        "schema": "hcs-c184-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C184",
        "evaluation_date": "2026-08-26",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "The all-level finite-gasket 2/5/6 genealogy closes exact characteristic, determinant, heat, and finite-zeta formulas, while graph refinement is not physical time and Route A is rejected",
        "gates": {
            "G0_source_DOI_clock_normalization_scope_and_A0_lock": "PASS_WITH_A0_FAIL",
            "G1_all_level_2_5_6_series_and_exceptional_continuation": "PASS",
            "G2_multiplicity_and_dimension_closure": "PASS",
            "G3_characteristic_cancellation_and_closed_determinant": "PASS",
            "G4_heat_finite_zeta_and_owner_boundary": "PASS_WITH_PARTIAL_ANALYTIC_STRUCTURE",
            "G5_checker_sympy_replay_repaired_hash_mutation": "PASS",
            "G6_route_a_v02_schema_and_seven_integrity_modes": "PASS",
            "G7_three_content_rounds_fresh_double_compile_fonts_logs_visual": "PASS",
            "G8_manifest_27_payload_and_disk_hash_closure": "PASS",
            "G9_arithmetic_target_Hilbert_Polya_Route_B": "NOT_CLAIMED",
        },
        "results": {
            "level_rows": 5,
            "lineage_rows": 103,
            "characteristic_coefficient_cells": 542,
            "graph_eigenvalue_cells": 537,
            "independent_checker_assertions": 3041,
            "sympy_checks": 33177,
            "direct_graph_characteristic_polynomials": 4,
            "repaired_hash_mutation_rejections": 70,
            "stale_hash_mutation_rejections": 1,
            "citation_registry_population": 1,
            "verified_reference_population": 1,
            "pdf_pages": 2,
            "evidence_bytes": evidence_path.stat().st_size,
            "evidence_payload_sha256": evidence["payload_sha256"],
            "evidence_sha256": digest(evidence_path),
            "pdf_sha256": digest(pdf),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence["route_a_verdict"],
        "nonclaims": evidence["nonclaims"],
        "integrity": {
            "finite_graph_diagonalization_is_all_level_proof": False,
            "external_reviewer_simulated": False,
            "acceptance_rate_reported": False,
            "mandatory_seven_mode_integrity_audit": "CLEAR",
            "route_a_v02_semantic_gate": "PASS",
            "refinement_clock_is_physical_time": False,
        },
        "excluded_from_manifest": ["C184_RELEASE_MANIFEST.json"],
        "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C184_MANIFEST_PASS",
        "file_count": len(files),
        "manifest_sha256": digest(MANIFEST),
        "evidence_payload_sha256": evidence["payload_sha256"],
        "evidence_sha256": digest(evidence_path),
        "pdf_sha256": digest(pdf),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
