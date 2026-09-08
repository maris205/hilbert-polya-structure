#!/usr/bin/env python3
"""Bounded new falsifiers, not a proof of an all-parameter theorem.

Pure Python; stdout only. No predecessor checks are imported or executed.
The quartic jets have explicit cutoffs. The Hénon checks use exact F_9
polynomials; finite-field point checks are identities, not geometric counts.
"""

import json


class Field:
    def __init__(self, p, quadratic=False):
        self.p = p
        self.quadratic = quadratic
        if quadratic and p != 3:
            raise ValueError("Only F_9=F_3[u]/(u^2+1) is implemented")

    def add(self, x, y):
        if not self.quadratic:
            return (x + y) % self.p
        return (x % 3 + y % 3) % 3 + 3 * ((x // 3 + y // 3) % 3)

    def neg(self, x):
        if not self.quadratic:
            return -x % self.p
        return (-x % 3) % 3 + 3 * ((- (x // 3)) % 3)

    def mul(self, x, y):
        if not self.quadratic:
            return x * y % self.p
        a, b, c, d = x % 3, x // 3, y % 3, y // 3
        return (a * c - b * d) % 3 + 3 * ((a * d + b * c) % 3)

    def power(self, x, n):
        ans = 1
        while n:
            if n & 1:
                ans = self.mul(ans, x)
            x = self.mul(x, x)
            n >>= 1
        return ans


class Ring:
    def __init__(self, field, nvars, cutoff=None, cutoff_axis=None):
        self.f = field
        self.nvars = nvars
        self.cutoff = cutoff
        self.cutoff_axis = cutoff_axis
        self.zero = (0,) * nvars

    def scalar(self, x):
        return {self.zero: x} if x else {}

    def kept(self, exponents):
        degree = (sum(exponents) if self.cutoff_axis is None
                  else exponents[self.cutoff_axis])
        return self.cutoff is None or degree < self.cutoff

    def variable(self, i):
        e = [0] * self.nvars
        e[i] = 1
        return {tuple(e): 1}

    def add(self, x, y):
        ans = dict(x)
        for e, c in y.items():
            ans[e] = self.f.add(ans.get(e, 0), c)
            if not ans[e]:
                del ans[e]
        return ans

    def scale(self, x, c):
        return {e: self.f.mul(a, c) for e, a in x.items() if c}

    def sub(self, x, y):
        return self.add(x, {e: self.f.neg(c) for e, c in y.items()})

    def mul(self, x, y):
        ans = {}
        for e, c in x.items():
            for f, d in y.items():
                ef = tuple(a + b for a, b in zip(e, f))
                if not self.kept(ef):
                    continue
                ans[ef] = self.f.add(ans.get(ef, 0), self.f.mul(c, d))
                if not ans[ef]:
                    del ans[ef]
        return ans

    def power(self, x, n):
        ans = self.scalar(1)
        while n:
            if n & 1:
                ans = self.mul(ans, x)
            x = self.mul(x, x)
            n >>= 1
        return ans

    def compose(self, poly, coords, coefficient_power=1):
        caches = [{} for _ in coords]
        ans = {}
        for exponents, c in poly.items():
            term = self.scalar(self.f.power(c, coefficient_power))
            for i, exponent in enumerate(exponents):
                if exponent not in caches[i]:
                    caches[i][exponent] = self.power(coords[i], exponent)
                term = self.mul(term, caches[i][exponent])
            ans = self.add(ans, term)
        return ans

    def frobenius(self, poly, q):
        return {tuple(q * i for i in e): self.f.power(c, q)
                for e, c in poly.items()
                if self.kept(tuple(q * i for i in e))}

    def evaluate(self, poly, values):
        ans = 0
        for exponents, c in poly.items():
            for x, exponent in zip(values, exponents):
                c = self.f.mul(c, self.f.power(x, exponent))
            ans = self.f.add(ans, c)
        return ans


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def quartic_jets():
    rows = []
    for p, cutoff in ((5, 64), (7, 128)):
        r = Ring(Field(p), 1, cutoff)
        z = r.variable(0)
        for b in range(p):
            f = r.add(r.add(z, r.power(z, 2)), r.power(z, 3))
            f = r.add(f, r.scale(r.power(z, 4), b))
            left = right = z
            for _ in range(p):
                left = r.compose(f, [left])
                right = r.compose(right, [f])
            require(left == right, "Independent composition order disagrees")
            difference = r.sub(left, z)
            degree = min((e[0] for e in difference), default=None)
            rows.append({"p": p, "b": b, "modulus": f"z^{cutoff}",
                         "i1": None if degree is None else degree - 1,
                         "leading_coefficient": None if degree is None
                         else difference[(degree,)],
                         "unresolved_if_zero_mod_cutoff": degree is None})
    return rows


def symbolic_quartic_first_term():
    """All coefficients b in two fixed characteristics; no all-prime claim."""
    rows = []
    for p in (5, 7):
        cutoff = 3 * p + 3
        r = Ring(Field(p), 2, cutoff, cutoff_axis=0)
        z, b = r.variable(0), r.variable(1)
        f = r.add(r.add(z, r.power(z, 2)), r.power(z, 3))
        f = r.add(f, r.mul(b, r.power(z, 4)))
        left = right = z
        for _ in range(p):
            left = r.compose(f, [left, b])
            right = r.compose(right, [f, b])
        require(left == right, "Symbolic-b compositions disagree")
        difference = r.sub(left, z)
        degree = min(e[0] for e in difference)
        coeffs = {str(e[1]): c for e, c in difference.items() if e[0] == degree}
        rows.append({"p": p, "modulus": f"z^{cutoff}",
                     "generic_i1": degree - 1,
                     "leading_coefficient_as_b_degree_to_Fp_coefficient": coeffs,
                     "nonconstant_has_exceptional_roots_over_finite_extensions":
                     any(int(deg) > 0 for deg in coeffs)})
    return rows


def twisted_henon():
    k = Field(3, quadratic=True)
    r = Ring(k, 2)
    x, y = r.variable(0), r.variable(1)
    rows = []
    # Both chosen pairs have a coefficient outside the prime field.
    for a, c in ((3, 4), (1, 3)):
        h = [y, r.sub(r.add(r.power(y, 3), r.scale(r.power(y, 2), c)),
                      r.scale(x, a))]
        def t(poly):
            return r.compose(poly, h, coefficient_power=3)
        def u(poly):
            return r.frobenius(poly, 3)
        def delta(poly):
            return r.sub(t(poly), u(poly))

        probe = r.add(r.scale(r.mul(x, r.power(y, 2)), 3),
                      r.add(r.scale(x, 4), r.scalar(5)))
        require(t(u(probe)) == u(t(probe)), "T,U failed commutation")
        require(delta(r.scalar(3)) == {}, "Delta failed to kill constants")
        # Contrast with the invalid replacement of T by coefficient-linear H*.
        hstar_delta = r.sub(r.compose(r.scale(y, 3), h), u(r.scale(y, 3)))
        require(max(map(sum, hstar_delta)) == 3,
                "Expected leading-degree failure without coefficient twist")

        tn_x, tn_y, un_x, un_y = x, y, x, y
        dn_y = y
        period_rows = []
        for n in (1, 2, 3):
            tn_x, tn_y, un_x, un_y = t(tn_x), t(tn_y), u(un_x), u(un_y)
            dn_y = delta(dn_y)
            f1, f2 = r.sub(tn_x, un_x), r.sub(tn_y, un_y)
            w = 3 if n == 3 else 1
            predicted_d = ((3 ** w + 1) // 2) * 3 ** (n - w)
            top1 = sorted(e for e in f1 if sum(e) == 3 ** n)
            top2 = sorted(e for e in f2 if sum(e) == predicted_d)
            require(max(map(sum, f1)) == 3 ** n and top1 == [(3 ** n, 0)],
                    "Wrong first equation leading monomial")
            require(max(map(sum, f2)) == predicted_d and top2 == [(0, predicted_d)],
                    "Wrong second equation leading monomial")
            if n == 3:
                require(f2 == dn_y, "Characteristic-three binomial failed")
            period_rows.append({"n": n, "first_degree": 3 ** n,
                                "second_degree": predicted_d,
                                "coprime_leading_monomials": [top1[0], top2[0]],
                                "quotient_length_from_these_monomials":
                                3 ** n * predicted_d})

        a_inv = k.power(a, 7)
        def s(point):
            xx, yy = point
            first = k.add(k.power(xx, 9), k.mul(c, k.power(xx, 6)))
            first = k.add(first, k.neg(k.power(yy, 3)))
            return (k.mul(a_inv, first), k.power(xx, 3))

        t2 = [t(t(x)), t(t(y))]
        checks = 0
        for xx in range(9):
            for yy in range(9):
                ss = s(s((xx, yy)))
                native_fixed = ss == (xx, yy)
                cocycle_fixed = all(r.evaluate(poly, (xx, yy)) == value
                                    for poly, value in zip(t2, (k.power(xx, 9),
                                                               k.power(yy, 9))))
                require(native_fixed == cocycle_fixed, "Native clock mismatch")
                checks += 1
        rows.append({"field": "F_9=F_3[u]/(u^2+1), a+b*u encoded a+3*b",
                     "a": a, "c": c, "period_polynomials": period_rows,
                     "native_two_step_equivalence_checks": checks,
                     "finite_field_points_not_used_as_geometric_counts": True})
    return rows


if __name__ == "__main__":
    result = {"scope": "bounded screening only", "quartic_jets": quartic_jets(),
              "symbolic_quartic_first_term": symbolic_quartic_first_term(),
              "twisted_henon": twisted_henon()}
    print(json.dumps(result, indent=2, sort_keys=True))
