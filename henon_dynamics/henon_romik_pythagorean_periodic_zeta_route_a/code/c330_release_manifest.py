#!/usr/bin/env python3
"""Closed release and manifest verifier for HCS-C330."""
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
MANIFEST = ROOT / "C330_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c330_romik_pythagorean_evidence.json"
TEX = ROOT / "paper/main.tex"
PDF = ROOT / "paper/main.pdf"
ROUNDS = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf",
          ROOT / "paper/main_round2.pdf"]
SOURCE = "5ca65027918c0fce7ef9af82f3faf2e46ed6530c"
EPOCH = 1788393600
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
WARNING = re.compile(
    r"LaTeX Warning|Package .* Warning|Overfull|Underfull|Missing character|undefined reference",
    re.I,
)
CONTROL = re.compile(rb"[\x00-\x08\x0b\x0e-\x1f\x7f]")
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c330_romik_pythagorean_checker.py",
    "code/c330_romik_pythagorean_mutation.py", "code/c330_romik_pythagorean_producer.py",
    "code/c330_romik_pythagorean_replay.py", "code/c330_romik_pythagorean_sympy_crosscheck.py",
    "code/c330_release_manifest.py", "evaluations/route_a/HCS-C330/2026-09-03.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c330_romik_pythagorean_evidence.json",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(script: str) -> str:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    return subprocess.check_output(
        [sys.executable, "-B", str(ROOT / "code" / script)], env=env, text=True
    )


def pages(path: Path) -> int:
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in output.splitlines()
                    if line.startswith("Pages:")))


def fonts(path: Path) -> int:
    output = subprocess.check_output(["pdffonts", str(path)], text=True)
    rows = [line for line in output.splitlines()[2:]
            if line.strip() and not line.lstrip().startswith("-")]
    if not rows or not all(len(row.split()) >= 7 and row.split()[-5] == "yes"
                           and row.split()[-4] == "yes" for row in rows):
        raise AssertionError("fonts not embedded and subset")
    return len(rows)


def extracted_bytes(path: Path) -> bytes:
    raw = subprocess.check_output(["pdftotext", "-layout", str(path), "-"])
    lowered = raw.lower()
    if (CONTROL.search(raw) or b"qquad" in lowered or b"??" in raw
            or b"[verify]" in lowered or b"unfinished" in lowered
            or b"placeholder" in lowered):
        raise AssertionError("PDF extracted-text gate")
    return raw


def raster(path: Path, count: int) -> list[int]:
    sizes = []
    with tempfile.TemporaryDirectory(prefix="c330-raster-") as directory:
        for page in range(1, count + 1):
            prefix = Path(directory) / f"page{page}"
            subprocess.run(
                ["pdftoppm", "-f", str(page), "-l", str(page), "-r", "72",
                 "-png", str(path), str(prefix)], check=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            )
            images = list(Path(directory).glob(f"page{page}-*.png"))
            if len(images) != 1 or images[0].stat().st_size < 1000:
                raise AssertionError("PDF raster gate")
            sizes.append(images[0].stat().st_size)
    return sizes


def fresh(round_number: int) -> bytes:
    with tempfile.TemporaryDirectory(prefix=f"c330-build-{round_number}-") as directory:
        work = Path(directory)
        shutil.copy2(TEX, work / "main.tex")
        env = dict(os.environ, SOURCE_DATE_EPOCH=str(EPOCH), FORCE_SOURCE_DATE="1", TZ="UTC")
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error",
                   "-jobname=main", source]
        for _ in range(2):
            subprocess.run(command, cwd=work, env=env, check=True,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = (work / "main.log").read_text(errors="replace")
        match = WARNING.search(log)
        if match:
            raise AssertionError(f"settled warning: {match.group(0)}")
        return (work / "main.pdf").read_bytes()


def expected_manifest() -> dict:
    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*")
                if path.is_file() and path != MANIFEST}
    if set(physical) != EXPECTED or len(physical) != 27:
        raise AssertionError(
            f"payload mismatch missing={sorted(EXPECTED-set(physical))} "
            f"extra={sorted(set(physical)-EXPECTED)}"
        )
    for name, path in physical.items():
        if not name.endswith(".pdf") and CONTROL.search(path.read_bytes()):
            raise AssertionError(f"control character in {name}")
    evidence = json.loads(EVIDENCE.read_text())
    body = dict(evidence)
    payload = body.pop("payload_sha256")
    canonical = json.dumps(body, sort_keys=True, separators=(",", ":"),
                           ensure_ascii=False).encode()
    if payload != hashlib.sha256(canonical).hexdigest():
        raise AssertionError("evidence payload")
    tokens = (
        "parity-oriented rational descent and the unique pythagorean tree",
        "quadratic periodic atlas, primitive counts, and source zeta",
        "exact word evidence and the route-a separation boundary",
    )
    receipts = []
    for number, path in enumerate(ROUNDS):
        count = pages(path)
        raw = extracted_bytes(path)
        normalized = " ".join(raw.decode("utf-8").lower().split())
        if tokens[number] not in normalized:
            raise AssertionError(f"round certificate {number}")
        receipts.append({
            "round": number, "path": str(path.relative_to(ROOT)),
            "sha256": sha(path), "bytes": path.stat().st_size, "pages": count,
            "font_rows": fonts(path), "raster_bytes": raster(path, count),
        })
    if len({row["sha256"] for row in receipts}) != 3:
        raise AssertionError("round PDFs are not distinct")
    if PDF.read_bytes() != ROUNDS[2].read_bytes():
        raise AssertionError("main PDF is not round 2")
    return {
        "schema": "hcs-release-manifest-v1", "candidate_id": "HCS-C330",
        "obstruction_id": "HEN-O314", "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": SCOPE, "payload_file_count": 27, "physical_file_count": 28,
        "evidence_sha256": sha(EVIDENCE), "evidence_payload_sha256": payload,
        "pdf_rounds": receipts,
        "files": {name: sha(path) for name, path in sorted(physical.items())},
    }


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C330 release refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    sentinels = [
        ("c330_romik_pythagorean_producer.py", "C330_PRODUCER_PASS"),
        ("c330_romik_pythagorean_checker.py", "C330 independent checker: PASS"),
        ("c330_romik_pythagorean_sympy_crosscheck.py", "C330 SymPy cross-check: PASS"),
        ("c330_romik_pythagorean_replay.py", "C330 byte replay: PASS"),
        ("c330_romik_pythagorean_mutation.py", "C330 hostile mutation suite: PASS"),
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
    print(f"C330_RELEASE_PASS {sha(EVIDENCE)} {sha(PDF)} {sha(MANIFEST)}")


if __name__ == "__main__":
    main()
