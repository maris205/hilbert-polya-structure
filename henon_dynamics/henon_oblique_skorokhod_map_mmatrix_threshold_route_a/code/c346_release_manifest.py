#!/usr/bin/env python3
"""Uniform 27-payload release gate for HCS-C346."""
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
MANIFEST = ROOT / "C346_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c346_skorokhod_evidence.json"
TEX = ROOT / "paper/main.tex"
MAIN_PDF = ROOT / "paper/main.pdf"
EVALUATION = ROOT / "evaluations/route_a/HCS-C346/2026-09-03.yaml"
EPOCH = 1788393600
SOURCE = "1af63b945e19b5f94ac1cb76f93af5ac66d3d562"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVALUATOR_AUTHORITY = "flow_systems/skills/route-a-evaluator.md"
EVALUATION_RAW_SHA256 = "4cad63c30708b42af42f3ee1f3563e8d31b2de8ae08047170c6b93050474a36c"
EVALUATION_SEMANTIC_SHA256 = "a9363fdab6fc2cd797ced2beb1d1f277876db3afcd69cbf37a8ad7f9de18fe4a"
ROUND_PDFS = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
WARNING = re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c346_release_manifest.py", "code/c346_skorokhod_checker.py", "code/c346_skorokhod_mutation.py", "code/c346_skorokhod_producer.py", "code/c346_skorokhod_replay.py", "code/c346_skorokhod_sympy_crosscheck.py",
    "evaluations/route_a/HCS-C346/2026-09-03.yaml", "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md", "results/c346_skorokhod_evidence.json",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_lane(name: str) -> str:
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)], env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC"), text=True)


def optimized_refusal(name: str) -> None:
    command = [sys.executable, "-O", "-B", str(ROOT / "code" / name)]
    with tempfile.TemporaryDirectory(prefix="c346-opt-") as directory:
        if name == "c346_skorokhod_producer.py":
            command += ["--output", str(Path(directory) / "forbidden.json")]
        run = subprocess.run(command, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC"), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if run.returncode == 0 or "refuses optimized Python" not in run.stdout:
            raise AssertionError(f"optimized execution not explicitly refused: {name}")


def pages(path: Path) -> int:
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in output.splitlines() if line.startswith("Pages:")))


def fonts(path: Path) -> int:
    output = subprocess.check_output(["pdffonts", str(path)], text=True)
    rows = [line for line in output.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]
    if not rows or not all(len(line.split()) >= 7 and line.split()[-5:-3] == ["yes", "yes"] for line in rows):
        raise AssertionError(f"font embedding/subsetting failure: {path}")
    return len(rows)


def text_of(path: Path) -> str:
    output = subprocess.check_output(["pdftotext", "-layout", str(path), "-"], text=True).translate({16: ord("("), 17: ord(")"), 18: ord("("), 19: ord(")")})
    if "\ufffd" in output or any(ord(ch) < 32 and ch not in "\n\r\t\f" for ch in output):
        raise AssertionError(f"unsafe extracted PDF text: {path}")
    if "qquad" in output.lower():
        raise AssertionError(f"bare TeX command rendered in PDF: {path}: qquad")
    return " ".join(output.lower().split())


def raster(path: Path, count: int):
    sizes = []
    with tempfile.TemporaryDirectory(prefix="c346-raster-") as directory:
        directory = Path(directory)
        for page in range(1, count + 1):
            prefix = directory / f"page-{page}"
            subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "72", "-png", str(path), str(prefix)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            images = list(directory.glob(f"page-{page}-*.png"))
            if len(images) != 1 or images[0].stat().st_size < 1000:
                raise AssertionError("PDF raster failure")
            sizes.append(images[0].stat().st_size)
    return sizes


def fresh(round_number: int) -> bytes:
    with tempfile.TemporaryDirectory(prefix=f"c346-build-{round_number}-") as directory:
        work = Path(directory)
        shutil.copy2(TEX, work / "main.tex")
        env = dict(os.environ, SOURCE_DATE_EPOCH=str(EPOCH), FORCE_SOURCE_DATE="1", TZ="UTC")
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", source]
        for _ in range(2):
            subprocess.run(command, cwd=work, env=env, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        match = WARNING.search((work / "main.log").read_text(errors="replace"))
        if match:
            raise AssertionError(f"paper warning round {round_number}: {match.group(0)}")
        return (work / "main.pdf").read_bytes()


def evidence_payload_hash() -> str:
    data = json.loads(EVIDENCE.read_text(), parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
    body = dict(data)
    claimed = body.pop("payload_sha256")
    computed = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    if claimed != computed:
        raise AssertionError("stale evidence payload")
    return claimed


def build_manifest() -> dict:
    files = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file() and path != MANIFEST}
    if set(files) != EXPECTED or len(files) != 27:
        raise AssertionError(f"payload ledger mismatch: missing={sorted(EXPECTED-set(files))}, extra={sorted(set(files)-EXPECTED)}")
    if sha(EVALUATION) != EVALUATION_RAW_SHA256:
        raise AssertionError("evaluation raw digest")
    tokens = ("fixed point and sharp m-matrix chamber", "weighted stability, picard, and time change", "sharp wall, executable audit, and route-a boundary")
    pdf_rows = []
    for round_number, path in enumerate(ROUND_PDFS):
        count = pages(path)
        if tokens[round_number] not in text_of(path):
            raise AssertionError(f"revision token absent: {round_number}")
        pdf_rows.append({"round": round_number, "path": str(path.relative_to(ROOT)), "sha256": sha(path), "bytes": path.stat().st_size, "pages": count, "font_rows": fonts(path), "raster_bytes": raster(path, count)})
    if len({row["sha256"] for row in pdf_rows}) != 3:
        raise AssertionError("revision PDFs are not distinct")
    if MAIN_PDF.read_bytes() != ROUND_PDFS[2].read_bytes():
        raise AssertionError("main.pdf is not Round 2")
    return {
        "schema": "hcs-release-manifest-v1", "candidate_id": "HCS-C346", "obstruction_id": "HEN-O330", "source_commit": SOURCE, "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "evaluator_authority": EVALUATOR_AUTHORITY,
        "payload_file_count": 27, "physical_file_count": 28, "evaluation_raw_sha256": EVALUATION_RAW_SHA256, "evaluation_semantic_sha256": EVALUATION_SEMANTIC_SHA256,
        "evidence_sha256": sha(EVIDENCE), "evidence_payload_sha256": evidence_payload_hash(), "pdf_rounds": pdf_rows,
        "files": {name: sha(path) for name, path in sorted(files.items())},
    }


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C346 release refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    lanes = [
        ("c346_skorokhod_producer.py", "C346_PRODUCER_PASS"),
        ("c346_skorokhod_checker.py", "C346 independent checker: PASS"),
        ("c346_skorokhod_sympy_crosscheck.py", "C346 SymPy cross-check: PASS"),
        ("c346_skorokhod_replay.py", "C346 byte replay: PASS"),
        ("c346_skorokhod_mutation.py", "C346 hostile mutation suite: PASS"),
    ]
    for name, sentinel in lanes:
        if sentinel not in run_lane(name):
            raise AssertionError(f"lane sentinel absent: {name}")
        optimized_refusal(name)
    for round_number, path in enumerate(ROUND_PDFS):
        one, two = fresh(round_number), fresh(round_number)
        if one != two or one != path.read_bytes():
            raise AssertionError(f"stale or nondeterministic PDF: Round {round_number}")
    manifest = build_manifest()
    raw = json.dumps(manifest, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if args.write:
        MANIFEST.write_text(raw)
    elif not MANIFEST.exists() or MANIFEST.read_text() != raw:
        raise AssertionError("release manifest missing or stale")
    sidecars = [path for path in ROOT.rglob("*") if path.is_file() and (path.suffix in {".aux", ".log", ".out", ".toc", ".pyc"} or "__pycache__" in path.parts)]
    if sidecars:
        raise AssertionError(f"forbidden sidecars: {sidecars}")
    print(f"C346_RELEASE_PASS {sha(EVIDENCE)} {sha(MAIN_PDF)} {sha(MANIFEST)}")


if __name__ == "__main__":
    main()
