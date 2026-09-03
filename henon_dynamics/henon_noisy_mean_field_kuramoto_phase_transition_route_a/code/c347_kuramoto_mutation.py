#!/usr/bin/env python3
"""Repaired-hash and strict-parser hostile tests for HCS-C347."""
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
EVIDENCE = ROOT / "results/c347_kuramoto_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C347/2026-09-03.yaml"
CHECKER = ROOT / "code/c347_kuramoto_checker.py"


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
        raise RuntimeError("C347 mutation lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    json_raw = EVIDENCE.read_text()
    yaml_raw = EVALUATION.read_text()
    attacks = []
    semantic = [
        (("candidate_id",), "HCS-C000"), (("obstruction_id",), "HEN-O000"),
        (("evaluation_date",), "2099-01-01"), (("source_commit",), "0" * 40),
        (("scope_literal",), "EXPANDED"), (("evaluator", "authority"), "wrong.md"),
        (("evaluator", "sha256"), "0" * 64),
        (("route_a_yaml", "relative_path"), "evaluation.yaml"),
        (("model", "parameters"), "D>=0"), (("model", "pde"), "sign reversed"),
        (("theorem_contract", "transition"), "threshold shifted"),
        (("theorem_contract", "linearization"), "wrong spectrum"),
        (("collision_boundary", "C322"), "same owner"),
        (("nonclaims", 0), "global convergence claimed"),
        (("references", 0, "identifier"), "DOI:mutated"),
        (("route_a", "tuple", 0), "A0_STRUCTURAL_ARITHMETIC_ORIGIN"),
        (("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_target_euler_factors"), True),
        (("bessel_coefficient_rows", 0, "coefficient_ratio"), "0"),
        (("formal_quotient_rows", 1, "coefficient"), "0"),
        (("tail_bracket_rows", 0, "strict_interval"), False),
        (("self_consistency_root_rows", 0, "root_count_analytic"), 2),
        (("fourier_rows", 10, "linearized_eigenvalue"), "99"),
        (("critical_expansion", "r_squared", 1), "5/6"),
        (("enumeration", "finite_evidence_proves_continuum_theorem"), True),
    ]
    for index, (path, value) in enumerate(semantic):
        changed = copy.deepcopy(data)
        set_path(changed, path, value)
        attacks.append((f"repaired-semantic-{index}", repair(changed), yaml_raw))
    for section in ("bessel_coefficient_rows", "formal_quotient_rows", "tail_bracket_rows",
                    "self_consistency_root_rows", "fourier_rows"):
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
        ("yaml-duplicate", yaml_raw + "candidate_id: HCS-C347\n"),
        ("yaml-anchor", yaml_raw.replace("candidate_id: HCS-C347", "candidate_id: &id HCS-C347", 1)),
        ("yaml-alias", "holder: &h HCS-C347\ncandidate_id: *h\n" + yaml_raw),
        ("yaml-merge", "base: &b {x: 1}\nmerged:\n  <<: *b\n" + yaml_raw),
        ("yaml-nonstring-key", "1: forbidden\n" + yaml_raw),
        ("yaml-implicit-timestamp", yaml_raw.replace("evaluation_date: '2026-09-03'", "evaluation_date: 2026-09-03", 1)),
        ("yaml-unknown-field", yaml_raw + "unknown_field: forbidden\n"),
        ("yaml-type", yaml_raw.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
        ("yaml-authority", yaml_raw.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md", "evaluator_authority: wrong.md", 1)),
        ("yaml-source", yaml_raw.replace("source_commit: 1af63b945e19b5f94ac1cb76f93af5ac66d3d562", "source_commit: 0000000000000000000000000000000000000000", 1)),
        ("yaml-route-b", yaml_raw.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1)),
        ("yaml-a4", yaml_raw.replace("  verdict: A4_FAIL", "  verdict: A4_FORMAL_HINT", 1)),
        ("yaml-theorem", yaml_raw.replace("theorem_status: PROVABLE_AS_STATED", "theorem_status: NOT_JUSTIFIED", 1)),
        ("yaml-artifact", yaml_raw.replace("results/c347_kuramoto_evidence.json", "results/other.json", 1)),
        ("yaml-evidence-role", yaml_raw.replace("Bessel series, certified root bracket, Fourier, parser, and implementation receipt only; analytic arguments prove the continuum stationary theorem", "enumeration proves PDE", 1)),
        ("yaml-root-array", "- invalid\n"),
    ]
    attacks.extend((name, json_raw, raw) for name, raw in yaml_changes)
    for name, raw in yaml_changes[5:15]:
        try:
            attacks.append(("repaired-" + name, repaired_yaml(data, raw), raw))
        except Exception:
            pass
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c347-mutation-") as directory:
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
    print(f"C347 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
