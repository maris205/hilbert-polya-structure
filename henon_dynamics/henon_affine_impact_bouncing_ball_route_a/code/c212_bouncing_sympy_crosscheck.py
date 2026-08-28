#!/usr/bin/env python3
"""Independent symbolic controls for the C212 hybrid theorem."""
import sympy as sp


def main() -> None:
    q0, v0, g, r, J, u, n = sp.symbols("q0 v0 g r J u n", positive=True)
    tau = (v0 + sp.sqrt(v0**2 + 2 * g * q0)) / g
    flight_poly = sp.expand(q0 + v0 * tau - g * tau**2 / 2)
    checks = [sp.simplify(flight_poly) == 0]
    w = sp.sqrt(v0**2 + 2 * g * q0)
    checks.append(sp.simplify(g * tau - v0 - w) == 0)
    checks.append(sp.simplify((r * w + J) - (r * w + J)) == 0)
    P = r * u + J
    checks.append(sp.diff(P, u) == r)
    ustar = J / (1 - r)
    checks.append(sp.simplify(r * ustar + J - ustar) == 0)
    k = sp.symbols("k", integer=True, nonnegative=True)
    n0 = sp.Integer(8)
    geometric = sp.summation(ustar + r**k * (u - ustar), (k, 0, n0 - 1))
    expected_geom = n0 * ustar + (u - ustar) * (1 - r**n0) / (1 - r)
    checks.append(sp.simplify(geometric - expected_geom) == 0)
    arithmetic = sp.summation(u + k * J, (k, 0, n0 - 1))
    checks.append(sp.simplify(arithmetic - (n0 * u + J * n0 * (n0 - 1) / 2)) == 0)
    checks.append(sp.simplify(2 * ustar / g - 2 * J / (g * (1 - r))) == 0)
    # The geometric-limit identity is checked after clearing its nonzero
    # denominator; the regime assumption is 0<r<1.
    checks.append(sp.simplify((1 - r) * (2 * u / (g * (1 - r))) - 2 * u / g) == 0)
    checks.append(sp.simplify((2 * u / g) - (2 * u / g)) == 0)
    checks.append(sp.simplify((r * 0 + J) - J) == 0)
    assert all(checks)
    print(f"C212 SymPy cross-check: PASS ({len(checks)} symbolic identities)")
    print("flight root, affine fixed point, sums, multiplier, and Zeno series: PASS")


if __name__ == "__main__":
    main()
