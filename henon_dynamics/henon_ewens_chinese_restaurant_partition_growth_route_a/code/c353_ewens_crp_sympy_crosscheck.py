#!/usr/bin/env python3
"""Independent symbolic combinatorics lane for HCS-C353."""
from __future__ import annotations

import math
import sys
from collections import Counter

import sympy as sp


def need(condition, label):
    if condition is not True and condition != sp.S.true:
        raise AssertionError(label)


def partitions(remaining, minimum=1):
    if remaining == 0:
        yield ()
    for first in range(minimum, remaining + 1):
        for tail in partitions(remaining - first, first):
            yield (first,) + tail


def falling_integer(value, order):
    result = 1
    for offset in range(order):
        result *= value - offset
    return result


def main():
    if sys.flags.optimize:
        raise RuntimeError("C353 SymPy lane refuses optimized Python")
    theta, z, n_symbol = sp.symbols("theta z n", positive=True)
    checks = 0

    # Unsigned Stirling coefficients exactly expand the rising factorial.
    table = {(0, 0): 1}
    for n in range(1, 21):
        for k in range(1, n + 1):
            table[n, k] = table.get((n - 1, k - 1), 0) + (n - 1) * table.get((n - 1, k), 0)
        rising = sp.prod(theta + i for i in range(n))
        polynomial = sum(table[n, k] * theta ** k for k in range(1, n + 1))
        need(sp.expand(rising - polynomial) == 0, f"Stirling expansion {n}")
        checks += 1

        # Independent-innovation PGF equals (theta*z) rising n /(theta rising n).
        bernoulli_pgf = sp.prod((i - 1 + theta * z) / (theta + i - 1)
                                for i in range(1, n + 1))
        target_pgf = sp.prod(theta * z + i for i in range(n)) / rising
        need(sp.cancel(bernoulli_pgf - target_pgf) == 0, f"PGF factorization {n}")
        checks += 1

    # Differentiate a generic independent-Bernoulli product; this avoids
    # disguising the probabilistic identity behind enormous expanded fractions.
    for count in range(1, 9):
        probabilities = sp.symbols(f"p0:{count}")
        pgf = sp.prod(1 - p + p * z for p in probabilities)
        mean = sp.diff(pgf, z).subs(z, 1)
        second = sp.diff(pgf, z, 2).subs(z, 1)
        variance = sp.expand(second + mean - mean ** 2)
        need(sp.expand(mean - sum(probabilities)) == 0, f"Bernoulli mean {count}")
        need(sp.expand(variance - sum(p * (1 - p) for p in probabilities)) == 0,
             f"Bernoulli variance {count}")
        checks += 2

    # Sum exact count-vector weights and selected factorial moments symbolically.
    for n in range(1, 11):
        rising = sp.prod(theta + i for i in range(n))
        rows = []
        for parts in partitions(n):
            counts = Counter(parts)
            denominator = math.prod(j ** count * math.factorial(count)
                                    for j, count in counts.items())
            multiplicity = math.factorial(n) // denominator
            rows.append((counts, multiplicity, len(parts)))
        total = sum(mult * theta ** blocks for _, mult, blocks in rows)
        need(sp.expand(total - rising) == 0, f"occupancy normalization {n}")
        checks += 1
        for j in range(1, min(4, n) + 1):
            for order in range(1, min(3, n // j) + 1):
                direct = sum(mult * theta ** blocks * falling_integer(counts.get(j, 0), order)
                             for counts, mult, blocks in rows) / rising
                occupied = j * order
                formula = ((theta / j) ** order * math.factorial(n) / math.factorial(n - occupied)
                           * sp.prod(theta + i for i in range(n - occupied)) / rising)
                need(sp.cancel(direct - formula) == 0, f"factorial moment n={n} j={j} r={order}")
                checks += 1

    # Joint two-size factorial moments, the essential independence-in-the-limit test.
    for n in range(3, 11):
        rising = sp.prod(theta + i for i in range(n))
        rows = []
        for parts in partitions(n):
            counts = Counter(parts)
            denominator = math.prod(j ** count * math.factorial(count)
                                    for j, count in counts.items())
            rows.append((counts, math.factorial(n) // denominator, len(parts)))
        for j in range(1, 4):
            for ell in range(j + 1, 5):
                occupied = j + ell
                if occupied > n:
                    continue
                direct = sum(mult * theta ** blocks * counts.get(j, 0) * counts.get(ell, 0)
                             for counts, mult, blocks in rows) / rising
                formula = (theta / j) * (theta / ell) * math.factorial(n) / math.factorial(n - occupied)
                formula *= sp.prod(theta + i for i in range(n - occupied)) / rising
                need(sp.cancel(direct - formula) == 0, f"joint moment n={n} j={j} ell={ell}")
                checks += 1

    # The finite factorial-moment correction tends to one for every fixed occupancy.
    for occupied in range(1, 13):
        correction = sp.prod(n_symbol - q for q in range(occupied)) / sp.prod(
            theta + n_symbol - occupied + q for q in range(occupied))
        need(sp.limit(correction, n_symbol, sp.oo) == 1, f"moment limit {occupied}")
        checks += 1

    # Fixed-n boundary chambers.
    for n in range(1, 17):
        rising = sp.prod(theta + i for i in range(n))
        one_block = theta * math.factorial(n - 1) / rising
        all_singletons = theta ** n / rising
        need(sp.limit(one_block, theta, 0, dir="+") == 1, f"theta zero {n}")
        need(sp.limit(all_singletons, theta, sp.oo) == 1, f"theta infinity {n}")
        checks += 2
    print(f"C353 SymPy cross-check: PASS {checks} exact symbolic checks")


if __name__ == "__main__":
    main()
