import numpy as np
import pytest

from henon_zeta.geometry import (
    fixed_points,
    generating_momenta,
    henon_inverse,
    henon_jacobian,
    henon_map,
    monodromy_matrix,
    periodic_action,
    reversor,
)


@pytest.mark.parametrize("a", [1.0056, 1.02])
def test_inverse_and_reversor(a):
    points = [(-1.3, 0.2), (0.0, 0.0), (0.4, -0.9), (1.7, 1.2)]
    for point in points:
        assert np.allclose(henon_inverse(henon_map(point, a), a), point, atol=1e-13)
        assert np.allclose(reversor(henon_map(reversor(point), a)), henon_inverse(point, a), atol=1e-13)


@pytest.mark.parametrize("a", [1.0056, 1.02])
def test_area_preservation_and_fixed_points(a):
    assert np.linalg.det(henon_jacobian((0.37, -0.91), a)) == pytest.approx(1.0)
    positive, negative = fixed_points(a)
    for record in (positive, negative):
        point = (record.coordinate, record.coordinate)
        assert np.allclose(henon_map(point, a), point, atol=1e-13)
        assert record.determinant == pytest.approx(1.0)
    assert positive.stability == "elliptic"
    assert negative.stability == "hyperbolic"


def test_generating_relations():
    a = 1.02
    q, p = 0.41, -0.72
    q_next = henon_map((q, p), a)[0]
    recovered_p, p_next = generating_momenta(q, q_next, a)
    assert recovered_p == pytest.approx(p)
    assert p_next == pytest.approx(q)


def test_fixed_orbit_monodromy_and_action():
    a = 1.02
    fixed = fixed_points(a)[0]
    matrix = monodromy_matrix([fixed.coordinate], a)
    assert np.allclose(matrix, henon_jacobian((fixed.coordinate, fixed.coordinate), a))
    assert np.isfinite(periodic_action([fixed.coordinate], a))
