#!/usr/bin/env python3
"""Author-side exact scout. Stdlib only; no imported manuscript formula code.

Output is canonical JSON. Finite boxes test but never prove all parameters.
Field 4 uses F_2[z]/(z^2+z+1). All remaining fields here are prime.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import product
from math import gcd, prod
import json


class Field:
    def __init__(self, q):
        self.q = q
    def add(self, a, b):
        return a ^ b if self.q in (2, 4) else (a+b) % self.q
    def neg(self, a):
        return a if self.q in (2, 4) else (-a) % self.q
    def mul(self, a, b):
        if self.q != 4:
            return a*b % self.q
        out = 0
        while b:
            if b & 1:
                out ^= a
            a <<= 1
            if a & 4:
                a ^= 7
            b >>= 1
        return out
    def sum(self, xs):
        out = 0
        for x in xs:
            out = self.add(out, x)
        return out


def graph_stats(nxt):
    n = len(nxt)
    indeg = [0]*n
    for y in nxt:
        indeg[y] += 1
    degree = Counter(indeg)
    queue = deque(i for i, d in enumerate(indeg) if not d)
    peel = []
    while queue:
        x = queue.popleft()
        peel.append(x)
        y = nxt[x]
        indeg[y] -= 1
        if not indeg[y]:
            queue.append(y)
    mu = [0]*n
    for x in reversed(peel):
        mu[x] = mu[nxt[x]]+1
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
    return {"states": n, "image": n-degree[0], "core": len(seen),
            "tail_max": max(mu), "tail_census": dict(sorted(Counter(mu).items())),
            "cycles": dict(sorted(cycles.items())), "fibre_max": max(degree),
            "fibre_max_targets": degree[max(degree)]}


def emit(label, params, nxt, assertions=None):
    row = {"candidate": label, "parameters": params, **graph_stats(nxt)}
    if assertions is not None:
        assertions(row)
        row["assertions"] = "PASS"
    print(json.dumps(row, sort_keys=True, separators=(",", ":")), flush=True)


def matrix_tools(n, q):
    f = Field(q)
    mats = list(product(range(q), repeat=n*n))
    ids = {v: i for i, v in enumerate(mats)}
    def add(a, b):
        return tuple(f.add(x, y) for x, y in zip(a, b))
    def neg(a):
        return tuple(f.neg(x) for x in a)
    def mul(a, b):
        return tuple(f.sum(f.mul(a[i*n+k], b[k*n+j]) for k in range(n))
                     for i in range(n) for j in range(n))
    def comm(a, b):
        return add(mul(a, b), neg(mul(b, a)))
    def trace(a):
        return f.sum(a[i*n+i] for i in range(n))
    return f, mats, ids, add, neg, mul, comm, trace


def matrix_scout():
    for n, q in ((2, 2), (2, 3), (2, 4), (3, 2)):
        f, mats, ids, add, neg, mul, comm, trace = matrix_tools(n, q)
        for label in ("JS", "TM", "TF"):
            nxt = []
            for a in mats:
                if label == "JS":
                    b = add(a, mul(a, a))
                elif label == "TM":
                    at = tuple(a[j*n+i] for i in range(n) for j in range(n))
                    b = comm(a, at)
                else:
                    tr = trace(a)
                    tr_i = tuple(tr if i == j else 0 for i in range(n) for j in range(n))
                    b = mul(a, add(tr_i, neg(a)))
                nxt.append(ids[b])
            emit(label, {"n": n, "q": q}, nxt)
    for q in (2, 4):
        f, mats, ids, add, neg, mul, comm, trace = matrix_tools(2, q)
        k = len(mats)
        nxt = [ids[comm(a, b)]*k+ids[add(a, b)] for a in mats for b in mats]
        # Compare every literal one-step fibre against the affine-centralizer claim.
        fibres = Counter(nxt)
        for i, c in enumerate(mats):
            for j, s in enumerate(mats):
                scalar = s[1] == s[2] == 0 and s[0] == s[3]
                possible = c == (0, 0, 0, 0) if scalar else trace(c) == trace(mul(c, s)) == 0
                expected = (q**4 if scalar else q**2) if possible else 0
                assert fibres[i*k+j] == expected, (q, c, s, expected, fibres[i*k+j])
        # All-time claim after two steps, including exact maximizing targets.
        two = Counter(nxt[nxt[x]] for x in range(k*k))
        three = Counter(nxt[nxt[nxt[x]]] for x in range(k*k))
        assert two == three
        for i, c in enumerate(mats):
            for j, s in enumerate(mats):
                target = i*k+j
                if trace(s):
                    expected = q**2 if trace(c) == trace(mul(c, s)) == 0 else 0
                elif c != (0, 0, 0, 0):
                    expected = 0
                else:
                    scalar = s[1] == s[2] == 0 and s[0] == s[3]
                    expected = q**5+q**4-q**3 if scalar else q**4-q**3
                assert two[target] == expected, ("two", q, c, s, two[target], expected)
        def check(row):
            assert row["image"] == q**6-q**3+q
            assert row["core"] == q**6-q**5+q**3
            assert row["tail_census"][2] == q**7-2*q**5+q**3
            assert row["cycles"][1] == q**4
            assert row["cycles"][2] == (q**5-q**3)//2
            if q == 4:
                assert row["cycles"][3] == 2*(q**5-q**3)//3
            assert row["fibre_max"] == q**4
            assert row["fibre_max_targets"] == q
        emit("CS", {"q": q}, nxt, check)


def gaussian(n, k, q):
    return prod(q**(n-i)-1 for i in range(k))//prod(q**(k-i)-1 for i in range(k))


def sp_order(m, q):
    return q**(m*m)*prod(q**(2*i)-1 for i in range(1, m+1))


def subspace_scout():
    for q, d in ((2, 2), (3, 2), (4, 2), (2, 4), (3, 4)):
        f = Field(q)
        vecs = list(product(range(q), repeat=d))
        vid = {v: i for i, v in enumerate(vecs)}
        zero = 1
        def members(mask):
            while mask:
                bit = mask & -mask
                yield bit.bit_length()-1
                mask -= bit
        vadd = [[vid[tuple(f.add(a, b) for a, b in zip(v, w))] for w in vecs] for v in vecs]
        scale = [[vid[tuple(f.mul(a, x) for x in v)] for a in range(q)] for v in vecs]
        def extend(mask, v):
            return sum(1 << w for w in {vadd[u][av] for u in members(mask) for av in scale[v]})
        spaces = {zero}
        frontier = [zero]
        for u in frontier:
            for v in range(q**d):
                if not ((u >> v) & 1):
                    w = extend(u, v)
                    if w not in spaces:
                        spaces.add(w)
                        frontier.append(w)
        spaces = sorted(spaces)
        sid = {s: i for i, s in enumerate(spaces)}
        def dim(mask):
            k, size = 0, mask.bit_count()
            while size > 1:
                assert size % q == 0
                k += 1
                size //= q
            return k
        m = d//2
        orth = []
        for v in vecs:
            mask = 0
            for wi, w in enumerate(vecs):
                dot = f.sum(f.add(f.mul(v[i], w[m+i]), f.neg(f.mul(v[m+i], w[i]))) for i in range(m))
                if dot == 0:
                    mask |= 1 << wi
            orth.append(mask)
        whole = (1 << (q**d))-1
        perp = []
        for u in spaces:
            mask = whole
            for v in members(u):
                mask &= orth[v]
            perp.append(mask)
        k = len(spaces)
        nxt = [j*k+sid[perp[i] & perp[j]] for i in range(k) for j in range(k)]
        # Orthogonal-complement intersection computes literal (U+V)^perp.
        fibres = Counter(nxt)
        for i, x in enumerate(spaces):
            for j, y in enumerate(spaces):
                target = i*k+j
                if x & perp[j] != x:
                    expected = 0
                else:
                    a, b = dim(x), dim(perp[j])-dim(x)
                    expected = sum(gaussian(a, ell, q)*q**((a-ell)*b) for ell in range(a+1))
                assert fibres[target] == expected, (q, d, i, j, expected, fibres[target])
        for x in range(k*k):
            y = x
            trace6 = [x]
            for _ in range(6):
                y = nxt[y]
                trace6.append(y)
            assert trace6[6] == trace6[3]
            u, v = divmod(trace6[3], k)
            assert spaces[u] & perp[v] == spaces[u]
            assert spaces[u] & perp[u] == spaces[v] & perp[v]
        recurrent = 0
        for r in range(m+1):
            isotropic = gaussian(m, r, q)*prod(q**(m-i)+1 for i in range(r))
            s = m-r
            decomposition = sum(sp_order(s, q)//(sp_order(a, q)*sp_order(b, q)*sp_order(s-a-b, q))
                                for a in range(s+1) for b in range(s-a+1))
            recurrent += isotropic*decomposition
        fixed = prod(q**i+1 for i in range(1, m+1))
        def check(row):
            assert row["core"] == recurrent
            assert row["cycles"] == {1: fixed, 3: (recurrent-fixed)//3}
            assert row["tail_max"] == 3
            assert row["fibre_max"] == sum(gaussian(d, ell, q) for ell in range(d+1))
            assert row["fibre_max_targets"] == 1
        emit("OF", {"q": q, "dimension": d, "subspaces": k}, nxt, check)


def arithmetic_scout():
    for p in (2, 3, 5):
        fs = list(product(range(p), repeat=p))
        ids = {f: i for i, f in enumerate(fs)}
        nxt = [ids[tuple((f[f[x]]-f[x]) % p for x in range(p))] for f in fs]
        emit("FC", {"p": p}, nxt)
    for n in (2, 3, 4, 6, 8, 9, 10, 12, 15):
        nxt = [(gcd(a, b, n) % n)*n+(a+b) % n for a in range(n) for b in range(n)]
        emit("GH", {"N": n}, nxt)
    for n in (4, 8, 12, 16, 36, 60, 100, 144, 300, 1020100):
        ds = [d for d in range(1, n+1) if n % d == 0]
        ids = {d: i for i, d in enumerate(ds)}
        nxt = [ids[gcd(n, d+n//d)] for d in ds]
        emit("DS", {"N": n}, nxt)


if __name__ == "__main__":
    matrix_scout()
    subspace_scout()
    arithmetic_scout()
