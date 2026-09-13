"""Bounded exact checks for the original qPI four-block torus invariant.

No files are read or written, no network, no numerical fitting.  SymPy is
used only to verify finite polynomial identities whose proofs are in the
companion diagnostic.  This is not a critical-scheme classification tool.
"""

from itertools import product

import sympy as sp


x, y, t, z = sp.symbols("x y t z")
j = y - x + x / y - t / x
b = x * (y - 1)
u = t - b
r = (b - 1) * x - b
ii = sp.I
pi = ii - 1


def expand_matrix(matrix):
    return matrix.applyfunc(sp.expand)


def zero(expression):
    """All expressions checked here have monomial or explicit unit denominators."""
    return sp.expand(sp.cancel(expression)) == 0


C = sp.Matrix([[u, -x], [-(y - 1) * u, b]])
D = sp.Matrix([[j - 1, 1], [j + b - 1, 1]])
E = sp.Matrix([[1, 0], [0, 0]])
blocks = (C, D, E)
assert zero((C + z * D + z**2 * E).det() - z**3)

# Direct coefficient enumeration: degree order is k0,k1,k2,k3, while
# matrix multiplication is A(i^3 z) A(i^2 z) A(i z) A(z).
trace_coefficient = 0
count = 0
for degrees in product(range(3), repeat=4):
    if sum(degrees) != 4:
        continue
    count += 1
    matrix = sp.eye(2)
    for place in (3, 2, 1, 0):
        matrix = expand_matrix(matrix * blocks[degrees[place]])
    phase = ii ** sum(place * degrees[place] for place in range(4))
    trace_coefficient += phase * sp.trace(matrix)
trace_coefficient = sp.expand(trace_coefficient)
assert count == 19

K = (D * C - C * D)[0, 0]
assert zero(K - t - (b + 2 * x) * j - 2 * r)
assert zero((D * C * D)[0, 0] - t * j * (j - 1) - b**2)
compressed = -j**4 + 4 * (t - b) * j**2 - 4 * t * j
compressed += 4 * ii * j * K + 4 * b**2 - 2 * t**2
Q = t + pi * b + 2 * ii * x
invariant = -j**4 + 4 * Q * j**2 + 4 * pi * t * j
invariant += 8 * ii * r * j + 4 * b**2 - 2 * t**2
assert zero(trace_coefficient - compressed)
assert zero(trace_coefficient - invariant)
print("PASS: original determinant and all 19 four-block trace contributions")
print("PASS: exact compressed invariant identity")

alpha = []
for variable in (x, y):
    dj = sp.diff(j, variable)
    db = sp.diff(b, variable)
    dx = int(variable == x)
    dr = sp.diff(r, variable)
    formula = (-j**3 + 2 * Q * j + pi * t + 2 * ii * r) * dj
    formula += pi * j**2 * db + 2 * ii * j**2 * dx
    formula += 2 * ii * j * dr + 2 * b * db
    direct = sp.diff(trace_coefficient, variable) / 4
    assert zero(formula - direct)
    alpha.append(formula)
print("PASS: both state coefficients of exact alpha4 = dI4/4")

Jx, Jy = sp.diff(j, x), sp.diff(j, y)
W = Jx * x - Jy * (y - 1)
# Mod 2, W = (1 + 1/y) J + t/(xy).  Verify its difference has even
# Laurent coefficients, without relying on any finite-field solver.
frame_difference = sp.Poly(sp.expand(x * y**2 * (W - (1 + 1 / y) * j - t / (x * y))), x, y, t)
assert all(int(coefficient) % 2 == 0 for coefficient in frame_difference.coeffs())

q = j + b - 1
aa = Q * j + ii * r + ii * j * q * x / W
hh = b + ii * j * (x - 1) - ii * j * q * Jy / W
F = -j**3 + pi * t + 2 * aa
G = pi * j**2 + 2 * hh
assert zero(alpha[0] - F * Jx - G * (y - 1))
assert zero(alpha[1] - F * Jy - G * x)
assert zero(2 - ii * pi**2)
Ap = ii * (aa - j**3)
Bp = ii * hh
assert zero(F - j**3 - pi * t - pi**2 * Ap)
assert zero(G - pi * j**2 - pi**2 * Bp)
assert zero(pi * F - j * G - pi**2 * (t + pi * Ap - j * Bp))
print("PASS: actual invertible (dJ, db) frame and exact ideal-elimination identity")

for variable in (x, y):
    dj = sp.diff(j, variable)
    db = sp.diff(b, variable)
    dx = int(variable == x)
    dr = sp.diff(r, variable)
    psi0 = (t * j + r) * dj + j**2 * dx + j * dr + b * db
    psi1 = (b * j + r) * dj + j**2 * dx + j * dr
    jet4 = -j**3 * dj + pi * (t * dj + j**2 * db) + 2 * psi0 + 2 * pi * psi1
    exact = alpha[int(variable == y)]
    assert zero(exact - jet4 - 4 * ii * x * j * dj)
print("PASS: modulo pi^3/pi^4 expansions, with exact omitted term 4 i x J dJ")

special = {x: 1, y: 1, t: 1}
assert zero(alpha[0].subs(special) - ii * pi)
assert zero(alpha[1].subs(special))
print("PASS: t=1, x=y=1 has alpha4=(i*pi) dx, no common-order exception")
print("All checks are finite exact identities; the local-ring unit argument is proved in the report.")
