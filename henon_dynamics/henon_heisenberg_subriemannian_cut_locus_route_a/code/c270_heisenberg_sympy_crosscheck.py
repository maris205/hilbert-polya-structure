#!/usr/bin/env python3
"""Symbolic derivation cross-check for HCS-C270."""
from __future__ import annotations

import sympy as sp


def main() -> None:
    r, phi, lam, t, theta, rho = sp.symbols("r phi lam t theta rho", real=True, nonzero=True)
    s = lam*t
    h1 = r*sp.cos(phi+s)
    h2 = r*sp.sin(phi+s)
    x = r*(sp.sin(phi+s)-sp.sin(phi))/lam
    y = r*(sp.cos(phi)-sp.cos(phi+s))/lam
    z = r**2*(s-sp.sin(s))/(2*lam**2)
    tests = []
    tests += [sp.simplify(sp.diff(x,t)-h1) == 0, sp.simplify(sp.diff(y,t)-h2) == 0]
    tests += [sp.trigsimp(sp.diff(z,t)-(-y*h1+x*h2)/2) == 0]
    tests += [sp.trigsimp(sp.diff(h1,t)+lam*h2) == 0, sp.trigsimp(sp.diff(h2,t)-lam*h1) == 0]
    tests += [sp.trigsimp(h1**2+h2**2-r**2) == 0]
    tests += [sp.trigsimp(x**2+y**2-4*r**2*sp.sin(s/2)**2/lam**2) == 0]
    jac = sp.trigsimp(sp.det(sp.Matrix([x,y,z]).jacobian([r,phi,lam])))
    expected = r**3*t*(2-2*sp.cos(s)-s*sp.sin(s))/lam**4
    factored = 4*r**3*t*sp.sin(s/2)*(sp.sin(s/2)-(s/2)*sp.cos(s/2))/lam**4
    tests += [sp.trigsimp(jac-expected) == 0, sp.trigsimp(expected-factored) == 0]
    tests += [sp.simplify(sp.limit(expected,lam,0)-r**3*t**5/12) == 0]
    tests += [sp.simplify(expected.subs(t,2*sp.pi/lam)) == 0]
    tests += [sp.simplify(z.subs(t,2*sp.pi/lam)-sp.pi*r**2/lam**2) == 0]
    mu = (theta-sp.sin(theta)*sp.cos(theta))/sp.sin(theta)**2
    dmu = 2*(sp.sin(theta)-theta*sp.cos(theta))/sp.sin(theta)**3
    tests += [sp.trigsimp(sp.diff(mu,theta)-dmu) == 0]
    lth = 2*sp.sin(theta)/rho
    zth = (theta-sp.sin(theta)*sp.cos(theta))/lth**2
    dth = 2*theta/lth
    tests += [sp.trigsimp(4*zth/rho**2-mu) == 0, sp.trigsimp(dth-rho*theta/sp.sin(theta)) == 0]
    tests += [sp.limit(mu,theta,0) == 0, sp.limit(rho*theta/sp.sin(theta),theta,0) == rho]
    tests += [sp.series(mu,theta,0,6).removeO() == sp.Rational(2,3)*theta+sp.Rational(4,45)*theta**3+sp.Rational(4,315)*theta**5]
    # Direct bracket computation on a generic quadratic-cubic test function.
    xx, yy, zz = sp.symbols("x y z")
    f = xx**2*yy + yy**2*zz + xx*zz**2
    X = lambda g: sp.diff(g,xx)-yy*sp.diff(g,zz)/2
    Y = lambda g: sp.diff(g,yy)+xx*sp.diff(g,zz)/2
    tests += [sp.expand(X(Y(f))-Y(X(f))-sp.diff(f,zz)) == 0]
    # Positivity witnesses underlying first-root ordering on (0,2 pi).
    u = sp.symbols("u", positive=True)
    tests += [sp.series(2-2*sp.cos(u)-u*sp.sin(u),u,0,8).removeO() == u**4/sp.Integer(12)-u**6/sp.Integer(180)]
    assert all(tests), [i for i,v in enumerate(tests) if not v]
    print(f"C270_SYMPY_PASS ({len(tests)} symbolic identities; flow, bracket, Jacobian, distance limits)")


if __name__ == "__main__":
    main()
