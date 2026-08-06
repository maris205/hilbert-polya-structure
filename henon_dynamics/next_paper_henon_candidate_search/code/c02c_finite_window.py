#!/usr/bin/env python3
"""HCS-C02C producer: effective finite-window H_6 pinning certificate.

Exact constants use Fraction arithmetic.  Complex floating computations are
adversarial/regression checks of the analytic derivation frozen in
C02C_FINITE_WINDOW_PROTOCOL.md; they are not the proof of the all-length
statements.
"""

from __future__ import annotations

import argparse
import cmath
import csv
import hashlib
import itertools
import json
import math
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence

import mpmath as mp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = PROJECT_ROOT / "results" / "c02c_finite_window"

CENTER = Fraction(23, 48)
RADIUS = Fraction(7, 48)
FIBRE_RADIUS = Fraction(123, 224)

POLE_CENTER = Fraction(23, 4)
DENOMINATOR_RADIUS = Fraction(515, 224)
POLE_CLEARANCE = Fraction(773, 224)
RECIPROCAL_DENOMINATOR = Fraction(1393719, 50176)
CHILD_CENTER = Fraction(288512, 1393719)
CHILD_RADIUS = Fraction(115360, 1393719)
CHILD_INNER = Fraction(224, 1803)
CHILD_OUTER = Fraction(224, 773)
CHILD_GAP = Fraction(448, 1803)
PARENT_MARGIN = Fraction(44903, 173152)
FIBRE_DERIVATIVE = Fraction(50176, 597529)
BASE_DERIVATIVE = Fraction(602112, 597529)

LEGACY_CHILD_CENTER = Fraction(23, 120)
LEGACY_CHILD_RADIUS = Fraction(9101, 92760)
LEGACY_CHILD_GAP = Fraction(4339, 23190)

DEFAULT_TOLERANCE = 1.0e-13
DISPLAY_TOLERANCE = 5.0e-11
MAX_ITERATIONS = 10000
MP_DPS = 100


def frac_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def sign_text(signs: Sequence[int]) -> str:
    return "".join("+" if sign > 0 else "-" for sign in signs)


def sign_words(length: int) -> Iterable[tuple[int, ...]]:
    return itertools.product((-1, 1), repeat=length)


def extended_admissible(signs: Sequence[int]) -> bool:
    return all(
        not (signs[index - 1] == 1 and signs[index + 1] == 1)
        for index in range(1, len(signs) - 1)
    )


def cyclic_admissible(signs: Sequence[int]) -> bool:
    length = len(signs)
    return all(
        not (
            signs[(index - 1) % length] == 1
            and signs[(index + 1) % length] == 1
        )
        for index in range(length)
    )


def minimal_word_period(signs: Sequence[int]) -> int:
    length = len(signs)
    for period in range(1, length + 1):
        if length % period == 0 and all(
            signs[index] == signs[index % period] for index in range(length)
        ):
            return period
    raise AssertionError("word period not found")


def principal_signed_root(sign: int, radicand: complex) -> complex:
    return sign * cmath.sqrt(radicand)


def solve_window(
    signs: Sequence[int],
    left_endpoint: complex,
    right_endpoint: complex,
    tolerance: float = DEFAULT_TOLERANCE,
    max_iterations: int = MAX_ITERATIONS,
) -> tuple[list[complex], int, float]:
    if len(signs) < 3 or not extended_admissible(signs):
        raise ValueError("window requires a locally admissible extended word")
    internal = [complex(sign * float(CENTER), 0.0) for sign in signs[1:-1]]
    last_increment = math.inf
    for iteration in range(1, max_iterations + 1):
        extended = [left_endpoint, *internal, right_endpoint]
        updated = []
        for index, sign in enumerate(signs[1:-1], start=1):
            radicand = (1.0 - extended[index - 1] - extended[index + 1]) / 6.0
            updated.append(principal_signed_root(sign, radicand))
        last_increment = max(
            abs(new - old) for new, old in zip(updated, internal)
        )
        internal = updated
        if last_increment <= tolerance:
            return internal, iteration, last_increment
    raise RuntimeError(
        f"window fixed point did not converge for {sign_text(signs)}; "
        f"last increment={last_increment:.3e}"
    )


def solve_cyclic(
    signs: Sequence[int],
    tolerance: float = DEFAULT_TOLERANCE,
    max_iterations: int = MAX_ITERATIONS,
) -> tuple[list[complex], int, float]:
    if not signs or not cyclic_admissible(signs):
        raise ValueError("cyclic word is not admissible")
    values = [complex(sign * float(CENTER), 0.0) for sign in signs]
    length = len(values)
    last_increment = math.inf
    for iteration in range(1, max_iterations + 1):
        updated = []
        for index, sign in enumerate(signs):
            radicand = (
                1.0
                - values[(index - 1) % length]
                - values[(index + 1) % length]
            ) / 6.0
            updated.append(principal_signed_root(sign, radicand))
        last_increment = max(abs(new - old) for new, old in zip(updated, values))
        values = updated
        if last_increment <= tolerance:
            return values, iteration, last_increment
    raise RuntimeError(
        f"cyclic fixed point did not converge for {sign_text(signs)}; "
        f"last increment={last_increment:.3e}"
    )


def mp_complex(value: complex) -> mp.mpc:
    """Convert a binary complex value without introducing further rounding."""

    return mp.mpc(repr(value.real), repr(value.imag))


def high_precision_window(
    signs: Sequence[int],
    left_endpoint: complex,
    right_endpoint: complex,
    initial_values: Sequence[complex],
) -> dict[str, float]:
    """Refine one open window and audit the crossed identity at 100 digits."""

    with mp.workdps(MP_DPS):
        left = mp_complex(left_endpoint)
        right = mp_complex(right_endpoint)
        values = [mp_complex(value) for value in initial_values]
        target = mp.mpf("1e-85")
        for _ in range(MAX_ITERATIONS):
            extended = [left, *values, right]
            updated = [
                sign
                * mp.sqrt(
                    (1 - extended[index - 1] - extended[index + 1]) / 6
                )
                for index, sign in enumerate(signs[1:-1], start=1)
            ]
            increment = max(abs(new - old) for new, old in zip(updated, values))
            values = updated
            if increment < target:
                break
        else:
            raise RuntimeError("high-precision open refinement did not converge")
        extended = [left, *values, right]
        recurrence = max(
            abs(
                1
                - 6 * extended[index] * extended[index]
                - extended[index - 1]
                - extended[index + 1]
            )
            for index in range(1, len(extended) - 1)
        )
        q, p = values[0], left
        for _ in values:
            q, p = 1 - 6 * q * q - p, q
        crossed = max(abs(q - right), abs(p - values[-1]))
        return {
            "recurrence_residual": float(recurrence),
            "crossed_residual": float(crossed),
        }


def high_precision_cyclic(
    signs: Sequence[int], initial_values: Sequence[complex]
) -> dict[str, float]:
    """Refine a cyclic word and audit determinant identities at 100 digits."""

    with mp.workdps(MP_DPS):
        values = [mp_complex(value) for value in initial_values]
        length = len(values)
        target = mp.mpf("1e-85")
        for _ in range(MAX_ITERATIONS):
            updated = [
                sign
                * mp.sqrt(
                    (
                        1
                        - values[(index - 1) % length]
                        - values[(index + 1) % length]
                    )
                    / 6
                )
                for index, sign in enumerate(signs)
            ]
            increment = max(abs(new - old) for new, old in zip(updated, values))
            values = updated
            if increment < target:
                break
        else:
            raise RuntimeError("high-precision cyclic refinement did not converge")

        open_matrix = mp.matrix(length)
        cyclic_matrix = mp.matrix(length)
        for row in range(length):
            for column in range(length):
                open_matrix[row, column] = 0
                cyclic_matrix[row, column] = 0
            open_matrix[row, row] = -12 * values[row]
            if row > 0:
                open_matrix[row, row - 1] = -1
            if row + 1 < length:
                open_matrix[row, row + 1] = -1
            cyclic_matrix[row, row] += -12 * values[row]
            cyclic_matrix[row, (row - 1) % length] -= 1
            cyclic_matrix[row, (row + 1) % length] -= 1

        theta = mp.det(open_matrix)
        left_rhs = mp.matrix(length, 1)
        right_rhs = mp.matrix(length, 1)
        for index in range(length):
            left_rhs[index] = 0
            right_rhs[index] = 0
        left_rhs[0] = 1
        right_rhs[length - 1] = 1
        left_derivative = mp.lu_solve(open_matrix, left_rhs)
        right_derivative = mp.lu_solve(open_matrix, right_rhs)
        matching = mp.matrix(
            [
                [left_derivative[length - 1] - 1, right_derivative[length - 1]],
                [left_derivative[0], right_derivative[0] - 1],
            ]
        )

        monodromy_mp = mp.eye(2)
        for value in values:
            monodromy_mp = mp.matrix([[-12 * value, -1], [1, 0]]) * monodromy_mp
        det_i_minus_m = mp.det(mp.eye(2) - monodromy_mp)
        matching_error = abs(mp.det(matching) + det_i_minus_m / theta)
        hill_error = abs(mp.det(cyclic_matrix) + det_i_minus_m)
        cyclic_residual_hp = max(
            abs(
                1
                - 6 * values[index] * values[index]
                - values[(index - 1) % length]
                - values[(index + 1) % length]
            )
            for index in range(length)
        )
        return {
            "cyclic_residual": float(cyclic_residual_hp),
            "matching_error": float(matching_error),
            "hill_error": float(hill_error),
        }


def window_residual(
    values: Sequence[complex], left_endpoint: complex, right_endpoint: complex
) -> float:
    extended = [left_endpoint, *values, right_endpoint]
    return max(
        abs(
            1.0
            - 6.0 * extended[index] * extended[index]
            - extended[index - 1]
            - extended[index + 1]
        )
        for index in range(1, len(extended) - 1)
    )


def cyclic_residual(values: Sequence[complex]) -> float:
    length = len(values)
    return max(
        abs(
            1.0
            - 6.0 * values[index] * values[index]
            - values[(index - 1) % length]
            - values[(index + 1) % length]
        )
        for index in range(length)
    )


def disk_margin(values: Sequence[complex], signs: Sequence[int]) -> float:
    return min(
        float(RADIUS) - abs(value - sign * float(CENTER))
        for value, sign in zip(values, signs)
    )


def solve_dense(matrix: Sequence[Sequence[complex]], rhs: Sequence[complex]) -> list[complex]:
    size = len(rhs)
    augmented = [
        [complex(value) for value in row] + [complex(rhs[index])]
        for index, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = max(range(column, size), key=lambda row: abs(augmented[row][column]))
        if abs(augmented[pivot][column]) < 1.0e-30:
            raise ZeroDivisionError("singular dense system")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        for entry in range(column, size + 1):
            augmented[column][entry] /= pivot_value
        for row in range(size):
            if row == column:
                continue
            multiplier = augmented[row][column]
            if multiplier == 0:
                continue
            for entry in range(column, size + 1):
                augmented[row][entry] -= multiplier * augmented[column][entry]
    return [augmented[row][size] for row in range(size)]


def determinant_dense(matrix: Sequence[Sequence[complex]]) -> complex:
    size = len(matrix)
    work = [[complex(value) for value in row] for row in matrix]
    determinant = 1.0 + 0.0j
    sign = 1
    for column in range(size):
        pivot = max(range(column, size), key=lambda row: abs(work[row][column]))
        if abs(work[pivot][column]) < 1.0e-30:
            return 0.0 + 0.0j
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            sign *= -1
        pivot_value = work[column][column]
        determinant *= pivot_value
        for row in range(column + 1, size):
            multiplier = work[row][column] / pivot_value
            for entry in range(column + 1, size):
                work[row][entry] -= multiplier * work[column][entry]
    return sign * determinant


def continuant(coefficients: Sequence[complex]) -> complex:
    previous_previous = 1.0 + 0.0j
    if not coefficients:
        return previous_previous
    previous = complex(coefficients[0])
    for coefficient in coefficients[1:]:
        current = coefficient * previous - previous_previous
        previous_previous, previous = previous, current
    return previous


def matmul2(
    left: Sequence[Sequence[complex]], right: Sequence[Sequence[complex]]
) -> list[list[complex]]:
    return [
        [
            sum(left[row][inner] * right[inner][column] for inner in range(2))
            for column in range(2)
        ]
        for row in range(2)
    ]


def det2(matrix: Sequence[Sequence[complex]]) -> complex:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def matrix_norm_max(matrix: Sequence[Sequence[complex]]) -> float:
    return max(abs(value) for row in matrix for value in row)


def matrix_difference_norm(
    left: Sequence[Sequence[complex]], right: Sequence[Sequence[complex]]
) -> float:
    return max(
        abs(left[row][column] - right[row][column])
        for row in range(2)
        for column in range(2)
    )


def monodromy(values: Sequence[complex], reverse: bool = False) -> list[list[complex]]:
    result = [[1.0 + 0.0j, 0.0 + 0.0j], [0.0 + 0.0j, 1.0 + 0.0j]]
    ordered = list(reversed(values)) if reverse else list(values)
    for value in ordered:
        jacobian = [[-12.0 * value, -1.0 + 0.0j], [1.0 + 0.0j, 0.0j]]
        result = matmul2(jacobian, result)
    return result


def iterate_state(
    q: complex, p: complex, steps: int
) -> tuple[complex, complex]:
    for _ in range(steps):
        q, p = 1.0 - 6.0 * q * q - p, q
    return q, p


def window_differentials(values: Sequence[complex]) -> dict[str, object]:
    length = len(values)
    neighbor_derivatives = [-1.0 / (12.0 * value) for value in values]
    fixed_matrix = [
        [0.0 + 0.0j for _ in range(length)] for _ in range(length)
    ]
    for row in range(length):
        fixed_matrix[row][row] = 1.0 + 0.0j
        if row > 0:
            fixed_matrix[row][row - 1] = -neighbor_derivatives[row]
        if row + 1 < length:
            fixed_matrix[row][row + 1] = -neighbor_derivatives[row]
    left_rhs = [0.0 + 0.0j for _ in range(length)]
    right_rhs = [0.0 + 0.0j for _ in range(length)]
    left_rhs[0] = neighbor_derivatives[0]
    right_rhs[-1] = neighbor_derivatives[-1]
    left_derivative = solve_dense(fixed_matrix, left_rhs)
    right_derivative = solve_dense(fixed_matrix, right_rhs)

    orbit_coefficients = [-12.0 * value for value in values]
    theta = continuant(orbit_coefficients)
    left_formula = [
        continuant(orbit_coefficients[index + 1 :]) / theta
        for index in range(length)
    ]
    right_formula = [
        continuant(orbit_coefficients[:index]) / theta
        for index in range(length)
    ]
    return {
        "neighbor_derivatives": neighbor_derivatives,
        "left": left_derivative,
        "right": right_derivative,
        "left_formula": left_formula,
        "right_formula": right_formula,
        "theta": theta,
        "orbit_coefficients": orbit_coefficients,
    }


def projective_chain(
    values: Sequence[complex],
    left_derivative: Sequence[complex],
    right_derivative: Sequence[complex],
    initial_slope: complex = 0.0 + 0.0j,
) -> dict[str, complex]:
    slope = initial_slope
    derivative_initial = 1.0 + 0.0j
    derivative_left = 0.0 + 0.0j
    derivative_right = 0.0 + 0.0j
    for value, value_left, value_right in zip(
        values, left_derivative, right_derivative
    ):
        denominator = -12.0 * value - slope
        derivative_m = 1.0 / (denominator * denominator)
        derivative_q = 12.0 / (denominator * denominator)
        slope = 1.0 / denominator
        derivative_initial = derivative_m * derivative_initial
        derivative_left = derivative_m * derivative_left + derivative_q * value_left
        derivative_right = derivative_m * derivative_right + derivative_q * value_right
    return {
        "slope": slope,
        "initial": derivative_initial,
        "left": derivative_left,
        "right": derivative_right,
    }


def analyze_window(
    signs: Sequence[int],
    left_endpoint: complex,
    right_endpoint: complex,
    tolerance: float,
) -> dict[str, object]:
    values, iterations, increment = solve_window(
        signs, left_endpoint, right_endpoint, tolerance
    )
    differentials = window_differentials(values)
    left_derivative = differentials["left"]
    right_derivative = differentials["right"]
    theta = differentials["theta"]
    ordered_monodromy = monodromy(values)
    crossed_output = iterate_state(values[0], left_endpoint, len(values))
    crossed_residual = max(
        abs(crossed_output[0] - right_endpoint),
        abs(crossed_output[1] - values[-1]),
    )

    a0 = 1.0 / math.sqrt(17.0)
    kappa = 2.0 / math.sqrt(17.0)
    beta = a0 / (1.0 - kappa)
    left_bounds = [beta * kappa**index for index in range(len(values))]
    right_bounds = [
        beta * kappa ** (len(values) - 1 - index)
        for index in range(len(values))
    ]
    left_ratio = max(
        abs(value) / bound for value, bound in zip(left_derivative, left_bounds)
    )
    right_ratio = max(
        abs(value) / bound for value, bound in zip(right_derivative, right_bounds)
    )

    formula_error = max(
        max(
            abs(value - formula)
            for value, formula in zip(left_derivative, differentials["left_formula"])
        ),
        max(
            abs(value - formula)
            for value, formula in zip(right_derivative, differentials["right_formula"])
        ),
    )

    projective = projective_chain(values, left_derivative, right_derivative)
    delta = float(FIBRE_DERIVATIVE)
    projective_left_bound = (
        12.0
        * delta
        * beta
        * (kappa ** len(values) - delta ** len(values))
        / (kappa - delta)
    )
    projective_right_bound = (
        12.0
        * delta
        * beta
        * (1.0 - (delta * kappa) ** len(values))
        / (1.0 - delta * kappa)
    )

    return {
        "values": values,
        "iterations": iterations,
        "increment": increment,
        "residual": window_residual(values, left_endpoint, right_endpoint),
        "disk_margin": disk_margin(values, signs[1:-1]),
        "crossed_residual": crossed_residual,
        "left_derivative": left_derivative,
        "right_derivative": right_derivative,
        "left_bound_ratio": left_ratio,
        "right_bound_ratio": right_ratio,
        "endpoint_formula_error": formula_error,
        "endpoint_reciprocity_error": abs(right_derivative[0] - left_derivative[-1]),
        "theta": theta,
        "theta_monodromy_error": abs(theta - ordered_monodromy[0][0]),
        "monodromy": ordered_monodromy,
        "projective": projective,
        "projective_initial_ratio": abs(projective["initial"]) / delta ** len(values),
        "projective_left_ratio": abs(projective["left"]) / projective_left_bound,
        "projective_right_ratio": abs(projective["right"]) / projective_right_bound,
        "projective_left_bound": projective_left_bound,
        "projective_right_bound": projective_right_bound,
    }


def cyclic_jacobian(values: Sequence[complex]) -> list[list[complex]]:
    length = len(values)
    matrix = [[0.0 + 0.0j for _ in range(length)] for _ in range(length)]
    for index, value in enumerate(values):
        matrix[index][index] += -12.0 * value
        matrix[index][(index - 1) % length] -= 1.0
        matrix[index][(index + 1) % length] -= 1.0
    return matrix


def unstable_eigendata(matrix: Sequence[Sequence[complex]]) -> tuple[complex, complex]:
    trace = matrix[0][0] + matrix[1][1]
    discriminant = cmath.sqrt(trace * trace - 4.0)
    candidates = ((trace + discriminant) / 2.0, (trace - discriminant) / 2.0)
    eigenvalue = max(candidates, key=abs)
    if abs(matrix[0][1]) > 1.0e-14:
        slope = (eigenvalue - matrix[0][0]) / matrix[0][1]
    else:
        slope = matrix[1][0] / (eigenvalue - matrix[1][1])
    return eigenvalue, slope


def projective_periodic_audit(
    values: Sequence[complex], matrix: Sequence[Sequence[complex]]
) -> tuple[float, float]:
    eigenvalue, initial_slope = unstable_eigendata(matrix)
    slope = initial_slope
    expansion = 1.0 + 0.0j
    for value in values:
        factor = -12.0 * value - slope
        expansion *= factor
        slope = 1.0 / factor
    return abs(slope - initial_slope), abs(expansion - eigenvalue) / max(1.0, abs(eigenvalue))


def projective_exact_audit() -> dict[str, object]:
    checks = {
        "denominator_radius": DENOMINATOR_RADIUS
        == 12 * RADIUS + FIBRE_RADIUS,
        "pole_clearance": POLE_CLEARANCE == POLE_CENTER - DENOMINATOR_RADIUS
        and POLE_CLEARANCE > 0,
        "reciprocal_denominator": RECIPROCAL_DENOMINATOR
        == POLE_CENTER * POLE_CENTER
        - DENOMINATOR_RADIUS * DENOMINATOR_RADIUS,
        "child_center": CHILD_CENTER
        == POLE_CENTER / RECIPROCAL_DENOMINATOR,
        "child_radius": CHILD_RADIUS
        == DENOMINATOR_RADIUS / RECIPROCAL_DENOMINATOR,
        "inner_radius": CHILD_CENTER - CHILD_RADIUS == CHILD_INNER,
        "outer_radius": CHILD_CENTER + CHILD_RADIUS == CHILD_OUTER,
        "child_gap": 2 * CHILD_INNER == CHILD_GAP,
        "parent_margin": FIBRE_RADIUS - CHILD_OUTER == PARENT_MARGIN
        and PARENT_MARGIN > 0,
        "fibre_derivative": CHILD_OUTER * CHILD_OUTER == FIBRE_DERIVATIVE,
        "base_derivative": 12 * FIBRE_DERIVATIVE == BASE_DERIVATIVE,
        "base_not_contraction": BASE_DERIVATIVE > 1,
        "legacy_enclosure": abs(CHILD_CENTER - LEGACY_CHILD_CENTER)
        + CHILD_RADIUS
        == LEGACY_CHILD_RADIUS,
        "legacy_gap": 2 * (LEGACY_CHILD_CENTER - LEGACY_CHILD_RADIUS)
        == LEGACY_CHILD_GAP,
    }

    point_errors: dict[str, float] = {}
    for epsilon in (-1, 1):
        outer = 1.0 / (
            -12.0 * epsilon / 3.0 - (-epsilon * float(FIBRE_RADIUS))
        )
        inner = 1.0 / (
            -12.0 * (5.0 * epsilon / 8.0) - epsilon * float(FIBRE_RADIUS)
        )
        complex_q = epsilon * float(CENTER) - 1j * float(RADIUS)
        complex_m = -1j * float(FIBRE_RADIUS)
        complex_image = 1.0 / (-12.0 * complex_q - complex_m)
        point_errors[f"epsilon_{epsilon}_outer"] = abs(
            outer - (-epsilon * float(CHILD_OUTER))
        )
        point_errors[f"epsilon_{epsilon}_inner"] = abs(
            inner - (-epsilon * float(CHILD_INNER))
        )
        point_errors[f"epsilon_{epsilon}_complex_tangency"] = abs(
            abs(complex_image + epsilon * float(CHILD_CENTER))
            - float(CHILD_RADIUS)
        )
    return {
        "constants": {
            "center": frac_text(CENTER),
            "coordinate_radius": frac_text(RADIUS),
            "parent_fibre_radius": frac_text(FIBRE_RADIUS),
            "denominator_center_magnitude": frac_text(POLE_CENTER),
            "denominator_radius": frac_text(DENOMINATOR_RADIUS),
            "pole_clearance": frac_text(POLE_CLEARANCE),
            "child_center_magnitude": frac_text(CHILD_CENTER),
            "child_radius": frac_text(CHILD_RADIUS),
            "child_inner_radius": frac_text(CHILD_INNER),
            "child_outer_radius": frac_text(CHILD_OUTER),
            "child_gap": frac_text(CHILD_GAP),
            "parent_margin": frac_text(PARENT_MARGIN),
            "fibre_derivative_bound": frac_text(FIBRE_DERIVATIVE),
            "base_derivative_bound": frac_text(BASE_DERIVATIVE),
        },
        "checks": checks,
        "point_errors": point_errors,
        "all_checks_pass": all(checks.values())
        and max(point_errors.values(), default=0.0) < 2.0e-15,
    }


def run_open_windows(max_length: int, tolerance: float) -> tuple[list[dict[str, object]], dict[str, object]]:
    rows: list[dict[str, object]] = []
    expected_counts: dict[str, int] = {}
    maxima = {
        "residual": 0.0,
        "crossed_residual": 0.0,
        "float64_forward_crossed_residual": 0.0,
        "left_bound_ratio": 0.0,
        "right_bound_ratio": 0.0,
        "endpoint_formula_error": 0.0,
        "endpoint_reciprocity_error": 0.0,
        "theta_monodromy_error": 0.0,
        "projective_initial_ratio": 0.0,
        "projective_left_ratio": 0.0,
        "projective_right_ratio": 0.0,
    }
    minimum_disk_margin = math.inf
    for length in range(1, max_length + 1):
        admissible = [
            tuple(signs)
            for signs in sign_words(length + 2)
            if extended_admissible(signs)
        ]
        expected_counts[str(length)] = len(admissible)
        for signs in admissible:
            analysis = analyze_window(
                signs,
                signs[0] * float(CENTER),
                signs[-1] * float(CENTER),
                tolerance,
            )
            high_precision = high_precision_window(
                signs,
                signs[0] * float(CENTER),
                signs[-1] * float(CENTER),
                analysis["values"],
            )
            case_id = f"N{length}:{sign_text(signs)}"
            row = {
                "case_id": case_id,
                "length": length,
                "extended_signs": sign_text(signs),
                "iterations": analysis["iterations"],
                "fixed_point_increment": analysis["increment"],
                "recurrence_residual": analysis["residual"],
                "minimum_disk_margin": analysis["disk_margin"],
                "crossed_residual": high_precision["crossed_residual"],
                "float64_forward_crossed_residual": analysis[
                    "crossed_residual"
                ],
                "left_bound_ratio": analysis["left_bound_ratio"],
                "right_bound_ratio": analysis["right_bound_ratio"],
                "endpoint_formula_error": analysis["endpoint_formula_error"],
                "endpoint_reciprocity_error": analysis[
                    "endpoint_reciprocity_error"
                ],
                "theta_monodromy_error": analysis["theta_monodromy_error"],
                "projective_initial_ratio": analysis["projective_initial_ratio"],
                "projective_left_ratio": analysis["projective_left_ratio"],
                "projective_right_ratio": analysis["projective_right_ratio"],
            }
            rows.append(row)
            minimum_disk_margin = min(minimum_disk_margin, analysis["disk_margin"])
            for key in maxima:
                maxima[key] = max(maxima[key], float(row[key if key != "residual" else "recurrence_residual"]))

    angle_pairs = [
        (0.0, 0.0),
        (math.pi / 2.0, -math.pi / 2.0),
        (math.pi, math.pi / 2.0),
        (3.0 * math.pi / 2.0, math.pi / 4.0),
    ]
    boundary_probe_count = 0
    boundary_max_residual = 0.0
    boundary_max_crossed = 0.0
    boundary_min_margin = math.inf
    boundary_max_derivative_ratio = 0.0
    for length in range(1, min(3, max_length) + 1):
        for signs in sign_words(length + 2):
            if not extended_admissible(signs):
                continue
            for left_angle, right_angle in angle_pairs:
                left = signs[0] * float(CENTER) + float(RADIUS) * cmath.exp(
                    1j * left_angle
                )
                right = signs[-1] * float(CENTER) + float(RADIUS) * cmath.exp(
                    1j * right_angle
                )
                analysis = analyze_window(signs, left, right, tolerance)
                boundary_probe_count += 1
                boundary_max_residual = max(
                    boundary_max_residual, analysis["residual"]
                )
                boundary_max_crossed = max(
                    boundary_max_crossed, analysis["crossed_residual"]
                )
                boundary_min_margin = min(
                    boundary_min_margin, analysis["disk_margin"]
                )
                boundary_max_derivative_ratio = max(
                    boundary_max_derivative_ratio,
                    analysis["left_bound_ratio"],
                    analysis["right_bound_ratio"],
                )

    summary = {
        "row_count": len(rows),
        "counts_by_length": expected_counts,
        "expected_first_counts": expected_counts.get("1") == 6
        and expected_counts.get("2") == 9
        and expected_counts.get("3") == 15,
        "complete_case_ids": [row["case_id"] for row in rows],
        "maxima": maxima,
        "minimum_disk_margin": minimum_disk_margin,
        "boundary_probes": {
            "count": boundary_probe_count,
            "expected_count": 4
            * sum(int(expected_counts[str(length)]) for length in range(1, min(3, max_length) + 1)),
            "maximum_recurrence_residual": boundary_max_residual,
            "maximum_crossed_residual": boundary_max_crossed,
            "minimum_disk_margin": boundary_min_margin,
            "maximum_derivative_bound_ratio": boundary_max_derivative_ratio,
        },
    }
    return rows, summary


def run_cyclic_windows(max_length: int, tolerance: float) -> tuple[list[dict[str, object]], dict[str, object]]:
    rows: list[dict[str, object]] = []
    counts: dict[str, int] = {}
    maxima = {
        "cyclic_residual": 0.0,
        "open_cyclic_value_error": 0.0,
        "determinant_identity_error": 0.0,
        "hill_identity_error": 0.0,
        "float64_hill_identity_error": 0.0,
        "projective_fixed_slope_error": 0.0,
        "projective_multiplier_relative_error": 0.0,
        "orientation_failures": 0,
    }
    for length in range(1, max_length + 1):
        admissible = [
            tuple(signs)
            for signs in sign_words(length)
            if cyclic_admissible(signs)
        ]
        counts[str(length)] = len(admissible)
        for signs in admissible:
            values, iterations, increment = solve_cyclic(signs, tolerance)
            extended_signs = (signs[-1], *signs, signs[0])
            open_analysis = analyze_window(
                extended_signs, values[-1], values[0], tolerance
            )
            value_error = max(
                abs(left - right)
                for left, right in zip(values, open_analysis["values"])
            )
            differentials = window_differentials(open_analysis["values"])
            left = differentials["left"]
            right = differentials["right"]
            theta = differentials["theta"]
            matching_derivative = [
                [left[-1] - 1.0, right[-1]],
                [left[0], right[0] - 1.0],
            ]
            matching_determinant = det2(matching_derivative)
            ordered_monodromy = monodromy(values)
            identity_minus_monodromy = [
                [1.0 - ordered_monodromy[0][0], -ordered_monodromy[0][1]],
                [-ordered_monodromy[1][0], 1.0 - ordered_monodromy[1][1]],
            ]
            det_i_minus_m = det2(identity_minus_monodromy)
            cyclic_matrix = cyclic_jacobian(values)
            cyclic_determinant = determinant_dense(cyclic_matrix)
            determinant_error = abs(
                matching_determinant + det_i_minus_m / theta
            )
            hill_error = abs(cyclic_determinant + det_i_minus_m)
            high_precision = high_precision_cyclic(signs, values)
            slope_error, multiplier_error = projective_periodic_audit(
                values, ordered_monodromy
            )
            orientation_prediction = -math.prod(-sign for sign in signs)
            orientation_observed = 1 if det_i_minus_m.real > 0 else -1
            orientation_ok = (
                abs(det_i_minus_m.imag) < DISPLAY_TOLERANCE
                and orientation_prediction == orientation_observed
            )
            if not orientation_ok:
                maxima["orientation_failures"] += 1

            row = {
                "case_id": f"C{length}:{sign_text(signs)}",
                "length": length,
                "cyclic_signs": sign_text(signs),
                "minimal_symbolic_period": minimal_word_period(signs),
                "iterations": iterations,
                "fixed_point_increment": increment,
                "cyclic_residual": cyclic_residual(values),
                "open_cyclic_value_error": value_error,
                "matching_determinant_real": matching_determinant.real,
                "matching_determinant_imag": matching_determinant.imag,
                "det_i_minus_m_real": det_i_minus_m.real,
                "det_i_minus_m_imag": det_i_minus_m.imag,
                "open_theta_real": theta.real,
                "open_theta_imag": theta.imag,
                "determinant_identity_error": high_precision["matching_error"],
                "cyclic_jacobian_determinant_real": cyclic_determinant.real,
                "cyclic_jacobian_determinant_imag": cyclic_determinant.imag,
                "hill_identity_error": high_precision["hill_error"],
                "float64_hill_identity_error": hill_error,
                "projective_fixed_slope_error": slope_error,
                "projective_multiplier_relative_error": multiplier_error,
                "orientation_prediction": orientation_prediction,
                "orientation_observed": orientation_observed,
                "orientation_ok": orientation_ok,
            }
            rows.append(row)
            for key in (
                "cyclic_residual",
                "open_cyclic_value_error",
                "determinant_identity_error",
                "hill_identity_error",
                "float64_hill_identity_error",
                "projective_fixed_slope_error",
                "projective_multiplier_relative_error",
            ):
                maxima[key] = max(maxima[key], float(row[key]))

    return rows, {
        "row_count": len(rows),
        "counts_by_length": counts,
        "complete_case_ids": [row["case_id"] for row in rows],
        "n1_only_negative": counts.get("1") == 1
        and rows[0]["cyclic_signs"] == "-",
        "n2_only_double_negative": counts.get("2") == 1
        and next(row for row in rows if row["length"] == 2)["cyclic_signs"] == "--",
        "maxima": maxima,
    }


def run_gluing_control(tolerance: float) -> tuple[list[dict[str, object]], dict[str, object]]:
    signs = tuple(1 if character == "+" else -1 for character in "++--++--")
    left_endpoint = float(CENTER) + 1j * float(RADIUS)
    right_endpoint = -float(CENTER) + float(RADIUS) * cmath.exp(1j * math.pi / 3.0)
    direct = analyze_window(signs, left_endpoint, right_endpoint, tolerance)
    direct_values = direct["values"]

    split = 3
    xi = signs[split] * float(CENTER)
    eta = signs[split + 1] * float(CENTER)
    last_increment = math.inf
    for interface_iteration in range(1, MAX_ITERATIONS + 1):
        left_signs = signs[: split + 2]
        right_signs = signs[split:]
        left_values, _, _ = solve_window(
            left_signs, left_endpoint, eta, tolerance
        )
        right_values, _, _ = solve_window(
            right_signs, xi, right_endpoint, tolerance
        )
        updated_xi = left_values[-1]
        updated_eta = right_values[0]
        last_increment = max(abs(updated_xi - xi), abs(updated_eta - eta))
        xi, eta = updated_xi, updated_eta
        if last_increment <= tolerance:
            break
    else:
        raise RuntimeError("two-coordinate interface iteration did not converge")

    left_values, _, _ = solve_window(signs[: split + 2], left_endpoint, eta, tolerance)
    right_values, _, _ = solve_window(signs[split:], xi, right_endpoint, tolerance)
    glued_values = [*left_values, *right_values]
    direct_glued_error = max(
        abs(left - right) for left, right in zip(direct_values, glued_values)
    )

    averaged = (xi + eta) / 2.0
    averaged_values = list(direct_values)
    averaged_values[split - 1] = averaged
    averaged_values[split] = averaged
    averaged_residual = window_residual(
        averaged_values, left_endpoint, right_endpoint
    )

    chronological = monodromy(direct_values)
    reversed_product = monodromy(direct_values, reverse=True)
    reversed_error = matrix_difference_norm(chronological, reversed_product)

    rows = [
        {
            "control_id": "G1_TWO_COORDINATE_GLUE",
            "expected": "PASS",
            "observed_metric": direct_glued_error,
            "threshold": DISPLAY_TOLERANCE,
            "passed": direct_glued_error < DISPLAY_TOLERANCE,
        },
        {
            "control_id": "G2_SCALAR_AVERAGE",
            "expected": "FAIL",
            "observed_metric": averaged_residual,
            "threshold": 1.0e-6,
            "passed": averaged_residual > 1.0e-6,
        },
        {
            "control_id": "O1_REVERSED_MONODROMY",
            "expected": "FAIL",
            "observed_metric": reversed_error,
            "threshold": 1.0e-6,
            "passed": reversed_error > 1.0e-6,
        },
    ]
    return rows, {
        "extended_word": sign_text(signs),
        "split_after_internal": split,
        "interface_iterations": interface_iteration,
        "interface_increment": last_increment,
        "interface_pair": {
            "xi_real": xi.real,
            "xi_imag": xi.imag,
            "eta_real": eta.real,
            "eta_imag": eta.imag,
        },
        "direct_glued_error": direct_glued_error,
        "scalar_average_residual": averaged_residual,
        "reversed_monodromy_error": reversed_error,
        "all_controls_pass": all(row["passed"] for row in rows),
    }


def write_csv(path: Path, rows: Sequence[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"refusing to write empty CSV: {path}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--max-open-length", type=int, default=8)
    parser.add_argument("--max-cyclic-length", type=int, default=8)
    parser.add_argument("--tolerance", type=float, default=DEFAULT_TOLERANCE)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not 3 <= args.max_open_length <= 12:
        raise SystemExit("require 3 <= max-open-length <= 12")
    if not 2 <= args.max_cyclic_length <= 12:
        raise SystemExit("require 2 <= max-cyclic-length <= 12")
    if not 0.0 < args.tolerance <= 1.0e-10:
        raise SystemExit("tolerance must lie in (0, 1e-10]")
    args.output_dir.mkdir(parents=True, exist_ok=True)

    projective = projective_exact_audit()
    open_rows, open_summary = run_open_windows(args.max_open_length, args.tolerance)
    cyclic_rows, cyclic_summary = run_cyclic_windows(
        args.max_cyclic_length, args.tolerance
    )
    gluing_rows, gluing_summary = run_gluing_control(args.tolerance)

    open_checks = {
        "expected_first_counts": open_summary["expected_first_counts"],
        "positive_disk_margin": open_summary["minimum_disk_margin"] > 0.0,
        "boundary_probe_count": open_summary["boundary_probes"]["count"]
        == open_summary["boundary_probes"]["expected_count"],
        "boundary_positive_disk_margin": open_summary["boundary_probes"][
            "minimum_disk_margin"
        ]
        > 0.0,
        "residual": open_summary["maxima"]["residual"] < DISPLAY_TOLERANCE,
        "boundary_residual": open_summary["boundary_probes"][
            "maximum_recurrence_residual"
        ]
        < DISPLAY_TOLERANCE,
        "crossed_identity": open_summary["maxima"]["crossed_residual"]
        < DISPLAY_TOLERANCE,
        "boundary_crossed_identity": open_summary["boundary_probes"][
            "maximum_crossed_residual"
        ]
        < DISPLAY_TOLERANCE,
        "left_localization": open_summary["maxima"]["left_bound_ratio"]
        <= 1.0 + 1.0e-10,
        "right_localization": open_summary["maxima"]["right_bound_ratio"]
        <= 1.0 + 1.0e-10,
        "boundary_localization": open_summary["boundary_probes"][
            "maximum_derivative_bound_ratio"
        ]
        <= 1.0 + 1.0e-10,
        "continuant_endpoint_formula": open_summary["maxima"][
            "endpoint_formula_error"
        ]
        < DISPLAY_TOLERANCE,
        "endpoint_reciprocity": open_summary["maxima"][
            "endpoint_reciprocity_error"
        ]
        < DISPLAY_TOLERANCE,
        "theta_monodromy": open_summary["maxima"]["theta_monodromy_error"]
        < DISPLAY_TOLERANCE,
        "projective_initial_memory": open_summary["maxima"][
            "projective_initial_ratio"
        ]
        <= 1.0 + 1.0e-10,
        "projective_left_endpoint": open_summary["maxima"][
            "projective_left_ratio"
        ]
        <= 1.0 + 1.0e-10,
        "projective_right_endpoint": open_summary["maxima"][
            "projective_right_ratio"
        ]
        <= 1.0 + 1.0e-10,
    }
    cyclic_checks = {
        "n1_chronology": cyclic_summary["n1_only_negative"],
        "n2_chronology": cyclic_summary["n2_only_double_negative"],
        "cyclic_residual": cyclic_summary["maxima"]["cyclic_residual"]
        < DISPLAY_TOLERANCE,
        "cyclic_open_equivalence": cyclic_summary["maxima"][
            "open_cyclic_value_error"
        ]
        < DISPLAY_TOLERANCE,
        "matching_determinant": cyclic_summary["maxima"][
            "determinant_identity_error"
        ]
        < DISPLAY_TOLERANCE,
        "hill_determinant": cyclic_summary["maxima"]["hill_identity_error"]
        < DISPLAY_TOLERANCE,
        "projective_fixed_slope": cyclic_summary["maxima"][
            "projective_fixed_slope_error"
        ]
        < DISPLAY_TOLERANCE,
        "projective_multiplier": cyclic_summary["maxima"][
            "projective_multiplier_relative_error"
        ]
        < DISPLAY_TOLERANCE,
        "orientation_character": cyclic_summary["maxima"][
            "orientation_failures"
        ]
        == 0,
    }
    all_checks = {
        "projective_exact": projective["all_checks_pass"],
        "open_windows": all(open_checks.values()),
        "cyclic_matching": all(cyclic_checks.values()),
        "gluing_and_expected_fail_controls": gluing_summary[
            "all_controls_pass"
        ],
    }

    open_path = args.output_dir / "open_windows.csv"
    cyclic_path = args.output_dir / "cyclic_matching.csv"
    gluing_path = args.output_dir / "gluing_controls.csv"
    write_csv(open_path, open_rows)
    write_csv(cyclic_path, cyclic_rows)
    write_csv(gluing_path, gluing_rows)

    report = {
        "run_id": "HCS_C02C_FINITE_WINDOW_V1",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "protocol": "code/C02C_FINITE_WINDOW_PROTOCOL.md",
        "object": {
            "map": "H_6(q,p)=(1-6q^2-p,q)",
            "clock": "one discrete H_6 iterate",
            "endpoint_center": frac_text(CENTER),
            "endpoint_radius": frac_text(RADIUS),
            "principal_square_root": True,
            "chronology": "ordered; duplicate n=1,2 neighbor occurrences retained",
        },
        "analytic_constants": {
            "a0": "1/sqrt(17)",
            "kappa": "2/sqrt(17)",
            "beta": "1/(sqrt(17)-2)",
            "a0_float": 1.0 / math.sqrt(17.0),
            "kappa_float": 2.0 / math.sqrt(17.0),
            "beta_float": 1.0 / (math.sqrt(17.0) - 2.0),
            "joint_endpoint_constant_float": 2.0
            / (math.sqrt(17.0) - 2.0),
        },
        "precision": {
            "primary_regression": "binary64 complex arithmetic",
            "global_crossed_and_hill_recheck_decimal_digits": MP_DPS,
            "conditioning_note": (
                "Binary64 local residuals are retained, but hyperbolic forward "
                "iteration and large determinant subtraction amplify them at "
                "length eight. The same frozen cases are therefore refined at "
                "100 decimal digits for global identities."
            ),
        },
        "projective_complex_base": projective,
        "open_windows": open_summary,
        "open_checks": open_checks,
        "cyclic_matching": cyclic_summary,
        "cyclic_checks": cyclic_checks,
        "gluing_controls": gluing_summary,
        "checks": all_checks,
        "all_checks_pass": all(all_checks.values()),
        "theorem_status": {
            "finite_window_holomorphic_solver": "PROVED_ANALYTICALLY_REGRESSION_PASS"
            if all(all_checks.values())
            else "FAILED_REGRESSION",
            "matching_hill_identity": "PROVED_ANALYTICALLY_REGRESSION_PASS"
            if all(cyclic_checks.values())
            else "FAILED_REGRESSION",
            "complex_projective_fibre": "PROVED_EXACT"
            if projective["all_checks_pass"]
            else "FAILED",
            "nuclear_operator": "NOT_ESTABLISHED",
            "fredholm_determinant": "NOT_ESTABLISHED",
            "route_a_a2": "DO_NOT_PROMOTE",
        },
        "novelty_ruling": (
            "The conjugate real signed-root SFT/uniqueness, general complex "
            "pinning/composition, and absolute-denominator Fredholm mechanism "
            "are prior art. Retain C02C as an effective complex H_6 "
            "specialization with unconfirmed novelty; a paper still requires "
            "a genuinely new signed aggregate operator truncation/error theorem."
        ),
        "artifacts": {
            "open_windows": open_path.name,
            "cyclic_matching": cyclic_path.name,
            "gluing_controls": gluing_path.name,
        },
    }
    certificate_path = args.output_dir / "certificate.json"
    certificate_path.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    results_text = rf"""# HCS-C02C finite-window results

Status: **{'PASS' if report['all_checks_pass'] else 'FAIL'}**  
Run ID: `HCS_C02C_FINITE_WINDOW_V1`

## Outcome

The analytic finite-window pinning, chronological gluing, matching/Hill
determinant, and complex-base projective certificates are consistent with all
frozen adversarial checks.  The result is an effective specialization of
known pinning theory, not a new general pinning or Fredholm theorem.

## Frozen object

\[
H_6(q,p)=(1-6q^2-p,q),\qquad
D_\sigma=\overline D(\sigma\,23/48,7/48).
\]

Open ledgers: {open_summary['row_count']} complete sign cases through
\(N={args.max_open_length}\).  Cyclic ledgers: {cyclic_summary['row_count']}
complete sign words through \(N={args.max_cyclic_length}\).  Short-window
complex boundary probes executed: {open_summary['boundary_probes']['count']};
their count and extrema are persisted in `certificate.json` rather than as
individual CSV rows.

## Strongest exact additions

- one-sided endpoint bounds
  \(|Q_{{i,u}}|\le\beta\kappa^{{i-1}}\) and
  \(|Q_{{i,v}}|\le\beta\kappa^{{N-i}}\), with
  \(\kappa=2/\sqrt{{17}}\),
  \(\beta=1/(\sqrt{{17}}-2)\);
- exact two-coordinate gluing, with scalar averaging rejected by the frozen
  expected-fail control;
- matching/Hill identity
  \[
  \det DF_N=-\frac{{\det(I-DH_6^N)}}{{\det L_N}}
  =\frac{{\det C_N}}{{\det L_N}};
  \]
- exact complex-base projective child disks
  \[
  D\left(-\varepsilon\frac{{288512}}{{1393719}},
  \frac{{115360}}{{1393719}}\right),
  \]
  separated by \(448/1803\), with fibre contraction
  \((224/773)^2\).

The base derivative bound is
\(12(224/773)^2={float(BASE_DERIVATIVE):.9f}>1\); no unscaled joint
base--fibre contraction is claimed.

## Worst regression metrics

- open recurrence residual: {open_summary['maxima']['residual']:.3e};
- center-case crossed identity residual (100 digit): {open_summary['maxima']['crossed_residual']:.3e};
- boundary-probe crossed residual: {open_summary['boundary_probes']['maximum_crossed_residual']:.3e};
- raw binary64 forward crossed discrepancy (conditioning diagnostic):
  {open_summary['maxima']['float64_forward_crossed_residual']:.3e};
- center-endpoint envelope ratio: {max(open_summary['maxima']['left_bound_ratio'], open_summary['maxima']['right_bound_ratio']):.6f};
- boundary-probe envelope ratio: {open_summary['boundary_probes']['maximum_derivative_bound_ratio']:.6f};
- matching determinant error: {cyclic_summary['maxima']['determinant_identity_error']:.3e};
- Hill determinant error: {cyclic_summary['maxima']['hill_identity_error']:.3e};
- raw binary64 Hill subtraction error (conditioning diagnostic):
  {cyclic_summary['maxima']['float64_hill_identity_error']:.3e};
- direct/glued discrepancy: {gluing_summary['direct_glued_error']:.3e};
- scalar-average expected-fail residual: {gluing_summary['scalar_average_residual']:.3e};
- reversed-order expected-fail discrepancy: {gluing_summary['reversed_monodromy_error']:.3e}.

## Scope decision

`RETAIN_EFFECTIVE_SPECIALIZATION; MANUSCRIPT_HOLD;
NOVELTY_DELTA_UNCONFIRMED`.

Sterling--Dullin--Meiss Theorem 3 already covers the linearly conjugate real
signed-root SFT and real uniqueness.  Rugh and
Baladi--Pujals--Sambarino provide the qualitative complex pinning,
composition, periodic closure, and the orientation-twisted
absolute-denominator Cauchy/Fredholm mechanism.  The present result supplies
explicit complex \(H_6\) domains, constants and signed finite-dimensional
bookkeeping, but its publishable novelty is unconfirmed.  A paper claim still
needs a genuinely new signed, aggregate trace-compatible operator
approximation theorem.  Nuclearity, an infinite Fredholm determinant, Route-A
A2, and Hilbert--Pólya remain unestablished.

The 100-digit recheck is an implementation conditioning correction, not a
change of the frozen map, domains, chronology, cases, or pass threshold.  The
larger raw binary64 discrepancies remain in the certificate and CSV ledgers.
"""
    results_path = args.output_dir / "RESULTS.md"
    results_path.write_text(results_text, encoding="utf-8")

    report["artifact_sha256"] = {
        path.name: sha256_file(path)
        for path in (open_path, cyclic_path, gluing_path, results_path)
    }
    certificate_path.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

    print(
        json.dumps(
            {
                "certificate": str(certificate_path),
                "certificate_sha256": sha256_file(certificate_path),
                "all_checks_pass": report["all_checks_pass"],
                "open_rows": len(open_rows),
                "cyclic_rows": len(cyclic_rows),
                "theorem_status": report["theorem_status"],
            },
            indent=2,
            sort_keys=True,
        )
    )
    if not report["all_checks_pass"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
