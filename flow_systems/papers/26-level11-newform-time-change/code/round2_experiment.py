#!/usr/bin/env python3
"""Deterministic Paper-26 Round-2 finite positive-word experiment.

The exact layer enumerates primitive positive L/R necklaces and retains only
representatives whose left-to-right matrix product lies in Gamma_0(11).  This
is deliberately *not* an enumeration of all primitive Gamma_0(11) conjugacy
classes.  The numerical layer evaluates a frozen q-truncated proxy for the
period of 2*pi*i*eta(z)^2*eta(11z)^2 dz along the invariant axis segment.

No prime table, Hecke-eigenvalue table, or Riemann-zero data is read or used.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from typing import Callable, Iterable, Sequence


Matrix = tuple[int, int, int, int]

IDENTITY: Matrix = (1, 0, 0, 1)
L_MATRIX: Matrix = (1, 1, 0, 1)
R_MATRIX: Matrix = (1, 0, 1, 1)

DEFAULT_MAX_WORD_LENGTH = 9
DEFAULT_Q_CUTOFF = 192
DEFAULT_Q_COMPARISON_CUTOFF = 48
DEFAULT_QUADRATURE_PANELS = 1024
DEFAULT_REPEAT_Q_CUTOFF = 4096
DEFAULT_REPEAT_Q_COMPARISON_CUTOFF = 2048
DEFAULT_REPEAT_QUADRATURE_PANELS = 512
DEFAULT_BASEPOINT_SHIFT = 0.125
DEFAULT_PERMUTATION_SHIFT = 3
GENERIC_J_Q_CUTOFF = 48


@dataclass(frozen=True)
class AxisGeometry:
    center: float
    radius: float
    length: float

    def point(self, u: float) -> complex:
        """Point on the oriented axis; the matrix translates u to u-length."""

        return complex(
            self.center - self.radius * math.tanh(u),
            self.radius / math.cosh(u),
        )

    def derivative(self, u: float) -> complex:
        sech = 1.0 / math.cosh(u)
        return complex(
            -self.radius * sech * sech,
            -self.radius * sech * math.tanh(u),
        )


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    a, b, c, d = left
    e, f, g, h = right
    return (
        a * e + b * g,
        a * f + b * h,
        c * e + d * g,
        c * f + d * h,
    )


def matrix_power(matrix: Matrix, exponent: int) -> Matrix:
    if exponent < 0:
        raise ValueError("matrix_power only supports nonnegative exponents")
    result = IDENTITY
    base = matrix
    power = exponent
    while power:
        if power & 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        power //= 2
    return result


def matrix_from_word(word: str) -> Matrix:
    matrix = IDENTITY
    for letter in word:
        if letter == "L":
            generator = L_MATRIX
        elif letter == "R":
            generator = R_MATRIX
        else:
            raise ValueError(f"unsupported letter {letter!r}")
        matrix = matrix_multiply(matrix, generator)
    return matrix


def determinant(matrix: Matrix) -> int:
    a, b, c, d = matrix
    return a * d - b * c


def trace(matrix: Matrix) -> int:
    return matrix[0] + matrix[3]


def mobius(matrix: Matrix, z: complex) -> complex:
    a, b, c, d = matrix
    return (a * z + b) / (c * z + d)


def canonical_rotation(word: str) -> str:
    return min(word[index:] + word[:index] for index in range(len(word)))


def primitive_root(word: str) -> tuple[str, int]:
    for root_length in range(1, len(word) + 1):
        if len(word) % root_length:
            continue
        root = word[:root_length]
        exponent = len(word) // root_length
        if root * exponent == word:
            return root, exponent
    raise AssertionError("every finite word has a primitive root")


def primitive_positive_necklaces(max_word_length: int) -> list[str]:
    representatives: list[str] = []
    for word_length in range(1, max_word_length + 1):
        for letters in product("LR", repeat=word_length):
            word = "".join(letters)
            root, exponent = primitive_root(word)
            if exponent != 1 or canonical_rotation(word) != word:
                continue
            matrix = matrix_from_word(word)
            if trace(matrix) <= 2:
                continue
            representatives.append(word)
    return representatives


def gamma0_11_positive_necklaces(max_word_length: int) -> list[str]:
    return [
        word
        for word in primitive_positive_necklaces(max_word_length)
        if matrix_from_word(word)[2] % 11 == 0
    ]


def geodesic_length(matrix: Matrix) -> float:
    matrix_trace = abs(trace(matrix))
    if matrix_trace <= 2:
        raise ValueError("geodesic_length requires a hyperbolic matrix")
    return 2.0 * math.acosh(matrix_trace / 2.0)


def axis_geometry(matrix: Matrix) -> AxisGeometry:
    a, _, c, d = matrix
    if c <= 0 or determinant(matrix) != 1 or trace(matrix) <= 2:
        raise ValueError("frozen axis chart requires c>0, determinant 1, trace>2")
    discriminant = trace(matrix) ** 2 - 4
    return AxisGeometry(
        center=(a - d) / (2.0 * c),
        radius=math.sqrt(discriminant) / (2.0 * c),
        length=geodesic_length(matrix),
    )


def multiply_by_squared_euler_factor(coefficients: list[int], exponent: int) -> list[int]:
    cutoff = len(coefficients) - 1
    updated = coefficients.copy()
    for index, value in enumerate(coefficients):
        if value == 0:
            continue
        if index + exponent <= cutoff:
            updated[index + exponent] -= 2 * value
        if index + 2 * exponent <= cutoff:
            updated[index + 2 * exponent] += value
    return updated


def level11_eta_product_coefficients(q_cutoff: int) -> list[int]:
    """Coefficients through q^q_cutoff of eta(z)^2 eta(11z)^2."""

    if q_cutoff < 1:
        raise ValueError("q_cutoff must be positive")
    coefficients = [0] * (q_cutoff + 1)
    coefficients[1] = 1
    for exponent in range(1, q_cutoff + 1):
        coefficients = multiply_by_squared_euler_factor(coefficients, exponent)
    for index in range(1, q_cutoff // 11 + 1):
        coefficients = multiply_by_squared_euler_factor(coefficients, 11 * index)
    return coefficients


def evaluate_q_series(coefficients: Sequence[int], z: complex) -> complex:
    q = complex(math.e) ** (2.0j * math.pi * z)
    value = 0.0j
    for coefficient in reversed(coefficients):
        value = value * q + coefficient
    return value


def composite_simpson(
    function: Callable[[float], complex | float], panels: int
) -> complex:
    if panels <= 0 or panels % 2:
        raise ValueError("Simpson panel count must be positive and even")
    total = function(0.0) + function(1.0)
    for index in range(1, panels):
        total += (4 if index % 2 else 2) * function(index / panels)
    return total / (3.0 * panels)


def axis_one_form_period(
    matrix: Matrix,
    coefficients: Sequence[int],
    panels: int,
    basepoint_shift: float = 0.0,
    reverse_orientation: bool = False,
) -> float:
    geometry = axis_geometry(matrix)
    if reverse_orientation:
        start_u = -geometry.length / 2.0 + basepoint_shift
        end_u = geometry.length / 2.0 + basepoint_shift
    else:
        start_u = geometry.length / 2.0 + basepoint_shift
        end_u = -geometry.length / 2.0 + basepoint_shift
    delta_u = end_u - start_u

    def integrand(parameter: float) -> complex:
        u = start_u + delta_u * parameter
        z = geometry.point(u)
        dz = geometry.derivative(u) * delta_u
        form_value = 2.0j * math.pi * evaluate_q_series(coefficients, z)
        return form_value * dz

    return composite_simpson(integrand, panels).real


def reduce_to_psl2z_fundamental_domain(z: complex) -> complex:
    """Deterministic reduction used only to stably evaluate a j-based control."""

    reduced = z
    for _ in range(64):
        translation = math.floor(reduced.real + 0.5)
        reduced -= translation
        if abs(reduced) < 1.0 - 1.0e-14:
            reduced = -1.0 / reduced
            continue
        if reduced.real < -0.5 - 1.0e-14 or reduced.real > 0.5 + 1.0e-14:
            continue
        return reduced
    raise RuntimeError("PSL2Z fundamental-domain reduction did not converge")


def divisor_sigma3(limit: int) -> list[int]:
    values = [0] * (limit + 1)
    for divisor in range(1, limit + 1):
        cube = divisor**3
        for multiple in range(divisor, limit + 1, divisor):
            values[multiple] += cube
    return values


SIGMA3 = divisor_sigma3(GENERIC_J_Q_CUTOFF)


def bounded_j_observable(z: complex) -> float:
    """A bounded PSL2Z-invariant cusp-decaying generic observable proxy.

    With J=j/1728, Re(J)/(1+|J|^2) is bounded by 1/2 and tends to zero
    at the cusp.  Evaluation happens after deterministic PSL2Z reduction.
    """

    reduced = reduce_to_psl2z_fundamental_domain(z)
    q = complex(math.e) ** (2.0j * math.pi * reduced)
    e4 = 1.0 + 0.0j
    q_power = 1.0 + 0.0j
    for exponent in range(1, GENERIC_J_Q_CUTOFF + 1):
        q_power *= q
        e4 += 240.0 * SIGMA3[exponent] * q_power
    delta = q
    q_power = 1.0 + 0.0j
    for exponent in range(1, GENERIC_J_Q_CUTOFF + 1):
        q_power *= q
        delta *= (1.0 - q_power) ** 24
    normalized_j = (e4**3 / delta) / 1728.0
    magnitude = abs(normalized_j)
    if magnitude > 1.0e100:
        inverse = 1.0 / normalized_j
        return inverse.real / (1.0 + abs(inverse) ** 2)
    return normalized_j.real / (1.0 + magnitude * magnitude)


def axis_generic_period(matrix: Matrix, panels: int) -> float:
    geometry = axis_geometry(matrix)
    start_u = geometry.length / 2.0
    end_u = -geometry.length / 2.0
    delta_u = end_u - start_u

    def integrand(parameter: float) -> float:
        u = start_u + delta_u * parameter
        # |du| is hyperbolic arclength along the invariant axis.
        return bounded_j_observable(geometry.point(u)) * abs(delta_u)

    return composite_simpson(integrand, panels).real


def pearson(left: Sequence[float], right: Sequence[float]) -> float | None:
    if len(left) != len(right) or len(left) < 2:
        return None
    left_mean = sum(left) / len(left)
    right_mean = sum(right) / len(right)
    numerator = sum(
        (x - left_mean) * (y - right_mean) for x, y in zip(left, right)
    )
    left_norm = math.sqrt(sum((x - left_mean) ** 2 for x in left))
    right_norm = math.sqrt(sum((y - right_mean) ** 2 for y in right))
    if left_norm == 0.0 or right_norm == 0.0:
        return None
    return numerator / (left_norm * right_norm)


def format_float(value: float | None) -> str:
    if value is None:
        return "not_applicable"
    return f"{value:.17e}"


def write_csv(path: Path, fieldnames: Sequence[str], rows: Iterable[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_outputs(
    output_directory: Path,
    max_word_length: int = DEFAULT_MAX_WORD_LENGTH,
    q_cutoff: int = DEFAULT_Q_CUTOFF,
    q_comparison_cutoff: int = DEFAULT_Q_COMPARISON_CUTOFF,
    quadrature_panels: int = DEFAULT_QUADRATURE_PANELS,
    repeat_q_cutoff: int = DEFAULT_REPEAT_Q_CUTOFF,
    repeat_q_comparison_cutoff: int = DEFAULT_REPEAT_Q_COMPARISON_CUTOFF,
    repeat_quadrature_panels: int = DEFAULT_REPEAT_QUADRATURE_PANELS,
    basepoint_shift: float = DEFAULT_BASEPOINT_SHIFT,
    permutation_shift: int = DEFAULT_PERMUTATION_SHIFT,
) -> dict[str, object]:
    output_directory.mkdir(parents=True, exist_ok=True)
    q_coefficients = level11_eta_product_coefficients(q_cutoff)
    if q_comparison_cutoff >= q_cutoff:
        raise ValueError("q_comparison_cutoff must be smaller than q_cutoff")
    low_q_coefficients = level11_eta_product_coefficients(q_comparison_cutoff)
    repeat_q_coefficients = level11_eta_product_coefficients(repeat_q_cutoff)
    if repeat_q_comparison_cutoff >= repeat_q_cutoff:
        raise ValueError(
            "repeat_q_comparison_cutoff must be smaller than repeat_q_cutoff"
        )
    repeat_low_q_coefficients = level11_eta_product_coefficients(
        repeat_q_comparison_cutoff
    )
    parent_words = primitive_positive_necklaces(max_word_length)
    gamma_words = [
        word for word in parent_words if matrix_from_word(word)[2] % 11 == 0
    ]

    raw_rows: list[dict[str, object]] = []
    periods: list[float] = []
    generic_raw_periods: list[float] = []
    for row_index, word in enumerate(gamma_words, start=1):
        matrix = matrix_from_word(word)
        a, b, c, d = matrix
        geometry = axis_geometry(matrix)
        basepoint = geometry.point(geometry.length / 2.0)
        endpoint = geometry.point(-geometry.length / 2.0)
        mapped_basepoint = mobius(matrix, basepoint)

        period = axis_one_form_period(matrix, q_coefficients, quadrature_panels)
        period_low_q = axis_one_form_period(
            matrix, low_q_coefficients, quadrature_panels
        )
        period_low_panels = axis_one_form_period(
            matrix, q_coefficients, quadrature_panels // 2
        )
        period_shifted = axis_one_form_period(
            matrix,
            q_coefficients,
            quadrature_panels,
            basepoint_shift=basepoint_shift,
        )
        period_reverse = axis_one_form_period(
            matrix,
            q_coefficients,
            quadrature_panels,
            reverse_orientation=True,
        )
        repeat_matrix = matrix_power(matrix, 2)
        repeat_length = geodesic_length(repeat_matrix)
        # The repeated orbit is integrated directly on the symmetric axis
        # segment of M^2.  Its lower endpoint height is much smaller than for
        # M, so this independently frozen check uses a deeper q cutoff.
        repeat_period_proxy = axis_one_form_period(
            repeat_matrix,
            repeat_q_coefficients,
            repeat_quadrature_panels,
        )
        repeat_period_low_q = axis_one_form_period(
            repeat_matrix,
            repeat_low_q_coefficients,
            repeat_quadrature_panels,
        )
        repeat_period_low_panels = axis_one_form_period(
            repeat_matrix,
            repeat_q_coefficients,
            repeat_quadrature_panels // 2,
        )
        generic_raw_period = axis_generic_period(matrix, quadrature_panels)

        periods.append(period)
        generic_raw_periods.append(generic_raw_period)
        raw_rows.append(
            {
                "row_id": f"P26-LR-{row_index:03d}",
                "word": word,
                "word_length": len(word),
                "necklace_canonical": canonical_rotation(word) == word,
                "primitive_root": primitive_root(word)[0],
                "primitive_exponent": primitive_root(word)[1],
                "orientation": "positive_LR_word_axis_M_forward",
                "matrix_a": a,
                "matrix_b": b,
                "matrix_c": c,
                "matrix_d": d,
                "matrix_determinant": determinant(matrix),
                "matrix_trace": trace(matrix),
                "gamma0_11_c_mod_11": c % 11,
                "hyperbolic": trace(matrix) > 2,
                "base_length": geometry.length,
                "axis_center": geometry.center,
                "axis_radius": geometry.radius,
                "basepoint_real": basepoint.real,
                "basepoint_imag": basepoint.imag,
                "endpoint_real": endpoint.real,
                "endpoint_imag": endpoint.imag,
                "basepoint_map_residual": abs(mapped_basepoint - endpoint),
                "newform_axis_period_proxy": period,
                # With rho_epsilon=1+epsilon*a, the frozen exact law is
                # T_epsilon=ell+epsilon*integral_gamma(alpha_f).  The
                # numerical period proxy is therefore also the first-
                # variation coefficient at epsilon=0.  Keep both fields so
                # that this contract is explicit in every ledger row.
                "first_variation_coefficient_dT_depsilon_at_0": period,
                "first_variation_sign": (
                    "POSITIVE" if period > 0.0 else "NEGATIVE" if period < 0.0 else "ZERO"
                ),
                "q_cutoff_residual": abs(period - period_low_q),
                "quadrature_residual": abs(period - period_low_panels),
                "basepoint_shift": basepoint_shift,
                "basepoint_residual": abs(period - period_shifted),
                "reverse_orientation_period": period_reverse,
                "orientation_residual": abs(period + period_reverse),
                "repeat2_word": word * 2,
                "repeat2_matrix_a": repeat_matrix[0],
                "repeat2_matrix_b": repeat_matrix[1],
                "repeat2_matrix_c": repeat_matrix[2],
                "repeat2_matrix_d": repeat_matrix[3],
                "repeat2_trace": trace(repeat_matrix),
                "repeat2_length": repeat_length,
                "length_repetition_residual": abs(
                    repeat_length - 2.0 * geometry.length
                ),
                "repeat2_period_proxy": repeat_period_proxy,
                "repeat_q_cutoff_residual": abs(
                    repeat_period_proxy - repeat_period_low_q
                ),
                "repeat_quadrature_residual": abs(
                    repeat_period_proxy - repeat_period_low_panels
                ),
                "period_repetition_residual": abs(repeat_period_proxy - 2.0 * period),
                "generic_j_raw_period": generic_raw_period,
            }
        )

    period_rms = math.sqrt(sum(value * value for value in periods) / len(periods))
    generic_rms = math.sqrt(
        sum(value * value for value in generic_raw_periods) / len(generic_raw_periods)
    )
    generic_scale = period_rms / generic_rms if generic_rms else 0.0
    generic_matched_periods = [value * generic_scale for value in generic_raw_periods]
    effective_shift = permutation_shift % len(periods)
    permuted_periods = periods[effective_shift:] + periods[:effective_shift]

    ledger_rows: list[dict[str, object]] = []
    for row, generic_matched, permuted in zip(
        raw_rows, generic_matched_periods, permuted_periods
    ):
        ledger_rows.append(
            {
                **row,
                "generic_j_norm_scale": generic_scale,
                "generic_j_matched_period": generic_matched,
                "permutation_id": f"cyclic_shift_{effective_shift}_sorted_ledger",
                "permuted_newform_period": permuted,
                "matrix_owner": "left_to_right_positive_LR_word_product_in_PSL2Z",
                "ledger_scope": "finite_primitive_positive_LR_necklaces_not_complete_Gamma0_11_conjugacy_classes",
                "exact_ledger_evidence_status": "NUMERICALLY_CERTIFIED",
                "period_proxy_evidence_status": "NUMERICAL_OBSERVATION",
                "control_evidence_status": "NUMERICAL_OBSERVATION",
                "hecke_euler_evidence_status": "HEURISTIC",
                "hecke_euler_testability": "NOT_TESTABLE",
                "prime_table_used": False,
                "riemann_zero_data_used": False,
            }
        )

    ledger_fieldnames = [
        "row_id",
        "word",
        "word_length",
        "necklace_canonical",
        "primitive_root",
        "primitive_exponent",
        "orientation",
        "matrix_a",
        "matrix_b",
        "matrix_c",
        "matrix_d",
        "matrix_determinant",
        "matrix_trace",
        "gamma0_11_c_mod_11",
        "hyperbolic",
        "base_length",
        "axis_center",
        "axis_radius",
        "basepoint_real",
        "basepoint_imag",
        "endpoint_real",
        "endpoint_imag",
        "basepoint_map_residual",
        "newform_axis_period_proxy",
        "first_variation_coefficient_dT_depsilon_at_0",
        "first_variation_sign",
        "q_cutoff_residual",
        "quadrature_residual",
        "basepoint_shift",
        "basepoint_residual",
        "reverse_orientation_period",
        "orientation_residual",
        "repeat2_word",
        "repeat2_matrix_a",
        "repeat2_matrix_b",
        "repeat2_matrix_c",
        "repeat2_matrix_d",
        "repeat2_trace",
        "repeat2_length",
        "length_repetition_residual",
        "repeat2_period_proxy",
        "repeat_q_cutoff_residual",
        "repeat_quadrature_residual",
        "period_repetition_residual",
        "generic_j_raw_period",
        "generic_j_norm_scale",
        "generic_j_matched_period",
        "permutation_id",
        "permuted_newform_period",
        "matrix_owner",
        "ledger_scope",
        "exact_ledger_evidence_status",
        "period_proxy_evidence_status",
        "control_evidence_status",
        "hecke_euler_evidence_status",
        "hecke_euler_testability",
        "prime_table_used",
        "riemann_zero_data_used",
    ]
    formatted_ledger_rows: list[dict[str, object]] = []
    for row in ledger_rows:
        formatted: dict[str, object] = {}
        for key in ledger_fieldnames:
            value = row[key]
            formatted[key] = format_float(value) if isinstance(value, float) else value
        formatted_ledger_rows.append(formatted)

    ledger_path = output_directory / "newform_timechange_variation_ledger.csv"
    write_csv(ledger_path, ledger_fieldnames, formatted_ledger_rows)

    parent_rows: list[dict[str, object]] = []
    gamma_set = set(gamma_words)
    for word in parent_words:
        matrix = matrix_from_word(word)
        parent_rows.append(
            {
                "word": word,
                "word_length": len(word),
                "matrix_a": matrix[0],
                "matrix_b": matrix[1],
                "matrix_c": matrix[2],
                "matrix_d": matrix[3],
                "matrix_trace": trace(matrix),
                "base_length": format_float(geodesic_length(matrix)),
                "in_gamma0_11_selected_ledger": word in gamma_set,
                "control_owner": "simpler_parent_positive_LR_necklace_in_PSL2Z",
            }
        )
    parent_path = output_directory / "simpler_parent_length_control.csv"
    write_csv(
        parent_path,
        [
            "word",
            "word_length",
            "matrix_a",
            "matrix_b",
            "matrix_c",
            "matrix_d",
            "matrix_trace",
            "base_length",
            "in_gamma0_11_selected_ledger",
            "control_owner",
        ],
        parent_rows,
    )

    lengths = [float(row["base_length"]) for row in raw_rows]
    summary: dict[str, object] = {
        "schema": "p26-round2-summary/1.0",
        "determinism": "DETERMINISTIC_FIXED_FLOAT_PIPELINE",
        "config": {
            "max_positive_word_length": max_word_length,
            "q_cutoff": q_cutoff,
            "q_cutoff_comparison": q_comparison_cutoff,
            "quadrature_panels": quadrature_panels,
            "quadrature_panels_comparison": quadrature_panels // 2,
            "repeat_q_cutoff": repeat_q_cutoff,
            "repeat_q_cutoff_comparison": repeat_q_comparison_cutoff,
            "repeat_quadrature_panels": repeat_quadrature_panels,
            "repeat_quadrature_panels_comparison": repeat_quadrature_panels // 2,
            "basepoint_axis_shift": basepoint_shift,
            "permutation_shift": effective_shift,
            "generic_j_q_cutoff_after_PSL2Z_reduction": GENERIC_J_Q_CUTOFF,
        },
        "counts": {
            "primitive_positive_parent_necklaces": len(parent_words),
            "gamma0_11_selected_positive_necklaces": len(gamma_words),
            "selected_by_word_length": {
                str(length): sum(len(word) == length for word in gamma_words)
                for length in range(1, max_word_length + 1)
            },
        },
        "quality_residual_maxima": {
            "basepoint_map": max(float(row["basepoint_map_residual"]) for row in raw_rows),
            "q_cutoff": max(float(row["q_cutoff_residual"]) for row in raw_rows),
            "quadrature": max(float(row["quadrature_residual"]) for row in raw_rows),
            "basepoint_shift": max(float(row["basepoint_residual"]) for row in raw_rows),
            "orientation": max(float(row["orientation_residual"]) for row in raw_rows),
            "length_repetition": max(
                float(row["length_repetition_residual"]) for row in raw_rows
            ),
            "period_repetition": max(
                float(row["period_repetition_residual"]) for row in raw_rows
            ),
            "repeat_q_cutoff": max(
                float(row["repeat_q_cutoff_residual"]) for row in raw_rows
            ),
            "repeat_quadrature": max(
                float(row["repeat_quadrature_residual"]) for row in raw_rows
            ),
        },
        "finite_ledger_controls": {
            "newform_period_rms": period_rms,
            "generic_j_raw_period_rms": generic_rms,
            "generic_j_norm_scale": generic_scale,
            "generic_j_matched_period_rms": math.sqrt(
                sum(value * value for value in generic_matched_periods)
                / len(generic_matched_periods)
            ),
            "newform_period_vs_length_pearson": pearson(periods, lengths),
            "generic_j_period_vs_length_pearson": pearson(
                generic_matched_periods, lengths
            ),
            "permuted_period_vs_length_pearson": pearson(permuted_periods, lengths),
        },
        "claim_boundary": {
            "finite_positive_word_ledger_complete_gamma0_11_conjugacy_certificate": False,
            "hecke_euler_evidence_status": "HEURISTIC",
            "hecke_euler_testability": "NOT_TESTABLE",
            "formal_route_a_tuple": "UNASSIGNED",
            "route_b_evaluation": "NOT_RUN",
            "route_b_invocation_allowed": False,
            "prime_table_used": False,
            "riemann_zero_data_used": False,
            "repetition_proxy_method": "direct_symmetric_M_squared_axis_integration_with_deeper_q_cutoff",
        },
    }
    summary_path = output_directory / "round2_summary.json"
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    project_directory = Path(__file__).resolve().parents[1]
    source_paths = [
        project_directory / "code" / "round2_experiment.py",
        project_directory / "code" / "test_round2_experiment.py",
        project_directory / "experiments" / "reproduce.sh",
    ]
    manifest = {
        "schema": "p26-round2-artifact-manifest/1.0",
        "source_bindings": [
            {
                "path": path.relative_to(project_directory).as_posix(),
                "sha256": sha256_file(path),
                "bytes": path.stat().st_size,
            }
            for path in source_paths
        ],
        "artifacts": [
            {
                "path": path.name,
                "sha256": sha256_file(path),
                "bytes": path.stat().st_size,
            }
            for path in [ledger_path, parent_path, summary_path]
        ],
        "claim_boundary": summary["claim_boundary"],
    }
    manifest_path = output_directory / "artifact_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return summary


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--max-word-length", type=int, default=DEFAULT_MAX_WORD_LENGTH)
    parser.add_argument("--q-cutoff", type=int, default=DEFAULT_Q_CUTOFF)
    parser.add_argument(
        "--q-comparison-cutoff",
        type=int,
        default=DEFAULT_Q_COMPARISON_CUTOFF,
    )
    parser.add_argument(
        "--quadrature-panels", type=int, default=DEFAULT_QUADRATURE_PANELS
    )
    parser.add_argument(
        "--repeat-q-cutoff", type=int, default=DEFAULT_REPEAT_Q_CUTOFF
    )
    parser.add_argument(
        "--repeat-q-comparison-cutoff",
        type=int,
        default=DEFAULT_REPEAT_Q_COMPARISON_CUTOFF,
    )
    parser.add_argument(
        "--repeat-quadrature-panels",
        type=int,
        default=DEFAULT_REPEAT_QUADRATURE_PANELS,
    )
    parser.add_argument(
        "--basepoint-shift", type=float, default=DEFAULT_BASEPOINT_SHIFT
    )
    parser.add_argument(
        "--permutation-shift", type=int, default=DEFAULT_PERMUTATION_SHIFT
    )
    return parser.parse_args()


def main() -> int:
    arguments = parse_args()
    summary = build_outputs(
        output_directory=arguments.output,
        max_word_length=arguments.max_word_length,
        q_cutoff=arguments.q_cutoff,
        q_comparison_cutoff=arguments.q_comparison_cutoff,
        quadrature_panels=arguments.quadrature_panels,
        repeat_q_cutoff=arguments.repeat_q_cutoff,
        repeat_q_comparison_cutoff=arguments.repeat_q_comparison_cutoff,
        repeat_quadrature_panels=arguments.repeat_quadrature_panels,
        basepoint_shift=arguments.basepoint_shift,
        permutation_shift=arguments.permutation_shift,
    )
    print(json.dumps(summary, indent=2, sort_keys=True, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
