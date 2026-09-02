#!/usr/bin/env python3
"""Independent symbolic lane for the C308 Hatano--Nelson identities."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("C308 SymPy lane requires assertions; python -O is forbidden")

import sympy as sp


def path_matrix(n, upper, lower):
    matrix = sp.zeros(n)
    for j in range(n - 1):
        matrix[j, j + 1] = upper
        matrix[j + 1, j] = lower
    return matrix


def cyclic_matrix(n, upper, lower):
    matrix = sp.zeros(n)
    for j in range(n):
        matrix[j, (j + 1) % n] += upper
        matrix[j, (j - 1) % n] += lower
    return matrix


def main() -> None:
    z, a, b, g, q = sp.symbols("z a b g q", nonzero=True)
    checks = 0

    def need(condition):
        nonlocal checks
        assert bool(condition)
        checks += 1

    p0, p1 = sp.Integer(1), z
    for n in range(2, 10):
        pn = sp.expand(z * p1 - a * b * p0)
        direct = sp.expand((z * sp.eye(n) - path_matrix(n, a, b)).det())
        need(sp.expand(pn - direct) == 0)
        cheb = sp.expand((a * b) ** sp.Rational(n, 2) * sp.chebyshevu(n, z / (2 * sp.sqrt(a * b))))
        need(sp.simplify(pn - cheb) == 0)
        p0, p1 = p1, pn

    for n in range(2, 9):
        h = path_matrix(n, g / q, g * q)
        d = sp.diag(*[q ** j for j in range(n)])
        core = path_matrix(n, g, g)
        need(sp.simplify(d.inv() * h * d - core) == sp.zeros(n))
        need(sp.simplify(h - d * core * d.inv()) == sp.zeros(n))
        zz = sp.Integer(3 * n + 1)
        need(sp.simplify((zz * sp.eye(n) - h).inv() - d * (zz * sp.eye(n) - core).inv() * d.inv()) == sp.zeros(n))

    for n in range(2, 8):
        s = sp.Matrix(n, n, lambda j, m: sp.sqrt(sp.Rational(2, n + 1)) * sp.sin((j + 1) * (m + 1) * sp.pi / (n + 1)))
        need((s.T * s).equals(sp.eye(n)))
        d = sp.diag(*[sp.Rational(2) ** j for j in range(n)])
        r, lt = d * s, s.T * d.inv()
        need((lt * r).equals(sp.eye(n)))
        for m in range(n):
            for j in range(n):
                need(sp.simplify(sp.trigsimp(lt[m, j] * r[j, m] - s[j, m] ** 2)) == 0)

    for n in range(3, 9):
        c = cyclic_matrix(n, sp.Integer(4), sp.Integer(1))
        need(c * c.T == c.T * c)
        one = cyclic_matrix(n, sp.Integer(2), sp.Integer(0))
        need(one ** n == (sp.Integer(2) ** n) * sp.eye(n))
        need(one.det() != 0)
        obc = path_matrix(n, sp.Integer(2), sp.Integer(0))
        need(obc ** n == sp.zeros(n))
        need(obc ** (n - 1) != sp.zeros(n))
        for power in range(n + 1):
            need((obc ** power).rank() == n - power)

    k, tr, tl = sp.symbols("k t_R t_L", real=True)
    energy = tr * sp.exp(sp.I * k) + tl * sp.exp(-sp.I * k)
    need(sp.simplify(sp.re(energy) - (tr + tl) * sp.cos(k)) == 0)
    need(sp.simplify(sp.im(energy) - (tr - tl) * sp.sin(k)) == 0)
    print(f"C308 independent SymPy lane: PASS ({checks} exact symbolic checks)")


if __name__ == "__main__":
    main()
