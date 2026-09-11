#!/usr/bin/env python3
"""Bounded geometry scout, not a paper or selection verifier."""
from collections import Counter
from itertools import product

checks = 0


def require(test):
    global checks
    checks += 1
    if not test:
        raise AssertionError(checks)


def cross(u, v, p):
    return tuple((u[(i + 1) % 3] * v[(i + 2) % 3]
                  - u[(i + 2) % 3] * v[(i + 1) % 3]) % p for i in range(3))


def dot(u, v, p):
    return sum(a * b for a, b in zip(u, v)) % p


def graph(succ):
    tails, periods, cycles = {}, {}, Counter()
    for start in range(len(succ)):
        if start in tails:
            continue
        path, loc, x = [], {}, start
        while x not in tails and x not in loc:
            loc[x] = len(path)
            path.append(x)
            x = succ[x]
        if x not in tails:
            c = loc[x]
            period = len(path) - c
            cycles[period] += 1
            for y in path[c:]:
                tails[y], periods[y] = 0, period
            path = path[:c]
        for y in reversed(path):
            tails[y] = tails[succ[y]] + 1
            periods[y] = periods[succ[y]]
    return max(tails.values()), dict(sorted(cycles.items()))


def inverse(w, s, p):
    if not any(s):
        return {(u, tuple(-a % p for a in u)) for u in product(range(p), repeat=3)} if not any(w) else set()
    if dot(w, s, p):
        return set()
    k = next(i for i in range(3) if s[i])
    a, b = (k + 1) % 3, (k + 2) % 3
    reciprocal = pow(s[k], -1, p)
    out = set()
    for t in range(p):
        u = [0, 0, 0]
        u[k] = t
        u[a] = (t * s[a] - w[b]) * reciprocal % p
        u[b] = (w[a] + t * s[b]) * reciprocal % p
        v = tuple((s[i] - u[i]) % p for i in range(3))
        out.add((tuple(u), v))
    return out


def main():
    print("CROSS_SUM_GEOMETRY_SCOUT_NOT_PROMOTED")
    for p in (3, 5, 7):
        vectors = list(product(range(p), repeat=3))
        states = list(product(vectors, repeat=2))
        ids = {x: i for i, x in enumerate(states)}
        pred = [[] for _ in states]
        succ = []
        for i, (u, v) in enumerate(states):
            w, s = cross(u, v, p), tuple((a + b) % p for a, b in zip(u, v))
            succ.append(ids[w, s])
            pred[ids[w, s]].append(i)
            require(dot(w, s, p) == 0)
            a, b, c = dot(u, u, p), dot(v, v, p), dot(u, v, p)
            require(dot(w, w, p) == (a * b - c * c) % p)
            require(dot(s, s, p) == (a + b + 2 * c) % p)
        for i, (w, s) in enumerate(states):
            recovered = inverse(w, s, p)
            require(recovered == {states[j] for j in pred[i]})
            expected = (p ** 3 if not any(w) else 0) if not any(s) else (p if dot(w, s, p) == 0 else 0)
            require(len(pred[i]) == expected)
        image = sum(bool(x) for x in pred)
        require(image == (p ** 3 - 1) * p ** 2 + 1)
        require(max(map(len, pred)) == p ** 3)
        require(sum(len(x) == p ** 3 for x in pred) == 1)
        height, cycles = graph(succ)
        norms = list(product(range(p), repeat=2))
        ni = {x: i for i, x in enumerate(norms)}
        sh, sc = graph([ni[(a * b) % p, (a + b) % p] for a, b in norms])
        print(f"p={p} states={len(states)} image={image} max_fibre={p**3} max_targets=1 tail={height} cycles={cycles} norm_tail={sh} norm_cycles={sc}")
    print(f"assertions={checks}")
    print("status=PASS_BOUNDED_INVERSE_ONLY")
    print("disposition=KILL_NO_ALL_PARAMETER_TEMPORAL_SPINE")


if __name__ == "__main__":
    main()
