#!/usr/bin/env python3
"""Exact period-feedback author verifier, with independent orbit controls."""
from collections import Counter, deque
from functools import lru_cache
from itertools import product
from math import comb, factorial, prod

checks = 0


def check(condition):
    global checks
    checks += 1
    assert condition, checks


def period_feedback(f):
    n = len(f)
    indegree = [0] * n
    for j in f:
        indegree[j] += 1
    queue = deque(i for i in range(n) if not indegree[i])
    peeled = []
    while queue:
        i = queue.popleft()
        peeled.append(i)
        j = f[i]
        indegree[j] -= 1
        if not indegree[j]:
            queue.append(j)
    out = [-1] * n
    for i in range(n):
        if not indegree[i] or out[i] >= 0:
            continue
        cycle = [i]
        j = f[i]
        while j != i:
            cycle.append(j)
            j = f[j]
        for j in cycle:
            out[j] = len(cycle) - 1
    for i in reversed(peeled):
        out[i] = out[f[i]]
    return tuple(out)


def orbit_control(f):
    result = []
    for start in range(len(f)):
        visited = {}
        i = start
        while i not in visited:
            visited[i] = len(visited)
            i = f[i]
        result.append(len(visited) - visited[i] - 1)
    return tuple(result)


@lru_cache(None)
def height(f):
    if not any(f):
        return 0
    return 1 + height(period_feedback(f))


def thresholds(h):
    n = 2
    for _ in range(2, h):
        n = n * (n + 1) // 2
    return n


def max_height(n):
    if n == 1:
        return 0
    h = 2
    while thresholds(h + 1) <= n:
        h += 1
    return h


@lru_cache(None)
def restricted_count(d, k):
    if not k:
        return 1
    total = 0
    for c in range(1, k // d + 1):
        m = d * c
        cyclic = factorial(m) // (d**c * factorial(c))
        rooted = 1 if m == k else m * k ** (k - m - 1)
        total += comb(k, m) * cyclic * rooted
    return total


def fibre_formula(g):
    return prod(restricted_count(j + 1, k) for j, k in Counter(g).items())


def image_test(g):
    return all(k >= j + 1 for j, k in Counter(g).items())


def image_count(n):
    coefficients = [0] * (n + 1)
    coefficients[0] = 1
    for d in range(1, n + 1):
        updated = coefficients.copy()
        for old in range(n + 1):
            for k in range(d, n - old + 1):
                updated[old + k] += coefficients[old] * comb(old + k, k)
        coefficients = updated
    return coefficients[n]


def critical_count(h):
    answer = 1
    for level in range(3, h + 1):
        answer *= factorial(thresholds(level) - thresholds(level - 1))
    return answer


def critical_witness(h):
    f = (1, 0)
    for level in range(3, h + 1):
        k = len(f)
        n = thresholds(level)
        inverse = [0] * k
        for i, j in enumerate(f):
            inverse[j] = i
        result = [-1] * n
        next_label = k
        for j in range(k):
            block = [inverse[j]] + list(range(next_label, next_label + j))
            next_label += j
            for a, b in zip(block, block[1:] + block[:1]):
                result[a] = b
        check(next_label == n)
        check(sorted(result) == list(range(n)))
        check(period_feedback(tuple(result))[:k] == f)
        f = tuple(result)
    return f


def main():
    for n in range(1, 8):
        fibres = Counter()
        depths = Counter()
        rank_heights = {}
        for index, f in enumerate(product(range(n), repeat=n)):
            g = period_feedback(f)
            if n <= 6 or index < 256:
                check(g == orbit_control(f))
            r, s = len(set(f)), len(set(g))
            check(r >= s * (s + 1) // 2)
            h = 0 if not any(f) else 1 + height(g)
            check(h <= max_height(n))
            if h >= 2:
                check(r >= thresholds(h))
            check(image_test(g))
            depths[h] += 1
            rank_heights[r] = max(rank_heights.get(r, 0), h)
            fibres[g] += 1
        check(max(depths) == max_height(n))
        check(depths[0] == 1)
        check(len(fibres) == image_count(n))
        check(max(fibres.values()) == (n + 1) ** (n - 1))
        check([g for g, mass in fibres.items()
               if mass == max(fibres.values())] == [(0,) * n])
        for r, h in rank_heights.items():
            check(h == (max_height(r) if r >= 2 else int(n >= 2)))
        for g, actual in fibres.items():
            check(actual == fibre_formula(g))
        if n <= 6:
            for g in product(range(n), repeat=n):
                check((g in fibres) == image_test(g))
                check(fibres[g] == fibre_formula(g))
        if n in (2, 3, 6):
            check(depths[max_height(n)] == critical_count(max_height(n)))
        print(f"n={n} states={n**n} image={len(fibres)} "
              f"height={max(depths)} depths={dict(sorted(depths.items()))} "
              f"max_fibre={max(fibres.values())}", flush=True)
        height.cache_clear()

    for h in range(2, 8):
        f = critical_witness(h)
        check(len(f) == thresholds(h))
        check(height(f) == h)
        profile = []
        x = f
        while any(x):
            profile.append(len(set(x)))
            x = period_feedback(x)
        profile.append(1)
        print(f"witness height={h} n={len(f)} rank_profile={profile}", flush=True)
        for extra in (1, 3, 11):
            padded = f + (0,) * extra
            check(height(padded) == h)
            check(len(set(padded)) == len(f))
        height.cache_clear()

    check(period_feedback((0, 1, 1)) == (0, 0, 0))
    check(period_feedback((1, 0, 1)) == (1, 1, 1))
    check(Counter((0, 1, 1)) == Counter((1, 0, 1)))
    print(f"ASSERTIONS={checks}")
    print("PASS / PROVISIONAL_THEOREM_SPIKE / HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
