#!/usr/bin/env python3
"""Independent exact pilots for the P166 Round-6 open scout.

Only the Python standard library is used.  Every family is generated from its
literal update rule; the closed forms below are checked against full small-box
enumeration rather than used to generate the data.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from math import comb, gcd, prod


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


# ---------------------------------------------------------------------------
# MPS: simultaneous shaving of every globally highest peak of a Dyck path.


@lru_cache(None)
def dyck_words(n):
    out = []

    def rec(prefix, up, down):
        if up == n and down == n:
            out.append(prefix)
            return
        if up < n:
            rec(prefix + "U", up + 1, down)
        if down < up:
            rec(prefix + "D", up, down + 1)

    rec("", 0, 0)
    return tuple(out)


def path_heights(word):
    ans = [0]
    for letter in word:
        ans.append(ans[-1] + (1 if letter == "U" else -1))
    return tuple(ans)


def mps_step(word):
    h = path_heights(word)
    maximum = max(h)
    if maximum <= 1:
        return word
    letters = list(word)
    for i in range(len(word) - 1):
        if word[i : i + 2] == "UD" and h[i + 1] == maximum:
            letters[i], letters[i + 1] = "D", "U"
    return "".join(letters)


def iterate(function, state, t):
    for _ in range(t):
        state = function(state)
    return state


def bounded_dyck_count(n, height_bound):
    return sum(max(path_heights(w)) <= height_bound for w in dyck_words(n))


def mps_top_band_sizes(word):
    """Semilengths of maximal excursions above max(word)-2."""
    h = path_heights(word)
    maximum = max(h)
    check(maximum > 1, "top bands only apply to a nonfixed target")
    threshold = maximum - 1
    sizes = []
    i = 0
    while i < len(h):
        if h[i] < threshold:
            i += 1
            continue
        j = i
        while j + 1 < len(h) and h[j + 1] >= threshold:
            j += 1
        peaks = sum(1 for q in range(i, j + 1) if h[q] == maximum)
        # A component may be merely a lower peak at height maximum-1.  Only
        # components that actually touch the top level are expanded backwards.
        if peaks:
            sizes.append(peaks)
        i = j + 1
    return tuple(sizes)


def mps_predicted_fibre(target, t):
    n = len(target) // 2
    height = max(path_heights(target))
    if height == 1:
        return bounded_dyck_count(n, t + 1)
    sizes = mps_top_band_sizes(target)
    return prod(bounded_dyck_count(s, t + 1) for s in sizes) - prod(
        bounded_dyck_count(s, t) for s in sizes
    )


def audit_mps():
    signatures = []
    for n in range(1, 10):
        states = dyck_words(n)
        fixed = "UD" * n
        depths = Counter()
        for word in states:
            height = max(path_heights(word))
            check(mps_step(word) in states)
            check(iterate(mps_step, word, height - 1) == fixed)
            check(mps_step(fixed) == fixed)
            check(height - 1 == min(t for t in range(n + 1) if iterate(mps_step, word, t) == fixed))
            depths[height - 1] += 1
            for t in range(n + 1):
                actual = path_heights(iterate(mps_step, word, t))
                level = max(1, height - t)
                predicted = tuple(
                    value
                    if value <= level
                    else level
                    if (value - level) % 2 == 0
                    else level - 1
                    for value in path_heights(word)
                )
                check(actual == predicted, (n, word, t, actual, predicted))

        for t in range(n + 1):
            fibres = Counter(iterate(mps_step, source, t) for source in states)
            for target in states:
                check(fibres[target] == mps_predicted_fibre(target, t), (n, t, target))

        image = {mps_step(word) for word in states}
        signatures.append(
            f"n={n}:states={len(states)},image={len(image)},maxdepth={max(depths)},depths="
            + ",".join(f"{d}:{depths[d]}" for d in sorted(depths))
        )
    return signatures


# ---------------------------------------------------------------------------
# XSD: exact-two-secant transform under a fixed coordinate duality of PG(2,p).


def inv_mod(a, p):
    return pow(a, p - 2, p)


def projective_points(p):
    pts = set()
    for v in product(range(p), repeat=3):
        if v == (0, 0, 0):
            continue
        first = next(x for x in v if x)
        scale = inv_mod(first, p)
        pts.add(tuple((scale * x) % p for x in v))
    return tuple(sorted(pts))


def xsd_table(p):
    points = projective_points(p)
    line_masks = []
    for coeff in points:
        mask = 0
        for i, point in enumerate(points):
            if sum(a * b for a, b in zip(coeff, point)) % p == 0:
                mask |= 1 << i
        line_masks.append(mask)
        check(mask.bit_count() == p + 1)

    def step(mask):
        result = 0
        for i, line in enumerate(line_masks):
            if (mask & line).bit_count() == 2:
                result |= 1 << i
        return result

    return points, step


def tail_period(function, start):
    seen = {}
    state = start
    time = 0
    while state not in seen:
        seen[state] = time
        state = function(state)
        time += 1
    return seen[state], time - seen[state]


def audit_xsd():
    signatures = []
    for p in (2, 3):
        points, step = xsd_table(p)
        states = range(1 << len(points))
        values = [step(state) for state in states]
        indegrees = Counter(values)
        temporal = Counter(tail_period(step, state) for state in states)
        check(sum(indegrees.values()) == 1 << len(points))
        check(sum(temporal.values()) == 1 << len(points))
        check(all(0 <= image < (1 << len(points)) for image in values))
        signatures.append(
            f"p={p}:points={len(points)},states={1 << len(points)},image={len(indegrees)},"
            f"max-tail={max(a for a, _ in temporal)},max-period={max(b for _, b in temporal)},"
            f"tail-period=" + ",".join(f"{a}/{b}:{c}" for (a, b), c in sorted(temporal.items()))
        )
    return signatures


# ---------------------------------------------------------------------------
# MEG: mutual-eccentric graph of a labelled {1,2}-metric.


def graph_pairs(n):
    return tuple(combinations(range(n), 2))


def meg_literal_step(n, graph):
    pairs = graph_pairs(n)
    complete = (1 << len(pairs)) - 1
    eccentricity = []
    for vertex in range(n):
        distances = []
        for index, (i, j) in enumerate(pairs):
            if vertex in (i, j):
                distances.append(1 if graph & (1 << index) else 2)
        eccentricity.append(max(distances, default=0))
    result = 0
    for index, (i, j) in enumerate(pairs):
        distance = 1 if graph & (1 << index) else 2
        if distance == eccentricity[i] == eccentricity[j]:
            result |= 1 << index
    universal = []
    for vertex in range(n):
        incident = [index for index, pair in enumerate(pairs) if vertex in pair]
        if all(graph & (1 << index) for index in incident):
            universal.append(vertex)
    predicted = complete ^ graph
    for i, j in combinations(universal, 2):
        predicted |= 1 << pairs.index((i, j))
    check(result == predicted)
    return result


def meg_predicted_indegree(n, graph):
    """Closed target formula from isolated vertices and clique components."""
    pairs = graph_pairs(n)
    index = {pair: i for i, pair in enumerate(pairs)}

    def adjacent(i, j):
        if i > j:
            i, j = j, i
        return bool(graph & (1 << index[(i, j)]))

    degrees = [sum(adjacent(i, j) for j in range(n) if j != i) for i in range(n)]
    isolated = sum(degree == 0 for degree in degrees)
    complete = (1 << len(pairs)) - 1
    if graph == complete:
        return 2
    if isolated >= 2:
        return 0
    if isolated == 1:
        return 1

    unseen = set(range(n))
    clique_components = 0
    while unseen:
        seed = min(unseen)
        component = {seed}
        frontier = [seed]
        unseen.remove(seed)
        while frontier:
            vertex = frontier.pop()
            neighbors = {w for w in tuple(unseen) if adjacent(vertex, w)}
            unseen.difference_update(neighbors)
            component.update(neighbors)
            frontier.extend(neighbors)
        if all(adjacent(i, j) for i, j in combinations(sorted(component), 2)):
            clique_components += 1
    return 1 + clique_components


def audit_meg():
    signatures = []
    for n in range(2, 7):
        edge_count = comb(n, 2)
        complete = (1 << edge_count) - 1
        values = [meg_literal_step(n, graph) for graph in range(1 << edge_count)]
        indegrees = Counter(values)
        temporal = Counter(tail_period(lambda g: meg_literal_step(n, g), g) for g in range(1 << edge_count))
        check(sum(indegrees.values()) == 1 << edge_count)
        check(sum(temporal.values()) == 1 << edge_count)
        for target in range(1 << edge_count):
            check(indegrees[target] == meg_predicted_indegree(n, target), (n, target))
        signatures.append(
            f"n={n}:graphs={1 << edge_count},image={len(indegrees)},"
            f"max-tail={max(a for a, _ in temporal)},max-period={max(b for _, b in temporal)},"
            f"tail-period=" + ",".join(f"{a}/{b}:{c}" for (a, b), c in sorted(temporal.items()))
            + ",indegree-spectrum=" + ",".join(f"{d}:{c}" for d, c in sorted(Counter(indegrees.values()).items()))
        )
    return signatures


# ---------------------------------------------------------------------------
# CTB: continuous-time balancing on a path (every unstable edge has rate one).


def weak_compositions(total, parts):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in weak_compositions(total - first, parts - 1):
            yield (first,) + rest


def ctb_children(state):
    out = []
    for i in range(len(state) - 1):
        if abs(state[i] - state[i + 1]) >= 2:
            nxt = list(state)
            if state[i] > state[i + 1]:
                nxt[i] -= 1
                nxt[i + 1] += 1
            else:
                nxt[i] += 1
                nxt[i + 1] -= 1
            out.append(tuple(nxt))
    return tuple(out)


def ctb_audit_box(n, total):
    states = tuple(weak_compositions(total, n))
    children = {state: ctb_children(state) for state in states}
    edge_count = 0
    for state, next_states in children.items():
        for nxt in next_states:
            edge_count += 1
            check(sum(nxt) == total)
            check(sum(x * x for x in nxt) < sum(x * x for x in state))

    @lru_cache(None)
    def endpoint_law(state):
        next_states = children[state]
        if not next_states:
            return ((state, Fraction(1)),)
        accumulator = defaultdict(Fraction)
        for nxt in next_states:
            for target, probability in endpoint_law(nxt):
                accumulator[target] += probability / len(next_states)
        check(sum(accumulator.values(), Fraction()) == 1)
        return tuple(sorted(accumulator.items()))

    @lru_cache(None)
    def jump_extrema(state):
        next_states = children[state]
        if not next_states:
            return (0, 0)
        vals = [jump_extrema(nxt) for nxt in next_states]
        return 1 + min(v[0] for v in vals), 1 + max(v[1] for v in vals)

    @lru_cache(None)
    def mean_time(state):
        next_states = children[state]
        if not next_states:
            return Fraction()
        return Fraction(1, len(next_states)) + sum((mean_time(nxt) for nxt in next_states), Fraction()) / len(next_states)

    absorbing = [state for state in states if not children[state]]
    for state in states:
        law = endpoint_law(state)
        check(all(target in absorbing for target, _ in law))
        check(sum(probability for _, probability in law) == 1)
    maximum_support = max(len(endpoint_law(state)) for state in states)
    multi_endpoint = sum(len(endpoint_law(state)) > 1 for state in states)
    start = (total,) + (0,) * (n - 1)
    support = len(endpoint_law(start))
    shortest, longest = jump_extrema(start)
    maximum_longest = max(jump_extrema(state)[1] for state in states)
    return (
        f"n={n},M={total}:states={len(states)},edges={edge_count},absorbing={len(absorbing)},"
        f"max-jumps={maximum_longest},max-endpoint-support={maximum_support},multi-endpoint={multi_endpoint},"
        f"corner-support={support},corner-jumps={shortest}-{longest},"
        f"corner-mean={mean_time(start)}"
    )


def audit_ctb():
    return [ctb_audit_box(n, total) for n, total in ((3, 4), (3, 6), (4, 6), (4, 8))]


# ---------------------------------------------------------------------------
# Integer partitions, used by DPF below.


def integer_partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    if maximum is None or maximum > n:
        maximum = n
    for first in range(maximum, 0, -1):
        for tail in integer_partitions(n - first, first):
            yield (first,) + tail


# ---------------------------------------------------------------------------
# DPF: divisor-count fragmentation of an integer partition.


def divisor_count(n):
    return sum(n % d == 0 for d in range(1, n + 1))


def dpf_step(partition):
    pieces = []
    for part in partition:
        reduced = divisor_count(part)
        pieces.append(reduced)
        pieces.extend([1] * (part - reduced))
    return tuple(sorted(pieces, reverse=True))


def audit_dpf():
    signatures = []
    for total in (4, 6, 8, 10, 12, 16, 20, 24):
        states = tuple(integer_partitions(total))
        state_set = set(states)
        values = []
        depths = Counter()
        for state in states:
            nxt = dpf_step(state)
            values.append(nxt)
            check(nxt in state_set)
            check(sum(nxt) == total)
            check(all(part <= 2 for part in state) == (nxt == state))
            orbit = [state]
            while orbit[-1] != dpf_step(orbit[-1]):
                candidate = dpf_step(orbit[-1])
                check(
                    sum(x for x in candidate if x >= 3)
                    < sum(x for x in orbit[-1] if x >= 3)
                )
                orbit.append(candidate)
            depths[len(orbit) - 1] += 1
        indegrees = Counter(values)
        check(sum(indegrees.values()) == len(states))
        check(sum(depths.values()) == len(states))
        signatures.append(
            f"N={total}:partitions={len(states)},image={len(indegrees)},maxdepth={max(depths)},"
            f"fixed={depths[0]},depths=" + ",".join(f"{d}:{depths[d]}" for d in sorted(depths))
            + ",max-indegree=" + str(max(indegrees.values()))
        )
    return signatures


# ---------------------------------------------------------------------------
# GGT: pairwise-gcd triangle on triples of divisors of N.


def divisors(n):
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def factorization(n):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            exponent = 0
            while n % p == 0:
                n //= p
                exponent += 1
            out.append((p, exponent))
        p += 1
    if n > 1:
        out.append((n, 1))
    return tuple(out)


def valuation(n, p):
    answer = 0
    while n % p == 0:
        n //= p
        answer += 1
    return answer


def ggt_step(state):
    a, b, c = state
    return gcd(a, b), gcd(b, c), gcd(c, a)


def ggt_one_step_fibre(N, target):
    answer = 1
    for p, exponent in factorization(N):
        values = tuple(valuation(x, p) for x in target)
        minimum = min(values)
        if values[0] == values[1] == values[2]:
            local = 1 + 3 * (exponent - minimum)
        elif values.count(minimum) == 2:
            local = 2 * (exponent - max(values)) + 1
        else:
            return 0
        answer *= local
    return answer


def ggt_two_step_diagonal_fibre(N, diagonal_value):
    answer = 1
    for p, exponent in factorization(N):
        h = valuation(diagonal_value, p)
        remaining = exponent - h
        answer *= (remaining + 1) ** 3 - remaining**3
    return answer


def audit_ggt():
    signatures = []
    for N in (2, 6, 12, 36, 72, 180):
        divs = divisors(N)
        states = tuple(product(divs, repeat=3))
        first = Counter(ggt_step(state) for state in states)
        second = Counter(iterate(ggt_step, state, 2) for state in states)
        depths = Counter()
        for state in states:
            common = gcd(gcd(state[0], state[1]), state[2])
            check(iterate(ggt_step, state, 2) == (common,) * 3)
            if state == (common,) * 3:
                depth = 0
            elif ggt_step(state) == (common,) * 3:
                depth = 1
            else:
                depth = 2
            depths[depth] += 1
        for target in states:
            check(first[target] == ggt_one_step_fibre(N, target), (N, target, first[target]))
            predicted_second = 0
            if target[0] == target[1] == target[2]:
                predicted_second = ggt_two_step_diagonal_fibre(N, target[0])
            check(second[target] == predicted_second, (N, target, second[target], predicted_second))
        check(sum(first.values()) == len(states))
        check(sum(second.values()) == len(states))
        signatures.append(
            f"N={N}:divisors={len(divs)},states={len(states)},image1={len(first)},image2={len(second)},"
            f"depths=" + ",".join(f"{d}:{depths[d]}" for d in sorted(depths))
        )
    return signatures


def print_section(name, lines):
    print(f"[{name}]")
    for line in lines:
        print(line)


def main():
    print("P166 ROUND-6 OPEN SCOUT -- INDEPENDENT EXACT SMALL-BOX AUDIT")
    print_section("MPS maximum-peak shaving", audit_mps())
    print_section("XSD exact-two-secant duality", audit_xsd())
    print_section("MEG mutual-eccentric graph", audit_meg())
    print_section("CTB continuous-time path balancing", audit_ctb())
    print_section("DPF divisor-count partition fragmentation", audit_dpf())
    print_section("GGT pairwise-gcd triangle", audit_ggt())
    print(f"ASSERTIONS={ASSERTIONS}")
    print("RESULT=PASS")
    print("SCOUT_DECISION=KILL_ALL")
    print("EXTERNAL_STATUS=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
