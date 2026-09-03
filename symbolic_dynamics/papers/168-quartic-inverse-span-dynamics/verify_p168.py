#!/usr/bin/env python3
"""Paper-local independent verifier for P168 quartic inverse-span dynamics.

Carrier: the complete F_q-subspace lattice of K = F_{q^4}, q prime.
Map:     I(A) = span_Fq({a^{-1}: 0 != a in A}), I(0) = 0.

Only the Python standard library is used.  The script constructs its own
irreducible quartic, field arithmetic, RREF subspaces, transition graph,
cycle data, and one-/two-step fibre tables.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product


PRIMES = (2, 3, 5)


def poly_eval(coeff, x, p):
    ans = 0
    for c in reversed(coeff):
        ans = (ans * x + c) % p
    return ans


def divisible_by_monic(coeff, divisor, p):
    rem = list(coeff)
    m = len(divisor) - 1
    for d in range(len(rem) - 1, m - 1, -1):
        c = rem[d] % p
        if c:
            for j in range(m + 1):
                rem[d - m + j] = (rem[d - m + j] - c * divisor[j]) % p
    return all(x % p == 0 for x in rem[:m])


def first_irreducible_quartic(p):
    # A quartic is reducible iff it has a linear or a quadratic factor.
    for c0 in range(1, p):
        for c1, c2, c3 in product(range(p), repeat=3):
            f = (c0, c1, c2, c3, 1)
            if any(poly_eval(f, a, p) == 0 for a in range(p)):
                continue
            if any(
                divisible_by_monic(f, (b, a, 1), p)
                for a, b in product(range(p), repeat=2)
            ):
                continue
            return f
    raise AssertionError("no irreducible quartic found")


def digits(x, p):
    out = []
    for _ in range(4):
        out.append(x % p)
        x //= p
    return out


def encode(v, p):
    ans = 0
    place = 1
    for x in v:
        ans += (x % p) * place
        place *= p
    return ans


class QuarticField:
    def __init__(self, p):
        self.p = p
        self.order = p**4
        self.modulus = first_irreducible_quartic(p)
        self._digits = tuple(tuple(digits(x, p)) for x in range(self.order))
        self._inverse = [0] * self.order
        for x in range(1, self.order):
            self._inverse[x] = self.pow(x, self.order - 2)
            assert self.mul(x, self._inverse[x]) == 1

    def add(self, x, y):
        return encode(((a + b) % self.p for a, b in zip(self._digits[x], self._digits[y])), self.p)

    def smul(self, c, x):
        return encode(((c * a) % self.p for a in self._digits[x]), self.p)

    def mul(self, x, y):
        p = self.p
        a, b = self._digits[x], self._digits[y]
        tmp = [0] * 7
        for i in range(4):
            for j in range(4):
                tmp[i + j] = (tmp[i + j] + a[i] * b[j]) % p
        for d in range(6, 3, -1):
            c = tmp[d] % p
            if c:
                tmp[d] = 0
                for j in range(4):
                    tmp[d - 4 + j] = (tmp[d - 4 + j] - c * self.modulus[j]) % p
        return encode(tmp[:4], p)

    def pow(self, x, n):
        ans = 1
        while n:
            if n & 1:
                ans = self.mul(ans, x)
            x = self.mul(x, x)
            n >>= 1
        return ans

    def inv(self, x):
        assert x
        return self._inverse[x]


def rref_span(vectors, p):
    rows = [digits(v, p) for v in vectors if v]
    rank = 0
    for col in range(4):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col] % p), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        scale = pow(rows[rank][col], -1, p)
        rows[rank] = [(scale * z) % p for z in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col] % p:
                c = rows[i][col]
                rows[i] = [(u - c * v) % p for u, v in zip(rows[i], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return tuple(encode(row, p) for row in rows[:rank])


def all_subspaces(p):
    spaces = []
    for k in range(5):
        for pivots in combinations(range(4), k):
            free = [(i, j) for i, pivot in enumerate(pivots) for j in range(pivot + 1, 4) if j not in pivots]
            for values in product(range(p), repeat=len(free)):
                rows = [[0] * 4 for _ in range(k)]
                for i, pivot in enumerate(pivots):
                    rows[i][pivot] = 1
                for (i, j), value in zip(free, values):
                    rows[i][j] = value
                spaces.append(tuple(encode(row, p) for row in rows))
    assert len(spaces) == len(set(spaces))
    return tuple(spaces)


@lru_cache(maxsize=None)
def members(space, p):
    out = []
    rows = [digits(v, p) for v in space]
    for coeffs in product(range(p), repeat=len(rows)):
        v = [0] * 4
        for c, row in zip(coeffs, rows):
            for j in range(4):
                v[j] = (v[j] + c * row[j]) % p
        out.append(encode(v, p))
    return tuple(sorted(out))


def image(space, field):
    if not space:
        return ()
    return rref_span((field.inv(x) for x in members(space, field.p) if x), field.p)


def scalar_space(lam, space, field):
    return rref_span((field.mul(lam, x) for x in space), field.p)


def graph_profile(edges):
    tails, periods = [], []
    cycle_keys = set()
    for start in range(len(edges)):
        seen = {}
        path = []
        x = start
        while x not in seen:
            seen[x] = len(path)
            path.append(x)
            x = edges[x]
        mu = seen[x]
        cyc = tuple(path[mu:])
        tails.append(mu)
        periods.append(len(cyc))
        cycle_keys.add(min(cyc))
    cycle_counts = Counter()
    for key in cycle_keys:
        x = edges[key]
        length = 1
        while x != key:
            x = edges[x]
            length += 1
        cycle_counts[length] += 1
    return tails, periods, cycle_counts


def gaussian_counts(p):
    line = p**3 + p**2 + p + 1
    plane = (p**2 + 1) * (p**2 + p + 1)
    return line, plane


def verify_prime(p):
    checks = 0
    field = QuarticField(p)
    spaces = all_subspaces(p)
    index = {space: i for i, space in enumerate(spaces)}
    line, plane = gaussian_counts(p)
    quadratic_planes = p**2 + 1
    total = 2 + 2 * line + plane
    recurrent_expected = 2 + line + quadratic_planes
    fixed_expected = 2 + __import__("math").gcd(2, line) + __import__("math").gcd(2, quadratic_planes)
    assert len(spaces) == total
    checks += 1

    transitions = []
    for space in spaces:
        target = image(space, field)
        assert target in index
        assert len(target) >= len(space)
        transitions.append(index[target])
        checks += 2

    tails, periods, cycles = graph_profile(transitions)
    recurrent = {i for i, tail in enumerate(tails) if tail == 0}
    assert len(recurrent) == recurrent_expected
    assert Counter(periods[i] for i in recurrent) == Counter(
        {1: fixed_expected, 2: recurrent_expected - fixed_expected}
    )
    assert cycles == Counter({1: fixed_expected, 2: (recurrent_expected - fixed_expected) // 2})
    checks += 3

    # Directly recover the unique quadratic subfield and all of its scalar planes.
    subfield_members = [x for x in range(field.order) if field.pow(x, p**2) == x]
    subfield = rref_span(subfield_members, p)
    scaled_subfield_planes = {scalar_space(lam, subfield, field) for lam in range(1, field.order)}
    recurrent_planes = {spaces[i] for i in recurrent if len(spaces[i]) == 2}
    assert len(subfield) == 2
    assert len(scaled_subfield_planes) == quadratic_planes
    assert recurrent_planes == scaled_subfield_planes
    checks += 3

    recurrent_lines = {spaces[i] for i in recurrent if len(spaces[i]) == 1}
    assert len(recurrent_lines) == line
    assert not any(len(spaces[i]) == 3 for i in recurrent)
    assert all(transitions[transitions[i]] == i for i in recurrent)
    checks += 3

    depth_hist = Counter(tails)
    if p == 2:
        assert depth_hist == Counter({0: recurrent_expected, 1: line, 2: plane - quadratic_planes})
        assert len(set(transitions)) == recurrent_expected + line
    else:
        assert depth_hist == Counter({0: recurrent_expected, 1: total - recurrent_expected})
        assert len(set(transitions)) == recurrent_expected
    checks += 2

    # Complete one- and two-step fibre atlas.
    indeg1 = Counter(transitions)
    targets2 = [transitions[transitions[i]] for i in range(total)]
    indeg2 = Counter(targets2)
    targets3 = [transitions[targets2[i]] for i in range(total)]
    targets4 = [transitions[targets3[i]] for i in range(total)]
    indeg3 = Counter(targets3)
    indeg4 = Counter(targets4)
    full = next(i for i, s in enumerate(spaces) if len(s) == 4)
    zero = index[()]
    for i, space in enumerate(spaces):
        d = len(space)
        if i == zero:
            want1 = want2 = 1
        elif i == full:
            want1 = 1 + line if p == 2 else 1 + line + plane - quadratic_planes
            want2 = 1 + line + plane - quadratic_planes
        elif i in recurrent:
            want1 = want2 = 1
        elif p == 2 and d == 3:
            want1, want2 = 2, 0
        else:
            want1 = want2 = 0
        assert indeg1[i] == want1
        assert indeg2[i] == want2
        assert indeg3[i] == want2
        assert indeg4[i] == want2
        checks += 4

    # Rank-by-rank transition law, including the characteristic-two anomaly.
    for i, space in enumerate(spaces):
        d, e = len(space), len(spaces[transitions[i]])
        if d in (0, 1, 4) or i in recurrent:
            assert e == d
        elif d == 3:
            assert e == 4
        elif d == 2:
            assert e == (3 if p == 2 else 4)
        checks += 1

    # Twisted scalar equivariance: I(lambda A)=lambda^{-1}I(A).
    lambdas = range(1, field.order) if p <= 3 else range(1, min(field.order, 32))
    sample_spaces = spaces if p <= 3 else spaces[::7]
    for lam in lambdas:
        inv_lam = field.inv(lam)
        for space in sample_spaces:
            left = image(scalar_space(lam, space, field), field)
            right = scalar_space(inv_lam, image(space, field), field)
            assert left == right
            checks += 1

    serial = []
    for i, space in enumerate(spaces):
        serial.append(f"{p}:{','.join(map(str, space))}>{','.join(map(str, spaces[transitions[i]]))}")
    digest = sha256("\n".join(serial).encode()).hexdigest()
    return {
        "q": p,
        "modulus": field.modulus,
        "states": total,
        "image": len(set(transitions)),
        "recurrent": recurrent_expected,
        "fixed": fixed_expected,
        "cycles": dict(sorted(cycles.items())),
        "depths": dict(sorted(depth_hist.items())),
        "full_fibre_t1": indeg1[full],
        "full_fibre_t2": indeg2[full],
        "sha256": digest,
        "checks": checks,
    }


def main():
    grand_checks = 0
    print("P168 quartic inverse-span author verifier v1")
    for p in PRIMES:
        row = verify_prime(p)
        grand_checks += row["checks"]
        print(
            "q={q} modulus={modulus} states={states} image={image} recurrent={recurrent} "
            "fixed={fixed} cycles={cycles} depths={depths} full_fibre(t=1,t=2)="
            "({full_fibre_t1},{full_fibre_t2}) sha256={sha256} checks={checks}".format(**row)
        )
    print(f"PASS total_checks={grand_checks}")
    print("decision=AUTHOR_ROUND0_PASS")
    print("external_status=HOLD_EXTERNAL_OWNER_THIN")


if __name__ == "__main__":
    main()
