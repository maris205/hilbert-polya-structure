#!/usr/bin/env python3
"""Independent LZK gate: edge-union components and invariant-skeleton blocks.

No author or historical implementation is imported. Exact finite tests support
the deductive reduction in PROOF_AND_COLLISION.md; they are not the proof.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, product
from math import comb, factorial

ASSERTIONS = 0


def check(ok, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not ok:
        raise AssertionError(label)


def states(r, s, q):
    for left in product(range(q), repeat=r):
        allowed = tuple(c for c in range(q) if c not in left)
        for right in product(allowed, repeat=s):
            yield left + right


def literal(x, r):
    if 0 not in x:
        return x
    parent = list(range(len(x)))

    def root(i):
        while parent[i] != i:
            i = parent[i]
        return i

    for i in range(r):
        for j in range(r, len(x)):
            if x[i] in (0, 1) and x[j] in (0, 1):
                parent[root(i)] = root(j)
    component = root(x.index(0))
    return tuple(1 - c if root(i) == component else c
                 for i, c in enumerate(x))


def skeleton(x):
    return tuple(-1 if c < 2 else c for c in x)


def bit_coordinate(x):
    active = [i for i, c in enumerate(x) if c < 2]
    return sum(1 << j for j, i in enumerate(active) if x[i] == 0)


@lru_cache(None)
def onto(n, k):
    # Recurrence, independent of author's inclusion-exclusion implementation.
    if n == 0:
        return int(k == 0)
    if k == 0 or k > n:
        return 0
    return k * (onto(n - 1, k) + onto(n - 1, k - 1))


@lru_cache(None)
def chi(r, s, k):
    if r == 0:
        return k ** s
    return sum(comb(k, a) * onto(r, a) * (k - a) ** s
               for a in range(min(r, k) + 1))


def multinomial(k, a, b):
    return comb(k, a) * comb(k - a, b)


def contract_cycles(r, s, q):
    return sum(multinomial(q - 2, a, b) * onto(r, a + 1) * onto(s, b + 1)
               for a in range(q - 1) for b in range(q - 1 - a))


def contract_depth(u, v, q, d):
    if d > u:
        return 0
    return comb(u, d) * sum(multinomial(q - 2, a, b)
                            * (onto(u - d, a) + onto(u - d, a + 1))
                            * onto(v, b)
                            for a in range(q - 1)
                            for b in range(q - 1 - a))


def predicted_sources(y, r, t):
    zero = [i for i, c in enumerate(y) if c == 0]
    one = [i for i, c in enumerate(y) if c == 1]
    if zero and one and ((zero[0] < r) != (one[0] < r)):
        z = tuple(1 - c if c < 2 else c for c in y) if t % 2 else y
        return {z}
    if zero:
        eligible = [i for i in one if i < zero[0] and ((i < r) == (zero[0] < r))]
        choices = combinations(eligible, t)
    else:
        choices = (v for j in range(min(t, len(one)) + 1)
                   for v in combinations(one, j))
    ans = set()
    for chosen in choices:
        x = list(y)
        for i in chosen:
            x[i] = 0
        ans.add(tuple(x))
    return ans


def audit(r, s, q):
    xx = list(states(r, s, q))
    index = {x: i for i, x in enumerate(xx)}
    ff = []
    groups = defaultdict(list)
    for i, x in enumerate(xx):
        y = literal(x, r)
        check(y in index, "proper closure")
        check(skeleton(y) == skeleton(x), "invariant frozen skeleton")
        ff.append(index[y])
        groups[skeleton(x)].append(i)
    rank_blocks = Counter()
    swap_blocks = 0
    for sk, indices in groups.items():
        active = [i for i, c in enumerate(sk) if c == -1]
        crosses = any(i < r for i in active) and any(i >= r for i in active)
        if crosses:
            check(len(indices) == 2, "crossing skeleton has exactly two states")
            a, b = indices
            check(ff[a] == b and ff[b] == a, "crossing block strict two-cycle")
            swap_blocks += 1
        else:
            m = len(active)
            rank_blocks[m] += 1
            check(len(indices) == 2 ** m, "one-side skeleton full Boolean carrier")
            check({bit_coordinate(xx[i]) for i in indices} == set(range(2 ** m)),
                  "coordinate bijection onto binary rank-m carrier")
            for i in indices:
                b = bit_coordinate(xx[i])
                check(bit_coordinate(xx[ff[i]]) == b & (b - 1),
                      "exact P100 binary conjugacy")
    k = q - 2
    expected_ranks = {0: chi(r, s, k)}
    for m in range(1, max(r, s) + 1):
        expected_ranks[m] = ((comb(r, m) * chi(r - m, s, k) if m <= r else 0)
                             + (comb(s, m) * chi(r, s - m, k) if m <= s else 0))
    for m, n in expected_ranks.items():
        check(rank_blocks[m] == n, "exact Boolean-block multiplicity")
    expected_swap = sum(comb(r, a) * comb(s, b) * chi(r - a, s - b, k)
                        for a in range(1, r + 1) for b in range(1, s + 1))
    check(swap_blocks == expected_swap == contract_cycles(r, s, q),
          "two-cycle census three routes")
    check(len(xx) == chi(r, s, q), "total chromatic census")
    depth_hist = Counter()
    periods = Counter()
    for i, x in enumerate(xx):
        seen = {}
        at = i
        while at not in seen:
            seen[at] = len(seen)
            at = ff[at]
        tail, period = seen[at], len(seen) - seen[at]
        depth_hist[tail] += 1
        periods[period] += 1
        zero = [j for j, c in enumerate(x) if c == 0]
        one = [j for j, c in enumerate(x) if c == 1]
        opposite = zero and one and ((zero[0] < r) != (one[0] < r))
        check((tail, period) == ((0, 2) if opposite else (len(zero), 1)),
              "pointwise clock and period")
    for d in range(max(r, s) + 1):
        by_blocks = sum(n * comb(m, d) for m, n in rank_blocks.items() if d <= m)
        by_blocks += 2 * swap_blocks if d == 0 else 0
        check(depth_hist[d] == by_blocks, "binomial-block depth polynomial")
        if d:
            check(depth_hist[d] == contract_depth(r, s, q, d)
                  + contract_depth(s, r, q, d), "author support/onto depth formula")
    fixed = sum(i == j for i, j in enumerate(ff))
    check(fixed == sum(rank_blocks.values()) == chi(r, s, q - 1), "fixed census")
    current = list(range(len(xx)))
    for t in range(max(r, s) + 3):
        actual = defaultdict(set)
        for i, j in enumerate(current):
            actual[j].add(xx[i])
        for j, y in enumerate(xx):
            check(actual[j] == predicted_sources(y, r, t), "all-time exact source sets")
        check(sum(map(len, actual.values())) == len(xx), "inverse mass")
        current = [ff[j] for j in current]
    fibre = Counter(ff)
    max_fibre = max(fibre.values())
    expected_image = rank_blocks[0] + sum(n * 2 ** (m - 1)
                         for m, n in rank_blocks.items() if m) + 2 * swap_blocks
    check(len(fibre) == expected_image, "image block census")
    for i, y in enumerate(xx):
        if q >= 3:
            equality = 0 not in y and y.count(1) == max(r, s)
            check((fibre[i] == max_fibre) == equality, "all maximum-fibre equality states")
    if q == 2:
        check(len(xx) == 2 and fixed == 0 and swap_blocks == 1 and max(depth_hist) == 0,
              "q=2 exact boundary")
        check(max_fibre == 1, "q=2 all fibres one")
    else:
        check(max(depth_hist) == max(r, s), "sharp tail")
        check(max_fibre == max(r, s) + 1, "sharp fibre")
        expected_maximizers = ((q - 2) ** min(r, s)) * (2 if r == s else 1)
        check(sum(v == max_fibre for v in fibre.values()) == expected_maximizers,
              "maximum-fibre equality census")
    print(f"q={q} r={r} s={s} states={len(xx)} image={len(fibre)} fixed={fixed} "
          f"two_cycles={swap_blocks} max_tail={max(depth_hist)} max_fibre={max_fibre} "
          f"Boolean_blocks={dict(sorted(rank_blocks.items()))}")


def main():
    print("LZK independent Stage-1 gate: invariant skeleton / union-find / P100 conjugacy")
    boxes = [(r, s, 2) for r, s in [(1, 1), (1, 5), (5, 1), (3, 4), (4, 3)]]
    boxes += [(r, s, 3) for r, s in [(1, 1), (1, 5), (5, 1), (2, 2), (3, 4), (4, 3), (5, 5)]]
    boxes += [(r, s, 4) for r, s in [(1, 4), (4, 1), (3, 4), (4, 3), (4, 4)]]
    boxes += [(r, s, 5) for r, s in [(3, 4), (4, 3), (4, 4)]]
    for r, s, q in boxes:
        audit(r, s, q)
    print(f"PASS boxes={len(boxes)} assertions={ASSERTIONS}")
    print("Gate disposition: KILL_COMPONENTWISE_P100_HF1_ERASURE / HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
