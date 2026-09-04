#!/usr/bin/env python3
"""Independent Review-B control for P195.

No paper or Review-A module is imported.  Edge-side sizes are obtained from a
single reroot dynamic program, rather than by deleting edges.  The EGF attack
uses exact rational formal series and is checked against the literal map.
"""

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import factorial
import heapq


N = 8
checks = 0
transitions = 0
digest = sha256()


def demand(condition):
    global checks
    checks += 1
    if not condition:
        raise AssertionError("Review-B check failed")


def decode_prufer(n, code):
    if n == 1:
        return []
    degree = [1] * n
    for x in code:
        degree[x] += 1
    leaves = [v for v in range(n) if degree[v] == 1]
    heapq.heapify(leaves)
    edges = []
    for x in code:
        leaf = heapq.heappop(leaves)
        edges.append((leaf, x))
        degree[leaf] -= 1
        degree[x] -= 1
        if degree[x] == 1:
            heapq.heappush(leaves, x)
    if n == 2 or len(edges) == n - 2:
        a = heapq.heappop(leaves)
        b = heapq.heappop(leaves)
        edges.append((a, b))
    demand(len(edges) == n - 1)
    return edges


def reroot_data(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    for row in adj:
        row.sort()

    parent = [-2] * n
    parent[0] = -1
    order = [0]
    for u in order:
        for v in adj[u]:
            if v != parent[u]:
                demand(parent[v] == -2)
                parent[v] = u
                order.append(v)
    demand(len(order) == n)

    subtree = [1] * n
    for v in reversed(order[1:]):
        subtree[parent[v]] += subtree[v]

    side = [dict() for _ in range(n)]
    for u, v in edges:
        if parent[v] == u:
            side[u][v] = subtree[v]
            side[v][u] = n - subtree[v]
        else:
            demand(parent[u] == v)
            side[v][u] = subtree[u]
            side[u][v] = n - subtree[u]

    nxt = []
    for u in range(n):
        eligible = [v for v in adj[u] if side[u][v] % 2 == 1]
        nxt.append(min(eligible) if eligible else u)
    return adj, side, tuple(nxt)


def recurrent_vertex(n, nxt, v):
    if n % 2:
        return nxt[v] == v
    return nxt[v] != v and nxt[nxt[v]] == v


def analyse_edges(n, edges):
    adj, side, nxt = reroot_data(n, edges)
    indegree = Counter(nxt)
    depth = []
    for start in range(n):
        seen = set()
        x = start
        d = 0
        while not recurrent_vertex(n, nxt, x):
            demand(x not in seen)
            seen.add(x)
            x = nxt[x]
            d += 1
            demand(d <= n)
        depth.append(d)
    return adj, side, nxt, indegree, tuple(depth)


def add(a, b):
    return [a[i] + b[i] for i in range(N + 1)]


def mul(a, b):
    out = [Fraction(0) for _ in range(N + 1)]
    for i, ai in enumerate(a):
        if not ai:
            continue
        for j, bj in enumerate(b[:N + 1 - i]):
            if bj:
                out[i + j] += ai * bj
    return out


def exp_series(a):
    demand(a[0] == 0)
    out = [Fraction(0) for _ in range(N + 1)]
    out[0] = 1
    for n in range(1, N + 1):
        out[n] = sum(Fraction(k) * a[k] * out[n - k]
                     for k in range(1, n + 1)) / n
    return out


def shift(a):
    return [Fraction(0)] + a[:N]


tree_counts = {}
recurrent_counts = {}
depth_histograms = {}
summary = []

for n in range(1, N + 1):
    tree_count = 0
    recurrent_total = 0
    hist = Counter()
    max_fibre = 0
    max_tail = 0
    for code in product(range(n), repeat=max(0, n - 2)):
        edges = decode_prufer(n, code)
        adj, side, nxt, indegree, depths = analyse_edges(n, edges)
        tree_count += 1
        transitions += n

        if n % 2:
            for u, v in edges:
                demand((side[u][v] % 2) != (side[v][u] % 2))
            demand(any(nxt[v] == v for v in range(n)))
        else:
            h_degree = [sum(side[u][v] % 2 for v in adj[u]) for u in range(n)]
            for u, v in edges:
                demand((side[u][v] % 2) == (side[v][u] % 2))
            demand(all(value % 2 == 1 for value in h_degree))
            demand(all(nxt[v] != v for v in range(n)))

        for target in range(n):
            self_term = int(all(side[target][w] % 2 == 0 for w in adj[target]))
            neighbour_term = 0
            for u in adj[target]:
                other_eligible = [w for w in adj[u]
                                  if w != target and side[u][w] % 2 == 1]
                condition = (side[u][target] % 2 == 1 and
                             (not other_eligible or target < min(other_eligible)))
                neighbour_term += int(condition)
            predicted = self_term + neighbour_term
            demand(predicted == indegree[target])

        recurrent_here = sum(recurrent_vertex(n, nxt, v) for v in range(n))
        recurrent_total += recurrent_here
        hist.update(depths)
        max_tail = max(max_tail, max(depths))
        max_fibre = max(max_fibre, max(indegree.values()))

        digest.update((repr(code) + ":" + repr(nxt) + ":" + repr(depths) +
                       ":" + repr(tuple(indegree[v] for v in range(n))) + ";").encode("ascii"))

    demand(tree_count == (1 if n == 1 else n ** (n - 2)))
    demand(max_tail == (n - 1) // 2)
    demand(max_fibre == ((n + 1) // 2 if n % 2 else n - 1))
    tree_counts[n] = tree_count
    recurrent_counts[n] = recurrent_total
    depth_histograms[n] = hist
    row = ",".join(f"{d}:{hist[d]}" for d in sorted(hist))
    summary.append(
        f"n={n} trees={tree_count} states={tree_count*n} recurrent={recurrent_total} "
        f"max_tail={max_tail} max_fibre={max_fibre} depth_hist={row}"
    )

# Formal-series calculation, built from Cayley coefficients only.
R = [Fraction(0)] + [Fraction(n ** (n - 1), factorial(n)) for n in range(1, N + 1)]
O = [R[n] if n % 2 else Fraction(0) for n in range(N + 1)]
E = [R[n] if n and n % 2 == 0 else Fraction(0) for n in range(N + 1)]
expE = exp_series(E)
expO_over_O = [Fraction(0) for _ in range(N + 1)]
power = [Fraction(0) for _ in range(N + 1)]
power[0] = 1
for j in range(N + 1):
    factor = Fraction(1, factorial(j + 1))
    expO_over_O = add(expO_over_O, [factor * x for x in power])
    power = mul(power, O)
W = shift(mul(expE, expO_over_O))
Wodd = [W[n] if n % 2 else Fraction(0) for n in range(N + 1)]
Wpair = mul(Wodd, Wodd)

for n in range(1, N + 1):
    if n % 2:
        predicted = factorial(n) * expE[n - 1]
    else:
        predicted = factorial(n) * Wpair[n]
    demand(predicted.denominator == 1)
    demand(predicted.numerator == recurrent_counts[n])

demand([recurrent_counts[n] for n in (1, 3, 5, 7)] == [1, 6, 380, 68712])
demand([recurrent_counts[n] for n in (2, 4, 6, 8)] == [2, 56, 6512, 1718656])

# Constructive sharp-tail and sharp-fibre witnesses, independently labelled.
for d in range(0, 8):
    n = 2 * d + 1
    odd_edges = [(i, i + 1) for i in range(d)] + [(i, d + 1 + i) for i in range(d)]
    _, _, _, _, odd_depth = analyse_edges(n, odd_edges)
    demand(odd_depth[0] == d)
    bouquet = [(0, 1 + i) for i in range(d)] + [
        (1 + i, 1 + d + i) for i in range(d)
    ]
    _, _, _, odd_indegree, _ = analyse_edges(n, bouquet)
    demand(odd_indegree[0] == d + 1)

    n = 2 * d + 2
    spine = [d + 1 - i for i in range(d + 2)]
    even_edges = [(spine[i], spine[i + 1]) for i in range(d + 1)]
    even_edges += [(spine[i], d + 1 + i) for i in range(1, d + 1)]
    _, _, _, _, even_depth = analyse_edges(n, even_edges)
    demand(even_depth[spine[0]] == d)
    star = [(0, leaf) for leaf in range(1, n)]
    _, _, _, star_indegree, _ = analyse_edges(n, star)
    demand(star_indegree[0] == n - 1)

# Regression against the false "one H-component, one attracting edge" claim.
double_star = [(0, 2), (1, 3), (2, 3), (2, 4), (3, 5)]
adj, side, nxt, _, _ = analyse_edges(6, double_star)
demand(all(side[u][v] % 2 for u, v in double_star))
mutual = {(min(u, nxt[u]), max(u, nxt[u])) for u in range(6)
          if nxt[u] != u and nxt[nxt[u]] == u}
demand(mutual == {(0, 2), (1, 3)})

print("P195 independent reroot-array / rational-EGF Review B")
for line in summary:
    print(line)
print("odd_recurrent=1,6,380,68712")
print("even_recurrent=2,56,6512,1718656")
print("double_star_mutual_edges=1-3,2-4")
print(f"transitions={transitions}")
print(f"assertions={checks}")
print(f"record_digest={digest.hexdigest()}")
print("open_critical=0 open_major=0 open_minor=0")
print("external_state=OWNER_AMBER/HOLD_EXTERNAL")
print("status=PASS")
