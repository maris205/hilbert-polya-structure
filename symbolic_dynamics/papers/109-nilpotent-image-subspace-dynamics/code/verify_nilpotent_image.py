#!/usr/bin/env python3
"""Exact controls for nilpotent image dynamics on finite subspace lattices.

The literal side enumerates every subspace through its unique reduced-row-
echelon basis, materializes all vectors, and applies one Jordan shift.  The
closed side uses only Gaussian-binomial formulas.  Prime fields and explicit
polynomial-basis models of F_4, F_8, F_9, and F_16 are covered.
"""

from collections import Counter, defaultdict
from itertools import combinations, product


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, message="assertion failed"):
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


class FiniteField:
    """Small polynomial-basis finite field F_p[x]/(modulus)."""

    def __init__(self, p, modulus=None, label=None):
        self.p = p
        if modulus is None:
            modulus = (0, 1)
        self.modulus = tuple(x % p for x in modulus)
        self.degree = len(self.modulus) - 1
        if self.modulus[-1] != 1:
            raise ValueError("the modulus must be monic")
        self.q = p**self.degree
        self.elements = tuple(range(self.q))
        self.label = label or f"F_{self.q}"

    def _decode(self, a):
        coeffs = []
        for _ in range(self.degree):
            coeffs.append(a % self.p)
            a //= self.p
        return coeffs

    def _encode(self, coeffs):
        out = 0
        place = 1
        for c in coeffs[: self.degree]:
            out += (c % self.p) * place
            place *= self.p
        return out

    def add(self, a, b):
        aa = self._decode(a)
        bb = self._decode(b)
        return self._encode([(x + y) % self.p for x, y in zip(aa, bb)])

    def mul(self, a, b):
        aa = self._decode(a)
        bb = self._decode(b)
        work = [0] * (2 * self.degree - 1)
        for i, x in enumerate(aa):
            for j, y in enumerate(bb):
                work[i + j] = (work[i + j] + x * y) % self.p
        for k in range(len(work) - 1, self.degree - 1, -1):
            c = work[k] % self.p
            if c:
                for j in range(self.degree):
                    work[k - self.degree + j] = (
                        work[k - self.degree + j] - c * self.modulus[j]
                    ) % self.p
        return self._encode(work)

    def validate(self):
        zero, one = 0, 1
        for a in self.elements:
            AUDIT.check(self.add(a, zero) == a)
            AUDIT.check(self.mul(a, one) == a)
            for b in self.elements:
                AUDIT.check(self.add(a, b) == self.add(b, a))
                AUDIT.check(self.mul(a, b) == self.mul(b, a))
        for a in self.elements[1:]:
            AUDIT.check(any(self.mul(a, b) == one for b in self.elements[1:]))


def vadd(u, v, field):
    return tuple(field.add(x, y) for x, y in zip(u, v))


def scale(c, u, field):
    return tuple(field.mul(c, x) for x in u)


def span(basis, field, d):
    out = {(0,) * d}
    for vector in basis:
        out = {
            vadd(x, scale(c, vector, field), field)
            for x in out
            for c in field.elements
        }
    return frozenset(out)


def all_subspaces(field, d):
    spaces = set()
    for r in range(d + 1):
        for pivots in combinations(range(d), r):
            pivot_set = set(pivots)
            free = [
                (i, j)
                for i, pivot in enumerate(pivots)
                for j in range(pivot + 1, d)
                if j not in pivot_set
            ]
            for values in product(field.elements, repeat=len(free)):
                rows = [[0] * d for _ in range(r)]
                for i, pivot in enumerate(pivots):
                    rows[i][pivot] = 1
                for (i, j), value in zip(free, values):
                    rows[i][j] = value
                spaces.add(span([tuple(row) for row in rows], field, d))
    return sorted(spaces, key=lambda space: (len(space), sorted(space)))


def qbinom(n, k, q):
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= q ** (n - i) - 1
        denominator *= q ** (k - i) - 1
    return numerator // denominator


def gauss_sum(d, q):
    return sum(qbinom(d, r, q) for r in range(d + 1))


def dimension(space, q):
    size = len(space)
    r = 0
    while q**r < size:
        r += 1
    AUDIT.check(q**r == size, "a materialized subspace has the wrong size")
    return r


def jordan_shift_vector(vector, t=1):
    d = len(vector)
    if t >= d:
        return (0,) * d
    return tuple(vector[t:]) + (0,) * t


def image(space, t=1):
    return frozenset(jordan_shift_vector(vector, t) for vector in space)


def fibre_formula(t, q, r, s):
    k = r - s
    if k < 0 or k > t:
        return 0
    return qbinom(t, k, q) * q ** (s * (t - k))


def transition_formula(d, t, q, r, s):
    if s < 0 or s > d - t:
        return 0
    return qbinom(d - t, s, q) * fibre_formula(t, q, r, s)


def run_lane(field, d):
    q = field.q
    spaces = all_subspaces(field, d)
    locate = {space: i for i, space in enumerate(spaces)}
    zero = spaces[0]
    whole = spaces[-1]
    AUDIT.check(len(spaces) == gauss_sum(d, q), "phase-size formula failed")

    dims = [dimension(space, q) for space in spaces]
    depth_hist = Counter()
    transitions = {t: Counter() for t in range(d + 1)}
    fibres = {t: defaultdict(Counter) for t in range(d + 1)}

    for u_index, u in enumerate(spaces):
        r = dims[u_index]
        x = u
        depth = 0
        while x != zero:
            x = image(x)
            depth += 1
            AUDIT.check(depth <= d, "orbit escaped the nilpotency bound")
        depth_hist[depth] += 1

        for t in range(d + 1):
            w = image(u, t)
            AUDIT.check(w in locate, "literal image is not a listed subspace")
            s = dims[locate[w]]
            transitions[t][(r, s)] += 1
            fibres[t][w][r] += 1
            if t < d:
                AUDIT.check(image(w) == image(u, t + 1), "iterate law failed")

        for period in range(1, d + 2):
            AUDIT.check((image(u, period) == u) == (u == zero), "periodic point found")

    expected_depths = {
        t: gauss_sum(t, q) - (gauss_sum(t - 1, q) if t else 0)
        for t in range(d + 1)
    }
    AUDIT.check(dict(depth_hist) == expected_depths, "exact-depth law failed")
    AUDIT.check(max(depth_hist) == d, "sharp maximal depth failed")

    for t in range(d + 1):
        image_whole = image(whole, t)
        for w_index, w in enumerate(spaces):
            s = dims[w_index]
            is_target = w.issubset(image_whole)
            for r in range(d + 1):
                expected = fibre_formula(t, q, r, s) if is_target else 0
                AUDIT.check(
                    fibres[t][w][r] == expected,
                    f"fibre mismatch at {(field.label, d, t, r, s)}",
                )
        for r in range(d + 1):
            for s in range(d + 1):
                AUDIT.check(
                    transitions[t][(r, s)] == transition_formula(d, t, q, r, s),
                    f"transition mismatch at {(field.label, d, t, r, s)}",
                )
        cumulative = sum(count for depth, count in depth_hist.items() if depth <= t)
        AUDIT.check(cumulative == gauss_sum(t, q), "absorption CDF failed")

    if d >= 1:
        image_whole = image(whole)
        for w_index, w in enumerate(spaces):
            if w.issubset(image_whole):
                total_preimages = sum(fibres[1][w].values())
                AUDIT.check(total_preimages == q ** dims[w_index] + 1, "indegree law failed")

    recovered_d = max(depth_hist)
    AUDIT.check(recovered_d == d)
    if d >= 2:
        b2 = sum(depth_hist[t] for t in range(3))
        AUDIT.check(b2 - 3 == q, "field-size recovery failed")

    signature = tuple(depth_hist[t] for t in range(d + 1))
    print(
        f"{field.label:>4}, d={d}: subspaces={len(spaces):>5}, "
        f"depths={signature}"
    )
    return signature


def main():
    fields = [
        (FiniteField(2, label="F_2"), 6),
        (FiniteField(3, label="F_3"), 5),
        (FiniteField(5, label="F_5"), 4),
        (FiniteField(2, (1, 1, 1), "F_4"), 4),
        (FiniteField(2, (1, 1, 0, 1), "F_8"), 3),
        (FiniteField(3, (1, 0, 1), "F_9"), 3),
        (FiniteField(2, (1, 1, 0, 0, 1), "F_16"), 3),
    ]
    signatures = []
    for field, max_d in fields:
        field.validate()
        for d in range(1, max_d + 1):
            signatures.append((field.q, d, run_lane(field, d)))

    for q1, d1, sig1 in signatures:
        for q2, d2, sig2 in signatures:
            if sig1 == sig2:
                AUDIT.check(
                    (d1 == d2 == 1) or (q1 == q2 and d1 == d2),
                    "rigidity signature has an unexpected collision",
                )

    print(f"PASS: {AUDIT.assertions:,} exact assertions")


if __name__ == "__main__":
    main()
