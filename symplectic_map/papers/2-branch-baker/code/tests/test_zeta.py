from __future__ import annotations

import sympy as sp
import pytest

from branch_baker.algebra import ADJACENCY, FACTOR_ORIENTATION
from branch_baker.cycles import periodic_point_counts
from branch_baker.zeta import (
    S,
    Z,
    FiniteRankClockCertificate,
    LocalLengthCoordinates,
    candidate_clock_certificate,
    exact_zeta_audit,
    factor_orientation_determinant,
    factor_orientation_multiplier_product,
    factor_orientation_weighted_zeta,
    graph_determinant,
    interval_lefschetz_zeta,
    orientation_nilpotence_residual,
    parent_boundary_quotient_factor,
    parent_core_zeta,
    parent_factor_orientation_object,
    unsigned_constant_slope_multiplier_product,
    unsigned_structural_determinant,
    unsigned_structural_zeta,
)


def test_unsigned_graph_determinant_and_zeta() -> None:
    assert unsigned_structural_determinant() == 1 - 2 * Z**2
    assert unsigned_structural_zeta() == 1 / (1 - 2 * Z**2)
    assert sp.expand(graph_determinant(sp.Matrix(((0, 1), (1, 0))), Z) - (1 - Z) * (1 + Z)) == 0
    with pytest.raises(ValueError, match="square"):
        graph_determinant(sp.ones(2, 3))


def test_log_zeta_coefficients_recover_graph_traces() -> None:
    log_series = sp.series(sp.log(unsigned_structural_zeta()), Z, 0, 21).removeO().expand()
    for period, fixed_points in enumerate(periodic_point_counts(ADJACENCY, 20), start=1):
        assert sp.expand(log_series).coeff(Z, period) == sp.Rational(fixed_points, period)


def test_factor_orientation_convention_is_nilpotent_and_separate() -> None:
    assert orientation_nilpotence_residual() == sp.zeros(3)
    assert FACTOR_ORIENTATION**2 != sp.zeros(3)
    assert factor_orientation_determinant() == 1
    assert factor_orientation_weighted_zeta() == 1
    assert all(sp.trace(FACTOR_ORIENTATION**period) == 0 for period in range(1, 21))


def test_single_boundary_euler_factor_gives_parent_zeta() -> None:
    assert parent_boundary_quotient_factor() == 1 + Z
    assert sp.simplify(parent_boundary_quotient_factor() * unsigned_structural_zeta() - parent_core_zeta()) == 0
    assert parent_core_zeta() == (Z + 1) / (1 - 2 * Z**2)


def test_parent_orientation_object_is_not_lefschetz_zeta() -> None:
    assert parent_factor_orientation_object() == 1 - Z
    assert interval_lefschetz_zeta() == 1 / (1 - Z)
    assert parent_factor_orientation_object() != interval_lefschetz_zeta()


def test_constant_slope_multiplier_products() -> None:
    expected = 1 / (1 - sp.Integer(2) ** (1 - S))
    assert sp.simplify(unsigned_constant_slope_multiplier_product() - expected) == 0
    assert factor_orientation_multiplier_product() == 1
    assert unsigned_constant_slope_multiplier_product(sp.Integer(2)) == 2


def test_candidate_finite_rank_clock_certificate() -> None:
    certificate = candidate_clock_certificate()
    assert certificate.basis_labels == ("log(2)",)
    assert certificate.original_memory == 1
    assert certificate.recoded_state_bound == 4
    assert certificate.span_rank == 1
    assert certificate.maximum_independent_exact_log_targets == 1
    assert certificate.cannot_contain_unbounded_independent_family is True
    assert certificate.periodic_length_coordinates(((0, 2), (2, 1))) == (1,)
    record = certificate.as_dict()
    assert record["span_rank"] == 1
    assert "unique-factorization independence of logarithms" in record["proof_dependencies"]


def test_general_finite_rank_clock_certificate_and_validation() -> None:
    certificate = FiniteRankClockCertificate(
        basis_labels=("b0", "b1", "redundant"),
        local_lengths=(
            LocalLengthCoordinates.create("a", (1, 0, 1)),
            LocalLengthCoordinates.create("b", (0, sp.Rational(1, 2), 0)),
            LocalLengthCoordinates.create("c", (1, 1, 1)),
        ),
        original_memory=3,
    )
    assert certificate.span_rank == 2
    assert certificate.periodic_length_coordinates(("a", "b", "c")) == (2, sp.Rational(3, 2), 2)
    with pytest.raises(KeyError, match="undeclared"):
        certificate.periodic_length_coordinates(("missing",))
    with pytest.raises(ValueError, match="at least one block"):
        certificate.periodic_length_coordinates(())
    with pytest.raises(ValueError, match="match the declared basis"):
        FiniteRankClockCertificate(
            basis_labels=("x", "y"),
            local_lengths=(LocalLengthCoordinates.create("a", (1,)),),
        )


def test_complete_zeta_audit_passes() -> None:
    audit = exact_zeta_audit()
    assert audit
    assert all(audit.values()), audit
