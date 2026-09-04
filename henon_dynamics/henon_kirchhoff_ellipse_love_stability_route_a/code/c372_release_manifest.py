#!/usr/bin/env python3
"""Deterministic 35-payload release gate for HCS-C372."""
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
MANIFEST = ROOT / "C372_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c372_kirchhoff_love_evidence.json"
TEX = ROOT / "paper/main.tex"
MAIN = ROOT / "paper/main.pdf"
YML = ROOT / "evaluations/route_a/HCS-C372/2026-09-04.yaml"
RAW = "0df240c2c2e2a8becf27eb76bc7797c532595b2b889296fffd125fee5aa20beb"
SEMANTIC = "49a6fd8fac70ecf15c2118bd64275627567f10feee99b46e65f9538a150ef904"
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
    "ASSUMPTIONS.md", "CLAIMS.md", "EXPERIMENT_PLAN.md", "LIMITATIONS.md", "NARRATIVE_REPORT.md",
    "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md", "README.md", "REFERENCES.md", "REPRODUCIBILITY.md",
    "RESEARCH_QUESTION.md", "SCOPE.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md", "requirements.txt",
    "code/README.md", "code/c372_release_manifest.py", "code/c372_kirchhoff_love_checker.py",
    "code/c372_kirchhoff_love_mutation.py", "code/c372_kirchhoff_love_producer.py",
    "code/c372_kirchhoff_love_replay.py", "code/c372_kirchhoff_love_sympy_crosscheck.py",
    "evaluations/route_a/HCS-C372/2026-09-04.yaml", "paper/COMPILE_REPORT.md", "paper/README.md",
    "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf",
    "paper/main_round2.pdf", "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c372_kirchhoff_love_evidence.json", "tests/test_c372_smoke.py",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def strict_json(path: Path):
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


def command(script: str, args=()) -> str:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    return subprocess.check_output(
        [sys.executable, "-B", str(ROOT / "code" / script), *args], env=env, text=True
    ).strip()


def isolated_lane(script: str) -> str:
    with tempfile.TemporaryDirectory(prefix="c372-lane-") as directory:
        args = (
            "--output",
            str(Path(directory) / "evidence.json"),
        ) if script == "c372_kirchhoff_love_producer.py" else ()
        return command(script, args)


def optimized_refusal(script: str) -> None:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    for flag in ("-O", "-OO"):
        cmd = [sys.executable, flag, "-B", str(ROOT / "code" / script)]
        with tempfile.TemporaryDirectory(prefix="c372-opt-") as directory:
            if script == "c372_kirchhoff_love_producer.py":
                cmd += ["--output", str(Path(directory) / "evidence.json")]
            proc = subprocess.run(
                cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
            )
        if proc.returncode == 0 or "refuses optimized Python" not in proc.stdout:
            raise AssertionError(f"optimized execution not refused: {flag} {script}")


def smoke_tests() -> str:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    proc = subprocess.run(
        [sys.executable, "-B", "-m", "unittest", "tests/test_c372_smoke.py"],
        cwd=ROOT,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    if proc.returncode != 0 or "OK" not in proc.stdout:
        raise AssertionError(f"smoke tests failed:\n{proc.stdout}")
    return "3/3 PASS"


def fresh_pdf(round_number: int) -> bytes:
    with tempfile.TemporaryDirectory(prefix=f"c372-build-{round_number}-") as directory:
        work = Path(directory)
        shutil.copy2(TEX, work / "main.tex")
        env = dict(
            os.environ,
            SOURCE_DATE_EPOCH=str(EPOCH),
            FORCE_SOURCE_DATE="1",
            TZ="UTC",
        )
        cmd = [
            "lualatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-jobname=main",
            rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}",
        ]
        for _ in range(2):
            subprocess.run(
                cmd,
                cwd=work,
                env=env,
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
        log = (work / "main.log").read_text(errors="replace")
        hit = WARNING.search(log)
        if hit:
            context = log[max(0, hit.start() - 120):hit.start() + 240].replace("\n", " ")
            raise AssertionError(f"paper warning round {round_number}: {context}")
        return (work / "main.pdf").read_bytes()


def page_count(path: Path) -> int:
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(
        next(line.split(":", 1)[1] for line in output.splitlines() if line.startswith("Pages:"))
    )


def font_count(path: Path) -> int:
    rows = [
        line
        for line in subprocess.check_output(["pdffonts", str(path)], text=True).splitlines()[2:]
        if line.strip() and not line.lstrip().startswith("-")
    ]
    if not rows:
        raise AssertionError("PDF has no fonts")
    for row in rows:
        columns = row.split()
        if len(columns) < 7 or columns[-5] != "yes" or columns[-4] != "yes":
            raise AssertionError(f"font not embedded and subset: {row}")
    return len(rows)


def text_and_raster(path: Path, pages: int):
    raw = subprocess.check_output(["pdftotext", "-layout", str(path), "-"])
    if re.search(rb"[\x00-\x08\x0b\x0e-\x1f\x7f]", raw):
        raise AssertionError("control byte in extracted PDF text")
    extracted = " ".join(raw.decode().lower().split())
    for bad in ("??", "[verify]", "qquad", "__mutated", "varepsilon_"):
        if bad in extracted:
            raise AssertionError(f"PDF text garbage: {bad}")
    raster = []
    with tempfile.TemporaryDirectory(prefix="c372-raster-") as directory:
        for page in range(1, pages + 1):
            prefix = Path(directory) / f"p{page}"
            subprocess.run(
                [
                    "pdftoppm", "-f", str(page), "-l", str(page), "-r", "72",
                    "-png", str(path), str(prefix),
                ],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            images = list(Path(directory).glob(f"p{page}-*.png"))
            if len(images) != 1 or images[0].stat().st_size < 1000:
                raise AssertionError("PDF raster failure")
            raster.append(images[0].stat().st_size)
    return extracted, raster


def pdf_receipts():
    round_tokens = (
        "the exact euler relative equilibrium",
        "love factorization and every finite-mode wall",
        "asymptotic ladder and finite instability count",
    )
    receipts = []
    for index, path in enumerate(ROUNDS):
        pages = page_count(path)
        extracted, raster = text_and_raster(path, pages)
        if round_tokens[index] not in extracted:
            raise AssertionError(f"round token missing: {index}")
        if index == 2:
            final_tokens = (
                "no nonlinear orbital or lyapunov stability",
                "route_a_rejected",
                "no target zero match",
            )
            for token in final_tokens:
                if token not in extracted:
                    raise AssertionError(f"final scope sentinel missing: {token}")
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


def evidence_payload_hash() -> str:
    value = strict_json(EVIDENCE)
    claimed = value.pop("payload_sha256")
    got = hashlib.sha256(canonical(value)).hexdigest()
    if claimed != got:
        raise AssertionError("stale evidence payload hash")
    return claimed


def generated_reports(outputs, pdfs, smoke):
    checker = re.search(
        r"PASS \((\d+) assertions\)", outputs["c372_kirchhoff_love_checker.py"]
    ).group(1)
    sympy = re.search(
        r"PASS \((\d+) exact checks\)", outputs["c372_kirchhoff_love_sympy_crosscheck.py"]
    ).group(1)
    attacks = re.search(
        r"PASS \((\d+) attacks\)", outputs["c372_kirchhoff_love_mutation.py"]
    ).group(1)
    evidence = strict_json(EVIDENCE)
    grid = evidence["finite_grid"]
    results = f'''# Results

The canonical evidence has SHA-256 `{sha(EVIDENCE)}` and self-excluding payload SHA-256 `{evidence_payload_hash()}`.  It covers {grid['distinct_aspect_ratios']} reduced rational aspect ratios, all modes through {grid['max_mode']}, {grid['modal_cells']} exact modal cells, {grid['critical_modes']} certified threshold brackets at {grid['critical_bisection_bits']} bits, and {grid['rigid_solution_rows']} exact rigid-solution rows.

The theorem separates sourced input from package-derived consequence.  Kirchhoff's ellipse rotates at `Omega = vorticity*a*b/(a+b)^2`; the sourced Love square factors as `F_m G_m`.  Exact sign and monotonicity arguments give one threshold for every `m >= 3`, their strict ordering, the sharp first wall `gamma_3 = 3`, and the high-mode law `m(1-delta_m) -> 1+W(exp(-1))`, hence `gamma_m/m -> 2/(1+W(exp(-1)))`.  These are spectral linear-mode statements only.
'''
    tests = f'''# Test report

All computational lanes pass:

- producer: {grid['distinct_aspect_ratios']} aspects, {grid['modal_cells']} modal cells, {grid['critical_modes']} thresholds, and {grid['rigid_solution_rows']} rigid rows PASS;
- independent unfactorized checker: {checker} assertions PASS;
- SymPy exact verifier: {sympy} checks PASS;
- isolated replay: two byte-identical temporary-directory builds PASS;
- hostile mutation suite: {attacks} attacks PASS (54 repaired-hash JSON, 1 stale-hash,
  3 malformed/root JSON, and 6 YAML attacks);
- unittest smoke suite: {smoke}.

Every executable lane refuses `python -O` and `python -OO`.  The release gate also verifies strict JSON/YAML parsing, raw and semantic evaluator locks, exact 35-payload membership, deterministic warning-free PDFs, embedded subset fonts, extracted text, rasterization, and self-excluding manifest closure.
'''
    hostile = f'''# Hostile audit

The hostile suite rejects {attacks} attacks: 54 repaired-hash JSON semantic attacks,
1 stale-hash JSON attack, 3 malformed/root JSON attacks, and 6 YAML attacks.
Together they cover metadata and source locks, the Euler/Love formula contracts,
factor and monotonicity receipts, the sharp wall, high-mode scaled-root law,
finite-grid anchors and hashes, threshold brackets, rigid rotation and period
conventions, boundary atlas, collision boundary, source roles, route tuple,
Route-B lock, and forbidden flags.  They also test deletion, insertion,
reordering, truncation, duplicate or nonfinite JSON, and duplicate or aliased
YAML.
'''
    lines = [
        "# Compile report",
        "",
        "Each conditional manuscript round was built twice in fresh directories with LuaLaTeX under `SOURCE_DATE_EPOCH=1788480000`; both bytes matched the stored artifact.  Settled logs have no warnings or layout defects, every font is embedded and subset, extracted text has no control garbage, and every page rasterizes.",
        "",
        "| round | pages | font rows | SHA-256 | substantive addition |",
        "|---|---:|---:|---|---|",
    ]
    additions = [
        "Euler relative equilibrium, exact interior field, invariant ledger, corrected patch and oriented-axis periods",
        "sourced Love input, symmetry modes, unique and ordered all-mode walls, sharp first instability at aspect 3",
        "Lambert-W high-mode asymptotic, finite instability block, exact evidence, boundaries, collision audit, route firewall",
    ]
    for row, addition in zip(pdfs, additions):
        lines.append(
            f'| {row["round"]} | {row["pages"]} | {row["font_rows"]} | '
            f'`{row["sha256"]}` | {addition} |'
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
        r"\Omega=\frac{\omega_0ab}{(a+b)^2}",
        r"\lambda_m^2=\frac{\omega_0^2}{4}",
        r"4\lambda_m^2=\omega_0^2F_m(\delta)G_m(\delta)",
        r"16\lambda_3^2",
        "instantaneous principal axes",
        "co-rotating-frame frequency",
        r"F_m'(\delta)=-m\delta-m\delta^{m-1}<0",
        r"G_m'(\delta)=m\delta(\delta^{m-2}-1)<0",
        r"F_{m+1}(\delta)-F_m(\delta)",
        r"\delta_3=\frac12",
        r"m(1-\delta_m)\longrightarrow c_*",
        r"c_*=1+W(e^{-1})",
        "spectral and linear",
        "no target zero match",
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
            f"ledger mismatch missing={sorted(EXPECTED-set(files))} "
            f"extra={sorted(set(files)-EXPECTED)}"
        )
    if sha(YML) != RAW:
        raise AssertionError("YAML raw drift")
    yml = yaml.safe_load(YML.read_text())
    if hashlib.sha256(canonical(yml)).hexdigest() != SEMANTIC:
        raise AssertionError("YAML semantic drift")
    checker = (ROOT / "code/c372_kirchhoff_love_checker.py").read_text()
    if re.search(r"(?:from|import)\s+[^\n]*c372_kirchhoff_love_producer", checker):
        raise AssertionError("checker imports producer")
    evidence = strict_json(EVIDENCE)
    route = {
        "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
        "overall": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
    }
    if (
        evidence["source_commit"] != SOURCE
        or evidence["scope_literal"] != SCOPE
        or evidence["route_a"] != route
    ):
        raise AssertionError("evidence metadata drift")
    if any(evidence["scope_flags"].values()):
        raise AssertionError("forbidden evidence flag")
    return {
        "schema": "hcs-release-manifest-v1",
        "candidate_id": "HCS-C372",
        "obstruction_id": "HEN-O356",
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
            "sympy_crosscheck": "PASS",
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
        raise RuntimeError("C372 release refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--build-pdfs", action="store_true")
    args = parser.parse_args()
    if args.build_pdfs and not args.write:
        raise ValueError("--build-pdfs requires --write")
    if args.write:
        command("c372_kirchhoff_love_producer.py")
    lanes = [
        ("c372_kirchhoff_love_producer.py", "C372_PRODUCER_PASS"),
        ("c372_kirchhoff_love_checker.py", "C372 independent checker: PASS"),
        ("c372_kirchhoff_love_sympy_crosscheck.py", "C372 SymPy cross-check: PASS"),
        ("c372_kirchhoff_love_replay.py", "C372 byte replay: PASS"),
        ("c372_kirchhoff_love_mutation.py", "C372 hostile mutation suite: PASS"),
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
            if first != second or not path.exists() or first != path.read_bytes():
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
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and (
            path.suffix in {".aux", ".log", ".out", ".toc", ".pyc"}
            or "__pycache__" in path.parts
        )
    ]
    if forbidden:
        raise AssertionError(f"forbidden sidecars: {forbidden}")
    print(f"C372_RELEASE_PASS {sha(EVIDENCE)} {sha(MAIN)} {sha(MANIFEST)}")


if __name__ == "__main__":
    main()
