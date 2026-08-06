from math import isclose

from hp_candidate_search.heat_activity import (
    asymptotic_constants,
    evaluate_record,
    exact_bracket,
    raw_polar_bracket,
)


def test_frozen_constants() -> None:
    constants = asymptotic_constants(51.0 / 50.0)
    assert isclose(constants["r_a"], 0.413006902309, rel_tol=0.0, abs_tol=5.0e-13)
    assert isclose(constants["coefficient"], -0.0137987335661, rel_tol=0.0, abs_tol=5.0e-14)
    assert isclose(constants["beta"], 2.98907358486, rel_tol=0.0, abs_tol=5.0e-12)
    assert isclose(constants["kappa"], 1.72992096098, rel_tol=0.0, abs_tol=5.0e-12)


def test_exact_carrier_is_positive_before_wk_sign() -> None:
    _, _, bracket = exact_bracket(1.0e-3, 51.0 / 50.0)
    assert bracket > 0.0


def test_raw_polar_matches_reduced_identity() -> None:
    a = 51.0 / 50.0
    for t in (1.0e-2, 1.0e-4):
        _, _, expected = exact_bracket(t, a)
        observed = raw_polar_bracket(t, a)
        assert abs(observed - expected) / expected <= 1.0e-9


def test_record_has_negative_formal_relative_carrier() -> None:
    record = evaluate_record(1.0e-4)
    assert record.identity_relative_error <= 1.0e-9
    assert record.formal_relative_heat_carrier < 0.0

