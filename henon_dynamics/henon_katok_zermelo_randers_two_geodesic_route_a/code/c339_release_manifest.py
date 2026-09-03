#!/usr/bin/env python3
"""Final 27-payload release gate and manifest writer for HCS-C339."""
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
MANIFEST = ROOT / "C339_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c339_katok_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C339/2026-09-03.yaml"
TEX = ROOT / "paper/main.tex"
MAIN_PDF = ROOT / "paper/main.pdf"
SOURCE = "e2d94f886963cbe3d42b83f6ef542413a163d3a4"
EPOCH = 1788393600
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVAL_RAW = "606a3a70932613ca8a42d2c964707a2788ed612c2ade624f490b51eeaacca9b0"
EVAL_SEMANTIC = "1e772f9884eb5e25af36001683ded882c1737115cc5e7129515c369b518cf83a"
ROUND_PDFS = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
WARNING = re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c339_katok_checker.py", "code/c339_katok_mutation.py",
    "code/c339_katok_producer.py", "code/c339_katok_replay.py",
    "code/c339_katok_sympy_crosscheck.py", "code/c339_release_manifest.py",
    "evaluations/route_a/HCS-C339/2026-09-03.yaml", "paper/COMPILE_REPORT.md", "paper/README.md",
    "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf",
    "paper/main_round2.pdf", "results/HOSTILE_AUDIT.md", "results/RESULTS.md",
    "results/TEST_REPORT.md", "results/c339_katok_evidence.json",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_lane(name: str) -> str:
    command = [sys.executable, "-B", str(ROOT / "code" / name)]
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c339-lane-") as directory:
        if name == "c339_katok_producer.py":
            command.extend(["--output", str(Path(directory) / "evidence.json")])
        return subprocess.check_output(command, env=environment, text=True)


def optimized_refusal(name: str):
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    for flag in ("-O", "-OO"):
        command = [sys.executable, flag, "-B", str(ROOT / "code" / name)]
        with tempfile.TemporaryDirectory(prefix="c339-opt-") as directory:
            if name == "c339_katok_producer.py":
                command.extend(["--output", str(Path(directory) / "forbidden.json")])
            process = subprocess.run(command, env=environment, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT, text=True)
        if process.returncode == 0 or "refuses optimized Python" not in process.stdout:
            raise AssertionError(f"optimized execution not explicitly refused: {flag} {name}")


def page_count(path: Path) -> int:
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in output.splitlines() if line.startswith("Pages:")))


def font_count(path: Path) -> int:
    output = subprocess.check_output(["pdffonts", str(path)], text=True)
    rows = [line for line in output.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]
    if not rows:
        raise AssertionError(f"no fonts in {path}")
    for row in rows:
        columns = row.split()
        if len(columns) < 7 or columns[-5] != "yes" or columns[-4] != "yes":
            raise AssertionError(f"font not embedded/subset: {path}: {row}")
    return len(rows)


def extracted_text(path: Path) -> str:
    raw = subprocess.check_output(["pdftotext", "-layout", str(path), "-"])
    if re.search(rb"[\x00-\x08\x0b\x0e-\x1f\x7f]", raw):
        raise AssertionError(f"forbidden extracted-text control byte: {path}")
    text = raw.decode("utf-8").lower()
    for token in ("qquad", "??", "[verify]", "todo", "fixme", "missing glyph", "__mutated"):
        if token in text:
            raise AssertionError(f"literal drafting or TeX garbage {token}: {path}")
    return " ".join(text.split())


def raster_sizes(path: Path, pages: int):
    sizes = []
    with tempfile.TemporaryDirectory(prefix="c339-raster-") as directory:
        work = Path(directory)
        for page in range(1, pages + 1):
            prefix = work / f"page-{page}"
            subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "72", "-png", str(path), str(prefix)],
                           check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            images = list(work.glob(f"page-{page}-*.png"))
            if len(images) != 1 or images[0].stat().st_size < 1000:
                raise AssertionError(f"raster failure: {path}, page {page}")
            sizes.append(images[0].stat().st_size)
    return sizes


def fresh_build(round_number: int) -> bytes:
    with tempfile.TemporaryDirectory(prefix=f"c339-build-{round_number}-") as directory:
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


def evidence_payload_hash() -> str:
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate evidence key")
            result[key] = value
        return result
    data = json.loads(EVIDENCE.read_text(), object_pairs_hook=unique,
                      parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    claimed = data.pop("payload_sha256")
    computed = hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    if claimed != computed:
        raise AssertionError("stale evidence payload hash")
    return claimed


def source_hygiene(files):
    for name, path in files.items():
        if path.suffix == ".pdf":
            continue
        raw = path.read_bytes()
        if re.search(rb"[\x00-\x09\x0b-\x1f\x7f]", raw):
            raise AssertionError(f"source control byte: {name}")


def build_manifest():
    files = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file() and path != MANIFEST}
    if set(files) != EXPECTED or len(files) != 27:
        raise AssertionError(f"payload ledger mismatch: missing={sorted(EXPECTED-set(files))}, extra={sorted(set(files)-EXPECTED)}")
    source_hygiene(files)
    if sha(EVALUATION) != EVAL_RAW:
        raise AssertionError("evaluation raw digest mismatch")
    if "c339_katok_producer" in (ROOT / "code/c339_katok_checker.py").read_text():
        raise AssertionError("checker imports or names producer")
    sentinels = ("commuting flow factorization", "rational boundary owner", "evidence and route firewall")
    compile_report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    pdf_rows = []
    for round_number, path in enumerate(ROUND_PDFS):
        pages = page_count(path)
        fonts = font_count(path)
        text = extracted_text(path)
        if sentinels[round_number] not in text:
            raise AssertionError(f"revision sentinel absent from round {round_number}")
        if sha(path) not in compile_report or f"| {pages} | {fonts} |" not in compile_report:
            raise AssertionError(f"compile report stale for round {round_number}")
        pdf_rows.append({"round": round_number, "path": str(path.relative_to(ROOT)), "sha256": sha(path),
                         "bytes": path.stat().st_size, "pages": pages, "font_rows": fonts,
                         "raster_bytes": raster_sizes(path, pages)})
    if len({row["sha256"] for row in pdf_rows}) != 3:
        raise AssertionError("revision PDFs are not distinct")
    if MAIN_PDF.read_bytes() != ROUND_PDFS[2].read_bytes():
        raise AssertionError("main.pdf is not round 2")
    return {
        "schema": "hcs-release-manifest-v1", "candidate_id": "HCS-C339", "obstruction_id": "HEN-O323",
        "source_commit": SOURCE, "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
        "payload_file_count": 27, "physical_file_count": 28,
        "evaluation_raw_sha256": EVAL_RAW, "evaluation_semantic_sha256": EVAL_SEMANTIC,
        "evidence_sha256": sha(EVIDENCE), "evidence_payload_sha256": evidence_payload_hash(),
        "pdf_rounds": pdf_rows, "files": {name: sha(path) for name, path in sorted(files.items())},
    }


def main():
    if sys.flags.optimize:
        raise RuntimeError("C339 release refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    lanes = [
        ("c339_katok_producer.py", "C339_PRODUCER_PASS"),
        ("c339_katok_checker.py", "C339 independent Katok checker: PASS"),
        ("c339_katok_sympy_crosscheck.py", "C339 SymPy cross-check: PASS"),
        ("c339_katok_replay.py", "C339 byte replay: PASS"),
        ("c339_katok_mutation.py", "C339 hostile mutation suite: PASS"),
    ]
    for name, sentinel in lanes:
        if sentinel not in run_lane(name):
            raise AssertionError(f"lane sentinel absent: {name}")
        optimized_refusal(name)
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
        raise AssertionError("release manifest missing or stale")
    sidecars = [path for path in ROOT.rglob("*") if path.is_file() and
                (path.suffix in {".aux", ".log", ".out", ".toc", ".pyc"} or "__pycache__" in path.parts)]
    if sidecars:
        raise AssertionError(f"forbidden sidecars: {sidecars}")
    print(f"C339_RELEASE_PASS {sha(EVIDENCE)} {sha(MAIN_PDF)} {sha(MANIFEST)}")


if __name__ == "__main__":
    main()
