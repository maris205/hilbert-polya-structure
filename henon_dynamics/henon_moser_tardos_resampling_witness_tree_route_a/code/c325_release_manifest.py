#!/usr/bin/env python3
"""Closed release and manifest verifier for HCS-C325."""
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
MANIFEST = ROOT / "C325_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c325_moser_tardos_evidence.json"
TEX = ROOT / "paper/main.tex"
PDF = ROOT / "paper/main.pdf"
ROUNDS = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf",
          ROOT / "paper/main_round2.pdf"]
SOURCE = "1aba1f6fd0cf81baa7c137a2ce7ce3d097ba63fc"
EPOCH = 1788393600
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
WARNING = re.compile(r"LaTeX Warning|Package .* Warning|Overfull|Underfull|Missing character|undefined reference", re.I)
CONTROL = re.compile(rb"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c325_moser_tardos_checker.py", "code/c325_moser_tardos_mutation.py",
    "code/c325_moser_tardos_producer.py", "code/c325_moser_tardos_replay.py",
    "code/c325_moser_tardos_sympy_crosscheck.py", "code/c325_release_manifest.py",
    "evaluations/route_a/HCS-C325/2026-09-03.yaml", "paper/COMPILE_REPORT.md", "paper/README.md",
    "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf",
    "paper/main_round2.pdf", "results/HOSTILE_AUDIT.md", "results/RESULTS.md",
    "results/TEST_REPORT.md", "results/c325_moser_tardos_evidence.json",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(script):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / script)], env=env, text=True)


def pages(path):
    out = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in out.splitlines() if line.startswith("Pages:")))


def fonts(path):
    out = subprocess.check_output(["pdffonts", str(path)], text=True)
    rows = [line for line in out.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]
    if not rows or not all(len(row.split()) >= 7 and row.split()[-5] == "yes" and row.split()[-4] == "yes" for row in rows):
        raise AssertionError("fonts not embedded/subset")
    return len(rows)


def text(path):
    return " ".join(subprocess.check_output(["pdftotext", "-layout", str(path), "-"], text=True).lower().split())


def raster(path, count):
    sizes = []
    with tempfile.TemporaryDirectory(prefix="c325-raster-") as directory:
        for page in range(1, count + 1):
            prefix = Path(directory) / f"p{page}"
            subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "72", "-png",
                            str(path), str(prefix)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            images = list(Path(directory).glob(f"p{page}-*.png"))
            if len(images) != 1 or images[0].stat().st_size < 1000:
                raise AssertionError("raster")
            sizes.append(images[0].stat().st_size)
    return sizes


def fresh(number):
    with tempfile.TemporaryDirectory(prefix=f"c325-build-{number}-") as directory:
        work = Path(directory); shutil.copy2(TEX, work / "main.tex")
        env = dict(os.environ, SOURCE_DATE_EPOCH=str(EPOCH), FORCE_SOURCE_DATE="1", TZ="UTC")
        source = rf"\def\CRevisionRound{{{number}}}\input{{main.tex}}"
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
        raise AssertionError(f"payload ledger mismatch missing={sorted(EXPECTED-set(physical))} extra={sorted(set(physical)-EXPECTED)}")
    for name, path in physical.items():
        if not name.endswith(".pdf") and CONTROL.search(path.read_bytes()):
            raise AssertionError(f"control character: {name}")
    evidence = json.loads(EVIDENCE.read_text())
    body = dict(evidence); payload = body.pop("payload_sha256")
    if payload != hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"),
                                              ensure_ascii=False).encode()).hexdigest():
        raise AssertionError("evidence payload")
    tokens = ("revision certificate: frozen resampling dynamics and exact chains",
              "revision certificate: complete witness-tree and branching proof",
              "revision certificate: arbitrary-rule robustness and scope closure")
    receipts = []
    for number, path in enumerate(ROUNDS):
        count = pages(path); extracted = text(path)
        if tokens[number] not in extracted or "qquad" in extracted or "??" in extracted:
            raise AssertionError(f"text gate round {number}")
        receipts.append({"round": number, "path": str(path.relative_to(ROOT)), "sha256": sha(path),
                         "bytes": path.stat().st_size, "pages": count, "font_rows": fonts(path),
                         "raster_bytes": raster(path, count)})
    if len({row["sha256"] for row in receipts}) != 3 or PDF.read_bytes() != ROUNDS[2].read_bytes():
        raise AssertionError("round distinction/final alias")
    return {"schema": "hcs-release-manifest-v1", "candidate_id": "HCS-C325",
            "obstruction_id": "HEN-O309", "source_commit": SOURCE, "fixed_epoch": EPOCH,
            "scope_literal": SCOPE, "payload_file_count": 27, "physical_file_count": 28,
            "evidence_sha256": sha(EVIDENCE), "evidence_payload_sha256": payload,
            "pdf_rounds": receipts, "files": {name: sha(path) for name, path in sorted(physical.items())}}


def main():
    if sys.flags.optimize:
        raise RuntimeError("C325 release refuses optimized Python")
    parser = argparse.ArgumentParser(); parser.add_argument("--write", action="store_true"); args = parser.parse_args()
    sentinels = [("c325_moser_tardos_producer.py", "C325_PRODUCER_PASS"),
                 ("c325_moser_tardos_checker.py", "C325 independent checker: PASS"),
                 ("c325_moser_tardos_sympy_crosscheck.py", "C325 SymPy cross-check: PASS"),
                 ("c325_moser_tardos_replay.py", "C325 byte replay: PASS"),
                 ("c325_moser_tardos_mutation.py", "C325 hostile mutation suite: PASS")]
    for script, sentinel in sentinels:
        if sentinel not in run(script):
            raise AssertionError(f"lane: {script}")
    for number, archive in enumerate(ROUNDS):
        first, second = fresh(number), fresh(number)
        if first != second or first != archive.read_bytes():
            raise AssertionError(f"nondeterministic round {number}")
    manifest = expected_manifest()
    rendered = json.dumps(manifest, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if args.write:
        MANIFEST.write_text(rendered)
    elif not MANIFEST.exists() or MANIFEST.read_text() != rendered:
        raise AssertionError("manifest stale")
    sidecars = {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
    if any(path.suffix in sidecars or "__pycache__" in path.parts for path in ROOT.rglob("*") if path.is_file()):
        raise AssertionError("build sidecar")
    print(f"C325_RELEASE_PASS {sha(EVIDENCE)} {sha(PDF)} {sha(MANIFEST)}")


if __name__ == "__main__":
    main()
