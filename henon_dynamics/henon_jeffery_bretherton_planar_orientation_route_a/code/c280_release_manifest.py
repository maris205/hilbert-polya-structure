#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C280 release."""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C280_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c280_jeffery_evidence.json"
PAPER = ROOT / "paper"
PDF = PAPER / "main.pdf"
TEX = PAPER / "main.tex"
YAML = ROOT / "evaluations/route_a/HCS-C280/2026-09-01.yaml"
SOURCE = "51fb3d46f96b854314811c1ad62d3103cd5d54e5"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788220800
EVIDENCE_SHA = "858a50dcdfc8ad83c2c3ab1d46f44e67d2357d2430d6d11d345f847efa308374"
TUPLE = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
ROUND_PATHS = [PAPER / "main_round0_original.pdf", PAPER / "main_round1.pdf", PAPER / "main_round2.pdf"]
ROUND_HASHES = [
    "28422d18428447a0e40e9502efa30d58365ce6bed968b2143eb127b04bbc22f4",
    "92de1db47228be078b5cac565376cbbde312fb3d5f2c4433195c8b2246add677",
    "768d840bfbde6ceb4632bc1d48c10faea5ec267c743e190986824dc467a81035",
]
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c280_jeffery_checker.py", "code/c280_jeffery_mutation.py",
    "code/c280_jeffery_producer.py", "code/c280_jeffery_replay.py",
    "code/c280_jeffery_sympy_crosscheck.py", "code/c280_release_manifest.py",
    "evaluations/route_a/HCS-C280/2026-09-01.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c280_jeffery_evidence.json",
}
WARNING_RE = re.compile(
    r"LaTeX Warning|Package [^:\n]* Warning|Overfull|Underfull|"
    r"undefined references|Rerun to get|Missing character"
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    clean = dict(data); clean.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def is_sidecar(path: Path) -> bool:
    return path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"} or "__pycache__" in path.parts or path.name.endswith(".synctex.gz")


def run_python(name: str) -> str:
    env = dict(os.environ); env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True)


def pdf_pages(path: Path) -> int:
    info = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))


def font_rows(path: Path) -> list[str]:
    out = subprocess.check_output(["pdffonts", str(path)], text=True)
    return [line for line in out.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]


def fresh_build(round_number: int) -> tuple[bytes, str]:
    with tempfile.TemporaryDirectory(prefix=f"c280-r{round_number}-") as temp:
        work = Path(temp)
        env = dict(os.environ)
        env.update({"SOURCE_DATE_EPOCH": str(EPOCH), "FORCE_SOURCE_DATE": "1", "TZ": "UTC"})
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{{TEX}}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", source]
        for _ in range(2):
            subprocess.run(command, cwd=work, env=env, check=True,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = (work / "main.log").read_text(errors="replace")
        assert not WARNING_RE.search(log)
        return (work / "main.pdf").read_bytes(), log


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    assert digest(EVIDENCE) == EVIDENCE_SHA
    assert data["payload_sha256"] == payload_hash(data)
    assert data["schema"] == "hcs-c280-jeffery-bretherton-planar-orientation-v1"
    assert data["candidate_id"] == "HCS-C280" and data["source_commit"] == SOURCE
    assert data["evaluation_date"] == "2026-09-01" and data["fixed_epoch"] == EPOCH
    assert data["scope_literal"] == SCOPE and data["evaluator"]["sha256"] == EVAL
    assert data["proof_contract"]["status"] == "PROVABLE AS STATED"
    assert data["classification_contract"]["invariant"] == "delta=lambda^2*(a^2+((b+c)/2)^2)-((b-c)/2)^2=-det(B2)"
    assert data["model_contract"]["sphere_convention"] == "at r=1 an unmarked sphere has no intrinsic shape director; RP2 is retained only for a marked material director"
    assert data["classification_contract"]["hyperbolic"] == "delta>0: exactly three eigen-directors; Ws([e0]) is P(span(e0,v_-)) without [v_-], Wu([e0]) is P(span(e0,v_+)) without [v_+], and their closures are RP1 projective lines"
    assert data["simple_shear_contract"]["domain"] == "gamma!=0 for period formulas; gamma=0 is the identity flow"
    assert data["simple_shear_contract"]["director_period"] == "pi*(r+r^(-1))/abs(gamma) on the equator for gamma!=0"
    assert data["simple_shear_contract"]["oriented_period"] == "2*pi*(r+r^(-1))/abs(gamma) for every nonvertical oriented vector; also the mixed-director RP2 period"
    assert data["route_a"] == {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    assert all(value is False for value in data["scope_flags"].values())
    counts = data["regression"]["counts"]
    assert counts == {"parameter_rows": 625, "orbit_rows": 320, "shear_rows": 10, "strobe_rows": 5, "boundary_rows": 6}

    yaml_text = YAML.read_text()
    for token in ("candidate_id: HCS-C280", f"source_commit: {SOURCE}", f"fixed_epoch: {EPOCH}",
                  f"scope_literal: {SCOPE}", f"evaluator_authority_sha256: {EVAL}",
                  "A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL",
                  "overall_verdict: ROUTE_A_REJECTED", "route_b_invocation_allowed: false"):
        assert token in yaml_text, token
    compile_report = (PAPER / "COMPILE_REPORT.md").read_text()
    for token in (f"SOURCE_DATE_EPOCH={EPOCH}", "byte-identical", "warning-free", "embedded and subset", "visually inspected"):
        assert token in compile_report, token
    tex_text = " ".join(TEX.read_text().split())
    for token in (r"\cite{Jeffery1922}", r"\cite{Bretherton1962}",
                  "cited only for the isolated-ellipsoid source equation",
                  "only for rigid-particle and spheroidal-parameter lineage",
                  "No classification or proof below is outsourced"):
        assert token in tex_text, token

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if is_sidecar(path)]
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, (sorted(EXPECTED-set(files)), sorted(set(files)-EXPECTED))
    assert len(files) == 27

    assert [digest(path) for path in ROUND_PATHS] == ROUND_HASHES
    assert len(set(ROUND_HASHES)) == 3 and digest(PDF) == ROUND_HASHES[2]
    page_counts = [pdf_pages(path) for path in ROUND_PATHS]
    assert page_counts == [2, 3, 3] and pdf_pages(PDF) == 3
    font_counts = []
    for path in ROUND_PATHS:
        rows = font_rows(path)
        assert rows and all(len(row.split()) >= 7 and row.split()[-5] == "yes" and row.split()[-4] == "yes" for row in rows)
        font_counts.append(len(rows))
    final_text = " ".join(subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower().split())
    for token in ("complete projective atlas", "exact projective lift", "source–saddle–sink",
                  "nilpotent fixed", "simple shear", "stroboscopic fixed sets", "marked material", "8,328", "25/25",
                  "a0_fail", "a1_weak", "route_a_rejected", SCOPE.lower(),
                  "10.1098/rspa.1922.0078", "10.1017/s002211206200124x"):
        assert token in final_text, token

    fresh_hashes = []
    for round_number, (archive, expected_hash) in enumerate(zip(ROUND_PATHS, ROUND_HASHES)):
        one, _ = fresh_build(round_number); two, _ = fresh_build(round_number)
        assert one == two == archive.read_bytes()
        pair = [hashlib.sha256(one).hexdigest(), hashlib.sha256(two).hexdigest()]
        assert pair == [expected_hash, expected_hash]
        fresh_hashes.append(pair)

    producer = run_python("c280_jeffery_producer.py")
    checker = run_python("c280_jeffery_checker.py")
    sympy = run_python("c280_jeffery_sympy_crosscheck.py")
    replay = run_python("c280_jeffery_replay.py")
    mutation = run_python("c280_jeffery_mutation.py")
    assert "C280_PRODUCER_PASS" in producer and "C280 independent checker: PASS" in checker
    assert "C280_SYMPY_PASS" in sympy and "C280 byte replay: PASS" in replay
    cm = re.search(r"PASS \((\d+) assertions", checker)
    sm = re.search(r"PASS \((\d+) symbolic", sympy)
    mm = re.search(r"PASS (\d+)/(\d+)", mutation)
    assert cm and int(cm.group(1)) == 8328
    assert sm and int(sm.group(1)) == 39
    assert mm and mm.group(1) == mm.group(2) == "25"
    assert digest(EVIDENCE) == EVIDENCE_SHA

    result = {
        "schema": "hcs-c280-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C280",
        "evaluation_date": "2026-09-01", "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": SCOPE, "headline": data["headline"], "theorem_status": data["proof_contract"]["status"],
        "build_contract": {"engine": "LuaLaTeX", "fixed_epoch": EPOCH, "passes_per_build": 2,
                           "fresh_builds_per_round": 2,
                           "round_artifacts": [str(p.relative_to(ROOT)) for p in ROUND_PATHS],
                           "round_pdf_sha256": ROUND_HASHES, "fresh_build_sha256": fresh_hashes,
                           "final_equals": "paper/main_round2.pdf"},
        "gates": {
            "G0_source_scope_evaluator": "PASS", "G1_projective_lift": "PASS",
            "G2_cayley_hamilton_sign_atlas": "PASS", "G3_hyperbolic_cell_decomposition": "PASS",
            "G4_nilpotent_identity_boundaries": "PASS", "G5_minimal_periods_strobes": "PASS",
            "G6_checker_sympy_replay_mutation": "PASS", "G7_two_substantive_revisions": "PASS",
            "G8_deterministic_pdf_fonts_log_visual": "PASS", "G9_manifest_hash_closure": "PASS",
            "G10_claim_source_traceability": "PASS", "G11_target_operator_route_b": "NOT_CLAIMED",
        },
        "results": {**counts, "checker_assertions": int(cm.group(1)), "sympy_checks": int(sm.group(1)),
                    "hostile_rejections": int(mm.group(1)), "pdf_pages": 3, "round_pdf_pages": page_counts,
                    "embedded_subset_font_rows": font_counts, "evidence_bytes": EVIDENCE.stat().st_size,
                    "evidence_payload_sha256": data["payload_sha256"], "evidence_sha256": EVIDENCE_SHA,
                    "pdf_sha256": digest(PDF)},
        "route_a_verdict": data["route_a"], "nonclaims": data["nonclaims"],
        "excluded_from_manifest": ["C280_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({"status": "C280_MANIFEST_PASS", "payload_file_count": 27, "physical_file_count": 28,
                      "manifest_sha256": digest(MANIFEST), "evidence_sha256": EVIDENCE_SHA,
                      "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
