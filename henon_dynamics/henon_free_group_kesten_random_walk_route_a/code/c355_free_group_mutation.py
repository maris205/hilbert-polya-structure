#!/usr/bin/env python3
"""Repaired-hash and strict-parser hostile tests for HCS-C355."""
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
EVIDENCE = ROOT / "results/c355_free_group_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C355/2026-09-03.yaml"
CHECKER = ROOT / "code/c355_free_group_checker.py"


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


def main():
    if sys.flags.optimize:
        raise RuntimeError("C355 mutation lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    json_raw = EVIDENCE.read_text()
    yaml_raw = EVALUATION.read_text()
    attacks = []
    semantic = [
        (("schema",), "wrong"), (("candidate_id",), "HCS-C000"),
        (("obstruction_id",), "HEN-O000"), (("evaluation_date",), "2099-01-01"),
        (("fixed_epoch",), 0), (("source_commit",), "0" * 40),
        (("scope_literal",), "EXPANDED"), (("evaluator", "authority"), "wrong.md"),
        (("evaluator", "sha256"), "0" * 64),
        (("route_a_yaml", "relative_path"), "wrong.yaml"),
        (("route_a_yaml", "raw_sha256"), "0" * 64),
        (("model", "degree"), "D=d"), (("model", "step_law"), "nonuniform"),
        (("theorem_contract", "spectrum"), "point spectrum"),
        (("theorem_contract", "returns"), "wrong formula"),
        (("theorem_contract", "escape"), "speed one"),
        (("collision_boundary", "C341"), "same model"),
        (("nonclaims", 2), "closed words are arithmetic primitive orbits"),
        (("references", 0, "identifier"), "DOI:mutated"),
        (("route_a", "tuple", 0), "A0_STRUCTURAL_ARITHMETIC_ORIGIN"),
        (("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_target_euler_factors"), True),
        (("radial_dp_rows", 10, "word_count"), -1),
        (("return_rows", 5, "closed_word_count"), 0),
        (("first_return_rows", 12, "catalan"), 0),
        (("renewal_rows", 3, "renewal_convolution"), 0),
        (("parameter_rows", 0, "escape_speed"), "1"),
        (("rank_one_boundary_rows", 4, "return_word_count"), 0),
        (("enumeration", "finite_evidence_proves_infinite_tree_theorems"), True),
    ]
    for index, (path, value) in enumerate(semantic):
        changed = copy.deepcopy(data)
        set_path(changed, path, value)
        attacks.append((f"repaired-semantic-{index}", repair(changed), yaml_raw))
    sections = ("radial_dp_rows", "return_rows", "first_return_rows", "renewal_rows",
                "parameter_rows", "rank_one_boundary_rows")
    for section in sections:
        changed = copy.deepcopy(data)
        changed[section][0]["unowned"] = "survive"
        attacks.append((f"nested-extra-{section}", repair(changed), yaml_raw))
        changed = copy.deepcopy(data)
        changed[section].pop(0)
        attacks.append((f"row-omit-{section}", repair(changed), yaml_raw))
        changed = copy.deepcopy(data)
        changed[section].insert(0, copy.deepcopy(changed[section][0]))
        attacks.append((f"row-duplicate-{section}", repair(changed), yaml_raw))
    for key in ("model", "theorem_contract", "finite_grid", "collision_boundary",
                "nonclaims", "references", "route_a", "scope_flags", "enumeration"):
        changed = copy.deepcopy(data)
        changed.pop(key)
        attacks.append((f"missing-{key}", repair(changed), yaml_raw))
    stale = copy.deepcopy(data)
    stale["candidate_id"] = "HCS-C000"
    attacks.extend([
        ("stale-hash", json.dumps(stale, sort_keys=True, indent=2) + "\n", yaml_raw),
        ("duplicate-json", json_raw.replace("{\n", '{\n  "schema": "duplicate",\n', 1), yaml_raw),
        ("nonfinite-json", json_raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1), yaml_raw),
        ("json-root-array", "[]\n", yaml_raw),
    ])
    yaml_attacks = [
        ("yaml-duplicate", yaml_raw + "candidate_id: HCS-C355\n"),
        ("yaml-anchor", yaml_raw.replace("candidate_id: HCS-C355", "candidate_id: &id HCS-C355", 1)),
        ("yaml-alias", "holder: &h HCS-C355\ncandidate_id: *h\n" + yaml_raw),
        ("yaml-merge", "base: &b {x: 1}\nmerged:\n  <<: *b\n" + yaml_raw),
        ("yaml-nonstring-key", "1: forbidden\n" + yaml_raw),
        ("yaml-implicit-timestamp", yaml_raw.replace("evaluation_date: '2026-09-03'", "evaluation_date: 2026-09-03", 1)),
        ("yaml-source", yaml_raw.replace("source_commit: 140c8714b74de666d56f441ddfb712026955901a",
                                         "source_commit: 0000000000000000000000000000000000000000", 1)),
        ("yaml-epoch-type", yaml_raw.replace("fixed_epoch: 1788393600", "fixed_epoch: '1788393600'", 1)),
        ("yaml-route-b", yaml_raw.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1)),
        ("yaml-a0", yaml_raw.replace("verdict: A0_FAIL", "verdict: A0_STRUCTURAL_ARITHMETIC_ORIGIN", 1)),
        ("yaml-a4-status", yaml_raw.replace("evidence_status: PROVED\n  strongest_evidence: P is", "evidence_status: STOP_SCOPED\n  strongest_evidence: P is", 1)),
        ("yaml-extra", yaml_raw + "unknown_field: forbidden\n"),
        ("yaml-root-array", "- invalid\n"),
    ]
    attacks.extend((name, json_raw, raw) for name, raw in yaml_attacks)
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c355-mutation-") as directory:
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
    print(f"C355 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
