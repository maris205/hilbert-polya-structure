#!/usr/bin/env python3
"""Independent R400 checker; deliberately does not import project code."""

from __future__ import annotations

import argparse
import hashlib
import json
from math import pi, sqrt
from pathlib import Path
from typing import Any

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares


TWO_PI = 2.0 * pi


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def one_step_derivatives(q: np.ndarray, a: float) -> tuple[float, np.ndarray, np.ndarray]:
    """Independent value/gradient/Hessian for the centered one-step well."""

    x, y = (float(value) for value in q)
    c = 2.0 * (sqrt(1.0 + a) - 1.0)
    u = np.array([-c * x - a * x * x - y, x])
    jacobian = np.array([[-c - 2.0 * a * x, -1.0], [1.0, 0.0]])
    component_hessian = np.array([[-2.0 * a, 0.0], [0.0, 0.0]])
    exponent = pi * float(u @ u)
    value = TWO_PI * np.exp(exponent)
    grad_exponent = TWO_PI * (jacobian.T @ u)
    hess_exponent = TWO_PI * (
        jacobian.T @ jacobian + u[0] * component_hessian
    )
    gradient = value * grad_exponent
    hessian = value * (
        hess_exponent + np.outer(grad_exponent, grad_exponent)
    )
    return float(value), gradient, hessian


def normal_oracle(a: float) -> dict[str, Any]:
    c = 2.0 * (sqrt(1.0 + a) - 1.0)
    matrix = np.array([[-c, -1.0], [1.0, 0.0]])
    eigenvalues, eigenvectors = np.linalg.eigh(matrix.T @ matrix)
    singular = np.sqrt(eigenvalues)
    for column in range(2):
        pivot = int(np.argmax(np.abs(eigenvectors[:, column])))
        if eigenvectors[pivot, column] < 0.0:
            eigenvectors[:, column] *= -1.0
    ratio = singular[1] / singular[0]
    fast_period = 1.0 / singular[1]
    angle = TWO_PI / ratio
    determinant = 4.0 * np.sin(angle / 2.0) ** 2
    phi2 = TWO_PI * (matrix.T @ matrix)
    phi3 = np.zeros((2, 2, 2))
    phi3[0, 0, 0] = 12.0 * pi * a * c
    for indices in ((0, 0, 1), (0, 1, 0), (1, 0, 0)):
        phi3[indices] = 4.0 * pi * a
    phi4 = np.zeros((2, 2, 2, 2))
    phi4[0, 0, 0, 0] = 24.0 * pi * a * a
    potential3 = TWO_PI * phi3
    potential4 = TWO_PI * (
        phi4
        + np.einsum("ij,kl->ijkl", phi2, phi2)
        + np.einsum("ik,jl->ijkl", phi2, phi2)
        + np.einsum("il,jk->ijkl", phi2, phi2)
    )
    normal3 = np.einsum(
        "ijk,ia,jb,kc->abc",
        potential3,
        eigenvectors,
        eigenvectors,
        eigenvectors,
    )
    normal4 = np.einsum(
        "ijkl,ia,jb,kc,ld->abcd",
        potential4,
        eigenvectors,
        eigenvectors,
        eigenvectors,
        eigenvectors,
    )
    omega = TWO_PI * singular
    third = np.array([normal3[1, 1, index] for index in range(2)])
    constant = -third / (4.0 * omega**2)
    second = -third / (4.0 * (omega**2 - 4.0 * omega[1] ** 2))
    frequency_coefficient = (
        normal4[1, 1, 1, 1] / 8.0
        + np.sum(third * (constant + 0.5 * second))
    ) / (2.0 * omega[1])
    period_slope = -fast_period * 2.0 * frequency_coefficient / omega[1] ** 3
    return {
        "c": float(c),
        "singular": singular,
        "eigenvectors": eigenvectors,
        "fast_period": float(fast_period),
        "fast_determinant": float(determinant),
        "fast_amplitude": float(fast_period / sqrt(determinant)),
        "period_slope": float(period_slope),
        "action_ratio_slope": float(0.5 * period_slope),
    }


def independent_cell(excess: float, a: float = 1.02) -> dict[str, Any]:
    oracle = normal_oracle(a)
    vectors = oracle["eigenvectors"]
    fast = vectors[:, 1]
    slow = vectors[:, 0]
    basis = np.column_stack((fast, slow))
    omega = TWO_PI * oracle["singular"][1]
    amplitude = sqrt(2.0 * excess) / omega
    momentum_scale = sqrt(2.0 * excess)
    half_period0 = 0.5 * oracle["fast_period"]
    energy = TWO_PI + excess

    def rhs(_time: float, state: np.ndarray) -> np.ndarray:
        _, gradient, _ = one_step_derivatives(state[:2], a)
        return np.concatenate((state[2:], -gradient))

    def decode(unknowns: np.ndarray) -> tuple[np.ndarray, float]:
        q0 = amplitude * (unknowns[0] * fast + unknowns[1] * slow)
        return q0, float(half_period0 * unknowns[2])

    def residual(unknowns: np.ndarray) -> np.ndarray:
        q0, half_period = decode(unknowns)
        solved = solve_ivp(
            rhs,
            (0.0, half_period),
            np.concatenate((q0, np.zeros(2))),
            method="DOP853",
            rtol=8.0e-12,
            atol=8.0e-14,
            max_step=half_period / 220.0,
        )
        p_half = basis.T @ solved.y[2:, -1]
        value, _, _ = one_step_derivatives(q0, a)
        return np.concatenate((p_half / momentum_scale, [(value - energy) / excess]))

    root = least_squares(
        residual,
        np.array([1.0, 0.0, 1.0]),
        bounds=(np.array([0.2, -1.0, 0.5]), np.array([2.0, 1.0, 1.5])),
        xtol=5.0e-14,
        ftol=5.0e-14,
        gtol=5.0e-14,
        max_nfev=140,
    )
    q0, half_period = decode(root.x)
    period = 2.0 * half_period
    state0 = np.concatenate((q0, np.zeros(2)))
    symplectic_form = np.block(
        [[np.zeros((2, 2)), np.eye(2)], [-np.eye(2), np.zeros((2, 2))]]
    )

    def augmented_rhs(_time: float, augmented: np.ndarray) -> np.ndarray:
        state = augmented[:4]
        _, gradient, hessian = one_step_derivatives(state[:2], a)
        flow_jacobian = np.block(
            [[np.zeros((2, 2)), np.eye(2)], [-hessian, np.zeros((2, 2))]]
        )
        monodromy = augmented[4:20].reshape(4, 4)
        return np.concatenate(
            (
                state[2:],
                -gradient,
                (flow_jacobian @ monodromy).ravel(),
                [float(state[2:] @ state[2:])],
            )
        )

    augmented0 = np.concatenate((state0, np.eye(4).ravel(), [0.0]))
    solved = solve_ivp(
        augmented_rhs,
        (0.0, period),
        augmented0,
        method="DOP853",
        rtol=8.0e-13,
        atol=8.0e-15,
        max_step=period / 1000.0,
    )
    final_state = solved.y[:4, -1]
    monodromy = solved.y[4:20, -1].reshape(4, 4)
    multipliers = np.linalg.eigvals(monodromy)
    ordering = np.argsort(np.abs(multipliers - 1.0))
    transverse = multipliers[ordering[2:]]
    determinant = np.prod(1.0 - transverse)
    return {
        "optimizer_success": bool(root.success),
        "initial_state": state0,
        "period": float(period),
        "action": float(solved.y[20, -1]),
        "closure": float(np.max(np.abs(final_state - state0))),
        "shooting_residual": float(np.max(np.abs(residual(root.x)))),
        "monodromy": monodromy,
        "determinant": determinant,
        "symplectic_defect": float(
            np.linalg.norm(
                monodromy.T @ symplectic_form @ monodromy - symplectic_form,
                ord=np.inf,
            )
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--result",
        type=Path,
        default=Path("results/r400_local_period_smoke"),
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    result = args.result if args.result.is_absolute() else root / args.result
    summary = json.loads((result / "summary.json").read_text())
    manifest = json.loads((result / "manifest.json").read_text())
    checks: dict[str, bool] = {}

    for relative, expected in manifest["source_sha256"].items():
        checks[f"source_hash:{relative}"] = sha256(root / relative) == expected
    for relative, expected in manifest["result_sha256"].items():
        checks[f"result_hash:{relative}"] = sha256(result / relative) == expected

    oracle = normal_oracle(1.02)
    stored = summary["normal_mode"]
    checks["oracle_c"] = abs(stored["c"] - oracle["c"]) < 2.0e-14
    checks["oracle_singular_values"] = bool(
        np.allclose(stored["singular_values"], oracle["singular"], atol=2.0e-14)
    )
    checks["oracle_fast_period"] = (
        abs(stored["periods"][1] - oracle["fast_period"]) < 2.0e-14
    )
    checks["oracle_stability"] = (
        abs(stored["fast_stability_determinant"] - oracle["fast_determinant"])
        < 2.0e-14
    )
    checks["oracle_amplitude"] = (
        abs(stored["fast_trace_amplitude"] - oracle["fast_amplitude"])
        < 2.0e-14
    )
    stored_normal_form = summary["fast_normal_form"]
    checks["oracle_period_slope"] = (
        abs(stored_normal_form["period_energy_slope"] - oracle["period_slope"])
        < 2.0e-14
    )
    checks["oracle_action_ratio_slope"] = (
        abs(
            stored_normal_form["action_ratio_energy_slope"]
            - oracle["action_ratio_slope"]
        )
        < 2.0e-14
    )

    for cell in summary["cells"]:
        name = f"delta_{cell['energy_excess']:.2f}".replace(".", "p")
        npz_path = result / "cells" / f"{name}.npz"
        checks[f"cell_npz_binding:{name}"] = sha256(npz_path) == cell["npz_sha256"]
        with np.load(npz_path) as arrays:
            closure = np.max(np.abs(arrays["states"][-1] - arrays["states"][0]))
            action = np.trapezoid(
                np.sum(arrays["states"][:, 2:] ** 2, axis=1), arrays["times"]
            )
            checks[f"cell_closure_raw:{name}"] = closure < 1.0e-10
            checks[f"cell_action_quadrature:{name}"] = (
                abs(action - cell["action"]) < 2.0e-8
            )
            checks[f"cell_monodromy_raw:{name}"] = bool(
                np.all(np.isfinite(arrays["monodromy"]))
            )
        checks[f"cell_frozen_gates:{name}"] = bool(cell["all_cell_gates_pass"])

    independent = independent_cell(0.05)
    target = next(cell for cell in summary["cells"] if cell["energy_excess"] == 0.05)
    comparisons = {
        "period_absolute": abs(independent["period"] - target["period"]),
        "action_absolute": abs(independent["action"] - target["action"]),
        "initial_state_max_absolute": float(
            np.max(np.abs(independent["initial_state"] - target["initial_state"]))
        ),
        "stability_determinant_absolute": abs(
            independent["determinant"].real
            - target["transverse_stability_determinant"]["real"]
        ),
    }
    checks["independent_optimizer"] = independent["optimizer_success"]
    checks["independent_shooting"] = independent["shooting_residual"] < 1.0e-10
    checks["independent_closure"] = independent["closure"] < 1.0e-10
    checks["independent_symplectic"] = independent["symplectic_defect"] < 1.0e-9
    checks["independent_period"] = comparisons["period_absolute"] < 2.0e-11
    checks["independent_action"] = comparisons["action_absolute"] < 2.0e-11
    checks["independent_initial_state"] = (
        comparisons["initial_state_max_absolute"] < 2.0e-10
    )
    checks["independent_stability"] = (
        comparisons["stability_determinant_absolute"] < 2.0e-10
    )
    checks["no_arithmetic_promotion"] = (
        summary["claim_boundary"]["prime_power_gate"] is False
        and summary["claim_boundary"]["zeta_zero_test"] is False
        and summary["claim_boundary"]["rh_claim"] is False
    )
    checks["run_reported_pass"] = bool(summary["all_gates_pass"])
    checks = {key: bool(value) for key, value in checks.items()}
    passed = all(checks.values())
    payload = {
        "status": "PASS" if passed else "FAIL",
        "checker_imported_project_package": False,
        "checks": checks,
        "independent_delta_0p05": {
            "period": independent["period"],
            "action": independent["action"],
            "closure": independent["closure"],
            "shooting_residual": independent["shooting_residual"],
            "symplectic_defect": independent["symplectic_defect"],
            "stability_determinant": {
                "real": float(independent["determinant"].real),
                "imag": float(independent["determinant"].imag),
            },
        },
        "comparisons": comparisons,
        "claim_boundary": "Classical local-orbit certificate only; no trace theorem, P, Z, or RH promotion.",
    }
    (result / "independent_checker.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n"
    )
    postcheck = {
        "r400_run_status": "PASS" if summary["all_gates_pass"] else "FAIL",
        "independent_checker_status": payload["status"],
        "final_smoke_status": "PASS" if passed and summary["all_gates_pass"] else "FAIL",
        "manifest_left_immutable": True,
    }
    (result / "POSTCHECK_STATUS.json").write_text(
        json.dumps(postcheck, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(postcheck))
    return 0 if postcheck["final_smoke_status"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
