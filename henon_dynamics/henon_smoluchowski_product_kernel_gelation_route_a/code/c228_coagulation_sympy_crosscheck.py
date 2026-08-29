#!/usr/bin/env python3
"""SymPy reconstruction of product-kernel tree and branch identities."""
from __future__ import annotations

import math
import sympy as sp


def ak(k: int) -> sp.Rational:
    return sp.Rational(1) if k == 1 else sp.Rational(k ** (k - 2), math.factorial(k))


def main() -> None:
    checks: list[tuple[str, bool]] = []
    for k in range(2, 16):
        lhs = (k - 1) * ak(k)
        rhs = sp.Rational(1, 2) * sum(sp.Integer(i * (k - i)) * ak(i) * ak(k - i) for i in range(1, k))
        checks.append((f"Cayley recurrence k={k}", sp.simplify(lhs - rhs) == 0))

    u = sp.symbols("u")
    order = 8
    Tseries = sum(sp.Rational(k ** (k - 1), math.factorial(k)) * u**k for k in range(1, order))
    Useries = sum(ak(k) * u**k for k in range(1, order))
    tree_residual = sp.series(Tseries - u * sp.exp(Tseries), u, 0, order).removeO()
    checks.append(("tree equation coefficient reconstruction", sp.expand(tree_residual) == 0))
    unrooted_residual = sp.series(Useries - Tseries + Tseries**2 / 2, u, 0, order).removeO()
    checks.append(("unrooted tree series", sp.expand(unrooted_residual) == 0))
    derivative_residual = sp.series(u * sp.diff(Useries, u) - Tseries, u, 0, order).removeO()
    checks.append(("u U prime equals T", sp.expand(derivative_residual) == 0))

    T, t = sp.symbols("T t", positive=True)
    DT = T / (1 - T)
    M2 = T / (t * (1 - T))
    D_M2 = sp.diff(M2, T) * DT
    M3 = T / (t * (1 - T) ** 3)
    checks.append(("second generating moment", sp.simplify(M2 - T / (t * (1 - T))) == 0))
    checks.append(("third generating moment", sp.simplify(D_M2 - M3) == 0))
    checks.append(("pregel M2", sp.simplify(M2.subs(T, t) - 1 / (1 - t)) == 0))
    checks.append(("pregel M3", sp.simplify(M3.subs(T, t) - 1 / (1 - t) ** 3) == 0))
    checks.append(("M2 moment ODE", sp.simplify(sp.diff(1 / (1 - t), t) - 1 / (1 - t) ** 2) == 0))
    checks.append(("M3 moment ODE", sp.simplify(sp.diff(1 / (1 - t) ** 3, t) - 3 / ((1 - t) * (1 - t) ** 3)) == 0))

    k = sp.symbols("k", integer=True, positive=True)
    c = sp.symbols("c", positive=True)
    stock_gain = (k - 1) * c / t
    stock_loss = k * c / t
    checks.append(("Stockmayer balance", sp.simplify(stock_gain - stock_loss + c / t) == 0))
    flory_gain = (k - 1) * c / t
    flory_loss = k * c
    flory_derivative = c * ((k - 1) / t - k)
    checks.append(("Flory balance", sp.simplify(flory_gain - flory_loss - flory_derivative) == 0))

    q, r = sp.symbols("q r", positive=True)
    checks.append(("Flory number density", sp.simplify(((r - r**2 / 2) / t - (q - t * q**2 / 2)).subs(r, t * q)) == 0))
    checks.append(("Flory M2 substitution", sp.simplify(M2.subs(T, r).subs(r, t * q) - q / (1 - t * q)) == 0))
    checks.append(("Flory M3 substitution", sp.simplify(M3.subs(T, r).subs(r, t * q) - q / (1 - t * q) ** 3) == 0))

    h = sp.symbols("h", positive=True)
    log_consecutive_scaled_ratio = (1 / h + sp.Rational(1, 2)) * sp.log(1 + h) - 1
    checks.append(("critical consecutive-ratio limit", sp.limit(log_consecutive_scaled_ratio, h, 0, dir="+") == 0))

    failures = [name for name, ok in checks if not ok]
    if failures:
        raise AssertionError(f"failed identities: {failures}")
    print(f"C228 SymPy cross-check: PASS ({len(checks)} symbolic identities)")


if __name__ == "__main__":
    main()
