#!/usr/bin/env python3
"""Repaired-hash and strict-parser hostile tests for HCS-C358."""
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
EVIDENCE = ROOT / "results/c358_may_leonard_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C358/2026-09-03.yaml"
CHECKER = ROOT / "code/c358_may_leonard_checker.py"


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
        raise RuntimeError("C358 mutation lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    original_json = EVIDENCE.read_text()
    original_yaml = EVALUATION.read_text()
    attacks = []
    mutations = [
        (("candidate_id",), "HCS-C000"), (("obstruction_id",), "HEN-O000"),
        (("evaluation_date",), "2099-01-01"), (("source_commit",), "0"*40),
        (("fixed_epoch",), 0), (("scope_literal",), "EXPANDED"),
        (("evaluator", "authority"), "wrong.md"), (("evaluator", "sha256"), "0"*64),
        (("route_a_yaml", "relative_path"), "wrong.yaml"),
        (("model", "equations", 0), "x'=0"),
        (("theorem_contract", "source_identity"), "wrong sign"),
        (("theorem_contract", "supercritical"), "all points converge to coexistence"),
        (("collision_boundary", "C211"), "same owner"),
        (("nonclaims", 0), "founder-control chamber proved"),
        (("references", 0, "identifier"), "DOI:mutated"),
        (("parameter_rows", 0, "phase"), "heteroclinic"),
        (("parameter_rows", 2, "tangent_real_part"), "1"),
        (("invariant_rows", 0, "dlog_R_formula"), "0"),
        (("invariant_rows", 1, "dS_formula"), "0"),
        (("critical_rows", 0, "product_derivative"), "1"),
        (("critical_rows", 1, "quartic_formula"), "0"),
        (("logistic_rows", 0, "logistic_rhs"), "0"),
        (("edge_rows", 0, "source"), "E2"),
        (("boundary_rows", 1, "classification"), "all interior points"),
        (("section_hashes", "critical_rows"), "0"*64),
        (("enumeration", "finite_evidence_proves_global_theorem"), True),
        (("route_a", "tuple", 0), "A0_ANALYTIC_ARITHMETIC_ORIGIN"),
        (("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_target_euler_factors"), True),
        (("scope_flags", "claims_hilbert_polya_operator"), True),
    ]
    for index, (path, value) in enumerate(mutations):
        changed = copy.deepcopy(data)
        set_path(changed, path, value)
        attacks.append((f"repaired-semantic-{index}", repair(changed), original_yaml))
    for section in ("parameter_rows", "invariant_rows", "critical_rows", "logistic_rows",
                    "edge_rows", "boundary_rows"):
        changed = copy.deepcopy(data)
        changed[section].pop(0)
        attacks.append((f"omit-{section}", repair(changed), original_yaml))
        changed = copy.deepcopy(data)
        changed[section].insert(0, copy.deepcopy(changed[section][0]))
        attacks.append((f"duplicate-{section}", repair(changed), original_yaml))
        changed = copy.deepcopy(data)
        changed[section][0]["unknown"] = "survive"
        attacks.append((f"nested-extra-{section}", repair(changed), original_yaml))
    missing = copy.deepcopy(data)
    missing.pop("theorem_contract")
    attacks.append(("missing-top", repair(missing), original_yaml))
    extra = copy.deepcopy(data)
    extra["unknown"] = 1
    attacks.append(("extra-top", repair(extra), original_yaml))
    stale = copy.deepcopy(data)
    stale["candidate_id"] = "HCS-C000"
    attacks.append(("stale-payload-hash", json.dumps(stale, sort_keys=True, indent=2)+"\n", original_yaml))
    attacks.extend([
        ("duplicate-json", original_json.replace("{\n", '{\n  "schema": "duplicate",\n', 1), original_yaml),
        ("nonfinite-json", original_json.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1), original_yaml),
        ("json-array", "[]\n", original_yaml),
    ])
    yaml_mutations = [
        ("yaml-duplicate", original_yaml + "candidate_id: HCS-C358\n"),
        ("yaml-anchor", original_yaml.replace("candidate_id: HCS-C358", "candidate_id: &id HCS-C358", 1)),
        ("yaml-alias", "holder: &h HCS-C358\ncandidate_id: *h\n" + original_yaml),
        ("yaml-merge", "base: &b {x: 1}\nmerged:\n  <<: *b\n" + original_yaml),
        ("yaml-nonstring", "1: forbidden\n" + original_yaml),
        ("yaml-date", original_yaml.replace("evaluation_date: '2026-09-03'", "evaluation_date: 2026-09-03", 1)),
        ("yaml-unknown", original_yaml + "unknown_field: forbidden\n"),
        ("yaml-type", original_yaml.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
        ("yaml-source", original_yaml.replace("source_commit: 140c8714b74de666d56f441ddfb712026955901a", "source_commit: 0000000000000000000000000000000000000000", 1)),
        ("yaml-a1", original_yaml.replace("  verdict: A1_WEAK", "  verdict: A1_PASS_ANALYTIC", 1)),
        ("yaml-route-b", original_yaml.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1)),
        ("yaml-artifact", original_yaml.replace("results/c358_may_leonard_evidence.json", "results/other.json", 1)),
    ]
    attacks.extend((name, original_json, raw) for name, raw in yaml_mutations)
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c358-mutation-") as directory:
        work = Path(directory)
        for index, (name, json_raw, yaml_raw) in enumerate(attacks):
            evidence = work / f"attack-{index}.json"
            evaluation = work / f"attack-{index}.yaml"
            evidence.write_text(json_raw)
            evaluation.write_text(yaml_raw)
            process = subprocess.run([sys.executable, "-B", str(CHECKER),
                                      "--evidence", str(evidence), "--evaluation", str(evaluation)],
                                     env=environment, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT, text=True)
            if process.returncode == 0:
                raise AssertionError(f"hostile attack survived: {name}")
            rejected += 1
    print(f"C358 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
