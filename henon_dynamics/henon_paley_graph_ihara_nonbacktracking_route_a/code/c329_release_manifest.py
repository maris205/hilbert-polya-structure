#!/usr/bin/env python3
"""Closed release and manifest verifier for HCS-C329."""
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
MANIFEST = ROOT / "C329_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c329_paley_ihara_evidence.json"
TEX = ROOT / "paper/main.tex"
PDF = ROOT / "paper/main.pdf"
ROUNDS = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf",
          ROOT / "paper/main_round2.pdf"]
SOURCE = "5ca65027918c0fce7ef9af82f3faf2e46ed6530c"
EPOCH = 1788393600
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
WARNING = re.compile(r"LaTeX Warning|Package .* Warning|Overfull|Underfull|Missing character|undefined reference", re.I)
CONTROL = re.compile(rb"[\x00-\x08\x0b\x0e-\x1f\x7f]")
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c329_paley_ihara_checker.py", "code/c329_paley_ihara_mutation.py",
    "code/c329_paley_ihara_producer.py", "code/c329_paley_ihara_replay.py",
    "code/c329_paley_ihara_sympy_crosscheck.py", "code/c329_release_manifest.py",
    "evaluations/route_a/HCS-C329/2026-09-03.yaml", "paper/COMPILE_REPORT.md", "paper/README.md",
    "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf",
    "paper/main_round2.pdf", "results/HOSTILE_AUDIT.md", "results/RESULTS.md",
    "results/TEST_REPORT.md", "results/c329_paley_ihara_evidence.json",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(script):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / script)],
                                   env=env, text=True)


def pages(path):
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in output.splitlines() if line.startswith("Pages:")))


def fonts(path):
    output = subprocess.check_output(["pdffonts", str(path)], text=True)
    rows = [line for line in output.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]
    if not rows or not all(len(row.split()) >= 7 and row.split()[-5] == "yes" and
                           row.split()[-4] == "yes" for row in rows):
        raise AssertionError("fonts not embedded and subset")
    return len(rows)


def extracted_bytes(path):
    raw = subprocess.check_output(["pdftotext", "-layout", str(path), "-"])
    if CONTROL.search(raw) or b"qquad" in raw.lower() or b"??" in raw or b"[verify]" in raw.lower():
        raise AssertionError("PDF extracted-text gate")
    return raw


def raster(path, count):
    sizes = []
    with tempfile.TemporaryDirectory(prefix="c329-raster-") as directory:
        for page in range(1, count + 1):
            prefix = Path(directory) / f"page{page}"
            subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "72",
                            "-png", str(path), str(prefix)], check=True,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            images = list(Path(directory).glob(f"page{page}-*.png"))
            if len(images) != 1 or images[0].stat().st_size < 1000:
                raise AssertionError("PDF raster gate")
            sizes.append(images[0].stat().st_size)
    return sizes


def fresh(round_number):
    with tempfile.TemporaryDirectory(prefix=f"c329-build-{round_number}-") as directory:
        work = Path(directory)
        shutil.copy2(TEX, work / "main.tex")
        env = dict(os.environ, SOURCE_DATE_EPOCH=str(EPOCH), FORCE_SOURCE_DATE="1", TZ="UTC")
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", source]
        for _ in range(2):
            subprocess.run(command, cwd=work, env=env, check=True, stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT, text=True)
        log = (work / "main.log").read_text(errors="replace")
        match = WARNING.search(log)
        if match:
            raise AssertionError(f"settled warning: {match.group(0)}")
        return (work / "main.pdf").read_bytes()


def expected_manifest():
    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*")
                if path.is_file() and path != MANIFEST}
    if set(physical) != EXPECTED or len(physical) != 27:
        raise AssertionError(f"payload mismatch missing={sorted(EXPECTED-set(physical))} extra={sorted(set(physical)-EXPECTED)}")
    for name, path in physical.items():
        if not name.endswith(".pdf") and CONTROL.search(path.read_bytes()):
            raise AssertionError(f"control character in {name}")
    evidence = json.loads(EVIDENCE.read_text())
    body = dict(evidence)
    payload = body.pop("payload_sha256")
    if payload != hashlib.sha256(json.dumps(
            body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest():
        raise AssertionError("evidence payload")
    tokens = ("frozen paley graph and character spectrum",
              "bass spectrum and primitive-cycle closure",
              "finite-field representation and route-a boundary")
    receipts = []
    for number, path in enumerate(ROUNDS):
        count = pages(path)
        raw = extracted_bytes(path)
        normalized = " ".join(raw.decode("utf-8").lower().split())
        if tokens[number] not in normalized:
            raise AssertionError(f"round certificate {number}")
        receipts.append({"round": number, "path": str(path.relative_to(ROOT)),
                         "sha256": sha(path), "bytes": path.stat().st_size, "pages": count,
                         "font_rows": fonts(path), "raster_bytes": raster(path, count)})
    if len({row["sha256"] for row in receipts}) != 3 or PDF.read_bytes() != ROUNDS[2].read_bytes():
        raise AssertionError("round distinction or final alias")
    return {"schema": "hcs-release-manifest-v1", "candidate_id": "HCS-C329",
            "obstruction_id": "HEN-O313", "source_commit": SOURCE, "fixed_epoch": EPOCH,
            "scope_literal": SCOPE, "payload_file_count": 27, "physical_file_count": 28,
            "evidence_sha256": sha(EVIDENCE), "evidence_payload_sha256": payload,
            "pdf_rounds": receipts,
            "files": {name: sha(path) for name, path in sorted(physical.items())}}


def main():
    if sys.flags.optimize:
        raise RuntimeError("C329 release refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    sentinels = [
        ("c329_paley_ihara_producer.py", "C329_PRODUCER_PASS"),
        ("c329_paley_ihara_checker.py", "C329 independent checker: PASS"),
        ("c329_paley_ihara_sympy_crosscheck.py", "C329 SymPy cross-check: PASS"),
        ("c329_paley_ihara_replay.py", "C329 byte replay: PASS"),
        ("c329_paley_ihara_mutation.py", "C329 hostile mutation suite: PASS"),
    ]
    for script, sentinel in sentinels:
        if sentinel not in run(script):
            raise AssertionError(f"failed lane {script}")
    for number, archive in enumerate(ROUNDS):
        first, second = fresh(number), fresh(number)
        if first != second or first != archive.read_bytes():
            raise AssertionError(f"nondeterministic PDF round {number}")
    manifest = expected_manifest()
    rendered = json.dumps(manifest, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if args.write:
        MANIFEST.write_text(rendered)
    elif not MANIFEST.exists() or MANIFEST.read_text() != rendered:
        raise AssertionError("manifest stale")
    sidecars = {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
    if any(path.suffix in sidecars or "__pycache__" in path.parts
           for path in ROOT.rglob("*") if path.is_file()):
        raise AssertionError("build sidecar")
    print(f"C329_RELEASE_PASS {sha(EVIDENCE)} {sha(PDF)} {sha(MANIFEST)}")


if __name__ == "__main__":
    main()
