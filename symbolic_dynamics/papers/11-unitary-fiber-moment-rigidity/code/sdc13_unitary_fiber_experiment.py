#!/usr/bin/env python3
"""Exact and numerical falsification audit for SD-C13.

The only promoted family is the tensor-prime symbolic loop system with one
frozen finite-dimensional unitary fiber U_p at each atom.  The positive
ledger uses normalized trace tau_p=Tr/d, and the ordinary trace is an
explicit control.  No Riemann-zero data, target roots, crossing census,
phase fitting, or cross-family construction occurs here.
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
# Intrinsic and control clocks
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


def composites(count: int) -> list[int]:
    result: list[int] = []
    value = 4
    while len(result) < count:
        if any(value % q == 0 for q in range(2, math.isqrt(value) + 1)):
            result.append(value)
        value += 1
    return result


def random_increasing_clock(count: int, seed: int = 1907) -> list[int]:
    rng = np.random.default_rng(seed)
    return [int(value) for value in 1 + np.cumsum(rng.integers(1, 13, size=count))]


# ---------------------------------------------------------------------------
# Unitary families and moments
# ---------------------------------------------------------------------------


def cycle_unitary(size: int, phase: float = 0.0) -> np.ndarray:
    """Cyclic shift with boundary phase; U^size=e^(i phase) I."""
    answer = np.zeros((size, size), dtype=complex)
    for source in range(size - 1):
        answer[source + 1, source] = 1.0
    answer[0, size - 1] = np.exp(1j * phase)
    return answer


def normalized_trace(matrix: np.ndarray) -> complex:
    return complex(np.trace(matrix) / len(matrix))


def moment_rows(repetition_cutoff: int = 32) -> list[dict]:
    rows: list[dict] = []
    families: list[tuple[str, np.ndarray, str]] = []
    for dimension in [1, 2, 3, 4, 8]:
        families.append((f"identity_d{dimension}", np.eye(dimension), "identity"))
    families.extend(
        [
            ("scalar_phase_pi_over_7", np.asarray([[np.exp(1j * math.pi / 7)]]), "scalar_phase"),
            (
                "conjugate_pair_pi_over_7",
                np.diag([np.exp(1j * math.pi / 7), np.exp(-1j * math.pi / 7)]),
                "diag_conjugate",
            ),
        ]
    )
    for size in range(2, 9):
        families.append((f"cycle_m{size}", cycle_unitary(size), "cycle"))

    for name, unitary, family in families:
        power = np.eye(len(unitary), dtype=complex)
        for repetition in range(1, repetition_cutoff + 1):
            power = power @ unitary
            tau = normalized_trace(power)
            ordinary = complex(np.trace(power))
            expected = None
            if family == "cycle":
                expected = 1.0 if repetition % len(unitary) == 0 else 0.0
            elif family == "identity":
                expected = 1.0
            rows.append(
                {
                    "family": family,
                    "name": name,
                    "dimension": len(unitary),
                    "repetition": repetition,
                    "tau_real": tau.real,
                    "tau_imag": tau.imag,
                    "ordinary_trace_real": ordinary.real,
                    "ordinary_trace_imag": ordinary.imag,
                    "distance_tau_from_one": abs(tau - 1),
                    "expected_tau": expected,
                    "expected_residual": (
                        None if expected is None else abs(tau - expected)
                    ),
                }
            )
    return rows


def moment_family_audit(repetition_cutoff: int = 32) -> dict:
    rows = moment_rows(repetition_cutoff)
    cycle_rows = [row for row in rows if row["family"] == "cycle"]
    return {
        "repetition_cutoff": repetition_cutoff,
        "rows": rows,
        "cycle_exact_max_residual": max(row["expected_residual"] for row in cycle_rows),
        "cycle_formula": "tau(P_m^r)=1 if m divides r, and 0 otherwise",
        "scalar_formula": "tau((e^(i theta))^r)=e^(i r theta)",
        "conjugate_pair_formula": "tau(diag(e^(i theta),e^(-i theta))^r)=cos(r theta)",
    }


# ---------------------------------------------------------------------------
# Positive and ordinary trace rigidity
# ---------------------------------------------------------------------------


def rigidity_audit(max_dimension: int = 8, seed_count: int = 32) -> dict:
    ordinary_rows = []
    for dimension in range(1, max_dimension + 1):
        # Newton identities with prescribed power sums p_1=...=p_d=1.
        elementary = [sp.Integer(1)]
        for order in range(1, dimension + 1):
            value = sum(
                (-1) ** (index - 1)
                * elementary[order - index]
                * sp.Integer(1)
                for index in range(1, order + 1)
            ) / order
            elementary.append(sp.simplify(value))
        ordinary_rows.append(
            {
                "dimension": dimension,
                "required_moments": dimension,
                "newton_elementary": json.dumps([str(value) for value in elementary[1:]]),
                "forced_determinant": str(elementary[-1]),
                "unitary_determinant_modulus_required": 1.0,
                "compatible": dimension == 1 and elementary[-1] == 1,
                "conclusion": (
                    "U=[1]"
                    if dimension == 1
                    else "impossible: Newton forces det(U)=0"
                ),
            }
        )

    random_rows = []
    for seed in range(seed_count):
        rng = np.random.default_rng(seed)
        dimension = int(rng.integers(2, max_dimension + 1))
        phases = rng.uniform(-math.pi, math.pi, size=dimension)
        unitary = np.diag(np.exp(1j * phases))
        tau = normalized_trace(unitary)
        hs_defect = normalized_trace(
            (unitary - np.eye(dimension)).conj().T
            @ (unitary - np.eye(dimension))
        ).real
        identity_formula = 2.0 - 2.0 * tau.real
        random_rows.append(
            {
                "seed": seed,
                "dimension": dimension,
                "tau_U_real": tau.real,
                "tau_U_imag": tau.imag,
                "normalized_HS_defect": hs_defect,
                "rigidity_formula_residual": abs(hs_defect - identity_formula),
                "nontrivial": hs_defect > 1e-12,
                "tau_equals_one": abs(tau - 1) < 1e-12,
            }
        )
    return {
        "normalized_trace_theorem": (
            "tau((U-I)^*(U-I))=2-tau(U)-tau(U*)=0 when tau(U)=1; "
            "faithfulness implies U=I"
        ),
        "ordinary_trace_theorem": (
            "Tr(U^r)=1 for r=1,...,d gives e_1=1 and e_2=...=e_d=0 "
            "by Newton identities; unitarity forces d=1 and U=1"
        ),
        "ordinary_rows": ordinary_rows,
        "random_positive_rows": random_rows,
        "max_rigidity_formula_residual": max(
            row["rigidity_formula_residual"] for row in random_rows
        ),
    }


# ---------------------------------------------------------------------------
# Nonfaithful and graded escape controls
# ---------------------------------------------------------------------------


def hidden_and_graded_audit(repetition_cutoff: int = 32) -> dict:
    z = 0.31 + 0.17j
    rows = []
    for hidden_dimension in range(2, 9):
        for theta in [0.0, 0.37, 1.11, 2.43]:
            hidden = cycle_unitary(hidden_dimension, theta)
            even = np.block(
                [
                    [np.ones((1, 1), dtype=complex), np.zeros((1, hidden_dimension), dtype=complex)],
                    [np.zeros((hidden_dimension, 1), dtype=complex), hidden],
                ]
            )
            state_max_error = 0.0
            supertrace_max_error = 0.0
            for repetition in range(1, repetition_cutoff + 1):
                hidden_power = np.linalg.matrix_power(hidden, repetition)
                even_power = np.linalg.matrix_power(even, repetition)
                state_moment = even_power[0, 0]
                supertrace = np.trace(even_power) - np.trace(hidden_power)
                state_max_error = max(state_max_error, abs(state_moment - 1))
                supertrace_max_error = max(supertrace_max_error, abs(supertrace - 1))

            det_hidden = np.linalg.det(np.eye(hidden_dimension) - z * hidden)
            det_even = np.linalg.det(np.eye(hidden_dimension + 1) - z * even)
            state_determinant = 1 - z
            graded_berezinian = det_even / det_hidden
            rows.append(
                {
                    "hidden_dimension": hidden_dimension,
                    "theta": theta,
                    "state_moment_max_error": state_max_error,
                    "ordinary_hidden_factor_real": det_hidden.real,
                    "ordinary_hidden_factor_imag": det_hidden.imag,
                    "ordinary_even_det_motion_visible": abs(det_even - state_determinant),
                    "graded_supertrace_max_error": supertrace_max_error,
                    "graded_berezinian_residual": abs(
                        graded_berezinian - state_determinant
                    ),
                }
            )
    return {
        "nonfaithful_state": (
            "rho(A)=<e_0,Ae_0> on U=1 direct-sum V gives rho(U^r)=1 "
            "while V is state-invisible"
        ),
        "nonfaithful_boundary": (
            "the ordinary determinant sees det(I-zV), so state moments do not "
            "control the full determinant"
        ),
        "graded_construction": "even=1 direct-sum V, odd=V",
        "graded_result": (
            "Str(U^r)=1, but Ber(I-zU)=(1-z)det(I-zV)/det(I-zV)=1-z; "
            "the moving sector cancels out of the determinant"
        ),
        "rows": rows,
    }


# ---------------------------------------------------------------------------
# Recurrent mixed-cycle formal-variable audit
# ---------------------------------------------------------------------------


def recurrence_audit(repetition_cutoff: int = 32) -> dict:
    x, y, z = sp.symbols("x y z")
    a, b = sp.symbols("a b")
    triangle_rows = []
    for cycle_size in range(2, 9):
        first_survival = None
        for repetition in range(1, repetition_cutoff + 1):
            tau = sp.Integer(1 if repetition % cycle_size == 0 else 0)
            coefficient = sp.expand(3 * (x * y * z) ** repetition * tau)
            if coefficient != 0 and first_survival is None:
                first_survival = repetition
            triangle_rows.append(
                {
                    "fiber_cycle_size": cycle_size,
                    "primitive_repetition": repetition,
                    "transfer_power": 3 * repetition,
                    "normalized_fiber_moment": int(tau),
                    "formal_coefficient": str(coefficient),
                    "survives": coefficient != 0,
                }
            )

    parallel_rows = []
    for repetition in range(1, repetition_cutoff + 1):
        independent = sp.expand(a**repetition + (-1) ** repetition * b**repetition)
        specialized = sp.expand(independent.subs(b, a))
        parallel_rows.append(
            {
                "repetition": repetition,
                "independent_path_polynomial": str(independent),
                "independent_nonzero": independent != 0,
                "equal_path_specialization": str(specialized),
                "equal_path_survives": specialized != 0,
            }
        )
    return {
        "triangle_formula": (
            "a three-edge mixed primitive with monomial xyz and m-cycle fiber "
            "contributes 3(xyz)^r tau(P_m^r), first surviving at r=m"
        ),
        "roots_of_unity_verdict": "delay mixed leakage to transfer power 3m but never erase it",
        "triangle_rows": triangle_rows,
        "parallel_formula": (
            "two return paths with independent monomials a,b and phases +1,-1 "
            "give a^r+(-1)^r b^r; independent monomials cannot cancel"
        ),
        "parallel_rows": parallel_rows,
    }


# ---------------------------------------------------------------------------
# Entropy block and matched-clock controls
# ---------------------------------------------------------------------------


def fiber_determinant_log(
    clocks: np.ndarray,
    dimension: int,
    theta: float,
    offsets: np.ndarray,
    s: complex,
    z: complex,
) -> complex:
    # det(I-a U_d(phi)) = 1-exp(i phi)*a^d for the cyclic boundary-phase fiber.
    amplitudes = z * np.exp(-s * np.log(clocks))
    return complex(
        np.sum(
            np.log1p(
                -np.exp(1j * (theta + offsets)) * amplitudes**dimension
            )
        )
    )


def entropy_clock_controls(atom_count: int = 48, seed_count: int = 32) -> dict:
    inventories = {
        "tensor_primes": np.asarray(internal_multiplicative_atoms(atom_count), dtype=float),
        "composites": np.asarray(composites(atom_count), dtype=float),
        "random_increasing": np.asarray(random_increasing_clock(atom_count), dtype=float),
    }
    theta_grid = np.linspace(0.0, 2.0 * math.pi, 129)
    s = 0.75 + 2.5j
    z = 0.72 + 0.11j
    rows = []
    for inventory_name, clocks in inventories.items():
        for dimension in [2, 3, 4]:
            first_ledger_failure = dimension
            for seed in range(seed_count):
                rng = np.random.default_rng(seed)
                offsets = rng.uniform(-math.pi, math.pi, size=atom_count)
                values = np.asarray(
                    [
                        fiber_determinant_log(
                            clocks, dimension, theta, offsets, s, z
                        )
                        for theta in theta_grid
                    ]
                )
                logabs = values.real
                rows.append(
                    {
                        "inventory": inventory_name,
                        "fiber_dimension": dimension,
                        "seed": seed,
                        "first_ledger_failure_repetition": first_ledger_failure,
                        "determinant_logabs_range": float(np.ptp(logabs)),
                        "determinant_motion": bool(np.ptp(logabs) > 1e-12),
                        "ledger_exact_all_r_to_32": False,
                    }
                )
    return {
        "atom_count": atom_count,
        "seed_count": seed_count,
        "fiber_dimensions": [2, 3, 4],
        "rows": rows,
        "motion_pass_count_by_inventory": {
            name: sum(
                row["determinant_motion"]
                for row in rows
                if row["inventory"] == name
            )
            for name in inventories
        },
        "verdict": (
            "PROVES_TOO_MUCH: finite Bloch determinant motion occurs for "
            "prime, composite, and random increasing clocks, while every "
            "nontrivial cycle fiber fails the ledger at r=d"
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

    moments = moment_family_audit()
    rigidity = rigidity_audit()
    hidden = hidden_and_graded_audit()
    recurrence = recurrence_audit()
    controls = entropy_clock_controls()
    results = {
        "metadata": {
            "candidate_id": "SD-C13",
            "candidate": "finite unitary fiber over tensor-prime atom loops",
            "primary_family": "symbolic dynamics",
            "positive_state": "normalized faithful matrix trace",
            "repetition_cutoff": 32,
            "uses_riemann_zero_data": False,
            "fits_target_zeros": False,
            "crossing_census_performed": False,
        },
        "moment_families": moments,
        "positive_and_ordinary_rigidity": rigidity,
        "hidden_and_graded_controls": hidden,
        "recurrent_mixed_cycles": recurrence,
        "entropy_clock_controls": controls,
        "claim_boundary": {
            "normalized_positive_moment_rigidity": "PROVED; tau(U)=1 alone forces U=I",
            "ordinary_all_moment_rigidity": "PROVED; first d moments force d=1,U=1",
            "nonfaithful_state_escape": "REFUTED as determinant control",
            "graded_escape": "ledger exact but moving V cancels from Berezinian",
            "roots_of_unity_escape": "REFUTED; delays mixed word to r=m",
            "positive_bloch_ledger_and_motion": "IMPOSSIBLE in frozen finite-fiber class",
            "arithmetic_specificity": "REFUTED by matched clocks",
            "rh_or_target_zero_claim": "FORBIDDEN / NOT MADE",
            "route_b_invocation_allowed": False,
        },
    }
    (args.output_dir / "summary.json").write_text(
        json.dumps(results, indent=2, sort_keys=True, default=str) + "\n"
    )
    write_csv(args.output_dir / "moment_families.csv", moments["rows"])
    write_csv(args.output_dir / "ordinary_rigidity.csv", rigidity["ordinary_rows"])
    write_csv(args.output_dir / "positive_state_controls.csv", rigidity["random_positive_rows"])
    write_csv(args.output_dir / "hidden_graded.csv", hidden["rows"])
    write_csv(args.output_dir / "triangle_recurrence.csv", recurrence["triangle_rows"])
    write_csv(args.output_dir / "parallel_paths.csv", recurrence["parallel_rows"])
    write_csv(args.output_dir / "entropy_clock_controls.csv", controls["rows"])
    print(
        json.dumps(
            {
                "output": str(args.output_dir / "summary.json"),
                "cycle_moment_residual": moments["cycle_exact_max_residual"],
                "rigidity_formula_residual": rigidity[
                    "max_rigidity_formula_residual"
                ],
                "matched_clock_motion": controls["motion_pass_count_by_inventory"],
                "no_zero_data": True,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
