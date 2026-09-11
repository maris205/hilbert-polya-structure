#!/usr/bin/env python3
"""P198 paper-local exact verifier; bounded checks do not replace proofs."""
from collections import Counter, deque
from math import comb

checks = 0


def check(condition):
    global checks
    checks += 1
    assert condition, checks


def matchings(n):
    return [x for x in range(1 << n)
            if not x & (x << 1) and not (x & 1 and x & (1 << (n - 1)))]


def holes(n, mask):
    return tuple(i for i in range(n)
                 if not mask & (1 << i) and not mask & (1 << ((i - 1) % n)))


def step(n, mask):
    unmatched = holes(n, mask)
    a = unmatched[0]
    if len(unmatched) == 1:
        return mask ^ (1 << a) ^ (1 << ((a + 1) % n))
    b = unmatched[1]
    return mask ^ (((1 << (b - a)) - 1) << a)


def inverse_sources(n, target):
    """Endpoint-set reconstruction, without the fibre-count formula."""
    u = holes(n, target)[0]
    sources = set()
    for a in range(u):
        for b in range(a + 1, u):
            arc = ((1 << (b - a)) - 1) << a
            candidate = target ^ arc
            if not candidate & (candidate << 1) and not (
                    candidate & 1 and candidate & (1 << (n - 1))):
                if holes(n, candidate)[:2] == (a, b):
                    sources.add(candidate)
    if len(holes(n, target)) == 1:
        a = (u - 2) % n
        sources.add(target ^ (1 << a) ^ (1 << ((a + 1) % n)))
    return sources


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    print("P198_CYCLIC_MONOMER_MATCHING")
    for n in range(3, 22, 2):
        m = (n - 1) // 2
        states = matchings(n)
        state_set = set(states)
        nxt = {x: step(n, x) for x in states}
        predecessors = {y: set() for y in states}
        for x, y in nxt.items():
            check(y in state_set)
            predecessors[y].add(x)
            check(y.bit_count() == x.bit_count() + (x.bit_count() < m))
        indegree = {x: len(predecessors[x]) for x in states}
        queue = deque(x for x in states if not indegree[x])
        peeled = []
        while queue:
            x = queue.popleft()
            peeled.append(x)
            y = nxt[x]
            indegree[y] -= 1
            if not indegree[y]:
                queue.append(y)
        recurrent = {x for x in states if indegree[x]}
        check(len(recurrent) == n)
        start = next(iter(recurrent))
        cycle, x = set(), start
        while x not in cycle:
            cycle.add(x)
            x = nxt[x]
        check(x == start and cycle == recurrent)
        depths = {x: 0 for x in recurrent}
        for x in reversed(peeled):
            depths[x] = depths[nxt[x]] + 1
        for y in states:
            u = holes(n, y)[0]
            r = u // 2
            check(depths[y] == m - y.bit_count())
            check(predecessors[y] == inverse_sources(n, y))
            check(len(predecessors[y]) == r * (r + 1) // 2 + (y.bit_count() == m))
            check(bool(predecessors[y]) == (u >= 2 or y.bit_count() == m))
            if y in recurrent:
                check(holes(n, nxt[y]) == ((u + 2) % n,))
        layers = Counter(depths.values())
        for r in range(m + 1):
            check(layers[m - r] == n * comb(n - r, r) // (n - r))
        image = sum(bool(v) for v in predecessors.values())
        check(image == fib(n - 1) + fib(n - 3) + 2)
        maximum = max(map(len, predecessors.values()))
        check(maximum == 1 + m * (m + 1) // 2)
        check([holes(n, y) for y in states if len(predecessors[y]) == maximum] == [(n - 1,)])
        check([x for x in states if depths[x] == m] == [0])
        print(f"n={n} states={len(states)} image={image} recurrent={n} "
              f"max_tail={m} max_fibre={maximum}", flush=True)
    print(f"ASSERTIONS={checks}")
    print("PASS / ROUND0_AUTHOR_CHECK / HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
