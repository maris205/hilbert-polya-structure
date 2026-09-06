#!/usr/bin/env python3
"""Formal integer-polynomial desk check. No finite-state pilot or old imports."""
import json

N = 8
ZERO_EXP = (0,) * N


class P(dict):
    def __init__(self, x=0):
        super().__init__(x if isinstance(x, dict) else ({ZERO_EXP: x} if x else {}))

    def __add__(self, other):
        out = P(self)
        for mon, coefficient in P(other).items():
            out[mon] = out.get(mon, 0) + coefficient
            if out[mon] == 0:
                del out[mon]
        return out

    __radd__ = __add__

    def __neg__(self):
        return P({mon: -coefficient for mon, coefficient in self.items()})

    def __sub__(self, other):
        return self + (-P(other))

    def __rsub__(self, other):
        return P(other) - self

    def __mul__(self, other):
        out = P()
        for m, a in self.items():
            for n, b in P(other).items():
                k = tuple(x + y for x, y in zip(m, n))
                out[k] = out.get(k, 0) + a * b
        return P({m: a for m, a in out.items() if a})

    __rmul__ = __mul__


def var(i):
    return P({tuple(int(j == i) for j in range(N)): 1})


def add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def sub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def scale(a, u):
    return tuple(a * x for x in u)


def det(u, v):
    return u[0] * v[1] - u[1] * v[0]


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def J(u):
    return (-u[1], u[0])


CHECKS = []


def check(name, lhs, rhs):
    if isinstance(lhs, tuple):
        for i, (a, b) in enumerate(zip(lhs, rhs)):
            check(name + ':' + str(i), a, b)
        return
    residual = P(lhs) - P(rhs)
    if residual:
        raise AssertionError((name, sorted(residual.items())))
    CHECKS.append(name)


v = tuple((var(2 * i), var(2 * i + 1)) for i in range(4))


def qas_areas(v):
    return tuple(det(sub(v[(i + 1) % 4], v[i]),
                     sub(v[(i - 1) % 4], v[i])) for i in range(4))


A = qas_areas(v)
w = tuple(add(v[i], scale(A[i], sub(add(v[(i + 1) % 4], v[(i - 1) % 4]),
                                  scale(2, v[i])))) for i in range(4))
Ap = qas_areas(w)
H, D, E = A[0] + A[2], A[2] - A[0], A[1] - A[3]
Hp, Dp, Ep = Ap[0] + Ap[2], Ap[2] - Ap[0], Ap[1] - Ap[3]
alpha, gamma = 1 - H, 1 - 3 * H
W = sub(add(v[1], v[3]), add(v[0], v[2]))
Wp = sub(add(w[1], w[3]), add(w[0], w[2]))
check('QAS_area_sum', H, A[1] + A[3])
check('QAS_diagonal_area', H, det(sub(v[2], v[0]), sub(v[3], v[1])))
check('QAS_midpoint_gap', Wp, scale(gamma, W))
check('QAS_H', Hp, H * alpha * alpha - alpha * (D * D + E * E))
check('QAS_D', Dp, gamma * alpha * D)
check('QAS_E', Ep, gamma * alpha * E)
check('QAS_R', Dp * Dp + Ep * Ep,
      gamma * gamma * alpha * alpha * (D * D + E * E))

v = v[:3]
B = tuple(dot(sub(v[(i + 1) % 3], v[i]),
              sub(v[(i - 1) % 3], v[i])) for i in range(3))
w = tuple(add(v[i], scale(B[i], sub(v[(i + 1) % 3], v[(i - 1) % 3])))
          for i in range(3))
x, y = sub(v[1], v[0]), sub(v[2], v[0])
xp, yp = sub(w[1], w[0]), sub(w[2], w[0])
a, b, c, delta = dot(x, x), dot(y, y), dot(x, y), det(x, y)
s = 1 + delta * delta
check('DTC_x', xp, add(x, scale(delta, J(x))))
check('DTC_y', yp, add(y, scale(delta, J(y))))
check('DTC_anchor', w[0], add(v[0], scale(c, sub(x, y))))
check('DTC_area', det(xp, yp), delta * s)
check('DTC_gram_xx', dot(xp, xp), s * a)
check('DTC_gram_xy', dot(xp, yp), s * c)
check('DTC_gram_yy', dot(yp, yp), s * b)
check('DTC_gram_determinant', a * b - c * c, delta * delta)
# Denominator-cleared orthocenter equations, hence no nonzero-area assumption
# is hidden inside the formal polynomial checks.
hnumer = scale(c, J(sub(x, y)))
check('DTC_Hdotx', dot(hnumer, x), delta * c)
check('DTC_Hdoty', dot(hnumer, y), delta * c)
check('DTC_center_translation', scale(-1, J(hnumer)), scale(c, sub(x, y)))

print(json.dumps({'kind': 'formal_integer_polynomial_identity_check',
                  'variables': N, 'identities': len(CHECKS),
                  'checks': CHECKS, 'nonzero_residuals': 0,
                  'finite_state_pilots': 0}, sort_keys=True, indent=2))
