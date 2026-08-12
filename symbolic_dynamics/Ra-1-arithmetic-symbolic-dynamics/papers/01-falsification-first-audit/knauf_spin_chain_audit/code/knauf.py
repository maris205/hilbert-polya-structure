"""Core arithmetic for the Knauf number-theoretic spin chain.

The convention follows equations (1.3), (1.5), and (1.7) of
A. Knauf, *The Spectrum of an Adelic Markov Operator*, arXiv:1305.6410.

No prime table or Riemann-zero table is used.  Prime factor information enters
only through a sieve that evaluates pre-specified arithmetic control weights on
the intrinsically generated values h_k(g).
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator, Sequence
from functools import lru_cache

import mpmath as mp
import numpy as np


UINT64_MASK = (1 << 64) - 1


def iter_h_levels(max_k: int) -> Iterator[tuple[int, np.ndarray, np.ndarray]]:
    """Yield ``(k, h_k, parity_k)`` in lexicographic word order.

    ``parity_k[g]`` is the intrinsic symbolic character
    ``(-1)**popcount(g)`` and is carried alongside ``h_k`` for the parity
    control.  The recurrence is

    h_k(x, 0) = h_{k-1}(x),
    h_k(x, 1) = h_{k-1}(x) + h_{k-1}(1-x).

    Complementation reverses lexicographic binary order, hence ``old[::-1]``.
    """

    if max_k < 0:
        raise ValueError("max_k must be non-negative")
    # The experiment is intentionally exhaustive, so this guard also prevents
    # accidental resource blow-ups from a typo in the locked protocol.
    if max_k > 30:
        raise ValueError("exhaustive h_k enumeration is locked to k <= 30")

    h = np.array([1], dtype=np.int64)
    parity = np.array([1], dtype=np.int8)
    yield 0, h, parity
    for k in range(1, max_k + 1):
        nxt = np.empty(2 * h.size, dtype=np.int64)
        nxt[0::2] = h
        nxt[1::2] = h + h[::-1]
        nxt_parity = np.empty(2 * parity.size, dtype=np.int8)
        nxt_parity[0::2] = parity
        nxt_parity[1::2] = -parity
        h, parity = nxt, nxt_parity
        yield k, h, parity


def h_values(k: int) -> np.ndarray:
    """Return the complete vector of ``h_k`` values."""

    for level, values, _ in iter_h_levels(k):
        if level == k:
            return values
    raise AssertionError("unreachable")


def h_value_recursive(bits: Sequence[int]) -> int:
    """Scalar reference implementation of Knauf's defining recurrence."""

    word = tuple(int(bit) for bit in bits)
    if any(bit not in (0, 1) for bit in word):
        raise ValueError("bits must contain only 0 and 1")

    @lru_cache(maxsize=None)
    def rec(current: tuple[int, ...]) -> int:
        if not current:
            return 1
        prefix, last = current[:-1], current[-1]
        if last == 0:
            return rec(prefix)
        complement = tuple(1 - bit for bit in prefix)
        return rec(prefix) + rec(complement)

    return rec(word)


def h_value_matrix(bits: Sequence[int]) -> int:
    """Independent exact 2x2-matrix implementation of ``h``.

    For L=[[1,1],[0,1]], R=[[1,0],[1,1]], the value is the sum of
    components of ``M_{g1} ... M_{gk} (1,0)^T``, with M_0=L, M_1=R.
    Python integers keep this cross-check exact.
    """

    a, b, c, d = 1, 0, 0, 1
    for raw_bit in bits:
        bit = int(raw_bit)
        if bit == 0:  # right multiply by L
            a, b, c, d = a, a + b, c, c + d
        elif bit == 1:  # right multiply by R
            a, b, c, d = a + b, b, c + d, d
        else:
            raise ValueError("bits must contain only 0 and 1")
    # Product applied to (1,0)^T is its first column.
    return a + c


def coefficient_histogram(values: np.ndarray, weights: np.ndarray | None = None) -> np.ndarray:
    """Aggregate state weights by the intrinsic integer label ``h_k(g)``."""

    if values.ndim != 1:
        raise ValueError("values must be one-dimensional")
    if weights is not None and weights.shape != values.shape:
        raise ValueError("weights and values must have identical shape")
    max_value = int(values.max(initial=0))
    if weights is None:
        return np.bincount(values, minlength=max_value + 1).astype(np.int64)
    # numpy's weighted bincount accumulates in float64.  Here all inputs and
    # totals are integral and at most 2^30, hence the conversion is exact.
    result = np.bincount(values, weights=weights, minlength=max_value + 1)
    rounded = np.rint(result).astype(np.int64)
    if not np.array_equal(result, rounded.astype(np.float64)):
        raise ArithmeticError("weighted histogram lost integer exactness")
    return rounded


def arithmetic_sieves(limit: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return Euler phi, Liouville lambda, and Moebius mu through ``limit``.

    This is a linear sieve and is algorithmic; no table of primes is loaded.
    """

    if limit < 1:
        raise ValueError("limit must be positive")
    phi = np.zeros(limit + 1, dtype=np.int64)
    liouville = np.zeros(limit + 1, dtype=np.int8)
    mobius = np.zeros(limit + 1, dtype=np.int8)
    composite = np.zeros(limit + 1, dtype=np.bool_)
    phi[1], liouville[1], mobius[1] = 1, 1, 1
    primes: list[int] = []
    for n in range(2, limit + 1):
        if not composite[n]:
            primes.append(n)
            phi[n] = n - 1
            liouville[n] = -1
            mobius[n] = -1
        for p in primes:
            value = n * p
            if value > limit:
                break
            composite[value] = True
            liouville[value] = -liouville[n]
            if n % p == 0:
                phi[value] = phi[n] * p
                mobius[value] = 0
                break
            phi[value] = phi[n] * (p - 1)
            mobius[value] = -mobius[n]
    return phi, liouville, mobius


def splitmix64_state_signs(size: int, base_seed: int, k: int) -> np.ndarray:
    """Deterministic random-sign control keyed by ``(seed, k, state_index)``.

    SplitMix64 is used as a fully specified counter hash, avoiding hidden RNG
    state and making the seed ledger portable across NumPy versions.
    """

    if size < 0 or k < 0:
        raise ValueError("size and k must be non-negative")
    indices = np.arange(size, dtype=np.uint64)
    seed_word = np.uint64(base_seed & UINT64_MASK)
    level_word = np.multiply(
        np.uint64(k), np.uint64(0xD2B74407B1CE6E93), dtype=np.uint64
    )
    z = indices ^ seed_word ^ level_word
    z = z + np.uint64(0x9E3779B97F4A7C15)
    z = (z ^ (z >> np.uint64(30))) * np.uint64(0xBF58476D1CE4E5B9)
    z = (z ^ (z >> np.uint64(27))) * np.uint64(0x94D049BB133111EB)
    z = z ^ (z >> np.uint64(31))
    return np.where((z >> np.uint64(63)) == 0, 1, -1).astype(np.int8)


def evaluate_dirichlet_complex128(coefficients: np.ndarray, s: complex) -> complex:
    """Evaluate a finite Dirichlet polynomial in complex128 arithmetic."""

    indices = np.flatnonzero(coefficients[1:]) + 1
    if indices.size == 0:
        return 0.0 + 0.0j
    coeff = coefficients[indices].astype(np.float64, copy=False)
    terms = np.exp(-np.complex128(s) * np.log(indices.astype(np.float64)))
    return complex(np.dot(coeff, terms))


def evaluate_dirichlet_mpmath(
    coefficients: np.ndarray, s: complex, dps: int
) -> tuple[str, str]:
    """Evaluate a finite Dirichlet polynomial using arbitrary precision.

    Decimal strings are returned so that leaving ``mp.workdps`` cannot round
    the audit value back to the process-global precision or binary64.
    """

    if dps < 20:
        raise ValueError("dps must be at least 20")
    indices = np.flatnonzero(coefficients[1:]) + 1
    with mp.workdps(dps):
        mp_s = mp.mpc(s.real, s.imag)
        terms = (
            mp.mpf(int(coefficients[n])) * mp.power(mp.mpf(int(n)), -mp_s)
            for n in indices
        )
        value = mp.fsum(terms)
        return mp.nstr(mp.re(value), n=dps), mp.nstr(mp.im(value), n=dps)


def analytic_unsigned(s: complex, dps: int = 100) -> complex | None:
    """Meromorphic ratio zeta(s-1)/zeta(s); None at a pole."""

    with mp.workdps(dps):
        mp_s = mp.mpc(s.real, s.imag)
        try:
            value = mp.zeta(mp_s - 1) / mp.zeta(mp_s)
        except (ValueError, ZeroDivisionError):
            return None
        if not (mp.isfinite(mp.re(value)) and mp.isfinite(mp.im(value))):
            return None
        return complex(float(mp.re(value)), float(mp.im(value)))


def analytic_liouville(s: complex, dps: int = 100) -> complex | None:
    """Meromorphic Liouville-twisted zeta ratio from Knauf (1.5)."""

    # At s=2 the displayed quotient has an infinite denominator; its
    # meromorphic continuation has the exactly known value zero.
    if s.real == 2.0 and s.imag == 0.0:
        return 0.0 + 0.0j
    with mp.workdps(dps):
        mp_s = mp.mpc(s.real, s.imag)
        try:
            value = (
                mp.zeta(mp_s)
                * mp.zeta(2 * (mp_s - 1))
                / (mp.zeta(mp_s - 1) * mp.zeta(2 * mp_s))
            )
        except (ValueError, ZeroDivisionError):
            return None
        if not (mp.isfinite(mp.re(value)) and mp.isfinite(mp.im(value))):
            return None
        return complex(float(mp.re(value)), float(mp.im(value)))


def complete_totient_prefix(histogram: np.ndarray, phi: np.ndarray) -> int:
    """Largest N for which phi_k(n)=phi(n) for every 1 <= n <= N."""

    upper = min(histogram.size, phi.size)
    result = 0
    for n in range(1, upper):
        if int(histogram[n]) != int(phi[n]):
            break
        result = n
    return result


def complex_parts(value: complex | None) -> tuple[float | None, float | None]:
    """JSON/CSV-friendly real and imaginary parts."""

    if value is None:
        return None, None
    return float(value.real), float(value.imag)


def parse_grid(points: Iterable[dict[str, object]]) -> list[dict[str, object]]:
    """Validate and normalize a protocol grid."""

    normalized: list[dict[str, object]] = []
    seen: set[str] = set()
    for point in points:
        grid_id = str(point["id"])
        if grid_id in seen:
            raise ValueError(f"duplicate grid id: {grid_id}")
        seen.add(grid_id)
        sigma = float(point["sigma"])
        tau = float(point["tau"])
        normalized.append({"id": grid_id, "sigma": sigma, "tau": tau})
    if not normalized:
        raise ValueError("grid must not be empty")
    return normalized
