#!/usr/bin/env python3
"""Independent hostile verifier for adaptive quotient-normalized rotation.

This file deliberately imports no scouting or author implementation.  It
tests the displayed update from first principles, including the distinction
between overlapping coordinate hyperplanes and the disjoint change-stratum
decomposition of the image.
"""

from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
from math import comb, gcd


class Audit:
    def __init__(self):
        self.assertions = 0

    def check(self, condition, label):
        self.assertions += 1
        if not condition:
            raise AssertionError(label)


A = Audit()


@lru_cache(maxsize=None)
def words(q, n):
    return tuple(product(range(q), repeat=n))


def rot(w, shift):
    n = len(w)
    shift %= n
    return w[shift:] + w[:shift]


def delta(w, q):
    n = len(w)
    return tuple((w[(i + 1) % n] - w[i]) % q for i in range(n))


def changes(w, q):
    return sum(x != 0 for x in delta(w, q))


def add_constant(w, a, q):
    return tuple((x + a) % q for x in w)


def step(w, q, c):
    s = c * changes(w, q)
    shifted = rot(w, s)
    return tuple((x - w[0]) % q for x in shifted)


def repeated_step(w, q, c, t):
    out = w
    for _ in range(t):
        out = step(out, q, c)
    return out


def proposed_iterate(w, q, c, t):
    if t == 0:
        return w
    n = len(w)
    s = (c * changes(w, q)) % n
    shifted = rot(w, t * s)
    offset = w[((t - 1) * s) % n]
    return tuple((x - offset) % q for x in shifted)


def supported(y, q, c):
    n = len(y)
    return y[(-c * changes(y, q)) % n] == 0


def predicted_sources(y, q, c, t):
    if not supported(y, q, c):
        return set()
    n = len(y)
    s = (c * changes(y, q)) % n
    base = rot(y, -t * s)
    return {add_constant(base, a, q) for a in range(q)}


def zero_histogram(source_set):
    return Counter(sum(x == 0 for x in source) for source in source_set)


def target_symbol_histogram(y, q):
    multiplicities = Counter(y)
    return Counter(multiplicities.get(a, 0) for a in range(q))


def zero_sum_nonzero_tuples(q, length):
    if length == 0:
        return 1
    return ((q - 1) ** length + (q - 1) * ((-1) ** length)) // q


def stratum_formula(q, n, k):
    return comb(n, k) * zero_sum_nonzero_tuples(q, k)


def fixed_formula(q, n, c, ell):
    answer = 0
    branch = Counter()
    for k in range(n + 1):
        g = gcd(n, ell * c * k)
        r = n // g
        if k % r:
            branch["r_not_divide_k"] += 1
            continue
        s = k // r
        if r % q == 0:
            term = comb(g, s) * (q - 1) ** s
            branch["q_divides_r"] += 1
        else:
            term = comb(g, s) * zero_sum_nonzero_tuples(q, s)
            branch["q_not_divide_r"] += 1
        answer += term
    return answer, branch


def least_rotation_period(w):
    return next(p for p in range(1, len(w) + 1) if rot(w, p) == w)


def point_period(y, q, c):
    current = step(y, q, c)
    period = 1
    while current != y:
        current = step(current, q, c)
        period += 1
        A.check(period <= len(y), ("period failed to close", q, c, y))
    return period


def reflect(w):
    n = len(w)
    return tuple(w[(-i) % n] for i in range(n))


def analyse_configuration(q, n, c, branch_totals):
    carrier = words(q, n)
    t_values = tuple(sorted({1, 2, n, n + 1, 2 * n + 3}))

    next_map = {w: step(w, q, c) for w in carrier}
    for w in carrier:
        d = delta(w, q)
        image = next_map[w]
        s = c * changes(w, q)
        A.check(sum(d) % q == 0, ("difference sum", q, n, c, w))
        A.check(changes(image, q) == changes(w, q), ("change invariant", q, n, c, w))
        A.check(delta(image, q) == rot(d, s), ("difference rotation", q, n, c, w))
        for t in range(0, n + 3):
            A.check(
                repeated_step(w, q, c, t) == proposed_iterate(w, q, c, t),
                ("iterate", q, n, c, t, w),
            )

    actual_image = set(next_map.values())
    predicted_image = {y for y in carrier if supported(y, q, c)}
    A.check(actual_image == predicted_image, ("image characterization", q, n, c))
    A.check(len(actual_image) == q ** (n - 1), ("image size", q, n, c))

    # The only disjoint union is by actual change stratum.  The unqualified
    # coordinate hyperplanes overlap and their raw union is generally larger.
    reconstructed = set()
    for k in range(n + 1):
        piece = {
            y
            for y in carrier
            if changes(y, q) == k and y[(-c * k) % n] == 0
        }
        A.check(not (reconstructed & piece), ("stratum pieces overlap", q, n, c, k))
        reconstructed |= piece
    A.check(reconstructed == actual_image, ("disjoint image union", q, n, c))
    for y in carrier:
        compatible_pieces = sum(
            changes(y, q) == k and y[(-c * k) % n] == 0
            for k in range(n + 1)
        )
        A.check(compatible_pieces == int(y in actual_image), ("piece membership", q, n, c, y))

    for k in range(n + 1):
        observed = sum(changes(y, q) == k for y in actual_image)
        A.check(observed == stratum_formula(q, n, k), ("stratum count", q, n, c, k))

    # Direct time-t fibre enumeration; no use of the closed iterate here.
    reference_weight = {}
    for t in t_values:
        actual_fibres = defaultdict(set)
        for source in carrier:
            actual_fibres[repeated_step(source, q, c, t)].add(source)
        A.check(set(actual_fibres) == actual_image, ("time image", q, n, c, t))
        for y in carrier:
            actual = actual_fibres.get(y, set())
            predicted = predicted_sources(y, q, c, t)
            A.check(actual == predicted, ("time fibre", q, n, c, t, y))
            A.check(len(actual) == (q if y in actual_image else 0), ("fibre size", q, n, c, t, y))
            if y in actual_image:
                observed_weight = zero_histogram(actual)
                desired_weight = target_symbol_histogram(y, q)
                A.check(observed_weight == desired_weight, ("weighted fibre", q, n, c, t, y))
                if y in reference_weight:
                    A.check(observed_weight == reference_weight[y], ("t independence", q, n, c, t, y))
                else:
                    reference_weight[y] = observed_weight

    # Every recurrent vertex has one recurrent predecessor and q-1 leaves.
    one_step_fibres = defaultdict(set)
    for source, target in next_map.items():
        one_step_fibres[target].add(source)
    for y in actual_image:
        sources = one_step_fibres[y]
        A.check(len(sources) == q, ("one-step indegree", q, n, c, y))
        recurrent_sources = sources & actual_image
        A.check(len(recurrent_sources) == 1, ("recurrent predecessor", q, n, c, y))
        A.check(len(sources - actual_image) == q - 1, ("leaf count", q, n, c, y))
        p = least_rotation_period(delta(y, q))
        desired_period = p // gcd(p, c * changes(y, q))
        A.check(point_period(y, q, c) == desired_period, ("point period", q, n, c, y))

    for ell in range(1, 2 * n + 4):
        observed = sum(repeated_step(y, q, c, ell) == y for y in actual_image)
        desired, branches = fixed_formula(q, n, c, ell)
        branch_totals.update(branches)
        A.check(observed == desired, ("fixed formula", q, n, c, ell, observed, desired))

    return actual_image


def showcase():
    q, n, c = 3, 6, 1
    image = {y for y in words(q, n) if supported(y, q, c)}
    periods = Counter(point_period(y, q, c) for y in image)
    strata = Counter(changes(y, q) for y in image)
    fixed = tuple(
        (ell, sum(repeated_step(y, q, c, ell) == y for y in image))
        for ell in range(1, 7)
    )
    return len(image), tuple(sorted(periods.items())), tuple(sorted(strata.items())), fixed


def overlap_and_time_witnesses():
    q, n, c = 3, 5, 1
    carrier = words(q, n)
    zero = (0,) * n
    memberships = tuple(k for k in range(n + 1) if zero[(-c * k) % n] == 0)
    raw_union = {y for y in carrier if any(y[(-c * k) % n] == 0 for k in range(n + 1))}
    true_image = {y for y in carrier if supported(y, q, c)}
    false_positive = min(raw_union - true_image)
    A.check(memberships == tuple(range(n + 1)), "zero hyperplane overlap")
    A.check(false_positive not in true_image, "raw-union false positive")

    time_witness = None
    for y in sorted(true_image):
        f1 = predicted_sources(y, q, c, 1)
        f2 = predicted_sources(y, q, c, 2)
        if f1 != f2:
            A.check(zero_histogram(f1) == zero_histogram(f2), ("witness polynomial", y))
            time_witness = (
                y,
                tuple(sorted(f1 - f2)),
                tuple(sorted(f2 - f1)),
                tuple(sorted(zero_histogram(f1).items())),
            )
            break
    A.check(time_witness is not None, "missing time-varying fibre witness")
    return memberships, len(raw_union), len(true_image), false_positive, time_witness


def recovery_audit():
    rows = []
    for q, max_n in ((3, 7), (5, 5), (7, 4)):
        for n in range(3, max_n + 1):
            atlases = []
            for c in range(n):
                image = {y for y in words(q, n) if supported(y, q, c)}
                atlases.append(frozenset(image))
                z2 = {
                    y.index(0)
                    for y in image
                    if changes(y, q) == 2 and y.count(0) == 1
                }
                z3 = {
                    y.index(0)
                    for y in image
                    if changes(y, q) == 3 and y.count(0) == 1
                }
                A.check(z2 == {(-2 * c) % n}, ("z2 recovery", q, n, c, z2))
                A.check(z3 == {(-3 * c) % n}, ("z3 recovery", q, n, c, z3))
                recovered = (next(iter(z2)) - next(iter(z3))) % n
                A.check(recovered == c, ("c recovery", q, n, c, recovered))
                reflected = {reflect(y) for y in image}
                opposite = {y for y in words(q, n) if supported(y, q, (-c) % n)}
                A.check(reflected == opposite, ("reflection conjugacy", q, n, c))
            A.check(len(set(atlases)) == n, ("distinct labelled atlases", q, n))
            rows.append((q, n, len(set(atlases))))
    return rows


def binary_and_small_boundaries():
    binary_rows = []
    for n in range(3, 10):
        grouped = defaultdict(list)
        for c in range(n):
            image = frozenset(y for y in words(2, n) if supported(y, 2, c))
            grouped[image].append(c)
        classes = tuple(sorted(tuple(v) for v in grouped.values()))
        expected = n if n % 2 else n // 2
        A.check(len(classes) == expected, ("binary atlas classes", n, classes))
        binary_rows.append((n, classes))

    n2_rows = []
    for q in (3, 5, 7):
        atlases = [
            frozenset(y for y in words(q, 2) if supported(y, q, c))
            for c in range(2)
        ]
        A.check(atlases[0] == atlases[1], ("n=2 collapse", q))
        n2_rows.append((q, len(set(atlases))))

    n1_rows = []
    for q in (2, 3, 5, 7):
        carrier = words(q, 1)
        image = {step(w, q, 0) for w in carrier}
        A.check(image == {(0,)}, ("n=1 image", q))
        A.check(sum(step(w, q, 0) == (0,) for w in carrier) == q, ("n=1 fibre", q))
        n1_rows.append((q, len(carrier), len(image)))
    return binary_rows, n2_rows, n1_rows


def c_zero_audit():
    rows = []
    for q, n in ((2, 8), (3, 6), (5, 4), (7, 3)):
        image = {step(w, q, 0) for w in words(q, n)}
        A.check(image == {y for y in words(q, n) if y[0] == 0}, ("c0 image", q, n))
        A.check(all(step(y, q, 0) == y for y in image), ("c0 idempotence", q, n))
        rows.append((q, n, len(image), q ** n - len(image)))
    return rows


def main():
    configs = []
    for q, max_n in ((2, 9), (3, 7), (5, 5), (7, 4)):
        for n in range(1, max_n + 1):
            for c in range(n):
                configs.append((q, n, c))

    branch_totals = Counter()
    for q, n, c in configs:
        analyse_configuration(q, n, c, branch_totals)

    image_size, periods, strata, fixed = showcase()
    memberships, raw_size, true_size, false_positive, time_witness = overlap_and_time_witnesses()
    recovery_rows = recovery_audit()
    binary_rows, n2_rows, n1_rows = binary_and_small_boundaries()
    c0_rows = c_zero_audit()

    A.check(branch_totals["q_divides_r"] > 0, "q|r branch untested")
    A.check(branch_totals["q_not_divide_r"] > 0, "q does not divide r branch untested")
    A.check(branch_totals["r_not_divide_k"] > 0, "r not divide k branch untested")

    print("AQN HOSTILE SPECIALIST GATE — INDEPENDENT EXACT ENUMERATION")
    print(f"scope=configurations:{len(configs)},q=2:n<=9,q=3:n<=7,q=5:n<=5,q=7:n<=4,all_c")
    print(f"showcase=q3,n6,c1:image:{image_size},point_periods:{periods},strata:{strata}")
    print(f"showcase_fixed={fixed}")
    print(
        "raw_hyperplane_attack="
        f"q3,n5,c1,zero_memberships:{memberships},raw_union:{raw_size},"
        f"true_image:{true_size},first_false_positive:{false_positive}"
    )
    print(f"time_fibre_witness={time_witness}")
    print(f"fixed_branch_coverage={tuple(sorted(branch_totals.items()))}")
    print(f"odd_recovery_rows={tuple(recovery_rows)}")
    print(f"binary_atlas_classes={tuple(binary_rows)}")
    print(f"n2_odd_collapse={tuple(n2_rows)}")
    print(f"n1_boundaries={tuple(n1_rows)}")
    print(f"c0_boundaries={tuple(c0_rows)}")
    print(f"ASSERTIONS {A.assertions}")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
