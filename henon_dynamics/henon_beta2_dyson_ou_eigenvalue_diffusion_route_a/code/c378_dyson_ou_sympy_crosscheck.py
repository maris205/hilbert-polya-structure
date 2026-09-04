#!/usr/bin/env python3
"""Independent symbolic verification lane for HCS-C378."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c378 SymPy lane refuses optimized Python")

import argparse

import sympy as s


def partitions(total, max_parts, ceiling=None):
    if total == 0:
        yield ()
        return
    if max_parts == 0:
        return
    upper = min(total, total if ceiling is None else ceiling)
    for first in range(upper, 0, -1):
        for tail in partitions(total - first, max_parts - 1, first):
            yield (first,) + tail


def dyson_generator(polynomial, variables):
    value = s.Rational(1, 2) * sum(s.diff(polynomial, x, 2) for x in variables)
    for i, x in enumerate(variables):
        drift = -x / 2 + sum(1 / (x - variables[j]) for j in range(len(variables)) if j != i)
        value += drift * s.diff(polynomial, x)
    return s.cancel(s.together(value))


def main():
    argparse.ArgumentParser().parse_args()
    checks = 0
    z = s.symbols("z")
    for degree in range(17):
        hermite = s.hermite_prob(degree, z)
        residual = s.diff(hermite, z, 2) - z * s.diff(hermite, z) + degree * hermite
        assert s.expand(residual) == 0
        checks += 1

    for n in range(2, 6):
        variables = s.symbols(f"x0:{n}")
        h = s.prod(variables[j] - variables[i] for i in range(n) for j in range(i + 1, n))
        d = n * (n - 1) // 2
        assert s.expand(sum(s.diff(h, x, 2) for x in variables)) == 0
        checks += 1
        assert s.expand(sum(x * s.diff(h, x) for x in variables) - d * h) == 0
        checks += 1
        log_density_gradient = [
            -x + 2 * sum(1 / (x - variables[j]) for j in range(n) if j != i)
            for i, x in enumerate(variables)
        ]
        for i, x in enumerate(variables):
            asserted_drift = -x / 2 + sum(1 / (x - variables[j]) for j in range(n) if j != i)
            assert s.cancel(log_density_gradient[i] / 2 - asserted_drift) == 0
            checks += 1

    # The Slater quotient realizes every partition through small exhaustive degrees.
    spectral_checks = 0
    for n in (2, 3):
        variables = s.symbols(f"u0:{n}")
        h = s.prod(variables[j] - variables[i] for i in range(n) for j in range(i + 1, n))
        d = n * (n - 1) // 2
        for degree in range(7):
            for partition in partitions(degree, n):
                padded = list(partition) + [0] * (n - len(partition))
                indices = [padded[n - 1 - i] + i for i in range(n)]
                slater = s.det(s.Matrix([[s.hermite_prob(m, x) for x in variables] for m in indices]))
                quotient = s.cancel(slater / h)
                assert s.denom(quotient) == 1
                residual = s.cancel(dyson_generator(quotient, variables) + s.Rational(degree, 2) * quotient)
                assert residual == 0
                assert sum(indices) == d + degree
                spectral_checks += 1
    checks += spectral_checks

    # Coefficients of the finite partition product equal the level multiplicities.
    q = s.symbols("q")
    partition_checks = 0
    for n in range(1, 9):
        coefficients = [0] * 33
        coefficients[0] = 1
        for part in range(1, n + 1):
            for degree in range(part, 33):
                coefficients[degree] += coefficients[degree - part]
        product_series = s.Integer(1)
        for part in range(1, n + 1):
            product_series = s.Poly(
                product_series * sum(q ** (part * repeat) for repeat in range(33 // part + 1)), q
            )
            product_series = s.Poly(
                sum(product_series.coeff_monomial(q**degree) * q**degree for degree in range(33)), q
            )
        for degree in range(33):
            assert product_series.coeff_monomial(q**degree) == coefficients[degree]
            partition_checks += 1
    checks += partition_checks

    # The first excited eigenfunction is the center-of-mass coordinate, fixing the sharp gap.
    for n in range(1, 9):
        variables = s.symbols(f"v0:{n}")
        center = sum(variables)
        assert s.cancel(dyson_generator(center, variables) + center / 2) == 0
        checks += 1

    print(
        f"C378 SymPy PASS: exact_symbolic_checks={checks} "
        f"slater_partition_checks={spectral_checks} heat_trace_coefficients={partition_checks}"
    )


if __name__ == "__main__":
    main()
