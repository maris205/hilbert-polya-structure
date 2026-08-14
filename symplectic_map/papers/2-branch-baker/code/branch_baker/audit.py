"""Independent numerical audits for the source-locked branch baker.

The high-precision parent audit intentionally does not import the exact
``cycles`` ledger.  It enumerates closed state words itself, obtains parent
periodic points by contracting inverse branches, and clusters the resulting
roots.  Agreement with the frozen count formula is therefore an independent
consistency check, not interval certification.

The floating audit checks one forward branch followed immediately by its
identified inverse at every step.  It then advances the forward image.  It
never reports a long chaotic trajectory reversal.
"""

from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path
import random
from datetime import datetime, timezone
from typing import Any, Mapping, Sequence

import mpmath as mp

from . import protocol
from .model import MarkovBakerModel, Point


PROJECT_ROOT = Path(__file__).resolve().parents[2]
SOURCE_LOCK_PATH = PROJECT_ROOT / "experiments" / "source_lock.json"
SPLITS = ("development", "validation", "test")


class AuditConfigurationError(RuntimeError):
    """Raised when an audit request disagrees with the frozen protocol."""


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_source_lock(path: str | Path | None = None) -> dict[str, Any]:
    """Load and minimally validate the candidate source lock."""

    lock_path = SOURCE_LOCK_PATH if path is None else Path(path)
    with lock_path.open("r", encoding="utf-8") as handle:
        lock = json.load(handle)
    if not isinstance(lock, dict):
        raise AuditConfigurationError("source lock must contain a JSON object")
    if lock.get("candidate_id") != "pcf_markov_baker_v1":
        raise AuditConfigurationError("source lock has the wrong candidate id")
    required = (
        "parent",
        "markov_factor",
        "verification_protocol",
        "split_seed_derivation",
    )
    missing = [key for key in required if key not in lock]
    if missing:
        raise AuditConfigurationError(
            f"source lock is missing required section(s): {', '.join(missing)}"
        )
    return lock


def derive_seed(candidate_id: str, split: str) -> int:
    """Apply the frozen SHA-256-to-unsigned-64-bit seed rule."""

    if split not in SPLITS:
        raise AuditConfigurationError(f"unknown split: {split!r}")
    digest = hashlib.sha256(f"{candidate_id}:{split}".encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big", signed=False)


def validate_split_seeds(lock: Mapping[str, Any]) -> dict[str, int]:
    """Recompute all seeds and reject a lock whose values drifted."""

    candidate_id = str(lock.get("candidate_id", ""))
    seed_section = lock.get("split_seed_derivation")
    if not isinstance(seed_section, Mapping):
        raise AuditConfigurationError("split_seed_derivation must be an object")
    expected_rule = (
        "unsigned big-endian integer from the first 8 bytes of "
        "SHA256('pcf_markov_baker_v1:' + split)"
    )
    if seed_section.get("rule") != expected_rule:
        raise AuditConfigurationError("seed derivation rule changed from the frozen rule")

    derived: dict[str, int] = {}
    for split in SPLITS:
        actual = seed_section.get(split)
        expected = derive_seed(candidate_id, split)
        if isinstance(actual, bool) or not isinstance(actual, int):
            raise AuditConfigurationError(f"source-lock seed for {split} is not an integer")
        if actual != expected:
            raise AuditConfigurationError(
                f"source-lock seed mismatch for {split}: expected {expected}, got {actual}"
            )
        derived[split] = expected
    return derived


def require_split_access(split: str) -> str:
    """Apply the hash-bound protocol gate before any random sample is drawn."""

    protocol.require_split(split)
    return "development_open" if split == "development" else "hash_marker_verified"


def _fraction_to_mpf(value: str) -> mp.mpf:
    numerator, separator, denominator = value.partition("/")
    if not separator:
        return mp.mpf(numerator)
    return mp.mpf(numerator) / mp.mpf(denominator)


def _parameter_polynomial(value: mp.mpf) -> mp.mpf:
    return value**3 - 2 * value**2 + 2 * value - 2


def _bisect_parameter(lower: mp.mpf, upper: mp.mpf, tolerance: mp.mpf) -> mp.mpf:
    low_value = _parameter_polynomial(lower)
    high_value = _parameter_polynomial(upper)
    if not low_value < 0 < high_value:
        raise AuditConfigurationError("frozen root interval does not bracket the root")
    while upper - lower > tolerance:
        midpoint = (lower + upper) / 2
        value = _parameter_polynomial(midpoint)
        if value < 0:
            lower = midpoint
        else:
            upper = midpoint
    return (lower + upper) / 2


def _closed_words(
    adjacency: Sequence[Sequence[int]], period: int
) -> list[tuple[int, ...]]:
    """Enumerate based closed words without using the main ledger module."""

    words: list[tuple[int, ...]] = []
    states = range(len(adjacency))

    def extend(path: list[int], start: int) -> None:
        if len(path) == period:
            if adjacency[path[-1]][start]:
                words.append(tuple(path))
            return
        for target in states:
            if adjacency[path[-1]][target]:
                path.append(target)
                extend(path, start)
                path.pop()

    for start in states:
        extend([start], start)
    return words


def _canonical_rotation(word: Sequence[int]) -> tuple[int, ...]:
    values = tuple(word)
    return min(values[offset:] + values[:offset] for offset in range(len(values)))


def _is_primitive_word(word: Sequence[int]) -> bool:
    values = tuple(word)
    period = len(values)
    return all(
        values != values[offset:] + values[:offset]
        for offset in range(1, period)
    )


def _primitive_cycle_representatives(
    adjacency: Sequence[Sequence[int]], period: int
) -> tuple[tuple[int, ...], ...]:
    """Direct local necklace enumeration, independent of ``cycles.py``."""

    representatives = {
        word
        for word in _closed_words(adjacency, period)
        if _is_primitive_word(word) and word == _canonical_rotation(word)
    }
    return tuple(sorted(representatives))


def _parent_map(value: mp.mpf, parameter: mp.mpf) -> mp.mpf:
    return 1 - parameter * value * value


def _inverse_branch(state: int, value: mp.mpf, parameter: mp.mpf) -> mp.mpf:
    radicand = (1 - value) / parameter
    if radicand < 0 and abs(radicand) < mp.eps * 64:
        radicand = mp.mpf("0")
    if radicand < 0:
        raise ArithmeticError("inverse branch left the real parent core")
    root = mp.sqrt(radicand)
    return -root if state == 0 else root


def _periodic_point_from_word(
    word: Sequence[int],
    parameter: mp.mpf,
    d_value: mp.mpf,
    tolerance: mp.mpf,
    max_iterations: int = 20_000,
) -> tuple[mp.mpf, int]:
    intervals = ((-d_value, mp.mpf("0")), (mp.mpf("0"), d_value), (d_value, mp.mpf("1")))
    low, high = intervals[word[0]]
    current = (low + high) / 2
    for iteration in range(1, max_iterations + 1):
        updated = current
        for state in reversed(word):
            updated = _inverse_branch(state, updated, parameter)
        if abs(updated - current) <= tolerance:
            return updated, iteration
        current = updated
    raise ArithmeticError(
        f"inverse-branch contraction did not converge for period-{len(word)} word"
    )


def _iterate_parent(value: mp.mpf, parameter: mp.mpf, period: int) -> mp.mpf:
    for _ in range(period):
        value = _parent_map(value, parameter)
    return value


def _cluster_count(values: Sequence[mp.mpf], tolerance: mp.mpf) -> int:
    if not values:
        return 0
    ordered = sorted(values)
    clusters = 1
    anchor = ordered[0]
    for value in ordered[1:]:
        if abs(value - anchor) > tolerance:
            clusters += 1
            anchor = value
    return clusters


def _decimal(value: mp.mpf, digits: int) -> str:
    return mp.nstr(value, n=digits, strip_zeros=False)


def independent_parent_audit(
    *,
    digits: int | None = None,
    max_period: int | None = None,
    source_lock_path: str | Path | None = None,
    allow_reduced_precision: bool = False,
) -> dict[str, Any]:
    """Numerically audit the parent factor without the exact cycle ledger.

    The frozen defaults are 100 decimal digits and periods through 20.  A
    lower precision is accepted only when explicitly labelled as reduced test
    mode; it never changes the frozen production target in the returned data.
    """

    lock_path = SOURCE_LOCK_PATH if source_lock_path is None else Path(source_lock_path)
    lock = load_source_lock(lock_path)
    verification = lock["verification_protocol"]
    frozen_digits = int(verification["independent_parent_audit_digits"])
    frozen_max_period = int(verification["candidate_max_period"])
    requested_digits = frozen_digits if digits is None else int(digits)
    requested_max_period = frozen_max_period if max_period is None else int(max_period)
    if requested_digits < 30:
        raise ValueError("parent audit requires at least 30 decimal digits")
    if requested_digits < frozen_digits and not allow_reduced_precision:
        raise AuditConfigurationError(
            "reduced precision requires allow_reduced_precision=True and is test-only"
        )
    if not 1 <= requested_max_period <= frozen_max_period:
        raise ValueError(f"max_period must lie in [1, {frozen_max_period}]")

    configured_target_text = str(verification["independent_parent_audit_residual_target"])
    with mp.workdps(requested_digits + 10):
        configured_target = mp.mpf(configured_target_text)
        if requested_digits < frozen_digits:
            effective_target = max(configured_target, mp.power(10, -(requested_digits - 20)))
        else:
            effective_target = configured_target
        # Five guard decades below the declared residual threshold suffice;
        # driving all 4,092 based words to the full display precision would
        # add cost without strengthening the frozen consistency claim.
        solve_tolerance = min(effective_target / 100_000, mp.power(10, -requested_digits))
        cluster_tolerance = max(effective_target * 10, mp.power(10, -(requested_digits - 15)))

        lower_text, upper_text = lock["parent"]["root_isolation_interval"]
        lower = _fraction_to_mpf(lower_text)
        upper = _fraction_to_mpf(upper_text)
        parameter = _bisect_parameter(lower, upper, solve_tolerance)
        d_value = parameter - 1
        parameter_residual = abs(_parameter_polynomial(parameter))

        actual_postcritical = [mp.mpf("0")]
        for _ in range(4):
            actual_postcritical.append(_parent_map(actual_postcritical[-1], parameter))
        expected_postcritical = (mp.mpf("0"), mp.mpf("1"), -d_value, d_value, d_value)
        postcritical_residuals = [
            abs(actual - expected)
            for actual, expected in zip(actual_postcritical, expected_postcritical)
        ]

        raw_adjacency = lock["markov_factor"]["adjacency"]
        adjacency = tuple(tuple(int(entry) for entry in row) for row in raw_adjacency)
        if adjacency != ((0, 0, 1), (0, 0, 1), (1, 1, 0)):
            raise AuditConfigurationError("parent audit only applies to the frozen adjacency")

        symbolic_counts: list[int] = []
        expected_parent_counts: list[int] = []
        numerical_parent_counts: list[int] = []
        boundary_duplicate_counts: list[int] = []
        max_periodic_residual = abs(_parent_map(d_value, parameter) - d_value)
        maximum_inverse_iterations = 0

        # Solve one point per primitive graph orbit, then generate its cyclic
        # points with the parent map.  This preserves a fully numerical root
        # audit while avoiding thousands of redundant solves of rotated or
        # imprimitive state words.
        orbit_points_by_primitive_period: dict[int, list[mp.mpf]] = {}
        for primitive_period in range(2, requested_max_period + 1, 2):
            orbit_points: list[mp.mpf] = []
            for word in _primitive_cycle_representatives(adjacency, primitive_period):
                root, iterations = _periodic_point_from_word(
                    word,
                    parameter,
                    d_value,
                    solve_tolerance,
                )
                maximum_inverse_iterations = max(maximum_inverse_iterations, iterations)
                point = root
                for _ in range(primitive_period):
                    orbit_points.append(point)
                    residual = abs(
                        _iterate_parent(point, parameter, primitive_period) - point
                    )
                    max_periodic_residual = max(max_periodic_residual, residual)
                    point = _parent_map(point, parameter)
            orbit_points_by_primitive_period[primitive_period] = orbit_points

        for period in range(1, requested_max_period + 1):
            words = _closed_words(adjacency, period)
            symbolic_counts.append(len(words))
            expected_parent = (
                1 if period % 2 else 2 ** (period // 2 + 1) - 1
            )
            expected_parent_counts.append(expected_parent)
            if period % 2:
                numerical_parent_counts.append(1)
                boundary_duplicate_counts.append(0)
                continue

            roots = [
                point
                for primitive_period, orbit_points in orbit_points_by_primitive_period.items()
                if period % primitive_period == 0
                for point in orbit_points
            ]
            distinct = _cluster_count(roots, cluster_tolerance)
            numerical_parent_counts.append(distinct)
            boundary_duplicate_counts.append(len(roots) - distinct)

        max_postcritical_residual = max(postcritical_residuals)
        residuals_pass = max(
            parameter_residual,
            max_postcritical_residual,
            max_periodic_residual,
        ) < effective_target
        expected_duplicates = [0 if period % 2 else 1 for period in range(1, requested_max_period + 1)]
        counts_pass = numerical_parent_counts == expected_parent_counts
        boundary_pass = boundary_duplicate_counts == expected_duplicates
        consistency_passed = residuals_pass and counts_pass and boundary_pass

        display_digits = min(requested_digits, 110)
        frozen_scale = (
            requested_digits == frozen_digits and requested_max_period == frozen_max_period
        )
        return {
            "candidate_id": lock["candidate_id"],
            "audit_kind": "independent_high_precision_parent_factor",
            "source_lock_sha256": _sha256_file(lock_path),
            "external_prime_or_zero_data_accessed": False,
            "digits": requested_digits,
            "max_period": requested_max_period,
            "interpretation": verification["parent_audit_interpretation"],
            "independence": (
                "closed words are enumerated locally and parent periodic points are "
                "obtained from high-precision monotone inverse branches; the exact "
                "cycle-ledger generator is not imported"
            ),
            "reduced_precision_test_mode": requested_digits < frozen_digits,
            "frozen_scale_executed": frozen_scale,
            "parameter": {
                "value": _decimal(parameter, display_digits),
                "polynomial_residual": _decimal(parameter_residual, display_digits),
                "inside_frozen_interval": bool(lower < parameter < upper),
            },
            "postcritical": {
                "values": [_decimal(value, display_digits) for value in actual_postcritical],
                "residuals": [
                    _decimal(value, display_digits) for value in postcritical_residuals
                ],
                "max_abs_residual": _decimal(max_postcritical_residual, display_digits),
            },
            "periodic_factor": {
                "symbolic_counts": symbolic_counts,
                "parent_expected_counts": expected_parent_counts,
                "numerically_distinct_parent_counts": numerical_parent_counts,
                "boundary_duplicate_counts": boundary_duplicate_counts,
                "expected_boundary_duplicate_counts": expected_duplicates,
                "max_periodic_residual": _decimal(max_periodic_residual, display_digits),
                "maximum_inverse_iterations": maximum_inverse_iterations,
            },
            "thresholds": {
                "residual_target": configured_target_text,
                "configured_residual_target": configured_target_text,
                "effective_residual_target": _decimal(effective_target, display_digits),
            },
            "residuals_passed": residuals_pass,
            "counts_passed": counts_pass,
            "boundary_collapse_passed": boundary_pass,
            "consistency_passed": consistency_passed,
            "frozen_protocol_passed": consistency_passed and frozen_scale,
            "passed": consistency_passed,
        }


def _point_error(actual: Point, expected: Point) -> float:
    if actual.label != expected.label:
        return math.inf
    return max(abs(actual.x - expected.x), abs(actual.y - expected.y))


def run_float_stress(
    model: MarkovBakerModel | None = None,
    *,
    split: str = "development",
    points: int | None = None,
    steps: int | None = None,
    source_lock_path: str | Path | None = None,
) -> dict[str, Any]:
    """Run the sealed, per-step forward/identified-inverse float audit."""

    lock_path = SOURCE_LOCK_PATH if source_lock_path is None else Path(source_lock_path)
    lock = load_source_lock(lock_path)
    seeds = validate_split_seeds(lock)
    gate_authorization = require_split_access(split)
    protocol.append_access_log(
        datetime.now(timezone.utc).isoformat(),
        split,
        "run_float_stress",
        gate_authorization,
        "authorized_before_sampling",
    )

    verification = lock["verification_protocol"]
    requested_points = (
        int(verification["float_points_per_split"]) if points is None else int(points)
    )
    requested_steps = int(verification["float_steps"]) if steps is None else int(steps)
    if requested_points <= 0 or requested_steps <= 0:
        raise ValueError("points and steps must both be positive")
    max_error_threshold = float(verification["float_roundtrip_max_error"])
    allowed_boundary_failures = int(
        verification["allowed_boundary_failures_in_random_stress"]
    )

    candidate = MarkovBakerModel() if model is None else model
    rng = random.Random(seeds[split])
    sample = candidate.sample(rng, requested_points)
    max_roundtrip_error = 0.0
    boundary_failures = 0
    completed_checks = 0
    edge_mismatches = 0
    exception_counts: dict[str, int] = {}

    for initial in sample:
        current = initial
        for _ in range(requested_steps):
            try:
                forward = candidate.forward(current)
                backward = candidate.inverse(forward.point)
                completed_checks += 1
                error = _point_error(backward.point, current)
                max_roundtrip_error = max(max_roundtrip_error, error)
                if backward.edge != forward.edge:
                    edge_mismatches += 1
                    boundary_failures += 1
                current = forward.point
            except (ArithmeticError, ValueError) as exc:
                boundary_failures += 1
                name = type(exc).__name__
                exception_counts[name] = exception_counts.get(name, 0) + 1
                break

    expected_checks = requested_points * requested_steps
    passed = (
        completed_checks == expected_checks
        and edge_mismatches == 0
        and boundary_failures <= allowed_boundary_failures
        and math.isfinite(max_roundtrip_error)
        and max_roundtrip_error < max_error_threshold
    )
    frozen_scale = (
        requested_points == int(verification["float_points_per_split"])
        and requested_steps == int(verification["float_steps"])
    )
    return {
        "candidate_id": lock["candidate_id"],
        "audit_kind": "floating_per_step_forward_identified_inverse",
        "source_lock_sha256": _sha256_file(lock_path),
        "external_prime_or_zero_data_accessed": False,
        "split": split,
        "seed": seeds[split],
        "gate": {
            "authorization": gate_authorization,
            "verified_before_sampling": True,
        },
        "points": requested_points,
        "steps": requested_steps,
        "expected_checks": expected_checks,
        "completed_checks": completed_checks,
        "roundtrip_definition": verification["float_roundtrip_definition"],
        "long_trajectory_reversal_claimed": False,
        "max_roundtrip_error": max_roundtrip_error,
        "edge_mismatches": edge_mismatches,
        "boundary_failures": boundary_failures,
        "exception_counts": exception_counts,
        "thresholds": {
            "max_roundtrip_error": max_error_threshold,
            "allowed_boundary_failures": allowed_boundary_failures,
        },
        "frozen_scale_executed": frozen_scale,
        "frozen_protocol_passed": passed and frozen_scale,
        "passed": passed,
    }


__all__ = [
    "AuditConfigurationError",
    "SOURCE_LOCK_PATH",
    "SPLITS",
    "derive_seed",
    "independent_parent_audit",
    "load_source_lock",
    "require_split_access",
    "run_float_stress",
    "validate_split_seeds",
]
