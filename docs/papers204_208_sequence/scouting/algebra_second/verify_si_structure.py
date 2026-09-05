#!/usr/bin/env python3
"""Author-side SI proof pressure and exact P167 adapter; no scout imports."""
from collections import Counter, defaultdict
from itertools import product
from math import comb, factorial
import json


def si(f):
    count = [0]*len(f)
    pre = [-1]*len(f)
    for u, v in enumerate(f):
        count[v] += 1
        pre[v] = u
    return tuple(pre[v] if count[v] == 1 else v for v in range(len(f)))


def p167(f):
    out = list(range(len(f)))
    for u in reversed(range(len(f))):
        out[f[u]] = u
    return tuple(out)


def paths(g):
    incoming = {}
    for u, v in enumerate(g):
        if u != v:
            if v in incoming:
                return None
            incoming[v] = u
    out = []
    for root in range(len(g)):
        if g[root] == root:
            chain = [root]
            while chain[-1] in incoming:
                chain.append(incoming[chain[-1]])
                assert len(chain) <= len(g)
            out.append(tuple(chain))
    return out


def associated_partitions(m):
    table = [[0]*(m+1) for _ in range(m+1)]
    table[0][0] = 1
    for n in range(1, m+1):
        for b in range(1, n//2+1):
            table[n][b] = sum(comb(n-1, j-1)*table[n-j][b-1] for j in range(2, n+1))
    return table[m]


def no_singleton_count(m):
    return sum(a*factorial(m)//factorial(m-b) for b, a in enumerate(associated_partitions(m)))


def atlas(k, p):
    return sum(comb(k-p, s)*no_singleton_count(k-s) for s in range(k-p+1))


def image_count_species(n):
    unrestricted = [1]
    for m in range(1, n+1):
        unrestricted.append(sum(comb(m-1, j-1)*(factorial(j)+(factorial(j-1) if j >= 2 else 0))
                                *unrestricted[m-j] for j in range(1, m+1)))
    derangements = [1, 0]
    for m in range(2, n+1):
        derangements.append((m-1)*(derangements[m-1]+derangements[m-2]))
    excluded = sum(comb(n, j)*factorial(j)*derangements[n-j] for j in range(2, n+1))
    return unrestricted[n]-excluded


def verify(n):
    fs = list(product(range(n), repeat=n))
    reverse = defaultdict(set)
    for f in fs:
        reverse[si(f)].add(f)
    candidate_assignments = 0
    shape_targets = 0
    for g in fs:
        ps = paths(g)
        if ps is None:
            assert g not in reverse
            continue
        shape_targets += 1
        k = len(ps)
        p = sum(len(path) > 1 for path in ps)
        assert len(reverse[g]) == atlas(k, p)
        # Structural image support, not inferred from a positive numerical formula.
        assert bool(reverse[g]) == ((k, p) != (1, 1))
        expected = list(g)
        covered = set()
        for path in ps:
            covered.update(path)
            expected[path[0]] = path[0]
            if len(path) > 1:
                expected[path[-1]] = path[-1]
                for i in range(1, len(path)-1):
                    expected[path[i]] = path[i+1]
        for u in range(n):
            if u not in covered:
                expected[g[u]] = u
        assert si(g) == tuple(expected)
        assert (si(g) == p167(g)) == all(len(path) == 1 or path[0] < path[1] for path in ps)
        # Decode and compare complete predecessor sets, not just cardinalities.
        nonfixed = {u for u in range(n) if g[u] != u}
        forced_sources = {g[u] for u in nonfixed}
        free = sorted(set(range(n))-forced_sources)
        fixed = sorted(set(range(n))-nonfixed)
        decoded = set()
        for choices in product(fixed, repeat=len(free)):
            candidate_assignments += 1
            f = [-1]*n
            for v in nonfixed:
                f[g[v]] = v
            for u, v in zip(free, choices):
                f[u] = v
            bins = {v: [u for u in free if f[u] == v] for v in fixed}
            if all(len(bins[v]) != 1 or bins[v] == [v] for v in fixed):
                decoded.add(tuple(f))
        assert decoded == reverse[g]
    exact_depth = Counter()
    for f in fs:
        seen = {}
        cur = f
        while cur not in seen:
            seen[cur] = len(seen)
            cur = si(cur)
        mu = seen[cur]
        period = len(seen)-seen[cur]
        assert period in (1, 2)
        g = si(f)
        assert paths(g) is not None
        expected_mu = 0 if len(set(f)) == n else 1+max((len(p)-1 for p in paths(g)), default=0)
        assert mu == expected_mu
        exact_depth[mu] += 1
    # Empty reverse[g] entries can have been inserted by the all-target loop.
    actual_image = sum(bool(pred) for pred in reverse.values())
    assert actual_image == image_count_species(n)
    return {"n": n, "states": len(fs), "shape_targets": shape_targets, "image": actual_image,
            "decoder_candidate_assignments": candidate_assignments,
            "depths": dict(sorted(exact_depth.items())), "all_target_decoder": "PASS",
            "partition_atlas": "PASS", "P167_split_branch_adapter": "PASS",
            "image_species": "PASS", "pointwise_tail": "PASS"}


if __name__ == "__main__":
    for n in range(1, 6):
        print(json.dumps(verify(n), sort_keys=True, separators=(",", ":")))
    g = (2, 0, 2)
    assert p167(g) == (1, 1, 0) and p167(p167(g)) == g
    assert si(g) == (1, 1, 2) and si(si(g)) == (0, 1, 2)
    f = (1, 0, 1)
    s = si(f)
    assert f[s[f[0]]] == 0 != f[0]
    print(json.dumps({"P167_iterate_obstruction": {"g": g, "M_g": p167(g), "S_g": si(g)},
                      "generalized_inverse_obstruction": {"f": f, "S_f": s, "fSf_at_0": f[s[f[0]]]},
                      "assertions": "PASS"}, sort_keys=True, separators=(",", ":")))
