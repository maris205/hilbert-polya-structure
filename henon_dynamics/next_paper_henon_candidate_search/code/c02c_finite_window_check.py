#!/usr/bin/env python3
"""Independent checker for HCS-C02C.

This file does not import the producer.  It uses Newton iteration on the orbit
residual rather than signed-root fixed-point iteration, independently rebuilds
the exact reciprocal disks, and rejects truncated/tampered in-memory ledgers.
"""

from __future__ import annotations

import argparse
import cmath
import csv
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Sequence

import mpmath as mp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = PROJECT_ROOT / "results" / "c02c_finite_window"

CENTER = Fraction(23, 48)
RADIUS = Fraction(7, 48)
PARENT_RADIUS = Fraction(123, 224)
DISPLAY_TOLERANCE = 5.0e-11


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


def solve_linear(matrix: Sequence[Sequence[complex]], rhs: Sequence[complex]) -> list[complex]:
    size = len(rhs)
    work = [
        [complex(value) for value in row] + [complex(rhs[index])]
        for index, row in enumerate(matrix)
    ]
    for column in range(size):
        pivot = max(range(column, size), key=lambda row: abs(work[row][column]))
        if abs(work[pivot][column]) < 1.0e-28:
            raise ZeroDivisionError("independent Newton matrix is singular")
        work[column], work[pivot] = work[pivot], work[column]
        for row in range(column + 1, size):
            multiplier = work[row][column] / work[column][column]
            for entry in range(column, size + 1):
                work[row][entry] -= multiplier * work[column][entry]
    answer = [0.0 + 0.0j for _ in range(size)]
    for row in range(size - 1, -1, -1):
        answer[row] = (
            work[row][size]
            - sum(work[row][column] * answer[column] for column in range(row + 1, size))
        ) / work[row][row]
    return answer


def determinant(matrix: Sequence[Sequence[complex]]) -> complex:
    size = len(matrix)
    work = [[complex(value) for value in row] for row in matrix]
    result = 1.0 + 0.0j
    parity = 1
    for column in range(size):
        pivot = max(range(column, size), key=lambda row: abs(work[row][column]))
        if abs(work[pivot][column]) < 1.0e-28:
            return 0.0 + 0.0j
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            parity *= -1
        pivot_value = work[column][column]
        result *= pivot_value
        for row in range(column + 1, size):
            multiplier = work[row][column] / pivot_value
            for entry in range(column + 1, size):
                work[row][entry] -= multiplier * work[column][entry]
    return parity * result


def open_residual_vector(
    values: Sequence[complex], left: complex, right: complex
) -> list[complex]:
    extended = [left, *values, right]
    return [
        1.0
        - 6.0 * extended[index] * extended[index]
        - extended[index - 1]
        - extended[index + 1]
        for index in range(1, len(extended) - 1)
    ]


def open_jacobian(values: Sequence[complex]) -> list[list[complex]]:
    length = len(values)
    matrix = [[0.0 + 0.0j for _ in range(length)] for _ in range(length)]
    for index, value in enumerate(values):
        matrix[index][index] = -12.0 * value
        if index > 0:
            matrix[index][index - 1] = -1.0
        if index + 1 < length:
            matrix[index][index + 1] = -1.0
    return matrix


def newton_open(
    signs: Sequence[int], left: complex, right: complex
) -> tuple[list[complex], int, float]:
    values = [complex(sign * float(CENTER), 0.0) for sign in signs[1:-1]]
    for iteration in range(1, 101):
        residual = open_residual_vector(values, left, right)
        norm = max(abs(value) for value in residual)
        if norm < 1.0e-14:
            return values, iteration, norm
        correction = solve_linear(
            open_jacobian(values), [-value for value in residual]
        )
        values = [value + step for value, step in zip(values, correction)]
    raise RuntimeError(f"independent open Newton failed for {sign_text(signs)}")


def cyclic_residual_vector(values: Sequence[complex]) -> list[complex]:
    length = len(values)
    return [
        1.0
        - 6.0 * values[index] * values[index]
        - values[(index - 1) % length]
        - values[(index + 1) % length]
        for index in range(length)
    ]


def cyclic_jacobian(values: Sequence[complex]) -> list[list[complex]]:
    length = len(values)
    matrix = [[0.0 + 0.0j for _ in range(length)] for _ in range(length)]
    for index, value in enumerate(values):
        matrix[index][index] += -12.0 * value
        matrix[index][(index - 1) % length] -= 1.0
        matrix[index][(index + 1) % length] -= 1.0
    return matrix


def newton_cyclic(signs: Sequence[int]) -> tuple[list[complex], int, float]:
    values = [complex(sign * float(CENTER), 0.0) for sign in signs]
    for iteration in range(1, 101):
        residual = cyclic_residual_vector(values)
        norm = max(abs(value) for value in residual)
        if norm < 1.0e-14:
            return values, iteration, norm
        correction = solve_linear(
            cyclic_jacobian(values), [-value for value in residual]
        )
        values = [value + step for value, step in zip(values, correction)]
    raise RuntimeError(f"independent cyclic Newton failed for {sign_text(signs)}")


def parse_sign_text(text: str) -> tuple[int, ...]:
    if not text or any(character not in "+-" for character in text):
        raise ValueError(f"invalid sign text: {text!r}")
    return tuple(1 if character == "+" else -1 for character in text)


def mp_newton_open_crossed(signs: Sequence[int]) -> dict[str, float]:
    """Independently revisit one ill-conditioned open case with MP Newton."""

    with mp.workdps(90):
        center = mp.mpf(CENTER.numerator) / CENTER.denominator
        left = signs[0] * center
        right = signs[-1] * center
        values = mp.matrix([sign * center for sign in signs[1:-1]])
        length = len(values)
        for _ in range(100):
            residual = mp.matrix(length, 1)
            matrix = mp.matrix(length)
            for row in range(length):
                for column in range(length):
                    matrix[row, column] = 0
                previous = left if row == 0 else values[row - 1]
                following = right if row + 1 == length else values[row + 1]
                residual[row] = 1 - 6 * values[row] ** 2 - previous - following
                matrix[row, row] = -12 * values[row]
                if row > 0:
                    matrix[row, row - 1] = -1
                if row + 1 < length:
                    matrix[row, row + 1] = -1
            residual_norm = max(abs(residual[row]) for row in range(length))
            if residual_norm < mp.mpf("1e-75"):
                break
            correction = mp.lu_solve(matrix, -residual)
            values += correction
        else:
            raise RuntimeError("independent high-precision open Newton failed")
        q, p = values[0], left
        for _ in range(length):
            q, p = 1 - 6 * q * q - p, q
        return {
            "newton_residual": float(residual_norm),
            "crossed_residual": float(
                max(abs(q - right), abs(p - values[length - 1]))
            ),
        }


def mp_newton_cyclic_identities(signs: Sequence[int]) -> dict[str, float]:
    """Independently revisit one ill-conditioned cyclic case with MP Newton."""

    with mp.workdps(90):
        center = mp.mpf(CENTER.numerator) / CENTER.denominator
        values = mp.matrix([sign * center for sign in signs])
        length = len(values)
        for _ in range(100):
            residual = mp.matrix(length, 1)
            cyclic = mp.matrix(length)
            for row in range(length):
                for column in range(length):
                    cyclic[row, column] = 0
                residual[row] = (
                    1
                    - 6 * values[row] ** 2
                    - values[(row - 1) % length]
                    - values[(row + 1) % length]
                )
                cyclic[row, row] += -12 * values[row]
                cyclic[row, (row - 1) % length] -= 1
                cyclic[row, (row + 1) % length] -= 1
            residual_norm = max(abs(residual[row]) for row in range(length))
            if residual_norm < mp.mpf("1e-75"):
                break
            correction = mp.lu_solve(cyclic, -residual)
            values += correction
        else:
            raise RuntimeError("independent high-precision cyclic Newton failed")

        open_matrix = mp.matrix(length)
        for row in range(length):
            for column in range(length):
                open_matrix[row, column] = 0
            open_matrix[row, row] = -12 * values[row]
            if row > 0:
                open_matrix[row, row - 1] = -1
            if row + 1 < length:
                open_matrix[row, row + 1] = -1
        theta = mp.det(open_matrix)
        left_rhs = mp.matrix(length, 1)
        right_rhs = mp.matrix(length, 1)
        for row in range(length):
            left_rhs[row] = 0
            right_rhs[row] = 0
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
        product = mp.eye(2)
        for value in values:
            product = mp.matrix([[-12 * value, -1], [1, 0]]) * product
        det_i_minus_m = mp.det(mp.eye(2) - product)
        return {
            "newton_residual": float(residual_norm),
            "matching_error": float(
                abs(mp.det(matching) + det_i_minus_m / theta)
            ),
            "hill_error": float(abs(mp.det(cyclic) + det_i_minus_m)),
        }


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


def monodromy(values: Sequence[complex]) -> list[list[complex]]:
    product = [[1.0 + 0.0j, 0.0j], [0.0j, 1.0 + 0.0j]]
    for value in values:
        product = matmul2(
            [[-12.0 * value, -1.0 + 0.0j], [1.0 + 0.0j, 0.0j]],
            product,
        )
    return product


def det2(matrix: Sequence[Sequence[complex]]) -> complex:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def endpoint_derivatives(values: Sequence[complex]) -> tuple[list[complex], list[complex], complex]:
    matrix = open_jacobian(values)
    length = len(values)
    left_rhs = [0.0 + 0.0j for _ in range(length)]
    right_rhs = [0.0 + 0.0j for _ in range(length)]
    left_rhs[0] = 1.0
    right_rhs[-1] = 1.0
    return (
        solve_linear(matrix, left_rhs),
        solve_linear(matrix, right_rhs),
        determinant(matrix),
    )


def iterate_state(q: complex, p: complex, count: int) -> tuple[complex, complex]:
    for _ in range(count):
        q, p = 1.0 - 6.0 * q * q - p, q
    return q, p


def expected_open_ids(max_length: int) -> list[str]:
    return [
        f"N{length}:{sign_text(signs)}"
        for length in range(1, max_length + 1)
        for signs in sign_words(length + 2)
        if extended_admissible(signs)
    ]


def expected_cyclic_ids(max_length: int) -> list[str]:
    return [
        f"C{length}:{sign_text(signs)}"
        for length in range(1, max_length + 1)
        for signs in sign_words(length)
        if cyclic_admissible(signs)
    ]


def complete_ids(expected: Sequence[str], observed: Sequence[str]) -> bool:
    return len(expected) == len(observed) and len(set(observed)) == len(observed) and set(expected) == set(observed)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def exact_projective_check(report: dict[str, object]) -> tuple[dict[str, bool], float]:
    denominator_center = Fraction(23, 4)
    denominator_radius = 12 * RADIUS + PARENT_RADIUS
    clearance = denominator_center - denominator_radius
    reciprocal = denominator_center * denominator_center - denominator_radius * denominator_radius
    child_center = denominator_center / reciprocal
    child_radius = denominator_radius / reciprocal
    inner = child_center - child_radius
    outer = child_center + child_radius
    persisted = report["projective_complex_base"]["constants"]
    checks = {
        "denominator_radius": denominator_radius == Fraction(515, 224),
        "clearance": clearance == Fraction(773, 224) and clearance > 0,
        "child_center": child_center == Fraction(288512, 1393719),
        "child_radius": child_radius == Fraction(115360, 1393719),
        "inner": inner == Fraction(224, 1803),
        "outer": outer == Fraction(224, 773),
        "gap": 2 * inner == Fraction(448, 1803),
        "parent_containment": PARENT_RADIUS - outer
        == Fraction(44903, 173152),
        "fibre_derivative": outer * outer == Fraction(50176, 597529),
        "base_sensitivity_exceeds_one": 12 * outer * outer
        == Fraction(602112, 597529)
        and 12 * outer * outer > 1,
        "persisted_center": persisted["child_center_magnitude"]
        == "288512/1393719",
        "persisted_radius": persisted["child_radius"] == "115360/1393719",
        "persisted_gap": persisted["child_gap"] == "448/1803",
    }
    maximum_point_error = 0.0
    for epsilon in (-1, 1):
        probes = [
            (
                epsilon / 3.0,
                -epsilon * float(PARENT_RADIUS),
                -epsilon * float(outer),
            ),
            (
                5.0 * epsilon / 8.0,
                epsilon * float(PARENT_RADIUS),
                -epsilon * float(inner),
            ),
        ]
        for q, m, target in probes:
            maximum_point_error = max(
                maximum_point_error, abs(1.0 / (-12.0 * q - m) - target)
            )
        q = epsilon * float(CENTER) - 1j * float(RADIUS)
        m = -1j * float(PARENT_RADIUS)
        image = 1.0 / (-12.0 * q - m)
        maximum_point_error = max(
            maximum_point_error,
            abs(abs(image + epsilon * float(child_center)) - float(child_radius)),
        )
    checks["adversarial_points"] = maximum_point_error < 2.0e-15
    return checks, maximum_point_error


def independent_open_audit() -> dict[str, object]:
    a0 = 1.0 / math.sqrt(17.0)
    kappa = 2.0 / math.sqrt(17.0)
    beta = a0 / (1.0 - kappa)
    angle_pairs = [
        None,
        (0.0, 0.0),
        (math.pi / 2.0, -math.pi / 2.0),
        (math.pi, math.pi / 2.0),
        (3.0 * math.pi / 2.0, math.pi / 4.0),
    ]
    count = 0
    maximum_residual = 0.0
    maximum_crossed = 0.0
    maximum_bound_ratio = 0.0
    minimum_margin = math.inf
    maximum_reciprocity_error = 0.0
    maximum_theta_error = 0.0
    for length in range(1, 4):
        for signs in sign_words(length + 2):
            if not extended_admissible(signs):
                continue
            for angles in angle_pairs:
                if angles is None:
                    left = signs[0] * float(CENTER)
                    right = signs[-1] * float(CENTER)
                else:
                    left = signs[0] * float(CENTER) + float(RADIUS) * cmath.exp(
                        1j * angles[0]
                    )
                    right = signs[-1] * float(CENTER) + float(RADIUS) * cmath.exp(
                        1j * angles[1]
                    )
                values, _, residual = newton_open(signs, left, right)
                left_derivative, right_derivative, theta = endpoint_derivatives(values)
                crossed = iterate_state(values[0], left, length)
                maximum_crossed = max(
                    maximum_crossed,
                    abs(crossed[0] - right),
                    abs(crossed[1] - values[-1]),
                )
                maximum_residual = max(maximum_residual, residual)
                minimum_margin = min(
                    minimum_margin,
                    min(
                        float(RADIUS) - abs(value - sign * float(CENTER))
                        for value, sign in zip(values, signs[1:-1])
                    ),
                )
                for index in range(length):
                    maximum_bound_ratio = max(
                        maximum_bound_ratio,
                        abs(left_derivative[index]) / (beta * kappa**index),
                        abs(right_derivative[index])
                        / (beta * kappa ** (length - 1 - index)),
                    )
                maximum_reciprocity_error = max(
                    maximum_reciprocity_error,
                    abs(right_derivative[0] - left_derivative[-1]),
                )
                maximum_theta_error = max(
                    maximum_theta_error, abs(theta - monodromy(values)[0][0])
                )
                count += 1
    return {
        "count": count,
        "expected_count": 5 * (6 + 9 + 15),
        "maximum_residual": maximum_residual,
        "maximum_crossed_residual": maximum_crossed,
        "maximum_derivative_bound_ratio": maximum_bound_ratio,
        "minimum_disk_margin": minimum_margin,
        "maximum_reciprocity_error": maximum_reciprocity_error,
        "maximum_theta_monodromy_error": maximum_theta_error,
    }


def independent_cyclic_audit() -> dict[str, object]:
    count = 0
    maximum_residual = 0.0
    maximum_matching_error = 0.0
    maximum_hill_error = 0.0
    n1_matrix_ok = False
    n2_matrix_ok = False
    for length in range(1, 5):
        for signs in sign_words(length):
            if not cyclic_admissible(signs):
                continue
            values, _, residual = newton_cyclic(signs)
            open_matrix = open_jacobian(values)
            left, right, theta = endpoint_derivatives(values)
            matching = [
                [left[-1] - 1.0, right[-1]],
                [left[0], right[0] - 1.0],
            ]
            matrix = monodromy(values)
            det_i_minus_m = det2(
                [
                    [1.0 - matrix[0][0], -matrix[0][1]],
                    [-matrix[1][0], 1.0 - matrix[1][1]],
                ]
            )
            cyclic_matrix = cyclic_jacobian(values)
            maximum_matching_error = max(
                maximum_matching_error,
                abs(det2(matching) + det_i_minus_m / theta),
            )
            maximum_hill_error = max(
                maximum_hill_error,
                abs(determinant(cyclic_matrix) + det_i_minus_m),
            )
            maximum_residual = max(maximum_residual, residual)
            if length == 1:
                n1_matrix_ok = len(cyclic_matrix) == 1 and abs(
                    cyclic_matrix[0][0] - (-12.0 * values[0] - 2.0)
                ) < 1.0e-13
            if length == 2:
                n2_matrix_ok = (
                    abs(cyclic_matrix[0][1] + 2.0) < 1.0e-13
                    and abs(cyclic_matrix[1][0] + 2.0) < 1.0e-13
                )
            if abs(determinant(open_matrix) - theta) > 1.0e-13:
                raise AssertionError("independent open determinant changed")
            count += 1
    return {
        "count": count,
        "maximum_residual": maximum_residual,
        "maximum_matching_error": maximum_matching_error,
        "maximum_hill_error": maximum_hill_error,
        "n1_doubled_incidence": n1_matrix_ok,
        "n2_doubled_incidence": n2_matrix_ok,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=Path, default=DEFAULT_RESULTS)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    certificate_path = args.results_dir / "certificate.json"
    open_path = args.results_dir / "open_windows.csv"
    cyclic_path = args.results_dir / "cyclic_matching.csv"
    gluing_path = args.results_dir / "gluing_controls.csv"
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
    open_rows = read_csv(open_path)
    cyclic_rows = read_csv(cyclic_path)
    gluing_rows = read_csv(gluing_path)

    max_open = max(int(key) for key in certificate["open_windows"]["counts_by_length"])
    max_cyclic = max(
        int(key) for key in certificate["cyclic_matching"]["counts_by_length"]
    )
    expected_open = expected_open_ids(max_open)
    expected_cyclic = expected_cyclic_ids(max_cyclic)
    observed_open = [row["case_id"] for row in open_rows]
    observed_cyclic = [row["case_id"] for row in cyclic_rows]

    exact_checks, projective_point_error = exact_projective_check(certificate)
    open_independent = independent_open_audit()
    cyclic_independent = independent_cyclic_audit()

    control_ids = [row["control_id"] for row in gluing_rows]
    control_passes = all(row["passed"] == "True" for row in gluing_rows)
    numeric_open_columns = [
        "recurrence_residual",
        "crossed_residual",
        "endpoint_formula_error",
        "endpoint_reciprocity_error",
        "theta_monodromy_error",
    ]
    max_open_persisted_error = max(
        float(row[column]) for row in open_rows for column in numeric_open_columns
    )
    max_open_ratio = max(
        float(row[column])
        for row in open_rows
        for column in (
            "left_bound_ratio",
            "right_bound_ratio",
            "projective_initial_ratio",
            "projective_left_ratio",
            "projective_right_ratio",
        )
    )
    max_cyclic_persisted_error = max(
        float(row[column])
        for row in cyclic_rows
        for column in (
            "cyclic_residual",
            "open_cyclic_value_error",
            "determinant_identity_error",
            "hill_identity_error",
            "projective_fixed_slope_error",
            "projective_multiplier_relative_error",
        )
    )

    worst_conditioned_open = max(
        open_rows, key=lambda row: float(row["float64_forward_crossed_residual"])
    )
    worst_conditioned_cyclic = max(
        cyclic_rows, key=lambda row: float(row["float64_hill_identity_error"])
    )
    mp_open_recheck = mp_newton_open_crossed(
        parse_sign_text(worst_conditioned_open["extended_signs"])
    )
    mp_cyclic_recheck = mp_newton_cyclic_identities(
        parse_sign_text(worst_conditioned_cyclic["cyclic_signs"])
    )

    # Mandatory in-memory negative controls.  These functions inspect exact
    # cardinality and complete IDs, so a prefix cannot pass accidentally.
    truncation_controls = {
        "truncated_open_rejected": not complete_ids(
            expected_open, observed_open[:-1]
        ),
        "truncated_cyclic_rejected": not complete_ids(
            expected_cyclic, observed_cyclic[:-1]
        ),
    }
    tampered = json.loads(json.dumps(certificate))
    tampered["projective_complex_base"]["constants"][
        "child_radius"
    ] = "115361/1393719"
    tampered_exact_checks, _ = exact_projective_check(tampered)
    truncation_controls["tampered_projective_rejected"] = not all(
        tampered_exact_checks.values()
    )

    checks = {
        "run_id": certificate.get("run_id") == "HCS_C02C_FINITE_WINDOW_V1",
        "producer_all_pass": certificate.get("all_checks_pass") is True,
        "map_exact": certificate["object"]["map"]
        == "H_6(q,p)=(1-6q^2-p,q)",
        "complete_open_ids": complete_ids(expected_open, observed_open),
        "complete_cyclic_ids": complete_ids(expected_cyclic, observed_cyclic),
        "certificate_open_ids": complete_ids(
            expected_open, certificate["open_windows"]["complete_case_ids"]
        ),
        "certificate_cyclic_ids": complete_ids(
            expected_cyclic, certificate["cyclic_matching"]["complete_case_ids"]
        ),
        "persisted_open_errors": max_open_persisted_error < DISPLAY_TOLERANCE,
        "persisted_open_bounds": max_open_ratio <= 1.0 + 1.0e-10,
        "persisted_cyclic_errors": max_cyclic_persisted_error
        < DISPLAY_TOLERANCE,
        "persisted_orientation": all(
            row["orientation_ok"] == "True" for row in cyclic_rows
        ),
        "control_ids": control_ids
        == [
            "G1_TWO_COORDINATE_GLUE",
            "G2_SCALAR_AVERAGE",
            "O1_REVERSED_MONODROMY",
        ],
        "controls_pass": control_passes,
        "projective_exact": all(exact_checks.values()),
        "independent_open_count": open_independent["count"]
        == open_independent["expected_count"],
        "independent_open_residual": open_independent["maximum_residual"]
        < DISPLAY_TOLERANCE,
        "independent_open_crossed": open_independent[
            "maximum_crossed_residual"
        ]
        < DISPLAY_TOLERANCE,
        "independent_open_margin": open_independent["minimum_disk_margin"] > 0,
        "independent_open_bounds": open_independent[
            "maximum_derivative_bound_ratio"
        ]
        <= 1.0 + 1.0e-10,
        "independent_reciprocity": open_independent[
            "maximum_reciprocity_error"
        ]
        < DISPLAY_TOLERANCE,
        "independent_theta_monodromy": open_independent[
            "maximum_theta_monodromy_error"
        ]
        < DISPLAY_TOLERANCE,
        "independent_cyclic_residual": cyclic_independent[
            "maximum_residual"
        ]
        < DISPLAY_TOLERANCE,
        "independent_matching": cyclic_independent[
            "maximum_matching_error"
        ]
        < DISPLAY_TOLERANCE,
        "independent_hill": cyclic_independent["maximum_hill_error"]
        < DISPLAY_TOLERANCE,
        "independent_n1_chronology": cyclic_independent[
            "n1_doubled_incidence"
        ],
        "independent_n2_chronology": cyclic_independent[
            "n2_doubled_incidence"
        ],
        "worst_conditioned_open_mp_newton": mp_open_recheck[
            "newton_residual"
        ]
        < 1.0e-60
        and mp_open_recheck["crossed_residual"] < 1.0e-60,
        "worst_conditioned_cyclic_mp_newton": mp_cyclic_recheck[
            "newton_residual"
        ]
        < 1.0e-60
        and mp_cyclic_recheck["matching_error"] < 1.0e-60
        and mp_cyclic_recheck["hill_error"] < 1.0e-60,
        "truncation_tamper_controls": all(truncation_controls.values()),
        "no_operator_promotion": certificate["theorem_status"][
            "nuclear_operator"
        ]
        == "NOT_ESTABLISHED"
        and certificate["theorem_status"]["fredholm_determinant"]
        == "NOT_ESTABLISHED"
        and certificate["theorem_status"]["route_a_a2"] == "DO_NOT_PROMOTE",
    }

    report = {
        "run_id": "HCS_C02C_FINITE_WINDOW_INDEPENDENT_CHECK_V1",
        "source": str(certificate_path),
        "method": (
            "Independent complex Newton solver on orbit residuals; exact "
            "Fraction reconstruction; complete-ID and in-memory tamper checks."
        ),
        "projective_point_maximum_error": projective_point_error,
        "independent_open": open_independent,
        "independent_cyclic": cyclic_independent,
        "conditioning_rechecks": {
            "open_case_id": worst_conditioned_open["case_id"],
            "open_raw_binary64_crossed_residual": float(
                worst_conditioned_open["float64_forward_crossed_residual"]
            ),
            "open_mp_newton": mp_open_recheck,
            "cyclic_case_id": worst_conditioned_cyclic["case_id"],
            "cyclic_raw_binary64_hill_error": float(
                worst_conditioned_cyclic["float64_hill_identity_error"]
            ),
            "cyclic_mp_newton": mp_cyclic_recheck,
        },
        "persisted_metrics": {
            "maximum_open_error": max_open_persisted_error,
            "maximum_open_bound_ratio": max_open_ratio,
            "maximum_cyclic_error": max_cyclic_persisted_error,
        },
        "truncation_tamper_controls": truncation_controls,
        "checks": checks,
        "all_checks_pass": all(checks.values()),
        "scope": (
            "Checks the effective finite-window certificate only. It does "
            "not certify novelty, a nuclear operator, a Fredholm determinant, "
            "Route-A A2, or a Hilbert--Polya construction."
        ),
    }
    output_path = args.results_dir / "independent_check.json"
    output_path.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    if not report["all_checks_pass"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
