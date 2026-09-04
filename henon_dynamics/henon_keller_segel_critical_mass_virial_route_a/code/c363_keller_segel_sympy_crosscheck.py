#!/usr/bin/env python3
"""Independent symbolic identities for the HCS-C363 theorem contract."""
from __future__ import annotations

import sys

import sympy as sp


def zero(expr, label):
    if sp.factor(sp.together(expr)) != 0:
        raise AssertionError(label)


def main():
    if sys.flags.optimize:
        raise RuntimeError("C363 SymPy lane refuses optimized Python")
    r, lam, radius, q, mass, scale, moment = sp.symbols(
        "r lam radius q mass scale moment", positive=True)
    checks = 0

    rho = 8*lam**2/(lam**2+r**2)**2
    potential = -2*sp.log(lam**2+r**2)
    laplacian = sp.diff(potential, r, 2)+sp.diff(potential, r)/r
    zero(-laplacian-rho, "Poisson profile")
    zero(sp.diff(sp.log(rho),r)-sp.diff(potential,r), "stationary flux")
    checks += 2

    enclosed = 8*r**2/(lam**2+r**2)
    zero(sp.diff(enclosed,r)-2*r*rho, "mass primitive divided by pi")
    zero(sp.limit(enclosed,r,sp.oo)-8, "critical mass")
    checks += 2

    truncated = 8*lam**2*(
        sp.log((lam**2+radius**2)/lam**2)
        +lam**2/(lam**2+radius**2)-1)
    zero(sp.diff(truncated,radius)-2*radius**3*rho.subs(r,radius),
         "second-moment primitive divided by pi")
    if sp.limit(truncated,radius,sp.oo) != sp.oo:
        raise AssertionError("infinite second moment")
    checks += 2

    n = 4*r**2/(lam**2+r**2)
    radial_rhs = sp.diff(n,r,2)-sp.diff(n,r)/r+n*sp.diff(n,r)/r
    zero(radial_rhs, "critical radial stationary equation")
    zero(sp.diff(n,r)-r*rho, "normalized cumulative derivative")
    checks += 2

    slope = 4*mass*(1-mass/(8*sp.pi))
    zero(slope.subs(mass,8*sp.pi*q)-32*sp.pi*q*(1-q), "virial scaling")
    bound = 2*sp.pi*moment/(mass*(mass-8*sp.pi))
    zero((sp.pi*bound).subs(mass,8*sp.pi*q)-moment/(32*q*(q-1)),
         "supercritical bound")
    checks += 2

    energy_shift = 2*mass*(1-mass/(8*sp.pi))*sp.log(scale)
    zero(energy_shift.subs(mass,8*sp.pi*q)
         -16*sp.pi*q*(1-q)*sp.log(scale), "energy scaling")
    zero(energy_shift.subs(mass,8*sp.pi), "critical scale invariance")
    checks += 2

    x1,x2,y1,y2 = sp.symbols("x1 x2 y1 y2", real=True)
    dx,dy = x1-y1,x2-y2
    squared = dx**2+dy**2
    sym_virial = x1*dx+x2*dy+y1*(-dx)+y2*(-dy)
    zero(sym_virial-squared, "pairwise virial symmetrization")
    zero(dx/squared+(-dx)/squared, "barycenter x cancellation")
    zero(dy/squared+(-dy)/squared, "barycenter y cancellation")
    checks += 3

    # Two-dimensional diffusion integrations by parts.
    dimension = sp.Integer(2)
    zero(2*dimension*mass-4*mass, "Laplacian second moment")
    zero(2*mass*(1-mass/(8*sp.pi))
         -(2*mass-mass**2/(4*sp.pi)), "free-energy scale coefficient")
    checks += 2
    print(f"C363 SymPy cross-check: PASS {checks} exact identities")


if __name__ == "__main__":
    main()
