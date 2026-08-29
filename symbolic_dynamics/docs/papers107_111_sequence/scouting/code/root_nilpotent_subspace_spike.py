#!/usr/bin/env python3
"""Exact discovery spike for U -> U + N U under one regular nilpotent block."""

from itertools import combinations, product


def rank_mod(rows, q):
    a = [list(row) for row in rows if any(x % q for x in row)]
    if not a:
        return 0
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c] % q), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][c] % q, -1, q)
        a[r] = [(x * inv) % q for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c] % q:
                z = a[i][c] % q
                a[i] = [(x - z * y) % q for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def nilpotent_shift(row):
    return tuple(row[1:]) + (0,)


def saturation_step(rows, q):
    candidates = list(rows) + [nilpotent_shift(row) for row in rows]
    basis = []
    for row in candidates:
        if rank_mod(basis + [row], q) > len(basis):
            basis.append(row)
    return tuple(basis)


def subspace_equal(a, b, q):
    return rank_mod(list(a) + list(b), q) == rank_mod(a, q) == rank_mod(b, q)


def pivot_gap_depth(pivots):
    if not pivots:
        return 0
    gaps = [pivots[0] - 1]
    gaps.extend(pivots[i] - pivots[i - 1] - 1 for i in range(1, len(pivots)))
    return max(gaps)


def schubert_weight(pivots, q):
    return q ** sum(p - i for i, p in enumerate(pivots, start=1))


def rref_cells(d, q):
    yield (), (), 1
    for k in range(1, d + 1):
        for pivots in combinations(range(1, d + 1), k):
            free = []
            pivot_set = set(pivots)
            for i, p in enumerate(pivots):
                for c in range(1, p):
                    if c not in pivot_set:
                        free.append((i, c - 1))
            assert len(free) == sum(p - i for i, p in enumerate(pivots, start=1))
            for values in product(range(q), repeat=len(free)):
                rows = [[0] * d for _ in range(k)]
                for i, p in enumerate(pivots):
                    rows[i][p - 1] = 1
                for (i, c), value in zip(free, values):
                    rows[i][c] = value
                yield tuple(tuple(row) for row in rows), pivots, schubert_weight(pivots, q)


def run_case(d, q):
    assertions = 0
    observed = {}
    cell_seen = {}
    mismatch_count = 0
    first_mismatch = None
    for rows, pivots, cell_weight in rref_cells(d, q):
        cell_seen[pivots] = cell_seen.get(pivots, 0) + 1
        predicted = pivot_gap_depth(pivots)
        current = rows
        tau = 0
        while True:
            nxt = saturation_step(current, q)
            if subspace_equal(current, nxt, q):
                break
            current = nxt
            tau += 1
            assert tau <= d
        if tau != predicted:
            mismatch_count += 1
            if first_mismatch is None:
                first_mismatch = (pivots, rows, tau, predicted)
        endpoint_dim = pivots[-1] if pivots else 0
        assert rank_mod(current, q) == endpoint_dim
        assertions += 1
        observed[tau] = observed.get(tau, 0) + 1
    for pivots, count in cell_seen.items():
        assert count == schubert_weight(pivots, q)
        assertions += 1
    assert observed.get(0, 0) == d + 1
    assertions += 1
    assert max(observed) == d - 1 if d > 1 else max(observed) == 0
    assertions += 1
    return assertions, sum(observed.values()), observed, mismatch_count, first_mismatch


def run():
    assertions = 0
    cases = []
    for q, max_d in ((2, 7), (3, 5), (5, 4)):
        for d in range(1, max_d + 1):
            checked, states, profile, mismatches, first = run_case(d, q)
            assertions += checked
            cases.append((q, d, states, profile, mismatches, first))
    witness = next(case for case in cases if case[4])
    assert witness[0:2] == (2, 4)
    assertions += 1
    print("root nilpotent-subspace spike: EXPECTED FALSIFICATION PASS")
    print(f"exact assertions: {assertions}")
    print(f"cases: {len(cases)}")
    print(f"first coefficient-sensitive case: q={witness[0]}, d={witness[1]}, witness={witness[5]}")
    for q, d, states, profile, mismatches, _ in cases[-5:]:
        print(f"q={q}, d={d}, subspaces={states}, depth_profile={profile}, pivot_mismatches={mismatches}")


if __name__ == "__main__":
    run()
