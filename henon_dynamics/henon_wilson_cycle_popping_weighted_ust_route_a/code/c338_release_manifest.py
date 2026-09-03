#!/usr/bin/env python3
"""Final 27-payload release gate and manifest writer for HCS-C338."""
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
MANIFEST = ROOT / "C338_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c338_wilson_ust_evidence.json"
TEX = ROOT / "paper/main.tex"
MAIN_PDF = ROOT / "paper/main.pdf"
EVALUATION = ROOT / "evaluations/route_a/HCS-C338/2026-09-03.yaml"
SOURCE = "db2c816b7b6bd450f51f79b91842cb882b0bd773"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
EVALUATION_RAW_SHA256 = "6fb6f931958632647dc29888e728ba08fedb1657dee2bc529cbf87e23008a981"
EVALUATION_SEMANTIC_SHA256 = "9555a89d78499a4125b90b0c9a3db1ac64a83f369cecbbea31e5a8da77d85325"
ROUND_PDFS = [
    ROOT / "paper/main_round0_original.pdf",
    ROOT / "paper/main_round1.pdf",
    ROOT / "paper/main_round2.pdf",
]
WARNING = re.compile(
    r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|"
    r"undefined (?:references|citations)|Rerun to get|Missing character"
)
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
    "code/c338_release_manifest.py",
    "code/c338_wilson_ust_checker.py",
    "code/c338_wilson_ust_mutation.py",
    "code/c338_wilson_ust_producer.py",
    "code/c338_wilson_ust_replay.py",
    "code/c338_wilson_ust_sympy_crosscheck.py",
    "evaluations/route_a/HCS-C338/2026-09-03.yaml",
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
    "results/c338_wilson_ust_evidence.json",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_lane(name):
    return subprocess.check_output(
        [sys.executable, "-B", str(ROOT / "code" / name)],
        env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC"), text=True,
    )


def check_optimized_refusal(name):
    for flag in ("-O", "-OO"):
        command = [sys.executable, flag, "-B", str(ROOT / "code" / name)]
        with tempfile.TemporaryDirectory(prefix="c338-opt-") as directory:
            if name == "c338_wilson_ust_producer.py":
                command.extend(["--output", str(Path(directory) / "forbidden.json")])
            process = subprocess.run(
                command, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC"),
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
            )
            if process.returncode == 0 or "refuses optimized Python" not in process.stdout:
                raise AssertionError(f"optimized execution not explicitly refused: {flag} {name}")


def pages(path):
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in output.splitlines() if line.startswith("Pages:")))


def font_rows(path):
    output = subprocess.check_output(["pdffonts", str(path)], text=True)
    rows = [line for line in output.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]
    if not rows:
        raise AssertionError(f"no fonts listed: {path}")
    if not all(len(line.split()) >= 7 and line.split()[-5] == "yes" and line.split()[-4] == "yes"
               for line in rows):
        raise AssertionError(f"font not embedded and subset: {path}")
    return len(rows)


def extracted_text(path):
    raw = subprocess.check_output(["pdftotext", "-layout", str(path), "-"])
    if re.search(rb"[\x00-\x08\x0b\x0e-\x1f\x7f]", raw):
        raise AssertionError(f"forbidden extracted-text control character: {path}")
    output = raw.decode("utf-8")
    lowered = output.lower()
    for forbidden in ("qquad", "??", "[verify]", "todo", "fixme", "missing glyph"):
        if forbidden in lowered:
            raise AssertionError(f"literal drafting/TeX garbage in extracted text: {path}: {forbidden}")
    return " ".join(lowered.split())


def raster_sizes(path, count):
    sizes = []
    with tempfile.TemporaryDirectory(prefix="c338-raster-") as directory:
        work = Path(directory)
        for page in range(1, count + 1):
            prefix = work / f"page-{page}"
            subprocess.run(
                ["pdftoppm", "-f", str(page), "-l", str(page), "-r", "96", "-png",
                 str(path), str(prefix)], check=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            )
            images = list(work.glob(f"page-{page}-*.png"))
            if len(images) != 1 or images[0].stat().st_size < 1000:
                raise AssertionError(f"raster failure: {path}, page {page}")
            sizes.append(images[0].stat().st_size)
    return sizes


def fresh_build(round_number):
    with tempfile.TemporaryDirectory(prefix=f"c338-build-{round_number}-") as directory:
        work = Path(directory)
        shutil.copy2(TEX, work / "main.tex")
        environment = dict(os.environ, SOURCE_DATE_EPOCH=str(EPOCH), FORCE_SOURCE_DATE="1", TZ="UTC")
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", source]
        for _ in range(2):
            subprocess.run(command, cwd=work, env=environment, check=True,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = (work / "main.log").read_text(errors="replace")
        match = WARNING.search(log)
        if match:
            raise AssertionError(f"paper warning in round {round_number}: {match.group(0)}")
        return (work / "main.pdf").read_bytes()


def evidence_payload_hash():
    def duplicate_pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError("duplicate evidence key")
            result[key] = value
        return result

    data = json.loads(EVIDENCE.read_text(), object_pairs_hook=duplicate_pairs,
                      parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    body = dict(data)
    claimed = body.pop("payload_sha256")
    computed = hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    if claimed != computed:
        raise AssertionError("stale evidence payload hash")
    return claimed


def build_manifest():
    files = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*")
             if path.is_file() and path != MANIFEST}
    if set(files) != EXPECTED or len(files) != 27:
        raise AssertionError(
            f"payload ledger mismatch: missing={sorted(EXPECTED-set(files))}, "
            f"extra={sorted(set(files)-EXPECTED)}")
    if sha(EVALUATION) != EVALUATION_RAW_SHA256:
        raise AssertionError("evaluation raw-byte digest mismatch")
    tokens = ("core stochastic closure", "determinantal boundary closure", "route firewall receipt")
    pdf_rows = []
    for round_number, path in enumerate(ROUND_PDFS):
        count = pages(path)
        text = extracted_text(path)
        if tokens[round_number] not in text:
            raise AssertionError(f"revision token absent from round {round_number}")
        if path.stat().st_size < 30000:
            raise AssertionError(f"implausibly small PDF: {path}")
        pdf_rows.append({
            "round": round_number,
            "path": str(path.relative_to(ROOT)),
            "sha256": sha(path),
            "bytes": path.stat().st_size,
            "pages": count,
            "font_rows": font_rows(path),
            "raster_bytes": raster_sizes(path, count),
        })
    if len({row["sha256"] for row in pdf_rows}) != 3:
        raise AssertionError("revision PDFs are not substantively distinct")
    if MAIN_PDF.read_bytes() != ROUND_PDFS[2].read_bytes():
        raise AssertionError("main.pdf is not the final revision")
    return {
        "schema": "hcs-release-manifest-v1",
        "candidate_id": "HCS-C338",
        "obstruction_id": "HEN-O322",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
        "payload_file_count": 27,
        "physical_file_count": 28,
        "evaluation_raw_sha256": EVALUATION_RAW_SHA256,
        "evaluation_semantic_sha256": EVALUATION_SEMANTIC_SHA256,
        "evidence_sha256": sha(EVIDENCE),
        "evidence_payload_sha256": evidence_payload_hash(),
        "pdf_rounds": pdf_rows,
        "files": {name: sha(path) for name, path in sorted(files.items())},
    }


def main():
    if sys.flags.optimize:
        raise RuntimeError("C338 release refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    lanes = [
        ("c338_wilson_ust_producer.py", "C338_PRODUCER_PASS"),
        ("c338_wilson_ust_checker.py", "C338 independent Wilson/UST checker: PASS"),
        ("c338_wilson_ust_sympy_crosscheck.py", "C338 SymPy cross-check: PASS"),
        ("c338_wilson_ust_replay.py", "C338 byte replay: PASS"),
        ("c338_wilson_ust_mutation.py", "C338 hostile mutation suite: PASS"),
    ]
    for name, sentinel in lanes:
        output = run_lane(name)
        if sentinel not in output:
            raise AssertionError(f"lane sentinel absent: {name}")
        check_optimized_refusal(name)
    for round_number, checked_in in enumerate(ROUND_PDFS):
        first = fresh_build(round_number)
        second = fresh_build(round_number)
        if first != second or first != checked_in.read_bytes():
            raise AssertionError(f"nondeterministic or stale PDF round {round_number}")
    manifest = build_manifest()
    raw = json.dumps(manifest, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if args.write:
        MANIFEST.write_text(raw)
    elif not MANIFEST.exists() or MANIFEST.read_text() != raw:
        raise AssertionError("release manifest is missing or stale")
    sidecars = [path for path in ROOT.rglob("*") if path.is_file()
                and (path.suffix in {".aux", ".log", ".out", ".toc", ".pyc"}
                     or "__pycache__" in path.parts)]
    if sidecars:
        raise AssertionError(f"forbidden build sidecars: {sidecars}")
    print(f"C338_RELEASE_PASS {sha(EVIDENCE)} {sha(MAIN_PDF)} {sha(MANIFEST)}")


if __name__ == "__main__":
    main()
