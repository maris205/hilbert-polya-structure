#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite for HCS-C364."""
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
CHECKER = ROOT / "code/c364_gauss_reduction_checker.py"
EVIDENCE = ROOT / "results/c364_gauss_reduction_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C364/2026-09-04.yaml"


def repair(data: dict) -> None:
    payload = dict(data); payload.pop("payload_sha256", None)
    data["payload_sha256"] = hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def rejected(evidence_bytes: bytes, evaluation_bytes: bytes) -> bool:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c364-hostile-") as directory:
        epath, ypath = Path(directory) / "evidence.json", Path(directory) / "evaluation.yaml"
        epath.write_bytes(evidence_bytes); ypath.write_bytes(evaluation_bytes)
        proc = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(epath), "--evaluation", str(ypath)], env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        return proc.returncode != 0


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C364 mutation suite refuses optimized Python")
    original = json.loads(EVIDENCE.read_text())
    original_yaml = EVALUATION.read_bytes()
    if rejected(EVIDENCE.read_bytes(), original_yaml):
        raise AssertionError("canonical baseline rejected before hostile mutations")
    attacks = []

    stale = copy.deepcopy(original); stale["candidate_id"] = "HCS-C000"
    attacks.append(("stale_hash_control", json.dumps(stale).encode(), original_yaml))

    def evidence_attack(name, mutate):
        value = copy.deepcopy(original); mutate(value); repair(value)
        attacks.append((name, (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode(), original_yaml))

    evidence_attack("candidate", lambda x: x.__setitem__("candidate_id", "HCS-C000"))
    evidence_attack("evaluator_authority", lambda x: x["evaluator"].__setitem__("authority", "elsewhere"))
    evidence_attack("evaluation_lock", lambda x: x["evaluation_lock"].__setitem__("raw_sha256", "0" * 64))
    evidence_attack("theorem", lambda x: x["theorem_contract"].__setitem__("reversal", "mutated"))
    evidence_attack("boundary", lambda x: x["boundary_atlas"].__setitem__("square", "mutated"))
    evidence_attack("reference", lambda x: x["references"][0].__setitem__("identifier", "10.invalid"))
    evidence_attack("collision", lambda x: x["collision_boundary"].__setitem__("C330", "mutated"))
    evidence_attack("nonclaim", lambda x: x["nonclaims"].__setitem__(0, "mutated"))
    evidence_attack("route_tuple", lambda x: x["route_a"]["tuple"].__setitem__(1, "A1_FAIL"))
    evidence_attack("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_target_zero_match", True))
    evidence_attack("state_extra", lambda x: x["state_rows"][0].__setitem__("extra", 1))
    evidence_attack("state_digit", lambda x: x["state_rows"][20].__setitem__("digit", x["state_rows"][20]["digit"] + 1))
    evidence_attack("state_successor", lambda x: x["state_rows"][30].__setitem__("successor", [1, 2]))
    evidence_attack("state_duplicate", lambda x: x["state_rows"].__setitem__(40, copy.deepcopy(x["state_rows"][39])))
    evidence_attack("state_omit", lambda x: x["state_rows"].pop(50))
    evidence_attack("cycle_matrix", lambda x: x["cycle_rows"][10]["period_matrix"][0].__setitem__(0, x["cycle_rows"][10]["period_matrix"][0][0] + 1))
    evidence_attack("cycle_reverse", lambda x: x["cycle_rows"][15].__setitem__("reverse_cycle_index", 999))
    evidence_attack("cycle_omit", lambda x: x["cycle_rows"].pop(25))
    evidence_attack("fixed_formula", lambda x: x["fixed_point_rows"][100].__setitem__("fixed_states", x["fixed_point_rows"][100]["fixed_states"] + 1))
    evidence_attack("enumeration", lambda x: x["enumeration"].__setitem__("state_rows", 0))
    evidence_attack("square_boundary", lambda x: x["boundary_rows"]["square"][5].__setitem__("terminal_integer", 99))
    evidence_attack("imprimitive_boundary", lambda x: x["boundary_rows"]["imprimitive"].__setitem__("content", 1))
    evidence_attack("top_extra", lambda x: x.__setitem__("unknown", 1))

    # Python considers bool a subclass of int and also equates integral floats
    # with integers.  These repaired-hash attacks enforce JSON leaf types, not
    # merely Python value equality.
    digit_one = next(i for i, row in enumerate(original["state_rows"]) if row["digit"] == 1)
    state_cycle_zero = next(i for i, row in enumerate(original["state_rows"]) if row["cycle_index"] == 0)
    determinant_one = next(i for i, row in enumerate(original["cycle_rows"]) if row["determinant"] == 1)
    orientation_one = next(i for i, row in enumerate(original["cycle_rows"]) if row["orientation_preserving_generator_power"] == 1)
    fixed_power_one = next(i for i, row in enumerate(original["fixed_point_rows"]) if row["power"] == 1)
    fixed_zero = next(i for i, row in enumerate(original["fixed_point_rows"]) if row["fixed_states"] == 0)
    evidence_attack("typed_scope_false_as_zero", lambda x: x["scope_flags"].__setitem__("claims_target_zero_match", 0))
    evidence_attack("typed_route_false_as_zero", lambda x: x["route_a"].__setitem__("route_b", 0))
    evidence_attack("typed_epoch_integer_as_float", lambda x: x.__setitem__("fixed_epoch", float(x["fixed_epoch"])))
    evidence_attack("typed_digit_one_as_true", lambda x: x["state_rows"][digit_one].__setitem__("digit", True))
    evidence_attack("typed_digit_one_as_float", lambda x: x["state_rows"][digit_one].__setitem__("digit", 1.0))
    evidence_attack("typed_cycle_zero_as_false", lambda x: x["state_rows"][state_cycle_zero].__setitem__("cycle_index", False))
    evidence_attack("typed_determinant_one_as_true", lambda x: x["cycle_rows"][determinant_one].__setitem__("determinant", True))
    evidence_attack("typed_orientation_one_as_true", lambda x: x["cycle_rows"][orientation_one].__setitem__("orientation_preserving_generator_power", True))
    evidence_attack("typed_fixed_power_one_as_true", lambda x: x["fixed_point_rows"][fixed_power_one].__setitem__("power", True))
    evidence_attack("typed_fixed_zero_as_false", lambda x: x["fixed_point_rows"][fixed_zero].__setitem__("fixed_states", False))
    evidence_attack("typed_enumeration_integer_as_float", lambda x: x["enumeration"].__setitem__("state_rows", float(x["enumeration"]["state_rows"])))
    evidence_attack("typed_boundary_integer_as_float", lambda x: x["boundary_rows"]["imprimitive"].__setitem__("content", 2.0))

    duplicate_json = EVIDENCE.read_text().replace('"candidate_id": "HCS-C364",', '"candidate_id": "HCS-C364",\n  "candidate_id": "HCS-C364",', 1).encode()
    attacks.append(("duplicate_json", duplicate_json, original_yaml))
    nonfinite_json = EVIDENCE.read_text().replace('"fixed_epoch": 1788480000', '"fixed_epoch": NaN', 1).encode()
    attacks.append(("nonfinite_json", nonfinite_json, original_yaml))
    yaml_attacks = [
        ("yaml_authority", original_yaml.replace(b"evaluator_authority: flow_systems/skills/route-a-evaluator.md", b"evaluator_authority: elsewhere")),
        ("yaml_status", original_yaml.replace(b"  evidence_status: STOP_SCOPED", b"  evidence_status: PROVED", 1)),
        ("yaml_date", original_yaml.replace(b"evaluation_date: '2026-09-04'", b"evaluation_date: '2026-09-05'")),
        ("yaml_artifact_type", original_yaml.replace(b"artifact_paths:\n", b"artifact_paths: wrong\n", 1)),
        ("yaml_duplicate", original_yaml + b"candidate_id: HCS-C364\n"),
        ("yaml_alias", original_yaml + b"hostile_anchor: &x value\nhostile_alias: *x\n"),
        ("yaml_nonstring", original_yaml + b"1: hostile\n"),
        ("yaml_source_token", original_yaml.replace(b"10.1090/S0002-9904-1930-05043-0", b"10.invalid", 1)),
        ("yaml_theorem_status", original_yaml.replace(b"PROVABLE_AS_STATED_AFTER_CONVENTION_LOCK", b"PROVABLE_AS_STATED")),
    ]
    for name, raw in yaml_attacks:
        attacks.append((name, EVIDENCE.read_bytes(), raw))

    passed = 0
    for name, evidence_bytes, evaluation_bytes in attacks:
        if not rejected(evidence_bytes, evaluation_bytes):
            raise AssertionError(f"hostile mutation survived: {name}")
        passed += 1
    print(f"C364 hostile mutation suite: PASS ({passed}/{len(attacks)} rejected)")


if __name__ == "__main__":
    main()
