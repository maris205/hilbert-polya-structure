#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite for HCS-C354."""
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
CHECKER = ROOT / "code/c354_lagrange_top_checker.py"
EVIDENCE = ROOT / "results/c354_lagrange_top_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C354/2026-09-03.yaml"


def repair(data):
    out = copy.deepcopy(data); out.pop("payload_sha256", None)
    payload = json.dumps(out, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    out["payload_sha256"] = hashlib.sha256(payload).hexdigest()
    return json.dumps(out, indent=2, sort_keys=True, ensure_ascii=False).encode()+b"\n"


def rejected(evidence_raw, evaluation_raw):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c354-mutation-") as directory:
        work = Path(directory); ep = work/"e.json"; yp = work/"y.yaml"
        ep.write_bytes(evidence_raw); yp.write_bytes(evaluation_raw)
        proc = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(ep), "--evaluation", str(yp)], env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return proc.returncode != 0


def main():
    if sys.flags.optimize:
        raise RuntimeError("C354 mutation suite refuses optimized Python")
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
    add("evaluation_raw", lambda x: x["evaluation_lock"].__setitem__("raw_sha256", "0"*64))
    add("evaluation_semantic", lambda x: x["evaluation_lock"].__setitem__("semantic_sha256", "0"*64))
    add("model", lambda x: x["model"].__setitem__("reduced_cubic", "mutated"))
    add("theorem", lambda x: x["theorem_contract"].__setitem__("phase_closure", "mutated"))
    add("boundary", lambda x: x["boundary_atlas"].__setitem__("separatrix", "finite"))
    add("reference", lambda x: x["references"][0].__setitem__("identifier", "fake"))
    add("collision", lambda x: x["collision_boundary"].__setitem__("C186", "same"))
    add("nonclaim", lambda x: x["nonclaims"].__setitem__(0, "priority claimed"))
    add("route_tuple", lambda x: x["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("route_overall", lambda x: x["route_a"].__setitem__("overall", "PASS"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_root_number", True))
    add("grid", lambda x: x["parameter_grid"][0].__setitem__(0, "2"))
    add("parameter_index", lambda x: x["parameter_rows"][0].__setitem__("index", 9))
    add("parameter_extra", lambda x: x["parameter_rows"][0].__setitem__("extra", 1))
    add("coefficient", lambda x: x["parameter_rows"][0]["coefficients_low_to_high"].__setitem__(0, "99"))
    add("noncanonical_rational", lambda x: x["parameter_rows"][0].__setitem__("A", "2/2"))
    add("nan_string", lambda x: x["parameter_rows"][0]["probes"][0].__setitem__("P_polynomial", "nan"))
    add("root_interval", lambda x: x["parameter_rows"][0]["root_intervals"][0].__setitem__("left", "0"))
    add("root_multiplicity", lambda x: x["parameter_rows"][0]["root_intervals"][0].__setitem__("multiplicity", 2))
    add("omit_root", lambda x: x["parameter_rows"][0]["root_intervals"].pop())
    add("duplicate_parameter", lambda x: x["parameter_rows"].__setitem__(1, copy.deepcopy(x["parameter_rows"][0])))
    add("probe_u", lambda x: x["parameter_rows"][0]["probes"][0].__setitem__("u", "0"))
    add("probe_phase", lambda x: x["parameter_rows"][0]["probes"][0].__setitem__("phi_dot", "0"))
    add("elliptic_root", lambda x: x["elliptic_rows"][0].__setitem__("r3", "3/2" if x["elliptic_rows"][0]["r3"] != "3/2" else "2"))
    add("elliptic_modulus", lambda x: x["elliptic_rows"][0].__setitem__("k_squared", "1"))
    add("elliptic_identity", lambda x: x["elliptic_rows"][0]["substitution_rhs"].__setitem__(1, "0"))
    add("steady", lambda x: x["steady_and_pole_rows"][0].__setitem__("P_prime", "1"))
    add("pole", lambda x: x["steady_and_pole_rows"][1].__setitem__("compatibility", "none"))
    add("enumeration", lambda x: x["enumeration"].__setitem__("probe_rows", 1))
    add("leaf_count", lambda x: x["enumeration"].__setitem__("leaf_count_without_payload_hash", 1))
    add("top_extra", lambda x: x.__setitem__("unexpected", 1))
    attacks.append(("stale_hash", base_raw.replace(b'"A": "1"', b'"A": "2"', 1), eval_raw))
    attacks.append(("duplicate_json", base_raw.replace(b'{\n', b'{\n  "schema": "duplicate",\n', 1), eval_raw))
    attacks.append(("nonfinite_json", base_raw.replace(b'"fixed_epoch": 1788393600', b'"fixed_epoch": NaN', 1), eval_raw))
    yaml_attacks = [
        ("yaml_authority", eval_raw.replace(b"evaluator_authority: flow_systems/skills/route-a-evaluator.md", b"evaluator_authority: elsewhere")),
        ("yaml_status", eval_raw.replace(b"evidence_status: PROVED", b"evidence_status: STOP_SCOPED", 1)),
        ("yaml_alias", eval_raw+b"alias_attack: &x 1\nalias_use: *x\n"),
        ("yaml_duplicate", eval_raw+b"candidate_id: HCS-C354\n"),
        ("yaml_nonstring", eval_raw+b"7: bad\n"),
    ]
    for name, raw in yaml_attacks:
        attacks.append((name, base_raw, raw))
    passed = 0
    for name, evidence, evaluation in attacks:
        if not rejected(evidence, evaluation):
            raise AssertionError(f"mutation survived: {name}")
        passed += 1
    print(f"C354 hostile mutation suite: PASS ({passed}/{len(attacks)} rejected)")


if __name__ == "__main__":
    main()
