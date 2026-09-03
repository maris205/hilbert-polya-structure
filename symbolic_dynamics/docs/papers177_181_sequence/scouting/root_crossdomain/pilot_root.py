#!/usr/bin/env python3
"""Root-lane exact pilots for P177--P181 discovery.

The script intentionally explores literal maps before any paper allocation.
Enumeration is falsification pressure only.
"""

from collections import Counter, defaultdict
from itertools import permutations, product
from math import gcd


def functional_stats(states, step):
    nxt = {x: step(x) for x in states}
    periods = Counter()
    tails = Counter()
    fibres = Counter(nxt.values())
    for x in states:
        seen = {}
        y = x
        t = 0
        while y not in seen:
            seen[y] = t
            y = nxt[y]
            t += 1
        mu = seen[y]
        lam = t - mu
        periods[lam] += 1
        tails[mu] += 1
    return len(set(nxt.values())), max(fibres.values()), sorted(periods), max(tails)


def first_descent_prefix(pi):
    n = len(pi)
    for i in range(n - 1):
        if pi[i] > pi[i + 1]:
            return tuple(reversed(pi[: i + 2])) + pi[i + 2 :]
    return pi


def first_ascent_prefix(pi):
    n = len(pi)
    for i in range(n - 1):
        if pi[i] < pi[i + 1]:
            return tuple(reversed(pi[: i + 2])) + pi[i + 2 :]
    return pi


def max_displaced_prefix(pi):
    """Reverse through the position of the smallest misplaced value."""
    n = len(pi)
    for value in range(1, n + 1):
        if pi[value - 1] != value:
            j = pi.index(value)
            return tuple(reversed(pi[: j + 1])) + pi[j + 1 :]
    return pi


def descent_rotate(pi):
    """Rotate left through the first descent, or fix increasing word."""
    for i in range(len(pi) - 1):
        if pi[i] > pi[i + 1]:
            k = i + 1
            return pi[k:] + pi[:k]
    return pi


def divisor_core(N, d):
    return d // gcd(d, N // d)


def divisor_reflected_quotient(N, d):
    """Complementary quotient gcd(N/d, d) removed from N/d."""
    q = N // d
    return q // gcd(d, q)


def binary_run_boundary(w):
    """Mark cyclic positions whose bit differs from its predecessor."""
    n = len(w)
    return tuple(int(w[i] != w[i - 1]) for i in range(n))


def binary_isolated_flip(w):
    """Flip every bit whose two cyclic neighbours agree with each other."""
    n = len(w)
    return tuple(w[i] ^ int(w[i - 1] == w[(i + 1) % n]) for i in range(n))


def binary_majority_boundary(w):
    """Boundary of cyclic majority-smoothed word."""
    n = len(w)
    m = tuple(int(w[i - 1] + w[i] + w[(i + 1) % n] >= 2) for i in range(n))
    return tuple(int(m[i] != m[i - 1]) for i in range(n))


def rgs_partitions(n):
    """All set partitions as restricted-growth strings."""
    if n == 0:
        yield ()
        return
    def rec(prefix, top):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for x in range(top + 2):
            prefix.append(x)
            yield from rec(prefix, max(top, x))
            prefix.pop()
    yield from rec([0], 0)


def isolate_label(rgs, i):
    """Make label i a singleton and recanonicalise."""
    blocks = defaultdict(list)
    for j, b in enumerate(rgs):
        blocks[b].append(j)
    if len(blocks[rgs[i]]) == 1:
        return rgs
    pieces = [tuple(v) for v in blocks.values() if i not in v]
    old = tuple(j for j in blocks[rgs[i]] if j != i)
    pieces.append(old)
    pieces.append((i,))
    pieces.sort(key=min)
    out = [None] * len(rgs)
    for b, block in enumerate(pieces):
        for j in block:
            out[j] = b
    return tuple(out)


def singleton_count(rgs):
    c = Counter(rgs)
    return sum(v == 1 for v in c.values())


def block_count(rgs):
    return len(set(rgs))


def radial_dot_step(pair, q):
    """Phi(u,v)=(<u,v>u,<u,v>v) over the prime field F_q."""
    u, v = pair
    c = sum(a * b for a, b in zip(u, v)) % q
    return (tuple(c * a % q for a in u), tuple(c * b % q for b in v))


def main():
    print("PERMUTATION PILOTS")
    for name, step in [
        ("first-descent-prefix", first_descent_prefix),
        ("first-ascent-prefix", first_ascent_prefix),
        ("smallest-misplaced-prefix", max_displaced_prefix),
        ("first-descent-rotate", descent_rotate),
    ]:
        rows = []
        for n in range(2, 9):
            states = list(permutations(range(1, n + 1)))
            rows.append((n,) + functional_stats(states, step))
        print(name, rows)

    print("SET-PARTITION ISOLATION PILOT")
    for n in range(1, 9):
        states = list(rgs_partitions(n))
        incoming = Counter()
        formula_checks = 0
        diag = Counter()
        for x in states:
            diag[singleton_count(x)] += 1
            for i in range(n):
                y = isolate_label(x, i)
                incoming[y] += 1
        distinct_pred = defaultdict(set)
        for x in states:
            for i in range(n):
                distinct_pred[isolate_label(x, i)].add(x)
        for y in states:
            s = singleton_count(y)
            b = block_count(y)
            expected = 0 if s == 0 else 1 + s * (b - s) + s * (s - 1) // 2
            assert len(distinct_pred[y]) == expected
            assert incoming[y] == s * b
            formula_checks += 2
        print(n, len(states), sorted(diag.items()), max(map(len, distinct_pred.values())), formula_checks)

    print("DOT-RADIAL PILOT")
    for q in [2, 3, 5, 7, 11, 13]:
        for m in [1, 2]:
            vecs = list(product(range(q), repeat=m))
            states = [(u, v) for u in vecs for v in vecs]
            stats = functional_stats(states, lambda z, q=q: radial_dot_step(z, q))
            zero_fibre = sum(radial_dot_step(z, q) == ((0,) * m, (0,) * m) for z in states)
            predicted = q ** (2 * m - 1) + q**m - q ** (m - 1)
            print(q, m, stats, zero_fibre, predicted)

    print("DIVISOR PILOTS")
    for name, step in [
        ("core", divisor_core),
        ("reflected-quotient", divisor_reflected_quotient),
    ]:
        rows = []
        for N in [12, 24, 36, 48, 72, 120, 144, 360, 720]:
            states = [d for d in range(1, N + 1) if N % d == 0]
            rows.append((N,) + functional_stats(states, lambda d, N=N: step(N, d)))
        print(name, rows)

    print("BINARY CYCLIC PILOTS")
    for name, step in [
        ("run-boundary", binary_run_boundary),
        ("isolated-flip", binary_isolated_flip),
        ("majority-boundary", binary_majority_boundary),
    ]:
        rows = []
        for n in range(2, 13):
            states = list(product(range(2), repeat=n))
            rows.append((n,) + functional_stats(states, step))
        print(name, rows)

    print("release_sentinel=DISCOVERY_ONLY/HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
