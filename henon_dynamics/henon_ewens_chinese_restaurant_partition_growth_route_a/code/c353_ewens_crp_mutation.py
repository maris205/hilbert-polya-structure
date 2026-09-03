#!/usr/bin/env python3
"""Repaired-hash and strict-parser hostile tests for HCS-C353."""
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
EVIDENCE = ROOT / "results/c353_ewens_crp_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C353/2026-09-03.yaml"
CHECKER = ROOT / "code/c353_ewens_crp_checker.py"


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
        raise RuntimeError("C353 mutation lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    json_raw = EVIDENCE.read_text()
    yaml_raw = EVALUATION.read_text()
    attacks = []
    semantic = [
        (("candidate_id",), "HCS-C000"), (("obstruction_id",), "HEN-O000"),
        (("evaluation_date",), "2099-01-01"), (("fixed_epoch",), 0),
        (("source_commit",), "0" * 40), (("scope_literal",), "EXPANDED"),
        (("evaluator", "authority"), "wrong.md"), (("evaluator", "sha256"), "0" * 64),
        (("route_a_yaml", "relative_path"), "wrong.yaml"),
        (("model", "new_block_probability"), "theta/(theta+n+1)"),
        (("theorem_contract", "eppf"), "wrong EPPF"),
        (("theorem_contract", "laws"), "almost sure equality at finite n"),
        (("collision_boundary", "C215"), "same model"),
        (("nonclaims", 0), "full Poisson-Dirichlet theorem"),
        (("references", 0, "identifier"), "DOI:mutated"),
        (("route_a", "tuple", 0), "A0_STRUCTURAL_ARITHMETIC_ORIGIN"),
        (("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_target_euler_factors"), True),
        (("count_vector_rows", 0, "cycle_multiplicity"), 2),
        (("count_vector_rows", 100, "block_count"), 99),
        (("stirling_rows", 3, "unsigned_stirling_first_kind"), 0),
        (("k_distribution_rows", 8, "probability"), "0"),
        (("bernoulli_rows", 20, "new_block_probability"), "1"),
        (("factorial_moment_rows", 5, "finite_correction"), "0"),
        (("normalization_rows", 2, "normalized_probability_sum"), "2"),
        (("boundary_rows", 3, "theta_one_single_block_probability"), "0"),
        (("enumeration", "finite_evidence_proves_asymptotic_theorem"), True),
    ]
    for index, (path, value) in enumerate(semantic):
        changed = copy.deepcopy(data)
        set_path(changed, path, value)
        attacks.append((f"repaired-semantic-{index}", repair(changed), yaml_raw))
    for section in ("count_vector_rows", "stirling_rows", "k_distribution_rows",
                    "bernoulli_rows", "factorial_moment_rows", "normalization_rows", "boundary_rows"):
        changed = copy.deepcopy(data)
        changed[section][0]["unowned"] = "survive"
        attacks.append((f"nested-extra-{section}", repair(changed), yaml_raw))
        changed = copy.deepcopy(data)
        changed[section].pop(0)
        attacks.append((f"row-omit-{section}", repair(changed), yaml_raw))
        changed = copy.deepcopy(data)
        changed[section].insert(0, copy.deepcopy(changed[section][0]))
        attacks.append((f"row-duplicate-{section}", repair(changed), yaml_raw))
    for key in ("model", "theorem_contract", "route_a", "scope_flags", "enumeration"):
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
        ("yaml-duplicate", yaml_raw + "candidate_id: HCS-C353\n"),
        ("yaml-anchor", yaml_raw.replace("candidate_id: HCS-C353", "candidate_id: &id HCS-C353", 1)),
        ("yaml-alias", "holder: &h HCS-C353\ncandidate_id: *h\n" + yaml_raw),
        ("yaml-merge", "base: &b {x: 1}\nmerged:\n  <<: *b\n" + yaml_raw),
        ("yaml-nonstring-key", "1: forbidden\n" + yaml_raw),
        ("yaml-date-type", yaml_raw.replace("evaluation_date: '2026-09-03'", "evaluation_date: 2026-09-03", 1)),
        ("yaml-source", yaml_raw.replace("source_commit: 327fc1172cebcdeb17adfd2d8ad12636fbb94f52", "source_commit: 0000000000000000000000000000000000000000", 1)),
        ("yaml-route-b", yaml_raw.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1)),
        ("yaml-a0", yaml_raw.replace("verdict: A0_FAIL", "verdict: A0_STRUCTURAL_ARITHMETIC_ORIGIN", 1)),
        ("yaml-extra", yaml_raw + "unknown_field: forbidden\n"),
        ("yaml-root-array", "- invalid\n"),
    ]
    attacks.extend((name, json_raw, raw) for name, raw in yaml_attacks)
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c353-mutation-") as directory:
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
    print(f"C353 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
