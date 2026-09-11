"""One bounded noncontributor check. No arguments, data reads or file writes."""
from collections import deque
from itertools import combinations, product
import json


def carrier(n, mass):
    for bars in combinations(range(mass + n - 1), n - 1):
        cuts = (-1,) + bars + (mass + n - 1,)
        yield tuple(cuts[j + 1] - cuts[j] - 1 for j in range(n))


def forward(a):
    n = len(a)
    return tuple(max(a[i] - a[(i + 1) % n], 0)
                 + min(a[i - 1], a[i]) for i in range(n))


def graph(states):
    succ = {a: forward(a) for a in states}
    pred = {a: set() for a in states}
    for a, b in succ.items():
        assert b in pred, ("closure", a, b)
        pred[b].add(a)
    deg = {a: len(pred[a]) for a in states}
    queue = deque(a for a in states if deg[a] == 0)
    order = []
    while queue:
        a = queue.popleft()
        order.append(a)
        b = succ[a]
        deg[b] -= 1
        if deg[b] == 0:
            queue.append(b)
    core = tuple(a for a in states if deg[a])
    assert all(succ[a] == a for a in core), ("nonfixed_cycle", core)
    depth = {a: 0 for a in core}
    terminal = {a: a for a in core}
    for a in reversed(order):
        depth[a] = depth[succ[a]] + 1
        terminal[a] = terminal[succ[a]]
    return succ, pred, depth, terminal


def terminal_formula(a):
    m = min(a)
    r = [x - m for x in a]
    n = len(a)
    if not any(r):
        return a
    cut = r.index(0)
    answer = [m] * n
    accumulated = 0
    for j in range(1, n + 1):
        i = (cut + j) % n
        accumulated += r[i]
        if r[(i + 1) % n] == 0:
            answer[i] += accumulated
            accumulated = 0
    assert accumulated == 0
    return tuple(answer)


def flux_sources(y):
    n = len(y)
    out = set()
    for q in product(*(range(y[(i + 1) % n] + 1) for i in range(n))):
        u = [y[i] - q[i - 1] for i in range(n)]
        v = [y[(i + 1) % n] + q[(i + 1) % n] - 2 * q[i]
             for i in range(n)]
        if any(x < 0 or z < 0 or x * z for x, z in zip(u, v)):
            continue
        a = tuple(u[i] + q[i] for i in range(n))
        assert a not in out, ("nonunique_flux", y, q, a)
        out.add(a)
    return out


branch_counts = {"r1": 0, "r2": 0, "r3plus": 0,
                 "descent_parity_reject": 0, "empty_interval": 0,
                 "positive_words": 0, "two_free_intervals": 0}


def chamber_sources(y):
    n = len(y)
    if n <= 2:
        return {y}
    out = {y} if len(set(y)) == 1 else set()
    for bits in product((0, 1), repeat=n):
        if min(bits) == max(bits):
            continue
        starts = [i for i in range(n) if bits[i] and not bits[i - 1]]
        data = []
        assigned = {}
        valid = True
        for start in starts:
            peak = start
            while bits[peak % n]:
                peak += 1
            end = peak
            while not bits[end % n]:
                end += 1
            r = peak - start
            A = {end: y[end % n]}
            for j in range(end - 1, peak, -1):
                num = y[j % n] + A[j + 1]
                if num % 2:
                    branch_counts["descent_parity_reject"] += 1
                    valid = False
                    break
                A[j] = num // 2
                if A[j] <= A[j + 1]:
                    valid = False
                    break
            if not valid:
                break
            assigned.update({j % n: a for j, a in A.items()})
            data.append((start, peak, end, r, A[peak + 1]))
        if not valid:
            continue
        free = []
        for start, peak, end, r, after in data:
            branch_counts["r1" if r == 1 else "r2" if r == 2 else "r3plus"] += 1
            if r == 1:
                p = y[peak % n] - y[start % n] + after
                if not (y[start % n] <= p and p > after):
                    valid = False
                    break
                assigned[peak % n] = p
            else:
                if y[(start + 1) % n] != y[start % n] or any(
                        y[j % n] > y[(j + 1) % n]
                        for j in range(start + 1, peak - 1)):
                    valid = False
                    break
                for j in range(start, peak - 1):
                    assigned[j % n] = y[(j + 1) % n]
                total = y[peak % n] + after
                lo = y[(peak - 1) % n]
                hi = min(total // 2, y[peak % n] - 1)
                if hi < lo:
                    branch_counts["empty_interval"] += 1
                    valid = False
                    break
                free.append((peak, total, lo, hi))
        if not valid:
            continue
        branch_counts["positive_words"] += 1
        branch_counts["two_free_intervals"] += int(len(free) >= 2)
        assert len(free) <= n // 3
        for choices in product(*(range(lo, hi + 1) for _, _, lo, hi in free)):
            values = assigned.copy()
            for (peak, total, _, _), t in zip(free, choices):
                values[(peak - 1) % n] = t
                values[peak % n] = total - t
            assert len(values) == n, ("coordinate_coverage", y, bits, values)
            a = tuple(values[i] for i in range(n))
            assert all((a[i] <= a[(i + 1) % n]) == bool(bits[i])
                       for i in range(n)), ("comparison_word", y, bits, a)
            assert min(a) >= 0 and sum(a) == sum(y), ("source_carrier", y, a)
            assert a not in out, ("duplicate_chamber_source", y, bits, a)
            out.add(a)
    return out


def fixed_fibre(y):
    m = min(y)
    r = [v - m for v in y]
    if not any(r):
        return 1
    result = 1
    for i, v in enumerate(r):
        if v:
            gap, j = 0, (i - 1) % len(y)
            while r[j] == 0:
                gap += 1
                j = (j - 1) % len(y)
            if gap >= 2:
                result *= v // 2 + 1
    return result


state_count = 0
carrier_count = 0
fixed_count = 0
print("INDEPENDENT_FIXED_BOX n=1..6 N=0..4; one_run; no_author_import")
for n in range(1, 7):
    for mass in range(5):
        states = tuple(carrier(n, mass))
        succ, pred, depth, terminal = graph(states)
        expected_height = 0
        if n >= 4 and mass:
            expected_height = mass - 1
        elif n == 3 and mass:
            power = 1
            while power < mass:
                power *= 2
                expected_height += 1
        assert max(depth.values()) == expected_height, ("sharp_height", n, mass)
        for y in states:
            assert flux_sources(y) == pred[y], ("flux_inverse", y)
            assert chamber_sources(y) == pred[y], ("chamber_inverse", y)
            assert min(succ[y]) == min(y), ("minimum", y)
            assert terminal[y] == terminal_formula(y), ("terminal", y)
            r = tuple(v - min(y) for v in y)
            assert (succ[y] == y) == all(not (r[i] and r[i - 1])
                                       for i in range(n)), ("fixed_support", y)
            if n == 3 and sum(bool(v) for v in r) == 2:
                endpoint = next(i for i in range(n) if r[i] and not r[(i + 1) % n])
                held, steps = r[endpoint], 0
                while held < sum(r):
                    held *= 2
                    steps += 1
                assert depth[y] == steps, ("pointwise_three_clock", y)
            if succ[y] == y:
                assert len(pred[y]) == fixed_fibre(y), ("fixed_fibre", y)
                fixed_count += 1
            if n >= 3:
                assert len(pred[y]) <= (2 ** n - 1) * (mass + 1) ** (n // 3)
            print("TARGET", json.dumps([y, succ[y], depth[y], terminal[y],
                                        sorted(pred[y])], separators=(",", ":")))
        k = n // 3
        if k and mass >= 2 * k:
            q = mass // (2 * k)
            y = [0] * n
            for j in range(k):
                y[3 * j + 2] = 2 * q
            y[2] += mass - 2 * k * q
            count = len(pred[tuple(y)])
            assert count >= (q + 1) ** k
            assert count * (2 * k) ** k >= mass ** k
        print("CARRIER", n, mass, len(states), "height", max(depth.values()),
              "image", sum(bool(pred[y]) for y in states),
              "max_fibre", max(map(len, pred.values())))
        state_count += len(states)
        carrier_count += 1
assert state_count == 461 and carrier_count == 30
assert all(branch_counts.values()), ("missing_branch_pressure", branch_counts)
print("BRANCH_COUNTS", json.dumps(branch_counts, sort_keys=True))
print("COMPLETE states=461 carriers=30 fixed_targets=" + str(fixed_count)
      + "; finite_agreement_only; no_author_pilot_reclassification; HOLD_EXTERNAL")
