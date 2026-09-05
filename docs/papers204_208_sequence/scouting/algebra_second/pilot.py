#!/usr/bin/env python3
"""Second algebra scout, six literal maps, exact small boxes, no imports.

SI singleton inverse; SP elementary-symmetric fold; TD truncated derivative;
TP coupled composition; HC cyclic histogram; OT totalized orthic triangle.
These are author-side pilots, not independent acceptance evidence.
"""
from collections import Counter, deque
from itertools import product
from math import comb, factorial
import json


def stats(nxt):
    n = len(nxt)
    indeg = [0]*n
    for y in nxt:
        indeg[y] += 1
    fibres = Counter(indeg)
    queue = deque(i for i in range(n) if indeg[i] == 0)
    peeled = []
    while queue:
        x = queue.popleft()
        peeled.append(x)
        y = nxt[x]
        indeg[y] -= 1
        if indeg[y] == 0:
            queue.append(y)
    depth = [0]*n
    for x in reversed(peeled):
        depth[x] = 1+depth[nxt[x]]
    seen = set()
    cycles = Counter()
    for x in range(n):
        if indeg[x] and x not in seen:
            y, length = x, 0
            while y not in seen:
                seen.add(y)
                length += 1
                y = nxt[y]
            cycles[length] += 1
    return {"states": n, "image": n-fibres[0], "core": len(seen),
            "tail_max": max(depth), "depths": dict(sorted(Counter(depth).items())),
            "cycles": dict(sorted(cycles.items())), "max_fibre": max(fibres),
            "max_fibre_targets": fibres[max(fibres)]}


def output(name, params, nxt, check=None):
    row = {"map": name, "parameters": params, **stats(nxt)}
    if check:
        check(row)
        row["assertions"] = "PASS"
    print(json.dumps(row, sort_keys=True, separators=(",", ":")), flush=True)


def singleton_inverse(f):
    pre = [[] for _ in f]
    for i, v in enumerate(f):
        pre[v].append(i)
    return tuple(pre[v][0] if len(pre[v]) == 1 else v for v in range(len(f)))


def falling(n, k):
    return factorial(n)//factorial(n-k)


def occupancy_count(k, p):
    # p unmatched path roots; k-p fixed self-labels may have their self singleton.
    total = 0
    for j in range(k+1):
        for h in range(max(0, j-p), min(j, k-p)+1):
            ways = comb(k-p, h)*comb(p, j-h)
            inj = sum((-1)**a*comb(h, a)*falling(k-a, j-a) for a in range(h+1))
            total += (-1)**j*ways*inj*(k-j)**(k-j)
    return total


def singleton_scout():
    for n in range(1, 6):
        fs = list(product(range(n), repeat=n))
        ids = {f: i for i, f in enumerate(fs)}
        nxt = [ids[singleton_inverse(f)] for f in fs]
        fibres = Counter(nxt)
        for i, g in enumerate(fs):
            nonfixed = [v for v in range(n) if g[v] != v]
            vals = [g[v] for v in nonfixed]
            if len(set(vals)) != len(vals):
                expected = 0
            else:
                fixed = set(range(n))-set(nonfixed)
                k = len(fixed)
                p = len(fixed & set(vals))
                expected = occupancy_count(k, p)
            assert fibres[i] == expected, (n, g, expected, fibres[i])
        def check(row):
            involutions = sum(factorial(n)//(2**j*factorial(j)*factorial(n-2*j)) for j in range(n//2+1))
            assert row["core"] == factorial(n)
            assert row["cycles"].get(1, 0) == involutions
            assert row["cycles"].get(2, 0) == (factorial(n)-involutions)//2
            assert all(k in (1, 2) for k in row["cycles"])
            assert row["tail_max"] == n-1
            assert row["max_fibre"] == occupancy_count(n, 0)
            # At n=1, id is the sole target; at n>=2 it remains the unique maximum.
            assert row["max_fibre_targets"] == 1
            if n >= 3:
                assert row["depths"][n-1] == 2*factorial(n)
        output("SI", {"n": n}, nxt, check)


def other_function_maps():
    for n in range(2, 6):
        fs = list(product(range(n), repeat=n))
        ids = {f: i for i, f in enumerate(fs)}
        nxt = []
        for f in fs:
            counts = Counter(f)
            nxt.append(ids[tuple(counts[v] % n for v in range(n))])
        output("HC", {"n": n}, nxt)
    for n in (2, 3, 4):
        fs = list(product(range(n), repeat=n))
        ids = {f: i for i, f in enumerate(fs)}
        size = len(fs)
        nxt = []
        for f in fs:
            for g in fs:
                fg = tuple(f[g[v]] for v in range(n))
                gf = tuple(g[f[v]] for v in range(n))
                nxt.append(ids[fg]*size+ids[gf])
        output("TP", {"n": n}, nxt)


def field_and_ring_maps():
    for p in (2, 3, 5, 7, 11, 13):
        nxt = [((x+y) % p)*p+(x*y) % p for x in range(p) for y in range(p)]
        output("SP", {"p": p}, nxt)
    for p in (2, 3, 5):
        fs = list(product(range(p), repeat=p))
        ids = {f: i for i, f in enumerate(fs)}
        nxt = []
        for f in fs:
            derivative = [(j*f[j]) % p for j in range(1, p)]
            out = tuple(sum(f[i]*derivative[k-i] for i in range(k+1) if 0 <= k-i < p-1) % p
                        for k in range(p))
            nxt.append(ids[out])
        output("TD", {"p": p, "algebra": "F_p[x]/(x^p)"}, nxt)


def orthic_triangles():
    for p in (3, 5):
        points = list(product(range(p), repeat=2))
        point_id = {a: i for i, a in enumerate(points)}
        size = len(points)
        def foot(a, b, c):
            dx, dy = (c[0]-b[0]) % p, (c[1]-b[1]) % p
            norm = (dx*dx+dy*dy) % p
            if norm == 0:
                return a
            t = ((a[0]-b[0])*dx+(a[1]-b[1])*dy)*pow(norm, -1, p) % p
            return ((b[0]+t*dx) % p, (b[1]+t*dy) % p)
        nxt = []
        for a, b, c in product(points, repeat=3):
            x, y, z = foot(a, b, c), foot(b, c, a), foot(c, a, b)
            nxt.append((point_id[x]*size+point_id[y])*size+point_id[z])
        output("OT", {"p": p, "zero_norm_rule": "retain_departing_vertex"}, nxt)


if __name__ == "__main__":
    singleton_scout()
    other_function_maps()
    field_and_ring_maps()
    orthic_triangles()
