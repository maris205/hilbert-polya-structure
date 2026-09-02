#!/usr/bin/env python3
"""Independent symbolic checks for the C291 PGF and moment theorem."""
from __future__ import annotations

import sympy as sp

x, z = sp.symbols("x z")
checks = 0


def claim(expr) -> None:
    global checks
    assert sp.simplify(expr) == 0
    checks += 1


def main() -> None:
    global checks
    H0 = 1 / (1 - x)
    claim(sp.diff(H0, x) - (H0 - 1) / x - x * H0**2)

    H1 = x * (1 - sp.exp(-2*x)) / (2 * (1-x)**2)
    claim(sp.diff(H1, x) - H1/x - 2*x*H0*H1 - x*H0**2)

    H2 = x * (4*x**2*sp.exp(2*x) - 3*x*sp.exp(4*x) - x + sp.exp(4*x) - 1) * sp.exp(-4*x) / (4*(x-1)**3)
    claim(sp.limit(H2, x, 0))
    claim(sp.diff(H2, x) - H2/x - 2*x*H0*H2 - 4*x*H0*H1 - 2*x*H1**2)

    a = sp.symbols("a")
    alpha = (1-a)/2
    c3 = (1-a)**2/2
    c2 = -sp.Rational(5, 4) + a + sp.Rational(5, 4)*a**2
    c1 = sp.Rational(3, 4) + a + sp.Rational(5, 4)*a**2
    f2_linear = sp.Rational(3, 2)*c3 + c2
    claim(c3/2 - alpha**2)
    claim(f2_linear + alpha + 2*alpha*a - a**2)
    claim(c3 + c2 + c1 - a - a**2 - 2*a**2)

    # Coefficient-level recurrence and the closed mean agree symbolically for
    # a nontrivial finite window; this is a cross-check, not the all-n proof.
    polys = [[sp.Integer(1)], [sp.Integer(1)]]
    for n in range(2, 13):
        row = [sp.Integer(0)] * (n//2 + 1)
        for left in range(n-1):
            right = n-2-left
            for i, p in enumerate(polys[left]):
                for j, q in enumerate(polys[right]):
                    row[i+j+1] += p*q/sp.Integer(n-1)
        while row[-1] == 0:
            row.pop()
        polys.append([sp.factor(value) for value in row])
        claim(sum(row)-1)
        mean = sum(k*value for k, value in enumerate(row))
        closed = sum(sp.Rational((n-j)*(-1)**(j+1)*2**(j-1), sp.factorial(j)) for j in range(1,n))
        claim(mean-closed)
        for value in row:
            assert value >= 0
            checks += 1

    # The path/cycle support endpoints match the exact shifted identity.
    for n in range(3, 31):
        assert 1 + (n-1)//3 == (n+2)//3
        assert 1 + (n-2)//2 == n//2
        checks += 2

    print(f"C291_SYMPY_PASS ({checks} symbolic checks; Riccati, H1, H2, pole algebra, supports)")


if __name__ == "__main__":
    main()
