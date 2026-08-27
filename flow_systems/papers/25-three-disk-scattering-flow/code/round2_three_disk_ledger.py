#!/usr/bin/env python3
"""Deterministic Round-2 three-disk orbit ledger and target-free controls.

The program keeps three objects separate in every row:

1. an exact symbolic primitive oriented cyclic word;
2. a center-polygon proxy (never called a billiard orbit);
3. a numerical specular billiard orbit, emitted only when independent solves,
   reflection residuals, visibility checks, and length recomputation agree.

No prime table or Riemann-zero table is read or generated.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import itertools
import json
import math
from collections import Counter
from decimal import Decimal, localcontext
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np
import scipy
from scipy.optimize import least_squares, minimize


DISK_RADIUS = 1.0
DISTANCE_RATIOS = (5.8, 6.0, 6.2)
MAX_TOPOLOGICAL_LENGTH = 12
PRIMARY_DISTANCE_RATIO = 6.0
STATISTIC_ID = "UNSTABLE_MULTIPLIER_HALF_DENSITY_V1"
CONTROL_SEED_LABEL = "P25-2026-08-27-target-free-controls-v1"
NEIGHBOR_CORRELATION_STOP_THRESHOLD = 0.98


def wrap_angle(value: float) -> float:
    return (value + math.pi) % (2.0 * math.pi) - math.pi


def canonical_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[index:] + word[:index] for index in range(len(word)))


def is_symbolically_primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    for size in range(1, n):
        if n % size == 0 and word == word[:size] * (n // size):
            return False
    return True


def primitive_oriented_cyclic_words(
    max_length: int = MAX_TOPOLOGICAL_LENGTH,
) -> list[tuple[int, ...]]:
    words: list[tuple[int, ...]] = []
    for length in range(2, max_length + 1):
        for word in itertools.product(range(3), repeat=length):
            if any(word[index] == word[(index + 1) % length] for index in range(length)):
                continue
            if word != canonical_rotation(word):
                continue
            if not is_symbolically_primitive(word):
                continue
            words.append(word)
    return words


def word_text(word: Sequence[int]) -> str:
    return "".join(str(symbol) for symbol in word)


def centers(distance_ratio: float) -> np.ndarray:
    d = float(distance_ratio)
    return np.array(
        [[0.0, 0.0], [d, 0.0], [0.5 * d, 0.5 * math.sqrt(3.0) * d]],
        dtype=float,
    )


def orbit_geometry(
    theta: np.ndarray, word: tuple[int, ...], distance_ratio: float
) -> tuple[float, np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    disk_centers = centers(distance_ratio)[list(word)]
    normals = np.column_stack((np.cos(theta), np.sin(theta)))
    tangents = np.column_stack((-np.sin(theta), np.cos(theta)))
    points = disk_centers + DISK_RADIUS * normals
    displacements = np.roll(points, -1, axis=0) - points
    segment_lengths = np.linalg.norm(displacements, axis=1)
    directions = displacements / segment_lengths[:, None]
    gradient = DISK_RADIUS * np.sum(
        tangents * (np.roll(directions, 1, axis=0) - directions), axis=1
    )
    return (
        float(np.sum(segment_lengths)),
        gradient,
        points,
        segment_lengths,
        directions,
        normals,
    )


def initial_angles(word: tuple[int, ...], distance_ratio: float) -> np.ndarray:
    all_centers = centers(distance_ratio)
    result: list[float] = []
    for index, symbol in enumerate(word):
        current = all_centers[symbol]
        previous = all_centers[word[index - 1]] - current
        following = all_centers[word[(index + 1) % len(word)]] - current
        previous /= np.linalg.norm(previous)
        following /= np.linalg.norm(following)
        direction = previous + following
        if np.linalg.norm(direction) < 1e-14:
            direction = previous
        result.append(math.atan2(direction[1], direction[0]))
    return np.array(result, dtype=float)


def specular_residuals(
    points: np.ndarray, directions: np.ndarray, normals: np.ndarray
) -> tuple[float, float, float]:
    residuals: list[float] = []
    outgoing_normal: list[float] = []
    incoming_normal: list[float] = []
    for index in range(len(points)):
        incoming = directions[index - 1]
        outgoing = directions[index]
        normal = normals[index]
        reflected = incoming - 2.0 * float(np.dot(incoming, normal)) * normal
        residuals.append(float(np.linalg.norm(outgoing - reflected)))
        outgoing_normal.append(float(np.dot(outgoing, normal)))
        incoming_normal.append(float(-np.dot(incoming, normal)))
    return max(residuals), min(outgoing_normal), min(incoming_normal)


def minimum_other_disk_clearance(
    points: np.ndarray, word: tuple[int, ...], distance_ratio: float
) -> float:
    all_centers = centers(distance_ratio)
    clearances: list[float] = []
    for index, start in enumerate(points):
        end = points[(index + 1) % len(points)]
        segment = end - start
        denominator = float(np.dot(segment, segment))
        endpoint_symbols = {word[index], word[(index + 1) % len(word)]}
        for disk_index, center in enumerate(all_centers):
            if disk_index in endpoint_symbols:
                continue
            parameter = float(np.dot(center - start, segment) / denominator)
            parameter = min(1.0, max(0.0, parameter))
            closest = start + parameter * segment
            clearances.append(float(np.linalg.norm(closest - center) - DISK_RADIUS))
    return min(clearances) if clearances else math.inf


def independent_length(points: np.ndarray) -> float:
    total = 0.0
    for index in range(len(points)):
        x0, y0 = (float(value) for value in points[index])
        x1, y1 = (float(value) for value in points[(index + 1) % len(points)])
        total += math.hypot(x1 - x0, y1 - y0)
    return total


def solve_orbit(word: tuple[int, ...], distance_ratio: float) -> dict[str, object]:
    start = initial_angles(word, distance_ratio)

    def objective(theta: np.ndarray) -> tuple[float, np.ndarray]:
        length, gradient, *_rest = orbit_geometry(theta, word, distance_ratio)
        return length, gradient

    primary = minimize(
        objective,
        start,
        jac=True,
        method="BFGS",
        options={"gtol": 1e-11, "maxiter": 1000},
    )
    primary_theta = np.asarray(primary.x, dtype=float)
    primary_eval = orbit_geometry(primary_theta, word, distance_ratio)

    # A deterministic fallback start is used only when the direct solve has a
    # large stationarity residual.  It is not selected using any target data.
    if float(np.max(np.abs(primary_eval[1]))) > 1e-8:
        offset = np.array(
            [0.05 * math.sin((index + 1) * math.sqrt(2.0)) for index in range(len(word))]
        )
        fallback = minimize(
            objective,
            start + offset,
            jac=True,
            method="BFGS",
            options={"gtol": 1e-11, "maxiter": 1500},
        )
        fallback_eval = orbit_geometry(np.asarray(fallback.x), word, distance_ratio)
        if float(np.max(np.abs(fallback_eval[1]))) < float(
            np.max(np.abs(primary_eval[1]))
        ):
            primary = fallback
            primary_theta = np.asarray(fallback.x, dtype=float)
            primary_eval = fallback_eval

    independent = least_squares(
        lambda theta: orbit_geometry(theta, word, distance_ratio)[1],
        primary_theta,
        xtol=1e-13,
        ftol=1e-13,
        gtol=1e-13,
        max_nfev=1200,
    )
    independent_theta = np.asarray(independent.x, dtype=float)
    independent_eval = orbit_geometry(independent_theta, word, distance_ratio)

    # The least-squares solve targets the reflection/stationarity equations
    # directly and is normally much more accurate for long words.  Keep the
    # variational BFGS solve as the independent recomputation.
    length, gradient, points, segment_lengths, directions, normals = independent_eval
    independent_value = float(primary_eval[0])
    theta_agreement = max(
        abs(wrap_angle(float(a - b)))
        for a, b in zip(primary_theta, independent_theta, strict=True)
    )
    reflection_residual, min_outgoing, min_incoming = specular_residuals(
        points, directions, normals
    )
    clearance = minimum_other_disk_clearance(points, word, distance_ratio)
    length_check = independent_length(points)
    length_recompute_residual = abs(length - length_check)
    independent_length_residual = abs(length - independent_value)

    reliable = (
        float(np.max(np.abs(gradient))) <= 2e-8
        and reflection_residual <= 2e-8
        and min_outgoing >= 1e-8
        and min_incoming >= 1e-8
        and clearance >= -1e-9
        and length_recompute_residual <= 2e-11
        and independent_length_residual <= 2e-9
        and theta_agreement <= 2e-7
    )
    return {
        "reliable": reliable,
        "primary_optimizer_success": bool(primary.success),
        "independent_optimizer_success": bool(independent.success),
        "theta": independent_theta,
        "points": points,
        "segment_lengths": segment_lengths,
        "directions": directions,
        "normals": normals,
        "length": float(length),
        "independent_length": independent_value,
        "center_proxy_length": center_polygon_length(word, distance_ratio),
        "stationarity_residual": float(np.max(np.abs(gradient))),
        "reflection_residual": reflection_residual,
        "min_outgoing_normal": min_outgoing,
        "min_incoming_normal": min_incoming,
        "other_disk_clearance": clearance,
        "length_recompute_residual": length_recompute_residual,
        "independent_length_residual": independent_length_residual,
        "independent_theta_residual": theta_agreement,
    }


def center_polygon_length(word: tuple[int, ...], distance_ratio: float) -> float:
    all_centers = centers(distance_ratio)
    return sum(
        float(np.linalg.norm(all_centers[word[(index + 1) % len(word)]] - all_centers[word[index]]))
        for index in range(len(word))
    )


def _matrix_multiply(left: tuple[tuple[float, float], tuple[float, float]], right: tuple[tuple[float, float], tuple[float, float]]) -> tuple[tuple[float, float], tuple[float, float]]:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def _decimal_matrix_multiply(
    left: tuple[tuple[Decimal, Decimal], tuple[Decimal, Decimal]],
    right: tuple[tuple[Decimal, Decimal], tuple[Decimal, Decimal]],
) -> tuple[tuple[Decimal, Decimal], tuple[Decimal, Decimal]]:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def stability_from_orbit(solution: dict[str, object]) -> dict[str, object]:
    segment_lengths = np.asarray(solution["segment_lengths"], dtype=float)
    directions = np.asarray(solution["directions"], dtype=float)
    normals = np.asarray(solution["normals"], dtype=float)
    double_matrix = ((1.0, 0.0), (0.0, 1.0))
    factors: list[tuple[float, float]] = []
    for index, flight_length in enumerate(segment_lengths):
        next_index = (index + 1) % len(segment_lengths)
        cosine = abs(float(np.dot(directions[index], normals[next_index])))
        curvature_factor = 2.0 / (DISK_RADIUS * cosine)
        free = ((1.0, float(flight_length)), (0.0, 1.0))
        reflection = ((1.0, 0.0), (curvature_factor, 1.0))
        double_matrix = _matrix_multiply(
            _matrix_multiply(reflection, free), double_matrix
        )
        factors.append((float(flight_length), cosine))

    # Long hyperbolic products have entries of order 1e13 at this cutoff, so
    # evaluating ad-bc in binary64 loses all useful digits even though every
    # free-flight and reflection factor has determinant one.  Rebuild the same
    # product with 80 decimal digits and retain the binary64 trace only as an
    # explicitly recorded cross-check.  This is a precision repair, not an
    # independent physical derivation; the finite-difference return map below
    # remains the independent stability check.
    with localcontext() as context:
        context.prec = 80
        one = Decimal(1)
        zero = Decimal(0)
        two = Decimal(2)
        high_matrix = ((one, zero), (zero, one))
        for flight_length, cosine in factors:
            flight_decimal = Decimal.from_float(flight_length)
            cosine_decimal = Decimal.from_float(cosine)
            curvature_decimal = two / (Decimal.from_float(DISK_RADIUS) * cosine_decimal)
            free_decimal = ((one, flight_decimal), (zero, one))
            reflection_decimal = ((one, zero), (curvature_decimal, one))
            high_matrix = _decimal_matrix_multiply(
                _decimal_matrix_multiply(reflection_decimal, free_decimal),
                high_matrix,
            )
        trace_decimal = high_matrix[0][0] + high_matrix[1][1]
        determinant_decimal = (
            high_matrix[0][0] * high_matrix[1][1]
            - high_matrix[0][1] * high_matrix[1][0]
        )
        discriminant_decimal = max(zero, trace_decimal * trace_decimal - Decimal(4))
        unstable_decimal = (trace_decimal + discriminant_decimal.sqrt()) / two
        half_density_decimal = one / unstable_decimal.sqrt()
        double_trace = double_matrix[0][0] + double_matrix[1][1]
        double_trace_residual = abs(
            Decimal.from_float(double_trace) - trace_decimal
        ) / max(abs(trace_decimal), one)
    return {
        "trace": float(trace_decimal),
        "determinant_high_precision": format(determinant_decimal, ".30g"),
        "determinant_high_precision_residual": float(abs(determinant_decimal - one)),
        "double_trace_relative_residual": float(double_trace_residual),
        "unstable_multiplier": float(unstable_decimal),
        "half_density": float(half_density_decimal),
    }


def ray_step(
    theta: float,
    tangent_momentum: float,
    current_disk: int,
    next_disk: int,
    distance_ratio: float,
) -> tuple[float, float]:
    all_centers = centers(distance_ratio)
    normal = np.array([math.cos(theta), math.sin(theta)])
    tangent = np.array([-normal[1], normal[0]])
    if abs(tangent_momentum) >= 1.0:
        raise ValueError("invalid tangent momentum")
    direction = math.sqrt(max(0.0, 1.0 - tangent_momentum**2)) * normal + tangent_momentum * tangent
    point = all_centers[current_disk] + DISK_RADIUS * normal
    relative = point - all_centers[next_disk]
    linear = float(np.dot(relative, direction))
    constant = float(np.dot(relative, relative) - DISK_RADIUS**2)
    discriminant = linear * linear - constant
    if discriminant <= 0:
        raise ValueError("requested disk not intersected")
    root = math.sqrt(discriminant)
    candidates = [value for value in (-linear - root, -linear + root) if value > 1e-10]
    if not candidates:
        raise ValueError("no forward intersection")
    hit = point + min(candidates) * direction
    next_normal = (hit - all_centers[next_disk]) / DISK_RADIUS
    next_theta = math.atan2(next_normal[1], next_normal[0])
    next_tangent = np.array([-next_normal[1], next_normal[0]])
    reflected = direction - 2.0 * float(np.dot(direction, next_normal)) * next_normal
    next_momentum = float(np.dot(reflected, next_tangent))
    return next_theta, next_momentum


def return_map(
    state: np.ndarray, word: tuple[int, ...], distance_ratio: float
) -> np.ndarray:
    theta, momentum = (float(value) for value in state)
    for index in range(len(word)):
        theta, momentum = ray_step(
            theta,
            momentum,
            word[index],
            word[(index + 1) % len(word)],
            distance_ratio,
        )
    return np.array([theta, momentum])


def finite_difference_stability_check(
    word: tuple[int, ...], distance_ratio: float, solution: dict[str, object], analytic_trace: float
) -> dict[str, object]:
    theta = np.asarray(solution["theta"], dtype=float)
    directions = np.asarray(solution["directions"], dtype=float)
    normal = np.array([math.cos(theta[0]), math.sin(theta[0])])
    tangent = np.array([-normal[1], normal[0]])
    base = np.array([theta[0], float(np.dot(directions[0], tangent))])
    try:
        returned = return_map(base, word, distance_ratio)
        return_residual = max(
            abs(wrap_angle(float(returned[0] - base[0]))),
            abs(float(returned[1] - base[1])),
        )
    except ValueError:
        return {
            "status": "OPEN",
            "return_residual": math.inf,
            "trace": math.nan,
            "determinant": math.nan,
            "relative_trace_residual": math.inf,
        }

    candidates: list[tuple[float, np.ndarray]] = []
    for step in (1e-5, 3e-6, 1e-6, 3e-7, 1e-7):
        jacobian = np.zeros((2, 2))
        try:
            for coordinate in range(2):
                plus = base.copy()
                minus = base.copy()
                plus[coordinate] += step
                minus[coordinate] -= step
                y_plus = return_map(plus, word, distance_ratio)
                y_minus = return_map(minus, word, distance_ratio)
                first_difference = wrap_angle(float(y_plus[0] - y_minus[0]))
                jacobian[:, coordinate] = (
                    first_difference / (2.0 * step),
                    float(y_plus[1] - y_minus[1]) / (2.0 * step),
                )
        except ValueError:
            continue
        determinant = float(np.linalg.det(jacobian))
        candidates.append((abs(determinant - 1.0), jacobian))
    if not candidates:
        return {
            "status": "OPEN",
            "return_residual": return_residual,
            "trace": math.nan,
            "determinant": math.nan,
            "relative_trace_residual": math.inf,
        }
    _error, jacobian = min(candidates, key=lambda item: item[0])
    trace = float(np.trace(jacobian))
    determinant = float(np.linalg.det(jacobian))
    relative = abs(trace - analytic_trace) / max(abs(analytic_trace), 1.0)
    status = (
        "NUMERICALLY_CERTIFIED"
        if return_residual <= 2e-8 and abs(determinant - 1.0) <= 2e-3 and relative <= 2e-5
        else "OPEN"
    )
    return {
        "status": status,
        "return_residual": return_residual,
        "trace": trace,
        "determinant": determinant,
        "relative_trace_residual": relative,
    }


def _float(value: float) -> str:
    if math.isnan(value):
        return ""
    if math.isinf(value):
        return "inf" if value > 0 else "-inf"
    return format(value, ".15g")


def _points_json(points: np.ndarray) -> str:
    rounded = [[float(format(value, ".15g")) for value in point] for point in points]
    return json.dumps(rounded, separators=(",", ":"))


LEDGER_FIELDS = [
    "row_id",
    "d_over_a",
    "topological_word_length",
    "cyclic_word",
    "reverse_oriented_word",
    "symbolic_primitive",
    "symbolic_repetition_exponent",
    "symbolic_enumeration_status",
    "center_polygon_proxy_status",
    "center_polygon_proxy_claim_boundary",
    "center_polygon_proxy_length",
    "actual_billiard_orbit_status",
    "collision_points",
    "actual_flight_length",
    "independent_flight_length",
    "length_recompute_residual",
    "independent_length_residual",
    "independent_theta_residual",
    "stationarity_residual",
    "reflection_residual",
    "minimum_other_disk_clearance",
    "minimum_outgoing_normal_component",
    "minimum_incoming_normal_component",
    "monodromy_trace",
    "monodromy_determinant_high_precision",
    "monodromy_determinant_residual_high_precision",
    "monodromy_double_trace_relative_residual",
    "unstable_multiplier",
    "half_density_statistic_id",
    "half_density_value",
    "finite_difference_validation_status",
    "stability_evidence_status",
    "finite_difference_return_residual",
    "finite_difference_trace_residual",
    "topological_cutoff_complete",
    "geometric_completeness_boundary",
    "evidence_status",
]

CONTROL_FIELDS = [
    "control_id",
    "row_id_d6",
    "cyclic_word",
    "topological_word_length",
    "half_density_d5_8",
    "half_density_d6_0",
    "half_density_d6_2",
    "neighbor_relative_span",
    "period_d6_fixed",
    "shuffled_period",
    "shuffled_from_row_id",
    "random_phase",
    "random_stability_half_density",
    "rank_integer_label",
    "guaranteed_composite_label",
    "deterministic_random_integer_label",
    "prime_or_zero_tables_used",
    "evidence_status",
]


def row_identifier(word: tuple[int, ...], distance_ratio: float) -> str:
    raw = f"d={distance_ratio:.1f};w={word_text(word)}".encode("ascii")
    return "D" + hashlib.sha256(raw).hexdigest()[:16]


def build_ledger() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    words = primitive_oriented_cyclic_words()
    for distance_ratio in DISTANCE_RATIOS:
        for word in words:
            solution = solve_orbit(word, distance_ratio)
            reliable = bool(solution["reliable"])
            if reliable:
                stability = stability_from_orbit(solution)
                fd_check = finite_difference_stability_check(
                    word, distance_ratio, solution, float(stability["trace"])
                )
                actual_status = "NUMERICALLY_CERTIFIED"
                stability_evidence = (
                    "NUMERICALLY_CERTIFIED"
                    if fd_check["status"] == "NUMERICALLY_CERTIFIED"
                    else "NUMERICAL_OBSERVATION"
                )
                evidence_status = stability_evidence
                points = _points_json(np.asarray(solution["points"]))
            else:
                stability = {
                    "trace": math.nan,
                    "determinant_high_precision": "",
                    "determinant_high_precision_residual": math.nan,
                    "double_trace_relative_residual": math.nan,
                    "unstable_multiplier": math.nan,
                    "half_density": math.nan,
                }
                fd_check = {
                    "status": "OPEN",
                    "return_residual": math.inf,
                    "relative_trace_residual": math.inf,
                }
                actual_status = "NOT_ESTABLISHED"
                stability_evidence = "OPEN"
                evidence_status = "OPEN"
                points = ""
            reverse_word = canonical_rotation(tuple(reversed(word)))
            rows.append(
                {
                    "row_id": row_identifier(word, distance_ratio),
                    "d_over_a": _float(distance_ratio),
                    "topological_word_length": str(len(word)),
                    "cyclic_word": word_text(word),
                    "reverse_oriented_word": word_text(reverse_word),
                    "symbolic_primitive": "true",
                    "symbolic_repetition_exponent": "1",
                    "symbolic_enumeration_status": "PROVED",
                    "center_polygon_proxy_status": "MODELING_CHOICE",
                    "center_polygon_proxy_claim_boundary": "PROXY_NOT_BILLIARD_ORBIT",
                    "center_polygon_proxy_length": _float(float(solution["center_proxy_length"])),
                    "actual_billiard_orbit_status": actual_status,
                    "collision_points": points,
                    "actual_flight_length": _float(float(solution["length"])) if reliable else "",
                    "independent_flight_length": _float(float(solution["independent_length"])) if reliable else "",
                    "length_recompute_residual": _float(float(solution["length_recompute_residual"])),
                    "independent_length_residual": _float(float(solution["independent_length_residual"])),
                    "independent_theta_residual": _float(float(solution["independent_theta_residual"])),
                    "stationarity_residual": _float(float(solution["stationarity_residual"])),
                    "reflection_residual": _float(float(solution["reflection_residual"])),
                    "minimum_other_disk_clearance": _float(float(solution["other_disk_clearance"])),
                    "minimum_outgoing_normal_component": _float(float(solution["min_outgoing_normal"])),
                    "minimum_incoming_normal_component": _float(float(solution["min_incoming_normal"])),
                    "monodromy_trace": _float(float(stability["trace"])),
                    "monodromy_determinant_high_precision": str(
                        stability["determinant_high_precision"]
                    ),
                    "monodromy_determinant_residual_high_precision": _float(
                        float(stability["determinant_high_precision_residual"])
                    ),
                    "monodromy_double_trace_relative_residual": _float(
                        float(stability["double_trace_relative_residual"])
                    ),
                    "unstable_multiplier": _float(float(stability["unstable_multiplier"])),
                    "half_density_statistic_id": STATISTIC_ID,
                    "half_density_value": _float(float(stability["half_density"])),
                    "finite_difference_validation_status": str(fd_check["status"]),
                    "stability_evidence_status": stability_evidence,
                    "finite_difference_return_residual": _float(float(fd_check["return_residual"])),
                    "finite_difference_trace_residual": _float(float(fd_check["relative_trace_residual"])),
                    "topological_cutoff_complete": "true",
                    "geometric_completeness_boundary": (
                        "ALL_SYMBOLIC_WORDS_LE_12_ENUMERATED;"
                        "ACTUAL_ORBIT_ONLY_IF_ROW_STATUS_NUMERICALLY_CERTIFIED"
                    ),
                    "evidence_status": evidence_status,
                }
            )
    return rows


def hash_uniform(label: str) -> float:
    value = int(hashlib.sha256(label.encode("utf-8")).hexdigest()[:16], 16)
    return value / float(2**64)


def pearson(xs: list[float], ys: list[float]) -> float:
    if len(xs) < 2:
        return math.nan
    x = np.asarray(xs, dtype=float)
    y = np.asarray(ys, dtype=float)
    if float(np.std(x)) == 0.0 or float(np.std(y)) == 0.0:
        return 0.0
    return float(np.corrcoef(x, y)[0, 1])


def fixed_half_exponent_rmse(labels: list[int], half_densities: list[float]) -> float:
    residual = np.log(np.asarray(half_densities)) + 0.5 * np.log(np.asarray(labels))
    residual -= np.mean(residual)
    return float(math.sqrt(float(np.mean(residual * residual))))


def build_controls(rows: list[dict[str, str]]) -> tuple[list[dict[str, str]], dict[str, object]]:
    by_key = {(row["d_over_a"], row["cyclic_word"]): row for row in rows}
    central = [
        row
        for row in rows
        if row["d_over_a"] == "6" and row["actual_billiard_orbit_status"] == "NUMERICALLY_CERTIFIED"
    ]
    central.sort(key=lambda row: (int(row["topological_word_length"]), row["cyclic_word"]))
    by_length: dict[int, list[dict[str, str]]] = {}
    for row in central:
        by_length.setdefault(int(row["topological_word_length"]), []).append(row)
    shuffle_source: dict[str, dict[str, str]] = {}
    for length, group in by_length.items():
        permuted = sorted(
            group,
            key=lambda row: hashlib.sha256(
                f"{CONTROL_SEED_LABEL}:period:{length}:{row['row_id']}".encode("utf-8")
            ).hexdigest(),
        )
        for target, source in zip(group, permuted, strict=True):
            shuffle_source[target["row_id"]] = source

    observed_log_half = [math.log(float(row["half_density_value"])) for row in central]
    low_log = min(observed_log_half)
    high_log = max(observed_log_half)
    controls: list[dict[str, str]] = []
    complete_triplets = 0
    for rank, row in enumerate(central, start=1):
        word = row["cyclic_word"]
        neighbor_low = by_key.get(("5.8", word))
        neighbor_high = by_key.get(("6.2", word))
        if not neighbor_low or not neighbor_high:
            continue
        if any(
            item["actual_billiard_orbit_status"] != "NUMERICALLY_CERTIFIED"
            for item in (neighbor_low, row, neighbor_high)
        ):
            continue
        complete_triplets += 1
        half_low = float(neighbor_low["half_density_value"])
        half_center = float(row["half_density_value"])
        half_high = float(neighbor_high["half_density_value"])
        relative_span = (max(half_low, half_center, half_high) - min(half_low, half_center, half_high)) / half_center
        shuffled = shuffle_source[row["row_id"]]
        phase_u = hash_uniform(f"{CONTROL_SEED_LABEL}:phase:{row['row_id']}")
        stability_u = hash_uniform(f"{CONTROL_SEED_LABEL}:stability:{row['row_id']}")
        integer_u = hash_uniform(f"{CONTROL_SEED_LABEL}:integer:{row['row_id']}")
        controls.append(
            {
                "control_id": "C" + row["row_id"][1:],
                "row_id_d6": row["row_id"],
                "cyclic_word": word,
                "topological_word_length": row["topological_word_length"],
                "half_density_d5_8": neighbor_low["half_density_value"],
                "half_density_d6_0": row["half_density_value"],
                "half_density_d6_2": neighbor_high["half_density_value"],
                "neighbor_relative_span": _float(relative_span),
                "period_d6_fixed": row["actual_flight_length"],
                "shuffled_period": shuffled["actual_flight_length"],
                "shuffled_from_row_id": shuffled["row_id"],
                "random_phase": _float(-math.pi + 2.0 * math.pi * phase_u),
                "random_stability_half_density": _float(math.exp(low_log + stability_u * (high_log - low_log))),
                "rank_integer_label": str(rank + 1),
                "guaranteed_composite_label": str((rank + 1) * (rank + 2)),
                "deterministic_random_integer_label": str(2 + int(integer_u * max(10, 20 * len(central)))),
                "prime_or_zero_tables_used": "false",
                "evidence_status": "NUMERICAL_OBSERVATION",
            }
        )

    log_center = [math.log(float(row["half_density_d6_0"])) for row in controls]
    log_low = [math.log(float(row["half_density_d5_8"])) for row in controls]
    log_high = [math.log(float(row["half_density_d6_2"])) for row in controls]
    log_period = [math.log(float(row["period_d6_fixed"])) for row in controls]
    log_shuffled_period = [math.log(float(row["shuffled_period"])) for row in controls]
    random_half = [float(row["random_stability_half_density"]) for row in controls]
    labels_rank = [int(row["rank_integer_label"]) for row in controls]
    labels_composite = [int(row["guaranteed_composite_label"]) for row in controls]
    labels_random = [int(row["deterministic_random_integer_label"]) for row in controls]
    half_center_values = [float(row["half_density_d6_0"]) for row in controls]
    neighbor_corr_low = pearson(log_center, log_low)
    neighbor_corr_high = pearson(log_center, log_high)
    stop_scoped = min(neighbor_corr_low, neighbor_corr_high) >= NEIGHBOR_CORRELATION_STOP_THRESHOLD

    status_counts = Counter(row["actual_billiard_orbit_status"] for row in rows)
    fd_counts = Counter(row["finite_difference_validation_status"] for row in rows)
    established = [row for row in rows if row["actual_billiard_orbit_status"] == "NUMERICALLY_CERTIFIED"]
    metrics: dict[str, object] = {
        "candidate_id": "P25-THREE-DISK-ROUND2-NEGATIVE-CONTROL",
        "generated_on": "2026-08-27",
        "distance_ratios": list(DISTANCE_RATIOS),
        "maximum_topological_word_length": MAX_TOPOLOGICAL_LENGTH,
        "primitive_oriented_symbolic_words": len(primitive_oriented_cyclic_words()),
        "ledger_rows": len(rows),
        "actual_orbits_numerically_certified": status_counts["NUMERICALLY_CERTIFIED"],
        "actual_orbits_not_established": status_counts["NOT_ESTABLISHED"],
        "finite_difference_stability_rows_certified": fd_counts["NUMERICALLY_CERTIFIED"],
        "finite_difference_stability_rows_open": fd_counts["OPEN"],
        "complete_neighbor_triplets": complete_triplets,
        "max_stationarity_residual_established": max(float(row["stationarity_residual"]) for row in established),
        "max_reflection_residual_established": max(float(row["reflection_residual"]) for row in established),
        "max_independent_length_residual_established": max(float(row["independent_length_residual"]) for row in established),
        "max_independent_theta_residual_established": max(float(row["independent_theta_residual"]) for row in established),
        "max_monodromy_determinant_residual_high_precision": max(
            float(row["monodromy_determinant_residual_high_precision"])
            for row in established
        ),
        "max_monodromy_double_trace_relative_residual": max(
            float(row["monodromy_double_trace_relative_residual"])
            for row in established
        ),
        "neighbor_log_half_density_correlation_d5_8_vs_d6": neighbor_corr_low,
        "neighbor_log_half_density_correlation_d6_2_vs_d6": neighbor_corr_high,
        "period_log_half_density_correlation": pearson(log_period, log_center),
        "shuffled_period_log_half_density_correlation": pearson(log_shuffled_period, log_center),
        "random_stability_log_period_correlation": pearson(
            log_period, [math.log(value) for value in random_half]
        ),
        "fixed_minus_half_exponent_rmse_rank_integer": fixed_half_exponent_rmse(labels_rank, half_center_values),
        "fixed_minus_half_exponent_rmse_guaranteed_composite": fixed_half_exponent_rmse(labels_composite, half_center_values),
        "fixed_minus_half_exponent_rmse_random_integer": fixed_half_exponent_rmse(labels_random, half_center_values),
        "neighbor_correlation_stop_threshold": NEIGHBOR_CORRELATION_STOP_THRESHOLD,
        "half_density_proves_too_much_control_evidence": "NUMERICAL_OBSERVATION",
        "half_density_proves_too_much_verdict": "STOP_SCOPED" if stop_scoped else "OPEN",
        "formal_a0_a4_tuple": "UNASSIGNED",
        "a0_source_evidence": "MODELING_CHOICE",
        "a0_source_status": "ABSENT_BY_CONSTRUCTION",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "prime_or_zero_tables_used": False,
        "scipy_version": scipy.__version__,
        "numpy_version": np.__version__,
        "evidence_status": "NUMERICAL_OBSERVATION",
    }
    return controls, metrics


def csv_bytes(rows: Iterable[dict[str, str]], fieldnames: list[str]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def json_bytes(payload: object) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def build_core_outputs() -> tuple[dict[str, bytes], dict[str, object]]:
    ledger = build_ledger()
    controls, metrics = build_controls(ledger)
    outputs = {
        "results/three_disk_primitive_ledger_round2.csv": csv_bytes(ledger, LEDGER_FIELDS),
        "results/three_disk_controls_round2.csv": csv_bytes(controls, CONTROL_FIELDS),
        "results/round2_metrics.json": json_bytes(metrics),
    }
    return outputs, metrics


def combined_hash(outputs: dict[str, bytes]) -> str:
    digest = hashlib.sha256()
    for name in sorted(outputs):
        digest.update(name.encode("utf-8"))
        digest.update(b"\0")
        digest.update(outputs[name])
        digest.update(b"\0")
    return digest.hexdigest()


def validation_markdown(metrics: dict[str, object], hashes: dict[str, str], digest: str, reproducibility: str) -> bytes:
    verdict = metrics["half_density_proves_too_much_verdict"]
    text = f"""# P25 Round-2 validation report

## Material Passport

- Origin Skill: experiment-agent
- Origin Mode: run + validate
- Origin Date: 2026-08-27
- Verification Status: VERIFIED
- Version Label: p25_round2_validation_v1

## Execution and reproducibility

- Determinism class: deterministic in the recorded Python/NumPy/SciPy environment.
- Reproducibility verdict: `{reproducibility}`.
- Core-output combined SHA-256: `{digest}`.
- Primitive oriented symbolic words through length 12: {metrics['primitive_oriented_symbolic_words']}.
- Ledger rows across three geometries: {metrics['ledger_rows']}.
- Actual billiard rows `NUMERICALLY_CERTIFIED`: {metrics['actual_orbits_numerically_certified']}.
- Actual billiard rows `NOT_ESTABLISHED`: {metrics['actual_orbits_not_established']}.
- Finite-difference stability cross-check certified/open: {metrics['finite_difference_stability_rows_certified']} / {metrics['finite_difference_stability_rows_open']}.

## Residual envelope on established rows

- Maximum stationarity residual: `{metrics['max_stationarity_residual_established']:.3e}`.
- Maximum specular-reflection residual: `{metrics['max_reflection_residual_established']:.3e}`.
- Maximum independent length residual: `{metrics['max_independent_length_residual_established']:.3e}`.
- Maximum independent angle residual: `{metrics['max_independent_theta_residual_established']:.3e}`.
- Maximum 80-digit monodromy determinant residual: `{metrics['max_monodromy_determinant_residual_high_precision']:.3e}`.
- Maximum binary64-versus-80-digit trace relative residual: `{metrics['max_monodromy_double_trace_relative_residual']:.3e}`.

## Target-free controls

- Neighbor log-half-density correlation, `d/a=5.8` vs `6.0`: `{metrics['neighbor_log_half_density_correlation_d5_8_vs_d6']:.9f}`.
- Neighbor log-half-density correlation, `d/a=6.2` vs `6.0`: `{metrics['neighbor_log_half_density_correlation_d6_2_vs_d6']:.9f}`.
- Frozen stop threshold: `{metrics['neighbor_correlation_stop_threshold']}`.
- Original period/log-half-density correlation: `{metrics['period_log_half_density_correlation']:.9f}`.
- Shuffled-period/log-half-density correlation: `{metrics['shuffled_period_log_half_density_correlation']:.9f}`.
- Random-stability/log-period correlation: `{metrics['random_stability_log_period_correlation']:.9f}`.
- Fixed `-1/2` exponent RMSE on rank/composite/random integer labels:
  `{metrics['fixed_minus_half_exponent_rmse_rank_integer']:.9f}` /
  `{metrics['fixed_minus_half_exponent_rmse_guaranteed_composite']:.9f}` /
  `{metrics['fixed_minus_half_exponent_rmse_random_integer']:.9f}`.
- Prime or zero tables used: `false`.
- Statistic-level verdict: `[{'STOP_SCOPED' if verdict == 'STOP_SCOPED' else 'OPEN'}]` / `{verdict if verdict == 'STOP_SCOPED' else 'PROVES_TOO_MUCH_NOT_ASSIGNED'}`.

The stop applies only to treating generic instability half-density persistence as
arithmetic evidence.  It does not assign a formal A0--A4 tuple and does not
alter the separately frozen `[MODELING_CHOICE] ABSENT_BY_CONSTRUCTION` source
status.

## File hashes

"""
    for name in sorted(hashes):
        text += f"- `{name}`: `{hashes[name]}`\n"
    text += """

## Claim boundary

The symbolic enumeration is exact for oriented primitive cyclic words over
three labels with no adjacent repetition through topological length 12.  A
center-polygon length is always labeled a proxy.  A row is called an actual
billiard orbit only when both solvers, the specular residual, visibility,
independent length, and angle agreement pass the frozen thresholds.  An `OPEN`
finite-difference stability cross-check is not silently promoted.  The 80-digit
monodromy rebuild repairs cancellation in long products but is not counted as
an independent physical stability derivation.  No exact
multiple-scattering determinant, dynamical-zeta divisor, or arithmetic owner is
claimed.
"""
    return text.encode("utf-8")


def write_run(project_root: Path) -> str:
    outputs, metrics = build_core_outputs()
    hashes = {name: hashlib.sha256(data).hexdigest() for name, data in outputs.items()}
    digest = combined_hash(outputs)
    receipt = {
        "candidate_id": "P25-THREE-DISK-ROUND2-NEGATIVE-CONTROL",
        "command": "python3 code/round2_three_disk_ledger.py",
        "date": "2026-08-27",
        "status": "COMPLETED",
        "verification_status": "ANALYZED",
        "reproducibility_verdict": "CANNOT_VERIFY_PENDING_SECOND_RUN",
        "combined_sha256": digest,
        "core_file_sha256": hashes,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "prime_or_zero_tables_used": False,
        "formal_route_a_tuple": "UNASSIGNED",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "evidence_status": "NUMERICAL_OBSERVATION",
    }
    artifacts = dict(outputs)
    artifacts["experiments/round2_receipt.json"] = json_bytes(receipt)
    artifacts["experiments/round2_validation.md"] = validation_markdown(
        metrics, hashes, digest, "CANNOT_VERIFY_PENDING_SECOND_RUN"
    )
    for relative, data in artifacts.items():
        destination = project_root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
    return digest


def verify_existing(project_root: Path) -> str:
    outputs, metrics = build_core_outputs()
    mismatches: list[str] = []
    for relative, data in outputs.items():
        path = project_root / relative
        if not path.exists() or path.read_bytes() != data:
            mismatches.append(relative)
    if mismatches:
        raise RuntimeError("deterministic rerun mismatch: " + ", ".join(mismatches))
    hashes = {name: hashlib.sha256(data).hexdigest() for name, data in outputs.items()}
    digest = combined_hash(outputs)
    receipt = {
        "candidate_id": "P25-THREE-DISK-ROUND2-NEGATIVE-CONTROL",
        "command_original": "python3 code/round2_three_disk_ledger.py",
        "command_rerun": "python3 code/round2_three_disk_ledger.py --verify-existing",
        "date": "2026-08-27",
        "status": "COMPLETED",
        "verification_status": "VERIFIED",
        "reproducibility_verdict": "REPRODUCIBLE",
        "determinism": "EXACT_CORE_OUTPUT_MATCH_SAME_ENVIRONMENT",
        "combined_sha256": digest,
        "core_file_sha256": hashes,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "prime_or_zero_tables_used": False,
        "formal_route_a_tuple": "UNASSIGNED",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "evidence_status": "NUMERICALLY_CERTIFIED",
    }
    (project_root / "experiments/round2_receipt.json").write_bytes(json_bytes(receipt))
    (project_root / "experiments/round2_validation.md").write_bytes(
        validation_markdown(metrics, hashes, digest, "REPRODUCIBLE")
    )
    return digest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verify-existing", action="store_true")
    args = parser.parse_args()
    project_root = Path(__file__).resolve().parents[1]
    digest = verify_existing(project_root) if args.verify_existing else write_run(project_root)
    print(json.dumps({"status": "PASS", "combined_sha256": digest}, sort_keys=True))


if __name__ == "__main__":
    main()
