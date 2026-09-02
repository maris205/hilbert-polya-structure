#!/usr/bin/env python3
"""Independent SymPy identities for HCS-C285."""
import math
import sympy as sp

w1, w2, w3, z = sp.symbols("w1 w2 w3 z", positive=True)
weights = (w1, w2, w3)
checks = 0


def verify(expression) -> None:
    global checks
    assert sp.simplify(expression) == 0
    checks += 1


def compositions(n, m):
    if m == 1:
        yield (n,)
    else:
        for k in range(n + 1):
            for tail in compositions(n - k, m - 1):
                yield (k,) + tail


h = []
series = sp.series(sp.prod(1 / (1 - weight * z) for weight in weights), z, 0, 6).removeO().expand()
for n in range(5):
    direct = sum(sp.prod(weights[i] ** state[i] for i in range(3)) for state in compositions(n, 3))
    coefficient = series.coeff(z, n)
    verify(coefficient - direct)
    h.append(sp.expand(direct))

for n in range(1, 5):
    newton = sum(sum(weight ** k for weight in weights) * h[n - k] for k in range(1, n + 1))
    verify(n * h[n] - newton)

for n in range(1, 5):
    euler = sum(weight * sp.diff(h[n], weight) for weight in weights)
    verify(euler - n * h[n])

log_h3 = sp.log(h[3])
for variable in weights:
    covariance_row_sum = variable * sp.diff(
        sum(weight * sp.diff(log_h3, weight) for weight in weights), variable
    )
    verify(covariance_row_sum)

# A symbolic two-station global-balance calculation, including self routes.
a, b, mu1, mu2 = sp.symbols("a b mu1 mu2", positive=True)
e1, e2 = b / (a + b), a / (a + b)
x1, x2 = e1 / mu1, e2 / mu2
states = ((0, 2), (1, 1), (2, 0))
q = sp.Matrix([
    [-2 * 0 + -mu2 * b, mu2 * b, 0],
    [mu1 * a, -(mu1 * a + mu2 * b), mu2 * b],
    [0, mu1 * a, -mu1 * a],
])
raw = sp.Matrix([[x2 ** 2, x1 * x2, x1 ** 2]])
balance = sp.simplify(raw * q)
for entry in balance:
    verify(entry)

# Exact nonreversible three-state time reversal is stochastic and involutive.
p = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2), 0],
               [0, sp.Rational(1, 3), sp.Rational(2, 3)],
               [sp.Rational(3, 4), 0, sp.Rational(1, 4)]])
e_symbols = sp.symbols("e0:3")
solution = sp.solve(list((sp.Matrix(1, 3, e_symbols) * p - sp.Matrix(1, 3, e_symbols)))[:2]
                    + [sum(e_symbols) - 1], e_symbols, dict=True)[0]
e = sp.Matrix([solution[value] for value in e_symbols])
pstar = sp.Matrix(3, 3, lambda i, j: sp.simplify(e[j] * p[j, i] / e[i]))
for i in range(3):
    verify(sum(pstar[i, j] for j in range(3)) - 1)
twice = sp.Matrix(3, 3, lambda i, j: sp.simplify(e[j] * pstar[j, i] / e[i]))
verify(sum((twice[i, j] - p[i, j]) ** 2 for i in range(3) for j in range(3)))
assert any(sp.simplify(e[i] * p[i, j] - e[j] * p[j, i]) != 0 for i in range(3) for j in range(3))
checks += 1

# Uniform weak compositions have the exact count and Dirichlet limiting moments.
for n in range(4):
    equal_h = sum(1 for _ in compositions(n, 3))
    verify(equal_h - math.comb(n + 2, 2))

assert checks == 28
print(f"C285_SYMPY_PASS ({checks} symbolic identities)")
