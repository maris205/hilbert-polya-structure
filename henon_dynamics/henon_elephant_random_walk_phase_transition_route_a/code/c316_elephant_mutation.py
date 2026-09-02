#!/usr/bin/env python3
"""Repaired-hash semantic and parser attacks for HCS-C316."""
import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c316_elephant_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C316/2026-09-03.yaml"
CHECKER = ROOT / "code/c316_elephant_checker.py"


def payload(data):
    body = dict(data); body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def set_path(data, path, value):
    cursor = data
    for item in path[:-1]: cursor = cursor[item]
    cursor[path[-1]] = value


def main():
    if sys.flags.optimize:
        raise RuntimeError("C316 mutation suite refuses optimized Python")
    pristine = json.loads(EVIDENCE.read_text()); raw = EVIDENCE.read_text(); yaml_raw = EVALUATION.read_text()
    mutations = [
        (("candidate_id",), "HCS-C000"), (("obstruction_id",), "HEN-O000"),
        (("source_commit",), "0"*40), (("scope_literal",), "EXPANDED"),
        (("route_a", "tuple", 4), "A4_PASS"), (("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_target_euler_factors"), True),
        (("model", "memory_rule"), "copy only"),
        (("theorem_contract", "martingale"), "one formula including p=0"),
        (("cases", 0, "phase"), "critical"), (("cases", 0, "times", 0, "total_mass"), "0"),
        (("cases", 4, "times", 3, "mean"), "99"), (("cases", 10, "times", 7, "second_moment"), "0"),
        (("cases", 20, "times", 13, "variance"), "-1"), (("cases", 25, "times", 5, "pmf", 0, "probability"), "0"),
        (("martingale_rows", 0, "normalized_after_mean"), "1"),
        (("martingale_rows", 100, "normalization"), "wrong"),
        (("history_crosschecks", 0, "positive_history_count"), 999),
        (("history_crosschecks", 2, "terminal_pmf", 0, "position"), -99),
        (("superdiffusive_moment_rows", 0, "moment_2", "prefactor"), "1"),
        (("superdiffusive_moment_rows", 0, "p"), "7/8"),
        (("superdiffusive_moment_rows", 8, "endpoint_class"), "nondegenerate"),
        (("enumeration", "parameter_case_count"), 34), (("enumeration", "audited_leaf_count"), 1),
    ]
    attacks = []
    for path, value in mutations:
        changed = copy.deepcopy(pristine); set_path(changed, path, value); changed["payload_sha256"] = payload(changed)
        attacks.append(("semantic", json.dumps(changed, sort_keys=True, indent=2) + "\n", yaml_raw))
    attacks += [
        ("stale-hash", raw.replace('"candidate_id": "HCS-C316"', '"candidate_id": "HCS-C000"', 1), yaml_raw),
        ("duplicate-json", raw.replace("{\n", '{\n  "schema": "duplicate",\n', 1), yaml_raw),
        ("nonfinite-json", raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1), yaml_raw),
        ("json-array", "[]\n", yaml_raw),
        ("yaml-duplicate", raw, yaml_raw + "candidate_id: HCS-C316\n"),
        ("yaml-anchor", raw, yaml_raw.replace("candidate_id: HCS-C316", "candidate_id: &bad HCS-C316", 1)),
        ("yaml-alias", raw, yaml_raw + "probe: *bad\n"),
        ("yaml-array", raw, "- bad\n"),
        ("yaml-route", raw, yaml_raw.replace("  - A0_FAIL", "  - A0_PASS", 1)),
        ("yaml-routeb", raw, yaml_raw.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1)),
        ("yaml-scope", raw, yaml_raw.replace("  claims_root_number: false", "  claims_root_number: true", 1)),
        ("yaml-epoch-type", raw, yaml_raw.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
        ("yaml-family-semantic", raw, yaml_raw.replace(
            'family: "non-Markovian reinforced random walks"',
            'family: "repaired but unauthorized family"', 1)),
        ("yaml-finite-role-semantic", raw, yaml_raw.replace(
            'finite_evidence_role: "regression evidence only; finite enumeration is not a proof of a central limit theorem"',
            'finite_evidence_role: "finite evidence proves the central limit theorem"', 1)),
    ]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC"); rejected = 0
    with tempfile.TemporaryDirectory(prefix="c316-mutation-") as tmp:
        for index, (name, text, yaml_text) in enumerate(attacks):
            path = Path(tmp)/f"{index}.json"; ypath = Path(tmp)/f"{index}.yaml"
            path.write_text(text); ypath.write_text(yaml_text)
            run = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(path), "--evaluation", str(ypath)],
                                 env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if run.returncode == 0: raise AssertionError(f"mutation survived {name}-{index}")
            rejected += 1
        optimized = subprocess.run([sys.executable, "-O", str(CHECKER)], env=env,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        if optimized.returncode == 0: raise AssertionError("optimized checker survived")
    print(f"C316 hostile mutation suite: PASS {rejected}/{len(attacks)} plus optimized-Python rejection")


if __name__ == "__main__": main()
