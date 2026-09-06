"""Fixed-intake author scout. Only Python standard library; stdout is canonical."""
from collections import Counter, deque
from itertools import combinations, permutations, product
import hashlib
import json

CHECKS = 0


def check(condition):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(CHECKS)


def encode(digits, p):
    value = 0
    for digit in digits:
        value = value * p + digit
    return value


def census(rule, params, mapping):
    size = len(mapping)
    check(all(0 <= target < size for target in mapping))
    fibres = Counter(mapping)
    indegree = [fibres[x] for x in range(size)]
    queue = deque(x for x in range(size) if not indegree[x])
    removed = []
    while queue:
        x = queue.popleft()
        removed.append(x)
        y = mapping[x]
        indegree[y] -= 1
        if not indegree[y]:
            queue.append(y)
    core = set(range(size)) - set(removed)
    depth = [0] * size
    for x in reversed(removed):
        depth[x] = depth[mapping[x]] + 1
    unseen = set(core)
    cycles = []
    while unseen:
        start = min(unseen)
        cyc = [start]
        y = mapping[start]
        while y != start:
            check(y in unseen)
            cyc.append(y)
            y = mapping[y]
        unseen.difference_update(cyc)
        cycles.append(cyc)
    check(sum(map(len, cycles)) == len(core))
    check(all(depth[x] == 0 if x in core else depth[x] == depth[mapping[x]] + 1
              for x in range(size)))
    maximum_depth = max(depth)
    tail = [depth.index(maximum_depth)]
    for _ in range(maximum_depth):
        tail.append(mapping[tail[-1]])
    largest_cycle = max(cycles, key=len)
    max_fibre = max(fibres.values())
    fibre_targets = [x for x in sorted(fibres) if fibres[x] == max_fibre]
    widths = [size]
    current = set(range(size))
    while True:
        nxt = {mapping[x] for x in current}
        if nxt == current:
            break
        widths.append(len(nxt))
        current = nxt
    check(current == core)
    check(len(widths) - 1 == maximum_depth)
    raw = json.dumps(mapping, separators=(",", ":")).encode()
    return dict(rule=rule, params=params, states=size, image=len(fibres),
                core=len(core), maximum_tail=maximum_depth,
                cycle_counts=dict(sorted(Counter(map(len, cycles)).items())),
                image_widths=widths, maximum_fibre=max_fibre,
                maximum_fibre_target_count=len(fibre_targets),
                first_maximum_fibre_target=fibre_targets[0],
                maximum_tail_orbit=tail, longest_cycle=largest_cycle,
                mapping_sha256=hashlib.sha256(raw).hexdigest())


def det2(matrix):
    """Determinant over F2 by row elimination; det(empty)=1."""
    a = [row[:] for row in matrix]
    r = len(a)
    for col in range(r):
        pivot = next((i for i in range(col, r) if a[i][col]), None)
        if pivot is None:
            return 0
        a[col], a[pivot] = a[pivot], a[col]
        for i in range(col + 1, r):
            if a[i][col]:
                a[i] = [x ^ y for x, y in zip(a[i], a[col])]
    return 1


def tree_mask(n, edges, selected):
    parent = list(range(n))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    mask = 0
    for idx in selected:
        u, v = edges[idx]
        a, b = root(u), root(v)
        if a == b:
            return None
        parent[a] = b
        mask |= 1 << idx
    return mask


def stc(n):
    edges = list(combinations(range(n), 2))
    m = len(edges)
    tau = [0] * (1 << m)
    for selected in combinations(range(m), n - 1):
        mask = tree_mask(n, edges, selected)
        if mask is not None:
            tau[mask] = 1
    check(sum(tau) == (1 if n == 1 else n ** (n - 2)))
    # XOR subset zeta transform: counts all spanning trees contained in G.
    for bit in range(m):
        for mask in range(1 << m):
            if mask & (1 << bit):
                tau[mask] ^= tau[mask ^ (1 << bit)]
    mapping = []
    complete = (1 << m) - 1
    for mask in range(1 << m):
        lap = [[0] * (n - 1) for _ in range(n - 1)]
        for e, (u, v) in enumerate(edges):
            if mask >> e & 1:
                if u < n - 1:
                    lap[u][u] ^= 1
                if v < n - 1:
                    lap[v][v] ^= 1
                    lap[u][v] ^= 1
                    lap[v][u] ^= 1
        check(tau[mask] == det2(lap))
        d = [det2([[lap[i][j] for j in range(n - 1) if j != k]
                   for i in range(n - 1) if i != k])
             for k in range(n - 1)] + [0]
        removed = 0
        for e, (u, v) in enumerate(edges):
            parity = (tau[mask] ^ tau[mask ^ (1 << e)]) if mask >> e & 1 else 0
            check(parity == ((mask >> e & 1) & (d[u] ^ d[v])))
            removed |= parity << e
        mapping.append(complete ^ removed)
    return census("STC", dict(n=n), mapping)


def permanent(a, r, p):
    total = 0
    for perm in permutations(range(r)):
        term = 1
        for i in range(r):
            term *= a[i * r + perm[i]]
        total += term
    return total % p


def pcg(r, p):
    mapping = []
    for a in product(range(p), repeat=r * r):
        base = permanent(a, r, p)
        out = []
        for i in range(r):
            for j in range(r):
                minor = tuple(a[u * r + v] for u in range(r) if u != i
                              for v in range(r) if v != j)
                value = permanent(minor, r - 1, p)
                changed = list(a)
                changed[i * r + j] = (changed[i * r + j] + 1) % p
                check(value == (permanent(changed, r, p) - base) % p)
                out.append(value)
        if r == 2:
            check(tuple(out) == tuple(reversed(a)))
        mapping.append(encode(out, p))
    if r == 2:
        check(all(mapping[mapping[x]] == x for x in range(len(mapping))))
    return census("PCG", dict(r=r, p=p), mapping)


def ump(p, d):
    points = list(product(range(p), repeat=d))
    v = len(points)
    inv2 = pow(2, -1, p)
    pairs = [(a, b, encode(tuple((x + y) * inv2 % p
                                for x, y in zip(points[a], points[b])), p))
             for a, b in combinations(range(v), 2)]
    mapping = []
    for mask in range(1 << v):
        counts = [0] * v
        for a, b, midpoint in pairs:
            if mask >> a & 1 and mask >> b & 1:
                counts[midpoint] += 1
        out = sum(1 << midpoint for midpoint, count in enumerate(counts) if count == 1)
        # Independent point-reflection count, divided by 2 as an integer.
        for midpoint, centre in enumerate(points):
            ordered = 0
            for a, point in enumerate(points):
                reflection = encode(tuple((2 * x - y) % p
                                          for x, y in zip(centre, point)), p)
                if a != reflection and mask >> a & 1 and mask >> reflection & 1:
                    ordered += 1
            check(ordered == 2 * counts[midpoint])
            check(bool(out >> midpoint & 1) == (ordered == 2))
        if mask.bit_count() < 2:
            check(out == 0)
        if mask.bit_count() == 2:
            check(out.bit_count() == 1)
        mapping.append(out)
    return census("UMP", dict(p=p, d=d), mapping)


def main():
    results = [stc(n) for n in (1, 2, 3, 4, 5, 6)]
    results += [pcg(r, p) for r, p in ((2, 3), (2, 5), (2, 7), (3, 3))]
    results += [ump(p, d) for p, d in ((3, 0), (3, 1), (3, 2), (5, 1), (7, 1), (11, 1))]
    check(len(results) == 16)
    check(sum(row["states"] for row in results) == 59387)
    print(json.dumps(dict(schema="twelfth-author-pilot-v1", assertions=CHECKS,
                          boxes=results), sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
