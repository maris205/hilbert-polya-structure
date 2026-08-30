#!/usr/bin/env python3
"""Independent exact control for the parity-guided root-rotation spike.

The program does not import the scouting pilot.  It compares literal orbit
iteration with a separately encoded spine clock, reconstructs every one-step
fibre from inverse rotations, and checks the fixed/recurrent/depth/fibre
generating functions coefficientwise.
"""

from collections import Counter, defaultdict
from functools import lru_cache


ASSERTIONS = 0
LEAF = None


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


@lru_cache(None)
def all_trees(order):
    """All plane full binary trees with ``order`` internal vertices."""
    if order == 0:
        return (LEAF,)
    result = []
    for left_order in range(order):
        right_order = order - 1 - left_order
        for left in all_trees(left_order):
            for right in all_trees(right_order):
                result.append((left, right))
    return tuple(result)


@lru_cache(None)
def order(tree):
    if tree is LEAF:
        return 0
    return 1 + order(tree[0]) + order(tree[1])


def update(tree):
    if tree is LEAF:
        return LEAF
    left, right = tree
    if order(left) % 2 == 0:
        if right is LEAF:
            return tree
        middle, outer = right
        return ((left, middle), outer)
    outer, middle = left
    return (outer, (middle, right))


def literal_orbit(tree):
    seen = {}
    states = []
    state = tree
    while state not in seen:
        seen[state] = len(states)
        states.append(state)
        state = update(state)
    depth = seen[state]
    period = len(states) - depth
    return depth, period, tuple(states), state


def fixed_shape(tree):
    if tree is LEAF:
        return True
    left, right = tree
    return order(left) % 2 == 0 and right is LEAF


def recurrent_shape(tree):
    if fixed_shape(tree):
        return True
    left, right = tree
    if order(left) % 2 == 0:
        return right is not LEAF and order(right[0]) % 2 == 0
    return order(left[0]) % 2 == 0


def spine_normal_form(tree):
    """Return the exact transient trace predicted by the two spine forms.

    The returned tuple starts at ``tree`` and ends at the first recurrent
    state.  No orbit detection or call to ``recurrent_shape`` is used.
    """
    if tree is LEAF:
        return (tree,)
    left, right = tree
    trace = [tree]
    if order(left) % 2 == 0:
        accumulator = left
        remainder = right
        while remainder is not LEAF:
            branch, tail = remainder
            if order(branch) % 2 == 0:
                break
            accumulator = (accumulator, branch)
            remainder = tail
            trace.append((accumulator, remainder))
        return tuple(trace)

    current_left = left
    accumulator = right
    while True:
        next_left, branch = current_left
        if order(branch) % 2 == 0:
            break
        current_left = next_left
        accumulator = (branch, accumulator)
        trace.append((current_left, accumulator))
    return tuple(trace)


def inverse_rotation_candidates(tree):
    """The at-most-two candidates supplied by literal inverse rotations."""
    candidates = set()
    if tree is LEAF:
        candidates.add(LEAF)
        return candidates

    left, right = tree
    if fixed_shape(tree):
        candidates.add(tree)

    # Invert a source left rotation: (A,(B,R)) -> ((A,B),R).
    if left is not LEAF:
        outer, middle = left
        if order(outer) % 2 == 0:
            candidates.add((outer, (middle, right)))

    # Invert a source right rotation: ((L,B),C) -> (L,(B,C)).
    if right is not LEAF:
        middle, outer = right
        source = ((left, middle), outer)
        if order(source[0]) % 2 == 1:
            candidates.add(source)
    return candidates


def catalans(maximum):
    values = [1]
    for n in range(1, maximum + 1):
        values.append(sum(values[j] * values[n - 1 - j] for j in range(n)))
    return values


def add(left, right, maximum):
    return [
        (left[n] if n < len(left) else 0) + (right[n] if n < len(right) else 0)
        for n in range(maximum + 1)
    ]


def multiply(left, right, maximum):
    result = [0] * (maximum + 1)
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right):
            if i + j > maximum:
                break
            if b:
                result[i + j] += a * b
    return result


def scale(series, factor):
    return [factor * coefficient for coefficient in series]


def shift(series, amount, maximum):
    return [0] * amount + list(series[: maximum + 1 - amount])


def witness(depth, even_order):
    """Sharp tree of order 2*depth+1 (odd) or 2*depth+2 (even)."""
    cherry = (LEAF, LEAF)
    tail = cherry if even_order else LEAF
    for _ in range(depth):
        tail = (cherry, tail)
    return (LEAF, tail)


def main():
    maximum = 12
    catalan = catalans(maximum)
    even = [value if n % 2 == 0 else 0 for n, value in enumerate(catalan)]
    odd = [value if n % 2 == 1 else 0 for n, value in enumerate(catalan)]

    e2 = multiply(even, even, maximum)
    e2c = multiply(e2, catalan, maximum)
    fixed_series = add([1] + [0] * maximum, shift(even, 1, maximum), maximum)
    recurrent_series = add(
        fixed_series,
        scale(shift(e2c, 2, maximum), 2),
        maximum,
    )

    # Targets of indegree two: fixed targets with an extra inverse left
    # rotation, or nonfixed targets admitting both inverse rotations.
    eo = multiply(even, odd, maximum)
    e2oc = multiply(multiply(e2, odd, maximum), catalan, maximum)
    fibre_two_series = add(
        shift(eo, 2, maximum),
        scale(shift(e2oc, 3, maximum), 2),
        maximum,
    )

    rows = []
    empirical_depth = [Counter() for _ in range(maximum + 1)]
    empirical_fixed = [0] * (maximum + 1)
    empirical_recurrent = [0] * (maximum + 1)
    empirical_fibres = [Counter() for _ in range(maximum + 1)]

    for n in range(maximum + 1):
        universe = all_trees(n)
        universe_set = set(universe)
        reverse = defaultdict(set)
        images = {}
        for tree in universe:
            image = update(tree)
            images[tree] = image
            reverse[image].add(tree)
            check(order(image) == n, (n, "order preservation"))
            check(image in universe_set, (n, "closure"))

        fixed = 0
        recurrent = 0
        depths = Counter()
        periods = Counter()
        fibres = Counter()
        for tree in universe:
            depth, period, states, repeated = literal_orbit(tree)
            normal_trace = spine_normal_form(tree)
            check(states[: len(normal_trace)] == normal_trace, (n, "spine trace"))
            check(depth == len(normal_trace) - 1, (n, "spine clock", depth))
            check(period in (1, 2), (n, "period", period))
            check(repeated == states[depth], (n, "cycle entry"))
            check((images[tree] == tree) == fixed_shape(tree), (n, "fixed test"))
            check((depth == 0) == recurrent_shape(tree), (n, "recurrent shape"))
            check((update(update(tree)) == tree) == (depth == 0), (n, "literal recurrence"))
            check(depth <= max(0, (n - 1) // 2), (n, "universal depth"))

            predicted_preimages = inverse_rotation_candidates(tree)
            check(predicted_preimages == reverse[tree], (n, "exact fibre", tree))
            check(len(predicted_preimages) <= 2, (n, "fibre ceiling"))
            for source in predicted_preimages:
                check(update(source) == tree, (n, "inverse candidate"))

            is_fixed = images[tree] == tree
            is_recurrent = depth == 0
            fixed += is_fixed
            recurrent += is_recurrent
            depths[depth] += 1
            periods[period] += 1
            fibres[len(reverse[tree])] += 1

        check(fixed == fixed_series[n], (n, "fixed OGF", fixed, fixed_series[n]))
        check(recurrent == recurrent_series[n], (n, "recurrent OGF"))
        check(fibres[2] == fibre_two_series[n], (n, "indegree-two OGF"))
        check(fibres[0] == fibres[2], (n, "zero/two balance"))
        check(fibres[1] + 2 * fibres[2] == len(universe), (n, "edge mass"))
        expected_maximum = 0 if n == 0 else (n - 1) // 2
        check(max(depths) == expected_maximum, (n, "sharp maximum"))
        check(depths[expected_maximum] == (1 if n % 2 else (1 if n == 0 else 2)),
              (n, "deepest census"))

        empirical_depth[n] = depths
        empirical_fixed[n] = fixed
        empirical_recurrent[n] = recurrent
        empirical_fibres[n] = fibres
        rows.append((n, len(universe), fixed, recurrent, dict(sorted(depths.items())),
                     dict(sorted(fibres.items()))))

    # Coefficientwise exact-depth theorem:
    # D_s(z)=(z O(z))^s (z E(z)+2 z^2 E(z)^2 C(z)).
    recurrent_nonleaf = recurrent_series[:]
    recurrent_nonleaf[0] -= 1
    z_odd = shift(odd, 1, maximum)
    power = [1] + [0] * maximum
    for depth in range((maximum - 1) // 2 + 1):
        predicted_layer = multiply(power, recurrent_nonleaf, maximum)
        if depth == 0:
            predicted_layer[0] += 1
        for n in range(maximum + 1):
            check(predicted_layer[n] == empirical_depth[n][depth],
                  (n, depth, "depth-layer OGF", predicted_layer[n],
                   empirical_depth[n][depth]))
        power = multiply(power, z_odd, maximum)

    # The bivariate depth decomposition at u=1 must reconstruct Catalan.
    reconstructed = [0] * (maximum + 1)
    reconstructed[0] = 1
    power = [1] + [0] * maximum
    for _ in range((maximum - 1) // 2 + 1):
        reconstructed = add(
            reconstructed,
            multiply(power, recurrent_nonleaf, maximum),
            maximum,
        )
        power = multiply(power, z_odd, maximum)
    check(reconstructed == catalan, ("depth decomposition", reconstructed, catalan))

    # Symbolic sharp families, far beyond the exhaustive Catalan carrier.
    for depth in range(41):
        odd_witness = witness(depth, even_order=False)
        even_witness = witness(depth, even_order=True)
        check(order(odd_witness) == 2 * depth + 1, (depth, "odd witness order"))
        check(order(even_witness) == 2 * depth + 2, (depth, "even witness order"))
        check(literal_orbit(odd_witness)[0] == depth, (depth, "odd witness depth"))
        check(literal_orbit(even_witness)[0] == depth, (depth, "even witness depth"))
        check(literal_orbit(odd_witness)[1] == 1, (depth, "odd witness endpoint"))
        check(literal_orbit(even_witness)[1] == 2, (depth, "even witness endpoint"))

    print("PARITY-GUIDED ROOT ROTATION: INDEPENDENT EXACT CONTROL PASS")
    print("n states fixed recurrent depth_hist indegree_hist")
    for row in rows:
        print(*row)
    print("fixed_coefficients_0_12=" + ",".join(map(str, empirical_fixed)))
    print("recurrent_coefficients_0_12=" + ",".join(map(str, empirical_recurrent)))
    print("indegree_two_coefficients_0_12=" +
          ",".join(str(empirical_fibres[n][2]) for n in range(maximum + 1)))
    print("sharp_symbolic_witnesses=82 orders=1..82")
    print(f"assertions={ASSERTIONS:,}")


if __name__ == "__main__":
    main()
