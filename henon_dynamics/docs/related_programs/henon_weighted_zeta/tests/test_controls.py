import numpy as np
import pytest

from henon_zeta.controls import (
    analytic_period2,
    analytic_period2_trace,
    analytic_period3,
    analytic_period3_traces,
    cat_fixed_point_count,
    cat_primitive_orbit_count,
    mobius,
    pcf_w2_zeta_coefficients,
    real_periodic_coordinate_bound,
)
from henon_zeta.geometry import monodromy_matrix


def test_mobius_values():
    assert [mobius(n) for n in range(1, 11)] == [1, -1, -1, 0, -1, 1, -1, 0, 0, 1]


def test_cat_known_counts():
    assert [cat_fixed_point_count(n) for n in range(1, 5)] == [1, 5, 16, 45]
    assert [cat_primitive_orbit_count(n) for n in range(1, 5)] == [1, 2, 5, 10]


def test_pcf_w2_rational_zeta_coefficients():
    assert pcf_w2_zeta_coefficients(7) == (1, 1, 2, 2, 4, 4, 8, 8)


def test_closed_form_period2_control():
    assert analytic_period2(1.02) == ()
    sequence = analytic_period2(3.6)[0]
    assert abs(float(np.trace(monodromy_matrix(sequence, 3.6))) - analytic_period2_trace(3.6)) < 1e-12


def test_closed_form_period3_control_at_target_parameter():
    sequences = analytic_period3(1.02)
    traces = analytic_period3_traces(1.02)
    assert len(sequences) == 2
    assert len(traces) == 2
    computed = [float(np.trace(monodromy_matrix(sequence, 1.02))) for sequence in sequences]
    assert sorted(computed) == pytest.approx(sorted(traces), abs=1e-12)
    assert sorted(traces) == pytest.approx(sorted([2.145470129472588, 1.534529870527412]), abs=1e-12)
    assert real_periodic_coordinate_bound(1.02) > max(abs(value) for sequence in sequences for value in sequence)
