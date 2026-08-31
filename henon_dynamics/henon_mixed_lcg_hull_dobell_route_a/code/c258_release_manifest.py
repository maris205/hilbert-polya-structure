#!/usr/bin/env python3
"""Content-addressed release gate for HCS-C258."""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C258_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c258_lcg_evidence.json"
PDF = ROOT / "paper/main.pdf"
YAML = ROOT / "evaluations/route_a/HCS-C258/2026-08-31.yaml"
SOURCE = "b89544f1f7b1043f4158dfdf9db77787b332f146"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788048000
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
    "code/c258_lcg_checker.py",
    "code/c258_lcg_mutation.py",
    "code/c258_lcg_producer.py",
    "code/c258_lcg_replay.py",
    "code/c258_lcg_sympy_crosscheck.py",
    "code/c258_release_manifest.py",
    "evaluations/route_a/HCS-C258/2026-08-31.yaml",
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
    "results/c258_lcg_evidence.json",
}
EXPECTED_TUPLE = [
    "A0_WEAK_ARITHMETIC_RELATION",
    "A1_WEAK",
    "A2_FAIL",
    "A3_FAIL",
    "A4_NATURAL_QUANTIZATION",
]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def is_sidecar(path):
    return (
        path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
        or path.name.endswith(".synctex.gz")
        or "__pycache__" in path.parts
    )


def run(script):
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output(
        [sys.executable, "-B", str(ROOT / "code" / script)],
        env=env,
        text=True,
    )


def main():
    data = json.loads(EVIDENCE.read_text())
    assert data["candidate_id"] == "HCS-C258"
    assert data["source_commit"] == SOURCE
    assert data["fixed_epoch"] == EPOCH
    assert data["scope_literal"] == SCOPE
    assert data["evaluator"]["sha256"] == EVAL
    assert data["payload_sha256"] == payload_hash(data)
    assert data["route_a"]["tuple"] == EXPECTED_TUPLE
    assert data["route_a"]["overall"] == "ROUTE_A_EXPLORATORY"
    assert data["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for value in data["scope_flags"].values())

    evaluation = YAML.read_text()
    for literal in (
        "candidate_id: HCS-C258",
        f"source_commit: {SOURCE}",
        f"scope_literal: {SCOPE}",
        f"evaluator_authority_sha256: {EVAL}",
        "overall_verdict: ROUTE_A_EXPLORATORY",
        "route_b_invocation_allowed: false",
        "A0_WEAK_ARITHMETIC_RELATION",
        "A4_NATURAL_QUANTIZATION",
        "Hull",
    ):
        assert literal in evaluation, literal

    assert f"SOURCE_DATE_EPOCH={EPOCH}" in (ROOT / "paper/COMPILE_REPORT.md").read_text()
    physical = {
        str(path.relative_to(ROOT)): path
        for path in ROOT.rglob("*")
        if path.is_file()
    }
    assert not [name for name, path in physical.items() if is_sidecar(path)]
    files = {
        name: digest(path)
        for name, path in sorted(physical.items())
        if path != MANIFEST
    }
    assert set(files) == EXPECTED, (
        f"payload mismatch missing={sorted(EXPECTED-set(files))} "
        f"extra={sorted(set(files)-EXPECTED)}"
    )

    rounds = [
        ROOT / "paper/main_round0_original.pdf",
        ROOT / "paper/main_round1.pdf",
        ROOT / "paper/main_round2.pdf",
    ]
    round_hashes = [digest(path) for path in rounds]
    assert len(set(round_hashes)) == 3
    assert digest(PDF) == round_hashes[2]
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    assert 2 <= pages <= 6
    fonts = [
        line
        for line in subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
        if line.strip() and not line.lstrip().startswith("-")
    ]
    assert fonts
    assert all(
        len(line.split()) >= 7
        and line.split()[-5] == "yes"
        and line.split()[-4] == "yes"
        for line in fonts
    )
    text = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower()
    for phrase in (
        "hull",
        "dobell",
        "congruential",
        "crt",
        "primitive",
        "a0_weak_arithmetic_relation",
        "route_a_exploratory",
        SCOPE.lower(),
    ):
        assert phrase in text, phrase

    producer = run("c258_lcg_producer.py")
    checker = run("c258_lcg_checker.py")
    symbolic = run("c258_lcg_sympy_crosscheck.py")
    replay = run("c258_lcg_replay.py")
    mutation = run("c258_lcg_mutation.py")
    assert "C258_PRODUCER_PASS" in producer
    assert "C258 independent checker: PASS" in checker
    assert "C258_SYMPY_PASS" in symbolic
    assert "C258 byte replay: PASS" in replay
    match = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert match and match.group(1) == match.group(2)
    checker_count = int(re.search(r"PASS \((\d+) assertions", checker).group(1))
    symbolic_count = int(re.search(r"PASS \((\d+) symbolic", symbolic).group(1))
    hostile_count = int(match.group(1))

    result = {
        "schema": "hcs-c258-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C258",
        "evaluation_date": "2026-08-31",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": data["headline"],
        "build_contract": {
            "engine": "LuaLaTeX",
            "fixed_epoch": EPOCH,
            "passes_per_round": 2,
            "fresh_builds_per_round": 2,
            "round_artifacts": [
                "paper/main_round0_original.pdf",
                "paper/main_round1.pdf",
                "paper/main_round2.pdf",
            ],
            "final_equals": "paper/main_round2.pdf",
        },
        "gates": {
            "G0_source_scope_evaluator_lock": "PASS",
            "G1_all_modulus_hull_dobell_theorem": "PASS",
            "G2_prime_power_valuation_and_crt": "PASS",
            "G3_primitive_zeta_and_koopman_ledgers": "PASS",
            "G4_checker_sympy_replay_mutation": "PASS",
            "G5_two_substantive_revisions": "PASS",
            "G6_fixed_epoch_pdf_fonts_text_visual": "PASS",
            "G7_manifest_hash_closure": "PASS",
            "G8_target_operator_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "moduli": data["regression"]["modulus_row_count"],
            "parameter_pairs": data["regression"]["enumerated_parameter_pairs"],
            "checker_assertions": checker_count,
            "sympy_checks": symbolic_count,
            "hostile_rejections": hostile_count,
            "pdf_pages": pages,
            "embedded_subset_fonts": len(fonts),
            "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": data["payload_sha256"],
            "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF),
            "round_pdf_sha256": round_hashes,
        },
        "route_a_verdict": data["route_a"],
        "nonclaims": data["nonclaims"],
        "excluded_from_manifest": [
            "C258_RELEASE_MANIFEST.json",
            "code/__pycache__/",
            "*.pyc",
            "paper build sidecars",
        ],
        "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(
        json.dumps(
            {
                "status": "C258_MANIFEST_PASS",
                "payload_file_count": 27,
                "physical_file_count": 28,
                "manifest_sha256": digest(MANIFEST),
                "evidence_sha256": digest(EVIDENCE),
                "pdf_sha256": digest(PDF),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
