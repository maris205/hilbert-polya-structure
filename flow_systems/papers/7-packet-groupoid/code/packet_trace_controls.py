#!/usr/bin/env python3
"""Deterministic, target-free controls for the Paper 7 packet-trace proxy.

The calculations in this module are finite regression checks for conventions
and algebraic identities frozen in ``notes/research_protocol.md``.  They do
not construct a trace on the source flow, prove source ownership, or supply a
Route verdict.  The implementation uses only the Python standard library and
does not use a network, random numbers, fitted parameters, target zeros, or
external datasets.
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


SCHEMA = "paper7-packet-trace-controls/2"
DEFAULT_MAX_PRIME = 5_000
POISSON_LENGTHS = (math.log(2.0), math.log(3.0), math.log(5.0), 2.0, 4.0, 8.0)
RIEMANN_LENGTHS = (1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 64.0)
SIGMAS = (1.25, 2.0, 3.0)
REPETITION_CUTOFFS = (1, 2, 4, 8, 16, 32)
FOURIER_CONVENTION = "fhat(xi)=integral_R f(t)*exp(-i*t*xi) dt"
GAUSSIAN_SCOPE = (
    "Schwartz convention control only; compact-support theorem remains analytic."
)
IMPLEMENTATION_RELATIVE_PATHS = (
    "code/packet_trace_controls.py",
    "code/test_packet_trace_controls.py",
    "code/README.md",
    "experiments/reproduce.sh",
    "experiments/README.md",
    "results/README.md",
)


def primes_up_to(limit: int) -> list[int]:
    """Return the rational primes not exceeding ``limit``."""

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


def gaussian(time: float) -> float:
    """The fixed Schwartz test function exp(-t^2/2)."""

    return math.exp(-0.5 * time * time)


def gaussian_fourier(frequency: float) -> float:
    """Fourier transform under the convention frozen in this file."""

    return math.sqrt(2.0 * math.pi) * math.exp(-0.5 * frequency * frequency)


def symmetric_sum(function: Callable[[float], float], step: float, radius: int) -> float:
    """Return sum_{index=-radius}^{radius} function(index*step)."""

    return math.fsum(function(index * step) for index in range(-radius, radius + 1))


def poisson_control(length: float, tail_coordinate: float = 12.0) -> dict[str, float | int]:
    """Compare both sides of Poisson summation for the fixed Gaussian.

    With fhat(xi)=integral f(t)exp(-it xi)dt, the relevant identity is

        L sum_r f(rL) = sum_n fhat(2*pi*n/L).

    Deterministic symmetric cutoffs put every omitted Gaussian argument past
    ``tail_coordinate``.  This is a convention check, not a numerical proof of
    Poisson summation for the manuscript's compactly supported test class.
    """

    if length <= 0.0:
        raise ValueError("length must be positive")
    time_radius = max(1, math.ceil(tail_coordinate / length))
    frequency_step = 2.0 * math.pi / length
    frequency_radius = max(1, math.ceil(tail_coordinate / frequency_step))
    return_side = length * symmetric_sum(gaussian, length, time_radius)
    spectral_side = symmetric_sum(
        gaussian_fourier, frequency_step, frequency_radius
    )
    absolute_error = abs(return_side - spectral_side)
    return {
        "time_radius": time_radius,
        "frequency_radius": frequency_radius,
        "return_side": return_side,
        "spectral_side": spectral_side,
        "absolute_error": absolute_error,
        "relative_error": absolute_error / max(abs(return_side), abs(spectral_side)),
    }


def trace_norm_riemann_control(
    length: float, tail_coordinate: float = 12.0
) -> dict[str, float | int]:
    """Evaluate the positive Gaussian trace norm and its Riemann scaling.

    For mesh h=2*pi/L,

        h sum_n |fhat(nh)| -> integral |fhat(xi)| dxi = 2*pi.

    Equivalently, the unscaled trace norm is asymptotic to L for this fixed
    Gaussian.  The Gaussian is used to lock normalization without target data.
    """

    if length <= 0.0:
        raise ValueError("length must be positive")
    mesh = 2.0 * math.pi / length
    frequency_radius = max(1, math.ceil(tail_coordinate / mesh))
    trace_norm = symmetric_sum(gaussian_fourier, mesh, frequency_radius)
    scaled_riemann_sum = mesh * trace_norm
    fourier_l1_norm = 2.0 * math.pi
    return {
        "frequency_radius": frequency_radius,
        "mesh": mesh,
        "trace_norm": trace_norm,
        "scaled_riemann_sum": scaled_riemann_sum,
        "fourier_l1_norm": fourier_l1_norm,
        "absolute_error": abs(scaled_riemann_sum - fourier_l1_norm),
        "trace_norm_over_length": trace_norm / length,
    }


def prime_power_decomposition(number: int) -> tuple[int, int] | None:
    """Return (p, r) exactly when number=p**r for a rational prime p."""

    if number < 2:
        return None
    remaining = number
    divisor = 2
    while divisor * divisor <= remaining and remaining % divisor != 0:
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining % divisor != 0:
        return (number, 1)
    exponent = 0
    while remaining % divisor == 0:
        remaining //= divisor
        exponent += 1
    if remaining == 1:
        return (divisor, exponent)
    return None


def von_mangoldt(number: int) -> float:
    """Return the finite exact-ledger value Lambda(number)."""

    decomposition = prime_power_decomposition(number)
    return 0.0 if decomposition is None else math.log(decomposition[0])


def log_z_partial(
    lengths: Sequence[float],
    masses: Sequence[float],
    sigma: float,
    repetitions: int,
) -> float:
    """Return the finite repetition approximation to positive ``log Z``.

    For the finite proxy used here, ``D=prod_j(1-exp(-sigma*L_j))**m_j``
    and ``Z=D**(-1)``.  Thus ``log Z=-tau(Log D)``.  The positive series in
    this function belongs to the reciprocal ``Z`` side, not to ``tau(Log D)``.
    """

    _validate_clock_inputs(lengths, masses, sigma)
    if repetitions < 1:
        raise ValueError("repetitions must be positive")
    return math.fsum(
        mass * math.exp(-repetition * sigma * length) / repetition
        for length, mass in zip(lengths, masses)
        for repetition in range(1, repetitions + 1)
    )


def log_z_exact(
    lengths: Sequence[float], masses: Sequence[float], sigma: float
) -> float:
    """Return exact positive ``log Z=-tau(Log D)`` on the real branch."""

    _validate_clock_inputs(lengths, masses, sigma)
    return math.fsum(
        -mass * math.log1p(-math.exp(-sigma * length))
        for length, mass in zip(lengths, masses)
    )


def tau_log_d_exact(
    lengths: Sequence[float], masses: Sequence[float], sigma: float
) -> float:
    """Return ``tau(Log D)=-log Z`` for the finite positive-real proxy."""

    return -log_z_exact(lengths, masses, sigma)


def compiled_d_product(
    lengths: Sequence[float], masses: Sequence[float], sigma: float
) -> float:
    """Return determinant-side ``D=prod_j(1-exp(-sigma*L_j))**m_j``."""

    _validate_clock_inputs(lengths, masses, sigma)
    return math.prod(
        (1.0 - math.exp(-sigma * length)) ** mass
        for length, mass in zip(lengths, masses)
    )


def compiled_z_product(
    lengths: Sequence[float], masses: Sequence[float], sigma: float
) -> float:
    """Return reciprocal-side ``Z=D**(-1)`` for a finite clock list."""

    _validate_clock_inputs(lengths, masses, sigma)
    return math.prod(
        (1.0 - math.exp(-sigma * length)) ** (-mass)
        for length, mass in zip(lengths, masses)
    )


def determinant_reciprocal_control(
    lengths: Sequence[float], masses: Sequence[float], sigma: float
) -> dict[str, float]:
    """Return both sides of ``log Z=-tau(Log D)`` and ``D*Z=1``.

    These are finite positive-real convention controls.  They do not assert
    source ownership, an infinite determinant, or a choice of complex branch.
    """

    log_z = log_z_exact(lengths, masses, sigma)
    tau_log_d = -log_z
    determinant = math.exp(tau_log_d)
    reciprocal = math.exp(log_z)
    compiled_d = compiled_d_product(lengths, masses, sigma)
    compiled_z = compiled_z_product(lengths, masses, sigma)
    return {
        "tau_Log_D": tau_log_d,
        "log_Z": log_z,
        "D": determinant,
        "Z": reciprocal,
        "compiled_D": compiled_d,
        "compiled_Z": compiled_z,
        "sign_residual": abs(tau_log_d + log_z),
        "reciprocal_residual": abs(determinant * reciprocal - 1.0),
        "D_product_residual": abs(determinant - compiled_d),
        "Z_product_residual": abs(reciprocal - compiled_z),
    }


def trace_log_partial(
    lengths: Sequence[float],
    masses: Sequence[float],
    sigma: float,
    repetitions: int,
) -> float:
    """Compatibility wrapper returning ``log_Z_partial`` (not tau(Log D))."""

    return log_z_partial(lengths, masses, sigma, repetitions)


def trace_log_exact(
    lengths: Sequence[float], masses: Sequence[float], sigma: float
) -> float:
    """Compatibility wrapper returning positive ``log_Z`` (not tau(Log D))."""

    return log_z_exact(lengths, masses, sigma)


def compiled_inverse_product(
    lengths: Sequence[float], masses: Sequence[float], sigma: float
) -> float:
    """Compatibility wrapper returning reciprocal-side ``Z``."""

    return compiled_z_product(lengths, masses, sigma)


def _validate_clock_inputs(
    lengths: Sequence[float], masses: Sequence[float], sigma: float
) -> None:
    if len(lengths) != len(masses):
        raise ValueError("lengths and masses must have equal size")
    if sigma <= 0.0:
        raise ValueError("sigma must be positive in these finite controls")
    if any(length <= 0.0 for length in lengths):
        raise ValueError("clock lengths must be positive")
    if any(mass <= 0.0 for mass in masses):
        raise ValueError("component masses must be positive")


def deterministic_mass(model: str, prime: int, rank: int) -> float:
    """Positive, preregistered mass families used only for falsification."""

    if model == "unit":
        return 1.0
    if model == "rank_modulated":
        return (0.75, 1.0, 1.25, 1.5)[rank % 4]
    if model == "clock_decay":
        return 1.0 / (1.0 + math.log(prime))
    raise ValueError(f"unknown mass model: {model}")


def format_float(value: float) -> str:
    """Stable round-trippable rendering for CSV artifacts."""

    if not math.isfinite(value):
        raise ValueError("non-finite numeric output is forbidden")
    if value == 0.0:
        value = 0.0
    return format(value, ".17g")


def write_csv(
    path: Path, fieldnames: Sequence[str], rows: Iterable[dict[str, object]]
) -> int:
    """Write a deterministic UTF-8 CSV and return its data-row count."""

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


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _artifact_record(path: Path, rows: int) -> dict[str, int | str]:
    return {"bytes": path.stat().st_size, "rows": rows, "sha256": sha256(path)}


def _poisson_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for length in POISSON_LENGTHS:
        result = poisson_control(length)
        rows.append(
            {
                "length": format_float(length),
                "time_radius": result["time_radius"],
                "frequency_radius": result["frequency_radius"],
                "return_side_L_sum_f_rL": format_float(float(result["return_side"])),
                "spectral_side_sum_fhat_2pi_n_over_L": format_float(
                    float(result["spectral_side"])
                ),
                "absolute_error": format_float(float(result["absolute_error"])),
                "relative_error": format_float(float(result["relative_error"])),
                "fourier_convention": FOURIER_CONVENTION,
                "scope": GAUSSIAN_SCOPE,
            }
        )
    return rows


def _riemann_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for length in RIEMANN_LENGTHS:
        result = trace_norm_riemann_control(length)
        rows.append(
            {
                "length": format_float(length),
                "mesh_2pi_over_L": format_float(float(result["mesh"])),
                "frequency_radius": result["frequency_radius"],
                "trace_norm_sum_abs_fhat": format_float(float(result["trace_norm"])),
                "scaled_riemann_sum": format_float(
                    float(result["scaled_riemann_sum"])
                ),
                "fourier_L1_target_2pi": format_float(
                    float(result["fourier_l1_norm"])
                ),
                "absolute_error": format_float(float(result["absolute_error"])),
                "trace_norm_over_L": format_float(
                    float(result["trace_norm_over_length"])
                ),
                "scope": GAUSSIAN_SCOPE,
            }
        )
    return rows


def _von_mangoldt_rows(limit: int = 256, sigma: float = 2.0) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for number in range(1, limit + 1):
        decomposition = prime_power_decomposition(number)
        if decomposition is None:
            prime = ""
            repetition: int | str = ""
            coefficient = 0.0
            return_time: float | str = ""
        else:
            prime, repetition = decomposition
            coefficient = math.log(prime) * number ** (-sigma)
            return_time = format_float(repetition * math.log(prime))
        rows.append(
            {
                "n": number,
                "is_prime_power": "true" if decomposition is not None else "false",
                "prime": prime,
                "repetition": repetition,
                "return_time_r_log_p": return_time,
                "von_mangoldt": format_float(von_mangoldt(number)),
                "coefficient_Lambda_n_times_n_minus_sigma": format_float(coefficient),
                "sigma": format_float(sigma),
            }
        )
    return rows


def _finite_prime_d_z_rows(primes: Sequence[int]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for cutoff in (5, 29, 97, 499):
        if not primes or cutoff > primes[-1]:
            continue
        prefix = [prime for prime in primes if prime <= cutoff]
        lengths = [math.log(prime) for prime in prefix]
        masses = [1.0] * len(prefix)
        for sigma in SIGMAS:
            quantities = determinant_reciprocal_control(lengths, masses, sigma)
            for repetitions in REPETITION_CUTOFFS:
                partial_log_z = log_z_partial(
                    lengths, masses, sigma, repetitions
                )
                rows.append(
                    {
                        "prime_cutoff": cutoff,
                        "prime_count": len(prefix),
                        "sigma": format_float(sigma),
                        "repetition_cutoff": repetitions,
                        "tau_Log_D_partial": format_float(-partial_log_z),
                        "log_Z_partial": format_float(partial_log_z),
                        "tau_Log_D": format_float(quantities["tau_Log_D"]),
                        "log_Z": format_float(quantities["log_Z"]),
                        "nonnegative_log_Z_tail": format_float(
                            quantities["log_Z"] - partial_log_z
                        ),
                        "D": format_float(quantities["D"]),
                        "Z": format_float(quantities["Z"]),
                        "compiled_D": format_float(quantities["compiled_D"]),
                        "compiled_Z": format_float(quantities["compiled_Z"]),
                        "sign_residual": format_float(
                            quantities["sign_residual"]
                        ),
                        "reciprocal_residual": format_float(
                            quantities["reciprocal_residual"]
                        ),
                        "D_product_residual": format_float(
                            quantities["D_product_residual"]
                        ),
                        "Z_product_residual": format_float(
                            quantities["Z_product_residual"]
                        ),
                        "domain": "finite-prime positive-real control",
                    }
                )
    return rows


def _mass_copy_rows(primes: Sequence[int]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    sigma = 2.0
    for rank, prime in enumerate(primes[:5]):
        unit_log_z = -math.log1p(-(prime ** -sigma))
        for model in ("unit", "rank_modulated", "clock_decay"):
            mass = deterministic_mass(model, prime, rank)
            weighted_log_z = mass * unit_log_z
            for copies in (1, 2, 3):
                additive_log_z = copies * weighted_log_z
                quantities = determinant_reciprocal_control(
                    [math.log(prime)] * copies, [mass] * copies, sigma
                )
                rows.append(
                    {
                        "prime": prime,
                        "prime_rank_zero_based": rank,
                        "sigma": format_float(sigma),
                        "mass_model": model,
                        "mass": format_float(mass),
                        "copies": copies,
                        "single_unit_mass_log_Z": format_float(unit_log_z),
                        "single_weighted_log_Z": format_float(weighted_log_z),
                        "copied_additive_log_Z": format_float(additive_log_z),
                        "tau_Log_D": format_float(quantities["tau_Log_D"]),
                        "log_Z": format_float(quantities["log_Z"]),
                        "D": format_float(quantities["D"]),
                        "Z": format_float(quantities["Z"]),
                        "sign_residual": format_float(
                            quantities["sign_residual"]
                        ),
                        "reciprocal_residual": format_float(
                            quantities["reciprocal_residual"]
                        ),
                        "additivity_residual": format_float(
                            abs(additive_log_z - quantities["log_Z"])
                        ),
                    }
                )
    return rows


def _probability_base_rows() -> list[dict[str, object]]:
    prime = 5
    sigma = 2.0
    return_coefficient = math.log(prime)
    zero_mode_log_z = -math.log1p(-(prime ** -sigma))
    models: tuple[tuple[str, str, str, Fraction], ...] = (
        ("singleton", "atomic", "1", Fraction(1, 1)),
        (
            "arbitrary_three_atom",
            "atomic",
            "1/2+1/3+1/6",
            Fraction(1, 2) + Fraction(1, 3) + Fraction(1, 6),
        ),
        (
            "arbitrary_four_atom",
            "atomic",
            "1/10+2/10+3/10+4/10",
            sum((Fraction(value, 10) for value in (1, 2, 3, 4)), Fraction()),
        ),
        (
            "unit_interval_lebesgue",
            "nonatomic symbolic probability model",
            "integral_[0,1] 1 dx",
            Fraction(1, 1),
        ),
    )
    rows: list[dict[str, object]] = []
    for name, kind, ledger, total in models:
        if total != 1:
            raise AssertionError(f"probability base {name} is not normalized")
        tau_projection = float(total)
        log_z = tau_projection * zero_mode_log_z
        tau_log_d = -log_z
        determinant = math.exp(tau_log_d)
        reciprocal = math.exp(log_z)
        rows.append(
            {
                "base_model": name,
                "base_kind": kind,
                "probability_ledger": ledger,
                "total_probability_exact": str(total),
                "prime": prime,
                "tau_zero_mode_projection": format_float(tau_projection),
                "return_coefficient_log_p": format_float(
                    tau_projection * return_coefficient
                ),
                "tau_Log_D": format_float(tau_log_d),
                "log_Z": format_float(log_z),
                "D": format_float(determinant),
                "Z": format_float(reciprocal),
                "sign_residual": format_float(abs(tau_log_d + log_z)),
                "reciprocal_residual": format_float(
                    abs(determinant * reciprocal - 1.0)
                ),
                "difference_from_singleton": format_float(tau_projection - 1.0),
                "interpretation": "constant-fiber trace depends only on total probability",
            }
        )
    return rows


def _clock_compiler_rows() -> list[dict[str, object]]:
    sigma = 2.0
    systems: tuple[tuple[str, tuple[str, ...], tuple[float, ...], str, int], ...] = (
        (
            "prime_reference",
            ("p=2", "p=3", "p=5"),
            (math.log(2.0), math.log(3.0), math.log(5.0)),
            "rational-prime labels supplied externally",
            0,
        ),
        (
            "arbitrary_positive_clocks",
            ("alpha", "beta", "gamma"),
            (0.7, 1.1, 2.3),
            "analytic compiler only; no arithmetic provenance claimed",
            0,
        ),
        (
            "composite_augmented",
            ("p=2", "p=3", "n=4", "n=6"),
            (math.log(2.0), math.log(3.0), math.log(4.0), math.log(6.0)),
            "analytic compiler survives; rational-prime provenance fails",
            2,
        ),
    )
    rows: list[dict[str, object]] = []
    for name, labels, lengths, provenance, composite_count in systems:
        masses = (1.0,) * len(lengths)
        quantities = determinant_reciprocal_control(lengths, masses, sigma)
        rows.append(
            {
                "clock_system": name,
                "labels": ";".join(labels),
                "lengths": ";".join(format_float(length) for length in lengths),
                "component_count": len(lengths),
                "composite_label_count": composite_count,
                "sigma": format_float(sigma),
                "tau_Log_D": format_float(quantities["tau_Log_D"]),
                "log_Z": format_float(quantities["log_Z"]),
                "D": format_float(quantities["D"]),
                "Z": format_float(quantities["Z"]),
                "compiled_D": format_float(quantities["compiled_D"]),
                "compiled_Z": format_float(quantities["compiled_Z"]),
                "sign_residual": format_float(quantities["sign_residual"]),
                "reciprocal_residual": format_float(
                    quantities["reciprocal_residual"]
                ),
                "D_product_residual": format_float(
                    quantities["D_product_residual"]
                ),
                "Z_product_residual": format_float(
                    quantities["Z_product_residual"]
                ),
                "analytic_compiles": "true",
                "provenance_status": provenance,
            }
        )
    return rows


def _hilbert_vs_tau_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for dimension in (1, 2, 4, 16, 256):
        rows.append(
            {
                "transverse_model": f"uniform_{dimension}_atom",
                "transverse_hilbert_dimension": dimension,
                "ordinary_Hilbert_trace_I_tensor_P0": dimension,
                "finite_tau_projection": format_float(1.0),
                "normalization": f"{dimension} fibers each weighted 1/{dimension}",
                "ordinary_trace_status": "finite and dimension-dependent",
            }
        )
    rows.append(
        {
            "transverse_model": "nonatomic_probability_base",
            "transverse_hilbert_dimension": "infinite",
            "ordinary_Hilbert_trace_I_tensor_P0": "infinite",
            "finite_tau_projection": format_float(1.0),
            "normalization": "integral of rank-one fiber trace over probability mass 1",
            "ordinary_trace_status": "not trace class in the ordinary representation",
        }
    )
    return rows


def _zero_time_rows(primes: Sequence[int], max_prime: int) -> list[dict[str, object]]:
    cutoffs = [cutoff for cutoff in (10, 100, 1_000, 5_000) if cutoff <= max_prime]
    if max_prime not in cutoffs:
        cutoffs.append(max_prime)
    cutoffs = sorted(set(cutoffs))
    rows: list[dict[str, object]] = []
    previous: dict[str, float] = {"unit": 0.0, "rank_modulated": 0.0}
    for cutoff in cutoffs:
        prefix = [prime for prime in primes if prime <= cutoff]
        for model in ("unit", "rank_modulated"):
            partial = math.fsum(
                deterministic_mass(model, prime, rank) * math.log(prime)
                for rank, prime in enumerate(prefix)
            )
            rows.append(
                {
                    "prime_cutoff": cutoff,
                    "prime_count": len(prefix),
                    "mass_model": model,
                    "f_at_zero": format_float(1.0),
                    "partial_sum_m_p_log_p_f0": format_float(partial),
                    "increment_from_previous_cutoff": format_float(
                        partial - previous[model]
                    ),
                    "monotone_positive": "true" if partial > previous[model] else "false",
                    "scope": "finite partial-sum witness; no regularized value assigned",
                }
            )
            previous[model] = partial
    return rows


def _implementation_hashes(paper_dir: Path) -> dict[str, str]:
    records: dict[str, str] = {}
    for relative in IMPLEMENTATION_RELATIVE_PATHS:
        path = paper_dir / relative
        if not path.is_file():
            raise FileNotFoundError(f"required reproduction file is missing: {path}")
        records[relative] = sha256(path)
    return records


def run(
    output_dir: Path,
    max_prime: int = DEFAULT_MAX_PRIME,
    paper_dir: Path | None = None,
) -> dict[str, object]:
    """Generate all deterministic controls and their hash manifest."""

    if max_prime < 100:
        raise ValueError("max_prime must be at least 100")
    output_dir.mkdir(parents=True, exist_ok=True)
    primes = primes_up_to(max_prime)
    tables: tuple[
        tuple[str, Sequence[str], list[dict[str, object]]], ...
    ] = (
        (
            "poisson_convention.csv",
            (
                "length",
                "time_radius",
                "frequency_radius",
                "return_side_L_sum_f_rL",
                "spectral_side_sum_fhat_2pi_n_over_L",
                "absolute_error",
                "relative_error",
                "fourier_convention",
                "scope",
            ),
            _poisson_rows(),
        ),
        (
            "trace_norm_riemann.csv",
            (
                "length",
                "mesh_2pi_over_L",
                "frequency_radius",
                "trace_norm_sum_abs_fhat",
                "scaled_riemann_sum",
                "fourier_L1_target_2pi",
                "absolute_error",
                "trace_norm_over_L",
                "scope",
            ),
            _riemann_rows(),
        ),
        (
            "prime_power_von_mangoldt.csv",
            (
                "n",
                "is_prime_power",
                "prime",
                "repetition",
                "return_time_r_log_p",
                "von_mangoldt",
                "coefficient_Lambda_n_times_n_minus_sigma",
                "sigma",
            ),
            _von_mangoldt_rows(),
        ),
        (
            "finite_prime_d_z_ledger.csv",
            (
                "prime_cutoff",
                "prime_count",
                "sigma",
                "repetition_cutoff",
                "tau_Log_D_partial",
                "log_Z_partial",
                "tau_Log_D",
                "log_Z",
                "nonnegative_log_Z_tail",
                "D",
                "Z",
                "compiled_D",
                "compiled_Z",
                "sign_residual",
                "reciprocal_residual",
                "D_product_residual",
                "Z_product_residual",
                "domain",
            ),
            _finite_prime_d_z_rows(primes),
        ),
        (
            "mass_copy_controls.csv",
            (
                "prime",
                "prime_rank_zero_based",
                "sigma",
                "mass_model",
                "mass",
                "copies",
                "single_unit_mass_log_Z",
                "single_weighted_log_Z",
                "copied_additive_log_Z",
                "tau_Log_D",
                "log_Z",
                "D",
                "Z",
                "sign_residual",
                "reciprocal_residual",
                "additivity_residual",
            ),
            _mass_copy_rows(primes),
        ),
        (
            "probability_base_blindness.csv",
            (
                "base_model",
                "base_kind",
                "probability_ledger",
                "total_probability_exact",
                "prime",
                "tau_zero_mode_projection",
                "return_coefficient_log_p",
                "tau_Log_D",
                "log_Z",
                "D",
                "Z",
                "sign_residual",
                "reciprocal_residual",
                "difference_from_singleton",
                "interpretation",
            ),
            _probability_base_rows(),
        ),
        (
            "clock_compiler_controls.csv",
            (
                "clock_system",
                "labels",
                "lengths",
                "component_count",
                "composite_label_count",
                "sigma",
                "tau_Log_D",
                "log_Z",
                "D",
                "Z",
                "compiled_D",
                "compiled_Z",
                "sign_residual",
                "reciprocal_residual",
                "D_product_residual",
                "Z_product_residual",
                "analytic_compiles",
                "provenance_status",
            ),
            _clock_compiler_rows(),
        ),
        (
            "hilbert_vs_tau_projection.csv",
            (
                "transverse_model",
                "transverse_hilbert_dimension",
                "ordinary_Hilbert_trace_I_tensor_P0",
                "finite_tau_projection",
                "normalization",
                "ordinary_trace_status",
            ),
            _hilbert_vs_tau_rows(),
        ),
        (
            "zero_time_partial_divergence.csv",
            (
                "prime_cutoff",
                "prime_count",
                "mass_model",
                "f_at_zero",
                "partial_sum_m_p_log_p_f0",
                "increment_from_previous_cutoff",
                "monotone_positive",
                "scope",
            ),
            _zero_time_rows(primes, max_prime),
        ),
    )

    artifacts: dict[str, dict[str, int | str]] = {}
    for filename, fieldnames, rows in tables:
        path = output_dir / filename
        row_count = write_csv(path, fieldnames, rows)
        artifacts[filename] = _artifact_record(path, row_count)

    effective_paper_dir = (
        Path(__file__).resolve().parents[1]
        if paper_dir is None
        else paper_dir.resolve()
    )
    manifest: dict[str, object] = {
        "schema": SCHEMA,
        "determinism": {
            "external_datasets": False,
            "fitting": False,
            "network": False,
            "randomness": False,
            "timestamps": False,
            "python_dependencies": "standard_library_only",
        },
        "parameters": {
            "max_prime": max_prime,
            "prime_count": len(primes),
            "fourier_convention": FOURIER_CONVENTION,
            "poisson_tail_coordinate": 12,
            "von_mangoldt_limit": 256,
            "sigmas": list(SIGMAS),
            "repetition_cutoffs": list(REPETITION_CUTOFFS),
        },
        "controls": [
            "Poisson convention",
            "trace-norm Riemann asymptotic",
            "finite prime-power/von Mangoldt ledger",
            "finite-prime log_Z=-tau_Log_D and D/Z reciprocal ledger",
            "positive mass perturbation and copied components",
            "singleton/arbitrary probability-base blindness",
            "arbitrary/composite clock compiler",
            "ordinary Hilbert multiplicity versus finite tau projection",
            "zero-time positive partial sums",
        ],
        "regression_status": "PASS",
        "determinant_quantity_convention": {
            "D": "exp(tau_Log_D)=product_j(1-exp(-sigma*L_j))**m_j",
            "Z": "D**(-1)=product_j(1-exp(-sigma*L_j))**(-m_j)",
            "log_Z": "-tau_Log_D; the positive repetition series belongs to Z",
            "tau_Log_D": "sum_j m_j*log(1-exp(-sigma*L_j)); negative for sigma>0",
            "scope": "finite positive-real proxy; no complex branch or source ownership",
        },
        "interpretation_boundary": (
            "Finite convention and identity checks for a selected proxy. They are "
            "not proofs, source-to-proxy transport, trace provenance, determinant "
            "provenance, or a Route verdict."
        ),
        "forbidden_evidence_not_used": [
            "Riemann-zero data",
            "fitted masses",
            "fitted clocks",
            "fitted shifts",
            "Euler-product agreement as trace provenance",
        ],
        "artifacts": artifacts,
        "implementation_files": _implementation_hashes(effective_paper_dir),
    }
    manifest_path = output_dir / "packet_trace_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return manifest


def verify(
    output_dir: Path, paper_dir: Path | None = None
) -> dict[str, object]:
    """Verify artifact records and the exact current implementation file set."""

    manifest_path = output_dir / "packet_trace_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema") != SCHEMA:
        raise ValueError("unexpected manifest schema")
    artifact_records = manifest.get("artifacts")
    if not isinstance(artifact_records, dict):
        raise ValueError("manifest artifacts field is invalid")
    for filename, raw_record in artifact_records.items():
        if not isinstance(filename, str) or not isinstance(raw_record, dict):
            raise ValueError("invalid artifact record")
        path = output_dir / filename
        if path.stat().st_size != raw_record.get("bytes"):
            raise ValueError(f"byte-size mismatch: {filename}")
        if sha256(path) != raw_record.get("sha256"):
            raise ValueError(f"SHA-256 mismatch: {filename}")
        with path.open("r", encoding="utf-8", newline="") as handle:
            row_count = sum(1 for _ in csv.DictReader(handle))
        if row_count != raw_record.get("rows"):
            raise ValueError(f"row-count mismatch: {filename}")

    implementation_records = manifest.get("implementation_files")
    if not isinstance(implementation_records, dict):
        raise ValueError("manifest implementation_files field is invalid")
    actual_entries = set(implementation_records)
    expected_entries = set(IMPLEMENTATION_RELATIVE_PATHS)
    missing = sorted(expected_entries - actual_entries)
    extra = sorted(actual_entries - expected_entries)
    if missing or extra:
        raise ValueError(
            "implementation file set mismatch: "
            f"missing={missing!r}, extra={extra!r}"
        )
    effective_paper_dir = (
        Path(__file__).resolve().parents[1]
        if paper_dir is None
        else paper_dir.resolve()
    )
    for relative in IMPLEMENTATION_RELATIVE_PATHS:
        expected_hash = implementation_records.get(relative)
        if not isinstance(expected_hash, str):
            raise ValueError(f"invalid implementation SHA-256: {relative}")
        path = effective_paper_dir / relative
        if not path.is_file():
            raise ValueError(f"implementation file is missing: {relative}")
        if sha256(path) != expected_hash:
            raise ValueError(f"implementation SHA-256 mismatch: {relative}")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--max-prime", type=int, default=DEFAULT_MAX_PRIME)
    parser.add_argument(
        "--verify-only",
        action="store_true",
        help="verify an existing manifest instead of regenerating artifacts",
    )
    args = parser.parse_args()
    if args.verify_only:
        manifest = verify(args.output_dir)
    else:
        try:
            manifest = run(args.output_dir, args.max_prime)
        except ValueError as error:
            parser.error(str(error))
        verify(args.output_dir)
    print(
        json.dumps(
            {
                "artifact_count": len(manifest["artifacts"]),
                "regression_status": manifest["regression_status"],
                "schema": manifest["schema"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
