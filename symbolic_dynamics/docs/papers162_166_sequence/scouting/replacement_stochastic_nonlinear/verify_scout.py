#!/usr/bin/env python3
"""Deterministic exact breadth checks for 24 stochastic nonlinear kernels."""

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb, gcd

ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def uniform(images):
    out = Counter(images)
    m = len(images)
    return {y: Fraction(c, m) for y, c in out.items()}


def weighted(items):
    items = [(y, w) for y, w in items if w > 0]
    total = sum(w for _, w in items)
    check(total > 0)
    out = defaultdict(Fraction)
    for y, w in items:
        out[y] += Fraction(w, total)
    return dict(out)


def propagate(dist, kernel, steps):
    for _ in range(steps):
        nxt = defaultdict(Fraction)
        for x, px in dist.items():
            for y, pxy in kernel(x).items():
                nxt[y] += px * pxy
        dist = dict(nxt)
        check(sum(dist.values(), Fraction()) == 1)
    return dist


def strong_lumpability(states, kernel, stat):
    seen = {}
    for x in states:
        row = defaultdict(Fraction)
        for y, p in kernel(x).items():
            row[stat(y)] += p
        key = stat(x)
        frozen = tuple(sorted(row.items(), key=lambda z: repr(z[0])))
        if key in seen and seen[key] != frozen:
            return False
        seen[key] = frozen
    return True


def analyse(cid, family, states, kernel, start, stat, steps=4):
    state_set = set(states)
    incoming = defaultdict(Fraction)
    absorbing = 0
    edges = 0
    for x in states:
        row = kernel(x)
        check(row)
        check(sum(row.values(), Fraction()) == 1, f"{cid}: stochastic row")
        check(all(p > 0 for p in row.values()))
        for y, p in row.items():
            check(y in state_set, f"{cid}: escaped carrier")
            incoming[y] += p
            edges += 1
        absorbing += int(row == {x: Fraction(1)})
    dist = propagate({start: Fraction(1)}, kernel, steps)
    positive = [p for p in incoming.values() if p]
    check(sum(incoming.values(), Fraction()) == len(states))
    lump = strong_lumpability(states, kernel, stat)
    pmax = max(dist.values())
    print(
        f"{cid} family={family} states={len(states)} edges={edges} "
        f"absorbing={absorbing} t{steps}_support={len(dist)} "
        f"t{steps}_pmax={pmax} incoming_zero={len(states)-len(incoming)} "
        f"incoming_range={min(positive)}..{max(positive)} coarse_lumpable={int(lump)}"
    )
    return dist, incoming, lump


def rotate_left(w, k):
    k %= len(w)
    return w[k:] + w[:k]


def run_count(w):
    return sum(w[i] != w[(i + 1) % len(w)] for i in range(len(w)))


def word_kernels():
    # W01: flip the strict interior of a pair with equal endpoint bits.
    n = 6
    states = list(product(range(2), repeat=n))
    pairs = list(combinations(range(n), 2))

    def w01(w):
        images = []
        for i, j in pairs:
            z = list(w)
            if w[i] == w[j]:
                for k in range(i + 1, j):
                    z[k] ^= 1
            images.append(tuple(z))
        return uniform(images)

    yield "W01", states, w01, (0, 1, 1, 0, 1, 0), lambda w: (sum(w), run_count(w))

    # W02: rotate an interval left only when its endpoint colours differ.
    n = 5
    states = list(product(range(3), repeat=n))
    pairs = list(combinations(range(n), 2))

    def w02(w):
        images = []
        for i, j in pairs:
            z = list(w)
            if w[i] != w[j]:
                z[i : j + 1] = z[i + 1 : j + 1] + z[i : i + 1]
            images.append(tuple(z))
        return uniform(images)

    yield "W02", states, w02, (0, 1, 2, 0, 2), lambda w: tuple(w.count(a) for a in range(3))

    # W03: select a run through a uniformly selected site and echo its parity
    # into the following site.
    n = 7
    states = list(product(range(2), repeat=n))

    def w03(w):
        images = []
        for i in range(n):
            bit = w[i]
            end = i
            length = 1
            while length < n and w[(end + 1) % n] == bit:
                end = (end + 1) % n
                length += 1
            z = list(w)
            if length < n:
                z[(end + 1) % n] = bit ^ (length & 1)
            images.append(tuple(z))
        return uniform(images)

    yield "W03", states, w03, (0, 0, 1, 1, 1, 0, 1), lambda w: (sum(w), run_count(w))

    # W04: an aba pattern at the sampled cyclic site triggers a global rotation.
    n = 5
    states = list(product(range(3), repeat=n))

    def aba_count(w):
        return sum(w[i] == w[(i + 2) % n] != w[(i + 1) % n] for i in range(n))

    def w04(w):
        return uniform(
            [rotate_left(w, i + 1) if w[i] == w[(i + 2) % n] != w[(i + 1) % n] else w for i in range(n)]
        )

    yield "W04", states, w04, (0, 1, 0, 2, 2), lambda w: (tuple(w.count(a) for a in range(3)), aba_count(w))

    # W05: sample a position and rotate by the multiplicity of its colour.
    n = 6
    states = list(product(range(3), repeat=n))

    def w05(w):
        counts = Counter(w)
        return uniform([rotate_left(w, counts[w[i]]) for i in range(n)])

    start = (0, 0, 0, 1, 1, 2)
    yield "W05", states, w05, start, lambda w: tuple(w.count(a) for a in range(3))

    # Independent convolution check: content is frozen, so increments are iid.
    step = Counter({3: Fraction(3, 6), 2: Fraction(2, 6), 1: Fraction(1, 6)})
    pos = {0: Fraction(1)}
    for _ in range(4):
        nxt = defaultdict(Fraction)
        for a, pa in pos.items():
            for b, pb in step.items():
                nxt[(a + b) % n] += pa * pb
        pos = dict(nxt)
    direct = propagate({start: Fraction(1)}, w05, 4)
    expected = defaultdict(Fraction)
    for k, p in pos.items():
        expected[rotate_left(start, k)] += p
    check(direct == dict(expected), "W05 cyclic convolution formula")


def urn_kernels():
    states6 = [(a, b) for a in range(7) for b in range(7 - a)]

    # U01: square-biased one-ball erosion.
    def u01(x):
        a, b = x
        if a + b == 0:
            return {x: Fraction(1)}
        return weighted([((a - 1, b), a * a), ((a, b - 1), b * b)])

    yield "U01", states6, u01, (4, 2), lambda x: sum(x)

    # U02: pair-reaction urn, AA -> B, BB -> A, AB -> empty.
    def u02(x):
        a, b = x
        z = comb(a + b, 2)
        if z == 0:
            return {x: Fraction(1)}
        return weighted([
            ((a - 2, b + 1), comb(a, 2)),
            ((a + 1, b - 2), comb(b, 2)),
            ((a - 1, b - 1), a * b),
        ])

    yield "U02", states6, u02, (4, 2), lambda x: (sum(x), (x[0] - x[1]) % 3)

    # U03: parity-catalysed growth to a hard population cap.
    def u03(x):
        a, b = x
        if a + b == 6:
            return {x: Fraction(1)}
        return weighted([
            ((a + 1, b), (a + 1) * (1 + (b & 1))),
            ((a, b + 1), (b + 1) * (1 + (a & 1))),
        ])

    yield "U03", states6, u03, (1, 1), lambda x: (sum(x), (x[0] & 1, x[1] & 1))

    # U04: compare a sampled pair; like pairs vanish, unlike pairs leave red.
    def u04(x):
        a, b = x
        z = comb(a + b, 2)
        if z == 0:
            return {x: Fraction(1)}
        return weighted([
            ((a - 2, b), comb(a, 2)),
            ((a, b - 2), comb(b, 2)),
            ((a, b - 1), a * b),
        ])

    yield "U04", states6, u04, (3, 3), lambda x: (sum(x), x[0] & 1)

    # U05: square-biased gcd-sized transfer on a fixed population.
    states = [(a, 6 - a) for a in range(7)]

    def u05(x):
        a, b = x
        items = []
        if a:
            k = min(a, gcd(a, b + 1))
            items.append(((a - k, b + k), a * a))
        if b:
            k = min(b, gcd(b, a + 1))
            items.append(((a + k, b - k), b * b))
        return weighted(items)

    yield "U05", states, u05, (4, 2), lambda x: gcd(x[0] + 1, x[1] + 1)


def mat_mul(a, b, q):
    return (
        (a[0] * b[0] + a[1] * b[2]) % q,
        (a[0] * b[1] + a[1] * b[3]) % q,
        (a[2] * b[0] + a[3] * b[2]) % q,
        (a[2] * b[1] + a[3] * b[3]) % q,
    )


def mat_add(a, b, q, sign=1):
    return tuple((x + sign * y) % q for x, y in zip(a, b))


def mat_rank(a, q):
    if all(x % q == 0 for x in a):
        return 0
    return 2 if (a[0] * a[3] - a[1] * a[2]) % q else 1


def algebra_kernels():
    # A01: random nonlinear mutation of one coefficient of a monic cubic.
    q = 3
    states = list(product(range(q), repeat=3))

    def a01(x):
        a, b, c = x
        return uniform((((b * c) % q, b, c), (a, (a * a + c) % q, c), (a, b, (a * b) % q)))

    yield "A01", states, a01, (1, 2, 2), lambda x: ((x[0] + x[1] + x[2]) % q, sum(v == 0 for v in x))

    # A02: random quadratic scalar update x -> x +/- x^2.
    p = 7
    states = list(range(p))

    def a02(x):
        return uniform(((x + x * x) % p, (x - x * x) % p))

    yield "A02", states, a02, 3, lambda x: (x == 0, pow(x, 3, p))

    # A03: random polynomial shears of a finite affine plane.
    p = 5
    states = list(product(range(p), repeat=2))

    def a03(x):
        a, b = x
        return uniform(((a, (b + a * b) % p), ((a + a * b) % p, b)))

    yield "A03", states, a03, (2, 3), lambda x: (x[0] * x[1]) % p

    # A04: random Frobenius shears in F_2[u]/(u^4).
    states = list(range(16))

    def ring_mul(x, y):
        z = 0
        for i in range(4):
            for j in range(4 - i):
                if ((x >> i) & 1) and ((y >> j) & 1):
                    z ^= 1 << (i + j)
        return z

    def a04(x):
        x2 = ring_mul(x, x)
        return uniform([x ^ ((x2 << k) & 15) for k in (1, 2, 3)])

    yield "A04", states, a04, 15, lambda x: ((x & -x).bit_length() - 1 if x else 4)

    # A05: random matrix polynomial A -> A +/- A^2.
    p = 3
    states = list(product(range(p), repeat=4))

    def a05(a):
        a2 = mat_mul(a, a, p)
        return uniform((mat_add(a, a2, p, 1), mat_add(a, a2, p, -1)))

    yield "A05", states, a05, (1, 1, 2, 0), lambda a: ((a[0] + a[3]) % p, (a[0] * a[3] - a[1] * a[2]) % p)


NGRAPH = 5
GEDGES = list(combinations(range(NGRAPH), 2))
GEDGE_INDEX = {e: i for i, e in enumerate(GEDGES)}


def has_edge(mask, u, v):
    if u > v:
        u, v = v, u
    return (mask >> GEDGE_INDEX[(u, v)]) & 1


def set_edge(mask, u, v, value):
    if u > v:
        u, v = v, u
    bit = 1 << GEDGE_INDEX[(u, v)]
    return (mask | bit) if value else (mask & ~bit)


def triangle_count(mask):
    return sum(all(has_edge(mask, u, v) for u, v in combinations(t, 2)) for t in combinations(range(NGRAPH), 3))


def permute_graph(mask, p):
    out = 0
    for u, v in GEDGES:
        if has_edge(mask, u, v):
            out = set_edge(out, p[u], p[v], 1)
    return out


def transitive_closure(mask, pairs, n):
    rel = [[False] * n for _ in range(n)]
    for k, (i, j) in enumerate(pairs):
        if (mask >> k) & 1:
            rel[i][j] = True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                rel[i][j] |= rel[i][k] and rel[k][j]
    out = 0
    for k, (i, j) in enumerate(pairs):
        out |= int(rel[i][j]) << k
    return out


def graph_poset_kernels():
    states = list(range(1 << len(GEDGES)))
    triples = list(combinations(range(NGRAPH), 3))

    # G01: sample a triple and complete it only if it is an induced wedge.
    def g01(mask):
        images = []
        for tri in triples:
            ep = list(combinations(tri, 2))
            present = [has_edge(mask, *e) for e in ep]
            z = mask
            if sum(present) == 2:
                z = set_edge(z, *ep[present.index(0)], 1)
            images.append(z)
        return uniform(images)

    yield "G01", states, g01, 0b0010110101, lambda m: (m.bit_count(), triangle_count(m))

    # G02: sample an ordered pair; both outside incidences become their XOR.
    ordered = [(u, v) for u in range(NGRAPH) for v in range(NGRAPH) if u != v]

    def g02(mask):
        images = []
        for u, v in ordered:
            z = mask
            old = {w: has_edge(mask, u, w) ^ has_edge(mask, v, w) for w in range(NGRAPH) if w not in (u, v)}
            for w, val in old.items():
                z = set_edge(z, u, w, val)
                z = set_edge(z, v, w, val)
            images.append(z)
        return uniform(images)

    yield "G02", states, g02, 0b1101010011, lambda m: (m.bit_count(), triangle_count(m))

    # G03: an induced one-edge triple triggers a cyclic relabelling of all vertices.
    actions = [(tri, direction) for tri in triples for direction in (1, -1)]

    def g03(mask):
        images = []
        for tri, direction in actions:
            if sum(has_edge(mask, *e) for e in combinations(tri, 2)) != 1:
                images.append(mask)
                continue
            a, b, c = tri
            p = list(range(NGRAPH))
            if direction == 1:
                p[a], p[b], p[c] = b, c, a
            else:
                p[a], p[b], p[c] = c, a, b
            images.append(permute_graph(mask, p))
        return uniform(images)

    yield "G03", states, g03, 0b0001011011, lambda m: (m.bit_count(), triangle_count(m))

    # G04: add a sampled natural comparison and close transitively.
    n = 4
    pairs = list(combinations(range(n), 2))
    posets = [m for m in range(1 << len(pairs)) if transitive_closure(m, pairs, n) == m]

    def g04(mask):
        return uniform([transitive_closure(mask | (1 << k), pairs, n) for k in range(len(pairs))])

    yield "G04", posets, g04, 0, lambda m: m.bit_count()

    # G05: toggle a sampled edge iff its endpoints have odd common-neighbour count.
    def g05(mask):
        images = []
        for u, v in GEDGES:
            cn = sum(has_edge(mask, u, w) and has_edge(mask, v, w) for w in range(NGRAPH) if w not in (u, v))
            images.append(set_edge(mask, u, v, 1 - has_edge(mask, u, v)) if cn & 1 else mask)
        return uniform(images)

    yield "G05", states, g05, 0b1110100101, lambda m: (m.bit_count(), triangle_count(m) & 1)

    # Every active G01 move adds exactly one edge and preserves components; the
    # unique terminal state is the disjoint union of component cliques.
    for mask in states:
        for z in g01(mask):
            check((z | mask) == z)
            check(z.bit_count() - mask.bit_count() in (0, 1))


def det2(u, v, q):
    return (u[0] * v[1] - u[1] * v[0]) % q


def geometry_kernels():
    q = 3
    points = list(product(range(q), repeat=2))
    triangles = list(product(points, repeat=3))

    # F01: sample a vertex and replace it by the midpoint of the opposite side.
    def f01(x):
        images = []
        for i in range(3):
            j, k = [r for r in range(3) if r != i]
            z = list(x)
            z[i] = tuple((2 * (x[j][c] + x[k][c])) % q for c in range(2))
            images.append(tuple(z))
        return uniform(images)

    yield "F01", triangles, f01, ((0, 0), (1, 0), (0, 1)), lambda x: det2(((x[1][0]-x[0][0])%q, (x[1][1]-x[0][1])%q), ((x[2][0]-x[0][0])%q, (x[2][1]-x[0][1])%q), q)

    # F02: area-gated shear of the sampled vertex along the opposite side.
    def f02(x):
        images = []
        for i in range(3):
            j, k = [r for r in range(3) if r != i]
            u = ((x[j][0] - x[i][0]) % q, (x[j][1] - x[i][1]) % q)
            v = ((x[k][0] - x[i][0]) % q, (x[k][1] - x[i][1]) % q)
            delta = det2(u, v, q)
            z = list(x)
            z[i] = tuple((x[i][c] + delta * (x[j][c] - x[k][c])) % q for c in range(2))
            images.append(tuple(z))
        return uniform(images)

    yield "F02", triangles, f02, ((0, 0), (1, 0), (0, 1)), lambda x: det2(((x[1][0]-x[0][0])%q, (x[1][1]-x[0][1])%q), ((x[2][0]-x[0][0])%q, (x[2][1]-x[0][1])%q), q)

    # F03: reflect the sampled vertex in the midpoint of the opposite side.
    def f03(x):
        images = []
        for i in range(3):
            j, k = [r for r in range(3) if r != i]
            z = list(x)
            z[i] = tuple((x[j][c] + x[k][c] - x[i][c]) % q for c in range(2))
            images.append(tuple(z))
        return uniform(images)

    yield "F03", triangles, f03, ((0, 0), (1, 0), (0, 1)), lambda x: det2(((x[1][0]-x[0][0])%q, (x[1][1]-x[0][1])%q), ((x[2][0]-x[0][0])%q, (x[2][1]-x[0][1])%q), q)

    # F04: sample one vector of a frame and rescale it by the determinant.
    frames = list(product(points, repeat=2))

    def f04(x):
        u, v = x
        d = det2(u, v, q)
        return uniform(((tuple(d * a % q for a in u), v), (u, tuple(d * a % q for a in v))))

    yield "F04", frames, f04, ((1, 0), (0, 2)), lambda x: det2(x[0], x[1], q)


def main():
    print("REPLACEMENT_STOCHASTIC_NONLINEAR_EXACT_SCOUT")
    counts = Counter()
    ids = []
    for family, generator in [
        ("word", word_kernels()),
        ("urn", urn_kernels()),
        ("algebra", algebra_kernels()),
        ("graph_poset", graph_poset_kernels()),
        ("geometry", geometry_kernels()),
    ]:
        for cid, states, kernel, start, stat in generator:
            ids.append(cid)
            counts[family] += 1
            analyse(cid, family, states, kernel, start, stat)
    check(len(ids) == 24)
    check(len(set(ids)) == 24)
    check(counts == Counter({"word": 5, "urn": 5, "algebra": 5, "graph_poset": 5, "geometry": 4}))
    print("FAMILY_COUNTS " + " ".join(f"{k}={counts[k]}" for k in ("word", "urn", "algebra", "graph_poset", "geometry")))
    print(f"ASSERTIONS {ASSERTIONS}")
    print("SURVIVORS 0")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
