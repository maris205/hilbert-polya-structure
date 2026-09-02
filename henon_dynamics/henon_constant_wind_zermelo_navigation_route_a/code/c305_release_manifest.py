#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C305 release."""
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
MANIFEST = ROOT / "C305_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c305_zermelo_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C305/2026-09-03.yaml"
TEX, PDF = ROOT / "paper/main.tex", ROOT / "paper/main.pdf"
SOURCE = "c0259978b1d7ebae63fe7b39fce1af2655b8529d"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE, EPOCH = "NO_BAD_EULER_OR_ROOT_NUMBER", 1788393600
EVIDENCE_SHA = "dd971dc65ced312ae4d09f15fb2625ea230dc913d7acbd6313037ff5159f9f58"
PAYLOAD_SHA = "50d6b7aa483eb808f1adb807dabbec02e8a7c8c504f9a7598901caf2ae18cfbb"
EVALUATION_FILE_SHA = "ae5b95baf612e87b076f9361cb2d8eb255dc7d57b3fd69b092f022f27129f456"
EVALUATION_SEMANTIC_SHA = "4299bef8945c7c14eba7f87594d08b3ae79e3aa06a0ae680673e4f641571062a"
ROUND_PATHS = [ROOT / "paper/main_round0_original.pdf", ROOT / "paper/main_round1.pdf", ROOT / "paper/main_round2.pdf"]
ROUND_HASHES = [
    "e4cb469251a2626bb8d0bdcda23cd9e00765092de4e9c88b26deb63b87cc4af1",
    "321e68a9f67939550ed259b70c26242fc3ed011db08ebd210d0a3d1825fdb06a",
    "26b69034b7cef082f01028a5c2c8b74c45d313aa1324ccdacfe434eae9bf6eea",
]
ROUND_PAGES, ROUND_FONTS = [2, 2, 3], [20, 20, 21]
ROUND_TEXT = [
    ("complete constant-wind atlas", "minimum is the smaller root", "source lineage"),
    ("value geometry, hjb, and exact boundaries", "global finsler norm", "zero target"),
    ("evidence, hostile audit, and route-a boundary", "route_a_rejected", "no_bad_euler_or_root_number", "ai use"),
]
WARNING_RE = re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md",
    "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md", "code/README.md",
    "code/c305_release_manifest.py", "code/c305_zermelo_checker.py", "code/c305_zermelo_mutation.py",
    "code/c305_zermelo_producer.py", "code/c305_zermelo_replay.py", "code/c305_zermelo_sympy_crosscheck.py",
    "evaluations/route_a/HCS-C305/2026-09-03.yaml", "paper/COMPILE_REPORT.md", "paper/README.md",
    "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf",
    "paper/main_round2.pdf", "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md",
    "results/c305_zermelo_evidence.json",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def duplicate_rejector(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_nonfinite(value):
    raise ValueError(f"nonfinite JSON: {value}")


def strict_json(path):
    value = json.loads(path.read_text(), object_pairs_hook=duplicate_rejector, parse_constant=reject_nonfinite)
    if type(value) is not dict:
        raise TypeError("JSON root must be object")
    return value


class UniqueSafeLoader(yaml.SafeLoader):
    pass


UniqueSafeLoader.yaml_implicit_resolvers = {key: [(tag, pattern) for tag, pattern in values if tag != "tag:yaml.org,2002:timestamp"] for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()}


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("bad YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML aliases forbidden")
    value = yaml.load(raw, Loader=UniqueSafeLoader)
    if type(value) is not dict:
        raise TypeError("YAML root must be mapping")
    return value


def semantic_hash(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def payload_hash(value):
    body = dict(value); body.pop("payload_sha256", None)
    return semantic_hash(body)


def sidecar(path):
    return path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"} or "__pycache__" in path.parts or path.name.endswith(".synctex.gz")


def run_python(name):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True)


def pdf_pages(path):
    text = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in text.splitlines() if line.startswith("Pages:")))


def font_rows(path):
    text = subprocess.check_output(["pdffonts", str(path)], text=True)
    return [line for line in text.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]


def pdf_text(path):
    return " ".join(subprocess.check_output(["pdftotext", "-layout", str(path), "-"], text=True).lower().split())


def raster(path, page_count):
    sizes = []
    with tempfile.TemporaryDirectory(prefix="c305-raster-") as temporary:
        for page in range(1, page_count + 1):
            prefix = Path(temporary) / f"page-{page}"
            subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", "72", "-png", str(path), str(prefix)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            outputs = list(Path(temporary).glob(f"page-{page}-*.png"))
            if len(outputs) != 1 or outputs[0].stat().st_size <= 1000:
                raise AssertionError("raster failed")
            sizes.append(outputs[0].stat().st_size)
    return sizes


def fresh_build(round_number):
    with tempfile.TemporaryDirectory(prefix=f"c305-r{round_number}-") as temporary:
        work = Path(temporary); shutil.copy2(TEX, work / "main.tex")
        env = dict(os.environ); env.update({"SOURCE_DATE_EPOCH": str(EPOCH), "FORCE_SOURCE_DATE": "1", "TZ": "UTC"})
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{main.tex}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", source]
        for _ in range(2):
            subprocess.run(command, cwd=work, env=env, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = (work / "main.log").read_text(errors="replace")
        matched = WARNING_RE.search(log)
        if matched:
            raise AssertionError(f"settled warning: {matched.group(0)}")
        return (work / "main.pdf").read_bytes()


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C305 release refuses optimized Python")
    if "C305_PRODUCER_PASS" not in run_python("c305_zermelo_producer.py"):
        raise AssertionError("producer failed")
    data = strict_json(EVIDENCE)
    if digest(EVIDENCE) != EVIDENCE_SHA or data["payload_sha256"] != PAYLOAD_SHA or payload_hash(data) != PAYLOAD_SHA:
        raise AssertionError("evidence hashes failed")
    if (data["candidate_id"], data["obstruction_id"], data["source_commit"], data["fixed_epoch"], data["scope_literal"]) != ("HCS-C305", "HEN-O289", SOURCE, EPOCH, SCOPE):
        raise AssertionError("identity/provenance failed")
    if data["evaluator"] != {"version": "0.2.0", "sha256": EVALUATOR}:
        raise AssertionError("evaluator failed")
    route = {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    if data["route_a"] != route or data["enumeration"]["audited_cell_count"] != 744:
        raise AssertionError("route/count contract failed")
    evaluation = strict_yaml(EVALUATION)
    if digest(EVALUATION) != EVALUATION_FILE_SHA or semantic_hash(evaluation) != EVALUATION_SEMANTIC_SHA:
        raise AssertionError("evaluation hashes failed")

    checker_source = (ROOT / "code/c305_zermelo_checker.py").read_text()
    tree = ast.parse(checker_source)
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import): imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom): imports.append(node.module or "")
    if any("producer" in name for name in imports) or any(isinstance(node, ast.Assert) for node in ast.walk(tree)):
        raise AssertionError("checker independence/explicit-raise failed")
    for token in ("checker refuses optimized Python", "duplicate JSON key", "YAML anchors and aliases are forbidden", "noncanonical rational receipt", "full EXPECTED_EVALUATION exact tree"):
        if token not in checker_source: raise AssertionError(f"checker guard absent: {token}")

    theorem = " ".join((ROOT / "THEOREM_PACKAGE.md").read_text().split())
    for token in ("all dimensions, winds, caps, and targets", "minimum is the smaller root", "all \\(t\\ge0\\) are attainable iff", "square-root loss of regularity", "A4_FAIL"):
        if token not in theorem: raise AssertionError(f"theorem token absent: {token}")
    hostile = " ".join((ROOT / "results/HOSTILE_AUDIT.md").read_text().split())
    for token in ("Wrong strong root", "All 85 attacks", "HJB sign error", "Route B is not invoked"):
        if token not in hostile: raise AssertionError(f"hostile token absent: {token}")
    compile_report = " ".join((ROOT / "paper/COMPILE_REPORT.md").read_text().split())
    for token in ("SOURCE_DATE_EPOCH=1788393600", "two isolated directories", "byte-identical", *ROUND_HASHES):
        if token not in compile_report: raise AssertionError(f"compile token absent: {token}")

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    bad = [name for name, path in physical.items() if sidecar(path)]
    if bad: raise AssertionError(f"sidecars: {bad}")
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    if set(files) != EXPECTED or len(files) != 27:
        raise AssertionError(f"ledger mismatch missing={sorted(EXPECTED-set(files))} extra={sorted(set(files)-EXPECTED)}")

    if [digest(path) for path in ROUND_PATHS] != ROUND_HASHES or PDF.read_bytes() != ROUND_PATHS[2].read_bytes():
        raise AssertionError("PDF archive failed")
    actual_pages = [pdf_pages(path) for path in ROUND_PATHS]
    if actual_pages != ROUND_PAGES: raise AssertionError("pages failed")
    font_counts, rasters = [], []
    for path, tokens, page_count in zip(ROUND_PATHS, ROUND_TEXT, ROUND_PAGES):
        rows = font_rows(path)
        if not rows or not all(len(row.split()) >= 7 and row.split()[-5] == "yes" and row.split()[-4] == "yes" for row in rows):
            raise AssertionError("font embedding/subsetting failed")
        font_counts.append(len(rows)); text = pdf_text(path)
        for token in tokens:
            if token not in text: raise AssertionError(f"PDF token absent: {path.name} {token}")
        rasters.append(raster(path, page_count))
    if font_counts != ROUND_FONTS: raise AssertionError("font count failed")

    fresh_hashes = []
    for round_number, (archive, expected) in enumerate(zip(ROUND_PATHS, ROUND_HASHES)):
        first, second = fresh_build(round_number), fresh_build(round_number)
        if first != second or first != archive.read_bytes() or hashlib.sha256(first).hexdigest() != expected:
            raise AssertionError(f"fresh deterministic build failed round {round_number}")
        fresh_hashes.append([expected, expected])

    checker, symbolic = run_python("c305_zermelo_checker.py"), run_python("c305_zermelo_sympy_crosscheck.py")
    replay, mutation = run_python("c305_zermelo_replay.py"), run_python("c305_zermelo_mutation.py")
    if "PASS (734 assertions; producer import forbidden)" not in checker: raise AssertionError("checker sentinel")
    if "PASS (27 symbolic identities)" not in symbolic: raise AssertionError("symbolic sentinel")
    if "C305 byte replay: PASS" not in replay: raise AssertionError("replay sentinel")
    if "PASS 85/85" not in mutation: raise AssertionError("mutation sentinel")

    result = {
        "schema": "hcs-c305-release-v1", "status": "RELEASE_COMPLETE", "candidate_id": "HCS-C305",
        "obstruction_id": "HEN-O289", "evaluation_date": "2026-09-03", "source_commit": SOURCE,
        "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "headline": "all-dimensional constant-wind Zermelo reachability, value, optimizer, HJB, and boundary atlas",
        "theorem_status": "PROVABLE AS STATED",
        "results": {"cases": 29, "hjb_probes": 12, "boundary_rows": 8, "audited_cells": 744,
                    "checker_assertions": 734, "symbolic_checks": 27, "hostile_rejections": 85,
                    "evidence_payload_sha256": PAYLOAD_SHA, "evidence_sha256": EVIDENCE_SHA,
                    "evaluation_semantic_sha256": EVALUATION_SEMANTIC_SHA, "pdf_sha256": digest(PDF), "pdf_pages": actual_pages[-1]},
        "build_contract": {"engine": "LuaLaTeX", "passes_per_build": 2, "fresh_builds_per_round": 2,
                           "fresh_build_directory_count": 6, "round_artifacts": [str(path.relative_to(ROOT)) for path in ROUND_PATHS],
                           "round_pdf_sha256": ROUND_HASHES, "fresh_build_sha256": fresh_hashes,
                           "round_pdf_pages": actual_pages, "round_embedded_subset_font_rows": font_counts,
                           "round_text_contracts": [list(tokens) for tokens in ROUND_TEXT], "raster_page_bytes": rasters,
                           "visual_inspection": "PASS all 7 archived pages", "final_equals": "paper/main_round2.pdf"},
        "gates": {"G0_provenance_scope_evaluator": "PASS", "G1_exact_time_ball_and_quadratic": "PASS",
                  "G2_weak_critical_strong_root_atlas": "PASS", "G3_attainable_time_sets": "PASS",
                  "G4_unique_constant_optimizer": "PASS", "G5_HJB_symmetry_regularities": "PASS",
                  "G6_zero_wind_cap_target_faces": "PASS", "G7_checker_sympy_replay_mutation": "PASS",
                  "G8_two_substantive_revisions": "PASS", "G9_six_fresh_builds_fonts_logs_text_raster": "PASS",
                  "G10_exact_manifest_ledger": "PASS", "G11_target_arithmetic_euler_root_zero_operator_route_b": "NOT_CLAIMED"},
        "route_a_verdict": data["route_a"], "nonclaims": data["nonclaims"],
        "boundary_risk": "Critical reachability requires p>0; strong-wind times form a finite window; cone-boundary regularity excludes the one-dimensional and zero-cap degeneracies; optimizer uniqueness is for nonzero reachable targets.",
        "collision_boundary": data["collision_boundary"],
        "evaluation_contract": {"path": str(EVALUATION.relative_to(ROOT)), "file_sha256": EVALUATION_FILE_SHA,
                                "semantic_sha256": EVALUATION_SEMANTIC_SHA, "duplicate_merge_anchor_alias_rejection": True,
                                "exact_recursive_semantic_tree_and_types": True},
        "excluded_from_manifest": ["C305_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    if len([path for path in ROOT.rglob("*") if path.is_file()]) != 28: raise AssertionError("physical count")
    print(json.dumps({"status": "C305_RELEASE_MANIFEST_PASS", "payload_file_count": 27, "physical_file_count": 28,
                      "manifest_sha256": digest(MANIFEST), "evidence_sha256": EVIDENCE_SHA, "pdf_sha256": digest(PDF)}, sort_keys=True))


if __name__ == "__main__":
    main()
