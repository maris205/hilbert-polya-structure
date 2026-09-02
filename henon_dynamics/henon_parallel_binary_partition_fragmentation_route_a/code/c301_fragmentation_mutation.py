#!/usr/bin/env python3
"""Mutation tests for the independent C301 checker and strict parsers."""
from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "code/c301_fragmentation_checker.py"
EVIDENCE = ROOT / "results/c301_fragmentation_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C301/2026-09-02.yaml"


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def canonical(data: dict) -> bytes:
    data["payload_sha256"] = payload_hash(data)
    return (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


def checker(evidence: Path, evaluation: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(CHECKER), "--evidence", str(evidence), "--yaml", str(evaluation)],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
    )


def main() -> None:
    baseline = checker(EVIDENCE, EVALUATION)
    if baseline.returncode:
        raise AssertionError("baseline checker failed:\n" + baseline.stdout)

    original = json.loads(EVIDENCE.read_text())
    yaml_original = EVALUATION.read_bytes()
    killed: list[str] = []
    survivors: list[tuple[str, str]] = []

    semantic_mutations = [
        ("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C300")),
        ("obstruction", lambda d: d.__setitem__("obstruction_id", "HEN-O000")),
        ("source", lambda d: d.__setitem__("source_commit", "0" * 40)),
        ("epoch-bool", lambda d: d.__setitem__("fixed_epoch", True)),
        ("scope", lambda d: d.__setitem__("scope_literal", "OPEN")),
        ("evaluator", lambda d: d.__setitem__("evaluator_authority_sha256", "0" * 64)),
        ("model-update", lambda d: d["model"].__setitem__("update", "block-shared bit")),
        ("kernel", lambda d: d["model"].__setitem__("one_step_kernel", "wrong")),
        ("partition-law", lambda d: d["theorem"].__setitem__("partition_law", "wrong")),
        ("diagonalization", lambda d: d["theorem"].__setitem__("diagonalizability", "diagonal entries suffice")),
        ("lattice", lambda d: d["theorem"].__setitem__("lattice_boundary", "continuous Gumbel law")),
        ("proof-certificate", lambda d: d["proof_certificates"].__setitem__("spectrum_guard", "triangular therefore diagonalizable")),
        ("stirling", lambda d: d["stirling_table"][8]["S_n_k_k_0_to_n"].__setitem__(4, d["stirling_table"][8]["S_n_k_k_0_to_n"][4] + 1)),
        ("bell", lambda d: d["transition_regression"]["groups"][5].__setitem__("bell_number", 202)),
        ("state", lambda d: d["transition_regression"]["groups"][3]["rows"][4].__setitem__("state_rgs", "0000")),
        ("rank", lambda d: d["transition_regression"]["groups"][4]["rows"][10].__setitem__("rank", 99)),
        ("transition-numerator", lambda d: d["transition_regression"]["groups"][5]["rows"][0]["transitions"][0].__setitem__("numerator", 3)),
        ("transition-denominator", lambda d: d["transition_regression"]["groups"][4]["rows"][1]["transitions"][0].__setitem__("denominator", 7)),
        ("transition-target", lambda d: d["transition_regression"]["groups"][2]["rows"][0]["transitions"][0].__setitem__("target_rgs", "012")),
        ("transition-count", lambda d: d["transition_regression"].__setitem__("listed_nonzero_probability_cells", 0)),
        ("time-q", lambda d: d["time_regression"]["rows"][35].__setitem__("q", 3)),
        ("block-coefficient", lambda d: d["time_regression"]["rows"][50]["block_count_k_1_to_n_numerators"].__setitem__(2, 0)),
        ("block-denominator", lambda d: d["time_regression"]["rows"][60].__setitem__("common_denominator", 1)),
        ("expectation", lambda d: d["time_regression"]["rows"][45].__setitem__("expected_blocks", "1/2")),
        ("absorption-cdf", lambda d: d["time_regression"]["rows"][70].__setitem__("absorption_cdf", "1")),
        ("trace", lambda d: d["time_regression"]["rows"][23].__setitem__("trace_K_power_t", "0")),
        ("mass", lambda d: d["absorption_mass_regression"][55].__setitem__("mass", "0")),
        ("diagnostic", lambda d: d["critical_window_diagnostics"][2].__setitem__("exact_cdf_decimal_12", "0.000000000000")),
        ("tuple", lambda d: d["route_a"]["tuple"].__setitem__(4, "A4_FORMAL_HINT")),
        ("verdict", lambda d: d["route_a"].__setitem__("overall_verdict", "ROUTE_A_ACCEPTED")),
        ("route-b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True)),
        ("scope-flag", lambda d: d["scope_flags"].__setitem__("claims_root_number", True)),
        ("collision", lambda d: d["collision_boundary"].__setitem__("C215", "same chain")),
        ("unknown-key", lambda d: d.__setitem__("unexpected", 1)),
        ("drop-key", lambda d: d.pop("nonclaims")),
    ]

    json_parser_mutations = [
        ("json-duplicate", lambda raw: raw.replace(b'{\n  "absorption_mass_regression"', b'{\n  "candidate_id": "HCS-C301",\n  "absorption_mass_regression"', 1)),
        ("json-trailing", lambda raw: raw + b"{}\n"),
        ("json-noncanonical", lambda raw: json.dumps(json.loads(raw)).encode()),
        ("json-nan", lambda raw: raw.replace(b'"fixed_epoch": 1788307200', b'"fixed_epoch": NaN', 1)),
        ("json-invalid-utf8", lambda raw: raw + b"\xff"),
        ("json-top-list", lambda raw: b"[]\n"),
    ]

    yaml_semantic_mutations = [
        ("yaml-candidate", lambda d: d.__setitem__("candidate_id", "HCS-C300")),
        ("yaml-source", lambda d: d.__setitem__("source_commit", "0" * 40)),
        ("yaml-epoch-bool", lambda d: d.__setitem__("fixed_epoch", True)),
        ("yaml-scope", lambda d: d.__setitem__("scope_literal", "OPEN")),
        ("yaml-obstruction", lambda d: d.__setitem__("obstruction_id", "HEN-O000")),
        ("yaml-a1", lambda d: d["a1"].__setitem__("verdict", "A1_PASS")),
        ("yaml-a4", lambda d: d["a4"].__setitem__("verdict", "A4_FORMAL_HINT")),
        ("yaml-tuple", lambda d: d["tuple"].__setitem__(0, "A0_PASS")),
        ("yaml-route-b", lambda d: d.__setitem__("route_b_invocation_allowed", True)),
        ("yaml-flag", lambda d: d["scope_flags"].__setitem__("claims_target_euler_factors", True)),
        ("yaml-artifact", lambda d: d["artifact_paths"].__setitem__(2, "paper/missing.pdf")),
        ("yaml-unknown", lambda d: d.__setitem__("unexpected", "value")),
    ]

    yaml_parser_mutations = [
        ("yaml-duplicate", lambda raw: raw + b"candidate_id: HCS-C301\n"),
        ("yaml-anchor", lambda raw: b"anchor: &x value\nalias: *x\n" + raw),
        ("yaml-merge", lambda raw: b"base: &b {x: 1}\nmerged: {<<: *b}\n" + raw),
        ("yaml-nonstring-key", lambda raw: b"1: bad\n" + raw),
    ]

    with tempfile.TemporaryDirectory(prefix="c301-mutation-") as folder:
        folder = Path(folder)
        for name, mutate in semantic_mutations:
            data = copy.deepcopy(original); mutate(data)
            evidence = folder / f"{name}.json"; evidence.write_bytes(canonical(data))
            result = checker(evidence, EVALUATION)
            (killed if result.returncode else survivors).append(name if result.returncode else (name, result.stdout))

        raw = EVIDENCE.read_bytes()
        for name, mutate in json_parser_mutations:
            evidence = folder / f"{name}.json"; evidence.write_bytes(mutate(raw))
            result = checker(evidence, EVALUATION)
            (killed if result.returncode else survivors).append(name if result.returncode else (name, result.stdout))

        # BaseLoader avoids implicit timestamps while providing mutable ordinary trees.
        yaml_data = yaml.load(EVALUATION.read_text(), Loader=yaml.BaseLoader)
        # Restore scalar types that the exact contract requires.
        yaml_data["fixed_epoch"] = 1788307200
        yaml_data["route_b_invocation_allowed"] = False
        for key in yaml_data["scope_flags"]:
            yaml_data["scope_flags"][key] = False
        for name, mutate in yaml_semantic_mutations:
            data = copy.deepcopy(yaml_data); mutate(data)
            evaluation = folder / f"{name}.yaml"
            evaluation.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True))
            result = checker(EVIDENCE, evaluation)
            (killed if result.returncode else survivors).append(name if result.returncode else (name, result.stdout))

        for name, mutate in yaml_parser_mutations:
            evaluation = folder / f"{name}.yaml"; evaluation.write_bytes(mutate(yaml_original))
            result = checker(EVIDENCE, evaluation)
            (killed if result.returncode else survivors).append(name if result.returncode else (name, result.stdout))

    if survivors:
        raise AssertionError(f"surviving mutations: {survivors}")
    expected = len(semantic_mutations) + len(json_parser_mutations) + len(yaml_semantic_mutations) + len(yaml_parser_mutations)
    if len(killed) != expected:
        raise AssertionError("mutation accounting mismatch")
    print(f"C301 mutation suite PASS ({len(killed)}/{expected} semantic/parser mutations killed)")
    print("classes=metadata,formula,kernel,spectrum,absorption,lattice,route,scope,JSON,YAML")


if __name__ == "__main__":
    main()
