#!/usr/bin/env python3
"""Exact symbolic lane for HCS-C328."""
import sys

import sympy as s

if sys.flags.optimize:
    raise RuntimeError("C328 SymPy lane refuses optimized Python")

y, alpha = s.symbols("y alpha", real=True, positive=True)
p = (1-y**2)**(alpha-1)
p_plus = (1+y)*p/2
p_minus = (1-y)*p/2
forward_plus = -s.diff((1-y)*p_plus, y) + alpha*(p_minus-p_plus)
forward_minus = -s.diff((-1-y)*p_minus, y) + alpha*(p_plus-p_minus)
if s.factor(forward_plus) != 0 or s.factor(forward_minus) != 0:
    raise AssertionError("stationary forward equations")
checks = 2

# Moment recurrence obtained by integrating
# d[y^(2n+1)(1-y^2)^alpha]/dy over [-1,1].
for nn in range(9):
    closed = s.rf(s.Rational(1, 2), nn) / s.rf(alpha+s.Rational(1, 2), nn)
    if nn:
        previous = s.rf(s.Rational(1, 2), nn-1) / s.rf(alpha+s.Rational(1, 2), nn-1)
        ratio = s.Rational(2*nn-1, 1)/(2*nn+2*alpha-1)
        if s.simplify(closed-previous*ratio) != 0:
            raise AssertionError("beta moment recurrence")
    elif closed != 1:
        raise AssertionError("beta normalization")
    checks += 1
    sigma_even_integrand = s.expand(y**(2*nn) * (p_plus-p_minus))
    if s.simplify(sigma_even_integrand.subs(y, -y)+sigma_even_integrand) != 0:
        raise AssertionError("mixed even moment parity")
    checks += 1

# Matrix exponential and its Jordan limit.
mu, lam, v, t = s.symbols("mu lam v t", positive=True)
cov_xx = v**2/(mu*(mu+2*lam))
cov_xs = v/(mu+2*lam)
off = v*(s.exp(-2*lam*t)-s.exp(-mu*t))/(mu-2*lam)
cxx = s.exp(-mu*t)*cov_xx + off*cov_xs
closed_cxx = v**2*(mu*s.exp(-2*lam*t)-2*lam*s.exp(-mu*t))/(mu*(mu+2*lam)*(mu-2*lam))
if s.simplify(cxx-closed_cxx) != 0:
    raise AssertionError("correlation formula")
jordan = s.simplify(s.limit(closed_cxx, lam, mu/2))
if s.simplify(jordan-v**2*(1+mu*t)*s.exp(-mu*t)/(2*mu**2)) != 0:
    raise AssertionError("Jordan correlation limit")
checks += 2


def matrix(filter_degree, mu_value, speed_value, lambda_value):
    size = 2*(filter_degree+1)
    out = s.zeros(size)
    for degree in range(filter_degree+1):
        a, b = 2*degree, 2*degree+1
        out[a, a] = -degree*mu_value
        out[b, b] = -degree*mu_value-2*lambda_value
        if degree:
            out[2*(degree-1)+1, a] = degree*speed_value
            out[2*(degree-1), b] = degree*speed_value
    return out


z = s.symbols("z")
for k in range(1, 7):
    mat = matrix(8, s.Integer(2), s.Integer(3), s.Integer(k))
    expected = s.prod(z+2*degree for degree in range(9)) * s.prod(z+2*degree+2*k for degree in range(9))
    if s.expand(mat.charpoly(z).as_expr()-expected) != 0:
        raise AssertionError("filtered characteristic polynomial")
    for degree in range(k, 9):
        eigenvalue = -2*degree
        nullity = mat.rows-(mat-eigenvalue*s.eye(mat.rows)).rank()
        if nullity != (1 if k % 2 else 2):
            raise AssertionError("odd/even resonance nullity")
        checks += 1
    checks += 1

print(f"C328 SymPy cross-check: PASS ({checks} exact identities)")
