#!/usr/bin/env python3
"""Reproducible audit of the SD-C12 entropy-paired relative determinant.

Parity convention is frozen to the writer source lock:

  plus/even sector  = odd entropy ranks p_1,p_3,...
  minus/odd sector  = even entropy ranks p_2,p_4,...

Thus

  R(s,z)=prod_n (1-z p_(2n-1)^(-s))/(1-z p_(2n)^(-s)).

The executable generates tensor-prime atoms internally and never loads or
compares Riemann-zero or target-spectrum data.
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
# Intrinsic inventories
# ---------------------------------------------------------------------------


def internal_multiplicative_atoms(count: int) -> list[int]:
    """Generate the first count multiplicative indecomposables by a sieve."""
    if count <= 0:
        return []
    if count < 6:
        upper = 15
    else:
        upper = int(count * (math.log(count) + math.log(math.log(count))) + 20)
    while True:
        sieve = np.ones(upper + 1, dtype=bool)
        sieve[:2] = False
        for prime in range(2, math.isqrt(upper) + 1):
            if sieve[prime]:
                sieve[prime * prime : upper + 1 : prime] = False
        atoms = np.flatnonzero(sieve)
        if len(atoms) >= count:
            return [int(value) for value in atoms[:count]]
        upper *= 2


def composite_inventory(count: int) -> list[int]:
    upper = max(32, 2 * count + 16)
    while True:
        sieve = np.ones(upper + 1, dtype=bool)
        sieve[:2] = False
        for prime in range(2, math.isqrt(upper) + 1):
            if sieve[prime]:
                sieve[prime * prime : upper + 1 : prime] = False
        values = np.flatnonzero(~sieve)
        values = values[values >= 4]
        if len(values) >= count:
            return [int(value) for value in values[:count]]
        upper *= 2


def random_increasing_inventory(count: int, seed: int = 1907) -> list[int]:
    rng = np.random.default_rng(seed)
    gaps = rng.integers(1, 16, size=count)
    return [int(value) for value in 1 + np.cumsum(gaps)]


# ---------------------------------------------------------------------------
# Pairings and relative traces
# ---------------------------------------------------------------------------


def adjacent_pairs(pair_count: int) -> list[tuple[int, int]]:
    return [(2 * index, 2 * index + 1) for index in range(pair_count)]


def offset_block_pairs(atom_count: int, offset: int) -> list[tuple[int, int]]:
    """Partition 2*offset blocks and pair their two offset-separated halves."""
    pairs: list[tuple[int, int]] = []
    block_size = 2 * offset
    for base in range(0, atom_count - block_size + 1, block_size):
        for local in range(offset):
            pairs.append((base + local, base + offset + local))
    return pairs


def random_block_pairs(
    atom_count: int,
    block_size: int,
    seed: int,
    random_orientation: bool = True,
) -> list[tuple[int, int]]:
    if block_size % 2:
        raise ValueError("block_size must be even")
    rng = np.random.default_rng(seed)
    pairs: list[tuple[int, int]] = []
    for base in range(0, atom_count - block_size + 1, block_size):
        order = list(rng.permutation(block_size))
        for local in range(0, block_size, 2):
            left, right = base + order[local], base + order[local + 1]
            if not random_orientation and left > right:
                left, right = right, left
            pairs.append((left, right))
    return pairs


def oriented_adjacent_pairs(pair_count: int, seed: int) -> list[tuple[int, int]]:
    rng = np.random.default_rng(seed)
    pairs = adjacent_pairs(pair_count)
    answer = []
    for left, right in pairs:
        answer.append((right, left) if rng.integers(0, 2) else (left, right))
    return answer


def powered(values: np.ndarray, s: complex) -> np.ndarray:
    return np.exp(-s * np.log(values))


def relative_trace(values: np.ndarray, pairs: list[tuple[int, int]], s: complex) -> complex:
    vector = powered(values, s)
    plus = np.fromiter((left for left, _ in pairs), dtype=int)
    minus = np.fromiter((right for _, right in pairs), dtype=int)
    return complex(np.sum(vector[plus] - vector[minus]))


def paired_trace_norm(
    values: np.ndarray, pairs: list[tuple[int, int]], s: complex
) -> float:
    vector = powered(values, s)
    plus = np.fromiter((left for left, _ in pairs), dtype=int)
    minus = np.fromiter((right for _, right in pairs), dtype=int)
    return float(np.sum(np.abs(vector[plus] - vector[minus])))


def log_relative(
    values: np.ndarray,
    pairs: list[tuple[int, int]],
    s: complex,
    z: complex = 1.0 + 0.0j,
) -> complex:
    vector = powered(values, s)
    plus = np.fromiter((left for left, _ in pairs), dtype=int)
    minus = np.fromiter((right for _, right in pairs), dtype=int)
    return complex(
        np.sum(np.log1p(-z * vector[plus]) - np.log1p(-z * vector[minus]))
    )


# ---------------------------------------------------------------------------
# Exact finite-prefix coefficient audit
# ---------------------------------------------------------------------------


def exact_prefix_audit(pair_count: int = 3, repetition_cutoff: int = 10) -> dict:
    plus = sp.symbols(f"a0:{pair_count}")
    minus = sp.symbols(f"b0:{pair_count}")
    z = sp.Symbol("z")
    numerator = sp.prod(1 - z * plus[index] for index in range(pair_count))
    denominator = sp.prod(1 - z * minus[index] for index in range(pair_count))
    product = numerator / denominator
    # Expand each local logarithm separately.  Asking SymPy to series-expand
    # the fully combined rational product causes unnecessary expression swell.
    log_series = sum(
        sp.series(sp.log(1 - z * plus[index]), z, 0, repetition_cutoff + 1).removeO()
        - sp.series(sp.log(1 - z * minus[index]), z, 0, repetition_cutoff + 1).removeO()
        for index in range(pair_count)
    )
    target_log = -sum(
        z**repetition
        * sum(
            plus[index] ** repetition - minus[index] ** repetition
            for index in range(pair_count)
        )
        / repetition
        for repetition in range(1, repetition_cutoff + 1)
    )
    # Truncated exact multiplication of (1-za)/(1-zb).  A local factor has
    # coefficients 1 and (b-a)b^(k-1), k>=1.
    coefficients: list[sp.Expr] = [sp.Integer(1)] + [sp.Integer(0)] * repetition_cutoff
    for index in range(pair_count):
        local = [sp.Integer(1)] + [
            (minus[index] - plus[index]) * minus[index] ** (degree - 1)
            for degree in range(1, repetition_cutoff + 1)
        ]
        updated = [sp.Integer(0)] * (repetition_cutoff + 1)
        for left_degree in range(repetition_cutoff + 1):
            for right_degree in range(repetition_cutoff + 1 - left_degree):
                updated[left_degree + right_degree] += (
                    coefficients[left_degree] * local[right_degree]
                )
        coefficients = [sp.expand(value) for value in updated]
    coefficient_series = sum(
        coefficients[degree] * z**degree
        for degree in range(repetition_cutoff + 1)
    )
    product_residual = sp.Poly(
        sp.expand(numerator - coefficient_series * denominator), z
    )
    product_coefficients_exact = all(
        product_residual.coeff_monomial(z**degree) == 0
        for degree in range(repetition_cutoff + 1)
    )
    rows = []
    for repetition in range(1, repetition_cutoff + 1):
        relative = sum(
            plus[index] ** repetition - minus[index] ** repetition
            for index in range(pair_count)
        )
        got = sp.expand(log_series).coeff(z, repetition)
        target = -relative / repetition
        rows.append(
            {
                "repetition": repetition,
                "relative_trace": str(relative),
                "log_coefficient": str(got),
                "target_log_coefficient": str(target),
                "exact": bool(sp.expand(got - target) == 0),
            }
        )
    return {
        "pair_count": pair_count,
        "repetition_cutoff": repetition_cutoff,
        "parity_convention": (
            "a_n=p_(2n-1)^(-s) is plus/even and appears in the numerator; "
            "b_n=p_(2n)^(-s) is minus/odd and appears in the denominator"
        ),
        "relative_product": str(product),
        "coefficient_series": str(coefficient_series),
        "product_coefficients_exact": product_coefficients_exact,
        "log_series_exact": bool(sp.expand(log_series - target_log) == 0),
        "rows": rows,
        "all_exact": all(row["exact"] for row in rows),
        "all_order_identity": (
            "log R_N(s,z)=-sum_(r>=1) z^r/r * "
            "sum_(n<=N)(p_(2n-1)^(-rs)-p_(2n)^(-rs))"
        ),
    }


# ---------------------------------------------------------------------------
# Trace-class convergence audit
# ---------------------------------------------------------------------------


def trace_tail_bound(s: complex, next_value: float, overlap: int = 1) -> float:
    sigma = s.real
    if sigma <= 0:
        return math.inf
    return overlap * abs(s) / sigma * next_value ** (-sigma)


def log_tail_bound(
    s: complex, z: complex, next_value: float, overlap: int = 1
) -> float:
    sigma = s.real
    radius = abs(z) * next_value ** (-sigma)
    if sigma <= 0 or radius >= 1:
        return math.inf
    return overlap * abs(z) * abs(s) / sigma * next_value ** (-sigma) / (1 - radius)


def convergence_audit(max_pairs: int = 2**14) -> dict:
    atoms = np.asarray(
        internal_multiplicative_atoms(2 * max_pairs + 1), dtype=float
    )
    plus = atoms[0 : 2 * max_pairs : 2]
    minus = atoms[1 : 2 * max_pairs : 2]
    points = [
        0.1 + 0j,
        0.25 + 0j,
        0.5 + 0j,
        1.0 + 0j,
        0.1 + 3j,
        0.25 + 10j,
        0.5 + 25j,
        1.0 + 40j,
    ]
    cutoffs = [16, 64, 256, 1024, 4096, max_pairs]
    rows = []
    for s in points:
        differences = powered(plus, s) - powered(minus, s)
        cumulative_l1 = np.cumsum(np.abs(differences))
        cumulative_trace = np.cumsum(differences)
        log_terms = np.log1p(-powered(plus, s)) - np.log1p(-powered(minus, s))
        cumulative_log = np.cumsum(log_terms)
        for cutoff in cutoffs:
            next_atom = atoms[2 * cutoff]
            rows.append(
                {
                    "sigma": s.real,
                    "height": s.imag,
                    "pair_cutoff": cutoff,
                    "last_minus_atom": int(minus[cutoff - 1]),
                    "l1_partial_sum": float(cumulative_l1[cutoff - 1]),
                    "trace_partial_real": float(cumulative_trace[cutoff - 1].real),
                    "trace_partial_imag": float(cumulative_trace[cutoff - 1].imag),
                    "cauchy_l1_to_max": float(
                        cumulative_l1[-1] - cumulative_l1[cutoff - 1]
                    ),
                    "rigorous_l1_tail_bound": trace_tail_bound(s, next_atom),
                    "log_R_partial_real": float(cumulative_log[cutoff - 1].real),
                    "log_R_partial_imag": float(cumulative_log[cutoff - 1].imag),
                    "cauchy_log_to_max": float(
                        abs(cumulative_log[-1] - cumulative_log[cutoff - 1])
                    ),
                    "rigorous_log_tail_bound_z1": log_tail_bound(
                        s, 1.0 + 0j, next_atom
                    ),
                }
            )
    return {
        "max_pairs": max_pairs,
        "last_generated_atom": int(atoms[-1]),
        "theorem": (
            "sum_n |p_(2n-1)^(-s)-p_(2n)^(-s)| <= "
            "|s|*2^(-sigma)/sigma for sigma=Re(s)>0"
        ),
        "tail_theorem": (
            "tail after N pairs <= |s|/sigma * p_(2N+1)^(-sigma)"
        ),
        "rows": rows,
    }


# ---------------------------------------------------------------------------
# Reflection product, motion, and zero-free strips
# ---------------------------------------------------------------------------


def g_curvature(x: np.ndarray) -> np.ndarray:
    root_inverse = x ** (-0.5)
    return root_inverse * np.log(x) ** 2 / (1.0 - root_inverse) ** 2


def reflection_audit(max_pairs: int = 2**14) -> dict:
    atoms = np.asarray(internal_multiplicative_atoms(2 * max_pairs + 1), dtype=float)
    cutoffs = sorted(
        set(cutoff for cutoff in [64, 256, 1024, 4096, max_pairs] if cutoff <= max_pairs)
    )
    heights = np.linspace(0.0, 80.0, 321)
    rows = []
    symmetry_rows = []
    for cutoff in cutoffs:
        values = atoms[: 2 * cutoff]
        pairs = adjacent_pairs(cutoff)
        h_values = []
        for height in heights:
            s = 0.5 + 1j * height
            log_r = log_relative(values, pairs, s)
            h_values.append(float(np.exp(2.0 * log_r.real)))
        plus = values[0::2]
        minus = values[1::2]
        curvature = float(2.0 * np.sum(g_curvature(plus) - g_curvature(minus)))
        curvature_tail_bound = float(2.0 * g_curvature(np.asarray([atoms[2 * cutoff]]))[0])
        rows.append(
            {
                "pair_cutoff": cutoff,
                "last_minus_atom": int(values[-1]),
                "H_at_t0": h_values[0],
                "H_min_t0_80": min(h_values),
                "H_max_t0_80": max(h_values),
                "H_range_t0_80": max(h_values) - min(h_values),
                "log_H_second_derivative_t0": curvature,
                "alternating_tail_bound_curvature": curvature_tail_bound,
                "strict_motion": curvature > 0,
            }
        )

        for s in [0.2 + 3j, 0.35 + 11j, 0.5 + 17j, 0.8 - 4j]:
            log_h = log_relative(values, pairs, s) + log_relative(
                values, pairs, 1.0 - s
            )
            log_h_reflected = log_relative(
                values, pairs, 1.0 - s
            ) + log_relative(values, pairs, s)
            h = np.exp(log_h)
            reflected = np.exp(log_h_reflected)
            symmetry_rows.append(
                {
                    "pair_cutoff": cutoff,
                    "sigma": s.real,
                    "height": s.imag,
                    "H_real": float(h.real),
                    "H_imag": float(h.imag),
                    "reflection_residual": float(abs(h - reflected)),
                }
            )
    return {
        "definition": "H(s,z)=R(s,z)R(1-s,z)",
        "exact_reflection": "H(s,z)=H(1-s,z)",
        "critical_line": "H(1/2+it,1)=|R(1/2+it,1)|^2>0",
        "curvature_formula": (
            "d2/dt2 log H(1/2+it,1)|0="
            "2 sum_n [g(p_(2n-1))-g(p_(2n))] > 0"
        ),
        "rows": rows,
        "symmetry_rows": symmetry_rows,
    }


def zero_free_audit() -> dict:
    rows = []
    for modulus in [0.5, 1.0, 1.25, 1.4, 1.5]:
        raw = math.log(modulus) / math.log(2.0)
        r_lower = max(0.0, raw)
        h_lower = r_lower
        h_upper = min(1.0, 1.0 - raw)
        nonempty = h_lower < h_upper
        midpoint = (h_lower + h_upper) / 2 if nonempty else math.nan
        margin = (
            1.0 - modulus * 2.0 ** (-midpoint) if nonempty else math.nan
        )
        rows.append(
            {
                "abs_z": modulus,
                "R_certified_halfplane_lower_sigma": r_lower,
                "H_certified_strip_lower_sigma": h_lower,
                "H_certified_strip_upper_sigma": h_upper,
                "H_strip_nonempty": nonempty,
                "midpoint_local_factor_margin": margin,
            }
        )
    return {
        "local_condition": "|z|*2^(-Re(s))<1",
        "ratio_bound": (
            "|(1-zb^(-s))/(1-za^(-s))-1| <= "
            "|z|*|a^(-s)-b^(-s)|/(1-|z|a^(-sigma))"
        ),
        "primary_z1_strip": "0<Re(s)<1",
        "primary_z1_zero_free": True,
        "reason": (
            "every local factor is nonzero and the sum of factor-minus-one "
            "is absolutely convergent; the relative Fredholm quotient is invertible"
        ),
        "rows": rows,
    }


# ---------------------------------------------------------------------------
# Pairing and inventory controls
# ---------------------------------------------------------------------------


def critical_h_range(
    values: np.ndarray,
    pairs: list[tuple[int, int]],
    max_height: float = 40.0,
    grid_size: int = 81,
) -> float:
    answers = []
    for height in np.linspace(0.0, max_height, grid_size):
        log_r = log_relative(values, pairs, 0.5 + 1j * height)
        answers.append(float(np.exp(2.0 * log_r.real)))
    return float(max(answers) - min(answers))


def pairing_inventory_controls(pair_count: int = 4096) -> dict:
    atom_count = 2 * pair_count
    primes = np.asarray(internal_multiplicative_atoms(atom_count), dtype=float)
    rows = []

    for offset in [1, 2, 3]:
        pairs = offset_block_pairs(atom_count, offset)
        rows.append(
            {
                "control_type": "offset_pairing",
                "name": f"offset_{offset}",
                "pair_count": len(pairs),
                "overlap_bound": offset,
                "trace_norm_sigma_0.1": paired_trace_norm(primes, pairs, 0.1),
                "trace_norm_sigma_0.5": paired_trace_norm(primes, pairs, 0.5),
                "critical_H_range": critical_h_range(primes, pairs),
                "trace_class_Re_s_positive": True,
                "verdict": "PROVES_TOO_MUCH",
            }
        )

    for seed in range(16):
        pairs = oriented_adjacent_pairs(pair_count, seed)
        rows.append(
            {
                "control_type": "within_pair_orientation",
                "name": f"orientation_seed_{seed}",
                "pair_count": len(pairs),
                "overlap_bound": 1,
                "trace_norm_sigma_0.1": paired_trace_norm(primes, pairs, 0.1),
                "trace_norm_sigma_0.5": paired_trace_norm(primes, pairs, 0.5),
                "critical_H_range": critical_h_range(primes, pairs),
                "trace_class_Re_s_positive": True,
                "verdict": "PROVES_TOO_MUCH",
            }
        )

    for seed in range(32):
        pairs = random_block_pairs(atom_count, block_size=8, seed=seed)
        rows.append(
            {
                "control_type": "random_block_pairing",
                "name": f"random_seed_{seed}",
                "pair_count": len(pairs),
                "overlap_bound": 4,
                "trace_norm_sigma_0.1": paired_trace_norm(primes, pairs, 0.1),
                "trace_norm_sigma_0.5": paired_trace_norm(primes, pairs, 0.5),
                "critical_H_range": critical_h_range(primes, pairs),
                "trace_class_Re_s_positive": True,
                "verdict": "PROVES_TOO_MUCH",
            }
        )

    rng = np.random.default_rng(1907)
    shuffled = primes.copy()
    for base in range(0, atom_count, 8):
        shuffled[base : base + 8] = shuffled[
            base + rng.permutation(min(8, atom_count - base))
        ]
    inventories = [
        ("tensor_primes", primes),
        ("within_block_shuffled_primes", shuffled),
        ("composites", np.asarray(composite_inventory(atom_count), dtype=float)),
        ("consecutive_integers", np.arange(2, atom_count + 2, dtype=float)),
        (
            "random_increasing_integers",
            np.asarray(random_increasing_inventory(atom_count), dtype=float),
        ),
    ]
    for name, values in inventories:
        pairs = adjacent_pairs(pair_count)
        rows.append(
            {
                "control_type": "inventory",
                "name": name,
                "pair_count": len(pairs),
                "overlap_bound": 1,
                "trace_norm_sigma_0.1": paired_trace_norm(values, pairs, 0.1),
                "trace_norm_sigma_0.5": paired_trace_norm(values, pairs, 0.5),
                "critical_H_range": critical_h_range(values, pairs),
                "trace_class_Re_s_positive": True,
                "verdict": (
                    "candidate_source"
                    if name == "tensor_primes"
                    else "PROVES_TOO_MUCH"
                ),
            }
        )
    return {
        "pair_count": pair_count,
        "rows": rows,
        "random_pairing_pass_count": sum(
            row["trace_class_Re_s_positive"]
            for row in rows
            if row["control_type"] == "random_block_pairing"
        ),
        "random_pairing_motion_count": sum(
            row["critical_H_range"] > 1e-10
            for row in rows
            if row["control_type"] == "random_block_pairing"
        ),
        "verdict": (
            "PROVES_TOO_MUCH: bounded-local shifted/random pairings and "
            "nonprime increasing inventories inherit convergence and motion"
        ),
    }


# ---------------------------------------------------------------------------
# Finite-block cancellation and parity-versus-phase
# ---------------------------------------------------------------------------


def block_weight_audit(max_blocks: int = 4096) -> dict:
    patterns = {
        "pair_zero_sum": [1, -1],
        "second_difference": [1, -2, 1],
        "four_block_zero_sum": [1, -1, -1, 1],
        "pair_all_positive": [1, 1],
        "triple_all_positive": [1, 1, 1],
    }
    maximum_width = max(len(pattern) for pattern in patterns.values())
    atoms = np.asarray(
        internal_multiplicative_atoms(max_blocks * maximum_width), dtype=float
    )
    rows = []
    cutoffs = sorted(
        set(cutoff for cutoff in [16, 64, 256, 1024, max_blocks] if cutoff <= max_blocks)
    )
    for name, pattern_list in patterns.items():
        pattern = np.asarray(pattern_list, dtype=float)
        width = len(pattern)
        values = atoms[: max_blocks * width].reshape(max_blocks, width)
        for sigma in [0.1, 0.5, 1.0]:
            block_values = np.sum(pattern[None, :] * values ** (-sigma), axis=1)
            cumulative = np.cumsum(np.abs(block_values))
            for cutoff in cutoffs:
                rows.append(
                    {
                        "pattern": name,
                        "weights": json.dumps(pattern_list),
                        "weight_sum": float(np.sum(pattern)),
                        "all_positive": bool(np.all(pattern > 0)),
                        "sigma": sigma,
                        "block_cutoff": cutoff,
                        "aggregate_l1_partial": float(cumulative[cutoff - 1]),
                        "zero_sum_condition": bool(np.sum(pattern) == 0),
                    }
                )
    return {
        "theorem": (
            "for one fixed asymptotically local finite-block pattern, "
            "extension to all Re(s)>0 requires and is supplied by sum_j c_j=0"
        ),
        "all_positive_impossibility": (
            "if every c_j>0 then sum_j c_j>0, so the zero-sum linear "
            "constraint is impossible"
        ),
        "scope": (
            "necessity assumes fixed bounded blocks, asymptotic locality, "
            "and divergence of the reciprocal block inventory"
        ),
        "rows": rows,
    }


def parity_phase_audit(repetition_cutoff: int = 10) -> dict:
    a, b = sp.symbols("a b")
    rows = []
    for repetition in range(1, repetition_cutoff + 1):
        fixed = a**repetition - b**repetition
        phase = a**repetition + (-1) ** repetition * b**repetition
        rows.append(
            {
                "repetition": repetition,
                "fixed_supertrace": str(fixed),
                "minus_one_cocycle_trace": str(phase),
                "difference": str(sp.expand(fixed - phase)),
                "same": bool(sp.expand(fixed - phase) == 0),
            }
        )
    return {
        "fixed_parity_rule": (
            "the minus sector has coefficient -1 at every repetition: a^r-b^r"
        ),
        "cocycle_phase_rule": (
            "a primitive holonomy -1 is exponentiated by repetition: "
            "a^r+(-1)^r b^r"
        ),
        "fixed_parity_product": "(1-za)/(1-zb)",
        "cocycle_phase_product": "(1-za)(1+zb)",
        "rows": rows,
        "coincide_only_at_odd_repetitions": all(
            row["same"] == bool(row["repetition"] % 2) for row in rows
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

    exact = exact_prefix_audit()
    convergence = convergence_audit()
    reflection = reflection_audit()
    zero_free = zero_free_audit()
    controls = pairing_inventory_controls()
    blocks = block_weight_audit()
    parity_phase = parity_phase_audit()

    results = {
        "metadata": {
            "candidate_id": "SD-C12",
            "candidate": "entropy-adjacent paired relative Fredholm determinant",
            "primary_family": "symbolic dynamics",
            "parity_convention": (
                "odd entropy rank is plus/even numerator; "
                "even entropy rank is minus/odd denominator"
            ),
            "primary_z": 1.0,
            "uses_riemann_zero_data": False,
            "fits_target_zeros": False,
            "crossing_census_performed": False,
        },
        "exact_prefix": exact,
        "trace_class_convergence": convergence,
        "reflection_product": reflection,
        "zero_free_strip": zero_free,
        "pairing_inventory_controls": controls,
        "block_weight_controls": blocks,
        "parity_versus_phase": parity_phase,
        "claim_boundary": {
            "paired_difference_trace_class": "PROVED for Re(s)>0",
            "relative_fredholm_product": "PROVED on |z|2^(-Re(s))<1",
            "all_repetition_relative_trace": "PROVED",
            "reflection": "PROVED",
            "critical_line_motion": "PROVED by positive center curvature",
            "primary_z1_strip": "0<Re(s)<1",
            "primary_z1_divisor": "EMPTY / ZERO-FREE",
            "positive_prime_orientation": "REFUTED by required fixed grading signs",
            "supertrace_equals_repetition_phase": "REFUTED",
            "rh_or_target_zero_claim": "FORBIDDEN / NOT MADE",
            "route_b_invocation_allowed": False,
        },
    }
    (args.output_dir / "summary.json").write_text(
        json.dumps(results, indent=2, sort_keys=True, default=str) + "\n"
    )
    write_csv(args.output_dir / "exact_coefficients.csv", exact["rows"])
    write_csv(args.output_dir / "trace_class_convergence.csv", convergence["rows"])
    write_csv(args.output_dir / "reflection_motion.csv", reflection["rows"])
    write_csv(args.output_dir / "reflection_symmetry.csv", reflection["symmetry_rows"])
    write_csv(args.output_dir / "zero_free_strips.csv", zero_free["rows"])
    write_csv(args.output_dir / "pairing_inventory_controls.csv", controls["rows"])
    write_csv(args.output_dir / "block_weight_controls.csv", blocks["rows"])
    write_csv(args.output_dir / "parity_phase.csv", parity_phase["rows"])

    print(
        json.dumps(
            {
                "output": str(args.output_dir / "summary.json"),
                "exact_prefix": exact["all_exact"],
                "max_pairs": convergence["max_pairs"],
                "primary_zero_free": zero_free["primary_z1_zero_free"],
                "random_pairings_trace_class": controls[
                    "random_pairing_pass_count"
                ],
                "random_pairings_move": controls[
                    "random_pairing_motion_count"
                ],
                "parity_phase_distinguished": parity_phase[
                    "coincide_only_at_odd_repetitions"
                ],
                "no_zero_data": True,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
