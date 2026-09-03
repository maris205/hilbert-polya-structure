#!/usr/bin/env python3
"""Exact symbolic cross-checks for HCS-C319."""
import sys
import sympy as s

if sys.flags.optimize:
    raise RuntimeError("C319 SymPy lane refuses optimized Python")
p, q, y, z = s.symbols("p q y z", positive=True)
n = p + q
yp = 2 * (n * y - q)
H = (n * y - q) / s.sqrt(y * (1 - y))
logA_y = q / (2 * y) - p / (2 * (1 - y))
checks = [
    s.simplify(logA_y * yp + H**2),
    s.simplify((p * y / (1-y) + q * (1-y) / y).subs(y, q/n) - n),
    s.simplify(q / p * p + p / q * q - n),
    s.simplify((q / n + z * s.exp(2*n*s.symbols("t"))).diff(s.symbols("t")) - 2*(n*(q/n + z*s.exp(2*n*s.symbols("t")))-q)),
]
if any(s.factor(v) != 0 for v in checks):
    raise AssertionError(checks)
count = len(checks)
for P in range(1, 21):
    for Q in range(1, 21):
        N = P + Q
        star = s.Rational(Q, N)
        if s.simplify(H.subs({p:P,q:Q,y:star})) != 0:
            raise AssertionError("minimal H")
        left = s.Rational(Q, Q-N*(star/2))
        right_y = star + (1-star)/2
        right = s.Rational(P, N*right_y-Q)
        if left <= 1 or right <= 1:
            raise AssertionError("positive lifespan")
        count += 3
print(f"C319 SymPy cross-check: PASS ({count} exact identities)")
