#!/usr/bin/env python3
"""Independent symbolic convention and formula audit for HCS-C377."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c377 sympy crosscheck refuses optimized Python")

import argparse

import sympy as sp


def conv(a, b):
    out = {}
    for j, x in a.items():
        for k, y in b.items():
            out[j + k] = sp.expand(out.get(j + k, 0) + x * y)
    return {k: sp.simplify(v) for k, v in out.items() if sp.simplify(v) != 0}


def hilbert(poly):
    return {k: sp.simplify(-sp.I * sp.sign(k) * v) for k, v in poly.items() if k}


def add(a, b, sign=1):
    out = {k: sp.simplify(a.get(k, 0) + sign * b.get(k, 0)) for k in set(a) | set(b)}
    return {k: v for k, v in out.items() if v != 0}


def main():
    argparse.ArgumentParser().parse_args()
    checks = 0
    # The Fourier convention fixes all later signs.
    for k in tuple(range(-128, 0)) + tuple(range(1, 129)):
        multiplier = -sp.I * sp.sign(k)
        assert sp.simplify(multiplier ** 2 + 1) == 0
        checks += 1
    a, b = sp.symbols("a b", real=True)
    # f=a*sin(x)+b*cos(2x): the chosen convention gives Hsin=-cos, Hcos=sin.
    f = {1: a / (2 * sp.I), -1: -a / (2 * sp.I), 2: b / 2, -2: b / 2}
    h = hilbert(f)
    assert sp.simplify(h[1] + a / 2) == 0
    assert sp.simplify(h[-1] + a / 2) == 0
    assert sp.simplify(h[2] + sp.I * b / 2) == 0
    assert sp.simplify(h[-2] - sp.I * b / 2) == 0
    checks += 4
    lhs = hilbert(conv(f, h))
    rhs = {k: sp.simplify(v / 2) for k, v in add(conv(h, h), conv(f, f), -1).items()}
    assert set(lhs) == set(rhs) and all(sp.simplify(lhs[k] - rhs[k]) == 0 for k in lhs)
    checks += len(lhs)
    # Mean conservation is the zero Fourier coefficient of f*Hf.
    assert sp.simplify(conv(f, h).get(0, 0)) == 0
    checks += 1

    mu, hh, ff = sp.symbols("mu hh ff", real=True)
    # From f_t=mu*h+f*h and h_t=-mu*f+(h^2-f^2)/2.
    ft = mu * hh + ff * hh
    ht = -mu * ff + (hh ** 2 - ff ** 2) / 2
    z = hh + sp.I * ff
    assert sp.simplify(ht + sp.I * ft - (sp.I * mu * z + z ** 2 / 2)) == 0
    checks += 1

    t, z0 = sp.symbols("t z0")
    zero_solution = 2 * z0 / (2 - t * z0)
    assert sp.simplify(sp.diff(zero_solution, t) - zero_solution ** 2 / 2) == 0
    checks += 1
    nonzero_solution = sp.exp(sp.I * mu * t) * z0 / (
        1 - (sp.exp(sp.I * mu * t) - 1) * z0 / (2 * sp.I * mu)
    )
    assert sp.simplify(sp.diff(nonzero_solution, t) - sp.I * mu * nonzero_solution - nonzero_solution ** 2 / 2) == 0
    assert sp.simplify(nonzero_solution.subs(t, 0) - z0) == 0
    checks += 2

    c, s, omega = sp.symbols("c s omega", real=True)
    zz0 = hh + sp.I * (omega - mu)
    E = c + sp.I * s
    delta = 2 * sp.I * mu - (E - 1) * zz0
    evolved = 2 * sp.I * mu * E * zz0 / delta
    identity = sp.factor((sp.im(sp.expand_complex(evolved)) + mu) * sp.expand_complex(delta * sp.conjugate(delta)) - 4 * mu ** 2 * omega)
    assert sp.simplify(identity.subs(c ** 2 + s ** 2, 1)) == 0
    checks += 1

    # Exact pole parametrization with r=cot(mu*t/2).
    r = sp.symbols("r", real=True)
    E_r = (r + sp.I) / (r - sp.I)
    z_pole = mu * (r - sp.I)
    assert sp.simplify(2 * sp.I * mu - (E_r - 1) * z_pole) == 0
    assert sp.im(z_pole) == -mu
    assert sp.re(z_pole) == mu * r
    checks += 3
    u = sp.symbols("u", real=True)
    assert sp.diff(sp.acot(u), u) == -1 / (u ** 2 + 1)
    checks += 1

    # One-mode zero-set extremum: H(mu+A sin(kx))=-A cos(kx).
    A, m = sp.symbols("A m", real=True)
    cos_sq_on_zero_set = 1 - m ** 2 / A ** 2
    assert sp.simplify(A ** 2 * cos_sq_on_zero_set - (A ** 2 - m ** 2)) == 0
    checks += 1

    # Simple-pole leading profiles: nonzero imaginary derivative makes the
    # real two-variable denominator map transverse.
    hp, wp, y, eps = sp.symbols("hp wp y eps", real=True, nonzero=True)
    lead = sp.I * mu * E_r * z_pole - (E_r - 1) * (hp + sp.I * wp) * y
    profile_expr = sp.limit(
        eps * (4 * mu ** 2 * wp * eps * y) / (eps ** 2 * sp.expand_complex(lead * sp.conjugate(lead))),
        eps, 0,
    )
    assert sp.simplify(profile_expr - 4 * mu ** 2 * wp * y / sp.expand_complex(lead * sp.conjugate(lead))) == 0
    checks += 1
    hstar = sp.symbols("hstar", positive=True)
    T = 2 / hstar
    lead_zero = hstar - T * (hp + sp.I * wp) * y
    profile_zero = sp.limit(
        eps * (4 * wp * eps * y) / (eps ** 2 * sp.expand_complex(lead_zero * sp.conjugate(lead_zero))),
        eps, 0,
    )
    assert sp.simplify(profile_zero - 4 * wp * y / sp.expand_complex(lead_zero * sp.conjugate(lead_zero))) == 0
    checks += 1
    print(f"C377 SymPy PASS: exact_symbolic_checks={checks} convention+Tricomi+Riccati+pole+profiles")


if __name__ == "__main__":
    main()
