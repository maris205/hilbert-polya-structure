#!/usr/bin/env python3
"""Deterministic exact controls for the nonlinear-algebra replacement scout.

Enumeration is counterexample pressure, not proof or an ownership certificate.
No third-party packages are used.
"""

from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
from hashlib import sha256


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def iterate(f, x, t):
    for _ in range(t):
        x = f(x)
    return x


def graph_stats(states, f):
    states = tuple(states)
    state_set = set(states)
    image = {}
    indegree = Counter()
    for x in states:
        y = f(x)
        check(y in state_set, "map is not closed")
        image[x] = y
        indegree[y] += 1
    cycles = set()
    tails = {}
    for start in states:
        path = []
        at = {}
        x = start
        while x not in at and x not in tails:
            at[x] = len(path)
            path.append(x)
            x = image[x]
        if x in at:
            j = at[x]
            cyc = tuple(path[j:])
            cycles.add(frozenset(cyc))
            for z in cyc:
                tails[z] = 0
            d = 0
            for z in reversed(path[:j]):
                d += 1
                tails[z] = d
        else:
            d = tails[x]
            for z in reversed(path):
                d += 1
                tails[z] = d
    cycle_hist = Counter(len(c) for c in cycles)
    check(len(tails) == len(states))
    check(sum(indegree.values()) == len(states))
    check(sum(k * v for k, v in Counter(indegree.values()).items()) == len(states))
    return {
        "states": len(states),
        "image": len(indegree),
        "fixed": sum(image[x] == x for x in states),
        "height": max(tails.values(), default=0),
        "cycles": dict(sorted(cycle_hist.items())),
        "indegree": dict(sorted(Counter(indegree.values()).items())),
    }


def sig(code, params, stats):
    print(
        f"{code} {params} S={stats['states']} I={stats['image']} "
        f"F={stats['fixed']} H={stats['height']} "
        f"C={stats['cycles']} D={stats['indegree']}"
    )


# ---------------------------------------------------------------------------
# Class-two Heisenberg windows.


def heisenberg(p):
    return tuple(product(range(p), repeat=3))


def hmul(x, y, p):
    a, b, z = x
    c, d, w = y
    return ((a + c) % p, (b + d) % p, (z + w + a * d) % p)


def hcomm(x, y, p):
    a, b, _ = x
    c, d, _ = y
    return (0, 0, (a * d - c * b) % p)


def group_windows():
    codes = []
    for code in ("NL01", "NL02"):
        for p in (2, 3):
            H = heisenberg(p)
            e = (0, 0, 0)
            states = tuple(product(H, repeat=2))
            if code == "NL01":
                f = lambda s, p=p: (s[1], hcomm(s[0], s[1], p))
                for s in states:
                    check(iterate(f, s, 3) == (e, e), "sliding commutator depth")
            else:
                f = lambda s, p=p: (hmul(s[0], s[1], p), hcomm(s[0], s[1], p))
                for s in states:
                    check(iterate(f, s, 3) == iterate(f, s, 2), "product-commutator settles")
            sig(code, f"p={p}", graph_stats(states, f))
        codes.append(code)

    for code in ("NL03", "NL04", "NL05", "NL06"):
        for p in (2, 3):
            H = heisenberg(p)
            e = (0, 0, 0)
            states = tuple(product(H, repeat=3))
            if code == "NL03":
                f = lambda s, p=p: (
                    hcomm(s[1], s[2], p),
                    hcomm(s[2], s[0], p),
                    hcomm(s[0], s[1], p),
                )
                for s in states:
                    check(iterate(f, s, 2) == (e, e, e), "commutator triangle depth")
            elif code == "NL04":
                f = lambda s, p=p: (s[1], s[2], hcomm(s[0], s[2], p))
                for s in states:
                    check(iterate(f, s, 4) == (e, e, e), "delayed commutator depth")
            elif code == "NL05":
                f = lambda s, p=p: (
                    hmul(s[0], s[1], p),
                    hmul(s[1], s[2], p),
                    hcomm(s[0], s[2], p),
                )
                for s in states:
                    out = f(s)
                    lhs = tuple((g[0], g[1]) for g in out)
                    x, y, z = (tuple(g[:2]) for g in s)
                    rhs = (
                        ((x[0] + y[0]) % p, (x[1] + y[1]) % p),
                        ((y[0] + z[0]) % p, (y[1] + z[1]) % p),
                        (0, 0),
                    )
                    check(lhs == rhs, "quotient recurrence mismatch")
            else:
                f = lambda s, p=p: (
                    hmul(hcomm(s[0], s[1], p), hcomm(s[1], s[2], p), p),
                    hmul(hcomm(s[1], s[2], p), hcomm(s[2], s[0], p), p),
                    hmul(hcomm(s[2], s[0], p), hcomm(s[0], s[1], p), p),
                )
                for s in states:
                    check(iterate(f, s, 2) == (e, e, e), "central circuit depth")
            sig(code, f"p={p}", graph_stats(states, f))
        codes.append(code)
    return codes


# ---------------------------------------------------------------------------
# Nilpotent semigroup recurrence windows.


def word_semigroup(alphabet, cap):
    words = [None]
    for n in range(1, cap + 1):
        words.extend("".join(w) for w in product(alphabet, repeat=n))
    return tuple(words)


def wmul(u, v, cap):
    if u is None or v is None or len(u) + len(v) > cap:
        return None
    return u + v


def thue_patterns(t):
    A, B = (0,), (1,)
    for _ in range(t):
        A, B = A + B, B + A
    return A, B


def parse_blocks(word, pattern, a, b):
    pos = 0
    values = {}
    for bit in pattern:
        width = a if bit == 0 else b
        block = word[pos : pos + width]
        pos += width
        if bit in values and values[bit] != block:
            return None
        values[bit] = block
    return values if pos == len(word) else None


def twc_target_fibre(A, B, t, cap, alphabet_size):
    total = len(word_semigroup(tuple(str(i) for i in range(alphabet_size)), cap)) ** 2
    if A is None or B is None:
        if (A, B) != (None, None):
            return 0
        cutoff = cap // (1 << (t - 1))
        live = sum((s - 1) * alphabet_size**s for s in range(2, cutoff + 1))
        return total - live
    if len(A) != len(B) or len(A) % (1 << (t - 1)):
        return 0
    s = len(A) // (1 << (t - 1))
    PA, PB = thue_patterns(t)
    count = 0
    for a in range(1, s):
        b = s - a
        va = parse_blocks(A, PA, a, b)
        vb = parse_blocks(B, PB, a, b)
        if va is not None and vb is not None and va == vb:
            count += 1
    return count


def check_twc_atlas(alphabet, cap):
    S = word_semigroup(alphabet, cap)
    states = tuple(product(S, repeat=2))
    f = lambda s: (wmul(s[0], s[1], cap), wmul(s[1], s[0], cap))
    q = len(alphabet)
    for t in range(1, 1 + (cap.bit_length())):
        fibres = Counter(iterate(f, s, t) for s in states)
        for target in states:
            check(
                fibres[target] == twc_target_fibre(target[0], target[1], t, cap, q),
                "all-time truncated-word fibre atlas",
            )
    one = Counter(f(s) for s in states)
    nonzero = {target: n for target, n in one.items() if target != (None, None)}
    expected_max = max(0, cap - 1)
    check(max(nonzero.values(), default=0) == max(1, expected_max))
    if cap >= 3:
        maximizers = {target for target, n in nonzero.items() if n == cap - 1}
        constants = {(a * cap, a * cap) for a in alphabet}
        check(maximizers == constants, "nonzero-fibre extremizers")


def path_semigroup(n):
    return (None,) + tuple((i, j) for i in range(n) for j in range(i + 1, n))


def pmul(x, y):
    if x is None or y is None or x[1] != y[0]:
        return None
    return (x[0], y[1])


def umul(a, b):
    # Strictly upper 3x3 matrices over F_2, bits 01,02,12.
    return ((a & 1) * ((b >> 2) & 1)) << 1


def decreasing_maps(n):
    return tuple((0,) + tail for tail in product(*(range(i) for i in range(1, n))))


def tcompose(f, g):
    return tuple(f[g[i]] for i in range(len(f)))


def semigroup_windows():
    codes = []
    for code, cap in (("NL07", 4), ("NL08", 4), ("NL09", 3)):
        S = word_semigroup("ab", cap)
        if code in ("NL07", "NL08"):
            states = tuple(product(S, repeat=2))
            if code == "NL07":
                f = lambda s, cap=cap: (wmul(s[0], s[1], cap), wmul(s[1], s[0], cap))
                for u, v in states:
                    if u is not None and v is not None:
                        out = f((u, v))
                        if len(u) + len(v) <= cap:
                            check(out == (u + v, v + u), "word conjugacy output")
                        else:
                            check(out == (None, None), "overflow sink")
                for q, h in ((2, 2), (2, 3), (2, 4), (2, 5), (3, 3)):
                    alphabet = tuple(str(i) for i in range(q))
                    check_twc_atlas(alphabet, h)
            else:
                f = lambda s, cap=cap: (
                    wmul(wmul(s[0], s[1], cap), s[0], cap),
                    wmul(wmul(s[1], s[0], cap), s[1], cap),
                )
        else:
            states = tuple(product(S, repeat=3))
            f = lambda s, cap=cap: (
                wmul(s[0], s[1], cap),
                wmul(s[1], s[2], cap),
                wmul(s[2], s[0], cap),
            )
        sig(code, f"alphabet=2,cap={cap}", graph_stats(states, f))
        codes.append(code)

    S = path_semigroup(5)
    states = tuple(product(S, repeat=2))
    f = lambda s: (pmul(s[0], s[1]), s[1])
    for s in states:
        check(iterate(f, s, 3) == iterate(f, s, 2), "path accumulator settles")
    sig("NL10", "path=5", graph_stats(states, f))
    codes.append("NL10")

    S = tuple(range(8))
    states = tuple(product(S, repeat=2))
    f = lambda s: (umul(s[0], s[1]), umul(umul(s[0], s[1]), s[0]))
    for s in states:
        check(iterate(f, s, 2) == (0, 0), "UT3 product window must vanish")
    sig("NL11", "UT3(F2)", graph_stats(states, f))
    codes.append("NL11")

    S = decreasing_maps(5)
    zero = tuple(0 for _ in range(5))
    states = tuple(product(S, repeat=2))
    f = lambda s: (
        tcompose(tcompose(s[0], s[1]), s[0]),
        tcompose(s[1], s[0]),
    )
    for s in states:
        check(iterate(f, s, 3) == (zero, zero), "decreasing transformation words must vanish")
    sig("NL12", "decreasing-transformations=5", graph_stats(states, f))
    codes.append("NL12")
    return codes


# ---------------------------------------------------------------------------
# Nonlinear finite-ring / finite-algebra maps.


def mmul(A, B, p):
    a, b, c, d = A
    e, f, g, h = B
    return (
        (a * e + b * g) % p,
        (a * f + b * h) % p,
        (c * e + d * g) % p,
        (c * f + d * h) % p,
    )


def mscale(c, A, p):
    return tuple((c * x) % p for x in A)


def ring_maps():
    codes = []
    for p in (3, 5):
        states = tuple(product(range(p), repeat=2))
        f = lambda s, p=p: (s[0], s[0] * s[1] % p)
        for s in states:
            for t in range(1, 5):
                check(iterate(f, s, t) == (s[0], pow(s[0], t, p) * s[1] % p))
        sig("NL13", f"p={p}", graph_stats(states, f))
    codes.append("NL13")

    for p in (3, 5):
        states = tuple(product(range(p), repeat=2))
        f = lambda s, p=p: (s[0] * s[1] % p, s[0] * (1 - s[1]) % p)
        indeg = Counter(f(s) for s in states)
        for u, v in states:
            expected = p if (u, v) == (0, 0) else (1 if (u + v) % p else 0)
            check(indeg[(u, v)] == expected, "splitter fibre law")
        sig("NL14", f"p={p}", graph_stats(states, f))
    codes.append("NL14")

    for p in (3, 5, 7):
        states = tuple(product(range(p), repeat=2))
        f = lambda s, p=p: (s[0] * s[1] % p, (s[0] - s[1]) % p)
        indeg = Counter(f(s) for s in states)
        for u, v in states:
            disc = (v * v + 4 * u) % p
            roots = sum((x * x) % p == disc for x in range(p))
            check(indeg[(u, v)] == roots, "multiplicative-difference discriminant")
        sig("NL15", f"p={p}", graph_stats(states, f))
    codes.append("NL15")

    for p in (2, 3):
        mats = tuple(product(range(p), repeat=4))
        I = (1, 0, 0, 1)
        f = lambda A, p=p: tuple(
            (A[i] + ((A[0] * A[3] - A[1] * A[2]) % p) * I[i]) % p
            for i in range(4)
        )
        sig("NL16", f"M2(F{p})", graph_stats(mats, f))
    codes.append("NL16")

    for p in (2, 3, 5):
        mats = tuple(product(range(p), repeat=4))
        zero = (0, 0, 0, 0)
        f = lambda A, p=p: (A[1] * A[2] % p, 0, 0, 0)
        for A in mats:
            check(iterate(f, A, 2) == zero, "Peirce collapse depth")
        sig("NL17", f"M2(F{p})", graph_stats(mats, f))
    codes.append("NL17")

    for p in (2, 3):
        mats = tuple(product(range(p), repeat=4))
        N = (0, 1, 0, 0)
        f = lambda A, p=p: mmul(mmul(A, N, p), A, p)
        for A in mats:
            check(iterate(f, A, 2) == mscale(A[2] * A[2] % p, f(A), p))
        sig("NL18", f"sandwich-M2(F{p})", graph_stats(mats, f))
    codes.append("NL18")
    return codes


# ---------------------------------------------------------------------------
# Rank-changing module and configuration maps over F_2.


def span_mask(vectors):
    span = {0}
    for v in vectors:
        span |= {x ^ v for x in tuple(span)}
    return sum(1 << x for x in span)


def vectors(mask, n):
    return tuple(v for v in range(1 << n) if (mask >> v) & 1)


def all_subspaces(n):
    seen = {1}
    todo = [1]
    while todo:
        U = todo.pop()
        for v in range(1, 1 << n):
            if not ((U >> v) & 1):
                W = span_mask(vectors(U, n) + (v,))
                if W not in seen:
                    seen.add(W)
                    todo.append(W)
    return tuple(sorted(seen))


def product_space(U, n, mul):
    vals = [mul(x, y) for x in vectors(U, n) for y in vectors(U, n)]
    return span_mask(vals)


def poly_mul3(a, b):
    out = 0
    for i in range(3):
        for j in range(3 - i):
            if ((a >> i) & 1) and ((b >> j) & 1):
                out ^= 1 << (i + j)
    return out


def heis_bracket(a, b):
    return (((a & 1) * ((b >> 1) & 1)) ^ (((a >> 1) & 1) * (b & 1))) << 2


def exterior_mul(a, b):
    # Basis 1,e1,e2,e12 indexed by subset masks 0,1,2,3.
    out = 0
    for i in range(4):
        for j in range(4):
            if ((a >> i) & 1) and ((b >> j) & 1) and not (i & j):
                out ^= 1 << (i | j)
    return out


def outer(l, r):
    return (
        ((l & 1) * (r & 1))
        | (((l & 1) * ((r >> 1) & 1)) << 1)
        | ((((l >> 1) & 1) * (r & 1)) << 2)
        | ((((l >> 1) & 1) * ((r >> 1) & 1)) << 3)
    )


def rectangular_hull(U):
    cols, rows = [], []
    for A in vectors(U, 4):
        cols.extend(((A & 1) | (((A >> 2) & 1) << 1), ((A >> 1) & 1) | (((A >> 3) & 1) << 1)))
        rows.extend(((A & 1) | (((A >> 1) & 1) << 1), ((A >> 2) & 1) | (((A >> 3) & 1) << 1)))
    L, R = span_mask(cols), span_mask(rows)
    return span_mask(outer(l, r) for l in vectors(L, 2) for r in vectors(R, 2))


def module_maps():
    codes = []
    subs4 = all_subspaces(4)
    check(len(subs4) == 67, "Gaussian subspace count n=4")
    one = 15
    states = tuple(U for U in subs4 if (U >> one) & 1)
    f = lambda U: product_space(U, 4, lambda x, y: x & y)
    for U in states:
        check((f(U) | U) == f(U), "unital Schur square must expand")
    sig("NL19", "unital-binary-codes,n=4", graph_stats(states, f))
    codes.append("NL19")

    subs3 = all_subspaces(3)
    check(len(subs3) == 16, "Gaussian subspace count n=3")
    f = lambda U: product_space(U, 3, poly_mul3)
    sig("NL20", "subspaces-F2[x]/x3", graph_stats(subs3, f))
    codes.append("NL20")

    f = lambda U: product_space(U, 3, heis_bracket)
    for U in subs3:
        check(iterate(f, U, 2) == 1, "class-two Lie derived collapse")
    sig("NL21", "Heisenberg-Lie-subspaces", graph_stats(subs3, f))
    codes.append("NL21")

    f = lambda U: product_space(U, 4, exterior_mul)
    sig("NL22", "exterior-algebra-2gen", graph_stats(subs4, f))
    codes.append("NL22")

    pair_states = tuple(product(subs3, repeat=2))
    f = lambda s: (span_mask(vectors(s[0], 3) + vectors(s[1], 3)), s[0] & s[1])
    for s in pair_states:
        check(iterate(f, s, 2) == f(s), "subspace comparator idempotence")
    sig("NL23", "subspace-pairs-F2^3", graph_stats(pair_states, f))
    codes.append("NL23")

    f = rectangular_hull
    for U in subs4:
        check(iterate(f, U, 2) == f(U), "tensor-support hull idempotence")
        check((f(U) | U) == f(U), "tensor-support hull contains source")
    sig("NL24", "matrix-subspaces-M2(F2)", graph_stats(subs4, f))
    codes.append("NL24")
    return codes


def main():
    print("REPLACEMENT_NONLINEAR_ALGEBRA_SCOUT_V1")
    print("EXACT_ENUMERATION_IS_COUNTEREXAMPLE_PRESSURE_ONLY")
    codes = group_windows() + semigroup_windows() + ring_maps() + module_maps()
    check(codes == [f"NL{i:02d}" for i in range(1, 25)], "candidate ledger mismatch")
    check(len(set(codes)) == 24)
    print("CANDIDATES=24 GROUP=6 SEMIGROUP=6 RING_ALGEBRA=6 MODULE_CONFIG=6")
    print("RETAINED=0 TOP=NONE EMPTY_POOL=YES")
    print("KILLED=24")
    print(f"ASSERTIONS={ASSERTIONS}")
    script_hash = sha256(Path(__file__).read_bytes()).hexdigest()
    print(f"SCRIPT_SHA256={script_hash}")
    print("STATUS=PASS HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
