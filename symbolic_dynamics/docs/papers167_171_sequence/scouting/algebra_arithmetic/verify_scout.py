#!/usr/bin/env python3
"""Deterministic breadth pilots for the P167--P171 algebra lane.

These are deliberately small exact boxes.  They are a screening device, not
evidence for an asymptotic theorem.  Every row is a different literal update.
"""

from __future__ import annotations

import json
from collections import Counter, deque
from itertools import combinations, combinations_with_replacement, permutations, product

from verify_qis import QuarticField, all_subspaces as quartic_subspaces, image as inverse_span


def profile(name, states, step, box):
    states = tuple(states)
    index = {x: i for i, x in enumerate(states)}
    assert len(index) == len(states)
    edges = []
    for x in states:
        y = step(x)
        assert y in index, (name, x, y)
        edges.append(index[y])
    recurrent = set()
    cycles = set()
    tails = []
    for start in range(len(states)):
        seen, path = {}, []
        x = start
        while x not in seen:
            seen[x] = len(path)
            path.append(x)
            x = edges[x]
        mu = seen[x]
        cyc = tuple(sorted(path[mu:]))
        cycles.add(cyc)
        recurrent.update(cyc)
        tails.append(mu)
    periods = Counter(len(c) for c in cycles)
    indeg = Counter(edges)
    return {
        "id": name,
        "box": box,
        "states": len(states),
        "image": len(set(edges)),
        "fixed": sum(i == y for i, y in enumerate(edges)),
        "recurrent": len(recurrent),
        "max_tail": max(tails, default=0),
        "depths": dict(sorted(Counter(tails).items())),
        "cycles": dict(sorted(periods.items())),
        "max_fibre": max(indeg.values(), default=0),
    }


def vec_digits(x, p, n):
    ans = []
    for _ in range(n):
        ans.append(x % p)
        x //= p
    return ans


def vec_encode(v, p):
    ans, place = 0, 1
    for x in v:
        ans += (x % p) * place
        place *= p
    return ans


def span(vectors, p, n):
    rows = [vec_digits(v, p, n) for v in vectors if v]
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col] % p), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inv = pow(rows[rank][col], -1, p)
        rows[rank] = [(inv * z) % p for z in rows[rank]]
        for i in range(len(rows)):
            if i != rank and rows[i][col] % p:
                c = rows[i][col]
                rows[i] = [(a - c * b) % p for a, b in zip(rows[i], rows[rank])]
        rank += 1
    return tuple(vec_encode(row, p) for row in rows[:rank])


def subspaces(p, n):
    out = []
    for k in range(n + 1):
        for pivots in combinations(range(n), k):
            free = [(i, j) for i, pivot in enumerate(pivots) for j in range(pivot + 1, n) if j not in pivots]
            for vals in product(range(p), repeat=len(free)):
                rows = [[0] * n for _ in range(k)]
                for i, pivot in enumerate(pivots):
                    rows[i][pivot] = 1
                for (i, j), val in zip(free, vals):
                    rows[i][j] = val
                out.append(tuple(vec_encode(row, p) for row in rows))
    assert len(out) == len(set(out))
    return tuple(out)


def space_members(space, p, n):
    rows = [vec_digits(v, p, n) for v in space]
    out = []
    for coeffs in product(range(p), repeat=len(rows)):
        v = [0] * n
        for c, row in zip(coeffs, rows):
            for j in range(n):
                v[j] = (v[j] + c * row[j]) % p
        out.append(vec_encode(v, p))
    return tuple(out)


def pilot_qis():
    field = QuarticField(2)
    spaces = quartic_subspaces(2)
    return profile("QIS", spaces, lambda a: inverse_span(a, field), "F2-subspaces of F16")


def pilot_cis():
    p, n = 5, 3
    spaces = subspaces(p, n)

    def step(space):
        vals = []
        for x in space_members(space, p, n):
            v = vec_digits(x, p, n)
            vals.append(vec_encode((0 if a == 0 else pow(a, p - 2, p) for a in v), p))
        return span(vals, p, n)

    return profile("CIS", spaces, step, "F5-subspaces of F5^3")


def hull(space, n):
    members = space_members(space, 2, n)
    return span(
        (x for x in members if all((x & b).bit_count() % 2 == 0 for b in space)),
        2,
        n,
    )


def pilot_hull_shortening(project):
    n = 6
    spaces = subspaces(2, n)

    def step(space):
        h = hull(space, n)
        support = 0
        for x in h:
            support |= x
        if project:
            return span((x & ~support for x in space), 2, n)
        return span((x for x in space_members(space, 2, n) if not (x & support)), 2, n)

    tag = "HSP" if project else "HSS"
    literal = "hull-support projection" if project else "hull-support shortening"
    return profile(tag, spaces, step, f"binary length 6; {literal}")


def pilot_exterior_square():
    types = [()]
    for r in range(1, 4):
        types += list(combinations_with_replacement(range(1, 7), r))
    # combinations are increasing; store invariant factors in decreasing order.
    types = tuple(tuple(reversed(x)) for x in types)

    def step(lam):
        factors = [min(lam[i], lam[j]) for i in range(len(lam)) for j in range(i + 1, len(lam))]
        return tuple(sorted(factors, reverse=True))

    return profile("EAF", types, step, "abelian p-types: exponent <=6, rank <=3")


def partial_bijections(n):
    out = []
    ground = tuple(range(n))
    for k in range(n + 1):
        for dom in combinations(ground, k):
            for image in combinations(ground, k):
                for perm in permutations(image):
                    f = [-1] * n
                    for a, b in zip(dom, perm):
                        f[a] = b
                    out.append(tuple(f))
    return tuple(out)


def pilot_partial_square():
    n = 4
    states = partial_bijections(n)

    def step(f):
        return tuple(-1 if f[i] < 0 or f[f[i]] < 0 else f[f[i]] for i in range(n))

    return profile("SQS", states, step, "symmetric inverse monoid I_4; f -> f^2")


def d16_mul(a, b):
    i, j = a % 8, a // 8
    k, ell = b % 8, b // 8
    return ((i + (-1 if j else 1) * k) % 8) + 8 * ((j + ell) % 2)


def d16_inv(a):
    return next(b for b in range(16) if d16_mul(a, b) == d16_mul(b, a) == 0)


def generated_d16(seed):
    h = {0, *seed}
    changed = True
    while changed:
        changed = False
        for a in tuple(h):
            for b in tuple(h):
                c = d16_mul(a, b)
                if c not in h:
                    h.add(c)
                    changed = True
    return frozenset(h)


def d16_subgroups():
    found = {frozenset({0})}
    queue = deque(found)
    while queue:
        h = queue.popleft()
        for g in range(16):
            if g not in h:
                k = generated_d16((*h, g))
                if k not in found:
                    found.add(k)
                    queue.append(k)
    return tuple(sorted(found, key=lambda x: (len(x), tuple(x))))


def d16_comm(a, b):
    return d16_mul(d16_mul(d16_mul(d16_inv(a), d16_inv(b)), a), b)


def pilot_d16(frattini):
    states = d16_subgroups()

    def step(h):
        gens = [d16_comm(a, b) for a in h for b in h]
        if frattini:
            gens += [d16_mul(a, a) for a in h]
        return generated_d16(gens)

    return profile("DFR" if frattini else "DRS", states, step, "subgroups of D16")


def pilot_partial_shift(adaptive):
    n = 5
    spaces = subspaces(2, n)

    def shift(x, power=1):
        return (x << power) & ((1 << n) - 1)

    def step(space):
        if adaptive:
            return span((shift(x, len(space)) for x in space), 2, n)
        cut = (x for x in space_members(space, 2, n) if x < (1 << (n - 1)))
        return span((shift(x) for x in cut), 2, n)

    return profile(
        "ARI" if adaptive else "PLS",
        spaces,
        step,
        "F2-subspaces of F2^5; rank-adaptive shift" if adaptive else "F2-subspaces of F2^5; partial shift",
    )


def pilot_det_feedback():
    p = 3
    states = tuple(product(range(p), repeat=4))

    def step(a):
        det = (a[0] * a[3] - a[1] * a[2]) % p
        return tuple(det * x % p for x in a)

    return profile("DFM", states, step, "M2(F3); A -> det(A)A")


def pilot_linear_feedback():
    p = 5
    states = tuple(product(range(p), repeat=3))

    def step(v):
        ell = sum(v) % p
        return tuple(ell * x % p for x in v)

    return profile("LFM", states, step, "F5^3; v -> (sum v_i)v")


def mat_mul(a, b, p):
    return (
        (a[0] * b[0] + a[1] * b[2]) % p,
        (a[0] * b[1] + a[1] * b[3]) % p,
        (a[2] * b[0] + a[3] * b[2]) % p,
        (a[2] * b[1] + a[3] * b[3]) % p,
    )


def pilot_cosquare():
    p = 3
    states = tuple(a for a in product(range(p), repeat=4) if (a[0] * a[3] - a[1] * a[2]) % p)

    def step(a):
        det = (a[0] * a[3] - a[1] * a[2]) % p
        invdet = pow(det, -1, p)
        inv_transpose = (a[3] * invdet % p, -a[2] * invdet % p, -a[1] * invdet % p, a[0] * invdet % p)
        return mat_mul(inv_transpose, a, p)

    return profile("CSM", states, step, "GL2(F3); A -> A^{-T}A")


def pilot_square_annihilator_ideal():
    e = 12
    states = tuple(range(e + 1))
    return profile(
        "SAI",
        states,
        lambda a: max(min(2 * a, e), e - a),
        "ideals (p^a) of Z/p^12; I -> I^2 intersect Ann(I)",
    )


def pilot_degree_frobenius_filter():
    m = 12
    states = tuple(range(1 << m))

    def step(mask):
        degree = sum(i + 1 for i in range(m) if mask >> i & 1)
        if not degree:
            return 0
        return sum(1 << i for i in range(m) if mask >> i & 1 and degree % (i + 1) == 0)

    return profile("DFF", states, step, "one irreducible factor of each degree 1..12")


def pilot_parallel_abacus():
    n, weight = 8, 4
    states = tuple(x for x in range(1 << n) if x.bit_count() == weight)

    def step(x):
        y = x
        for i in range(n - 1):
            if (x >> i) & 3 == 1:  # left-to-right bits at i,i+1 are 1,0
                y ^= 3 << i
        return y

    return profile("PAF", states, step, "4 beads on a linear 8-runner binary abacus")


def pilot_matrix_fibonacci():
    p = 2
    mats = tuple(product(range(p), repeat=4))
    states = tuple(product(mats, repeat=2))
    return profile("MFP", states, lambda ab: (mat_mul(ab[0], ab[1], p), ab[0]), "M2(F2)^2; (A,B)->(AB,A)")


def main():
    rows = [
        pilot_qis(),
        pilot_cis(),
        pilot_hull_shortening(False),
        pilot_hull_shortening(True),
        pilot_exterior_square(),
        pilot_partial_square(),
        pilot_d16(True),
        pilot_d16(False),
        pilot_partial_shift(False),
        pilot_partial_shift(True),
        pilot_det_feedback(),
        pilot_linear_feedback(),
        pilot_cosquare(),
        pilot_square_annihilator_ideal(),
        pilot_degree_frobenius_filter(),
        pilot_parallel_abacus(),
        pilot_matrix_fibonacci(),
    ]
    assert len(rows) >= 15
    assert len({row["id"] for row in rows}) == len(rows)
    print("P167-P171 algebra/arithmetic breadth canonical v1")
    for row in rows:
        print(json.dumps(row, sort_keys=True, separators=(",", ":")))
    print(f"PASS literal_systems={len(rows)}")


if __name__ == "__main__":
    main()
