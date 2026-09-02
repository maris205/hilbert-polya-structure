#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite for HCS-C307."""
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
CHECKER = ROOT / "code/c307_connectivity_checker.py"
EVIDENCE = ROOT / "results/c307_connectivity_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C307/2026-09-03.yaml"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def canonical(data: dict, repair: bool = True) -> bytes:
    if repair:
        data["payload_sha256"] = payload_hash(data)
    return (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()


def run(evidence: Path, evaluation: Path, optimized: bool = False):
    command = [sys.executable]
    if optimized:
        command.append("-O")
    command += [str(CHECKER), "--evidence", str(evidence), "--yaml", str(evaluation), "--skip-exhaustive"]
    return subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)


def main() -> None:
    baseline = run(EVIDENCE, EVALUATION)
    if baseline.returncode:
        raise AssertionError("baseline failed:\n" + baseline.stdout)
    optimized = run(EVIDENCE, EVALUATION, optimized=True)
    if optimized.returncode == 0 or "refuses python -O" not in optimized.stdout:
        raise AssertionError("checker did not explicitly reject python -O")
    checker_text = CHECKER.read_text(encoding="utf-8")
    if "import c307_connectivity_producer" in checker_text or "from c307_connectivity_producer" in checker_text:
        raise AssertionError("checker imports producer")

    original = json.loads(EVIDENCE.read_text())
    raw = EVIDENCE.read_bytes()
    yaml_raw = EVALUATION.read_bytes()
    killed: list[str] = []
    survived: list[tuple[str, str]] = []
    semantic = [
        ("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C306")),
        ("obstruction", lambda d: d.__setitem__("obstruction_id", "HEN-O000")),
        ("source", lambda d: d.__setitem__("source_commit", "0" * 40)),
        ("epoch-bool", lambda d: d.__setitem__("fixed_epoch", True)),
        ("epoch-float", lambda d: d.__setitem__("fixed_epoch", 1788393600.0)),
        ("scope", lambda d: d.__setitem__("scope_literal", "OPEN")),
        ("model-replacement", lambda d: d["model"].__setitem__("edges", "independent Bernoulli edges")),
        ("model-hitting", lambda d: d["model"].__setitem__("hitting_time", "last isolated vertex")),
        ("recurrence", lambda d: d["theorem"].__setitem__("recurrence", "wrong")),
        ("support", lambda d: d["theorem"].__setitem__("support", "wrong")),
        ("moments", lambda d: d["theorem"].__setitem__("moments", "first moment only")),
        ("gumbel", lambda d: d["theorem"].__setitem__("gumbel", "Gaussian")),
        ("proof-factorial", lambda d: d["proof_certificates"].__setitem__("isolated_factorial", "assumed")),
        ("proof-other", lambda d: d["proof_certificates"].__setitem__("other_components", "ignored")),
        ("atlas-nmin-bool", lambda d: d["finite_connected_atlas"].__setitem__("n_min", True)),
        ("atlas-nmax-float", lambda d: d["finite_connected_atlas"].__setitem__("n_max", 12.0)),
        ("atlas-row-count", lambda d: d["finite_connected_atlas"].__setitem__("row_count", 11)),
        ("atlas-cell-float", lambda d: d["finite_connected_atlas"].__setitem__("coefficient_cells", 298.0)),
        ("atlas-extra-row", lambda d: d["finite_connected_atlas"]["rows"].append(copy.deepcopy(d["finite_connected_atlas"]["rows"][-1]))),
        ("row-n-bool", lambda d: d["finite_connected_atlas"]["rows"][0].__setitem__("n", False)),
        ("row-K-float", lambda d: d["finite_connected_atlas"]["rows"][5].__setitem__("K", 15.0)),
        ("row-cell-count", lambda d: d["finite_connected_atlas"]["rows"][6].__setitem__("cell_count", 0)),
        ("first-support", lambda d: d["finite_connected_atlas"]["rows"][7].__setitem__("first_possible_hitting_m", 0)),
        ("last-support", lambda d: d["finite_connected_atlas"]["rows"][8].__setitem__("last_possible_hitting_m", 1)),
        ("tree-endpoint", lambda d: d["finite_connected_atlas"]["rows"][4].__setitem__("tree_endpoint_count", 1)),
        ("complete-endpoint", lambda d: d["finite_connected_atlas"]["rows"][9].__setitem__("complete_endpoint_count", 2)),
        ("entry-extra", lambda d: d["finite_connected_atlas"]["rows"][4]["entries"].append(copy.deepcopy(d["finite_connected_atlas"]["rows"][4]["entries"][-1]))),
        ("entry-m-bool", lambda d: d["finite_connected_atlas"]["rows"][4]["entries"][0].__setitem__("m", False)),
        ("connected-count", lambda d: d["finite_connected_atlas"]["rows"][4]["entries"][4].__setitem__("connected_count", 0)),
        ("connected-count-bool", lambda d: d["finite_connected_atlas"]["rows"][5]["entries"][5].__setitem__("connected_count", True)),
        ("total-count-float", lambda d: d["finite_connected_atlas"]["rows"][6]["entries"][6].__setitem__("total_graph_count", 1.0)),
        ("cdf", lambda d: d["finite_connected_atlas"]["rows"][5]["entries"][5].__setitem__("cdf", "1")),
        ("pmf", lambda d: d["finite_connected_atlas"]["rows"][6]["entries"][7].__setitem__("pmf", "0")),
        ("tail", lambda d: d["finite_connected_atlas"]["rows"][7]["entries"][8].__setitem__("tail", "0")),
        ("moment-count-bool", lambda d: d["finite_connected_atlas"]["rows"][8].__setitem__("moment_count", True)),
        ("moment-order-float", lambda d: d["finite_connected_atlas"]["rows"][8]["moments"][0].__setitem__("order", 1.0)),
        ("moment-value", lambda d: d["finite_connected_atlas"]["rows"][8]["moments"][1].__setitem__("raw_moment", "0")),
        ("diagnostic-count", lambda d: d["isolated_vertex_diagnostics"].__setitem__("row_count", 59)),
        ("diagnostic-extra", lambda d: d["isolated_vertex_diagnostics"]["rows"].append(copy.deepcopy(d["isolated_vertex_diagnostics"]["rows"][-1]))),
        ("diagnostic-n-bool", lambda d: d["isolated_vertex_diagnostics"]["rows"][0].__setitem__("n", True)),
        ("diagnostic-c-float", lambda d: d["isolated_vertex_diagnostics"]["rows"][1].__setitem__("c", -1.0)),
        ("diagnostic-m", lambda d: d["isolated_vertex_diagnostics"]["rows"][2].__setitem__("m", 0)),
        ("diagnostic-r-bool", lambda d: d["isolated_vertex_diagnostics"]["rows"][3].__setitem__("r", True)),
        ("diagnostic-range", lambda d: d["isolated_vertex_diagnostics"]["rows"][4].__setitem__("within_edge_range", False)),
        ("diagnostic-value", lambda d: d["isolated_vertex_diagnostics"]["rows"][5].__setitem__("factorial_moment_decimal_12", "0.000000000000")),
        ("diagnostic-target", lambda d: d["isolated_vertex_diagnostics"]["rows"][6].__setitem__("poisson_target_decimal_12", "0.000000000000")),
        ("route-tuple", lambda d: d["route_a"]["tuple"].__setitem__(4, "A4_FORMAL_HINT")),
        ("route-verdict", lambda d: d["route_a"].__setitem__("overall_verdict", "ROUTE_A_ACCEPTED")),
        ("route-b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True)),
        ("scope-flag", lambda d: d["scope_flags"].__setitem__("claims_target_euler_factors", True)),
        ("boundary", lambda d: d["boundaries"].__setitem__(1, "pathwise identity claimed")),
        ("collision-C301", lambda d: d["collision_boundary"].__setitem__("C301", "identical")),
        ("collision-C291", lambda d: d["collision_boundary"].__setitem__("C291", "identical")),
        ("collision-C276", lambda d: d["collision_boundary"].__setitem__("C276", "identical")),
        ("source-token", lambda d: d["source_owner_tokens"].__setitem__(0, "fake")),
        ("summary-bool", lambda d: d["regression_summary"].__setitem__("finite_rows", True)),
        ("summary-masks", lambda d: d["regression_summary"].__setitem__("exhaustive_graph_masks", 0)),
        ("unknown-key", lambda d: d.__setitem__("unknown", 1)),
        ("drop-key", lambda d: d.pop("proof_certificates")),
    ]
    json_parser = [
        ("json-duplicate", lambda b: b.replace(b'{\n  "boundaries"', b'{\n  "candidate_id": "HCS-C307",\n  "boundaries"', 1)),
        ("json-trailing", lambda b: b + b"{}\n"),
        ("json-compact", lambda b: json.dumps(json.loads(b)).encode()),
        ("json-nan", lambda b: b.replace(b'"fixed_epoch": 1788393600', b'"fixed_epoch": NaN', 1)),
        ("json-invalid-utf8", lambda b: b + b"\xff"),
        ("json-top-list", lambda b: b"[]\n"),
    ]
    yaml_semantic = [
        ("yaml-candidate", lambda d: d.__setitem__("candidate_id", "HCS-C306")),
        ("yaml-source", lambda d: d.__setitem__("source_commit", "0" * 40)),
        ("yaml-epoch-bool", lambda d: d.__setitem__("fixed_epoch", True)),
        ("yaml-obstruction", lambda d: d.__setitem__("obstruction_id", "HEN-O000")),
        ("yaml-a0", lambda d: d["a0"].__setitem__("verdict", "A0_PASS")),
        ("yaml-a4", lambda d: d["a4"].__setitem__("verdict", "A4_FORMAL_HINT")),
        ("yaml-tuple", lambda d: d["tuple"].__setitem__(2, "A2_PASS")),
        ("yaml-route-b", lambda d: d.__setitem__("route_b_invocation_allowed", True)),
        ("yaml-flag", lambda d: d["scope_flags"].__setitem__("claims_root_number", True)),
        ("yaml-artifact-extra", lambda d: d["artifact_paths"].append("extra")),
        ("yaml-source-token", lambda d: d["source_owner_tokens"].__setitem__(0, "fake")),
        ("yaml-unknown", lambda d: d.__setitem__("unknown", "x")),
    ]
    yaml_parser = [
        ("yaml-duplicate", lambda b: b + b"candidate_id: HCS-C307\n"),
        ("yaml-anchor", lambda b: b"a: &x y\nb: *x\n" + b),
        ("yaml-merge", lambda b: b"a: &x {v: 1}\nb: {<<: *x}\n" + b),
        ("yaml-nonstring", lambda b: b"1: bad\n" + b),
    ]

    with tempfile.TemporaryDirectory(prefix="c307-mutation-") as folder_name:
        folder = Path(folder_name)
        for name, mutate in semantic:
            data = copy.deepcopy(original)
            mutate(data)
            path = folder / (name + ".json")
            path.write_bytes(canonical(data, repair=True))
            result = run(path, EVALUATION)
            (killed if result.returncode else survived).append(name if result.returncode else (name, result.stdout))
        stale = copy.deepcopy(original)
        stale["candidate_id"] = "HCS-C306"
        stale_path = folder / "stale-hash.json"
        stale_path.write_bytes(canonical(stale, repair=False))
        result = run(stale_path, EVALUATION)
        (killed if result.returncode else survived).append("stale-hash" if result.returncode else ("stale-hash", result.stdout))
        for name, mutate in json_parser:
            path = folder / (name + ".json")
            path.write_bytes(mutate(raw))
            result = run(path, EVALUATION)
            (killed if result.returncode else survived).append(name if result.returncode else (name, result.stdout))
        base = yaml.safe_load(EVALUATION.read_text())
        for name, mutate in yaml_semantic:
            data = copy.deepcopy(base)
            mutate(data)
            path = folder / (name + ".yaml")
            path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True))
            result = run(EVIDENCE, path)
            (killed if result.returncode else survived).append(name if result.returncode else (name, result.stdout))
        for name, mutate in yaml_parser:
            path = folder / (name + ".yaml")
            path.write_bytes(mutate(yaml_raw))
            result = run(EVIDENCE, path)
            (killed if result.returncode else survived).append(name if result.returncode else (name, result.stdout))

    if survived:
        raise AssertionError(f"surviving mutations: {survived}")
    expected = len(semantic) + 1 + len(json_parser) + len(yaml_semantic) + len(yaml_parser)
    if len(killed) != expected:
        raise AssertionError("mutation accounting")
    print(f"C307 mutation suite PASS ({len(killed)}/{expected} repaired semantic/parser/stale-hash mutations killed)")
    print("classes=model,counts,coordinates,type-traps,CDF,PMF,moments,Gumbel,route,scope,JSON,YAML,python-O")


if __name__ == "__main__":
    main()
