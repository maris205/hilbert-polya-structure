#!/usr/bin/env python3
"""Independent symbolic identities for the HCS-C304 theorem."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    alpha, kappa, n, m, t, amplitude = sp.symbols(
        "alpha kappa n m t amplitude", real=True
    )
    checks = 0

    def zero(expr, label):
        nonlocal checks
        if sp.simplify(expr) != 0:
            raise AssertionError(label)
        checks += 1

    sigma = alpha * n - kappa * n**2
    energy_coefficient = kappa * n - alpha
    zero(sigma + n * energy_coefficient, "rate-energy factorization")
    zero(
        energy_coefficient * sigma * amplitude**2
        + n * energy_coefficient**2 * amplitude**2,
        "modal energy dissipation",
    )
    zero(
        sigma - (alpha**2 / (4 * kappa) - kappa * (n - alpha / (2 * kappa)) ** 2),
        "completed square",
    )
    zero(
        (alpha * n - kappa * n**2) - (alpha * m - kappa * m**2)
        - (n - m) * (alpha - kappa * (n + m)),
        "shell tie factorization",
    )
    zero(sp.diff(sp.exp(t * sigma), t) - sigma * sp.exp(t * sigma), "modal flow")
    zero(sp.diff(sp.exp(t * sigma), t, 2) - sigma**2 * sp.exp(t * sigma), "analytic orbit")

    # Exact finite regression points spanning stable, critical, unstable, and ties.
    cases = [
        (1, -1), (1, 1), (1, 5), (2, 1), (1, 3), (1, 0),
        (2, 7), (2, -1), (2, 2), (2, 6), (3, 2), (3, 3),
        (3, 15), (1, -2), (2, 13),
    ]
    for kap, alp in cases:
        zero(sigma.subs({kappa: kap, alpha: alp, n: 1}) - (alp - kap), "first shell")

    # Shell-tie samples: sigma_n=sigma_m iff alpha=kappa(n+m).
    for kap, left, right in ((1, 1, 4), (1, 1, 2), (2, 1, 2), (3, 2, 3)):
        alp = kap * (left + right)
        zero(
            sigma.subs({kappa: kap, alpha: alp, n: left})
            - sigma.subs({kappa: kap, alpha: alp, n: right}),
            "represented tie",
        )

    # The analytic exhaustion argument is algebraic, not a finite-shell assumption.
    j = sp.symbols("j", integer=True, positive=True)
    zero(
        (alpha * j - kappa * j**2) - (alpha - kappa)
        - (j - 1) * (alpha - kappa * (j + 1)),
        "monotonic comparison with shell one",
    )
    zero((alpha * n - kappa * n**2) - n * (alpha - kappa * n), "cutoff sign")

    # Singular kappa=0 face and critical shell.
    zero(sigma.subs(kappa, 0) - alpha * n, "kappa-zero spectrum")
    zero(sigma.subs({alpha: kappa, n: 1}), "critical first shell")
    zero(sigma.subs({alpha: kappa, n: 2}) + 2 * kappa, "critical higher shell")

    # Low-dimensional multiplicity coefficients obtained independently by expansion.
    z = sp.symbols("z")
    one_dimensional = 1 + 2 * z + 2 * z**4 + 2 * z**9
    for dimension, expected_first in ((1, 2), (2, 4), (3, 6), (4, 8), (5, 10), (6, 12)):
        polynomial = sp.expand(one_dimensional**dimension)
        zero(polynomial.coeff(z, 1) - expected_first, "first-shell multiplicity")

    print(f"C304 SymPy cross-check: PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
