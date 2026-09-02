#!/usr/bin/env python3
"""Exact falsifier for P152 triangular-book local triad dynamics.

The script is self-contained and uses only integers and fractions.Fraction.
It enumerates literal bit states and independently solves rational Bellman
systems; it is counterexample pressure, not an all-parameter proof, ownership
certificate, or release gate.
"""

from fractions import Fraction as Q
from math import isqrt


ASSERTIONS = 0
SECTION_ASSERTIONS = {}
CURRENT_SECTION = "setup"
DIAGNOSTICS = {}


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    SECTION_ASSERTIONS[CURRENT_SECTION] = SECTION_ASSERTIONS.get(CURRENT_SECTION, 0) + 1
    if not condition:
        raise AssertionError(message)


def equal(left, right, message="exact equality failed"):
    check(left == right, f"{message}: {left!r} != {right!r}")


def solve_linear(matrix, rhs):
    """Solve a square rational system by deterministic Gauss--Jordan elimination."""
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


def direct_transform(r, z, u):
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


def chebyshev_transform(r, z, u):
    if r == 1:
        return [Q(1), z * (2 + u) / 3]
    xi = (9 + z * z * (4 - u * u)) / (12 * z)
    numerator = (3 * chebyshev_u(r - 2, xi)
                 - 2 * z * chebyshev_u(r - 3, xi) + z * u)
    denominator = 3 * chebyshev_u(r - 1, xi) - 2 * z * chebyshev_u(r - 2, xi)
    first = numerator / denominator
    values = [Q(1)]
    for k in range(1, r + 1):
        values.append(chebyshev_u(k - 1, xi) * first - chebyshev_u(k - 2, xi))
    return values


def mean_direct(r):
    matrix = [[Q(int(i == j)) for j in range(r)] for i in range(r)]
    rhs = [Q(1)] * r
    for k in range(1, r + 1):
        row = k - 1
        for coefficient, target in ((Q(2, 3), k - 1), (Q(1, 3), r - k)):
            if target:
                matrix[row][target - 1] -= coefficient
    return [Q(0)] + solve_linear(matrix, rhs)


def parity_direct(r):
    matrix = [[Q(int(i == j)) for j in range(r)] for i in range(r)]
    rhs = [Q(0)] * r
    for k in range(1, r + 1):
        row = k - 1
        # A private flip has parity mark +1; a spine flip has parity mark -1.
        for coefficient, target in ((Q(2, 3), k - 1), (Q(-1, 3), r - k)):
            if target == 0:
                rhs[row] += coefficient
            else:
                matrix[row][target - 1] -= coefficient
    return [Q(1)] + solve_linear(matrix, rhs)


def mean_formula(r, k):
    return Q(k * (r + 2 - k), 2)


def odd_spine_probability(r, k):
    return Q(k, r + 2)


def inverse_criterion(mean, odd_probability):
    """Implement the exact feasible-image criterion without floating point."""
    mean, odd_probability = Q(mean), Q(odd_probability)
    if not Q(0) < odd_probability < Q(1):
        return None
    square = 2 * mean / (odd_probability * (1 - odd_probability))
    if square < 0 or square.denominator != 1:
        return None
    scale = isqrt(square.numerator)
    if scale * scale != square.numerator or scale < 3:
        return None
    count = odd_probability * scale
    if count.denominator != 1:
        return None
    count = count.numerator
    if not 1 <= count <= scale - 2:
        return None
    return scale - 2, count


def survival_probability(r, start, steps):
    """Exact nonabsorption mass after ``steps`` quotient updates."""
    distribution = {start: Q(1)}
    for _ in range(steps):
        successor = {}
        for state, mass in distribution.items():
            for probability, target in ((Q(2, 3), state - 1),
                                        (Q(1, 3), r - state)):
                if target:
                    successor[target] = successor.get(target, Q(0)) + mass * probability
        distribution = successor
    return sum(distribution.values(), Q(0))


def verify_literal_lumping():
    global CURRENT_SECTION
    CURRENT_SECTION = "BTB literal lumpability"
    for r in range(1, 10):
        all_bits = (1 << r) - 1
        for mask in range(1, 1 << r):
            k = mask.bit_count()
            counts = {}
            active = [i for i in range(r) if mask & (1 << i)]
            for page in active:
                # The two private edges clear only the selected active page.
                private_target = (mask & ~(1 << page)).bit_count()
                counts[private_target] = counts.get(private_target, 0) + 2
                # The common spine complements all imbalance bits.
                spine_target = (mask ^ all_bits).bit_count()
                counts[spine_target] = counts.get(spine_target, 0) + 1
            expected = {}
            expected[k - 1] = expected.get(k - 1, 0) + 2 * k
            expected[r - k] = expected.get(r - k, 0) + k
            equal(counts, expected, "literal strong lumping")
            equal(sum(counts.values()), 3 * k, "literal action count")


def verify_transform():
    global CURRENT_SECTION
    CURRENT_SECTION = "BTB Chebyshev elimination"
    test_points = (
        (Q(1, 4), Q(-1, 2)),
        (Q(1, 3), Q(0)),
        (Q(2, 5), Q(1, 3)),
        (Q(1, 2), Q(1)),
    )
    for r in range(1, 21):
        for z, u in test_points:
            direct = direct_transform(r, z, u)
            formula = chebyshev_transform(r, z, u)
            equal(direct, formula, "transform vector")
            for k in range(1, r + 1):
                equal(formula[k], z * (Q(2, 3) * formula[k - 1]
                                       + Q(1, 3) * u * formula[r - k]),
                      "formula satisfies Bellman")
            for k in range(1, r):
                xi = (9 + z * z * (4 - u * u)) / (12 * z)
                equal(formula[k + 1], 2 * xi * formula[k] - formula[k - 1],
                      "eliminated recurrence")

    CURRENT_SECTION = "BTB r=1/r=2/z=0 boundaries"
    for z, u in test_points:
        equal(direct_transform(1, z, u)[1], z * (2 + u) / 3, "r=1")
        direct_r2 = direct_transform(2, z, u)
        equal(direct_r2[1], 2 * z / (3 - z * u), "r=2 reduced factor")
        equal(direct_r2, chebyshev_transform(2, z, u), "r=2 continuation")
    for r in range(1, 21):
        zero = direct_transform(r, Q(0), Q(1, 3))
        equal(zero, [Q(1)] + [Q(0)] * r, "z=0 Bellman boundary")


def verify_mean_parity_extrema():
    global CURRENT_SECTION
    CURRENT_SECTION = "BTB mean/parity/extrema"
    for r in range(1, 61):
        means = mean_direct(r)
        parity = parity_direct(r)
        expected_means = [Q(0)] + [Q(k * (r + 2 - k), 2) for k in range(1, r + 1)]
        expected_parity = [Q(1)] + [Q(r + 2 - 2 * k, r + 2) for k in range(1, r + 1)]
        equal(means, expected_means, "quadratic mean")
        equal(parity, expected_parity, "affine parity")
        if r == 1:
            equal(means[1], Q(1), "r=1 sole extremum")
        else:
            minimizers = [k for k in range(1, r + 1) if means[k] == min(means[1:])]
            maximizers = [k for k in range(1, r + 1) if means[k] == max(means[1:])]
            equal(minimizers, [1], "unique nonabsorbing minimum")
            if r % 2 == 0:
                equal(maximizers, [(r + 2) // 2], "even maximum")
                equal(max(means[1:]), Q((r + 2) ** 2, 8), "even maximum value")
            else:
                equal(maximizers, [(r + 1) // 2, (r + 3) // 2], "odd maxima")
                equal(max(means[1:]), Q((r + 2) ** 2 - 1, 8), "odd maximum value")


def verify_inverse_and_absorption():
    global CURRENT_SECTION
    CURRENT_SECTION = "BTB inverse/absorption certificate"
    for r in range(1, 301):
        for k in range(1, r + 1):
            q = Q(k, r + 2)
            mean = Q(k * (r + 2 - k), 2)
            square = 2 * mean / (q * (1 - q))
            equal(square, Q((r + 2) ** 2), "inverse square")
            recovered_scale = r + 2
            equal(q * recovered_scale, k, "inverse count")
            check(0 < q < 1, "inverse nonabsorbing domain")
        # A pre-generated run of r private edge-types clears every live bit.
        for k in range(1, r + 1):
            remaining = k
            for _ in range(r):
                if remaining:
                    remaining -= 1
            equal(remaining, 0, "r-private block absorbs")


def verify_inverse_iff_and_collisions():
    """Pressure both directions of the exact inverse on a bounded rational grid."""
    global CURRENT_SECTION
    CURRENT_SECTION = "BTB inverse iff grid/collisions"

    # All exact observations from R=r+2<=26.  On the candidate grid below,
    # m<=20 and min q(1-q)=11/144, so any feasible R has R^2<=5760/11<24^2.
    # Thus r<=24 is a rigorous complete search envelope for that grid.
    literal_image = {}
    for r in range(1, 25):
        for k in range(1, r + 1):
            observation = (mean_formula(r, k), odd_spine_probability(r, k))
            check(observation not in literal_image, "two-statistic image collision")
            literal_image[observation] = (r, k)

    q_grid = sorted({Q(a, d) for d in range(2, 13) for a in range(1, d)})
    m_grid = [Q(n, 8) for n in range(-2, 161)]
    rejected = 0
    accepted = 0
    for mean in m_grid:
        for odd_probability in q_grid:
            recovered = inverse_criterion(mean, odd_probability)
            expected = literal_image.get((mean, odd_probability))
            equal(recovered, expected, "bounded exact inverse iff")
            if recovered is None:
                rejected += 1
            else:
                accepted += 1

    # Hand-picked exact failures isolate every rejection gate, including
    # the open-q domain, negative/zero scale, nonsquare scale, rational but
    # nonintegral scale, scale below three, nonintegral k, and k>R-2.
    impossible = (
        (Q(1), Q(0)),
        (Q(1), Q(1)),
        (Q(1), Q(-1, 3)),
        (Q(1), Q(4, 3)),
        (Q(-1), Q(1, 2)),
        (Q(0), Q(1, 2)),
        (Q(2), Q(1, 3)),
        (Q(49, 32), Q(1, 2)),
        (Q(4, 9), Q(1, 3)),
        (Q(25, 8), Q(1, 2)),
        (Q(2), Q(4, 5)),
        (Q(1), Q(2, 3)),
    )
    for mean, odd_probability in impossible:
        equal(inverse_criterion(mean, odd_probability), None,
              "infeasible exact candidate rejected")

    # The two scalar collisions printed in the manuscript are checked as
    # collisions, not merely mentioned as prose examples.
    q_left = odd_spine_probability(1, 1)
    q_right = odd_spine_probability(4, 2)
    equal(q_left, q_right, "parity-only collision")
    equal(q_left, Q(1, 3), "parity-only collision value")
    check(mean_formula(1, 1) != mean_formula(4, 2),
          "parity collision must be separated by the mean")
    check((1, 1) != (4, 2), "parity collision uses distinct states")

    m_left = mean_formula(2, 2)
    m_right = mean_formula(3, 1)
    equal(m_left, m_right, "mean-only collision")
    equal(m_left, Q(2), "mean-only collision value")
    check(odd_spine_probability(2, 2) != odd_spine_probability(3, 1),
          "mean collision must be separated by parity")
    check((2, 2) != (3, 1), "mean collision uses distinct states")

    DIAGNOSTICS["inverse_grid_candidates"] = len(m_grid) * len(q_grid)
    DIAGNOSTICS["inverse_grid_accepted"] = accepted
    DIAGNOSTICS["inverse_grid_rejected"] = rejected
    DIAGNOSTICS["explicit_infeasible_candidates"] = len(impossible)
    DIAGNOSTICS["single_statistic_collision_pairs"] = 2


def verify_private_block_probability_and_tail():
    """Check exact block masses and finite instances of the tail inequality."""
    global CURRENT_SECTION
    CURRENT_SECTION = "BTB private-block probability/tail"
    tail_instances = 0
    block_words = 0
    for r in range(1, 13):
        total_mass = Q(0)
        all_private_mass = Q(0)
        for word in range(1 << r):
            private_choices = word.bit_count()
            mass = Q(2, 3) ** private_choices * Q(1, 3) ** (r - private_choices)
            total_mass += mass
            block_words += 1
            if private_choices == r:
                all_private_mass += mass
        equal(total_mass, Q(1), "private/spine word mass")
        equal(all_private_mass, Q(2, 3) ** r, "all-private block probability")

        for start in range(1, r + 1):
            for blocks in range(0, 7):
                tail = survival_probability(r, start, blocks * r)
                bound = (1 - Q(2, 3) ** r) ** blocks
                check(tail <= bound, "finite exact block-tail inequality")
                tail_instances += 1
                if blocks == 0:
                    equal(tail, bound, "n=0 tail boundary")

    DIAGNOSTICS["private_block_words"] = block_words
    DIAGNOSTICS["tail_bound_instances"] = tail_instances


def main():
    verify_literal_lumping()
    verify_transform()
    verify_mean_parity_extrema()
    verify_inverse_and_absorption()
    verify_inverse_iff_and_collisions()
    verify_private_block_probability_and_tail()
    print("P152 triangular-book exact verifier")
    for section in sorted(SECTION_ASSERTIONS):
        print(f"{section}: {SECTION_ASSERTIONS[section]}")
    for diagnostic in sorted(DIAGNOSTICS):
        print(f"{diagnostic}={DIAGNOSTICS[diagnostic]}")
    print(f"assertions={ASSERTIONS}")
    print("arithmetic=integer_and_Fraction_only")
    print("enumeration_is_not_proof=1")
    print("external_status=HOLD_EXTERNAL")
    print("PASS")


if __name__ == "__main__":
    main()
