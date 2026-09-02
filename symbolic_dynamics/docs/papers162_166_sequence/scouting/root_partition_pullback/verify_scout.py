#!/usr/bin/env python3
"""Exact scout for endpoint-duplicating pullback dynamics on set partitions.

The verifier enumerates every set partition through n=8.  It compares the
literal pullback map with its closed iterate, checks the complete depth and
image laws, and checks every coefficient of the two-variable every-target
fibre polynomial.  Enumeration is counterexample pressure, not proof.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
from math import comb


ASSERTIONS = 0


def require(condition: bool, witness: object) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(witness)


@lru_cache(maxsize=None)
def partitions(n: int) -> tuple[tuple[int, ...], ...]:
    """Restricted-growth encodings of Pi_n."""
    if n == 0:
        return ((),)
    out: list[tuple[int, ...]] = []

    def rec(word: list[int]) -> None:
        if len(word) == n:
            out.append(tuple(word))
            return
        ceiling = 0 if not word else max(word) + 1
        for value in range(ceiling + 1):
            word.append(value)
            rec(word)
            word.pop()

    rec([0])
    return tuple(out)


def canonical(word: tuple[int, ...]) -> tuple[int, ...]:
    relabel: dict[int, int] = {}
    out: list[int] = []
    for value in word:
        if value not in relabel:
            relabel[value] = len(relabel)
        out.append(relabel[value])
    return tuple(out)


def step(pi: tuple[int, ...]) -> tuple[int, ...]:
    if len(pi) <= 1:
        return pi
    return canonical(tuple(pi[max(0, i - 1)] for i in range(len(pi))))


def closed(pi: tuple[int, ...], t: int) -> tuple[int, ...]:
    n = len(pi)
    if n <= 1:
        return pi
    h = min(t, n - 1)
    return canonical(tuple(pi[max(0, i - h)] for i in range(n)))


def iterate(pi: tuple[int, ...], t: int) -> tuple[int, ...]:
    cur = pi
    for _ in range(t):
        cur = step(cur)
    return cur


def blocks(pi: tuple[int, ...]) -> int:
    return 0 if not pi else max(pi) + 1


def root_size(pi: tuple[int, ...]) -> int:
    return 0 if not pi else sum(x == pi[0] for x in pi)


@lru_cache(maxsize=None)
def stirling2(n: int, k: int) -> int:
    if n == k == 0:
        return 1
    if n == 0 or k == 0 or k > n:
        return 0
    return stirling2(n - 1, k - 1) + k * stirling2(n - 1, k)


@lru_cache(maxsize=None)
def bell(n: int) -> int:
    return sum(stirling2(n, k) for k in range(n + 1))


def predicted_fibre(
    eta: tuple[int, ...], t: int
) -> Counter[tuple[int, int]]:
    """Coefficient dictionary in z^(number blocks) u^(root-block size)."""
    n = len(eta)
    h = min(t, max(0, n - 1))
    if any(eta[i] != eta[0] for i in range(h + 1)):
        return Counter()
    b = blocks(eta)
    a = root_size(eta) - h
    if a < 1:
        return Counter()
    ans: Counter[tuple[int, int]] = Counter()
    for j in range(h + 1):
        choose_new_only = comb(h, j)
        for k in range(j + 1):
            s = stirling2(j, k)
            if not s:
                continue
            attached = h - j
            for r in range(attached + 1):
                ways = (
                    choose_new_only
                    * s
                    * comb(attached, r)
                    * (b - 1) ** (attached - r)
                )
                if ways:
                    ans[(b + k, a + r)] += ways
    return ans


def point_depth(pi: tuple[int, ...]) -> int:
    n = len(pi)
    if n <= 1 or blocks(pi) == 1:
        return 0
    m = 1
    while m < n and pi[m] == pi[0]:
        m += 1
    return n - m


def main() -> None:
    rows: list[str] = []
    grand_states = 0
    for n in range(1, 9):
        states = partitions(n)
        grand_states += len(states)
        require(len(states) == bell(n), ("Bell census", n))

        depths = Counter(point_depth(pi) for pi in states)
        expected_depths = Counter({0: 1})
        for t in range(1, n):
            expected_depths[t] = bell(t + 1) - bell(t)
        require(depths == expected_depths, ("depth histogram", n, depths))
        require(max(depths) == max(0, n - 1), ("sharp height", n))

        for pi in states:
            d = point_depth(pi)
            require(closed(pi, d) == (0,) * n, ("depth hits", n, pi))
            if d:
                require(closed(pi, d - 1) != (0,) * n, ("depth sharp", n, pi))
            require(step(pi) == closed(pi, 1), ("one step", n, pi))
            require(step(pi) == pi if d == 0 else step(pi) != pi,
                    ("fixed iff universal", n, pi))

        image_sizes: list[int] = []
        max_fibre = 0
        for t in range(n + 2):
            h = min(t, n - 1)
            actual: dict[tuple[int, ...], Counter[tuple[int, int]]] = defaultdict(Counter)
            for pi in states:
                eta = iterate(pi, t)
                require(eta == closed(pi, t), ("iterate", n, t, pi))
                actual[eta][(blocks(pi), root_size(pi))] += 1

            require(len(actual) == bell(n - h), ("image size", n, t))
            image_sizes.append(len(actual))
            for eta in states:
                predicted = predicted_fibre(eta, t)
                observed = actual.get(eta, Counter())
                require(observed == predicted, ("weighted fibre", n, t, eta,
                                                 observed, predicted))
                require(bool(observed) == all(eta[i] == eta[0]
                                              for i in range(h + 1)),
                        ("image criterion", n, t, eta))
                if observed:
                    b = blocks(eta)
                    rbell = sum(comb(h, j) * (b ** (h - j)) * bell(j)
                                for j in range(h + 1))
                    require(sum(observed.values()) == rbell,
                            ("unweighted r-Bell", n, t, eta))
                    max_fibre = max(max_fibre, rbell)

        rows.append(
            f"n={n}|states={len(states)}|height={max(depths)}|"
            f"depths={','.join(f'{k}:{depths[k]}' for k in sorted(depths))}|"
            f"images={','.join(map(str, image_sizes))}|max_fibre={max_fibre}"
        )

    print("ENDPOINT_DUPLICATING_PARTITION_PULLBACK_SCOUT_V1")
    print(f"boxes=8 states={grand_states}")
    for row in rows:
        print(row)
    print(f"assertions={ASSERTIONS}")
    print("DECISION GREEN_PENDING_INDEPENDENT_HOSTILE_GATE")
    print("EXTERNAL HOLD_EXTERNAL")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
