#!/usr/bin/env python3
"""Hostile mutation suite for C294 JSON and Route-A YAML contracts."""
from __future__ import annotations

import copy
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "code/c294_three_disk_checker.py"
EVIDENCE = ROOT / "results/c294_three_disk_evidence.json"
YAML_PATH = ROOT / "evaluations/route_a/HCS-C294/2026-09-02.yaml"


def payload_hash(data: dict) -> str:
    import hashlib
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def set_path(data, path, value):
    cursor = data
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value


def rejected(evidence_text: str, yaml_text: str) -> bool:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c294-mutation-") as tmp:
        ep = Path(tmp) / "evidence.json"
        yp = Path(tmp) / "route.yaml"
        ep.write_text(evidence_text)
        yp.write_text(yaml_text)
        run = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(ep), "--yaml", str(yp)], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return run.returncode != 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    yaml_text = YAML_PATH.read_text()
    mutations = []
    semantic = [
        (("schema",), "wrong"),
        (("candidate_id",), "HCS-C999"),
        (("obstruction_id",), "HEN-O999"),
        (("source_commit",), "0" * 40),
        (("fixed_epoch",), 0),
        (("scope_literal",), "ALLOW_BAD_EULER"),
        (("evaluator", "sha256"), "0" * 64),
        (("model", "clock"), "geometric length"),
        (("model", "parameter_chamber"), "d>2r"),
        (("theorem_contract", "coding"), "cyclic classes correspond directly to geometric rays"),
        (("theorem_contract", "iterate_convention"), "traversal multiplicity is discarded"),
        (("theorem_contract", "fixed_count"), "3^n"),
        (("theorem_contract", "collision_zeta"), "1/(1-3z)"),
        (("proof_contract", "uniqueness"), "finite search"),
        (("proof_contract", "finite_role"), "proof of coding"),
        (("enumeration", "count_rows", 1, "fixed_rooted_words"), 7),
        (("enumeration", "count_rows", 0, "n"), True),
        (("enumeration", "count_rows", 0, "fixed_rooted_words"), False),
        (("enumeration", "count_rows", 5, "primitive_orbits"), 999),
        (("enumeration", "direct_rows", 0, "n"), True),
        (("enumeration", "direct_rows", 9, "fixed_rooted_words"), 999),
        (("enumeration", "direct_rows", 7, "reversal_symmetric_rooted_words"), -1),
        (("enumeration", "zeta_coefficients_0_to_16", 0), True),
        (("enumeration", "zeta_coefficients_0_to_16", 4), 8),
        (("enumeration", "optical_rows", 0, "determinant"), "2"),
        (("enumeration", "optical_rows", 10, "trace"), "2"),
        (("enumeration", "geometry_rows", 0, "no_eclipse"), False),
        (("enumeration", "geometry_rows", 0, "pair_gap"), True),
        (("enumeration", "optical_rows", 0, "determinant"), True),
        (("enumeration", "symmetric_orbits", 0, "monodromy_trace"), "13"),
        (("route_a", "tuple", 1), "A1_WEAK"),
        (("route_a", "overall"), "ROUTE_A_STRONG_CANDIDATE"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("route_a", "route_b_invocation_allowed"), 0),
        (("scope_flags", "claims_target_euler_factors"), True),
        (("nonclaims", 0), "We claim a target Euler factor and root number."),
        (("references", 2, "identifier"), "fake"),
    ]
    for index, (path, value) in enumerate(semantic):
        mutant = copy.deepcopy(base)
        set_path(mutant, path, value)
        mutant["payload_sha256"] = payload_hash(mutant)
        mutations.append((f"json-semantic-{index}", json.dumps(mutant, sort_keys=True, indent=2) + "\n", yaml_text))
    missing = copy.deepcopy(base)
    missing.pop("proof_contract")
    missing["payload_sha256"] = payload_hash(missing)
    mutations.append(("json-missing", json.dumps(missing, sort_keys=True, indent=2) + "\n", yaml_text))
    unknown = copy.deepcopy(base)
    unknown["unknown"] = 1
    unknown["payload_sha256"] = payload_hash(unknown)
    mutations.append(("json-unknown", json.dumps(unknown, sort_keys=True, indent=2) + "\n", yaml_text))
    raw = EVIDENCE.read_text()
    mutations.append(("json-duplicate", raw.replace('  "candidate_id": "HCS-C294",', '  "candidate_id": "HCS-C294",\n  "candidate_id": "HCS-C294",', 1), yaml_text))

    yaml_replacements = [
        ("candidate_id: HCS-C294", "candidate_id: HCS-C999"),
        ("obstruction_id: HEN-O278", "obstruction_id: HEN-O999"),
        ("scope_literal: NO_BAD_EULER_OR_ROOT_NUMBER", "scope_literal: BAD"),
        ("overall_verdict: ROUTE_A_REJECTED", "overall_verdict: ROUTE_A_STRONG_CANDIDATE"),
        ("route_b_invocation_allowed: false", "route_b_invocation_allowed: true"),
        ("verdict: A1_PASS_ANALYTIC", "verdict: A1_WEAK"),
        ("verdict: A4_NATURAL_QUANTIZATION", "verdict: A4_ROUTE_B_READY"),
        ("fixed_epoch: 1788307200", "fixed_epoch: '1788307200'"),
        ("theorem_status: PROVABLE_AS_STATED", "theorem_status: HEURISTIC"),
        ("route_b_invocation_allowed: false", "route_b_invocation_allowed: 0"),
        ("  claims_root_number: false", "  claims_root_number: 0"),
        ("  evidence_status: exact negative classification", "  evidence_status: true"),
        ("  strongest_evidence: every primitive cyclic class has one isolated hyperbolic primitive ray, while word powers encode positive traversal multiplicity", "  strongest_evidence: altered"),
        ("  artifacts: [THEOREM_PACKAGE.md, paper/main.pdf, results/c294_three_disk_evidence.json]", "  artifacts: [paper/missing.pdf]"),
        ("a1:\n  verdict: A1_PASS_ANALYTIC", "a1:\n  alien_nested_key: escaped\n  verdict: A1_PASS_ANALYTIC"),
    ]
    for index, (old, new) in enumerate(yaml_replacements):
        assert old in yaml_text
        mutations.append((f"yaml-semantic-{index}", raw, yaml_text.replace(old, new, 1)))
    mutations.append(("yaml-duplicate", raw, yaml_text + "candidate_id: HCS-C294\n"))
    mutations.append(("yaml-unknown", raw, yaml_text + "unknown_top_key: 1\n"))
    mutations.append(("yaml-missing", raw, yaml_text.replace("obstruction_id: HEN-O278\n", "", 1)))

    passed = 0
    for name, evidence_text, candidate_yaml in mutations:
        if not rejected(evidence_text, candidate_yaml):
            raise AssertionError(f"mutation survived: {name}")
        passed += 1
    print(f"C294 hostile mutation suite: PASS {passed}/{len(mutations)}")


if __name__ == "__main__":
    main()
