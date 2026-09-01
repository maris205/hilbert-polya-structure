#!/usr/bin/env python3
"""Release closure for HCS-C271."""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C271_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c271_sis_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE = "9cb7483e97ef82fdc06d45ecb3043f183ce22391"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788134400
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c271_sis_checker.py", "code/c271_sis_mutation.py", "code/c271_sis_producer.py", "code/c271_sis_replay.py", "code/c271_sis_sympy_crosscheck.py", "code/c271_release_manifest.py",
    "evaluations/route_a/HCS-C271/2026-09-01.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md", "results/c271_sis_evidence.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sidecar(path: Path) -> bool:
    return path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"} or "__pycache__" in path.parts or path.name.endswith(".synctex.gz")


def run(name: str) -> str:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True)


def main() -> None:
    d = json.loads(EVIDENCE.read_text())
    assert d["source_commit"] == SOURCE and d["fixed_epoch"] == EPOCH
    assert d["scope_literal"] == SCOPE and d["evaluator"]["sha256"] == EVALUATOR
    assert d["route_a"]["overall"] == "ROUTE_A_REJECTED" and not d["route_a"]["route_b_invocation_allowed"]
    assert all(v is False for v in d["scope_flags"].values())
    yaml = (ROOT / "evaluations/route_a/HCS-C271/2026-09-01.yaml").read_text()
    for token in ("candidate_id: HCS-C271", SOURCE, EVALUATOR, SCOPE, "A1_FAIL", "overall_verdict: ROUTE_A_REJECTED", "route_b_invocation_allowed: false"):
        assert token in yaml
    report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    assert f"SOURCE_DATE_EPOCH={EPOCH}" in report and "byte-identical" in report and "warning-free" in report
    physical = {str(p.relative_to(ROOT)): p for p in ROOT.rglob("*") if p.is_file()}
    assert not [n for n, p in physical.items() if sidecar(p)]
    files = {n: digest(p) for n, p in sorted(physical.items()) if p != MANIFEST}
    assert set(files) == EXPECTED, (sorted(EXPECTED - set(files)), sorted(set(files) - EXPECTED))
    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    round_hashes = [digest(p) for p in rounds]
    assert len(set(round_hashes)) == 3 and digest(PDF) == round_hashes[2]
    pages = int(next(x.split(":", 1)[1] for x in subprocess.check_output(["pdfinfo", str(PDF)], text=True).splitlines() if x.startswith("Pages:")))
    assert 2 <= pages <= 6
    font_lines = [x for x in subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:] if x.strip() and not x.lstrip().startswith("-")]
    assert font_lines and all(len(x.split()) >= 7 and x.split()[-5] == "yes" and x.split()[-4] == "yes" for x in font_lines)
    text = re.sub(r"\s+", " ", subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower())
    for token in ("irreducible network sis", "critical 1/t", "unique endemic", "route_a_rejected", SCOPE.lower()):
        assert token in text, token
    producer = run("c271_sis_producer.py")
    checker = run("c271_sis_checker.py")
    sympy = run("c271_sis_sympy_crosscheck.py")
    replay = run("c271_sis_replay.py")
    mutation = run("c271_sis_mutation.py")
    assert "C271_PRODUCER_PASS" in producer and "independent checker: PASS" in checker
    assert "C271_SYMPY_PASS" in sympy and "byte replay: PASS" in replay
    mm = re.search(r"PASS (\d+)/(\d+)", mutation); assert mm and mm.group(1) == mm.group(2)
    result = {
        "schema": "hcs-c271-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C271",
        "evaluation_date": "2026-09-01", "source_commit": SOURCE, "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "headline": "Global threshold, unique endemic state, and sharp critical Perron asymptotic for irreducible network SIS",
        "build_contract": {"engine": "LuaLaTeX", "fixed_epoch": EPOCH, "passes_per_build": 2, "fresh_builds_per_round": 2, "final_equals": "paper/main_round2.pdf"},
        "gates": {"theorem_status": "PROVABLE_AS_STATED", "independent_checker": "PASS", "symbolic_crosscheck": "PASS", "byte_replay": "PASS", "hostile_mutation": "PASS", "deterministic_pdf": "PASS", "manifest_closure": "PASS", "target_operator_route_b": "NOT_CLAIMED"},
        "results": {"parameter_cases": d["regression"]["counts"]["parameter_cases"], "critical_samples": d["regression"]["counts"]["critical_samples"], "checker_assertions": int(re.search(r"\((\d+) assertions", checker).group(1)), "sympy_checks": int(re.search(r"\((\d+) symbolic", sympy).group(1)), "hostile_rejections": int(mm.group(1)), "pdf_pages": pages, "embedded_subset_fonts": len(font_lines), "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF), "round_pdf_sha256": round_hashes},
        "route_a_verdict": d["route_a"], "nonclaims": d["nonclaims"],
        "excluded_from_manifest": ["C271_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"], "files": files,
    }
    assert len(files) == 27
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([p for p in ROOT.rglob("*") if p.is_file()]) == 28
    print(json.dumps({"status": "C271_MANIFEST_PASS", "payload_file_count": 27, "physical_file_count": 28, "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
