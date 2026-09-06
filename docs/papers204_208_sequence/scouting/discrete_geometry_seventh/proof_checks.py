#!/usr/bin/env python3
"""Author audit of deductions, within the original INTAKE boxes only.

Imports pilot literal forward maps; reverse descriptions are implemented
separately. This is neither an independent reviewer nor a new admission.
"""
from collections import Counter
from hashlib import sha256
from itertools import product
from math import comb, factorial, prod
import json

import pilot

checks = 0
digest = sha256()


def require(condition, *datum):
    global checks
    checks += 1
    if not condition:
        raise AssertionError((checks, datum))
    digest.update(json.dumps(datum, separators=(",", ":"), sort_keys=True).encode())
    digest.update(b"\n")


def compositions(total, slots):
    if slots == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, slots - 1):
                yield (first,) + rest


def qhk_inverse(length, population):
    predicted = Counter()
    inventories = 0
    for counts in compositions(population, length):
        inventories += 1
        destinations, pushed = {}, [0] * length
        for x, centre in enumerate(counts):
            if not centre:
                continue
            left = counts[x - 1] if x else 0
            right = counts[x + 1] if x + 1 < length else 0
            step = 1 if right > centre + 3 * left else (-1 if left >= centre + 3 * right else 0)
            destinations[x] = x + step
            pushed[x + step] += centre
            require(not step or (counts[x + step], -x - step) > (centre, -x),
                    "QHK-priority", length, population, counts, x, step)
        numerator = prod(factorial(v) for v in pushed)
        denominator = prod(factorial(v) for v in counts)
        require(numerator % denominator == 0, "QHK-integrality", counts, pushed)
        predicted[tuple(pushed)] += numerator // denominator
        representative = tuple(x for x, count in enumerate(counts) for _ in range(count))
        require(pilot.qhk(representative) == tuple(destinations[x] for x in representative),
                "QHK-literal", length, population, counts)
    actual = Counter()
    for state in product(range(length), repeat=population):
        target = pilot.qhk(state)
        actual[target] += 1
        require(target == state or len(set(target)) < len(set(state)),
                "QHK-support", length, state, target)
        point, depth = state, 0
        while pilot.qhk(point) != point:
            point = pilot.qhk(point)
            depth += 1
            require(depth <= len(set(state)) - 1, "QHK-tail", length, state, depth)
    for target in product(range(length), repeat=population):
        histogram = tuple(target.count(x) for x in range(length))
        require(actual[target] == predicted[histogram], "QHK-fibre", length, target, actual[target])
    return {"rule": "QHK", "parameter": [length, population], "inventories": inventories,
            "states": length ** population, "all_labelled_fibres_checked": True}


def ols_inverse(a, b):
    points = [(x, y) for x in range(-a, a + 1) for y in range(-b, b + 1)]
    order = lambda p: (p[0] ** 2 + p[1] ** 2, p[0], p[1])
    rows = [sorted([p for p in points if p[1] == y], key=order) for y in range(-b, b + 1)]
    diagonals = [sorted([p for p in points if p[0] - p[1] == d], key=order)
                 for d in sorted({p[0] - p[1] for p in points})]
    point_index = {p: i for i, p in enumerate(points)}
    encode = lambda selected: sum(1 << point_index[p] for p in selected)
    predicted = Counter()
    inventory_count = 0
    for counts in product(*(range(len(row) + 1) for row in rows)):
        inventory_count += 1
        first = {p for row, count in zip(rows, counts) for p in row[:count]}
        second = {p for diagonal in diagonals for p in diagonal[:sum(q in first for q in diagonal)]}
        predicted[encode(second)] += prod(comb(len(row), count) for row, count in zip(rows, counts))
    size, update, _ = pilot.ols(a, b)
    actual = Counter(update(state) for state in range(1 << size))
    for target in range(1 << size):
        require(actual[target] == predicted[target], "OLS-fibre", a, b, target, actual[target])
        if update(target) == target:
            selected = {p for i, p in enumerate(points) if target & (1 << i)}
            for partition in (rows, diagonals):
                require(all(set(line[:sum(p in selected for p in line)]).issubset(selected)
                            for line in partition), "OLS-common-fixed", a, b, target)
    require(sum(predicted.values()) == 1 << size, "OLS-total", a, b, sum(predicted.values()))
    return {"rule": "OLS", "parameter": [a, b], "row_inventories": inventory_count,
            "states": 1 << size, "all_fibres_checked": True}


def lvc_inverse(n, m):
    states = list(product(range(n + 1), repeat=m))
    update, _ = pilot.laguerre(n, m)
    actual = Counter(update(state) for state in states)
    costs = [[(q - i) ** 2 for i in range(m)] for q in range(n)]
    for state in states:
        assignment = [min(range(m), key=lambda i: (costs[q][i] - state[i], i)) for q in range(n)]
        require(assignment == sorted(assignment), "LVC-monotone", n, m, state, assignment)
        minimum = min(state)
        normalized = tuple(w - minimum for w in state)
        require(update(normalized) == update(state), "LVC-translation", n, m, state)
    target_count = 0
    for target in compositions(n, m):
        target_count += 1
        start, constraints = 0, []
        for i, count in enumerate(target):
            if count:
                for j in range(m):
                    if j == i:
                        continue
                    endpoints = (start, start + count - 1)
                    bound = max(costs[q][i] - costs[q][j] + int(j < i) for q in endpoints)
                    require(bound == max(costs[q][i] - costs[q][j] + int(j < i)
                                         for q in range(start, start + count)),
                            "LVC-endpoint", n, m, target, i, j, bound)
                    constraints.append((i, j, bound))
            start += count
        predicted = 0
        for weights in states:
            accepted = all(weights[i] - weights[j] >= bound for i, j, bound in constraints)
            require(accepted == (update(weights) == target), "LVC-chamber", n, m, target, weights, accepted)
            predicted += accepted
        require(predicted == actual[target], "LVC-fibre", n, m, target, predicted)
    require(sum(actual.values()) == len(states), "LVC-total", n, m, len(states))
    require(all(sum(target) == n for target in actual), "LVC-valid-totals", n, m)
    return {"rule": "LVC", "parameter": [n, m], "states": len(states),
            "composition_targets": target_count, "all_wrong_total_volume_targets_have_zero_fibre": True,
            "all_chamber_memberships_checked": True}


def geometric_boundaries():
    records = []
    for a, b in ((1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (3, 3), (3, 4)):
        size, rectangles = pilot.rectangle_centres(a, b)
        _, ties = pilot.nearest_ties(a, b)
        for state in range(1 << size):
            centre_target, tie_target = rectangles(state), ties(state)
            require((centre_target == 0) == (state == (1 << size) - 1), "MER-empty-fibre", a, b, state)
            require(centre_target != state and not centre_target & state, "MER-no-fixed", a, b, state)
            require((tie_target == state) == (state == 0), "NTL-only-fixed", a, b, state)
            if a == 1:
                sites = [i for i in range(b) if state & (1 << i)]
                midpoint_target = sum(1 << ((left + right) // 2)
                                      for left, right in zip(sites, sites[1:]) if (right - left) % 2 == 0)
                require(midpoint_target == tie_target, "NTL-midpoints", b, state, midpoint_target)
                depth, point = 0, state
                while point:
                    point = ties(point)
                    depth += 1
                    require(depth <= (b + 1) // 2, "NTL-sharp-bound", b, state, depth)
        if a == 1:
            state = sum(1 << i for i in range(0, b, 2))
            point, depth = state, 0
            while point:
                point, depth = ties(point), depth + 1
            require(depth == (b + 1) // 2, "NTL-sharp-witness", b, state, depth)
        records.append({"rule": "MER+NTL", "parameter": [a, b], "states": 1 << size})
    _, rectangles = pilot.rectangle_centres(3, 3)
    witness = None
    for state in range(512):
        orbit = [state]
        for _ in range(4):
            orbit.append(rectangles(orbit[-1]))
        if orbit[-1] == state and len(set(orbit[:-1])) == 4:
            witness = orbit
            break
    require(witness is not None, "MER-four-cycle", witness)
    _, ties = pilot.nearest_ties(2, 2)
    require(ties(9) == 6 and ties(6) == 9, "NTL-two-cycle", 9, 6)
    for a, b in ((2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (3, 4), (4, 2), (4, 3)):
        size, singular = pilot.singular_vertices(a, b)
        inverse = Counter()
        for state in range(1 << size):
            target = singular(state)
            inverse[target] += 1
            require(target == singular(((1 << size) - 1) ^ state), "NSV-complement", a, b, state)
        require(all(v % 2 == 0 for v in inverse.values()), "NSV-even-fibres", a, b)
        records.append({"rule": "NSV", "parameter": [a, b], "states": 1 << size})
    _, singular = pilot.singular_vertices(3, 3)
    stripe_cycle, stripe_fixed = [], []
    for t in range(3):
        stripe = sum(1 << (3 * i + j) for i in range(3) for j in range(3) if (i + j) % 3 == t)
        next_stripe = sum(1 << (3 * i + j) for i in range(3) for j in range(3) if (i + j) % 3 == (t + 1) % 3)
        fixed = sum(1 << (3 * i + j) for i in range(3) for j in range(3) if (i - j) % 3 == t)
        require(singular(stripe) == next_stripe, "NSV-stripe-shift", t, stripe, next_stripe)
        require(singular(fixed) == fixed, "NSV-stripe-fixed", t, fixed)
        stripe_cycle.append(stripe)
        stripe_fixed.append(fixed)
    return records, {"MER_3x3_four_cycle": witness, "NTL_2x2_two_cycle": [9, 6, 9],
                     "NSV_3x3_stripe_cycle": stripe_cycle + stripe_cycle[:1],
                     "NSV_3x3_fixed_stripes": stripe_fixed}


def main():
    records = [qhk_inverse(length, population) for length in range(1, 7) for population in range(1, 6)]
    records.extend(ols_inverse(a, b) for a, b in
                   ((0, 0), (0, 1), (0, 2), (1, 0), (2, 0), (1, 1), (1, 2), (2, 1)))
    records.extend(lvc_inverse(n, m) for n in range(1, 8) for m in range(1, min(4, n) + 1))
    geometry, witnesses = geometric_boundaries()
    records.extend(geometry)
    print(json.dumps({"status": "AUTHOR_DEDUCTION_AUDIT_NOT_INDEPENDENT_REVIEW", "assertions": checks,
                      "assertion_datum_sha256": digest.hexdigest(), "cutoffs": "original INTAKE only",
                      "profiles": records, "witnesses": witnesses}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
