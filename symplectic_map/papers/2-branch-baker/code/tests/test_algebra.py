from __future__ import annotations

import sympy as sp
import pytest

from branch_baker.algebra import (
    ADJACENCY,
    ALLOWED_EDGES,
    D,
    FACTOR_ORIENTATION,
    LEFT_PF_VECTOR,
    PARAMETER_POLYNOMIAL,
    PARAMETER_ROOT,
    PF_EIGENVALUE,
    RECTANGLE_AREAS,
    RIGHT_PF_VECTOR,
    ROOT_LOWER,
    ROOT_UPPER,
    U,
    branch_jacobian,
    branch_orientation,
    branch_symplectic_residual,
    exact_identity_audit,
    markov_endpoint_images,
    postcritical_orbit,
    postcritical_residuals,
    reduce_mod_parameter,
    root_isolation_certificate,
    strip_tiling_residuals,
)


def test_frozen_matrices_are_exact_and_immutable() -> None:
    assert ADJACENCY == sp.Matrix(((0, 0, 1), (0, 0, 1), (1, 1, 0)))
    assert FACTOR_ORIENTATION == sp.Matrix(((0, 0, 1), (0, 0, -1), (-1, -1, 0)))
    assert ALLOWED_EDGES == ((0, 2), (1, 2), (2, 0), (2, 1))
    with pytest.raises(TypeError):
        ADJACENCY[0, 0] = 1


def test_exact_root_isolation_certificate() -> None:
    certificate = root_isolation_certificate()
    assert certificate.lower == ROOT_LOWER
    assert certificate.upper == ROOT_UPPER
    assert certificate.polynomial_at_lower == sp.Rational(-4136221, 15625000000)
    assert certificate.polynomial_at_upper == sp.Rational(32678453, 1000000000000)
    assert certificate.open_interval_root_count == 1
    assert certificate.certified
    assert PARAMETER_ROOT.poly.as_expr() == PARAMETER_POLYNOMIAL
    assert float(ROOT_LOWER) < float(PARAMETER_ROOT.evalf(30)) < float(ROOT_UPPER)


def test_postcritical_orbit_is_exact_mod_parameter_polynomial() -> None:
    assert postcritical_orbit() == (0, 1, -D, D, D)
    assert postcritical_residuals() == (0, 0, 0, 0, 0)
    assert reduce_mod_parameter(PARAMETER_POLYNOMIAL) == 0
    assert sp.expand(reduce_mod_parameter(U**3) - (2 * U**2 - 2 * U + 2)) == 0
    with pytest.raises(ValueError, match="polynomial"):
        reduce_mod_parameter(1 / U)


def test_markov_endpoint_images_and_parent_orientations() -> None:
    assert markov_endpoint_images() == ((D, 1), (1, D), (D, -D))
    assert tuple(branch_orientation(source) for source in range(3)) == (1, -1, -1)
    for source, target in ALLOWED_EDGES:
        assert FACTOR_ORIENTATION[source, target] == branch_orientation(source)
    with pytest.raises(IndexError):
        branch_orientation(3)


def test_pf_vectors_rectangle_areas_and_strip_tiling() -> None:
    assert ADJACENCY * RIGHT_PF_VECTOR == PF_EIGENVALUE * RIGHT_PF_VECTOR
    assert LEFT_PF_VECTOR.T * ADJACENCY == PF_EIGENVALUE * LEFT_PF_VECTOR.T
    assert (LEFT_PF_VECTOR.T * RIGHT_PF_VECTOR)[0] == 1
    assert RECTANGLE_AREAS == (sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(1, 2))
    residuals = strip_tiling_residuals()
    assert residuals == {
        "source_widths": (0, 0, 0),
        "destination_heights": (0, 0, 0),
        "area_normalization": 0,
    }


def test_every_allowed_branch_is_exactly_symplectic() -> None:
    expected_signs = {(0, 2): 1, (1, 2): -1, (2, 0): -1, (2, 1): -1}
    for edge, sign in expected_signs.items():
        jacobian = branch_jacobian(*edge)
        assert jacobian == sp.diag(sign * sp.sqrt(2), sign / sp.sqrt(2))
        assert jacobian.det() == 1
        assert branch_symplectic_residual(*edge) == sp.zeros(2)
    with pytest.raises(ValueError, match="not allowed"):
        branch_jacobian(0, 0)


def test_complete_algebra_audit_passes() -> None:
    audit = exact_identity_audit()
    assert audit
    assert all(audit.values()), audit
