#!/usr/bin/env python3
"""Repaired-hash, parser, and evaluator-lock attacks for HCS-C327."""
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
EVIDENCE = ROOT / "results/c327_kronig_penney_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C327/2026-09-03.yaml"
CHECKER = ROOT / "code/c327_kronig_penney_checker.py"


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def set_path(data, path, value):
    cursor = data
    for key in path[:-1]:
        cursor = cursor[key]
    cursor[path[-1]] = value


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C327 mutation lane refuses optimized Python")
    data = json.loads(EVIDENCE.read_text())
    json_raw = EVIDENCE.read_text()
    yaml_raw = EVALUATION.read_text()
    attacks = []
    semantic = [
        (("candidate_id",), "HCS-C000"),
        (("obstruction_id",), "HEN-O000"),
        (("source_commit",), "0" * 40),
        (("scope_literal",), "EXPANDED"),
        (("evaluator", "authority"), "route-a-evaluator"),
        (("evaluator", "version"), "9.9.9"),
        (("model", "operator"), "H=+d^2/dx^2"),
        (("model", "jump"), "wrong jump sign"),
        (("theorem_contract", "floquet_spectrum"), "point spectrum allowed"),
        (("theorem_contract", "negative_atlas"), "threshold ga=-2"),
        (("references", 0, "identifier"), "10.0000/fake"),
        (("collision_boundary", "C288"), "same owner"),
        (("nonclaims", 1), "transfer determinant is an Euler factor"),
        (("route_a", "tuple", 4), "A4_ROUTE_B_READY"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("scope_flags", "claims_target_zero_match"), True),
        (("parameter_grid", "bragg_n"), "1..12"),
        (("negative_atlas_rows", 0, "zero_location"), "BAND_INTERIOR"),
        (("negative_atlas_rows", 0, "y_plus"), "1.0"),
        (("negative_atlas_rows", 2, "negative_gap_to_zero"), True),
        (("low_edge_rows", 2, "kind"), "BAND_INTERIOR"),
        (("low_edge_rows", 3, "positive_edge_x"), "2.0"),
        (("bragg_rows", 0, "positive_axis_gap_portion"), "0.0"),
        (("bragg_rows", 24, "side"), "RIGHT"),
        (("bragg_rows", 215, "scaled_gap_width"), "0.0"),
        (("bragg_rows", 215, "gap_open"), False),
        (("transfer_rows", 0, "determinant"), "0.0"),
        (("transfer_rows", 1, "half_trace"), "0.0"),
        (("transfer_rows", 2, "in_spectrum"), True),
        (("ids_dos_rows", 0, "band_index"), 4),
        (("ids_dos_rows", 0, "unwrapped_phase"), "0.0"),
        (("ids_dos_rows", 69, "dos_per_unit_length_at_a_one"), "0.0"),
        (("enumeration", "bragg_rows"), 0),
        (("enumeration", "audited_leaf_count"), 0),
    ]
    for path, value in semantic:
        mutated = copy.deepcopy(data)
        set_path(mutated, path, value)
        mutated["payload_sha256"] = payload_hash(mutated)
        attacks.append(("semantic", json.dumps(mutated, sort_keys=True, indent=2) + "\n", yaml_raw))

    extra = copy.deepcopy(data)
    extra["bragg_rows"][0]["unowned"] = "survive?"
    extra["payload_sha256"] = payload_hash(extra)
    attacks.append(("extra-row-key", json.dumps(extra, sort_keys=True, indent=2) + "\n", yaml_raw))
    missing = copy.deepcopy(data)
    del missing["theorem_contract"]
    missing["payload_sha256"] = payload_hash(missing)
    attacks.append(("missing-top-key", json.dumps(missing, sort_keys=True, indent=2) + "\n", yaml_raw))
    attacks.extend([
        ("duplicate-json", json_raw.replace("{\n", '{\n  "schema": "duplicate",\n', 1), yaml_raw),
        ("nan-json", json_raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1), yaml_raw),
        ("json-root-array", "[]\n", yaml_raw),
    ])
    yaml_attacks = [
        ("yaml-duplicate", yaml_raw + "candidate_id: HCS-C327\n"),
        ("yaml-anchor", yaml_raw.replace("candidate_id: HCS-C327", "candidate_id: &owner HCS-C327", 1)),
        ("yaml-source", yaml_raw.replace(
            "source_commit: 1aba1f6fd0cf81baa7c137a2ce7ce3d097ba63fc",
            "source_commit: 0000000000000000000000000000000000000000", 1)),
        ("yaml-authority-rewrite", yaml_raw.replace(
            "evaluator_authority: flow_systems/skills/route-a-evaluator.md",
            "evaluator_authority: route-a-evaluator", 1)),
        ("yaml-authority-delete", yaml_raw.replace(
            "evaluator_authority: flow_systems/skills/route-a-evaluator.md\n", "", 1)),
        ("yaml-status-rewrite", yaml_raw.replace("  evidence_status: STOP_SCOPED", "  evidence_status: PROVED", 1)),
        ("yaml-status-delete", yaml_raw.replace("  evidence_status: PROVED\n", "", 1)),
        ("yaml-route-b", yaml_raw.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true", 1)),
        ("yaml-flag", yaml_raw.replace("  claims_target_zero_match: false", "  claims_target_zero_match: true", 1)),
        ("yaml-root-array", "- invalid\n"),
        ("yaml-equivalent-whitespace", yaml_raw + "\n"),
        ("yaml-merge", "base: &b {x: 1}\nmerged:\n  <<: *b\n" + yaml_raw),
        ("yaml-nonstring-key", "1: invalid\n" + yaml_raw),
        ("yaml-implicit-timestamp", yaml_raw.replace('evaluation_date: "2026-09-03"', "evaluation_date: 2026-09-03", 1)),
        ("yaml-unknown-field", yaml_raw + "unknown_field: forbidden\n"),
        ("yaml-type-mutation", yaml_raw.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
    ]
    attacks.extend((name, json_raw, changed_yaml) for name, changed_yaml in yaml_attacks)

    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c327-mutation-") as directory:
        directory = Path(directory)
        for index, (name, raw_json, raw_yaml) in enumerate(attacks):
            evidence = directory / f"attack-{index}.json"
            evaluation = directory / f"attack-{index}.yaml"
            evidence.write_text(raw_json)
            evaluation.write_text(raw_yaml)
            process = subprocess.run(
                [sys.executable, "-B", str(CHECKER), "--evidence", str(evidence), "--evaluation", str(evaluation)],
                env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
            )
            if process.returncode == 0:
                raise AssertionError(f"hostile attack survived: {name}-{index}")
            rejected += 1
    print(f"C327 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
