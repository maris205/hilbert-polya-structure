import pytest

from prime_multiplier.controls import CONTROL_SPECS, audit_control, audit_controls


def test_all_frozen_controls_pass():
    record = audit_controls()
    assert record["status"] == "PASS"
    assert not record["candidate_accessed"]
    assert [item["control_id"] for item in record["controls"]] == [
        "c_zero",
        "c_minus_2",
        "c_minus_3_over_4",
    ]


def test_fixed_control_multipliers_are_recovered():
    for spec in CONTROL_SPECS:
        record = audit_control(spec)
        found = set(record["periods"][0]["rational_candidates"])
        expected = {str(item) for item in spec.fixed_multiplier_prediction}
        assert found == expected


def test_assumption_violation_control_detects_three():
    record = audit_control(CONTROL_SPECS[2])
    assert not record["algebraic_integer_coefficients"]
    fixed = record["periods"][0]["rational_candidate_records"]
    assert any(item["multiplier"] == "3" and item["raw_rational_prime"] for item in fixed)


def test_control_period_cutoff_is_frozen():
    with pytest.raises(ValueError, match="periods 1..4"):
        audit_controls(max_period=3)

