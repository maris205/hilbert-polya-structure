#!/usr/bin/env python3
"""Hostile repaired-hash and parser mutation suite for HCS-C321."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c321_preferential_attachment_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C321/2026-09-03.yaml"
CHECKER = ROOT / "code/c321_preferential_attachment_checker.py"
PRODUCER = ROOT / "code/c321_preferential_attachment_producer.py"


def repair(data: dict) -> None:
    body = dict(data)
    body.pop("payload_sha256", None)
    data["payload_sha256"] = hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def rejected(evidence_bytes: bytes, evaluation_bytes: bytes) -> bool:
    with tempfile.TemporaryDirectory(prefix="c321-mutation-") as directory:
        base = Path(directory)
        evidence = base / "evidence.json"
        evaluation = base / "evaluation.yaml"
        evidence.write_bytes(evidence_bytes)
        evaluation.write_bytes(evaluation_bytes)
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
        proc = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(evidence),
                               "--evaluation", str(evaluation)], env=env,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return proc.returncode != 0


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C321 mutation lane refuses optimized Python")
    original = json.loads(EVIDENCE.read_text())
    yaml_raw = EVALUATION.read_bytes()
    mutations = []

    def add(name, fn):
        value = copy.deepcopy(original)
        fn(value)
        repair(value)
        mutations.append((name, (json.dumps(value, sort_keys=True, indent=2,
                                             ensure_ascii=False) + "\n").encode(), yaml_raw))

    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C320"))
    add("source", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("evaluation-date", lambda d: d.__setitem__("evaluation_date", "2026-09-04"))
    add("extra-root-key", lambda d: d.__setitem__("unexpected", 1))
    add("model-denominator", lambda d: d["model"].__setitem__("update", "vertex n+1 attaches with denominator 2n"))
    add("self-loop", lambda d: d["model"].__setitem__("self_loops", True))
    add("observable-mix", lambda d: d["model"].__setitem__("fixed_observable", "D_i=N_i"))
    add("limit-scale", lambda d: d["theorem_contract"].__setitem__("fixed_limit", "D_i(n)/n converges"))
    add("maximum-degree-overclaim", lambda d: d["theorem_contract"].__setitem__("excluded", "none"))
    add("route-upgrade", lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route-b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope", lambda d: d["scope_flags"].__setitem__("claims_root_number", True))
    add("reference", lambda d: d["references"][2].__setitem__("identifier", "wrong-doi"))
    add("collision", lambda d: d["collision_boundary"].__setitem__("C263", "same model"))
    add("nonclaim", lambda d: d["nonclaims"].__setitem__(0, "finite evidence proves the limit"))
    add("yaml-relative-path", lambda d: d["route_a_yaml"].__setitem__("relative_path", "wrong.yaml"))
    add("moment", lambda d: d["time_rows"][3]["fixed_vertex_moments"][4].__setitem__("observed", "0"))
    add("population", lambda d: d["time_rows"][5]["degree_population_moments"][0].__setitem__("second_moment", "0"))
    add("terminal", lambda d: d["terminal_degree_vector_distribution"][0].__setitem__("probability", "0"))
    add("profile", lambda d: d["profile_rows"][4].__setitem__("p_k", "1"))
    add("nested-extra-key", lambda d: d["time_rows"][0]["fixed_vertex_moments"][0].__setitem__("extra", 1))
    add("duplicate-cell", lambda d: d["time_rows"][2]["fixed_vertex_moments"].append(copy.deepcopy(d["time_rows"][2]["fixed_vertex_moments"][-1])))
    add("omit-cell", lambda d: d["time_rows"][3]["degree_population_moments"].pop())
    add("truncated-profile", lambda d: d["profile_rows"].pop())
    add("leaf-count", lambda d: d.__setitem__("audited_leaf_count", 1))

    raw_json = EVIDENCE.read_text()
    malformed_json = [
        ("json-duplicate", raw_json.replace('"candidate_id": "HCS-C321",', '"candidate_id": "HCS-C321",\n  "candidate_id": "HCS-C321",', 1).encode()),
        ("json-nonfinite", raw_json.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1).encode()),
        ("json-root", b"[]\n"),
    ]
    for name, raw in malformed_json:
        mutations.append((name, raw, yaml_raw))

    yaml_text = EVALUATION.read_text()
    malformed_yaml = [
        ("yaml-duplicate", yaml_text + "candidate_id: HCS-C321\n"),
        ("yaml-alias", "probe: &probe 1\ncopy: *probe\n" + yaml_text),
        ("yaml-merge", "base: &base {x: 1}\nmerged:\n  <<: *base\n" + yaml_text),
        ("yaml-nonstring-key", "1: forbidden\n" + yaml_text),
        ("yaml-root", "- not\n- a\n- mapping\n"),
        ("yaml-implicit-timestamp", yaml_text.replace('evaluation_date: "2026-09-03"', "evaluation_date: 2026-09-03", 1)),
        ("yaml-unknown-field", yaml_text + "unknown_field: forbidden\n"),
        ("yaml-missing-field", yaml_text.replace("arithmetic_origin: \"none\"\n", "", 1)),
        ("yaml-typed-epoch", yaml_text.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
        ("yaml-typed-route-lock", yaml_text.replace("route_b_invocation_allowed: false", 'route_b_invocation_allowed: "false"', 1)),
        ("yaml-authority", yaml_text.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md", "evaluator_authority: route-a-evaluator", 1)),
        ("yaml-status-delete", yaml_text.replace("  evidence_status: PROVED\n", "", 1)),
        ("yaml-status-rewrite", yaml_text.replace("  evidence_status: STOP_SCOPED\n", "  evidence_status: PROVED\n", 1)),
    ]
    for name, text in malformed_yaml:
        mutations.append((name, EVIDENCE.read_bytes(), text.encode()))

    failures = [name for name, evidence, evaluation in mutations if not rejected(evidence, evaluation)]
    if failures:
        raise AssertionError(f"mutations survived: {failures}")

    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    for script in (PRODUCER, CHECKER):
        proc = subprocess.run([sys.executable, "-O", str(script)], env=env,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if proc.returncode == 0:
            raise AssertionError(f"optimized mode survived: {script.name}")
    print(f"C321 hostile mutation suite: PASS ({len(mutations)}/{len(mutations)} rejected; optimized mode rejected)")


if __name__ == "__main__":
    main()
