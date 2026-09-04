#!/usr/bin/env python3
"""Deterministic 38-payload release gate for HCS-C378."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c378 release refuses optimized Python")

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
MANIFEST = ROOT / "C378_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c378_dyson_ou_evidence.json"
TEX = ROOT / "paper/main.tex"
MAIN_PDF = ROOT / "paper/main.pdf"
EVALUATION = ROOT / "evaluations/route_a/HCS-C378/2026-09-04.yaml"
YAML_RAW_SHA = "b70bfed7319e0ebfd5697491a29c11bd803eab74f66fb303a6f3d11c1e475af9"
YAML_SEMANTIC_SHA = "6d374dfee088737ada5dc669e7b597844b6da08d26ce5e7ec13313df03766b3f"
AUTHORITY = "flow_systems/skills/route-a-evaluator.md"
AUTHORITY_VERSION = "0.2.0"
AUTHORITY_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
PDF_NAMES = ("main_round0_original.pdf", "main_round1.pdf", "main_round2.pdf")
WRAPPER_NAMES = ("main_round0.tex", "main_round1.tex", "main_round2.tex")
EXPECTED = (
    "ASSUMPTIONS.md", "CLAIMS.md", "EXPERIMENT_PLAN.md", "LIMITATIONS.md",
    "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md", "README.md",
    "REFERENCES.md", "REPRODUCIBILITY.md", "RESEARCH_QUESTION.md", "SCOPE.md",
    "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md", "requirements.txt", "code/README.md",
    "code/c378_dyson_ou_checker.py", "code/c378_dyson_ou_mutation.py",
    "code/c378_dyson_ou_producer.py", "code/c378_dyson_ou_replay.py",
    "code/c378_dyson_ou_sympy_crosscheck.py", "code/c378_release_manifest.py",
    "evaluations/route_a/HCS-C378/2026-09-04.yaml", "paper/COMPILE_REPORT.md",
    "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0.tex", "paper/main_round1.tex", "paper/main_round2.tex", "paper/main_round0_original.pdf",
    "paper/main_round1.pdf", "paper/main_round2.pdf", "results/HOSTILE_AUDIT.md",
    "results/RESULTS.md", "results/TEST_REPORT.md", "results/c378_dyson_ou_evidence.json",
    "tests/test_c378_smoke.py",
)
SCRIPTS = (
    "c378_dyson_ou_producer.py", "c378_dyson_ou_checker.py",
    "c378_dyson_ou_sympy_crosscheck.py", "c378_dyson_ou_replay.py",
    "c378_dyson_ou_mutation.py", "c378_release_manifest.py",
)
WARNING_PATTERN = re.compile(
    r"(?:LaTeX|Package [^:\n]+) Warning:|warning  \(pdf backend\)|Overfull|Underfull|"
    r"undefined (?:references|citations)|Rerun to get|Missing character"
)
UNESCAPED_TEX_SPACING_PATTERN = re.compile(r"(?<!\\)\b(?:quad|qquad)\b")
ROUND_TITLES = (
    "Beta-Two Dyson–Ornstein–Uhlenbeck Diffusion: Matrix Radialization and Ordered GUE Equilibrium",
    "Beta-Two Dyson–Ornstein–Uhlenbeck Diffusion: Exact Chamber Kernel and Noncollision",
    "Beta-Two Dyson–Ornstein–Uhlenbeck Diffusion: Exact Chamber Kernel and Complete Partition Spectrum",
)
ROUND_TITLE_SUFFIXES = (
    "Matrix Radialization and Ordered GUE Equilibrium",
    "Exact Chamber Kernel and Noncollision",
    "Exact Chamber Kernel and Complete Partition Spectrum",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command, **kwargs) -> str:
    process = subprocess.run(command, capture_output=True, text=True, **kwargs)
    if process.returncode:
        raise AssertionError(f"command failed {command}:\n{process.stdout}\n{process.stderr}")
    return process.stdout.strip()


def actual_files():
    return sorted(str(path.relative_to(ROOT)) for path in ROOT.rglob("*") if path.is_file())


def unique_object(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON key {key}")
        value[key] = item
    return value


def strict_json(path: Path):
    return json.loads(
        path.read_text(), object_pairs_hook=unique_object,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)),
    )


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def evidence_payload_hash() -> str:
    value = strict_json(EVIDENCE)
    claimed = value.pop("payload_sha256")
    assert claimed == hashlib.sha256(canonical(value)).hexdigest()
    return claimed


def assert_tex_spacing_hygiene(text: str, label: str):
    match = UNESCAPED_TEX_SPACING_PATTERN.search(text)
    assert match is None, f"unescaped TeX spacing command {match.group(0)!r} in {label}"


def assert_round_title(flat_text: str, round_index: int):
    assert ROUND_TITLES[round_index] in flat_text, (
        f"exact round-{round_index} title missing"
    )
    for other_index, suffix in enumerate(ROUND_TITLE_SUFFIXES):
        if other_index != round_index:
            assert suffix not in flat_text, (
                f"round-{round_index} contains round-{other_index} title content"
            )


def compile_round(round_index: int) -> bytes:
    blobs = []
    for build_index in range(2):
        with tempfile.TemporaryDirectory(prefix=f"c378-tex-r{round_index}-b{build_index}-") as directory:
            work = Path(directory)
            shutil.copy2(TEX, work / "main.tex")
            wrapper = ROOT / "paper" / WRAPPER_NAMES[round_index]
            shutil.copy2(wrapper, work / wrapper.name)
            environment = dict(os.environ, SOURCE_DATE_EPOCH="1788480000", FORCE_SOURCE_DATE="1")
            command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", wrapper.name]
            run(command, cwd=work, env=environment)
            run(command, cwd=work, env=environment)
            log = (work / "main.log").read_text(errors="replace")
            assert not WARNING_PATTERN.search(log), f"settled LaTeX warning in round {round_index}"
            blobs.append((work / "main.pdf").read_bytes())
    assert blobs[0] == blobs[1], f"fresh builds differ in round {round_index}"
    return blobs[0]


def pdf_gate(path: Path, round_index: int):
    info = run(["pdfinfo", str(path)])
    match = re.search(r"^Pages:\s+(\d+)", info, re.MULTILINE)
    assert match
    pages = int(match.group(1))
    assert 2 <= pages <= 8
    font_report = run(["pdffonts", str(path)])
    fonts = font_report.splitlines()[2:]
    assert fonts
    assert "DroidSansFallback" in font_report.replace(" ", ""), "embedded CJK font missing"
    for line in fonts:
        columns = line.split()
        assert len(columns) >= 7 and columns[-5] == "yes" and columns[-4] == "yes", line
    with tempfile.TemporaryDirectory(prefix="c378-pdf-audit-") as directory:
        work = Path(directory)
        text_path = work / "text.txt"
        run(["pdftotext", str(path), str(text_path)])
        raw = text_path.read_bytes()
        assert all(byte >= 32 or byte in (10, 12, 13) for byte in raw), "PDF text control byte"
        text = raw.decode("utf-8")
        flat = " ".join(text.split())
        assert "Beta-Two Dyson–Ornstein–Uhlenbeck Diffusion" in text
        assert_round_title(flat, round_index)
        assert "中文摘要" in text and "关键词" in text and "Keywords:" in text
        assert not UNESCAPED_TEX_SPACING_PATTERN.search(text), "literal quad/qquad leaked into PDF text"
        assert "??" not in text and "TODO" not in text and "[VERIFY]" not in text
        tokens = (
            "round zero matrix radialization and reversible GUE density",
            "round one determinant Doob kernel and no collision",
            "round two complete partition spectrum and Route A closure",
        )
        assert tokens[round_index] in flat
        keyword_tokens = (
            ("Hermitian matrix diffusion", "eigenvalue process", "Ornstein–Uhlenbeck dynamics", "ordered chamber", "GUE equilibrium"),
            ("Dyson diffusion", "Karlin–McGregor kernel", "Doob transform", "Vandermonde function", "noncollision", "reversible diffusion"),
            ("Dyson diffusion", "Hermite polynomials", "partition spectrum", "spectral gap", "heat trace", "Fredholm determinant", "Route A"),
        )
        assert all(token in flat for token in keyword_tokens[round_index])
        if round_index == 0:
            for future in ("Vandermonde mass", "never reaches a collision wall", "partition spectrum", "Fredholm determinant", "Route A closure"):
                assert future not in flat, f"round-zero leak: {future}"
        if round_index == 1:
            for future in ("complete partition spectrum", "partition-product heat trace", "Fredholm determinant", "Route A closure"):
                assert future not in flat, f"round-one leak: {future}"
        if round_index >= 1:
            assert "Vandermonde mass" in flat and "never reaches a collision wall" in flat
        if round_index == 2:
            assert "16,602 partitions" in flat
            assert "NO_BAD_EULER_OR_ROOT_NUMBER" in flat
            assert "not promoted to a target" in flat
        prefix = work / "page"
        run(["pdftoppm", "-png", "-r", "72", str(path), str(prefix)])
        images = sorted(work.glob("page-*.png"))
        assert len(images) == pages
        raster_sizes = [image.stat().st_size for image in images]
        assert all(size > 1000 for size in raster_sizes)
    return pages, len(fonts), raster_sizes


def optimized_gate():
    for name in SCRIPTS:
        for flag in ("-O", "-OO"):
            process = subprocess.run(
                [sys.executable, flag, str(ROOT / "code" / name), "--help"],
                capture_output=True, text=True,
            )
            assert process.returncode and "refuses optimized Python" in process.stdout + process.stderr


def source_gate():
    texts = []
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix in (".md", ".py", ".tex", ".txt", ".yaml"):
            raw = path.read_bytes()
            assert all(byte >= 32 or byte in (10, 13) for byte in raw), f"control byte in {path}"
            text = path.read_text(errors="strict")
            if path.suffix == ".tex":
                assert_tex_spacing_hygiene(text, str(path.relative_to(ROOT)))
            texts.append(text)
    joined = "\n".join(texts)
    for index, name in enumerate(WRAPPER_NAMES):
        expected = f"\\def\\CRevisionRound{{{index}}}\n\\input{{main.tex}}\n".encode()
        assert (ROOT / "paper" / name).read_bytes() == expected, f"wrapper contract mismatch: {name}"
    assert not UNESCAPED_TEX_SPACING_PATTERN.search(r"x,\quad y; z,\qquad w")
    assert UNESCAPED_TEX_SPACING_PATTERN.search("x,quad y")
    assert UNESCAPED_TEX_SPACING_PATTERN.search("x,qquad y")
    for stale in ("HCS-" + "C373", "HEN-" + "O357", "c373" + "_", "Hemispherical " + "Higgs"):
        assert stale not in joined, f"stale template token {stale}"
    evidence = strict_json(EVIDENCE)
    assert evidence["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert all(value is False for value in evidence["scope_flags"].values())
    assert evidence["route_a"]["route_b_invocation_allowed"] is False
    assert evidence["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
    assert "no Hilbert-Polya operator and no Route B" in evidence["nonclaims"]
    required = (
        "A Brownian-Motion Model for the Eigenvalues of a Random Matrix",
        "Coincidence probabilities", "Diffusing particles with electrostatic repulsion",
        "Brownian motion in a Weyl chamber", "The Calogero--Sutherland Model",
        "candidate_registry.md:860", "candidate_registry.md:836",
        "candidate_registry.md:770", "candidate_registry.md:374",
    )
    assert all(token in joined for token in required)
    assert "Droid Sans Fallback" in joined and "中文摘要" in joined and "关键词" in joined


def lane_gate():
    outputs = []
    python = sys.executable
    with tempfile.TemporaryDirectory(prefix="c378-release-evidence-") as directory:
        output = Path(directory) / "evidence.json"
        outputs.append(run([python, str(ROOT / "code/c378_dyson_ou_producer.py"), "--output", str(output)]))
        assert output.read_bytes() == EVIDENCE.read_bytes()
    outputs.append(run([python, str(ROOT / "code/c378_dyson_ou_checker.py")]))
    outputs.append(run([python, str(ROOT / "code/c378_dyson_ou_sympy_crosscheck.py")]))
    outputs.append(run([python, str(ROOT / "code/c378_dyson_ou_replay.py")]))
    outputs.append(run([python, str(ROOT / "code/c378_dyson_ou_mutation.py")]))
    run([python, "-B", "-m", "unittest", "tests/test_c378_smoke.py"], cwd=ROOT)
    outputs.append("C378 unittest smoke PASS: tests=3")
    return outputs


def make_manifest(rounds):
    files = {relative: sha256(ROOT / relative) for relative in EXPECTED}
    assert sha256(EVALUATION) == YAML_RAW_SHA
    evidence = strict_json(EVIDENCE)
    assert evidence["route_a_yaml"] == {
        "relative_path": "evaluations/route_a/HCS-C378/2026-09-04.yaml",
        "raw_sha256": YAML_RAW_SHA, "semantic_sha256": YAML_SEMANTIC_SHA,
    }
    assert evidence["evaluator"] == {
        "authority": AUTHORITY, "version": AUTHORITY_VERSION, "sha256": AUTHORITY_SHA,
    }
    return {
        "schema": "hcs-release-manifest-v1", "candidate_id": "HCS-C378",
        "obstruction_id": "HEN-O362", "source_commit": "f58422d8f03235329863f946654981ecb5d4dc97",
        "fixed_epoch": 1788480000, "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator_authority": AUTHORITY, "evaluator_version": AUTHORITY_VERSION,
        "evaluator_authority_sha256": AUTHORITY_SHA, "payload_file_count": 38,
        "physical_file_count": 39, "evaluation_raw_sha256": YAML_RAW_SHA,
        "evaluation_semantic_sha256": YAML_SEMANTIC_SHA,
        "evidence_sha256": sha256(EVIDENCE), "evidence_payload_sha256": evidence_payload_hash(),
        "main_pdf_sha256": sha256(MAIN_PDF),
        "release_lanes": {
            "producer": "PASS", "independent_checker": "PASS", "sympy_crosscheck": "PASS",
            "isolated_byte_replay": "PASS", "hostile_mutation": "PASS",
            "unittest_smoke": "PASS", "optimized_mode_refusal": "PASS",
            "deterministic_pdf_rebuild": "PASS", "payload_membership": "PASS",
            "forbidden_claim_firewall": "PASS", "text_control_byte_hygiene": "PASS",
        },
        "pdf_rounds": rounds, "files": {key: files[key] for key in sorted(files)},
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--build-pdfs", action="store_true")
    args = parser.parse_args()
    if args.build_pdfs:
        blobs = [compile_round(round_index) for round_index in range(3)]
        for blob, name in zip(blobs, PDF_NAMES):
            (ROOT / "paper" / name).write_bytes(blob)
        MAIN_PDF.write_bytes(blobs[2])
        print("C378 PDF build PASS: three double-fresh rounds; main=round2")
        return

    current = actual_files()
    allowed = sorted(EXPECTED + (MANIFEST.name,))
    permitted = sorted(EXPECTED) if args.write and not MANIFEST.exists() else allowed
    assert current == permitted, (
        f"file ledger mismatch extra={sorted(set(current) - set(permitted))} "
        f"missing={sorted(set(permitted) - set(current))}"
    )
    source_gate()
    outputs = lane_gate()
    optimized_gate()
    rounds = []
    blobs = []
    for round_index, name in enumerate(PDF_NAMES):
        blob = compile_round(round_index)
        path = ROOT / "paper" / name
        assert blob == path.read_bytes(), f"stale {name}"
        pages, font_rows, raster_sizes = pdf_gate(path, round_index)
        blobs.append(blob)
        rounds.append({
            "round": round_index, "path": f"paper/{name}", "sha256": sha256(path),
            "bytes": path.stat().st_size, "pages": pages, "font_rows": font_rows,
            "raster_bytes": raster_sizes,
        })
    assert len(set(blobs)) == 3 and MAIN_PDF.read_bytes() == blobs[2]
    assert rounds[0]["pages"] < rounds[1]["pages"] < rounds[2]["pages"], "PDF page counts must increase by round"
    pdf_gate(MAIN_PDF, 2)
    compile_report = (ROOT / "paper/COMPILE_REPORT.md").read_text()
    for row in rounds:
        assert row["sha256"] in compile_report
    assert sha256(EVIDENCE) in (ROOT / "results/RESULTS.md").read_text()
    manifest = make_manifest(rounds)
    blob = json.dumps(manifest, sort_keys=True, indent=2).encode() + b"\n"
    if args.write:
        MANIFEST.write_bytes(blob)
    else:
        assert MANIFEST.read_bytes() == blob, "manifest stale"
    print("C378 release PASS: payload=38 physical=39 " + " | ".join(outputs))
    print(
        f"manifest_sha256={hashlib.sha256(blob).hexdigest()} "
        f"pdf_sha256={sha256(MAIN_PDF)} evidence_sha256={sha256(EVIDENCE)}"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"C378 release FAIL: {type(exc).__name__}: {exc}", file=sys.stderr)
        sys.exit(1)
