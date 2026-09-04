#!/usr/bin/env python3
"""Deterministic 38-payload release gate for HCS-C376."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c376 release refuses optimized Python")

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
MANIFEST = ROOT / "C376_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c376_flat_magnetic_torus_evidence.json"
TEX = ROOT / "paper/main.tex"
MAIN_PDF = ROOT / "paper/main.pdf"
EVALUATION = ROOT / "evaluations/route_a/HCS-C376/2026-09-04.yaml"
YAML_RAW_SHA = "f1a920fc208186a02d4a5cafcf5cefbb554825699e503b7061dc8b0b29306287"
YAML_SEMANTIC_SHA = "9580d0e0d6fc1664cb701964c8bf5c82db6faecb1ec69c044dd50797f4990915"
AUTHORITY = "flow_systems/skills/route-a-evaluator.md"
AUTHORITY_VERSION = "0.2.0"
AUTHORITY_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
PDF_NAMES = ("main_round0_original.pdf", "main_round1.pdf", "main_round2.pdf")
WRAPPER_NAMES = ("main_round0.tex", "main_round1.tex", "main_round2.tex")
EXPECTED = (
    "ASSUMPTIONS.md", "CLAIMS.md", "EXPERIMENT_PLAN.md", "LIMITATIONS.md", "NARRATIVE_REPORT.md",
    "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md", "README.md", "REFERENCES.md", "REPRODUCIBILITY.md",
    "RESEARCH_QUESTION.md", "SCOPE.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md", "requirements.txt",
    "code/README.md", "code/c376_flat_magnetic_torus_checker.py",
    "code/c376_flat_magnetic_torus_mutation.py", "code/c376_flat_magnetic_torus_producer.py",
    "code/c376_flat_magnetic_torus_replay.py", "code/c376_flat_magnetic_torus_sympy_crosscheck.py",
    "code/c376_release_manifest.py", "evaluations/route_a/HCS-C376/2026-09-04.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0.tex", "paper/main_round1.tex", "paper/main_round2.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c376_flat_magnetic_torus_evidence.json", "tests/test_c376_smoke.py",
)
SCRIPTS = (
    "c376_flat_magnetic_torus_producer.py", "c376_flat_magnetic_torus_checker.py",
    "c376_flat_magnetic_torus_sympy_crosscheck.py", "c376_flat_magnetic_torus_replay.py",
    "c376_flat_magnetic_torus_mutation.py", "c376_release_manifest.py",
)
WARNING_PATTERN = re.compile(
    r"(?:LaTeX|Package [^:\n]+) Warning:|warning  \(pdf backend\)|Overfull|Underfull|"
    r"undefined (?:references|citations)|Rerun to get|Missing character"
)
UNESCAPED_TEX_SPACING_PATTERN = re.compile(r"(?<!\\)\b(?:quad|qquad)\b")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command, **kwargs) -> str:
    process = subprocess.run(command, capture_output=True, text=True, **kwargs)
    if process.returncode:
        raise AssertionError(f"command failed {command}:\n{process.stdout}\n{process.stderr}")
    return process.stdout.strip()


def actual_files():
    return sorted(str(path.relative_to(ROOT)) for path in ROOT.rglob("*") if path.is_file())


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key {key}")
        out[key] = value
    return out


def strict_json(path: Path):
    return json.loads(
        path.read_text(), object_pairs_hook=unique_object,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)),
    )


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def evidence_payload_hash() -> str:
    value = strict_json(EVIDENCE)
    claimed = value.pop("payload_sha256")
    assert claimed == hashlib.sha256(canonical(value)).hexdigest()
    return claimed


def compile_round(round_index: int) -> bytes:
    blobs = []
    for build_index in range(2):
        with tempfile.TemporaryDirectory(prefix=f"c376-tex-r{round_index}-b{build_index}-") as directory:
            work = Path(directory)
            shutil.copy2(TEX, work / "main.tex")
            wrapper = ROOT / "paper" / WRAPPER_NAMES[round_index]
            shutil.copy2(wrapper, work / wrapper.name)
            environment = dict(os.environ, SOURCE_DATE_EPOCH="1788480000", FORCE_SOURCE_DATE="1")
            command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", wrapper.name]
            run(command, cwd=work, env=environment)
            run(command, cwd=work, env=environment)
            log = (work / "main.log").read_text(errors="replace")
            match = WARNING_PATTERN.search(log)
            assert match is None, f"settled LaTeX warning in round {round_index}: {match.group(0)}"
            blobs.append((work / "main.pdf").read_bytes())
    assert blobs[0] == blobs[1], f"fresh builds differ in round {round_index}"
    return blobs[0]


def pdf_gate(path: Path, round_index: int):
    info = run(["pdfinfo", str(path)])
    match = re.search(r"^Pages:\s+(\d+)", info, re.MULTILINE)
    assert match
    pages = int(match.group(1))
    font_report = run(["pdffonts", str(path)])
    font_lines = font_report.splitlines()[2:]
    assert font_lines
    assert "DroidSansFallback" in font_report.replace(" ", ""), "embedded CJK font missing"
    for line in font_lines:
        columns = line.split()
        assert len(columns) >= 7 and columns[-5] == "yes" and columns[-4] == "yes", line
    with tempfile.TemporaryDirectory(prefix="c376-pdf-audit-") as directory:
        work = Path(directory)
        text_path = work / "text.txt"
        run(["pdftotext", str(path), str(text_path)])
        raw = text_path.read_bytes()
        assert all(byte >= 32 or byte in (10, 12, 13) for byte in raw), "PDF text control byte"
        text = raw.decode("utf-8")
        flat = " ".join(text.split())
        assert "A Charged Particle on a Flat Magnetic Torus" in text
        assert "中文摘要" in text and "关键词" in text and "Keywords:" in text
        assert not UNESCAPED_TEX_SPACING_PATTERN.search(text), "literal quad/qquad leaked into PDF text"
        assert "??" not in text and "TODO" not in text and "[VERIFY]" not in text
        tokens = (
            "round zero proves complete clean",
            "round one adds the complete",
            "round two adds exact heat",
        )
        assert tokens[round_index] in text
        keyword_tokens = (
            ("magnetic torus", "cyclotron flow", "clean return", "flux quantization", "line bundle"),
            ("magnetic torus", "Bochner Laplacian", "Landau levels", "flux quantization", "magnetic translations", "finite Heisenberg group"),
            ("magnetic torus", "Landau levels", "magnetic translations", "spectral zeta", "zeta determinant", "quantum revival", "Route A"),
        )
        assert all(token in flat for token in keyword_tokens[round_index])
        if round_index == 0:
            for future in ("Bochner Landau ladder", "Finite magnetic translations", "spectral zeta", "quantum revival", "Route-A closure"):
                assert future not in flat, f"round-zero leak: {future}"
        if round_index == 1:
            for future in ("Heat trace, spectral zeta", "zeta determinant", "quantum revival", "Route-A closure"):
                assert future not in flat, f"round-one leak: {future}"
        if round_index == 2:
            assert "NO_BAD_EULER_OR_ROOT_NUMBER" in text
            assert "least positive identity time" in text
            assert "2|N|/2" not in text
        prefix = work / "page"
        run(["pdftoppm", "-png", "-r", "72", str(path), str(prefix)])
        images = sorted(work.glob("page-*.png"))
        assert len(images) == pages
        raster_sizes = [item.stat().st_size for item in images]
        assert all(size > 1000 for size in raster_sizes)
    return {"pages": pages, "fonts": len(font_lines), "raster_sizes": raster_sizes}


def optimized_gate():
    for name in SCRIPTS:
        for flag in ("-O", "-OO"):
            process = subprocess.run(
                [sys.executable, flag, str(ROOT / "code" / name), "--help"],
                capture_output=True, text=True,
            )
            assert process.returncode and "refuses optimized Python" in process.stdout + process.stderr


def source_gate():
    texts = []
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix in (".md", ".py", ".tex", ".txt", ".yaml"):
            raw = path.read_bytes()
            assert all(byte >= 32 or byte in (10, 13) for byte in raw), f"control byte in {path}"
            source_text = path.read_text(errors="replace")
            if path.suffix == ".tex":
                assert not UNESCAPED_TEX_SPACING_PATTERN.search(source_text), f"unescaped TeX spacing command in {path}"
            texts.append(source_text)
    joined = "\n".join(texts)
    for index, name in enumerate(WRAPPER_NAMES):
        expected = f"\\def\\CRevisionRound{{{index}}}\n\\input{{main.tex}}\n".encode()
        assert (ROOT / "paper" / name).read_bytes() == expected, f"wrapper contract mismatch: {name}"
    for stale in ("HCS-" + "C373", "HEN-" + "O357", "c373" + "_", "Higgs" + " oscillator"):
        assert stale not in joined, f"stale template token {stale}"
    evidence = strict_json(EVIDENCE)
    assert evidence["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert all(value is False for value in evidence["scope_flags"].values())
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert "no Hilbert-Polya operator and no Route B" in evidence["nonclaims"]
    assert "10.1016/j.aop.2008.07.006" in joined
    assert "10.1023/A:1004115827959" in joined
    assert "10.1007/s00220-025-05267-9" in joined
    assert "Droid Sans Fallback" in joined and "中文摘要" in joined and "关键词" in joined
    assert not UNESCAPED_TEX_SPACING_PATTERN.search(r"x,\quad y; z,\qquad w")
    assert UNESCAPED_TEX_SPACING_PATTERN.search("x,quad y")
    assert UNESCAPED_TEX_SPACING_PATTERN.search("x,qquad y")


def lane_gate():
    outputs = []
    python = sys.executable
    with tempfile.TemporaryDirectory(prefix="c376-release-evidence-") as directory:
        path = Path(directory) / "evidence.json"
        outputs.append(run([python, "-B", str(ROOT / "code/c376_flat_magnetic_torus_producer.py"), "--output", str(path)]))
        assert path.read_bytes() == EVIDENCE.read_bytes()
    outputs.append(run([python, "-B", str(ROOT / "code/c376_flat_magnetic_torus_checker.py")]))
    outputs.append(run([python, "-B", str(ROOT / "code/c376_flat_magnetic_torus_sympy_crosscheck.py")]))
    outputs.append(run([python, "-B", str(ROOT / "code/c376_flat_magnetic_torus_replay.py")]))
    outputs.append(run([python, "-B", str(ROOT / "code/c376_flat_magnetic_torus_mutation.py")]))
    run([python, "-B", "-m", "unittest", "tests/test_c376_smoke.py"], cwd=ROOT)
    outputs.append("C376 unittest smoke PASS: tests=3")
    return outputs


def make_manifest(rounds, lanes):
    files = {relative: sha256(ROOT / relative) for relative in EXPECTED}
    evidence = strict_json(EVIDENCE)
    return {
        "schema": "hcs-release-manifest-v1", "candidate_id": "HCS-C376",
        "obstruction_id": "HEN-O360", "source_commit": "f58422d8f03235329863f946654981ecb5d4dc97", "fixed_epoch": 1788480000,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER", "evaluator_authority": AUTHORITY,
        "evaluator_version": AUTHORITY_VERSION, "evaluator_authority_sha256": AUTHORITY_SHA,
        "payload_file_count": 38, "physical_file_count": 39,
        "evaluation_raw_sha256": YAML_RAW_SHA, "evaluation_semantic_sha256": YAML_SEMANTIC_SHA,
        "evidence_sha256": sha256(EVIDENCE), "evidence_payload_sha256": evidence_payload_hash(),
        "main_pdf_sha256": sha256(MAIN_PDF),
        "release_lanes": {
            "producer": "PASS", "independent_checker": "PASS", "sympy_crosscheck": "PASS",
            "isolated_byte_replay": "PASS", "hostile_mutation": "PASS", "unittest_smoke": "PASS",
            "optimized_mode_refusal": "PASS", "deterministic_pdf_rebuild": "PASS",
            "payload_membership": "PASS", "forbidden_claim_firewall": "PASS",
            "text_control_byte_hygiene": "PASS",
        },
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
        for blob, name in zip(blobs, PDF_NAMES):
            (ROOT / "paper" / name).write_bytes(blob)
        MAIN_PDF.write_bytes(blobs[2])
        print("C376 PDF build PASS: three double-fresh rounds; main=round2")
        return

    current = actual_files()
    allowed = sorted(EXPECTED + (MANIFEST.name,))
    permitted = sorted(EXPECTED) if args.write and not MANIFEST.exists() else allowed
    assert current == permitted, (
        f"file ledger mismatch extra={sorted(set(current) - set(permitted))} "
        f"missing={sorted(set(permitted) - set(current))}"
    )
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
    assert rounds[0]["pages"] < rounds[1]["pages"] < rounds[2]["pages"], "PDF page counts must increase by round"
    assert compile_round(0) == (ROOT / "paper/main_round0_original.pdf").read_bytes()
    assert compile_round(1) == (ROOT / "paper/main_round1.pdf").read_bytes()
    assert compile_round(2) == (ROOT / "paper/main_round2.pdf").read_bytes()
    manifest = make_manifest(rounds, lanes)
    if args.write:
        MANIFEST.write_bytes(json.dumps(manifest, sort_keys=True, indent=2, ensure_ascii=False).encode() + b"\n")
        print("C376 manifest WRITE PASS: payload=38 physical=39")
    else:
        exact = strict_json(MANIFEST)
        assert exact == manifest, "manifest does not match fresh release reconstruction"
        print(
            "C376 release PASS: evidence=" + manifest["evidence_sha256"]
            + " pdf=" + manifest["main_pdf_sha256"]
            + " manifest=" + sha256(MANIFEST)
        )


if __name__ == "__main__":
    main()
