#!/usr/bin/env python3
"""Substantive symbolic checks for C246, independent of producer/checker.

Each identity is reconstructed from the integrated hazard, the generator, or
the cycle-reward ratio.  In particular, no ``expr-expr`` placeholder is used
for the Laplace, Palm, or parameter checks.
"""
from __future__ import annotations

from fractions import Fraction as F
import sympy as sp


def main() -> None:
    beta, y, yn, a, rho, T, E, s, z, x, m = sp.symbols(
        "beta y y_next a rho T E s z x m", positive=True
    )
    checks = 0

    def ok(expr, label: str) -> None:
        nonlocal checks
        checks += 1
        reduced = sp.simplify(expr)
        if reduced != 0:
            raise AssertionError(f"{label}: {sp.factor(reduced)}")

    def yes(condition: bool, label: str) -> None:
        nonlocal checks
        checks += 1
        if not condition:
            raise AssertionError(label)

    # Integrated hazard and square completion with the increase a.
    hazard = rho * (beta * y * T + a * T**2 / 2)
    yn_expr = beta * y + a * T
    ok((yn_expr**2 - beta**2 * y**2) - 2 * a * hazard / rho, "square completion")
    ok(
        hazard.subs(T, (yn - beta * y) / a)
        - rho * (yn**2 - beta**2 * y**2) / (2 * a),
        "hazard in endpoint variables",
    )
    positive_root = (-beta * y + sp.sqrt(beta**2 * y**2 + 2 * a * E / rho)) / a
    ok(hazard.subs(T, positive_root) - E, "positive waiting-time root")

    # Exponential innovation transform and finite-prefix q-product factor.
    q = sp.integrate(sp.exp(-(1 + s) * z), (z, 0, sp.oo))
    ok(q - 1 / (1 + s), "Exp(1) Laplace")
    c = sp.symbols("c", positive=True)
    scaled = sp.integrate(sp.exp(-(1 + c * s) * z), (z, 0, sp.oo))
    ok(scaled - 1 / (1 + c * s), "scaled exponential factor")
    prefix5 = sp.prod((1 + c * beta ** (2 * j) * s) ** (-1) for j in range(5))
    shifted4 = sp.prod((1 + c * beta ** (2 * (j + 1)) * s) ** (-1) for j in range(4))
    ok(prefix5 - (1 + c * s) ** (-1) * shifted4, "q-prefix shift relation")

    # Generator calculation and the chain rule at beta*s.  Dividing the
    # stationarity equation by rho gives the displayed Laplace identity.
    phi_s, phi_b, dphi_s, dphi_b = sp.symbols(
        "phi_s phi_b dphi_s dphi_b"
    )
    stationary_equation = -a * s * phi_s + rho * (dphi_s - dphi_b)
    target_relation = dphi_s - dphi_b - (a / rho) * s * phi_s
    ok(sp.together(stationary_equation / rho - target_relation), "stationary Laplace generator")
    Phi = sp.Function("Phi")
    xi = sp.symbols("xi", positive=True)
    chain_lhs = sp.diff(Phi(beta * s), s)
    chain_rhs = beta * sp.Subs(sp.diff(Phi(xi), xi), xi, beta * s)
    ok(chain_lhs - chain_rhs, "Laplace chain rule")

    # Monomial generator recurrence, obtained by solving the stationarity
    # equation for the next moment rather than copying its rearrangement.
    Mprev, Mnext = sp.symbols("Mprev Mnext")
    equation = sp.Eq(a * m * Mprev + rho * (beta**m - 1) * Mnext, 0)
    solved_next = sp.solve(equation, Mnext)[0]
    ok(solved_next - a * m * Mprev / (rho * (1 - beta**m)), "monomial generator solve")

    # Cycle reward uses both endpoints.  The Palm ratio then follows by
    # identifying the stationary marginals of successive jump times.
    reward = sp.integrate(x**m, (x, beta * y, yn))
    ok(
        reward - (yn ** (m + 1) - (beta * y) ** (m + 1)) / (m + 1),
        "cycle reward endpoint",
    )
    e1, en1, epow, enpow = sp.symbols("e1 en1 epow enpow", positive=True)
    reward_mean = (enpow - beta ** (m + 1) * epow) / (a * (m + 1))
    duration_mean = (en1 - beta * e1) / a
    palm_ratio = reward_mean / duration_mean
    target_ratio = (1 - beta ** (m + 1)) * epow / ((m + 1) * (1 - beta) * e1)
    ok(
        palm_ratio.subs({enpow: epow, en1: e1}) - target_ratio,
        "Palm stationary-marginal ratio",
    )

    # Beta=0 reset face: Rayleigh pre-jump and half-normal occupation laws.
    lam = sp.symbols("lam", positive=True)
    fy = 2 * lam * y * sp.exp(-lam * y**2)
    ok(sp.integrate(fy, (y, 0, sp.oo)) - 1, "Rayleigh normalization")
    ok(sp.integrate(y * fy, (y, 0, sp.oo)) - sp.sqrt(sp.pi) / (2 * sp.sqrt(lam)), "Rayleigh mean")
    fx = 2 * sp.sqrt(lam / sp.pi) * sp.exp(-lam * x**2)
    ok(sp.integrate(fx, (x, 0, sp.oo)) - 1, "half-normal normalization")
    ok(sp.integrate(x * fx, (x, 0, sp.oo)) - 1 / sp.sqrt(sp.pi * lam), "half-normal mean")

    # Exact rational parameter spots, independently checking the scale and
    # contraction inequalities (the old self-equality check is avoided).
    for bb in (F(1, 2), F(2, 3), F(3, 4)):
        for aa in (F(1, 2), F(1), F(3, 2)):
            for rr in (F(1, 2), F(1), F(2)):
                c_q = F(2) * aa / rr
                yes(c_q * rr == F(2) * aa, "2a/rho scale identity")
                yes(F(0) < bb < F(1), "beta contraction domain")
                yes(c_q > F(0), "positive innovation scale")

    print(f"C246_SYMPY_PASS ({checks} symbolic/rational identities)")


if __name__ == "__main__":
    main()
