#!/usr/bin/env python3
"""Exact symbolic cross-checks for the HCS-C300 Riemann theorem."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    rho, m, a = sp.symbols("rho m a", positive=True)
    u = m / rho
    checks = 0

    def zero(expr, label):
        nonlocal checks
        assert sp.simplify(expr) == 0, label
        checks += 1

    flux = sp.Matrix([m, m**2 / rho + a**2 * rho])
    jac = flux.jacobian((rho, m))
    lam = sp.symbols("lam")
    zero(sp.factor(jac.charpoly(lam).as_expr() - ((lam - u)**2 - a**2)), "characteristic polynomial")
    zero(jac.det() - (u**2 - a**2), "Jacobian determinant")
    zero(jac.trace() - 2 * u, "Jacobian trace")

    eta = m**2 / (2 * rho) + a**2 * rho * sp.log(rho)
    qflux = u * (eta + a**2 * rho)
    compatibility = (sp.Matrix([sp.diff(eta, rho), sp.diff(eta, m)]).T * jac
                     - sp.Matrix([sp.diff(qflux, rho), sp.diff(qflux, m)]).T)
    zero(compatibility[0], "entropy compatibility rho")
    zero(compatibility[1], "entropy compatibility m")
    hessian = sp.hessian(eta, (rho, m))
    zero(hessian[1, 1] - 1 / rho, "entropy Hessian lower diagonal")
    zero(hessian.det() - a**2 / rho**2, "entropy Hessian determinant")

    r, r0 = sp.symbols("r r0", positive=True)
    rare = a * sp.log(r / r0)
    shock = a * (r - r0) / sp.sqrt(r * r0)
    zero(sp.limit(rare, r, r0) - sp.limit(shock, r, r0), "wave curve C0")
    zero(sp.limit(sp.diff(rare, r), r, r0) - sp.limit(sp.diff(shock, r), r, r0), "wave curve C1")
    zero(sp.limit(sp.diff(rare, r), r, r0) - a / r0, "branch derivative")

    R, rho0, u0 = sp.symbols("R rho0 u0", positive=True)
    sqrtR = sp.sqrt(R)

    def state_entropy(density, velocity):
        return density * velocity**2 / 2 + a**2 * density * sp.log(density)

    def state_flux(density, velocity):
        return velocity * (state_entropy(density, velocity) + a**2 * density)

    # Family 1: outer left state (rho0,u0), compressed right star state.
    rl, ul = rho0, u0
    rr, ur = R * rho0, u0 - a * (R - 1) / sqrtR
    s1 = u0 - a * sqrtR
    zero(s1 * (rr - rl) - (rr * ur - rl * ul), "1-shock mass")
    zero(s1 * (rr * ur - rl * ul) - ((rr * ur**2 + a**2 * rr) - (rl * ul**2 + a**2 * rl)), "1-shock momentum")
    zero(s1 - (ur - a / sqrtR), "1-shock two speeds")
    zero((s1 - (ur - a)) - a * (1 - 1 / sqrtR), "1-shock lower Lax gap")
    zero(((ul - a) - s1) - a * (sqrtR - 1), "1-shock upper Lax gap")
    d1 = state_flux(rr, ur) - state_flux(rl, ul) - s1 * (state_entropy(rr, ur) - state_entropy(rl, ul))
    closed = a**3 * rho0 * sqrtR * (sp.log(R) - (R - 1 / R) / 2)
    zero(d1 - closed, "1-shock entropy production")

    # Family 2: compressed left star state and outer right state.
    rl, ul = R * rho0, u0 + a * (R - 1) / sqrtR
    rr, ur = rho0, u0
    s2 = u0 + a * sqrtR
    zero(s2 * (rr - rl) - (rr * ur - rl * ul), "2-shock mass")
    zero(s2 * (rr * ur - rl * ul) - ((rr * ur**2 + a**2 * rr) - (rl * ul**2 + a**2 * rl)), "2-shock momentum")
    zero(s2 - (ul + a / sqrtR), "2-shock two speeds")
    zero((s2 - (ur + a)) - a * (sqrtR - 1), "2-shock lower Lax gap")
    zero(((ul + a) - s2) - a * (1 - 1 / sqrtR), "2-shock upper Lax gap")
    d2 = state_flux(rr, ur) - state_flux(rl, ul) - s2 * (state_entropy(rr, ur) - state_entropy(rl, ul))
    zero(d2 - closed, "2-shock entropy production")

    h = (R - 1 / R) / 2 - sp.log(R)
    zero(sp.diff(h, R) - (R - 1)**2 / (2 * R**2), "strict entropy derivative")
    zero(h.subs(R, 1), "entropy equality only at zero shock")

    # Centered fans and Riemann invariants.
    xi, uL, rhoL, uR, rhoR = sp.symbols("xi uL rhoL uR rhoR", positive=True)
    u1 = xi + a
    rho1 = rhoL * sp.exp((uL - u1) / a)
    zero(xi - (u1 - a), "1-fan characteristic")
    zero(u1 + a * sp.log(rho1) - (uL + a * sp.log(rhoL)), "1-fan invariant")
    u2 = xi - a
    rho2 = rhoR * sp.exp((u2 - uR) / a)
    zero(xi - (u2 + a), "2-fan characteristic")
    zero(u2 - a * sp.log(rho2) - (uR - a * sp.log(rhoR)), "2-fan invariant")

    # Two exact pressureless-boundary probes for symmetric densities.
    sep = sp.exp(-sp.Rational(1, 2) / a)
    zero(2 * a * sp.log(sep) + 1, "separating root")
    c = 1 / (2 * a)
    y = (c + sp.sqrt(c**2 + 4)) / 2
    zero(y - 1 / y - c, "compressive square-root equation")

    print(f"C300 SymPy cross-check: PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
