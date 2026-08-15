from __future__ import annotations

import pytest

from cat_torsion.finite_field import (
    EXPECTED_PERIOD_PROFILES,
    boundary_profiles,
    enumerate_period_profile,
    jordan_mod5_certificate,
    primitive_kernel_certificate,
    vector_period,
)
from cat_torsion.algebra import CAT_MATRIX


def test_boundary_profiles_and_jordan_repair_are_exact():
    assert enumerate_period_profile(2) == {3: 3}
    assert enumerate_period_profile(3) == {4: 8}
    assert enumerate_period_profile(5) == {2: 4, 10: 20}
    boundary = boundary_profiles()
    assert boundary["pass"] is True
    jordan = jordan_mod5_certificate()
    assert jordan["pass"] is True
    assert jordan["period_profile"] == {"2": 4, "10": 20}
    assert jordan["checks"]["two_period_ten_cycles"] is True


def test_primitive_kernel_exact_period_control():
    certificate = primitive_kernel_certificate(3, 2)
    assert certificate["pass"] is True
    assert certificate["exact_periods"] == [3]
    assert certificate["nonzero_kernel_count"] == 3


def test_finite_field_scope_is_locked_to_support_and_period_cutoff():
    with pytest.raises(ValueError):
        enumerate_period_profile(13)
    with pytest.raises(ValueError):
        vector_period(CAT_MATRIX, 2, (1, 0), maximum_period=13)
    with pytest.raises(ValueError):
        vector_period(CAT_MATRIX, 2, (0, 0))
    assert set(EXPECTED_PERIOD_PROFILES) == {2, 3, 5, 7, 11, 19, 29, 199}
