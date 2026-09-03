#!/usr/bin/env python3
"""Final 27-payload release gate and manifest writer for HCS-C343."""
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
MANIFEST = ROOT / "C343_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c343_erlang2_delay_evidence.json"
TEX = ROOT / "paper/main.tex"
MAIN_PDF = ROOT / "paper/main.pdf"
EVALUATION = ROOT / "evaluations/route_a/HCS-C343/2026-09-03.yaml"
SOURCE = "e2d94f886963cbe3d42b83f6ef542413a163d3a4"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
EVAL_RAW = "7c148a98c804c66d57ed14946fb3e59b945098fe259a55ade3c9054002ab9033"
EVAL_SEMANTIC = "4f804ecbfce827f03931d97aae994fb8a346fd5e9ba064eb3b31f4c6e2067c08"
ROUND_PDFS = [
    ROOT/"paper/main_round0_original.pdf",
    ROOT/"paper/main_round1.pdf",
    ROOT/"paper/main_round2.pdf",
]
WARNING = re.compile(
    r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|"
    r"undefined (?:references|citations)|Rerun to get|Missing character"
)
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "code/README.md", "code/c343_erlang2_delay_checker.py",
    "code/c343_erlang2_delay_mutation.py", "code/c343_erlang2_delay_producer.py",
    "code/c343_erlang2_delay_replay.py", "code/c343_erlang2_delay_sympy_crosscheck.py",
    "code/c343_release_manifest.py", "evaluations/route_a/HCS-C343/2026-09-03.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c343_erlang2_delay_evidence.json",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_lane(name: str) -> str:
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    command = [sys.executable, "-B", str(ROOT/"code"/name)]
    with tempfile.TemporaryDirectory(prefix="c343-lane-") as directory:
        if name == "c343_erlang2_delay_producer.py":
            command.extend(["--output", str(Path(directory)/"evidence.json")])
        return subprocess.check_output(command, env=environment, text=True)


def check_optimized_refusal(name: str) -> None:
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    command = [sys.executable, "-OO", "-B", str(ROOT/"code"/name)]
    with tempfile.TemporaryDirectory(prefix="c343-opt-") as directory:
        if name == "c343_erlang2_delay_producer.py":
            command.extend(["--output", str(Path(directory)/"forbidden.json")])
        process = subprocess.run(
            command, env=environment, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, text=True,
        )
    if process.returncode == 0 or "refuses optimized Python" not in process.stdout:
        raise AssertionError(f"optimized execution was not explicitly refused: {name}")


def page_count(path: Path) -> int:
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(
        line.split(":", 1)[1]
        for line in output.splitlines() if line.startswith("Pages:")
    ))


def font_count(path: Path) -> int:
    output = subprocess.check_output(["pdffonts", str(path)], text=True)
    rows = [
        line for line in output.splitlines()[2:]
        if line.strip() and not line.lstrip().startswith("-")
    ]
    if not rows:
        raise AssertionError(f"no fonts: {path}")
    for line in rows:
        columns = line.split()
        if len(columns) < 7 or columns[-5] != "yes" or columns[-4] != "yes":
            raise AssertionError(f"font not embedded/subset: {path}: {line}")
    return len(rows)


def extracted_text(path: Path) -> str:
    raw = subprocess.check_output(["pdftotext", "-layout", str(path), "-"])
    if re.search(rb"[\x00-\x08\x0b\x0e-\x1f\x7f]", raw):
        raise AssertionError(f"forbidden extracted-text control byte: {path}")
    text = raw.decode("utf-8")
    lowered = text.lower()
    for token in ("??", "[verify]", "qquad", "lambda_", "__mutated"):
        if token in lowered:
            raise AssertionError(f"literal TeX/audit garbage {token}: {path}")
    return " ".join(lowered.split())


def raster_sizes(path: Path, pages: int) -> list[int]:
    sizes = []
    with tempfile.TemporaryDirectory(prefix="c343-raster-") as directory:
        work = Path(directory)
        for page in range(1, pages+1):
            prefix = work/f"page-{page}"
            subprocess.run(
                ["pdftoppm", "-f", str(page), "-l", str(page), "-r", "72",
                 "-png", str(path), str(prefix)],
                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            )
            images = list(work.glob(f"page-{page}-*.png"))
            if len(images) != 1 or images[0].stat().st_size < 1000:
                raise AssertionError(f"raster failure: {path}, page {page}")
            sizes.append(images[0].stat().st_size)
    return sizes


def fresh_build(round_number: int) -> tuple[bytes, str]:
    with tempfile.TemporaryDirectory(prefix=f"c343-build-{round_number}-") as directory:
        work = Path(directory)
        shutil.copy2(TEX, work/"main.tex")
        environment = dict(
            os.environ, SOURCE_DATE_EPOCH=str(EPOCH),
            FORCE_SOURCE_DATE="1", TZ="UTC",
        )
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}"
        command = [
            "lualatex", "-interaction=nonstopmode", "-halt-on-error",
            "-jobname=main", source,
        ]
        for _ in range(2):
            subprocess.run(
                command, cwd=work, env=environment, check=True,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
            )
        log = (work/"main.log").read_text(errors="replace")
        match = WARNING.search(log)
        if match:
            raise AssertionError(f"paper warning in round {round_number}: {match.group(0)}")
        return (work/"main.pdf").read_bytes(), log


def evidence_payload_hash() -> str:
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate evidence key")
            result[key] = value
        return result

    data = json.loads(
        EVIDENCE.read_text(), object_pairs_hook=unique,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)),
    )
    claimed = data.pop("payload_sha256")
    computed = hashlib.sha256(json.dumps(
        data, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode()).hexdigest()
    if claimed != computed:
        raise AssertionError("stale evidence payload hash")
    return claimed


def build_manuscripts() -> None:
    for round_number, path in enumerate(ROUND_PDFS):
        first, _ = fresh_build(round_number)
        second, _ = fresh_build(round_number)
        if first != second:
            raise AssertionError(f"nondeterministic PDF round {round_number}")
        path.write_bytes(first)
    MAIN_PDF.write_bytes(ROUND_PDFS[2].read_bytes())


def build_manifest() -> dict:
    tex_source = TEX.read_text()
    required_source = (
        r"\operatorname{disc}p=br^2\{4(r-a)^3-27br^2\}",
        r"\operatorname{Re}\lambda_+'(b_H)",
        "No nonlinear periodic",
    )
    for required in required_source:
        if required not in tex_source:
            raise AssertionError(f"required theorem boundary absent from TeX: {required}")
    if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", tex_source):
        raise AssertionError("TeX source contains a forbidden control byte")

    files = {
        str(path.relative_to(ROOT)): path
        for path in ROOT.rglob("*") if path.is_file() and path != MANIFEST
    }
    if set(files) != EXPECTED or len(files) != 27:
        raise AssertionError(
            f"payload ledger mismatch: missing={sorted(EXPECTED-set(files))}, "
            f"extra={sorted(set(files)-EXPECTED)}"
        )
    if sha(EVALUATION) != EVAL_RAW:
        raise AssertionError("evaluation raw digest mismatch")
    checker_text = (ROOT/"code/c343_erlang2_delay_checker.py").read_text()
    forbidden_name = "c343_erlang2_delay_" + "producer"
    if forbidden_name in checker_text:
        raise AssertionError("checker imports or names producer")

    tokens = (
        "chain equivalence owner",
        "routh hopf atlas owner",
        "jordan boundary and route firewall",
    )
    pdf_rows = []
    for round_number, path in enumerate(ROUND_PDFS):
        pages = page_count(path)
        text = extracted_text(path)
        if tokens[round_number] not in text:
            raise AssertionError(f"revision token absent: round {round_number}")
        if round_number == 2 and "no nonlinear periodic branch is claimed" not in text:
            raise AssertionError("nonlinear-claim boundary absent")
        pdf_rows.append({
            "round": round_number,
            "path": str(path.relative_to(ROOT)),
            "sha256": sha(path),
            "bytes": path.stat().st_size,
            "pages": pages,
            "font_rows": font_count(path),
            "raster_bytes": raster_sizes(path, pages),
        })
    if len({row["sha256"] for row in pdf_rows}) != 3:
        raise AssertionError("revision PDFs are not distinct")
    if MAIN_PDF.read_bytes() != ROUND_PDFS[2].read_bytes():
        raise AssertionError("main.pdf is not round 2")
    return {
        "schema": "hcs-release-manifest-v1",
        "candidate_id": "HCS-C343",
        "obstruction_id": "HEN-O327",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
        "payload_file_count": 27,
        "physical_file_count": 28,
        "evaluation_raw_sha256": EVAL_RAW,
        "evaluation_semantic_sha256": EVAL_SEMANTIC,
        "evidence_sha256": sha(EVIDENCE),
        "evidence_payload_sha256": evidence_payload_hash(),
        "pdf_rounds": pdf_rows,
        "files": {name: sha(path) for name, path in sorted(files.items())},
    }


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C343 release refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--build-pdfs", action="store_true")
    args = parser.parse_args()
    lanes = [
        ("c343_erlang2_delay_producer.py", "C343_PRODUCER_PASS"),
        ("c343_erlang2_delay_checker.py", "C343 independent Erlang-delay checker: PASS"),
        ("c343_erlang2_delay_sympy_crosscheck.py", "C343 SymPy cross-check: PASS"),
        ("c343_erlang2_delay_replay.py", "C343 byte replay: PASS"),
        ("c343_erlang2_delay_mutation.py", "C343 hostile mutation suite: PASS"),
    ]
    for name, sentinel in lanes:
        if sentinel not in run_lane(name):
            raise AssertionError(f"lane sentinel absent: {name}")
        check_optimized_refusal(name)
    if args.build_pdfs:
        build_manuscripts()
    for round_number, checked_in in enumerate(ROUND_PDFS):
        first, _ = fresh_build(round_number)
        second, _ = fresh_build(round_number)
        if first != second or first != checked_in.read_bytes():
            raise AssertionError(f"nondeterministic or stale PDF round {round_number}")
    manifest = build_manifest()
    raw = json.dumps(manifest, sort_keys=True, indent=2, ensure_ascii=False)+"\n"
    if args.write:
        MANIFEST.write_text(raw)
    elif not MANIFEST.exists() or MANIFEST.read_text() != raw:
        raise AssertionError("release manifest missing or stale")
    sidecars = [
        path for path in ROOT.rglob("*") if path.is_file()
        and (path.suffix in {".aux", ".log", ".out", ".toc", ".pyc"}
             or "__pycache__" in path.parts)
    ]
    if sidecars:
        raise AssertionError(f"forbidden sidecars: {sidecars}")
    print(f"C343_RELEASE_PASS {sha(EVIDENCE)} {sha(MAIN_PDF)} {sha(MANIFEST)}")


if __name__ == "__main__":
    main()
