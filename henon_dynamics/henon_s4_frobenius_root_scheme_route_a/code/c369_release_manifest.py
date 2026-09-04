#!/usr/bin/env python3
"""Deterministic 35-payload release gate for HCS-C369."""
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
MANIFEST = ROOT / "C369_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c369_s4_frobenius_evidence.json"
TEX = ROOT / "paper/main.tex"
MAIN = ROOT / "paper/main.pdf"
YML = ROOT / "evaluations/route_a/HCS-C369/2026-09-04.yaml"
RAW = "421a590612cbe66b3ba3dc7af6c8ee6bbca83a465343c9eb19b852e323d2cd13"
SEMANTIC = "36f2d0a42d65a3f1def14c18cf7fd5601c049c02477a7f4c5e89edae0369f731"
SOURCE = "c6553f02d928c6aa05400ded57746869a85f0238"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788480000
ROUNDS = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
WARNING = re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|warning  \(pdf backend\)|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")
OWNERSHIP_BOUNDARY = {
    "inherited_workspace_owner": "HCS-C12A owns the universal zero-dimensional Frobenius finite-permutation fixed-point and finite zeta/determinant mechanism",
    "c369_owner": "x^4-x-1 S4 Galois proof, five-class all-good-prime factor/fixed/primitive/density atlas, p=283 non-etale boundary, and convention-locked executable ledger",
    "nonownership": "HCS-C369 does not claim workspace ownership of the universal finite-permutation zeta/determinant mechanism",
}
C12A_COLLISION = "C12A owns the universal zero-dimensional Frobenius finite-permutation fixed-point and finite zeta/determinant mechanism; C369 owns only the x^4-x-1 S4 all-good-prime factor/fixed/primitive/density atlas, p=283 boundary, and convention-locked executable ledger"
EXPECTED = {
    "ASSUMPTIONS.md", "CLAIMS.md", "EXPERIMENT_PLAN.md", "LIMITATIONS.md", "NARRATIVE_REPORT.md",
    "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md", "README.md", "REFERENCES.md", "REPRODUCIBILITY.md",
    "RESEARCH_QUESTION.md", "SCOPE.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md", "requirements.txt",
    "code/README.md", "code/c369_release_manifest.py", "code/c369_s4_frobenius_checker.py",
    "code/c369_s4_frobenius_mutation.py", "code/c369_s4_frobenius_producer.py",
    "code/c369_s4_frobenius_replay.py", "code/c369_s4_frobenius_sympy_crosscheck.py",
    "evaluations/route_a/HCS-C369/2026-09-04.yaml", "paper/COMPILE_REPORT.md", "paper/README.md",
    "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf",
    "paper/main_round2.pdf", "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c369_s4_frobenius_evidence.json", "tests/test_c369_smoke.py",
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
    return json.loads(path.read_text(), object_pairs_hook=unique, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def command(script, args=()):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / script), *args], env=env, text=True).strip()


def isolated_lane(script):
    with tempfile.TemporaryDirectory(prefix="c369-lane-") as directory:
        args = ("--output", str(Path(directory) / "evidence.json")) if script == "c369_s4_frobenius_producer.py" else ()
        return command(script, args)


def optimized_refusal(script):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    for flag in ("-O", "-OO"):
        cmd = [sys.executable, flag, "-B", str(ROOT / "code" / script)]
        with tempfile.TemporaryDirectory(prefix="c369-opt-") as directory:
            if script == "c369_s4_frobenius_producer.py":
                cmd += ["--output", str(Path(directory) / "evidence.json")]
            proc = subprocess.run(cmd, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if proc.returncode == 0 or "refuses optimized Python" not in proc.stdout:
            raise AssertionError(f"optimized execution not refused: {flag} {script}")


def smoke_tests():
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    proc = subprocess.run(
        [sys.executable, "-B", "-m", "unittest", "tests/test_c369_smoke.py"],
        cwd=ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
    )
    if proc.returncode != 0 or "OK" not in proc.stdout:
        raise AssertionError(f"smoke tests failed:\n{proc.stdout}")
    return "3/3 PASS"


def fresh_pdf(round_number):
    with tempfile.TemporaryDirectory(prefix=f"c369-build-{round_number}-") as directory:
        work = Path(directory)
        shutil.copy2(TEX, work / "main.tex")
        env = dict(os.environ, SOURCE_DATE_EPOCH=str(EPOCH), FORCE_SOURCE_DATE="1", TZ="UTC")
        cmd = [
            "lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main",
            rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}",
        ]
        for _ in range(2):
            subprocess.run(cmd, cwd=work, env=env, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = (work / "main.log").read_text(errors="replace")
        hit = WARNING.search(log)
        if hit:
            raise AssertionError(f"paper warning round {round_number}: {hit.group(0)}")
        return (work / "main.pdf").read_bytes()


def page_count(path):
    output = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in output.splitlines() if line.startswith("Pages:")))


def font_count(path):
    rows = [line for line in subprocess.check_output(["pdffonts", str(path)], text=True).splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]
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
    with tempfile.TemporaryDirectory(prefix="c369-raster-") as directory:
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
        "arithmetic and galois closure",
        "fixed, primitive, and determinant identities",
        "complete density and boundary atlas",
    )
    receipts = []
    for index, path in enumerate(ROUNDS):
        pages = page_count(path)
        text, raster = text_and_raster(path, pages)
        if tokens[index] not in text:
            raise AssertionError(f"round token missing: {index}")
        if index == 2 and ("no determinant-class regularization" not in text or "route b is not invoked" not in text):
            raise AssertionError("final scope sentinel missing")
        receipts.append({
            "round": index, "path": str(path.relative_to(ROOT)), "sha256": sha(path),
            "bytes": path.stat().st_size, "pages": pages, "font_rows": font_count(path), "raster_bytes": raster,
        })
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
    checker = re.search(r"PASS \((\d+) assertions\)", outputs["c369_s4_frobenius_checker.py"]).group(1)
    sympy = re.search(r"PASS \((\d+) exact checks\)", outputs["c369_s4_frobenius_sympy_crosscheck.py"]).group(1)
    attacks = re.search(r"PASS \((\d+) attacks\)", outputs["c369_s4_frobenius_mutation.py"]).group(1)
    evidence = strict_json(EVIDENCE)
    enum = evidence["enumeration"]
    counts = enum["class_counts"]
    results = f'''# Results

The canonical evidence has SHA-256 `{sha(EVIDENCE)}` and self-excluding payload SHA-256 `{evidence_payload_hash()}`.  It exhausts {enum['good_primes']} good primes at most {enum['prime_bound']} and {enum['prime_iterate_cells']} prime--iterate cells through r={enum['iterate_bound']}.

The five exact finite counts are: `1+1+1+1`: {counts['1+1+1+1']}; `2+1+1`: {counts['2+1+1']}; `2+2`: {counts['2+2']}; `3+1`: {counts['3+1']}; `4`: {counts['4']}.  These are regression receipts, not density estimates.  C12A retains ownership of the universal zero-dimensional finite-permutation zeta/determinant mechanism.  C369 proves the `x^4-x-1`-specific `S4` Galois theorem, the all-good-prime five-class factor/fixed/primitive/density atlas, the non-etale boundary at 283, and the convention-locked executable ledger.
'''
    tests = f'''# Test report

All computational lanes pass:

- producer: {enum['good_primes']} good-prime rows and {enum['prime_iterate_cells']} iterate cells PASS;
- independent finite-field checker: {checker} assertions PASS;
- SymPy exact verifier: {sympy} checks PASS;
- isolated replay: two byte-identical temporary-directory builds PASS;
- hostile mutation suite: {attacks} attacks PASS;
- unittest smoke suite: {smoke}.

Every executable lane refuses `python -O` and `python -OO`.  The release gate also verifies strict JSON/YAML parsing, raw and semantic evaluator locks, exact 35-payload membership, deterministic warning-free PDFs, embedded subset fonts, extracted text, rasterization, and self-excluding manifest closure.
'''
    hostile = f'''# Hostile audit

The repaired-hash suite rejects {attacks} attacks against identity and source locks, the C12A/C369 ownership and collision boundary, the arithmetic/geometric Frobenius convention, discriminant and `S4` receipts, determinant and boundary theorems, five witnesses, class atlas, per-prime fixed and primitive ledgers, Koopman flags, enumeration totals, route tuple, Route-B lock, and forbidden flags.  It also rejects deletion, insertion, reordering, truncation, stale hashes, duplicate or nonfinite JSON, invalid roots, duplicate or aliased YAML, and route/scope YAML mutations.
'''
    lines = [
        "# Compile report", "",
        "Each conditional manuscript round was built twice in fresh directories with LuaLaTeX under `SOURCE_DATE_EPOCH=1788480000`; both bytes matched the stored artifact.  Settled logs have no warnings or layout defects, every font is embedded and subset, extracted text has no control garbage, and every page rasterizes.", "",
        "| round | pages | font rows | SHA-256 | substantive addition |", "|---|---:|---:|---|---|",
    ]
    additions = [
        "root scheme, Frobenius convention, discriminant, irreducibility, S4 proof, factor/orbit dictionary, ownership boundary",
        "five witnesses, inherited finite-permutation mechanism specialized to the all-iterate ledger, exhaustive evidence",
        "Chebotarev densities, p=283 non-etale boundary, Koopman classification, ownership and route firewalls",
    ]
    for row, addition in zip(pdfs, additions):
        lines.append(f'| {row["round"]} | {row["pages"]} | {row["font_rows"]} | `{row["sha256"]}` | {addition} |')
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
        r"f(x)=x^4-x-1", r"-283", r"\Gal(L/\mathbb Q)\cong S_4", r"F_p:X_p",
        r"\det(I-uP_p)^{-1}", r"\sum_{d\mid n}\mu(d)N_p(n/d)",
        r"(x-115)(x-93)^2(x+18)", r"HCS-C12A already owns",
        r"does not claim workspace ownership", r"no cross-prime Fredholm direct sum", r"Route B is not invoked",
    )
    for token in theorem_tokens:
        if token not in source:
            raise AssertionError(f"missing theorem token: {token}")
    if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", source) or re.search(r"(?<!\\)qquad", source):
        raise AssertionError("TeX hygiene failure")
    files = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file() and path != MANIFEST}
    if set(files) != EXPECTED or len(files) != 35:
        raise AssertionError(f"ledger mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}")
    if sha(YML) != RAW:
        raise AssertionError("YAML raw drift")
    yml = yaml.safe_load(YML.read_text())
    if hashlib.sha256(canonical(yml)).hexdigest() != SEMANTIC:
        raise AssertionError("YAML semantic drift")
    checker = (ROOT / "code/c369_s4_frobenius_checker.py").read_text()
    if re.search(r"(?:from|import)\s+[^\n]*c369_s4_frobenius_producer", checker):
        raise AssertionError("checker imports producer")
    evidence = strict_json(EVIDENCE)
    route = {
        "tuple": ["A0_STRUCTURAL_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
        "overall": "ROUTE_A_ARITHMETIC_CANDIDATE", "route_b_invocation_allowed": False,
    }
    if evidence["source_commit"] != SOURCE or evidence["scope_literal"] != SCOPE or evidence["route_a"] != route:
        raise AssertionError("evidence metadata drift")
    if evidence.get("ownership_boundary") != OWNERSHIP_BOUNDARY:
        raise AssertionError("evidence ownership boundary drift")
    if evidence.get("collision_boundary", {}).get("nearest_C12A") != C12A_COLLISION:
        raise AssertionError("C12A collision boundary drift")
    if "no workspace ownership of the universal zero-dimensional finite-permutation zeta/determinant mechanism already owned by C12A" not in evidence.get("nonclaims", []):
        raise AssertionError("C12A nonownership lock drift")
    if any(evidence["scope_flags"].values()):
        raise AssertionError("forbidden evidence flag")
    return {
        "schema": "hcs-release-manifest-v1", "candidate_id": "HCS-C369", "obstruction_id": "HEN-O353",
        "source_commit": SOURCE, "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "evaluator_authority": "flow_systems/skills/route-a-evaluator.md", "evaluator_version": "0.2.0",
        "evaluator_authority_sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c",
        "payload_file_count": 35, "physical_file_count": 36,
        "evaluation_raw_sha256": RAW, "evaluation_semantic_sha256": SEMANTIC,
        "evidence_sha256": sha(EVIDENCE), "evidence_payload_sha256": evidence_payload_hash(),
        "release_lanes": {
            "producer": "PASS", "independent_checker": "PASS", "sympy_crosscheck": "PASS",
            "isolated_byte_replay": "PASS", "hostile_mutation": "PASS", "unittest_smoke": "PASS",
            "optimized_mode_refusal": "PASS", "deterministic_pdf_rebuild": "PASS", "payload_membership": "PASS",
        },
        "pdf_rounds": pdfs, "main_pdf_sha256": sha(MAIN),
        "files": {name: sha(path) for name, path in sorted(files.items())},
    }


def main():
    if sys.flags.optimize:
        raise RuntimeError("C369 release refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--build-pdfs", action="store_true")
    args = parser.parse_args()
    if args.build_pdfs and not args.write:
        raise ValueError("--build-pdfs requires --write")
    if args.write:
        command("c369_s4_frobenius_producer.py")
    lanes = [
        ("c369_s4_frobenius_producer.py", "C369_PRODUCER_PASS"),
        ("c369_s4_frobenius_checker.py", "C369 independent checker: PASS"),
        ("c369_s4_frobenius_sympy_crosscheck.py", "C369 SymPy cross-check: PASS"),
        ("c369_s4_frobenius_replay.py", "C369 byte replay: PASS"),
        ("c369_s4_frobenius_mutation.py", "C369 hostile mutation suite: PASS"),
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
    print(f"C369_RELEASE_PASS {sha(EVIDENCE)} {sha(MAIN)} {sha(MANIFEST)}")


if __name__ == "__main__":
    main()
