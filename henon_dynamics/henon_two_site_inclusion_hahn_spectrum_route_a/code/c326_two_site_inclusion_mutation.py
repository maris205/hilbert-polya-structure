#!/usr/bin/env python3
"""Hostile repaired-hash and parser mutations for HCS-C326."""
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
EVIDENCE = ROOT / "results/c326_two_site_inclusion_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C326/2026-09-03.yaml"
CHECKER = ROOT / "code/c326_two_site_inclusion_checker.py"
PRODUCER = ROOT / "code/c326_two_site_inclusion_producer.py"


def repair(data):
    body = dict(data); body.pop("payload_sha256", None)
    data["payload_sha256"] = hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def rejected(evidence, evaluation):
    with tempfile.TemporaryDirectory(prefix="c326-mutation-") as directory:
        base = Path(directory); ep = base / "e.json"; yp = base / "e.yaml"
        ep.write_bytes(evidence); yp.write_bytes(evaluation)
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
        run = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(ep),
                              "--evaluation", str(yp)], env=env, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, text=True)
        return run.returncode != 0


def main():
    if sys.flags.optimize:
        raise RuntimeError("C326 mutation lane refuses optimized Python")
    original = json.loads(EVIDENCE.read_text()); yaml_bytes = EVALUATION.read_bytes(); cases = []

    def add(name, edit):
        value = copy.deepcopy(original); edit(value); repair(value)
        rendered = (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()
        cases.append((name, rendered, yaml_bytes))

    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C325"))
    add("source", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("date", lambda d: d.__setitem__("evaluation_date", "2026-09-04"))
    add("root-extra", lambda d: d.__setitem__("extra", 1))
    add("state-space", lambda d: d["model"].__setitem__("state_space", "all integers"))
    add("parameter", lambda d: d["model"].__setitem__("parameter_domain", "alpha>=0"))
    add("up-rate", lambda d: d["model"].__setitem__("upward_rate", "N-x"))
    add("clock", lambda d: d["model"].__setitem__("clock", "discrete time"))
    add("spectrum-contract", lambda d: d["theorem_contract"].__setitem__("spectrum", "numerical"))
    add("boundary-contract", lambda d: d["theorem_contract"].__setitem__("alpha_zero_face", "omitted"))
    add("row-extra", lambda d: d["parameter_rows"][0].__setitem__("extra", 1))
    add("row-drop", lambda d: d["parameter_rows"].pop())
    add("row-coordinate", lambda d: d["parameter_rows"][1].__setitem__("N", 8))
    add("stationary-extra", lambda d: d["parameter_rows"][10]["stationary"][0].__setitem__("extra", 1))
    add("stationary-drop", lambda d: d["parameter_rows"][10]["stationary"].pop())
    add("stationary-value", lambda d: d["parameter_rows"][10]["stationary"][0].__setitem__("probability", "1/7"))
    add("rate-extra", lambda d: d["parameter_rows"][20]["rate_rows"][0].__setitem__("extra", 1))
    add("rate-drop", lambda d: d["parameter_rows"][20]["rate_rows"].pop())
    add("rate-value", lambda d: d["parameter_rows"][20]["rate_rows"][1].__setitem__("upward", "0"))
    add("spectral-extra", lambda d: d["parameter_rows"][30]["spectral_rows"][0].__setitem__("extra", 1))
    add("spectral-drop", lambda d: d["parameter_rows"][30]["spectral_rows"].pop())
    add("eigenvalue", lambda d: d["parameter_rows"][30]["spectral_rows"][2].__setitem__("eigenvalue", "0"))
    add("hahn-truncate", lambda d: d["parameter_rows"][30]["spectral_rows"][2]["hahn_values"].pop())
    add("hahn-value", lambda d: d["parameter_rows"][30]["spectral_rows"][2]["hahn_values"].__setitem__(1, "0"))
    add("norm", lambda d: d["parameter_rows"][30]["spectral_rows"][2].__setitem__("squared_norm", "1"))
    add("boundary-extra", lambda d: d["alpha_zero_rows"][3].__setitem__("extra", 1))
    add("boundary-drop", lambda d: d["alpha_zero_rows"].pop())
    add("absorption", lambda d: d["alpha_zero_rows"][4]["absorption_probability_at_N"][2].__setitem__("probability", "0"))
    add("weak-limit", lambda d: d["alpha_zero_rows"][4]["stationary_weak_limit"][0].__setitem__("probability", "1"))
    add("stationary-family", lambda d: d["alpha_zero_rows"][4].__setitem__("stationary_law_family", "delta_0 only"))
    add("enumeration", lambda d: d["enumeration"].__setitem__("state_rows", 179))
    add("collision", lambda d: d["collision_boundary"].__setitem__("C253", "same"))
    add("nonclaim", lambda d: d["nonclaims"].__setitem__(1, "multisite included"))
    add("reference", lambda d: d["references"][0].__setitem__("identifier", "wrong"))
    add("route", lambda d: d["route_a"]["tuple"].__setitem__(4, "A4_FAIL"))
    add("route-b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope", lambda d: d["scope_flags"].__setitem__("claims_hilbert_polya_operator", True))
    add("yaml-path", lambda d: d["route_a_yaml"].__setitem__("relative_path", "wrong.yaml"))
    raw = EVIDENCE.read_text()
    cases += [
        ("json-duplicate", raw.replace('"candidate_id": "HCS-C326",', '"candidate_id": "HCS-C326",\n  "candidate_id": "HCS-C326",', 1).encode(), yaml_bytes),
        ("json-nonfinite", raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1).encode(), yaml_bytes),
        ("json-root", b"[]\n", yaml_bytes),
    ]
    text = EVALUATION.read_text()
    yaml_cases = [
        ("yaml-duplicate", text + "candidate_id: HCS-C326\n"),
        ("yaml-alias", "probe: &p 1\ncopy: *p\n" + text),
        ("yaml-merge", "base: &b {x: 1}\nmerged:\n  <<: *b\n" + text),
        ("yaml-nonstring", "1: bad\n" + text),
        ("yaml-root", "- bad\n"),
        ("yaml-timestamp", text.replace('evaluation_date: "2026-09-03"', "evaluation_date: 2026-09-03", 1)),
        ("yaml-unknown", text + "unknown: bad\n"),
        ("yaml-missing", text.replace('arithmetic_origin: "none"\n', "", 1)),
        ("yaml-epoch-type", text.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
        ("yaml-route-type", text.replace("route_b_invocation_allowed: false", 'route_b_invocation_allowed: "false"', 1)),
        ("yaml-authority", text.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md", "evaluator_authority: wrong", 1)),
        ("yaml-status", text.replace("  evidence_status: STOP_SCOPED", "  evidence_status: PROVED", 1)),
        ("yaml-verdict", text.replace("overall_verdict: ROUTE_A_REJECTED", "overall_verdict: ROUTE_A_ACCEPTED", 1)),
        ("yaml-theorem", text.replace("theorem_status: PROVABLE_AS_STATED", "theorem_status: NUMERICAL_ONLY", 1)),
        ("yaml-schema", text.replace("schema: route-a-evaluation-v0.2.0", "schema: wrong", 1)),
        ("yaml-artifact", text.replace("  - THEOREM_PACKAGE.md", "  - WRONG.md", 1)),
        ("yaml-a4-status", text.replace("a4:\n  verdict: A4_FORMAL_HINT\n  evidence_status: PROVED", "a4:\n  verdict: A4_FORMAL_HINT\n  evidence_status: STOP_SCOPED", 1)),
        ("yaml-finite-role", text.replace("exact rational regression audit only, never proof by finite extrapolation", "finite grid proves theorem", 1)),
        ("yaml-route-reason", text.replace("Route A failure does not authorize Route B under the scope firewall", "Route B authorized", 1)),
        ("yaml-normalization", text.replace("state x is site-one occupancy and N-x is site-two occupancy", "state x is total mass", 1)),
        ("yaml-source-token", text.replace("  - DLMF:18.22(ii)", "  - DLMF:wrong", 1)),
        ("yaml-candidate", text.replace("finite birth-death chain x in 0..N with inclusion rates (N-x)(alpha+x) and x(alpha+N-x)", "different chain", 1)),
    ]
    cases.extend((name, EVIDENCE.read_bytes(), value.encode()) for name, value in yaml_cases)
    survived = [name for name, evidence, evaluation in cases if not rejected(evidence, evaluation)]
    if survived:
        raise AssertionError(f"mutations survived: {survived}")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    for script in (PRODUCER, CHECKER):
        if subprocess.run([sys.executable, "-O", str(script)], env=env,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0:
            raise AssertionError("optimized mode survived")
    print(f"C326 hostile mutation suite: PASS ({len(cases)}/{len(cases)} rejected; optimized mode rejected)")


if __name__ == "__main__":
    main()
