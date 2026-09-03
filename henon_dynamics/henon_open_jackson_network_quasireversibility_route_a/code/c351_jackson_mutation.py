#!/usr/bin/env python3
"""Repaired-hash and strict-parser hostile tests for HCS-C351."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c351_jackson_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C351/2026-09-03.yaml"
CHECKER = ROOT / "code/c351_jackson_checker.py"


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def repair(data):
    changed = copy.deepcopy(data)
    changed.pop("payload_sha256", None)
    changed["payload_sha256"] = hashlib.sha256(canonical(changed)).hexdigest()
    return json.dumps(changed, sort_keys=True, indent=2, ensure_ascii=False) + "\n"


def set_path(data, path, value):
    cursor = data
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value


def repaired_yaml(data, raw):
    changed = copy.deepcopy(data)
    semantic = yaml.safe_load(raw)
    changed["route_a_yaml"]["raw_sha256"] = hashlib.sha256(raw.encode()).hexdigest()
    changed["route_a_yaml"]["semantic_sha256"] = hashlib.sha256(canonical(semantic)).hexdigest()
    return repair(changed)


def main():
    if sys.flags.optimize:
        raise RuntimeError("C351 mutation lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    json_raw = EVIDENCE.read_text()
    yaml_raw = EVALUATION.read_text()
    attacks = []
    semantic_attacks = [
        (("candidate_id",), "HCS-C000"), (("obstruction_id",), "HEN-O000"),
        (("evaluation_date",), "2099-01-01"), (("source_commit",), "0" * 40),
        (("scope_literal",), "EXPANDED"),
        (("evaluator", "authority"), "route-a-evaluator"),
        (("evaluator", "sha256"), "0" * 64),
        (("route_a_yaml", "relative_path"), "evaluation.yaml"),
        (("model", "traffic_convention"), "column convention"),
        (("model", "external_input"), "dependent inputs"),
        (("theorem_contract", "stability"), "sufficient only"),
        (("theorem_contract", "time_reversal"), "indices omitted"),
        (("theorem_contract", "external_departures"), "all internal flows independent"),
        (("theorem_contract", "time_reversal"), "reverse network requires positive exogenous rates at every node"),
        (("theorem_contract", "external_departures"), "stationary external departure law is inferred from the full marked path including phantom self-routing"),
        (("theorem_contract", "proof_owner"), "analytic generator balance and stationary drift necessity"),
        (("collision_boundary", "C285"), "same mechanism"),
        (("nonclaims", 0), "all routed arc flows are independent"),
        (("references", 0, "identifier"), "DOI:mutated"),
        (("route_a", "tuple", 0), "A0_ANALYTIC_ARITHMETIC_ORIGIN"),
        (("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_target_euler_factors"), True),
        (("network_rows", 0, "traffic", 0), "0"),
        (("network_rows", 6, "routing_power_certificate", "maximum_row_sum"), "1"),
        (("balance_rows", 17, "residual"), "1"),
        (("reverse_network_rows", 5, "reverse_exit_probabilities", 0), "0"),
        (("reverse_jump_rows", 0, "reverse_rate"), "0"),
        (("boundary_rows", 4, "classification"), "positive_recurrent"),
        (("enumeration", "finite_evidence_proves_infinite_theorem"), True),
    ]
    for index, (path, value) in enumerate(semantic_attacks):
        changed = copy.deepcopy(data)
        set_path(changed, path, value)
        attacks.append((f"repaired-semantic-{index}", repair(changed), yaml_raw))
    for section in ("network_rows", "balance_rows", "reverse_network_rows",
                    "reverse_jump_rows", "boundary_rows"):
        changed = copy.deepcopy(data)
        changed[section][0]["unowned"] = "survive"
        attacks.append((f"nested-extra-{section}", repair(changed), yaml_raw))
        changed = copy.deepcopy(data)
        changed[section].pop(0)
        attacks.append((f"row-omit-{section}", repair(changed), yaml_raw))
        changed = copy.deepcopy(data)
        changed[section].insert(0, copy.deepcopy(changed[section][0]))
        attacks.append((f"row-duplicate-{section}", repair(changed), yaml_raw))
    missing = copy.deepcopy(data)
    missing.pop("theorem_contract")
    attacks.append(("missing-top-key", repair(missing), yaml_raw))
    unknown = copy.deepcopy(data)
    unknown["unknown_top"] = 1
    attacks.append(("unknown-top-key", repair(unknown), yaml_raw))
    stale = copy.deepcopy(data)
    stale["candidate_id"] = "HCS-C000"
    attacks.append(("stale-hash-control",
                    json.dumps(stale, sort_keys=True, indent=2) + "\n", yaml_raw))
    attacks.extend([
        ("duplicate-json", json_raw.replace("{\n", '{\n  "schema": "duplicate",\n', 1), yaml_raw),
        ("nonfinite-json", json_raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": Infinity', 1), yaml_raw),
        ("json-root-array", "[]\n", yaml_raw),
    ])
    yaml_changes = [
        ("yaml-duplicate", yaml_raw + "candidate_id: HCS-C351\n"),
        ("yaml-anchor", yaml_raw.replace("candidate_id: HCS-C351", "candidate_id: &id HCS-C351", 1)),
        ("yaml-alias", "holder: &h HCS-C351\ncandidate_id: *h\n" + yaml_raw),
        ("yaml-merge", "base: &b {x: 1}\nmerged:\n  <<: *b\n" + yaml_raw),
        ("yaml-nonstring-key", "1: forbidden\n" + yaml_raw),
        ("yaml-implicit-timestamp", yaml_raw.replace("evaluation_date: '2026-09-03'", "evaluation_date: 2026-09-03", 1)),
        ("yaml-unknown-field", yaml_raw + "unknown_field: forbidden\n"),
        ("yaml-type", yaml_raw.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
        ("yaml-authority", yaml_raw.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md", "evaluator_authority: route-a-evaluator", 1)),
        ("yaml-source", yaml_raw.replace("source_commit: 327fc1172cebcdeb17adfd2d8ad12636fbb94f52", "source_commit: 0000000000000000000000000000000000000000", 1)),
        ("yaml-route-b", yaml_raw.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1)),
        ("yaml-a4", yaml_raw.replace("  verdict: A4_FAIL", "  verdict: A4_ROUTE_B_READY", 1)),
        ("yaml-theorem", yaml_raw.replace("theorem_status: PROVABLE_AS_STATED", "theorem_status: NOT_JUSTIFIED", 1)),
        ("yaml-artifact", yaml_raw.replace("results/c351_jackson_evidence.json", "results/other.json", 1)),
        ("yaml-evidence-role", yaml_raw.replace("convention and implementation receipt, not proof of the infinite-state network theorem", "proof by finite enumeration", 1)),
        ("yaml-owner-token", yaml_raw.replace("DOI:10.1287/OPRE.5.4.518", "DOI:mutated", 1)),
        ("yaml-definition", yaml_raw.replace("finite open single-class Jackson network", "closed Jackson network", 1)),
        ("yaml-root-array", "- invalid\n"),
    ]
    attacks.extend((name, json_raw, changed) for name, changed in yaml_changes)
    for name, changed in yaml_changes[5:-1]:
        try:
            attacks.append(("repaired-" + name, repaired_yaml(data, changed), changed))
        except Exception:
            pass
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c351-mutation-") as directory:
        work = Path(directory)
        for index, (name, evidence_raw, evaluation_raw) in enumerate(attacks):
            evidence = work / f"attack-{index}.json"
            evaluation = work / f"attack-{index}.yaml"
            evidence.write_text(evidence_raw)
            evaluation.write_text(evaluation_raw)
            process = subprocess.run([sys.executable, "-B", str(CHECKER),
                "--evidence", str(evidence), "--evaluation", str(evaluation)],
                env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if process.returncode == 0:
                raise AssertionError(f"hostile attack survived: {name}")
            rejected += 1
    print(f"C351 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
