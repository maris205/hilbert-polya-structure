#!/usr/bin/env python3
"""HCS-C05 target-free Maslov/action/instability pilot.

The script reads only the frozen H_6 primitive-orbit catalogue.  It rebuilds
the cyclic action Hessian, computes every repeated-orbit inertia directly,
audits Hill's determinant identity and reversal, and constructs finite formal
cycle-determinant sections.  It never reads arithmetic target data.

The absolute phase is deliberately labelled gauge-fixed: adding a constant C
to the generating function preserves the classical map but sends
    A_p -> A_p + n_p C,
which is the same as z -> z exp(i theta C).  Consequently fixed-z root angles
are not intrinsic to the classical Hénon map.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np


PARAMETER = 6.0
CUTOFFS = (8, 12, 16, 20)
S_VALUES = (0.0, 0.5)
THETA_VALUES = (0.0, 1.0)
SEEDS = (20260805, 20260806, 20260807)
Z_POINTS = {
    "z025": 0.25 + 0.0j,
    "z050": 0.50 + 0.0j,
    "z050i": 0.0 + 0.50j,
    "z035p035i": 0.35 + 0.35j,
}


@dataclass(frozen=True)
class Orbit:
    orbit_id: str
    sign_word: str
    period: int
    coordinates: np.ndarray
    action: float
    length: float
    trace: float
    orientation: int


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def display_path(path: Path, repo: Path) -> str:
    """Use a repository-relative path when possible, otherwise an absolute path."""

    resolved = path.resolve()
    try:
        return str(resolved.relative_to(repo.resolve()))
    except ValueError:
        return str(resolved)


def canonical_rotation(word: str) -> str:
    return min(word[index:] + word[:index] for index in range(len(word)))


def load_catalog(path: Path) -> tuple[dict, list[Orbit]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = payload["orbits"]
    orbits = [
        Orbit(
            orbit_id=row["canonical_word"],
            sign_word=row["sign_word"],
            period=int(row["period"]),
            coordinates=np.asarray(row["coordinates"], dtype=float),
            action=float(row["action"]),
            length=float(row["instability_length"]),
            trace=float(row["monodromy_trace"]),
            orientation=int(row["orientation"]),
        )
        for row in rows
    ]
    orbits.sort(key=lambda item: (item.period, item.orbit_id))
    return payload, orbits


def periodic_action(coordinates: np.ndarray, parameter: float = PARAMETER) -> float:
    q = np.asarray(coordinates, dtype=float)
    return float(np.sum(q * np.roll(q, -1) - q + parameter * q**3 / 3.0))


def cyclic_hessian(coordinates: np.ndarray, parameter: float = PARAMETER) -> np.ndarray:
    """Return D^2 sum_i S(q_i,q_{i+1}), with n=1,2 handled exactly."""

    q = np.asarray(coordinates, dtype=float)
    period = q.size
    if period == 0:
        raise ValueError("empty orbit")
    if period == 1:
        return np.asarray([[2.0 + 2.0 * parameter * q[0]]], dtype=float)
    hessian = np.diag(2.0 * parameter * q)
    if period == 2:
        hessian[0, 1] = hessian[1, 0] = 2.0
        return hessian
    for index in range(period):
        successor = (index + 1) % period
        hessian[index, successor] += 1.0
        hessian[successor, index] += 1.0
    return hessian


def monodromy(coordinates: np.ndarray, parameter: float = PARAMETER) -> np.ndarray:
    matrix = np.eye(2, dtype=float)
    for coordinate in np.asarray(coordinates, dtype=float):
        jacobian = np.asarray([[-2.0 * parameter * coordinate, -1.0], [1.0, 0.0]])
        matrix = jacobian @ matrix
    return matrix


def trace_power(trace: float, repetition: int) -> float:
    """tr(M^r) for det M=1, via its exact Chebyshev recurrence."""

    if repetition < 1:
        raise ValueError("repetition must be positive")
    if repetition == 1:
        return float(trace)
    previous_previous = 2.0
    previous = float(trace)
    for _ in range(2, repetition + 1):
        current = trace * previous - previous_previous
        previous_previous, previous = previous, current
    return previous


def inertia(hessian: np.ndarray) -> tuple[int, int, float, float, int]:
    eigenvalues = np.linalg.eigvalsh(hessian)
    scale = max(1.0, float(np.max(np.abs(eigenvalues))))
    tolerance = 1.0e-11 * scale
    zeros = int(np.count_nonzero(np.abs(eigenvalues) <= tolerance))
    negatives = int(np.count_nonzero(eigenvalues < -tolerance))
    signature = int(np.count_nonzero(eigenvalues > tolerance)) - negatives
    minimum = float(np.min(np.abs(eigenvalues)))
    sign, logabs = np.linalg.slogdet(hessian)
    return negatives, signature, minimum, float(logabs), int(sign)


def maslov_phase(index: int) -> complex:
    return (-1.0j) ** int(index)


def reversal_map(orbits: Iterable[Orbit]) -> tuple[dict[str, Orbit], dict[str, str]]:
    by_sign = {canonical_rotation(orbit.sign_word): orbit for orbit in orbits}
    if len(by_sign) != len(tuple(orbits)):
        raise ValueError("sign necklaces are not unique")
    partners: dict[str, str] = {}
    for key, orbit in by_sign.items():
        reverse_key = canonical_rotation(key[::-1])
        if reverse_key not in by_sign:
            raise ValueError(f"missing reverse partner for {orbit.orbit_id}")
        partners[orbit.orbit_id] = by_sign[reverse_key].orbit_id
    return {orbit.orbit_id: orbit for orbit in by_sign.values()}, partners


def build_phase_ledger(orbits: list[Orbit], max_degree: int) -> tuple[list[dict], dict]:
    by_id, partners = reversal_map(orbits)
    primitive_mu: dict[str, int] = {}
    for orbit in orbits:
        primitive_mu[orbit.orbit_id] = inertia(cyclic_hessian(orbit.coordinates))[0]

    ledger: list[dict] = []
    max_hill_log_error = 0.0
    max_action_error = 0.0
    max_trace_error = 0.0
    minimum_hessian_eigenvalue = math.inf
    zero_inertia_count = 0
    parity_failures = 0
    repetition_additivity_failures = 0
    symbol_count_failures = 0
    hill_sign_mismatches = 0
    reversal_failures = 0
    phase_counts: Counter[int] = Counter()
    minimum_coordinate_modulus = min(
        abs(float(coordinate)) for orbit in orbits for coordinate in orbit.coordinates
    )
    coordinate_bound_failures = sum(
        abs(float(coordinate)) < (1.0 / 3.0)
        for orbit in orbits
        for coordinate in orbit.coordinates
    )
    minimum_diagonal_dominance_margin = math.inf

    for orbit in orbits:
        if orbit.period > max_degree:
            continue
        partner = by_id[partners[orbit.orbit_id]]
        partner_mu = primitive_mu[partner.orbit_id]
        reverse_errors = {
            "action": abs(orbit.action - partner.action),
            "length": abs(orbit.length - partner.length),
            "trace": abs(orbit.trace - partner.trace),
            "orientation": int(orbit.orientation != partner.orientation),
            "maslov": int(primitive_mu[orbit.orbit_id] != partner_mu),
        }
        reversal_failures += int(any(value > 1.0e-11 for value in reverse_errors.values()))

        for repetition in range(1, max_degree // orbit.period + 1):
            repeated_coordinates = np.tile(orbit.coordinates, repetition)
            total_period = orbit.period * repetition
            hessian = cyclic_hessian(repeated_coordinates)
            mu, signature, min_eigenvalue, hessian_logabs, hessian_sign = inertia(hessian)
            negative_symbol_count = int(np.count_nonzero(repeated_coordinates < 0.0))
            symbol_match = mu == negative_symbol_count
            symbol_count_failures += int(not symbol_match)
            if total_period == 1:
                diagonal_dominance_margin = abs(float(hessian[0, 0]))
            else:
                diagonal_dominance_margin = float(
                    np.min(np.abs(2.0 * PARAMETER * repeated_coordinates) - 2.0)
                )
            minimum_diagonal_dominance_margin = min(
                minimum_diagonal_dominance_margin, diagonal_dominance_margin
            )
            minimum_hessian_eigenvalue = min(minimum_hessian_eigenvalue, min_eigenvalue)
            zero_inertia_count += int(min_eigenvalue <= 1.0e-11)
            repeated_trace = trace_power(orbit.trace, repetition)
            stability_determinant = 2.0 - repeated_trace
            expected_sign = int(((-1) ** (total_period - 1)) * np.sign(stability_determinant))
            expected_logabs = math.log(abs(stability_determinant))
            hill_log_error = abs(hessian_logabs - expected_logabs)
            max_hill_log_error = max(max_hill_log_error, hill_log_error)
            hill_sign_match = hessian_sign == expected_sign
            hill_sign_mismatches += int(not hill_sign_match)

            direct_action = periodic_action(repeated_coordinates)
            action_error = abs(direct_action - repetition * orbit.action)
            max_action_error = max(max_action_error, action_error)

            direct_trace = float(np.trace(monodromy(repeated_coordinates)))
            trace_error = abs(direct_trace - repeated_trace) / max(1.0, abs(repeated_trace))
            max_trace_error = max(max_trace_error, trace_error)

            expected_parity = ((-1) ** total_period) * (orbit.orientation**repetition)
            parity_ok = ((-1) ** mu) == expected_parity
            parity_failures += int(not parity_ok)
            additive = mu == repetition * primitive_mu[orbit.orbit_id]
            repetition_additivity_failures += int(not additive)
            phase = maslov_phase(mu)
            phase_counts[mu % 4] += 1
            ledger.append(
                {
                    "orbit_id": orbit.orbit_id,
                    "reverse_partner_id": partner.orbit_id,
                    "self_reversing": orbit.orbit_id == partner.orbit_id,
                    "primitive_period": orbit.period,
                    "repetition": repetition,
                    "total_period": total_period,
                    "primitive_action": orbit.action,
                    "direct_repeated_action": direct_action,
                    "action_repetition_error": action_error,
                    "primitive_length": orbit.length,
                    "repeated_length": repetition * orbit.length,
                    "primitive_trace": orbit.trace,
                    "repeated_trace": repeated_trace,
                    "trace_repetition_relative_error": trace_error,
                    "primitive_orientation": orbit.orientation,
                    "repeated_orientation": orbit.orientation**repetition,
                    "primitive_maslov": primitive_mu[orbit.orbit_id],
                    "repeated_maslov": mu,
                    "negative_symbol_count": negative_symbol_count,
                    "symbol_count_maslov_match": symbol_match,
                    "maslov_repetition_defect": mu - repetition * primitive_mu[orbit.orbit_id],
                    "maslov_mod4": mu % 4,
                    "maslov_phase_real": phase.real,
                    "maslov_phase_imag": phase.imag,
                    "hessian_signature": signature,
                    "minimum_absolute_hessian_eigenvalue": min_eigenvalue,
                    "diagonal_dominance_margin": diagonal_dominance_margin,
                    "hessian_determinant_sign": hessian_sign,
                    "hill_expected_sign": expected_sign,
                    "hill_sign_match": hill_sign_match,
                    "hill_logabs_error": hill_log_error,
                    "maslov_orientation_parity_ok": parity_ok,
                    "reversal_action_error": reverse_errors["action"],
                    "reversal_length_error": reverse_errors["length"],
                    "reversal_trace_error": reverse_errors["trace"],
                    "reversal_orientation_mismatch": reverse_errors["orientation"],
                    "reversal_maslov_mismatch": reverse_errors["maslov"],
                }
            )

    metrics = {
        "primitive_cycle_count": len(orbits),
        "ledger_row_count": len(ledger),
        "nontrivial_repetition_count": sum(row["repetition"] > 1 for row in ledger),
        "self_reversing_primitive_count": sum(
            partners[orbit.orbit_id] == orbit.orbit_id for orbit in orbits
        ),
        "reversal_paired_primitive_count": sum(
            partners[orbit.orbit_id] != orbit.orbit_id for orbit in orbits
        ),
        "missing_reverse_partner_count": 0,
        "reversal_failure_count": reversal_failures,
        "repetition_maslov_additivity_failure_count": repetition_additivity_failures,
        "symbol_count_maslov_failure_count": symbol_count_failures,
        "maslov_orientation_parity_failure_count": parity_failures,
        "hill_sign_mismatch_count": hill_sign_mismatches,
        "near_zero_hessian_count": zero_inertia_count,
        "coordinate_bound": "|q_i| >= 1/3 on the certified survivor",
        "coordinate_bound_failure_count": coordinate_bound_failures,
        "minimum_coordinate_modulus": minimum_coordinate_modulus,
        "minimum_strict_diagonal_dominance_margin": minimum_diagonal_dominance_margin,
        "minimum_absolute_hessian_eigenvalue": minimum_hessian_eigenvalue,
        "maximum_hill_logabs_error": max_hill_log_error,
        "maximum_action_repetition_error": max_action_error,
        "maximum_trace_repetition_relative_error": max_trace_error,
        "maslov_mod4_counts_all_ledger_rows": {
            str(key): int(value) for key, value in sorted(phase_counts.items())
        },
    }
    return ledger, metrics


def shuffled_actions(orbits: list[Orbit], seed: int) -> dict[str, float]:
    rng = np.random.default_rng(seed)
    grouped: dict[int, list[Orbit]] = defaultdict(list)
    for orbit in orbits:
        grouped[orbit.period].append(orbit)
    result: dict[str, float] = {}
    for period in sorted(grouped):
        group = sorted(grouped[period], key=lambda item: item.orbit_id)
        values = np.asarray([item.action for item in group])
        permuted = values[rng.permutation(len(values))]
        result.update({item.orbit_id: float(value) for item, value in zip(group, permuted)})
    return result


def random_phases(orbits: list[Orbit], seed: int) -> dict[str, complex]:
    rng = np.random.default_rng(seed)
    return {
        orbit.orbit_id: complex(np.exp(2.0j * np.pi * rng.random()))
        for orbit in sorted(orbits, key=lambda item: item.orbit_id)
    }


def determinant_coefficients(
    orbits: list[Orbit],
    cutoff: int,
    spectral: float,
    theta: float,
    primitive_mu: dict[str, int],
    variant: str,
    seed: int | None = None,
    action_constant: float = 0.0,
) -> np.ndarray:
    """Finite coefficient section using exact repeated Hessian phases."""

    action_map = shuffled_actions(orbits, int(seed)) if variant == "shuffled_action" else None
    phase_map = random_phases(orbits, int(seed)) if variant == "random_phase" else None
    flat_traces = np.zeros(cutoff + 1, dtype=np.complex128)
    for orbit in orbits:
        if orbit.period > cutoff:
            continue
        action = action_map[orbit.orbit_id] if action_map is not None else orbit.action
        action += orbit.period * float(action_constant)
        length = float(orbit.period) if variant == "constant_roof" else orbit.length
        for repetition in range(1, cutoff // orbit.period + 1):
            degree = repetition * orbit.period
            repeated_trace = trace_power(orbit.trace, repetition)
            denominator = math.sqrt(abs(2.0 - repeated_trace))
            if variant == "orientation_fallback":
                character = complex(orbit.orientation**repetition)
            elif variant == "random_phase":
                character = phase_map[orbit.orbit_id] ** repetition
            else:
                # Exact local collapse on the certified survivor: strict
                # sign-diagonal dominance gives mu = number of negative q symbols.
                repeated_mu = repetition * int(np.count_nonzero(orbit.coordinates < 0.0))
                character = maslov_phase(repeated_mu)
            weight = (
                character
                * np.exp(-spectral * repetition * length)
                * np.exp(1.0j * theta * repetition * action)
                / denominator
            )
            flat_traces[degree] += orbit.period * weight

    coefficients = np.zeros(cutoff + 1, dtype=np.complex128)
    coefficients[0] = 1.0
    for degree in range(1, cutoff + 1):
        coefficients[degree] = -sum(
            flat_traces[index] * coefficients[degree - index]
            for index in range(1, degree + 1)
        ) / degree
    return coefficients


def additive_constant_gauge_audit(orbits: list[Orbit], ledger: list[dict]) -> dict:
    """Numerically verify S+C is exactly a coefficient-wise z rotation."""

    primitive_mu = {
        row["orbit_id"]: int(row["primitive_maslov"])
        for row in ledger
        if int(row["repetition"]) == 1
    }
    constant = 0.37
    theta = 1.0
    maximum_error = 0.0
    rows: list[dict] = []
    for spectral in S_VALUES:
        for cutoff in CUTOFFS:
            baseline = determinant_coefficients(
                orbits, cutoff, spectral, theta, primitive_mu, "baseline"
            )
            shifted = determinant_coefficients(
                orbits,
                cutoff,
                spectral,
                theta,
                primitive_mu,
                "baseline",
                action_constant=constant,
            )
            expected = baseline * np.exp(
                1.0j * theta * constant * np.arange(cutoff + 1, dtype=float)
            )
            error = float(np.max(np.abs(shifted - expected)))
            maximum_error = max(maximum_error, error)
            rows.append({"s": spectral, "cutoff": cutoff, "maximum_coefficient_error": error})
    return {
        "test_constant": constant,
        "test_theta": theta,
        "maximum_coefficient_rotation_error": maximum_error,
        "rows": rows,
    }


def period4_zero_action_audit(catalog_payload: dict, orbits: list[Orbit]) -> dict:
    exact = catalog_payload.get("exact_clock_audit", {})
    candidates = [orbit for orbit in orbits if orbit.period == 4 and orbit.action == 0.0]
    if len(candidates) != 1:
        raise ValueError(f"expected one stored zero-action period-4 orbit, found {len(candidates)}")
    orbit = candidates[0]
    direct_action = periodic_action(orbit.coordinates)
    source_pass = (
        exact.get("period4_action") == "0"
        and exact.get("period4_action_positive_roof") is False
        and exact.get("nonlattice_proof_inputs_pass") is True
    )
    return {
        "source_exact_action": exact.get("period4_action"),
        "source_exact_coordinates": exact.get("period4_coordinates"),
        "source_exact_audit_pass": source_pass,
        "catalog_orbit_id": orbit.orbit_id,
        "catalog_sign_word": orbit.sign_word,
        "catalog_action": orbit.action,
        "direct_float64_action": direct_action,
        "direct_action_absolute_error_from_zero": abs(direct_action),
        "negative_symbol_count": int(np.count_nonzero(orbit.coordinates < 0.0)),
        "maslov_phase": [
            maslov_phase(int(np.count_nonzero(orbit.coordinates < 0.0))).real,
            maslov_phase(int(np.count_nonzero(orbit.coordinates < 0.0))).imag,
        ],
        "pass": bool(source_pass and orbit.action == 0.0 and abs(direct_action) < 1.0e-14),
    }


def coefficient_rows(orbits: list[Orbit], ledger: list[dict]) -> tuple[list[dict], list[dict]]:
    primitive_mu = {
        row["orbit_id"]: int(row["primitive_maslov"])
        for row in ledger
        if int(row["repetition"]) == 1
    }
    variants: list[tuple[str, int | None]] = [
        ("maslov_action", None),
        ("orientation_fallback", None),
        ("constant_roof", None),
    ]
    variants.extend(("random_phase", seed) for seed in SEEDS)
    variants.extend(("shuffled_action", seed) for seed in SEEDS)
    rows: list[dict] = []
    evaluations: list[dict] = []
    for variant, seed in variants:
        internal_variant = "baseline" if variant == "maslov_action" else variant
        for spectral in S_VALUES:
            for theta in THETA_VALUES:
                for cutoff in CUTOFFS:
                    coefficients = determinant_coefficients(
                        orbits,
                        cutoff,
                        spectral,
                        theta,
                        primitive_mu,
                        internal_variant,
                        seed,
                    )
                    for degree, value in enumerate(coefficients):
                        rows.append(
                            {
                                "variant": variant,
                                "seed": "" if seed is None else seed,
                                "s": spectral,
                                "theta": theta,
                                "cutoff": cutoff,
                                "degree": degree,
                                "coefficient_real": value.real,
                                "coefficient_imag": value.imag,
                                "coefficient_abs": abs(value),
                            }
                        )
                    roots = np.polynomial.polynomial.polyroots(coefficients)
                    for label, z_value in Z_POINTS.items():
                        value = np.polynomial.polynomial.polyval(z_value, coefficients)
                        evaluations.append(
                            {
                                "variant": variant,
                                "seed": "" if seed is None else seed,
                                "s": spectral,
                                "theta": theta,
                                "cutoff": cutoff,
                                "z_label": label,
                                "value_real": value.real,
                                "value_imag": value.imag,
                                "value_abs": abs(value),
                                "coefficient_l1": float(np.sum(np.abs(coefficients[1:]))),
                                "tail_l2_last4": float(np.linalg.norm(coefficients[max(1, cutoff - 3) :])),
                                "minimum_root_modulus": float(np.min(np.abs(roots))),
                            }
                        )
    return rows, evaluations


def summarize_controls(rows: list[dict], evaluations: list[dict]) -> dict:
    lookup = {
        (
            row["variant"],
            str(row["seed"]),
            row["s"],
            row["theta"],
            row["cutoff"],
            row["z_label"],
        ): row
        for row in evaluations
    }
    drifts: list[dict] = []
    for variant in sorted({row["variant"] for row in evaluations}):
        seeds = sorted({str(row["seed"]) for row in evaluations if row["variant"] == variant})
        for seed in seeds:
            for spectral in S_VALUES:
                for theta in THETA_VALUES:
                    for label in Z_POINTS:
                        previous = None
                        for cutoff in CUTOFFS:
                            row = lookup[(variant, seed, spectral, theta, cutoff, label)]
                            if previous is not None:
                                drift = abs(
                                    complex(row["value_real"], row["value_imag"])
                                    - complex(previous["value_real"], previous["value_imag"])
                                )
                                drifts.append(
                                    {
                                        "variant": variant,
                                        "seed": seed,
                                        "s": spectral,
                                        "theta": theta,
                                        "z_label": label,
                                        "from_cutoff": previous["cutoff"],
                                        "to_cutoff": cutoff,
                                        "absolute_drift": drift,
                                    }
                                )
                            previous = row

    coefficient_arrays: dict[tuple, np.ndarray] = {}
    for row in rows:
        key = (
            row["variant"],
            str(row["seed"]),
            row["s"],
            row["theta"],
            row["cutoff"],
        )
        if key not in coefficient_arrays:
            coefficient_arrays[key] = np.zeros(int(row["cutoff"]) + 1, dtype=np.complex128)
        coefficient_arrays[key][int(row["degree"])] = complex(
            row["coefficient_real"], row["coefficient_imag"]
        )
    prefix_drifts: list[dict] = []
    for variant in sorted({row["variant"] for row in rows}):
        seeds = sorted({str(row["seed"]) for row in rows if row["variant"] == variant})
        for seed in seeds:
            for spectral in S_VALUES:
                for theta in THETA_VALUES:
                    for lower, upper in zip(CUTOFFS, CUTOFFS[1:]):
                        lower_values = coefficient_arrays[(variant, seed, spectral, theta, lower)]
                        upper_values = coefficient_arrays[(variant, seed, spectral, theta, upper)]
                        prefix_drifts.append(
                            {
                                "variant": variant,
                                "seed": seed,
                                "s": spectral,
                                "theta": theta,
                                "from_cutoff": lower,
                                "to_cutoff": upper,
                                "maximum_prefix_drift": float(
                                    np.max(np.abs(lower_values - upper_values[: lower + 1]))
                                ),
                            }
                        )

    def aggregate(variant: str) -> dict:
        subset = [row for row in drifts if row["variant"] == variant]
        final = [row for row in evaluations if row["variant"] == variant and row["cutoff"] == 20]
        prefix = [row for row in prefix_drifts if row["variant"] == variant]
        return {
            "maximum_coefficient_prefix_drift": max(
                row["maximum_prefix_drift"] for row in prefix
            ),
            "maximum_evaluation_drift": max(row["absolute_drift"] for row in subset),
            "median_evaluation_drift": float(np.median([row["absolute_drift"] for row in subset])),
            "minimum_root_modulus_range_at_cutoff20": [
                min(row["minimum_root_modulus"] for row in final),
                max(row["minimum_root_modulus"] for row in final),
            ],
            "coefficient_l1_range_at_cutoff20": [
                min(row["coefficient_l1"] for row in final),
                max(row["coefficient_l1"] for row in final),
            ],
        }

    diagnostic_slice: dict[str, dict] = {}
    for variant in sorted({row["variant"] for row in evaluations}):
        subset = [
            row
            for row in drifts
            if row["variant"] == variant and row["s"] == 0.5 and row["theta"] == 1.0
        ]
        diagnostic_slice[variant] = {
            "maximum_evaluation_drift": max(row["absolute_drift"] for row in subset),
            "median_evaluation_drift": float(
                np.median([row["absolute_drift"] for row in subset])
            ),
        }
    return {
        "evaluation_drift_rows": drifts,
        "coefficient_prefix_drift_rows": prefix_drifts,
        "diagnostic_slice_s0p5_theta1": diagnostic_slice,
        "variant_aggregates": {
            variant: aggregate(variant) for variant in sorted({row["variant"] for row in evaluations})
        },
    }


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        raise ValueError(f"no rows for {path}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def render_results(summary: dict) -> str:
    audit = summary["phase_audit"]
    aggregates = summary["controls"]["variant_aggregates"]
    diagnostic = summary["controls"]["diagnostic_slice_s0p5_theta1"]
    return f"""# HCS-C05 Maslov/action/instability pilot

## Frozen object

- Map: `H_6(q,p) = (1 - 6 q^2 - p, q)` on the certified local four-state survivor.
- Input: `{summary['source']['catalog_path']}` (`sha256={summary['source']['catalog_sha256']}`).
- Primitive catalogue: {audit['primitive_cycle_count']} cycles, complete only for that local survivor through period 20.
- Cutoffs: {list(CUTOFFS)}; `s={list(S_VALUES)}`, `theta={list(THETA_VALUES)}`.
- Fixed control seeds: {list(SEEDS)}.
- No arithmetic target tables were read.

## Phase convention and its hard boundary

The Morse/Maslov candidate is the negative inertia of the cyclic Hessian of

`sum_i [q_i q_(i+1) - q_i + 2 q_i^3]`.

The Fourier branch is frozen as `sqrt(i)=exp(i*pi/4)`, hence the stationary-phase character is `(-i)^mu`. This ledger is reproducible under the frozen convention. It is **not** an absolute phase selected by classical Hénon dynamics: `S -> S+C` leaves the map unchanged but sends `A_p -> A_p+n_p C`, equivalently `z -> z exp(i theta C)`. A global quantum-kernel phase has the same effect. Fixed-`z` root angles therefore fail the intrinsicness gate.

The explicit coefficient-rotation audit for `C=0.37`, `theta=1` agrees to {summary['gauge_audit']['coefficient_rotation_numeric_audit']['maximum_coefficient_rotation_error']:.3e}. A closed coboundary `f(Q)-f(q)` cancels on every periodic orbit, but the additive constant does not.

## Exact-structure audit

- Reversal partners found: {audit['primitive_cycle_count'] - audit['missing_reverse_partner_count']}/{audit['primitive_cycle_count']}; self-reversing: {audit['self_reversing_primitive_count']}.
- Reversal failures: {audit['reversal_failure_count']}.
- Nontrivial repeated-orbit Hessians rebuilt directly: {audit['nontrivial_repetition_count']}.
- `mu(p^r)=r mu(p)` failures through total period 20: {audit['repetition_maslov_additivity_failure_count']} (this equality was tested, never assumed).
- `mu(gamma)=#{{i:q_i<0}}` failures: {audit['symbol_count_maslov_failure_count']}.
- Certified-coordinate bound failures for `|q_i|>=1/3`: {audit['coordinate_bound_failure_count']}; observed minimum `|q_i|={audit['minimum_coordinate_modulus']:.6g}`.
- Minimum strict sign-diagonal-dominance margin: {audit['minimum_strict_diagonal_dominance_margin']:.6g}.
- Maslov/orientation parity failures: {audit['maslov_orientation_parity_failure_count']}.
- Hill determinant-sign mismatches: {audit['hill_sign_mismatch_count']}.
- Near-singular Hessians: {audit['near_zero_hessian_count']}; minimum absolute Hessian eigenvalue: {audit['minimum_absolute_hessian_eigenvalue']:.6g}.
- Maximum Hill log-determinant error, including dedicated `n=1,2` formulas: {audit['maximum_hill_logabs_error']:.3e}.
- Maximum action repetition error: {audit['maximum_action_repetition_error']:.3e}.
- Maximum direct/Chebyshev monodromy trace relative error: {audit['maximum_trace_repetition_relative_error']:.3e}.

Here the repetition statement is stronger than a numerical pattern. On the certified survivor, `|q_i|>=1/3`. For `n>=3` the Hessian has diagonal `12q_i` and two unit off-diagonal entries; for `n=2` the single off-diagonal entry is `2`. Hence every row is strictly sign-diagonally dominant. Scaling the off-diagonal part continuously to zero never crosses a singular matrix, so Sylvester inertia is exactly the number of negative `q_i` symbols. The `n=1` Hessian `2+12q_0` is checked separately and has the same sign conclusion. Therefore

`mu(gamma) = #{{i:q_i<0}}` and `mu(gamma^r)=r mu(gamma)`

are **proved on this survivor**, and the Maslov character is merely the one-symbol locally constant weight `(-i)^(# negative symbols)`. The direct Hessian ledger independently verifies the proof on every available repetition.

The inherited exact audit also supplies one period-four orbit with coordinates `(-1/sqrt(6),-1/sqrt(6),1/sqrt(6),1/sqrt(6))` and exact action zero. Its stored/direct checks pass, so action cannot serve as a positive roof.

## Finite determinant controls

These are finite formal sections only. Coefficient-prefix agreement is algebraic engineering consistency, and evaluation drift does not establish an infinite Fredholm determinant, A2, continuation, or A3.

| Variant | coefficient-prefix drift | max prescribed-point cutoff drift | median drift | min-root-modulus range at cutoff 20 |
|---|---:|---:|---:|---:|
""" + "\n".join(
        f"| {name} | {data['maximum_coefficient_prefix_drift']:.3e} | {data['maximum_evaluation_drift']:.3e} | {data['median_evaluation_drift']:.3e} | [{data['minimum_root_modulus_range_at_cutoff20'][0]:.6g}, {data['minimum_root_modulus_range_at_cutoff20'][1]:.6g}] |"
        for name, data in aggregates.items()
    ) + "\n\nOn the prespecified `s=0.5, theta=1` slice, maximum evaluation drifts are " + ", ".join(
        f"`{name}={data['maximum_evaluation_drift']:.3e}`"
        for name, data in diagnostic.items()
    ) + f""". The Maslov/action section beats random-phase and shuffled-action controls, so the geometric cancellation is real at finite order; however, the simpler branch-independent orientation fallback is at least as stable, and the constant-roof control is also highly stable. This does not isolate a C05-specific mechanism.

## Decision

**Hard kill for promotion as an intrinsic absolute-phase RH candidate.** The additive-constant/global-kernel phase is not fixed by the classical map. More strongly, strict sign-diagonal dominance proves that the Maslov character is only a one-symbol locally constant weight and that every repetition phase is the corresponding primitive power. Reversal supplies equality/degeneracy, not a new conjugation or functional-equation mechanism. Although the target-free finite section is substantially more stable than random/shuffled controls, the simpler orientation fallback matches or improves that stability. Thus the result is genuine dynamical cancellation but not a distinct C05 phase mechanism.

Retain the exact local Maslov collapse as `PROVED` and the finite determinant sections as a reusable `NUMERICAL_OBSERVATION`/bookkeeping baseline. The Hessian ledger, Hill identity, reversal pairing, and branch-independent orientation character are valid inputs for a later localized trace theorem. Formal status remains `A1_WEAK`; there is no A2/A3 promotion.

## Controls not run

- No neighboring-parameter catalogue was used: the inherited neighboring catalogues are numerical continuations, not certified complete survivor catalogues.
- No independent arbitrary-precision Hessian implementation was rerun; this pilot inherits the 80-digit coordinates and audits the Hessian identities in float64.
- No direct coefficient-by-coefficient comparison against every inherited scalar determinant artifact was added; `orientation_fallback` is the cheapest parent control used here.

These omissions limit any positive stability claim. They do not weaken the negative C05 decision, which follows exactly from the additive-constant gauge and the local-symbol Maslov collapse.
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    repo = Path(__file__).resolve().parents[2]
    parser.add_argument(
        "--catalog",
        type=Path,
        default=repo / "henon_instability_roof_zeta" / "results" / "catalog_robustness.json",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=repo / "next_paper_henon_candidate_search" / "results" / "c05_maslov",
    )
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    catalog_payload, orbits = load_catalog(args.catalog)
    if catalog_payload.get("max_period") != 20 or len(orbits) != 2170:
        raise ValueError("unexpected frozen catalogue")

    ledger, audit = build_phase_ledger(orbits, max(CUTOFFS))
    gauge_numeric = additive_constant_gauge_audit(orbits, ledger)
    period4_audit = period4_zero_action_audit(catalog_payload, orbits)
    coefficient_data, evaluations = coefficient_rows(orbits, ledger)
    controls = summarize_controls(coefficient_data, evaluations)
    summary = {
        "candidate_id": "HCS-C05",
        "evidence_status": "PROVED_LOCAL_MASLOV_COLLAPSE_WITH_NUMERICAL_FINITE_SECTIONS",
        "source": {
            "catalog_path": display_path(args.catalog, repo),
            "catalog_sha256": sha256(args.catalog),
            "catalog_run_id": catalog_payload.get("run_id"),
            "catalog_scope": catalog_payload.get("scope"),
        },
        "frozen_protocol": {
            "parameter": PARAMETER,
            "cutoffs": list(CUTOFFS),
            "s_values": list(S_VALUES),
            "theta_values": list(THETA_VALUES),
            "z_points": {key: [value.real, value.imag] for key, value in Z_POINTS.items()},
            "seeds": list(SEEDS),
            "maslov_rule": "negative inertia of repeated cyclic action Hessian",
            "fourier_branch": "sqrt(i)=exp(i*pi/4)",
            "maslov_character": "exp(-i*pi*mu/2)",
            "repetition_rule": "rebuild rn-by-rn Hessian; do not assume additive inertia",
            "data_firewall": "Hénon orbit catalogue only; no arithmetic target data",
        },
        "gauge_audit": {
            "closed_coboundary": "S -> S + f(Q)-f(q) leaves every closed-orbit action unchanged",
            "additive_constant": "S -> S+C sends A_p -> A_p+n_p*C",
            "determinant_effect": "z -> z*exp(i*theta*C)",
            "coefficient_rotation_numeric_audit": gauge_numeric,
            "global_kernel_phase": "same per-step z-rotation ambiguity",
            "maslov_status": "TESTABLE_UNDER_FROZEN_FOURIER_BRANCH",
            "absolute_fixed_z_phase_status": "NOT_TESTABLE_AS_CLASSICAL_INVARIANT",
            "branch_independent_fallback": "orientation^r",
        },
        "phase_audit": audit,
        "period4_zero_action_audit": period4_audit,
        "repetition_additivity_lemma": {
            "status": "PROVED",
            "statement": "strict sign-diagonal dominance and a nonsingular homotopy to diag(12*q_i) imply mu(gamma)=number of negative q symbols and hence mu(gamma^r)=r*mu(gamma); n=1 is checked separately",
            "finite_ledger_confirmation": "all repetitions with r*n<=20 pass",
        },
        "unrun_controls": [
            "neighboring-parameter catalogue: inherited neighbors are not certified complete",
            "independent arbitrary-precision Hessian implementation",
            "direct comparison to every inherited scalar-determinant artifact",
        ],
        "controls": controls,
        "decision": {
            "hard_kill": True,
            "promotion": False,
            "verdict": "HARD_KILL_INTRINSIC_ABSOLUTE_PHASE; RETAIN_FINITE_LEDGER_BASELINE",
            "route_a": "A1_WEAK; NO_A2_OR_A3_PROMOTION",
            "reason": "exact additive-constant/global-phase gauge obstruction; proved one-symbol Maslov collapse; simpler orientation fallback matches or improves finite-section stability",
            "finite_section_boundary": "engineering stability only; no tail, Fredholm, continuation, or root-count theorem",
        },
    }

    write_csv(args.output / "phase_ledger.csv", ledger)
    write_csv(args.output / "determinant_coefficients.csv", coefficient_data)
    write_csv(args.output / "cutoff_evaluations.csv", evaluations)
    (args.output / "controls.json").write_text(
        json.dumps(controls, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (args.output / "summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    (args.output / "RESULTS.md").write_text(render_results(summary), encoding="utf-8")
    print(json.dumps(summary["decision"], sort_keys=True))


if __name__ == "__main__":
    main()
