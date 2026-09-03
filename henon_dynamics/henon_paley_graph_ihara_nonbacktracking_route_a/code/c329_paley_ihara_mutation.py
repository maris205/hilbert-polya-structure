#!/usr/bin/env python3
"""Hostile repaired-hash and parser mutations for HCS-C329."""
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
EVIDENCE = ROOT / "results/c329_paley_ihara_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C329/2026-09-03.yaml"
CHECKER = ROOT / "code/c329_paley_ihara_checker.py"
PRODUCER = ROOT / "code/c329_paley_ihara_producer.py"


def repair(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    data["payload_sha256"] = hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def rejected(evidence, evaluation):
    with tempfile.TemporaryDirectory(prefix="c329-mutation-") as directory:
        root = Path(directory)
        ep, yp = root / "evidence.json", root / "evaluation.yaml"
        ep.write_bytes(evidence)
        yp.write_bytes(evaluation)
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
        run = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(ep),
                              "--evaluation", str(yp)], env=env, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, text=True)
        return run.returncode != 0


def main():
    if sys.flags.optimize:
        raise RuntimeError("C329 mutation lane refuses optimized Python")
    original = json.loads(EVIDENCE.read_text())
    yaml_bytes = EVALUATION.read_bytes()
    cases = []

    def add(name, edit):
        value = copy.deepcopy(original)
        edit(value)
        repair(value)
        rendered = (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()
        cases.append((name, rendered, yaml_bytes))

    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C330"))
    add("obstruction", lambda d: d.__setitem__("obstruction_id", "HEN-O314"))
    add("source", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("date", lambda d: d.__setitem__("evaluation_date", "2026-09-04"))
    add("root-extra", lambda d: d.__setitem__("extra", 1))
    add("model-field", lambda d: d["model"].__setitem__("field_domain", "primes only"))
    add("model-graph", lambda d: d["model"].__setitem__("graph", "complete graph"))
    add("model-transition", lambda d: d["model"].__setitem__("transition", "backtracking allowed"))
    add("model-orbit", lambda d: d["model"].__setitem__("orbit_convention", "quotient reversal"))
    add("contract-graph", lambda d: d["theorem_contract"].__setitem__("graph", "numerical"))
    add("contract-bass", lambda d: d["theorem_contract"].__setitem__("bass", "assumed"))
    add("contract-boundary", lambda d: d["theorem_contract"].__setitem__("boundary", "omitted"))
    add("grid-q", lambda d: d["finite_grid"]["q_values"].pop())
    add("grid-trace", lambda d: d["finite_grid"].__setitem__("max_trace_power", 11))
    add("field-drop", lambda d: d["field_rows"].pop())
    add("field-duplicate", lambda d: d["field_rows"].append(copy.deepcopy(d["field_rows"][-1])))
    add("field-extra-key", lambda d: d["field_rows"][0].__setitem__("extra", 1))
    add("field-coordinate", lambda d: d["field_rows"][1].__setitem__("q", 5))
    add("modulus", lambda d: d["field_rows"][1]["modulus_coefficients_low_to_high"].__setitem__(0, 2))
    add("residue-drop", lambda d: d["field_rows"][4]["quadratic_residues"].pop())
    add("residue-duplicate", lambda d: d["field_rows"][4]["quadratic_residues"].append(d["field_rows"][4]["quadratic_residues"][0]))
    add("degree", lambda d: d["field_rows"][5].__setitem__("degree", 1))
    add("edge-count", lambda d: d["field_rows"][6].__setitem__("edge_count", 1))
    add("srg-extra", lambda d: d["field_rows"][7]["strongly_regular"].__setitem__("extra", 1))
    add("srg-lambda", lambda d: d["field_rows"][7]["strongly_regular"].__setitem__("lambda", 0))
    add("spectrum-drop", lambda d: d["field_rows"][8]["adjacency_spectrum"].pop())
    add("spectrum-multiplicity", lambda d: d["field_rows"][8]["adjacency_spectrum"][1].__setitem__("multiplicity", 1))
    add("bass-exponent", lambda d: d["field_rows"][9]["bass_factorization"].__setitem__("one_minus_u_squared_exponent", 0))
    add("bass-total", lambda d: d["field_rows"][9]["bass_factorization"].__setitem__("total_degree", 0))
    add("trace-drop", lambda d: d["field_rows"][10]["trace_rows"].pop())
    add("trace-extra", lambda d: d["field_rows"][10]["trace_rows"][0].__setitem__("extra", 1))
    add("trace-value", lambda d: d["field_rows"][10]["trace_rows"][4].__setitem__("trace", 1))
    add("primitive-value", lambda d: d["field_rows"][10]["trace_rows"][4].__setitem__("primitive_oriented_cycles", 1))
    add("control", lambda d: d["arithmetic_controls"].__setitem__(0, "none"))
    add("collision", lambda d: d["collision_boundary"].__setitem__("C15", "same owner"))
    add("nonclaim", lambda d: d["nonclaims"].__setitem__(1, "target RH"))
    add("reference", lambda d: d["references"][0].__setitem__("identifier", "wrong"))
    add("route", lambda d: d["route_a"]["tuple"].__setitem__(0, "A0_STRUCTURAL_ARITHMETIC_RELATION"))
    add("overall", lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route-b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope", lambda d: d["scope_flags"].__setitem__("claims_target_euler_factors", True))
    add("yaml-path", lambda d: d["route_a_yaml"].__setitem__("relative_path", "wrong.yaml"))
    add("yaml-raw", lambda d: d["route_a_yaml"].__setitem__("raw_sha256", "0" * 64))
    add("enumeration", lambda d: d["enumeration"].__setitem__("trace_rows", 155))
    raw = EVIDENCE.read_text()
    cases.extend([
        ("json-duplicate", raw.replace('"candidate_id": "HCS-C329",', '"candidate_id": "HCS-C329",\n  "candidate_id": "HCS-C329",', 1).encode(), yaml_bytes),
        ("json-nonfinite", raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1).encode(), yaml_bytes),
        ("json-root", b"[]\n", yaml_bytes),
    ])
    text = EVALUATION.read_text()
    yaml_cases = [
        ("yaml-duplicate", text + "candidate_id: HCS-C329\n"),
        ("yaml-alias", "probe: &p 1\ncopy: *p\n" + text),
        ("yaml-merge", "base: &b {x: 1}\nmerged:\n  <<: *b\n" + text),
        ("yaml-nonstring", "1: bad\n" + text),
        ("yaml-root", "- bad\n"),
        ("yaml-timestamp", text.replace('evaluation_date: "2026-09-03"', "evaluation_date: 2026-09-03", 1)),
        ("yaml-unknown", text + "unknown: bad\n"),
        ("yaml-missing", text.replace("training_data: none\n", "", 1)),
        ("yaml-epoch-type", text.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
        ("yaml-route-type", text.replace("route_b_invocation_allowed: false", 'route_b_invocation_allowed: "false"', 1)),
        ("yaml-authority", text.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md", "evaluator_authority: wrong", 1)),
        ("yaml-status", text.replace("  evidence_status: STOP_SCOPED", "  evidence_status: PROVED", 1)),
        ("yaml-verdict", text.replace("overall_verdict: ROUTE_A_EXPLORATORY", "overall_verdict: ROUTE_A_ACCEPTED", 1)),
        ("yaml-theorem", text.replace("theorem_status: PROVABLE_AS_STATED", "theorem_status: NUMERICAL_ONLY", 1)),
        ("yaml-schema", text.replace("schema: route-a-evaluation-v0.2.0", "schema: wrong", 1)),
        ("yaml-artifact", text.replace("  - THEOREM_PACKAGE.md", "  - WRONG.md", 1)),
        ("yaml-a1", text.replace("  verdict: A1_PASS_ANALYTIC", "  verdict: A1_WEAK", 1)),
        ("yaml-finite-role", text.replace("exact finite-field regression audit only, never proof by finite extrapolation", "finite grid proves theorem", 1)),
        ("yaml-route-reason", text.replace("exploratory Route A status does not authorize Route B under the scope firewall", "Route B authorized", 1)),
        ("yaml-normalization", text.replace("primitive cycles are oriented and quotiented by cyclic shift but not reversal", "reversal quotient", 1)),
        ("yaml-source-token", text.replace("  - DOI:10.1002/sapm1933121311", "  - DOI:wrong", 1)),
        ("yaml-candidate", text.replace("Paley graph on the additive group of F_q with q an odd prime power congruent to one modulo four and Hashimoto dynamics on directed edges", "different graph", 1)),
        ("yaml-scope", text.replace("  claims_target_euler_factors: false", "  claims_target_euler_factors: true", 1)),
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
    print(f"C329 hostile mutation suite: PASS ({len(cases)}/{len(cases)} rejected; optimized mode rejected)")


if __name__ == "__main__":
    main()
