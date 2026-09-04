#!/usr/bin/env python3
"""Release gate and self-excluding manifest for HCS-C359."""
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
MANIFEST = ROOT / "C359_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c359_pais_uhlenbeck_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C359/2026-09-04.yaml"
TEX = ROOT / "paper/main.tex"
MAIN_PDF = ROOT / "paper/main.pdf"
SOURCE = "05ca5f96b2c69a6ad6ba153d1084df750d7722c0"
EPOCH = 1788480000
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVAL_RAW = "7e46f2ada7433620bf08d1e0fcfe0da43e48455985312c30cc474425aee61156"
EVAL_SEMANTIC = "a15b1abe7eb8b34cdaf979485a1bcace0cd14de24289b4ed3fee7ecc7b4c9f64"
ROUND_PDFS = [ROOT/"paper/main_round0_original.pdf", ROOT/"paper/main_round1.pdf", ROOT/"paper/main_round2.pdf"]
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "code/README.md",
    "code/c359_pais_uhlenbeck_checker.py", "code/c359_pais_uhlenbeck_mutation.py",
    "code/c359_pais_uhlenbeck_producer.py", "code/c359_pais_uhlenbeck_replay.py",
    "code/c359_pais_uhlenbeck_sympy_crosscheck.py", "code/c359_release_manifest.py",
    "evaluations/route_a/HCS-C359/2026-09-04.yaml",
    "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c359_pais_uhlenbeck_evidence.json",
}
WARNING = re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|warning  \(pdf backend\)|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_lane(name):
    command = [sys.executable, "-B", str(ROOT/"code"/name)]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c359-lane-") as directory:
        if name == "c359_pais_uhlenbeck_producer.py":
            command += ["--output", str(Path(directory)/"evidence.json")]
        return subprocess.check_output(command, env=env, text=True)


def optimized_refusal(name):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    for flag in ("-O", "-OO"):
        command = [sys.executable, flag, "-B", str(ROOT/"code"/name)]
        with tempfile.TemporaryDirectory(prefix="c359-opt-") as directory:
            if name == "c359_pais_uhlenbeck_producer.py":
                command += ["--output", str(Path(directory)/"evidence.json")]
            proc = subprocess.run(command, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if proc.returncode == 0 or "refuses optimized Python" not in proc.stdout:
            raise AssertionError(f"optimized refusal absent: {flag} {name}")


def fresh_build(round_number):
    with tempfile.TemporaryDirectory(prefix=f"c359-build-{round_number}-") as directory:
        work = Path(directory); shutil.copy2(TEX, work/"main.tex")
        env = dict(os.environ, SOURCE_DATE_EPOCH=str(EPOCH), FORCE_SOURCE_DATE="1", TZ="UTC")
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", source]
        for _ in range(2):
            subprocess.run(command, cwd=work, env=env, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = (work/"main.log").read_text(errors="replace")
        match = WARNING.search(log)
        if match:
            raise AssertionError(f"paper warning round {round_number}: {match.group(0)}")
        return (work/"main.pdf").read_bytes()


def build_pdfs():
    blobs = []
    for round_number, target in enumerate(ROUND_PDFS):
        first, second = fresh_build(round_number), fresh_build(round_number)
        if first != second:
            raise AssertionError(f"nondeterministic PDF round {round_number}")
        target.write_bytes(first); blobs.append(first)
    MAIN_PDF.write_bytes(blobs[2])


def pages(path):
    text = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in text.splitlines() if line.startswith("Pages:")))


def fonts(path):
    text = subprocess.check_output(["pdffonts", str(path)], text=True)
    rows = [line for line in text.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]
    if not rows:
        raise AssertionError("no fonts")
    for row in rows:
        cols = row.split()
        if len(cols) < 7 or cols[-5] != "yes" or cols[-4] != "yes":
            raise AssertionError(f"font not embedded/subset: {row}")
    return len(rows)


def pdf_text(path):
    raw = subprocess.check_output(["pdftotext", "-layout", str(path), "-"])
    if re.search(rb"[\x00-\x08\x0b\x0e-\x1f\x7f]", raw):
        raise AssertionError("PDF text control byte")
    text = raw.decode("utf-8").lower()
    for token in ("qquad", "??", "[verify]", "todo", "fixme", "missing glyph", "__mutated"):
        if token in text:
            raise AssertionError(f"PDF garbage token {token}")
    return " ".join(text.split())


def raster(path, count):
    sizes = []
    with tempfile.TemporaryDirectory(prefix="c359-raster-") as directory:
        work = Path(directory)
        for page in range(1, count+1):
            prefix = work/f"p-{page}"
            subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "72", "-png", str(path), str(prefix)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            images = list(work.glob(f"p-{page}-*.png"))
            if len(images) != 1 or images[0].stat().st_size < 1000:
                raise AssertionError("raster failure")
            sizes.append(images[0].stat().st_size)
    return sizes


def evidence_payload():
    def unique(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError("duplicate evidence key")
            out[key] = value
        return out
    data = json.loads(EVIDENCE.read_text(), object_pairs_hook=unique,
                      parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    claimed = data.pop("payload_sha256")
    computed = hashlib.sha256(json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    if claimed != computed:
        raise AssertionError("stale evidence hash")
    return claimed


def build_manifest():
    files = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file() and path != MANIFEST}
    if set(files) != EXPECTED or len(files) != 27:
        raise AssertionError(f"ledger mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}")
    for name, path in files.items():
        if path.suffix != ".pdf" and re.search(rb"[\x00-\x09\x0b-\x1f\x7f]", path.read_bytes()):
            raise AssertionError(f"source control byte: {name}")
    if sha(EVALUATION) != EVAL_RAW:
        raise AssertionError("evaluation raw mismatch")
    checker = (ROOT/"code/c359_pais_uhlenbeck_checker.py").read_text()
    if "c359_pais_uhlenbeck_"+"producer" in checker:
        raise AssertionError("checker names producer")
    theorem = (ROOT/"THEOREM_PACKAGE.md").read_text()
    for token in ("PROVABLE AS STATED", "Kronecker", "Bézout", "pure point", "size-two Jordan"):
        if token not in theorem:
            raise AssertionError(f"theorem sentinel absent: {token}")
    source = (ROOT/"SOURCE_AUDIT.md").read_text()
    for token in ("10.1103/PhysRev.79.145", "10.1016/j.nuclphysb.2004.10.037", "quant-ph/0501024"):
        if token not in source:
            raise AssertionError(f"source sentinel absent: {token}")
    report = (ROOT/"paper/COMPILE_REPORT.md").read_text()
    sentinels = ("canonical-sign owner", "jordan-boundary owner", "dense pure-point owner")
    pdf_rows = []
    for round_number, path in enumerate(ROUND_PDFS):
        count, font_rows, text = pages(path), fonts(path), pdf_text(path)
        if sentinels[round_number] not in text:
            raise AssertionError(f"revision sentinel absent round {round_number}")
        if round_number == 2:
            for token in ("unbounded below", "not a hilbert", "route a is rejected", "route b is false"):
                if token not in text:
                    raise AssertionError(f"final paper sentinel absent: {token}")
        digest = sha(path)
        if digest not in report or f"| {round_number} | {count} | {font_rows} |" not in report:
            raise AssertionError(f"compile report stale round {round_number}")
        pdf_rows.append({"round": round_number, "path": str(path.relative_to(ROOT)), "sha256": digest,
                         "bytes": path.stat().st_size, "pages": count, "font_rows": font_rows,
                         "raster_bytes": raster(path, count)})
    if len({row["sha256"] for row in pdf_rows}) != 3 or MAIN_PDF.read_bytes() != ROUND_PDFS[2].read_bytes():
        raise AssertionError("PDF revision identity")
    return {
        "schema": "hcs-release-manifest-v1", "candidate_id": "HCS-C359",
        "obstruction_id": "HEN-O343", "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": SCOPE, "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
        "evaluator_version": "0.2.0", "evaluator_authority_sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
        "evaluation_raw_sha256": EVAL_RAW, "evaluation_semantic_sha256": EVAL_SEMANTIC,
        "payload_file_count": 27, "physical_file_count": 28,
        "evidence_sha256": sha(EVIDENCE), "evidence_payload_sha256": evidence_payload(),
        "main_pdf_sha256": sha(MAIN_PDF),
        "release_lanes": {"producer": "PASS", "independent_checker": "PASS", "sympy_crosscheck": "PASS", "isolated_byte_replay": "PASS", "hostile_mutation": "PASS", "optimized_mode_refusal": "PASS", "deterministic_pdf_rebuild": "PASS", "payload_membership": "PASS"},
        "pdf_rounds": pdf_rows, "files": {name: sha(path) for name, path in sorted(files.items())},
    }


def main():
    if sys.flags.optimize:
        raise RuntimeError("C359 release refuses optimized Python")
    parser = argparse.ArgumentParser(); parser.add_argument("--write", action="store_true"); parser.add_argument("--build-pdfs", action="store_true"); args = parser.parse_args()
    lanes = [
        ("c359_pais_uhlenbeck_producer.py", "C359_PRODUCER_PASS"),
        ("c359_pais_uhlenbeck_checker.py", "C359 independent Pais--Uhlenbeck checker: PASS"),
        ("c359_pais_uhlenbeck_sympy_crosscheck.py", "C359 SymPy cross-check: PASS"),
        ("c359_pais_uhlenbeck_replay.py", "C359 byte replay: PASS"),
        ("c359_pais_uhlenbeck_mutation.py", "C359 hostile mutation suite: PASS"),
    ]
    for name, sentinel in lanes:
        if sentinel not in run_lane(name):
            raise AssertionError(f"lane sentinel absent: {name}")
        optimized_refusal(name)
    if args.build_pdfs:
        build_pdfs()
    for round_number, checked in enumerate(ROUND_PDFS):
        first, second = fresh_build(round_number), fresh_build(round_number)
        if first != second or first != checked.read_bytes():
            raise AssertionError(f"stale or nondeterministic PDF round {round_number}")
    manifest = build_manifest()
    canonical = json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.write:
        MANIFEST.write_text(canonical)
    elif not MANIFEST.exists() or MANIFEST.read_text() != canonical:
        raise AssertionError("checked-in manifest stale")
    print("C359_RELEASE_PASS " + json.dumps({
        "checker": run_lane("c359_pais_uhlenbeck_checker.py").strip(),
        "sympy": run_lane("c359_pais_uhlenbeck_sympy_crosscheck.py").strip(),
        "mutation": run_lane("c359_pais_uhlenbeck_mutation.py").strip(),
        "evidence_sha256": manifest["evidence_sha256"], "pdf_sha256": manifest["pdf_rounds"][2]["sha256"],
        "pages": manifest["pdf_rounds"][2]["pages"],
        "manifest_sha256": hashlib.sha256(canonical.encode()).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
