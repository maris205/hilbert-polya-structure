#!/usr/bin/env python3
"""SymPy reconstruction of the HCS-C227 Lorenz identities."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    x, y, z, ell = sp.symbols("x y z ell", real=True)
    sigma, beta, rho = sp.symbols("sigma beta rho", positive=True, real=True)
    f = sp.Matrix([sigma * (y - x), x * (rho - z) - y, x * y - beta * z])
    J = f.jacobian([x, y, z])
    checks: list[tuple[str, bool]] = []

    checks.append(("constant divergence", sp.simplify(sp.trace(J) + sigma + beta + 1) == 0))
    c = rho + sigma
    V = x**2 + y**2 + (z - c) ** 2
    Vdot = sp.expand(sp.Matrix([sp.diff(V, v) for v in (x, y, z)]).dot(f))
    ledger = -2 * sigma * x**2 - 2 * y**2 - beta * z**2 - beta * (z - c) ** 2 + beta * c**2
    checks.append(("Lyapunov cross-term cancellation", sp.expand(Vdot - ledger) == 0))
    checks.append(("completed-square identity", sp.expand(-2 * beta * z * (z - c) + beta * z**2 + beta * (z - c) ** 2 - beta * c**2) == 0))

    J0 = J.subs({x: 0, y: 0, z: 0})
    chi0 = sp.factor((ell * sp.eye(3) - J0).det())
    expected0 = (ell + beta) * (ell**2 + (sigma + 1) * ell + sigma * (1 - rho))
    checks.append(("origin characteristic factorization", sp.expand(chi0 - expected0) == 0))

    amp = sp.symbols("amp", real=True)
    Jwing = J.subs({x: amp, y: amp, z: rho - 1})
    chiwing_raw = sp.Poly(sp.expand((ell * sp.eye(3) - Jwing).det()), amp)
    chiwing = sp.expand(chiwing_raw.as_expr().subs(amp**2, beta * (rho - 1)))
    expected_wing = ell**3 + (sigma + beta + 1) * ell**2 + beta * (sigma + rho) * ell + 2 * sigma * beta * (rho - 1)
    checks.append(("wing characteristic polynomial", sp.expand(chiwing - expected_wing) == 0))

    margin = sp.expand((sigma + beta + 1) * (sigma + rho) - 2 * sigma * (rho - 1))
    margin2 = sigma * (sigma + beta + 3) + (beta + 1 - sigma) * rho
    checks.append(("Routh-Hurwitz affine margin", sp.expand(margin - margin2) == 0))

    rho_h = sigma * (sigma + beta + 3) / (sigma - beta - 1)
    hopf_poly = sp.together(expected_wing.subs(rho, rho_h))
    hopf_factor = (ell + sigma + beta + 1) * (ell**2 + beta * (sigma + rho_h))
    checks.append(("Hopf factorization", sp.factor(sp.together(hopf_poly - hopf_factor)) == 0))
    checks.append(("Hopf margin zero", sp.factor(sp.together(margin2.subs(rho, rho_h))) == 0))
    checks.append(("rho_H minus one numerator", sp.factor(sp.together(rho_h - 1) * (sigma - beta - 1) - (sigma + 1) * (sigma + beta + 1)) == 0))

    s = sp.symbols("s", real=True)
    E_sigma0 = {sigma: 0, x: s, y: beta * rho * s / (beta + s**2), z: rho * s**2 / (beta + s**2)}
    f_sigma0 = sp.simplify(f.subs(E_sigma0))
    checks.append(("sigma=0 equilibrium curve", all(sp.factor(v) == 0 for v in f_sigma0)))
    chi_sigma0 = sp.factor((ell * sp.eye(3) - J.subs(E_sigma0)).det())
    expected_sigma0 = ell * (ell**2 + (1 + beta) * ell + beta + s**2)
    checks.append(("sigma=0 transverse polynomial", sp.factor(chi_sigma0 - expected_sigma0) == 0))

    z0 = sp.symbols("z0", real=True)
    J_beta0 = J.subs({beta: 0, x: 0, y: 0, z: z0})
    chi_beta0 = sp.factor((ell * sp.eye(3) - J_beta0).det())
    expected_beta0 = ell * (ell**2 + (sigma + 1) * ell + sigma * (1 - rho + z0))
    checks.append(("beta=0 transverse polynomial", sp.expand(chi_beta0 - expected_beta0) == 0))

    f_double_line_z = f.subs({sigma: 0, beta: 0, x: 0, y: 0})
    f_double_line_x = f.subs({sigma: 0, beta: 0, y: 0, z: rho})
    checks.append(("double-zero z-line", all(sp.simplify(v) == 0 for v in f_double_line_z)))
    checks.append(("double-zero x-line", all(sp.simplify(v) == 0 for v in f_double_line_x)))

    failed = [name for name, ok in checks if not ok]
    if failed:
        raise AssertionError(f"failed symbolic identities: {failed}")
    print(f"C227 SymPy cross-check: PASS ({len(checks)} symbolic identities)")


if __name__ == "__main__":
    main()
