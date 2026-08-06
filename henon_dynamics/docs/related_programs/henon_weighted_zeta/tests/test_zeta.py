import numpy as np
import pytest

from henon_zeta.orbits import build_orbit_record
from henon_zeta.zeta import (
    determinant_coefficients,
    euler_log_derivative_coefficients,
    leading_resonance_from_determinant,
    log_zeta_coefficients,
    monodromy_trace_power,
    perron_fixed_point_traces,
    perron_fredholm_coefficients,
    zeta_coefficients,
)


def test_single_fixed_hyperbolic_factor_series():
    record = build_orbit_record(1.02, [-2.3737912160345], True)
    weight = max(abs(record.multiplier_large), abs(record.multiplier_small)) ** -1
    determinant = determinant_coefficients([record], 4, beta=1.0)
    zeta = zeta_coefficients([record], 4, beta=1.0)
    assert np.allclose(determinant, [1.0, -weight, 0.0, 0.0, 0.0])
    assert np.allclose(zeta, [weight**degree for degree in range(5)])


def test_trace_and_log_coefficient_relation():
    record = build_orbit_record(1.02, [-2.3737912160345], True)
    log_coefficients = log_zeta_coefficients([record], 6, beta=0.5)
    traces = euler_log_derivative_coefficients([record], 6, beta=0.5)
    assert np.allclose(traces, np.arange(7) * log_coefficients)


def test_determinant_and_zeta_are_inverse_series():
    records = [
        build_orbit_record(1.02, [-2.3737912160345], True),
        build_orbit_record(1.02, [-1.7093442975027715, -0.9901475429766743, 1.7093442975027715, -0.9901475429766743], True),
    ]
    determinant = determinant_coefficients(records, 10, beta=1.0)
    zeta = zeta_coefficients(records, 10, beta=1.0)
    convolution = np.convolve(determinant, zeta)[:11]
    assert np.allclose(convolution, [1.0] + [0.0] * 10, atol=1e-12)


def test_leading_resonance_inverts_smallest_polynomial_root():
    coefficients = np.array([1.0, -0.5])
    assert leading_resonance_from_determinant(coefficients) == pytest.approx(0.5)


def test_monodromy_trace_power_recurrence():
    trace = 3.0
    assert monodromy_trace_power(trace, 0) == 2.0
    assert monodromy_trace_power(trace, 1) == 3.0
    assert monodromy_trace_power(trace, 2) == 7.0
    assert monodromy_trace_power(trace, 3) == 18.0


def test_perron_fredholm_coefficient_recurrence():
    record = build_orbit_record(1.02, [-2.3737912160345], True)
    traces = perron_fixed_point_traces([record], 4)
    coefficients = perron_fredholm_coefficients([record], 4)
    assert traces[1] > 0.0
    assert coefficients[0] == 1.0
    for degree in range(1, 5):
        recurrence = -sum(traces[index] * coefficients[degree - index] for index in range(1, degree + 1)) / degree
        assert coefficients[degree] == pytest.approx(recurrence)
