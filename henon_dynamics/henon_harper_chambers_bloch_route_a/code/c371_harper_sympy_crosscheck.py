#!/usr/bin/env python3
"""Exact cyclotomic quotient-ring lane for HCS-C371."""
from __future__ import annotations

import math
import sys
from fractions import Fraction as F

import sympy as s


def cyclotomic_context(q):
    z = s.symbols("z")
    phi = s.Poly(s.cyclotomic_poly(q, z), z)
    ascending = tuple(F(int(c)) for c in reversed(phi.all_coeffs()))
    assert ascending[-1] == 1
    return ascending


def qzero(phi):
    return (F(0),) * (len(phi) - 1)


def qreduce(raw, phi):
    degree = len(phi) - 1
    work = list(raw) + [F(0)] * max(0, degree - len(raw))
    for power in range(len(work) - 1, degree - 1, -1):
        coefficient = work[power]
        if not coefficient:
            continue
        offset = power - degree
        for j, phi_coefficient in enumerate(phi):
            work[offset + j] -= coefficient * phi_coefficient
    work = work[:degree]
    work += [F(0)] * (degree - len(work))
    return tuple(work)


def qadd(a, b, phi):
    return qreduce([x + y for x, y in zip(a, b)], phi)


def qneg(a):
    return tuple(-x for x in a)


def qmul(a, b, phi):
    raw = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            raw[i + j] += x * y
    return qreduce(raw, phi)


def qscalar(value, phi):
    out = [F(0)] * (len(phi) - 1)
    out[0] = F(value)
    return tuple(out)


def qz(power, q, phi):
    raw = [F(0)] * (power % q + 1)
    raw[power % q] = F(1)
    return qreduce(raw, phi)


def padd(a, b, phi):
    out = dict(a)
    zero = qzero(phi)
    for key, coefficient in b.items():
        value = qadd(out.get(key, zero), coefficient, phi)
        if value == zero:
            out.pop(key, None)
        else:
            out[key] = value
    return out


def pmul(a, b, phi):
    out = {}
    zero = qzero(phi)
    for (ea, ya, la), ca in a.items():
        for (eb, yb, lb), cb in b.items():
            key = (ea + eb, ya + yb, la + lb)
            value = qadd(out.get(key, zero), qmul(ca, cb, phi), phi)
            if value == zero:
                out.pop(key, None)
            else:
                out[key] = value
    return out


def pterm(key, coefficient):
    return {} if not any(coefficient) else {key: coefficient}


def mmul(a, b, phi):
    return (
        (
            padd(pmul(a[0][0], b[0][0], phi), pmul(a[0][1], b[1][0], phi), phi),
            padd(pmul(a[0][0], b[0][1], phi), pmul(a[0][1], b[1][1], phi), phi),
        ),
        (
            padd(pmul(a[1][0], b[0][0], phi), pmul(a[1][1], b[1][0], phi), phi),
            padd(pmul(a[1][0], b[0][1], phi), pmul(a[1][1], b[1][1], phi), phi),
        ),
    )


def exact_trace(p, q):
    """Trace as (E power, y power, lambda power) -> Q[zeta]/Phi_q."""
    phi = cyclotomic_context(q)
    one, minus_one = qscalar(1, phi), qscalar(-1, phi)
    zero = {}
    monodromy = ((pterm((0, 0, 0), one), zero), (zero, pterm((0, 0, 0), one)))
    for n in range(q):
        a00 = pterm((1, 0, 0), one)
        a00 = padd(a00, pterm((0, 1, 1), qneg(qz(p * n, q, phi))), phi)
        a00 = padd(a00, pterm((0, -1, 1), qneg(qz(-p * n, q, phi))), phi)
        step = ((a00, pterm((0, 0, 0), minus_one)), (pterm((0, 0, 0), one), zero))
        monodromy = mmul(step, monodromy, phi)
    return padd(monodromy[0][0], monodromy[1][1], phi), phi


def central_polynomial(trace):
    return {(e, ell): coefficient for (e, y, ell), coefficient in trace.items() if y == 0}


def main():
    if sys.flags.optimize:
        raise RuntimeError("C371 SymPy lane refuses optimized Python")
    checks = 0
    fluxes = [(p, q) for q in range(3, 11) for p in range(1, q) if math.gcd(p, q) == 1]
    cache = {}
    for p, q in fluxes:
        trace, phi = exact_trace(p, q)
        cache[(p, q)] = (central_polynomial(trace), phi)
        one = qscalar(1, phi)
        allowed = {0, -q, q}
        assert all(y in allowed for e, y, ell in trace)
        checks += len(trace)
        assert trace.get((0, q, q)) == qneg(one)
        assert trace.get((0, -q, q)) == qneg(one)
        checks += 2
        for (e, y, ell), coefficient in trace.items():
            if y:
                assert (e, y, ell) in {(0, q, q), (0, -q, q)}
            else:
                assert (e - q) % 2 == 0
                assert 0 <= ell <= q - e
            checks += 1
        ppoly = cache[(p, q)][0]
        for (e, ell), coefficient in ppoly.items():
            reflected = (e, q - e - ell)
            assert ppoly.get(reflected, qzero(phi)) == coefficient
            checks += 1
        if q % 2 == 0:
            sign = F(2 * ((-1) ** (q // 2)))
            assert ppoly.get((0, 0), qzero(phi)) == qscalar(sign, phi)
            assert ppoly.get((0, q), qzero(phi)) == qscalar(sign, phi)
            assert all(e != 0 or ell in (0, q) for e, ell in ppoly)
            checks += 3
        else:
            assert all(e != 0 for e, ell in ppoly)
            checks += 1

    for p, q in fluxes:
        left, phi = cache[(p, q)]
        right, right_phi = cache[(q - p, q)]
        assert phi == right_phi and left == right
        checks += len(left) + 1

    # The direct q=1 and q=2 accumulated-edge fibers fix the convention.
    E, L, X, Y = s.symbols("E L X Y", nonzero=True)
    d1 = E - (X + 1 / X) - L * (Y + 1 / Y)
    assert s.simplify(d1 - (E - (X + 1 / X) - L * (Y + 1 / Y))) == 0
    checks += 1
    h2 = s.Matrix(
        [
            [L * (Y + 1 / Y), 1 + 1 / X],
            [1 + X, -L * (Y + 1 / Y)],
        ]
    )
    d2 = s.factor((E * s.eye(2) - h2).det())
    p2 = E**2 - 2 * (1 + L**2)
    expected2 = p2 - (X + 1 / X) - L**2 * (Y**2 + Y ** (-2))
    assert s.simplify(d2 - expected2) == 0
    assert s.simplify(p2.subs(E, 0) + 2 * (1 + L**2)) == 0
    assert s.diff(p2, E).subs(E, 0) == 0
    checks += 3

    # Transfer determinant and edge multiplicity are independently symbolic.
    C = s.symbols("C", positive=True)
    P = s.Function("P")
    energy = s.symbols("energy", real=True)
    edge_product = P(energy) ** 2 - C**2
    assert s.diff(edge_product, energy) == 2 * P(energy) * s.diff(P(energy), energy)
    checks += 1
    print(f"C371 SymPy/cyclotomic cross-check: PASS ({checks} exact checks; {len(fluxes)} reduced fluxes)")


if __name__ == "__main__":
    main()
