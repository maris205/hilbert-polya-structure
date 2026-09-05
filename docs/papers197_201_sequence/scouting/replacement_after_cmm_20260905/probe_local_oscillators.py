#!/usr/bin/env python3
"""Bounded three-rule finite-oscillator scouting, not a theorem verifier."""
from collections import Counter, deque
from itertools import product


def ordered_reset(x, q):
    return tuple((a+1) % q if a <= x[(i+1) % len(x)] else 0
                 for i, a in enumerate(x))


def agreement_reset(x, q):
    return tuple((a+1) % q if a == x[(i+1) % len(x)] else 0
                 for i, a in enumerate(x))


def disagreement_advance(x, q):
    return tuple((a+1) % q if a != x[(i+1) % len(x)] else a
                 for i, a in enumerate(x))


def box(step, q, n):
    states = list(product(range(q), repeat=n))
    index = {x:i for i,x in enumerate(states)}
    nxt = [index[step(x, q)] for x in states]
    fibre = Counter(nxt)
    degree = [fibre.get(i, 0) for i in range(len(states))]
    queue = deque(i for i,d in enumerate(degree) if d == 0)
    peeled = []
    while queue:
        i = queue.popleft()
        peeled.append(i)
        j = nxt[i]
        degree[j] -= 1
        if degree[j] == 0:
            queue.append(j)
    seen = set()
    periods = Counter()
    for i,d in enumerate(degree):
        if d and i not in seen:
            j = i
            cyc = []
            while j not in seen:
                seen.add(j)
                cyc.append(j)
                j = nxt[j]
            periods[len(cyc)] += 1
    depth = [0] * len(states)
    for i in reversed(peeled):
        depth[i] = depth[nxt[i]] + 1
    maxf = max(fibre.values())
    maxstates = [states[i] for i in range(len(states)) if fibre.get(i, 0) == maxf]
    # Independent generic local-constraint inverse on the smallest boxes.
    checks = 0
    if q**n <= 300:
        local = {(a,b):step((a,b), q)[0] for a in range(q) for b in range(q)}
        for y in states:
            sources = sum(all(local[x[i],x[(i+1)%n]] == y[i]
                              for i in range(n)) for x in states)
            assert sources == fibre.get(index[y], 0)
            checks += 1
    return (len(states), len(fibre), tuple(sorted(periods.items())),
            max(depth), maxf, len(maxstates), tuple(maxstates[:2]), checks)


def main():
    print("OSCILLATOR_SCOUT / BOUNDED_ONLY / NO_PROMOTION / HOLD_EXTERNAL")
    for name, step in (("OR", ordered_reset), ("AR", agreement_reset),
                       ("DA", disagreement_advance)):
        for q in (2,3,4,5):
            upper = {2:10,3:8,4:6,5:5}[q]
            for n in range(1,upper+1):
                print(name, "q=", q, "n=", n, box(step,q,n), flush=True)
    print("DONE / SCOUT_SIGNATURES_NOT_ALL_PARAMETER_THEOREMS")


if __name__ == "__main__":
    main()
