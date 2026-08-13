import pytest
import sympy as sp

from action_audit.gauge import gauge_shift_record, symbolic_telescoping_audit


def test_compatible_endpoint_removes_endpoint_term():
    record = gauge_shift_record(
        base_action=0,
        gauge_values=[1, 4, 1],
        constants=[2, 3],
        values_declared_algebraic=True,
    )
    assert record["endpoint_mismatch"] == "0"
    assert record["direct_shift"] == "5"
    assert record["short_sum_constants_formula_allowed"]


def test_incompatible_endpoint_is_retained():
    record = gauge_shift_record(
        base_action=0,
        gauge_values=[1, 4, 8],
        constants=[2, 3],
        values_declared_algebraic=True,
    )
    assert record["endpoint_mismatch"] == "7"
    assert record["direct_shift"] == "12"
    assert not record["short_sum_constants_formula_allowed"]
    assert record["pass"]


def test_uniform_constant_gives_n_times_c():
    record = gauge_shift_record(
        base_action=sp.Rational(1, 3),
        gauge_values=[0, 0, 0, 0, 0],
        constants=[sp.Rational(2, 5)] * 4,
        values_declared_algebraic=True,
    )
    assert record["direct_shift"] == "8/5"
    assert record["shifted_action"] == "29/15"


@pytest.mark.parametrize("period", [1, 2, 7, 13])
def test_symbolic_general_telescope(period):
    assert symbolic_telescoping_audit(period)["pass"]


def test_symbolic_telescope_rejects_nonpositive_period():
    with pytest.raises(ValueError):
        symbolic_telescoping_audit(0)


def test_gauge_rejects_mismatched_lengths():
    with pytest.raises(ValueError):
        gauge_shift_record(
            base_action=0,
            gauge_values=[0, 0],
            constants=[1, 2],
            values_declared_algebraic=True,
        )


def test_gauge_rejects_float_input():
    with pytest.raises(ValueError):
        gauge_shift_record(
            base_action=0,
            gauge_values=[0, 0],
            constants=[0.5],
            values_declared_algebraic=True,
        )


def test_uncertified_gauge_data_fail_closed():
    record = gauge_shift_record(
        base_action=0,
        gauge_values=[0, 1],
        constants=[0],
        values_declared_algebraic=False,
    )
    assert not record["pass"]
    assert record["classification"].startswith("STOP_")
