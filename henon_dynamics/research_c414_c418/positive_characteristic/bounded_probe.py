"""Bounded exact screening, not an all-height theorem or a release checker."""

import json
import platform

import sympy as sp
from sympy.polys.domains import GF
from sympy.polys.rings import ring


def resonance():
    R, x, y = ring("x,y", GF(3))
    def frobenius(poly, q):
        return R.from_dict({tuple(q*i for i in mon): coeff for mon, coeff in poly.items()})
    records = []
    for q in [9, 27]:
        for lower in [R.zero, y**5, y**2]:
            hx, hy = x, y
            rows = []
            for n in range(1, 4):
                hx, hy = hy, frobenius(hy, q) + frobenius(hy, 3)**2 + lower.compose(y, hy) - hx
                f1, f2 = hx - x ** (q**n), hy - y ** (q**n)
                d2 = max(sum(m) for m in f2)
                top = sorted((m, int(c)) for m, c in f2.items() if sum(m) == d2)
                assert len(top) == 1 and top[0][0][0] == 0
                assert max(sum(m) for m in f1) == q**n
                rows.append({"n": n, "second_degree": d2, "second_top": top,
                             "coprime_top_length": q**n * d2,
                             "second_terms": len(f2)})
            records.append({"q": q, "g": str(y**6 + lower), "rows": rows})
    return records


def cubic():
    x = sp.Symbol("x")
    iterate = sp.Poly(x, x, modulus=3)
    rows = []
    for n in range(1, 7):
        iterate = iterate**3 + iterate**2
        f = iterate - sp.Poly(x, x, modulus=3)
        _, factors = f.sqf_list()
        root_count = sum(poly.degree() for poly, multiplicity in factors)
        rows.append({"n": n, "scheme_length": f.degree(),
                     "distinct_geometric_roots": root_count,
                     "squarefree_factor_degrees_multiplicities":
                     [(poly.degree(), int(mult)) for poly, mult in factors]})
        if n == 5:
            assert root_count == 238
            repeated = next(poly for poly, mult in factors if mult == 2)
            rows[-1]["repeated_factor"] = str(repeated.as_expr())
            assert sp.gcd(repeated, sp.Poly(x**3+x**2-x, x, modulus=3)).degree() == 0
    return rows


def skew_prime_field():
    rows = []
    for p in [3, 5, 7]:
        # On F_p the two forcings coincide pointwise. The report proves the
        # stronger all-extension bijective conjugacy, without testing it here.
        for n in [1, 2, 3, 4, 5, 6]:
            counts = []
            for power in [1, p, p*p]:
                count = 0
                for x in range(p):
                    for y in range(p):
                        u, v = x, y
                        for _ in range(n):
                            u, v = u*u % p, (pow(v,p,p)+pow(u,power,p)) % p
                        count += (u, v) == (x, y)
                counts.append(count)
            assert len(set(counts)) == 1
            rows.append({"p": p, "n": n, "counts_P_x_xp_xp2": counts})
    return rows


if __name__ == "__main__":
    result = {"python": platform.python_version(), "sympy": sp.__version__,
              "resonance": resonance(), "cubic": cubic(),
              "skew_prime_field": skew_prime_field()}
    print(json.dumps(result, indent=2))
