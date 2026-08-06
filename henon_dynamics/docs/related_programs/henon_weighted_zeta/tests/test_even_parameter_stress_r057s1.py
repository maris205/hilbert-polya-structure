"""Regression tests for the R057S1 centered-even staircase corollary."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from scripts.audit_even_parameter_stress_r057s1 import (
    PROTOCOL_SHA256,
    expand_configurations,
    load_protocol,
    sha256_file,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R057S1_EVEN_PARAMETER_STRESS_PROTOCOL.json"
)
RESULT = PROJECT_ROOT / "results" / "even_parameter_stress_r057s1.json"
ANALYSIS = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R057S1_EVEN_PARAMETER_STRESS_ANALYSIS.md"
)


def exact_ceiling(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def test_r057s1_protocol_hash_and_panel_are_frozen():
    payload = load_protocol()
    jobs = expand_configurations(payload)
    assert sha256_file(PROTOCOL) == PROTOCOL_SHA256
    assert len(jobs) == 266
    assert len({item.configuration_id for item in jobs}) == 266


def test_r057s1_persisted_outcome_and_gates():
    payload = json.loads(RESULT.read_text(encoding="utf-8"))
    analysis = payload["analysis"]
    assert payload["run_id"] == "R057S1_EVEN_PARAMETER_STRESS"
    assert payload["protocol_sha256"] == PROTOCOL_SHA256
    assert len(payload["records"]) == 266
    assert analysis["pass_count"] == 157
    assert analysis["fail_count"] == 109
    assert analysis["grid_with_any_failure_count"] == 10
    assert analysis["cap_active_configuration_count"] == 0
    assert analysis["all_witnesses_pass"]
    assert analysis["all_failures_at_center"]
    assert analysis["baseline_duplicate_consistency_pass"]
    assert analysis["strict_all_gates_pass"]


def test_r057s1_center_boundary_formula_matches_every_configuration():
    payload = json.loads(RESULT.read_text(encoding="utf-8"))
    radius = Fraction("0.6380064794363034")
    for record in payload["records"]:
        grid = int(record["grid"])
        a_value = Fraction(record["a_fraction"])
        eta = Fraction(record["eta_fraction"])
        width = 2 * radius / grid
        expected_k = exact_ceiling(2 * a_value * width / eta)
        expected_omega = a_value * (width / expected_k) ** 2
        assert record["center_boundary_index"] == grid // 2
        assert record["center_left_k"] == expected_k
        assert record["center_right_k"] == expected_k
        assert Fraction(record["center_omega_plus_fraction"]) == expected_omega
        assert record["certificate_pass"] == record["center_plus_pass"]
        assert record["center_minus_pass"]
        assert record["all_failures_at_center"]


def test_r057s1_eta_monotonicity_and_a_reentry_are_reproduced():
    payload = json.loads(RESULT.read_text(encoding="utf-8"))
    analysis = payload["analysis"]
    assert analysis["eta_nonmonotone_grid_count"] == 0
    assert all(item["transition_count"] <= 1 for item in analysis["eta_sequences"])
    nonmonotone_a = [
        item["grid"]
        for item in analysis["a_sequences"]
        if item["nonmonotone_pass_fail_sequence"]
    ]
    assert nonmonotone_a == [46, 92, 106]
    assert [
        item["transition_count"]
        for item in analysis["a_sequences"]
        if item["nonmonotone_pass_fail_sequence"]
    ] == [4, 2, 2]


def test_r057s1_analysis_records_post_primary_scope():
    text = ANALYSIS.read_text(encoding="utf-8")
    assert "ALL GATES PASS" in text
    assert "post-primary supplement" in text
    assert "not held-out confirmation" in text
    assert "sawtooth" in text
    proof = (PROJECT_ROOT / "PROOF_PACKAGE.md").read_text(encoding="utf-8")
    assert "Corollary D" in proof
