#!/usr/bin/env python3
"""Independent exhaustive verifier for degree-feedback jump (DFJ).

For an endofunction f:[n]->[n], DFJ sends
    v |-> f^(1+indeg_f(v))(v).

The program exhausts every endofunction through n=6.  It does not import any
project verifier.  Besides the full transformation functional graph, it checks
the monotone support invariants, the exact fixed-point criterion, the embedded
power-map family, and every permutation-target fibre against the classical
square-root formula.
"""

from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import factorial


ASSERTIONS = 0


def check(condition, tag):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(tag)


def indegrees(f):
    d = [0] * len(f)
    for y in f:
        d[y] += 1
    return tuple(d)


def follow(f, v, steps):
    for _ in range(steps):
        v = f[v]
    return v


def dfj(f):
    d = indegrees(f)
    return tuple(follow(f, v, 1 + d[v]) for v in range(len(f)))


def compose_power(f, exponent):
    return tuple(follow(f, v, exponent) for v in range(len(f)))


def is_permutation(f):
    return len(set(f)) == len(f)


def conjugate(f, label_map):
    out = [None] * len(f)
    for old in range(len(f)):
        out[label_map[old]] = label_map[f[old]]
    return tuple(out)


def weak_components(f):
    n = len(f)
    adjacency = [set() for _ in range(n)]
    for v, y in enumerate(f):
        adjacency[v].add(y)
        adjacency[y].add(v)
    unseen = set(range(n))
    components = []
    while unseen:
        start = min(unseen)
        unseen.remove(start)
        stack = [start]
        component = []
        while stack:
            v = stack.pop()
            component.append(v)
            for y in adjacency[v]:
                if y in unseen:
                    unseen.remove(y)
                    stack.append(y)
        components.append(tuple(sorted(component)))
    return tuple(sorted(components))


def cycle_data(f):
    """Return sorted cycles, cyclic vertices, and every vertex's cycle depth."""
    n = len(f)
    finished = set()
    cycles = []
    depths = [None] * n
    for start in range(n):
        if start in finished:
            continue
        path = []
        position = {}
        v = start
        while v not in finished and v not in position:
            position[v] = len(path)
            path.append(v)
            v = f[v]
        if v in position:
            cut = position[v]
            cycle = tuple(path[cut:])
            cycles.append(cycle)
            for x in cycle:
                depths[x] = 0
            for x in reversed(path[:cut]):
                depths[x] = depths[f[x]] + 1
        else:
            for x in reversed(path):
                depths[x] = depths[f[x]] + 1
        finished.update(path)
    cyclic = frozenset(x for cycle in cycles for x in cycle)
    return tuple(sorted(cycles, key=lambda c: (len(c), min(c)))), cyclic, tuple(depths)


def fixed_criterion(f):
    """Pointwise equivalent form: f^d(v)(f(v))=f(v)."""
    d = indegrees(f)
    return all(follow(f, f[v], d[v]) == f[v] for v in range(len(f)))


def fixed_point_egf_counts(cutoff):
    """Coefficient check for the exact fixed-functional-digraph species."""
    zero = [Fraction(0) for _ in range(cutoff + 1)]

    def add(left, right):
        return [left[i] + right[i] for i in range(cutoff + 1)]

    def scale(series, scalar):
        return [scalar * value for value in series]

    def multiply(left, right):
        answer = zero[:]
        for i, x in enumerate(left):
            for j in range(cutoff + 1 - i):
                answer[i + j] += x * right[j]
        return answer

    def power(series, exponent):
        answer = [Fraction(1)] + zero[1:]
        for _ in range(exponent):
            answer = multiply(answer, series)
        return answer

    def residue_exponential(series, modulus, residue):
        answer = zero[:]
        current = [Fraction(1)] + zero[1:]
        for amount in range(cutoff + 1):
            if amount % modulus == residue:
                answer = add(answer, scale(current, Fraction(1, factorial(amount))))
            current = multiply(current, series)
        return answer

    z = zero[:]
    if cutoff:
        z[1] = 1
    exponent = zero[:]
    for length in range(1, cutoff + 1):
        leaf_set = zero[:]
        for amount in range(0, cutoff + 1, length):
            leaf_set[amount] = Fraction(1, factorial(amount))
        branch = multiply(z, leaf_set)
        core_vertex = multiply(
            z, residue_exponential(branch, length, (length - 1) % length)
        )
        exponent = add(
            exponent, scale(power(core_vertex, length), Fraction(1, length))
        )
    full = residue_exponential(exponent, 1, 0)
    counts = []
    for n, coefficient in enumerate(full):
        value = coefficient * factorial(n)
        check(value.denominator == 1, ("fixed-egf-integrality", n, value))
        counts.append(value.numerator)
    return tuple(counts)


def transformation_graph(n):
    states = tuple(product(range(n), repeat=n))
    index = {f: i for i, f in enumerate(states)}
    images = []
    rank_transitions = Counter()
    weak_splits = 0
    cyclic_losses = 0

    generators = []
    if n >= 2:
        generators.append(tuple([1, 0] + list(range(2, n))))
        generators.append(tuple(list(range(1, n)) + [0]))
    else:
        generators.append((0,))

    for f in states:
        g = dfj(f)
        images.append(index[g])
        rank_transitions[(len(set(f)), len(set(g)))] += 1

        check(set(g) <= set(f), ("image-monotonicity", n, f, g))
        old_components = weak_components(f)
        new_components = weak_components(g)
        old_owner = {v: component for component in old_components for v in component}
        for component in new_components:
            check(len({old_owner[v] for v in component}) == 1,
                  ("component-refinement", n, f, g, component))
        weak_splits += old_components != new_components

        old_cycles, old_cyclic, _ = cycle_data(f)
        _, new_cyclic, _ = cycle_data(g)
        check(new_cyclic <= old_cyclic, ("cyclic-support", n, f, g))
        cyclic_losses += new_cyclic != old_cyclic

        check((f == g) == fixed_criterion(f), ("fixed-criterion", n, f))
        if is_permutation(f):
            check(g == compose_power(f, 2), ("permutation-square", n, f))

        # These two relabellings generate S_n, so this is a bounded exact
        # equivariance check without multiplying the census by n!.
        for label_map in generators:
            check(dfj(conjugate(f, label_map)) == conjugate(g, label_map),
                  ("equivariance-generator", n, f, label_map))

    fibre = Counter(images)
    fibre_histogram = Counter(fibre.values())

    # Classify the full functional graph of DFJ on [n]^[n].
    size = len(states)
    depth = [None] * size
    cycle_length = [None] * size
    cycles = []
    resolved = [False] * size
    for start in range(size):
        if resolved[start]:
            continue
        path = []
        position = {}
        v = start
        while not resolved[v] and v not in position:
            position[v] = len(path)
            path.append(v)
            v = images[v]
        if resolved[v]:
            next_depth = depth[v]
            period = cycle_length[v]
            for x in reversed(path):
                next_depth += 1
                depth[x] = next_depth
                cycle_length[x] = period
                resolved[x] = True
        else:
            cut = position[v]
            cycle = tuple(path[cut:])
            cycles.append(cycle)
            period = len(cycle)
            for x in cycle:
                depth[x] = 0
                cycle_length[x] = period
                resolved[x] = True
            next_depth = 0
            for x in reversed(path[:cut]):
                next_depth += 1
                depth[x] = next_depth
                cycle_length[x] = period
                resolved[x] = True

    check(all(value is not None for value in depth), ("all-depths", n))
    check(sum(fibre.values()) == size, ("fibre-mass", n))
    check(sum(length * count for length, count in Counter(map(len, cycles)).items())
          == sum(value == 0 for value in depth), ("recurrent-mass", n))

    stats = {
        "states": size,
        "image": len(fibre),
        "zero_fibres": size - len(fibre),
        "fixed": sum(states[i] == states[images[i]] for i in range(size)),
        "recurrent": sum(value == 0 for value in depth),
        "max_tail": max(depth),
        "cycles": Counter(map(len, cycles)),
        "depths": Counter(depth),
        "fibres": fibre_histogram,
        "rank": rank_transitions,
        "weak_splits": weak_splits,
        "cyclic_losses": cyclic_losses,
        "states_tuple": states,
        "fibre_tuple": fibre,
    }
    return stats


def cycle_multiplicities(perm):
    cycles, _, _ = cycle_data(perm)
    return Counter(map(len, cycles))


def permutation_square_root_count(target):
    """Classical cycle-pairing formula for square roots in S_n."""
    answer = 1
    for length, amount in cycle_multiplicities(target).items():
        if length % 2 == 0:
            if amount % 2:
                return 0
            pairs = amount // 2
            answer *= factorial(amount) * length ** pairs
            answer //= 2 ** pairs * factorial(pairs)
        else:
            subtotal = 0
            for pairs in range(amount // 2 + 1):
                subtotal += (
                    factorial(amount)
                    * length ** pairs
                    // (
                        factorial(amount - 2 * pairs)
                        * 2 ** pairs
                        * factorial(pairs)
                    )
                )
            answer *= subtotal
    return answer


def permutation_fibre_suite(all_stats):
    boxes = 0
    identity_fibres = []
    for n, stats in enumerate(all_stats, start=1):
        fibre = stats["fibre_tuple"]
        states = stats["states_tuple"]
        index = {f: i for i, f in enumerate(states)}
        for target in permutations(range(n)):
            observed = fibre.get(index[target], 0)
            expected = permutation_square_root_count(target)
            check(observed == expected,
                  ("permutation-target-square-roots", n, target, observed, expected))
            boxes += 1
        identity = tuple(range(n))
        identity_fibres.append(fibre[index[identity]])
    check(identity_fibres == [1, 2, 4, 10, 26, 76],
          ("identity-involution-sequence", identity_fibres))
    return boxes, tuple(identity_fibres)


def uniform_leaf_lift(core_perm, leaves_per_core):
    core_size = len(core_perm)
    r = leaves_per_core
    total = core_size * (r + 1)
    f = [None] * total
    for v in range(core_size):
        f[v] = core_perm[v]
        for j in range(r):
            leaf = core_size + v * r + j
            f[leaf] = v
    return tuple(f)


def uniform_leaf_power_suite():
    boxes = 0
    for core_size in range(1, 7):
        for r in range(7):
            if core_size * (r + 1) > 6:
                break
            exponent = r + 2
            for perm in permutations(range(core_size)):
                initial = uniform_leaf_lift(perm, r)
                current = initial
                for t in range(5):
                    expected_core = compose_power(perm, exponent ** t)
                    expected = uniform_leaf_lift(expected_core, r)
                    check(current == expected,
                          ("uniform-leaf-power", core_size, r, perm, t))
                    current = dfj(current)
                    boxes += 1
    return boxes


def coarse_descriptor(f):
    cycles, _, depths = cycle_data(f)
    return (
        len(set(f)),
        tuple(sorted(indegrees(f))),
        tuple(sorted(map(len, cycles))),
        tuple(sorted(depths)),
        tuple(sorted(map(len, weak_components(f)))),
    )


def irregular_fibre_witness(stats_n6):
    first = (1, 0, 0, 0, 1, 3)
    second = (1, 0, 0, 0, 1, 4)
    states = stats_n6["states_tuple"]
    index = {f: i for i, f in enumerate(states)}
    fibre = stats_n6["fibre_tuple"]
    check(coarse_descriptor(first) == coarse_descriptor(second),
          ("same-coarse-descriptor", first, second))
    first_fibre = fibre.get(index[first], 0)
    second_fibre = fibre.get(index[second], 0)
    check((first_fibre, second_fibre) == (1, 2),
          ("shape-sensitive-fibre", first_fibre, second_fibre))
    return first, first_fibre, second, second_fibre


def compact_counter(counter):
    return ",".join(f"{key}:{counter[key]}" for key in sorted(counter))


def compact_pairs(counter):
    return ",".join(
        f"{left}>{right}:{counter[(left, right)]}"
        for left, right in sorted(counter)
    )


def main():
    all_stats = []
    for n in range(1, 7):
        stats = transformation_graph(n)
        all_stats.append(stats)
        print(
            f"n={n}|N={stats['states']}|image={stats['image']}|"
            f"zero={stats['zero_fibres']}|fixed={stats['fixed']}|"
            f"recurrent={stats['recurrent']}|max_tail={stats['max_tail']}|"
            f"cycles={compact_counter(stats['cycles'])}|"
            f"depths={compact_counter(stats['depths'])}|"
            f"fibres={compact_counter(stats['fibres'])}|"
            f"rank={compact_pairs(stats['rank'])}|"
            f"weak_splits={stats['weak_splits']}|"
            f"cyclic_losses={stats['cyclic_losses']}"
        )

    permutation_boxes, identity_fibres = permutation_fibre_suite(all_stats)
    lift_boxes = uniform_leaf_power_suite()
    first, first_fibre, second, second_fibre = irregular_fibre_witness(all_stats[-1])
    fixed_egf = fixed_point_egf_counts(6)
    observed_fixed = (1,) + tuple(stats["fixed"] for stats in all_stats)
    check(fixed_egf == observed_fixed, ("fixed-egf", fixed_egf, observed_fixed))

    print(f"PERMUTATION_TARGET_FIBRE_BOXES={permutation_boxes}")
    print("IDENTITY_FIBRES=" + ",".join(map(str, identity_fibres)))
    print("FIXED_EGF_COUNTS_N0_TO_N6=" + ",".join(map(str, fixed_egf)))
    print(f"UNIFORM_LEAF_POWER_ASSERTIONS={lift_boxes}")
    print(f"IRREGULAR_FIBRE_WITNESS={first}:{first_fibre}|{second}:{second_fibre}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("MATH_STATUS=PASS")
    print("DECISION=KILL_POWER_MAP_CORE_AND_NO_SECOND_AXIS")
    print("EXTERNAL=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
