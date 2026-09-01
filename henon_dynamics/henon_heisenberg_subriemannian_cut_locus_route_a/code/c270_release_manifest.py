#!/usr/bin/env python3
"""Full 27-payload release closure for HCS-C270."""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C270_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c270_heisenberg_evidence.json"
PDF = ROOT / "paper/main.pdf"
YAML = ROOT / "evaluations/route_a/HCS-C270/2026-09-01.yaml"
SOURCE = "9cb7483e97ef82fdc06d45ecb3043f183ce22391"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788134400
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c270_heisenberg_checker.py", "code/c270_heisenberg_mutation.py",
    "code/c270_heisenberg_producer.py", "code/c270_heisenberg_replay.py",
    "code/c270_heisenberg_sympy_crosscheck.py", "code/c270_release_manifest.py",
    "evaluations/route_a/HCS-C270/2026-09-01.yaml", "paper/COMPILE_REPORT.md", "paper/README.md",
    "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf",
    "paper/main_round2.pdf", "results/HOSTILE_AUDIT.md", "results/RESULTS.md",
    "results/TEST_REPORT.md", "results/c270_heisenberg_evidence.json",
}


def digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def payload_hash(d: dict) -> str:
    q = dict(d)
    q.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(q, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def sidecar(p: Path) -> bool:
    return p.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"} or "__pycache__" in p.parts or p.name.endswith(".synctex.gz")


def run(name: str) -> str:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True)


def main() -> None:
    d = json.loads(EVIDENCE.read_text())
    assert d["candidate_id"] == "HCS-C270" and d["source_commit"] == SOURCE
    assert d["fixed_epoch"] == EPOCH and d["scope_literal"] == SCOPE
    assert d["evaluator"]["sha256"] == EVAL and d["payload_sha256"] == payload_hash(d)
    assert d["proof_contract"]["status"] == "PROVABLE AS STATED"
    assert d["proof_contract"]["scope"] == "only standard H^1; no theorem for arbitrary Carnot groups"
    assert d["proof_contract"]["complete_geodesics"] == (
        "there are no nontrivial closed complete geodesics: lambda=0 gives lines, "
        "while lambda!=0 has nonzero vertical drift per horizontal period"
    )
    assert d["trajectory_contract"]["first_cut_time"] == "2*pi/abs(lambda)"
    assert d["trajectory_contract"]["first_conjugate_time"] == "2*pi/abs(lambda)"
    assert d["distance_contract"]["cut_locus_from_identity"] == "{(0,0,z): z!=0}"
    assert d["route_a"] == {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    assert all(value is False for value in d["scope_flags"].values())

    y = YAML.read_text()
    for token in ("candidate_id: HCS-C270", f"source_commit: {SOURCE}", f"scope_literal: {SCOPE}",
                  f"evaluator_authority_sha256: {EVAL}", "A1_FAIL", "A4_FORMAL_HINT",
                  "overall_verdict: ROUTE_A_REJECTED", "route_b_invocation_allowed: false"):
        assert token in y, token
    report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    assert f"SOURCE_DATE_EPOCH={EPOCH}" in report and "byte-identical" in report and "warning-free" in report

    physical = {str(p.relative_to(ROOT)): p for p in ROOT.rglob("*") if p.is_file()}
    assert not [name for name, p in physical.items() if sidecar(p)]
    files = {name: digest(p) for name, p in sorted(physical.items()) if p != MANIFEST}
    assert set(files) == EXPECTED, (sorted(EXPECTED-set(files)), sorted(set(files)-EXPECTED))
    assert len(files) == 27

    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    round_hashes = [digest(p) for p in rounds]
    assert len(set(round_hashes)) == 3 and digest(PDF) == round_hashes[2]
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    assert 2 <= pages <= 6
    fonts = [line for line in subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
             if line.strip() and not line.lstrip().startswith("-")]
    assert fonts and all(len(line.split()) >= 7 and line.split()[-5] == "yes" and line.split()[-4] == "yes" for line in fonts)
    text = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower()
    for token in ("provable as stated", "first conjugate", "first cut", "implicit angle", "cut locus",
                  "a1_fail", "a4_formal_hint", "route_a_rejected", SCOPE.lower(), "arbitrary carnot groups"):
        assert token in text, token

    producer = run("c270_heisenberg_producer.py")
    checker = run("c270_heisenberg_checker.py")
    sympy = run("c270_heisenberg_sympy_crosscheck.py")
    replay = run("c270_heisenberg_replay.py")
    mutation = run("c270_heisenberg_mutation.py")
    assert "C270_PRODUCER_PASS" in producer and "C270 independent checker: PASS" in checker
    assert "C270_SYMPY_PASS" in sympy and "C270 byte replay: PASS" in replay
    cm = re.search(r"PASS \((\d+) assertions", checker)
    sm = re.search(r"PASS \((\d+) symbolic", sympy)
    mm = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert cm and sm and mm and mm.group(1) == mm.group(2)
    counts = d["regression"]["counts"]

    result = {
        "schema": "hcs-c270-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C270",
        "evaluation_date": "2026-09-01", "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": "Complete Hamilton, first-conjugate, cut-locus, and distance atlas for standard real H^1",
        "build_contract": {"engine": "LuaLaTeX", "fixed_epoch": EPOCH, "passes_per_build": 2,
                           "fresh_builds_per_round": 2,
                           "round_artifacts": ["paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf"],
                           "final_equals": "paper/main_round2.pdf"},
        "gates": {"G0_source_scope_evaluator": "PASS", "G1_frame_hamilton_contact": "PASS",
                  "G2_complete_flow_and_no_closed_geodesics": "PASS", "G3_jacobian_first_conjugate": "PASS",
                  "G4_dido_cut_locus": "PASS", "G5_distance_and_boundaries": "PASS",
                  "G6_checker_sympy_replay_mutation": "PASS", "G7_two_substantive_revisions": "PASS",
                  "G8_deterministic_pdf_fonts_log": "PASS", "G9_manifest_hash_closure": "PASS",
                  "G10_general_carnot_extension": "NOT_CLAIMED", "G11_target_operator_route_b": "NOT_CLAIMED"},
        "results": {"trajectory_rows": counts["trajectory_rows"], "distance_rows": counts["distance_rows"],
                    "vertical_rows": counts["vertical_rows"], "numeric_cells": counts["numeric_cells"],
                    "checker_assertions": int(cm.group(1)), "sympy_checks": int(sm.group(1)),
                    "hostile_rejections": int(mm.group(1)), "pdf_pages": pages,
                    "embedded_subset_fonts": len(fonts), "evidence_bytes": EVIDENCE.stat().st_size,
                    "evidence_payload_sha256": d["payload_sha256"], "evidence_sha256": digest(EVIDENCE),
                    "pdf_sha256": digest(PDF), "round_pdf_sha256": round_hashes},
        "route_a_verdict": d["route_a"], "theorem_status": d["proof_contract"]["status"],
        "nonclaims": d["nonclaims"],
        "excluded_from_manifest": ["C270_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([p for p in ROOT.rglob("*") if p.is_file()]) == 28
    print(json.dumps({"status": "C270_MANIFEST_PASS", "payload_file_count": 27, "physical_file_count": 28,
                      "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(EVIDENCE),
                      "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
