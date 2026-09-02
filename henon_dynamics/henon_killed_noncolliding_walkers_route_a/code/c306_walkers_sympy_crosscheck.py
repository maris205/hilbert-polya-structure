#!/usr/bin/env python3
"""Exact symbolic lane for the exterior-power spectrum in HCS-C306."""
from __future__ import annotations

import itertools
import math
import sys

import sympy as sp

if sys.flags.optimize:
    raise RuntimeError("HCS-C306 SymPy lane refuses python -O")


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def matrix(L: int, k: int) -> sp.Matrix:
    states = list(itertools.combinations(range(1, L + 1), k))
    index = {state: i for i, state in enumerate(states)}
    q = sp.zeros(len(states))
    for i, state in enumerate(states):
        q[i, i] = -2 * k
        for coordinate in range(k):
            for step in (-1, 1):
                trial = list(state)
                trial[coordinate] += step
                if 1 <= trial[coordinate] <= L and len(set(trial)) == k:
                    trial.sort()
                    q[i, index[tuple(trial)]] = 1
    return q


def main() -> None:
    z = sp.symbols("z")
    characteristic_cases = 0
    coefficient_identities = 0
    resolvent_moments = 0
    for L in range(1, 6):
        energies = [2 - 2 * sp.cos(sp.pi * r / (L + 1)) for r in range(1, L + 1)]
        for k in range(1, L + 1):
            q = matrix(L, k)
            modes = list(itertools.combinations(range(1, L + 1), k))
            expected = sp.prod(z + sum(energies[r - 1] for r in mode) for mode in modes)
            actual = q.charpoly(z).as_expr()
            check(sp.simplify(sp.expand(expected) - actual) == 0, f"charpoly L={L},k={k}")
            characteristic_cases += 1
            coefficient_identities += len(modes) + 1

            # Exact phase-type moments from the integer generator: positivity,
            # and the singleton Exp(2L) boundary are checked without floats.
            ones = sp.ones(q.rows, 1)
            first = (-q).inv() * ones
            second = 2 * (-q).inv() * first
            check(all(value > 0 for value in first), f"positive mean L={L},k={k}")
            check(all(value > 0 for value in second), f"positive second moment L={L},k={k}")
            if k == L:
                check(first[0] == sp.Rational(1, 2 * L), "singleton mean")
                check(second[0] == sp.Rational(2, (2 * L) ** 2), "singleton second")
            resolvent_moments += 2 * q.rows

    for L in range(1, 21):
        full_energy = sum(2 - 2 * sp.cos(sp.pi * r / (L + 1)) for r in range(1, L + 1))
        check(sp.simplify(sp.expand_trig(full_energy) - 2 * L) == 0, f"full occupancy energy L={L}")

    print("C306 SymPy cross-check PASS")
    print(f"exact_characteristic_cases={characteristic_cases} coefficient_identities={coefficient_identities}")
    print(f"exact_phase_type_moment_cells={resolvent_moments} full_occupancy_identities=20")


if __name__ == "__main__":
    main()
