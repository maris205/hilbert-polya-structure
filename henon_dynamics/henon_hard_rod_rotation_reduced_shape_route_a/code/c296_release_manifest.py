#!/usr/bin/env python3
"""Close the exact 27-payload / 28-physical-file HCS-C296 release."""
from __future__ import annotations

import ast
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "C296_RELEASE_MANIFEST.json"
EVIDENCE = ROOT / "results/c296_hard_rod_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C296/2026-09-02.yaml"
PAPER = ROOT / "paper"
TEX = PAPER / "main.tex"
PDF = PAPER / "main.pdf"
SOURCE = "f8d3ad9a8940b54e82854b2924be353575ed8fcb"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200
EVIDENCE_SHA = "7d12ae96f3e146b25586caa99d4f594be6243ecea2684683dbe8aee5368dc06b"
EVALUATION_SHA = "5e0c4609143ece03f46cab5822ba104af41b2513698dba999f8d4bf86b6e8ed1"
TUPLE = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
FLAGS = {
    "arithmetic_local_data": False, "euler_factors": False, "root_numbers": False,
    "automorphy": False, "target_divisor_or_counting_law": False,
    "target_functional_equation": False, "target_zero_match": False,
    "hilbert_polya_operator": False, "route_b_input": False,
}
EVALUATION_EXPECTED = {
    "schema": "route-a-evaluation-v0.2.0", "candidate_id": "HCS-C296",
    "obstruction_id": "HEN-O280",
    "evaluation_date": "2026-09-02", "source_commit": SOURCE,
    "fixed_epoch": EPOCH, "scope_literal": SCOPE,
    "evaluator_authority_sha256": EVALUATOR,
    "theorem_status": "PROVABLE AS CORRECTED", "tuple": TUPLE,
    "overall_verdict": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
    "axes": {
        "A0": "no arithmetic local-data carrier",
        "A1": "exact reduced periodic-return classification but no prime-like orbit bridge",
        "A2": "no arithmetic clock or target dynamical determinant",
        "A3": "no target analytic structure",
        "A4": "natural hard-core kinetic quantization on the reduced collision chamber",
    },
    "scope_flags": FLAGS,
}
ROUND_PATHS = [PAPER / "main_round0_original.pdf", PAPER / "main_round1.pdf", PAPER / "main_round2.pdf"]
ROUND_HASHES = [
    "8ea2fd6618e41272a03c396a295957f1e02acbbc2a1e7cb3e56fbed96555d15b",
    "9cac72b380bdbc9794037a113f1dd1b05629b9e6c9b00e1e8ac16308de56270f",
    "dc8890acabb563e3de21572381e479c8ac7ea2a23e6e4077aab4f8bffa6589f9",
]
ROUND_TEXT = [
    ("corrected phase space", "exact shape conjugacy", "cyclic-start identity"),
    ("all events, conservation, and no zeno", "why the unreduced statement is false", "full physical rod returns after"),
    ("complete return criterion", "stabilizer and minimal-period theorem", "96/96", "hen-o280", "route_a_rejected", SCOPE.lower()),
]
EXPECTED = {
    "EXPERIMENT_PLAN.md", "NARRATIVE_REPORT.md", "PAPER_IMPROVEMENT_LOG.md", "PAPER_PLAN.md", "README.md", "RESEARCH_QUESTION.md", "SOURCE_AUDIT.md", "THEOREM_PACKAGE.md",
    "code/README.md", "code/c296_hard_rod_checker.py", "code/c296_hard_rod_mutation.py", "code/c296_hard_rod_producer.py", "code/c296_hard_rod_replay.py", "code/c296_hard_rod_sympy_crosscheck.py", "code/c296_release_manifest.py",
    "evaluations/route_a/HCS-C296/2026-09-02.yaml", "paper/COMPILE_REPORT.md", "paper/README.md", "paper/main.pdf", "paper/main.tex", "paper/main_round0_original.pdf", "paper/main_round1.pdf", "paper/main_round2.pdf",
    "results/HOSTILE_AUDIT.md", "results/RESULTS.md", "results/TEST_REPORT.md", "results/c296_hard_rod_evidence.json",
}
WARNING_RE = re.compile(r"(?:LaTeX|Package [^:\n]+) Warning:|Overfull|Underfull|undefined (?:references|citations)|Rerun to get|Missing character")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


class UniqueSafeLoader(yaml.SafeLoader):
    """Safe YAML loader with duplicate rejection and dates kept as strings."""


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def construct_unique_mapping(loader: UniqueSafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
    loader.flatten_mapping(node)
    out = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in out
        except TypeError as error:
            raise yaml.constructor.ConstructorError(None, None, "unhashable YAML key", key_node.start_mark) from error
        if duplicate:
            raise yaml.constructor.ConstructorError(None, None, f"duplicate YAML key: {key}", key_node.start_mark)
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique_mapping)


def strict_yaml_load(path: Path) -> dict:
    value = yaml.load(path.read_text(), Loader=UniqueSafeLoader)
    if type(value) is not dict:
        raise TypeError("evaluation YAML top level must be object")
    return value


def exact_tree(value, expected, label: str) -> None:
    assert type(value) is type(expected), f"{label} exact type"
    if type(expected) is dict:
        assert set(value) == set(expected), f"{label} exact keys"
        for key in expected:
            exact_tree(value[key], expected[key], f"{label}.{key}")
    elif type(expected) is list:
        assert len(value) == len(expected), f"{label} length"
        for index, item in enumerate(expected):
            exact_tree(value[index], item, f"{label}[{index}]")
    else:
        assert value == expected, f"{label} value"


def semantic_hash(value: dict) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def sidecar(path: Path) -> bool:
    return path.suffix in {".aux", ".log", ".out", ".toc", ".fls", ".fdb_latexmk", ".pyc"} or "__pycache__" in path.parts or path.name.endswith(".synctex.gz")


def run_python(name: str) -> str:
    env = dict(os.environ)
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "TZ": "UTC"})
    return subprocess.check_output([sys.executable, "-B", str(ROOT / "code" / name)], env=env, text=True)


def pdf_pages(path: Path) -> int:
    text = subprocess.check_output(["pdfinfo", str(path)], text=True)
    return int(next(line.split(":", 1)[1] for line in text.splitlines() if line.startswith("Pages:")))


def font_rows(path: Path) -> list[str]:
    text = subprocess.check_output(["pdffonts", str(path)], text=True)
    return [line for line in text.splitlines()[2:] if line.strip() and not line.lstrip().startswith("-")]


def pdf_text(path: Path) -> str:
    text = subprocess.check_output(["pdftotext", "-layout", str(path), "-"], text=True)
    return " ".join(text.lower().split())


def fresh_build(round_number: int) -> bytes:
    with tempfile.TemporaryDirectory(prefix=f"c296-r{round_number}-") as temporary:
        work = Path(temporary)
        env = dict(os.environ)
        env.update({"SOURCE_DATE_EPOCH": str(EPOCH), "FORCE_SOURCE_DATE": "1", "TZ": "UTC"})
        source = rf"\def\CRevisionRound{{{round_number}}}\input{{{TEX}}}"
        command = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", "-jobname=main", source]
        for _ in range(2):
            subprocess.run(command, cwd=work, env=env, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        log = (work / "main.log").read_text(errors="replace")
        match = WARNING_RE.search(log)
        assert match is None, match.group(0) if match else ""
        return (work / "main.pdf").read_bytes()


def main() -> None:
    producer = run_python("c296_hard_rod_producer.py")
    assert "C296_PRODUCER_PASS" in producer
    data = json.loads(EVIDENCE.read_text())
    assert digest(EVIDENCE) == EVIDENCE_SHA
    assert data["payload_sha256"] == payload_hash(data)
    assert data["schema"] == "hcs-c296-hard-rod-rotation-reduced-shape-v1"
    assert data["candidate_id"] == "HCS-C296" and data["obstruction_id"] == "HEN-O280"
    assert data["source_commit"] == SOURCE and data["evaluation_date"] == "2026-09-02"
    assert data["fixed_epoch"] == EPOCH and data["scope_literal"] == SCOPE
    assert data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR}
    assert data["model"]["shape_quotient"].startswith("global spatial rotations are removed")
    assert data["theorem_contract"]["return"].startswith("a reduced state returns")
    assert data["theorem_contract"]["topology_obstruction"].startswith("without rotation reduction")
    assert data["proof_contract"]["obstruction_proof"].startswith("for N=1")
    assert data["route_a"] == {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    assert data["scope_flags"] == FLAGS and all(value is False for value in FLAGS.values())
    assert data["enumeration"] == {
        "boundary_cells": 9, "conservation_cells": 7, "event_group_cells": 21,
        "event_time_cells": 16, "pair_crossing_cells": 23, "particle_cells": 20,
        "return_cells": 7, "scenario_count": 7, "shape_query_cells": 29,
        "symbolic_return_cells": 1, "velocity_class_cells": 16,
    }
    assert [row["identifier"] for row in data["references"]] == ["10.1063/1.1704288", "10.1103/PhysRev.50.955"]

    evaluation = strict_yaml_load(EVALUATION)
    exact_tree(evaluation, EVALUATION_EXPECTED, "evaluation")
    assert semantic_hash(evaluation) == EVALUATION_SHA
    yaml_text = EVALUATION.read_text()
    for token in (
        f"source_commit: {SOURCE}", f"fixed_epoch: {EPOCH}", f"scope_literal: {SCOPE}",
        f"evaluator_authority_sha256: {EVALUATOR}", "obstruction_id: HEN-O280",
        "tuple: [A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION]",
        "overall_verdict: ROUTE_A_REJECTED", "route_b_invocation_allowed: false",
    ):
        assert token in yaml_text, token

    theorem = " ".join((ROOT / "THEOREM_PACKAGE.md").read_text().split())
    for token in ("PROVABLE AS CORRECTED", "HEN-O280", "rotation-reduced", "y_i+T v_i", "lcm(d_u,d_w)", "N=1", "not claimed"):
        assert token in theorem, token
    source_audit = (ROOT / "SOURCE_AUDIT.md").read_text()
    for token in ("10.1063/1.1704288", "10.1103/PhysRev.50.955", "direct classical owners", "does not claim literature"):
        assert token in source_audit, token
    tex = TEX.read_text()
    assert "v_i=v_{\\sigma(i)},\\quad" in tex and "v_i=v_{\\sigma(i)}quad" not in tex
    for token in ("HEN-O280", "Exact shape conjugacy", "All-event law", "Why the unreduced statement is false", "Stabilizer and minimal-period theorem", "NO\\_BAD\\_EULER\\_OR\\_ROOT\\_NUMBER"):
        assert token in tex, token

    checker_source = (ROOT / "code/c296_hard_rod_checker.py").read_text()
    tree = ast.parse(checker_source)
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
    assert not [name for name in imports if "producer" in name]
    assert "object_pairs_hook=reject_duplicate_keys" in checker_source
    assert "roots_by_integer_scan" in checker_source and "translations_fixing" in checker_source
    mutation_source = (ROOT / "code/c296_hard_rod_mutation.py").read_text()
    for token in ("obstruction-id", "yaml-obstruction-id", "theorem-topology", "boundary-counterexample", "return-translation", "raw-duplicate-top", "yaml-route-b-true"):
        assert token in mutation_source, token

    compile_report = (PAPER / "COMPILE_REPORT.md").read_text()
    for token in (f"SOURCE_DATE_EPOCH={EPOCH}", "two isolated directories for each round", "byte-identical", "settled warning regex found no", "embedded and subset", *ROUND_HASHES):
        assert token in compile_report, token
    hostile = (ROOT / "results/HOSTILE_AUDIT.md").read_text()
    for token in ("All 96 attacks", "HEN-O280", "false restoration", "sqrt(2)", "duplicate top and nested", "Route-B", "affirmative target Euler/root-number attack"):
        assert token in hostile, token

    physical = {str(path.relative_to(ROOT)): path for path in ROOT.rglob("*") if path.is_file()}
    assert not [name for name, path in physical.items() if sidecar(path)]
    files = {name: digest(path) for name, path in sorted(physical.items()) if path != MANIFEST}
    assert set(files) == EXPECTED, (sorted(EXPECTED-set(files)), sorted(set(files)-EXPECTED))
    assert len(files) == 27
    assert [digest(path) for path in ROUND_PATHS] == ROUND_HASHES
    assert len(set(ROUND_HASHES)) == 3 and digest(PDF) == ROUND_HASHES[2]
    pages = [pdf_pages(path) for path in ROUND_PATHS]
    assert pages == [2, 3, 4]
    font_counts = []
    for path, required in zip(ROUND_PATHS, ROUND_TEXT):
        rows = font_rows(path)
        assert rows and all(len(row.split()) >= 7 and row.split()[-5] == "yes" and row.split()[-4] == "yes" for row in rows)
        font_counts.append(len(rows))
        text = pdf_text(path)
        for token in required:
            assert token in text, (path.name, token)
    assert font_counts == [19, 17, 18]

    fresh_hashes = []
    for round_number, (archive, expected) in enumerate(zip(ROUND_PATHS, ROUND_HASHES)):
        first = fresh_build(round_number)
        second = fresh_build(round_number)
        assert first == second == archive.read_bytes()
        pair = [hashlib.sha256(first).hexdigest(), hashlib.sha256(second).hexdigest()]
        assert pair == [expected, expected]
        fresh_hashes.append(pair)

    checker = run_python("c296_hard_rod_checker.py")
    symbolic = run_python("c296_hard_rod_sympy_crosscheck.py")
    replay = run_python("c296_hard_rod_replay.py")
    mutation = run_python("c296_hard_rod_mutation.py")
    assert "C296 independent quotient/event checker: PASS" in checker and "strict duplicate-rejecting JSON/YAML schemas" in checker
    assert f"evaluation-semantic-sha256={EVALUATION_SHA}" in checker
    assert "C296_SYMPY_PASS" in symbolic and "C296 byte replay: PASS" in replay and "C296_MUTATION_PASS 96/96" in mutation
    checker_n = int(re.search(r"PASS \((\d+) assertions", checker).group(1))
    symbolic_n = int(re.search(r"PASS \((\d+) symbolic", symbolic).group(1))
    mutation_n = int(re.search(r"PASS (\d+)/(\d+)", mutation).group(1))
    assert (checker_n, symbolic_n, mutation_n) == (2685, 159064, 96)
    assert digest(EVIDENCE) == EVIDENCE_SHA

    result = {
        "schema": "hcs-c296-release-v1", "status": "RELEASE_COMPLETE",
        "candidate_id": "HCS-C296", "obstruction_id": "HEN-O280",
        "evaluation_date": "2026-09-02", "source_commit": SOURCE,
        "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "headline": "rotation-reduced circular hard rods: exact free-flow conjugacy, all events, return CRT, and unreduced angle obstruction",
        "theorem_status": "PROVABLE AS CORRECTED",
        "build_contract": {
            "engine": "LuaLaTeX", "fixed_epoch": EPOCH, "passes_per_build": 2,
            "fresh_builds_per_round": 2, "settled_warning_regex": WARNING_RE.pattern,
            "round_artifacts": [str(path.relative_to(ROOT)) for path in ROUND_PATHS],
            "round_pdf_sha256": ROUND_HASHES, "fresh_build_sha256": fresh_hashes,
            "round_pdf_pages": pages, "round_embedded_subset_font_rows": font_counts,
            "all_round_text_contracts": [list(row) for row in ROUND_TEXT],
            "visual_inspection": "PASS all pages; return equation punctuation verified",
            "final_equals": "paper/main_round2.pdf",
        },
        "evaluation_contract": {
            "path": str(EVALUATION.relative_to(ROOT)), "obstruction_id": "HEN-O280", "semantic_sha256": EVALUATION_SHA,
            "duplicate_keys_rejected": True, "exact_schema_types_values": True,
            "orbit_cutoff": "NOT_APPLICABLE_ANALYTIC_ALL_PARAMETER_THEOREM",
        },
        "gates": {
            "G0_source_scope_evaluator": "PASS",
            "G0a_evaluation_yaml_duplicate_rejecting_exact_schema": "PASS",
            "G1_evidence_duplicate_rejecting_exact_schema": "PASS",
            "G2_rotation_reduced_gap_bijection": "PASS",
            "G3_free_flow_collision_glued_conjugacy": "PASS",
            "G4_all_events_conservation_no_zeno": "PASS",
            "G5_sigma_c_return_and_stabilizer_crt": "PASS",
            "G6_unreduced_global_angle_obstruction": "PASS",
            "G7_checker_sympy_replay_mutation": "PASS",
            "G8_two_substantive_revisions": "PASS",
            "G9_six_fresh_pdf_builds_fonts_logs_text": "PASS",
            "G10_manifest_hash_closure": "PASS",
            "G11_target_euler_zero_operator_route_b": "NOT_CLAIMED",
        },
        "results": {
            **data["enumeration"], "audited_cells": 149,
            "checker_assertions": checker_n, "symbolic_checks": symbolic_n,
            "hostile_rejections": mutation_n, "evidence_bytes": EVIDENCE.stat().st_size,
            "evidence_payload_sha256": data["payload_sha256"],
            "evidence_sha256": EVIDENCE_SHA, "evaluation_semantic_sha256": EVALUATION_SHA,
            "pdf_sha256": digest(PDF), "pdf_pages": pages[-1],
        },
        "route_a_verdict": data["route_a"], "nonclaims": data["nonclaims"],
        "excluded_from_manifest": ["C296_RELEASE_MANIFEST.json", "code/__pycache__/", "*.pyc", "paper build sidecars"],
        "files": files,
    }
    MANIFEST.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    assert len([path for path in ROOT.rglob("*") if path.is_file()]) == 28
    print(json.dumps({
        "status": "C296_MANIFEST_PASS", "payload_file_count": 27,
        "physical_file_count": 28, "manifest_sha256": digest(MANIFEST),
        "evidence_sha256": EVIDENCE_SHA, "pdf_sha256": digest(PDF),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
