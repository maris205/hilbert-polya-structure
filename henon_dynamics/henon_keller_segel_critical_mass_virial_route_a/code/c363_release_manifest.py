#!/usr/bin/env python3
"""Final 27-payload release gate and manifest writer for HCS-C363."""
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
MANIFEST = ROOT / "C363_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c363_keller_segel_evidence.json"
TEX = ROOT / "paper/main.tex"
MAIN_PDF = ROOT / "paper/main.pdf"
COMPILE_REPORT = ROOT / "paper/COMPILE_REPORT.md"
EVALUATION = ROOT / "evaluations/route_a/HCS-C363/2026-09-04.yaml"
SOURCE = "05ca5f96b2c69a6ad6ba153d1084df750d7722c0"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788480000
EVALUATION_RAW_SHA256 = "aa52111eaa5c48cb46a895a7ff4c4b0ebcfed5a91d8f3a37ef8b9a083a04488a"
EVALUATION_SEMANTIC_SHA256 = "7914a5f2d01e7ca45e1619289dd962bbf29638bd70734fdc4923c461115120a9"
ROUND_PDFS = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf",
              ROOT / "paper/main_round2.pdf"]
WARNING = re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|warning  \(pdf backend\)|"
                     r"Overfull|Underfull|undefined (?:references|citations)|"
                     r"Rerun to get|Missing character")
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "code/README.md", "code/c363_keller_segel_checker.py",
    "code/c363_keller_segel_mutation.py", "code/c363_keller_segel_producer.py",
    "code/c363_keller_segel_replay.py", "code/c363_keller_segel_sympy_crosscheck.py",
    "code/c363_release_manifest.py", "evaluations/route_a/HCS-C363/2026-09-04.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c363_keller_segel_evidence.json",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_lane(name: str) -> str:
    command = [sys.executable, "-B", str(ROOT / "code" / name)]
    with tempfile.TemporaryDirectory(prefix="c363-lane-") as directory:
        output = Path(directory) / "evidence.json"
        if name == "c363_keller_segel_producer.py":
            command.extend(["--output", str(output), "--evaluation", str(EVALUATION)])
        result = subprocess.check_output(
            command,
            env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC"),
            text=True,
        )
        if name == "c363_keller_segel_producer.py" and output.read_bytes() != EVIDENCE.read_bytes():
            raise AssertionError("producer output differs from checked evidence")
        return result


def check_optimized_refusal(name: str) -> None:
    for flag in ("-O", "-OO"):
        command = [sys.executable, flag, "-B", str(ROOT / "code" / name)]
        with tempfile.TemporaryDirectory(prefix="c363-opt-") as directory:
            if name == "c363_keller_segel_producer.py":
                command.extend(["--output", str(Path(directory) / "forbidden.json"),
                                "--evaluation", str(EVALUATION)])
            process = subprocess.run(
                command,
                env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC"),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            if process.returncode == 0 or "refuses optimized Python" not in process.stdout:
                raise AssertionError(
                    f"optimized execution not explicitly refused: {flag} {name}"
                )


def pages(path: Path) -> int:
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in output.splitlines()
                    if line.startswith("Pages:")))


def font_rows(path: Path) -> int:
    output = subprocess.check_output(["pdffonts", str(path)], text=True)
    rows = [line for line in output.splitlines()[2:]
            if line.strip() and not line.lstrip().startswith("-")]
    if not rows:
        raise AssertionError(f"no fonts: {path}")
    for line in rows:
        fields = line.split()
        if len(fields) < 7 or fields[-5] != "yes" or fields[-4] != "yes":
            raise AssertionError(f"font not embedded and subset: {path}: {line}")
    return len(rows)


def extracted_text(path: Path) -> str:
    raw = subprocess.check_output(["pdftotext", "-layout", str(path), "-"])
    normalized = raw.replace(b"\x12", b"").replace(b"\x13", b"")
    if re.search(rb"[\x00-\x08\x0b\x0e-\x1f\x7f]", normalized):
        raise AssertionError(f"extracted-text control character: {path}")
    text = raw.decode("utf-8")
    lowered = text.lower()
    for forbidden in ("qquad", "quadb", "??", "[verify]", "todo", "fixme",
                      "missing glyph"):
        if forbidden in lowered:
            raise AssertionError(f"draft/TeX garbage: {path}: {forbidden}")
    return " ".join(lowered.split())


def raster_sizes(path: Path, count: int) -> list[int]:
    answer = []
    with tempfile.TemporaryDirectory(prefix="c363-raster-") as directory:
        work = Path(directory)
        for page in range(1, count + 1):
            prefix = work / f"page-{page}"
            subprocess.run(
                ["pdftoppm", "-f", str(page), "-l", str(page), "-r", "96",
                 "-png", str(path), str(prefix)],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            images = list(work.glob(f"page-{page}-*.png"))
            if len(images) != 1 or images[0].stat().st_size < 1000:
                raise AssertionError(f"raster failure: {path} page {page}")
            answer.append(images[0].stat().st_size)
    return answer


def fresh_build(round_number: int) -> bytes:
    with tempfile.TemporaryDirectory(prefix=f"c363-build-{round_number}-") as directory:
        work = Path(directory)
        shutil.copy2(TEX, work / "main.tex")
        environment = dict(os.environ, SOURCE_DATE_EPOCH=str(EPOCH),
                           FORCE_SOURCE_DATE="1", TZ="UTC")
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error",
                   "-jobname=main", source]
        for _ in range(2):
            subprocess.run(command, cwd=work, env=environment, check=True,
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = (work / "main.log").read_text(errors="replace")
        match = WARNING.search(log)
        if match:
            raise AssertionError(f"paper warning in round {round_number}: {match.group(0)}")
        return (work / "main.pdf").read_bytes()


def pairs(items):
    answer = {}
    for key, value in items:
        if key in answer:
            raise ValueError("duplicate evidence key")
        answer[key] = value
    return answer


def evidence_payload_hash() -> str:
    data = json.loads(
        EVIDENCE.read_text(),
        object_pairs_hook=pairs,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)),
    )
    body = dict(data)
    claimed = body.pop("payload_sha256")
    computed = hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"),
                   ensure_ascii=False).encode()
    ).hexdigest()
    if claimed != computed:
        raise AssertionError("stale evidence payload hash")
    return claimed


def build_manifest() -> dict:
    files = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*")
             if path.is_file() and path != MANIFEST}
    if set(files) != EXPECTED or len(files) != 27:
        raise AssertionError(
            f"payload mismatch missing={sorted(EXPECTED-set(files))} "
            f"extra={sorted(set(files)-EXPECTED)}"
        )
    if sha(EVALUATION) != EVALUATION_RAW_SHA256:
        raise AssertionError("evaluation raw-byte digest")
    report = COMPILE_REPORT.read_text()
    for path in ROUND_PDFS:
        if sha(path) not in report:
            raise AssertionError(f"compile report lacks current PDF digest: {path.name}")
    tokens = (
        "round zero energy scaling and critical mass closure",
        "round one virial bound and stationary profile closure",
        "round two radial dynamics, evidence, and route a closure",
    )
    pdf_rows = []
    for round_number, path in enumerate(ROUND_PDFS):
        count = pages(path)
        text = extracted_text(path)
        if tokens[round_number] not in text:
            raise AssertionError(f"revision token absent: round {round_number}")
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
        raise AssertionError("revision PDFs not distinct")
    if MAIN_PDF.read_bytes() != ROUND_PDFS[2].read_bytes():
        raise AssertionError("main.pdf is not round 2")
    return {
        "schema": "hcs-release-manifest-v1",
        "candidate_id": "HCS-C363",
        "obstruction_id": "HEN-O347",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
        "evaluator_version": "0.2.0",
        "evaluator_authority_sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
        "payload_file_count": 27,
        "physical_file_count": 28,
        "evaluation_raw_sha256": EVALUATION_RAW_SHA256,
        "evaluation_semantic_sha256": EVALUATION_SEMANTIC_SHA256,
        "evidence_sha256": sha(EVIDENCE),
        "evidence_payload_sha256": evidence_payload_hash(),
        "main_pdf_sha256": sha(MAIN_PDF),
        "release_lanes": {"producer": "PASS", "independent_checker": "PASS",
                          "sympy_crosscheck": "PASS",
                          "isolated_byte_replay": "PASS",
                          "hostile_mutation": "PASS",
                          "optimized_mode_refusal": "PASS",
                          "deterministic_pdf_rebuild": "PASS",
                          "payload_membership": "PASS"},
        "pdf_rounds": pdf_rows,
        "files": {name: sha(path) for name, path in sorted(files.items())},
    }


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C363 release refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    lanes = [
        ("c363_keller_segel_producer.py", "C363 producer: PASS"),
        ("c363_keller_segel_checker.py", "C363 independent checker: PASS"),
        ("c363_keller_segel_sympy_crosscheck.py", "C363 SymPy cross-check: PASS"),
        ("c363_keller_segel_replay.py", "C363 byte replay: PASS"),
        ("c363_keller_segel_mutation.py", "C363 hostile mutation suite: PASS"),
    ]
    for name, sentinel in lanes:
        output = run_lane(name)
        if sentinel not in output:
            raise AssertionError(f"lane sentinel absent: {name}")
        check_optimized_refusal(name)
    for round_number, checked in enumerate(ROUND_PDFS):
        first, second = fresh_build(round_number), fresh_build(round_number)
        if first != second or first != checked.read_bytes():
            raise AssertionError(f"nondeterministic or stale PDF round {round_number}")
    manifest = build_manifest()
    raw = json.dumps(manifest, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if args.write:
        MANIFEST.write_text(raw)
    elif not MANIFEST.exists() or MANIFEST.read_text() != raw:
        raise AssertionError("release manifest missing or stale")
    sidecars = [path for path in ROOT.rglob("*") if path.is_file()
                and (path.suffix in {".aux", ".log", ".out", ".toc", ".pyc"}
                     or "__pycache__" in path.parts)]
    if sidecars:
        raise AssertionError(f"forbidden build sidecars: {sidecars}")
    print(f"C363_RELEASE_PASS {sha(EVIDENCE)} {sha(MAIN_PDF)} {sha(MANIFEST)}")


if __name__ == "__main__":
    main()
