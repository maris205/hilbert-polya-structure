#!/usr/bin/env python3
"""Exact controls for odd-side least-neighbour walks on labelled trees."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import factorial


def prufer_trees(n: int):
    if n == 1:
        yield ((),)
        return
    for code in product(range(n), repeat=n - 2):
        degree = [1] * n
        for x in code:
            degree[x] += 1
        adj = [set() for _ in range(n)]
        for x in code:
            leaf = next(i for i, d in enumerate(degree) if d == 1)
            adj[leaf].add(x)
            adj[x].add(leaf)
            degree[leaf] -= 1
            degree[x] -= 1
        u, v = [i for i, d in enumerate(degree) if d == 1]
        adj[u].add(v)
        adj[v].add(u)
        yield tuple(tuple(sorted(a)) for a in adj)


def side_sizes(adj: tuple[tuple[int, ...], ...]) -> list[list[int]]:
    n = len(adj)
    out = [[0] * n for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            seen = {u}
            stack = [v]
            count = 0
            while stack:
                w = stack.pop()
                if w in seen:
                    continue
                seen.add(w)
                count += 1
                stack.extend(adj[w])
            out[u][v] = count
    return out


def root_map(adj, sides) -> tuple[int, ...]:
    return tuple(min((v for v in adj[u] if sides[u][v] % 2), default=u)
                 for u in range(len(adj)))


def orbit_data(f: tuple[int, ...], start: int) -> tuple[int, int]:
    seen: dict[int, int] = {}
    x = start
    while x not in seen:
        seen[x] = len(seen)
        x = f[x]
    return seen[x], len(seen) - seen[x]


def local_indegree(adj, sides, target: int) -> int:
    fixed = not any(sides[target][v] % 2 for v in adj[target])
    count = int(fixed)
    for u in adj[target]:
        if sides[u][target] % 2 == 0:
            continue
        eligible = [v for v in adj[u] if sides[u][v] % 2]
        count += target == min(eligible)
    return count


def add(a, b):
    n = max(len(a), len(b))
    return [(a[i] if i < len(a) else 0) +
            (b[i] if i < len(b) else 0) for i in range(n)]


def mul(a, b, nmax):
    out = [Fraction(0) for _ in range(nmax + 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= nmax:
                out[i + j] += x * y
    return out


def exp_series(f, nmax):
    out = [Fraction(0) for _ in range(nmax + 1)]
    out[0] = 1
    for n in range(1, nmax + 1):
        out[n] = sum(Fraction(k) * f[k] * out[n - k]
                     for k in range(1, n + 1)) / n
    return out


def egf_predictions(nmax: int):
    tree = [Fraction(0) for _ in range(nmax + 1)]
    for n in range(1, nmax + 1):
        tree[n] = Fraction(n ** (n - 1), factorial(n))
    even = [tree[n] if n % 2 == 0 else Fraction(0)
            for n in range(nmax + 1)]
    odd = [tree[n] if n % 2 else Fraction(0)
           for n in range(nmax + 1)]
    exp_even = exp_series(even, nmax)

    ratio = [Fraction(0) for _ in range(nmax + 1)]
    power = [Fraction(0) for _ in range(nmax + 1)]
    power[0] = 1
    for j in range(nmax + 1):
        ratio = add(ratio, [x / factorial(j + 1) for x in power])[:nmax + 1]
        power = mul(power, odd, nmax)
    w0 = mul(exp_even, ratio, nmax)
    w = [Fraction(0)] + w0[:-1]
    w_odd = [w[n] if n % 2 else Fraction(0) for n in range(nmax + 1)]
    recurrent_even = mul(w_odd, w_odd, nmax)
    fixed_odd = [Fraction(0)] + exp_even[:-1]
    return (
        [int(fixed_odd[n] * factorial(n)) for n in range(nmax + 1)],
        [int(recurrent_even[n] * factorial(n)) for n in range(nmax + 1)],
    )


def main() -> None:
    nmax = 8
    fixed_pred, recurrent_pred = egf_predictions(nmax)
    assertions = 0
    transitions = 0
    records: list[str] = []
    for n in range(1, nmax + 1):
        depths = Counter()
        periods = Counter()
        recurrent = 0
        max_fibre = 0
        tree_count = 0
        for adj in prufer_trees(n):
            tree_count += 1
            sides = side_sizes(adj)
            f = root_map(adj, sides)
            fibres = Counter(f)
            transitions += n
            if n % 2 == 0:
                assert all(sum(sides[u][v] % 2 for v in adj[u]) % 2 == 1
                           for u in range(n))
                assertions += n
            for r in range(n):
                depth, period = orbit_data(f, r)
                depths[depth] += 1
                periods[period] += 1
                recurrent += depth == 0
                assert fibres[r] == local_indegree(adj, sides, r)
                assertions += 1
                max_fibre = max(max_fibre, fibres[r])
        assert tree_count == (1 if n == 1 else n ** (n - 2))
        assertions += 1
        expected_tail = (n - 1) // 2
        assert max(depths) == expected_tail
        assertions += 1
        if n % 2:
            assert set(periods) == {1}
            assert recurrent == fixed_pred[n]
            assert max_fibre == (n + 1) // 2
        else:
            assert set(periods) == {2}
            assert recurrent == recurrent_pred[n]
            assert max_fibre == n - 1
        assertions += 3
        hist = ",".join(f"{d}:{depths[d]}" for d in sorted(depths))
        records.append(
            f"n={n} trees={tree_count} states={sum(depths.values())} "
            f"recurrent={recurrent} max_tail={max(depths)} "
            f"max_fibre={max_fibre} depth_hist={hist}"
        )
    digest = sha256("\n".join(records).encode()).hexdigest()
    print("odd-side least-neighbour tree controls")
    for line in records:
        print(line)
    print(f"transitions={transitions}")
    print(f"assertions={assertions}")
    print(f"record_digest={digest}")
    print("status=PASS")


if __name__ == "__main__":
    main()
