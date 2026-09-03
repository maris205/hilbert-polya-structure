#!/usr/bin/env python3
"""Closed-release verifier and manifest writer for HCS-C321."""
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
MANIFEST = ROOT / "C321_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c321_preferential_attachment_evidence.json"
TEX = ROOT / "paper/main.tex"
PDF = ROOT / "paper/main.pdf"
ROUNDS = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf",
          ROOT / "paper/main_round2.pdf"]
SOURCE = "1ccbfe2d759fe007c6b53c9646e1ab031878b34a"
EPOCH = 1788393600
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
WARNING = re.compile(r"LaTeX Warning|Package .* Warning|Overfull|Underfull|Missing character|undefined reference", re.I)
CONTROL = re.compile(rb"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")

EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c321_preferential_attachment_checker.py",
    "code/c321_preferential_attachment_mutation.py", "code/c321_preferential_attachment_producer.py",
    "code/c321_preferential_attachment_replay.py", "code/c321_preferential_attachment_sympy_crosscheck.py",
    "code/c321_release_manifest.py", "evaluations/route_a/HCS-C321/2026-09-03.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c321_preferential_attachment_evidence.json",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sidecar(path: Path) -> bool:
    return (path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
            or "__pycache__" in path.parts or path.name.endswith(".synctex.gz"))


def run(name: str) -> str:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)],
                                   env=env, text=True)


def pdf_pages(path: Path) -> int:
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in output.splitlines() if line.startswith("Pages:")))


def font_count(path: Path) -> int:
    output = subprocess.check_output(["pdffonts", str(path)], text=True)
    rows = [line for line in output.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]
    if not rows or not all(len(row.split()) >= 7 and row.split()[-5] == "yes" and row.split()[-4] == "yes"
                           for row in rows):
        raise AssertionError("fonts are not embedded and subset")
    return len(rows)


def pdf_text(path: Path) -> str:
    output = subprocess.check_output(["pdftotext", "-layout", str(path), "-"], text=True)
    return " ".join(output.lower().split())


def raster(path: Path, pages: int) -> list[int]:
    sizes = []
    with tempfile.TemporaryDirectory(prefix="c321-raster-") as directory:
        for page in range(1, pages + 1):
            prefix = Path(directory) / f"p{page}"
            subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "72", "-png",
                            str(path), str(prefix)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            found = list(Path(directory).glob(f"p{page}-*.png"))
            if len(found) != 1 or found[0].stat().st_size < 1000:
                raise AssertionError("PDF raster failure")
            sizes.append(found[0].stat().st_size)
    return sizes


def fresh(round_number: int) -> bytes:
    with tempfile.TemporaryDirectory(prefix=f"c321-build-{round_number}-") as directory:
        work = Path(directory)
        shutil.copy2(TEX, work / "main.tex")
        env = dict(os.environ, SOURCE_DATE_EPOCH=str(EPOCH), FORCE_SOURCE_DATE="1", TZ="UTC")
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", source]
        for _ in range(2):
            subprocess.run(command, cwd=work, env=env, check=True,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = (work / "main.log").read_text(errors="replace")
        match = WARNING.search(log)
        if match:
            raise AssertionError(f"settled LaTeX warning: {match.group(0)}")
        return (work / "main.pdf").read_bytes()


def strict_json(path: Path):
    def pairs(items):
        out = {}
        for key, value in items:
            if key in out:
                raise ValueError("duplicate JSON key")
            out[key] = value
        return out
    return json.loads(path.read_text(), object_pairs_hook=pairs,
                      parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))


def expected_manifest() -> dict:
    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*")
                if path.is_file() and path != MANIFEST}
    if set(physical) != EXPECTED or len(physical) != 27:
        raise AssertionError(f"payload ledger mismatch missing={sorted(EXPECTED-set(physical))} extra={sorted(set(physical)-EXPECTED)}")
    if CONTROL.search(TEX.read_bytes()):
        raise AssertionError("control character in TeX source")
    evidence = strict_json(EVIDENCE)
    body = dict(evidence)
    payload = body.pop("payload_sha256")
    semantic = hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"),
                                           ensure_ascii=False).encode()).hexdigest()
    if semantic != payload:
        raise AssertionError("evidence payload hash")
    tokens = (
        "revision certificate: convention and exact factorial law",
        "revision certificate: both microscopic and macroscopic limits",
        "revision certificate: independent evidence and scope closure",
    )
    rows = []
    for number, path in enumerate(ROUNDS):
        pages = pdf_pages(path)
        if tokens[number] not in pdf_text(path):
            raise AssertionError(f"revision token absent for round {number}")
        rows.append({"round": number, "path": str(path.relative_to(ROOT)), "sha256": sha(path),
                     "bytes": path.stat().st_size, "pages": pages, "font_rows": font_count(path),
                     "raster_bytes": raster(path, pages)})
    if len({row["sha256"] for row in rows}) != 3 or PDF.read_bytes() != ROUNDS[2].read_bytes():
        raise AssertionError("round archives or final alias")
    return {
        "schema": "hcs-release-manifest-v1", "candidate_id": "HCS-C321", "obstruction_id": "HEN-O305",
        "source_commit": SOURCE, "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "payload_file_count": 27, "physical_file_count": 28,
        "evidence_sha256": sha(EVIDENCE), "evidence_payload_sha256": payload,
        "pdf_rounds": rows,
        "files": {name: sha(path) for name, path in sorted(physical.items())},
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if sys.flags.optimize:
        raise RuntimeError("C321 release refuses optimized Python")
    sentinels = [
        ("c321_preferential_attachment_producer.py", "C321_PRODUCER_PASS"),
        ("c321_preferential_attachment_checker.py", "C321 independent checker: PASS"),
        ("c321_preferential_attachment_sympy_crosscheck.py", "C321 SymPy cross-check: PASS"),
        ("c321_preferential_attachment_replay.py", "C321 byte replay: PASS"),
        ("c321_preferential_attachment_mutation.py", "C321 hostile mutation suite: PASS"),
    ]
    for name, sentinel in sentinels:
        if sentinel not in run(name):
            raise AssertionError(f"lane failed: {name}")
    for number, archive in enumerate(ROUNDS):
        first = fresh(number)
        second = fresh(number)
        if first != second or first != archive.read_bytes():
            raise AssertionError(f"nondeterministic PDF round {number}")
    manifest = expected_manifest()
    rendered = json.dumps(manifest, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if args.write:
        MANIFEST.write_text(rendered)
    elif not MANIFEST.exists() or MANIFEST.read_text() != rendered:
        raise AssertionError("manifest absent or stale")
    all_files = [path for path in ROOT.rglob("*") if path.is_file()]
    if any(sidecar(path) for path in all_files):
        raise AssertionError("build sidecar present")
    print(f"C321_RELEASE_PASS {sha(EVIDENCE)} {sha(PDF)} {sha(MANIFEST)}")


if __name__ == "__main__":
    main()
