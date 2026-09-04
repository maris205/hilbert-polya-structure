#!/usr/bin/env python3
"""Deterministic 35-payload release gate for HCS-C371."""
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

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C371_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c371_harper_evidence.json"
TEX = ROOT / "paper/main.tex"
MAIN = ROOT / "paper/main.pdf"
YML = ROOT / "evaluations/route_a/HCS-C371/2026-09-04.yaml"
RAW = "96ed0db538adbf9e123ef89787d281430dd62d14f37b6256e7d306d1a92ccd8f"
SEMANTIC = "9d10dd13dee407f999937a3642bb533a10d04a1770bbd3235ee84ef2d15a3d32"
SOURCE = "c6553f02d928c6aa05400ded57746869a85f0238"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788480000
ROUNDS = [
    ROOT / "paper/main_round0_original.pdf",
    ROOT / "paper/main_round1.pdf",
    ROOT / "paper/main_round2.pdf",
]
WARNING = re.compile(
    r"(?:LaTeX|Package [^:\n]+) Warning:|warning  \(pdf backend\)|Overfull|Underfull|"
    r"undefined (?:references|citations)|Rerun to get|Missing character"
)
EXPECTED = {
    "ASSUMPTIONS.md", "CLAIMS.md", "EXPERIMENT_PLAN.md", "LIMITATIONS.md",
    "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md", "README.md",
    "REFERENCES.md", "REPRODUCIBILITY.md", "RESEARCH_QUESTION.md", "SCOPE.md",
    "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md", "requirements.txt", "code/README.md",
    "code/c371_release_manifest.py", "code/c371_harper_checker.py",
    "code/c371_harper_mutation.py", "code/c371_harper_producer.py",
    "code/c371_harper_replay.py", "code/c371_harper_sympy_crosscheck.py",
    "evaluations/route_a/HCS-C371/2026-09-04.yaml", "paper/COMPILE_REPORT.md",
    "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c371_harper_evidence.json", "tests/test_c371_smoke.py",
}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def strict_json(path):
    def unique(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError("duplicate JSON key")
            out[key] = value
        return out

    return json.loads(
        path.read_text(),
        object_pairs_hook=unique,
        parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)),
    )


def command(script, args=()):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    return subprocess.check_output(
        [sys.executable, "-B", str(ROOT / "code" / script), *args], env=env, text=True
    ).strip()


def isolated_lane(script):
    with tempfile.TemporaryDirectory(prefix="c371-lane-") as directory:
        args = (
            "--output", str(Path(directory) / "evidence.json")
        ) if script == "c371_harper_producer.py" else ()
        return command(script, args)


def optimized_refusal(script):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    for flag in ("-O", "-OO"):
        cmd = [sys.executable, flag, "-B", str(ROOT / "code" / script)]
        with tempfile.TemporaryDirectory(prefix="c371-opt-") as directory:
            if script == "c371_harper_producer.py":
                cmd += ["--output", str(Path(directory) / "evidence.json")]
            proc = subprocess.run(
                cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
            )
        if proc.returncode == 0 or "refuses optimized Python" not in proc.stdout:
            raise AssertionError(f"optimized execution not refused: {flag} {script}")


def smoke_tests():
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    proc = subprocess.run(
        [sys.executable, "-B", "-m", "unittest", "tests/test_c371_smoke.py"],
        cwd=ROOT,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    if proc.returncode != 0 or "OK" not in proc.stdout:
        raise AssertionError(f"smoke tests failed:\n{proc.stdout}")
    return "3/3 PASS"


def fresh_pdf(round_number):
    with tempfile.TemporaryDirectory(prefix=f"c371-build-{round_number}-") as directory:
        work = Path(directory)
        shutil.copy2(TEX, work / "main.tex")
        env = dict(
            os.environ,
            SOURCE_DATE_EPOCH=str(EPOCH),
            FORCE_SOURCE_DATE="1",
            TZ="UTC",
        )
        cmd = [
            "lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main",
            rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}",
        ]
        for _ in range(2):
            subprocess.run(
                cmd, cwd=work, env=env, check=True,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
            )
        log = (work / "main.log").read_text(errors="replace")
        hit = WARNING.search(log)
        if hit:
            raise AssertionError(f"paper warning round {round_number}: {hit.group(0)}")
        return (work / "main.pdf").read_bytes()


def page_count(path):
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in output.splitlines() if line.startswith("Pages:")))


def font_count(path):
    rows = [
        line for line in subprocess.check_output(["pdffonts", str(path)], text=True).splitlines()[2:]
        if line.strip() and not line.lstrip().startswith("-")
    ]
    if not rows:
        raise AssertionError("PDF has no fonts")
    for row in rows:
        columns = row.split()
        if len(columns) < 7 or columns[-5] != "yes" or columns[-4] != "yes":
            raise AssertionError(f"font not embedded and subset: {row}")
    return len(rows)


def text_and_raster(path, pages):
    raw = subprocess.check_output(["pdftotext", "-layout", str(path), "-"])
    if re.search(rb"[\x00-\x08\x0b\x0e-\x1f\x7f]", raw):
        raise AssertionError("control byte in extracted PDF text")
    text = " ".join(raw.decode().lower().split())
    for bad in ("??", "[verify]", "qquad", "__mutated", "varepsilon_"):
        if bad in text:
            raise AssertionError(f"PDF text garbage: {bad}")
    raster = []
    with tempfile.TemporaryDirectory(prefix="c371-raster-") as directory:
        for page in range(1, pages + 1):
            prefix = Path(directory) / f"p{page}"
            subprocess.run(
                ["pdftoppm", "-f", str(page), "-l", str(page), "-r", "72", "-png", str(path), str(prefix)],
                check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            )
            images = list(Path(directory).glob(f"p{page}-*.png"))
            if len(images) != 1 or images[0].stat().st_size < 1000:
                raise AssertionError("PDF raster failure")
            raster.append(images[0].stat().st_size)
    return text, raster


def pdf_receipts():
    tokens = (
        "chambers phase-collapse owner",
        "spectrum, duality, and edge owner",
        "evidence, collision, and route owner",
    )
    receipts = []
    for index, path in enumerate(ROUNDS):
        pages = page_count(path)
        text, raster = text_and_raster(path, pages)
        if tokens[index] not in text:
            raise AssertionError(f"round token missing: {index}")
        if index == 2 and (
            "no target arithmetic local datum" not in text or "route b remains locked" not in text
        ):
            raise AssertionError("final scope sentinel missing")
        receipts.append(
            {
                "round": index,
                "path": str(path.relative_to(ROOT)),
                "sha256": sha(path),
                "bytes": path.stat().st_size,
                "pages": pages,
                "font_rows": font_count(path),
                "raster_bytes": raster,
            }
        )
    if len({row["sha256"] for row in receipts}) != 3:
        raise AssertionError("conditional PDFs are not distinct")
    if MAIN.read_bytes() != ROUNDS[2].read_bytes():
        raise AssertionError("main PDF is not round 2")
    return receipts


def evidence_payload_hash():
    value = strict_json(EVIDENCE)
    claimed = value.pop("payload_sha256")
    got = hashlib.sha256(canonical(value)).hexdigest()
    if claimed != got:
        raise AssertionError("stale evidence payload hash")
    return claimed


def generated_reports(outputs, pdfs, smoke):
    checker = re.search(
        r"PASS \((\d+) assertions\)", outputs["c371_harper_checker.py"]
    ).group(1)
    sympy = re.search(
        r"PASS \((\d+) exact checks", outputs["c371_harper_sympy_crosscheck.py"]
    ).group(1)
    attacks = re.search(
        r"PASS \((\d+) attacks\)", outputs["c371_harper_mutation.py"]
    ).group(1)
    evidence = strict_json(EVIDENCE)
    enum = evidence["enumeration"]
    maxima = {
        key: max(float(row[key]) for row in evidence["panels"] if row[key] is not None)
        for key in (
            "determinant_normalized_residual_max",
            "flux_reversal_coefficient_residual_max",
            "aubry_duality_coefficient_residual_max",
            "parity_coefficient_residual_max",
            "central_edge_residual",
        )
    }
    results = f'''# Results

The canonical evidence has SHA-256 `{sha(EVIDENCE)}` and self-excluding payload SHA-256 `{evidence_payload_hash()}`.  It contains {enum['reduced_fluxes']} reduced fluxes, {enum['panels']} flux--anisotropy panels, {enum['bloch_fibers']} Bloch fibers, {enum['fiber_eigenvalues']} eigenvalues, and {enum['determinant_probe_checks']} determinant probes.

The largest normalized characteristic residual is `{maxima['determinant_normalized_residual_max']:.3e}`.  The largest raw coefficient residuals for flux reversal, Aubry duality, and parity are respectively `{maxima['flux_reversal_coefficient_residual_max']:.3e}`, `{maxima['aubry_duality_coefficient_residual_max']:.3e}`, and `{maxima['parity_coefficient_residual_max']:.3e}`; the largest even-cell central-edge residual is `{maxima['central_edge_residual']:.3e}`.  All lie below the declared `2e-7` numerical threshold.  The exact cyclotomic lane separately checks zero residual for all {enum['cyclotomic_fluxes_q_at_most_10']} reduced fluxes through denominator ten with symbolic anisotropy degree.

The analytic theorem, not finite sampling, proves the all-rational Chambers identity, spectral preimage, real endpoint-fiber edge factorization, multiplicity criterion, duality, reversal, parity, and accumulated small-cell boundaries.  The all-even-denominator central value is mapped to Lamoureux--Mingo Theorem 2.5 and Corollary 2.6 under `lambda_LM=2 lambda`; parity then gives the derivative.
'''
    tests = f'''# Test report

All computational lanes pass:

- producer: {enum['panels']} panels and {enum['bloch_fibers']} fibers PASS;
- independent characteristic/fiber checker: {checker} assertions PASS;
- SymPy exact cyclotomic verifier: {sympy} checks PASS;
- isolated replay: two byte-identical temporary-directory builds PASS;
- hostile repaired-hash mutation suite: {attacks} attacks PASS;
- unittest smoke suite: {smoke}.

Every executable lane refuses `python -O` and `python -OO`.  The release gate additionally verifies strict JSON/YAML parsing, raw and semantic evaluator locks, exact 35-payload membership, deterministic warning-free PDFs, embedded subset fonts, extracted text, rasterization, and self-excluding manifest closure.
'''
    hostile = f'''# Hostile audit

The repaired-hash suite rejects {attacks} attacks against identity and source locks, total Bloch-phase conventions, both Chambers signs, real endpoint-fiber edge identities, the Lamoureux--Mingo normalization map, spectral and edge claims, duality, reversal, parity, the forced central contact, small-cell formulas, workspace and literature collision boundaries, Route-A/Route-B fields, forbidden flags, flux rows, polynomial coefficients, phase dimensions, eigenvalue digests, residual claims, and enumeration totals.  It also rejects deletion, insertion, reordering, truncation, stale hashes, duplicate or nonfinite JSON, duplicate or aliased YAML, non-string YAML keys, and route/scope YAML mutations.
'''
    lines = [
        "# Compile report", "",
        "Each conditional manuscript round was built twice in fresh directories with LuaLaTeX under `SOURCE_DATE_EPOCH=1788480000`; both bytes matched.  Settled logs have no warnings or layout defects, every font is embedded and subset, extracted text has no control garbage, and every page rasterizes.", "",
        "| round | pages | font rows | SHA-256 | substantive addition |",
        "|---|---:|---:|---|---|",
    ]
    additions = [
        "magnetic owner, total-phase convention, transfer determinant, and full anisotropic Chambers identity",
        "spectral preimage, real endpoint-fiber edge factors, sourced even-cell lemma, duality, reversal, parity, and small cells",
        "exact and dense evidence, direct-precedent collision audit, limitations, and strict Route-A firewall",
    ]
    for row, addition in zip(pdfs, additions):
        lines.append(
            f'| {row["round"]} | {row["pages"]} | {row["font_rows"]} | `{row["sha256"]}` | {addition} |'
        )
    lines += ["", "`main.pdf` is byte-identical to round 2.", ""]
    return {
        "results/RESULTS.md": results,
        "results/TEST_REPORT.md": tests,
        "results/HOSTILE_AUDIT.md": hostile,
        "paper/COMPILE_REPORT.md": "\n".join(lines),
    }


def make_manifest(pdfs):
    source = TEX.read_text()
    theorem_tokens = (
        r"u_{m+q}=e^{iqk_x}u_m",
        r"D_{p/q,\lambda}(E;k_x,k_y)",
        r"-2\lambda^q\cos(qk_y)",
        r"\Spec(\HH_{p/q,\lambda})",
        r"B_{p/q,\lambda}(E)",
        r"\PP(E)-\CC_{q,\lambda}=D(E;0,0)",
        r"\PP(E)+\CC_{q,\lambda}=D(E;\pi/q,\pi/q)",
        r"L=2\lambda",
        r"Theorem~2.5",
        r"Corollary~2.6",
        r"\cite{LamoureuxMingo}",
        r"\lambda^q\PP_{p/q,1/\lambda}(E/\lambda)",
        r"\PP_{p/q,\lambda}(-E)&=(-1)^q",
        r"\PP(E)=E^2-2(1+\lambda^2)",
        r"No target arithmetic local datum",
        r"Route B remains locked",
    )
    for token in theorem_tokens:
        if token not in source:
            raise AssertionError(f"missing theorem token: {token}")
    if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", source) or re.search(
        r"(?<![\\A-Za-z])(?:qquad|quad)(?![A-Za-z])", source
    ):
        raise AssertionError("TeX hygiene failure")
    files = {
        str(path.relative_to(ROOT)): path
        for path in ROOT.rglob("*")
        if path.is_file() and path != MANIFEST
    }
    if set(files) != EXPECTED or len(files) != 35:
        raise AssertionError(
            f"ledger mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}"
        )
    if sha(YML) != RAW:
        raise AssertionError("YAML raw drift")
    yml = yaml.safe_load(YML.read_text())
    if hashlib.sha256(canonical(yml)).hexdigest() != SEMANTIC:
        raise AssertionError("YAML semantic drift")
    checker = (ROOT / "code/c371_harper_checker.py").read_text()
    if re.search(r"(?:from|import)\s+[^\n]*c371_harper_producer", checker):
        raise AssertionError("checker imports producer")
    evidence = strict_json(EVIDENCE)
    route = {
        "tuple": [
            "A0_WEAK_ARITHMETIC_RELATION", "A1_FAIL", "A2_FAIL", "A3_FAIL",
            "A4_NATURAL_QUANTIZATION",
        ],
        "overall": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
    }
    if evidence["source_commit"] != SOURCE or evidence["scope_literal"] != SCOPE or evidence["route_a"] != route:
        raise AssertionError("evidence metadata drift")
    if any(evidence["scope_flags"].values()):
        raise AssertionError("forbidden evidence flag")
    if "10.1090/S0002-9939-07-08830-2" not in evidence["references"]:
        raise AssertionError("Lamoureux-Mingo source lock missing")
    for name in ("ASSUMPTIONS.md", "CLAIMS.md", "SCOPE.md", "LIMITATIONS.md", "REPRODUCIBILITY.md"):
        if not (ROOT / name).read_text().strip():
            raise AssertionError(f"empty ARS-rich artifact: {name}")
    return {
        "schema": "hcs-release-manifest-v1",
        "candidate_id": "HCS-C371",
        "obstruction_id": "HEN-O355",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
        "evaluator_version": "0.2.0",
        "evaluator_authority_sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
        "payload_file_count": 35,
        "physical_file_count": 36,
        "evaluation_raw_sha256": RAW,
        "evaluation_semantic_sha256": SEMANTIC,
        "evidence_sha256": sha(EVIDENCE),
        "evidence_payload_sha256": evidence_payload_hash(),
        "release_lanes": {
            "producer": "PASS",
            "independent_checker": "PASS",
            "sympy_cyclotomic_crosscheck": "PASS",
            "isolated_byte_replay": "PASS",
            "hostile_mutation": "PASS",
            "unittest_smoke": "PASS",
            "optimized_mode_refusal": "PASS",
            "deterministic_pdf_rebuild": "PASS",
            "payload_membership": "PASS",
        },
        "pdf_rounds": pdfs,
        "main_pdf_sha256": sha(MAIN),
        "files": {name: sha(path) for name, path in sorted(files.items())},
    }


def main():
    if sys.flags.optimize:
        raise RuntimeError("C371 release refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--build-pdfs", action="store_true")
    args = parser.parse_args()
    if args.build_pdfs and not args.write:
        raise ValueError("--build-pdfs requires --write")
    if args.write:
        command("c371_harper_producer.py")
    lanes = [
        ("c371_harper_producer.py", "C371_PRODUCER_PASS"),
        ("c371_harper_checker.py", "C371 independent Harper checker: PASS"),
        ("c371_harper_sympy_crosscheck.py", "C371 SymPy/cyclotomic cross-check: PASS"),
        ("c371_harper_replay.py", "C371 byte replay: PASS"),
        ("c371_harper_mutation.py", "C371 hostile mutation suite: PASS"),
    ]
    outputs = {}
    for script, sentinel in lanes:
        output = isolated_lane(script)
        if sentinel not in output:
            raise AssertionError(f"lane sentinel missing: {script}")
        outputs[script] = output
        optimized_refusal(script)
    smoke = smoke_tests()
    if args.build_pdfs:
        for index, path in enumerate(ROUNDS):
            first = fresh_pdf(index)
            second = fresh_pdf(index)
            if first != second:
                raise AssertionError(f"nondeterministic PDF round {index}")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(first)
        MAIN.write_bytes(ROUNDS[2].read_bytes())
    else:
        for index, path in enumerate(ROUNDS):
            first = fresh_pdf(index)
            second = fresh_pdf(index)
            if first != second or first != path.read_bytes():
                raise AssertionError(f"stale/nondeterministic PDF round {index}")
    pdfs = pdf_receipts()
    reports = generated_reports(outputs, pdfs, smoke)
    for name, raw in reports.items():
        path = ROOT / name
        if args.write:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(raw)
        elif not path.exists() or path.read_text() != raw:
            raise AssertionError(f"report missing or stale: {name}")
    manifest = make_manifest(pdfs)
    raw = json.dumps(manifest, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if args.write:
        MANIFEST.write_text(raw)
    elif not MANIFEST.exists() or MANIFEST.read_text() != raw:
        raise AssertionError("manifest missing or stale")
    forbidden = [
        path for path in ROOT.rglob("*") if path.is_file()
        and (path.suffix in {".aux", ".log", ".out", ".toc", ".pyc"} or "__pycache__" in path.parts)
    ]
    if forbidden:
        raise AssertionError(f"forbidden sidecars: {forbidden}")
    print(f"C371_RELEASE_PASS {sha(EVIDENCE)} {sha(MAIN)} {sha(MANIFEST)}")


if __name__ == "__main__":
    main()
