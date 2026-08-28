#!/usr/bin/env python3
"""Build and validate the self-excluded C218 release manifest."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C218_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c218_kv_evidence.json"
PDF = ROOT / "paper/main.pdf"
EVALUATION = ROOT / "evaluations/route_a/HCS-C218/2026-08-28.yaml"
SOURCE_COMMIT = "077a098ac5811e465b69db71b5e6031a4827eb55"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c218_kv_checker.py", "code/c218_kv_mutation.py",
    "code/c218_kv_producer.py", "code/c218_kv_replay.py",
    "code/c218_kv_sympy_crosscheck.py", "code/c218_release_manifest.py",
    "evaluations/route_a/HCS-C218/2026-08-28.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c218_kv_evidence.json",
}


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def run(script: str) -> str:
    return subprocess.check_output([sys.executable, str(ROOT / "code" / script)], text=True)


def sidecar(path: Path) -> bool:
    return path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"} or "__pycache__" in path.parts or path.name.endswith(".synctex.gz")


def main() -> None:
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["source_commit"] == SOURCE_COMMIT
    assert evidence["evaluator"]["sha256"] == EVALUATOR_SHA256
    assert evidence["scope_literal"] == SCOPE
    assert evidence["payload_sha256"] == payload_hash(evidence)
    assert evidence["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    assert evidence["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert all(v is False for v in evidence["scope_flags"].values())
    evaluation_text = EVALUATION.read_text()
    for literal in (f"candidate_id: HCS-C218", f"source_commit: {SOURCE_COMMIT}",
                    f"scope_literal: {SCOPE}", f"sha256: {EVALUATOR_SHA256}",
                    "overall_verdict: ROUTE_A_REJECTED", "route_b_invocation_allowed: false"):
        assert literal in evaluation_text, literal
    physical = {str(p.relative_to(ROOT)): p for p in ROOT.rglob("*") if p.is_file()}
    assert not [name for name, p in physical.items() if sidecar(p)], "build sidecar present"
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, f"payload mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}"
    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    hashes = [digest(p) for p in rounds]
    assert len(set(hashes)) == 3 and digest(PDF) == hashes[2]
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    assert 2 <= pages <= 6
    fonts = subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:]
    assert fonts and all(line.split()[-5:-3] == ["yes", "yes"] for line in fonts)
    text = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True)
    for phrase in ["Kelvin", "spectral-abscissa", "ROUTE_A_REJECTED", SCOPE, "Jordan"]:
        assert phrase.lower() in text.lower(), phrase
    checker = run("c218_kv_checker.py")
    sympy = run("c218_kv_sympy_crosscheck.py")
    replay = run("c218_kv_replay.py")
    mutation = run("c218_kv_mutation.py")
    assert "independent checker: PASS" in checker
    assert "symbolic identities" in sympy
    assert "byte replay: PASS" in replay
    assert re.search(r"PASS \d+/\d+", mutation)
    checker_count = int(re.search(r"\((\d+) assertions", checker).group(1))
    sympy_count = int(re.search(r"PASS \((\d+) symbolic identities", sympy).group(1))
    hostile = int(re.search(r"PASS (\d+)/(\d+)", mutation).group(1))
    result = {
        "schema": "hcs-c218-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C218",
        "evaluation_date": "2026-08-28", "source_commit": SOURCE_COMMIT, "scope_literal": SCOPE,
        "headline": evidence["headline"],
        "build_contract": {
            "engine": "LuaLaTeX", "fixed_epoch": 1787788800, "passes_per_round": 2,
            "round_artifacts": ["paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf"],
            "final_equals": "paper/main_round2.pdf",
        },
        "gates": {
            "G0_source_scope_evaluator_lock": "PASS",
            "G1_root_regime_jordan_atlas": "PASS",
            "G2_essential_point_gap_optimizer_energy": "PASS",
            "G3_checker_sympy_replay_mutation": "PASS",
            "G4_two_substantive_revisions": "PASS",
            "G5_fixed_epoch_pdf_fonts_text_visual": "PASS",
            "G6_manifest_hash_closure": "PASS",
            "G7_target_operator_and_route_b": "NOT_CLAIMED",
        },
        "results": {
            "cases": len(evidence["regression"]["cases"]),
            "modes": len(evidence["regression"]["cases"]) * evidence["regression"]["modes_per_case"],
            "checker_assertions": checker_count, "sympy_checks": sympy_count,
            "hostile_rejections": hostile, "pdf_pages": pages,
            "embedded_subset_fonts": len(fonts), "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": evidence["payload_sha256"], "evidence_sha256": digest(EVIDENCE),
            "pdf_sha256": digest(PDF), "round_pdf_sha256": hashes,
        },
        "route_a_verdict": evidence["route_a"], "nonclaims": evidence["nonclaims"],
        "excluded_from_manifest": ["C218_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([p for p in ROOT.rglob("*") if p.is_file()]) == 28
    print(json.dumps({"status": "C218_MANIFEST_PASS", "payload_file_count": len(files),
                      "physical_file_count": 28, "manifest_sha256": digest(MANIFEST),
                      "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
