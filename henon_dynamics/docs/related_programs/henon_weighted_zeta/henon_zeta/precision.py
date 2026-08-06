"""High-precision Newton refinement and invariant audits."""

from __future__ import annotations

from collections.abc import Iterable

import mpmath as mp


def _cyclic_residual(sequence: list[mp.mpf], a: mp.mpf) -> list[mp.mpf]:
    period = len(sequence)
    return [
        sequence[(index + 1) % period]
        + sequence[(index - 1) % period]
        + a * sequence[index] ** 2
        - 1
        for index in range(period)
    ]


def _cyclic_jacobian(sequence: list[mp.mpf], a: mp.mpf) -> mp.matrix:
    period = len(sequence)
    jacobian = mp.matrix(period, period)
    for index in range(period):
        jacobian[index, index] += 2 * a * sequence[index]
        jacobian[index, (index - 1) % period] += 1
        jacobian[index, (index + 1) % period] += 1
    return jacobian


def _monodromy(sequence: list[mp.mpf], a: mp.mpf) -> mp.matrix:
    matrix = mp.eye(2)
    for coordinate in sequence:
        derivative = mp.matrix([[-2 * a * coordinate, -1], [1, 0]])
        matrix = derivative * matrix
    return matrix


def _action(sequence: list[mp.mpf], a: mp.mpf) -> mp.mpf:
    period = len(sequence)
    return mp.fsum(
        sequence[index] * sequence[(index + 1) % period]
        - sequence[index]
        + a * sequence[index] ** 3 / 3
        for index in range(period)
    )


def refine_and_audit(
    sequence: Iterable[float],
    a: float,
    dps: int = 80,
    max_iterations: int = 20,
) -> dict[str, object]:
    """Refine a periodic sequence and audit high-precision invariants."""

    with mp.workdps(dps):
        a_mp = mp.mpf(str(a))
        coordinates = [mp.mpf(str(value)) for value in sequence]
        target = mp.power(10, -(dps - 15))
        converged = False
        iterations = 0
        for iterations in range(1, max_iterations + 1):
            residual = mp.matrix(_cyclic_residual(coordinates, a_mp))
            jacobian = _cyclic_jacobian(coordinates, a_mp)
            correction = mp.lu_solve(jacobian, residual)
            coordinates = [coordinates[index] - correction[index] for index in range(len(coordinates))]
            if max(abs(value) for value in correction) < target:
                converged = True
                break

        residual_values = _cyclic_residual(coordinates, a_mp)
        residual_inf = max(abs(value) for value in residual_values)
        coordinate_norm = max(abs(value) for value in coordinates)
        scaled_residual = residual_inf / (1 + 2 * coordinate_norm + abs(a_mp) * coordinate_norm**2)

        monodromy = _monodromy(coordinates, a_mp)
        trace = monodromy[0, 0] + monodromy[1, 1]
        determinant = monodromy[0, 0] * monodromy[1, 1] - monodromy[0, 1] * monodromy[1, 0]
        determinant_error = abs(determinant - 1)

        phase_traces = []
        for shift in range(len(coordinates)):
            rotated = coordinates[shift:] + coordinates[:shift]
            shifted_monodromy = _monodromy(rotated, a_mp)
            phase_traces.append(shifted_monodromy[0, 0] + shifted_monodromy[1, 1])
        phase_trace_spread = max(phase_traces) - min(phase_traces)
        threshold = mp.power(10, -(dps - 20))
        passed = bool(
            converged
            and scaled_residual < threshold
            and determinant_error < threshold
            and abs(phase_trace_spread) < threshold
        )

        digits = max(25, dps - 5)
        return {
            "passed": passed,
            "dps": dps,
            "iterations": iterations,
            "converged": converged,
            "sequence": [mp.nstr(value, digits) for value in coordinates],
            "scaled_residual_inf": mp.nstr(scaled_residual, digits),
            "residual_inf": mp.nstr(residual_inf, digits),
            "trace": mp.nstr(trace, digits),
            "determinant": mp.nstr(determinant, digits),
            "determinant_error": mp.nstr(determinant_error, digits),
            "phase_trace_spread": mp.nstr(phase_trace_spread, digits),
            "action": mp.nstr(_action(coordinates, a_mp), digits),
        }
