#!/usr/bin/env python3
"""Deterministic 27-payload release gate for HCS-C350."""
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
MANIFEST = ROOT / "C350_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c350_schnakenberg_evidence.json"
TEX = ROOT / "paper/main.tex"
MAIN_PDF = ROOT / "paper/main.pdf"
EVALUATION = ROOT / "evaluations/route_a/HCS-C350/2026-09-03.yaml"
SOURCE = "327fc1172cebcdeb17adfd2d8ad12636fbb94f52"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
EVAL_RAW = "392e9d205af7e0e7f765bc34889f23cd094434335d68e9ab1cf4853bf32e0d21"
EVAL_SEMANTIC = "ed762fcd6f342b51d83c2445e5d862407317fec49d961a73bc1cf20830cc7cda"
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
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "code/README.md",
    "code/c350_release_manifest.py", "code/c350_schnakenberg_checker.py",
    "code/c350_schnakenberg_mutation.py", "code/c350_schnakenberg_producer.py",
    "code/c350_schnakenberg_replay.py", "code/c350_schnakenberg_sympy_crosscheck.py",
    "evaluations/route_a/HCS-C350/2026-09-03.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c350_schnakenberg_evidence.json",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def strict_json(path: Path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    return json.loads(
        path.read_text(), object_pairs_hook=unique,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)),
    )


def run_lane(name: str) -> str:
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    command = [sys.executable, "-B", str(ROOT / "code" / name)]
    with tempfile.TemporaryDirectory(prefix="c350-lane-") as directory:
        if name == "c350_schnakenberg_producer.py":
            command.extend(["--output", str(Path(directory) / "evidence.json")])
        return subprocess.check_output(command, env=environment, text=True)


def check_optimized_refusal(name: str) -> None:
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    for flag in ("-O", "-OO"):
        command = [sys.executable, flag, "-B", str(ROOT / "code" / name)]
        with tempfile.TemporaryDirectory(prefix="c350-opt-") as directory:
            if name == "c350_schnakenberg_producer.py":
                command.extend(["--output", str(Path(directory) / "forbidden.json")])
            process = subprocess.run(
                command, env=environment, stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT, text=True,
            )
        if process.returncode == 0 or "refuses optimized Python" not in process.stdout:
            raise AssertionError(
                f"optimized execution was not explicitly refused: {flag} {name}"
            )


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
    lowered = " ".join(text.lower().split())
    for token in ("??", "[verify]", "qquad", "__mutated", "varepsilon_"):
        if token in lowered:
            raise AssertionError(f"literal TeX/audit garbage {token}: {path}")
    return lowered


def raster_sizes(path: Path, pages: int) -> list[int]:
    sizes = []
    with tempfile.TemporaryDirectory(prefix="c350-raster-") as directory:
        work = Path(directory)
        for page in range(1, pages + 1):
            prefix = work / f"page-{page}"
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
    with tempfile.TemporaryDirectory(prefix=f"c350-build-{round_number}-") as directory:
        work = Path(directory)
        shutil.copy2(TEX, work / "main.tex")
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
        log = (work / "main.log").read_text(errors="replace")
        match = WARNING.search(log)
        if match:
            raise AssertionError(
                f"paper warning in round {round_number}: {match.group(0)}"
            )
        return (work / "main.pdf").read_bytes(), log


def evidence_payload_hash() -> str:
    data = strict_json(EVIDENCE)
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


def build_manifest(lane_outputs: dict[str, str]) -> dict:
    tex_source = TEX.read_text()
    required_source = (
        r"\mu_n=(n\pi/L)^2", r"B>0,\qquad Q>0",
        r"\lceil r_+\rceil-\lfloor r_-\rfloor-1",
        "unique positive spatially homogeneous",
        "linear", "Route B remains locked",
    )
    for required in required_source:
        if required not in tex_source:
            raise AssertionError(f"required theorem boundary absent from TeX: {required}")
    if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", tex_source):
        raise AssertionError("TeX source contains a forbidden control byte")
    if re.search(r"(?<!\\)qquad", tex_source):
        raise AssertionError("bare qquad-like TeX token")

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
    checker_text = (ROOT / "code/c350_schnakenberg_checker.py").read_text()
    if re.search(r"(?:from|import)\s+[^\n]*c350_schnakenberg_producer", checker_text):
        raise AssertionError("checker imports producer")

    tokens = (
        "kinetic and modal dispersion closure",
        "strict interval mode-count closure",
        "operator, boundary, and route closure",
    )
    pdf_rows = []
    for round_number, path in enumerate(ROUND_PDFS):
        pages = page_count(path)
        text = extracted_text(path)
        if tokens[round_number] not in text:
            raise AssertionError(f"revision token absent: round {round_number}")
        if round_number == 2 and "route b remains locked" not in text:
            raise AssertionError("Route-B lock absent from final PDF")
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

    evidence = strict_json(EVIDENCE)
    if evidence["source_commit"] != SOURCE or evidence["scope_literal"] != SCOPE:
        raise AssertionError("evidence source/scope drift")
    if evidence["route_a"] != {
        "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
    }:
        raise AssertionError("evidence Route-A drift")

    return {
        "schema": "hcs-release-manifest-v1",
        "candidate_id": "HCS-C350", "obstruction_id": "HEN-O334",
        "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
        "evaluator_version": "0.2.0",
        "evaluator_authority_sha256":
            "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
        "payload_file_count": 27, "physical_file_count": 28,
        "evaluation_raw_sha256": EVAL_RAW,
        "evaluation_semantic_sha256": EVAL_SEMANTIC,
        "evidence_sha256": sha(EVIDENCE),
        "evidence_payload_sha256": evidence_payload_hash(),
        "release_lanes": lane_outputs,
        "pdf_rounds": pdf_rows,
        "main_pdf_sha256": sha(MAIN_PDF),
        "files": {name: sha(path) for name, path in sorted(files.items())},
    }


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C350 release refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--build-pdfs", action="store_true")
    args = parser.parse_args()
    lanes = [
        ("c350_schnakenberg_producer.py", "C350_PRODUCER_PASS"),
        ("c350_schnakenberg_checker.py", "C350 independent Schnakenberg checker: PASS"),
        ("c350_schnakenberg_sympy_crosscheck.py", "C350 SymPy cross-check: PASS"),
        ("c350_schnakenberg_replay.py", "C350 byte replay: PASS"),
        ("c350_schnakenberg_mutation.py", "C350 hostile mutation suite: PASS"),
    ]
    lane_outputs = {}
    for name, sentinel in lanes:
        output = run_lane(name).strip()
        if sentinel not in output:
            raise AssertionError(f"lane sentinel absent: {name}")
        lane_outputs[name] = output
        check_optimized_refusal(name)
    if args.build_pdfs:
        build_manuscripts()
    for round_number, checked_in in enumerate(ROUND_PDFS):
        first, _ = fresh_build(round_number)
        second, _ = fresh_build(round_number)
        if first != second or first != checked_in.read_bytes():
            raise AssertionError(f"nondeterministic or stale PDF round {round_number}")
    manifest = build_manifest(lane_outputs)
    raw = json.dumps(manifest, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
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
    print(f"C350_RELEASE_PASS {sha(EVIDENCE)} {sha(MAIN_PDF)} {sha(MANIFEST)}")


if __name__ == "__main__":
    main()
