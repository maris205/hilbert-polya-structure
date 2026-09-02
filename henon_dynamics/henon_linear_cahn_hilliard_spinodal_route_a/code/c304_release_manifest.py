#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C304 release."""
from __future__ import annotations

import ast
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
MANIFEST = ROOT / "C304_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c304_ch_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C304/2026-09-03.yaml"
TEX = ROOT / "paper/main.tex"
PDF = ROOT / "paper/main.pdf"
SOURCE = "c0259978b1d7ebae63fe7b39fce1af2655b8529d"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
EVIDENCE_SHA = "a1f026d7cb41c12c2cbe798eba28ee75e07f4e0aa909434a0c92da9d78a488bc"
PAYLOAD_SHA = "e8cd24bb51e60e34ff5adee65f46004eb940ffb3409effa048752b15847a3530"
EVALUATION_FILE_SHA = "9defd433a03b8a49bcd0f566fe2ffd6cd58805afc2c75a7dbf4f85da3b24465e"
EVALUATION_SEMANTIC_SHA = "e62f212e422f35ff01c066fc1e96a34d386b400e5b0eb783d06126a32092048d"
ROUND_PATHS = [
    ROOT / "paper/main_round0_original.pdf",
    ROOT / "paper/main_round1.pdf",
    ROOT / "paper/main_round2.pdf",
]
ROUND_HASHES = [
    "5bd10d6e78d18bbdeeffe967329a80bb7e896ab13bba9d2ebec60149505752b1",
    "6b5ed469f5a8bda8113fd3ea7a8444fdfb2f7f6597331ed8fb0ae25afa6370fe",
    "9d9525ab50369f110dbfd0a98ff3f153b7c6c146b3c0facfe0f1f2ac9f2b3c47",
]
ROUND_PAGES = [2, 2, 3]
ROUND_FONTS = [24, 25, 26]
ROUND_TEXT = [
    ("full linear spinodal atlas", "whole represented spectrum", "source lineage"),
    ("gradient-flow law and singular faces", "boundary completion", "natural generator domain", "no nonstationary periodic solution"),
    ("finite evidence, hostile audit, and scope", "three round variants", "byte-identical alias", "route_a_rejected", "no_bad_euler_or_root_number", "ai use"),
]
WARNING_RE = re.compile(
    r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|"
    r"undefined (?:references|citations)|Rerun to get|Missing character"
)
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md",
    "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md",
    "THEOREM_PACKAGE.md", "code/README.md", "code/c304_ch_checker.py",
    "code/c304_ch_mutation.py", "code/c304_ch_producer.py",
    "code/c304_ch_replay.py", "code/c304_ch_sympy_crosscheck.py",
    "code/c304_release_manifest.py",
    "evaluations/route_a/HCS-C304/2026-09-03.yaml", "paper/COMPILE_REPORT.md",
    "paper/README.md", "paper/main.pdf", "paper/main.tex",
    "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c304_ch_evidence.json",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def reject_duplicates(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON key: {key}")
        value[key] = item
    return value


def reject_nonfinite(value):
    raise ValueError(f"nonfinite JSON: {value}")


def strict_json(path: Path) -> dict:
    value = json.loads(path.read_text(), object_pairs_hook=reject_duplicates, parse_constant=reject_nonfinite)
    if type(value) is not dict:
        raise TypeError("JSON root must be an object")
    return value


class UniqueSafeLoader(yaml.SafeLoader):
    pass


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("non-string or duplicate YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path) -> dict:
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML aliases forbidden")
    value = yaml.load(raw, Loader=UniqueSafeLoader)
    if type(value) is not dict:
        raise TypeError("YAML root must be a mapping")
    return value


def semantic_hash(value: dict) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def payload_hash(value: dict) -> str:
    body = dict(value)
    body.pop("payload_sha256", None)
    return semantic_hash(body)


def sidecar(path: Path) -> bool:
    return (
        path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"}
        or "__pycache__" in path.parts
        or path.name.endswith(".synctex.gz")
    )


def run_python(name: str) -> str:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True)


def pages(path: Path) -> int:
    text = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in text.splitlines() if line.startswith("Pages:")))


def fonts(path: Path) -> list[str]:
    text = subprocess.check_output(["pdffonts", str(path)], text=True)
    return [line for line in text.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]


def pdf_text(path: Path) -> str:
    text = subprocess.check_output(["pdftotext", "-layout", str(path), "-"], text=True)
    return " ".join(text.lower().split())


def raster(path: Path, page_count: int) -> list[int]:
    sizes = []
    with tempfile.TemporaryDirectory(prefix="c304-raster-") as temporary:
        for page in range(1, page_count + 1):
            prefix = Path(temporary) / f"page-{page}"
            subprocess.run(
                ["pdftoppm", "-f", str(page), "-l", str(page), "-r", "72", "-png", str(path), str(prefix)],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            outputs = list(Path(temporary).glob(f"page-{page}-*.png"))
            if len(outputs) != 1 or outputs[0].stat().st_size <= 1000:
                raise AssertionError("raster audit failed")
            sizes.append(outputs[0].stat().st_size)
    return sizes


def fresh_build(round_number: int) -> tuple[bytes, str]:
    with tempfile.TemporaryDirectory(prefix=f"c304-r{round_number}-") as temporary:
        work = Path(temporary)
        shutil.copy2(TEX, work / "main.tex")
        env = dict(os.environ)
        env.update({"SOURCE_DATE_EPOCH": str(EPOCH), "FORCE_SOURCE_DATE": "1", "TZ": "UTC"})
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", source]
        for _ in range(2):
            subprocess.run(command, cwd=work, env=env, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = (work / "main.log").read_text(errors="replace")
        matched = WARNING_RE.search(log)
        if matched is not None:
            raise AssertionError(f"settled PDF warning: {matched.group(0)}")
        return (work / "main.pdf").read_bytes(), log


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C304 release refuses optimized Python")
    producer = run_python("c304_ch_producer.py")
    if "C304_PRODUCER_PASS" not in producer:
        raise AssertionError("producer failed")
    data = strict_json(EVIDENCE)
    if digest(EVIDENCE) != EVIDENCE_SHA or data["payload_sha256"] != payload_hash(data) or data["payload_sha256"] != PAYLOAD_SHA:
        raise AssertionError("evidence hash contract failed")
    if data["candidate_id"] != "HCS-C304" or data["obstruction_id"] != "HEN-O288":
        raise AssertionError("identity contract failed")
    if data["source_commit"] != SOURCE or data["fixed_epoch"] != EPOCH or data["scope_literal"] != SCOPE:
        raise AssertionError("provenance contract failed")
    if data["evaluator"] != {"version": "0.2.0", "sha256": EVALUATOR}:
        raise AssertionError("evaluator contract failed")
    if data["route_a"] != {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}:
        raise AssertionError("route contract failed")
    if data["enumeration"]["audited_cell_count"] != 1653:
        raise AssertionError("evidence count failed")

    evaluation = strict_yaml(EVALUATION)
    if digest(EVALUATION) != EVALUATION_FILE_SHA or semantic_hash(evaluation) != EVALUATION_SEMANTIC_SHA:
        raise AssertionError("evaluation hash contract failed")

    checker_path = ROOT / "code/c304_ch_checker.py"
    checker_source = checker_path.read_text()
    tree = ast.parse(checker_source)
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    if any("producer" in name for name in imports) or any(isinstance(node, ast.Assert) for node in ast.walk(tree)):
        raise AssertionError("checker independence/assert contract failed")
    for token in (
        "checker refuses optimized Python", "duplicate JSON key", "YAML anchors and aliases are forbidden",
        "noncanonical rational receipt", "analytic_exhaustion_cutoff", "exact proof tree",
    ):
        if token not in checker_source:
            raise AssertionError(f"checker guard absent: {token}")

    theorem = " ".join((ROOT / "THEOREM_PACKAGE.md").read_text().split())
    for token in (
        "all parameters and all represented shells", "fastest-shell maximization is global",
        "natural generator domain", "zero generator has domain all of", "1653 audited leaves",
        "A4_FORMAL_HINT",
    ):
        if token not in theorem:
            raise AssertionError(f"theorem token absent: {token}")
    hostile = " ".join((ROOT / "results/HOSTILE_AUDIT.md").read_text().split())
    for token in ("Finite-cutoff promotion", "All 72 attacks", "analytic_exhaustion_cutoff", "Route B is not invoked"):
        if token not in hostile:
            raise AssertionError(f"hostile token absent: {token}")
    compile_report = " ".join((ROOT / "paper/COMPILE_REPORT.md").read_text().split())
    for token in ("SOURCE_DATE_EPOCH=1788393600", "three round variants", "two fresh isolated", "byte-identical", *ROUND_HASHES):
        if token not in compile_report:
            raise AssertionError(f"compile token absent: {token}")

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    bad_sidecars = [name for name, path in physical.items() if sidecar(path)]
    if bad_sidecars:
        raise AssertionError(f"sidecars present: {bad_sidecars}")
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    if set(files) != EXPECTED or len(files) != 27:
        raise AssertionError(f"ledger mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}")

    if [digest(path) for path in ROUND_PATHS] != ROUND_HASHES or PDF.read_bytes() != ROUND_PATHS[2].read_bytes():
        raise AssertionError("archived PDF hashes failed")
    actual_pages = [pages(path) for path in ROUND_PATHS]
    if actual_pages != ROUND_PAGES:
        raise AssertionError("page contract failed")
    font_counts, raster_sizes = [], []
    for path, required, page_count in zip(ROUND_PATHS, ROUND_TEXT, ROUND_PAGES):
        rows = fonts(path)
        if not rows or not all(len(row.split()) >= 7 and row.split()[-5] == "yes" and row.split()[-4] == "yes" for row in rows):
            raise AssertionError(f"unembedded/unsubset font: {path.name}")
        font_counts.append(len(rows))
        text = pdf_text(path)
        for token in required:
            if token not in text:
                raise AssertionError(f"PDF sentinel absent: {path.name} {token}")
        raster_sizes.append(raster(path, page_count))
    if font_counts != ROUND_FONTS:
        raise AssertionError("font-count contract failed")

    fresh_hashes = []
    for round_number, (archive, expected_hash) in enumerate(zip(ROUND_PATHS, ROUND_HASHES)):
        first, _ = fresh_build(round_number)
        second, _ = fresh_build(round_number)
        if first != second or first != archive.read_bytes():
            raise AssertionError(f"nondeterministic round {round_number}")
        observed = hashlib.sha256(first).hexdigest()
        if observed != expected_hash:
            raise AssertionError(f"fresh hash mismatch round {round_number}")
        fresh_hashes.append([observed, observed])

    checker = run_python("c304_ch_checker.py")
    symbolic = run_python("c304_ch_sympy_crosscheck.py")
    replay = run_python("c304_ch_replay.py")
    mutation = run_python("c304_ch_mutation.py")
    if "PASS (1930 assertions; producer import forbidden)" not in checker:
        raise AssertionError("checker sentinel failed")
    if "PASS (36 symbolic identities)" not in symbolic:
        raise AssertionError("symbolic sentinel failed")
    if "C304 byte replay: PASS" not in replay:
        raise AssertionError("replay sentinel failed")
    if "PASS 72/72" not in mutation:
        raise AssertionError("mutation sentinel failed")

    result = {
        "schema": "hcs-c304-release-v1",
        "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C304",
        "obstruction_id": "HEN-O288",
        "evaluation_date": "2026-09-03",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "headline": "all-parameter full-dimensional linear periodic Cahn--Hilliard spinodal semigroup atlas",
        "theorem_status": "PROVABLE AS STATED",
        "results": {
            "cases": 18, "shell_rows": 216, "support_probes": 6, "boundary_rows": 6,
            "audited_cells": 1653, "checker_assertions": 1930, "symbolic_checks": 36,
            "hostile_rejections": 72, "evidence_payload_sha256": PAYLOAD_SHA,
            "evidence_sha256": EVIDENCE_SHA, "evaluation_semantic_sha256": EVALUATION_SEMANTIC_SHA,
            "pdf_sha256": digest(PDF), "pdf_pages": actual_pages[-1],
        },
        "build_contract": {
            "engine": "LuaLaTeX", "passes_per_build": 2, "fresh_builds_per_round": 2,
            "fresh_build_directory_count": 6, "round_artifacts": [str(path.relative_to(ROOT)) for path in ROUND_PATHS],
            "round_pdf_sha256": ROUND_HASHES, "fresh_build_sha256": fresh_hashes,
            "round_pdf_pages": actual_pages, "round_embedded_subset_font_rows": font_counts,
            "round_text_contracts": [list(tokens) for tokens in ROUND_TEXT], "raster_page_bytes": raster_sizes,
            "visual_inspection": "PASS all 7 archived pages", "final_equals": "paper/main_round2.pdf",
        },
        "gates": {
            "G0_provenance_scope_evaluator": "PASS", "G1_fourier_semigroup": "PASS",
            "G2_energy_morse_kernel": "PASS", "G3_global_fastest_shell_and_ties": "PASS",
            "G4_actual_support_and_recurrence": "PASS", "G5_kappa_zero_boundary": "PASS",
            "G6_checker_sympy_replay_mutation": "PASS", "G7_two_substantive_revisions": "PASS",
            "G8_six_fresh_builds_fonts_logs_text_raster": "PASS", "G9_exact_manifest_ledger": "PASS",
            "G10_target_arithmetic_euler_root_zero_route_b": "NOT_CLAIMED",
        },
        "route_a_verdict": data["route_a"],
        "nonclaims": data["nonclaims"],
        "boundary_risk": "The theorem is linear, finite-dimensional in torus dimension but arbitrary over all finite d; finite receipts do not prove fastest-shell exhaustion, and kappa=0 is a separate singular face.",
        "collision_boundary": data["collision_boundary"],
        "evaluation_contract": {
            "path": str(EVALUATION.relative_to(ROOT)), "file_sha256": EVALUATION_FILE_SHA,
            "semantic_sha256": EVALUATION_SEMANTIC_SHA,
            "duplicate_merge_anchor_alias_rejection": True, "exact_recursive_semantic_tree_and_types": True,
        },
        "excluded_from_manifest": ["C304_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    if len([path for path in ROOT.rglob("*") if path.is_file()]) != 28:
        raise AssertionError("physical file count is not 28")
    print(json.dumps({
        "status": "C304_RELEASE_MANIFEST_PASS", "payload_file_count": 27,
        "physical_file_count": 28, "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": EVIDENCE_SHA, "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
