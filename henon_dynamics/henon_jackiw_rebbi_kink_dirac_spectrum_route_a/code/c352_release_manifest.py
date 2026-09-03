#!/usr/bin/env python3
"""Final 27-payload release gate and manifest writer for HCS-C352."""
from __future__ import annotations

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
MANIFEST = ROOT / "C352_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c352_jackiw_rebbi_evidence.json"
TEX = ROOT / "paper/main.tex"
MAIN_PDF = ROOT / "paper/main.pdf"
EVALUATION = ROOT / "evaluations/route_a/HCS-C352/2026-09-03.yaml"
SOURCE = "327fc1172cebcdeb17adfd2d8ad12636fbb94f52"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
EVALUATION_RAW_SHA256 = "232e3fce6d9acd33d2700f461be42d3ca4f2491e76df298ecbcbfb0f3a56c827"
EVALUATION_SEMANTIC_SHA256 = "64d65968f25f0a7d94a681de29c7e3ffd5e2291013921e9ca2e52266b2c08d4b"
ROUND_PDFS = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf",
              ROOT / "paper/main_round2.pdf"]
WARNING = re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|"
                     r"undefined (?:references|citations)|Rerun to get|Missing character")
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "code/README.md", "code/c352_jackiw_rebbi_checker.py",
    "code/c352_jackiw_rebbi_mutation.py", "code/c352_jackiw_rebbi_producer.py",
    "code/c352_jackiw_rebbi_replay.py", "code/c352_jackiw_rebbi_sympy_crosscheck.py",
    "code/c352_release_manifest.py", "evaluations/route_a/HCS-C352/2026-09-03.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c352_jackiw_rebbi_evidence.json",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_lane(name):
    command = [sys.executable, "-B", str(ROOT / "code" / name)]
    with tempfile.TemporaryDirectory(prefix="c352-lane-") as directory:
        if name == "c352_jackiw_rebbi_producer.py":
            output = Path(directory) / "evidence.json"
            command.extend(["--output", str(output)])
        result = subprocess.check_output(command,
            env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC"), text=True)
        if name == "c352_jackiw_rebbi_producer.py" and output.read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("producer output differs from checked evidence")
        return result


def check_optimized_refusal(name):
    for flag in ("-O", "-OO"):
        command = [sys.executable, flag, "-B", str(ROOT / "code" / name)]
        with tempfile.TemporaryDirectory(prefix="c352-opt-") as directory:
            if name == "c352_jackiw_rebbi_producer.py":
                command.extend(["--output", str(Path(directory) / "forbidden.json")])
            process = subprocess.run(command,
                env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC"),
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if process.returncode == 0 or "refuses optimized Python" not in process.stdout:
                raise AssertionError(f"optimized execution not explicitly refused: {flag} {name}")


def pages(path):
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in output.splitlines()
                    if line.startswith("Pages:")))


def font_rows(path):
    output = subprocess.check_output(["pdffonts", str(path)], text=True)
    rows = [line for line in output.splitlines()[2:]
            if line.strip() and not line.lstrip().startswith("-")]
    if not rows:
        raise AssertionError(f"no fonts: {path}")
    for line in rows:
        fields = line.split()
        if len(fields) < 7 or fields[-5] != "yes" or fields[-4] != "yes":
            raise AssertionError(f"font not embedded and subset: {path}: {line}")
    return len(rows)


def extracted_text(path):
    raw = subprocess.check_output(["pdftotext", "-layout", str(path), "-"])
    normalized = raw.replace(b"\x12", b"").replace(b"\x13", b"")
    if re.search(rb"[\x00-\x08\x0b\x0e-\x1f\x7f]", normalized):
        raise AssertionError(f"extracted-text control character: {path}")
    text = raw.decode("utf-8")
    lowered = text.lower()
    for forbidden in ("qquad", "quadb", "??", "[verify]", "todo", "fixme", "missing glyph"):
        if forbidden in lowered:
            raise AssertionError(f"draft/TeX garbage: {path}: {forbidden}")
    return " ".join(lowered.split())


def raster_sizes(path, count):
    answer = []
    with tempfile.TemporaryDirectory(prefix="c352-raster-") as directory:
        work = Path(directory)
        for page in range(1, count + 1):
            prefix = work / f"page-{page}"
            subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "96",
                            "-png", str(path), str(prefix)], check=True,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            images = list(work.glob(f"page-{page}-*.png"))
            if len(images) != 1 or images[0].stat().st_size < 1000:
                raise AssertionError(f"raster failure: {path} page {page}")
            answer.append(images[0].stat().st_size)
    return answer


def fresh_build(round_number):
    with tempfile.TemporaryDirectory(prefix=f"c352-build-{round_number}-") as directory:
        work = Path(directory)
        shutil.copy2(TEX, work / "main.tex")
        environment = dict(os.environ, SOURCE_DATE_EPOCH=str(EPOCH),
                           FORCE_SOURCE_DATE="1", TZ="UTC")
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error",
                   "-jobname=main", source]
        for _ in range(2):
            subprocess.run(command, cwd=work, env=environment, check=True,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = (work / "main.log").read_text(errors="replace")
        match = WARNING.search(log)
        if match:
            raise AssertionError(f"paper warning in round {round_number}: {match.group(0)}")
        return (work / "main.pdf").read_bytes()


def pairs(items):
    answer = {}
    for key, value in items:
        if key in answer:
            raise ValueError("duplicate evidence key")
        answer[key] = value
    return answer


def evidence_payload_hash():
    data = json.loads(EVIDENCE.read_text(), object_pairs_hook=pairs,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    body = dict(data)
    claimed = body.pop("payload_sha256")
    computed = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"),
                                         ensure_ascii=False).encode()).hexdigest()
    if claimed != computed:
        raise AssertionError("stale evidence payload hash")
    return claimed


def build_manifest():
    files = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*")
             if path.is_file() and path != MANIFEST}
    if set(files) != EXPECTED or len(files) != 27:
        raise AssertionError(f"payload mismatch missing={sorted(EXPECTED-set(files))} "
                             f"extra={sorted(set(files)-EXPECTED)}")
    if sha(EVALUATION) != EVALUATION_RAW_SHA256:
        raise AssertionError("evaluation raw-byte digest")
    tokens = ("domain, factorization, and complete discrete-ladder closure",
              "round-one threshold-resonance and reflectionless-scattering closure",
              "round-two spectral-type, boundary, evidence, and route-a closure")
    pdf_rows = []
    for round_number, path in enumerate(ROUND_PDFS):
        count = pages(path)
        text = extracted_text(path)
        if tokens[round_number] not in text:
            raise AssertionError(f"revision token absent: round {round_number}")
        if path.stat().st_size < 30000:
            raise AssertionError(f"implausibly small PDF: {path}")
        pdf_rows.append({"round": round_number, "path": str(path.relative_to(ROOT)),
            "sha256": sha(path), "bytes": path.stat().st_size, "pages": count,
            "font_rows": font_rows(path), "raster_bytes": raster_sizes(path, count)})
    if len({row["sha256"] for row in pdf_rows}) != 3:
        raise AssertionError("revision PDFs not distinct")
    if MAIN_PDF.read_bytes() != ROUND_PDFS[2].read_bytes():
        raise AssertionError("main.pdf is not round 2")
    return {
        "schema": "hcs-release-manifest-v1", "candidate_id": "HCS-C352",
        "obstruction_id": "HEN-O336", "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
        "payload_file_count": 27, "physical_file_count": 28,
        "evaluation_raw_sha256": EVALUATION_RAW_SHA256,
        "evaluation_semantic_sha256": EVALUATION_SEMANTIC_SHA256,
        "evidence_sha256": sha(EVIDENCE), "evidence_payload_sha256": evidence_payload_hash(),
        "pdf_rounds": pdf_rows,
        "files": {name: sha(path) for name, path in sorted(files.items())},
    }


def main():
    if sys.flags.optimize:
        raise RuntimeError("C352 release refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    lanes = [
        ("c352_jackiw_rebbi_producer.py", "C352_PRODUCER_PASS"),
        ("c352_jackiw_rebbi_checker.py", "C352 independent Jackiw-Rebbi checker: PASS"),
        ("c352_jackiw_rebbi_sympy_crosscheck.py", "C352 SymPy cross-check: PASS"),
        ("c352_jackiw_rebbi_replay.py", "C352 byte replay: PASS"),
        ("c352_jackiw_rebbi_mutation.py", "C352 hostile mutation suite: PASS"),
    ]
    for name, sentinel in lanes:
        output = run_lane(name)
        if sentinel not in output:
            raise AssertionError(f"lane sentinel absent: {name}")
        check_optimized_refusal(name)
    for round_number, checked in enumerate(ROUND_PDFS):
        first, second = fresh_build(round_number), fresh_build(round_number)
        if first != second or first != checked.read_bytes():
            raise AssertionError(f"nondeterministic or stale PDF round {round_number}")
    manifest = build_manifest()
    raw = json.dumps(manifest, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if args.write:
        MANIFEST.write_text(raw)
    elif not MANIFEST.exists() or MANIFEST.read_text() != raw:
        raise AssertionError("release manifest missing or stale")
    sidecars = [path for path in ROOT.rglob("*") if path.is_file()
                and (path.suffix in {".aux", ".log", ".out", ".toc", ".pyc"}
                     or "__pycache__" in path.parts)]
    if sidecars:
        raise AssertionError(f"forbidden build sidecars: {sidecars}")
    print(f"C352_RELEASE_PASS {sha(EVIDENCE)} {sha(MAIN_PDF)} {sha(MANIFEST)}")


if __name__ == "__main__":
    main()
