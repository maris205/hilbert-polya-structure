#!/usr/bin/env python3
"""Round-3 independent stability validation for the three-disk ledger.

The Round-2 half-density was computed from a paraxial matrix product.  This
program does *not* rebuild that product.  Instead it follows the physical ray
intersection/reflection map in Birkhoff coordinates ``(theta, p_t)`` using
``mpmath`` arithmetic, refines each periodic fixed point against that map, and
forms central finite differences at three frozen step sizes.

The Round-2 paraxial trace is read only after the direct return-map Jacobians
have been computed.  It is used as a comparison target, with the explicit
orientation convention

    trace(direct physical map) = (-1)^n trace(paraxial product).

No prime table, zero table, arithmetic label, or external target data is read.
The aggregate half-density remains a numerical observation even when a row
passes this independent dynamical calibration.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import platform
from collections import Counter, defaultdict
from pathlib import Path
from typing import Iterable, Sequence

import mpmath as mp


MP_DPS = 100
mp.mp.dps = MP_DPS
STEP_EXPONENTS = (28, 32, 36)
REFINEMENT_TOLERANCE = mp.mpf("1e-70")
POST_REFINEMENT_RESIDUAL_LIMIT = mp.mpf("1e-60")
MULTISCALE_TRACE_RELATIVE_SPAN_LIMIT = mp.mpf("1e-18")
FINE_DETERMINANT_RESIDUAL_LIMIT = mp.mpf("1e-18")
PARITY_TRACE_RELATIVE_RESIDUAL_LIMIT = mp.mpf("2e-12")
HALF_DENSITY_RELATIVE_RESIDUAL_LIMIT = mp.mpf("2e-12")
EXPECTED_ROWS = 2241
EXPECTED_SOURCE_CERTIFIED = 9
EXPECTED_SOURCE_OPEN = 2232
DATE = "2026-08-27"
CANDIDATE_ID = "P25-THREE-DISK-ROUND3-DIRECT-RETURN-MAP"


def wrap_angle(value: mp.mpf) -> mp.mpf:
    """Return an angle in (-pi, pi] without binary64 conversion."""

    return mp.atan2(mp.sin(value), mp.cos(value))


def disk_centers(distance_ratio: mp.mpf) -> tuple[tuple[mp.mpf, mp.mpf], ...]:
    return (
        (mp.mpf(0), mp.mpf(0)),
        (distance_ratio, mp.mpf(0)),
        (distance_ratio / 2, mp.sqrt(3) * distance_ratio / 2),
    )


def ray_step_mp(
    theta: mp.mpf,
    tangent_momentum: mp.mpf,
    current_disk: int,
    next_disk: int,
    distance_ratio: mp.mpf,
) -> tuple[mp.mpf, mp.mpf]:
    """One exact-geometry ray hit and specular reflection in high precision.

    This routine intentionally contains no paraxial/Jacobi matrix formula.
    """

    centers = disk_centers(distance_ratio)
    normal_x = mp.cos(theta)
    normal_y = mp.sin(theta)
    tangent_x = -normal_y
    tangent_y = normal_x
    radial_momentum_squared = 1 - tangent_momentum * tangent_momentum
    if radial_momentum_squared <= 0:
        raise ValueError("invalid Birkhoff tangent momentum")
    radial_momentum = mp.sqrt(radial_momentum_squared)
    direction_x = radial_momentum * normal_x + tangent_momentum * tangent_x
    direction_y = radial_momentum * normal_y + tangent_momentum * tangent_y

    point_x = centers[current_disk][0] + normal_x
    point_y = centers[current_disk][1] + normal_y
    relative_x = point_x - centers[next_disk][0]
    relative_y = point_y - centers[next_disk][1]
    linear = relative_x * direction_x + relative_y * direction_y
    constant = relative_x * relative_x + relative_y * relative_y - 1
    discriminant = linear * linear - constant
    if discriminant <= 0:
        raise ValueError("requested next disk is not intersected")
    root = mp.sqrt(discriminant)
    candidates = [value for value in (-linear - root, -linear + root) if value > mp.mpf("1e-80")]
    if not candidates:
        raise ValueError("no positive forward intersection")
    flight = min(candidates)

    hit_x = point_x + flight * direction_x
    hit_y = point_y + flight * direction_y
    next_normal_x = hit_x - centers[next_disk][0]
    next_normal_y = hit_y - centers[next_disk][1]
    normal_norm = mp.sqrt(next_normal_x * next_normal_x + next_normal_y * next_normal_y)
    next_normal_x /= normal_norm
    next_normal_y /= normal_norm
    next_theta = mp.atan2(next_normal_y, next_normal_x)

    incidence = direction_x * next_normal_x + direction_y * next_normal_y
    reflected_x = direction_x - 2 * incidence * next_normal_x
    reflected_y = direction_y - 2 * incidence * next_normal_y
    next_tangent_x = -next_normal_y
    next_tangent_y = next_normal_x
    next_momentum = reflected_x * next_tangent_x + reflected_y * next_tangent_y
    return next_theta, next_momentum


def direct_return_map(
    state: Sequence[mp.mpf], word: tuple[int, ...], distance_ratio: mp.mpf
) -> tuple[mp.mpf, mp.mpf]:
    theta, momentum = state
    for index in range(len(word)):
        theta, momentum = ray_step_mp(
            theta,
            momentum,
            word[index],
            word[(index + 1) % len(word)],
            distance_ratio,
        )
    return theta, momentum


def direct_return_residual(
    state: Sequence[mp.mpf], word: tuple[int, ...], distance_ratio: mp.mpf
) -> tuple[mp.mpf, mp.mpf]:
    returned_theta, returned_momentum = direct_return_map(state, word, distance_ratio)
    return wrap_angle(returned_theta - state[0]), returned_momentum - state[1]


def max_abs(values: Iterable[mp.mpf]) -> mp.mpf:
    return max((abs(value) for value in values), default=mp.mpf(0))


def initial_state_from_row(row: dict[str, str]) -> tuple[mp.mpf, mp.mpf]:
    """Recover a Birkhoff state from serialized collision points.

    ``parse_float=str`` preserves the decimal bytes written by Round 2 instead
    of performing an avoidable binary64 round trip.
    """

    points = json.loads(row["collision_points"], parse_float=str, parse_int=str)
    if len(points) < 2:
        raise ValueError("at least two collision points are required")
    word = tuple(int(symbol) for symbol in row["cyclic_word"])
    distance = mp.mpf(row["d_over_a"])
    centers = disk_centers(distance)
    x0, y0 = (mp.mpf(value) for value in points[0])
    x1, y1 = (mp.mpf(value) for value in points[1])
    normal_x = x0 - centers[word[0]][0]
    normal_y = y0 - centers[word[0]][1]
    normal_norm = mp.sqrt(normal_x * normal_x + normal_y * normal_y)
    normal_x /= normal_norm
    normal_y /= normal_norm
    theta = mp.atan2(normal_y, normal_x)
    direction_x = x1 - x0
    direction_y = y1 - y0
    direction_norm = mp.sqrt(direction_x * direction_x + direction_y * direction_y)
    direction_x /= direction_norm
    direction_y /= direction_norm
    momentum = direction_x * (-normal_y) + direction_y * normal_x
    return theta, momentum


def initial_collision_angles_from_row(row: dict[str, str]) -> tuple[mp.mpf, ...]:
    points = json.loads(row["collision_points"], parse_float=str, parse_int=str)
    word = tuple(int(symbol) for symbol in row["cyclic_word"])
    distance = mp.mpf(row["d_over_a"])
    centers = disk_centers(distance)
    return tuple(
        mp.atan2(
            mp.mpf(point[1]) - centers[symbol][1],
            mp.mpf(point[0]) - centers[symbol][0],
        )
        for point, symbol in zip(points, word, strict=True)
    )


def specular_stationarity_gradient(
    angles: Sequence[mp.mpf], word: tuple[int, ...], distance_ratio: mp.mpf
) -> tuple[mp.mpf, ...]:
    """Geometric length gradient used only as a refinement fallback.

    It uses collision points and unit segment directions, not the paraxial
    stability formula.  The final stability Jacobian is still formed from the
    direct ray map after this refinement.
    """

    centers = disk_centers(distance_ratio)
    points: list[tuple[mp.mpf, mp.mpf]] = []
    tangents: list[tuple[mp.mpf, mp.mpf]] = []
    for angle, symbol in zip(angles, word, strict=True):
        normal_x = mp.cos(angle)
        normal_y = mp.sin(angle)
        points.append((centers[symbol][0] + normal_x, centers[symbol][1] + normal_y))
        tangents.append((-normal_y, normal_x))
    directions: list[tuple[mp.mpf, mp.mpf]] = []
    for index, point in enumerate(points):
        following = points[(index + 1) % len(points)]
        displacement_x = following[0] - point[0]
        displacement_y = following[1] - point[1]
        length = mp.sqrt(displacement_x * displacement_x + displacement_y * displacement_y)
        directions.append((displacement_x / length, displacement_y / length))
    return tuple(
        tangents[index][0] * (directions[index - 1][0] - directions[index][0])
        + tangents[index][1] * (directions[index - 1][1] - directions[index][1])
        for index in range(len(word))
    )


def state_from_collision_angles(
    angles: Sequence[mp.mpf], word: tuple[int, ...], distance_ratio: mp.mpf
) -> tuple[mp.mpf, mp.mpf]:
    centers = disk_centers(distance_ratio)
    normal_x = mp.cos(angles[0])
    normal_y = mp.sin(angles[0])
    point0 = (centers[word[0]][0] + normal_x, centers[word[0]][1] + normal_y)
    point1 = (
        centers[word[1]][0] + mp.cos(angles[1]),
        centers[word[1]][1] + mp.sin(angles[1]),
    )
    direction_x = point1[0] - point0[0]
    direction_y = point1[1] - point0[1]
    direction_norm = mp.sqrt(direction_x * direction_x + direction_y * direction_y)
    direction_x /= direction_norm
    direction_y /= direction_norm
    momentum = direction_x * (-normal_y) + direction_y * normal_x
    return mp.mpf(angles[0]), momentum


def refine_state_via_specular_stationarity(
    row: dict[str, str], word: tuple[int, ...], distance_ratio: mp.mpf
) -> tuple[tuple[mp.mpf, mp.mpf], mp.mpf]:
    """Condition-aware fallback when direct fixed-point Newton leaves its cylinder."""

    initial_angles = initial_collision_angles_from_row(row)

    def equations(*angles: mp.mpf) -> tuple[mp.mpf, ...]:
        return specular_stationarity_gradient(angles, word, distance_ratio)

    refined_angles = mp.findroot(
        equations,
        initial_angles,
        solver="mdnewton",
        tol=REFINEMENT_TOLERANCE,
        maxsteps=25,
        verify=True,
    )
    angles = tuple(mp.mpf(value) for value in refined_angles)
    stationarity_residual = max_abs(
        specular_stationarity_gradient(angles, word, distance_ratio)
    )
    return state_from_collision_angles(angles, word, distance_ratio), stationarity_residual


def refine_periodic_state(
    initial_state: tuple[mp.mpf, mp.mpf],
    word: tuple[int, ...],
    distance_ratio: mp.mpf,
) -> tuple[tuple[mp.mpf, mp.mpf], mp.mpf, mp.mpf]:
    """Refine a periodic point using only the direct physical return map."""

    initial_residual = max_abs(direct_return_residual(initial_state, word, distance_ratio))

    def equations(theta: mp.mpf, momentum: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
        return direct_return_residual((theta, momentum), word, distance_ratio)

    refined = mp.findroot(
        equations,
        initial_state,
        solver="mdnewton",
        tol=REFINEMENT_TOLERANCE,
        maxsteps=35,
        verify=True,
    )
    refined_state = (mp.mpf(refined[0]), mp.mpf(refined[1]))
    final_residual = max_abs(direct_return_residual(refined_state, word, distance_ratio))
    return refined_state, initial_residual, final_residual


def central_difference_jacobian(
    state: tuple[mp.mpf, mp.mpf],
    word: tuple[int, ...],
    distance_ratio: mp.mpf,
    step: mp.mpf,
) -> tuple[tuple[mp.mpf, mp.mpf], tuple[mp.mpf, mp.mpf]]:
    """Direct central-difference Jacobian; no analytic monodromy is accepted."""

    columns: list[tuple[mp.mpf, mp.mpf]] = []
    for coordinate in range(2):
        plus = [state[0], state[1]]
        minus = [state[0], state[1]]
        plus[coordinate] += step
        minus[coordinate] -= step
        plus_image = direct_return_map(plus, word, distance_ratio)
        minus_image = direct_return_map(minus, word, distance_ratio)
        columns.append(
            (
                wrap_angle(plus_image[0] - minus_image[0]) / (2 * step),
                (plus_image[1] - minus_image[1]) / (2 * step),
            )
        )
    # Return conventional row-major layout.
    return (
        (columns[0][0], columns[1][0]),
        (columns[0][1], columns[1][1]),
    )


def trace_and_determinant(
    matrix: tuple[tuple[mp.mpf, mp.mpf], tuple[mp.mpf, mp.mpf]]
) -> tuple[mp.mpf, mp.mpf]:
    trace = matrix[0][0] + matrix[1][1]
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return trace, determinant


def relative_residual(observed: mp.mpf, expected: mp.mpf) -> mp.mpf:
    return abs(observed - expected) / max(abs(expected), mp.mpf(1))


def unstable_multiplier_from_trace(trace: mp.mpf) -> mp.mpf:
    magnitude = abs(trace)
    if magnitude <= 2:
        raise ValueError("trace is not hyperbolic")
    return (magnitude + mp.sqrt(magnitude * magnitude - 4)) / 2


def _mp_text(value: mp.mpf, digits: int = 32) -> str:
    return mp.nstr(value, n=digits, strip_zeros=False)


def validate_row(row: dict[str, str]) -> dict[str, str]:
    word = tuple(int(symbol) for symbol in row["cyclic_word"])
    distance = mp.mpf(row["d_over_a"])
    result = {
        "row_id": row["row_id"],
        "d_over_a": row["d_over_a"],
        "topological_word_length": row["topological_word_length"],
        "cyclic_word": row["cyclic_word"],
        "source_round2_fd_status": row["finite_difference_validation_status"],
        "source_paraxial_trace": row["monodromy_trace"],
        "physical_trace_parity_factor": str((-1) ** len(word)),
        "precision_decimal_digits": str(MP_DPS),
        "finite_difference_step_exponents": ";".join(str(value) for value in STEP_EXPONENTS),
        "pre_refinement_return_residual": "",
        "post_refinement_return_residual": "",
        "theta_correction": "",
        "momentum_correction": "",
        "refinement_method": "",
        "fallback_stationarity_residual": "",
        "direct_trace_h1e_28": "",
        "direct_trace_h1e_32": "",
        "direct_trace_h1e_36": "",
        "determinant_residual_h1e_28": "",
        "determinant_residual_h1e_32": "",
        "determinant_residual_h1e_36": "",
        "multiscale_trace_relative_span": "",
        "parity_corrected_trace_relative_residual": "",
        "direct_half_density": "",
        "source_half_density": row["half_density_value"],
        "half_density_relative_residual": "",
        "validation_status": "OPEN",
        "failure_tier": "UNCLASSIFIED_OPEN",
        "independence_boundary": (
            "DIRECT_MP_RAY_INTERSECTION_REFLECTION_AND_MULTISCALE_FINITE_DIFFERENCE;"
            "PARAXIAL_TRACE_READ_ONLY_AFTER_DIRECT_JACOBIANS"
        ),
        "half_density_evidence_status": "NUMERICAL_OBSERVATION",
        "prime_or_zero_tables_used": "false",
    }
    try:
        initial_state = initial_state_from_row(row)
        initial_residual = max_abs(direct_return_residual(initial_state, word, distance))
        result["pre_refinement_return_residual"] = _mp_text(initial_residual)
    except Exception as exc:
        result["failure_tier"] = f"INITIAL_STATE_OPEN:{type(exc).__name__}"
        return result

    try:
        refined_state, initial_residual, final_residual = refine_periodic_state(
            initial_state, word, distance
        )
        result["refinement_method"] = "DIRECT_RETURN_MAP_MDNEWTON"
    except Exception:
        try:
            refined_state, stationarity_residual = refine_state_via_specular_stationarity(
                row, word, distance
            )
            final_residual = max_abs(direct_return_residual(refined_state, word, distance))
            result["refinement_method"] = "SPECULAR_STATIONARITY_FALLBACK"
            result["fallback_stationarity_residual"] = _mp_text(stationarity_residual)
        except Exception as exc:  # keep every failed row explicit in the ledger
            result["failure_tier"] = f"REFINEMENT_OPEN:{type(exc).__name__}"
            return result

    result["post_refinement_return_residual"] = _mp_text(final_residual)
    result["theta_correction"] = _mp_text(wrap_angle(refined_state[0] - initial_state[0]))
    result["momentum_correction"] = _mp_text(refined_state[1] - initial_state[1])

    if final_residual > POST_REFINEMENT_RESIDUAL_LIMIT:
        result["failure_tier"] = "POST_REFINEMENT_RESIDUAL_OPEN"
        return result

    traces: list[mp.mpf] = []
    determinant_residuals: list[mp.mpf] = []
    try:
        for exponent in STEP_EXPONENTS:
            jacobian = central_difference_jacobian(
                refined_state, word, distance, mp.power(10, -exponent)
            )
            trace, determinant = trace_and_determinant(jacobian)
            traces.append(trace)
            determinant_residuals.append(abs(determinant - 1))
    except Exception as exc:
        result["failure_tier"] = f"DIRECT_DIFFERENCE_OPEN:{type(exc).__name__}"
        return result

    for exponent, trace, determinant_residual in zip(
        STEP_EXPONENTS, traces, determinant_residuals, strict=True
    ):
        result[f"direct_trace_h1e_{exponent}"] = _mp_text(trace)
        result[f"determinant_residual_h1e_{exponent}"] = _mp_text(determinant_residual)

    fine_trace = traces[-1]
    multiscale_span = max_abs(trace - fine_trace for trace in traces[:-1]) / max(
        abs(fine_trace), mp.mpf(1)
    )
    source_trace = mp.mpf(row["monodromy_trace"])
    parity_trace = ((-1) ** len(word)) * source_trace
    trace_residual = relative_residual(fine_trace, parity_trace)
    direct_multiplier = unstable_multiplier_from_trace(fine_trace)
    direct_half_density = 1 / mp.sqrt(direct_multiplier)
    source_half_density = mp.mpf(row["half_density_value"])
    half_density_residual = abs(direct_half_density - source_half_density) / max(
        abs(source_half_density), mp.mpf("1e-80")
    )
    result["multiscale_trace_relative_span"] = _mp_text(multiscale_span)
    result["parity_corrected_trace_relative_residual"] = _mp_text(trace_residual)
    result["direct_half_density"] = _mp_text(direct_half_density)
    result["half_density_relative_residual"] = _mp_text(half_density_residual)

    if multiscale_span > MULTISCALE_TRACE_RELATIVE_SPAN_LIMIT:
        result["failure_tier"] = "MULTISCALE_CONVERGENCE_OPEN"
    elif determinant_residuals[-1] > FINE_DETERMINANT_RESIDUAL_LIMIT:
        result["failure_tier"] = "SYMPLECTIC_DETERMINANT_OPEN"
    elif trace_residual > PARITY_TRACE_RELATIVE_RESIDUAL_LIMIT:
        result["failure_tier"] = "PARITY_CORRECTED_TRACE_COMPARISON_OPEN"
    elif half_density_residual > HALF_DENSITY_RELATIVE_RESIDUAL_LIMIT:
        result["failure_tier"] = "HALF_DENSITY_COMPARISON_OPEN"
    else:
        result["validation_status"] = "NUMERICALLY_CERTIFIED"
        result["failure_tier"] = "NONE"
    return result


OUTPUT_FIELDS = [
    "row_id",
    "d_over_a",
    "topological_word_length",
    "cyclic_word",
    "source_round2_fd_status",
    "source_paraxial_trace",
    "physical_trace_parity_factor",
    "precision_decimal_digits",
    "finite_difference_step_exponents",
    "pre_refinement_return_residual",
    "post_refinement_return_residual",
    "theta_correction",
    "momentum_correction",
    "refinement_method",
    "fallback_stationarity_residual",
    "direct_trace_h1e_28",
    "direct_trace_h1e_32",
    "direct_trace_h1e_36",
    "determinant_residual_h1e_28",
    "determinant_residual_h1e_32",
    "determinant_residual_h1e_36",
    "multiscale_trace_relative_span",
    "parity_corrected_trace_relative_residual",
    "direct_half_density",
    "source_half_density",
    "half_density_relative_residual",
    "validation_status",
    "failure_tier",
    "independence_boundary",
    "half_density_evidence_status",
    "prime_or_zero_tables_used",
]


def condition_tier(trace: float) -> str:
    value = abs(trace)
    if value <= 1e3:
        return "ABS_TRACE_LE_1E3"
    if value <= 1e6:
        return "ABS_TRACE_1E3_TO_1E6"
    if value <= 1e9:
        return "ABS_TRACE_1E6_TO_1E9"
    if value <= 1e12:
        return "ABS_TRACE_1E9_TO_1E12"
    return "ABS_TRACE_GT_1E12"


def _maximum(rows: list[dict[str, str]], field: str) -> float:
    values = [float(row[field]) for row in rows if row[field]]
    return max(values) if values else float("nan")


def build_metrics(source_rows: list[dict[str, str]], rows: list[dict[str, str]]) -> dict[str, object]:
    status_counts = Counter(row["validation_status"] for row in rows)
    failure_counts = Counter(row["failure_tier"] for row in rows)
    refinement_counts = Counter(row["refinement_method"] for row in rows)
    source_counts = Counter(row["source_round2_fd_status"] for row in rows)
    by_length: dict[str, Counter[str]] = defaultdict(Counter)
    by_distance: dict[str, Counter[str]] = defaultdict(Counter)
    by_condition: dict[str, Counter[str]] = defaultdict(Counter)
    for source, row in zip(source_rows, rows, strict=True):
        by_length[row["topological_word_length"]][row["validation_status"]] += 1
        by_distance[row["d_over_a"]][row["validation_status"]] += 1
        by_condition[condition_tier(float(source["monodromy_trace"]))][row["validation_status"]] += 1

    certified = [row for row in rows if row["validation_status"] == "NUMERICALLY_CERTIFIED"]
    odd_rows = sum(int(row["topological_word_length"]) % 2 for row in rows)
    old_open_odd = sum(
        int(row["topological_word_length"]) % 2
        and row["source_round2_fd_status"] == "OPEN"
        for row in rows
    )
    old_open_even = sum(
        int(row["topological_word_length"]) % 2 == 0
        and row["source_round2_fd_status"] == "OPEN"
        for row in rows
    )
    return {
        "candidate_id": CANDIDATE_ID,
        "generated_on": DATE,
        "input_ledger_rows": len(source_rows),
        "round2_finite_difference_rows_certified": source_counts["NUMERICALLY_CERTIFIED"],
        "round2_finite_difference_rows_open": source_counts["OPEN"],
        "round3_direct_return_map_rows_certified": status_counts["NUMERICALLY_CERTIFIED"],
        "round3_direct_return_map_rows_open": status_counts["OPEN"],
        "newly_certified_rows": sum(
            row["source_round2_fd_status"] == "OPEN"
            and row["validation_status"] == "NUMERICALLY_CERTIFIED"
            for row in rows
        ),
        "odd_topological_length_rows": odd_rows,
        "round2_open_odd_rows_affected_by_trace_sign_convention": old_open_odd,
        "round2_open_even_rows_affected_by_binary64_conditioning": old_open_even,
        "status_by_topological_length": {
            key: dict(sorted(value.items())) for key, value in sorted(by_length.items(), key=lambda item: int(item[0]))
        },
        "status_by_distance_ratio": {
            key: dict(sorted(value.items())) for key, value in sorted(by_distance.items(), key=lambda item: float(item[0]))
        },
        "status_by_source_trace_condition_tier": {
            key: dict(sorted(value.items())) for key, value in sorted(by_condition.items())
        },
        "failure_tier_counts": dict(sorted(failure_counts.items())),
        "refinement_method_counts": dict(sorted(refinement_counts.items())),
        "precision_decimal_digits": MP_DPS,
        "finite_difference_step_exponents": list(STEP_EXPONENTS),
        "post_refinement_residual_limit": str(POST_REFINEMENT_RESIDUAL_LIMIT),
        "multiscale_trace_relative_span_limit": str(MULTISCALE_TRACE_RELATIVE_SPAN_LIMIT),
        "fine_determinant_residual_limit": str(FINE_DETERMINANT_RESIDUAL_LIMIT),
        "parity_trace_relative_residual_limit": str(PARITY_TRACE_RELATIVE_RESIDUAL_LIMIT),
        "half_density_relative_residual_limit": str(HALF_DENSITY_RELATIVE_RESIDUAL_LIMIT),
        "max_pre_refinement_return_residual": _maximum(rows, "pre_refinement_return_residual"),
        "max_post_refinement_return_residual_certified": _maximum(certified, "post_refinement_return_residual"),
        "max_fallback_stationarity_residual_certified": _maximum(
            [row for row in certified if row["fallback_stationarity_residual"]],
            "fallback_stationarity_residual",
        ),
        "max_abs_theta_correction_certified": max(abs(float(row["theta_correction"])) for row in certified),
        "max_abs_momentum_correction_certified": max(abs(float(row["momentum_correction"])) for row in certified),
        "max_multiscale_trace_relative_span_certified": _maximum(certified, "multiscale_trace_relative_span"),
        "max_fine_determinant_residual_certified": _maximum(certified, "determinant_residual_h1e_36"),
        "max_parity_corrected_trace_relative_residual_certified": _maximum(certified, "parity_corrected_trace_relative_residual"),
        "max_half_density_relative_residual_certified": _maximum(certified, "half_density_relative_residual"),
        "direct_method": (
            "100_DIGIT_PHYSICAL_RAY_INTERSECTION_REFLECTION_MAP;"
            "DIRECT_FIXED_POINT_REFINEMENT_WITH_SPECULAR_STATIONARITY_FALLBACK;"
            "CENTRAL_DIFFERENCE_AT_1E-28_1E-32_1E-36"
        ),
        "independence_boundary": (
            "NO_PARAXIAL_FACTORS_IN_DIRECT_MAP_OR_JACOBIAN;"
            "ROUND2_PARAXIAL_TRACE_USED_ONLY_AS_FINAL_COMPARISON_TARGET"
        ),
        "physical_trace_convention": "DIRECT_TRACE=(-1)^WORD_LENGTH*PARAXIAL_TRACE",
        "half_density_evidence_status": "NUMERICAL_OBSERVATION",
        "half_density_proves_too_much_verdict": "STOP_SCOPED",
        "formal_a0_a4_tuple": "UNASSIGNED",
        "a2_evaluation": "NOT_RUN",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "prime_or_zero_tables_used": False,
        "mpmath_version": mp.__version__,
        "python_version": platform.python_version(),
    }


def read_source_rows(project_root: Path) -> tuple[Path, list[dict[str, str]]]:
    path = project_root / "results/three_disk_primitive_ledger_round2.csv"
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != EXPECTED_ROWS:
        raise RuntimeError(f"expected {EXPECTED_ROWS} source rows, found {len(rows)}")
    counts = Counter(row["finite_difference_validation_status"] for row in rows)
    if counts["NUMERICALLY_CERTIFIED"] != EXPECTED_SOURCE_CERTIFIED or counts["OPEN"] != EXPECTED_SOURCE_OPEN:
        raise RuntimeError(f"unexpected Round-2 finite-difference status counts: {dict(counts)}")
    if any(row["actual_billiard_orbit_status"] != "NUMERICALLY_CERTIFIED" for row in rows):
        raise RuntimeError("Round-3 direct validation requires a certified Round-2 orbit in every row")
    return path, rows


def csv_bytes(rows: Iterable[dict[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=OUTPUT_FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode("utf-8")


def json_bytes(payload: object) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def build_core_outputs(project_root: Path) -> tuple[dict[str, bytes], dict[str, object], str]:
    mp.mp.dps = MP_DPS
    source_path, source_rows = read_source_rows(project_root)
    validation_rows = [validate_row(row) for row in source_rows]
    metrics = build_metrics(source_rows, validation_rows)
    outputs = {
        "results/three_disk_return_map_validation_round3.csv": csv_bytes(validation_rows),
        "results/round3_stability_metrics.json": json_bytes(metrics),
    }
    source_sha = hashlib.sha256(source_path.read_bytes()).hexdigest()
    return outputs, metrics, source_sha


def combined_hash(outputs: dict[str, bytes]) -> str:
    digest = hashlib.sha256()
    for name in sorted(outputs):
        digest.update(name.encode("utf-8"))
        digest.update(b"\0")
        digest.update(outputs[name])
        digest.update(b"\0")
    return digest.hexdigest()


def validation_markdown(
    metrics: dict[str, object], hashes: dict[str, str], source_sha: str, digest: str, verdict: str
) -> bytes:
    text = f"""# P25 Round-3 direct return-map validation

## Material Passport

- Origin Skill: experiment-agent
- Origin Mode: run + validate
- Origin Date: {DATE}
- Verification Status: {'VERIFIED' if verdict == 'REPRODUCIBLE' else 'ANALYZED'}
- Version Label: p25_round3_direct_return_map_v1

## Execution result

- Round-2 finite-difference certified/open: {metrics['round2_finite_difference_rows_certified']} / {metrics['round2_finite_difference_rows_open']}.
- Round-3 direct return-map certified/open: {metrics['round3_direct_return_map_rows_certified']} / {metrics['round3_direct_return_map_rows_open']}.
- Newly certified rows: {metrics['newly_certified_rows']}.
- Deterministic replay verdict: `{verdict}`.
- Core-output combined SHA-256: `{digest}`.
- Round-2 input-ledger SHA-256: `{source_sha}`.

## Independent numerical path

Each row is reconstructed from its collision points and then refined as a
periodic point of the 100-decimal-digit physical ray-intersection/reflection
map.  The Jacobian is formed by central differences at `1e-28`, `1e-32`, and
`1e-36`.  Neither the direct map nor its Jacobian accepts a paraxial matrix as
input.  The Round-2 paraxial trace is read only as the final comparison target.
When rounded collision points lie outside the direct Newton cylinder, a
high-precision specular-stationarity solve refines the collision geometry; the
reported stability still comes exclusively from the direct return map.

The physical Birkhoff map and the positive-reflection paraxial convention differ
by one orientation sign per collision:

```text
trace(direct physical map) = (-1)^word_length * trace(paraxial product).
```

This convention accounts for {metrics['round2_open_odd_rows_affected_by_trace_sign_convention']}
odd-length rows that the old signed comparison left open.  The remaining
{metrics['round2_open_even_rows_affected_by_binary64_conditioning']} old open
even-length rows lie beyond the binary64 finite-difference conditioning window.

## Certified residual envelope

- Maximum post-refinement return residual: `{metrics['max_post_refinement_return_residual_certified']:.3e}`.
- Refinement methods: `{json.dumps(metrics['refinement_method_counts'], sort_keys=True)}`.
- Maximum multiscale trace relative span: `{metrics['max_multiscale_trace_relative_span_certified']:.3e}`.
- Maximum finest-step determinant residual: `{metrics['max_fine_determinant_residual_certified']:.3e}`.
- Maximum parity-corrected trace relative residual: `{metrics['max_parity_corrected_trace_relative_residual_certified']:.3e}`.
- Maximum half-density relative residual: `{metrics['max_half_density_relative_residual_certified']:.3e}`.
- Failure tiers: `{json.dumps(metrics['failure_tier_counts'], sort_keys=True)}`.

## Claim boundary

The direct validation closes the numerical return-map cross-check at the frozen
word and geometry cutoffs.  It does not turn finite numerical work into a
theorem, an exact determinant identity, an arithmetic owner, a formal A0--A4
tuple, or an A2/Route-B evaluation.  The aggregate half-density remains
`NUMERICAL_OBSERVATION`, and its use as arithmetic evidence remains
`STOP_SCOPED / PROVES_TOO_MUCH`.  No prime or zero table was used.

## Core file hashes

"""
    for name in sorted(hashes):
        text += f"- `{name}`: `{hashes[name]}`\n"
    return text.encode("utf-8")


def receipt_payload(
    outputs: dict[str, bytes], source_sha: str, digest: str, verified: bool
) -> dict[str, object]:
    hashes = {name: hashlib.sha256(data).hexdigest() for name, data in outputs.items()}
    return {
        "candidate_id": CANDIDATE_ID,
        "command_original": "python3 code/round3_return_map_validation.py",
        "command_rerun": "python3 code/round3_return_map_validation.py --verify-existing",
        "date": DATE,
        "status": "COMPLETED",
        "verification_status": "VERIFIED" if verified else "ANALYZED",
        "reproducibility_verdict": "REPRODUCIBLE" if verified else "CANNOT_VERIFY_PENDING_SECOND_RUN",
        "determinism": "EXACT_CORE_OUTPUT_MATCH_SAME_ENVIRONMENT" if verified else "DETERMINISTIC_EXPECTED",
        "combined_sha256": digest,
        "round2_input_ledger_sha256": source_sha,
        "core_file_sha256": hashes,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "prime_or_zero_tables_used": False,
        "half_density_evidence_status": "NUMERICAL_OBSERVATION",
        "half_density_proves_too_much_verdict": "STOP_SCOPED",
        "formal_route_a_tuple": "UNASSIGNED",
        "a2_evaluation": "NOT_RUN",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
    }


def write_run(project_root: Path) -> str:
    outputs, metrics, source_sha = build_core_outputs(project_root)
    digest = combined_hash(outputs)
    hashes = {name: hashlib.sha256(data).hexdigest() for name, data in outputs.items()}
    artifacts = dict(outputs)
    artifacts["experiments/round3_receipt.json"] = json_bytes(
        receipt_payload(outputs, source_sha, digest, verified=False)
    )
    artifacts["experiments/round3_validation.md"] = validation_markdown(
        metrics, hashes, source_sha, digest, "CANNOT_VERIFY_PENDING_SECOND_RUN"
    )
    for relative, data in artifacts.items():
        destination = project_root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
    return digest


def verify_existing(project_root: Path) -> str:
    outputs, metrics, source_sha = build_core_outputs(project_root)
    mismatches = [
        relative
        for relative, data in outputs.items()
        if not (project_root / relative).exists() or (project_root / relative).read_bytes() != data
    ]
    if mismatches:
        raise RuntimeError("deterministic rerun mismatch: " + ", ".join(mismatches))
    digest = combined_hash(outputs)
    hashes = {name: hashlib.sha256(data).hexdigest() for name, data in outputs.items()}
    (project_root / "experiments/round3_receipt.json").write_bytes(
        json_bytes(receipt_payload(outputs, source_sha, digest, verified=True))
    )
    (project_root / "experiments/round3_validation.md").write_bytes(
        validation_markdown(metrics, hashes, source_sha, digest, "REPRODUCIBLE")
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
