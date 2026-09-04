#!/usr/bin/env python3
"""Deterministic 38-payload release gate for HCS-C377."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c377 release refuses optimized Python")

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C377_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c377_periodic_clm_evidence.json"
TEX = ROOT / "paper/main.tex"
MAIN_PDF = ROOT / "paper/main.pdf"
EVALUATION = ROOT / "evaluations/route_a/HCS-C377/2026-09-04.yaml"
YAML_RAW_SHA = "f7a15957460d7ebdf3b18c51044e31899d66fb4d4fba3a7f280c50e2355e8920"
YAML_SEMANTIC_SHA = "9645872c74a85036a2aa42bb9221ab20a7295731034dcd624f8599150424e2d8"
AUTHORITY = "flow_systems/skills/route-a-evaluator.md"
AUTHORITY_VERSION = "0.2.0"
AUTHORITY_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
PDF_NAMES = ("main_round0_original.pdf", "main_round1.pdf", "main_round2.pdf")
EXPECTED = (
    "ASSUMPTIONS.md", "CLAIMS.md", "EXPERIMENT_PLAN.md", "LIMITATIONS.md", "NARRATIVE_REPORT.md",
    "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md", "README.md", "REFERENCES.md", "REPRODUCIBILITY.md",
    "RESEARCH_QUESTION.md", "SCOPE.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md", "requirements.txt",
    "code/README.md", "code/c377_periodic_clm_checker.py", "code/c377_periodic_clm_mutation.py",
    "code/c377_periodic_clm_producer.py", "code/c377_periodic_clm_replay.py",
    "code/c377_periodic_clm_sympy_crosscheck.py", "code/c377_release_manifest.py",
    "evaluations/route_a/HCS-C377/2026-09-04.yaml", "paper/COMPILE_REPORT.md", "paper/README.md",
    "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf",
    "paper/main_round2.pdf", "paper/main_round0.tex", "paper/main_round1.tex", "paper/main_round2.tex",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c377_periodic_clm_evidence.json", "tests/test_c377_smoke.py",
)
SCRIPTS = (
    "c377_periodic_clm_producer.py", "c377_periodic_clm_checker.py",
    "c377_periodic_clm_sympy_crosscheck.py", "c377_periodic_clm_replay.py",
    "c377_periodic_clm_mutation.py", "c377_release_manifest.py",
)
WARNING_PATTERN = re.compile(
    r"(?:LaTeX|Package [^:\n]+) Warning:|warning  \(pdf backend\)|Overfull|Underfull|"
    r"undefined (?:references|citations)|Rerun to get|Missing character"
)
UNESCAPED_TEX_SPACING_PATTERN = re.compile(r"(?<!\\)\b(?:quad|qquad)\b")


def sha256(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command, **kwargs):
    process = subprocess.run(command, capture_output=True, text=True, **kwargs)
    if process.returncode:
        raise AssertionError(f"command failed {command}:\n{process.stdout}\n{process.stderr}")
    return process.stdout.strip()


def actual_files(): return sorted(str(path.relative_to(ROOT)) for path in ROOT.rglob("*") if path.is_file())


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        if key in out: raise ValueError(f"duplicate JSON key {key}")
        out[key] = value
    return out


def strict_json(path):
    return json.loads(path.read_text(), object_pairs_hook=unique_object,
                      parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))


def canonical(value): return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def evidence_payload_hash():
    value = strict_json(EVIDENCE)
    claimed = value.pop("payload_sha256")
    assert claimed == hashlib.sha256(canonical(value)).hexdigest()
    return claimed


def compile_round(index):
    blobs = []
    for build in range(2):
        with tempfile.TemporaryDirectory(prefix=f"c377-tex-r{index}-b{build}-") as directory:
            work = Path(directory)
            shutil.copy2(TEX, work / "main.tex")
            wrapper = ROOT / "paper" / f"main_round{index}.tex"
            shutil.copy2(wrapper, work / wrapper.name)
            env = dict(os.environ, SOURCE_DATE_EPOCH="1788480000", FORCE_SOURCE_DATE="1")
            command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", wrapper.name]
            run(command, cwd=work, env=env)
            run(command, cwd=work, env=env)
            log = (work / "main.log").read_text(errors="replace")
            match = WARNING_PATTERN.search(log)
            assert match is None, f"settled LaTeX warning round {index}: {match.group(0)}"
            blobs.append((work / "main.pdf").read_bytes())
    assert blobs[0] == blobs[1], f"fresh builds differ round {index}"
    return blobs[0]


def pdf_gate(path, index):
    info = run(["pdfinfo", str(path)])
    match = re.search(r"^Pages:\s+(\d+)", info, re.MULTILINE)
    assert match
    pages = int(match.group(1))
    fonts = run(["pdffonts", str(path)]).splitlines()[2:]
    assert fonts
    for line in fonts:
        columns = line.split()
        assert len(columns) >= 7 and columns[-5] == "yes" and columns[-4] == "yes", line
    assert any("DroidSansFallback" in line.replace(" ", "") for line in fonts), "CJK font absent"
    with tempfile.TemporaryDirectory(prefix="c377-pdf-audit-") as directory:
        work = Path(directory)
        txt = work / "main.txt"
        run(["pdftotext", str(path), str(txt)])
        raw = txt.read_bytes()
        assert all(byte >= 32 or byte in (10, 12, 13) for byte in raw)
        text = raw.decode("utf-8")
        normalized = " ".join(text.split())
        lowered = normalized.lower()
        assert "The Periodic Constantin–Lax–Majda Equation" in normalized
        assert "??" not in text and "TODO" not in text and "[VERIFY]" not in text
        assert "qquad" not in text and " quad " not in text
        assert "Keywords:" in text and "中文摘要" in text and "关键词" in text
        english_keywords = text.split("Keywords:", 1)[1].split("中文摘要", 1)[0]
        chinese_keywords = text.split("关键词", 1)[1].split("1 Convention", 1)[0]
        assert 5 <= english_keywords.count(";") + 1 <= 7
        assert 5 <= chinese_keywords.count("；") + 1 <= 7
        tokens = (
            "round zero fixes the periodic",
            "round one adds necessary-and-",
            "round two adds transverse local",
        )
        assert tokens[index] in text
        if index == 0:
            assert "Complete First-Pole Clock" not in normalized
            assert "Transverse Profiles" not in normalized
            assert "Complete forward-time classification" not in text
            assert "Transverse first-pole profiles" not in text
            assert "forward smooth breakdown occurs if and only if" not in lowered
        elif index == 1:
            assert "Complete First-Pole Clock" in normalized
            assert "Transverse Profiles" not in normalized
            assert "Complete forward-time classification" in text
            assert "Transverse first-pole profiles" not in text
            assert "forward smooth breakdown occurs if and only if" in lowered
        else:
            assert "First-Pole Clock, and Transverse Profiles" in normalized
            assert "Complete forward-time classification" in text
            assert "Transverse first-pole profiles" in text
            assert "at every simple first pole" in lowered
        if index == 2:
            assert "NO_BAD_EULER_OR_ROOT_NUMBER" in text
            assert "not asserted at a tangent zero" in lowered
            assert "if every point attaining" in lowered
        prefix = work / "page"
        run(["pdftoppm", "-png", "-r", "72", str(path), str(prefix)])
        images = sorted(work.glob("page-*.png"))
        assert len(images) == pages
        sizes = [image.stat().st_size for image in images]
        assert all(size > 1000 for size in sizes)
    return {"pages": pages, "fonts": len(fonts), "raster_sizes": sizes}


def optimized_gate():
    for name in SCRIPTS:
        for flag in ("-O", "-OO"):
            p = subprocess.run([sys.executable, flag, str(ROOT / "code" / name), "--help"], capture_output=True, text=True)
            assert p.returncode and "refuses optimized Python" in p.stdout + p.stderr


def source_gate():
    texts = []
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix in (".md", ".py", ".tex", ".txt", ".yaml"):
            raw = path.read_bytes()
            assert all(byte >= 32 or byte in (10, 13) for byte in raw), f"control byte {path}"
            text = path.read_text(errors="replace")
            if path.suffix == ".tex":
                match = UNESCAPED_TEX_SPACING_PATTERN.search(text)
                assert match is None, f"unescaped TeX spacing token {match.group(0)} in {path}"
            texts.append(text)
    for index in range(3):
        wrapper = ROOT / "paper" / f"main_round{index}.tex"
        assert wrapper.read_text() == f"\\def\\CRevisionRound{{{index}}}\n\\input{{main.tex}}\n"
    title_contract = """\\ifcase\\CRevisionRound
\\title{The Periodic Constantin--Lax--Majda Equation:\\
Exact Arbitrary-Mean Riccati Flow}
\\or
\\title{The Periodic Constantin--Lax--Majda Equation:\\
Exact Arbitrary-Mean Flow and Complete First-Pole Clock}
\\else
\\title{The Periodic Constantin--Lax--Majda Equation:\\
Exact Arbitrary-Mean Flow, First-Pole Clock, and Transverse Profiles}
\\fi"""
    assert TEX.read_text().count(title_contract) == 1
    joined = "\n".join(texts)
    for stale in ("HCS-" + "C376", "HEN-" + "O360", "c376" + "_", "Landau" + " ladder"):
        assert stale not in joined, f"stale token {stale}"
    x = strict_json(EVIDENCE)
    assert x["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert all(value is False for value in x["scope_flags"].values())
    assert x["route_a"]["route_b_invocation_allowed"] is False
    assert "no unconditional self-similar rate at tangent or higher-order zeros" in x["nonclaims"]
    assert "10.1002/cpa.3160380605" in joined and "10.1007/s00332-021-09737-x" in joined


def lane_gate():
    outputs = []
    python = sys.executable
    with tempfile.TemporaryDirectory(prefix="c377-release-evidence-") as directory:
        output = Path(directory) / "evidence.json"
        outputs.append(run([python, "-B", str(ROOT / "code/c377_periodic_clm_producer.py"), "--output", str(output)]))
        assert output.read_bytes() == EVIDENCE.read_bytes()
    outputs.append(run([python, "-B", str(ROOT / "code/c377_periodic_clm_checker.py")]))
    outputs.append(run([python, "-B", str(ROOT / "code/c377_periodic_clm_sympy_crosscheck.py")]))
    outputs.append(run([python, "-B", str(ROOT / "code/c377_periodic_clm_replay.py")]))
    outputs.append(run([python, "-B", str(ROOT / "code/c377_periodic_clm_mutation.py")]))
    run([python, "-B", "-m", "unittest", "tests/test_c377_smoke.py"], cwd=ROOT)
    outputs.append("C377 unittest smoke PASS: tests=3")
    return outputs


def make_manifest(rounds, lanes):
    files = {relative: sha256(ROOT / relative) for relative in EXPECTED}
    return {
        "schema": "hcs-release-manifest-v1", "candidate_id": "HCS-C377", "obstruction_id": "HEN-O361",
        "source_commit": "f58422d8f03235329863f946654981ecb5d4dc97", "fixed_epoch": 1788480000,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER", "evaluator_authority": AUTHORITY,
        "evaluator_version": AUTHORITY_VERSION, "evaluator_authority_sha256": AUTHORITY_SHA,
        "payload_file_count": 38, "physical_file_count": 39,
        "evaluation_raw_sha256": YAML_RAW_SHA, "evaluation_semantic_sha256": YAML_SEMANTIC_SHA,
        "evidence_sha256": sha256(EVIDENCE), "evidence_payload_sha256": evidence_payload_hash(),
        "main_pdf_sha256": sha256(MAIN_PDF),
        "release_lanes": {"producer": "PASS", "independent_checker": "PASS", "sympy_crosscheck": "PASS", "isolated_byte_replay": "PASS", "hostile_mutation": "PASS", "unittest_smoke": "PASS", "optimized_mode_refusal": "PASS", "deterministic_pdf_rebuild": "PASS", "payload_membership": "PASS", "forbidden_claim_firewall": "PASS", "text_control_byte_hygiene": "PASS"},
        "lane_receipts": lanes, "pdf_rounds": rounds,
        "files": {key: files[key] for key in sorted(files)},
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--build-pdfs", action="store_true")
    args = parser.parse_args()
    if args.build_pdfs:
        blobs = [compile_round(index) for index in range(3)]
        for blob, name in zip(blobs, PDF_NAMES): (ROOT / "paper" / name).write_bytes(blob)
        MAIN_PDF.write_bytes(blobs[2])
        print("C377 PDF build PASS: three double-fresh rounds; main=round2")
        return
    current = actual_files()
    allowed = sorted(EXPECTED + (MANIFEST.name,))
    permitted = sorted(EXPECTED) if args.write and not MANIFEST.exists() else allowed
    assert current == permitted, f"file ledger mismatch extra={sorted(set(current)-set(permitted))} missing={sorted(set(permitted)-set(current))}"
    assert sha256(EVALUATION) == YAML_RAW_SHA
    optimized_gate()
    source_gate()
    lanes = lane_gate()
    assert MAIN_PDF.read_bytes() == (ROOT / "paper/main_round2.pdf").read_bytes()
    rounds = []
    for index, name in enumerate(PDF_NAMES):
        path = ROOT / "paper" / name
        audit = pdf_gate(path, index)
        audit.update({"round": index, "file": "paper/" + name, "sha256": sha256(path)})
        rounds.append(audit)
    assert rounds[0]["pages"] < rounds[1]["pages"] < rounds[2]["pages"], "page counts must increase"
    for index, name in enumerate(PDF_NAMES):
        assert compile_round(index) == (ROOT / "paper" / name).read_bytes()
    manifest = make_manifest(rounds, lanes)
    if args.write:
        MANIFEST.write_bytes(json.dumps(manifest, sort_keys=True, indent=2, ensure_ascii=False).encode() + b"\n")
        print("C377 manifest WRITE PASS: payload=38 physical=39")
    else:
        assert strict_json(MANIFEST) == manifest, "manifest does not match fresh reconstruction"
        print("C377 release PASS: evidence=" + manifest["evidence_sha256"] + " pdf=" + manifest["main_pdf_sha256"] + " manifest=" + sha256(MANIFEST))


if __name__ == "__main__":
    main()
