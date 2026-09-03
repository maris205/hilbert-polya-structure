#!/usr/bin/env python3
"""Repaired-hash and strict-parser hostile tests for HCS-C341."""
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
EVIDENCE = ROOT / "results/c341_lamplighter_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C341/2026-09-03.yaml"
CHECKER = ROOT / "code/c341_lamplighter_checker.py"


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


def repaired_yaml(data, yaml_raw):
    changed = copy.deepcopy(data)
    semantic = yaml.safe_load(yaml_raw)
    changed["route_a_yaml"]["raw_sha256"] = hashlib.sha256(yaml_raw.encode()).hexdigest()
    changed["route_a_yaml"]["semantic_sha256"] = hashlib.sha256(canonical(semantic)).hexdigest()
    return repair(changed)


def main():
    if sys.flags.optimize:
        raise RuntimeError("C341 mutation lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    json_raw = EVIDENCE.read_text()
    yaml_raw = EVALUATION.read_text()
    attacks = []
    semantic = [
        (("candidate_id",), "HCS-C000"), (("obstruction_id",), "HEN-O000"),
        (("evaluation_date",), "2099-01-01"), (("source_commit",), "0" * 40),
        (("scope_literal",), "EXPANDED"), (("evaluator", "authority"), "route-a-evaluator"),
        (("evaluator", "sha256"), "0" * 64),
        (("route_a_yaml", "relative_path"), "evaluation.yaml"),
        (("route_a_yaml", "raw_sha256"), "0" * 64),
        (("route_a_yaml", "semantic_sha256"), "0" * 64),
        (("model", "switch"), "deterministic toggle"),
        (("theorem_contract", "gap"), "upper bound only"),
        (("collision_boundary", "C171"), "same owner"),
        (("nonclaims", 2), "target Euler factor claimed"),
        (("references", 0, "identifier"), "DOI:mutated"),
        (("route_a", "tuple", 4), "A4_ROUTE_B_READY"),
        (("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_target_euler_factors"), True),
        (("cycle_rows", 0, "gap_formula"), "0"),
        (("block_rows", 0, "charpoly_low_to_high", 0), "999"),
        (("block_rows", 2045, "run_lengths"), [10]),
        (("direct_matrix_rows", 5, "symmetry_failures"), 1),
        (("enumeration", "all_checks_exact"), False),
    ]
    for index, (path, value) in enumerate(semantic):
        changed = copy.deepcopy(data)
        set_path(changed, path, value)
        attacks.append((f"repaired-semantic-{index}", repair(changed), yaml_raw))
    for section in ("cycle_rows", "block_rows", "direct_matrix_rows"):
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
    stale = copy.deepcopy(data)
    stale["candidate_id"] = "HCS-C000"
    attacks.append(("stale-hash-control", json.dumps(stale, sort_keys=True, indent=2) + "\n", yaml_raw))
    attacks.extend([
        ("duplicate-json", json_raw.replace("{\n", '{\n  "schema": "duplicate",\n', 1), yaml_raw),
        ("nonfinite-json", json_raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1), yaml_raw),
        ("json-root-array", "[]\n", yaml_raw),
    ])
    yaml_changes = [
        ("yaml-duplicate", yaml_raw + "candidate_id: HCS-C341\n"),
        ("yaml-anchor", yaml_raw.replace("candidate_id: HCS-C341", "candidate_id: &id HCS-C341", 1)),
        ("yaml-alias", "holder: &h HCS-C341\ncandidate_id: *h\n" + yaml_raw),
        ("yaml-merge", "base: &b {x: 1}\nmerged:\n  <<: *b\n" + yaml_raw),
        ("yaml-nonstring-key", "1: forbidden\n" + yaml_raw),
        ("yaml-implicit-timestamp", yaml_raw.replace("evaluation_date: '2026-09-03'", "evaluation_date: 2026-09-03", 1)),
        ("yaml-unknown-field", yaml_raw + "unknown_field: forbidden\n"),
        ("yaml-type", yaml_raw.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
        ("yaml-authority", yaml_raw.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md", "evaluator_authority: route-a-evaluator", 1)),
        ("yaml-route-b", yaml_raw.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1)),
        ("yaml-a4", yaml_raw.replace("  verdict: A4_FORMAL_HINT", "  verdict: A4_ROUTE_B_READY", 1)),
        ("yaml-theorem", yaml_raw.replace("theorem_status: PROVABLE_AS_STATED", "theorem_status: NOT_JUSTIFIED", 1)),
        ("yaml-artifact", yaml_raw.replace("results/c341_lamplighter_evidence.json", "results/other.json", 1)),
        ("yaml-root-array", "- invalid\n"),
    ]
    attacks.extend((name, json_raw, changed) for name, changed in yaml_changes)
    for name, changed in yaml_changes[5:13]:
        try:
            attacks.append(("repaired-" + name, repaired_yaml(data, changed), changed))
        except Exception:
            pass
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c341-mutation-") as directory:
        directory = Path(directory)
        for index, (name, evidence_raw, evaluation_raw) in enumerate(attacks):
            evidence = directory / f"attack-{index}.json"
            evaluation = directory / f"attack-{index}.yaml"
            evidence.write_text(evidence_raw)
            evaluation.write_text(evaluation_raw)
            process = subprocess.run(
                [sys.executable, "-B", str(CHECKER), "--evidence", str(evidence),
                 "--evaluation", str(evaluation)], env=environment,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if process.returncode == 0:
                raise AssertionError(f"hostile attack survived: {name}")
            rejected += 1
    print(f"C341 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
