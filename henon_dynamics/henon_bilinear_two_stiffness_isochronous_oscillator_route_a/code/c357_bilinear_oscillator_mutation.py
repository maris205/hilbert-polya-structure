#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite for HCS-C357."""
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
CHECKER = ROOT/"code/c357_bilinear_oscillator_checker.py"
EVIDENCE = ROOT/"results/c357_bilinear_oscillator_evidence.json"
EVALUATION = ROOT/"evaluations/route_a/HCS-C357/2026-09-03.yaml"


def repair(data):
    out = copy.deepcopy(data); out.pop("payload_sha256", None)
    raw = json.dumps(out, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    out["payload_sha256"] = hashlib.sha256(raw).hexdigest()
    return json.dumps(out, indent=2, sort_keys=True, ensure_ascii=False).encode()+b"\n"


def rejected(evidence, evaluation):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c357-mutation-") as directory:
        work = Path(directory); ep = work/"e.json"; yp = work/"y.yaml"
        ep.write_bytes(evidence); yp.write_bytes(evaluation)
        proc = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(ep), "--evaluation", str(yp)], env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return proc.returncode != 0


def main():
    if sys.flags.optimize:
        raise RuntimeError("C357 mutation suite refuses optimized Python")
    base_raw = EVIDENCE.read_bytes(); eval_raw = EVALUATION.read_bytes(); base = json.loads(base_raw)
    attacks = []
    def add(name, fn):
        value = copy.deepcopy(base); fn(value); attacks.append((name, repair(value), eval_raw))
    add("candidate", lambda x: x.__setitem__("candidate_id", "HCS-C000"))
    add("obstruction", lambda x: x.__setitem__("obstruction_id", "HEN-O000"))
    add("date", lambda x: x.__setitem__("evaluation_date", "2026-09-04"))
    add("source", lambda x: x.__setitem__("source_commit", "0"*40))
    add("epoch", lambda x: x.__setitem__("fixed_epoch", 0))
    add("scope", lambda x: x.__setitem__("scope_literal", "OTHER"))
    add("evaluator_authority", lambda x: x["evaluator"].__setitem__("authority", "elsewhere"))
    add("evaluator_sha", lambda x: x["evaluator"].__setitem__("sha256", "0"*64))
    add("evaluation_path", lambda x: x["evaluation_lock"].__setitem__("relative_path", "wrong"))
    add("evaluation_raw", lambda x: x["evaluation_lock"].__setitem__("raw_sha256", "0"*64))
    add("model", lambda x: x["model"].__setitem__("action_angle_regularness", "globally smooth"))
    add("wronskian", lambda x: x["model"].__setitem__("wronskian", "difference sign"))
    add("theorem_iff", lambda x: x["theorem_contract"].__setitem__("classical_iff", "one side suffices"))
    add("theorem_quantum", lambda x: x["theorem_contract"].__setitem__("quantum", "full L2 arithmetic spectrum"))
    add("boundary", lambda x: x["boundary_atlas"].__setitem__("one_sided_zero", "periodic"))
    add("reference", lambda x: x["references"][0].__setitem__("identifier", "fake"))
    add("collision", lambda x: x["collision_boundary"].__setitem__("C232", "same"))
    add("nonclaim", lambda x: x["nonclaims"].__setitem__(1, "equispaced"))
    add("route_tuple", lambda x: x["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("route_overall", lambda x: x["route_a"].__setitem__("overall", "PASS"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_target_zero_match", True))
    add("frequency_grid", lambda x: x["frequency_grid"][0].__setitem__(0, "2"))
    add("energy_grid", lambda x: x["energy_grid"].__setitem__(0, "1"))
    add("coordinate", lambda x: x["classical_rows"][0].__setitem__("energy_index", 5))
    add("row_extra", lambda x: x["classical_rows"][0].__setitem__("extra", 1))
    add("noncanonical", lambda x: x["classical_rows"][0].__setitem__("omega_plus", "2/2"))
    add("nan_string", lambda x: x["classical_rows"][0].__setitem__("action", "nan"))
    add("period", lambda x: x["classical_rows"][0].__setitem__("period_over_pi", "9"))
    add("action", lambda x: x["classical_rows"][0].__setitem__("action", "9"))
    add("amplitude", lambda x: x["classical_rows"][0].__setitem__("amplitude_plus_squared", "9"))
    add("time_fraction", lambda x: x["classical_rows"][0].__setitem__("right_time_fraction", "9"))
    add("half_matrix", lambda x: x["classical_rows"][0]["right_half_matrix"][0].__setitem__(0, "1"))
    add("monodromy", lambda x: x["classical_rows"][0]["full_monodromy"][0].__setitem__(0, "-1"))
    add("duplicate_classical", lambda x: x["classical_rows"].__setitem__(1, copy.deepcopy(x["classical_rows"][0])))
    add("omit_classical", lambda x: x["classical_rows"].pop())
    add("quantum_level", lambda x: x["quantum_equal_frequency_rows"][0].__setitem__("level", 2))
    add("quantum_lambda", lambda x: x["quantum_equal_frequency_rows"][0].__setitem__("lambda", "9"))
    add("quantum_parity", lambda x: x["quantum_equal_frequency_rows"][0].__setitem__("parity", "odd"))
    add("quantum_factor", lambda x: x["quantum_equal_frequency_rows"][0].__setitem__("vanishing_interface_factor", "D_value"))
    add("quantum_boolean", lambda x: x["quantum_equal_frequency_rows"][0].__setitem__("wronskian_zero", 1))
    add("boundary_flat", lambda x: x["zero_stiffness_rows"][0].__setitem__("flat_side", "left"))
    add("boundary_compact", lambda x: x["zero_stiffness_rows"][0].__setitem__("quantum_compact_resolvent", True))
    add("enumeration", lambda x: x["enumeration"].__setitem__("classical_rows", 1))
    add("leaf_count", lambda x: x["enumeration"].__setitem__("leaf_count_without_payload_hash", 1))
    add("top_extra", lambda x: x.__setitem__("unexpected", 1))
    attacks.append(("stale_hash", base_raw.replace(b'"action": "1/8"', b'"action": "9"', 1), eval_raw))
    attacks.append(("duplicate_json", base_raw.replace(b'{\n', b'{\n  "schema": "duplicate",\n', 1), eval_raw))
    attacks.append(("nonfinite_json", base_raw.replace(b'"fixed_epoch": 1788393600', b'"fixed_epoch": NaN', 1), eval_raw))
    for name, raw in [
        ("yaml_authority", eval_raw.replace(b"evaluator_authority: flow_systems/skills/route-a-evaluator.md", b"evaluator_authority: elsewhere")),
        ("yaml_status", eval_raw.replace(b"evidence_status: PROVED", b"evidence_status: STOP_SCOPED", 1)),
        ("yaml_alias", eval_raw+b"alias_attack: &x 1\nalias_use: *x\n"),
        ("yaml_duplicate", eval_raw+b"candidate_id: HCS-C357\n"),
        ("yaml_nonstring", eval_raw+b"7: bad\n"),
    ]:
        attacks.append((name, base_raw, raw))
    passed = 0
    for name, evidence, evaluation in attacks:
        if not rejected(evidence, evaluation):
            raise AssertionError(f"mutation survived: {name}")
        passed += 1
    print(f"C357 hostile mutation suite: PASS ({passed}/{len(attacks)} rejected)")


if __name__ == "__main__":
    main()
