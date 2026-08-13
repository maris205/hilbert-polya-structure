"""Periodic-orbit equations, binary anti-integrable seeds, and ledgers."""

from __future__ import annotations

from itertools import product
from math import isqrt
from typing import Any, Iterable, Sequence

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy.optimize import least_squares, root

from .model import HenonHomotopy


FloatArray = NDArray[np.float64]


def _divisors(number: int) -> list[int]:
    divisors: list[int] = []
    for candidate in range(1, isqrt(number) + 1):
        if number % candidate == 0:
            divisors.append(candidate)
            if candidate * candidate != number:
                divisors.append(number // candidate)
    return sorted(divisors)


def moebius(number: int) -> int:
    """Elementary integer Möbius function (avoids a symbolic dependency)."""

    if number < 1:
        raise ValueError("number must be positive")
    remaining = number
    prime_count = 0
    factor = 2
    while factor * factor <= remaining:
        if remaining % factor == 0:
            remaining //= factor
            prime_count += 1
            if remaining % factor == 0:
                return 0
            while remaining % factor == 0:
                remaining //= factor
        factor += 1
    if remaining > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def binary_primitive_orbit_count(period: int) -> int:
    """Number of primitive binary necklaces of length ``period``."""

    if period < 1:
        raise ValueError("period must be positive")
    return sum(moebius(divisor) * 2 ** (period // divisor) for divisor in _divisors(period)) // period


def canonical_rotation(values: Sequence[Any]) -> tuple[Any, ...]:
    """Lexicographically least cyclic rotation."""

    sequence = tuple(values)
    if not sequence:
        raise ValueError("values must be nonempty")
    return min(sequence[offset:] + sequence[:offset] for offset in range(len(sequence)))


def _word_minimal_period(word: Sequence[int]) -> int:
    sequence = tuple(word)
    for divisor in _divisors(len(sequence)):
        if divisor < len(sequence) and all(sequence[index] == sequence[index % divisor] for index in range(len(sequence))):
            return divisor
    return len(sequence)


def primitive_binary_necklaces(period: int) -> list[tuple[int, ...]]:
    """Enumerate one representative of every primitive binary necklace."""

    if period < 1:
        raise ValueError("period must be positive")
    representatives: list[tuple[int, ...]] = []
    for word in product((0, 1), repeat=period):
        if _word_minimal_period(word) != period:
            continue
        if word == canonical_rotation(word):
            representatives.append(word)
    return representatives


def cyclic_residual(q_cycle: ArrayLike, a: float, rho: float) -> FloatArray:
    """Residual of ``q[i+1]+rho*q[i-1]-1+a*q[i]^2=0``."""

    q = np.asarray(q_cycle, dtype=float)
    if q.ndim != 1 or q.size == 0:
        raise ValueError("q_cycle must be a nonempty one-dimensional array")
    return np.roll(q, -1) + rho * np.roll(q, 1) - 1.0 + a * q * q


def cyclic_jacobian(q_cycle: ArrayLike, a: float, rho: float) -> FloatArray:
    """Analytic Jacobian of :func:`cyclic_residual`, including n=1,2."""

    q = np.asarray(q_cycle, dtype=float)
    if q.ndim != 1 or q.size == 0:
        raise ValueError("q_cycle must be a nonempty one-dimensional array")
    period = q.size
    jacobian = np.zeros((period, period), dtype=float)
    for index in range(period):
        jacobian[index, index] += 2.0 * a * q[index]
        jacobian[index, (index + 1) % period] += 1.0
        jacobian[index, (index - 1) % period] += rho
    return jacobian


def numerical_minimal_period(q_cycle: ArrayLike, tolerance: float = 1e-8) -> int:
    q = np.asarray(q_cycle, dtype=float)
    if q.ndim != 1 or q.size == 0:
        raise ValueError("q_cycle must be a nonempty one-dimensional array")
    for divisor in _divisors(q.size):
        if divisor < q.size and np.allclose(q, np.resize(q[:divisor], q.size), rtol=0.0, atol=tolerance):
            return divisor
    return int(q.size)


def _canonical_numeric_cycle(q_cycle: ArrayLike, decimals: int = 12) -> FloatArray:
    q = np.asarray(q_cycle, dtype=float)
    rotations = [np.roll(q, -offset) for offset in range(q.size)]
    keys = [tuple(np.round(rotation, decimals=decimals)) for rotation in rotations]
    return rotations[min(range(q.size), key=keys.__getitem__)].copy()


def _same_orbit(left: FloatArray, right: FloatArray, tolerance: float) -> bool:
    if left.size != right.size:
        return False
    return any(np.allclose(left, np.roll(right, offset), rtol=0.0, atol=tolerance) for offset in range(left.size))


def solve_cycle(
    initial_q: ArrayLike,
    a: float,
    rho: float,
    residual_tolerance: float = 1e-11,
) -> tuple[FloatArray, dict[str, Any]]:
    """Correct one seed to a periodic coordinate cycle.

    A Newton/hybrid solve is attempted first.  A deterministic trust-region
    least-squares correction is the fallback; acceptance is based on the
    equation residual rather than the optimizer's status flag.
    """

    initial = np.asarray(initial_q, dtype=float)
    solution = root(
        cyclic_residual,
        initial,
        args=(a, rho),
        jac=cyclic_jacobian,
        method="hybr",
        options={"xtol": 1e-12, "maxfev": 4000},
    )
    corrected = np.asarray(solution.x, dtype=float)
    method = "hybr"
    residual = float(np.linalg.norm(cyclic_residual(corrected, a, rho), ord=np.inf))
    if not np.isfinite(residual) or residual > residual_tolerance:
        fallback = least_squares(
            cyclic_residual,
            initial,
            jac=cyclic_jacobian,
            args=(a, rho),
            method="trf",
            xtol=1e-14,
            ftol=1e-14,
            gtol=1e-14,
            max_nfev=10000,
        )
        corrected = np.asarray(fallback.x, dtype=float)
        method = "least_squares"
        residual = float(np.linalg.norm(cyclic_residual(corrected, a, rho), ord=np.inf))
        optimizer_success = bool(fallback.success)
        message = str(fallback.message)
    else:
        optimizer_success = bool(solution.success)
        message = str(solution.message)
    return corrected, {
        "accepted": bool(np.isfinite(residual) and residual <= residual_tolerance),
        "method": method,
        "optimizer_success": optimizer_success,
        "message": message,
        "residual_inf": residual,
    }


def _orbit_record(q_cycle: FloatArray, a: float, rho: float, seed_word: Sequence[int], solve: dict[str, Any]) -> dict[str, Any]:
    model = HenonHomotopy(a=a, rho=rho)
    q = _canonical_numeric_cycle(q_cycle)
    # In H(q_i,q_{i-1})=(q_{i+1},q_i), ordered phase-space points are
    # (q_i,q_{i-1}).
    points = np.column_stack([q, np.roll(q, 1)])
    monodromy = model.monodromy(points)
    direct_determinant = float(np.linalg.det(monodromy))
    analytic_determinant = model.monodromy_determinant(q.size)
    eigenvalues = np.linalg.eigvals(monodromy)
    record: dict[str, Any] = {
        "period": int(q.size),
        "seed_word": "".join(str(bit) for bit in seed_word),
        "q": [float(value) for value in q],
        "residual_inf": float(np.linalg.norm(cyclic_residual(q, a, rho), ord=np.inf)),
        "monodromy": [[float(value) for value in row] for row in monodromy],
        "monodromy_trace": float(np.trace(monodromy)),
        # The local-product value is algebraically exact.  The direct
        # determinant is retained as a conditioning diagnostic: for strongly
        # hyperbolic long cycles it subtracts two large, nearly equal products.
        "monodromy_determinant": analytic_determinant,
        "monodromy_determinant_direct_float64": direct_determinant,
        "monodromy_determinant_direct_absolute_error": abs(direct_determinant - analytic_determinant),
        "determinant_source": "product_of_pointwise_determinants_rho^period",
        "multipliers": [
            {"real": float(value.real), "imag": float(value.imag)} for value in eigenvalues
        ],
        "solve_method": str(solve["method"]),
    }
    if np.isclose(rho, 1.0, rtol=0.0, atol=1e-14):
        record["periodic_action"] = model.periodic_action(q)
    return record


def build_orbit_ledger(
    a: float,
    rho: float,
    max_period: int,
    *,
    regime: str = "exploratory_incomplete",
    residual_tolerance: float = 1e-10,
    dedup_tolerance: float = 1e-8,
) -> dict[str, Any]:
    """Build a deterministic ledger from primitive binary necklace seeds.

    The binary seed family is complete only in a validated full two-shift
    regime.  Callers must state the regime explicitly; the mixed-regime
    default is intentionally marked incomplete.
    """

    if max_period < 1:
        raise ValueError("max_period must be positive")
    if regime not in {"full_shift_positive_control", "exploratory_incomplete"}:
        raise ValueError("unrecognized regime")

    periods: list[dict[str, Any]] = []
    every_count_matches = True
    for period in range(1, max_period + 1):
        expected = binary_primitive_orbit_count(period)
        necklaces = primitive_binary_necklaces(period)
        accepted: list[tuple[FloatArray, tuple[int, ...], dict[str, Any]]] = []
        rejected: list[dict[str, Any]] = []
        seed_amplitude = 1.0 / np.sqrt(abs(a)) if a != 0.0 else 1.0
        for word in necklaces:
            initial = np.array([seed_amplitude if bit else -seed_amplitude for bit in word])
            corrected, solve = solve_cycle(initial, a, rho, residual_tolerance=residual_tolerance)
            if not solve["accepted"]:
                rejected.append({"seed_word": "".join(map(str, word)), "reason": "residual", **solve})
                continue
            actual_period = numerical_minimal_period(corrected, tolerance=dedup_tolerance)
            if actual_period != period:
                rejected.append(
                    {
                        "seed_word": "".join(map(str, word)),
                        "reason": "collapsed_to_lower_period",
                        "actual_period": actual_period,
                        **solve,
                    }
                )
                continue
            if any(_same_orbit(corrected, prior[0], dedup_tolerance) for prior in accepted):
                rejected.append({"seed_word": "".join(map(str, word)), "reason": "duplicate", **solve})
                continue
            accepted.append((corrected, word, solve))

        records = [_orbit_record(cycle, a, rho, word, solve) for cycle, word, solve in accepted]
        records.sort(key=lambda record: tuple(record["q"]))
        count_matches = len(records) == expected
        every_count_matches &= count_matches
        periods.append(
            {
                "period": period,
                "binary_primitive_necklaces": expected,
                "seeds_attempted": len(necklaces),
                "orbits_found": len(records),
                "count_matches_binary_shift": count_matches,
                "orbits": records,
                "rejected_seeds": rejected,
            }
        )

    if regime == "full_shift_positive_control":
        completeness = (
            "validated_against_binary_necklace_counts"
            if every_count_matches
            else "positive_control_failed_binary_count_check"
        )
    else:
        completeness = "incomplete_binary_seed_exploration_no_completeness_claim"
    return {
        "schema_version": 1,
        "map": "H_{a,rho}(x,y)=(1-a*x^2-rho*y,x)",
        "parameters": {"a": float(a), "rho": float(rho)},
        "max_period": int(max_period),
        "regime": regime,
        "deterministic": True,
        "external_arithmetic_data_used": False,
        "completeness_status": completeness,
        "all_binary_counts_match": bool(every_count_matches),
        "periods": periods,
    }
