#!/usr/bin/env python3
"""Independent symbolic identities for the HCS-C360 theorem contract."""
from __future__ import annotations

import sys

import sympy as sp


def zero(expr, label):
    if sp.factor(sp.together(expr)) != 0:
        raise AssertionError(label)


def main():
    if sys.flags.optimize:
        raise RuntimeError("C360 SymPy lane refuses optimized Python")
    A, C, k, u, v, tau = sp.symbols("A C k u v tau", positive=True)
    r = C/A
    Ad = -8+4*r
    Cd = -4*r**2
    rd = sp.diff(r, A)*Ad+sp.diff(r, C)*Cd
    checks = 0
    zero(rd-8*r*(1-r)/A, "ratio equation")
    checks += 1

    ric_h = 4/A-2*C/A**2
    ric_v = 2*C/A**2
    kh = (4*A-3*C)/A**2
    km = C/A**2
    scalar = (8*A-2*C)/A**2
    zero(scalar-2*(kh+2*km), "scalar from sectional curvature")
    zero(scalar-(2*ric_h+ric_v), "scalar from Ricci")
    zero(Ad/A+Cd/(2*C)+scalar, "volume evolution")
    checks += 3

    jminus = C**2/(1-r)
    jplus = C**2/(r-1)
    zero(sp.diff(jminus,A)*Ad+sp.diff(jminus,C)*Cd, "squashed first integral")
    zero(sp.diff(jplus,A)*Ad+sp.diff(jplus,C)*Cd, "stretched first integral")
    checks += 2

    primitive_minus = u/(1-u**2)+sp.atanh(u)
    primitive_plus = v/(1+v**2)+sp.atan(v)
    zero(sp.diff(primitive_minus,u)-2/(1-u**2)**2, "atanh primitive")
    zero(sp.diff(primitive_plus,v)-2/(1+v**2)**2, "atan primitive")
    checks += 2

    rminus = 1-u**2
    Aminus = k*u/rminus
    Cminus = k*u
    ud = -4*(1-u**2)**2/k
    zero(sp.diff(Aminus,u)*ud-(-8+4*rminus), "squashed A chart")
    zero(sp.diff(Cminus,u)*ud+4*rminus**2, "squashed C chart")
    zero(sp.diff(rminus,u)*ud-8*rminus*(1-rminus)/Aminus, "squashed ratio chart")
    checks += 3

    rplus = 1+v**2
    Aplus = k*v/rplus
    Cplus = k*v
    vd = -4*(1+v**2)**2/k
    zero(sp.diff(Aplus,v)*vd-(-8+4*rplus), "stretched A chart")
    zero(sp.diff(Cplus,v)*vd+4*rplus**2, "stretched C chart")
    zero(sp.diff(rplus,v)*vd-8*rplus*(1-rplus)/Aplus, "stretched ratio chart")
    checks += 3

    And = sp.Rational(8,3)*(r-1)
    Cnd = sp.Rational(16,3)*r*(1-r)
    rnd = sp.diff(r,A)*And+sp.diff(r,C)*Cnd
    zero(rnd-8*r*(1-r)/A, "normalized ratio")
    zero(2*A*And*C+A**2*Cnd, "normalized volume")
    volume_scale = (A**2*C)**sp.Rational(1,3)
    zero(A-volume_scale*r**(-sp.Rational(1,3)), "fixed-volume chart")
    checks += 3

    A0, t = sp.symbols("A0 t", positive=True)
    round_solution = A0-4*t
    zero(sp.diff(round_solution,t)-(-8+4), "round A equation")
    zero(sp.diff(round_solution,t)-(-4), "round C equation")
    checks += 2
    zero(kh.subs(C,sp.Rational(4,3)*A), "sectional sign wall")
    zero(ric_h.subs(C,2*A), "horizontal Ricci sign wall")
    zero(scalar.subs(C,4*A), "scalar sign wall")
    checks += 3

    remaining_minus = k*primitive_minus/8
    remaining_plus = k*primitive_plus/8
    scalar_minus = scalar.subs({A:Aminus,C:Cminus})
    scalar_plus = scalar.subs({A:Aplus,C:Cplus})
    mixed_minus = km.subs({A:Aminus,C:Cminus})
    mixed_plus = km.subs({A:Aplus,C:Cplus})
    zero(sp.limit(remaining_minus*scalar_minus,u,0)-sp.Rational(3,2),
         "squashed scalar blow-up coefficient")
    zero(sp.limit(remaining_plus*scalar_plus,v,0)-sp.Rational(3,2),
         "stretched scalar blow-up coefficient")
    zero(sp.limit(remaining_minus*mixed_minus,u,0)-sp.Rational(1,4),
         "squashed mixed-curvature blow-up coefficient")
    zero(sp.limit(remaining_plus*mixed_plus,v,0)-sp.Rational(1,4),
         "stretched mixed-curvature blow-up coefficient")
    checks += 4
    print(f"C360 SymPy cross-check: PASS {checks} exact identities")


if __name__ == "__main__":
    main()
