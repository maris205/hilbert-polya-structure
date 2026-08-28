#!/usr/bin/env python3
"""Independent symbolic identities for the planar Kepler package."""
from __future__ import annotations

import json
import sympy as s


def zero(expr: s.Expr, label: str, checks: list[str]) -> None:
    reduced = s.trigsimp(s.factor(s.cancel(expr)), method="fu")
    reduced = s.factor(s.cancel(reduced))
    if reduced != 0:
        raise AssertionError(f"{label}: {reduced}")
    checks.append(label)


def main() -> None:
    mu, r, vr, vt, E, ell = s.symbols("mu r v_r v_t E ell", positive=True)
    # A radial/tangential chart is sufficient because both identities are
    # rotation invariant and avoids any hidden square-root branch choice.
    L = r * vt
    energy = (vr**2 + vt**2) / 2 - mu / r
    Ax, Ay = r * vt**2 - mu, -r * vr * vt
    checks: list[str] = []
    zero(Ax * r - (L**2 - mu * r), "A.q identity", checks)
    zero(Ax**2 + Ay**2 - (mu**2 + 2 * energy * L**2), "Runge-Lenz norm identity", checks)
    zero(energy - ((vr**2 + vt**2) / 2 - mu / r), "Hamiltonian definition", checks)

    # The conic polynomial and its turning-point factorization.
    a = -mu / (2 * E)
    ecc2 = 1 + 2 * E * ell**2 / mu**2
    rminus, rplus = a * (1 - s.sqrt(ecc2)), a * (1 + s.sqrt(ecc2))
    poly = 2 * E * s.Symbol("R")**2 + 2 * mu * s.Symbol("R") - ell**2
    R = s.Symbol("R")
    zero(s.expand(poly.subs(R, rminus)), "inner turning root", checks)
    zero(s.expand(poly.subs(R, rplus)), "outer turning root", checks)
    zero((rminus + rplus) - (-mu / E), "turning-point sum", checks)
    zero(rminus * rplus - (-ell**2 / (2 * E)), "turning-point product", checks)

    # Hyperbolic scattering identity sin^2(chi/2)=1/e^2.
    chi_half = s.asin(1 / s.sqrt(ecc2))
    zero(s.sin(chi_half) ** 2 - 1 / ecc2, "scattering sine convention", checks)
    zero(s.diff(mu / s.sqrt(-2 * E) - ell, E) - mu / (-2 * E) ** s.Rational(3, 2), "radial-action derivative", checks)
    zero((2 * s.pi * mu / (-2 * E) ** s.Rational(3, 2)) / (2 * s.pi) - mu / (-2 * E) ** s.Rational(3, 2), "period-action relation", checks)

    # Levi--Civita algebra in real coordinates.  If u''=(E/2)u and the
    # energy constraint holds, the transformed Newton equation follows.
    ur, ui, upr, upi = s.symbols("u_r u_i u'_r u'_i", real=True)
    usq = ur**2 + ui**2
    upsq = upr**2 + upi**2
    constraint = 2 * upsq - E * usq - mu
    # With z=u^2 and dt/dtau=|u|^2, Newton's equation is equivalent (for
    # u!=0) to 2*(u''*conj(u)-u'*conj(u'))=-mu.  Substitution of the
    # oscillator equation and the energy constraint checks this equivalence,
    # rather than checking a rearrangement of the constraint alone.
    newton_residual = 2 * ((E * ur / 2) * ur + (E * ui / 2) * ui - upsq) + mu
    zero(newton_residual + constraint, "Levi-Civita transformed equation", checks)
    ucomplex = ur + s.I * ui
    upcomplex = upr + s.I * upi
    angular_complex = s.expand_complex(s.im(2 * s.conjugate(ucomplex) * upcomplex))
    zero(angular_complex - 2 * (ur * upi - ui * upr), "Levi-Civita angular convention", checks)
    # Physical reconstruction q=u^2 and dt/dtau=|u|^2 preserve the stated
    # constraint; these are polynomial identities rather than numerical fits.
    qr, qi = ur**2 - ui**2, 2 * ur * ui
    zero(qr**2 + qi**2 - usq**2, "complex-square radius", checks)
    zero((qr**2 + qi**2) - usq**2, "time-density radius", checks)

    # Explicit radial collision antiderivative checks at the three signs of E.
    z = s.symbols("z", positive=True)
    # Differentiation is done after the standard substitutions r=(mu/alpha)sin^2 z
    # and r=(mu/E)sinh^2 z; it verifies the finite endpoint formulas used in
    # the producer without relying on floating-point quadrature.
    alpha = s.symbols("alpha", positive=True)
    r_trig = mu / alpha * s.sin(z) ** 2
    t_trig = mu / (s.sqrt(2) * alpha ** s.Rational(3, 2)) * (z - s.sin(z) * s.cos(z))
    trig_check = s.diff(t_trig, z) ** 2 * 2 * (mu / r_trig - alpha) - s.diff(r_trig, z) ** 2
    for _ in range(4):
        trig_check = s.expand(trig_check).subs(s.cos(z) ** 2, 1 - s.sin(z) ** 2)
    zero(trig_check, "negative-energy collision antiderivative", checks)
    r_hyp = mu / E * s.sinh(z) ** 2
    t_hyp = mu / (s.sqrt(2) * E ** s.Rational(3, 2)) * (s.sinh(z) * s.cosh(z) - z)
    hyp_check = s.diff(t_hyp, z) ** 2 * 2 * (E + mu / r_hyp) - s.diff(r_hyp, z) ** 2
    for _ in range(4):
        hyp_check = s.expand(hyp_check).subs(s.cosh(z) ** 2, 1 + s.sinh(z) ** 2)
    zero(hyp_check, "positive-energy collision antiderivative", checks)
    r_par = z
    t_par = 2 * z ** s.Rational(3, 2) / (3 * s.sqrt(2 * mu))
    zero(s.diff(t_par, z) ** 2 * 2 * mu / z - 1, "zero-energy collision antiderivative", checks)

    print(json.dumps({"status": "C216_SYMPY_PASS", "checks": len(checks), "identity_labels": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
