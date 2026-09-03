#!/usr/bin/env python3
"""Final 27-payload release gate and manifest writer for HCS-C336."""
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
MANIFEST = ROOT / "C336_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c336_crow_kimura_evidence.json"
TEX = ROOT / "paper/main.tex"
MAIN_PDF = ROOT / "paper/main.pdf"
EVALUATION = ROOT / "evaluations/route_a/HCS-C336/2026-09-03.yaml"
SOURCE = "db2c816b7b6bd450f51f79b91842cb882b0bd773"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
EVALUATION_RAW_SHA256 = "0c48ad05b07c835172f55442d812a1492ca9ef5e320b817916246d62b16d5f56"
EVALUATION_SEMANTIC_SHA256 = "43b56588a42292014f578318aa99d7ab6db99fcdac162e7669f73a1598a73ae3"
EVIDENCE_SHA256 = "b4102f835b4fc68165c6fa94f657166d56977b10c86ea9959361d2aa67025f8a"
ROUND_PDFS = [
    ROOT / "paper/main_round0_original.pdf",
    ROOT / "paper/main_round1.pdf",
    ROOT / "paper/main_round2.pdf",
]
ROUND_SHA256 = [
    "a055046d2fb2bbb5940fa3f3b9ecff8423ff09508947f123cc7800b448501a02",
    "f5ca1f243db737a0b4b2f86b4fd8dbbd074d5b734e0d3f2b0f27f4324f97e3bc",
    "cdde6ab95da987d1c21c816edc734c77d0d81a47ed9011076e75cd92cefd6d1a",
]
WARNING = re.compile(
    r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|"
    r"undefined (?:references|citations)|Rerun to get|Missing character|missing glyph",
    re.IGNORECASE,
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
    "code/c336_crow_kimura_checker.py",
    "code/c336_crow_kimura_mutation.py",
    "code/c336_crow_kimura_producer.py",
    "code/c336_crow_kimura_replay.py",
    "code/c336_crow_kimura_sympy_crosscheck.py",
    "code/c336_release_manifest.py",
    "evaluations/route_a/HCS-C336/2026-09-03.yaml",
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
    "results/c336_crow_kimura_evidence.json",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_lane(name: str) -> str:
    return subprocess.check_output(
        [sys.executable, "-B", str(ROOT / "code" / name)],
        env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC"), text=True,
    )


def check_optimized_refusal(name: str) -> None:
    command = [sys.executable, "-OO", "-B", str(ROOT / "code" / name)]
    with tempfile.TemporaryDirectory(prefix="c336-opt-") as directory:
        if name == "c336_crow_kimura_producer.py":
            command.extend(["--output", str(Path(directory) / "forbidden.json")])
        process = subprocess.run(
            command, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC"),
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
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
    raw = subprocess.check_output(["pdftotext", "-layout", str(path), "-"])
    if re.search(rb"[\x00-\x08\x0b\x0e-\x1f\x7f]", raw):
        raise AssertionError(f"forbidden extracted-text control character: {path}")
    output = raw.decode("utf-8")
    lowered = output.lower()
    if "qquad" in lowered or "lambda_" in lowered or "??" in output:
        raise AssertionError(f"literal TeX/reference garbage in extracted text: {path}")
    return " ".join(lowered.split())


def raster_sizes(path: Path, count: int) -> list[int]:
    sizes = []
    with tempfile.TemporaryDirectory(prefix="c336-raster-") as directory:
        work = Path(directory)
        for page in range(1, count + 1):
            prefix = work / f"page-{page}"
            subprocess.run(
                ["pdftoppm", "-f", str(page), "-l", str(page), "-r", "72", "-png", str(path), str(prefix)],
                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            )
            images = list(work.glob(f"page-{page}-*.png"))
            if len(images) != 1 or images[0].stat().st_size < 1000:
                raise AssertionError(f"raster failure: {path}, page {page}")
            sizes.append(images[0].stat().st_size)
    return sizes


def fresh_build(round_number: int) -> bytes:
    with tempfile.TemporaryDirectory(prefix=f"c336-build-{round_number}-") as directory:
        work = Path(directory)
        shutil.copy2(TEX, work / "main.tex")
        environment = dict(
            os.environ, SOURCE_DATE_EPOCH=str(EPOCH), FORCE_SOURCE_DATE="1", TZ="UTC",
        )
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", source]
        for _ in range(2):
            subprocess.run(
                command, cwd=work, env=environment, check=True,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
            )
        match = WARNING.search((work / "main.log").read_text(errors="replace"))
        if match:
            raise AssertionError(f"paper warning in round {round_number}: {match.group(0)}")
        return (work / "main.pdf").read_bytes()


def evidence_payload_hash() -> str:
    def duplicate_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate evidence key")
            result[key] = value
        return result

    data = json.loads(
        EVIDENCE.read_text(), object_pairs_hook=duplicate_pairs,
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
            f"payload ledger mismatch: missing={sorted(EXPECTED-set(files))}, extra={sorted(set(files)-EXPECTED)}"
        )
    if sha(EVALUATION) != EVALUATION_RAW_SHA256:
        raise AssertionError("evaluation raw-byte digest mismatch")
    if sha(EVIDENCE) != EVIDENCE_SHA256:
        raise AssertionError("evidence byte digest mismatch")
    tokens = (
        "projective semigroup owner",
        "strict secular interlacing",
        "finite-length boundary and route firewall",
    )
    pdf_rows = []
    for round_number, path in enumerate(ROUND_PDFS):
        count = pages(path)
        if tokens[round_number] not in extracted_text(path):
            raise AssertionError(f"revision token absent from round {round_number}")
        if sha(path) != ROUND_SHA256[round_number]:
            raise AssertionError(f"checked PDF hash drift in round {round_number}")
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
        "candidate_id": "HCS-C336",
        "obstruction_id": "HEN-O320",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
        "payload_file_count": 27,
        "physical_file_count": 28,
        "evaluation_raw_sha256": EVALUATION_RAW_SHA256,
        "evaluation_semantic_sha256": EVALUATION_SEMANTIC_SHA256,
        "evidence_sha256": EVIDENCE_SHA256,
        "evidence_payload_sha256": evidence_payload_hash(),
        "pdf_rounds": pdf_rows,
        "files": {name: sha(path) for name, path in sorted(files.items())},
    }


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C336 release refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    lanes = [
        ("c336_crow_kimura_producer.py", "C336_PRODUCER_PASS"),
        ("c336_crow_kimura_checker.py", "C336 independent Crow-Kimura checker: PASS"),
        ("c336_crow_kimura_sympy_crosscheck.py", "C336 SymPy cross-check: PASS"),
        ("c336_crow_kimura_replay.py", "C336 byte replay: PASS"),
        ("c336_crow_kimura_mutation.py", "C336 hostile mutation suite: PASS"),
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
        path for path in ROOT.rglob("*") if path.is_file()
        and (path.suffix in {".aux", ".log", ".out", ".toc", ".pyc"} or "__pycache__" in path.parts)
    ]
    if sidecars:
        raise AssertionError(f"forbidden sidecars: {sidecars}")
    print("C336 release manifest: PASS payloads=27 physical=28")


if __name__ == "__main__":
    main()
