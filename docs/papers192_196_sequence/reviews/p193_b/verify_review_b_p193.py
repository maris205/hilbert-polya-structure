#!/usr/bin/env python3
"""Independent Review-B control for P193.

This program intentionally imports neither paper code nor Review-A code.  It
uses a cut-bit/interval representation, literal nominations, and a recursive
weighted grouping of target intervals.
"""

from collections import Counter
from hashlib import sha256
from itertools import permutations
from math import factorial


N = 8
checks = 0
transitions = 0
digest = sha256()


def demand(condition):
    global checks
    checks += 1
    if not condition:
        raise AssertionError("Review-B check failed")


def cut_intervals(p):
    """Direct-sum blocks from the cut-bit word max(prefix)==length."""
    blocks = []
    left = 0
    running_max = 0
    for right, value in enumerate(p, 1):
        running_max = max(running_max, value)
        if running_max == right:
            blocks.append((left, right))
            left = right
    demand(left == len(p))
    return blocks


def literal_step(p):
    """Compute the two nominations literally, then swap all mutual pairs."""
    global transitions
    transitions += 1
    active = []
    for i, value in enumerate(p):
        later = [(p[j], j) for j in range(i + 1, len(p)) if p[j] < value]
        if not later:
            continue
        chosen_value, j = min(later)
        earlier_larger = [ell for ell in range(j) if p[ell] > chosen_value]
        demand(bool(earlier_larger))
        if min(earlier_larger) == i:
            active.append((i, j))

    used = [v for pair in active for v in pair]
    demand(len(used) == len(set(used)))
    q = list(p)
    for i, j in active:
        q[i], q[j] = q[j], q[i]
    return tuple(q), tuple(active)


def surgery_step(p, intervals):
    q = list(p)
    pairs = []
    for left, right in intervals:
        if right - left == 1:
            continue
        j = min(range(left, right), key=p.__getitem__)
        pairs.append((left, j))
        q[left], q[j] = q[j], q[left]
    return tuple(q), tuple(pairs)


def component_sizes(p):
    return tuple(right - left for left, right in cut_intervals(p))


def grouping_weight(sizes):
    """Sum parent weights over legal consecutive interval groupings.

    This recursion does not use the closed product.  A group may start only at
    a singleton target interval and has weight equal to its terminal interval
    length.
    """
    if not sizes or sizes[0] != 1:
        return 0
    total = 0

    def visit(start, product):
        nonlocal total
        for end in range(start, len(sizes)):
            weight = sizes[end]
            if end + 1 == len(sizes):
                total += product * weight
            elif sizes[end + 1] == 1:
                visit(end + 1, product * weight)

    visit(0, 1)
    return total


def product_weight(sizes):
    if not sizes or sizes[0] != 1:
        return 0
    out = sizes[-1]
    for j in range(1, len(sizes)):
        if sizes[j] == 1:
            out *= 1 + sizes[j - 1]
    return out


def convolution(a, b, n):
    return sum(a[j] * b[n - j] for j in range(n + 1))


depth_by_n = {}
indec_cumulative = {}
all_cumulative = {}
summary = []

for n in range(1, N + 1):
    states = list(permutations(range(1, n + 1)))
    state_set = set(states)
    arrow = {}
    intervals = {}

    for p in states:
        iv = cut_intervals(p)
        intervals[p] = iv
        q, literal_pairs = literal_step(p)
        q2, block_pairs = surgery_step(p, iv)
        demand(q == q2)
        demand(literal_pairs == block_pairs)
        demand(q in state_set)
        if q != p:
            old_cuts = {right for _, right in iv[:-1]}
            new_iv = cut_intervals(q)
            new_cuts = {right for _, right in new_iv[:-1]}
            demand(old_cuts < new_cuts)
        arrow[p] = q

    identity = tuple(range(1, n + 1))
    demand(arrow[identity] == identity)
    depth = {}
    histogram = Counter()
    for p in states:
        seen = set()
        x = p
        d = 0
        while x != identity:
            demand(x not in seen)
            seen.add(x)
            x = arrow[x]
            d += 1
            demand(d <= n - 1)
        depth[p] = d
        histogram[d] += 1

    indegree = Counter(arrow.values())
    indegree_from_indec = Counter(
        arrow[p] for p in states if len(intervals[p]) == 1
    )
    demand(sum(indegree.values()) == factorial(n))
    demand(set(indegree) == {p for p in states if p[0] == 1})

    for target in states:
        sizes = component_sizes(target)
        recursive = grouping_weight(sizes)
        closed = product_weight(sizes)
        actual = indegree[target]
        demand(recursive == closed)
        demand(actual == recursive)

    # Reopen the indecomposable-parent lemma by enumerating incoming sources.
    if n >= 2:
        for gamma in permutations(range(1, n)):
            target = (1,) + tuple(value + 1 for value in gamma)
            incoming_indec = indegree_from_indec[target]
            demand(incoming_indec == component_sizes(gamma)[-1])

    max_depth = max(depth.values())
    deepest = sum(value == max_depth for value in depth.values())
    max_fibre = max(indegree.values())
    maximizers = [p for p in states if indegree[p] == max_fibre]
    demand(max_depth == n - 1)
    demand(deepest == factorial(n - 1))
    demand(max_fibre == 2 ** (n - 1))
    demand(maximizers == [identity])

    depth_by_n[n] = histogram
    for t in range(N):
        all_cumulative[n, t] = sum(count for d, count in histogram.items() if d <= t)
        indec_cumulative[n, t] = sum(
            depth[p] <= t and len(intervals[p]) == 1 for p in states
        )

    for p in states:
        digest.update(
            (repr(p) + ">" + repr(arrow[p]) + ":" + str(depth[p]) +
             ":" + str(indegree[p]) + ";").encode("ascii")
        )

    row = ",".join(f"{d}:{histogram[d]}" for d in sorted(histogram))
    summary.append(
        f"n={n} states={factorial(n)} max_tail={max_depth} "
        f"deepest={deepest} image={len(indegree)} max_fibre={max_fibre} "
        f"depth_hist={row}"
    )

# Independent coefficient attack on both formal identities.
for t in range(N - 1):
    A = [1] + [all_cumulative[n, t] for n in range(1, N + 1)]
    B = [0] + [indec_cumulative[n, t] for n in range(1, N + 1)]
    Bnext = [0] + [indec_cumulative[n, t + 1] for n in range(1, N + 1)]
    for n in range(N + 1):
        demand(convolution(A, [1] + [-x for x in B[1:]], n) == (1 if n == 0 else 0))
    demand(Bnext[1] == 1)
    for n in range(2, N + 1):
        coefficient = sum(A[r] * (n - r - 1) * B[n - r - 1]
                          for r in range(n - 1))
        demand(Bnext[n] == coefficient)

demand([depth_by_n[8][d] for d in range(8)] ==
       [1, 127, 1064, 3484, 7614, 11722, 11268, 5040])

print("P193 independent cut-bit / recursive-grouping Review B")
for line in summary:
    print(line)
print("depth_row_n8=1,127,1064,3484,7614,11722,11268,5040")
print(f"transitions={transitions}")
print(f"assertions={checks}")
print(f"record_digest={digest.hexdigest()}")
print("open_critical=0 open_major=0 open_minor=0")
print("external_state=OWNER_AMBER/HOLD_EXTERNAL")
print("status=PASS")
