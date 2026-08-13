import pytest

from action_audit.henon import (
    henon_static_identity_audit,
    projective_infinity_audit,
    recurrence_multiplicity_audit,
    s_integral_denominator_ledger,
)


def test_henon_static_identities_all_zero():
    record = henon_static_identity_audit()
    assert record["pass"]
    assert set(record["residuals"].values()) == {"0"}


def test_henon_static_audit_does_not_substitute_candidate():
    record = henon_static_identity_audit()
    assert not record["candidate_parameter_substituted"]
    assert not record["periodic_equation_solved"]


def test_henon_jacobian_is_one():
    assert henon_static_identity_audit()["jacobian_determinant"] == "1"


def test_low_period_neighbors_retain_multiplicity():
    record = recurrence_multiplicity_audit()
    assert record["pass"]
    assert "2*q_0" in record["period_1_equation"]
    assert "2*q_1" in record["period_2_equations"][0]


def test_projective_infinity_audit_passes_declared_periods():
    record = projective_infinity_audit((1, 2, 3, 7))
    assert record["pass"]
    assert all(item["projective_point_at_infinity_exists"] is False for item in record["records"])


def test_projective_infinity_is_proof_audit_not_enumeration():
    record = projective_infinity_audit()
    assert record["proof_not_orbit_enumeration"]
    assert not record["periodic_equation_solved"]


def test_projective_infinity_rejects_nonpositive_period():
    with pytest.raises(ValueError):
        projective_infinity_audit((0,))


def test_s_integral_ledger_uses_orbit_field_extension():
    record = s_integral_denominator_ledger()
    assert record["pass"]
    assert record["orbit_field"].startswith("finite K/K0")
    assert "above S0" in record["extended_places"]


def test_denominator_three_is_sharp_in_control():
    record = s_integral_denominator_ledger()
    assert record["denominator_support"] == [3]
    assert record["sharpness_control"]["action"] == "-1/3"
    assert record["sharpness_control"]["shows_A_need_not_be_integral_away_from_3"]
