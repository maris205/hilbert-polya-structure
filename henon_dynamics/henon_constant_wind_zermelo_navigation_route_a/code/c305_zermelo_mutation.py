#!/usr/bin/env python3
"""Repaired-hash semantic and parser attacks for the C305 checker."""
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
EVIDENCE = ROOT / "results/c305_zermelo_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C305/2026-09-03.yaml"
CHECKER = ROOT / "code/c305_zermelo_checker.py"


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def set_path(data, path, value):
    cursor = data
    for item in path[:-1]:
        cursor = cursor[item]
    cursor[path[-1]] = value


def main() -> None:
    pristine = json.loads(EVIDENCE.read_text())
    yaml_raw = EVALUATION.read_text()
    attacks = []
    mutations = [
        (("schema",), "false-schema"), (("candidate_id",), "HCS-C000"), (("obstruction_id",), "HEN-O000"),
        (("evaluation_date",), "2026-09-04"), (("fixed_epoch",), 1788393601), (("source_commit",), "0" * 40),
        (("scope_literal",), "EXPANDED_SCOPE"), (("evaluator", "sha256"), "0" * 64),
        (("model", "dynamics"), False), (("theorem_contract", "three_chambers"), False),
        (("theorem_contract", "optimizer"), "sometimes constant"), (("proof_contract", "quadratic"), False),
        (("proof_contract", "root_choice"), "larger strong root"), (("proof_contract", "uniqueness"), "assumed"),
        (("proof_contract", "hjb"), "wrong sign"), (("proof_contract", "finite_role"), "finite cases prove theorem"),
        (("route_a", "tuple", 0), "A0_PASS"), (("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        (("route_a", "route_b_invocation_allowed"), True), (("scope_flags", "claims_target_euler_factors"), True),
        (("scope_flags", "claims_root_number"), True), (("scope_flags", "claims_hilbert_polya_operator"), True),
        (("nonclaims", 0), "We construct target Euler factors."),
        (("collision_boundary", "C222"), "identical"), (("collision_boundary", "C270"), "identical"),
        (("collision_boundary", "C268"), "identical"),
        (("references", 0, "identifier"), "invented"), (("references", 0, "role"), False),
        (("boundaries", 4, "statement"), False), (("enumeration", "case_count"), 28),
        (("enumeration", "case_ids", 0), "W0-D2-345"), (("enumeration", "hjb_probe_count"), 11),
        (("enumeration", "boundary_rows"), 7), (("enumeration", "audited_cell_count"), 743),
        (("cases", 0, "dimension"), True), (("cases", 0, "wind", 0), "0/1"),
        (("cases", 0, "speed_cap"), "2/1"), (("cases", 0, "target", 0), "6/2"),
        (("cases", 0, "w_squared"), "1"), (("cases", 0, "p"), "1"),
        (("cases", 0, "r_squared"), "8"), (("cases", 0, "quadratic_coefficient"), "-3"),
        (("cases", 0, "discriminant"), "35"), (("cases", 0, "chamber"), "strong_wind"),
        (("cases", 0, "reachable"), 1), (("cases", 0, "minimum_time"), 1),
        (("cases", 0, "formula_branch"), "strong_smaller_root"),
        (("cases", 0, "attainable_time_interval", "kind"), "closed_window"),
        (("cases", 0, "attainable_time_interval", "lower"), "1.0"),
        (("cases", 0, "optimal_control", 0), "1.0"), (("cases", 0, "optimal_speed"), "1.0"),
        (("cases", 0, "terminal_residual"), "1.0"),
        (("cases", 10, "reachable"), True), (("cases", 10, "minimum_time"), "1.0"),
        (("cases", 17, "attainable_time_interval", "upper"), "2.0"),
        (("cases", 22, "optimal_control", 0), "1.0"),
        (("cases", 24, "attainable_time_interval", "kind"), "singleton_zero"),
        (("hjb_probes", 0, "gradient", 0), "0.1"), (("hjb_probes", 1, "hjb_lhs"), "0.9"),
        (("hjb_probes", 2, "target_scale_three_time"), "1.0"), (("hjb_probes", 3, "velocity_scale_two_time"), 0),
    ]
    for path, value in mutations:
        changed = copy.deepcopy(pristine)
        set_path(changed, path, value)
        changed["payload_sha256"] = payload_hash(changed)
        attacks.append(("semantic-" + "-".join(map(str, path)), json.dumps(changed, sort_keys=True, indent=2) + "\n", yaml_raw))

    for name, mutator in (
        ("extra-top-key", lambda d: d.__setitem__("unexpected", False)),
        ("extra-case-key", lambda d: d["cases"][0].__setitem__("unexpected", 0)),
        ("extra-interval-key", lambda d: d["cases"][0]["attainable_time_interval"].__setitem__("unexpected", 0)),
        ("extra-hjb-key", lambda d: d["hjb_probes"][0].__setitem__("unexpected", 0)),
        ("duplicate-case-id", lambda d: d["cases"][1].__setitem__("case_id", d["cases"][0]["case_id"])),
        ("reordered-cases", lambda d: d["cases"].reverse()),
        ("missing-boundary", lambda d: d["boundaries"].pop()),
    ):
        changed = copy.deepcopy(pristine)
        mutator(changed)
        changed["payload_sha256"] = payload_hash(changed)
        attacks.append((name, json.dumps(changed, sort_keys=True, indent=2) + "\n", yaml_raw))

    raw = EVIDENCE.read_text()
    attacks.extend([
        ("stale-payload-hash", raw.replace('"candidate_id": "HCS-C305"', '"candidate_id": "HCS-C000"', 1), yaml_raw),
        ("duplicate-json-key", raw.replace("{\n", '{\n  "schema": "duplicate",\n', 1), yaml_raw),
        ("nonfinite-json", raw.replace('"fixed_epoch": 1788393600', '"fixed_epoch": NaN', 1), yaml_raw),
        ("json-top-array", "[]\n", yaml_raw),
    ])
    yaml_attacks = [
        ("duplicate-yaml-key", yaml_raw + "candidate_id: HCS-C305\n"),
        ("yaml-anchor", yaml_raw.replace("candidate_id: HCS-C305", "candidate_id: &bad HCS-C305", 1)),
        ("yaml-alias", yaml_raw + "alias_probe: *bad\n"), ("yaml-merge", yaml_raw + "merge_probe:\n  <<: {x: y}\n"),
        ("yaml-top-array", "- HCS-C305\n"), ("yaml-epoch-string", yaml_raw.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
        ("yaml-title-false", yaml_raw.replace('title: "All-dimensional constant-wind Zermelo reachability and value atlas"', "title: false", 1)),
        ("yaml-dynamics-false", yaml_raw.replace('dynamics: "xdot=W+u with constant W and measurable norm-bounded control"', "dynamics: false", 1)),
        ("yaml-a0-failure-false", yaml_raw.replace('  strongest_failure: "no rational-prime local datum or target Euler factor is constructed"', "  strongest_failure: false", 1)),
        ("yaml-a4-artifact-missing", yaml_raw.replace("    - SOURCE_AUDIT.md\n    - paper/main.pdf", "    - SOURCE_AUDIT.md", 1)),
        ("yaml-scope-int", yaml_raw.replace("  claims_target_euler_factors: false", "  claims_target_euler_factors: 0", 1)),
        ("yaml-tuple-pass", yaml_raw.replace("  - A0_FAIL", "  - A0_PASS", 1)),
        ("yaml-scope-escalation", yaml_raw.replace("NO_BAD_EULER_OR_ROOT_NUMBER", "EXPANDED_SCOPE", 1)),
    ]
    attacks.extend((name, raw, altered) for name, altered in yaml_attacks)

    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c305-mutations-") as temporary:
        base = Path(temporary)
        for index, (name, evidence_text, yaml_text) in enumerate(attacks):
            evidence_path, evaluation_path = base / f"evidence-{index}.json", base / f"evaluation-{index}.yaml"
            evidence_path.write_text(evidence_text); evaluation_path.write_text(yaml_text)
            completed = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(evidence_path), "--evaluation", str(evaluation_path)], env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if completed.returncode == 0:
                raise AssertionError(f"mutation survived: {name}")
            rejected += 1
    if rejected != len(attacks):
        raise AssertionError("mutation accounting mismatch")
    print(f"C305 hostile mutation suite: PASS {rejected}/{len(attacks)}")


if __name__ == "__main__":
    main()
