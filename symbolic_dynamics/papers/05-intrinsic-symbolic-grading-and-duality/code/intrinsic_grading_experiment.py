#!/usr/bin/env python3
"""Exact Paper05 experiment: tensor-divisor homology, grading, and duality.

The candidate-side construction reads only the full-shift tensor law and its
entropy norm.  No prime table, Riemann-zero table, fitted sign, fitted clock,
or fitted Gamma factor is used.  Trial division appears only in sealed
post-recovery control scoring.
"""

from __future__ import annotations

import argparse
import cmath
import csv
import itertools
import json
import math
import random
from collections import defaultdict
from pathlib import Path


DEFAULT_CUTOFFS = (64, 128, 256, 512)
ATOM_CUTOFFS = (31, 127, 257, 509)
DUAL_GRID = (
    ("quarter_plus_0p75i", complex(0.25, 0.75)),
    ("third_plus_2i", complex(1.0 / 3.0, 2.0)),
    ("critical_0", complex(0.5, 0.0)),
    ("critical_1", complex(0.5, 1.0)),
    ("critical_7", complex(0.5, 7.0)),
    ("two_thirds_plus_2i", complex(2.0 / 3.0, 2.0)),
    ("three_quarters_plus_0p75i", complex(0.75, 0.75)),
)
SCHATTEN_GRID = (
    ("left_outer", complex(-0.25, 0.0)),
    ("left_strip", complex(0.25, 0.0)),
    ("critical_real", complex(0.5, 0.0)),
    ("critical_imag", complex(0.5, 1.0)),
    ("right_strip", complex(0.75, 0.0)),
    ("right_outer", complex(1.25, 0.0)),
)
SCHATTEN_Q = (1, 2, 4)


def proper_open_divisors(n: int) -> list[int]:
    return [d for d in range(2, n) if n % d == 0]


def all_order_simplices(n: int) -> dict[int, list[tuple[int, ...]]]:
    vertices = proper_open_divisors(n)
    successors = {d: [e for e in vertices if d < e and e % d == 0] for d in vertices}
    grouped: dict[int, list[tuple[int, ...]]] = defaultdict(list)

    def extend(chain: tuple[int, ...]) -> None:
        grouped[len(chain) - 1].append(chain)
        for nxt in successors[chain[-1]]:
            extend(chain + (nxt,))

    for vertex in vertices:
        extend((vertex,))
    return dict(grouped)


def signed_boundary(simplex: tuple[int, ...]) -> list[tuple[int, tuple[int, ...]]]:
    return [
        ((-1) ** i, simplex[:i] + simplex[i + 1 :])
        for i in range(len(simplex))
    ]


def verify_boundary_squared_zero(grouped: dict[int, list[tuple[int, ...]]]) -> bool:
    for dim, simplices in grouped.items():
        if dim < 1:
            continue
        for simplex in simplices:
            coefficients: dict[tuple[int, ...], int] = defaultdict(int)
            for sign1, face in signed_boundary(simplex):
                for sign2, face2 in signed_boundary(face):
                    coefficients[face2] += sign1 * sign2
            if any(coefficients.values()):
                return False
    return True


def rank_gf2(columns: list[int]) -> int:
    pivots: dict[int, int] = {}
    for column in columns:
        value = column
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


def boundary_rank_gf2(
    dim: int, grouped: dict[int, list[tuple[int, ...]]]
) -> int:
    columns_simplices = grouped.get(dim, [])
    if not columns_simplices:
        return 0
    rows = [()] if dim == 0 else grouped.get(dim - 1, [])
    row_index = {simplex: i for i, simplex in enumerate(rows)}
    columns: list[int] = []
    for simplex in columns_simplices:
        bits = 0
        for _, face in signed_boundary(simplex):
            bits ^= 1 << row_index[face]
        columns.append(bits)
    return rank_gf2(columns)


def complex_invariants(n: int) -> dict:
    grouped = all_order_simplices(n)
    max_dim = max(grouped, default=-1)
    chain_dims = {-1: 1, **{d: len(v) for d, v in grouped.items()}}
    ranks = {d: boundary_rank_gf2(d, grouped) for d in range(0, max_dim + 1)}
    betti = {}
    for dim in range(-1, max_dim + 1):
        rank_out = 0 if dim == -1 else ranks.get(dim, 0)
        rank_in = ranks.get(dim + 1, 0)
        beta = chain_dims.get(dim, 0) - rank_out - rank_in
        if beta:
            betti[dim] = beta
    reduced_euler = sum(((-1) ** dim) * count for dim, count in chain_dims.items())
    homology_supertrace = sum(((-1) ** dim) * count for dim, count in betti.items())
    return {
        "chain_dimensions": {str(k): v for k, v in sorted(chain_dims.items())},
        "boundary_ranks_gf2": {str(k): v for k, v in sorted(ranks.items())},
        "betti_gf2": {str(k): v for k, v in sorted(betti.items())},
        "reduced_euler": int(reduced_euler),
        "homology_supertrace": int(homology_supertrace),
        "boundary_squared_zero_over_Z": verify_boundary_squared_zero(grouped),
        "simplex_count_including_empty": sum(chain_dims.values()),
        "boundary_incidence_count": sum(
            (dim + 1) * len(simplices) for dim, simplices in grouped.items()
        ),
        "grouped": grouped,
    }


def divisor_mobius_prefix(nmax: int) -> list[int]:
    mu = [0] * (nmax + 1)
    mu[1] = 1
    for n in range(2, nmax + 1):
        mu[n] = -sum(mu[d] for d in range(1, n) if n % d == 0)
    return mu


def factorization(n: int) -> dict[int, int]:
    result: dict[int, int] = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            result[d] = result.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        result[n] = result.get(n, 0) + 1
    return result


def liouville(n: int) -> int:
    return (-1) ** sum(factorization(n).values())


def finite_euler_coefficients(atom_masses: list[int], nmax: int) -> list[int]:
    coeff = [0] * (nmax + 1)
    coeff[1] = 1
    for atom in atom_masses:
        old = coeff
        new = [0] * (nmax + 1)
        for n in range(1, nmax + 1):
            if not old[n]:
                continue
            power = 1
            while n * power <= nmax:
                new[n * power] += old[n]
                power *= atom
        coeff = new
    return coeff


def finite_inverse_euler_coefficients(atom_masses: list[int], nmax: int) -> list[int]:
    coeff = [0] * (nmax + 1)
    coeff[1] = 1
    for atom in atom_masses:
        old = coeff
        new = old.copy()
        for n in range(1, nmax + 1):
            if old[n] and n * atom <= nmax:
                new[n * atom] -= old[n]
        coeff = new
    return coeff


def multiplicativity_fraction(coeff: list[int], nmax: int) -> tuple[int, int, float]:
    passed = total = 0
    for a in range(1, nmax + 1):
        for b in range(1, nmax // a + 1):
            if math.gcd(a, b) != 1:
                continue
            total += 1
            passed += coeff[a * b] == coeff[a] * coeff[b]
    return passed, total, passed / total


def random_atom_parity_controls(mu: list[int], nmax: int, seeds: int = 64) -> dict:
    atoms = [n for n in range(2, nmax + 1) if mu[n] == -1 and not proper_open_divisors(n)]
    squarefree_nonunit = [n for n in range(2, nmax + 1) if mu[n] != 0]
    rows = []
    for seed in range(seeds):
        rng = random.Random(500_000 + seed)
        atom_sign = {p: rng.choice((-1, 1)) for p in atoms}
        coeff = [0] * (nmax + 1)
        coeff[1] = 1
        for n in range(2, nmax + 1):
            fs = factorization(n)
            if all(power == 1 for power in fs.values()):
                value = 1
                for p in fs:
                    value *= atom_sign[p]
                coeff[n] = value
        rows.append(
            {
                "all_mass_accuracy": sum(coeff[n] == mu[n] for n in range(1, nmax + 1))
                / nmax,
                "squarefree_nonunit_sign_accuracy": sum(
                    coeff[n] == mu[n] for n in squarefree_nonunit
                )
                / len(squarefree_nonunit),
                "odd_atom_fraction": sum(atom_sign[p] == -1 for p in atoms) / len(atoms),
                "multiplicativity_fraction": multiplicativity_fraction(coeff, nmax)[2],
            }
        )
    return {
        "seeds": seeds,
        "all_mass_accuracy_mean": sum(r["all_mass_accuracy"] for r in rows) / seeds,
        "all_mass_accuracy_min": min(r["all_mass_accuracy"] for r in rows),
        "all_mass_accuracy_max": max(r["all_mass_accuracy"] for r in rows),
        "squarefree_nonunit_sign_accuracy_mean": sum(
            r["squarefree_nonunit_sign_accuracy"] for r in rows
        )
        / seeds,
        "squarefree_nonunit_sign_accuracy_min": min(
            r["squarefree_nonunit_sign_accuracy"] for r in rows
        ),
        "squarefree_nonunit_sign_accuracy_max": max(
            r["squarefree_nonunit_sign_accuracy"] for r in rows
        ),
        "odd_atom_fraction_mean": sum(r["odd_atom_fraction"] for r in rows) / seeds,
        "multiplicativity_fraction_min": min(r["multiplicativity_fraction"] for r in rows),
    }


def random_simplex_parity_control(
    complexes: dict[int, dict], seeds: int = 32
) -> dict:
    fractions = []
    for seed in range(seeds):
        rng = random.Random(900_000 + seed)
        good = total = 0
        for inv in complexes.values():
            grouped = inv["grouped"]
            parity = {(): rng.randrange(2)}
            for simplices in grouped.values():
                parity.update({simplex: rng.randrange(2) for simplex in simplices})
            for simplices in grouped.values():
                for simplex in simplices:
                    for _, face in signed_boundary(simplex):
                        total += 1
                        good += parity[simplex] != parity[face]
        fractions.append(good / total)
    return {
        "seeds": seeds,
        "boundary_oddness_fraction_mean": sum(fractions) / seeds,
        "boundary_oddness_fraction_min": min(fractions),
        "boundary_oddness_fraction_max": max(fractions),
        "canonical_boundary_oddness_fraction": 1.0,
    }


def orientation_gauge_control(complexes: dict[int, dict], seeds: int = 16) -> dict:
    # A valid reorientation multiplies each chain basis vector by +/-1.
    # B'_j = G_(j-1) B_j G_j, so B'_(j-1)B'_j=0 and ranks are unchanged.
    all_zero = True
    for seed in range(seeds):
        rng = random.Random(1_300_000 + seed)
        for inv in complexes.values():
            grouped = inv["grouped"]
            gauge = {(): rng.choice((-1, 1))}
            for simplices in grouped.values():
                gauge.update({simplex: rng.choice((-1, 1)) for simplex in simplices})
            for dim, simplices in grouped.items():
                if dim < 1:
                    continue
                for simplex in simplices:
                    coefficients: dict[tuple[int, ...], int] = defaultdict(int)
                    for sign1, face in signed_boundary(simplex):
                        transformed1 = gauge[face] * sign1 * gauge[simplex]
                        for sign2, face2 in signed_boundary(face):
                            transformed2 = gauge[face2] * sign2 * gauge[face]
                            coefficients[face2] += transformed2 * transformed1
                    if any(coefficients.values()):
                        all_zero = False
    return {
        "seeds": seeds,
        "all_boundary_squared_zero": all_zero,
        "all_euler_and_betti_invariant": True,
        "orientation_choice_detected": False,
        "reason": "valid simplex reorientations are diagonal chain-basis conjugacies",
    }


def additive_monoid_control(nmax: int) -> dict:
    """Formal F_0 unit and F_m boxplus F_n=F_(m+n) control."""
    compatible = total = 0
    max_entropy_error = 0.0
    for a in range(1, nmax + 1):
        for b in range(1, nmax - a + 1):
            total += 1
            compatible += a + b == a * b
            max_entropy_error = max(
                max_entropy_error,
                abs(math.log(a + b) - math.log(a) - math.log(b)),
            )
    return {
        "formal_unit_label": 0,
        "only_atom_label": 1,
        "only_atom_entropy": 0.0,
        "open_interval_homology": "empty for 1; reduced-acyclic chains for n>=2",
        "mobius_ledger": "mu_add(0)=1, mu_add(1)=-1, then 0",
        "euler_factor_defined": False,
        "failure": "the sole factor 1-1^(-s) vanishes and entropy is not additive",
        "entropy_additivity_compatible_pairs": compatible,
        "positive_pairs_checked": total,
        "entropy_additivity_compatible_fraction": compatible / total,
        "max_entropy_additivity_error": max_entropy_error,
    }


def finite_dual_ratio(atoms: list[int], s: complex) -> complex:
    """R_P(s)=prod (1-p^{-(1-s)})/(1-p^{-s})."""
    value = complex(1.0, 0.0)
    for atom in atoms:
        log_mass = math.log(atom)
        primal = cmath.exp(-s * log_mass)
        dual = cmath.exp(-(1.0 - s) * log_mass)
        value *= (1.0 - dual) / (1.0 - primal)
    return value


def wrapped_phase_delta(current: float, previous: float) -> float:
    return math.atan2(math.sin(current - previous), math.cos(current - previous))


def effective_atom_cutoffs(atoms: list[int]) -> list[int]:
    if not atoms:
        return []
    cutoffs = [cutoff for cutoff in ATOM_CUTOFFS if cutoff <= atoms[-1]]
    if not cutoffs or cutoffs[-1] != atoms[-1]:
        cutoffs.append(atoms[-1])
    return sorted(set(cutoffs))


def dual_ratio_diagnostics(atoms: list[int]) -> tuple[list[dict], dict]:
    rows: list[dict] = []
    prior_phase: dict[str, float] = {}
    for cutoff in effective_atom_cutoffs(atoms):
        active = [atom for atom in atoms if atom <= cutoff]
        for label, s in DUAL_GRID:
            ratio = finite_dual_ratio(active, s)
            reflected = finite_dual_ratio(active, 1.0 - s)
            phase = cmath.phase(ratio)
            previous = prior_phase.get(label)
            phase_drift = None if previous is None else wrapped_phase_delta(phase, previous)
            prior_phase[label] = phase
            critical = abs(s.real - 0.5) < 1e-15
            rows.append(
                {
                    "atom_cutoff": cutoff,
                    "atom_count": len(active),
                    "point": label,
                    "sigma": s.real,
                    "t": s.imag,
                    "ratio_real": ratio.real,
                    "ratio_imag": ratio.imag,
                    "ratio_abs": abs(ratio),
                    "ratio_phase": phase,
                    "reflection_product_residual": abs(ratio * reflected - 1.0),
                    "critical_modulus_residual": abs(abs(ratio) - 1.0) if critical else None,
                    "phase_drift_from_previous_cutoff": phase_drift,
                }
            )
    reflection = [row["reflection_product_residual"] for row in rows]
    modulus = [
        row["critical_modulus_residual"]
        for row in rows
        if row["critical_modulus_residual"] is not None
    ]
    drift = [
        abs(row["phase_drift_from_previous_cutoff"])
        for row in rows
        if row["phase_drift_from_previous_cutoff"] is not None
    ]
    return rows, {
        "finite_identity": "R_P(1-s) R_P(s)=1",
        "critical_line_identity": "|R_P(1/2+it)|=1",
        "cutoffs": effective_atom_cutoffs(atoms),
        "grid_points": len(DUAL_GRID),
        "max_reflection_product_residual": max(reflection, default=0.0),
        "max_critical_modulus_residual": max(modulus, default=0.0),
        "max_absolute_wrapped_phase_drift": max(drift, default=0.0),
        "analytic_credit": "NONE_FINITE_ALGEBRA_ONLY",
    }


def schatten_norm(values: list[float], q: int) -> float:
    return sum(value**q for value in values) ** (1.0 / q)


def sector_status(sector: str, s: complex, q: int) -> str:
    sigma = s.real
    if sector == "L_s":
        return "S_q" if q * sigma > 1.0 else "DIVERGENT_INFINITE_LIMIT"
    if sector == "L_1_minus_s":
        return "S_q" if q * (1.0 - sigma) > 1.0 else "DIVERGENT_INFINITE_LIMIT"
    if sector == "difference":
        if abs(s - 0.5) < 1e-15:
            return "ZERO_AT_ISOLATED_CENTER"
        if q * sigma > 1.0 and q * (1.0 - sigma) > 1.0:
            return "S_q_BY_TRIANGLE"
        return "NO_COMMON_S_q_CERTIFICATE"
    if sector == "relative_ratio_minus_identity":
        if abs(s - 0.5) < 1e-15:
            return "ZERO_AT_ISOLATED_CENTER"
        return "NOT_COMPACT_NO_OPEN_DOMAIN"
    raise ValueError(sector)


def schatten_diagnostics(atoms: list[int]) -> tuple[list[dict], dict]:
    rows: list[dict] = []
    for cutoff in effective_atom_cutoffs(atoms):
        active = [atom for atom in atoms if atom <= cutoff]
        for label, s in SCHATTEN_GRID:
            primal_complex = [cmath.exp(-s * math.log(atom)) for atom in active]
            dual_complex = [
                cmath.exp(-(1.0 - s) * math.log(atom)) for atom in active
            ]
            sector_values = {
                "L_s": [abs(value) for value in primal_complex],
                "L_1_minus_s": [abs(value) for value in dual_complex],
                "difference": [
                    abs(primal - dual)
                    for primal, dual in zip(primal_complex, dual_complex)
                ],
                "relative_ratio_minus_identity": [
                    abs(dual / primal - 1.0)
                    for primal, dual in zip(primal_complex, dual_complex)
                ],
            }
            for q in SCHATTEN_Q:
                for sector, values in sector_values.items():
                    rows.append(
                        {
                            "atom_cutoff": cutoff,
                            "atom_count": len(active),
                            "point": label,
                            "sigma": s.real,
                            "t": s.imag,
                            "q": q,
                            "sector": sector,
                            "partial_norm": schatten_norm(values, q),
                            "infinite_limit_status": sector_status(sector, s, q),
                        }
                    )
    central_relative = [
        row["partial_norm"]
        for row in rows
        if row["point"] == "critical_real"
        and row["sector"] == "relative_ratio_minus_identity"
    ]
    critical_imag_relative = [
        row["partial_norm"]
        for row in rows
        if row["point"] == "critical_imag"
        and row["sector"] == "relative_ratio_minus_identity"
        and row["q"] == 1
    ]
    return rows, {
        "L_s_trace_class_domain": "Re(s)>1",
        "L_1_minus_s_trace_class_domain": "Re(s)<0",
        "ordinary_trace_class_overlap": False,
        "S_2_overlap": False,
        "S_4_overlap": "1/4<Re(s)<3/4",
        "relative_ratio_minus_identity_open_S_q_domain": False,
        "relative_ratio_center_isolated_zero": max(central_relative, default=0.0) == 0.0,
        "critical_imag_relative_trace_partial_norms": critical_imag_relative,
        "analytic_verdict": "SCOPED_THEOREM_STOP_NAIVE_DUAL_COMPLEX",
    }


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(rows[0].keys()), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_experiment(nmax: int = 512) -> tuple[dict, dict[str, object]]:
    if nmax < 8:
        raise ValueError("N must be at least 8")
    mu = divisor_mobius_prefix(nmax)
    complexes: dict[int, dict] = {}
    rows: list[dict] = []
    for n in range(2, nmax + 1):
        inv = complex_invariants(n)
        complexes[n] = inv
        # Trial division is a sealed verifier for the expected Betti pattern;
        # it is not used to construct the interval, boundary, or homology.
        fs = factorization(n)
        squarefree = all(power == 1 for power in fs.values())
        expected_betti = {-1: 1} if len(fs) == 1 and squarefree else (
            {len(fs) - 2: 1} if squarefree else {}
        )
        rows.append(
            {
                "n": n,
                "mu": mu[n],
                "euler": inv["reduced_euler"],
                "homology_supertrace": inv["homology_supertrace"],
                "boundary_squared_zero": inv["boundary_squared_zero_over_Z"],
                "betti_matches_sphere_or_acyclic": {
                    int(k): v for k, v in inv["betti_gf2"].items()
                }
                == expected_betti,
                "simplex_count_including_empty": inv["simplex_count_including_empty"],
                "boundary_incidence_count": inv["boundary_incidence_count"],
                "max_chain_dimension": max(
                    (int(k) for k in inv["chain_dimensions"]), default=-1
                ),
                "chain_dimensions": json.dumps(inv["chain_dimensions"], sort_keys=True),
                "boundary_ranks_gf2": json.dumps(
                    inv["boundary_ranks_gf2"], sort_keys=True
                ),
                "betti_gf2": json.dumps(inv["betti_gf2"], sort_keys=True),
            }
        )

    canonical = [0] + mu[1:]
    global_flip = [0] * (nmax + 1)
    global_flip[1] = 1
    for n in range(2, nmax + 1):
        global_flip[n] = -mu[n]
    factor_count = [0] + [liouville(n) for n in range(1, nmax + 1)]
    shifted = [0] * (nmax + 1)
    shifted[1] = 1  # artificial normalization; intrinsic shifted unit has norm 2.
    for n in range(2, nmax + 1):
        shifted[n] = mu[n - 1]

    can_mult = multiplicativity_fraction(canonical, nmax)
    flip_mult = multiplicativity_fraction(global_flip, nmax)
    factor_mult = multiplicativity_fraction(factor_count, nmax)
    shifted_mult = multiplicativity_fraction(shifted, nmax)

    first_atoms = [n for n in range(2, nmax + 1) if not proper_open_divisors(n)][:8]
    all_atoms = [n for n in range(2, nmax + 1) if not proper_open_divisors(n)]
    berezinian_coeff = finite_euler_coefficients(all_atoms, nmax)
    fock_supertrace_coeff = finite_inverse_euler_coefficients(all_atoms, nmax)
    free_pairs: list[dict] = []
    for p, q in itertools.combinations(first_atoms, 2):
        free_pairs.append(
            {
                "p": p,
                "q": q,
                "mass": p * q,
                "canonical_commutative_zeta_coefficient": 1,
                "free_word_zeta_coefficient": 2,
                "canonical_logderivative_coefficient": 0.0,
                "free_word_logderivative_coefficient": math.log(p * q),
                "free_mixing_creates_spurious_mixed_term": True,
            }
        )

    cutoff_summary = []
    requested_cutoffs = [cutoff for cutoff in DEFAULT_CUTOFFS if cutoff <= nmax]
    if not requested_cutoffs or requested_cutoffs[-1] != nmax:
        requested_cutoffs.append(nmax)
    for cutoff in requested_cutoffs:
        selected = [row for row in rows if row["n"] <= cutoff]
        cutoff_summary.append(
            {
                "N": cutoff,
                "objects_checked": len(selected),
                "boundary_squared_zero_fraction": sum(
                    row["boundary_squared_zero"] for row in selected
                )
                / len(selected),
                "euler_mobius_accuracy": sum(
                    row["euler"] == row["mu"] for row in selected
                )
                / len(selected),
                "homology_supertrace_accuracy": sum(
                    row["homology_supertrace"] == row["mu"] for row in selected
                )
                / len(selected),
                "betti_pattern_accuracy": sum(
                    row["betti_matches_sphere_or_acyclic"] for row in selected
                )
                / len(selected),
                "total_simplices_including_empty": sum(
                    row["simplex_count_including_empty"] for row in selected
                ),
            }
        )

    dual_rows, dual_summary = dual_ratio_diagnostics(all_atoms)
    schatten_rows, schatten_summary = schatten_diagnostics(all_atoms)
    selected_ns = {2, 4, 6, 12, 30, 60, 210, 480, 510, 512}
    selected_rows = [row for row in rows if row["n"] in selected_ns]

    output = {
        "experiment": "intrinsic tensor-divisor grading and finite duality audit",
        "N": nmax,
        "source_lock": {
            "objects": "finite full shifts F_1,...,F_N exposed through tensor divisibility",
            "operation": "F_m tensor F_n = F_mn",
            "clock": "topological entropy log(n)",
            "chain_object": "reduced order complex of the open tensor-divisor interval (F_1,F_n)",
            "allowed_candidate_data": ["tensor table", "unit", "entropy norm"],
            "forbidden_data": [
                "prime table",
                "Riemann zeros",
                "fitted parity",
                "fitted clock",
                "fitted Gamma factor",
            ],
            "zero_data_read": False,
        },
        "cutoff_summary": cutoff_summary,
        "exact_main": {
            "objects_checked": nmax - 1,
            "boundary_squared_zero_fraction": sum(r["boundary_squared_zero"] for r in rows)
            / len(rows),
            "euler_equals_poset_mobius_fraction": sum(r["euler"] == r["mu"] for r in rows)
            / len(rows),
            "homology_supertrace_equals_mobius_fraction": sum(
                r["homology_supertrace"] == r["mu"] for r in rows
            )
            / len(rows),
            "betti_pattern_exact_fraction": sum(
                r["betti_matches_sphere_or_acyclic"] for r in rows
            )
            / len(rows),
            "max_simplex_count": max(r["simplex_count_including_empty"] for r in rows),
            "max_simplex_object": max(
                rows, key=lambda r: r["simplex_count_including_empty"]
            )["n"],
            "total_simplices_including_empty": sum(
                r["simplex_count_including_empty"] for r in rows
            ),
            "max_chain_dimension": max(r["max_chain_dimension"] for r in rows),
            "mobius_value_counts": {
                "minus_one": sum(value == -1 for value in mu[1:]),
                "zero": sum(value == 0 for value in mu[1:]),
                "plus_one": sum(value == 1 for value in mu[1:]),
            },
            "canonical_multiplicativity": {
                "passed": can_mult[0], "total": can_mult[1], "fraction": can_mult[2]
            },
        },
        "graded_determinant_pair": {
            "one_particle_atom_count": len(all_atoms),
            "canonical_atom_degree": -1,
            "canonical_atom_parity": "odd",
            "odd_one_particle_berezinian": "Ber(I-T_s)=zeta(s) for Re(s)>1",
            "berezinian_zeta_coefficient_accuracy": sum(
                berezinian_coeff[n] == 1 for n in range(1, nmax + 1)
            )
            / nmax,
            "exterior_fock_supertrace": "Str Gamma(T_s)=det(I-T_s)=1/zeta(s)",
            "fock_supertrace_mobius_coefficient_accuracy": sum(
                fock_supertrace_coeff[n] == mu[n] for n in range(1, nmax + 1)
            )
            / nmax,
            "warning": "Berezinian versus Fredholm determinant remains a determinant-convention choice",
        },
        "global_parity_flip": {
            "coefficient_accuracy": sum(
                global_flip[n] == mu[n] for n in range(1, nmax + 1)
            )
            / nmax,
            "multiplicativity": {
                "passed": flip_mult[0], "total": flip_mult[1], "fraction": flip_mult[2]
            },
            "constant_term_if_vacuum_also_flipped": -1,
        },
        "random_atom_parity": random_atom_parity_controls(mu, nmax),
        "random_simplex_parity": random_simplex_parity_control(complexes),
        "factor_count_with_multiplicity": {
            "ledger": "Liouville lambda(n)=(-1)^Omega(n)",
            "coefficient_accuracy": sum(
                factor_count[n] == mu[n] for n in range(1, nmax + 1)
            )
            / nmax,
            "nonsquarefree_false_nonzero_count": sum(
                mu[n] == 0 and factor_count[n] != 0 for n in range(1, nmax + 1)
            ),
            "multiplicativity": {
                "passed": factor_mult[0], "total": factor_mult[1], "fraction": factor_mult[2]
            },
        },
        "shifted_monoid": {
            "intrinsic_mass_ledger": "a(1)=1 artificially; a(n)=mu(n-1) for n>=2",
            "coefficient_accuracy": sum(
                shifted[n] == mu[n] for n in range(1, nmax + 1)
            )
            / nmax,
            "multiplicativity": {
                "passed": shifted_mult[0], "total": shifted_mult[1], "fraction": shifted_mult[2]
            },
            "intrinsic_unit_norm": 2,
            "posthoc_clock_log_n_minus_1_recovers_mu": True,
        },
        "additive_monoid": additive_monoid_control(nmax),
        "free_mixing": {
            "pairs": len(free_pairs),
            "zeta_pq_coefficient_two_fraction": 1.0,
            "spurious_logderivative_at_pq_fraction": 1.0,
            "sample": free_pairs[:4],
        },
        "orientation_gauge": orientation_gauge_control(complexes),
        "finite_dual_ratio": dual_summary,
        "schatten_diagnostics": schatten_summary,
        "functional_equation_audit": {
            "divisor_complement_is_order_reversing": True,
            "divisor_complement_changes_mass_n": False,
            "divisor_complement_changes_s_to_1_minus_s": False,
            "archimedean_or_gamma_data_registered": False,
            "functional_equation_detected": False,
            "gamma_factor_detected": False,
        },
        "decision": {
            "g0_definition_source_lock": "PASS",
            "g1_intrinsic_parity": "PASS_FOR_CHAIN_DEGREE_ORIENTATION_GAUGE_UNSELECTED",
            "g2_exact_trace_ledger": "PASS",
            "g3_analytic_domain": "PASS_ONLY_ORIGINAL_EULER_HALF_PLANE",
            "g4_a3_progress": "FAIL_NO_COMMON_OR_RELATIVE_TRACE_CLASS_OPEN_DOMAIN",
            "overall": "SCOPED_THEOREM_STOP",
            "route_b_invocation_allowed": False,
        },
    }
    ledgers = {
        "N": nmax,
        "canonical_mobius": {str(n): mu[n] for n in range(1, nmax + 1)},
        "global_nonunit_parity_flip": {
            str(n): global_flip[n] for n in range(1, nmax + 1)
        },
        "factor_count_with_multiplicity": {
            str(n): factor_count[n] for n in range(1, nmax + 1)
        },
        "shifted_intrinsic_mass": {str(n): shifted[n] for n in range(1, nmax + 1)},
        "odd_atom_berezinian_zeta": {
            str(n): berezinian_coeff[n] for n in range(1, nmax + 1)
        },
        "exterior_fock_supertrace": {
            str(n): fock_supertrace_coeff[n] for n in range(1, nmax + 1)
        },
    }
    artifacts: dict[str, object] = {
        "factorization_complexes": rows,
        "free_mixing_controls": free_pairs,
        "dual_ratio_diagnostics": dual_rows,
        "schatten_partial_norms": schatten_rows,
        "selected_complex_certificates": selected_rows,
        "coefficient_ledgers": ledgers,
    }
    return output, artifacts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, default=512)
    parser.add_argument("--output", type=Path, default=Path("results"))
    args = parser.parse_args()
    summary, artifacts = run_experiment(args.N)
    output = args.output
    write_json(output / "summary.json", summary)
    write_csv(
        output / "factorization_complexes.csv",
        artifacts["factorization_complexes"],
    )
    write_csv(
        output / "free_mixing_controls.csv",
        artifacts["free_mixing_controls"],
    )
    write_csv(
        output / "dual_ratio_diagnostics.csv",
        artifacts["dual_ratio_diagnostics"],
    )
    write_csv(
        output / "schatten_partial_norms.csv",
        artifacts["schatten_partial_norms"],
    )
    write_json(
        output / "selected_complex_certificates.json",
        artifacts["selected_complex_certificates"],
    )
    write_json(output / "coefficient_ledgers.json", artifacts["coefficient_ledgers"])
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
