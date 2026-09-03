#!/usr/bin/env python3
"""Hostile repaired-hash and parser mutations for HCS-C325."""
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
EVIDENCE = ROOT / "results/c325_moser_tardos_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C325/2026-09-03.yaml"
CHECKER = ROOT / "code/c325_moser_tardos_checker.py"
PRODUCER = ROOT / "code/c325_moser_tardos_producer.py"


def repair(data):
    body = dict(data); body.pop("payload_sha256", None)
    data["payload_sha256"] = hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def rejected(evidence, evaluation):
    with tempfile.TemporaryDirectory(prefix="c325-mutation-") as directory:
        base = Path(directory); ep = base / "e.json"; yp = base / "e.yaml"
        ep.write_bytes(evidence); yp.write_bytes(evaluation)
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
        run = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(ep),
                              "--evaluation", str(yp)], env=env, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, text=True)
        return run.returncode != 0


def main():
    if sys.flags.optimize:
        raise RuntimeError("C325 mutation lane refuses optimized Python")
    original = json.loads(EVIDENCE.read_text()); yaml_bytes = EVALUATION.read_bytes(); cases = []

    def add(name, edit):
        value = copy.deepcopy(original); edit(value); repair(value)
        cases.append((name, (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode(), yaml_bytes))

    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C326"))
    add("source", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("date", lambda d: d.__setitem__("evaluation_date", "2026-09-04"))
    add("root-extra", lambda d: d.__setitem__("extra", 1))
    add("dependence", lambda d: d["model"].__setitem__("dependence", "arbitrary graph"))
    add("selection", lambda d: d["model"].__setitem__("selection_rule", "lexicographic only"))
    add("criterion", lambda d: d["theorem_contract"].__setitem__("criterion", "symmetric LLL only"))
    add("termination", lambda d: d["theorem_contract"].__setitem__("termination", "finite examples only"))
    add("bound", lambda d: d["theorem_contract"].__setitem__("per_event_bound", "E[N_A]<=x_A"))
    add("instance-extra", lambda d: d["instance_rows"][0].__setitem__("extra", 1))
    add("instance-drop", lambda d: d["instance_rows"].pop())
    add("event-extra", lambda d: d["instance_rows"][0]["event_rows"][0].__setitem__("extra", 1))
    add("event-probability", lambda d: d["instance_rows"][0]["event_rows"][0].__setitem__("probability", "1/7"))
    add("event-dependency", lambda d: d["instance_rows"][0]["event_rows"][0]["dependencies"].clear())
    add("tree-weight", lambda d: d["instance_rows"][1]["event_rows"][1]["witness_tree_weight_by_size_1_to_6"].__setitem__(3, "0"))
    add("transition-extra", lambda d: d["instance_rows"][0]["transition_rows"][0].__setitem__("extra", 1))
    add("transition-drop", lambda d: d["instance_rows"][0]["transition_rows"].pop())
    add("transition-probability", lambda d: d["instance_rows"][1]["transition_rows"][0]["targets"][0].__setitem__("probability", "1/9"))
    add("expected", lambda d: d["instance_rows"][2]["expected_total_resamplings"].__class__ and d["instance_rows"][2].__setitem__("expected_total_resamplings", "0"))
    add("enumeration", lambda d: d["enumeration"].__setitem__("state_rows", 111))
    add("collision", lambda d: d["collision_boundary"].__setitem__("C192", "same"))
    add("nonclaim", lambda d: d["nonclaims"].__setitem__(1, "parallel included"))
    add("reference", lambda d: d["references"][0].__setitem__("identifier", "wrong"))
    add("route", lambda d: d["route_a"]["tuple"].__setitem__(4, "A4_FORMAL_HINT"))
    add("route-b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope", lambda d: d["scope_flags"].__setitem__("claims_hilbert_polya_operator", True))
    add("yaml-path", lambda d: d["route_a_yaml"].__setitem__("relative_path", "wrong.yaml"))
    raw = EVIDENCE.read_text()
    cases += [
        ("json-duplicate", raw.replace('"candidate_id": "HCS-C325",', '"candidate_id": "HCS-C325",\n  "candidate_id": "HCS-C325",', 1).encode(), yaml_bytes),
        ("json-nonfinite", raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1).encode(), yaml_bytes),
        ("json-root", b"[]\n", yaml_bytes),
    ]
    text = EVALUATION.read_text()
    yaml_cases = [
        ("yaml-duplicate", text + "candidate_id: HCS-C325\n"),
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
        ("yaml-finite-role", text.replace("regression evidence only; finite assignment chains and truncated witness trees do not prove the general theorem", "finite examples prove the theorem", 1)),
        ("yaml-route-reason", text.replace("all Route-A layers fail and the frozen scope contains no bad-prime, Euler-factor, or root-number datum", "Route B is ready", 1)),
        ("yaml-strongest-evidence", text.replace("the expected resampling bounds are analytic", "numerical only", 1)),
        ("yaml-strongest-failure", text.replace("it has no natural unitary, scattering, Hamiltonian, or self-adjoint quantization", "a Hamiltonian exists", 1)),
    ]
    cases.extend((name, EVIDENCE.read_bytes(), value.encode()) for name, value in yaml_cases)
    survived = [name for name, evidence, evaluation in cases if not rejected(evidence, evaluation)]
    if survived:
        raise AssertionError(f"mutations survived: {survived}")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    for script in (PRODUCER, CHECKER):
        if subprocess.run([sys.executable, "-O", str(script)], env=env, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE).returncode == 0:
            raise AssertionError("optimized mode survived")
    print(f"C325 hostile mutation suite: PASS ({len(cases)}/{len(cases)} rejected; optimized mode rejected)")


if __name__ == "__main__":
    main()
