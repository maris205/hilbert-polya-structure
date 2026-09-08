"""Small exact diagnostics for the pre-frozen NG1--NG3 scout.

No census, numerical approximation, boundary-scheme calculation or old
payload rerun. Run with: python exact_checks.py
"""

from fractions import Fraction as Q
from itertools import product
import json

import sympy as s


def cluster_step(point, b, c):
    x, y = point
    assert x and y
    u = (1 + y**b) / x
    assert u
    v = (1 + u**c) / y
    assert v
    return u, v


def main():
    x, y, z, a, k, t = s.symbols("x y z a k t")
    ka = lambda p: sum(q*q for q in p) - s.prod(p) - a*sum(p)
    image = (y, z, y*z+a-x)
    assert s.expand(ka(image) - ka((x, y, z))) == 0
    assert s.expand((t*t+a-t-t).subs(a, 2*t-t*t)) == 0

    finite_type = {}
    for b, c, period in [(1, 1, 5), (1, 2, 3), (1, 3, 4)]:
        pair = (x, y)
        for _ in range(period):
            u = s.cancel((1 + pair[1]**b) / pair[0])
            v = s.cancel((1 + u**c) / pair[1])
            pair = (u, v)
        assert s.cancel(pair[0]-x) == 0
        assert s.cancel(pair[1]-y) == 0
        finite_type[f"{b},{c}"] = period

    # Affine conic conjugacy: y = uv-1, not an extension across y=0.
    u, v = s.symbols("u v")
    next_u = s.cancel((u+v**3)/(u*v-1))
    invariant = (u*u+v*v)/(u*v-1)
    assert s.cancel(next_u - (invariant*v-u)) == 0
    next_invariant = (v*v+next_u*next_u)/(v*next_u-1)
    assert s.cancel(next_invariant-invariant) == 0
    start = (Q(3, 7), Q(-34, 49))
    orbit, pair = [], start
    for _ in range(3):
        orbit.append([str(q) for q in pair])
        pair = cluster_step(pair, 1, 4)
    assert pair == start
    assert len({tuple(p) for p in orbit}) == 3

    wk = lambda p: sum(q*q for q in p) + s.prod(p)**2 + k*s.prod(p)
    compact_identity = x*x+y*y+z*z+(x*y*z+k/2)**2-k*k/4
    assert s.expand(compact_identity-wk((x, y, z))) == 0
    sx = (-x-k*y*z/(1+y*y*z*z), y, z)
    assert s.cancel(wk(sx)-wk((x, y, z))) == 0
    assert s.cancel(-sx[0]-k*y*z/(1+y*y*z*z)-x) == 0

    def k3_step(point, parameter):
        p = list(point)
        for i in range(3):
            j, ell = (i+1) % 3, (i+2) % 3
            p[i] = -p[i]-parameter*p[j]*p[ell]/(1+p[j]**2*p[ell]**2)
        return tuple(p)

    boundary = {}
    for parameter in (-4, 4):
        points = [(Q(0),)*3]
        points += [tuple(map(Q, p)) for p in product((-1, 1), repeat=3)
                   if parameter*p[0]*p[1]*p[2] == -4]
        for p in points:
            assert k3_step(p, parameter) == p
        boundary[str(parameter)] = len(points)

    print(json.dumps({
        "ng1_invariant_and_unbounded_parameter_fixed_points": "PASS",
        "ng2_finite_type_rational_map_identities": finite_type,
        "ng2_affine_conic_invariant_and_linearization": "PASS",
        "ng2_native_affine_period_three_witness": orbit,
        "ng3_involution_and_invariant": "PASS",
        "ng3_all_real_points_compact_square_identity": "PASS",
        "ng3_k_plus_minus_four_fixed_boundary_point_counts": boundary,
        "scope": "identities and explicit witnesses; not global periodic exhaustion",
    }, indent=2))


if __name__ == "__main__":
    main()
