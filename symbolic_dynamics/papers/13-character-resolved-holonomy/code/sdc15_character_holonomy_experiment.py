"""Deterministic experiment for the frozen SD-C15 preregistration.

The module regenerates only this paper project's ``results`` directory and
never reads, stores, or compares Riemann-zero data.
"""

from __future__ import annotations

import cmath
import csv
import hashlib
import json
import math
import random
from collections import defaultdict
from pathlib import Path
from typing import Iterable

import numpy as np


ATOM_CUTOFFS = (2, 3, 4, 8, 16, 32, 64, 128)
SOURCE_POINTS = (1.25 + 0j, 1.5 + 0j, 2.0 + 0j, 1.5 + 0.75j)
Z_POINTS = (0.15, 0.35, 0.6)
CHARACTER_COUNT = 1024
SHUFFLE_SEED = 13013
RANDOM_INVENTORY_SEED = 13014
POSITIVE_CHARGE_SEEDS = tuple(range(15000, 15032))


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2
    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2
    return True


def first_primes(count: int) -> tuple[int, ...]:
    values = []
    candidate = 2
    while len(values) < count:
        if is_prime(candidate):
            values.append(candidate)
        candidate += 1
    return tuple(values)


def first_composites(count: int) -> tuple[int, ...]:
    values = []
    candidate = 4
    while len(values) < count:
        if not is_prime(candidate):
            values.append(candidate)
        candidate += 1
    return tuple(values)


def inventory(kind: str, count: int) -> tuple[int, ...]:
    if kind == "primes":
        return first_primes(count)
    if kind == "composites":
        return first_composites(count)
    if kind == "shuffled_primes":
        values = list(first_primes(128))
        random.Random(SHUFFLE_SEED).shuffle(values)
        return tuple(values[:count])
    if kind == "random_increasing":
        values = random.Random(RANDOM_INVENTORY_SEED).sample(
            range(2, 16 * count + 2), count
        )
        return tuple(sorted(values))
    raise ValueError(kind)


def masses(values: Iterable[int], source_s: complex) -> tuple[complex, ...]:
    return tuple(complex(value) ** (-source_s) for value in values)


def endpoint_amplitudes(xs: tuple[complex, ...]) -> tuple[complex, ...]:
    return tuple((left + right) / 2 for left, right in zip(xs[:-1], xs[1:]))


def primary_charges(count: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return (1,) * (count - 1), (1,) * (count - 1)


def inverse_charges(count: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    return (1,) * (count - 1), (-1,) * (count - 1)


def positive_charge_field(count: int, seed: int) -> tuple[tuple[int, ...], tuple[int, ...]]:
    rng = random.Random(seed)
    forward = tuple(rng.randint(1, 3) for _ in range(count - 1))
    backward = tuple(rng.randint(1, 3) for _ in range(count - 1))
    return forward, backward


Polynomial = dict[int, complex]


def clean_polynomial(poly: Polynomial, tolerance: float = 0.0) -> Polynomial:
    if tolerance == 0:
        return {degree: value for degree, value in poly.items() if value != 0}
    return {degree: value for degree, value in poly.items() if abs(value) > tolerance}


def continuant_polynomial(
    xs: tuple[complex, ...],
    determinant_z: complex,
    forward: tuple[int, ...],
    backward: tuple[int, ...],
) -> Polynomial:
    """Exact-in-structure O(N degree) continuant for det(I-z L(w))."""

    count = len(xs)
    if len(forward) != count - 1 or len(backward) != count - 1:
        raise ValueError("charge field length mismatch")
    amplitudes = endpoint_amplitudes(xs)
    delta_minus_two: Polynomial = {0: 1.0 + 0j}
    delta_minus_one: Polynomial = {0: 1 - determinant_z * xs[0]}
    if count == 1:
        return delta_minus_one
    for index in range(1, count):
        diagonal = 1 - determinant_z * xs[index]
        cycle_degree = forward[index - 1] + backward[index - 1]
        cycle_factor = -(determinant_z**2) * amplitudes[index - 1] ** 2
        current: defaultdict[int, complex] = defaultdict(complex)
        for degree, coefficient in delta_minus_one.items():
            current[degree] += diagonal * coefficient
        for degree, coefficient in delta_minus_two.items():
            current[degree + cycle_degree] += cycle_factor * coefficient
        delta_minus_two, delta_minus_one = delta_minus_one, clean_polynomial(dict(current))
    return delta_minus_one


def evaluate_polynomial(poly: Polynomial, character_w: complex) -> complex:
    return sum(coefficient * character_w**degree for degree, coefficient in poly.items())


def coefficient_energy(poly: Polynomial) -> float:
    zero = poly.get(0, 0j)
    if zero == 0:
        return math.inf
    transverse = math.sqrt(
        sum(abs(coefficient) ** 2 for degree, coefficient in poly.items() if degree >= 1)
    )
    return transverse / abs(zero)


def euler_constant_coefficient(xs: tuple[complex, ...], determinant_z: complex) -> complex:
    value = 1.0 + 0j
    for x in xs:
        value *= 1 - determinant_z * x
    return value


def dense_transfer(
    xs: tuple[complex, ...],
    character_w: complex,
    forward: tuple[int, ...],
    backward: tuple[int, ...],
) -> np.ndarray:
    count = len(xs)
    matrix = np.diag(np.asarray(xs, dtype=np.complex128))
    for index, amplitude in enumerate(endpoint_amplitudes(xs)):
        matrix[index + 1, index] = amplitude * character_w ** forward[index]
        matrix[index, index + 1] = amplitude * character_w ** backward[index]
    return matrix


def dense_determinant(
    xs: tuple[complex, ...],
    determinant_z: complex,
    character_w: complex,
    forward: tuple[int, ...],
    backward: tuple[int, ...],
) -> complex:
    matrix = dense_transfer(xs, character_w, forward, backward)
    return complex(np.linalg.det(np.eye(len(xs)) - determinant_z * matrix))


def trace_log_reconstruction(
    xs: tuple[complex, ...],
    determinant_z: complex,
    character_w: complex,
    forward: tuple[int, ...],
    backward: tuple[int, ...],
    power_cutoff: int = 64,
) -> complex:
    """Truncated trace-log germ, used only where |z| rho(L)<1."""

    eigenvalues = np.linalg.eigvals(dense_transfer(xs, character_w, forward, backward))
    scaled = determinant_z * eigenvalues
    if float(np.max(np.abs(scaled))) >= 1:
        raise ValueError("trace-log reconstruction called outside convergence disk")
    log_value = 0j
    powers = np.ones_like(scaled)
    for repetition in range(1, power_cutoff + 1):
        powers *= scaled
        log_value -= np.sum(powers) / repetition
    return cmath.exp(log_value)


def dft_coefficient_residual(poly: Polynomial) -> float:
    if max(poly) >= CHARACTER_COUNT:
        raise ValueError("character grid would alias this determinant polynomial")
    samples = np.asarray(
        [
            evaluate_polynomial(poly, cmath.exp(2j * math.pi * index / CHARACTER_COUNT))
            for index in range(CHARACTER_COUNT)
        ]
    )
    recovered = np.fft.fft(samples) / CHARACTER_COUNT
    expected = np.zeros(CHARACTER_COUNT, dtype=np.complex128)
    for degree, coefficient in poly.items():
        expected[degree] = coefficient
    return float(np.max(np.abs(recovered - expected)))


def high_precision_continuant(
    values: tuple[int, ...],
    source_s: complex,
    determinant_z: float,
    theta: float,
    forward: tuple[int, ...],
    backward: tuple[int, ...],
) -> complex:
    """Selected 80-digit scalar continuant confirmation."""

    import mpmath as mp

    with mp.workdps(80):
        mp_s = mp.mpc(source_s.real, source_s.imag)
        mp_z = mp.mpf(str(determinant_z))
        mp_w = mp.e ** (mp.j * mp.mpf(str(theta)))
        xs = tuple(mp.power(value, -mp_s) for value in values)
        amplitudes = tuple((left + right) / 2 for left, right in zip(xs[:-1], xs[1:]))
        delta_minus_two = mp.mpc(1)
        delta_minus_one = 1 - mp_z * xs[0]
        for index in range(1, len(values)):
            degree = forward[index - 1] + backward[index - 1]
            current = (
                (1 - mp_z * xs[index]) * delta_minus_one
                - mp_z**2 * amplitudes[index - 1] ** 2 * mp_w**degree * delta_minus_two
            )
            delta_minus_two, delta_minus_one = delta_minus_one, current
        return complex(delta_minus_one)


def forward_dag_determinant_polynomial(
    xs: tuple[complex, ...], determinant_z: complex
) -> Polynomial:
    """Only forward arrows: the determinant is exactly triangular/Euler."""

    return {0: euler_constant_coefficient(xs, determinant_z)}


def charged_path_census(
    values: tuple[int, ...],
    max_power: int,
    forward: tuple[int, ...],
    backward: tuple[int, ...],
) -> list[dict[str, object]]:
    """Exact rational census at s=2, aggregated by r/cross-count/charge."""

    from fractions import Fraction

    xs = tuple(Fraction(1, value * value) for value in values)
    amplitudes = tuple((left + right) / 2 for left, right in zip(xs[:-1], xs[1:]))
    aggregate: defaultdict[tuple[int, int, int], Fraction] = defaultdict(Fraction)
    word_counts: defaultdict[tuple[int, int, int], int] = defaultdict(int)
    for start in range(len(values)):
        state: dict[tuple[int, int, int], tuple[Fraction, int]] = {
            (start, 0, 0): (Fraction(1), 1)
        }
        for repetition in range(1, max_power + 1):
            next_state: defaultdict[tuple[int, int, int], list[object]] = defaultdict(
                lambda: [Fraction(0), 0]
            )
            for (current, cross_count, charge), (coefficient, count) in state.items():
                loop_key = (current, cross_count, charge)
                next_state[loop_key][0] += coefficient * xs[current]
                next_state[loop_key][1] += count
                if current + 1 < len(values):
                    key = (current + 1, cross_count + 1, charge + forward[current])
                    next_state[key][0] += coefficient * amplitudes[current]
                    next_state[key][1] += count
                if current > 0:
                    key = (current - 1, cross_count + 1, charge + backward[current - 1])
                    next_state[key][0] += coefficient * amplitudes[current - 1]
                    next_state[key][1] += count
            state = {
                key: (value[0], int(value[1])) for key, value in next_state.items()
            }
            for (current, cross_count, charge), (coefficient, count) in state.items():
                if current == start:
                    aggregate[(repetition, cross_count, charge)] += coefficient
                    word_counts[(repetition, cross_count, charge)] += count
    rows = []
    for (repetition, cross_count, charge), coefficient in sorted(aggregate.items()):
        rows.append(
            {
                "N": len(values),
                "r": repetition,
                "cross_count": cross_count,
                "charge": charge,
                "pure": cross_count == 0,
                "closed_word_count": word_counts[(repetition, cross_count, charge)],
                "coefficient": str(coefficient),
            }
        )
    return rows


def gauge_residual(values: tuple[int, ...], source_s: complex, theta: float, kind: str) -> float:
    xs = masses(values, source_s)
    amplitudes = endpoint_amplitudes(xs)
    if kind == "rank":
        potentials = tuple(float(index) for index in range(len(values)))
    elif kind == "entropy":
        potentials = tuple(math.log(value) for value in values)
    else:
        raise ValueError(kind)
    baseline = dense_transfer(xs, 1 + 0j, *primary_charges(len(values)))
    # Replace the primary +1/+1 phases by the U(1) coboundary phase.
    phased = np.diag(np.asarray(xs, dtype=np.complex128))
    for index, amplitude in enumerate(amplitudes):
        phase = cmath.exp(1j * theta * (potentials[index + 1] - potentials[index]))
        phased[index + 1, index] = amplitude * phase
        phased[index, index + 1] = amplitude / phase
    gauge = np.diag(np.exp(1j * theta * np.asarray(potentials)))
    expected = gauge @ baseline @ gauge.conj().T
    return float(np.max(np.abs(phased - expected)))


def roof_shift_residual(value: int, source_s: complex, theta: float) -> float:
    left = value ** (-source_s) * cmath.exp(1j * theta * math.log(value))
    right = value ** (-(source_s - 1j * theta))
    return abs(left - right)


def character_range(poly: Polynomial) -> dict[str, float]:
    if max(poly) >= CHARACTER_COUNT:
        raise ValueError("character grid aliases the determinant polynomial")
    coefficients = np.zeros(CHARACTER_COUNT, dtype=np.complex128)
    for degree, coefficient in poly.items():
        coefficients[degree] = coefficient
    values = np.fft.ifft(coefficients) * CHARACTER_COUNT
    magnitudes = np.abs(values)
    return {
        "magnitude_min": float(np.min(magnitudes)),
        "magnitude_max": float(np.max(magnitudes)),
        "magnitude_range": float(np.max(magnitudes) - np.min(magnitudes)),
    }


def frozen_energy_rows() -> list[dict[str, object]]:
    rows = []
    for count in ATOM_CUTOFFS:
        for kind in ("primes", "composites", "shuffled_primes", "random_increasing"):
            values = inventory(kind, count)
            for source_s in SOURCE_POINTS:
                xs = masses(values, source_s)
                forward, backward = primary_charges(count)
                for determinant_z in Z_POINTS:
                    poly = continuant_polynomial(xs, determinant_z, forward, backward)
                    ranges = character_range(poly)
                    rows.append(
                        {
                            "inventory": kind,
                            "N": count,
                            "s": str(source_s),
                            "z": determinant_z,
                            "degree": max(poly),
                            "E": coefficient_energy(poly),
                            "d0_residual": abs(
                                poly.get(0, 0j)
                                - euler_constant_coefficient(xs, determinant_z)
                            ),
                            **ranges,
                        }
                    )
    return rows


def frozen_positive_charge_rows() -> list[dict[str, object]]:
    rows = []
    for count in ATOM_CUTOFFS:
        values = inventory("primes", count)
        for source_s in SOURCE_POINTS:
            xs = masses(values, source_s)
            for determinant_z in Z_POINTS:
                for seed in POSITIVE_CHARGE_SEEDS:
                    charges = positive_charge_field(count, seed)
                    poly = continuant_polynomial(xs, determinant_z, *charges)
                    ranges = character_range(poly)
                    rows.append(
                        {
                            "control_type": "positive_charge",
                            "control_id": seed,
                            "N": count,
                            "s": str(source_s),
                            "z": determinant_z,
                            "E": coefficient_energy(poly),
                            "degree": max(poly),
                            "d0_residual": abs(
                                poly.get(0, 0j)
                                - euler_constant_coefficient(xs, determinant_z)
                            ),
                            **ranges,
                        }
                    )
    return rows


def summary() -> dict[str, object]:
    count, source_s, determinant_z = 32, 1.5 + 0j, 0.35
    selectivity = {}
    for kind in ("primes", "composites", "shuffled_primes", "random_increasing"):
        values = inventory(kind, count)
        xs = masses(values, source_s)
        poly = continuant_polynomial(xs, determinant_z, *primary_charges(count))
        selectivity[kind] = {
            "E": coefficient_energy(poly),
            "degree": max(poly),
            "d0_residual": abs(
                poly.get(0, 0j) - euler_constant_coefficient(xs, determinant_z)
            ),
        }
    positive_controls = []
    prime_xs = masses(inventory("primes", count), source_s)
    for seed in POSITIVE_CHARGE_SEEDS:
        charges = positive_charge_field(count, seed)
        poly = continuant_polynomial(prime_xs, determinant_z, *charges)
        positive_controls.append(
            {"seed": seed, "E": coefficient_energy(poly), "degree": max(poly)}
        )
    inverse_poly = continuant_polynomial(
        masses(inventory("primes", 2), 2 + 0j), 0.35, *inverse_charges(2)
    )
    dag_poly = forward_dag_determinant_polynomial(prime_xs, determinant_z)
    selected_values = inventory("primes", 8)
    selected_xs = masses(selected_values, 1.5 + 0.75j)
    selected_charges = primary_charges(8)
    selected_theta = 2 * math.pi * 127 / CHARACTER_COUNT
    selected_w = cmath.exp(1j * selected_theta)
    selected_poly = continuant_polynomial(selected_xs, 0.6, *selected_charges)
    selected_value = evaluate_polynomial(selected_poly, selected_w)
    selected_dense = dense_determinant(
        selected_xs, 0.6, selected_w, *selected_charges
    )
    selected_trace = trace_log_reconstruction(
        selected_xs, 0.6, selected_w, *selected_charges, power_cutoff=64
    )
    selected_high_precision = high_precision_continuant(
        selected_values,
        1.5 + 0.75j,
        0.6,
        selected_theta,
        *selected_charges,
    )
    return {
        "candidate": "SD-C15",
        "frozen_summary_point": {"N": count, "s": str(source_s), "z": determinant_z},
        "zero_data_used": False,
        "selectivity": selectivity,
        "positive_charge_controls": positive_controls,
        "inverse_two_atom": {
            "polynomial": {str(k): [v.real, v.imag] for k, v in inverse_poly.items()},
            "nonzero_zero_degree_mixed_term": True,
        },
        "forward_dag": {
            "E": coefficient_energy(dag_poly),
            "degree": max(dag_poly),
        },
        "gauge_max_residual": max(
            gauge_residual(inventory("primes", 8), 1.5 + 0.75j, 0.713, kind)
            for kind in ("rank", "entropy")
        ),
        "roof_shift_max_residual": max(
            roof_shift_residual(value, 1.5 + 0.75j, 0.713)
            for value in inventory("primes", 8)
        ),
        "selected_determinant_audit": {
            "N": 8,
            "s": "1.5+0.75i",
            "z": 0.6,
            "theta_index": 127,
            "dense_residual": abs(selected_value - selected_dense),
            "trace_power_64_residual": abs(selected_value - selected_trace),
            "high_precision_80_digit_residual": abs(
                selected_value - selected_high_precision
            ),
            "dft_coefficient_residual": dft_coefficient_residual(selected_poly),
        },
        "decision": {
            "GO_CHARACTER_RESOLUTION": True,
            "GO_ARITHMETIC_SELECTIVITY": False,
            "STOP_ARITHMETIC_SELECTIVITY": True,
            "STOP_TIME_REVERSAL": True,
            "PROVES_TOO_MUCH": True,
        },
    }


def write_outputs(target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    frozen_summary = summary()
    (target / "summary.json").write_text(
        json.dumps(frozen_summary, indent=2, sort_keys=True) + "\n"
    )

    energy_rows = frozen_energy_rows()
    with (target / "determinant_fourier_audit.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(energy_rows[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(energy_rows)

    gauge_rows = []
    for count in (8, 16, 32):
        values = inventory("primes", count)
        for source_s in SOURCE_POINTS:
            for theta in (0.0, 0.713, 2.2):
                for kind in ("rank", "entropy"):
                    gauge_rows.append(
                        {
                            "control": f"{kind}_coboundary",
                            "N": count,
                            "s": str(source_s),
                            "theta": theta,
                            "residual": gauge_residual(values, source_s, theta, kind),
                        }
                    )
                gauge_rows.append(
                    {
                        "control": "entropy_roof_shift",
                        "N": count,
                        "s": str(source_s),
                        "theta": theta,
                        "residual": max(
                            roof_shift_residual(value, source_s, theta) for value in values
                        ),
                    }
                )
    with (target / "gauge_reparameterization.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(gauge_rows[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(gauge_rows)

    control_rows = []
    for item in energy_rows:
        control_rows.append(
            {
                "control_type": "inventory",
                "control_id": item["inventory"],
                "N": item["N"],
                "s": item["s"],
                "z": item["z"],
                "E": item["E"],
                "degree": item["degree"],
                "d0_residual": item["d0_residual"],
                "magnitude_min": item["magnitude_min"],
                "magnitude_max": item["magnitude_max"],
                "magnitude_range": item["magnitude_range"],
            }
        )
    control_rows.extend(frozen_positive_charge_rows())
    with (target / "inventory_charge_controls.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(control_rows[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(control_rows)

    census_rows = []
    for count in (2, 3, 4, 5):
        values = first_primes(count)
        census_rows.extend(
            {"charge_case": "positive", **row}
            for row in charged_path_census(values, 12, *primary_charges(count))
        )
        census_rows.extend(
            {"charge_case": "inverse", **row}
            for row in charged_path_census(values, 12, *inverse_charges(count))
        )
    with (target / "exact_path_census.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(census_rows[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(census_rows)

    paper_root = target.parent
    checksum_paths = sorted(
        path
        for path in (paper_root / "code").glob("*.py")
        if path.is_file()
    ) + sorted(
        path
        for path in target.iterdir()
        if path.is_file() and path.name != "SHA256SUMS.txt"
    )
    checksum_lines = []
    for path in checksum_paths:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        checksum_lines.append(f"{digest}  {path.relative_to(paper_root)}")
    (target / "SHA256SUMS.txt").write_text("\n".join(checksum_lines) + "\n")


if __name__ == "__main__":
    output = Path(__file__).resolve().parents[1] / "results"
    write_outputs(output)
    print(output)
