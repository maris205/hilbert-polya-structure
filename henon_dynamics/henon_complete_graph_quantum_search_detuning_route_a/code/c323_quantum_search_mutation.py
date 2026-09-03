#!/usr/bin/env python3
"""Repaired-hash and parser attacks for HCS-C323."""
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
EVIDENCE = ROOT / "results/c323_quantum_search_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C323/2026-09-03.yaml"
CHECKER = ROOT / "code/c323_quantum_search_checker.py"


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def set_path(data, path, value):
    cursor = data
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C323 mutation lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    json_raw = EVIDENCE.read_text()
    yaml_raw = EVALUATION.read_text()
    attacks = []
    semantic = [
        (("candidate_id",), "HCS-C000"),
        (("obstruction_id",), "HEN-O000"),
        (("source_commit",), "0" * 40),
        (("scope_literal",), "EXPANDED"),
        (("evaluator", "version"), "9.9.9"),
        (("model", "hamiltonian"), "H=+g|s><s|-P_W"),
        (("theorem_contract", "perfect_search"), "perfect for every g"),
        (("references", 0, "identifier"), "10.0000/fake"),
        (("collision_boundary", "C171"), "collision erased"),
        (("nonclaims", 1), "target spectrum claimed"),
        (("route_a", "tuple", 4), "A4_ROUTE_B_READY"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_hilbert_polya_operator"), True),
        (("parameter_grid", "g", 3), "5/4"),
        (("interior_rows", 0, "omega_squared"), "0"),
        (("interior_rows", 0, "bright_trace"), "0"),
        (("interior_rows", 0, "marked_dark_multiplicity"), 1),
        (("interior_rows", 0, "success_maximum"), "1"),
        (("interior_rows", 0, "search_oscillation_nonconstant"), True),
        (("interior_rows", 3, "resonant"), False),
        (("interior_rows", 3, "success_maximum_defect"), "1/2"),
        (("critical_window_rows", 0, "g"), "1"),
        (("critical_window_rows", 0, "limit_success_maximum"), "1.0"),
        (("boundary_rows", 0, "success_probability"), "1"),
        (("boundary_rows", 1, "orthogonal_multiplicity"), -1),
        (("enumeration", "interior_rows"), 0),
        (("enumeration", "audited_leaf_count"), 0),
    ]
    for path, value in semantic:
        mutated = copy.deepcopy(data)
        set_path(mutated, path, value)
        mutated["payload_sha256"] = payload_hash(mutated)
        attacks.append(("semantic", json.dumps(mutated, sort_keys=True, indent=2) + "\n", yaml_raw))

    extra = copy.deepcopy(data)
    extra["interior_rows"][0]["unlocked"] = "survive?"
    extra["payload_sha256"] = payload_hash(extra)
    attacks.append(("extra-row-key", json.dumps(extra, sort_keys=True, indent=2) + "\n", yaml_raw))
    missing = copy.deepcopy(data)
    del missing["model"]
    missing["payload_sha256"] = payload_hash(missing)
    attacks.append(("missing-top-key", json.dumps(missing, sort_keys=True, indent=2) + "\n", yaml_raw))
    attacks.extend(
        [
            ("duplicate-json", json_raw.replace("{\n", '{\n  "schema": "duplicate",\n', 1), yaml_raw),
            ("nan-json", json_raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1), yaml_raw),
            ("json-root-array", "[]\n", yaml_raw),
        ]
    )
    yaml_attacks = [
        ("yaml-duplicate", yaml_raw + "candidate_id: HCS-C323\n"),
        ("yaml-anchor", yaml_raw.replace("candidate_id: HCS-C323", "candidate_id: &owner HCS-C323", 1)),
        ("yaml-source", yaml_raw.replace("source_commit: 1ccbfe2d759fe007c6b53c9646e1ab031878b34a", "source_commit: 0000000000000000000000000000000000000000", 1)),
        (
            "yaml-authority-rewrite",
            yaml_raw.replace(
                "evaluator_authority: flow_systems/skills/route-a-evaluator.md",
                "evaluator_authority: route-a-evaluator",
                1,
            ),
        ),
        (
            "yaml-authority-delete",
            yaml_raw.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md\n", "", 1),
        ),
        (
            "yaml-evidence-status-rewrite",
            yaml_raw.replace("  evidence_status: STOP_SCOPED", "  evidence_status: PROVED", 1),
        ),
        ("yaml-evidence-status-delete", yaml_raw.replace("  evidence_status: PROVED\n", "", 1)),
        ("yaml-root-array", "- invalid\n"),
        ("yaml-equivalent-whitespace", yaml_raw + "\n"),
    ]
    attacks.extend((name, json_raw, mutated_yaml) for name, mutated_yaml in yaml_attacks)

    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c323-mutation-") as directory:
        directory = Path(directory)
        for index, (name, raw_json, raw_yaml) in enumerate(attacks):
            evidence = directory / f"attack-{index}.json"
            evaluation = directory / f"attack-{index}.yaml"
            evidence.write_text(raw_json)
            evaluation.write_text(raw_yaml)
            process = subprocess.run(
                [sys.executable, "-B", str(CHECKER), "--evidence", str(evidence), "--evaluation", str(evaluation)],
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            if process.returncode == 0:
                raise AssertionError(f"hostile attack survived: {name}-{index}")
            rejected += 1
    print(f"C323 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
