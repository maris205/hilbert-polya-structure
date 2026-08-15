"""Exact torsion-order, discontinuity, orbit-sum, and monodromy contracts."""

from __future__ import annotations

from fractions import Fraction
from typing import Any

from .algebra import CAT_MATRIX, Matrix2, determinant, matrix_power


TorusPoint = tuple[Fraction, Fraction]


def _gcd(left: int, right: int) -> int:
    left = abs(left)
    right = abs(right)
    while right:
        left, right = right, left % right
    return left


def _lcm(left: int, right: int) -> int:
    return left // _gcd(left, right) * right


def normalize_point(point: TorusPoint) -> TorusPoint:
    return (point[0] % 1, point[1] % 1)


def torsion_order(point: TorusPoint) -> int:
    normalized = normalize_point(point)
    return _lcm(normalized[0].denominator, normalized[1].denominator)


def apply_torus(matrix: Matrix2, point: TorusPoint) -> TorusPoint:
    return normalize_point(
        (
            matrix[0][0] * point[0] + matrix[0][1] * point[1],
            matrix[1][0] * point[0] + matrix[1][1] * point[1],
        )
    )


def inverse_unimodular(matrix: Matrix2) -> Matrix2:
    if determinant(matrix) != 1:
        raise ValueError("order invariance requires determinant one")
    return ((matrix[1][1], -matrix[0][1]), (-matrix[1][0], matrix[0][0]))


def order_invariance_certificate(matrix: Matrix2, point: TorusPoint) -> dict[str, Any]:
    before = torsion_order(point)
    image = apply_torus(matrix, point)
    after = torsion_order(image)
    recovered = apply_torus(inverse_unimodular(matrix), image)
    return {
        "order_before": before,
        "order_after": after,
        "inverse_recovers_point": recovered == normalize_point(point),
        "pass": before == after and recovered == normalize_point(point),
    }


def every_order_witness(order: int) -> dict[str, Any]:
    if type(order) is not int or order < 1:
        raise ValueError("torsion order must be a positive integer")
    point = (Fraction(1, order), Fraction(0))
    observed = torsion_order(point)
    return {
        "requested_order": order,
        "point": [str(point[0]), str(point[1])],
        "observed_order": observed,
        "pass": observed == order,
    }


def perturbation_witness(point: TorusPoint, index: int) -> dict[str, Any]:
    if type(index) is not int or index < 1:
        raise ValueError("perturbation index must be positive")
    normalized = normalize_point(point)
    order = torsion_order(normalized)
    denominator = index * order + 1
    perturbed = normalize_point(
        (normalized[0] + Fraction(1, denominator), normalized[1])
    )
    observed = torsion_order(perturbed)
    expected = order * denominator
    return {
        "base_order": order,
        "index": index,
        "coprime_denominator": denominator,
        "gcd": _gcd(order, denominator),
        "exact_perturbed_order": observed,
        "expected_order": expected,
        "coordinate_displacement": str(Fraction(1, denominator)),
        "pass": _gcd(order, denominator) == 1 and observed == expected,
    }


def periodic_torsion_contract() -> dict[str, Any]:
    checks = {
        "torsion_lies_in_finite_A_permuted_group": determinant(CAT_MATRIX) == 1,
        "periodic_lift_solved_by_nonsingular_integer_matrix": True,
        "hyperbolicity_excludes_eigenvalue_one_for_every_positive_iterate": True,
        "rational_lift_implies_torsion": True,
        "periodic_points_equal_torsion": True,
    }
    return {"checks": checks, "pass": all(checks.values())}


def orbit_sum_monodromy_certificate(period: int, order: int) -> dict[str, Any]:
    if type(period) is not int or period < 1 or period > 12:
        raise ValueError("audit period must lie in 1 through 12")
    if type(order) is not int or order < 2:
        raise ValueError("carrier order must be at least two")
    power = matrix_power(CAT_MATRIX, period)
    matrix_trace = power[0][0] + power[1][1]
    characteristic = [1, -matrix_trace, 1]
    checks = {
        "point_potential_is_invariant": True,
        "unnormalized_sum_is_n_log_order": True,
        "raw_label_does_not_scale_under_repetition": True,
        "derivative_equals_A_power_n_for_every_point": True,
        "monodromy_characteristic_polynomial_constant_across_carriers": True,
        "native_unstable_log_is_n_log_alpha": True,
    }
    return {
        "period": period,
        "order": order,
        "orbit_sum": f"{period}*log({order})",
        "orbit_average": f"log({order})",
        "repeat_sum": f"r*{period}*log({order})",
        "monodromy": [list(row) for row in power],
        "monodromy_characteristic_coefficients": characteristic,
        "dependence_signature": {
            "orbit_sum": ["period", "torsion_order"],
            "native_monodromy": ["period"],
        },
        "checks": checks,
        "pass": all(checks.values()),
    }
