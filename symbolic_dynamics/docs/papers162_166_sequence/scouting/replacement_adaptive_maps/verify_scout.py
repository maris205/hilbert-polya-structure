#!/usr/bin/env python3
"""Deterministic exact probes for the adaptive-map replacement lane.

This file is intentionally independent of every paper and prior scout
verifier.  It uses the Python standard library only.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from math import comb, gcd


class Audit:
    def __init__(self):
        self.assertions = 0

    def eq(self, got, want, label=""):
        self.assertions += 1
        if got != want:
            raise AssertionError(f"{label}: got {got!r}, want {want!r}")

    def ok(self, value, label=""):
        self.assertions += 1
        if not value:
            raise AssertionError(label or "assertion failed")


A = Audit()


def rot(x, s):
    if not x:
        return x
    s %= len(x)
    return x[s:] + x[:s]


def iterate(fn, x, t):
    for _ in range(t):
        x = fn(x)
    return x


def functional_signature(states, fn):
    states = tuple(states)
    state_set = set(states)
    fibres = Counter(fn(x) for x in states)
    A.ok(set(fibres) <= state_set, "functional closure")
    cycles = set()
    max_tail = 0
    tail_hist = Counter()
    for start in states:
        order = {}
        path = []
        x = start
        while x not in order:
            order[x] = len(path)
            path.append(x)
            x = fn(x)
        mu = order[x]
        max_tail = max(max_tail, mu)
        tail_hist[mu] += 1
        cycles.add(frozenset(path[mu:]))
    return (
        len(fibres),
        tuple(sorted(Counter(fibres.values()).items())),
        tuple(sorted(Counter(map(len, cycles)).items())),
        max_tail,
        tuple(sorted(tail_hist.items())),
    )


# ---------------------------------------------------------------------------
# 01. Adaptive quotient-normalized rotation (full candidate pressure test).


def differences(w, q):
    return tuple((w[(i + 1) % len(w)] - w[i]) % q for i in range(len(w)))


def change_count(w, q):
    return sum(x != 0 for x in differences(w, q))


def aqn(w, q, c=1):
    k = change_count(w, q)
    rw = rot(w, c * k)
    return tuple((x - w[0]) % q for x in rw)


def aqn_direct(w, q, c, t):
    if t == 0:
        return w
    n = len(w)
    k = change_count(w, q)
    s = c * k
    return tuple((w[(i + t * s) % n] - w[((t - 1) * s) % n]) % q for i in range(n))


def rotational_period(x):
    return next(s for s in range(1, len(x) + 1) if rot(x, s) == x)


def zero_sum_nonzero_tuples(q, s):
    # Number of ordered s-tuples of nonzero field elements with zero sum.
    return ((q - 1) ** s + (q - 1) * ((-1) ** s)) // q


def aqn_invariant_count_formula(n, q, k):
    return comb(n, k) * zero_sum_nonzero_tuples(q, k)


def aqn_fixed_formula(n, q, c, ell):
    total = 0
    for k in range(n + 1):
        g = gcd(n, ell * c * k)
        repeat = n // g
        if k % repeat:
            continue
        s = k // repeat
        if q and repeat % q == 0:
            assignments = comb(g, s) * (q - 1) ** s
        else:
            assignments = comb(g, s) * zero_sum_nonzero_tuples(q, s)
        total += assignments
    return total


def probe_aqn():
    configs = [(2, n) for n in range(1, 10)] + [(3, n) for n in range(1, 8)] + [(5, n) for n in range(1, 6)]
    showcase = None
    for q, n in configs:
        states = tuple(product(range(q), repeat=n))
        c_values = sorted({0, 1, 2 % n, (n - 1) % n})
        for c in c_values:
            fn = lambda w, q=q, c=c: aqn(w, q, c)
            fibres = Counter(fn(w) for w in states)
            image = set(fibres)
            A.eq(len(image), q ** (n - 1), "AQN image size")
            A.ok(all(v == q for v in fibres.values()), "AQN uniform fibres")
            for y in states:
                k = change_count(y, q)
                A.eq(y in image, y[(-c * k) % n] == 0, "AQN image criterion")
            for w in states:
                k = change_count(w, q)
                A.eq(change_count(fn(w), q), k, "AQN invariant")
                A.eq(differences(fn(w), q), rot(differences(w, q), c * k), "AQN difference rotation")
                for t in range(1, n + 3):
                    A.eq(iterate(fn, w, t), aqn_direct(w, q, c, t), "AQN iterate")
            for t in range(1, min(n, 3) + 1):
                weighted = defaultdict(Counter)
                for w in states:
                    weighted[iterate(fn, w, t)][sum(x == 0 for x in w)] += 1
                A.eq(set(weighted), image, "AQN all-time image")
                for y, actual in weighted.items():
                    freq = Counter(y)
                    expected = Counter(freq.get(a, 0) for a in range(q))
                    A.eq(actual, expected, "AQN zero-weight fibre polynomial")
            hist = Counter(change_count(y, q) for y in image)
            for k in range(n + 1):
                A.eq(hist[k], aqn_invariant_count_formula(n, q, k), "AQN invariant census")
            for ell in range(1, 2 * n + 1):
                actual = sum(iterate(fn, y, ell) == y for y in image)
                A.eq(actual, aqn_fixed_formula(n, q, c, ell), "AQN fixed-count formula")
            for y in image:
                d = differences(y, q)
                p = rotational_period(d)
                k = change_count(y, q)
                predicted = p // gcd(p, c * k)
                actual = next(s for s in range(1, n + 1) if iterate(fn, y, s) == y)
                A.eq(actual, predicted, "AQN cycle period")
            if (q, n, c) == (3, 6, 1):
                periods = Counter(next(s for s in range(1, n + 1) if iterate(fn, y, s) == y) for y in image)
                showcase = (len(states), len(image), tuple(sorted(periods.items())), tuple(sorted(hist.items())))
        if q % 2 and n >= 3:
            marked = {}
            for y in states:
                zeros = [i for i, x in enumerate(y) if x == 0]
                if len(zeros) == 1 and change_count(y, q) in (2, 3):
                    marked[(change_count(y, q), zeros[0])] = y
            for c in range(n):
                z2 = (-2 * c) % n
                z3 = (-3 * c) % n
                A.ok((2, z2) in marked and (3, z3) in marked, "AQN marked recovery witnesses")
                y2, y3 = marked[(2, z2)], marked[(3, z3)]
                A.ok(y2[(-2 * c) % n] == 0 and y3[(-3 * c) % n] == 0, "AQN marked images")
                A.eq((z2 - z3) % n, c, "AQN parameter recovery")
    A.ok(showcase is not None, "AQN showcase")
    return f"AQN q=3,n=6 state/image={showcase[0]}/{showcase[1]}, point-periods={showcase[2]}, change-census={showcase[3]}"


# ---------------------------------------------------------------------------
# State-dependent finite actions (02--14).


def binary_weight_rotation(w):
    return rot(w, sum(w))


def difference_rotation(w, q):
    return rot(w, change_count(w, q))


def reverse_tuple(w):
    return tuple(reversed(w))


def adaptive_dihedral(w, q):
    k = change_count(w, q)
    return rot(w, k) if k % 2 == 0 else rot(reverse_tuple(w), k)


def colour_count_rotation(w):
    return rot(w, len(set(w)))


def translate_mask(mask, n, s):
    out = 0
    for i in range(n):
        if mask >> i & 1:
            out |= 1 << ((i + s) % n)
    return out


def set_partitions(n):
    out = []

    def rec(rgs):
        if len(rgs) == n:
            blocks = []
            for b in range(max(rgs) + 1):
                blocks.append(frozenset(i for i, x in enumerate(rgs) if x == b))
            out.append(frozenset(blocks))
            return
        for x in range(max(rgs) + 2):
            rec(rgs + [x])

    if n == 0:
        return (frozenset(),)
    rec([0])
    return tuple(out)


def rotate_partition(P, n):
    s = len(P)
    return frozenset(frozenset((x + s) % n for x in block) for block in P)


def edge_list(n):
    return tuple(combinations(range(n), 2))


def relabel_graph(mask, n):
    edges = edge_list(n)
    index = {e: i for i, e in enumerate(edges)}
    s = mask.bit_count() % n
    out = 0
    for j, (u, v) in enumerate(edges):
        if mask >> j & 1:
            e = tuple(sorted(((u + s) % n, (v + s) % n)))
            out |= 1 << index[e]
    return out


def conjugate_shift(f, s):
    n = len(f)
    return tuple((f[(i - s) % n] + s) % n for i in range(n))


def permutation_fixed_conjugation(p):
    s = sum(p[i] == i for i in range(len(p)))
    return conjugate_shift(p, s)


def endofunction_image_conjugation(f):
    return conjugate_shift(f, len(set(f)))


def rotate_partial_word(w):
    return rot(w, sum(x is None for x in w))


def partial_permutations(n):
    out = []
    for r in range(n + 1):
        for dom in combinations(range(n), r):
            for image in combinations(range(n), r):
                for vals in permutations(image):
                    f = [None] * n
                    for i, v in zip(dom, vals):
                        f[i] = v
                    out.append(tuple(f))
    return tuple(out)


def conjugate_partial(p):
    n = len(p)
    s = sum(x is None for x in p)
    out = [None] * n
    for i in range(n):
        old = (i - s) % n
        if p[old] is not None:
            out[i] = (p[old] + s) % n
    return tuple(out)


def inv0(x, q):
    return 0 if x == 0 else pow(x, q - 2, q)


def inverse_support_rotation(w, q):
    k = sum(x != 0 for x in w)
    return rot(tuple(inv0(x, q) for x in w), k)


def weight_complement_rotation(w):
    return rot(tuple(1 - x for x in w), sum(w))


def matrix_rank_f2(bits, r, c):
    rows = []
    for i in range(r):
        row = sum(((bits >> (i * c + j)) & 1) << j for j in range(c))
        rows.append(row)
    rank = 0
    for col in range(c):
        pivot = next((i for i in range(rank, r) if rows[i] >> col & 1), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(r):
            if i != rank and rows[i] >> col & 1:
                rows[i] ^= rows[rank]
        rank += 1
    return rank


def matrix_rank_rotation(bits, r=3, c=3):
    k = matrix_rank_f2(bits, r, c)
    out = 0
    for i in range(r):
        for j in range(c):
            if bits >> (i * c + j) & 1:
                u = (i + k) % r
                v = (j + k + 1) % c
                out |= 1 << (u * c + v)
    return out


def colouring_translation(w, q):
    k = len(set(w))
    return tuple((x + k) % q for x in w)


def probe_actions():
    lines = []
    states = tuple(product((0, 1), repeat=9))
    lines.append(f"HWR binary n=9 signature={functional_signature(states, binary_weight_rotation)}")

    states = tuple(product(range(3), repeat=6))
    lines.append(f"DCR q=3,n=6 signature={functional_signature(states, lambda w: difference_rotation(w, 3))}")
    lines.append(f"DAR q=3,n=6 signature={functional_signature(states, lambda w: adaptive_dihedral(w, 3))}")
    lines.append(f"CCR q=3,n=6 signature={functional_signature(states, colour_count_rotation)}")

    n = 9
    states = tuple(range(1 << n))
    lines.append(f"SVT subsets Z_9 signature={functional_signature(states, lambda x: translate_mask(x, n, x.bit_count()))}")

    n = 6
    states = set_partitions(n)
    A.eq(len(states), 203, "Bell(6)")
    lines.append(f"BRT partitions n=6 signature={functional_signature(states, lambda P: rotate_partition(P, n))}")

    n = 6
    states = tuple(range(1 << comb(n, 2)))
    lines.append(f"EGR graphs n=6 signature={functional_signature(states, lambda x: relabel_graph(x, n))}")

    states = tuple(permutations(range(7)))
    lines.append(f"PFC permutations n=7 signature={functional_signature(states, permutation_fixed_conjugation)}")

    states = tuple(product(range(5), repeat=5))
    lines.append(f"EIC endofunctions n=5 signature={functional_signature(states, endofunction_image_conjugation)}")

    states = tuple(product((None, 0, 1), repeat=7))
    lines.append(f"PDR partial binary words n=7 signature={functional_signature(states, rotate_partial_word)}")

    states = partial_permutations(5)
    A.eq(len(states), 1546, "partial permutations n=5")
    lines.append(f"PCR partial permutations n=5 signature={functional_signature(states, conjugate_partial)}")

    states = tuple(product(range(5), repeat=5))
    lines.append(f"ISR q=5,n=5 signature={functional_signature(states, lambda w: inverse_support_rotation(w, 5))}")

    states = tuple(product((0, 1), repeat=9))
    sig = functional_signature(states, weight_complement_rotation)
    A.ok(all(iterate(weight_complement_rotation, w, 2) == w for w in states), "WCR involution")
    lines.append(f"WCR binary n=9 signature={sig}")

    states = tuple(range(1 << 9))
    lines.append(f"MRR binary 3x3 matrices signature={functional_signature(states, matrix_rank_rotation)}")

    states = tuple(product(range(4), repeat=6))
    lines.append(f"CLT q=4,n=6 signature={functional_signature(states, lambda w: colouring_translation(w, 4))}")
    return lines


# ---------------------------------------------------------------------------
# Endofunction/partial-function nonlinear controls (15--18).


def indegree_histogram(f):
    n = len(f)
    deg = Counter(f)
    return tuple(deg[i] % n for i in range(n))


def preimage_index_sum(f):
    n = len(f)
    out = [0] * n
    for i, y in enumerate(f):
        out[y] = (out[y] + i) % n
    return tuple(out)


def orbit_cycle_length(f, start):
    order = {}
    x = start
    while x not in order:
        order[x] = len(order)
        x = f[x]
    return len(order) - order[x]


def orbit_length_map(f):
    n = len(f)
    return tuple(orbit_cycle_length(f, i) % n for i in range(n))


def basin_size_map(f):
    n = len(f)
    adj = [set() for _ in range(n)]
    for i, y in enumerate(f):
        adj[i].add(y)
        adj[y].add(i)
    sizes = [0] * n
    unseen = set(range(n))
    while unseen:
        root = min(unseen)
        stack = [root]
        comp = set()
        while stack:
            x = stack.pop()
            if x in comp:
                continue
            comp.add(x)
            stack.extend(adj[x] - comp)
        unseen -= comp
        for x in comp:
            sizes[x] = len(comp) % n
    return tuple(sizes)


def probe_endofunctions():
    states = tuple(product(range(5), repeat=5))
    return [
        f"IDH n=5 signature={functional_signature(states, indegree_histogram)}",
        f"PIS n=5 signature={functional_signature(states, preimage_index_sum)}",
        f"OCL n=5 signature={functional_signature(states, orbit_length_map)}",
        f"BAS n=5 signature={functional_signature(states, basin_size_map)}",
    ]


# ---------------------------------------------------------------------------
# Adaptive automata/nonlinear-feedback controls (19--24).


def compose_left(g, f):
    return tuple(g[x] for x in f)


def rank_adaptive_composition(f):
    n = len(f)
    a = tuple((i + 1) % n for i in range(n))
    b = tuple(0 if i == n - 1 else i for i in range(n))
    return compose_left(a if len(set(f)) % 2 else b, f)


def image_mask(mask, trans, n):
    out = 0
    for i in range(n):
        if mask >> i & 1:
            out |= 1 << trans[i]
    return out


def cerny_greedy(mask, n):
    a = tuple((i + 1) % n for i in range(n))
    b = tuple(0 if i == n - 1 else i for i in range(n))
    bm = image_mask(mask, b, n)
    return bm if bm.bit_count() < mask.bit_count() else image_mask(mask, a, n)


def parity_adaptive_subset(mask, n):
    a = tuple((i + 1) % n for i in range(n))
    b = tuple(0 if i in (0, n - 1) else i for i in range(n))
    return image_mask(mask, a if mask.bit_count() % 2 else b, n)


def majority_feedback(w):
    bit = int(2 * sum(w) >= len(w))
    return w[1:] + (bit,)


def nand_feedback(w):
    bit = 1 - (w[0] & w[-1])
    return w[1:] + (bit,)


def adaptive_ca(w):
    n = len(w)
    if sum(w) % 2:
        return tuple(w[(i - 1) % n] | w[(i + 1) % n] for i in range(n))
    return tuple(w[(i - 1) % n] & w[(i + 1) % n] for i in range(n))


def probe_automata():
    lines = []
    states = tuple(product(range(5), repeat=5))
    lines.append(f"RAC n=5 signature={functional_signature(states, rank_adaptive_composition)}")

    n = 9
    states = tuple(range(1, 1 << n))
    lines.append(f"CNY subset n=9 signature={functional_signature(states, lambda x: cerny_greedy(x, n))}")
    lines.append(f"PAS subset n=9 signature={functional_signature(states, lambda x: parity_adaptive_subset(x, n))}")

    states = tuple(product((0, 1), repeat=10))
    lines.append(f"MFS binary n=10 signature={functional_signature(states, majority_feedback)}")
    lines.append(f"NFS binary n=10 signature={functional_signature(states, nand_feedback)}")

    states = tuple(product((0, 1), repeat=9))
    lines.append(f"ACA binary cycle n=9 signature={functional_signature(states, adaptive_ca)}")
    return lines


def main():
    lines = [probe_aqn()]
    lines.extend(probe_actions())
    lines.extend(probe_endofunctions())
    lines.extend(probe_automata())
    A.eq(len(lines), 26, "twenty-six literal systems")
    print("P162--P166 REPLACEMENT ADAPTIVE-MAPS SCOUT")
    for i, line in enumerate(lines, 1):
        print(f"{i:02d} {line}")
    print(f"ASSERTIONS {A.assertions}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
