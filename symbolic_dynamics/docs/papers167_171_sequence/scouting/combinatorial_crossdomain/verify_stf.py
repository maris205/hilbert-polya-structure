#!/usr/bin/env python3
"""Exact verifier for successor transfer on canonical set partitions.

The program has no third-party dependencies.  It verifies finite carriers; it
does not pretend that finite checks prove the theorems recorded in the audit.
The five-state transfer formula is checked against literal predecessor counts
for every target through n=9.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product
from math import factorial


ASSERTIONS = 0


def check(test: bool) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not test:
        raise AssertionError


def rgs_words(n: int):
    """All restricted-growth words of length n, in lexical order."""
    if n == 0:
        yield ()
        return

    def rec(prefix, maximum):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for a in range(maximum + 2):
            prefix.append(a)
            yield from rec(prefix, max(maximum, a))
            prefix.pop()

    yield from rec([0], 0)


def is_rgs(w) -> bool:
    if not w:
        return True
    if w[0] != 0:
        return False
    maximum = 0
    for a in w[1:]:
        if a > maximum + 1:
            return False
        maximum = max(maximum, a)
    return True


def stf(w):
    """Increment the final occurrence of each repeated letter, cyclically."""
    if not w:
        return w
    k = max(w) + 1
    if k == 1:
        return w
    count = [0] * k
    last = [0] * k
    for j, a in enumerate(w):
        count[a] += 1
        last[a] = j
    ans = list(w)
    for a in range(k):
        if count[a] >= 2:
            ans[last[a]] = (a + 1) % k
    return tuple(ans)


def is_recurrent_form(w) -> bool:
    if len(w) <= 1:
        return True
    k = max(w) + 1
    if k in (1, len(w)):
        return True
    m = len(w) - k
    if m >= k:
        return len(set(w[:m])) == k and len(set(w[-k:])) == k
    return w[:k] == tuple(range(k)) and len(set(w[-m:])) == m


def tail_and_period(w):
    seen = {}
    u = w
    while u not in seen:
        seen[u] = len(seen)
        u = stf(u)
    return seen[u], len(seen) - seen[u]


def stirling2(n: int, k: int) -> int:
    row = [1] + [0] * k
    for _ in range(n):
        row = [0] + [j * row[j] + row[j - 1] for j in range(1, k + 1)]
    return row[k]


def falling(k: int, m: int) -> int:
    return factorial(k) // factorial(k - m)


# A state describes the chosen incoming element relative to its target block.
NONE, SINGLETON, MINIMUM, MAXIMUM, INTERIOR = range(5)
NSTATES = 5


def category_values(block, state):
    if state == NONE:
        return (None,)
    if state == SINGLETON:
        return tuple(block) if len(block) == 1 else ()
    if state == MINIMUM:
        return (block[0],) if len(block) >= 2 else ()
    if state == MAXIMUM:
        return (block[-1],) if len(block) >= 2 else ()
    return tuple(block[1:-1]) if len(block) >= 3 else ()


def retained_extrema(block, incoming_state):
    """(size, minimum, maximum) after deleting the encoded incoming token."""
    if incoming_state == NONE:
        return len(block), block[0], block[-1]
    choices = category_values(block, incoming_state)
    if not choices:
        return None
    size = len(block) - 1
    if not size:
        return 0, None, None
    if incoming_state in (SINGLETON, MINIMUM):
        minimum = block[1]
    else:
        minimum = block[0]
    if incoming_state in (SINGLETON, MAXIMUM):
        maximum = block[-2]
    else:
        maximum = block[-1]
    return size, minimum, maximum


def blocks(w):
    k = max(w) + 1
    return tuple(tuple(j for j, a in enumerate(w) if a == i) for i in range(k))


def local_matrix(target_blocks, i):
    """The explicit five-state local inverse matrix M_i."""
    k = len(target_blocks)
    current = target_blocks[i]
    nxt = target_blocks[(i + 1) % k]
    matrix = [[0] * NSTATES for _ in range(NSTATES)]
    for incoming in range(NSTATES):
        retained = retained_extrema(current, incoming)
        if retained is None:
            continue
        rsize, rmin, rmax = retained
        for outgoing in range(NSTATES):
            for x in category_values(nxt, outgoing):
                # No outgoing token means the source block must be singleton;
                # an outgoing token means it must have a retained element and
                # the outgoing token must be its strict maximum.
                if outgoing == NONE:
                    if rsize != 1:
                        continue
                elif rsize == 0 or x <= rmax:
                    continue

                # Canonical source blocks have strictly increasing minima.
                # There is deliberately no cyclic comparison after block k-1.
                if i < k - 1:
                    nxt_retained = retained_extrema(nxt, outgoing)
                    if nxt_retained is None or nxt_retained[0] == 0:
                        continue
                    if rsize == 0 or rmin >= nxt_retained[1]:
                        continue
                matrix[incoming][outgoing] += 1
    return matrix


def matmul(a, b):
    return [
        [sum(a[i][h] * b[h][j] for h in range(NSTATES)) for j in range(NSTATES)]
        for i in range(NSTATES)
    ]


def fibre_formula(target):
    target_blocks = blocks(target)
    ans = [[int(i == j) for j in range(NSTATES)] for i in range(NSTATES)]
    for i in range(len(target_blocks)):
        ans = matmul(ans, local_matrix(target_blocks, i))
    return sum(ans[i][i] for i in range(NSTATES))


def queue_step(z):
    fired = [int(a > 0) for a in z]
    return tuple(z[i] - fired[i] + fired[i - 1] for i in range(len(z)))


def cone_height(z, t, i):
    """Max-plus solution H_i(t), with a sufficiently long periodic lift."""
    k = len(z)

    def height(j):
        q, r = divmod(j, k)
        return q * sum(z) + sum(z[: r + 1])

    return max(height(i - j) - (t - j) for j in range(t + 1))


def verify_queue_cones():
    tests = 0
    for k in range(1, 8):
        for z in product(range(4), repeat=k):
            if sum(z) > 10:
                continue
            u = z
            for t in range(k):
                for i in range(k):
                    # The max-plus height difference is the literal queue.
                    recovered = cone_height(z, t, i) - cone_height(z, t, i - 1)
                    check(recovered == u[i])
                    cone_mass = sum(z[(i - j) % k] for j in range(t + 1))
                    if u[i] == 0:
                        check(cone_mass <= t)
                    if u[i] >= 2:
                        check(cone_mass >= t + 2)
                    tests += 1
                u = queue_step(u)

            m = sum(z)
            if m == 0:
                continue
            u = z
            horizon = min(m, k) - 1
            for _ in range(horizon):
                u = queue_step(u)
            if m <= k:
                check(max(u) <= 1)
            if m >= k:
                check(min(u) >= 1)
    return tests


def verify_stf_carriers(nmax=10):
    rows = []
    for n in range(1, nmax + 1):
        states = tuple(rgs_words(n))
        by_k = defaultdict(list)
        recurrent = Counter()
        period_counts = Counter()
        max_tail = 0
        witness = None
        for w in states:
            v = stf(w)
            check(is_rgs(v))
            check(max(v) == max(w))
            tail, period = tail_and_period(w)
            max_tail = max(max_tail, tail)
            if tail == max_tail:
                witness = w
            k = max(w) + 1
            by_k[k].append(tail)
            check((tail == 0) == is_recurrent_form(w))
            if tail == 0:
                recurrent[k] += 1
                period_counts[period] += 1
                check(period == (1 if k in (1, n) else k))

        expected_clock = 0 if n == 1 else n - 2
        check(max_tail == expected_clock)
        for k in range(1, n + 1):
            stratum_clock = 0 if k in (1, n) else min(n - 2, 2 * k - 2)
            check(max(by_k[k]) == stratum_clock)
            if k in (1, n):
                expected = 1
            else:
                m = n - k
                expected = factorial(k) * stirling2(m, k) if m >= k else falling(k, m)
            check(recurrent[k] == expected)
        rows.append((n, len(states), max_tail, dict(sorted(period_counts.items())), witness))
    return rows


def verify_fibres(nmax=9):
    rows = []
    targets_checked = 0
    for n in range(1, nmax + 1):
        states = tuple(rgs_words(n))
        literal = Counter(stf(w) for w in states)
        image = 0
        maximum = 0
        for target in states:
            formula = fibre_formula(target)
            check(formula == literal[target])
            image += formula > 0
            maximum = max(maximum, formula)
            targets_checked += 1
        rows.append((n, len(states), image, maximum))

    # Fibre size is not a disguised function of block sizes and endpoint data.
    a = (0, 1, 0, 1, 1, 0)  # 025|134
    b = (0, 1, 1, 0, 1, 0)  # 035|124
    check(tuple((len(c), c[0], c[-1]) for c in blocks(a)) ==
          tuple((len(c), c[0], c[-1]) for c in blocks(b)))
    check(fibre_formula(a) == 2)
    check(fibre_formula(b) == 1)
    return rows, targets_checked


def verify_sharp_family(limit=50):
    for n in range(2, limit + 1):
        for k in range(2, n):
            # All excess letters are initially stacked at 0.  This one family
            # realizes the sharp clock in every nontrivial k-block stratum.
            w = (0,) * (n - k + 1) + tuple(range(1, k))
            tail, period = tail_and_period(w)
            check(tail == min(n - 2, 2 * k - 2))
            check(period == k)


def main():
    print("P167_171_STF_EXACT_AUDIT_V1")
    queue_tests = verify_queue_cones()
    carrier_rows = verify_stf_carriers()
    fibre_rows, targets = verify_fibres()
    verify_sharp_family()
    print("QUEUE_CONE_CASES", queue_tests)
    for row in carrier_rows:
        print("CARRIER", row)
    for row in fibre_rows:
        print("FIBRE", row)
    print("FIBRE_TARGETS", targets)
    print("STRATUM_CLOCK", "min(n-2,2k-2)", "VERIFIED_N_LE_10")
    print("SHARP_WITNESS", "0^(n-k+1)12...(k-1)", "VERIFIED_N_LE_50")
    print("FIBRE_FORMULA", "TRACE_OF_5_STATE_LOCAL_PRODUCT")
    print("ASSERTIONS", ASSERTIONS)
    print("STATUS PASS")


if __name__ == "__main__":
    main()
