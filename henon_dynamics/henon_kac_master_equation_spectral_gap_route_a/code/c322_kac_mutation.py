#!/usr/bin/env python3
"""Hostile repaired-hash and parser mutation suite for HCS-C322."""
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
EVIDENCE = ROOT / "results/c322_kac_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C322/2026-09-03.yaml"
CHECKER = ROOT / "code/c322_kac_checker.py"
PRODUCER = ROOT / "code/c322_kac_producer.py"


def repair(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    data["payload_sha256"] = hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def rejected(evidence_bytes, yaml_bytes):
    with tempfile.TemporaryDirectory(prefix="c322-mutation-") as directory:
        base = Path(directory)
        evidence = base / "evidence.json"
        evaluation = base / "evaluation.yaml"
        evidence.write_bytes(evidence_bytes)
        evaluation.write_bytes(yaml_bytes)
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
        process = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(evidence),
                                  "--evaluation", str(evaluation)], env=env,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return process.returncode != 0


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C322 mutation lane refuses optimized Python")
    original = json.loads(EVIDENCE.read_text())
    yaml_raw = EVALUATION.read_bytes()
    mutations = []

    def add(name, function):
        value = copy.deepcopy(original)
        function(value)
        repair(value)
        raw = (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False) + "\n").encode()
        mutations.append((name, raw, yaml_raw))

    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C321"))
    add("source", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("root-extra", lambda d: d.__setitem__("unexpected", 1))
    add("missing-generator-N", lambda d: d["model"].__setitem__("positive_generator", "I-Q_N"))
    add("ordered-pairs", lambda d: d["model"].__setitem__("pair_sampling", "uniform ordered pairs"))
    add("angle-normalization", lambda d: d["model"].__setitem__("angle_measure", "dtheta/pi"))
    add("zero-energy", lambda d: d["model"].__setitem__("zero_energy_boundary", "gap remains positive"))
    add("gap", lambda d: d["theorem_contract"].__setitem__("gap", "1/2"))
    add("lower-bound", lambda d: d["theorem_contract"].__setitem__("lower_bound", "finite matrix check"))
    add("projection-transfer", lambda d: d["theorem_contract"].__setitem__("projection_transfer", "permutation heuristic"))
    add("multiplicity", lambda d: d["theorem_contract"].__setitem__("multiplicity", "one for all N"))
    add("quartic-action", lambda d: d["quartic_ambient_action"].__setitem__("coefficient_sum_v4", "wrong"))
    add("conditional-extra", lambda d: d["conditional_operator_rows"][0].__setitem__("extra", 0))
    add("conditional-cell", lambda d: d["conditional_operator_rows"][2]["cells"][2].__setitem__("eigenvalue", "0"))
    add("conditional-omit", lambda d: d["conditional_operator_rows"][0]["cells"].pop())
    add("conditional-truncate", lambda d: d["conditional_operator_rows"].pop())
    add("gap-center", lambda d: d["gap_rows"][3].__setitem__("quartic_center", "0"))
    add("gap-multiplicity", lambda d: d["gap_rows"][0].__setitem__("slow_multiplicity", "one"))
    add("gap-duplicate", lambda d: d["gap_rows"].append(copy.deepcopy(d["gap_rows"][-1])))
    add("basis", lambda d: d["polynomial_form_rows"][0]["basis"][1].__setitem__(0, 8))
    add("gram", lambda d: d["polynomial_form_rows"][1]["gram_upper"][9].__setitem__("value", "0"))
    add("q-form", lambda d: d["polynomial_form_rows"][2]["q_form_upper"][20].__setitem__("value", "0"))
    add("form-cell-extra", lambda d: d["polynomial_form_rows"][0]["gram_upper"][0].__setitem__("extra", 1))
    add("form-cell-duplicate", lambda d: d["polynomial_form_rows"][0]["q_form_upper"].append(copy.deepcopy(d["polynomial_form_rows"][0]["q_form_upper"][-1])))
    add("form-truncate", lambda d: d["polynomial_form_rows"].pop())
    add("enumeration", lambda d: d["enumeration"].__setitem__("upper_form_cells", 1))
    add("route-a4", lambda d: d["route_a"]["tuple"].__setitem__(4, "A4_ROUTE_B_READY"))
    add("route-b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope", lambda d: d["scope_flags"].__setitem__("claims_hilbert_polya_operator", True))
    add("reference", lambda d: d["references"][1].__setitem__("identifier", "wrong"))
    add("collision", lambda d: d["collision_boundary"].__setitem__("C170", "same model"))
    add("nonclaim", lambda d: d["nonclaims"].__setitem__(0, "finite matrices prove the gap"))
    add("yaml-relative-path", lambda d: d["route_a_yaml"].__setitem__("relative_path", "evaluations/route_a/HCS-C321/2026-09-03.yaml"))
    add("leaf-count", lambda d: d["enumeration"].__setitem__("audited_leaf_count", 1))

    raw_json = EVIDENCE.read_text()
    for name, raw in [
        ("json-duplicate", raw_json.replace('"candidate_id": "HCS-C322",', '"candidate_id": "HCS-C322",\n  "candidate_id": "HCS-C322",', 1).encode()),
        ("json-nonfinite", raw_json.replace('"fixed_epoch": 1788393600', '"fixed_epoch": Infinity', 1).encode()),
        ("json-root", b"[]\n"),
    ]:
        mutations.append((name, raw, yaml_raw))

    text = EVALUATION.read_text()
    yaml_mutations = [
        ("yaml-duplicate", text + "candidate_id: HCS-C322\n"),
        ("yaml-alias", "probe: &probe 1\ncopy: *probe\n" + text),
        ("yaml-merge", "base: &base {x: 1}\nmerged:\n  <<: *base\n" + text),
        ("yaml-nonstring-key", "1: bad\n" + text),
        ("yaml-root", "- wrong\n- root\n"),
        ("yaml-timestamp", text.replace('evaluation_date: "2026-09-03"', "evaluation_date: 2026-09-03", 1)),
        ("yaml-unknown", text + "unknown_field: bad\n"),
        ("yaml-missing", text.replace('arithmetic_origin: "none"\n', "", 1)),
        ("yaml-typed-epoch", text.replace("fixed_epoch: 1788393600", 'fixed_epoch: "1788393600"', 1)),
        ("yaml-typed-lock", text.replace("route_b_invocation_allowed: false", 'route_b_invocation_allowed: "false"', 1)),
        ("yaml-authority", text.replace("evaluator_authority: flow_systems/skills/route-a-evaluator.md", "evaluator_authority: route-a-evaluator", 1)),
        ("yaml-status-delete", text.replace("  evidence_status: PROVED\n", "", 1)),
        ("yaml-status-rewrite", text.replace("  evidence_status: STOP_SCOPED\n", "  evidence_status: PROVED\n", 1)),
        ("yaml-theorem-status", text.replace("theorem_status: PROVABLE_AS_STATED", "theorem_status: NUMERICAL_ONLY", 1)),
    ]
    for name, value in yaml_mutations:
        mutations.append((name, EVIDENCE.read_bytes(), value.encode()))

    survived = [name for name, evidence, evaluation in mutations if not rejected(evidence, evaluation)]
    if survived:
        raise AssertionError(f"mutations survived: {survived}")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    for script in (PRODUCER, CHECKER):
        process = subprocess.run([sys.executable, "-O", str(script)], env=env,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if process.returncode == 0:
            raise AssertionError(f"optimized mode survived: {script.name}")
    print(f"C322 hostile mutation suite: PASS ({len(mutations)}/{len(mutations)} rejected; optimized mode rejected)")


if __name__ == "__main__":
    main()
