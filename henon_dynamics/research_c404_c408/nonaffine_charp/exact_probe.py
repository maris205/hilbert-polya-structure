"""Small exact scout checks, not a proof of all-period claims.

Markov counts are quotient lengths of the literal Frobenius-twist fixed
equations, independently of the proposed quadratic-character count formula.
The script reads no historical outputs and writes no files.
"""
import itertools
import json
import platform
import sympy as s

x, y, z = s.symbols("x y z")


def quotient_dimension(polys, p):
    gb = s.groebner(polys, x, y, z, modulus=p, order="grevlex")
    leads = [tuple(g.LM(order=gb.order).exponents) for g in gb.polys]
    if (0, 0, 0) in leads:
        return 0, len(leads)
    bounds = []
    for j in range(3):
        pure = [e[j] for e in leads if e[j] and all(e[k] == 0 for k in range(3) if k != j)]
        assert pure, (p, j, leads)
        bounds.append(min(pure))
    dim = sum(not any(all(e[j] >= a[j] for j in range(3)) for a in leads)
              for e in itertools.product(*(range(b) for b in bounds)))
    return dim, len(leads)


def character(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)


def markov_case(p, kappa, k, n):
    qn = p ** n
    u, v = x, y
    for _ in range(k * n):
        u, v = v, s.expand(z * v - u)
    fx = u.subs({x: x ** qn, y: y ** qn}, simultaneous=True) - x
    fy = v.subs({x: x ** qn, y: y ** qn}, simultaneous=True) - y
    polys = [fx, fy, z ** qn - z, x*x + y*y + z*z - x*y*z - kappa]
    actual, size = quotient_dimension(polys, p)
    eps, eta = character(kappa - 4, p), character(kappa, p)
    expected = qn*qn + 1 + 2*(p*eps)**n + (p*((-1)**k)*eps)**n + (p*eps*eta)**n
    assert actual == expected, (p, kappa, k, n, actual, expected)
    return dict(p=p, kappa=kappa, twist_power=k, period=n,
                quotient_length=actual, proposed_formula=expected,
                groebner_basis_size=size)


def witt_check():
    u, v = x, y
    rows = []
    for n in range(1, 10):
        u, v = s.Poly(u + 1, x, y, modulus=3).as_expr(), s.Poly(v - u*u - u, x, y, modulus=3).as_expr()
        if n in (1, 3, 9):
            rows.append(dict(n=n, first=str(u), second=str(v)))
    assert s.Poly(u-x, x, y, modulus=3).is_zero
    assert s.Poly(v-y, x, y, modulus=3).is_zero
    assert rows[1]["first"] == "x" and rows[1]["second"] == "y + 1"
    return rows


if __name__ == "__main__":
    cases = [(3, 2, 1, 1), (3, 2, 2, 1), (3, 2, 1, 2),
             (5, 1, 1, 1), (5, 1, 2, 1), (5, 2, 1, 1),
             (7, 1, 1, 1), (7, 2, 1, 1), (7, 3, 2, 1)]
    output = dict(scope="FINITE_SCOUT_CHECKS_NOT_ALL_PERIOD_PROOF",
                  environment=dict(python=platform.python_version(), sympy=s.__version__),
                  markov=[markov_case(*case) for case in cases],
                  witt_characteristic_three=witt_check())
    print(json.dumps(output, indent=2, sort_keys=True))
