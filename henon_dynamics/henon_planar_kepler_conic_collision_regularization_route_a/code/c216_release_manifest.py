#!/usr/bin/env python3
"""Build the content-addressed, self-excluded C216 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C216_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c216_kepler_evidence.json"
PDF = ROOT / "paper/main.pdf"
EVALUATION = ROOT / "evaluations/route_a/HCS-C216/2026-08-28.yaml"
SOURCE_COMMIT = "077a098ac5811e465b69db71b5e6031a4827eb55"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
PAYLOAD_SHA256 = "eeac27260e27d0b7dcd6d32fcfe72ccec8e5ce083c2ea1056a1b26c20c799225"
EVIDENCE_SHA256 = "7dc68924fe22c40bdababe055bf83b25f605ffbf9c16811bcceae9f5cc5fec55"
PDF_SHA256 = "10b9769a1ef8be2a10ba6a1f9d8f55e271b8724124a93b7167ebbd64b571cf05"
ROUND_HASHES = [
    "6b2a70d3ecc166c787a1124e4b2689e619dd6363c1f63430e8d180453344d23b",
    "d4d9883869f02f4a45b275a5c8d92722054ccf7b3d1ffbf2462fea79368696a5",
    "10b9769a1ef8be2a10ba6a1f9d8f55e271b8724124a93b7167ebbd64b571cf05",
]

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
    "code/c216_kepler_checker.py",
    "code/c216_kepler_mutation.py",
    "code/c216_kepler_producer.py",
    "code/c216_kepler_replay.py",
    "code/c216_kepler_sympy_crosscheck.py",
    "code/c216_release_manifest.py",
    "evaluations/route_a/HCS-C216/2026-08-28.yaml",
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
    "results/c216_kepler_evidence.json",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def sidecar(path: Path) -> bool:
    return (
        path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
        or path.name.endswith(".synctex.gz")
        or "__pycache__" in path.parts
    )


def run_json(script: Path) -> dict:
    output = subprocess.check_output([sys.executable, "-B", str(script)], text=True)
    return json.loads(output.strip().splitlines()[-1])


def pdf_pages(path: Path) -> int:
    info = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    metadata = evidence["metadata"]
    assert evidence["schema"] == "hcs-c216-planar-kepler-v1"
    assert metadata["candidate_id"] == "HCS-C216"
    assert metadata["evaluation_date"] == "2026-08-28"
    assert metadata["source_commit"] == SOURCE_COMMIT
    assert metadata["evaluator"]["sha256"] == EVALUATOR_SHA256
    assert metadata["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == PAYLOAD_SHA256 == payload_hash(evidence)
    assert digest(EVIDENCE) == EVIDENCE_SHA256
    assert evidence["route_a"]["tuple"] == [
        "A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"
    ]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert evidence["route_a"]["route_b_invocation_allowed"] is False

    evaluation_text = EVALUATION.read_text()
    for literal in (
        "candidate_id: HCS-C216",
        f"source_commit: {SOURCE_COMMIT}",
        f"scope_literal: {SCOPE}",
        f"sha256: {EVALUATOR_SHA256}",
        "overall: ROUTE_A_REJECTED",
        "route_b_invocation_allowed: false",
    ):
        assert literal in evaluation_text, literal

    physical = [path for path in ROOT.rglob("*") if path.is_file()]
    bad = [str(path.relative_to(ROOT)) for path in physical if sidecar(path)]
    assert not bad, f"build sidecar present: {bad}"
    files = {
        str(path.relative_to(ROOT)): digest(path)
        for path in sorted(physical)
        if path != MANIFEST
    }
    assert set(files) == EXPECTED_PAYLOADS, (
        f"payload path mismatch; missing={sorted(EXPECTED_PAYLOADS-set(files))}; "
        f"extra={sorted(set(files)-EXPECTED_PAYLOADS)}"
    )

    rounds = [
        ROOT / "paper/main_round0_original.pdf",
        ROOT / "paper/main_round1.pdf",
        ROOT / "paper/main_round2.pdf",
    ]
    assert all(path.exists() for path in rounds + [PDF])
    round_hashes = [digest(path) for path in rounds]
    assert ROUND_HASHES and round_hashes == ROUND_HASHES and len(set(round_hashes)) == 3
    assert PDF_SHA256 and digest(PDF) == PDF_SHA256 == round_hashes[-1]
    pages = pdf_pages(PDF)
    assert 2 <= pages <= 6
    font_lines = subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
    assert font_lines and all(line.split()[-5:-3] == ["yes", "yes"] for line in font_lines)
    extracted = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True)
    for phrase in (
        "Runge",
        "Levi",
        "radial action",
        "T = mP",
        "Artin",
        "ROUTE_A_REJECTED",
        SCOPE,
    ):
        assert phrase in extracted, phrase

    producer = run_json(ROOT / "code/c216_kepler_producer.py")
    checker = run_json(ROOT / "code/c216_kepler_checker.py")
    sympy = run_json(ROOT / "code/c216_kepler_sympy_crosscheck.py")
    replay = run_json(ROOT / "code/c216_kepler_replay.py")
    mutation = run_json(ROOT / "code/c216_kepler_mutation.py")
    assert producer["status"] == "C216_PRODUCER_PASS"
    assert checker["status"] == "C216_CHECKER_PASS"
    assert sympy["status"] == "C216_SYMPY_PASS"
    assert replay["status"] == "C216_REPLAY_PASS"
    assert mutation["status"] == "C216_MUTATION_PASS"

    result = {
        "schema": "hcs-c216-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C216",
        "evaluation_date": "2026-08-28",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "build_contract": {
            "engine": "LuaLaTeX",
            "fixed_epoch": 1787875200,
            "passes_per_round": 2,
            "round_artifacts": [
                "paper/main_round0_original.pdf",
                "paper/main_round1.pdf",
                "paper/main_round2.pdf",
            ],
            "final_equals": "paper/main_round2.pdf",
        },
        "headline": (
            "The planar Kepler Hamiltonian has a closed all-energy conic/action/scattering "
            "ledger, an explicit finite-time collision boundary, a fixed-energy Levi-Civita "
            "configuration continuation, and a positive-dimensional strobe obstruction."
        ),
        "gates": {
            "G0_source_scope_evaluator_lock": "PASS",
            "G1_runge_lenz_all_energy_conics": "PASS",
            "G2_period_action_scattering_collision_levi_civita": "PASS",
            "G3_fixed_shell_resonance_boundary": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS",
            "G5_two_substantive_revisions": "PASS",
            "G6_fixed_epoch_pdf_fonts_text_visual": "PASS",
            "G7_manifest_hash_closure": "PASS",
            "G8_target_operator_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "orbit_rows": evidence["summary"]["orbit_row_count"],
            "radial_collision_rows": evidence["summary"]["radial_collision_row_count"],
            "levi_civita_rows": evidence["summary"]["levi_civita_row_count"],
            "fixed_set_rows": evidence["summary"]["fixed_set_row_count"],
            "exact_identity_cells": evidence["summary"]["exact_identity_cells"],
            "checker_assertions": checker["assertions"],
            "sympy_checks": sympy["checks"],
            "replay_bytes": replay["bytes"],
            "repaired_hash_mutation_rejections": mutation["repaired_hash_rejections"],
            "stale_hash_mutation_rejections": mutation["stale_hash_rejections"],
            "hostile_rejections": mutation["total_rejections"],
            "pdf_pages": pages,
            "embedded_subset_fonts": len(font_lines),
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": evidence["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": evidence["route_a"],
        "nonclaims": evidence["nonclaims"],
        "excluded_from_manifest": [
            "C216_RELEASE_MANIFEST.json",
            "code/__pycache__/",
            "*.pyc",
            "paper/*.aux",
            "paper/*.log",
            "paper/*.out",
            "paper/*.fls",
            "paper/*.fdb_latexmk",
            "paper/*.synctex.gz",
        ],
        "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    physical_after = [path for path in ROOT.rglob("*") if path.is_file()]
    assert len(physical_after) == 28
    print(json.dumps({
        "status": "C216_MANIFEST_PASS",
        "payload_file_count": len(files),
        "physical_file_count": len(physical_after),
        "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": digest(EVIDENCE),
        "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
