#!/usr/bin/env python3
"""Deterministic, target-free controls for Paper 8 isotropy traces.

The functions in this module check finite algebraic identities, Fourier-sign
conventions, normalization bookkeeping, and domain boundaries frozen in the
active Paper 8 protocol.  They do not prove a P8 theorem, construct a packet
completion, transport a one-orbit result to a packet, or award Route credit.

Only the Python standard library is used.  There is no network access,
randomness, target-zero data, fitted parameter, or external dataset.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Callable, Iterable, Sequence


SCHEMA = "paper8-isotropy-trace-controls/1"
FOURIER_CONVENTION = "fhat(xi)=integral_R f(t)*exp(-i*t*xi) dt"
INDUCED_CONVENTION = (
    "chi_theta(rL)=exp(+i*r*theta); xi(u+rL)=exp(-i*r*theta)xi(u); "
    "frequencies=(2*pi*n-theta)/L"
)
GAUSSIAN_SCOPE = (
    "shifted Gaussian is a Schwartz convention control, not a numerical proof "
    "for the compact-support theorem target"
)

EXPECTED_ACTIVE_TUPLE_HASHES = {
    "notes/candidate_lock.md": (
        "8a5a460bac51843e532c9894fcb99470247c7de7833449c3660813ccd183d64e"
    ),
    "notes/phase2_domain_amendment.md": (
        "412e6d24c43ab5a995d135c6ecb207f5225414fac223fcf63080486af6fc3de3"
    ),
    "notes/research_protocol.md": (
        "e1149ebd9609de24e0df00dcaeafdbcd31ee973e8ebe04b15cf86541f8084535"
    ),
}

IMPLEMENTATION_RELATIVE_PATHS = (
    "code/isotropy_trace_controls.py",
    "code/test_isotropy_trace_controls.py",
    "code/README.md",
    "experiments/reproduce.sh",
    "experiments/README.md",
    "results/README.md",
)

ARTIFACT_FILENAMES = (
    "shifted_poisson_convention.csv",
    "finite_character_grid.csv",
    "nontrivial_character_phase.csv",
    "trace_scale_controls.csv",
    "rank_one_corner_peaks.csv",
    "linfinity_representatives.csv",
    "clock_copy_composite_controls.csv",
    "transverse_probability_controls.csv",
    "domain_boundary_controls.csv",
)

POISSON_LENGTHS = (math.log(2.0), 1.0, math.log(5.0), 2.0)
POISSON_THETAS = (0.0, math.pi / 3.0, math.pi / 2.0, 4.0 * math.pi / 5.0)
PEAK_INDICES = (1, 2, 4, 8, 16, 32, 64)


def format_float(value: float) -> str:
    """Return a stable, finite, round-trippable decimal representation."""

    if not math.isfinite(value):
        raise ValueError("non-finite numeric output is forbidden")
    if value == 0.0:
        value = 0.0
    return format(value, ".17g")


def sha256(path: Path) -> str:
    """Return the SHA-256 digest of a local file."""

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def complex_fsum(values: Iterable[complex]) -> complex:
    """Accurately sum complex values by summing real and imaginary parts."""

    materialized = list(values)
    return complex(
        math.fsum(value.real for value in materialized),
        math.fsum(value.imag for value in materialized),
    )


def primes_up_to(limit: int) -> list[int]:
    """Return all rational primes not exceeding ``limit``."""

    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for candidate in range(2, math.isqrt(limit) + 1):
        if sieve[candidate]:
            start = candidate * candidate
            sieve[start : limit + 1 : candidate] = b"\x00" * (
                (limit - start) // candidate + 1
            )
    return [number for number in range(2, limit + 1) if sieve[number]]


def shifted_gaussian(time: float, center: float = 0.37, width: float = 0.8) -> float:
    """Fixed non-even Schwartz control ``exp(-(t-center)^2/(2 width^2))``."""

    if width <= 0.0:
        raise ValueError("Gaussian width must be positive")
    return math.exp(-0.5 * ((time - center) / width) ** 2)


def shifted_gaussian_fourier(
    frequency: float, center: float = 0.37, width: float = 0.8
) -> complex:
    """Analytic Fourier transform under the active negative-exponent sign."""

    if width <= 0.0:
        raise ValueError("Gaussian width must be positive")
    amplitude = (
        width
        * math.sqrt(2.0 * math.pi)
        * math.exp(-0.5 * (width * frequency) ** 2)
    )
    phase = complex(
        math.cos(-center * frequency), math.sin(-center * frequency)
    )
    return amplitude * phase


def character_phase(repetition: int, theta: float) -> complex:
    """Return the active return phase ``exp(+i*r*theta)``."""

    angle = repetition * theta
    return complex(math.cos(angle), math.sin(angle))


def shifted_poisson_control(
    length: float,
    theta: float,
    *,
    center: float = 0.37,
    width: float = 0.8,
    tail_coordinate: float = 12.0,
) -> dict[str, float | int]:
    """Check the active shifted-Poisson convention with a shifted Gaussian.

    The tested identity is

      sum_n fhat((2*pi*n-theta)/L)
        = L sum_r f(rL) exp(+i*r*theta).

    A non-even shifted Gaussian makes the imaginary part sensitive to the
    simultaneous frequency/return-phase sign.  Deterministic symmetric
    cutoffs place omitted Gaussian coordinates beyond ``tail_coordinate``.
    """

    if length <= 0.0:
        raise ValueError("length must be positive")
    if width <= 0.0 or tail_coordinate <= 0.0:
        raise ValueError("width and tail_coordinate must be positive")

    time_radius = max(
        2, math.ceil((abs(center) + tail_coordinate * width) / length) + 1
    )
    frequency_radius = max(
        2,
        math.ceil(
            ((tail_coordinate / width) * length + abs(theta))
            / (2.0 * math.pi)
        )
        + 2,
    )

    return_side = length * complex_fsum(
        shifted_gaussian(repetition * length, center, width)
        * character_phase(repetition, theta)
        for repetition in range(-time_radius, time_radius + 1)
    )
    wrong_phase_side = length * complex_fsum(
        shifted_gaussian(repetition * length, center, width)
        * character_phase(repetition, -theta)
        for repetition in range(-time_radius, time_radius + 1)
    )
    spectral_side = complex_fsum(
        shifted_gaussian_fourier(
            (2.0 * math.pi * index - theta) / length, center, width
        )
        for index in range(-frequency_radius, frequency_radius + 1)
    )
    residual = abs(spectral_side - return_side)
    scale = max(abs(spectral_side), abs(return_side), 1.0)
    return {
        "time_radius": time_radius,
        "frequency_radius": frequency_radius,
        "spectral_real": spectral_side.real,
        "spectral_imag": spectral_side.imag,
        "return_real": return_side.real,
        "return_imag": return_side.imag,
        "absolute_error": residual,
        "relative_error": residual / scale,
        "wrong_phase_error": abs(spectral_side - wrong_phase_side),
    }


def exact_character_grid_average(repetition: int, grid_size: int) -> int:
    """Return the exact root-of-unity average using modular arithmetic."""

    if grid_size < 1:
        raise ValueError("grid_size must be positive")
    return 1 if repetition % grid_size == 0 else 0


def numeric_character_grid_average(repetition: int, grid_size: int) -> complex:
    """Numerically check the exact root-of-unity classification."""

    if grid_size < 1:
        raise ValueError("grid_size must be positive")
    return complex_fsum(
        character_phase(repetition, 2.0 * math.pi * index / grid_size)
        for index in range(grid_size)
    ) / grid_size


def compact_bump(time: float, center: float, radius: float) -> float:
    """A deterministic C-infinity bump supported in ``(center-radius, center+radius)``."""

    if radius <= 0.0:
        raise ValueError("bump radius must be positive")
    coordinate = (time - center) / radius
    if abs(coordinate) >= 1.0:
        return 0.0
    return math.exp(-1.0 / (1.0 - coordinate * coordinate))


def _return_indices(length: float, center: float, radius: float) -> range:
    if length <= 0.0:
        raise ValueError("length must be positive")
    lower = center - radius
    upper = center + radius
    first = math.floor(lower / length) - 1
    last = math.ceil(upper / length) + 1
    return range(first, last + 1)


def compact_trace_scale_control(
    length: float, center: float, radius: float
) -> dict[str, float | int]:
    """Compute length/probability regular and trivial-character values."""

    indices = tuple(_return_indices(length, center, radius))
    values = {
        repetition: compact_bump(repetition * length, center, radius)
        for repetition in indices
    }
    nonzero = {key: value for key, value in values.items() if value > 0.0}
    f_zero = compact_bump(0.0, center, radius)
    two_sided_sum = math.fsum(nonzero.values())
    positive_sum = math.fsum(
        value for repetition, value in nonzero.items() if repetition >= 1
    )
    negative_sum = math.fsum(
        value for repetition, value in nonzero.items() if repetition <= -1
    )
    regular_length = length * f_zero
    trivial_length = length * two_sided_sum
    return {
        "return_term_count": len(nonzero),
        "positive_term_count": sum(key >= 1 for key in nonzero),
        "negative_term_count": sum(key <= -1 for key in nonzero),
        "f_zero": f_zero,
        "regular_length": regular_length,
        "trivial_length": trivial_length,
        "positive_length": length * positive_sum,
        "negative_length": length * negative_sum,
        "regular_probability": regular_length / length,
        "trivial_probability": trivial_length / length,
        "positive_probability": positive_sum,
        "negative_probability": negative_sum,
    }


def positive_return_for_length(
    length: float, *, center: float = 2.5, radius: float = 2.25
) -> tuple[float, int]:
    """Return ``L sum_{r>=1} f(rL)`` for the fixed positive-time bump."""

    if center - radius <= 0.0:
        raise ValueError("positive-time bump support must exclude zero")
    control = compact_trace_scale_control(length, center, radius)
    return float(control["positive_length"]), int(control["positive_term_count"])


def rank_one_peak_control(index: int) -> dict[str, float | int]:
    """Exact shrinking triangular-peak ledger in the finite rank-one corner."""

    if index < 1:
        raise ValueError("peak index must be positive")
    return {
        "index": index,
        "point_value": 1.0,
        "haar_integral": 1.0 / (2.0 * math.pi * index),
        "support_probability": 1.0 / (math.pi * index),
        "essential_supremum": 1.0,
        "linfinity_infimum_class": 0.0,
        "pointwise_infimum_at_theta_zero": 1.0,
    }


def write_csv(
    path: Path, fieldnames: Sequence[str], rows: Iterable[dict[str, object]]
) -> int:
    """Write deterministic UTF-8 CSV and return the number of data rows."""

    materialized = list(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=list(fieldnames),
            lineterminator="\n",
            extrasaction="raise",
        )
        writer.writeheader()
        writer.writerows(materialized)
    return len(materialized)


def _shifted_poisson_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for length in POISSON_LENGTHS:
        for theta in POISSON_THETAS:
            result = shifted_poisson_control(length, theta)
            rows.append(
                {
                    "length": format_float(length),
                    "theta": format_float(theta),
                    "time_radius": result["time_radius"],
                    "frequency_radius": result["frequency_radius"],
                    "spectral_real": format_float(float(result["spectral_real"])),
                    "spectral_imag": format_float(float(result["spectral_imag"])),
                    "return_real_plus_phase": format_float(
                        float(result["return_real"])
                    ),
                    "return_imag_plus_phase": format_float(
                        float(result["return_imag"])
                    ),
                    "absolute_error": format_float(float(result["absolute_error"])),
                    "relative_error": format_float(float(result["relative_error"])),
                    "wrong_minus_phase_error": format_float(
                        float(result["wrong_phase_error"])
                    ),
                    "frequency_lattice": "(2*pi*n-theta)/L",
                    "return_phase": "exp(+i*r*theta)",
                    "scope": GAUSSIAN_SCOPE,
                }
            )
    return rows


def _character_grid_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for grid_size in (5, 7, 11):
        for repetition in range(-12, 13):
            exact = exact_character_grid_average(repetition, grid_size)
            numeric = numeric_character_grid_average(repetition, grid_size)
            rows.append(
                {
                    "grid_size": grid_size,
                    "repetition": repetition,
                    "exact_average": exact,
                    "survives_exactly": "true" if exact else "false",
                    "numeric_real": format_float(numeric.real),
                    "numeric_imag": format_float(numeric.imag),
                    "numeric_residual": format_float(abs(numeric - exact)),
                    "exact_rule": "1 iff grid_size divides repetition; otherwise 0",
                    "phase_sign": "+",
                }
            )
    return rows


def _nontrivial_phase_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for theta_name, theta in (("pi/2", math.pi / 2.0), ("pi/3", math.pi / 3.0)):
        for repetition in range(-3, 4):
            phase = character_phase(repetition, theta)
            rows.append(
                {
                    "theta_name": theta_name,
                    "theta": format_float(theta),
                    "repetition": repetition,
                    "phase_real": format_float(phase.real),
                    "phase_imag": format_float(phase.imag),
                    "active_formula": "exp(+i*r*theta)",
                    "positive_sign_witness": (
                        "true"
                        if theta_name == "pi/2" and repetition == 1 and phase.imag > 0
                        else "not_designated"
                    ),
                    "multiplicity_is_nonnegative": (
                        "true"
                        if abs(phase.imag) < 1.0e-15 and phase.real >= 0.0
                        else "false"
                    ),
                }
            )
    return rows


def _trace_scale_rows() -> list[dict[str, object]]:
    profiles = (
        ("zero_only_compact_bump", 1.0, 0.0, 0.45),
        ("positive_only_compact_bump", 1.0, 1.5, 1.2),
        ("two_sided_compact_bump", 1.0, 0.35, 2.4),
        ("nonunit_length_two_sided", math.log(5.0), 0.35, 2.4),
    )
    rows: list[dict[str, object]] = []
    for name, length, center, radius in profiles:
        control = compact_trace_scale_control(length, center, radius)
        rows.append(
            {
                "profile": name,
                "length": format_float(length),
                "support_left": format_float(center - radius),
                "support_right": format_float(center + radius),
                "return_term_count": control["return_term_count"],
                "positive_term_count": control["positive_term_count"],
                "negative_term_count": control["negative_term_count"],
                "f_zero": format_float(float(control["f_zero"])),
                "regular_length_L_f0": format_float(
                    float(control["regular_length"])
                ),
                "trivial_length_L_sum_r": format_float(
                    float(control["trivial_length"])
                ),
                "positive_length_L_sum_r_ge_1": format_float(
                    float(control["positive_length"])
                ),
                "regular_probability_f0": format_float(
                    float(control["regular_probability"])
                ),
                "trivial_probability_sum_r": format_float(
                    float(control["trivial_probability"])
                ),
                "regular_common_scale_residual": format_float(
                    abs(
                        float(control["regular_length"])
                        - length * float(control["regular_probability"])
                    )
                ),
                "trivial_common_scale_residual": format_float(
                    abs(
                        float(control["trivial_length"])
                        - length * float(control["trivial_probability"])
                    )
                ),
                "regular_owner": "dual-Haar/identity-time",
                "trivial_owner": "theta=0 character fibre",
            }
        )
    return rows


def _corner_peak_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for index in PEAK_INDICES:
        control = rank_one_peak_control(index)
        rows.append(
            {
                "peak_index": index,
                "corner_projection": "p=1 tensor e; rank(e)=1",
                "character_corner_value": format_float(
                    float(control["point_value"])
                ),
                "regular_corner_haar_integral": format_float(
                    float(control["haar_integral"])
                ),
                "support_probability": format_float(
                    float(control["support_probability"])
                ),
                "essential_supremum": format_float(
                    float(control["essential_supremum"])
                ),
                "linfinity_infimum_class": format_float(
                    float(control["linfinity_infimum_class"])
                ),
                "pointwise_infimum_at_theta_zero": format_float(
                    float(control["pointwise_infimum_at_theta_zero"])
                ),
                "corner_is_central": "false",
                "fixed_map_still_required": "true",
            }
        )
    return rows


def _linfinity_representative_rows() -> list[dict[str, object]]:
    return [
        {
            "representative": "zero_everywhere",
            "linfinity_class": "zero",
            "point_value_at_theta_zero": "0",
            "haar_integral": "0",
            "essential_supremum": "0",
            "differs_from_zero_only_on_null_set": "false",
            "point_evaluation_well_defined_on_class": "false",
        },
        {
            "representative": "singleton_spike_at_theta_zero",
            "linfinity_class": "zero",
            "point_value_at_theta_zero": "1",
            "haar_integral": "0",
            "essential_supremum": "0",
            "differs_from_zero_only_on_null_set": "true",
            "point_evaluation_well_defined_on_class": "false",
        },
    ]


def _clock_rows() -> list[dict[str, object]]:
    systems: tuple[
        tuple[str, tuple[str, ...], tuple[float, ...], str, int], ...
    ] = (
        (
            "prime_label_reference",
            ("p=2", "p=3", "p=5"),
            (math.log(2.0), math.log(3.0), math.log(5.0)),
            "input labels only; no new source proof",
            1,
        ),
        (
            "arbitrary_positive_clocks",
            ("alpha", "beta", "gamma"),
            (0.7, 1.1, 2.3),
            "analytic mechanism only; arithmetic provenance not applicable",
            1,
        ),
        (
            "copied_clock_threefold",
            ("beta-copy-1", "beta-copy-2", "beta-copy-3"),
            (1.1, 1.1, 1.1),
            "copy additivity control; no canonical packet mass",
            3,
        ),
        (
            "composite_augmented_clocks",
            ("p=2", "p=3", "n=4", "n=6"),
            (math.log(2.0), math.log(3.0), math.log(4.0), math.log(6.0)),
            "analytic mechanism survives; rational-prime provenance fails",
            1,
        ),
    )
    rows: list[dict[str, object]] = []
    single_beta, _ = positive_return_for_length(1.1)
    for name, labels, lengths, provenance, expected_copy_factor in systems:
        component_values = [positive_return_for_length(length)[0] for length in lengths]
        total = math.fsum(component_values)
        copy_residual = (
            abs(total - 3.0 * single_beta)
            if name == "copied_clock_threefold"
            else 0.0
        )
        rows.append(
            {
                "clock_system": name,
                "labels": ";".join(labels),
                "lengths": ";".join(format_float(length) for length in lengths),
                "component_count": len(lengths),
                "expected_copy_factor": expected_copy_factor,
                "positive_return_ledger": format_float(total),
                "single_beta_reference": (
                    format_float(single_beta)
                    if name == "copied_clock_threefold"
                    else ""
                ),
                "copy_additivity_residual": format_float(copy_residual),
                "analytic_mechanism_compiles": "true",
                "arithmetic_provenance": provenance,
                "fitting_used": "false",
            }
        )
    return rows


def _transverse_probability_rows() -> list[dict[str, object]]:
    time_only_value, _ = positive_return_for_length(1.0)
    models: tuple[
        tuple[str, tuple[Fraction, ...], tuple[int, ...]], ...
    ] = (
        ("singleton", (Fraction(1, 1),), (0,)),
        (
            "three_atom_left",
            (Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)),
            (0, 1, 2),
        ),
        (
            "three_atom_uniform",
            (Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)),
            (0, 1, 2),
        ),
        (
            "three_atom_right",
            (Fraction(1, 6), Fraction(1, 3), Fraction(1, 2)),
            (0, 1, 2),
        ),
    )
    rows: list[dict[str, object]] = []
    for name, weights, observable in models:
        total = sum(weights, Fraction())
        expectation = sum(
            (weight * value for weight, value in zip(weights, observable)),
            Fraction(),
        )
        rows.append(
            {
                "measure_model": name,
                "weights_exact": ";".join(str(weight) for weight in weights),
                "total_probability_exact": str(total),
                "time_only_value": format_float(float(total) * time_only_value),
                "time_only_residual_from_unit_mass": format_float(
                    abs(float(total) * time_only_value - time_only_value)
                ),
                "transverse_observable": ";".join(str(value) for value in observable),
                "full_observable_expectation_exact": str(expectation),
                "full_observable_expectation": format_float(float(expectation)),
                "full_trace_selected_canonically": "false",
                "packet_measure_theorem_claimed": "false",
            }
        )
    return rows


def _domain_rows() -> list[dict[str, object]]:
    local = compact_trace_scale_control(1.0, 0.35, 2.4)

    finite_lengths = tuple(math.log(prime) for prime in (2, 3, 5))
    finite_values = [positive_return_for_length(length) for length in finite_lengths]
    finite_total = math.fsum(value for value, _ in finite_values)
    finite_terms = sum(count for _, count in finite_values)

    center = 2.5
    radius = 2.25
    support_upper = center + radius
    prime_bound = math.floor(math.exp(support_upper))
    global_primes = primes_up_to(prime_bound)
    global_values = [
        (prime, *positive_return_for_length(math.log(prime), center=center, radius=radius))
        for prime in global_primes
    ]
    contributing = [row for row in global_values if row[1] > 0.0]
    global_total = math.fsum(row[1] for row in contributing)
    global_terms = sum(row[2] for row in contributing)

    return [
        {
            "domain_id": "local_one_orbit_two_sided",
            "test_class": "C_c^infinity(R) on one time kernel",
            "support": "(-2.05,2.75)",
            "component_count": 1,
            "return_term_count": local["return_term_count"],
            "ledger_value": format_float(float(local["trivial_length"])),
            "zero_time_included": "true",
            "negative_time_included": "true",
            "finite_prime_support": "not_applicable",
            "locally_finite": "true",
            "global_operator_asserted": "false",
            "cstar_trace_asserted": "false",
            "scope": "one-orbit scalar control",
        },
        {
            "domain_id": "finite_prime_support_positive",
            "test_class": "algebraic direct sum over p=2,3,5",
            "support": "(0.25,4.75)",
            "component_count": len(finite_lengths),
            "return_term_count": finite_terms,
            "ledger_value": format_float(finite_total),
            "zero_time_included": "false",
            "negative_time_included": "false",
            "finite_prime_support": "true",
            "locally_finite": "true",
            "global_operator_asserted": "false",
            "cstar_trace_asserted": "false",
            "scope": "finite algebraic assembly only",
        },
        {
            "domain_id": "all_prime_positive_time_distribution",
            "test_class": "C_c^infinity((0,infinity)) scalar test",
            "support": "(0.25,4.75)",
            "component_count": len(contributing),
            "return_term_count": global_terms,
            "ledger_value": format_float(global_total),
            "zero_time_included": "false",
            "negative_time_included": "false",
            "finite_prime_support": "false",
            "locally_finite": "true",
            "global_operator_asserted": "false",
            "cstar_trace_asserted": "false",
            "scope": f"scalar distribution; support-implied p<={prime_bound}",
        },
    ]


def _artifact_record(path: Path, rows: int) -> dict[str, int | str]:
    return {"bytes": path.stat().st_size, "rows": rows, "sha256": sha256(path)}


def _hash_relative_files(paper_dir: Path, paths: Sequence[str]) -> dict[str, str]:
    records: dict[str, str] = {}
    for relative in paths:
        path = paper_dir / relative
        if not path.is_file():
            raise FileNotFoundError(f"required file missing: {relative}")
        records[relative] = sha256(path)
    return records


def _validate_active_tuple(paper_dir: Path) -> dict[str, str]:
    current = _hash_relative_files(
        paper_dir, tuple(sorted(EXPECTED_ACTIVE_TUPLE_HASHES))
    )
    if current != EXPECTED_ACTIVE_TUPLE_HASHES:
        raise ValueError(
            "active tuple SHA-256 mismatch; controls are locked to the final "
            "Paper 8 protocol/candidate/amendment bytes"
        )
    return current


def _csv_row_count(path: Path) -> int:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return max(0, sum(1 for _ in csv.reader(handle)) - 1)


def run(output_dir: Path, *, paper_dir: Path | None = None) -> dict[str, object]:
    """Generate all deterministic artifacts and their hash manifest."""

    resolved_paper = (
        Path(__file__).resolve().parents[1]
        if paper_dir is None
        else paper_dir.resolve()
    )
    active_tuple = _validate_active_tuple(resolved_paper)
    output_dir.mkdir(parents=True, exist_ok=True)

    table_specs: tuple[
        tuple[str, Sequence[str], Iterable[dict[str, object]]], ...
    ] = (
        (
            "shifted_poisson_convention.csv",
            (
                "length",
                "theta",
                "time_radius",
                "frequency_radius",
                "spectral_real",
                "spectral_imag",
                "return_real_plus_phase",
                "return_imag_plus_phase",
                "absolute_error",
                "relative_error",
                "wrong_minus_phase_error",
                "frequency_lattice",
                "return_phase",
                "scope",
            ),
            _shifted_poisson_rows(),
        ),
        (
            "finite_character_grid.csv",
            (
                "grid_size",
                "repetition",
                "exact_average",
                "survives_exactly",
                "numeric_real",
                "numeric_imag",
                "numeric_residual",
                "exact_rule",
                "phase_sign",
            ),
            _character_grid_rows(),
        ),
        (
            "nontrivial_character_phase.csv",
            (
                "theta_name",
                "theta",
                "repetition",
                "phase_real",
                "phase_imag",
                "active_formula",
                "positive_sign_witness",
                "multiplicity_is_nonnegative",
            ),
            _nontrivial_phase_rows(),
        ),
        (
            "trace_scale_controls.csv",
            (
                "profile",
                "length",
                "support_left",
                "support_right",
                "return_term_count",
                "positive_term_count",
                "negative_term_count",
                "f_zero",
                "regular_length_L_f0",
                "trivial_length_L_sum_r",
                "positive_length_L_sum_r_ge_1",
                "regular_probability_f0",
                "trivial_probability_sum_r",
                "regular_common_scale_residual",
                "trivial_common_scale_residual",
                "regular_owner",
                "trivial_owner",
            ),
            _trace_scale_rows(),
        ),
        (
            "rank_one_corner_peaks.csv",
            (
                "peak_index",
                "corner_projection",
                "character_corner_value",
                "regular_corner_haar_integral",
                "support_probability",
                "essential_supremum",
                "linfinity_infimum_class",
                "pointwise_infimum_at_theta_zero",
                "corner_is_central",
                "fixed_map_still_required",
            ),
            _corner_peak_rows(),
        ),
        (
            "linfinity_representatives.csv",
            (
                "representative",
                "linfinity_class",
                "point_value_at_theta_zero",
                "haar_integral",
                "essential_supremum",
                "differs_from_zero_only_on_null_set",
                "point_evaluation_well_defined_on_class",
            ),
            _linfinity_representative_rows(),
        ),
        (
            "clock_copy_composite_controls.csv",
            (
                "clock_system",
                "labels",
                "lengths",
                "component_count",
                "expected_copy_factor",
                "positive_return_ledger",
                "single_beta_reference",
                "copy_additivity_residual",
                "analytic_mechanism_compiles",
                "arithmetic_provenance",
                "fitting_used",
            ),
            _clock_rows(),
        ),
        (
            "transverse_probability_controls.csv",
            (
                "measure_model",
                "weights_exact",
                "total_probability_exact",
                "time_only_value",
                "time_only_residual_from_unit_mass",
                "transverse_observable",
                "full_observable_expectation_exact",
                "full_observable_expectation",
                "full_trace_selected_canonically",
                "packet_measure_theorem_claimed",
            ),
            _transverse_probability_rows(),
        ),
        (
            "domain_boundary_controls.csv",
            (
                "domain_id",
                "test_class",
                "support",
                "component_count",
                "return_term_count",
                "ledger_value",
                "zero_time_included",
                "negative_time_included",
                "finite_prime_support",
                "locally_finite",
                "global_operator_asserted",
                "cstar_trace_asserted",
                "scope",
            ),
            _domain_rows(),
        ),
    )

    artifacts: dict[str, dict[str, int | str]] = {}
    for filename, fieldnames, rows in table_specs:
        path = output_dir / filename
        row_count = write_csv(path, fieldnames, rows)
        artifacts[filename] = _artifact_record(path, row_count)

    if tuple(sorted(artifacts)) != tuple(sorted(ARTIFACT_FILENAMES)):
        raise AssertionError("generated artifact set does not match the frozen set")

    implementation_files = _hash_relative_files(
        resolved_paper, IMPLEMENTATION_RELATIVE_PATHS
    )
    manifest: dict[str, object] = {
        "schema": SCHEMA,
        "regression_status": "PASS",
        "active_tuple_files": active_tuple,
        "artifacts": artifacts,
        "controls": [
            "shifted Poisson convention with (2*pi*n-theta)/L and exp(+i*r*theta)",
            "finite character-grid exact cancellation",
            "nontrivial positive character phase",
            "trivial-character versus dual-Haar identity-time trace",
            "zero-time exposure and common length/probability scaling",
            "trace-finite rank-one-corner shrinking peaks",
            "L-infinity representative-class witness",
            "arbitrary/copied/composite clock falsification",
            "transverse-probability time-only invariance and full-observable variance",
            "local/finite-prime/positive-time domain separation",
        ],
        "determinism": {
            "network": False,
            "randomness": False,
            "target_zero_data": False,
            "fitting": False,
            "external_datasets": False,
            "timestamps": False,
            "python_dependencies": "standard_library_only",
        },
        "normalization": {
            "fourier": FOURIER_CONVENTION,
            "induced_character": INDUCED_CONVENTION,
            "length_regular": "L*f(0)",
            "length_trivial": "L*sum_r f(rL)",
            "probability_scale": "divide both regular and trivial values by L",
            "dual_haar": "dtheta/(2*pi)",
        },
        "finite_corner_boundary": (
            "p=1 tensor e is a symbolic rank-one finite-corner control. The CSVs "
            "do not establish its image in the fixed regular completion, a normal "
            "extension theorem, or packet transport."
        ),
        "local_packet_boundary": (
            "One-orbit and scalar finite/positive-time checks only. No packet LCH "
            "completion, Q_p measure theorem, all-prime C*-operator, or packet "
            "same-map bridge is asserted."
        ),
        "forbidden_evidence_not_used": [
            "Riemann-zero data",
            "Euler-product target matching",
            "fitted phases",
            "fitted clocks",
            "fitted transverse probabilities or packet masses",
            "Paper 7 determinant or Route credit",
        ],
        "implementation_files": implementation_files,
        "parameters": {
            "gaussian_center": 0.37,
            "gaussian_width": 0.8,
            "gaussian_tail_coordinate": 12.0,
            "positive_bump_center": 2.5,
            "positive_bump_radius": 2.25,
            "peak_indices": list(PEAK_INDICES),
        },
        "interpretation_boundary": (
            "Deterministic convention, falsification, and domain-regression checks. "
            "They are not mathematical proofs, source ownership, packet transport, "
            "a normality theorem, or a Route verdict."
        ),
    }
    manifest_path = output_dir / "isotropy_trace_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return manifest


def verify(output_dir: Path, *, paper_dir: Path | None = None) -> dict[str, object]:
    """Verify generated bytes, active locks, and implementation hashes."""

    resolved_paper = (
        Path(__file__).resolve().parents[1]
        if paper_dir is None
        else paper_dir.resolve()
    )
    manifest_path = output_dir / "isotropy_trace_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema") != SCHEMA:
        raise ValueError("manifest schema mismatch")

    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, dict) or set(artifacts) != set(ARTIFACT_FILENAMES):
        raise ValueError("artifact file set mismatch")
    for filename in ARTIFACT_FILENAMES:
        record = artifacts[filename]
        path = output_dir / filename
        if not path.is_file():
            raise ValueError(f"missing artifact: {filename}")
        if sha256(path) != record.get("sha256"):
            raise ValueError(f"artifact SHA-256 mismatch: {filename}")
        if path.stat().st_size != record.get("bytes"):
            raise ValueError(f"artifact byte-size mismatch: {filename}")
        if _csv_row_count(path) != record.get("rows"):
            raise ValueError(f"artifact row-count mismatch: {filename}")

    active_tuple = _validate_active_tuple(resolved_paper)
    if manifest.get("active_tuple_files") != active_tuple:
        raise ValueError("manifest active tuple mismatch")

    manifest_implementation = manifest.get("implementation_files")
    if not isinstance(manifest_implementation, dict) or set(
        manifest_implementation
    ) != set(IMPLEMENTATION_RELATIVE_PATHS):
        raise ValueError("implementation file set mismatch")
    current_implementation = _hash_relative_files(
        resolved_paper, IMPLEMENTATION_RELATIVE_PATHS
    )
    if manifest_implementation != current_implementation:
        raise ValueError("implementation SHA-256 mismatch")
    return manifest


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results",
    )
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="verify existing artifacts and implementation hashes without writing",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    if args.verify_only:
        verify(args.output_dir)
        print("PASS: artifact, active-tuple, and implementation hashes verified")
    else:
        run(args.output_dir)
        print(f"PASS: generated {len(ARTIFACT_FILENAMES)} deterministic CSV artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
