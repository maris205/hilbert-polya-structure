#!/usr/bin/env python3
"""Exact small-box verifier for the P166 Round-5 sparse-carrier scout.

Seven maps on seven carrier classes are implemented from their literal
definitions.  The script is deterministic and imports no project verifier.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import permutations, product
from math import comb


ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def digest(rows):
    return sha256("\n".join(map(str, rows)).encode()).hexdigest()


def functional_shapes(states, step):
    memo = {}
    for start in states:
        if start in memo:
            continue
        path, seen = [], {}
        x = start
        while x not in memo and x not in seen:
            seen[x] = len(path)
            path.append(x)
            x = step(x)
        if x in memo:
            tail, period = memo[x]
            for y in reversed(path):
                tail += 1
                memo[y] = (tail, period)
        else:
            first = seen[x]
            period = len(path) - first
            for y in path[first:]:
                memo[y] = (0, period)
            tail = 0
            for y in reversed(path[:first]):
                tail += 1
                memo[y] = (tail, period)
    return memo


# ---------------------------------------------------------------------------
# XCT: translate a Boolean function's support by its XOR centroid.


def xor_centroid(s):
    out = 0
    x = s
    while x:
        bit = x & -x
        out ^= bit.bit_length() - 1
        x -= bit
    return out


def translate_support(s, a, q):
    out = 0
    for x in range(q):
        if (s >> x) & 1:
            out |= 1 << (x ^ a)
    return out


def xct_probe():
    rows, transitions = [], []
    for n in range(0, 5):
        q = 1 << n
        states = list(range(1 << q))

        def step(s):
            return translate_support(s, xor_centroid(s), q)

        source_map = defaultdict(set)
        for s in states:
            t = step(s)
            a = xor_centroid(s)
            expected_centroid = a if s.bit_count() % 2 == 0 else 0
            check(xor_centroid(t) == expected_centroid, f"XCT centroid n={n},s={s}")
            source_map[t].add(s)
            transitions.append((n, s, t))
        shapes = functional_shapes(states, step)
        fibre1 = Counter(step(s) for s in states)
        for target in states:
            k, a = target.bit_count(), xor_centroid(target)
            expected = 1 if k % 2 == 0 else (q if a == 0 else 0)
            check(fibre1[target] == expected, f"XCT one-fibre n={n},B={target}")
            if k % 2 == 0:
                predicted = {translate_support(target, a, q)}
            elif a == 0:
                predicted = {translate_support(target, v, q) for v in range(q)}
            else:
                predicted = set()
            actual = source_map[target]
            check(actual == predicted, f"XCT source set n={n},B={target}")
        for t in (1, 2, 3):
            counts = Counter()
            for s in states:
                y = s
                for _ in range(t):
                    y = step(y)
                counts[y] += 1
            check(counts == fibre1, f"XCT stable time fibres n={n},t={t}")

        # Weight-resolved XOR-sum census by character extraction.
        for k in range(q + 1):
            actual = Counter(xor_centroid(s) for s in states if s.bit_count() == k)
            if n == 0:
                check(actual[0] == comb(q, k), f"XCT n0 weight k={k}")
                continue
            beta = 0 if k % 2 else ((-1) ** (k // 2)) * comb(q // 2, k // 2)
            zero = (comb(q, k) + (q - 1) * beta) // q
            nonzero = (comb(q, k) - beta) // q
            check(actual[0] == zero, f"XCT zero-sum weight n={n},k={k}")
            check(all(actual[a] == nonzero for a in range(1, q)),
                  f"XCT nonzero-sum weight n={n},k={k}")

        if n == 0:
            expected_shapes = Counter({(0, 1): 2})
            image_size = 2
        else:
            fixed = (1 << (q - n)) + (q - 1) * (1 << (q // 2 - 1))
            tail = (q - 1) * (1 << (q - n - 1))
            cycle2 = (q - 1) * ((1 << (q - n - 1)) - (1 << (q // 2 - 1)))
            expected_shapes = Counter({(0, 1): fixed, (1, 1): tail})
            if cycle2:
                expected_shapes[(0, 2)] = cycle2
            image_size = (1 << (q - 1)) + (1 << (q - n - 1))
        check(Counter(shapes.values()) == expected_shapes, f"XCT shape census n={n}")
        check(len(fibre1) == image_size, f"XCT image size n={n}")
        rows.append((n, len(states), len(fibre1), tuple(sorted(expected_shapes.items())),
                     tuple(sorted(Counter(fibre1.values()).items()))))
    return rows, digest(transitions)


# ---------------------------------------------------------------------------
# BND: iterate the topological boundary of a marked subset.


def labelled_topologies(n):
    count_subsets = 1 << n
    if count_subsets == 1:
        return [1]
    mandatory = (1 << 0) | (1 << (count_subsets - 1))
    out = []
    for middle in range(1 << (count_subsets - 2)):
        family = mandatory | (middle << 1)
        opens = [a for a in range(count_subsets) if (family >> a) & 1]
        if all(((family >> (a | b)) & 1) and ((family >> (a & b)) & 1)
               for a in opens for b in opens):
            out.append(family)
    return out


def topo_closure(a, topology, n):
    full = (1 << n) - 1
    out = full
    for u in range(1 << n):
        if (topology >> u) & 1:
            closed = full ^ u
            if a & ~closed == 0:
                out &= closed
    return out


def topo_interior(a, topology, n):
    out = 0
    for u in range(1 << n):
        if (topology >> u) & 1 and u & ~a == 0:
            out |= u
    return out


def topo_boundary(a, topology, n):
    full = (1 << n) - 1
    return topo_closure(a, topology, n) & topo_closure(full ^ a, topology, n)


def bnd_probe():
    rows, transitions = [], []
    known = {0: 1, 1: 1, 2: 4, 3: 29, 4: 355}
    for n in range(0, 5):
        topologies = labelled_topologies(n)
        check(len(topologies) == known[n], f"BND topology census n={n}")
        aggregate_shapes = Counter()
        aggregate_fibres = Counter()
        fixed = 0
        max_fibre = 0
        for topology in topologies:
            states = list(range(1 << n))
            step = lambda a: topo_boundary(a, topology, n)
            shapes = functional_shapes(states, step)
            aggregate_shapes.update(shapes.values())
            fibres = Counter(step(a) for a in states)
            aggregate_fibres.update(fibres.values())
            max_fibre = max(max_fibre, max(fibres.values()))
            for a in states:
                b, c = step(a), step(step(a))
                check(step(c) == c, f"BND boundary cube n={n}")
                check(topo_closure(b, topology, n) == b, f"BND first closed n={n}")
                check(topo_interior(c, topology, n) == 0, f"BND second nowhere dense n={n}")
                fixed += (step(a) == a)
                transitions.append((n, topology, a, b))
        rows.append((n, len(topologies), len(topologies) * (1 << n), fixed,
                     max_fibre, tuple(sorted(aggregate_shapes.items())),
                     tuple(sorted(aggregate_fibres.items()))))
    return rows, digest(transitions)


# ---------------------------------------------------------------------------
# ZAT: zero-triggered arrow transport in a pointed A_2 representation.


def matvec(matrix, u, q, m, n):
    return tuple(sum(matrix[i * m + j] * u[j] for j in range(m)) % q
                 for i in range(n))


def zat_probe():
    boxes = [(2, 0, 2), (2, 2, 0), (2, 1, 2), (2, 2, 1),
             (2, 2, 2), (3, 1, 2), (3, 2, 2)]
    rows, transitions = [], []
    for q, m, n in boxes:
        matrices = list(product(range(q), repeat=m * n))
        us = list(product(range(q), repeat=m))
        vs = list(product(range(q), repeat=n))
        states = [(a, u, v) for a in matrices for u in us for v in vs]
        zero = (0,) * n

        def step(state):
            a, u, v = state
            au = matvec(a, u, q, m, n)
            return (a, u, au) if v == zero and au != zero else state

        fibres = Counter(step(s) for s in states)
        shapes = functional_shapes(states, step)
        for s in states:
            target = step(s)
            check(step(target) == target, f"ZAT idempotent qmn={q,m,n}")
            transitions.append((q, m, n, s, target))
        for target in states:
            a, u, v = target
            au = matvec(a, u, q, m, n)
            if v == zero:
                expected = 1 if au == zero else 0
            else:
                expected = 1 + int(au == v)
            check(fibres[target] == expected, f"ZAT fibre qmn={q,m,n}")
        rows.append(((q, m, n), len(states), len(fibres),
                     tuple(sorted(Counter(shapes.values()).items())),
                     tuple(sorted(Counter(fibres.values()).items()))))
    return rows, digest(transitions)


# ---------------------------------------------------------------------------
# EOD: exact-one incidence feedback in the complement-of-singletons design.


def eod_literal_step(s, v):
    full = (1 << v) - 1
    out = 0
    for x in range(v):
        block = full ^ (1 << x)
        if (block & s).bit_count() == 1:
            out |= 1 << x
    return out


def eod_formula_step(s, v):
    k = s.bit_count()
    if k == 1:
        return ((1 << v) - 1) ^ s
    if k == 2:
        return s
    return 0


def eod_probe():
    rows, transitions = [], []
    for v in range(2, 13):
        states = list(range(1 << v))
        step = lambda s: eod_literal_step(s, v)
        fibres = Counter(step(s) for s in states)
        shapes = functional_shapes(states, step)
        source_map = defaultdict(set)
        for s in states:
            check(step(s) == eod_formula_step(s, v), f"EOD literal formula v={v}")
            source_map[step(s)].add(s)
            transitions.append((v, s, step(s)))
        for target in states:
            predicted = set()
            if target == 0:
                predicted = {s for s in states if s.bit_count() not in (1, 2)}
            if target.bit_count() == 2:
                predicted.add(target)
            if target.bit_count() == v - 1:
                predicted.add(((1 << v) - 1) ^ target)
            actual = source_map[target]
            check(actual == predicted, f"EOD target sources v={v}")
        rows.append((v, len(states), len(fibres),
                     tuple(sorted(Counter(shapes.values()).items())),
                     tuple(sorted(Counter(fibres.values()).items()))))
    return rows, digest(transitions)


# ---------------------------------------------------------------------------
# NIM: canonical optimal move in capped two-pile Nim.


def nim_probe():
    rows, transitions = [], []
    for cap in range(0, 31):
        states = list(product(range(cap + 1), repeat=2))
        step = lambda p: (min(p), min(p))
        fibres = Counter(step(s) for s in states)
        shapes = functional_shapes(states, step)
        for s in states:
            check(step(step(s)) == step(s), f"NIM idempotent cap={cap}")
            transitions.append((cap, s, step(s)))
        for a, b in states:
            expected = 2 * (cap - a) + 1 if a == b else 0
            check(fibres[(a, b)] == expected, f"NIM fibre cap={cap},target={a,b}")
        if cap <= 10 or cap in (15, 20, 25, 30):
            rows.append((cap, len(states), len(fibres),
                         tuple(sorted(Counter(shapes.values()).items())),
                         max(fibres.values())))
    return rows, digest(transitions)


# ---------------------------------------------------------------------------
# GSR: global-sign reorientation of signed subsets.


def sign_product(s):
    out = 1
    for x in s:
        if x:
            out *= x
    return out


def gsr_probe():
    rows, transitions = [], []
    for n in range(0, 10):
        states = list(product((-1, 0, 1), repeat=n))

        def step(s):
            p = sign_product(s)
            return tuple(p * x for x in s)

        fibres = Counter(step(s) for s in states)
        shapes = functional_shapes(states, step)
        fixed = sum(sign_product(s) == 1 for s in states)
        tail = sum(sign_product(s) == -1 and sum(x != 0 for x in s) % 2 == 1
                   for s in states)
        period2 = len(states) - fixed - tail
        expected_shapes = Counter({(0, 1): fixed})
        if tail:
            expected_shapes[(1, 1)] = tail
        if period2:
            expected_shapes[(0, 2)] = period2
        check(Counter(shapes.values()) == expected_shapes, f"GSR shapes n={n}")
        for s in states:
            transitions.append((n, s, step(s)))
        for target in states:
            k, p = sum(x != 0 for x in target), sign_product(target)
            if k % 2 == 0:
                expected = 1
            else:
                expected = 2 if p == 1 else 0
            check(fibres[target] == expected, f"GSR fibre n={n}")
        for t in (1, 2, 3):
            counts = Counter()
            for s in states:
                y = s
                for _ in range(t):
                    y = step(y)
                counts[y] += 1
            check(counts == fibres, f"GSR stable time fibres n={n},t={t}")
        rows.append((n, len(states), len(fibres), tuple(sorted(expected_shapes.items())),
                     tuple(sorted(Counter(fibres.values()).items()))))
    return rows, digest(transitions)


# ---------------------------------------------------------------------------
# DLR: diagonal-controlled row action on labelled Latin squares.


def latin_squares(n):
    row_pool = list(permutations(range(n)))
    out = []

    def extend(rows):
        if len(rows) == n:
            out.append(tuple(rows))
            return
        for row in row_pool:
            if all(row[j] not in {old[j] for old in rows} for j in range(n)):
                extend(rows + [row])

    extend([])
    return out


def diagonal_row_step(square):
    n = len(square)
    diagonal = tuple(square[i][i] for i in range(n))
    if len(set(diagonal)) != n:
        return square
    return tuple(square[diagonal[i]] for i in range(n))


def is_latin(square):
    n = len(square)
    symbols = set(range(n))
    return (all(set(row) == symbols for row in square) and
            all({square[i][j] for i in range(n)} == symbols for j in range(n)))


def dlr_probe():
    known = {1: 1, 2: 2, 3: 12, 4: 576}
    rows, transitions = [], []
    for n in range(1, 5):
        states = latin_squares(n)
        check(len(states) == known[n], f"DLR Latin census n={n}")
        state_set = set(states)
        fibres = Counter(diagonal_row_step(s) for s in states)
        shapes = functional_shapes(states, diagonal_row_step)
        diagonal_permutations = 0
        for s in states:
            t = diagonal_row_step(s)
            check(t in state_set and is_latin(t), f"DLR closure n={n}")
            diagonal_permutations += (len({s[i][i] for i in range(n)}) == n)
            transitions.append((n, s, t))
        rows.append((n, len(states), diagonal_permutations, len(fibres),
                     tuple(sorted(Counter(shapes.values()).items())),
                     tuple(sorted(Counter(fibres.values()).items()))))
    return rows, digest(transitions)


def main():
    print("P166 ROUND5 SPARSE-CARRIER SCOUT — EXACT TRANSCRIPT")
    print("scope=7 literal systems / 7 carrier classes / HOLD_EXTERNAL")

    probes = [
        ("XCT Boolean support XOR-centroid translation", xct_probe),
        ("BND finite-topology boundary iteration", bnd_probe),
        ("ZAT pointed-quiver zero-triggered arrow transport", zat_probe),
        ("EOD complement-design exact-one feedback", eod_probe),
        ("NIM capped two-pile canonical optimal move", nim_probe),
        ("GSR signed-set global reorientation", gsr_probe),
        ("DLR Latin-square diagonal row feedback", dlr_probe),
    ]
    for title, probe in probes:
        rows, checksum = probe()
        print("\n[" + title + "]")
        for row in rows:
            print(row)
        print("transition_sha256=" + checksum)

    print("\nDECISIONS")
    print("XCT=KILL_INTERNAL_P162_TRANSLATION_STABILIZER_FIBRE_ENGINE")
    print("BND=KILL_STANDARD_BOUNDARY_OPERATOR_PLUS_NO_TARGET_ATLAS")
    print("ZAT=KILL_GUARDED_ONE_STEP_PROJECTION")
    print("EOD=KILL_TRIVIAL_DESIGN_PLUS_THRESHOLD_NETWORK_COLLISION")
    print("NIM=KILL_DIRECT_BOUTON_STRATEGY_PLUS_IDEMPOTENT_PROJECTION")
    print("GSR=KILL_THIN_STATE_DEPENDENT_CENTRAL_INVOLUTION")
    print("DLR=KILL_NO_ALL_PARAMETER_SPINE_PLUS_LATIN_ACTION_OWNER_DENSITY")
    print("ROUND5=KILL_ALL")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
