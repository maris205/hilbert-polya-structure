#!/usr/bin/env python3
"""Independent exact symbolic reconstruction of the C256 root atlas."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c256_kdv_evidence.json"


def main() -> None:
    u, r1, r2, r3, q, xi, a = sp.symbols("u r1 r2 r3 q xi a", real=True)
    checks = 0

    def ck(expr, label: str) -> None:
        nonlocal checks
        checks += 1
        out = sp.factor(sp.simplify(expr))
        if out != 0:
            raise AssertionError(f"{label}: {out}")

    P = sp.expand(2*(r3-u)*(u-r2)*(u-r1))
    c = 2*(r1+r2+r3)
    pair = r1*r2+r1*r3+r2*r3
    ck(sp.Poly(P, u).coeff_monomial(u**3)+2, "leading cubic")
    ck(sp.Poly(P, u).coeff_monomial(u**2)-c, "speed coefficient")
    ck(sp.Poly(P, u).coeff_monomial(u)+2*pair, "linear coefficient")
    ck(sp.Poly(P, u).coeff_monomial(1)-2*r1*r2*r3, "constant coefficient")
    ck(sp.diff(P, u)/2-(c*u-3*u**2-pair), "energy derivative profile ODE")
    for rr in (r1, r2, r3):
        ck(P.subs(u, rr), "root vanishing")

    D = r3-r1
    d = r3-r2
    mod = d/D
    k2 = D/2
    U = r2+d*q
    qprime2 = 4*q*(1-q)*(1-mod+mod*q)
    ck(d**2*k2*qprime2-P.subs(u, U), "cn-square first integral")
    fprime = sp.diff(qprime2, q)
    Upp = d*k2*fprime/2
    ck(Upp-(c*U-3*U**2-pair), "cn-square profile ODE")
    ck(mod*D-d, "modulus relation")
    ck(U.subs(q, 0)-r2, "lower turning point")
    ck(U.subs(q, 1)-r3, "upper turning point")

    # Lower-double-root soliton using s=sech^2(k xi) algebra only.
    s = sp.symbols("s", nonnegative=True)
    Us = r1+D*s
    sprime2 = 4*k2*s**2*(1-s)
    Psol = 2*(r3-Us)*(Us-r1)**2
    ck(D**2*sprime2-Psol, "soliton first integral")
    fps = sp.diff(sprime2, s)
    csol = 2*(2*r1+r3)
    pairsol = r1**2+2*r1*r3
    ck(D*fps/2-(csol*Us-3*Us**2-pairsol), "soliton profile ODE")

    # Galilean covariance for the plus-sign convention.
    ut, ux, uxxx = sp.symbols("u_t u_x u_xxx")
    transformed = (ut-6*a*ux)+6*(u+a)*ux+uxxx
    ck(transformed-(ut+6*u*ux+uxxx), "Galilean PDE covariance")
    ck(2*((r1+a)+(r2+a)+(r3+a))-(c+6*a), "Galilean speed")
    ck(((r3+a)-(r2+a))/((r3+a)-(r1+a))-mod, "Galilean modulus")
    ck(((r3+a)-(r1+a))-D, "Galilean scale")

    # A broad rational grid certifies signs and all coefficient conventions.
    triples = [(-5,-2,1),(-4,1,2),(-3,-1,2),(-2,0,3),(-2,3,7),(-1,0,1),(-1,1,4),(0,1,2),(0,1,3),(0,2,5),(1,2,4),(2,5,9)]
    for av, bv, cv in triples:
        sub = {r1: sp.Rational(av), r2: sp.Rational(bv), r3: sp.Rational(cv)}
        Pv = sp.factor(P.subs(sub))
        ck(Pv-2*(cv-u)*(u-bv)*(u-av), "grid factor")
        ck(c.subs(sub)-2*(av+bv+cv), "grid speed")
        ck(pair.subs(sub)-(av*bv+av*cv+bv*cv), "grid pair")
        ck(mod.subs(sub)-sp.Rational(cv-bv, cv-av), "grid modulus")
        for qv in (sp.Rational(0), sp.Rational(1,7), sp.Rational(1,4), sp.Rational(1,2), sp.Rational(2,3), sp.Rational(6,7), sp.Rational(1)):
            ck((d**2*k2*qprime2-P.subs(u,U)).subs(sub).subs(q,qv), "grid cn energy")
            ck((Upp-(c*U-3*U**2-pair)).subs(sub).subs(q,qv), "grid cn ODE")

    data = json.loads(EVIDENCE.read_text())
    formulas = {row["id"]: row["formula"] for row in data["exact_identities"]}
    expected = {
        "traveling_reduction": "-c*U'+6*U*U'+U'''=0",
        "profile_ode": "U''=c*U-3*U^2+A",
        "energy_cubic": "(U')^2=-2*U^3+c*U^2+2*A*U+B",
        "root_factor": "(U')^2=2*(r3-U)*(U-r2)*(U-r1)",
        "speed": "c=2*(r1+r2+r3)",
        "period": "L=2*sqrt(2/(r3-r1))*K(m)",
        "mean": "mean(U)=r1+(r3-r1)*E(m)/K(m)",
        "galilean": "u_a(x,t)=u(x-6*a*t,t)+a; roots->roots+a; c->c+6*a",
    }
    for key, value in expected.items():
        checks += 1
        if formulas.get(key) != value:
            raise AssertionError("evidence formula " + key)
    checks += 1
    if data["route_a"]["tuple"] != ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]:
        raise AssertionError("route tuple")
    checks += 1
    if data["route_a"]["route_b_invocation_allowed"] is not False:
        raise AssertionError("route B")
    print(f"C256_SYMPY_PASS ({checks} symbolic identities; cubic roots, cn-square reduction, soliton and Galilean faces)")


if __name__ == "__main__":
    main()
