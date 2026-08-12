"""Independent arbitrary-precision audit of periodic-orbit ledgers.

This module intentionally reimplements the cyclic equations and their Newton
matrix with :mod:`mpmath`; it does not call the NumPy/SciPy residual or solver.
The result is a high-precision consistency audit, not an interval proof.
"""

from __future__ import annotations

from copy import deepcopy
from typing import Any, Mapping, Sequence

import mpmath as mp


def _mp(value: Any) -> mp.mpf:
    """Convert through the JSON-style decimal spelling, not binary arithmetic."""

    return mp.mpf(str(value))


def _decimal(value: mp.mpf, digits: int) -> str:
    return mp.nstr(value, n=digits, strip_zeros=False)


def _complex_decimal(value: mp.mpf | mp.mpc, digits: int) -> dict[str, str]:
    return {
        "real": _decimal(mp.re(value), digits),
        "imag": _decimal(mp.im(value), digits),
    }


def _cyclic_residual(q: Sequence[mp.mpf], a: mp.mpf, rho: mp.mpf) -> list[mp.mpf]:
    period = len(q)
    return [
        q[(index + 1) % period]
        + rho * q[(index - 1) % period]
        - 1
        + a * q[index] ** 2
        for index in range(period)
    ]


def _cyclic_jacobian(q: Sequence[mp.mpf], a: mp.mpf, rho: mp.mpf) -> mp.matrix:
    period = len(q)
    jacobian = mp.matrix(period, period)
    for index in range(period):
        # += is essential for periods one and two, where neighbor columns
        # coincide with each other or the diagonal.
        jacobian[index, index] += 2 * a * q[index]
        jacobian[index, (index + 1) % period] += 1
        jacobian[index, (index - 1) % period] += rho
    return jacobian


def _residual_norm(q: Sequence[mp.mpf], a: mp.mpf, rho: mp.mpf) -> mp.mpf:
    return max(abs(value) for value in _cyclic_residual(q, a, rho))


def _refine_cycle(
    initial_q: Sequence[mp.mpf],
    a: mp.mpf,
    rho: mp.mpf,
    digits: int,
    max_iterations: int,
) -> tuple[list[mp.mpf], dict[str, Any]]:
    q = list(initial_q)
    initial_residual = _residual_norm(q, a, rho)
    target = mp.power(10, -(digits - 20))
    iterations = 0
    stopped_reason = "residual_target_reached" if initial_residual <= target else "iteration_limit"
    for iteration in range(max_iterations):
        residual = _cyclic_residual(q, a, rho)
        if max(abs(value) for value in residual) <= target:
            stopped_reason = "residual_target_reached"
            break
        try:
            correction = mp.lu_solve(_cyclic_jacobian(q, a, rho), mp.matrix([-value for value in residual]))
        except (ZeroDivisionError, ValueError):
            stopped_reason = "singular_newton_matrix"
            break
        q = [q[index] + correction[index] for index in range(len(q))]
        iterations = iteration + 1
    final_residual = _residual_norm(q, a, rho)
    if final_residual <= target:
        stopped_reason = "residual_target_reached"
    return q, {
        "imported_residual_inf": _decimal(initial_residual, digits),
        "refined_residual_inf": _decimal(final_residual, digits),
        "newton_iterations": iterations,
        "refinement_converged": bool(final_residual <= target),
        "refinement_target": _decimal(target, digits),
        "stopped_reason": stopped_reason,
    }


def _matmul_2x2(left: mp.matrix, right: mp.matrix) -> mp.matrix:
    result = mp.matrix(2, 2)
    for row in range(2):
        for column in range(2):
            result[row, column] = sum(left[row, inner] * right[inner, column] for inner in range(2))
    return result


def _monodromy(q: Sequence[mp.mpf], a: mp.mpf, rho: mp.mpf) -> mp.matrix:
    matrix = mp.eye(2)
    for coordinate in q:
        local = mp.matrix([[-2 * a * coordinate, -rho], [1, 0]])
        matrix = _matmul_2x2(local, matrix)
    return matrix


def _multiplier_pair(trace: mp.mpf, determinant: mp.mpf) -> tuple[mp.mpf | mp.mpc, mp.mpf | mp.mpc]:
    discriminant = mp.mpc(trace**2 - 4 * determinant)
    square_root = mp.sqrt(discriminant)
    first = (trace + square_root) / 2
    second = (trace - square_root) / 2
    # Reconstruct the small multiplier from the determinant when the spectrum
    # is strongly hyperbolic, avoiding cancellation even at high precision.
    if abs(first) >= abs(second) and first != 0:
        second = determinant / first
    elif second != 0:
        first = determinant / second
    return first, second


def audit_orbit(
    orbit: Mapping[str, Any],
    *,
    a: Any,
    rho: Any,
    digits: int = 80,
    max_iterations: int = 12,
) -> dict[str, Any]:
    """Audit and refine one serialized orbit at arbitrary precision."""

    if digits < 40:
        raise ValueError("digits must be at least 40 for this audit")
    with mp.workdps(digits):
        a_mp = _mp(a)
        rho_mp = _mp(rho)
        initial_q = [_mp(value) for value in orbit["q"]]
        refined_q, refinement = _refine_cycle(initial_q, a_mp, rho_mp, digits, max_iterations)
        matrix = _monodromy(refined_q, a_mp, rho_mp)
        direct_determinant = matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]
        analytic_determinant = rho_mp ** len(refined_q)
        trace = matrix[0, 0] + matrix[1, 1]
        multipliers = _multiplier_pair(trace, analytic_determinant)
        return {
            "period": len(refined_q),
            "seed_word": orbit.get("seed_word"),
            **refinement,
            "q_refined": [_decimal(value, digits) for value in refined_q],
            "monodromy": [
                [_decimal(matrix[row, column], digits) for column in range(2)]
                for row in range(2)
            ],
            "monodromy_trace": _decimal(trace, digits),
            "monodromy_determinant_direct": _decimal(direct_determinant, digits),
            "monodromy_determinant_analytic": _decimal(analytic_determinant, digits),
            "determinant_absolute_error": _decimal(
                abs(direct_determinant - analytic_determinant), digits
            ),
            "determinant_reference": "analytic_product_of_local_determinants_rho^period",
            "multiplier_method": "characteristic_polynomial_with_analytic_determinant_and_stable_small_root",
            "multipliers": [_complex_decimal(value, digits) for value in multipliers],
        }


def audit_run(
    ledger_run: Mapping[str, Any],
    *,
    digits: int = 80,
    max_iterations: int = 12,
) -> dict[str, Any]:
    """Audit every accepted orbit in one ledger run."""

    parameters = ledger_run["parameters"]
    period_audits: list[dict[str, Any]] = []
    all_refined = True
    for period_record in ledger_run["periods"]:
        orbit_audits = [
            audit_orbit(
                orbit,
                a=parameters["a"],
                rho=parameters["rho"],
                digits=digits,
                max_iterations=max_iterations,
            )
            for orbit in period_record["orbits"]
        ]
        all_refined &= all(item["refinement_converged"] for item in orbit_audits)
        period_audits.append(
            {
                "period": int(period_record["period"]),
                "orbits_audited": len(orbit_audits),
                "orbits": orbit_audits,
            }
        )
    return {
        "parameters": deepcopy(parameters),
        "regime": ledger_run.get("regime"),
        "input_completeness_status": ledger_run.get("completeness_status"),
        "all_orbits_refined_to_target": all_refined,
        "periods": period_audits,
    }


def audit_ledger_payload(
    payload: Mapping[str, Any],
    *,
    digits: int = 80,
    max_iterations: int = 12,
) -> dict[str, Any]:
    """Audit either a top-level ``run_ledger`` payload or one raw ledger."""

    if "runs" in payload:
        runs = payload["runs"]
    elif "periods" in payload and "parameters" in payload:
        runs = [payload]
    else:
        raise ValueError("input is not a recognized periodic-orbit ledger")
    return {
        "audit_kind": "high_precision_residual_audit",
        "precision_decimal_digits": int(digits),
        "implementation": "independent_mpmath_cyclic_equations_newton_and_monodromy",
        "input_semantics": (
            "audits the exact decimal tokens serialized in the input JSON; "
            "it cannot recover parameter digits absent from that file"
        ),
        "interval_certification": False,
        "certification_claim": "none; this is a high-precision consistency audit, not an interval proof",
        "runs": [
            audit_run(run, digits=digits, max_iterations=max_iterations) for run in runs
        ],
    }
