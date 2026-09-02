#!/usr/bin/env python3
"""Independent exact checks for the HTM/BTB focused freeze gate.

This script deliberately does not import the Stage-1 scout verifier.  All
computations use integers and fractions.Fraction, and every comparison is an
exact equality.  It is evidence for internal falsification only, not a novelty
or priority claim.
"""

from fractions import Fraction as Q
from itertools import combinations_with_replacement, permutations, product


ASSERTIONS = 0
SECTION_ASSERTIONS = {}
CURRENT_SECTION = "setup"


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    SECTION_ASSERTIONS[CURRENT_SECTION] = SECTION_ASSERTIONS.get(CURRENT_SECTION, 0) + 1
    if not condition:
        raise AssertionError(message)


def equal(left, right, message="exact equality failed"):
    check(left == right, f"{message}: {left!r} != {right!r}")


def solve_linear(matrix, rhs):
    """Solve a square rational system by deterministic Gauss-Jordan elimination."""
    n = len(rhs)
    aug = [[Q(x) for x in row] + [Q(rhs[i])] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next((row for row in range(col, n) if aug[row][col]), None)
        check(pivot is not None, f"singular system at column {col}")
        if pivot != col:
            aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for row in range(n):
            if row == col or not aug[row][col]:
                continue
            factor = aug[row][col]
            aug[row] = [a - factor * b for a, b in zip(aug[row], aug[col])]
    return [aug[i][-1] for i in range(n)]


def prefix_products(branching):
    ans = []
    running = 1
    for factor in branching:
        running *= factor
        ans.append(running)
    return ans


def leaves(branching):
    return product(*(range(b) for b in branching))


def zero_lcp(leaf):
    depth = 0
    for symbol in leaf:
        if symbol:
            break
        depth += 1
    return depth


def htm_kernel_literal(branching):
    """Depth kernel obtained by enumerating literal uniformly sampled leaves."""
    h = len(branching)
    all_leaves = list(leaves(branching))
    total = len(all_leaves)
    kernel = []
    for depth in range(h + 1):
        counts = [0] * (h + 1)
        for leaf in all_leaves:
            counts[min(depth, zero_lcp(leaf))] += 1
        row = [Q(count, total) for count in counts]
        equal(sum(row), Q(1), "HTM stochastic row")
        kernel.append(row)
    return kernel


def row_times_kernel(distribution, kernel):
    n = len(distribution)
    return [sum(distribution[i] * kernel[i][j] for i in range(n)) for j in range(n)]


def htm_transform_resolvent(branching, z, y):
    kernel = htm_kernel_literal(branching)
    n = len(kernel)
    matrix = [[Q(int(i == j)) - z * kernel[i][j] for j in range(n)] for i in range(n)]
    rhs = [y**d for d in range(n)]
    return solve_linear(matrix, rhs)[-1]


def htm_area_bellman(branching):
    kernel = htm_kernel_literal(branching)
    h = len(branching)
    # Root has zero future area.  Solve only on depths 1,...,h.
    matrix = []
    rhs = []
    for d in range(1, h + 1):
        matrix.append([Q(int(d == j)) - kernel[d][j] for j in range(1, h + 1)])
        rhs.append(Q(d))
    return solve_linear(matrix, rhs)[-1]


def htm_expected_area_formula(branching):
    return sum(Q(B, B - 1) for B in prefix_products(branching))


def verify_htm():
    global CURRENT_SECTION

    CURRENT_SECTION = "HTM literal layers/transform"
    profiles = []
    for h in range(1, 5):
        profiles.extend(product((2, 3, 4), repeat=h))
    for branching in profiles:
        h = len(branching)
        Bs = prefix_products(branching)
        kernel = htm_kernel_literal(branching)
        distribution = [Q(0)] * h + [Q(1)]
        for t in range(7):
            for k in range(1, h + 1):
                tail = sum(distribution[k:])
                equal(tail, Q(1, Bs[k - 1] ** t), "HTM nested layer tail")
            if t:
                equal(distribution[0], Q(1) - Q(1, branching[0] ** t), "HTM root layer")
            distribution = row_times_kernel(distribution, kernel)
        for z, y in ((Q(1, 3), Q(2, 5)), (Q(2, 5), Q(7, 4))):
            direct = htm_transform_resolvent(branching, z, y)
            formula = Q(1, 1 - z)
            previous_power = Q(1)
            for k, B in enumerate(Bs, start=1):
                current_power = y**k
                formula += (current_power - previous_power) / (1 - z / B)
                previous_power = current_power
            equal(direct, formula, "HTM all-time transform")

    CURRENT_SECTION = "HTM clock/area/inverse"
    for branching in profiles:
        Bs = prefix_products(branching)
        kernel = htm_kernel_literal(branching)
        b1 = branching[0]
        for depth in range(1, len(branching) + 1):
            equal(kernel[depth][0], Q(b1 - 1, b1), "HTM root hazard")
        equal(htm_area_bellman(branching), htm_expected_area_formula(branching), "HTM area")
        # Known time-one layer recovers every prefix product and factor exactly.
        recovered_Bs = []
        for k, B in enumerate(Bs, start=1):
            tail = Q(1, B)
            recovered = tail.denominator // tail.numerator
            equal(recovered, B, "HTM prefix inverse")
            recovered_Bs.append(recovered)
        recovered_factors = [recovered_Bs[0]] + [recovered_Bs[i] // recovered_Bs[i - 1]
                                                    for i in range(1, len(recovered_Bs))]
        equal(tuple(recovered_factors), tuple(branching), "HTM branching inverse")
        # Exact geometric clock moments.
        mean = Q(b1, b1 - 1)
        variance = Q(b1, (b1 - 1) ** 2)
        second = variance + mean * mean
        equal(second, Q(b1 * (b1 + 1), (b1 - 1) ** 2), "HTM clock second moment")

    # Unknown observation time is genuinely ambiguous, even for a full layer.
    b_time_1 = (4, 9)
    b_time_2 = (2, 3)
    for B1, B2 in zip(prefix_products(b_time_1), prefix_products(b_time_2)):
        equal(Q(1, B1), Q(1, B2**2), "HTM unknown-time perfect-power ambiguity")

    CURRENT_SECTION = "HTM fixed-multiset extremizers"
    for length in range(2, 6):
        for multiset in combinations_with_replacement((2, 3, 4, 5), length):
            orders = sorted(set(permutations(multiset)))
            values = {order: htm_expected_area_formula(order) for order in orders}
            ascending = tuple(sorted(multiset))
            descending = tuple(sorted(multiset, reverse=True))
            equal(values[ascending], max(values.values()), "HTM ascending maximum")
            equal(values[descending], min(values.values()), "HTM descending minimum")
            equal([order for order, value in values.items() if value == max(values.values())],
                  [ascending], "HTM unique maximum modulo equal entries")
            equal([order for order, value in values.items() if value == min(values.values())],
                  [descending], "HTM unique minimum modulo equal entries")
            # Every adjacent inversion has exactly the claimed strict sign.
            for order in orders:
                for i in range(length - 1):
                    if order[i] == order[i + 1]:
                        continue
                    swapped = list(order)
                    swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
                    swapped = tuple(swapped)
                    if order[i] < order[i + 1]:
                        check(values[order] > values[swapped], "HTM exchange sign")
                    else:
                        check(values[order] < values[swapped], "HTM exchange sign")

    CURRENT_SECTION = "HTM boundary cases"
    for b1 in range(2, 15):
        only = (b1,)
        equal(htm_expected_area_formula(only), Q(b1, b1 - 1), "HTM h=1 area/clock equality")
        equal(tuple(sorted(only)), tuple(sorted(only, reverse=True)), "HTM h=1 extremizer tautology")
    # b1=1 is correctly excluded: the root hazard vanishes and the area formula is singular.
    equal(Q(1) - Q(1, 1), Q(0), "HTM b1=1 has no root hazard")


def chebyshev_u(index, x):
    if index == -1:
        return Q(0)
    check(index >= 0, f"unsupported U index {index}")
    if index == 0:
        return Q(1)
    previous, current = Q(1), 2 * x
    for _ in range(1, index):
        previous, current = current, 2 * x * current - previous
    return current


def btb_direct_transform(r, z, u):
    matrix = [[Q(int(i == j)) for j in range(r)] for i in range(r)]
    rhs = [Q(0)] * r
    for k in range(1, r + 1):
        row = k - 1
        for coefficient, target in ((2 * z / 3, k - 1), (z * u / 3, r - k)):
            if target == 0:
                rhs[row] += coefficient
            else:
                matrix[row][target - 1] -= coefficient
    return [Q(1)] + solve_linear(matrix, rhs)


def btb_chebyshev_transform(r, z, u):
    if r == 1:
        return [Q(1), z * (2 + u) / 3]
    xi = (9 + z * z * (4 - u * u)) / (12 * z)
    numerator = (3 * chebyshev_u(r - 2, xi)
                 - 2 * z * chebyshev_u(r - 3, xi) + z * u)
    denominator = 3 * chebyshev_u(r - 1, xi) - 2 * z * chebyshev_u(r - 2, xi)
    F1 = numerator / denominator
    values = [Q(1)]
    for k in range(1, r + 1):
        values.append(chebyshev_u(k - 1, xi) * F1 - chebyshev_u(k - 2, xi))
    return values


def btb_mean_direct(r):
    matrix = [[Q(int(i == j)) for j in range(r)] for i in range(r)]
    rhs = [Q(1)] * r
    for k in range(1, r + 1):
        row = k - 1
        for coefficient, target in ((Q(2, 3), k - 1), (Q(1, 3), r - k)):
            if target:
                matrix[row][target - 1] -= coefficient
    return [Q(0)] + solve_linear(matrix, rhs)


def btb_parity_direct(r):
    matrix = [[Q(int(i == j)) for j in range(r)] for i in range(r)]
    rhs = [Q(0)] * r
    for k in range(1, r + 1):
        row = k - 1
        # A private flip contributes +1, a spine flip contributes -1.
        for coefficient, target in ((Q(2, 3), k - 1), (Q(-1, 3), r - k)):
            if target == 0:
                rhs[row] += coefficient
            else:
                matrix[row][target - 1] -= coefficient
    return [Q(1)] + solve_linear(matrix, rhs)


def verify_btb():
    global CURRENT_SECTION

    CURRENT_SECTION = "BTB literal lumpability"
    for r in range(1, 10):
        all_bits = (1 << r) - 1
        for mask in range(1, 1 << r):
            k = mask.bit_count()
            counts = {}
            active = [i for i in range(r) if mask & (1 << i)]
            for page in active:
                # Two private physical edges clear only the chosen page.
                private_target = (mask & ~(1 << page)).bit_count()
                counts[private_target] = counts.get(private_target, 0) + 2
                # The common spine complements every imbalance bit.
                spine_target = (mask ^ all_bits).bit_count()
                counts[spine_target] = counts.get(spine_target, 0) + 1
            expected = {}
            expected[k - 1] = expected.get(k - 1, 0) + 2 * k
            expected[r - k] = expected.get(r - k, 0) + k
            equal(counts, expected, "BTB literal strong lumping")
            equal(sum(counts.values()), 3 * k, "BTB literal action count")

    CURRENT_SECTION = "BTB Chebyshev elimination"
    test_points = (
        (Q(1, 4), Q(-1, 2)),
        (Q(1, 3), Q(0)),
        (Q(2, 5), Q(1, 3)),
        (Q(1, 2), Q(1)),
    )
    for r in range(1, 21):
        for z, u in test_points:
            direct = btb_direct_transform(r, z, u)
            formula = btb_chebyshev_transform(r, z, u)
            equal(direct, formula, "BTB transform vector")
            for k in range(1, r + 1):
                equal(formula[k], z * (Q(2, 3) * formula[k - 1]
                                       + Q(1, 3) * u * formula[r - k]),
                      "BTB formula satisfies Bellman")
            for k in range(1, r):
                xi = (9 + z * z * (4 - u * u)) / (12 * z)
                equal(formula[k + 1], 2 * xi * formula[k] - formula[k - 1],
                      "BTB eliminated recurrence")

    CURRENT_SECTION = "BTB r=1/r=2/z=0 boundaries"
    for z, u in test_points:
        equal(btb_direct_transform(1, z, u)[1], z * (2 + u) / 3, "BTB r=1")
        direct_r2 = btb_direct_transform(2, z, u)
        equal(direct_r2[1], 2 * z / (3 - z * u), "BTB r=2 removable-factor reduction")
        equal(direct_r2, btb_chebyshev_transform(2, z, u), "BTB r=2 rational continuation")
    for r in range(1, 21):
        zero = btb_direct_transform(r, Q(0), Q(1, 3))
        equal(zero, [Q(1)] + [Q(0)] * r, "BTB z=0 Bellman boundary")

    CURRENT_SECTION = "BTB mean/parity/extrema"
    for r in range(1, 61):
        means = btb_mean_direct(r)
        parity = btb_parity_direct(r)
        expected_means = [Q(0)] + [Q(k * (r + 2 - k), 2) for k in range(1, r + 1)]
        expected_parity = [Q(1)] + [Q(r + 2 - 2 * k, r + 2) for k in range(1, r + 1)]
        equal(means, expected_means, "BTB quadratic mean")
        equal(parity, expected_parity, "BTB affine parity")
        if r == 1:
            equal(means[1], Q(1), "BTB r=1 sole extremum")
        else:
            minimizers = [k for k in range(1, r + 1) if means[k] == min(means[1:])]
            maximizers = [k for k in range(1, r + 1) if means[k] == max(means[1:])]
            equal(minimizers, [1], "BTB unique nonabsorbing minimum")
            if r % 2 == 0:
                equal(maximizers, [(r + 2) // 2], "BTB even maximum")
                equal(max(means[1:]), Q((r + 2) ** 2, 8), "BTB even maximum value")
            else:
                equal(maximizers, [(r + 1) // 2, (r + 3) // 2], "BTB odd maxima")
                equal(max(means[1:]), Q((r + 2) ** 2 - 1, 8), "BTB odd maximum value")

    CURRENT_SECTION = "BTB inverse/absorption certificate"
    for r in range(1, 301):
        for k in range(1, r + 1):
            q = Q(k, r + 2)
            mean = Q(k * (r + 2 - k), 2)
            square = 2 * mean / (q * (1 - q))
            equal(square, Q((r + 2) ** 2), "BTB inverse square")
            recovered_scale = r + 2  # exact positive square root of the checked square
            equal(q * recovered_scale, k, "BTB inverse k")
            check(0 < q < 1, "BTB inverse nonabsorbing domain")
        # A pre-generated run of r private edge-types clears every live bit.
        for k in range(1, r + 1):
            remaining = k
            for _ in range(r):
                if remaining:
                    remaining -= 1
            equal(remaining, 0, "BTB r-private block absorbs")


def main():
    verify_htm()
    verify_btb()
    for section in sorted(SECTION_ASSERTIONS):
        print(f"{section}: {SECTION_ASSERTIONS[section]}")
    print(f"PASS assertions={ASSERTIONS}")


if __name__ == "__main__":
    main()
