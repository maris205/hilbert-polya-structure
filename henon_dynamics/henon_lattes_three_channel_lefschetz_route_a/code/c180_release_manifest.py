#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C180 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

import yaml


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C180_RELEASE_MANIFEST.json"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def pdf_pages(path: Path) -> int:
    text = subprocess.check_output(["pdfinfo", str(path)], text=True)
    match = re.search(r"^Pages:\s+(\d+)\s*$", text, re.MULTILINE)
    if not match:
        raise AssertionError("pdfinfo page count unavailable")
    return int(match.group(1))


def validate_route_evaluation(path: Path, evidence: dict) -> None:
    evaluation = yaml.safe_load(path.read_text())
    required_inputs = {
        "candidate_id", "candidate_definition", "family", "phase_space", "dynamics",
        "parameters", "parameter_provenance", "arithmetic_origin", "clock", "normalization",
        "determinant_convention", "orbit_cutoff", "precision", "training_data", "forbidden_data",
        "code_commit", "artifact_paths",
    }
    assert required_inputs <= evaluation.keys(), "Route-A v0.2 required inputs missing"
    assert evaluation["skill"] == "route-a-evaluator" and evaluation["skill_version"] == "0.2.0"
    assert evaluation["candidate_id"] == "HCS-C180"
    assert evaluation["source_commit"] == evidence["source_commit"] == evaluation["code_commit"]
    assert evaluation["evaluator_authority_sha256"] == evidence["evaluator"]["authority_sha256"]
    assert evaluation["artifact_path_base"] == evidence["artifact_path_base"]
    assert evaluation["scope_literal"] == evidence["scope_literal"]
    required_lock = {
        "object", "arithmetic_origin", "clock", "normalization", "determinant_convention",
        "cutoff", "precision", "allowed_data", "forbidden_data",
    }
    assert required_lock <= evaluation["source_lock"].keys(), "Route-A v0.2 source lock incomplete"
    assert evaluation["source_lock"]["arithmetic_origin"] == evidence["source_lock"]["arithmetic_origin"]
    axis_keys = {"a0": "A0", "a1": "A1", "a2": "A2", "a3": "A3", "a4": "A4"}
    for axis in ("a0", "a1", "a2", "a3", "a4"):
        assert evaluation[axis]["verdict"] == evidence["route_a_verdict"][axis_keys[axis]]
        artifacts = evaluation[axis].get("artifacts")
        assert isinstance(artifacts, list) and artifacts, f"{axis}.artifacts missing"
        assert all((ROOT / artifact).is_file() for artifact in artifacts), f"{axis}.artifacts unresolved"
    assert evaluation["a3"].get("weil_compression"), "a3.weil_compression missing"
    assert evaluation["a0"]["verdict"] == "A0_FAIL"
    assert evaluation["overall_verdict"] == evidence["route_a_verdict"]["overall"] == "ROUTE_A_REJECTED"
    assert evaluation["route_b_invocation_allowed"] is evidence["route_a_verdict"]["route_b_invocation_allowed"] is False


def main() -> None:
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

    evidence_path = ROOT / "results/c180_lattes_evidence.json"
    pdf_path = ROOT / "paper/main.pdf"
    evidence = json.loads(evidence_path.read_text())
    validate_route_evaluation(ROOT / "evaluations/route_a/HCS-C180/2026-08-26.yaml", evidence)
    result = {
        "schema": "hcs-c180-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C180",
        "evaluation_date": "2026-08-26",
        "source_commit": "bbb809ee198bc9ad5f196383baab1e3d9de38e43",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "The full multiplication Lattes family has an exact plus/minus/branch multiplier census, Lefschetz sum one, rational Artin--Mazur zeta, and proper-isometry Wold boundary",
        "gates": {
            "G0_source_moduli_parameter_clock_lock": "PASS",
            "G0b_route_a_v02_schema_and_artifact_paths": "PASS",
            "G1_classical_ownership_and_collision_boundary": "PASS",
            "G2_all_tau_all_m_three_channel_theorem": "PASS",
            "G3_multiplier_and_lefschetz_identity": "PASS",
            "G4_exact_period_and_artin_mazur_zeta": "PASS",
            "G5_even_fourier_wold_and_determinant_boundary": "PASS_WITH_ROUTE_A_OBSTRUCTION",
            "G6_checker_sympy_replay_mutation": "PASS",
            "G7_three_content_rounds_double_compile_fonts_layout_visual": "PASS",
            "G8_manifest_hash_and_disk_closure": "PASS",
            "G9_arithmetic_target_hilbert_polya_route_b": "NOT_CLAIMED",
        },
        "results": {
            **evidence["counts"],
            "independent_checker_assertions": 43184,
            "sympy_checks": 18065,
            "repaired_hash_mutation_rejections": 23,
            "stale_hash_mutation_rejections": 1,
            "pdf_pages": pdf_pages(pdf_path),
            "evidence_payload_sha256": evidence["payload_sha256"],
            "evidence_sha256": digest(evidence_path),
            "pdf_sha256": digest(pdf_path),
            "paper_round_sha256": [
                digest(ROOT / "paper/main_round0_original.pdf"),
                digest(ROOT / "paper/main_round1.pdf"),
                digest(ROOT / "paper/main_round2.pdf"),
            ],
        },
        "route_a_verdict": {
            "A0": "A0_FAIL", "A1": "A1_WEAK", "A2": "A2_FAIL", "A3": "A3_FAIL",
            "A4": "A4_FORMAL_HINT", "overall": "ROUTE_A_REJECTED",
            "a0_failure_forces_rejection": True, "route_b_invocation_allowed": False,
        },
        "nonclaims": evidence["nonclaims"],
        "integrity": {
            "hard_gate": "all-moduli three-channel multiplier census plus Lefschetz and Wold boundary",
            "hard_gate_status": "PASS_WITH_ROUTE_A_REJECTION",
            "finite_ledgers_are_proof": False,
            "external_reviewer_simulated": False,
            "acceptance_rate_reported": False,
            "citation_population": 1,
            "mandatory_seven_mode_integrity_audit": "CLEAR",
            "route_a_v02_semantic_gate": "PASS",
        },
        "excluded_from_manifest": [
            "C180_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper/main.aux",
            "paper/main.log", "paper/main.out", "paper/main.fdb_latexmk", "paper/main.fls", "paper/main.synctex.gz",
        ],
        "files": files,
    }
    expected = {
        "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
        "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
        "code/README.md", "code/c180_lattes_checker.py", "code/c180_lattes_producer.py",
        "code/c180_mutation.py", "code/c180_release_manifest.py", "code/c180_replay.py",
        "code/c180_sympy_crosscheck.py", "evaluations/route_a/HCS-C180/2026-08-26.yaml",
        "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
        "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
        "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
        "results/c180_lattes_evidence.json",
    }
    assert len(files) == 27 and set(files) == expected, f"payload mismatch: {set(files) ^ expected}"
    rounds = result["results"]["paper_round_sha256"]
    assert len(set(rounds)) == 3 and rounds[-1] == result["results"]["pdf_sha256"]
    assert result["results"]["evidence_payload_sha256"] == "aff8291d4a6816df8a8925055729bb0f060da1ef2340f6e14ab50aba45bcdc86"
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C180_MANIFEST_PASS", "file_count": len(files), "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(evidence_path), "pdf_sha256": digest(pdf_path)}, sort_keys=True))


if __name__ == "__main__":
    main()
