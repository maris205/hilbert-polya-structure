#!/usr/bin/env python3
"""Exact symbolic cross-checks for the HCS-C299 theorem formulas."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    xi, r, tau, nu, gamma, p = sp.symbols("xi r tau nu gamma p", positive=True)
    amplitude = sp.symbols("amplitude", real=True)
    checks = 0

    def zero(expr, label):
        nonlocal checks
        assert sp.simplify(expr) == 0, label
        checks += 1

    profile = amplitude * sp.exp(-xi**2 / (4 * nu))
    ode = nu * (sp.diff(profile, xi, 2) + sp.diff(profile, xi) / xi) + profile + xi * sp.diff(profile, xi) / 2
    zero(ode, "similarity ODE")
    zero(nu * xi * sp.diff(profile, xi) + xi**2 * profile / 2, "integrated first order equation")

    omega = gamma / (4 * sp.pi * nu * tau) * sp.exp(-r**2 / (4 * nu * tau))
    x = r**2 / (4 * nu * tau)
    dt_omega = sp.diff(omega, tau)
    radial_laplacian = sp.diff(omega, r, 2) + sp.diff(omega, r) / r
    zero(dt_omega - nu * radial_laplacian, "heat equation")
    zero(dt_omega - gamma * (x - 1) * sp.exp(-x) / (4 * sp.pi * nu * tau**2), "normalized derivative")

    utheta = gamma * (1 - sp.exp(-x)) / (2 * sp.pi * r)
    zero(sp.diff(r * utheta, r) / r - omega, "Biot-Savart curl")
    zero(sp.limit(utheta, r, 0), "origin velocity")
    zero(sp.limit(r * utheta, r, sp.oo) - gamma / (2 * sp.pi), "far-field circulation")

    total = sp.integrate(2 * sp.pi * r * omega, (r, 0, sp.oo))
    zero(total - gamma, "circulation")
    for k in range(9):
        moment = sp.integrate(2 * sp.pi * r ** (2 * k + 1) * omega, (r, 0, sp.oo))
        zero(moment - gamma * sp.factorial(k) * (4 * nu * tau) ** k, f"moment {k}")

    abs_gamma = sp.symbols("g", positive=True)
    positive_omega = abs_gamma / (4 * sp.pi * nu * tau) * sp.exp(-x)
    for integer_p in range(1, 7):
        lp_power = sp.integrate(2 * sp.pi * r * positive_omega**integer_p, (r, 0, sp.oo))
        target = abs_gamma**integer_p / (integer_p * (4 * sp.pi * nu * tau) ** (integer_p - 1))
        zero(lp_power - target, f"Lp {integer_p}")

    enstrophy = sp.integrate(2 * sp.pi * r * omega**2, (r, 0, sp.oo))
    palinstrophy = sp.integrate(2 * sp.pi * r * sp.diff(omega, r)**2, (r, 0, sp.oo))
    zero(enstrophy - gamma**2 / (8 * sp.pi * nu * tau), "enstrophy")
    zero(palinstrophy - gamma**2 / (16 * sp.pi * nu**2 * tau**2), "palinstrophy")
    zero(sp.diff(enstrophy, tau) + 2 * nu * palinstrophy, "dissipation identity")

    b = sp.symbols("b", positive=True)
    primitive = tau * (1 - sp.exp(-b / tau)) - b * sp.Ei(-b / tau)
    zero(sp.diff(primitive, tau) - (1 - sp.exp(-b / tau)), "Ei primitive")
    zero(sp.limit((1 - sp.exp(-b / tau)) * tau, tau, sp.oo) - b, "large-age angular kernel")
    zero(sp.limit(utheta / r, r, 0) - gamma / (8 * sp.pi * nu * tau), "solid-body core rate")

    radial_energy_density = 2 * sp.pi * r * utheta**2
    zero(sp.limit(radial_energy_density * r, r, sp.oo) - gamma**2 / (2 * sp.pi), "energy log integrand")
    # Kinetic energy has the conventional factor 1/2, hence Gamma^2/(4 pi) log R.
    zero(sp.limit(radial_energy_density * r / 2, r, sp.oo) - gamma**2 / (4 * sp.pi), "kinetic energy coefficient")

    print(f"C299 SymPy cross-check: PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
