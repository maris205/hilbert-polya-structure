#!/usr/bin/env python3
"""Bounded exact D01 diagnostic; p=3,m=1,a=2,t=1, original matrix.

No input/output data files, floating point, fitted parameters, or GPU.
Integral descending nine-factor trace is differentiated and divided by nine
in Z[q]/(q^6+q^3+1).  Its image modulo pi^6, pi=q-1, has characteristic 3.
Local tests use F9[a]/(a^2+a+2), j=1+z, y=2+w, x=a+nilpotents,
and the D-stable quotient (pi^n,z^8,w^3), 2<=n<=6.  D=d/dw fixes pi,j.
Passing these tests is NOT proof of descent or of integral-closure descent.
The separate exact Laurent certificate at the end verifies the second
coefficient identity used by the local complete-ideal proof in the companion
document.  That proof, not the finite tests, closes the higher-order tail.
"""

from collections import defaultdict
from math import comb
from time import perf_counter


ZBOUND = 8
WBOUND = 3
PIBOUND = 6


def clean(poly):
    return {key: value for key, value in poly.items() if value}


def original_matrix():
    # Keys: (spectral degree, x Laurent exponent, y exponent, q exponent).
    rows = [
        {(0, 0, 0, 0): 1, (0, 1, 1, 0): -1, (0, 1, 0, 0): 1,
         (1, 0, 1, 0): 1, (1, 1, 0, 0): -1, (1, 1, -1, 0): 1,
         (1, -1, 0, 0): -1, (1, 0, 0, 0): -1, (2, 0, 0, 0): 1},
        {(0, 1, 0, 0): -1, (1, 0, 0, 0): 1},
        {(0, 1, 2, 0): 1, (0, 1, 1, 0): -2, (0, 1, 0, 0): 1,
         (0, 0, 1, 0): -1, (0, 0, 0, 0): 1,
         (1, 1, 1, 0): 1, (1, 0, 1, 0): 1, (1, 1, 0, 0): -2,
         (1, 1, -1, 0): 1, (1, -1, 0, 0): -1, (1, 0, 0, 0): -1},
        {(0, 1, 1, 0): 1, (0, 1, 0, 0): -1, (1, 0, 0, 0): 1},
    ]
    return rows


def left_factor_multiply(factor, product, k):
    result = [defaultdict(int) for _ in range(4)]
    for i in range(2):
        for j in range(2):
            dst = result[2*i+j]
            for h in range(2):
                for (df, xf, yf, _), cf in factor[2*i+h].items():
                    phase = k*df
                    for (dp, xp, yp, qp), cp in product[2*h+j].items():
                        if df+dp <= 9:
                            dst[(df+dp, xf+xp, yf+yp, (phase+qp) % 9)] += cf*cp
    return [clean(poly) for poly in result]


def integral_alpha():
    factor = original_matrix()
    one = {(0, 0, 0, 0): 1}
    product = [one, {}, {}, one]
    started = perf_counter()
    for k in range(9):
        product = left_factor_multiply(factor, product, k)
        print(f"factor={k+1} sparse_terms={sum(map(len, product))}", flush=True)
    integral = defaultdict(int)
    for diagonal in (0, 3):
        for (degree, xe, ye, qe), value in product[diagonal].items():
            if degree != 9:
                continue
            if qe < 6:
                integral[(xe, ye, qe)] += value
            else:
                integral[(xe, ye, qe-3)] -= value
                integral[(xe, ye, qe-6)] -= value
    integral = clean(integral)
    alpha = []
    for direction in (0, 1):
        coeff = defaultdict(int)
        for (xe, ye, qe), value in integral.items():
            exponent = (xe, ye)[direction]
            numerator = value*exponent
            assert numerator % 9 == 0, (direction, xe, ye, qe, numerator)
            if not numerator:
                continue
            nx, ny = xe-(direction == 0), ye-(direction == 1)
            for pe in range(qe+1):
                coeff[(pe, nx, ny)] += (numerator//9)*comb(qe, pe)
        alpha.append({key: value % 3 for key, value in coeff.items() if value % 3})
    print(f"integral_trace_terms={len(integral)} alpha_pi_terms={list(map(len, alpha))} "
          f"seconds={perf_counter()-started:.6f}", flush=True)
    return alpha


# F9 elements c0+3*c1 represent c0+c1*a, with a^2=1+2*a.
def field_add(x, y):
    return ((x % 3+y % 3) % 3)+3*((x//3+y//3) % 3)


def field_mul(x, y):
    a, b, c, d = x % 3, x//3, y % 3, y//3
    return ((a*c+b*d) % 3)+3*((a*d+b*c+2*b*d) % 3)


ADD = [[field_add(x, y) for y in range(9)] for x in range(9)]
MUL = [[field_mul(x, y) for y in range(9)] for x in range(9)]
NEG = [next(y for y in range(9) if ADD[x][y] == 0) for x in range(9)]
INV = [0]+[next(y for y in range(1, 9) if MUL[x][y] == 1) for x in range(1, 9)]


def padd(a, b):
    result = dict(a)
    for key, value in b.items():
        result[key] = ADD[result.get(key, 0)][value]
    return clean(result)


def pscale(a, c):
    return clean({key: MUL[value][c] for key, value in a.items()})


def psub(a, b):
    return padd(a, pscale(b, 2))


def pmul(a, b):
    result = {}
    for (za, wa), ca in a.items():
        for (zb, wb), cb in b.items():
            if za+zb < ZBOUND and wa+wb < WBOUND:
                key = (za+zb, wa+wb)
                result[key] = ADD[result.get(key, 0)][MUL[ca][cb]]
    return clean(result)


def ppow(a, n):
    if n < 0:
        return ppow(pinv(a), -n)
    result = {(0, 0): 1}
    while n:
        if n & 1:
            result = pmul(result, a)
        a = pmul(a, a)
        n //= 2
    return result


def pinv(a):
    constant = a.get((0, 0), 0)
    assert constant
    c = INV[constant]
    u = psub(pscale(a, c), {(0, 0): 1})
    result = {(0, 0): 1}
    term = result
    for _ in range(ZBOUND+WBOUND):
        term = pscale(pmul(term, u), 2)
        result = padd(result, term)
    result = pscale(result, c)
    assert pmul(a, result) == {(0, 0): 1}
    return result


def pdiffw(a):
    return clean({(z, w-1): MUL[value][w % 3]
                  for (z, w), value in a.items() if w})


def local_state():
    one = {(0, 0): 1}
    y = {(0, 0): 2, (0, 1): 1}
    j = {(0, 0): 1, (1, 0): 1}
    x = {(0, 0): 3}
    for _ in range(5):
        # F=(y-1)x^2-y(y-j)x+y; derivative unit at the chosen F9 point.
        f = padd(psub(pmul(psub(y, one), pmul(x, x)),
                       pmul(pmul(y, psub(y, j)), x)), y)
        fx = psub(pscale(pmul(psub(y, one), x), 2), pmul(y, psub(y, j)))
        x = psub(x, pmul(f, pinv(fx)))
    f = padd(psub(pmul(psub(y, one), pmul(x, x)),
                   pmul(pmul(y, psub(y, j)), x)), y)
    assert not f
    j_from_xy = psub(padd(psub(y, x), pmul(x, pinv(y))), pinv(x))
    assert j_from_xy == j
    jx = padd(psub(pinv(y), one), ppow(x, -2))
    jy = psub(one, pmul(x, ppow(y, -2)))
    assert jx.get((0, 0), 0)
    assert not padd(pmul(jx, pdiffw(x)), jy)
    return x, y, j, jx, jy


def evaluate_laurent(alpha, x, y):
    xe = {key[1] for coeff in alpha for key in coeff}
    ye = {key[2] for coeff in alpha for key in coeff}
    xp = {exponent: ppow(x, exponent) for exponent in xe}
    yp = {exponent: ppow(y, exponent) for exponent in ye}
    result = []
    for coeff in alpha:
        parts = [{} for _ in range(PIBOUND)]
        for (pe, xx, yy), value in coeff.items():
            parts[pe] = padd(parts[pe], pscale(pmul(xp[xx], yp[yy]), value))
        result.append(parts)
    return result


def to_vector(parts, n, shift=(0, 0, 0)):
    vector = [0]*(n*ZBOUND*WBOUND)
    sp, sz, sw = shift
    for p, coeff in enumerate(parts):
        if p+sp >= n:
            break
        for (z, w), value in coeff.items():
            if z+sz < ZBOUND and w+sw < WBOUND:
                vector[(p+sp)*ZBOUND*WBOUND+(z+sz)*WBOUND+w+sw] = value
    return vector


def reduce_vector(vector, basis):
    result = list(vector)
    for pivot in sorted(basis):
        c = result[pivot]
        if c:
            row = basis[pivot]
            for i in range(pivot, len(result)):
                if row[i]:
                    result[i] = ADD[result[i]][NEG[MUL[c][row[i]]]]
    return result


def ideal_basis(generators, n):
    basis = {}
    for parts in generators:
        for p in range(n):
            for z in range(ZBOUND):
                for w in range(WBOUND):
                    vector = reduce_vector(to_vector(parts, n, (p, z, w)), basis)
                    if not any(vector):
                        continue
                    pivot = next(i for i, v in enumerate(vector) if v)
                    c = INV[vector[pivot]]
                    basis[pivot] = [MUL[c][v] for v in vector]
    return basis


def format_vector(vector):
    answer = []
    for index, value in enumerate(vector):
        if value:
            p, zw = divmod(index, ZBOUND*WBOUND)
            z, w = divmod(zw, WBOUND)
            answer.append((p, z, w, value % 3, value//3))
    return answer


def laurent_add(a, b, sign=1):
    result = dict(a)
    for key, value in b.items():
        result[key] = (result.get(key, 0)+sign*value) % 3
    return clean(result)


def laurent_mul(a, b):
    result = defaultdict(int)
    for (xa, ya), ca in a.items():
        for (xb, yb), cb in b.items():
            key = (xa+xb, ya+yb)
            result[key] = (result[key]+ca*cb) % 3
    return clean(result)


def symbolic_low_coefficients(alpha):
    """Exact global Laurent certificate, not a finite w-jet extrapolation."""
    import sympy as s
    x, y = s.symbols("x y")
    spectral = s.symbols("Z")
    matrix = s.Matrix(2, 2, [sum(value*spectral**dd*x**xx*y**yy
                                for (dd, xx, yy, _), value in entry.items())
                            for entry in original_matrix()])
    original_j = y-x+x/y-1/x
    assert s.expand(s.trace(matrix)-(1+original_j*spectral+spectral**2)) == 0
    assert s.expand(matrix.det()-spectral**3) == 0
    print("ORIGINAL_MATRIX trace_and_determinant PASS", flush=True)
    j = {(0, 1): 1, (1, 0): 2, (1, -1): 1, (-1, 0): 2}
    jx = {(0, 0): 2, (0, -1): 1, (-2, 0): 1}
    jy = {(0, 0): 1, (1, -2): 2}
    f1 = s.Poly((y-1)*x*x-y*(y-1)*x+y, x, y, modulus=3)
    divided_by = f1**3
    coeff = [[{(xx, yy): value for (pp, xx, yy), value in part.items() if pp == p}
              for p in range(3)] for part in alpha]
    def as_poly(terms, minx, miny):
        return s.Poly.from_dict({(xx-minx, yy-miny): value
                                for (xx, yy), value in terms.items()}, (x, y), modulus=3)

    jp = laurent_add(j, {(0, 0): 1})
    hasse = laurent_add(laurent_mul(j, j), {(0, 0): 2})
    hasse2 = laurent_mul(hasse, hasse)
    hasse4 = laurent_mul(hasse2, hasse2)
    assert coeff[0][0] == laurent_mul(hasse4, jx)
    assert coeff[1][0] == laurent_mul(hasse4, jy)
    print("EXACT_RESIDUE alpha[0]=H^4*dj PASS", flush=True)
    tests = {
        "A1": coeff[0][1],
        "B1": coeff[1][1],
        "Jx_B1_minus_Jy_A1": laurent_add(laurent_mul(jx, coeff[1][1]),
                                         laurent_mul(jy, coeff[0][1]), -1),
        "Jx_B2_minus_Jy_A2": laurent_add(laurent_mul(jx, coeff[1][2]),
                                         laurent_mul(jy, coeff[0][2]), -1),
        "A2_minus_(j+1)_Jx": laurent_add(coeff[0][2],
                                         laurent_mul(jp, jx), -1),
        "B2_minus_(j+1)_Jy": laurent_add(coeff[1][2],
                                         laurent_mul(jp, jy), -1),
    }
    d = y-1
    expected = {
        "A2_minus_(j+1)_Jx": (-5, -7,
            -x**6*d**5+x**3*y**3*(y+1)**3*d**2-x**2*y**3*d-y**3*(y*y+1)),
        "B2_minus_(j+1)_Jy": (-4, -8,
            x**6*d**4*(y+1)-x**3*y**3*d*(y+1)**4-x**2*y**3+x*y**5+y**3*d*(y+1)),
    }
    print("SYMBOLIC_F1=", f1.as_expr(), flush=True)
    for name, terms in tests.items():
        minx = min(xx for xx, yy in terms)
        miny = min(yy for xx, yy in terms)
        poly = as_poly(terms, minx, miny)
        quotient, remainder = poly.div(divided_by)
        assert remainder.is_zero, name
        if name in expected:
            ex, ey, eq = expected[name]
            assert (minx, miny) == (ex, ey), name
            assert quotient == s.Poly(eq, x, y, modulus=3), name
        if name == "Jx_B1_minus_Jy_A1":
            residual = s.Poly(quotient.as_expr().subs(y, 2), x, modulus=3).rem(
                s.Poly(x*x+x+2, x, modulus=3))
            assert residual == s.Poly(2, x, modulus=3)
            print("FIRST_TANGENT_CERTIFICATE R(a,2)=2 PASS", flush=True)
        print(f"LAURENT_DIVISIBILITY {name} monomial_shift=({minx},{miny}) "
              f"quotient_terms={len(quotient.terms())} zero_remainder=True "
              f"compact_certificate={'PASS' if name in expected else 'not_needed'}", flush=True)


def main():
    started = perf_counter()
    alpha = integral_alpha()
    x, y, j, jx, jy = local_state()
    ax, ay = evaluate_laurent(alpha, x, y)
    hasse4 = ppow(padd(ppow(j, 2), {(0, 0): 2}), 4)
    assert ax[0] == pmul(hasse4, jx)
    assert ay[0] == pmul(hasse4, jy)
    # In (dj,dy), alpha = U*dj+V*dy. This is an invertible frame change.
    u = [pmul(part, pinv(jx)) for part in ax]
    v = [psub(ay[k], pmul(u[k], jy)) for k in range(PIBOUND)]
    assert not v[0]
    du = [pdiffw(part) for part in u]
    dv = [pdiffw(part) for part in v]
    # H^3=2*z^3+z^6; b1(P) is the z^3 term in V[1] divided by 2.
    b1_at_p = MUL[v[1].get((3, 0), 0)][2]
    assert b1_at_p == 5  # 2+a, nonzero in F9.
    print("EXACT_FIRST_TANGENT b1(P)=2+a NONZERO", flush=True)
    found = False
    for n in range(2, PIBOUND+1):
        basis = ideal_basis([u, v], n)
        ru = reduce_vector(to_vector(du, n), basis)
        rv = reduce_vector(to_vector(dv, n), basis)
        fail = bool(any(ru) or any(rv))
        print(f"n={n} dimension={n*ZBOUND*WBOUND} ideal_rank={len(basis)} "
              f"quotient_dimension={n*ZBOUND*WBOUND-len(basis)} "
              f"D_stability={'FAIL' if fail else 'PASS_BOUNDED_ONLY'}", flush=True)
        if fail and not found:
            found = True
            print("first_failure_remainder_DU=", format_vector(ru), flush=True)
            print("first_failure_remainder_DV=", format_vector(rv), flush=True)
            for name, parts in (("U", u), ("V", v)):
                print(f"{name}_first_failure=", format_vector(to_vector(parts, n)), flush=True)
    print(f"TOTAL_SECONDS={perf_counter()-started:.6f}", flush=True)
    symbolic_low_coefficients(alpha)
    print(f"TOTAL_WITH_SYMBOLIC_SECONDS={perf_counter()-started:.6f}", flush=True)


if __name__ == "__main__":
    main()
