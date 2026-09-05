#!/usr/bin/env python3
"""Seven probes plus an immediate closure control. Author-side evidence."""
from collections import Counter, deque
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json

CHECKS = 0
DIGEST = sha256()


def check(condition):
    global CHECKS
    CHECKS += 1
    assert condition, CHECKS


def analyse(name, parameter, nxt):
    size = len(nxt)
    check(all(0 <= y < size for y in nxt))
    depth = [-1] * size
    period = [0] * size
    cycles = Counter()
    for start in range(size):
        if depth[start] >= 0:
            continue
        path, index = [], {}
        v = start
        while depth[v] < 0 and v not in index:
            index[v] = len(path)
            path.append(v)
            v = nxt[v]
        if v in index:
            cut = index[v]
            cyc = path[cut:]
            cycles[len(cyc)] += 1
            for w in cyc:
                depth[w], period[w] = 0, len(cyc)
            path = path[:cut]
        for w in reversed(path):
            depth[w], period[w] = depth[nxt[w]] + 1, period[nxt[w]]
    for x, y in enumerate(nxt):
        check(period[x] == period[y])
        check(depth[x] == 0 or depth[x] == depth[y] + 1)
        DIGEST.update(f"{name}:{parameter}:{x}:{y}:{depth[x]}:{period[x]}\n".encode())
    fibres = Counter(nxt)
    max_fibre = max(fibres.values())
    maximizers = sorted(y for y, count in fibres.items() if count == max_fibre)
    height = max(depth)
    longest = max(period)
    witness = depth.index(height)
    orbit, seen = [], set()
    cur = witness
    while cur not in seen:
        seen.add(cur)
        orbit.append(cur)
        cur = nxt[cur]
    return dict(rule=name, parameter=parameter, states=size,
                image=len(fibres), core=depth.count(0),
                fixed=sum(x == y for x, y in enumerate(nxt)),
                height=height, cycles=dict(sorted(cycles.items())),
                depths=dict(sorted(Counter(depth).items())),
                max_fibre=max_fibre,
                max_fibre_target_count=len(maximizers),
                first_max_fibre_target=maximizers[0],
                max_fibre_targets_digest=sha256(json.dumps(maximizers).encode()).hexdigest(),
                height_witness=witness, height_orbit=orbit,
                height_orbit_repeat=cur,
                longest_period=longest,
                longest_period_witness=period.index(longest))


def metric(n, edges, mask):
    adj = [set() for _ in range(n)]
    for bit, (u, v) in enumerate(edges):
        if mask >> bit & 1:
            adj[u].add(v)
            adj[v].add(u)
    dist = [[-1] * n for _ in range(n)]
    ways = [[0] * n for _ in range(n)]
    for root in range(n):
        dist[root][root], ways[root][root] = 0, 1
        queue = deque([root])
        while queue:
            v = queue.popleft()
            for w in sorted(adj[v]):
                if dist[root][w] < 0:
                    dist[root][w] = dist[root][v] + 1
                    queue.append(w)
                if dist[root][w] == dist[root][v] + 1:
                    ways[root][w] += ways[root][v]
    parts = []
    unassigned = set(range(n))
    while unassigned:
        u = min(unassigned)
        part = tuple(v for v in range(n) if dist[u][v] >= 0)
        parts.append(part)
        unassigned.difference_update(part)
    return adj, dist, ways, parts


def inverse(matrix):
    n = len(matrix)
    a = [[Fraction(x) for x in row] +
         [Fraction(i == j) for j in range(n)]
         for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if a[i][col])
        a[col], a[pivot] = a[pivot], a[col]
        val = a[col][col]
        a[col] = [x / val for x in a[col]]
        for row in range(n):
            if row != col and a[row][col]:
                val = a[row][col]
                a[row] = [x - val * y for x, y in zip(a[row], a[col])]
    return [row[n:] for row in a]


def graph_successors(n, mask):
    edges = list(combinations(range(n), 2))
    adj, dist, ways, parts = metric(n, edges, mask)
    result = {name: 0 for name in ("DIA", "ODD", "EVEN", "TWO", "MMD", "RED")}
    diam, resistance, rmax = {}, {}, {}
    for part in parts:
        diameter = max(dist[u][v] for u in part for v in part)
        for u in part:
            diam[u] = diameter
        if len(part) < 2:
            continue
        free, ground = part[:-1], part[-1]
        reduced = [[len(adj[u]) if u == v else -int(v in adj[u])
                    for v in free] for u in free]
        inv = inverse(reduced)
        lookup = {u: i for i, u in enumerate(free)}
        maximum = Fraction(0)
        for u, v in combinations(part, 2):
            if v == ground:
                value = inv[lookup[u]][lookup[u]]
            else:
                i, j = lookup[u], lookup[v]
                value = inv[i][i] + inv[j][j] - inv[i][j] - inv[j][i]
            check(value > 0)
            resistance[u, v] = value
            maximum = max(maximum, value)
        for u in part:
            rmax[u] = maximum
    for bit, (u, v) in enumerate(edges):
        if dist[u][v] < 0:
            continue
        predicates = {
            "DIA": dist[u][v] == diam[u],
            "ODD": dist[u][v] % 2 == 1,
            "EVEN": dist[u][v] % 2 == 0,
            "TWO": ways[u][v] == 2,
            "MMD": all(dist[w][v] <= dist[u][v] for w in adj[u]) and
                   all(dist[w][u] <= dist[u][v] for w in adj[v]),
            "RED": resistance[u, v] == rmax[u],
        }
        for name, yes in predicates.items():
            if yes:
                result[name] |= 1 << bit
    return result


def projection(p, a, b, c):
    ax, ay = a % p, a // p
    bx, by = b % p, b // p
    dx, dy = (c % p - bx) % p, (c // p - by) % p
    norm = (dx * dx + dy * dy) % p
    if norm == 0:
        check(b == c)  # p = 3 mod 4: anisotropic dot product.
        return b
    scalar = (((ax - bx) * dx + (ay - by) * dy) * pow(norm, -1, p)) % p
    return (bx + scalar * dx) % p + p * ((by + scalar * dy) % p)


def reflect(p, a, foot):
    return (2 * (foot % p) - a % p) % p + p * ((2 * (foot // p) - a // p) % p)


def geometric_successors(p):
    q = p * p
    nxt = {"PED": [], "REF": []}
    origin_feet = [[projection(p, 0, b, c) for c in range(q)] for b in range(q)]
    for c in range(q):
        for b in range(q):
            for a in range(q):
                pa, pb, pc = origin_feet[b][c], origin_feet[c][a], origin_feet[a][b]
                nxt["PED"].append(pa + q * pb + q * q * pc)
                ra = reflect(p, a, projection(p, a, b, c))
                rb = reflect(p, b, projection(p, b, c, a))
                rc = reflect(p, c, projection(p, c, a, b))
                nxt["REF"].append(ra + q * rb + q * q * rc)
    return nxt


def main():
    rows = []
    for n in range(6):
        maps = {name: [] for name in ("DIA", "ODD", "EVEN", "TWO", "MMD", "RED")}
        for mask in range(1 << (n * (n - 1) // 2)):
            results = graph_successors(n, mask)
            for name, y in results.items():
                maps[name].append(y)
        for name, nxt in maps.items():
            rows.append(analyse(name, n, nxt))
    for p in (3, 7):
        for name, nxt in geometric_successors(p).items():
            rows.append(analyse(name, p, nxt))
    # ODD has a universal inflationarity witness: every old edge has distance one.
    for n in range(6):
        for mask in range(1 << (n * (n - 1) // 2)):
            check(graph_successors(n, mask)["ODD"] & mask == mask)
    # A proof-directed single C_7 sentinel, not a larger exhaustive cutoff.
    n = 7
    edges = list(combinations(range(n), 2))
    cycle = sum(1 << bit for bit, (u, v) in enumerate(edges)
                if (u - v) % n in (1, n - 1))
    sentinels = []
    for name in ("DIA", "MMD", "RED", "EVEN"):
        orbit = [cycle]
        for _ in range(3):
            orbit.append(graph_successors(n, orbit[-1])[name])
        check(orbit[0] == orbit[3] and len(set(orbit[:3])) == 3)
        sentinels.append(dict(rule=name, graph="C7", period=3, orbit=orbit))
    print(json.dumps(dict(schema="eight-literal-bounded-scout-v1", checks=CHECKS,
                          states=sum(row["states"] for row in rows),
                          enumeration_digest=DIGEST.hexdigest(), rows=rows,
                          proof_directed_sentinels=sentinels),
                     sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
