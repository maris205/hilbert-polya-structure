#!/usr/bin/env python3
"""Author bounded pilot. No imports from an earlier scientific producer."""
import hashlib
import itertools as it
import json
from collections import Counter
from functools import lru_cache

CHECKS = 0


def require(condition):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(CHECKS)


def det2(u, v):
    return u[0]*v[1]-u[1]*v[0]


def points_rule(state, p, rule):
    pts = tuple(zip(state[::2], state[1::2]))
    n = len(pts)
    result = []
    for i, v in enumerate(pts):
        after, before = pts[(i+1) % n], pts[(i-1) % n]
        u = (after[0]-v[0], after[1]-v[1])
        w = (before[0]-v[0], before[1]-v[1])
        if rule == "QAS":
            f = det2(u, w)
            result.extend((v[j]+f*(u[j]+w[j])) % p for j in range(2))
        else:
            f = sum(u[j]*w[j] for j in range(2))
            result.extend((v[j]+f*(u[j]-w[j])) % p for j in range(2))
    return tuple(result)


@lru_cache(None)
def triangulations(vertices):
    if len(vertices) <= 3:
        return ((),)
    out = set()
    a, b = vertices[0], vertices[-1]
    for k in range(1, len(vertices)-1):
        c = vertices[k]
        add = []
        if k > 1:
            add.append((a, c))
        if k < len(vertices)-2:
            add.append((c, b))
        for left in triangulations(vertices[:k+1]):
            for right in triangulations(vertices[k:]):
                out.add(tuple(sorted(left+right+tuple(add))))
    return tuple(sorted(out))


def ofs(state, n):
    current = set(state)
    boundary = {(i, i+1) for i in range(n-1)} | {(0, n-1)}
    for a, b in state:
        if (a, b) not in current:
            continue
        edges = current | boundary
        common = [v for v in range(n) if v not in (a, b)
                  and tuple(sorted((a, v))) in edges
                  and tuple(sorted((b, v))) in edges]
        require(len(common) == 2)
        current.remove((a, b))
        current.add(tuple(sorted(common)))
    return tuple(sorted(current))


def sbf(state, p):
    x, y = state
    return (x*(1-y) % p, x*y % p)


def hgf(state, p):
    s = sum(x*x for x in state)
    return tuple(x*(s-2*x*x) % p for x in state)


def matrix(state):
    a, b, c, d, e, f = state
    return ((a, b, c), (b, d, e), (c, e, f))


def matrix_rank(state, p):
    a = [list(row) for row in matrix(state)]
    r = 0
    for j in range(3):
        pivot = next((k for k in range(r, 3) if a[k][j] % p), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = pow(a[r][j], -1, p)
        a[r] = [x*q % p for x in a[r]]
        for k in range(3):
            if k != r:
                c = a[k][j]
                a[k] = [(a[k][h]-c*a[r][h]) % p for h in range(3)]
        r += 1
    return r


def adjugate(state, p):
    a = matrix(state)
    out = []
    for i, j in ((0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)):
        # adj(A)[i,j] deletes row j and column i.
        b = [[a[r][c] for c in range(3) if c != i]
             for r in range(3) if r != j]
        out.append(((-1)**(i+j)*det2(b[0], b[1])) % p)
    return tuple(out)


def jca(state, p):
    return tuple(pow(u, -1, p) if u else 0 for u in adjugate(state, p))


def analyze(name, parameter, states, operation):
    states = tuple(states)
    index = {state: i for i, state in enumerate(states)}
    require(len(states) == len(index))
    nexts = []
    for state in states:
        nxt = operation(state)
        require(nxt in index)
        nexts.append(index[nxt])
    indeg = Counter(nexts)
    depth = [-1]*len(states)
    period = [0]*len(states)
    cycles = Counter()
    witnesses = {}
    for initial in range(len(states)):
        if depth[initial] >= 0:
            continue
        path, seen = [], {}
        cur = initial
        while depth[cur] < 0 and cur not in seen:
            seen[cur] = len(path)
            path.append(cur)
            cur = nexts[cur]
        stop = len(path)
        if depth[cur] < 0:
            start = seen[cur]
            cycle = path[start:]
            length = len(cycle)
            cycles[length] += 1
            for node in cycle:
                depth[node], period[node] = 0, length
            if str(length) not in witnesses:
                witnesses[str(length)] = [states[node] for node in cycle]
            stop = start
        for node in reversed(path[:stop]):
            depth[node] = depth[nexts[node]]+1
            period[node] = period[nexts[node]]
    for i, j in enumerate(nexts):
        require(period[i] == period[j])
        require(depth[i] == depth[j]+1 if depth[i] else depth[j] == 0)
    require(sum(k*v for k, v in cycles.items()) == depth.count(0))
    require(sum(indeg.values()) == len(states))
    mf = max(indeg.values())
    mh = max(depth)
    result = {
        "id": name, "parameter": parameter, "states": len(states),
        "image": len(indeg), "recurrent": depth.count(0), "height": mh,
        "fixed": sum(i == j for i, j in enumerate(nexts)),
        "cycles": dict(sorted(cycles.items())),
        "depth_histogram": dict(sorted(Counter(depth).items())),
        "indegree_histogram": dict(sorted(Counter(indeg.get(i, 0) for i in range(len(states))).items())),
        "maximum_fibre": mf,
        "maximum_fibre_target_count": sum(v == mf for v in indeg.values()),
        "maximum_fibre_first_target": states[min(i for i, v in indeg.items() if v == mf)],
        "maximum_depth_first_state": states[depth.index(mh)],
        "cycle_witnesses": witnesses,
        "next_index_sha256": hashlib.sha256(json.dumps(nexts, separators=(",", ":")).encode()).hexdigest(),
    }
    if name == "SBF":
        p = parameter["p"]
        for i, (a, b) in enumerate(states):
            total = (a+b) % p
            expected = 1 if total else p if a == b == 0 else 0
            require(indeg.get(i, 0) == expected)
        require(result["fixed"] == p)
    if name == "HGF":
        p = parameter["p"]
        require(indeg[index[(0, 0, 0)]] == (4 if p == 2 else 6*p-5))
        for i, state in enumerate(states):
            if p == 2:
                require(nexts[nexts[i]] == nexts[i])
            if p == 3:
                scalar = (sum(x*x for x in state)+1) % 3
                require(states[nexts[i]] == tuple(x*scalar % 3 for x in state))
    if name == "JCA":
        p = parameter["p"]
        zero = index[(0,)*6]
        for i, state in enumerate(states):
            rank = matrix_rank(state, p)
            if rank < 3:
                require(nexts[nexts[i]] == zero)
            if p <= 3:
                require(states[nexts[i]] == adjugate(state, p))
        result["rank_histogram"] = dict(sorted(Counter(matrix_rank(s, p) for s in states).items()))
    return result


def main():
    rows = []
    for p in (2, 3):
        rows.append(analyze("QAS", {"p": p}, it.product(range(p), repeat=8),
                            lambda s, p=p: points_rule(s, p, "QAS")))
    for p in (2, 3, 5):
        rows.append(analyze("DTC", {"p": p}, it.product(range(p), repeat=6),
                            lambda s, p=p: points_rule(s, p, "DTC")))
    for n in range(3, 11):
        carrier = triangulations(tuple(range(n)))
        # Catalan recurrence, independent of the polygon split generator.
        catalan = [1]
        for k in range(1, n-1):
            catalan.append(sum(catalan[j]*catalan[k-1-j] for j in range(k)))
        require(len(carrier) == catalan[n-2])
        require(all(len(s) == n-3 for s in carrier))
        rows.append(analyze("OFS", {"n": n}, carrier, lambda s, n=n: ofs(s, n)))
    for p in (2, 3, 5, 7, 11, 13, 17, 19):
        rows.append(analyze("SBF", {"p": p}, it.product(range(p), repeat=2),
                            lambda s, p=p: sbf(s, p)))
    for p in (2, 3, 5, 7, 11, 13):
        rows.append(analyze("HGF", {"p": p}, it.product(range(p), repeat=3),
                            lambda s, p=p: hgf(s, p)))
    for p in (2, 3, 5):
        rows.append(analyze("JCA", {"p": p}, it.product(range(p), repeat=6),
                            lambda s, p=p: jca(s, p)))
    print(json.dumps({"role": "author_bounded_pilot", "assertions": CHECKS,
                      "rows": rows}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
