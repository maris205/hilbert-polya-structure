#!/usr/bin/env python3
"""Deterministic exact falsifier for the second algebraic replacement pool.

This is a breadth-stage verifier, not a proof and not a novelty test.  Every
state space below is enumerated literally.  The output is intentionally stable
so that CANONICAL.txt can be cold-replayed and diffed.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import permutations, product
from math import comb


ASSERTIONS = 0
TOTAL_STATES = 0
LINES: list[str] = []


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def inv0(x: int, p: int) -> int:
    return 0 if x % p == 0 else pow(x, -1, p)


def chi(x: int, p: int) -> int:
    x %= p
    if x == 0:
        return 0
    return 1 if pow(x, (p - 1) // 2, p) == 1 else -1


def compact_counter(c: Counter[int]) -> str:
    return ",".join(f"{k}:{c[k]}" for k in sorted(c))


def graph_profile(states, step, label: str):
    """Return exact finite-functional-graph statistics.

    The orbit solver is global and handles both newly discovered cycles and
    paths merging into an already resolved component.
    """
    global TOTAL_STATES
    states = list(states)
    state_set = set(states)
    check(len(state_set) == len(states), f"{label}: duplicate carrier states")
    TOTAL_STATES += len(states)
    nxt = {}
    for x in states:
        y = step(x)
        check(y in state_set, f"{label}: update left carrier at {x!r}")
        nxt[x] = y

    fibres = Counter(nxt.values())
    resolved = {}
    cycle_counts: Counter[int] = Counter()
    for start in states:
        if start in resolved:
            continue
        path = []
        index = {}
        u = start
        while u not in resolved and u not in index:
            index[u] = len(path)
            path.append(u)
            u = nxt[u]
        if u in resolved:
            depth, period = resolved[u]
            for v in reversed(path):
                depth += 1
                resolved[v] = (depth, period)
        else:
            j = index[u]
            cycle = path[j:]
            period = len(cycle)
            cycle_counts[period] += 1
            for v in cycle:
                resolved[v] = (0, period)
            depth = 0
            for v in reversed(path[:j]):
                depth += 1
                resolved[v] = (depth, period)

    check(len(resolved) == len(states), f"{label}: unresolved states")
    for x in states:
        dx, px = resolved[x]
        dy, py = resolved[nxt[x]]
        check(px == py, f"{label}: period changed on an edge")
        check(dx == 0 or dx == dy + 1, f"{label}: bad depth recursion")
    tails = Counter(d for d, _ in resolved.values())
    recurrent = tails[0]
    check(recurrent == sum(k * v for k, v in cycle_counts.items()),
          f"{label}: cycle census mismatch")
    mapping_digest = sha256(
        "\n".join(f"{x!r}->{nxt[x]!r}" for x in states).encode()
    ).hexdigest()[:16]
    return {
        "states": len(states),
        "image": len(fibres),
        "max_fibre": max(fibres.values()),
        "recurrent": recurrent,
        "max_tail": max(tails),
        "tails": tails,
        "cycles": cycle_counts,
        "fibres": fibres,
        "next": nxt,
        "resolved": resolved,
        "digest": mapping_digest,
    }


def record(handle: str, box: str, g) -> None:
    LINES.append(
        f"{handle} {box} states={g['states']} image={g['image']} "
        f"maxf={g['max_fibre']} rec={g['recurrent']} "
        f"maxt={g['max_tail']} cycles={compact_counter(g['cycles'])} "
        f"tails={compact_counter(g['tails'])} mapsha={g['digest']}"
    )


# ---------------------------------------------------------------------------
# QCD: quadratic-character drift, x -> x + chi(x), chi(0)=0.


def verify_qcd() -> None:
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
        step = lambda x, p=p: (x + chi(x, p)) % p
        g = graph_profile(range(p), step, f"QCD p={p}")
        c2 = (p - chi(-1, p)) // 4
        double_targets = (
            (p - 1 + chi(2, p) - chi(-2, p)) // 4
            + (1 + chi(-1, p)) // 2
        )
        check(g["cycles"] == Counter({1: 1, 2: c2}),
              f"QCD p={p}: fixed/2-cycle theorem failed")
        check(g["max_fibre"] <= 2, f"QCD p={p}: fibre above two")
        check(sum(v == 2 for v in g["fibres"].values()) == double_targets,
              f"QCD p={p}: double-fibre formula failed")
        check(g["image"] == p - double_targets,
              f"QCD p={p}: image formula failed")
        record("QCD", f"p={p}", g)


# ---------------------------------------------------------------------------
# ESP: elementary-symmetric plane map, (x,y) -> (xy,x+y).


def verify_esp() -> None:
    for p in (3, 5, 7, 11, 13, 17, 19, 23):
        states = [(x, y) for x in range(p) for y in range(p)]
        step = lambda s, p=p: (s[0] * s[1] % p, (s[0] + s[1]) % p)
        g = graph_profile(states, step, f"ESP p={p}")
        check(g["image"] == p * (p + 1) // 2,
              f"ESP p={p}: image formula failed")
        check(g["max_fibre"] == 2, f"ESP p={p}: max fibre")
        hist = Counter(g["fibres"].values())
        check(hist == Counter({1: p, 2: p * (p - 1) // 2}),
              f"ESP p={p}: Vieta fibre histogram failed")
        record("ESP", f"p={p}", g)


# ---------------------------------------------------------------------------
# AHP: totalized arithmetic/harmonic pair.
# (x,y) -> (x+y, xy inv0(x+y)).


def verify_ahp() -> None:
    for p in (3, 5, 7, 11, 13, 17, 19, 23):
        states = [(x, y) for x in range(p) for y in range(p)]

        def step(s, p=p):
            x, y = s
            u = (x + y) % p
            return u, x * y * inv0(u, p) % p

        g = graph_profile(states, step, f"AHP p={p}")
        check(g["image"] == (p * p + 1) // 2,
              f"AHP p={p}: image formula failed")
        check(g["max_fibre"] == p, f"AHP p={p}: max fibre")
        check(g["fibres"][(0, 0)] == p, f"AHP p={p}: singular fibre")
        for target, size in g["fibres"].items():
            check(target == (0, 0) or size <= 2,
                  f"AHP p={p}: nonsingular fibre above two")
        record("AHP", f"p={p}", g)


# ---------------------------------------------------------------------------
# CCS: character-controlled squaring.
# Quadratic residues (and zero) are fixed; nonresidues are squared.


def verify_ccs() -> None:
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
        step = lambda x, p=p: x if chi(x, p) >= 0 else x * x % p
        g = graph_profile(range(p), step, f"CCS p={p}")
        check(g["cycles"] == Counter({1: (p + 1) // 2}),
              f"CCS p={p}: fixed count")
        check(g["tails"] == Counter({0: (p + 1) // 2, 1: (p - 1) // 2}),
              f"CCS p={p}: one-step silhouette")
        check(g["image"] == (p + 1) // 2, f"CCS p={p}: image")
        record("CCS", f"p={p}", g)


# ---------------------------------------------------------------------------
# Permutation helpers used by HUR, KRC, and CWR-style owner checks.


def pcompose(a, b):
    """a after b."""
    return tuple(a[b[i]] for i in range(len(a)))


def pinverse(a):
    ans = [0] * len(a)
    for i, j in enumerate(a):
        ans[j] = i
    return tuple(ans)


# HUR: two-strand Hurwitz braid move (a,b)->(b,b^{-1}ab).


def verify_hur() -> None:
    for n in (2, 3, 4, 5):
        group = list(permutations(range(n)))
        states = [(a, b) for a in group for b in group]

        def step(s):
            a, b = s
            return b, pcompose(pinverse(b), pcompose(a, b))

        g = graph_profile(states, step, f"HUR n={n}")
        check(g["image"] == len(states) and g["max_fibre"] == 1,
              f"HUR n={n}: not a permutation")
        check(g["recurrent"] == len(states) and g["max_tail"] == 0,
              f"HUR n={n}: tail in braid action")
        for a, b in states:
            c, d = step((a, b))
            recovered = (pcompose(c, pcompose(d, pinverse(c))), c)
            check(recovered == (a, b), f"HUR n={n}: inverse failed")
            check(pcompose(a, b) == pcompose(c, d),
                  f"HUR n={n}: product invariant failed")
        record("HUR", f"n={n}", g)


# ---------------------------------------------------------------------------
# MRK: Markoff Vieta rotor on x^2+y^2+z^2=3xyz over F_p.


def verify_mrk() -> None:
    for p in (5, 7, 11, 13, 17, 19, 23):
        states = [
            (x, y, z)
            for x in range(p) for y in range(p) for z in range(p)
            if (x * x + y * y + z * z - 3 * x * y * z) % p == 0
        ]
        step = lambda s, p=p: (s[1], s[2], (3 * s[1] * s[2] - s[0]) % p)
        g = graph_profile(states, step, f"MRK p={p}")
        check(g["image"] == len(states) and g["max_fibre"] == 1,
              f"MRK p={p}: Vieta rotor not bijective")
        for s in states:
            a, b, c = step(s)
            recovered = ((3 * a * b - c) % p, a, b)
            check(recovered == s, f"MRK p={p}: inverse failed")
        record("MRK", f"p={p}", g)


# ---------------------------------------------------------------------------
# CLU: zero-totalized rank-two cluster/QRT map.
# (x,y) -> (y,(1+y^2)inv0(x)).


def verify_clu() -> None:
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
        states = [(x, y) for x in range(p) for y in range(p)]

        def step(s, p=p):
            x, y = s
            return y, (1 + y * y) * inv0(x, p) % p

        g = graph_profile(states, step, f"CLU p={p}")
        if p % 4 == 3:
            check(g["image"] == p * p and g["max_fibre"] == 1,
                  f"CLU p={p}: expected nonsingular permutation")
            check(g["recurrent"] == p * p and g["max_tail"] == 0,
                  f"CLU p={p}: unexpected tails")
        for x, y in states:
            z = step((x, y))[1]
            if x and y and z:
                k = (x * x + y * y + 1) * inv0(x * y % p, p) % p
                check(z == (k * y - x) % p,
                      f"CLU p={p}: linear recurrence reduction failed")
                y2, z2 = step((y, z))
                if y2 and z2:
                    k2 = (y2 * y2 + z2 * z2 + 1) * inv0(y2 * z2 % p, p) % p
                    check(k2 == k, f"CLU p={p}: invariant failed")
        record("CLU", f"p={p}", g)


# ---------------------------------------------------------------------------
# Polynomial helpers for SFE and PRE.  Coefficients are low-to-high.


def ptrim(f):
    f = list(f)
    while f and f[-1] == 0:
        f.pop()
    return tuple(f)


def pderivative(f, p):
    return ptrim(tuple(i * f[i] % p for i in range(1, len(f))))


def pscale(f, a, p):
    return ptrim(tuple(a * x % p for x in f))


def pdivmod(f, g, p):
    f = list(ptrim(f))
    g = ptrim(g)
    check(bool(g), "polynomial division by zero")
    q = [0] * max(0, len(f) - len(g) + 1)
    invlead = pow(g[-1], -1, p)
    while f and len(f) >= len(g):
        shift = len(f) - len(g)
        coeff = f[-1] * invlead % p
        q[shift] = coeff
        for i, gi in enumerate(g):
            f[i + shift] = (f[i + shift] - coeff * gi) % p
        while f and f[-1] == 0:
            f.pop()
    return ptrim(q), tuple(f)


def pgcd(f, g, p):
    f, g = ptrim(f), ptrim(g)
    while g:
        _, r = pdivmod(f, g, p)
        f, g = g, r
    if not f:
        return ()
    return pscale(f, pow(f[-1], -1, p), p)


def monic_polynomials(p, n):
    ans = [(1,)]
    for d in range(1, n + 1):
        ans.extend(tuple(low) + (1,) for low in product(range(p), repeat=d))
    return ans


# SFE: squarefree erosion, f -> monic gcd(f,f').


def verify_sfe() -> None:
    for p, n in ((3, 2), (5, 3), (7, 4), (11, 4)):
        states = monic_polynomials(p, n)
        step = lambda f, p=p: pgcd(f, pderivative(f, p), p)
        g = graph_profile(states, step, f"SFE p={p} n={n}")
        check(g["cycles"] == Counter({1: 1}), f"SFE p={p},n={n}: recurrent")
        check(g["max_tail"] == n, f"SFE p={p},n={n}: sharp depth")
        witness = (0,) * n + (1,)
        check(g["resolved"][witness][0] == n,
              f"SFE p={p},n={n}: x^n not sharp")
        for f in states:
            if f != (1,):
                check(len(step(f)) < len(f), f"SFE p={p},n={n}: degree not reduced")
        record("SFE", f"p={p},n={n}", g)


# ---------------------------------------------------------------------------
# GCM: Gram-cube A -> A A^T A on 2x2 matrices.


def mmul(a, b, p):
    return (
        (a[0] * b[0] + a[1] * b[2]) % p,
        (a[0] * b[1] + a[1] * b[3]) % p,
        (a[2] * b[0] + a[3] * b[2]) % p,
        (a[2] * b[1] + a[3] * b[3]) % p,
    )


def verify_gcm() -> None:
    for p in (2, 3, 5, 7):
        states = list(product(range(p), repeat=4))

        def step(a, p=p):
            at = (a[0], a[2], a[1], a[3])
            return mmul(mmul(a, at, p), a, p)

        g = graph_profile(states, step, f"GCM p={p}")
        record("GCM", f"p={p}", g)


# ---------------------------------------------------------------------------
# BHD: typed binary-Hessian descent: cubic -> Hessian quadratic ->
# discriminant scalar -> sink.  The grading is deliberately part of the state.


def verify_bhd() -> None:
    for p in (5, 7, 11):
        sink = ("Z",)
        cubics = [("C",) + s for s in product(range(p), repeat=4)]
        quads = [("Q",) + s for s in product(range(p), repeat=3)]
        scalars = [("S", s) for s in range(p)]
        states = [sink] + scalars + quads + cubics

        def step(s, p=p):
            if s[0] == "Z":
                return s
            if s[0] == "S":
                return ("Z",)
            if s[0] == "Q":
                _, a, b, c = s
                return ("S", (b * b - 4 * a * c) % p)
            _, a, b, c, d = s
            return (
                "Q",
                (3 * a * c - b * b) % p,
                (9 * a * d - b * c) % p,
                (3 * b * d - c * c) % p,
            )

        g = graph_profile(states, step, f"BHD p={p}")
        expected_tails = Counter({0: 1, 1: p, 2: p ** 3, 3: p ** 4})
        check(g["tails"] == expected_tails, f"BHD p={p}: typed grading")
        check(g["cycles"] == Counter({1: 1}), f"BHD p={p}: sink")
        record("BHD", f"p={p}", g)


# ---------------------------------------------------------------------------
# PRE: bounded polynomial-remainder Euclidean dynamics.
# (f,g)->(g,rem(f,g)), with (f,0) fixed.


def all_polynomials(p, n):
    return sorted(
        {ptrim(v) for v in product(range(p), repeat=n + 1)},
        key=lambda f: (len(f), f),
    )


def verify_pre() -> None:
    for p, n in ((2, 3), (3, 2), (5, 2)):
        polys = all_polynomials(p, n)
        states = [(f, g) for f in polys for g in polys]

        def step(s, p=p):
            f, g = s
            if not g:
                return s
            _, r = pdivmod(f, g, p)
            return g, r

        g = graph_profile(states, step, f"PRE p={p} n={n}")
        check(set(g["cycles"]) == {1}, f"PRE p={p},n={n}: nonfixed cycle")
        check(g["recurrent"] == len(polys), f"PRE p={p},n={n}: terminals")
        check(g["max_tail"] <= n + 1, f"PRE p={p},n={n}: Euclid bound")
        for f, h in states:
            if h:
                _, r = pdivmod(f, h, p)
                check(len(r) < len(h), f"PRE p={p},n={n}: remainder degree")
        record("PRE", f"p={p},n={n}", g)


# ---------------------------------------------------------------------------
# KRC: Kreweras complement on noncrossing set partitions.


def set_partitions(n):
    """Canonical tuples of sorted blocks of {0,...,n-1}."""
    parts = [((0,),)]
    for x in range(1, n):
        new = []
        for part in parts:
            for i in range(len(part)):
                blocks = list(part)
                blocks[i] = blocks[i] + (x,)
                new.append(tuple(blocks))
            new.append(part + ((x,),))
        parts = new
    return parts


def noncrossing(part) -> bool:
    owner = {}
    for i, block in enumerate(part):
        for x in block:
            owner[x] = i
    n = sum(map(len, part))
    for a in range(n):
        for c in range(a + 1, n):
            if owner[a] == owner[c]:
                for b in range(a + 1, c):
                    for d in range(c + 1, n):
                        if owner[b] == owner[d] and owner[b] != owner[a]:
                            return False
    return True


def partition_permutation(part):
    n = sum(map(len, part))
    ans = list(range(n))
    for block in part:
        for a, b in zip(block, block[1:] + block[:1]):
            ans[a] = b
    return tuple(ans)


def verify_krc() -> None:
    for n in range(2, 9):
        nc = [p for p in set_partitions(n) if noncrossing(p)]
        states = [partition_permutation(p) for p in nc]
        cycle = tuple(list(range(1, n)) + [0])
        state_set = set(states)
        step = lambda pi, cycle=cycle: pcompose(pinverse(pi), cycle)
        for pi in states:
            check(step(pi) in state_set, f"KRC n={n}: complement left NC(n)")
        g = graph_profile(states, step, f"KRC n={n}")
        catalan = comb(2 * n, n) // (n + 1)
        check(len(states) == catalan, f"KRC n={n}: Catalan carrier count")
        check(g["image"] == len(states) and g["max_fibre"] == 1,
              f"KRC n={n}: not a permutation")
        check(g["max_tail"] == 0, f"KRC n={n}: tail")
        record("KRC", f"n={n}", g)


# ---------------------------------------------------------------------------
# NWT: zero-totalized Newton map for f=x^3-x over F_p.
# N(x)=x-(x^3-x)inv0(3x^2-1).


def verify_nwt() -> None:
    for p in (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43):
        def step(x, p=p):
            f = (x * x * x - x) % p
            d = (3 * x * x - 1) % p
            return (x - f * inv0(d, p)) % p

        g = graph_profile(range(p), step, f"NWT p={p}")
        expected_fixed = 3 + (2 if chi(3, p) == 1 else 0)
        check(g["cycles"][1] == expected_fixed,
              f"NWT p={p}: root/critical fixed count")
        check(g["max_fibre"] <= 4, f"NWT p={p}: cubic inverse bound")
        for y in range(p):
            for x in range(p):
                d = (3 * x * x - 1) % p
                if d:
                    cubic = (2 * x ** 3 - 3 * y * x * x + y) % p
                    check((step(x) == y) == (cubic == 0),
                          f"NWT p={p}: cubic inverse equation")
        record("NWT", f"p={p}", g)


def main() -> None:
    verify_qcd()
    verify_esp()
    verify_ahp()
    verify_ccs()
    verify_hur()
    verify_mrk()
    verify_clu()
    verify_sfe()
    verify_gcm()
    verify_bhd()
    verify_pre()
    verify_krc()
    verify_nwt()
    profile_hash = sha256("\n".join(LINES).encode()).hexdigest()
    print("ALGEBRAIC_REPLACEMENT2_CANONICAL_V1")
    for line in LINES:
        print(line)
    print(f"BOXES={len(LINES)}")
    print(f"TOTAL_STATES={TOTAL_STATES}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print(f"PROFILE_SHA256={profile_hash}")
    print("STATUS=EXACT_REPLAY_PASS__NOT_PROOF__NOT_NOVELTY")


if __name__ == "__main__":
    main()
