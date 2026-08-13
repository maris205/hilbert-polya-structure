#!/usr/bin/env python3
"""Reproducible SD-C09 exact-algebra and finite-prefix experiment.

The atom inventory is generated internally as the multiplicative
indecomposables of the positive integers and ordered by entropy ``log(p)``.
The script never loads Riemann-zero data and has no fitting objective.

Main candidate
--------------
    D_s = diag(p_1**(-s), ..., p_N**(-s))
    S e_j = e_(j+1)
    L_(alpha,s) = D_s + alpha D_s S + (1-alpha) S D_s.

The frozen candidate is alpha=1/2.  Alpha=0 and alpha=1 are target-only and
source-only phase-gauge controls.  All numerical root counts below refer to
the independently frozen scalar det(I-L_t^* L_t), never to target zeros.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.linalg import block_diag


def internal_multiplicative_atoms(count: int) -> list[int]:
    """Return the first ``count`` nonunit multiplicative indecomposables."""
    atoms: list[int] = []
    candidate = 2
    while len(atoms) < count:
        if not any(
            candidate % divisor == 0
            for divisor in range(2, math.isqrt(candidate) + 1)
        ):
            atoms.append(candidate)
        candidate += 1
    return atoms


def d_matrix(masses: list[int] | np.ndarray, s: complex) -> np.ndarray:
    return np.diag(np.exp(-s * np.log(np.asarray(masses, dtype=float))))


def successor(size: int, bidirectional: bool = False) -> np.ndarray:
    shift = np.diag(np.ones(size - 1), 1)
    return shift + shift.T if bidirectional else shift


def l_matrix(
    masses: list[int] | np.ndarray,
    s: complex,
    alpha: float = 0.5,
    bidirectional: bool = False,
    endpoint_phases: tuple[np.ndarray, np.ndarray] | None = None,
) -> np.ndarray:
    """Build the successor transfer, optionally with frozen endpoint phases."""
    diagonal = np.diag(d_matrix(masses, s))
    size = len(diagonal)
    answer = np.diag(diagonal).astype(complex)
    if endpoint_phases is None:
        source_phase = np.ones(size - 1, dtype=complex)
        target_phase = np.ones(size - 1, dtype=complex)
    else:
        source_phase, target_phase = endpoint_phases
    edge = (
        alpha * source_phase * diagonal[:-1]
        + (1.0 - alpha) * target_phase * diagonal[1:]
    )
    answer += np.diag(edge, 1)
    if bidirectional:
        answer += np.diag(edge, -1)
    return answer


def chiral(matrix: np.ndarray) -> np.ndarray:
    rows, columns = matrix.shape
    return np.block(
        [
            [np.zeros((rows, rows), dtype=complex), matrix],
            [matrix.conj().T, np.zeros((columns, columns), dtype=complex)],
        ]
    )


def schatten4_fourth_power(matrix: np.ndarray) -> float:
    gram = matrix.conj().T @ matrix
    return float(np.trace(gram @ gram).real)


def exact_successor_ledger(size: int = 4, max_power: int = 8) -> dict:
    variables = sp.symbols(f"x0:{size}")
    z = sp.symbols("z")
    diagonal = sp.diag(*variables)
    shift = sp.zeros(size)
    for index in range(size - 1):
        shift[index, index + 1] = 1
    transfer = diagonal + (diagonal * shift + shift * diagonal) / 2
    trace_rows = []
    for power in range(1, max_power + 1):
        value = sp.expand(sp.trace(transfer**power))
        target = sum(variable**power for variable in variables)
        trace_rows.append(
            {
                "power": power,
                "trace": str(value),
                "target": str(target),
                "exact": bool(sp.expand(value - target) == 0),
            }
        )
    determinant = sp.factor((sp.eye(size) - z * transfer).det())
    target_determinant = sp.prod(1 - z * variable for variable in variables)
    return {
        "size": size,
        "trace_rows": trace_rows,
        "determinant": str(determinant),
        "target_determinant": str(target_determinant),
        "determinant_exact": bool(
            sp.expand(determinant - target_determinant) == 0
        ),
        "proof_reason": "upper triangular with diagonal (x_0,...,x_(N-1))",
    }


def closed_walk_census(
    size: int = 5, max_length: int = 8, bidirectional: bool = False
) -> dict:
    adjacency = np.eye(size, dtype=int)
    adjacency += np.diag(np.ones(size - 1, dtype=int), 1)
    if bidirectional:
        adjacency += np.diag(np.ones(size - 1, dtype=int), -1)
    rows = []
    examples: list[list[int]] = []
    for length in range(1, max_length + 1):
        closed = mixed = 0
        for vertices in itertools.product(range(size), repeat=length):
            if all(
                adjacency[vertices[index], vertices[(index + 1) % length]]
                for index in range(length)
            ):
                closed += 1
                if len(set(vertices)) > 1:
                    mixed += 1
                    if len(examples) < 12:
                        examples.append(list(vertices))
        rows.append(
            {
                "length": length,
                "based_closed_walks": closed,
                "pure_loop_walks": size,
                "mixed_closed_walks": mixed,
            }
        )
    return {
        "size": size,
        "bidirectional": bidirectional,
        "rows": rows,
        "first_mixed_examples": examples,
    }


def bidirectional_failure_exact(size: int = 3) -> dict:
    variables = sp.symbols(f"x0:{size}")
    z = sp.symbols("z")
    diagonal = sp.diag(*variables)
    forward = sp.zeros(size)
    for index in range(size - 1):
        forward[index, index + 1] = 1
    adjacency = forward + forward.T
    transfer = diagonal + (diagonal * adjacency + adjacency * diagonal) / 2
    trace2_extra = sp.factor(
        sp.trace(transfer**2) - sum(variable**2 for variable in variables)
    )
    determinant = sp.factor((sp.eye(size) - z * transfer).det())
    target = sp.prod(1 - z * variable for variable in variables)
    return {
        "size": size,
        "trace2_extra": str(trace2_extra),
        "determinant": str(determinant),
        "target_determinant": str(target),
        "determinant_difference": str(sp.factor(determinant - target)),
        "ledger_exact": bool(sp.expand(determinant - target) == 0),
        "periodic_census": closed_walk_census(
            size=size, max_length=4, bidirectional=True
        ),
    }


def one_sided_random_k_gauge(seed: int = 907, size: int = 7) -> dict:
    rng = np.random.default_rng(seed)
    atoms = internal_multiplicative_atoms(size)
    coupling = rng.normal(size=(size, size)) + 1j * rng.normal(
        size=(size, size)
    )
    a_zero = d_matrix(atoms, 0.5) @ coupling
    b_zero = chiral(a_zero)
    rows = []
    for height in [-11.0, -3.25, -0.4, 0.0, 0.7, 4.5, 13.0]:
        phase = np.diag(
            np.exp(-1j * height * np.log(np.asarray(atoms, dtype=float)))
        )
        a_height = d_matrix(atoms, 0.5 + 1j * height) @ coupling
        b_height = chiral(a_height)
        gauge = block_diag(phase, np.eye(size))
        rows.append(
            {
                "height": height,
                "left_phase_error": float(
                    np.linalg.norm(a_height - phase @ a_zero)
                ),
                "chiral_gauge_error": float(
                    np.linalg.norm(
                        b_height - gauge @ b_zero @ gauge.conj().T
                    )
                ),
                "singular_max_error": float(
                    np.max(
                        np.abs(
                            np.linalg.svd(a_height, compute_uv=False)
                            - np.linalg.svd(a_zero, compute_uv=False)
                        )
                    )
                ),
                "chiral_eigen_max_error": float(
                    np.max(
                        np.abs(
                            np.linalg.eigvalsh(b_height)
                            - np.linalg.eigvalsh(b_zero)
                        )
                    )
                ),
            }
        )
    return {
        "seed": seed,
        "size": size,
        "atoms": atoms,
        "identity": "D_(1/2+it)K=U_t D_(1/2)K for arbitrary K",
        "rows": rows,
    }


def alpha_motion_controls(size: int = 8) -> dict:
    atoms = internal_multiplicative_atoms(size)
    heights = np.linspace(0.0, 40.0, 801)
    rows = []
    for alpha in [0.0, 0.125, 0.25, 0.5, 0.75, 0.875, 1.0]:
        reference = np.linalg.svd(
            l_matrix(atoms, 0.5, alpha), compute_uv=False
        )
        frobenius2 = []
        schatten4 = []
        singular_shifts = []
        for height in heights:
            transfer = l_matrix(atoms, 0.5 + 1j * height, alpha)
            frobenius2.append(float(np.linalg.norm(transfer) ** 2))
            schatten4.append(schatten4_fourth_power(transfer))
            singular_shifts.append(
                float(
                    np.linalg.norm(
                        np.linalg.svd(transfer, compute_uv=False) - reference
                    )
                )
            )
        rows.append(
            {
                "alpha": alpha,
                "frobenius_squared_range": float(
                    max(frobenius2) - min(frobenius2)
                ),
                "schatten4_fourth_power_range": float(
                    max(schatten4) - min(schatten4)
                ),
                "max_singular_l2_shift_vs_t0": float(max(singular_shifts)),
                "has_strict_singular_motion": bool(
                    max(singular_shifts) > 1e-8
                ),
            }
        )
    cosine = sp.symbols("c", real=True)
    n2_frobenius2 = sp.Rational(25, 24) + sp.sqrt(6) * cosine / 12
    n2_schatten4 = sp.expand(n2_frobenius2**2 - sp.Rational(1, 3))
    return {
        "size": size,
        "atoms": atoms,
        "height_grid": {"start": 0.0, "stop": 40.0, "points": 801},
        "rows": rows,
        "endpoint_identities": {
            "source_alpha_1": "L_(1,s)=D_s(I+S)=U_t L_(1,1/2)",
            "target_alpha_0": "L_(0,s)=(I+S)D_s=L_(0,1/2)U_t",
        },
        "n2_alpha_half_exact": {
            "cosine_definition": "c=cos(t log(3/2))",
            "frobenius_squared": str(n2_frobenius2),
            "schatten4_fourth_power": str(n2_schatten4),
            "strict_motion_certificate": bool(
                sp.diff(n2_schatten4, cosine) != 0
            ),
        },
    }


def crossing_scalar(
    masses: list[int] | np.ndarray,
    heights: np.ndarray | float,
    alpha: float = 0.5,
) -> np.ndarray:
    """Evaluate det(I-L_t^*L_t) by a Hermitian-tridiagonal recurrence."""
    height = np.asarray(heights, dtype=float)
    mass = np.asarray(masses, dtype=float)
    previous = np.ones_like(height)
    current = np.full_like(height, 1.0 - 1.0 / mass[0])
    for index in range(1, len(mass)):
        delta = math.log(mass[index] / mass[index - 1])
        edge_squared = (
            alpha**2 / mass[index - 1]
            + (1.0 - alpha) ** 2 / mass[index]
            + 2.0
            * alpha
            * (1.0 - alpha)
            / math.sqrt(mass[index - 1] * mass[index])
            * np.cos(height * delta)
        )
        gram_diagonal = 1.0 - 1.0 / mass[index] - edge_squared
        gram_offdiagonal_squared = edge_squared / mass[index - 1]
        following = (
            gram_diagonal * current
            - gram_offdiagonal_squared * previous
        )
        previous, current = current, following
    return current


def bisect_bracket(
    masses: list[int], left: float, right: float, iterations: int = 60
) -> float:
    left_value = float(crossing_scalar(masses, left))
    right_value = float(crossing_scalar(masses, right))
    if np.signbit(left_value) == np.signbit(right_value):
        raise ValueError("the interval is not a sign-changing bracket")
    for _ in range(iterations):
        midpoint = (left + right) / 2.0
        middle_value = float(crossing_scalar(masses, midpoint))
        if np.signbit(middle_value) == np.signbit(left_value):
            left, left_value = midpoint, middle_value
        else:
            right, right_value = midpoint, middle_value
    return (left + right) / 2.0


def sign_change_roots(masses: list[int], stop: float, step: float) -> list[float]:
    grid = np.arange(0.0, stop + step / 2.0, step)
    values = crossing_scalar(masses, grid)
    indices = np.flatnonzero(np.signbit(values[:-1]) != np.signbit(values[1:]))
    return [
        bisect_bracket(masses, float(grid[index]), float(grid[index + 1]))
        for index in indices
    ]


def exact_n2_crossing(maximum_height: float = 320.0) -> dict:
    frequency = math.log(3.0 / 2.0)
    theta = math.acos(math.sqrt(6.0) / 4.0)
    maximum_k = int(
        math.ceil(maximum_height * frequency / (2.0 * math.pi))
    ) + 2
    roots = []
    for k_value in range(-maximum_k, maximum_k + 1):
        for sign in [-1.0, 1.0]:
            root = (2.0 * math.pi * k_value + sign * theta) / frequency
            if 0.0 < root <= maximum_height:
                roots.append(root)
    return {
        "scalar": "(3-2*sqrt(6)*cos(t*log(3/2)))/24",
        "root_family": "t=(2*pi*k +/- acos(sqrt(6)/4))/log(3/2)",
        "theta": theta,
        "period": 2.0 * math.pi / frequency,
        "positive_roots_to_320": sorted(roots),
    }


def cutoff_zero_census() -> dict:
    cutoffs = [2, 3, 4, 8, 16, 32, 64, 128]
    horizons = [20, 40, 80, 160, 320]
    grid_step = 1.0 / 256.0
    validation_step = grid_step / 2.0
    exact_two = exact_n2_crossing(max(horizons))
    root_cache: dict[int, list[float]] = {}
    rows = []
    for cutoff in cutoffs:
        atoms = internal_multiplicative_atoms(cutoff)
        roots = sign_change_roots(atoms, max(horizons), grid_step)
        validation_roots = sign_change_roots(
            atoms, max(horizons), validation_step
        )
        root_cache[cutoff] = roots
        counts = {
            str(horizon): sum(root <= horizon + 1e-12 for root in roots)
            for horizon in horizons
        }
        validation_counts = {
            str(horizon): sum(
                root <= horizon + 1e-12 for root in validation_roots
            )
            for horizon in horizons
        }
        row = {
            "cutoff": cutoff,
            "last_atom": atoms[-1],
            "positive_sign_change_counts": counts,
            "full_reflection_counts": {
                key: 2 * value for key, value in counts.items()
            },
            "validation_counts": validation_counts,
            "count_stable_under_step_halving": counts == validation_counts,
            "positive_roots_to_320": roots,
        }
        if cutoff == 2:
            exact_roots = exact_two["positive_roots_to_320"]
            row["count_matches_exact_family"] = len(roots) == len(exact_roots)
            row["max_abs_root_error_vs_exact"] = float(
                max(abs(left - right) for left, right in zip(roots, exact_roots))
            )
        rows.append(row)

    stability = []
    for smaller, larger in zip(cutoffs[:-1], cutoffs[1:]):
        small_roots = np.asarray(root_cache[smaller])
        large_roots = np.asarray(root_cache[larger])
        for horizon in horizons:
            small = small_roots[small_roots <= horizon]
            large = large_roots[large_roots <= horizon]
            distances = np.min(np.abs(small[:, None] - large[None, :]), axis=1)
            stability.append(
                {
                    "from_cutoff": smaller,
                    "to_cutoff": larger,
                    "horizon": horizon,
                    "small_root_count": len(small),
                    "large_root_count": len(large),
                    "median_nearest_shift": float(np.median(distances)),
                    "max_nearest_shift": float(np.max(distances)),
                }
            )
    return {
        "frozen_grid_step": grid_step,
        "validation_grid_step": validation_step,
        "count_definition": (
            "sign-changing brackets on 0<t<=T; full count doubles by reflection"
        ),
        "limitation": (
            "a grid sign-change census does not detect hypothetical even-multiplicity "
            "tangencies and is not an argument-principle certification"
        ),
        "no_external_zero_data": True,
        "exact_n2": exact_two,
        "rows": rows,
        "successive_cutoff_nearest_root_diagnostics": stability,
    }


def high_precision_first_root_audit() -> dict:
    """Resolve the apparent high-cutoff plateau beyond binary64."""
    mp.mp.dps = 150

    def mp_scalar(masses: list[int], height: mp.mpf) -> mp.mpf:
        mass = [mp.mpf(value) for value in masses]
        previous = mp.mpf(1)
        current = 1 - 1 / mass[0]
        for index in range(1, len(mass)):
            edge_squared = (
                mp.mpf("0.25") / mass[index - 1]
                + mp.mpf("0.25") / mass[index]
                + mp.mpf("0.5")
                / mp.sqrt(mass[index - 1] * mass[index])
                * mp.cos(
                    height * mp.log(mass[index] / mass[index - 1])
                )
            )
            following = (
                (1 - 1 / mass[index] - edge_squared) * current
                - edge_squared / mass[index - 1] * previous
            )
            previous, current = current, following
        return current

    def mp_root(masses: list[int]) -> mp.mpf:
        left, right = mp.mpf("2.82"), mp.mpf("2.83")
        left_value = mp_scalar(masses, left)
        for _ in range(520):
            midpoint = (left + right) / 2
            middle_value = mp_scalar(masses, midpoint)
            if (middle_value < 0) == (left_value < 0):
                left, left_value = midpoint, middle_value
            else:
                right = midpoint
        return (left + right) / 2

    cutoffs = [8, 16, 32, 64, 128]
    roots = [mp_root(internal_multiplicative_atoms(cutoff)) for cutoff in cutoffs]
    rows = []
    for index, (cutoff, root) in enumerate(zip(cutoffs, roots)):
        rows.append(
            {
                "cutoff": cutoff,
                "first_positive_root_100_digits": mp.nstr(root, 100),
                "shift_from_previous": None
                if index == 0
                else mp.nstr(abs(root - roots[index - 1]), 25),
            }
        )
    return {
        "decimal_precision": 150,
        "bisection_iterations": 520,
        "rows": rows,
        "interpretation": (
            "zero displayed shift means below this 150-digit computation, "
            "not an exact cutoff-independence theorem"
        ),
    }


def finite_det3_checks(size: int = 8) -> dict:
    atoms = internal_multiplicative_atoms(size)
    rows = []
    for height in [-17.0, -5.25, -0.8, 0.0, 0.8, 5.25, 17.0]:
        transfer = l_matrix(atoms, 0.5 + 1j * height)
        reflected_transfer = l_matrix(atoms, 0.5 - 1j * height)
        block = chiral(transfer)
        scalar = np.linalg.det(
            np.eye(size) - transfer.conj().T @ transfer
        )
        block_determinant = np.linalg.det(np.eye(2 * size) - block)
        trace_block = np.trace(block)
        trace_block2_half = np.trace(block @ block) / 2.0
        determinant3 = block_determinant * np.exp(
            trace_block + trace_block2_half
        )
        reflected_scalar = np.linalg.det(
            np.eye(size) - reflected_transfer.conj().T @ reflected_transfer
        )
        rows.append(
            {
                "height": height,
                "antiunitary_conjugation_error": float(
                    np.linalg.norm(chiral(reflected_transfer) - np.conjugate(block))
                ),
                "block_determinant_error": float(
                    abs(block_determinant - scalar)
                ),
                "reflection_scalar_error": float(
                    abs(reflected_scalar - scalar)
                ),
                "trace_B_abs": float(abs(trace_block)),
                "trace_B2_half_imag_abs": float(abs(trace_block2_half.imag)),
                "det_I_minus_B": [
                    float(block_determinant.real),
                    float(block_determinant.imag),
                ],
                "det3_I_minus_B": [
                    float(determinant3.real),
                    float(determinant3.imag),
                ],
                "det3_positive_multiplier": float(
                    np.exp(trace_block2_half.real)
                ),
            }
        )
    return {
        "size": size,
        "atoms": atoms,
        "identities": [
            "det(I-B_t)=det(I-L_t^*L_t)",
            "det_3(I-B_t)=det(I-B_t) exp(Tr(B_t)+Tr(B_t^2)/2)",
            "Tr(B_t)=0 and Tr(B_t^2)/2=Tr(L_t^*L_t)>0",
            "B_(-t)=complex_conjugate(B_t)",
        ],
        "rows": rows,
    }


def recurrence_dense_audit() -> dict:
    rows = []
    for size in [2, 3, 4, 8, 16]:
        atoms = internal_multiplicative_atoms(size)
        for height in [0.0, 0.37, 3.1, 11.7]:
            transfer = l_matrix(atoms, 0.5 + 1j * height)
            dense = np.linalg.det(
                np.eye(size) - transfer.conj().T @ transfer
            )
            recurrence = float(crossing_scalar(atoms, height))
            rows.append(
                {
                    "size": size,
                    "height": height,
                    "dense_imag_abs": float(abs(dense.imag)),
                    "recurrence_dense_abs_error": float(abs(recurrence - dense)),
                }
            )
    return {
        "rows": rows,
        "max_abs_error": max(
            row["recurrence_dense_abs_error"] for row in rows
        ),
    }


def inventory_and_phase_controls(seed: int = 1907, size: int = 8) -> dict:
    rng = np.random.default_rng(seed)
    base = internal_multiplicative_atoms(size)
    shuffled = list(map(int, np.asarray(base)[rng.permutation(size)]))
    composites = [4, 6, 8, 9, 10, 12, 14, 15]
    random_masses = sorted(
        map(int, rng.choice(np.arange(2, 80), size=size, replace=False))
    )
    inventories = {
        "entropy_ordered_atoms": base,
        "shuffled_same_atoms": shuffled,
        "composites_only": composites,
        "matched_count_random_integers": random_masses,
    }
    height_grid = np.linspace(0.0, 40.0, 801)
    inventory_rows = []
    for label, masses in inventories.items():
        values = [
            schatten4_fourth_power(l_matrix(masses, 0.5 + 1j * height))
            for height in height_grid
        ]
        inventory_rows.append(
            {
                "label": label,
                "masses": masses,
                "triangular_ledger_exact": True,
                "schatten4_range": float(max(values) - min(values)),
                "strict_motion_on_grid": bool(max(values) - min(values) > 1e-8),
                "arithmetic_origin_gate": (
                    "passes source definition"
                    if label == "entropy_ordered_atoms"
                    else "fails or destroys intrinsic entropy ordering"
                ),
            }
        )

    source_phases = np.exp(1j * rng.uniform(-math.pi, math.pi, size - 1))
    target_phases = np.exp(1j * rng.uniform(-math.pi, math.pi, size - 1))
    phase_values = [
        schatten4_fourth_power(
            l_matrix(
                base,
                0.5 + 1j * height,
                endpoint_phases=(source_phases, target_phases),
            )
        )
        for height in height_grid
    ]
    return {
        "seed": seed,
        "inventory_rows": inventory_rows,
        "random_endpoint_phase_control": {
            "source_angles": [float(np.angle(value)) for value in source_phases],
            "target_angles": [float(np.angle(value)) for value in target_phases],
            "triangular_ledger_exact": True,
            "schatten4_range": float(max(phase_values) - min(phase_values)),
            "strict_motion_on_grid": bool(
                max(phase_values) - min(phase_values) > 1e-8
            ),
            "verdict": "PROVES_TOO_MUCH",
        },
        "interpretation": (
            "triangularity preserves every power trace and determinant under all "
            "four inventory choices and under arbitrary forward-edge phases"
        ),
    }


def random_dag_proves_too_much(seed_count: int = 24, size: int = 8) -> dict:
    masses = internal_multiplicative_atoms(size)
    heights = np.linspace(0.0, 40.0, 401)
    rows = []
    for seed in range(seed_count):
        rng = np.random.default_rng(seed)
        mask = np.triu(rng.random((size, size)) < 0.35, 1)
        coefficients = mask * rng.normal(size=(size, size))

        def dag_transfer(height: float) -> np.ndarray:
            diagonal = np.diag(d_matrix(masses, 0.5 + 1j * height))
            edge = coefficients * (
                diagonal[:, None] + diagonal[None, :]
            ) / 2.0
            return np.diag(diagonal) + edge

        reference = np.linalg.svd(dag_transfer(0.0), compute_uv=False)
        schatten4 = []
        singular_shifts = []
        for height in heights:
            transfer = dag_transfer(float(height))
            schatten4.append(schatten4_fourth_power(transfer))
            singular_shifts.append(
                float(
                    np.linalg.norm(
                        np.linalg.svd(transfer, compute_uv=False) - reference
                    )
                )
            )
        rows.append(
            {
                "seed": seed,
                "edge_count": int(mask.sum()),
                "schatten4_range": float(max(schatten4) - min(schatten4)),
                "max_singular_shift": float(max(singular_shifts)),
                "strict_motion": bool(max(singular_shifts) > 1e-8),
            }
        )

    variables = sp.symbols("x0:4")
    z = sp.symbols("z")
    exact = sp.diag(*variables)
    exact[0, 1] = (variables[0] + variables[1]) / 2
    exact[0, 3] = 2 * (variables[0] + variables[3]) / 3
    exact[1, 3] = -(variables[1] + variables[3]) / 5
    exact[2, 3] = 3 * (variables[2] + variables[3]) / 7
    traces_exact = all(
        sp.expand(sp.trace(exact**power) - sum(q**power for q in variables))
        == 0
        for power in range(1, 9)
    )
    determinant_exact = (
        sp.expand(
            (sp.eye(4) - z * exact).det()
            - sp.prod(1 - z * q for q in variables)
        )
        == 0
    )
    ranges = np.asarray([row["schatten4_range"] for row in rows])
    return {
        "label": "PROVES_TOO_MUCH",
        "reason": (
            "every entropy-oriented DAG is triangular and retains the cyclic "
            "ledger independently of its forward-edge geometry"
        ),
        "exact_opaque_dag": {
            "trace_powers_1_to_8_exact": traces_exact,
            "determinant_product_exact": bool(determinant_exact),
        },
        "seed_count": seed_count,
        "strict_motion_seed_count": sum(row["strict_motion"] for row in rows),
        "schatten4_range_summary": {
            "mean": float(ranges.mean()),
            "min": float(ranges.min()),
            "max": float(ranges.max()),
        },
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results" / "sdc09_results.json",
    )
    parser.add_argument(
        "--skip-high-precision",
        action="store_true",
        help="omit the 150-decimal first-root cutoff audit",
    )
    arguments = parser.parse_args()

    results = {
        "metadata": {
            "candidate": "SD-C09 entropy-oriented anticommutator successor shift",
            "atom_definition": (
                "multiplicative indecomposables of N_{>=2}, ordered by entropy log(p)"
            ),
            "first_atoms": internal_multiplicative_atoms(16),
            "operator": "L_s=D_s+(D_s S+S D_s)/2",
            "uses_riemann_zero_data": False,
            "fits_any_target_zeros": False,
        },
        "exact_successor_ledger": exact_successor_ledger(),
        "successor_periodic_census": closed_walk_census(),
        "one_sided_arbitrary_K_gauge_control": one_sided_random_k_gauge(),
        "alpha_source_target_motion_controls": alpha_motion_controls(),
        "bidirectional_successor_failure": bidirectional_failure_exact(),
        "finite_det3_reflection": finite_det3_checks(),
        "crossing_recurrence_dense_audit": recurrence_dense_audit(),
        "cutoff_zero_census": cutoff_zero_census(),
        "inventory_and_phase_controls": inventory_and_phase_controls(),
        "random_upper_DAG_control": random_dag_proves_too_much(),
    }
    if not arguments.skip_high_precision:
        results["high_precision_first_root_audit"] = high_precision_first_root_audit()
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "output": str(arguments.output),
                "ledger_exact": results["exact_successor_ledger"][
                    "determinant_exact"
                ],
                "cutoff_rows": len(results["cutoff_zero_census"]["rows"]),
                "no_zero_data": not results["metadata"]["uses_riemann_zero_data"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
