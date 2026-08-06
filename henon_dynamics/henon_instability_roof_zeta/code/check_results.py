#!/usr/bin/env python3
"""Independent, read-only audit of the instability-roof experiment.

The checker intentionally does not import :mod:`henon_roof` or any producer
script.  It reconstructs the symbolic counts, orbit invariants, exact clock
algebra, determinant coefficients, root matching, and frozen gate decisions
from the persisted protocol and raw JSON ledgers.  Its only write is the
checker report requested with ``--output``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable, Sequence

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.optimize import linear_sum_assignment


PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPOSITORY_ROOT = PROJECT_ROOT.parent
RESULTS_ROOT = PROJECT_ROOT / "results"
DEFAULT_PROTOCOL = PROJECT_ROOT / "refine-logs" / "R000_FROZEN_PROTOCOL.json"
DEFAULT_CATALOG = RESULTS_ROOT / "catalog_robustness.json"
DEFAULT_ROOTS = RESULTS_ROOT / "roots_robustness.json"
DEFAULT_CONTROLS = RESULTS_ROOT / "controls.json"
DEFAULT_ANALYSIS = RESULTS_ROOT / "analysis_summary.json"
DEFAULT_OUTPUT = RESULTS_ROOT / "independent_check.json"
DEFAULT_DEPENDENCY_LOCK = (
    PROJECT_ROOT / "refine-logs" / "INHERITED_DEPENDENCIES.json"
)

# This digest was frozen before the validation, sealed-test, and robustness
# artifacts were produced.  Merely comparing mutually supplied hashes would
# not protect against a protocol and all children changing together.
EXPECTED_PROTOCOL_SHA256 = "0c284a1b3610a3d772aa00c6a8b33161a8bc6814957a9968d5c80fb618eec399"

STATE_NAMES = ("--", "-+", "+-", "++")
STATE_INDEX = {name: index for index, name in enumerate(STATE_NAMES)}
ADJACENCY = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)
STAGED_ARTIFACTS = (
    ("development", 8, (7, 8)),
    ("validation", 12, (7, 8, 10, 12)),
    ("sealed_test", 16, (7, 8, 10, 12, 14, 16)),
    ("robustness", 20, (7, 8, 10, 12, 14, 16, 18, 20)),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--protocol", type=Path, default=DEFAULT_PROTOCOL)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--roots", type=Path, default=DEFAULT_ROOTS)
    parser.add_argument("--controls", type=Path, default=DEFAULT_CONTROLS)
    parser.add_argument("--analysis", type=Path, default=DEFAULT_ANALYSIS)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def json_default(value: Any) -> Any:
    """Convert scalar objects produced by independent numerical libraries."""
    if isinstance(value, np.bool_):
        return bool(value)
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    if isinstance(value, mp.mpf):
        return mp.nstr(value, 80)
    if isinstance(value, mp.mpc):
        return {"real": mp.nstr(value.real, 80), "imag": mp.nstr(value.imag, 80)}
    if isinstance(value, sp.Basic):
        return str(value)
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable")


def portable(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(REPOSITORY_ROOT))
    except ValueError:
        return str(resolved)


def resolve_recorded_path(text: str, referring_path: Path) -> Path:
    candidate = Path(text)
    if candidate.is_absolute() and candidate.exists():
        return candidate.resolve()
    possibilities = (
        REPOSITORY_ROOT / candidate,
        PROJECT_ROOT / candidate,
        referring_path.parent / candidate,
    )
    for possibility in possibilities:
        if possibility.exists():
            return possibility.resolve()
    raise FileNotFoundError(f"could not resolve recorded artifact path {text!r}")


def matrix_multiply(
    left: tuple[tuple[int, ...], ...], right: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, ...], ...]:
    size = len(left)
    return tuple(
        tuple(
            sum(left[row][index] * right[index][column] for index in range(size))
            for column in range(size)
        )
        for row in range(size)
    )


def matrix_power(
    matrix: tuple[tuple[int, ...], ...], exponent: int
) -> tuple[tuple[int, ...], ...]:
    size = len(matrix)
    result = tuple(
        tuple(int(row == column) for column in range(size)) for row in range(size)
    )
    factor = matrix
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = matrix_multiply(result, factor)
        factor = matrix_multiply(factor, factor)
        remaining >>= 1
    return result


def mobius(number: int) -> int:
    remaining = number
    prime_factors = 0
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor:
            divisor += 1
            continue
        remaining //= divisor
        prime_factors += 1
        if remaining % divisor == 0:
            return 0
        while remaining % divisor == 0:
            remaining //= divisor
        divisor += 1
    if remaining > 1:
        prime_factors += 1
    return -1 if prime_factors % 2 else 1


def divisors(number: int) -> list[int]:
    return [value for value in range(1, number + 1) if number % value == 0]


def exact_symbolic_counts(max_period: int) -> tuple[dict[int, int], dict[int, int]]:
    fixed: dict[int, int] = {}
    primitive: dict[int, int] = {}
    for period in range(1, max_period + 1):
        power = matrix_power(ADJACENCY, period)
        fixed[period] = sum(power[index][index] for index in range(4))
        numerator = sum(
            mobius(divisor) * fixed[period // divisor]
            for divisor in divisors(period)
        )
        if numerator % period:
            raise ArithmeticError(f"nonintegral primitive count at period {period}")
        primitive[period] = numerator // period
    return fixed, primitive


def rotations(word: tuple[int, ...]) -> list[tuple[int, ...]]:
    return [word[index:] + word[:index] for index in range(len(word))]


def is_primitive_word(word: tuple[int, ...]) -> bool:
    period = len(word)
    return all(
        word != word[:divisor] * (period // divisor)
        for divisor in range(1, period)
        if period % divisor == 0
    )


def parse_state_word(text: str) -> tuple[int, ...]:
    try:
        return tuple(STATE_INDEX[state] for state in text.split("|"))
    except KeyError as exc:
        raise ValueError(f"unknown state in {text!r}") from exc


def close_mp(left: mp.mpf, right: mp.mpf, tolerance: mp.mpf) -> bool:
    return bool(abs(left - right) <= tolerance * max(mp.mpf(1), abs(left), abs(right)))


def multiply_2x2(
    left: tuple[tuple[mp.mpf, mp.mpf], tuple[mp.mpf, mp.mpf]],
    right: tuple[tuple[mp.mpf, mp.mpf], tuple[mp.mpf, mp.mpf]],
) -> tuple[tuple[mp.mpf, mp.mpf], tuple[mp.mpf, mp.mpf]]:
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


def audit_orbit_catalog(catalog: dict[str, Any]) -> tuple[dict[str, bool], dict[str, Any]]:
    max_period = int(catalog["max_period"])
    fixed_counts, primitive_counts = exact_symbolic_counts(max_period)
    rows = catalog["orbits"]
    count_by_period = Counter(int(row["period"]) for row in rows)
    words: set[str] = set()

    word_integrity = True
    recurrence_gate = True
    determinant_gate = True
    serialized_determinant_roundoff_gate = True
    contraction_gate = True
    hyperbolicity_gate = True
    invariant_consistency = True
    maximum_recurrence = mp.mpf(0)
    maximum_determinant_error = mp.mpf(0)
    maximum_stored_determinant_discrepancy = mp.mpf(0)
    maximum_serialized_determinant_error = mp.mpf(0)
    stored_determinants_over_science_threshold = 0
    maximum_contraction_bound = mp.mpf(0)
    minimum_hyperbolicity_margin = mp.inf
    maximum_iterations = 0
    orientation_counts: Counter[int] = Counter()

    with mp.workdps(max(100, int(catalog["precision_dps"]) + 20)):
        invariant_tolerance = mp.mpf("1e-55")
        # The producer formed det(M) by subtracting products as large as about
        # 1e32 at 80 dps.  Its serialized determinant therefore has fewer
        # reliable digits than the coordinates and trace.  This tolerance is
        # solely for record-to-reconstruction agreement; the independently
        # recomputed determinant-one science gate below remains 1e-50.
        stored_determinant_tolerance = mp.mpf("1e-48")
        gate_tolerance = mp.mpf("1e-50")
        for row in rows:
            period = int(row["period"])
            word = parse_state_word(str(row["canonical_word"]))
            expected_signs = tuple(
                1 if STATE_NAMES[state][0] == "+" else -1 for state in word
            )
            observed_signs = tuple(1 if value == "+" else -1 for value in row["sign_word"])
            admissible = all(
                ADJACENCY[word[index]][word[(index + 1) % period]]
                for index in range(period)
            )
            canonical = word == min(rotations(word))
            unique = str(row["canonical_word"]) not in words
            words.add(str(row["canonical_word"]))
            word_integrity &= bool(
                len(word) == period
                and len(observed_signs) == period
                and observed_signs == expected_signs
                and admissible
                and canonical
                and is_primitive_word(word)
                and unique
            )

            parameter = mp.mpf(row["parameter"])
            coordinates = [mp.mpf(value) for value in row["coordinates"]]
            coordinate_signs = tuple(1 if value > 0 else -1 for value in coordinates)
            word_integrity &= coordinate_signs == expected_signs

            recurrence = max(
                abs(
                    coordinates[(index + 1) % period]
                    - (1 - parameter * coordinates[index] ** 2 - coordinates[(index - 1) % period])
                )
                for index in range(period)
            )
            maximum_recurrence = max(maximum_recurrence, recurrence)
            recurrence_gate &= recurrence < gate_tolerance
            invariant_consistency &= close_mp(
                recurrence, mp.mpf(row["recurrence_residual"]), invariant_tolerance
            )

            monodromy = ((mp.mpf(1), mp.mpf(0)), (mp.mpf(0), mp.mpf(1)))
            for coordinate in coordinates:
                jacobian = ((-2 * parameter * coordinate, mp.mpf(-1)), (mp.mpf(1), mp.mpf(0)))
                monodromy = multiply_2x2(jacobian, monodromy)
            trace = monodromy[0][0] + monodromy[1][1]
            determinant = monodromy[0][0] * monodromy[1][1] - monodromy[0][1] * monodromy[1][0]
            determinant_error = abs(determinant - 1)
            stored_determinant = mp.mpf(row["monodromy_determinant"])
            serialized_determinant_error = abs(stored_determinant - 1)
            stored_determinant_discrepancy = abs(determinant - stored_determinant)
            maximum_serialized_determinant_error = max(
                maximum_serialized_determinant_error,
                serialized_determinant_error,
            )
            maximum_stored_determinant_discrepancy = max(
                maximum_stored_determinant_discrepancy,
                stored_determinant_discrepancy,
            )
            stored_determinants_over_science_threshold += int(
                serialized_determinant_error >= gate_tolerance
            )
            serialized_determinant_roundoff_gate &= (
                serialized_determinant_error < mp.mpf("1e-45")
            )
            margin = abs(trace) - 2
            maximum_determinant_error = max(maximum_determinant_error, determinant_error)
            minimum_hyperbolicity_margin = min(minimum_hyperbolicity_margin, margin)
            determinant_gate &= determinant_error < gate_tolerance
            hyperbolicity_gate &= margin > 0
            invariant_consistency &= close_mp(
                trace, mp.mpf(row["monodromy_trace"]), invariant_tolerance
            ) and close_mp(
                determinant,
                stored_determinant,
                stored_determinant_tolerance,
            )

            discriminant = trace**2 - 4 * determinant
            if discriminant <= 0:
                hyperbolicity_gate = False
                continue
            eigenvalues = (
                (trace + mp.sqrt(discriminant)) / 2,
                (trace - mp.sqrt(discriminant)) / 2,
            )
            unstable = max(eigenvalues, key=abs)
            unstable_modulus = abs(unstable)
            orientation = 1 if unstable > 0 else -1
            length = mp.log(unstable_modulus)
            action = mp.fsum(
                coordinates[index] * coordinates[(index + 1) % period]
                - coordinates[index]
                + parameter * coordinates[index] ** 3 / 3
                for index in range(period)
            )
            invariant_consistency &= bool(
                orientation == int(row["orientation"])
                and close_mp(unstable, mp.mpf(row["unstable_multiplier"]), invariant_tolerance)
                and close_mp(unstable_modulus, mp.mpf(row["unstable_modulus"]), invariant_tolerance)
                and close_mp(length, mp.mpf(row["instability_length"]), invariant_tolerance)
                and close_mp(action, mp.mpf(row["action"]), invariant_tolerance)
            )
            orientation_counts[orientation] += 1

            contraction_delta = mp.mpf(row["contraction_delta"])
            contraction_factor = (2 / mp.sqrt(17)) * mp.sqrt(6 / parameter)
            if not 0 < contraction_factor < 1:
                contraction_gate = False
                contraction_bound = mp.inf
            else:
                contraction_bound = contraction_delta / (1 - contraction_factor)
            maximum_contraction_bound = max(maximum_contraction_bound, contraction_bound)
            contraction_gate &= contraction_bound < gate_tolerance
            invariant_consistency &= close_mp(
                contraction_bound,
                mp.mpf(row["contraction_error_bound"]),
                invariant_tolerance,
            )
            maximum_iterations = max(maximum_iterations, int(row["contraction_iterations"]))

    count_gate = bool(
        all(count_by_period.get(period, 0) == primitive_counts[period] for period in primitive_counts)
        and len(rows) == sum(primitive_counts.values())
        and {int(key): int(value) for key, value in catalog["primitive_counts"].items()}
        == primitive_counts
        and {int(key): int(value) for key, value in catalog["symbolic_fixed_point_counts"].items()}
        == fixed_counts
    )
    orientation_gate = {
        int(key): int(value) for key, value in catalog["orientation_counts"].items()
    } == dict(orientation_counts)
    recomputed_gates = {
        "symbolic_count_match": count_gate,
        "all_recurrence_residuals_below_1e_minus_50": recurrence_gate,
        "all_determinant_errors_below_1e_minus_50": determinant_gate,
        "all_contraction_bounds_below_1e_minus_50": contraction_gate,
        "all_cycles_hyperbolic": hyperbolicity_gate,
    }
    persisted_gate_match = recomputed_gates == {
        key: bool(value) for key, value in catalog["gates"].items()
    }
    metric_tolerance = mp.mpf("1e-12")
    metrics = catalog["metrics"]
    serialized_metric_match = bool(
        "maximum_serialized_monodromy_determinant_error" not in metrics
        or close_mp(
            maximum_serialized_determinant_error,
            mp.mpf(metrics["maximum_serialized_monodromy_determinant_error"]),
            mp.mpf("1e-60"),
        )
    )
    metric_match = bool(
        close_mp(maximum_recurrence, mp.mpf(metrics["maximum_recurrence_residual"]), metric_tolerance)
        and close_mp(maximum_determinant_error, mp.mpf(metrics["maximum_determinant_error"]), metric_tolerance)
        and close_mp(maximum_contraction_bound, mp.mpf(metrics["maximum_contraction_error_bound"]), metric_tolerance)
        and close_mp(minimum_hyperbolicity_margin, mp.mpf(metrics["minimum_hyperbolicity_margin"]), metric_tolerance)
        and maximum_iterations == int(metrics["maximum_contraction_iterations"])
        and serialized_metric_match
    )
    checks = {
        "exact_primitive_counts": count_gate,
        "symbolic_word_integrity": word_integrity,
        "recurrence_gate": recurrence_gate,
        "determinant_one_gate": determinant_gate,
        "serialized_determinant_roundoff_below_1e_minus_45": (
            serialized_determinant_roundoff_gate
        ),
        "contraction_gate": contraction_gate,
        "hyperbolicity_gate": hyperbolicity_gate,
        "orbit_invariant_consistency": invariant_consistency,
        "orientation_count_match": orientation_gate,
        "persisted_orbit_gate_match": persisted_gate_match,
        "persisted_orbit_metric_match": metric_match,
    }
    details = {
        "max_period": max_period,
        "total_primitive_orbits": len(rows),
        "primitive_counts": {str(key): value for key, value in primitive_counts.items()},
        "fixed_point_counts": {str(key): value for key, value in fixed_counts.items()},
        "orientation_counts": {str(key): value for key, value in sorted(orientation_counts.items())},
        "maximum_recomputed_recurrence_residual": mp.nstr(maximum_recurrence, 20),
        "maximum_recomputed_determinant_error": mp.nstr(maximum_determinant_error, 20),
        "maximum_stored_determinant_discrepancy": mp.nstr(
            maximum_stored_determinant_discrepancy, 20
        ),
        "maximum_serialized_determinant_error": mp.nstr(
            maximum_serialized_determinant_error, 20
        ),
        "stored_determinant_roundoff_tolerance": "1e-48",
        "stored_determinants_over_1e_minus_50": stored_determinants_over_science_threshold,
        "maximum_recomputed_contraction_bound": mp.nstr(maximum_contraction_bound, 20),
        "minimum_recomputed_hyperbolicity_margin": mp.nstr(minimum_hyperbolicity_margin, 20),
        "maximum_contraction_iterations": maximum_iterations,
        "recomputed_gates": recomputed_gates,
    }
    return checks, details


def audit_exact_clock(catalog: dict[str, Any]) -> tuple[bool, dict[str, Any]]:
    x = sp.symbols("X")
    u = sp.symbols("u")
    sqrt7 = sp.sqrt(7)
    fixed_trace = 2 + 2 * sqrt7
    fixed_multiplier = sp.simplify((fixed_trace + sp.sqrt(fixed_trace**2 - 4)) / 2)
    fixed_polynomial = sp.Poly(sp.minimal_polynomial(fixed_multiplier, x), x)
    period4_multiplier = 289 + 24 * sp.sqrt(145)
    period4_polynomial = sp.Poly(sp.minimal_polynomial(period4_multiplier, x), x)
    q = 1 / sp.sqrt(6)
    period4_coordinates = (-q, -q, q, q)
    period4_action = sp.simplify(
        sum(
            period4_coordinates[index] * period4_coordinates[(index + 1) % 4]
            - period4_coordinates[index]
            + 2 * period4_coordinates[index] ** 3
            for index in range(4)
        )
    )
    expansion_lower_bound = sp.Rational(4) - sp.Rational(123, 224)
    expected_fixed = x**4 - 4 * x**3 - 22 * x**2 - 4 * x + 1
    expected_period4 = x**2 - 578 * x + 1
    fixed_root_moduli = sorted(
        abs(complex(value)) for value in sp.nroots(expected_fixed, n=50)
    )
    distinct_conjugate_moduli = all(
        abs(left - right) > 1e-12
        for left, right in zip(fixed_root_moduli[:-1], fixed_root_moduli[1:], strict=True)
    )
    twisted_factorization = sp.expand((1 - u**2) * (1 - u + u**2))

    zero_action_rows = [
        row
        for row in catalog["orbits"]
        if row["canonical_word"] == "--|+-|++|-+"
    ]
    with mp.workdps(100):
        catalog_zero_action = bool(
            len(zero_action_rows) == 1
            and int(zero_action_rows[0]["period"]) == 4
            and mp.mpf(zero_action_rows[0]["action"]) == 0
            and close_mp(
                mp.mpf(zero_action_rows[0]["unstable_modulus"]),
                mp.mpf(str(sp.N(period4_multiplier, 90))),
                mp.mpf("1e-70"),
            )
        )
    persisted = catalog["exact_clock_audit"]
    exact_pass = bool(
        fixed_polynomial.as_expr() == expected_fixed
        and period4_polynomial.as_expr() == expected_period4
        and period4_action == 0
        and expansion_lower_bound == sp.Rational(773, 224)
        and expansion_lower_bound > 1
        and distinct_conjugate_moduli
        and fixed_polynomial.degree() == 4
        and period4_polynomial.degree() == 2
        and twisted_factorization == 1 - u + u**3 - u**4
        and catalog_zero_action
        and persisted["roof_positive"] is True
        and persisted["period4_action_positive_roof"] is False
        and persisted["nonlattice_proof_inputs_pass"] is True
        and persisted["fixed_orbit_multiplier_minimal_polynomial"] == str(expected_fixed)
        and persisted["period4_multiplier_minimal_polynomial"] == str(expected_period4)
        and persisted["unit_clock_determinant"] == "1 - exp(-s) - exp(-3*s) - exp(-4*s)"
        and persisted["unit_clock_periodicity"] == "2*pi*i"
        and persisted["orientation_twisted_factorization"]
        == "(1-exp(-2*s))*(1-exp(-s)+exp(-2*s))"
    )
    return exact_pass, {
        "expansion_lower_bound": str(expansion_lower_bound),
        "fixed_multiplier_minimal_polynomial": str(fixed_polynomial.as_expr()),
        "fixed_multiplier_degree": fixed_polynomial.degree(),
        "fixed_multiplier_conjugate_moduli": fixed_root_moduli,
        "period4_multiplier_minimal_polynomial": str(period4_polynomial.as_expr()),
        "period4_multiplier_degree": period4_polynomial.degree(),
        "period4_action": str(period4_action),
        "catalog_zero_action_orbit_pass": catalog_zero_action,
        "nonlattice_ingredients_pass": bool(
            fixed_polynomial.degree() == 4
            and period4_polynomial.degree() == 2
            and distinct_conjugate_moduli
        ),
    }


def roots_from_pairs(rows: Sequence[Sequence[float]]) -> list[complex]:
    return [complex(float(row[0]), float(row[1])) for row in rows]


def boundary_distance(root: complex, rectangle: dict[str, float]) -> float:
    return min(
        root.real - float(rectangle["real_min"]),
        float(rectangle["real_max"]) - root.real,
        root.imag - float(rectangle["imag_min"]),
        float(rectangle["imag_max"]) - root.imag,
    )


def match_roots(
    source: Sequence[complex], target: Sequence[complex], tolerance: float
) -> dict[str, Any]:
    if not source:
        return {
            "matches": [],
            "missing_source_indices": [],
            "extra_target_indices": list(range(len(target))),
        }
    if not target:
        return {
            "matches": [],
            "missing_source_indices": list(range(len(source))),
            "extra_target_indices": [],
        }
    distances = np.abs(np.asarray(source)[:, None] - np.asarray(target)[None, :])
    source_indices, target_indices = linear_sum_assignment(distances)
    matches: list[dict[str, float | int]] = []
    used_source: set[int] = set()
    used_target: set[int] = set()
    for source_index, target_index in zip(source_indices, target_indices, strict=True):
        distance = float(distances[source_index, target_index])
        if distance <= tolerance:
            used_source.add(int(source_index))
            used_target.add(int(target_index))
            matches.append(
                {
                    "source_index": int(source_index),
                    "target_index": int(target_index),
                    "distance": distance,
                }
            )
    return {
        "matches": matches,
        "missing_source_indices": sorted(set(range(len(source))) - used_source),
        "extra_target_indices": sorted(set(range(len(target))) - used_target),
    }


def drift_summary(match: dict[str, Any], source_count: int) -> dict[str, float | int]:
    distances = np.asarray([row["distance"] for row in match["matches"]], dtype=float)
    return {
        "source_count": int(source_count),
        "matched_count": int(distances.size),
        "retained_fraction": float(distances.size / source_count) if source_count else 1.0,
        "median_drift": float(np.median(distances)) if distances.size else float("inf"),
        "p90_drift": float(np.quantile(distances, 0.9)) if distances.size else float("inf"),
        "maximum_drift": float(np.max(distances)) if distances.size else float("inf"),
        "missing_count": len(match["missing_source_indices"]),
        "extra_count": len(match["extra_target_indices"]),
    }


def summaries_close(left: dict[str, Any], right: dict[str, Any]) -> bool:
    integer_fields = (
        "source_count",
        "matched_count",
        "missing_count",
        "extra_count",
    )
    float_fields = (
        "retained_fraction",
        "median_drift",
        "p90_drift",
        "maximum_drift",
    )
    return bool(
        all(int(left[field]) == int(right[field]) for field in integer_fields)
        and all(
            np.isclose(float(left[field]), float(right[field]), rtol=1e-10, atol=1e-12)
            for field in float_fields
        )
    )


def audit_root_blocks(
    payloads: Sequence[tuple[Path, dict[str, Any]]], protocol: dict[str, Any]
) -> tuple[dict[str, bool], dict[str, Any]]:
    threshold_residual = mp.mpf(protocol["high_precision_root_residual_max"])
    threshold_discrepancy = mp.mpf(
        protocol["high_precision_implementation_discrepancy_max"]
    )
    expected_samples = [int(value) for value in protocol["contour_samples"]]
    rectangle = protocol["root_rectangle"]
    argument_agreement = True
    explicit_count_agreement = True
    precision_gate = True
    raw_summary_consistency = True
    root_geometry = True
    conjugation_consistency = True
    block_count = 0
    root_count = 0
    maximum_product_residual = mp.mpf(0)
    maximum_trace_residual = mp.mpf(0)
    maximum_coefficient_discrepancy = mp.mpf(0)
    maximum_precision_drift = 0.0

    for path, payload in payloads:
        for sector in ("0", "1"):
            for cutoff_text, block in payload["sectors"][sector]["cutoffs"].items():
                block_count += 1
                roots = roots_from_pairs(block["roots"])
                root_count += len(roots)
                contour = block["argument_principle"]
                samples = [int(row["samples"]) for row in contour]
                counts = [int(row["root_count"]) for row in contour]
                computed_argument_agreement = bool(
                    samples == expected_samples and len(set(counts)) == 1
                )
                computed_discrepancy = counts[-1] - len(roots)
                argument_agreement &= computed_argument_agreement
                explicit_count_agreement &= computed_discrepancy == 0
                raw_summary_consistency &= bool(
                    bool(block["argument_counts_agree"]) == computed_argument_agreement
                    and int(block["root_count_discovered"]) == len(roots)
                    and int(block["root_count_discrepancy"]) == computed_discrepancy
                    and int(block["cutoff"]) == int(cutoff_text)
                    and int(block["kappa"]) == int(sector)
                )
                root_geometry &= all(
                    float(rectangle["real_min"]) - 2e-8 <= root.real <= float(rectangle["real_max"]) + 2e-8
                    and float(rectangle["imag_min"]) - 2e-8 <= root.imag <= float(rectangle["imag_max"]) + 2e-8
                    for root in roots
                ) and all(
                    abs(first - second) > 1e-7
                    for index, first in enumerate(roots)
                    for second in roots[index + 1 :]
                )

                computed_conjugation = max(
                    (min(abs(root.conjugate() - other) for other in roots) for root in roots),
                    default=0.0,
                )
                conjugation_consistency &= bool(
                    np.isclose(
                        computed_conjugation,
                        float(block["conjugation_residual"]),
                        rtol=1e-7,
                        atol=1e-12,
                    )
                    and computed_conjugation < 1e-6
                )

                high_precision = block["high_precision_roots"]
                if len(high_precision) != len(roots):
                    precision_gate = False
                    continue
                local_product: list[mp.mpf] = []
                local_trace: list[mp.mpf] = []
                local_discrepancy: list[mp.mpf] = []
                local_shifts: list[float] = []
                for root, row in zip(roots, high_precision, strict=True):
                    product_residual = mp.mpf(row["product_residual"])
                    trace_residual = mp.mpf(row["trace_residual"])
                    coefficient_discrepancy = mp.mpf(row["coefficient_discrepancy"])
                    refined = complex(float(row["real"]), float(row["imag"]))
                    computed_shift = abs(refined - root)
                    local_product.append(product_residual)
                    local_trace.append(trace_residual)
                    local_discrepancy.append(coefficient_discrepancy)
                    local_shifts.append(computed_shift)
                    precision_gate &= bool(
                        product_residual < threshold_residual
                        and trace_residual < threshold_residual
                        and coefficient_discrepancy < threshold_discrepancy
                    )
                    raw_summary_consistency &= np.isclose(
                        computed_shift,
                        float(row["float_to_high_precision_shift"]),
                        rtol=2e-5,
                        atol=2e-15,
                    )
                product_max = max(local_product, default=mp.mpf(0))
                trace_max = max(local_trace, default=mp.mpf(0))
                discrepancy_max = max(local_discrepancy, default=mp.mpf(0))
                shift_max = max(local_shifts, default=0.0)
                maximum_product_residual = max(maximum_product_residual, product_max)
                maximum_trace_residual = max(maximum_trace_residual, trace_max)
                maximum_coefficient_discrepancy = max(
                    maximum_coefficient_discrepancy, discrepancy_max
                )
                maximum_precision_drift = max(maximum_precision_drift, shift_max)
                raw_summary_consistency &= bool(
                    close_mp(
                        product_max,
                        mp.mpf(block["high_precision_root_residual_max"]),
                        mp.mpf("1e-12"),
                    )
                    and close_mp(
                        discrepancy_max,
                        mp.mpf(block["high_precision_coefficient_discrepancy_max"]),
                        mp.mpf("1e-12"),
                    )
                    and np.isclose(
                        shift_max,
                        float(block["precision_drift_max"]),
                        rtol=2e-5,
                        atol=2e-15,
                    )
                    and np.isclose(
                        max(block["float_implementation_discrepancies"]),
                        float(block["float_implementation_discrepancy_max"]),
                        rtol=1e-12,
                        atol=1e-15,
                    )
                )

    checks = {
        "argument_principle_resolution_agreement": argument_agreement,
        "explicit_vs_argument_count_agreement": explicit_count_agreement,
        "root_precision_and_residual_gates": precision_gate,
        "root_raw_summary_consistency": raw_summary_consistency,
        "root_rectangle_and_uniqueness": root_geometry,
        "root_conjugation_consistency": conjugation_consistency,
    }
    details = {
        "artifact_count": len(payloads),
        "cutoff_block_count": block_count,
        "reported_root_instances": root_count,
        "maximum_product_residual": mp.nstr(maximum_product_residual, 20),
        "maximum_trace_residual": mp.nstr(maximum_trace_residual, 20),
        "maximum_coefficient_discrepancy": mp.nstr(
            maximum_coefficient_discrepancy, 20
        ),
        "maximum_float_to_high_precision_shift": maximum_precision_drift,
    }
    return checks, details


def independent_contour_points(
    rectangle: dict[str, float], samples: int
) -> np.ndarray:
    if samples % 4:
        raise ValueError("contour sample count must be divisible by four")
    per_edge = samples // 4
    bottom = np.linspace(
        rectangle["real_min"], rectangle["real_max"], per_edge, endpoint=False
    ) + 1j * rectangle["imag_min"]
    right = rectangle["real_max"] + 1j * np.linspace(
        rectangle["imag_min"], rectangle["imag_max"], per_edge, endpoint=False
    )
    top = np.linspace(
        rectangle["real_max"], rectangle["real_min"], per_edge, endpoint=False
    ) + 1j * rectangle["imag_max"]
    left = rectangle["real_min"] + 1j * np.linspace(
        rectangle["imag_max"], rectangle["imag_min"], per_edge, endpoint=False
    )
    open_contour = np.concatenate((bottom, right, top, left)).astype(np.complex128)
    return np.concatenate((open_contour, open_contour[:1]))


def independent_float_sections_on_points(
    orbits: Sequence[dict[str, Any]],
    cutoffs: Sequence[int],
    points: np.ndarray,
    kappa: int,
    chunk_size: int = 4096,
) -> dict[int, np.ndarray]:
    """Evaluate every requested cycle section through an independent trace recursion."""
    maximum_cutoff = max(cutoffs)
    requested = set(cutoffs)
    trace_terms: list[tuple[np.ndarray, np.ndarray]] = [
        (np.empty(0, dtype=float), np.empty(0, dtype=np.complex128))
        for _ in range(maximum_cutoff + 1)
    ]
    for degree in range(1, maximum_cutoff + 1):
        lengths: list[float] = []
        coefficients: list[complex] = []
        for orbit in orbits:
            period = int(orbit["period"])
            if period > maximum_cutoff or degree % period:
                continue
            repetition = degree // period
            lengths.append(repetition * float(orbit["instability_length"]))
            coefficients.append(
                period * (int(orbit["orientation"]) ** kappa) ** repetition
            )
        trace_terms[degree] = (
            np.asarray(lengths, dtype=float),
            np.asarray(coefficients, dtype=np.complex128),
        )

    values = {
        cutoff: np.empty(points.size, dtype=np.complex128) for cutoff in cutoffs
    }
    for start in range(0, points.size, chunk_size):
        stop = min(start + chunk_size, points.size)
        spectral = points[start:stop]
        cycle_coefficients = [
            np.zeros(spectral.size, dtype=np.complex128)
            for _ in range(maximum_cutoff + 1)
        ]
        cycle_coefficients[0].fill(1)
        traces = [np.zeros(spectral.size, dtype=np.complex128)]
        for degree in range(1, maximum_cutoff + 1):
            lengths, weights = trace_terms[degree]
            traces.append(
                np.sum(
                    weights[:, None]
                    * np.exp(-lengths[:, None] * spectral[None, :]),
                    axis=0,
                )
                if lengths.size
                else np.zeros(spectral.size, dtype=np.complex128)
            )
        determinant = cycle_coefficients[0].copy()
        for degree in range(1, maximum_cutoff + 1):
            accumulator = np.zeros(spectral.size, dtype=np.complex128)
            for index in range(1, degree + 1):
                accumulator += traces[index] * cycle_coefficients[degree - index]
            cycle_coefficients[degree] = -accumulator / degree
            determinant += cycle_coefficients[degree]
            if degree in requested:
                values[degree][start:stop] = determinant
    return values


def audit_independent_windings(
    catalog: dict[str, Any], roots_payload: dict[str, Any], protocol: dict[str, Any]
) -> tuple[dict[str, bool], dict[str, Any]]:
    samples = sorted(int(value) for value in protocol["contour_samples"])
    finest = samples[-1]
    points = independent_contour_points(protocol["root_rectangle"], finest)
    cutoffs = [int(value) for value in roots_payload["cutoffs"]]
    count_match = True
    explicit_match = True
    phase_safe = True
    details: dict[str, Any] = {}
    for sector in (0, 1):
        finest_values = independent_float_sections_on_points(
            catalog["orbits"], cutoffs, points, sector
        )
        sector_rows: dict[str, Any] = {}
        for cutoff in cutoffs:
            stored_block = roots_payload["sectors"][str(sector)]["cutoffs"][str(cutoff)]
            stored_by_samples = {
                int(row["samples"]): int(row["root_count"])
                for row in stored_block["argument_principle"]
            }
            computed_rows: list[dict[str, Any]] = []
            for sample_count in samples:
                stride = finest // sample_count
                values = np.concatenate(
                    (finest_values[cutoff][:-1:stride], finest_values[cutoff][:1])
                )
                increments = np.angle(values[1:] / values[:-1])
                winding = int(np.rint(np.sum(increments) / (2 * np.pi)))
                minimum_modulus = float(np.min(np.abs(values)))
                maximum_phase_step = float(np.max(np.abs(increments)))
                count_match &= winding == stored_by_samples.get(sample_count)
                explicit_match &= winding == len(stored_block["roots"])
                phase_safe &= maximum_phase_step < np.pi
                computed_rows.append(
                    {
                        "samples": sample_count,
                        "root_count": winding,
                        "minimum_boundary_modulus": minimum_modulus,
                        "maximum_phase_step": maximum_phase_step,
                    }
                )
            sector_rows[str(cutoff)] = computed_rows
        details[f"sector_{sector}"] = sector_rows
    return {
        "independent_argument_principle_counts": count_match,
        "independent_explicit_vs_argument_counts": explicit_match,
        "independent_contour_phase_steps_below_pi": phase_safe,
    }, details


def audit_stability(
    roots_payload: dict[str, Any], protocol: dict[str, Any]
) -> tuple[dict[str, bool], dict[str, Any]]:
    tolerance = float(protocol["root_match_tolerance"])
    boundary_margin = float(protocol["training_boundary_margin"])
    rectangle = protocol["root_rectangle"]
    stability_match = True
    gate_match = True
    leading_root_match = True
    twisted_zero = True
    details: dict[str, Any] = {}

    for sector in ("0", "1"):
        sector_payload = roots_payload["sectors"][sector]
        blocks = sector_payload["cutoffs"]
        roots7 = roots_from_pairs(blocks["7"]["roots"])
        roots8 = roots_from_pairs(blocks["8"]["roots"])
        training_match = match_roots(roots7, roots8, tolerance)
        retained_indices = {
            int(row["target_index"])
            for row in training_match["matches"]
            if boundary_distance(roots8[int(row["target_index"])], rectangle)
            >= boundary_margin
        }
        training_roots = [
            root for index, root in enumerate(roots8) if index in retained_indices
        ]
        stored_stability = sector_payload["stability"]
        stored_training = roots_from_pairs(stored_stability["training_roots"])
        stability_match &= bool(
            len(training_roots) == int(stored_stability["training_root_count"])
            and len(training_roots) == len(stored_training)
            and all(
                abs(left - right) <= 1e-12
                for left, right in zip(training_roots, stored_training, strict=True)
            )
        )

        roots12 = roots_from_pairs(blocks["12"]["roots"])
        validation_match = match_roots(training_roots, roots12, tolerance)
        validation_summary = drift_summary(validation_match, len(training_roots))
        validation_roots = [
            roots12[int(row["target_index"])] for row in validation_match["matches"]
        ]
        validation_gates = protocol["validation_gates"]
        validation_pass = bool(
            validation_summary["retained_fraction"]
            >= float(validation_gates["retained_fraction_min"])
            and validation_summary["median_drift"]
            <= float(validation_gates["median_drift_max"])
            and validation_summary["p90_drift"] <= float(validation_gates["p90_drift_max"])
        )
        stored_validation = stored_stability["validation_8_to_12"]
        stability_match &= summaries_close(validation_summary, stored_validation)
        gate_match &= validation_pass == bool(stored_validation["gate_pass"])

        roots16 = roots_from_pairs(blocks["16"]["roots"])
        sealed_match = match_roots(validation_roots, roots16, tolerance)
        sealed_summary = drift_summary(sealed_match, len(validation_roots))
        sealed_gates = protocol["sealed_test_gates"]
        sealed_pass = bool(
            sealed_summary["retained_fraction"]
            >= float(sealed_gates["retained_fraction_min"])
            and sealed_summary["median_drift"] <= float(sealed_gates["median_drift_max"])
            and sealed_summary["p90_drift"] <= float(sealed_gates["p90_drift_max"])
        )
        stored_sealed = stored_stability["sealed_12_to_16"]
        stability_match &= summaries_close(sealed_summary, stored_sealed)
        gate_match &= sealed_pass == bool(stored_sealed["gate_pass"])

        roots20 = roots_from_pairs(blocks["20"]["roots"])
        robustness_match = match_roots(roots16, roots20, tolerance)
        robustness_summary = drift_summary(robustness_match, len(roots16))
        stability_match &= summaries_close(
            robustness_summary, stored_stability["robustness_16_to_20"]
        )

        if sector == "0":
            positive = {
                cutoff: max(
                    value
                    for value in blocks[str(cutoff)]["real_roots_in_minus1_1"]
                    if value > 0
                )
                for cutoff in (10, 12, 16, 20)
            }
            validation_drift = abs(positive[12] - positive[10])
            sealed_drift = abs(positive[16] - positive[12])
            robustness_drift = abs(positive[20] - positive[16])
            leading = sector_payload["leading_real_root_gate"]
            leading_root_match &= bool(
                np.isclose(positive[10], float(leading["h10"]), atol=1e-13)
                and np.isclose(positive[12], float(leading["h12"]), atol=1e-13)
                and np.isclose(positive[16], float(leading["h16"]), atol=1e-13)
                and np.isclose(validation_drift, float(leading["validation_drift"]), atol=1e-15)
                and np.isclose(sealed_drift, float(leading["sealed_test_drift"]), atol=1e-15)
                and bool(leading["validation_pass"])
                == (
                    validation_drift
                    <= float(validation_gates["untwisted_leading_real_root_drift_max"])
                )
                and bool(leading["sealed_test_pass"])
                == (
                    sealed_drift
                    <= float(sealed_gates["untwisted_leading_real_root_drift_max"])
                )
            )
            details["leading_real_root"] = {
                "h10": positive[10],
                "h12": positive[12],
                "h16": positive[16],
                "h20": positive[20],
                "validation_drift": validation_drift,
                "sealed_test_drift": sealed_drift,
                "robustness_drift": robustness_drift,
            }
        else:
            leading_root_match &= sector_payload["leading_real_root_gate"] is None
            twisted_zero &= all(
                any(abs(root) <= 1e-12 for root in roots_from_pairs(blocks[str(cutoff)]["roots"]))
                for cutoff in roots_payload["cutoffs"]
            )

        details[f"sector_{sector}"] = {
            "training_root_count": len(training_roots),
            "validation": validation_summary,
            "sealed_test": sealed_summary,
            "robustness": robustness_summary,
            "validation_gate_pass": validation_pass,
            "sealed_test_gate_pass": sealed_pass,
        }

    checks = {
        "root_stability_recomputed": stability_match,
        "validation_and_sealed_gate_recomputed": gate_match,
        "leading_real_root_drifts_recomputed": leading_root_match,
        "orientation_twisted_exact_zero_at_s0": twisted_zero,
    }
    return checks, details


def independent_product_coefficients(
    orbits: Sequence[dict[str, Any]], cutoff: int, spectral: mp.mpc, kappa: int
) -> list[mp.mpc]:
    coefficients = [mp.mpc(0) for _ in range(cutoff + 1)]
    coefficients[0] = mp.mpc(1)
    for orbit in orbits:
        period = int(orbit["period"])
        if period > cutoff:
            continue
        weight = (int(orbit["orientation"]) ** kappa) * mp.exp(
            -spectral * mp.mpf(orbit["instability_length"])
        )
        updated = list(coefficients)
        for degree in range(period, cutoff + 1):
            updated[degree] -= weight * coefficients[degree - period]
        coefficients = updated
    return coefficients


def independent_trace_coefficients(
    orbits: Sequence[dict[str, Any]], cutoff: int, spectral: mp.mpc, kappa: int
) -> list[mp.mpc]:
    traces = [mp.mpc(0) for _ in range(cutoff + 1)]
    for orbit in orbits:
        period = int(orbit["period"])
        if period > cutoff:
            continue
        length = mp.mpf(orbit["instability_length"])
        signed = int(orbit["orientation"]) ** kappa
        for repetition in range(1, cutoff // period + 1):
            degree = repetition * period
            traces[degree] += (
                period
                * signed**repetition
                * mp.exp(-spectral * repetition * length)
            )
    coefficients = [mp.mpc(0) for _ in range(cutoff + 1)]
    coefficients[0] = mp.mpc(1)
    for degree in range(1, cutoff + 1):
        coefficients[degree] = -mp.fsum(
            traces[index] * coefficients[degree - index]
            for index in range(1, degree + 1)
        ) / degree
    return coefficients


def audit_determinant_spots(
    catalog: dict[str, Any], roots_payload: dict[str, Any]
) -> tuple[bool, dict[str, Any]]:
    worst_coefficient_discrepancy = mp.mpf(0)
    worst_root_residual = mp.mpf(0)
    rows: list[dict[str, Any]] = []
    with mp.workdps(80):
        for sector in (0, 1):
            blocks = roots_payload["sectors"][str(sector)]["cutoffs"]
            for cutoff in (8, 12, 16, 20):
                block = blocks[str(cutoff)]
                roots = roots_from_pairs(block["roots"])
                if sector == 0:
                    candidates = [
                        (index, root)
                        for index, root in enumerate(roots)
                        if root.real > 0 and abs(root.imag) < 1e-8
                    ]
                    index = max(candidates, key=lambda item: item[1].real)[0]
                else:
                    index = min(range(len(roots)), key=lambda item: abs(roots[item]))
                refined = block["high_precision_roots"][index]
                spectral = mp.mpc(mp.mpf(refined["real"]), mp.mpf(refined["imag"]))
                product = independent_product_coefficients(
                    catalog["orbits"], cutoff, spectral, sector
                )
                trace = independent_trace_coefficients(
                    catalog["orbits"], cutoff, spectral, sector
                )
                discrepancy = max(
                    abs(left - right)
                    for left, right in zip(product, trace, strict=True)
                )
                residual = max(abs(mp.fsum(product)), abs(mp.fsum(trace)))
                worst_coefficient_discrepancy = max(
                    worst_coefficient_discrepancy, discrepancy
                )
                worst_root_residual = max(worst_root_residual, residual)
                rows.append(
                    {
                        "sector": sector,
                        "cutoff": cutoff,
                        "root_real": mp.nstr(spectral.real, 20),
                        "root_imag": mp.nstr(spectral.imag, 20),
                        "coefficient_discrepancy": mp.nstr(discrepancy, 20),
                        "determinant_residual": mp.nstr(residual, 20),
                    }
                )
    passed = bool(
        worst_coefficient_discrepancy < mp.mpf("1e-30")
        and worst_root_residual < mp.mpf("1e-30")
    )
    return passed, {
        "spot_checks": rows,
        "worst_coefficient_discrepancy": mp.nstr(
            worst_coefficient_discrepancy, 20
        ),
        "worst_determinant_residual": mp.nstr(worst_root_residual, 20),
    }


def audit_prior_bridge(catalog: dict[str, Any]) -> tuple[bool, dict[str, Any]]:
    bridge = catalog.get("prior_period12_bridge")
    if not bridge:
        return False, {"reason": "missing prior_period12_bridge"}
    recorded = Path(bridge["prior_path"])
    if recorded.exists():
        prior_path = recorded.resolve()
    else:
        prior_path = (
            REPOSITORY_ROOT
            / "docs"
            / "related_programs"
            / "henon_weighted_zeta"
            / "results"
            / "certified_domain_r059.json"
        ).resolve()
    prior = load_json(prior_path)
    current = {
        row["canonical_word"]: row
        for row in catalog["orbits"]
        if int(row["period"]) <= 12
    }
    prior_rows = {row["canonical_word"]: row for row in prior["selected_orbits"]}
    missing = sorted(set(prior_rows) - set(current))
    extra = sorted(set(current) - set(prior_rows))
    with mp.workdps(100):
        relative = [
            abs(
                mp.mpf(current[word]["unstable_modulus"])
                - mp.mpf(prior_rows[word]["unstable_modulus"])
            )
            / mp.mpf(prior_rows[word]["unstable_modulus"])
            for word in sorted(set(current) & set(prior_rows))
        ]
        maximum_relative = max(relative, default=mp.mpf(0))
    passed = bool(
        not missing
        and not extra
        and len(current) == 79
        and maximum_relative < mp.mpf("1e-50")
        and bridge["word_set_match"] is True
        and int(bridge["prior_count"]) == 79
        and int(bridge["current_count_through_12"]) == 79
        and close_mp(
            maximum_relative,
            mp.mpf(bridge["maximum_relative_multiplier_difference"]),
            mp.mpf("1e-12"),
        )
    )
    return passed, {
        "prior_path": portable(prior_path),
        "prior_sha256": sha256_file(prior_path),
        "current_count_through_12": len(current),
        "missing_words": missing,
        "extra_words": extra,
        "maximum_relative_multiplier_difference": mp.nstr(maximum_relative, 20),
    }


def audit_source_chain(
    args: argparse.Namespace,
    protocol: dict[str, Any],
    protocol_hash: str,
    catalog: dict[str, Any],
    roots_payload: dict[str, Any],
    controls: dict[str, Any],
    analysis: dict[str, Any],
) -> tuple[dict[str, bool], dict[str, Any], list[tuple[Path, dict[str, Any]]]]:
    candidate_id = protocol["candidate_id"]
    staged_catalogs: dict[str, tuple[Path, dict[str, Any]]] = {}
    staged_roots: list[tuple[Path, dict[str, Any]]] = []
    stage_hashes: dict[str, dict[str, str]] = {}
    protocol_links = True
    root_catalog_links = True
    stage_shapes = True
    catalog_prefixes = True
    dependency_lock = load_json(DEFAULT_DEPENDENCY_LOCK)
    dependency_hashes: dict[str, dict[str, Any]] = {}
    for row in dependency_lock["dependencies"]:
        path = REPOSITORY_ROOT / row["path"]
        actual = sha256_file(path) if path.is_file() else None
        matches = actual == row["sha256"]
        dependency_hashes[row["path"]] = {
            "expected_sha256": row["sha256"],
            "actual_sha256": actual,
            "matches": matches,
        }
        protocol_links &= matches

    final_by_word = {row["canonical_word"]: row for row in catalog["orbits"]}
    for label, expected_max_period, expected_cutoffs in STAGED_ARTIFACTS:
        catalog_path = RESULTS_ROOT / f"catalog_{label}.json"
        roots_path = RESULTS_ROOT / f"roots_{label}.json"
        catalog_payload = load_json(catalog_path)
        root_payload = load_json(roots_path)
        staged_catalogs[label] = (catalog_path, catalog_payload)
        staged_roots.append((roots_path, root_payload))
        stage_hashes[label] = {
            "catalog": sha256_file(catalog_path),
            "roots": sha256_file(roots_path),
        }
        protocol_links &= bool(
            catalog_payload.get("protocol_sha256") == protocol_hash
            and root_payload.get("protocol_sha256") == protocol_hash
            and catalog_payload.get("candidate_id") == candidate_id
            and root_payload.get("candidate_id") == candidate_id
        )
        recorded_catalog = resolve_recorded_path(root_payload["catalog_path"], roots_path)
        root_catalog_links &= bool(
            sha256_file(recorded_catalog) == root_payload["catalog_sha256"]
            and recorded_catalog == catalog_path.resolve()
        )
        stage_shapes &= bool(
            int(catalog_payload["max_period"]) == expected_max_period
            and tuple(int(value) for value in root_payload["cutoffs"])
            == expected_cutoffs
            and int(root_payload["catalog_max_period"]) == expected_max_period
            and root_payload["determinant_convention"] == protocol["determinant"]
        )
        catalog_prefixes &= all(
            final_by_word.get(row["canonical_word"]) == row
            for row in catalog_payload["orbits"]
        ) and all(bool(value) for value in catalog_payload["gates"].values())

    controls_catalog = resolve_recorded_path(controls["catalog_path"], args.controls)
    controls_roots = resolve_recorded_path(controls["root_results_path"], args.controls)
    expected_control_seeds = set(int(seed) for seed in protocol["control_seeds"])
    observed_control_seeds = {
        name: set(int(seed) for seed in seed_rows)
        for name, seed_rows in controls["controls"].items()
    }
    control_seed_protocol = all(
        seeds == (
            {int(protocol["control_seeds"][0])}
            if name == "constant_roof_parent"
            else expected_control_seeds
        )
        for name, seeds in observed_control_seeds.items()
    )
    controls_links = bool(
        controls.get("protocol_sha256") == protocol_hash
        and controls.get("candidate_id") == candidate_id
        and sha256_file(controls_catalog) == controls["catalog_sha256"]
        and sha256_file(controls_roots) == controls["root_results_sha256"]
        and set(controls["controls"]) == set(protocol["random_controls"])
        and control_seed_protocol
    )
    neighbor_links = True
    neighbor_hashes: dict[str, str] = {}
    neighbor_audits: dict[str, Any] = {}
    for parameter, row in controls["neighbors"].items():
        neighbor_path = resolve_recorded_path(row["catalog_path"], args.controls)
        actual_hash = sha256_file(neighbor_path)
        neighbor_hashes[parameter] = actual_hash
        neighbor_payload = load_json(neighbor_path)
        neighbor_checks, neighbor_details = audit_orbit_catalog(neighbor_payload)
        neighbor_audits[parameter] = {
            "all_checks_pass": all(bool(value) for value in neighbor_checks.values()),
            "checks": neighbor_checks,
            "maximum_recomputed_contraction_bound": neighbor_details[
                "maximum_recomputed_contraction_bound"
            ],
        }
        neighbor_links &= bool(
            actual_hash == row["catalog_sha256"]
            and neighbor_payload["protocol_sha256"] == protocol_hash
            and all(bool(value) for value in neighbor_payload["gates"].values())
            and all(bool(value) for value in neighbor_checks.values())
        )

    analysis_links = bool(
        analysis.get("protocol_sha256") == protocol_hash
        and analysis["source_hashes"]["catalog"] == sha256_file(args.catalog)
        and analysis["source_hashes"]["roots"] == sha256_file(args.roots)
        and analysis["source_hashes"]["controls"] == sha256_file(args.controls)
    )
    primary_links = bool(
        catalog.get("protocol_sha256") == protocol_hash
        and roots_payload.get("protocol_sha256") == protocol_hash
        and catalog.get("candidate_id") == candidate_id
        and roots_payload.get("candidate_id") == candidate_id
        and sha256_file(resolve_recorded_path(roots_payload["catalog_path"], args.roots))
        == roots_payload["catalog_sha256"]
        and roots_payload["catalog_sha256"] == sha256_file(args.catalog)
    )
    checks = {
        "all_protocol_hash_links": protocol_links,
        "all_root_to_catalog_hash_links": root_catalog_links,
        "staged_artifact_shapes": stage_shapes,
        "staged_catalog_prefix_consistency": catalog_prefixes,
        "primary_catalog_root_source_lock": primary_links,
        "controls_source_lock": controls_links,
        "neighbor_catalog_source_locks": neighbor_links,
        "analysis_source_locks": analysis_links,
    }
    details = {
        "inherited_dependencies": dependency_hashes,
        "stage_hashes": stage_hashes,
        "primary_hashes": {
            "catalog": sha256_file(args.catalog),
            "roots": sha256_file(args.roots),
            "controls": sha256_file(args.controls),
            "analysis": sha256_file(args.analysis),
        },
        "controls_catalog_path": portable(controls_catalog),
        "controls_roots_path": portable(controls_roots),
        "neighbor_catalog_hashes": neighbor_hashes,
        "neighbor_catalog_audits": neighbor_audits,
    }
    return checks, details, staged_roots


def main() -> None:
    args = parse_args()
    protocol = load_json(args.protocol)
    catalog = load_json(args.catalog)
    roots_payload = load_json(args.roots)
    controls = load_json(args.controls)
    analysis = load_json(args.analysis)
    protocol_hash = sha256_file(args.protocol)

    checks: dict[str, bool] = {
        "frozen_protocol_hash": protocol_hash == EXPECTED_PROTOCOL_SHA256,
        "protocol_candidate_lock": protocol.get("candidate_id")
        == "henon_h6_instability_roof_v1",
        "protocol_clock_lock": protocol.get("clock")
        == "T_p = log(abs(Lambda_u,p)) with no rescaling",
    }
    details: dict[str, Any] = {
        "protocol": {
            "path": portable(args.protocol),
            "actual_sha256": protocol_hash,
            "expected_sha256": EXPECTED_PROTOCOL_SHA256,
        }
    }

    source_checks, source_details, staged_roots = audit_source_chain(
        args,
        protocol,
        protocol_hash,
        catalog,
        roots_payload,
        controls,
        analysis,
    )
    checks.update(source_checks)
    details["source_chain"] = source_details

    orbit_checks, orbit_details = audit_orbit_catalog(catalog)
    checks.update(orbit_checks)
    details["orbit_audit"] = orbit_details

    clock_pass, clock_details = audit_exact_clock(catalog)
    checks["exact_clock_algebra"] = clock_pass
    details["clock_audit"] = clock_details

    prior_pass, prior_details = audit_prior_bridge(catalog)
    checks["prior_period12_bridge"] = prior_pass
    details["prior_bridge"] = prior_details

    root_checks, root_details = audit_root_blocks(staged_roots, protocol)
    checks.update(root_checks)
    details["root_block_audit"] = root_details

    winding_checks, winding_details = audit_independent_windings(
        catalog, roots_payload, protocol
    )
    checks.update(winding_checks)
    details["independent_winding_audit"] = winding_details

    stability_checks, stability_details = audit_stability(roots_payload, protocol)
    checks.update(stability_checks)
    details["root_stability_audit"] = stability_details

    determinant_pass, determinant_details = audit_determinant_spots(
        catalog, roots_payload
    )
    checks["independent_determinant_spot_checks"] = determinant_pass
    details["determinant_audit"] = determinant_details

    all_passed = all(checks.values())
    output = {
        "run_id": "independent_check_r050",
        "created_utc": protocol["created_utc"],
        "checker": "standalone artifact audit; no producer modules imported",
        "candidate_id": protocol["candidate_id"],
        "protocol_sha256": protocol_hash,
        "source_paths": {
            "catalog": portable(args.catalog),
            "roots": portable(args.roots),
            "controls": portable(args.controls),
            "analysis": portable(args.analysis),
        },
        "checks": checks,
        "details": details,
        "all_checks_pass": all_passed,
        "status": "PASS" if all_passed else "FAIL",
        "scope": (
            "Artifact integrity and finite-section recomputation only; this report does not "
            "establish analytic continuation, a limiting divisor, a continuous transfer "
            "operator, or any Riemann/Hilbert--Polya correspondence."
        ),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(
            output,
            allow_nan=False,
            indent=2,
            sort_keys=True,
            default=json_default,
        )
        + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output": portable(args.output),
                "status": output["status"],
                "check_count": len(checks),
                "failed_checks": [key for key, value in checks.items() if not value],
            },
            indent=2,
        )
    )
    if not all_passed:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
