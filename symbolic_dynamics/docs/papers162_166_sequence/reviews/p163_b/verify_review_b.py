#!/usr/bin/env python3
"""Independent Hostile Review B verifier for complemented-shadow dynamics.

This file constructs the literal map from scratch.  It imports neither the
author verifier nor Review A evidence and uses only the Python standard
library.
"""

from collections import Counter, defaultdict
from math import comb


ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def bits(mask):
    while mask:
        low = mask & -mask
        yield low.bit_length() - 1
        mask ^= low


def atom_step(a, n):
    """Family mask S_n({a}); subset a is a bit mask on [n]."""
    if a == 0:
        return 0
    universe = (1 << n) - 1
    out = 0
    for point in bits(a):
        deleted = a & ~(1 << point)
        out |= 1 << (universe ^ deleted)
    return out


def family_step(family, atom_images):
    out = 0
    for a in bits(family):
        out |= atom_images[a]
    return out


def expected_kernel(a, t, n):
    if t == 0:
        return 1 << a
    if a == 0:
        return 0
    k = a.bit_count()
    s = t // 2
    out = 0
    if t % 2 == 0:
        for b in range(1 << n):
            if b.bit_count() == k and k - (a & b).bit_count() <= s:
                out |= 1 << b
    else:
        dual_rank = n - k + 1
        for c in range(1 << n):
            if c.bit_count() == dual_rank and (a & c).bit_count() <= s + 1:
                out |= 1 << c
    return out


def rank_layers(n):
    layers = [[] for _ in range(n + 1)]
    for a in range(1 << n):
        layers[a.bit_count()].append(a)
    return layers


def rank_support(family, layers):
    support = set()
    for k in range(1, len(layers)):
        if any(family & (1 << a) for a in layers[k]):
            support.add(k)
    return frozenset(support)


def rank_union(support, layers):
    out = 0
    for k in support:
        for a in layers[k]:
            out |= 1 << a
    return out


def phi_support(support, n, power=1):
    if power % 2 == 0:
        return frozenset(support)
    return frozenset(n - k + 1 for k in support)


def precompute_slice_radii(n, layers):
    """Map (k, global slice mask) to the two manuscript radii."""
    radii = {}
    for k in range(1, n + 1):
        layer = layers[k]
        dual = layers[n - k + 1]
        for local in range(1, 1 << len(layer)):
            chosen = [layer[i] for i in range(len(layer)) if local & (1 << i)]
            global_mask = sum(1 << a for a in chosen)
            even = max(
                min(k - (a & b).bit_count() for a in chosen) for b in layer
            )
            odd = max(
                min((a & c).bit_count() - 1 for a in chosen) for c in dual
            )
            radii[(k, global_mask)] = (even, odd)
    return radii


def clock_formula(family, n, layers, radii):
    support = rank_support(family, layers)
    if not support:
        return 1 if family & 1 else 0
    even_values = []
    odd_values = []
    for k in support:
        slice_mask = 0
        for a in layers[k]:
            if family & (1 << a):
                slice_mask |= 1 << a
        even, odd = radii[(k, slice_mask)]
        even_values.append(even)
        odd_values.append(odd)
    saturation = min(2 * max(even_values), 2 * max(odd_values) + 1)
    return max(1 if family & 1 else 0, saturation)


def tail_and_period(start, next_map):
    first_seen = {}
    state = start
    time = 0
    while state not in first_seen:
        first_seen[state] = time
        state = next_map[state]
        time += 1
    return first_seen[state], time - first_seen[state]


def support_formula(n, support):
    middle = (n + 1) // 2
    if middle not in support:
        return 0
    value = 2 * comb(n, middle)
    for k in support:
        if k != middle:
            value *= (1 << comb(n, k)) - 1
    return value


def rank_orbits(n):
    unseen = set(range(1, n + 1))
    result = []
    while unseen:
        k = min(unseen)
        orbit = frozenset((k, n - k + 1))
        result.append(orbit)
        unseen -= orbit
    return result


def deepest_period_one_formula(n):
    middle = (n + 1) // 2
    result = 2 * comb(n, middle)
    for orbit in rank_orbits(n):
        if middle in orbit:
            factor = 1
            for k in orbit - {middle}:
                factor *= (1 << comb(n, k)) - 1
        else:
            factor = 1
            product = 1
            for k in orbit:
                product *= (1 << comb(n, k)) - 1
            factor += product
        result *= factor
    return result


def verify_atomic(n):
    atom_images = [atom_step(a, n) for a in range(1 << n)]
    depth_hist = Counter()
    for a in range(1 << n):
        kernel = 1 << a
        seen = {}
        for t in range(0, 2 * n + 3):
            check(kernel == expected_kernel(a, t, n), "atomic kernel identity")
            if kernel not in seen:
                seen[kernel] = t
            kernel = family_step(kernel, atom_images)
        if a:
            k = a.bit_count()
            expected_depth = min(
                2 * min(k, n - k),
                2 * min(k - 1, n - k) + 1,
            )
            depth, period = tail_and_period(1 << a, [
                family_step(f, atom_images) for f in range(1 << (1 << n))
            ]) if n <= 3 else (expected_depth, None)
            if n <= 3:
                check(depth == expected_depth, "atomic functional depth")
                check(period in (1, 2), "atomic terminal period")
            depth_hist[expected_depth] += 1
    for d in range(n):
        rank = n - d // 2 if d % 2 == 0 else (d + 1) // 2
        check(depth_hist[d] == comb(n, rank), "atomic exact-depth census")
        check(depth_hist[d] == comb(n, (d + 1) // 2), "atomic binomial form")
    check(set(depth_hist) == set(range(n)), "every atomic depth occurs")
    return atom_images, depth_hist


def subset_mobius(values, bit_count):
    result = list(values)
    for bit in range(bit_count):
        step = 1 << bit
        for mask in range(1 << bit_count):
            if mask & step:
                result[mask] -= result[mask ^ step]
    return result


def verify_all_families(n):
    atom_count = 1 << n
    family_count = 1 << atom_count
    layers = rank_layers(n)
    atom_images, _ = verify_atomic(n)

    next_map = [0] * family_count
    for family in range(1, family_count):
        low = family & -family
        a = low.bit_length() - 1
        next_map[family] = next_map[family ^ low] | atom_images[a]

    radii = precompute_slice_radii(n, layers)
    recurrent_expected = {
        rank_union(frozenset(k + 1 for k in bits(support_mask)), layers)
        for support_mask in range(1 << n)
    }
    recurrent_actual = set()
    fixed_actual = Counter()
    tails = {}
    periods = {}
    deepest_by_support = Counter()
    deepest_by_period = Counter()

    for family in range(family_count):
        tail, period = tail_and_period(family, next_map)
        tails[family] = tail
        periods[family] = period
        check(tail == clock_formula(family, n, layers, radii), "mixed-rank clock")
        if tail == 0:
            recurrent_actual.add(family)
        if tail == n - 1:
            deepest_by_support[rank_support(family, layers)] += 1
            deepest_by_period[period] += 1

        state = family
        for j in range(1, 5):
            state = next_map[state]
            if state == family:
                fixed_actual[j] += 1

    check(recurrent_actual == recurrent_expected, "recurrent rank unions")
    check(len(recurrent_actual) == 1 << n, "recurrent count")
    for recurrent in recurrent_actual:
        support = rank_support(recurrent, layers)
        check(next_map[recurrent] == rank_union(phi_support(support, n), layers), "support involution")
    for j in range(1, 5):
        expected_fixed = 1 << ((n + 1) // 2) if j % 2 else 1 << n
        check(fixed_actual[j] == expected_fixed, "fixed-iterate census")

    check(max(tails.values()) == n - 1, "sharp global height")
    middle = (n + 1) // 2
    central_layer = layers[middle]
    central_predicate_count = 0
    for family in range(family_count):
        central_size = sum(bool(family & (1 << a)) for a in central_layer)
        if central_size == 1:
            central_predicate_count += 1
        if n >= 3:
            check((tails[family] == n - 1) == (central_size == 1), "deepest iff central singleton")

    if n >= 3:
        middle_size = comb(n, middle)
        total_formula = middle_size * (1 << (atom_count - middle_size))
        check(sum(deepest_by_support.values()) == total_formula, "deepest total")
        check(central_predicate_count == total_formula, "central singleton total")
        for support_mask in range(1 << n):
            support = frozenset(k + 1 for k in range(n) if support_mask & (1 << k))
            check(deepest_by_support[support] == support_formula(n, support), "support-refined deepest count")
        fixed_period = deepest_period_one_formula(n)
        check(deepest_by_period[1] == fixed_period, "deepest eventual period one")
        check(deepest_by_period[2] == total_formula - fixed_period, "deepest eventual period two")
        check(set(deepest_by_period) <= {1, 2}, "deepest terminal periods")
    else:
        check(n == 2, "only n=2 exceptional full-family box")
        check(sum(1 for value in tails.values() if value == 1) == 12, "n=2 twelve deepest")
        check(deepest_by_period[1] == 6, "n=2 period-one split")
        check(deepest_by_period[2] == 6, "n=2 period-two split")
        check(central_predicate_count == 8, "n=2 central predicate selects eight")

    # Every-target inverse formula via a full subset Moebius transform.
    current = list(range(family_count))
    kernels = [1 << a for a in range(atom_count)]
    for t in range(0, n + 2):
        if t == 0:
            for target in range(family_count):
                check(current[target] == target, "t=0 identity boundary")
        else:
            current = [next_map[state] for state in current]
            kernels = [family_step(kernel, atom_images) for kernel in kernels]
            actual_fibres = Counter(current)

            admissible_counts = [0] * family_count
            admissible_unions = [0] * family_count
            for target in range(family_count):
                count = 0
                union = 0
                for a in range(1, atom_count):
                    kernel = kernels[a]
                    if kernel & ~target == 0:
                        count += 1
                        union |= kernel
                admissible_counts[target] = count
                admissible_unions[target] = union
            cover_counts = subset_mobius(
                [1 << admissible_counts[target] for target in range(family_count)],
                atom_count,
            )
            for target in range(family_count):
                predicted = 2 * cover_counts[target]
                check(actual_fibres[target] == predicted, "every-target cover fibre")
                check((actual_fibres[target] > 0) == (admissible_unions[target] == target), "image iff cover union")
            check(actual_fibres[0] == 2, "positive-time empty target fibre")
            for target in range(family_count):
                if target & 1:
                    check(actual_fibres[target] == 0, "target containing silent atom is impossible")

            if t >= n - 1:
                check(set(actual_fibres) == recurrent_expected, "stable image is recurrent core")
                for support_mask in range(1 << n):
                    support = frozenset(k + 1 for k in range(n) if support_mask & (1 << k))
                    target = rank_union(support, layers)
                    source_support = phi_support(support, n, t)
                    predicted = 2
                    for k in source_support:
                        predicted *= (1 << comb(n, k)) - 1
                    check(actual_fibres[target] == predicted, "stable every-rank product fibre")

    return {
        "families": family_count,
        "height": max(tails.values()),
        "deepest": sum(deepest_by_support.values()),
        "period1": deepest_by_period[1],
        "period2": deepest_by_period[2],
    }


def verify_symbolic_boundaries():
    # Formula-only integer and equality controls beyond feasible full phases.
    for n in range(3, 13):
        middle = (n + 1) // 2
        total = comb(n, middle) * (1 << ((1 << n) - comb(n, middle)))
        support_sum = 0
        invariant_sum = 0
        for support_mask in range(1 << n):
            support = frozenset(k + 1 for k in range(n) if support_mask & (1 << k))
            value = support_formula(n, support)
            support_sum += value
            if support == phi_support(support, n):
                invariant_sum += value
        check(support_sum == total, "symbolic support sum")
        check(invariant_sum == deepest_period_one_formula(n), "symbolic invariant-support product")
        check(0 < invariant_sum <= total, "symbolic period split bounds")

        # Every central singleton hits depth n-1; every two-point central
        # slice fails the equality.  These are the two rigidity sentinels.
        layers = rank_layers(n)
        central = layers[middle]
        for a in central:
            family = 1 << a
            radii = precompute_slice_radii_for_selected(n, layers, middle, [a])
            check(min(2 * radii[0], 2 * radii[1] + 1) == n - 1, "central singleton sentinel")
        # Relabelling is transitive on ordered central pairs with fixed
        # intersection size, so one canonical representative per feasible
        # intersection checks every pair orbit without a quadratic scan.
        a = (1 << middle) - 1
        minimum_overlap = max(0, 2 * middle - n)
        for overlap in range(minimum_overlap, middle):
            shared = (1 << overlap) - 1
            new_part = ((1 << (middle - overlap)) - 1) << middle
            b = shared | new_part
            check(b.bit_count() == middle, "canonical central pair rank")
            check((a & b).bit_count() == overlap, "canonical central pair overlap")
            radii = precompute_slice_radii_for_selected(n, layers, middle, [a, b])
            check(min(2 * radii[0], 2 * radii[1] + 1) < n - 1, "central pair sentinel")


def precompute_slice_radii_for_selected(n, layers, k, chosen):
    even = max(min(k - (a & b).bit_count() for a in chosen) for b in layers[k])
    odd = max(
        min((a & c).bit_count() - 1 for a in chosen)
        for c in layers[n - k + 1]
    )
    return even, odd


def main():
    # Atomic boxes extend well past the fully enumerated family spaces.
    atomic_summaries = []
    for n in range(2, 10):
        _, histogram = verify_atomic(n)
        atomic_summaries.append(
            f"n={n}:" + ",".join(f"d{d}={histogram[d]}" for d in range(n))
        )

    full_summaries = []
    for n in range(2, 5):
        row = verify_all_families(n)
        full_summaries.append(
            f"n={n},families={row['families']},height={row['height']},"
            f"deepest={row['deepest']},split={row['period1']}+{row['period2']}"
        )

    verify_symbolic_boundaries()

    print("P163_HOSTILE_REVIEW_B_INDEPENDENT")
    print("ATOMIC=" + ";".join(atomic_summaries))
    print("FULL=" + ";".join(full_summaries))
    print("BOUNDARIES=empty,silent,t0,n2,central_singleton,central_pair,stable_image")
    print("CHECKS=kernels,clock,recurrent,fixed,deepest,support,period,cover_fibres")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
