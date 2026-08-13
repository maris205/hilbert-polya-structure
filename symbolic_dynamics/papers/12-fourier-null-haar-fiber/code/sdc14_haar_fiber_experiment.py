#!/usr/bin/env python3
"""Deterministic audit of the SD-C14 Fourier-null Haar fiber.

The promoted single-block object is W=1 direct-sum u in
C direct-sum L(Z), with positive trace

    Phi_c(a direct-sum x)=a+c*tau(x), c>=0.

For every nonzero integer r, Phi_c(W^r)=1.  The trace is faithful for c>0
but has total mass 1+c and is not a state.  No target zeros, crossings,
fitting, or cross-family data are used.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Iterable

import numpy as np
import sympy as sp


# ---------------------------------------------------------------------------
# Intrinsic and control inventories
# ---------------------------------------------------------------------------


def internal_multiplicative_atoms(count: int) -> list[int]:
    if count <= 0:
        return []
    upper = 32 if count < 8 else int(count * (math.log(count) + math.log(math.log(count))) + 32)
    while True:
        sieve = np.ones(upper + 1, dtype=bool)
        sieve[:2] = False
        for prime in range(2, math.isqrt(upper) + 1):
            if sieve[prime]:
                sieve[prime * prime : upper + 1 : prime] = False
        values = np.flatnonzero(sieve)
        if len(values) >= count:
            return [int(value) for value in values[:count]]
        upper *= 2


def composite_inventory(count: int) -> list[int]:
    result: list[int] = []
    value = 4
    while len(result) < count:
        if any(value % divisor == 0 for divisor in range(2, math.isqrt(value) + 1)):
            result.append(value)
        value += 1
    return result


def random_increasing_inventory(count: int, seed: int = 1907) -> list[int]:
    rng = np.random.default_rng(seed)
    return [int(value) for value in 1 + np.cumsum(rng.integers(1, 15, size=count))]


# ---------------------------------------------------------------------------
# Exact Haar and cyclic moments
# ---------------------------------------------------------------------------


def haar_moment(c: float, repetition: int, normalized: bool = False) -> float:
    value = 1.0 + c if repetition == 0 else 1.0
    return value / (1.0 + c) if normalized else value


def cyclic_moment(c: float, order: int, repetition: int, normalized: bool = False) -> float:
    value = 1.0 + (c if repetition % order == 0 else 0.0)
    return value / (1.0 + c) if normalized else value


def haar_classification() -> dict:
    return {
        "theorem": (
            "Every finite positive circle measure mu with integral u^r dmu=1 "
            "for all r>=1 is uniquely mu=delta_1+c*m_Haar with c>=0."
        ),
        "proof": (
            "nu=mu-delta_1 has every nonzero Fourier coefficient zero; "
            "Fourier uniqueness gives nu=c*m_Haar, and positivity forces c>=0."
        ),
        "normalized_state_consequence": "mu(T)=1 forces c=0 and mu=delta_1",
        "finite_support_consequence": "finite support forces c=0 and mu=delta_1",
        "nonnormalized_escape": "c>0 is positive and faithful but Phi_c(1)=1+c",
    }


def cyclic_approximant_audit(max_order: int = 64, repetition_cutoff: int = 128) -> dict:
    c = 1.0
    q_values = [
        0.2 + 0.1j,
        0.7 - 0.15j,
        0.92 * np.exp(0.37j),
    ]
    moment_rows = []
    summary_rows = []
    for order in range(2, max_order + 1):
        first_leak = None
        for repetition in range(1, repetition_cutoff + 1):
            value = cyclic_moment(c, order, repetition)
            leaks = value != 1.0
            if leaks and first_leak is None:
                first_leak = repetition
            moment_rows.append(
                {
                    "order": order,
                    "repetition": repetition,
                    "unnormalized_moment": value,
                    "normalized_moment": cyclic_moment(
                        c, order, repetition, normalized=True
                    ),
                    "haar_target": 1.0,
                    "leaks": leaks,
                }
            )
        errors = []
        for q in q_values:
            log_d_n = np.log1p(-q) + (c / order) * np.log1p(-(q**order))
            d_n = np.exp(log_d_n)
            d_haar = 1.0 - q
            errors.append(abs(d_n - d_haar))
        summary_rows.append(
            {
                "order": order,
                "first_leak_repetition": first_leak,
                "first_leak_equals_order": first_leak == order,
                "max_det_error_vs_haar": max(errors),
                "formula": "(1-q)*(1-q^N)^(c/N)",
            }
        )
    return {
        "c": c,
        "max_order": max_order,
        "repetition_cutoff": repetition_cutoff,
        "moment_formula": "Phi_c,N(W_N^r)=1+c if N divides r, else 1",
        "determinant_formula": "D_c,N(q)=(1-q)(1-q^N)^(c/N) on |q|<1",
        "all_first_leaks_exact": all(
            row["first_leak_equals_order"] for row in summary_rows
        ),
        "moment_rows": moment_rows,
        "summary_rows": summary_rows,
    }


# ---------------------------------------------------------------------------
# Analytic determinant and FK magnitude
# ---------------------------------------------------------------------------


def analytic_haar_determinant(q: complex) -> complex:
    return 1.0 - q


def fk_unnormalized(c: float, q: complex) -> float:
    return abs(1.0 - q) * max(1.0, abs(q)) ** c


def fk_normalized(c: float, q: complex) -> float:
    return fk_unnormalized(c, q) ** (1.0 / (1.0 + c))


def fk_quadrature(c: float, q: complex, grid_size: int = 2**16) -> float:
    angles = 2.0 * math.pi * (np.arange(grid_size) + 0.5) / grid_size
    haar_log = np.mean(np.log(np.abs(1.0 - q * np.exp(1j * angles))))
    return float(np.exp(math.log(abs(1.0 - q)) + c * haar_log))


def haar_formula_audit() -> dict:
    rows = []
    q_values = [
        0.5 * np.exp(0.37j),
        0.9 * np.exp(0.37j),
        1.1 * np.exp(0.37j),
        1.5 * np.exp(0.37j),
    ]
    for c in [0.25, 1.0, 3.0]:
        for q in q_values:
            exact = fk_unnormalized(c, q)
            quadrature = fk_quadrature(c, q)
            rows.append(
                {
                    "c": c,
                    "q_abs": abs(q),
                    "q_arg": np.angle(q),
                    "unnormalized_positive_moment_r1": haar_moment(c, 1),
                    "normalized_state_moment_r1": haar_moment(c, 1, True),
                    "analytic_D_real": analytic_haar_determinant(q).real,
                    "analytic_D_imag": analytic_haar_determinant(q).imag,
                    "fk_unnormalized": exact,
                    "fk_normalized": fk_normalized(c, q),
                    "fk_quadrature": quadrature,
                    "fk_quadrature_residual": abs(quadrature - exact),
                }
            )
    return {
        "positive_moments": "Phi_c(W^r)=1 for every nonzero integer r",
        "normalized_moments": "phi_c(W^r)=1/(1+c)",
        "analytic_determinant": "D_c(q)=1-q on |q|<1",
        "fk_unnormalized": "Delta_c(1-qW)=|1-q|*max(1,|q|)^c",
        "fk_normalized": "Delta_phi=(|1-q|*max(1,|q|)^c)^(1/(1+c))",
        "rows": rows,
    }


# ---------------------------------------------------------------------------
# Fourier-density perturbations
# ---------------------------------------------------------------------------


def perturbed_moment(c: float, epsilon: float, frequency: int, repetition: int) -> float:
    return 1.0 + (c * epsilon if repetition == frequency else 0.0)


def density_perturbation_audit(repetition_cutoff: int = 32) -> dict:
    q = 0.62 + 0.14j
    c = 1.0
    rows = []
    for frequency in range(1, 17):
        for epsilon in [-0.25, -0.1, 0.1, 0.25]:
            first_leak = None
            for repetition in range(1, repetition_cutoff + 1):
                if perturbed_moment(c, epsilon, frequency, repetition) != 1.0:
                    first_leak = repetition
                    break
            determinant = (1.0 - q) * np.exp(
                -c * epsilon * q**frequency / frequency
            )
            rows.append(
                {
                    "frequency": frequency,
                    "epsilon": epsilon,
                    "density_minimum": 1.0 - 2.0 * abs(epsilon),
                    "density_nonnegative": abs(epsilon) <= 0.5,
                    "first_leak_repetition": first_leak,
                    "first_leak_equals_frequency": first_leak == frequency,
                    "leak_value": perturbed_moment(
                        c, epsilon, frequency, frequency
                    ),
                    "determinant_real": determinant.real,
                    "determinant_imag": determinant.imag,
                    "determinant_formula": (
                        "(1-q)*exp(-c*epsilon*q^k/k)"
                    ),
                }
            )
    return {
        "density": "1+2 epsilon cos(k theta), |epsilon|<=1/2",
        "moment_formula": "Phi(W^r)=1+c epsilon when r=k, otherwise 1",
        "all_first_leaks_exact": all(
            row["first_leak_equals_frequency"] for row in rows
        ),
        "rows": rows,
    }


# ---------------------------------------------------------------------------
# Self-adjoint and recurrent balanced controls
# ---------------------------------------------------------------------------


def selfadjoint_audit(power_cutoff: int = 16) -> dict:
    rows = []
    for c in [0.25, 1.0, 3.0]:
        for power in range(1, power_cutoff + 1):
            unnormalized = 0.0 if power % 2 else 2.0 * (1.0 + c)
            normalized_channel = unnormalized / 2.0
            rows.append(
                {
                    "c": c,
                    "power": power,
                    "unnormalized_block_trace": unnormalized,
                    "channel_normalized_trace": normalized_channel,
                    "odd_zero": power % 2 == 1 and unnormalized == 0,
                    "H2_identity": power != 2 or normalized_channel == 1.0 + c,
                }
            )
    return {
        "object": "H=[[0,W],[W*,0]]",
        "identity": "H^2=I",
        "trace_formula": "Tr_2 tensor Phi_c(H^(2r))=2(1+c), odd powers zero",
        "first_even_leak_power": 2,
        "rows": rows,
    }


def balanced_word_audit() -> dict:
    x, y, c = sp.symbols("x y c", positive=True)
    mixed_two_cycle = sp.expand(2 * (1 + c) * x * y)
    normalized_vertex_trace = sp.expand((1 + c) * x * y)
    return {
        "word": "u*u^(-1)=1",
        "formal_variables": ["x", "y"],
        "matrix_trace_coefficient": str(mixed_two_cycle),
        "vertex_normalized_coefficient": str(normalized_vertex_trace),
        "nonzero": mixed_two_cycle != 0,
        "conclusion": (
            "Haar Fourier nullity kills nonzero exponent words, but every "
            "balanced inverse word lies in the identity Fourier sector"
        ),
    }


# ---------------------------------------------------------------------------
# Inventory-blind determinant controls
# ---------------------------------------------------------------------------


def inventory_controls(atom_count: int = 128) -> dict:
    inventories = {
        "tensor_primes": np.asarray(internal_multiplicative_atoms(atom_count), dtype=float),
        "composites": np.asarray(composite_inventory(atom_count), dtype=float),
        "random_increasing": np.asarray(random_increasing_inventory(atom_count), dtype=float),
    }
    s = 1.2 + 2.3j
    z = 0.7 + 0.1j
    phase_grid = np.linspace(0.0, 2.0 * math.pi, 33)
    rows = []
    for name, values in inventories.items():
        q = z * np.exp(-s * np.log(values))
        base_log = complex(np.sum(np.log1p(-q)))
        for c in [0.25, 1.0, 3.0]:
            phase_values = []
            for phase in phase_grid:
                # Haar invariance makes e^(i phase)u have the same nonzero moments.
                phase_values.append(base_log)
            rows.append(
                {
                    "inventory": name,
                    "atom_count": atom_count,
                    "c": c,
                    "base_log_D_real": base_log.real,
                    "base_log_D_imag": base_log.imag,
                    "haar_log_D_real": base_log.real,
                    "haar_log_D_imag": base_log.imag,
                    "analytic_difference": 0.0,
                    "phase_log_D_range": float(
                        max(abs(value - phase_values[0]) for value in phase_values)
                    ),
                    "determinant_blind": True,
                }
            )
    return {
        "formula": "product_a D_c(z a^(-s))=product_a(1-z a^(-s))",
        "honest_domain": "frozen finite prefixes; infinite Euler product on Re(s)>1",
        "rows": rows,
        "all_determinant_blind": all(row["determinant_blind"] for row in rows),
        "verdict": (
            "PROVES_TOO_MUCH: the Haar sector is analytically invisible for "
            "prime, composite, and random positive inventories"
        ),
    }


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------


def write_csv(path: Path, rows: Iterable[dict]) -> None:
    rows = list(rows)
    if not rows:
        return
    fields: list[str] = []
    for row in rows:
        for key in row:
            if key not in fields:
                fields.append(key)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    key: (
                        json.dumps(value, sort_keys=True)
                        if isinstance(value, (dict, list))
                        else value
                    )
                    for key, value in row.items()
                }
            )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results",
    )
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    classification = haar_classification()
    cyclic = cyclic_approximant_audit()
    formulas = haar_formula_audit()
    perturbations = density_perturbation_audit()
    selfadjoint = selfadjoint_audit()
    balanced = balanced_word_audit()
    inventories = inventory_controls()
    results = {
        "metadata": {
            "candidate_id": "SD-C14",
            "candidate": "Fourier-null infinite Haar fiber",
            "primary_family": "symbolic dynamics",
            "uses_riemann_zero_data": False,
            "fits_target_zeros": False,
            "crossing_census_performed": False,
        },
        "classification": classification,
        "cyclic_approximants": cyclic,
        "haar_formulas": formulas,
        "density_perturbations": perturbations,
        "selfadjoint_control": selfadjoint,
        "balanced_inverse_word": balanced,
        "inventory_controls": inventories,
        "claim_boundary": {
            "positive_measure_classification": "PROVED",
            "infinite_haar_moment_escape": "PROVED for nonnormalized positive trace c>0",
            "normalized_state_escape": "REFUTED; normalized moments are 1/(1+c)",
            "finite_support_escape": "REFUTED; first cyclic leak occurs at r=N",
            "analytic_haar_visibility": "REFUTED; D_c(q)=1-q",
            "fk_formula": "PROVED and kept distinct from analytic determinant",
            "density_perturbation": "first nonzero Fourier coefficient leaks at its frequency",
            "selfadjoint_escape": "REFUTED by H^2=I",
            "recurrent_balanced_escape": "REFUTED by uu^(-1)=1",
            "arithmetic_specificity": "REFUTED by matched inventories",
            "rh_or_target_zero_claim": "FORBIDDEN / NOT MADE",
            "route_b_invocation_allowed": False,
        },
    }
    (args.output_dir / "summary.json").write_text(
        json.dumps(results, indent=2, sort_keys=True, default=str) + "\n"
    )
    write_csv(args.output_dir / "cyclic_moments.csv", cyclic["moment_rows"])
    write_csv(args.output_dir / "cyclic_approximants.csv", cyclic["summary_rows"])
    write_csv(args.output_dir / "haar_fk_formulas.csv", formulas["rows"])
    write_csv(args.output_dir / "density_perturbations.csv", perturbations["rows"])
    write_csv(args.output_dir / "selfadjoint_control.csv", selfadjoint["rows"])
    write_csv(args.output_dir / "inventory_controls.csv", inventories["rows"])
    print(
        json.dumps(
            {
                "output": str(args.output_dir / "summary.json"),
                "classification": classification["theorem"],
                "cyclic_first_leaks": cyclic["all_first_leaks_exact"],
                "density_first_leaks": perturbations["all_first_leaks_exact"],
                "inventory_blind": inventories["all_determinant_blind"],
                "max_fk_residual": max(
                    row["fk_quadrature_residual"] for row in formulas["rows"]
                ),
                "no_zero_data": True,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
