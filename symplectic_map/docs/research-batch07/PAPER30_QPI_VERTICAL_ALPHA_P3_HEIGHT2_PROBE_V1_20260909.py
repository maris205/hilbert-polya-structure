#!/usr/bin/env python3
"""Bounded exact N=9 contraction at the first terminal chart; no I_9 expansion.

The point part is over ZZ[q,t]/Phi_9(q).  The state-jet part is over F_3
in (pi,u,v)-total degree <= 5, valid since v_pi(3)=6.  This script neither
claims a complete coefficient ideal nor extrapolates to other heights.
"""

from collections import defaultdict
from math import comb
import sympy as s


def point_contraction():
    q, t, pi = s.symbols("q t pi")
    phi = q**6 + q**3 + 1

    def red(a):
        return s.Poly(s.expand(a), q).rem(s.Poly(phi, q)).as_expr()

    product = [s.eye(2)] + [s.zeros(2) for _ in range(9)]
    for k in range(8, 0, -1):
        factor = [s.Matrix([[t, -1], [0, 0]]),
                  q**k * s.Matrix([[0, 0], [-t, 1]]),
                  q**(2*k) * s.diag(1, 0)]
        product = [sum((product[j-l] * factor[l]
                        for l in range(min(2, j)+1)), s.zeros(2)).applyfunc(red)
                   for j in range(10)]
    derivatives = [
        [s.zeros(2), s.Matrix([[-t, 1], [0, 0]])],
        [s.Matrix([[-1, 0], [-t, 1]]), s.Matrix([[-1, 0], [1, 0]])],
    ]
    values = [red(sum((s.trace(der[j] * product[9-j]) for j in range(2)),
                      s.S.Zero)) for der in derivatives]
    result = {}
    for delta, (label, tv) in enumerate([("t=1", s.S.One), ("t=q", q)]):
        au, av = [s.expand(red(c.subs(t, tv)).subs(q, 1+pi)) for c in values]
        tangent = s.rem(s.expand(tv.subs(q, 1+pi)*av-au),
                        s.expand(phi.subs(q, 1+pi)), pi)
        print(label, "point Au =", au)
        print(label, "point Av =", av)
        print(label, "point (t Av-Au) =", tangent)
        result[delta] = (au, av, tangent)
    return result


class JetRing:
    def __init__(self, degree):
        self.degree = degree

    def scalar(self, c):
        return {(0, 0, 0): c % 3} if c % 3 else {}

    def mono(self, a, b, c, coefficient=1):
        return {(a, b, c): coefficient % 3} if coefficient % 3 else {}

    def add(self, *terms):
        out = defaultdict(int)
        for term in terms:
            for key, val in term.items():
                out[key] = (out[key]+val) % 3
        return {key: val for key, val in out.items() if val}

    def scale(self, a, c):
        return {key: (val*c) % 3 for key, val in a.items() if (val*c) % 3}

    def mul(self, a, b):
        out = defaultdict(int)
        for ka, va in a.items():
            for kb, vb in b.items():
                key = tuple(ka[i]+kb[i] for i in range(3))
                if sum(key) <= self.degree:
                    out[key] = (out[key]+va*vb) % 3
        return {key: val for key, val in out.items() if val}

    def derivative(self, a, variable):
        out = {}
        for key, val in a.items():
            if key[variable] % 3:
                new = list(key)
                new[variable] -= 1
                out[tuple(new)] = (val*key[variable]) % 3
        return out

    def truncate(self, a, degree):
        return {key: val for key, val in a.items() if sum(key) <= degree}

    def homogeneous(self, a, degree):
        return {key: val for key, val in a.items() if sum(key) == degree}

    def zero_matrix(self):
        return [[{}, {}], [{}, {}]]

    def matrix_mul(self, a, b):
        return [[self.add(*(self.mul(a[i][k], b[k][j]) for k in range(2)))
                 for j in range(2)] for i in range(2)]

    def matrix_add(self, *matrices):
        return [[self.add(*(m[i][j] for m in matrices)) for j in range(2)]
                for i in range(2)]

    def matrix_scale(self, a, polynomial):
        return [[self.mul(a[i][j], polynomial) for j in range(2)] for i in range(2)]

    def q_power(self, k):
        return {(j, 0, 0): comb(k, j) % 3
                for j in range(min(k, self.degree)+1) if comb(k, j) % 3}

    def show(self, polynomial):
        pi, u, v = s.symbols("pi u v")
        return s.expand(sum((c*pi**a*u**b*v**d
                             for (a, b, d), c in polynomial.items()), s.S.Zero))


def jet_contraction(delta, degree=5):
    if delta not in (0, 1) or not 0 <= degree <= 5:
        raise ValueError("Only t in {1,q} and total jet degree <= 5 are certified")
    # Build one extra state degree BEFORE differentiating the matrix.
    ring = JetRing(degree+1)
    one, zero = ring.scalar(1), {}
    pi, u, v = ring.mono(1, 0, 0), ring.mono(0, 1, 0), ring.mono(0, 0, 1)
    t = ring.add(one, ring.scale(pi, delta))
    uv = ring.mul(u, v)
    W = ring.add(one, uv)
    inverse_W = ring.add(*(ring.mono(0, j, j, (-1)**j)
                           for j in range((degree+1)//2+1)))
    J = ring.add(W, ring.scale(ring.mul(v, inverse_W), -1),
                 ring.scale(ring.mul(t, u), -1))
    A0 = [[ring.add(t, ring.scale(v, -1)), ring.scalar(-1)],
          [ring.scale(ring.mul(v, ring.add(t, ring.scale(v, -1))), -1), v]]
    A1 = [[ring.add(J, ring.scalar(-1)), u],
          [ring.add(v, ring.scale(t, -1), ring.mul(ring.mul(v, v), inverse_W)), one]]
    A2 = [[one, zero], [zero, zero]]
    original = [A0, A1, A2]
    derivative = [[[ [ring.truncate(ring.derivative(m[i][j], variable), degree)
                       for j in range(2)] for i in range(2)] for m in original]
                  for variable in (1, 2)]
    jder = [ring.truncate(ring.derivative(J, variable), degree) for variable in (1, 2)]
    original = [[[ring.truncate(m[i][j], degree) for j in range(2)]
                 for i in range(2)] for m in original]
    ring.degree = degree
    identity = [[one, zero], [zero, one]]
    product = [identity] + [ring.zero_matrix() for _ in range(9)]
    for k in range(8, 0, -1):
        factor = [ring.matrix_scale(original[l], ring.q_power(k*l)) for l in range(3)]
        product = [ring.matrix_add(*(ring.matrix_mul(product[j-l], factor[l])
                                     for l in range(min(2, j)+1))) for j in range(10)]
    result = []
    for der in derivative:
        matrix = ring.matrix_add(*(ring.matrix_mul(der[l], product[9-l]) for l in range(3)))
        result.append(ring.add(matrix[0][0], matrix[1][1]))
    au, av = result
    tangent = ring.add(ring.mul(au, jder[1]), ring.scale(ring.mul(av, jder[0]), -1))
    print("delta =", delta, "jet degree =", degree)
    for name, coefficient in [("Au", au), ("Av", av), ("T=Au Jv-Av Ju", tangent)]:
        for d in range(degree+1):
            print(name, "homogeneous", d, "=", ring.show(ring.homogeneous(coefficient, d)))
    return ring, (au, av, tangent)


if __name__ == "__main__":
    exact_points = point_contraction()
    pi = s.symbols("pi")
    for delta in (0, 1):
        ring, jets = jet_contraction(delta)
        for exact, jet in zip(exact_points[delta], jets):
            jet_at_point = ring.show({key: val for key, val in jet.items()
                                      if key[1] == key[2] == 0})
            difference = s.Poly(s.expand(exact-jet_at_point), pi, modulus=3)
            assert difference.is_zero, (delta, exact, jet_at_point)
    print("CHECK: independent exact-point and truncated-state representations agree")
