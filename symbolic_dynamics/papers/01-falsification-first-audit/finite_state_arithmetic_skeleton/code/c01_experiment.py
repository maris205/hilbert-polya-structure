#!/usr/bin/env python3
"""Reproducible exact/numerical checks for preregistered candidate SD-C01.

No Riemann-zero data are imported or used.  Integer and finite-field
calculations are labelled exact.  Root counts for the nonlattice control are
argument-principle observations at the requested working precision.
"""

from __future__ import annotations

import csv
import itertools
import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

import mpmath as mp
import numpy as np


SESSION_ID = "SD-S4-2026-08-12"
CANDIDATE_ID = "SD-C01"
MASTER_SEED = 20260812
UNITARY_SEED = 20260815
Q_VALUES = (2, 3, 5)
FORMULA_DEGREE_CUTOFF = 12
BRUTE_NECKLACE_CUTOFFS = {2: 10, 3: 8, 5: 7}
BRUTE_IRREDUCIBLE_CUTOFFS = {2: 9, 3: 7, 5: 6}
ROOT_COUNT_T_VALUES = (10, 20, 40, 80)
DECIMAL_PRECISION = 80


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def prime_divisors(n: int) -> list[int]:
    out: list[int] = []
    p = 2
    m = n
    while p * p <= m:
        if m % p == 0:
            out.append(p)
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        out.append(m)
    return out


def mobius(n: int) -> int:
    factors = 0
    p = 2
    m = n
    while p * p <= m:
        if m % p == 0:
            m //= p
            factors += 1
            if m % p == 0:
                return 0
            while m % p == 0:
                m //= p
        p += 1
    if m > 1:
        factors += 1
    return -1 if factors % 2 else 1


def primitive_necklace_formula(q: int, n: int) -> int:
    numerator = sum(mobius(d) * q ** (n // d) for d in divisors(n))
    assert numerator % n == 0
    return numerator // n


def is_aperiodic_word(word: Sequence[int]) -> bool:
    n = len(word)
    for d in divisors(n):
        if d < n and all(word[i] == word[i % d] for i in range(n)):
            return False
    return True


def brute_aperiodic_necklace_count(q: int, n: int) -> int:
    count = 0
    for word in itertools.product(range(q), repeat=n):
        if not is_aperiodic_word(word):
            continue
        rotations = [word[k:] + word[:k] for k in range(n)]
        if word == min(rotations):
            count += 1
    return count


def _poly_trim(a: Sequence[int], q: int) -> list[int]:
    out = [x % q for x in a]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def _poly_sub(a: Sequence[int], b: Sequence[int], q: int) -> list[int]:
    n = max(len(a), len(b))
    out = [0] * n
    for i in range(n):
        out[i] = ((a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)) % q
    return _poly_trim(out, q)


def _poly_divmod(a: Sequence[int], b: Sequence[int], q: int) -> tuple[list[int], list[int]]:
    rem = _poly_trim(a, q)
    den = _poly_trim(b, q)
    if den == [0]:
        raise ZeroDivisionError("polynomial division by zero")
    quotient = [0] * max(1, len(rem) - len(den) + 1)
    inv_lead = pow(den[-1], -1, q)
    while rem != [0] and len(rem) >= len(den):
        shift = len(rem) - len(den)
        coeff = rem[-1] * inv_lead % q
        quotient[shift] = coeff
        for j, value in enumerate(den):
            rem[j + shift] = (rem[j + shift] - coeff * value) % q
        rem = _poly_trim(rem, q)
    return _poly_trim(quotient, q), rem


def _poly_gcd(a: Sequence[int], b: Sequence[int], q: int) -> list[int]:
    left = _poly_trim(a, q)
    right = _poly_trim(b, q)
    while right != [0]:
        _, remainder = _poly_divmod(left, right, q)
        left, right = right, remainder
    inv_lead = pow(left[-1], -1, q)
    return _poly_trim([(x * inv_lead) % q for x in left], q)


def _poly_mul_mod(a: Sequence[int], b: Sequence[int], modulus: Sequence[int], q: int) -> list[int]:
    product = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            product[i + j] = (product[i + j] + x * y) % q
    _, remainder = _poly_divmod(product, modulus, q)
    return remainder


def _poly_pow_mod(base: Sequence[int], exponent: int, modulus: Sequence[int], q: int) -> list[int]:
    result = [1]
    power = _poly_trim(base, q)
    e = exponent
    while e:
        if e & 1:
            result = _poly_mul_mod(result, power, modulus, q)
        power = _poly_mul_mod(power, power, modulus, q)
        e >>= 1
    return result


def _frobenius_power_x(steps: int, polynomial: Sequence[int], q: int) -> list[int]:
    value = [0, 1]
    for _ in range(steps):
        value = _poly_pow_mod(value, q, polynomial, q)
    return value


def is_monic_irreducible(polynomial: Sequence[int], q: int) -> bool:
    f = _poly_trim(polynomial, q)
    n = len(f) - 1
    if n < 1 or f[-1] != 1:
        return False
    x_mod = _poly_divmod([0, 1], f, q)[1]
    if _frobenius_power_x(n, f, q) != x_mod:
        return False
    for ell in prime_divisors(n):
        test = _poly_sub(_frobenius_power_x(n // ell, f, q), x_mod, q)
        if _poly_gcd(f, test, q) != [1]:
            return False
    return True


def brute_monic_irreducible_count(q: int, n: int) -> int:
    return sum(
        is_monic_irreducible(tuple(coefficients) + (1,), q)
        for coefficients in itertools.product(range(q), repeat=n)
    )


def _poly_mul_truncated(a: Sequence[int], b: Sequence[int], degree: int) -> list[int]:
    out = [0] * (degree + 1)
    for i, x in enumerate(a):
        if i > degree:
            break
        for j, y in enumerate(b):
            if i + j > degree:
                break
            out[i + j] += x * y
    return out


def euler_product_coefficients(q: int, degree: int, inverse: bool) -> list[int]:
    """Return product over n <= degree of (1-u^n)^(+/-N_q(n))."""
    result = [1] + [0] * degree
    for n in range(1, degree + 1):
        count = primitive_necklace_formula(q, n)
        factor = [0] * (degree + 1)
        factor[0] = 1
        for j in range(1, degree // n + 1):
            if inverse:
                factor[j * n] = math.comb(count + j - 1, j)
            elif j <= count:
                factor[j * n] = (-1) ** j * math.comb(count, j)
        result = _poly_mul_truncated(result, factor, degree)
    return result


def repetition_ledger(q: int, degree: int) -> list[dict[str, int | bool]]:
    rows = []
    for n in range(1, degree + 1):
        contributions = {str(d): d * primitive_necklace_formula(q, d) for d in divisors(n)}
        total = sum(contributions.values())
        rows.append(
            {
                "period": n,
                "fixed_points": q**n,
                "primitive_repetition_sum": total,
                "matches": total == q**n,
                "contributions_json": json.dumps(contributions, sort_keys=True),
            }
        )
    return rows


def haar_unitary(rng: np.random.Generator, dimension: int) -> np.ndarray:
    z = rng.normal(size=(dimension, dimension)) + 1j * rng.normal(size=(dimension, dimension))
    q_matrix, r_matrix = np.linalg.qr(z)
    diagonal = np.diag(r_matrix)
    phases = np.where(np.abs(diagonal) > 0, diagonal / np.abs(diagonal), 1.0)
    return q_matrix @ np.diag(np.conjugate(phases))


def lattice_unitary_control() -> dict[str, object]:
    rng = np.random.default_rng(UNITARY_SEED)
    weights = np.array(
        [0.45, 0.35 * np.exp(0.3j), 0.25 * np.exp(-0.6j)], dtype=np.complex128
    )
    unitaries = [haar_unitary(rng, 2) for _ in weights]
    aggregate = sum(weight * unitary for weight, unitary in zip(weights, unitaries, strict=True))
    eigenvalues = np.linalg.eigvals(aggregate)
    h = math.log(3.0)
    x_bounds = (-3.0, 3.0)

    def exact_count(t_max: float) -> int:
        count = 0
        for eigenvalue in eigenvalues:
            real_part = math.log(abs(eigenvalue)) / h
            if not (x_bounds[0] < real_part < x_bounds[1]):
                continue
            phase = math.atan2(eigenvalue.imag, eigenvalue.real)
            k_min = math.ceil((-t_max * h - phase) / (2.0 * math.pi))
            k_max = math.floor((t_max * h - phase) / (2.0 * math.pi))
            count += max(0, k_max - k_min + 1)
        return count

    rows = []
    for t_value in ROOT_COUNT_T_VALUES:
        count = exact_count(float(t_value))
        rows.append({"T": t_value, "root_count": count, "count_over_T": count / t_value})
    return {
        "evidence_status": "NUMERICAL_OBSERVATION",
        "seed": UNITARY_SEED,
        "dimension": 2,
        "number_of_symbolic_loops": 3,
        "roof": h,
        "horizontal_window": list(x_bounds),
        "weights": [[float(w.real), float(w.imag)] for w in weights],
        "unitarity_residuals": [
            float(np.linalg.norm(u.conj().T @ u - np.eye(2), ord=np.inf)) for u in unitaries
        ],
        "aggregate_eigenvalues": [[float(z.real), float(z.imag)] for z in eigenvalues],
        "root_counts": rows,
        "count_method": "closed-form lattice strings of zeros of det(I-exp(-h*s)C)",
    }


@dataclass(frozen=True)
class NonlatticeControl:
    roofs: tuple[mp.mpf, ...]
    weights: tuple[mp.mpc, ...]

    def determinant(self, s: mp.mpc) -> mp.mpc:
        return mp.mpc(1) - sum(
            weight * mp.exp(-roof * s) for roof, weight in zip(self.roofs, self.weights, strict=True)
        )


def _rectangle_boundary(
    x_left: mp.mpf,
    x_right: mp.mpf,
    t_max: mp.mpf,
    horizontal_steps: int,
    vertical_steps: int,
) -> Iterable[mp.mpc]:
    for j in range(horizontal_steps):
        yield mp.mpc(x_left + (x_right - x_left) * j / horizontal_steps, -t_max)
    for j in range(vertical_steps):
        yield mp.mpc(x_right, -t_max + 2 * t_max * j / vertical_steps)
    for j in range(horizontal_steps):
        yield mp.mpc(x_right - (x_right - x_left) * j / horizontal_steps, t_max)
    for j in range(vertical_steps):
        yield mp.mpc(x_left, t_max - 2 * t_max * j / vertical_steps)
    yield mp.mpc(x_left, -t_max)


def argument_principle_count(
    control: NonlatticeControl,
    t_max: int,
    samples_per_unit: int,
) -> dict[str, object]:
    x_left = mp.mpf(-3)
    x_right = mp.mpf(3)
    horizontal_steps = max(96, samples_per_unit * 6)
    vertical_steps = max(128, samples_per_unit * 2 * t_max)
    points = list(_rectangle_boundary(x_left, x_right, mp.mpf(t_max), horizontal_steps, vertical_steps))
    values = [control.determinant(point) for point in points]
    phase_increments = [mp.arg(right / left) for left, right in zip(values, values[1:])]
    winding_raw = mp.fsum(phase_increments) / (2 * mp.pi)
    winding = int(mp.nint(winding_raw))
    return {
        "root_count": winding,
        "winding_raw": mp.nstr(winding_raw, 30),
        "min_boundary_abs_D": mp.nstr(min(abs(value) for value in values), 30),
        "max_phase_increment": mp.nstr(max(abs(value) for value in phase_increments), 30),
        "boundary_samples": len(points),
    }


def nonlattice_root_count_control(precision: int = DECIMAL_PRECISION) -> dict[str, object]:
    mp.mp.dps = precision
    control = NonlatticeControl(
        roofs=(mp.mpf(1), mp.sqrt(2), mp.sqrt(3)),
        weights=(
            mp.mpf("0.37"),
            mp.mpf("0.29") * mp.e ** (mp.mpc(0, mp.mpf("0.4"))),
            mp.mpf("0.23") * mp.e ** (mp.mpc(0, mp.mpf("-0.7"))),
        ),
    )
    rows = []
    for t_value in ROOT_COUNT_T_VALUES:
        coarse = argument_principle_count(control, t_value, samples_per_unit=24)
        fine = argument_principle_count(control, t_value, samples_per_unit=48)
        rows.append(
            {
                "T": t_value,
                **fine,
                "coarse_root_count": coarse["root_count"],
                "sampling_stable": coarse["root_count"] == fine["root_count"],
                "count_over_T": fine["root_count"] / t_value,
            }
        )
    t_array = np.array([row["T"] for row in rows], dtype=float)
    count_array = np.array([row["root_count"] for row in rows], dtype=float)
    slope, intercept = np.polyfit(t_array, count_array, 1)
    return {
        "evidence_status": "NUMERICAL_OBSERVATION",
        "precision_decimal_digits": precision,
        "roofs": [mp.nstr(value, 40) for value in control.roofs],
        "roof_ratio_sqrt2_irrational_by_definition": True,
        "weights": [[mp.nstr(value.real, 40), mp.nstr(value.imag, 40)] for value in control.weights],
        "horizontal_window": [-3, 3],
        "root_counts": rows,
        "linear_fit_count_vs_T": {"slope": float(slope), "intercept": float(intercept)},
        "all_sampling_stable": all(bool(row["sampling_stable"]) for row in rows),
        "method": "argument principle on rectangle boundary; no target zeros",
    }


def build_results(precision: int = DECIMAL_PRECISION) -> dict[str, object]:
    exact_rows: list[dict[str, object]] = []
    all_exact_checks = True
    for q in Q_VALUES:
        for n in range(1, FORMULA_DEGREE_CUTOFF + 1):
            formula = primitive_necklace_formula(q, n)
            row: dict[str, object] = {
                "q": q,
                "degree": n,
                "formula_count": formula,
                "brute_necklace_count": None,
                "brute_irreducible_count": None,
                "necklace_matches": None,
                "irreducible_matches": None,
            }
            if n <= BRUTE_NECKLACE_CUTOFFS[q]:
                brute_necklace = brute_aperiodic_necklace_count(q, n)
                row["brute_necklace_count"] = brute_necklace
                row["necklace_matches"] = brute_necklace == formula
                all_exact_checks &= bool(row["necklace_matches"])
            if n <= BRUTE_IRREDUCIBLE_CUTOFFS[q]:
                brute_irreducible = brute_monic_irreducible_count(q, n)
                row["brute_irreducible_count"] = brute_irreducible
                row["irreducible_matches"] = brute_irreducible == formula
                all_exact_checks &= bool(row["irreducible_matches"])
            exact_rows.append(row)

    euler_results: dict[str, object] = {}
    ledgers: dict[str, object] = {}
    for q in Q_VALUES:
        determinant_coefficients = euler_product_coefficients(q, FORMULA_DEGREE_CUTOFF, inverse=False)
        zeta_coefficients = euler_product_coefficients(q, FORMULA_DEGREE_CUTOFF, inverse=True)
        expected_determinant = [1, -q] + [0] * (FORMULA_DEGREE_CUTOFF - 1)
        expected_zeta = [q**n for n in range(FORMULA_DEGREE_CUTOFF + 1)]
        determinant_matches = determinant_coefficients == expected_determinant
        zeta_matches = zeta_coefficients == expected_zeta
        all_exact_checks &= determinant_matches and zeta_matches
        euler_results[str(q)] = {
            "determinant_product_coefficients": determinant_coefficients,
            "expected_1_minus_q_u": expected_determinant,
            "determinant_matches": determinant_matches,
            "zeta_product_coefficients": zeta_coefficients,
            "expected_one_over_1_minus_q_u": expected_zeta,
            "zeta_matches": zeta_matches,
        }
        ledger = repetition_ledger(q, FORMULA_DEGREE_CUTOFF)
        all_exact_checks &= all(bool(row["matches"]) for row in ledger)
        ledgers[str(q)] = ledger

    return {
        "schema_version": "1.0.0",
        "session_id": SESSION_ID,
        "candidate_id": CANDIDATE_ID,
        "run_id": "SD-C01-frozen-v1",
        "source_lock": {
            "family": "symbolic dynamics / finite-state full shifts and finite-memory controls",
            "q_values": list(Q_VALUES),
            "clock": "constant roof log(q) per symbol for the frozen arithmetic skeleton",
            "normalization": "u=q^{-s}",
            "determinant_convention": "D_q(s)=zeta_sigma(q^{-s})^{-1}=1-q^{1-s}",
            "forbidden_data_respected": True,
            "riemann_zero_data_used": False,
        },
        "reproducibility": {
            "master_seed": MASTER_SEED,
            "unitary_cocycle_seed": UNITARY_SEED,
            "precision": {"exact": "Python arbitrary-precision integers", "numerical_decimal_digits": precision},
            "cutoff": {
                "formula_and_euler_degree": FORMULA_DEGREE_CUTOFF,
                "brute_necklace_by_q": BRUTE_NECKLACE_CUTOFFS,
                "brute_irreducible_by_q": BRUTE_IRREDUCIBLE_CUTOFFS,
                "root_count_T_values": list(ROOT_COUNT_T_VALUES),
            },
        },
        "exact": {
            "evidence_status": "PROVED",
            "necklace_irreducible_identity_rows": exact_rows,
            "euler_product": euler_results,
            "repetition_ledgers": ledgers,
            "all_computational_identities_pass": all_exact_checks,
            "finite_memory_divisor_obstruction": {
                "evidence_status": "PROVED",
                "statement": "Every nonzero determinant det(I-B(s)) from a finite graph, finitely many positive edge roofs, finite edge weights, and finite-dimensional unitary cocycles is an exponential polynomial and has n_D(R)=O(R).",
                "derivation": [
                    "Each matrix entry is a finite sum of c*exp(-tau*s).",
                    "The finite Leibniz expansion of the determinant is a finite sum sum_k c_k*exp(-lambda_k*s), with lambda_k>=0.",
                    "A nonzero exponential polynomial is entire of finite exponential type.",
                    "Jensen's formula, centered at any fixed nonzero-value point and followed by disk inclusion, bounds its zero count with multiplicity by O(R).",
                ],
                "comparison_benchmark": "Riemann-von Mangoldt has order T log T; theorem-level benchmark only, no zero table used.",
                "stop_rule_triggered": True,
            },
        },
        "numerical": {
            "finite_unitary_lattice_control": lattice_unitary_control(),
            "nonlattice_control": nonlattice_root_count_control(precision),
        },
        "claim_boundary": "Exact finite-degree identities and the stated exponential-polynomial theorem are separated from numerical rectangle root counts.",
        "route_b_invocation_allowed": False,
    }


def write_results(output_dir: Path, precision: int = DECIMAL_PRECISION) -> dict[str, object]:
    output_dir.mkdir(parents=True, exist_ok=True)
    results = build_results(precision)
    json_path = output_dir / "sd_c01_results.json"
    json_path.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    csv_path = output_dir / "sd_c01_exact_counts.csv"
    fields = [
        "candidate_id",
        "evidence_status",
        "seed",
        "precision",
        "cutoff",
        "q",
        "degree",
        "formula_count",
        "brute_necklace_count",
        "brute_irreducible_count",
        "necklace_matches",
        "irreducible_matches",
    ]
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in results["exact"]["necklace_irreducible_identity_rows"]:  # type: ignore[index]
            writer.writerow(
                {
                    "candidate_id": CANDIDATE_ID,
                    "evidence_status": "PROVED",
                    "seed": MASTER_SEED,
                    "precision": "exact_integer",
                    "cutoff": FORMULA_DEGREE_CUTOFF,
                    **row,
                }
            )
    return results


if __name__ == "__main__":
    default_output = Path(__file__).resolve().parents[1] / "results"
    built = write_results(default_output)
    print(json.dumps({"candidate_id": CANDIDATE_ID, "passed": built["exact"]["all_computational_identities_pass"]}))
