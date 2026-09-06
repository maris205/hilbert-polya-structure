#!/usr/bin/env python3
"""Bounded literal-iterate checks; no prior result files or nonlinear binomial rule.

The custom small finite fields exercise genuine non-prime-field coefficients.
Prime-subfield cases additionally use SymPy's F5B Groebner implementation.
The full theorem is proved in PROOF_PACKAGE.md, not inferred from these cases.
This program writes only JSON to stdout.
"""

import hashlib
import json
import platform
import time

import sympy as sp


class Field:
    """F_p[z]/(modulus), with little-endian base-p integer representatives."""

    def __init__(self, p, modulus):
        self.p = p
        self.modulus = tuple(modulus)
        self.e = len(modulus) - 1
        self.q = p**self.e
        assert modulus[-1] == 1
        for a in range(self.q):
            assert self.power(a, self.q) == a
            if a:
                assert self.mul(a, self.power(a, self.q - 2)) == 1

    def digits(self, value):
        out = []
        for _ in range(self.e):
            out.append(value % self.p)
            value //= self.p
        assert value == 0
        return out

    def pack(self, digits):
        return sum((a % self.p) * self.p**i for i, a in enumerate(digits))

    def add(self, a, b):
        return self.pack([x + y for x, y in zip(self.digits(a), self.digits(b))])

    def neg(self, a):
        return self.pack([-x for x in self.digits(a)])

    def mul(self, a, b):
        aa, bb = self.digits(a), self.digits(b)
        out = [0] * (2 * self.e - 1)
        for i, x in enumerate(aa):
            for j, y in enumerate(bb):
                out[i + j] = (out[i + j] + x * y) % self.p
        for i in range(len(out) - 1, self.e - 1, -1):
            top = out[i]
            for j in range(self.e):
                out[i - self.e + j] = (
                    out[i - self.e + j] - top * self.modulus[j]
                ) % self.p
        return self.pack(out[: self.e])

    def power(self, a, n):
        out = 1
        while n:
            if n & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            n //= 2
        return out


class Ring:
    """Sparse bivariate polynomials over one of the explicitly checked fields."""

    def __init__(self, field):
        self.f = field
        self.x = {(1, 0): 1}
        self.y = {(0, 1): 1}

    def add(self, a, b):
        out = dict(a)
        for key, value in b.items():
            new = self.f.add(out.get(key, 0), value)
            if new:
                out[key] = new
            else:
                out.pop(key, None)
        return out

    def scale(self, poly, coeff):
        return {
            key: new
            for key, value in poly.items()
            if (new := self.f.mul(value, coeff))
        }

    def mul(self, a, b):
        out = {}
        for (i, j), c in a.items():
            for (k, ell), d in b.items():
                key = (i + k, j + ell)
                new = self.f.add(out.get(key, 0), self.f.mul(c, d))
                if new:
                    out[key] = new
                else:
                    out.pop(key, None)
        return out

    def power(self, a, n):
        out = {(0, 0): 1}
        while n:
            if n & 1:
                out = self.mul(out, a)
            n //= 2
            if n:
                a = self.mul(a, a)
        return out

    def frobenius(self, poly):
        q = self.f.q
        return {(i * q, j * q): self.f.power(c, q) for (i, j), c in poly.items()}

    def evaluate_univariate(self, coeffs, poly):
        out = {}
        for coeff in reversed(coeffs):
            out = self.mul(out, poly)
            if coeff:
                out = self.add(out, {(0, 0): coeff})
        return out

    def literal_iterate(self, a, g, n):
        xx, yy = self.x, self.y
        for _ in range(n):
            next_y = self.add(self.frobenius(yy), self.evaluate_univariate(g, yy))
            next_y = self.add(next_y, self.scale(xx, self.f.neg(a)))
            xx, yy = yy, next_y
        return xx, yy

    def derivative(self, poly, index):
        out = {}
        for powers, coeff in poly.items():
            exponent = powers[index]
            new = self.f.mul(coeff, exponent % self.f.p)
            if new:
                shifted = list(powers)
                shifted[index] -= 1
                out[tuple(shifted)] = new
        return out


def degree_and_top(poly):
    degree = max(sum(key) for key in poly)
    return degree, {key: value for key, value in poly.items() if sum(key) == degree}


def canonical(poly):
    return [[i, j, c] for (i, j), c in sorted(poly.items())]


def digest(poly):
    return hashlib.sha256(json.dumps(canonical(poly), separators=(",", ":")).encode()).hexdigest()


def p_part(n, p):
    r = 1
    while n % p == 0:
        n //= p
        r *= p
    return r


def groebner_length_if_prime_subfield(f1, f2, p):
    if any(c >= p for c in list(f1.values()) + list(f2.values())):
        return {"status": "NOT_RUN_NONPRIME_FIELD_COEFFICIENTS"}
    x, y = sp.symbols("x y")
    # SymPy may normalize values in the supplied dictionary in place.
    # Give it copies so the independent sparse-field producer remains untouched.
    polys = [sp.Poly.from_dict(dict(poly), (x, y), modulus=p) for poly in (f1, f2)]
    basis = sp.groebner(polys, x, y, modulus=p, order="grevlex", method="f5b")
    leads = [tuple(poly.LM(order=basis.order).exponents) for poly in basis.polys]
    x_bound = min(i for i, j in leads if i and not j)
    y_bound = min(j for i, j in leads if j and not i)
    length = sum(
        not any(i >= a and j >= b for a, b in leads)
        for i in range(x_bound)
        for j in range(y_bound)
    )
    return {"status": "EXACT_F5B", "leading_monomials": leads, "standard_monomial_count": length}


def run_case(spec):
    started = time.monotonic()
    field = Field(spec["p"], spec["modulus"])
    ring = Ring(field)
    a, g, n = spec["a"], spec["g_coefficients"], spec["n"]
    q, m = field.q, len(g) - 1
    assert a and g[-1] and 2 <= m < q
    xx, yy = ring.literal_iterate(a, g, n)
    big_q = q**n
    f1 = ring.add(xx, {(big_q, 0): field.neg(1)})
    f2 = ring.add(yy, {(0, big_q): field.neg(1)})
    degree1, top1 = degree_and_top(f1)
    degree2, top2 = degree_and_top(f2)
    dx1, dy1 = ring.derivative(f1, 0), ring.derivative(f1, 1)
    dx2, dy2 = ring.derivative(f2, 0), ring.derivative(f2, 1)
    jac = ring.add(ring.mul(dx1, dy2), ring.scale(ring.mul(dy1, dx2), field.neg(1)))
    assert jac == {(0, 0): field.power(a, n)}
    assert top1 == {(big_q, 0): field.neg(1)}
    assert len(top2) == 1 and (0, degree2) in top2
    exact_length = degree1 * degree2  # justified by coprime actual top monomials
    r = p_part(n, field.p)
    proposed_numerator = (m - 1) * q ** (2 * n) + (q - m) * q ** (2 * n - r)
    assert proposed_numerator % (q - 1) == 0
    proposed_count = proposed_numerator // (q - 1)
    gb = groebner_length_if_prime_subfield(f1, f2, field.p)
    if gb["status"] == "EXACT_F5B":
        assert gb["standard_monomial_count"] == exact_length
    if spec["expected_scope"] == "IN_THEOREM":
        assert m % field.p != 0
        assert exact_length == proposed_count
        d_r = ((m - 1) * q**r + q - m) // (q - 1)
        assert degree2 == q ** (n - r) * d_r
        c_r = field.mul(field.power(g[-1], r), field.power(m % field.p, r - 1))
        assert top2[(0, degree2)] == field.mul((n // r) % field.p, c_r)
    else:
        assert spec["expected_scope"] == "OUTSIDE_P_DIVIDES_M"
        assert m % field.p == 0
        assert exact_length != proposed_count
    return {
        **spec,
        "q": q,
        "degree_g": m,
        "p_part_of_n": r,
        "fixed_equation_degrees": [degree1, degree2],
        "top_forms": [canonical(top1), canonical(top2)],
        "term_counts": [len(f1), len(f2)],
        "literal_equation_sha256": [digest(f1), digest(f2)],
        "jacobian_constant": field.power(a, n),
        "exact_quotient_length_and_geometric_count": exact_length,
        "theorem_formula_or_deliberate_out_of_scope_extrapolation": proposed_count,
        "sympy_cross_check": gb,
        "elapsed_seconds": round(time.monotonic() - started, 6),
    }


def main():
    cases = [
        {"id": "q5_perturbed_prime_to_p", "p": 5, "modulus": [0, 1], "a": 2,
         "g_coefficients": [4, 1, 3, 2], "n": 2, "expected_scope": "IN_THEOREM"},
        {"id": "q9_perturbed_wild", "p": 3, "modulus": [1, 0, 1], "a": 2,
         "g_coefficients": [1, 1, 2], "n": 3, "expected_scope": "IN_THEOREM"},
        {"id": "f4_nonscalar_coefficients_n2", "p": 2, "modulus": [1, 1, 1], "a": 3,
         "g_coefficients": [2, 1, 3, 2], "n": 2, "expected_scope": "IN_THEOREM"},
        {"id": "f4_nonscalar_coefficients_n4", "p": 2, "modulus": [1, 1, 1], "a": 3,
         "g_coefficients": [2, 1, 3, 2], "n": 4, "expected_scope": "IN_THEOREM"},
        {"id": "q8_nonadditive_divisible_degree_boundary", "p": 2, "modulus": [1, 1, 0, 1], "a": 1,
         "g_coefficients": [1, 0, 0, 1, 0, 0, 1], "n": 2,
         "expected_scope": "OUTSIDE_P_DIVIDES_M"},
    ]
    output = {
        "status": "EXACT_BOUNDED_CHECKS_NOT_AN_ALL_PERIOD_PROOF",
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "field_encoding": "base-p digits; alpha is encoded as p; modulus coefficients low to high",
        "method": "literal H composition, exact finite-field arithmetic, actual top forms and Jacobian; F5B only for prime-subfield coefficients",
        "old_runs_reused_or_rerun": False,
        "cases": [run_case(spec) for spec in cases],
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
