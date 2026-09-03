#!/usr/bin/env python3
"""Final 27-payload release gate and manifest writer for HCS-C323."""
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
MANIFEST = ROOT / "C323_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c323_quantum_search_evidence.json"
TEX = ROOT / "paper/main.tex"
MAIN_PDF = ROOT / "paper/main.pdf"
EPOCH = 1788393600
SOURCE = "1ccbfe2d759fe007c6b53c9646e1ab031878b34a"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVALUATION = ROOT / "evaluations/route_a/HCS-C323/2026-09-03.yaml"
EVALUATION_RAW_SHA256 = "32e01825c6a7337ce34f24a95838c7589ad54a0945b0026ab212feea05c0e0d4"
EVALUATION_SEMANTIC_SHA256 = "c2a1d3bf4d4af87c29c9efb002871d64b0210da3a2fcd4f4a36a9e694b21bdfa"
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
    "code/c323_release_manifest.py",
    "code/c323_quantum_search_checker.py",
    "code/c323_quantum_search_mutation.py",
    "code/c323_quantum_search_producer.py",
    "code/c323_quantum_search_replay.py",
    "code/c323_quantum_search_sympy_crosscheck.py",
    "evaluations/route_a/HCS-C323/2026-09-03.yaml",
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
    "results/c323_quantum_search_evidence.json",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_lane(name: str) -> str:
    return subprocess.check_output(
        [sys.executable, "-B", str(ROOT / "code" / name)],
        env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC"),
        text=True,
    )


def check_optimized_refusal(name: str) -> None:
    command = [sys.executable, "-O", "-B", str(ROOT / "code" / name)]
    with tempfile.TemporaryDirectory(prefix="c323-opt-") as directory:
        if name == "c323_quantum_search_producer.py":
            command.extend(["--output", str(Path(directory) / "forbidden.json")])
        process = subprocess.run(
            command,
            env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC"),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        if process.returncode == 0 or "refuses optimized Python" not in process.stdout:
            raise AssertionError(f"optimized execution was not explicitly refused: {name}")


def pages(path: Path) -> int:
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in output.splitlines() if line.startswith("Pages:")))


def font_rows(path: Path) -> int:
    output = subprocess.check_output(["pdffonts", str(path)], text=True)
    rows = [line for line in output.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]
    if not rows:
        raise AssertionError(f"no fonts listed: {path}")
    if not all(len(line.split()) >= 7 and line.split()[-5] == "yes" and line.split()[-4] == "yes" for line in rows):
        raise AssertionError(f"font not embedded and subset: {path}")
    return len(rows)


def extracted_text(path: Path) -> str:
    output = subprocess.check_output(["pdftotext", "-layout", str(path), "-"], text=True)
    return " ".join(output.lower().split())


def raster_sizes(path: Path, count: int) -> list[int]:
    sizes = []
    with tempfile.TemporaryDirectory(prefix="c323-raster-") as directory:
        directory = Path(directory)
        for page in range(1, count + 1):
            prefix = directory / f"page-{page}"
            subprocess.run(
                ["pdftoppm", "-f", str(page), "-l", str(page), "-r", "72", "-png", str(path), str(prefix)],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            images = list(directory.glob(f"page-{page}-*.png"))
            if len(images) != 1 or images[0].stat().st_size < 1000:
                raise AssertionError(f"raster failure: {path}, page {page}")
            sizes.append(images[0].stat().st_size)
    return sizes


def fresh_build(round_number: int) -> bytes:
    with tempfile.TemporaryDirectory(prefix=f"c323-build-{round_number}-") as directory:
        work = Path(directory)
        shutil.copy2(TEX, work / "main.tex")
        environment = dict(
            os.environ,
            SOURCE_DATE_EPOCH=str(EPOCH),
            FORCE_SOURCE_DATE="1",
            TZ="UTC",
        )
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", source]
        for _ in range(2):
            subprocess.run(
                command,
                cwd=work,
                env=environment,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
        match = WARNING.search((work / "main.log").read_text(errors="replace"))
        if match:
            raise AssertionError(f"paper warning in round {round_number}: {match.group(0)}")
        return (work / "main.pdf").read_bytes()


def evidence_payload_hash() -> str:
    data = json.loads(
        EVIDENCE.read_text(),
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(f"nonfinite {token}")),
    )
    body = dict(data)
    claimed = body.pop("payload_sha256")
    computed = hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()
    if computed != claimed:
        raise AssertionError("stale evidence payload hash")
    return claimed


def build_manifest() -> dict:
    files = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file() and path != MANIFEST}
    if set(files) != EXPECTED or len(files) != 27:
        raise AssertionError(
            f"payload ledger mismatch: missing={sorted(EXPECTED - set(files))}, "
            f"extra={sorted(set(files) - EXPECTED)}"
        )
    if sha(EVALUATION) != EVALUATION_RAW_SHA256:
        raise AssertionError("evaluation raw-byte digest mismatch")
    tokens = (
        "exact success law and full spectrum",
        "critical detuning window and boundary atlas",
        "evidence collision and route boundary",
    )
    pdf_rows = []
    for round_number, path in enumerate(ROUND_PDFS):
        count = pages(path)
        if tokens[round_number] not in extracted_text(path):
            raise AssertionError(f"revision token absent from round {round_number}")
        pdf_rows.append(
            {
                "round": round_number,
                "path": str(path.relative_to(ROOT)),
                "sha256": sha(path),
                "bytes": path.stat().st_size,
                "pages": count,
                "font_rows": font_rows(path),
                "raster_bytes": raster_sizes(path, count),
            }
        )
    if len({row["sha256"] for row in pdf_rows}) != 3:
        raise AssertionError("revision PDFs are not substantively distinct")
    if MAIN_PDF.read_bytes() != ROUND_PDFS[2].read_bytes():
        raise AssertionError("main.pdf is not the final revision")
    return {
        "schema": "hcs-release-manifest-v1",
        "candidate_id": "HCS-C323",
        "obstruction_id": "HEN-O307",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "payload_file_count": 27,
        "physical_file_count": 28,
        "evaluation_raw_sha256": EVALUATION_RAW_SHA256,
        "evaluation_semantic_sha256": EVALUATION_SEMANTIC_SHA256,
        "evidence_sha256": sha(EVIDENCE),
        "evidence_payload_sha256": evidence_payload_hash(),
        "pdf_rounds": pdf_rows,
        "files": {name: sha(path) for name, path in sorted(files.items())},
    }


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C323 release refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    lanes = [
        ("c323_quantum_search_producer.py", "C323_PRODUCER_PASS"),
        ("c323_quantum_search_checker.py", "C323 independent quantum-search checker: PASS"),
        ("c323_quantum_search_sympy_crosscheck.py", "C323 SymPy cross-check: PASS"),
        ("c323_quantum_search_replay.py", "C323 byte replay: PASS"),
        ("c323_quantum_search_mutation.py", "C323 hostile mutation suite: PASS"),
    ]
    for name, sentinel in lanes:
        if sentinel not in run_lane(name):
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

    sidecars = [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and (path.suffix in {".aux", ".log", ".out", ".toc", ".pyc"} or "__pycache__" in path.parts)
    ]
    if sidecars:
        raise AssertionError(f"forbidden build sidecars: {sidecars}")
    print(f"C323_RELEASE_PASS {sha(EVIDENCE)} {sha(MAIN_PDF)} {sha(MANIFEST)}")


if __name__ == "__main__":
    main()
