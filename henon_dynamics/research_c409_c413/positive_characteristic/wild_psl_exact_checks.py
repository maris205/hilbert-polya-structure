#!/usr/bin/env python3
"""Bounded exact diagnostics for WILD_PSL_RATIONAL_PROOF.md; stdout only.

The function-field proof, not these finite computations, establishes all
heights. GAP constructs the proposed abstract groups; it does not compute
a function-field Galois group. All cases and precisions are fixed below.
"""

from __future__ import annotations

import json
import subprocess
from fractions import Fraction

import sympy as sp


def first_model(p: int) -> dict:
    v, w = sp.symbols("v w")
    m, b = (p - 1) // 2, (p + 1) // 2
    domain = sp.GF(p).frac_field(v)
    relation = sp.Poly(w**p - w - v**(-b), w, domain=domain)
    r, target = v**m, v**(m * p) + v**(-m)

    def zero(expr: sp.Expr) -> bool:
        numerator, denominator = sp.together(expr).as_numer_denom()
        den = sp.Poly(denominator, w, domain=domain).rem(relation)
        assert not den.is_zero, "undefined expression in the AS function field"
        return sp.Poly(numerator, w, domain=domain).rem(relation).is_zero

    roots = [r] + [r * (w + i)**(p - 1) for i in range(p)]
    for root in roots:
        assert zero(root**(p + 1) - target * root + 1)
    for i in range(p):
        assert zero(roots[i + 1] - r - v**(-1) / (w + i))

    # The root-generated field recovers the AS generators exactly.
    x0, x1 = r + v**(-1) / w, r + v**(-1) / (w + 1)
    assert zero(1 / (x1 - r) - 1 / (x0 - r) - v)
    assert zero(1 / (v * (x0 - r)) - w)

    # Standard unipotent and inversion matrices generate SL_2(F_p).
    for a, c, e, h in ((1, 0, 1, 1), (0, 1, -1, 0)):
        vv = v * (a + c * w)**2
        ww = (e + h * w) / (a + c * w)
        assert zero(ww**p - ww - vv**(-b))
        assert zero(vv**(m * p) + vv**(-m) - target)

    x, t = sp.symbols("x t")
    polynomial = sp.Poly(x**(p + 1) - t*x + 1, x, domain=sp.GF(p).frac_field(t))
    assert polynomial.gcd(polynomial.diff()).degree() == 0
    disc = sp.Poly(sp.discriminant(x**(p + 1) - t*x + 1, x), t, modulus=p)
    assert disc.degree() == 0 and disc.LC() != 0
    return {"p": p, "roots_checked": len(roots), "root_recovery": True,
            "sl2_generator_actions": True, "finite_branch_discriminant": str(disc.LC())}


def series_mul(a: list[int], b: list[int], p: int, precision: int) -> list[int]:
    out = [0] * precision
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b[:precision-i]):
                if y:
                    out[i+j] = (out[i+j] + x*y) % p
    return out


def series_power(a: list[int], exponent: int, p: int, precision: int) -> list[int]:
    out = [1] + [0] * (precision - 1)
    while exponent:
        if exponent & 1:
            out = series_mul(out, a, p, precision)
        a = series_mul(a, a, p, precision)
        exponent >>= 1
    return out


def series_inverse(a: list[int], p: int, precision: int) -> list[int]:
    out = [pow(a[0], -1, p)] + [0] * (precision - 1)
    for n in range(1, precision):
        out[n] = -out[0] * sum(a[i] * out[n-i] for i in range(1, n+1)) % p
    return out


def unit_root(a: list[int], exponent: int, p: int, precision: int) -> list[int]:
    assert a[0] == 1 and exponent % p
    out = [1] + [0] * (precision - 1)
    inverse_exponent = pow(exponent, -1, p)
    for n in range(1, precision):
        coefficient = series_power(out, exponent, p, precision)[n]
        out[n] = (a[n] - coefficient) * inverse_exponent % p
    assert series_power(out, exponent, p, precision) == a
    return out


def local_stability(p: int) -> dict:
    """Use A=pi^-m and B=pi^-m+pi at fixed precision 40.

    Compute the small roots and their m-th roots, then check directly
    that the two AS right sides have identical negative Laurent parts.
    """
    precision = 40
    m, b = (p-1)//2, (p+1)//2
    one = [1] + [0] * (precision - 1)
    units = []
    for perturbation in (False, True):
        a_unit = one.copy()
        if perturbation:
            a_unit[m+1] = 1
        # A^-1 = pi^m / a_unit. The small root s=pi^m*S obeys
        # S = a_unit^-1 * (1 + pi^(m*(p+1))*S^(p+1)).
        inverse_a = series_inverse(a_unit, p, precision)
        s_unit = inverse_a.copy()
        for _ in range(precision):
            powered = series_power(s_unit, p+1, p, precision)
            rhs = one.copy()
            shift = m*(p+1)
            for j in range(precision-shift):
                rhs[j+shift] = (rhs[j+shift] + powered[j]) % p
            new = series_mul(inverse_a, rhs, p, precision)
            if new == s_unit:
                break
            s_unit = new
        else:
            raise AssertionError("fixed precision Hensel iteration did not stabilize")
        v_unit = unit_root(s_unit, m, p, precision)
        as_unit = series_power(series_inverse(v_unit, p, precision), b, p, precision)
        units.append((s_unit, v_unit, as_unit))
    differences = [i for i, (a, z) in enumerate(zip(units[0][2], units[1][2])) if a != z]
    first_difference = differences[0] if differences else None
    assert first_difference is not None and first_difference >= b
    assert units[0][2][:b] == units[1][2][:b]
    s_differences = [i for i, (a, z) in enumerate(zip(units[0][0], units[1][0])) if a != z]
    assert m + s_differences[0] == 2*m+1
    return {"p": p, "precision": precision,
            "small_root_difference_order": 2*m+1,
            "as_difference_laurent_order": first_difference-b,
            "negative_as_parts_equal": True}


def projective_generators(p: int) -> list[tuple[int, ...]]:
    # Coordinates are F_p followed by infinity. Translation and -1/z.
    translation = tuple(list(range(1, p)) + [0, p])
    inversion = tuple([p] + [(-pow(i, -1, p)) % p for i in range(1, p)] + [0])
    return [translation, inversion]


def wreath_generators(p: int, n: int) -> list[tuple[int, ...]]:
    first = projective_generators(p)
    if n == 1:
        return first
    d, branch = p+1, (p+1)**(n-1)
    size = d*branch
    output = [tuple(g[i//branch]*branch + i%branch for i in range(size)) for g in first]
    for block in range(d):
        for g in wreath_generators(p, n-1):
            perm = list(range(size))
            for j in range(branch):
                perm[block*branch+j] = block*branch+g[j]
            output.append(tuple(perm))
    return output


def group_checks() -> list[dict]:
    commands = ["SetInfoLevel(InfoWarning,0);;"]
    expected = []
    for p in (5, 7):
        d, first_order = p+1, p*(p*p-1)//2
        for n in (1, 2):
            generators = ["PermList(" + str([i+1 for i in g]) + ")"
                          for g in wreath_generators(p, n)]
            commands.append("g:=Group([" + ",".join(generators) + "]);;")
            commands.append("h:=Stabilizer(g,1);;")
            commands.append("lens:=SortedList(List(Orbits(h,[2.." + str(d**n)
                            + "]),Length));;")
            commands.append('Print("GROUP ",' + str(p) + '," ",' + str(n)
                            + '," ",Size(g)," ",Size(h)," ",lens,"\\n");;')
            order = first_order**((d**n-1)//p)
            expected.append((p, n, order, order//d**n, sorted([p*d**j for j in range(n)])))
    commands.append("QUIT;")
    process = subprocess.run(["gap", "-q", "-b"], input="\n".join(commands),
                             text=True, capture_output=True, check=True, timeout=45)
    assert not process.stderr.strip(), process.stderr
    actual = []
    for row in process.stdout.splitlines():
        if row.startswith("GROUP "):
            header, lengths = row.split("[", 1)
            p, n, order, stabilizer = map(int, header.split()[1:])
            orbit_lengths = [int(v.strip()) for v in lengths.rstrip("] ").split(",")]
            actual.append((p, n, order, stabilizer, orbit_lengths))
    assert actual == expected, (actual, expected, process.stdout)
    return [{"p": p, "n": n, "abstract_wreath_order": order,
             "leaf_stabilizer_order": stabilizer, "other_leaf_orbit_lengths": lengths}
            for p, n, order, stabilizer, lengths in actual]


def ramification_arithmetic() -> list[dict]:
    rows = []
    for p in (5, 7, 11):
        m, b, d = (p-1)//2, (p+1)//2, p+1
        first_order = p*(p*p-1)//2
        for n in (1, 2, 3):
            order = first_order**((d**n-1)//p)
            e = m*p**n
            different = p**(n+1)-(m+2)
            root_different = 2*p*(p**n-1)//(p-1)
            assert different == m-1+m*root_different
            assert different == e-1+b*(p**n-1)
            genus = 1 + Fraction(order, 2) * (-2+Fraction(different, e))
            claimed = 1 + Fraction(order, 2*m) * (1-Fraction(m+2, p**n))
            assert genus == claimed and genus.denominator == 1 and genus >= 0
            if n == 1:
                assert genus == m*m
            rows.append({"p": p, "n": n, "e_infinity": e, "different": different,
                         "lower_break": b, "genus": int(genus)})
    return rows


def main() -> None:
    payload = {"first_level_symbolic": [first_model(p) for p in (5, 7, 11)],
               "local_stability": [local_stability(p) for p in (5, 7, 11)],
               "groups": group_checks(), "ramification_consistency": ramification_arithmetic(),
               "boundaries": {"finite_tests_are_not_all_height_proof": True,
                              "gap_does_not_compute_function_field_galois_groups": True,
                              "p_2_3_excluded": True, "no_finite_field_census": True}}
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
