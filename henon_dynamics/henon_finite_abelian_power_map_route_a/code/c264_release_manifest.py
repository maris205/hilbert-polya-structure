#!/usr/bin/env python3
"""Content-addressed 27-payload release gate for HCS-C264."""
from __future__ import annotations

import hashlib, json, os, re, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C264_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c264_power_map_evidence.json"
PDF = ROOT / "paper/main.pdf"
SOURCE = "a24c701881d22a4e49eaa2a44b94395c3c540b3d"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788048000
TUPLE = ["A0_WEAK_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c264_power_map_checker.py", "code/c264_power_map_mutation.py",
    "code/c264_power_map_producer.py", "code/c264_power_map_replay.py",
    "code/c264_power_map_sympy_crosscheck.py", "code/c264_release_manifest.py",
    "evaluations/route_a/HCS-C264/2026-08-31.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c264_power_map_evidence.json",
}


def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data):
    body = dict(data); body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def sidecar(path):
    return path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"} or "__pycache__" in path.parts or path.name.endswith(".synctex.gz")


def run(name):
    env = dict(os.environ); env["PYTHONDONTWRITEBYTECODE"] = "1"
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True)


def fresh_pdf_check():
    tex = ROOT / "paper/main.tex"
    outputs = []
    env = dict(os.environ); env["SOURCE_DATE_EPOCH"] = str(EPOCH)
    for _ in range(2):
        with tempfile.TemporaryDirectory(prefix="c264-pdf-") as td:
            cmd = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", rf"\def\CRevisionRound{{2}}\input{{{tex}}}"]
            subprocess.check_output(cmd, cwd=td, env=env, stderr=subprocess.STDOUT)
            subprocess.check_output(cmd, cwd=td, env=env, stderr=subprocess.STDOUT)
            log = (Path(td) / "main.log").read_text(errors="replace")
            forbidden = [r"LaTeX Warning", r"Package .* Warning", r"Overfull", r"Underfull", r"undefined references", r"Rerun to get"]
            assert not any(re.search(p, log) for p in forbidden)
            outputs.append((Path(td) / "main.pdf").read_bytes())
    assert outputs[0] == outputs[1] == PDF.read_bytes()


def main():
    data = json.loads(EVIDENCE.read_text())
    assert data["candidate_id"] == "HCS-C264" and data["source_commit"] == SOURCE
    assert data["fixed_epoch"] == EPOCH and data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert data["evaluator"]["sha256"] == EVAL and data["payload_sha256"] == payload_hash(data)
    assert data["route_a"]["tuple"] == TUPLE and data["route_a"]["overall"] == "ROUTE_A_PARTIAL"
    assert data["route_a"]["route_b_invocation_allowed"] is False
    assert all(v is False for v in data["scope_flags"].values())
    yaml = (ROOT / "evaluations/route_a/HCS-C264/2026-08-31.yaml").read_text()
    for literal in ["candidate_id: HCS-C264", f"source_commit: {SOURCE}", f"evaluator_authority_sha256: {EVAL}",
                    "overall_verdict: ROUTE_A_PARTIAL", "route_b_invocation_allowed: false", *TUPLE]:
        assert literal in yaml, literal

    physical = {str(p.relative_to(ROOT)): p for p in ROOT.rglob("*") if p.is_file()}
    assert not [name for name, p in physical.items() if sidecar(p)]
    files = {name: digest(p) for name, p in sorted(physical.items()) if p != MANIFEST}
    assert set(files) == EXPECTED, f"missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}"
    assert len(files) == 27
    rounds = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
    round_hashes = [digest(p) for p in rounds]
    assert len(set(round_hashes)) == 3 and digest(PDF) == round_hashes[2]
    assert round_hashes == [
        "9a0a03dff8c93f0e1e6a17cf40795f6132f2ebc5601d96dca74bd80e00b0dc4f",
        "21252916e5cc1074b2f4eb2ac55c4c171dd2f54f251febeb19a1a758a616756b",
        "d3d604ea273a27c1286463b23e07ab7bda78895fd5d998a281800343a2aefc3a",
    ]
    fresh_pdf_check()
    info = subprocess.check_output(["pdfinfo", str(PDF)], text=True)
    pages = int(next(line.split(":", 1)[1] for line in info.splitlines() if line.startswith("Pages:")))
    assert pages == 2
    font_lines = [line for line in subprocess.check_output(["pdffonts", str(PDF)], text=True).splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]
    assert font_lines and all(line.split()[-5] == "yes" and line.split()[-4] == "yes" for line in font_lines)
    pdftext = subprocess.check_output(["pdftotext", str(PDF), "-"], text=True).lower()
    for phrase in ["prime-support splitting", "uniform transient trees", "koopman jordan atlas", "zero jordan-block", "route_a_partial", "no_bad_euler_or_root_number", "10.1016/j.disc.2023.113393"]:
        assert phrase in pdftext, phrase

    producer, checker = run("c264_power_map_producer.py"), run("c264_power_map_checker.py")
    symbolic, replay, mutation = run("c264_power_map_sympy_crosscheck.py"), run("c264_power_map_replay.py"), run("c264_power_map_mutation.py")
    assert "C264_PRODUCER_PASS" in producer and "C264 independent checker: PASS" in checker
    assert "C264_SYMPY_PASS" in symbolic and "C264 byte replay: PASS" in replay
    m = re.search(r"PASS (\d+)/(\d+)", mutation); assert m and m.group(1) == m.group(2)
    checker_count = int(re.search(r"PASS \((\d+) assertions", checker).group(1))
    symbolic_count = int(re.search(r"PASS \((\d+) symbolic", symbolic).group(1))
    counts = data["regression"]["counts"]
    result = {
        "schema": "hcs-c264-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C264",
        "evaluation_date": "2026-08-31", "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": data["scope_literal"], "headline": data["headline"],
        "build_contract": {"engine": "LuaLaTeX", "fixed_epoch": EPOCH, "passes_per_build": 2,
                           "fresh_builds_per_round": 2, "final_equals": "paper/main_round2.pdf"},
        "gates": {"G0_source_scope_evaluator_lock": "PASS", "G1_periodic_fixed_primitive_zeta": "PASS",
                  "G2_uniform_tree_and_boundaries": "PASS", "G3_full_koopman_jordan_atlas": "PASS",
                  "G4_checker_sympy_replay_mutation": "PASS", "G5_two_substantive_revisions": "PASS",
                  "G6_pdf_determinism_fonts_text_visual": "PASS", "G7_manifest_hash_closure": "PASS",
                  "G8_target_operator_and_route_b": "NOT_CLAIMED"},
        "results": {**counts, "checker_assertions": checker_count, "sympy_checks": symbolic_count,
                    "hostile_rejections": int(m.group(1)), "pdf_pages": pages,
                    "embedded_subset_fonts": len(font_lines), "evidence_bytes": EVIDENCE.stat().st_size,
                    "evidence_payload_sha256": data["payload_sha256"], "evidence_sha256": digest(EVIDENCE),
                    "pdf_sha256": digest(PDF), "round_pdf_sha256": round_hashes},
        "route_a_verdict": data["route_a"], "nonclaims": data["nonclaims"],
        "excluded_from_manifest": ["C264_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([p for p in ROOT.rglob("*") if p.is_file()]) == 28
    print(json.dumps({"status": "C264_MANIFEST_PASS", "payload_file_count": 27, "physical_file_count": 28,
                      "manifest_sha256": digest(MANIFEST), "evidence_sha256": digest(EVIDENCE), "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__": main()
