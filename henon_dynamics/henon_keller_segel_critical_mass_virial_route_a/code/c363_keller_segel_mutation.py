#!/usr/bin/env python3
"""Repaired-hash and strict-parser hostile tests for HCS-C363."""
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
EVIDENCE = ROOT / "results/c363_keller_segel_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C363/2026-09-04.yaml"
CHECKER = ROOT / "code/c363_keller_segel_checker.py"


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def repair(data):
    changed = copy.deepcopy(data)
    changed.pop("payload_sha256", None)
    changed["payload_sha256"] = hashlib.sha256(canonical(changed)).hexdigest()
    return json.dumps(changed, sort_keys=True, indent=2, ensure_ascii=False)+"\n"


def set_path(data, path, value):
    cursor = data
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value


def main():
    if sys.flags.optimize:
        raise RuntimeError("C363 mutation lane refuses optimized Python")
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
        (("model", "pde"), "rho_t=0"),
        (("model", "classical_domain"), "unqualified smooth density"),
        (("theorem_contract", "hypotheses"), "no moment or positivity assumptions"),
        (("theorem_contract", "virial"), "I'=0"),
        (("collision_boundary", "C231"), "same owner"),
        (("nonclaims", 0), "weak solutions proved"),
        (("references", 0, "identifier"), "DOI:mutated"),
        (("virial_rows", 0, "virial_slope_over_pi"), "0"),
        (("scaling_rows", 0, "energy_shift_sign"), "zero"),
        (("profile_rows", 0, "poisson_residual"), "1"),
        (("radial_rows", 0, "stationary_radial_residual"), "1"),
        (("boundary_rows", 1, "classification"), "convergence proved"),
        (("section_hashes", "virial_rows"), "0"*64),
        (("enumeration", "finite_evidence_proves_pde_theorem"), True),
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
    sections = ("virial_rows", "scaling_rows", "profile_rows", "radial_rows", "boundary_rows")
    for section in sections:
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
        ("nonfinite-json", original_json.replace('"fixed_epoch": 1788480000', '"fixed_epoch": NaN', 1), original_yaml),
        ("json-array", "[]\n", original_yaml),
    ])
    yaml_mutations = [
        ("yaml-duplicate", original_yaml+"candidate_id: HCS-C363\n"),
        ("yaml-anchor", original_yaml.replace("candidate_id: HCS-C363", "candidate_id: &id HCS-C363", 1)),
        ("yaml-alias", "holder: &h HCS-C363\ncandidate_id: *h\n"+original_yaml),
        ("yaml-merge", "base: &b {x: 1}\nmerged:\n  <<: *b\n"+original_yaml),
        ("yaml-nonstring", "1: forbidden\n"+original_yaml),
        ("yaml-date", original_yaml.replace("evaluation_date: '2026-09-04'", "evaluation_date: 2026-09-04", 1)),
        ("yaml-unknown", original_yaml+"unknown_field: forbidden\n"),
        ("yaml-type", original_yaml.replace("fixed_epoch: 1788480000", 'fixed_epoch: "1788480000"', 1)),
        ("yaml-source", original_yaml.replace("source_commit: 05ca5f96b2c69a6ad6ba153d1084df750d7722c0", "source_commit: 0000000000000000000000000000000000000000", 1)),
        ("yaml-a1", original_yaml.replace("  verdict: A1_FAIL", "  verdict: A1_PASS_ANALYTIC", 1)),
        ("yaml-route-b", original_yaml.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1)),
        ("yaml-artifact", original_yaml.replace("results/c363_keller_segel_evidence.json", "results/other.json", 1)),
    ]
    attacks.extend((name, original_json, raw) for name, raw in yaml_mutations)
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c363-mutation-") as directory:
        work = Path(directory)
        for index, (name, json_raw, yaml_raw) in enumerate(attacks):
            evidence = work/f"attack-{index}.json"
            evaluation = work/f"attack-{index}.yaml"
            evidence.write_text(json_raw)
            evaluation.write_text(yaml_raw)
            process = subprocess.run([sys.executable, "-B", str(CHECKER),
                                      "--evidence", str(evidence), "--evaluation", str(evaluation)],
                                     env=environment, stdout=subprocess.PIPE,
                                     stderr=subprocess.STDOUT, text=True)
            if process.returncode == 0:
                raise AssertionError(f"hostile attack survived: {name}")
            rejected += 1
    print(f"C363 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
