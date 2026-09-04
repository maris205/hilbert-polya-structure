#!/usr/bin/env python3
"""Repaired-hash hostile mutations for the C374 independent checker."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c374_kummer_arboreal_evidence.json"
CHECKER = ROOT / "code/c374_kummer_arboreal_checker.py"
EVALUATION = ROOT / "evaluations/route_a/HCS-C374/2026-09-04.yaml"
SOURCE = "f58422d8f03235329863f946654981ecb5d4dc97"


def canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def repaired(value: dict) -> bytes:
    value = copy.deepcopy(value)
    value.pop("payload_sha256", None)
    value["payload_sha256"] = hashlib.sha256(canonical(value)).hexdigest()
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def rejected(blob: bytes) -> bool:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    with tempfile.TemporaryDirectory(prefix="c374-mutation-") as directory:
        path = Path(directory) / "evidence.json"
        path.write_bytes(blob)
        proc = subprocess.run(
            [sys.executable, "-B", str(CHECKER), "--input", str(path)],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
    return proc.returncode != 0


def validate_evaluator(value: dict) -> None:
    assert value["schema"] == "route-a-evaluation-v0.2.0"
    assert value["skill"] == "route-a-evaluator" and value["skill_version"] == "0.2.0"
    assert value["candidate_id"] == "HCS-C374"
    assert value["source_commit"] == SOURCE and value["code_commit"] == SOURCE
    assert set(value["source_lock"]) == {
        "object", "arithmetic_origin", "clock", "normalization",
        "determinant_convention", "cutoff", "precision", "allowed_data", "forbidden_data",
    }
    assert len(value["a0"]["arithmetic_controls"]) >= 3
    assert [row["status"] for row in value["a0"]["arithmetic_controls"]] == [
        "ANALYTICALLY_PROVED", "EXECUTED_EXACT", "EXECUTED_EXACT",
    ]
    composite_result = value["a0"]["arithmetic_controls"][2]["result"]
    assert all(token in composite_result for token in (
        "5 prime powers", "Frob_p^r repetition controls", "20 mixed composites",
        "no one-prime Frobenius owner",
    ))
    assert value["a1"]["verdict"] == "A1_WEAK"
    assert value["a1"]["metrics"]["mandatory_a1_controls_completed"] == 0
    assert value["a4"]["verdict"] == "A4_FORMAL_HINT"
    assert value["a4"]["metrics"]["canonical_time_reversal_for_family"] is False
    assert value["a4"]["metrics"]["nontrivial_phase_weight_preserved"] is False
    assert value["tuple"] == [
        "A0_STRUCTURAL_ARITHMETIC_RELATION", "A1_WEAK", "A2_FAIL",
        "A3_FAIL", "A4_FORMAL_HINT",
    ]
    assert value["overall_verdict"] == "ROUTE_A_EXPLORATORY"
    assert value["adversarial_controls"]["verdict"] == "PASS_SCOPE_LIMIT_RETAINED"
    assert value["claim_boundary"] and len(value["blocking_conditions"]) >= 5
    assert value["next_smallest_test"] and len(value["round2_clues"]) >= 2
    assert value["route_b_invocation_allowed"] is False
    assert not any(value["scope_flags"].values())


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C374 mutation lane refuses optimized Python")
    original_blob = EVIDENCE.read_bytes()
    base = json.loads(original_blob)
    attacks: list[tuple[str, bytes]] = []

    stale = copy.deepcopy(base)
    stale["candidate_id"] = "HCS-C000"
    attacks.append(("stale payload hash", (json.dumps(stale, indent=2, sort_keys=True) + "\n").encode()))

    def add(name, edit):
        value = copy.deepcopy(base)
        edit(value)
        attacks.append((name, repaired(value)))

    add("candidate substitution", lambda x: x.__setitem__("candidate_id", "HCS-C375"))
    add("source substitution", lambda x: x.__setitem__("source_commit", "0" * 40))
    add("basepoint mutation", lambda x: x["model"].__setitem__("basepoint", 3))
    add("intersection mutation", lambda x: x["analytic_theorem"].__setitem__("radical_cyclotomic_intersection", "Q"))
    add("group-order mutation", lambda x: x["group_ledger"][0].__setitem__("group_order", 17))
    add("fixed-law mutation", lambda x: x["group_ledger"][3]["fixed_point_histogram"].__setitem__("2", 1))
    add("density mutation", lambda x: x["group_ledger"][1].__setitem__("root_prime_density", "1/2"))
    add("restriction mutation", lambda x: x["group_ledger"][1]["restriction_to_previous"].__setitem__("kernel_order", 2))
    add("prime-stream mutation", lambda x: x["prime_regression"].__setitem__("row_stream_sha256", "f" * 64))
    add("prime-histogram mutation", lambda x: x["prime_regression"]["levels"][0]["root_histogram"].__setitem__("4", 1))
    add("DOI mutation", lambda x: x["sources"][0].__setitem__("doi", "10.fake/example"))
    add("ownership mutation", lambda x: x["ownership_boundary"].__setitem__("inherited", "none"))
    add("route mutation", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_FULL_PASS"))
    add("A1 escalation", lambda x: x["route_a"]["tuple"].__setitem__(1, "A1_" + "PASS_ANALYTIC"))
    add("basepoint-three control mutation", lambda x: x["arithmetic_controls"]["neighboring_basepoint_3"].__setitem__("shared_Q_sqrt_2_character_entanglement", True))
    add("full-affine control mutation", lambda x: x["arithmetic_controls"]["simpler_parent_full_affine"].__setitem__("restores_four_fixed_roots", False))
    add("prime-power repetition-owner mutation", lambda x: x["arithmetic_controls"]["composite_label_decomposition"].__setitem__("prime_power_owner", "all " + "composites are rejected"))
    add("mixed-composite owner mutation", lambda x: x["arithmetic_controls"]["composite_label_decomposition"].__setitem__("mixed_composite_has_single_prime_frobenius_owner", True))
    add("prime-power classification mutation", lambda x: x["arithmetic_controls"]["composite_label_decomposition"]["prime_power_labels"][0].__setitem__("value", 15))
    add("quantization time-reversal escalation", lambda x: x["quantization_boundary"].__setitem__("canonical_global_time_reversal_to_inverse", True))
    add("quantization route escalation", lambda x: x["quantization_boundary"].__setitem__("route_a_verdict", "A4_" + "NATURAL_QUANTIZATION"))
    add("empirical-density credit mutation", lambda x: x["arithmetic_controls"].__setitem__("empirical_density_earns_a0_credit", True))
    add("forbidden-flag mutation", lambda x: x["scope_flags"].__setitem__("claims_target_euler_factors", True))
    add("unknown-key insertion", lambda x: x.__setitem__("unregistered_claim", True))
    add("required-key deletion", lambda x: x.pop("collision_boundary"))

    duplicate = original_blob.replace(b'{\n  "analytic_theorem"', b'{\n  "candidate_id": "HCS-C374",\n  "analytic_theorem"', 1)
    attacks.append(("duplicate JSON key", duplicate))
    attacks.append(("nonfinite JSON", original_blob.replace(b'"fixed_epoch": 1788480000', b'"fixed_epoch": NaN', 1)))

    for name, blob in attacks:
        if not rejected(blob):
            raise AssertionError(f"checker accepted hostile mutation: {name}")
    attack_count = len(attacks)

    evaluator = yaml.safe_load(EVALUATION.read_text())
    validate_evaluator(evaluator)
    evaluator_mutations = [
        lambda x: x.__setitem__("skill_version", "0.1.0"),
        lambda x: x.__setitem__("code_commit", "0" * 40),
        lambda x: x["source_lock"].pop("clock"),
        lambda x: x["a0"].__setitem__("arithmetic_controls", []),
        lambda x: x["a0"]["arithmetic_controls"][2].__setitem__("result", "all " + "composites have no owner"),
        lambda x: x["a1"].__setitem__("verdict", "A1_" + "PASS_ANALYTIC"),
        lambda x: x["a1"]["metrics"].__setitem__("mandatory_a1_controls_completed", 6),
        lambda x: x["a4"].__setitem__("verdict", "A4_" + "NATURAL_QUANTIZATION"),
        lambda x: x["a4"]["metrics"].__setitem__("canonical_time_reversal_for_family", True),
        lambda x: x["tuple"].__setitem__(4, "A4_" + "NATURAL_QUANTIZATION"),
        lambda x: x.__setitem__("overall_verdict", "ROUTE_A_" + "ARITHMETIC_CANDIDATE"),
        lambda x: x["adversarial_controls"].__setitem__("verdict", "PASS"),
        lambda x: x.__setitem__("blocking_conditions", []),
        lambda x: x.__setitem__("route_b_invocation_allowed", True),
    ]
    for mutation in evaluator_mutations:
        candidate = copy.deepcopy(evaluator)
        mutation(candidate)
        try:
            validate_evaluator(candidate)
        except (AssertionError, KeyError, TypeError, ValueError):
            attack_count += 1
        else:
            raise AssertionError("evaluator mutation survived validation")
    print(f"C374 hostile mutation suite: PASS ({attack_count} attacks)")


if __name__ == "__main__":
    main()
