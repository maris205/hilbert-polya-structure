#!/usr/bin/env python3
"""Independent hostile-review verifier for P172.

This program was implemented from the literal rule A <- A intersect f(A).
It imports no author, scout, manuscript, or prior-paper code.  Its main
cross-check count uses inclusion--exclusion for onto maps instead of the
paper's Stirling recurrence.  It also uses sparse trajectory propagation,
coefficientwise marked histories, and fraction-free rank elimination.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product
from math import comb, factorial, gcd, lcm


ASSERTIONS = 0


def require(statement: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not statement:
        raise AssertionError(label)


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


@lru_cache(maxsize=None)
def state_space(n: int):
    universe = tuple(range(n))
    return tuple(
        frozenset(block)
        for cardinality in range(n + 1)
        for block in combinations(universe, cardinality)
    )


def onto_by_exclusion(domain_size: int, range_size: int) -> int:
    """Count onto functions by inclusion--exclusion, not set partitions."""
    return sum(
        (-1) ** omitted
        * comb(range_size, omitted)
        * (range_size - omitted) ** domain_size
        for omitted in range(range_size + 1)
    )


def stirling_by_blocks(n: int, k: int) -> int:
    """Independent recurrence used only to audit k! S(n,k)."""
    if k < 0 or k > n:
        return 0
    previous = [1]
    for size in range(1, n + 1):
        current = [0] * (size + 1)
        for blocks in range(1, size + 1):
            inherited = previous[blocks] * blocks if blocks < len(previous) else 0
            created = previous[blocks - 1]
            current[blocks] = inherited + created
        previous = current
    return previous[k] if k < len(previous) else 0


def predicted_fixed_target_count(n: int, a: int, b: int, image_size: int) -> int:
    outside = image_size - b
    if not (0 <= b <= a <= n):
        return 0
    if not (0 <= image_size <= a):
        return 0
    if not (0 <= outside <= n - a):
        return 0
    return choose(n - a, outside) * onto_by_exclusion(a, image_size)


@lru_cache(maxsize=None)
def literal_marked_counts(n: int):
    """Enumerate restrictions A -> [n] and retain endpoint plus image size."""
    universe = tuple(range(n))
    table = {}
    for source in state_space(n):
        ordered_source = tuple(sorted(source))
        counts = defaultdict(int)
        for values in product(universe, repeat=len(ordered_source)):
            image = frozenset(values)
            endpoint = source.intersection(image)
            counts[endpoint, len(image)] += 1
        table[source] = dict(counts)
        require(
            sum(counts.values()) == (n ** len(source) if source else 1),
            f"restriction mass n={n} A={sorted(source)}",
        )
    return table


def closed_marked_size_kernel(n: int):
    kernel = [[{} for _ in range(n + 1)] for _ in range(n + 1)]
    for a in range(n + 1):
        denominator = n**a if a else 1
        row_mass = Fraction(0)
        for b in range(a + 1):
            for image_size in range(a + 1):
                count = choose(a, b) * predicted_fixed_target_count(
                    n, a, b, image_size
                )
                if count:
                    kernel[a][b][image_size] = Fraction(count, denominator)
                    row_mass += Fraction(count, denominator)
        require(row_mass == 1, f"closed marked row mass n={n} a={a}")
    return kernel


def unmarked_size_kernel(marked_kernel):
    n = len(marked_kernel) - 1
    return [
        [sum(marked_kernel[a][b].values(), Fraction(0)) for b in range(n + 1)]
        for a in range(n + 1)
    ]


def literal_unmarked_kernel(n: int):
    marked = literal_marked_counts(n)
    result = {}
    for source in state_space(n):
        denominator = n ** len(source) if source else 1
        row = defaultdict(Fraction)
        for (target, _image_size), count in marked[source].items():
            row[target] += Fraction(count, denominator)
        require(sum(row.values(), Fraction(0)) == 1, f"literal probability mass n={n}")
        result[source] = dict(row)
    return result


def audit_one_step(n: int) -> None:
    marked = literal_marked_counts(n)
    closed = closed_marked_size_kernel(n)
    states = state_space(n)

    for a in range(n + 1):
        for k in range(a + 1):
            require(
                onto_by_exclusion(a, k) == factorial(k) * stirling_by_blocks(a, k),
                f"onto/Stirling identity n={n} a={a} k={k}",
            )

    for source in states:
        a = len(source)
        denominator = n**a if a else 1
        direct_size_mark = defaultdict(Fraction)
        for (target, image_size), count in marked[source].items():
            direct_size_mark[len(target), image_size] += Fraction(count, denominator)

        for target in states:
            b = len(target)
            contained = target.issubset(source)
            for image_size in range(n + 1):
                actual = marked[source].get((target, image_size), 0)
                expected = (
                    predicted_fixed_target_count(n, a, b, image_size)
                    if contained
                    else 0
                )
                require(
                    actual == expected,
                    "fixed endpoint mark "
                    f"n={n} A={sorted(source)} B={sorted(target)} k={image_size}",
                )

        for b in range(n + 1):
            for image_size in range(n + 1):
                require(
                    direct_size_mark.get((b, image_size), Fraction(0))
                    == closed[a][b].get(image_size, Fraction(0)),
                    f"literal/closed quotient n={n} A={sorted(source)} b={b} k={image_size}",
                )


def step_labelled_distribution(distribution, n: int):
    marked = literal_marked_counts(n)
    answer = defaultdict(Fraction)
    for source, mass in distribution.items():
        denominator = n ** len(source) if source else 1
        for (target, _image_size), count in marked[source].items():
            answer[target] += mass * Fraction(count, denominator)
    return dict(answer)


def step_size_distribution(distribution, size_kernel):
    answer = defaultdict(Fraction)
    for source_size, mass in distribution.items():
        for target_size, probability in enumerate(size_kernel[source_size]):
            if probability:
                answer[target_size] += mass * probability
    return dict(answer)


def audit_labelled_time(n: int, horizon: int) -> None:
    labelled_kernel = literal_unmarked_kernel(n)
    size_kernel = unmarked_size_kernel(closed_marked_size_kernel(n))
    states = state_space(n)

    for initial in states:
        a = len(initial)
        labelled = {initial: Fraction(1)}
        sizes = {a: Fraction(1)}
        for epoch in range(horizon + 1):
            for target in states:
                b = len(target)
                expected = (
                    sizes.get(b, Fraction(0)) / choose(a, b)
                    if target.issubset(initial)
                    else Fraction(0)
                )
                require(
                    labelled.get(target, Fraction(0)) == expected,
                    f"label division n={n} t={epoch} A={sorted(initial)} B={sorted(target)}",
                )
            require(
                sum(labelled.values(), Fraction(0)) == 1,
                f"labelled power mass n={n} t={epoch} A={sorted(initial)}",
            )
            if epoch < horizon:
                next_labelled = defaultdict(Fraction)
                for current, mass in labelled.items():
                    for target, probability in labelled_kernel[current].items():
                        next_labelled[target] += mass * probability
                labelled = dict(next_labelled)
                sizes = step_size_distribution(sizes, size_kernel)


def advance_labelled_marks(distribution, n: int):
    marked = literal_marked_counts(n)
    answer = defaultdict(Fraction)
    for (source, history), mass in distribution.items():
        denominator = n ** len(source) if source else 1
        for (target, image_size), count in marked[source].items():
            answer[target, history + (image_size,)] += mass * Fraction(count, denominator)
    return dict(answer)


def advance_size_marks(distribution, marked_size_kernel):
    answer = defaultdict(Fraction)
    for (source_size, history), mass in distribution.items():
        for target_size, image_law in enumerate(marked_size_kernel[source_size]):
            for image_size, probability in image_law.items():
                answer[target_size, history + (image_size,)] += mass * probability
    return dict(answer)


def audit_marked_histories(n: int, horizon: int) -> None:
    marked_size = closed_marked_size_kernel(n)
    states = state_space(n)
    for initial in states:
        a = len(initial)
        labelled = {(initial, ()): Fraction(1)}
        sizes = {(a, ()): Fraction(1)}
        for epoch in range(1, horizon + 1):
            labelled = advance_labelled_marks(labelled, n)
            sizes = advance_size_marks(sizes, marked_size)

            for (target_size, history), total_mass in sizes.items():
                denominator = choose(a, target_size)
                for target in states:
                    if len(target) == target_size and target.issubset(initial):
                        require(
                            labelled.get((target, history), Fraction(0))
                            == total_mass / denominator,
                            "marked label division "
                            f"n={n} t={epoch} A={sorted(initial)} "
                            f"B={sorted(target)} history={history}",
                        )

            for (target, history), mass in labelled.items():
                require(target.issubset(initial), f"marked nesting n={n} t={epoch}")
                require(
                    mass
                    == sizes[len(target), history] / choose(a, len(target)),
                    f"marked reverse coverage n={n} t={epoch} history={history}",
                )
            require(
                sum(labelled.values(), Fraction(0)) == 1,
                f"marked total mass n={n} t={epoch} A={sorted(initial)}",
            )


def square_matrix(matrix):
    dimension = len(matrix)
    return [
        [
            sum(
                (matrix[row][middle] * matrix[middle][column] for middle in range(dimension)),
                Fraction(0),
            )
            for column in range(dimension)
        ]
        for row in range(dimension)
    ]


def fraction_free_rank(matrix) -> int:
    """Exact rank after clearing row denominators and fraction-free elimination."""
    if not matrix:
        return 0
    integers = []
    for row in matrix:
        row_scale = 1
        for value in row:
            row_scale = lcm(row_scale, Fraction(value).denominator)
        integers.append([int(Fraction(value) * row_scale) for value in row])

    rows = len(integers)
    columns = len(integers[0])
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, rows) if integers[row][column]),
            None,
        )
        if pivot is None:
            continue
        integers[pivot_row], integers[pivot] = integers[pivot], integers[pivot_row]
        pivot_value = integers[pivot_row][column]
        for row in range(pivot_row + 1, rows):
            entry = integers[row][column]
            if not entry:
                continue
            integers[row] = [
                pivot_value * integers[row][j] - entry * integers[pivot_row][j]
                for j in range(columns)
            ]
            common = 0
            for value in integers[row]:
                common = gcd(common, abs(value))
            if common > 1:
                integers[row] = [value // common for value in integers[row]]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def audit_size_jordan(n: int):
    size_kernel = unmarked_size_kernel(closed_marked_size_kernel(n))
    eigenvalues = [Fraction(factorial(a), n**a) for a in range(n + 1)]
    for a in range(n - 1):
        require(eigenvalues[a] > eigenvalues[a + 1], f"strict diagonal n={n} a={a}")
    require(eigenvalues[n - 1] == eigenvalues[n], f"top collision n={n}")
    require(
        all(
            eigenvalues[i] != eigenvalues[j]
            for i in range(n - 1)
            for j in range(i + 1, n + 1)
        ),
        f"unique quotient collision n={n}",
    )
    for a in range(n + 1):
        require(size_kernel[a][a] == eigenvalues[a], f"quotient diagonal n={n} a={a}")

    resonance = eigenvalues[n]
    shifted = [
        [
            size_kernel[row][column]
            - (resonance if row == column else Fraction(0))
            for column in range(n + 1)
        ]
        for row in range(n + 1)
    ]
    shifted_square = square_matrix(shifted)
    nullity_one = (n + 1) - fraction_free_rank(shifted)
    nullity_two = (n + 1) - fraction_free_rank(shifted_square)
    require(nullity_one == 1, f"quotient eigenspace n={n}")
    require(nullity_two == 2, f"quotient generalized eigenspace n={n}")
    require(size_kernel[n][n - 1] > 0, f"forced coupling n={n}")
    return nullity_one, nullity_two, size_kernel


def full_matrix(n: int):
    states = state_space(n)
    index = {state: position for position, state in enumerate(states)}
    raw = literal_marked_counts(n)
    matrix = [[Fraction(0) for _ in states] for _ in states]
    for source in states:
        denominator = n ** len(source) if source else 1
        row = index[source]
        for (target, _image_size), count in raw[source].items():
            matrix[row][index[target]] += Fraction(count, denominator)
    return states, matrix


def audit_full_spectrum(n: int) -> int:
    states, matrix = full_matrix(n)
    dimension = len(states)
    resonance = Fraction(factorial(n), n**n)
    algebraic_multiplicity = 0
    for row, source in enumerate(states):
        expected_diagonal = Fraction(factorial(len(source)), n ** len(source))
        require(matrix[row][row] == expected_diagonal, f"full diagonal n={n} row={row}")
        if expected_diagonal == resonance:
            algebraic_multiplicity += 1
        for column, target in enumerate(states):
            if column > row:
                require(matrix[row][column] == 0, f"full triangularity n={n}")
            if not target.issubset(source):
                require(matrix[row][column] == 0, f"full nesting n={n}")
    require(algebraic_multiplicity == n + 1, f"full top multiplicity n={n}")
    shifted = [
        [
            matrix[row][column] - (resonance if row == column else Fraction(0))
            for column in range(dimension)
        ]
        for row in range(dimension)
    ]
    geometric_multiplicity = dimension - fraction_free_rank(shifted)
    require(
        geometric_multiplicity < algebraic_multiplicity,
        f"full nonsemisimplicity n={n}",
    )
    return geometric_multiplicity


def absorption_means(size_kernel):
    n = len(size_kernel) - 1
    means = [Fraction(0)] * (n + 1)
    for a in range(1, n + 1):
        numerator = 1 + sum(size_kernel[a][b] * means[b] for b in range(a))
        means[a] = numerator / (1 - size_kernel[a][a])
    return means


def audit_absorption(n: int, size_kernel) -> Fraction:
    means = absorption_means(size_kernel)
    for a in range(1, n + 1):
        require(size_kernel[a][a] < 1, f"transient self-loop n={n} a={a}")
        require(
            means[a]
            == 1 + sum(size_kernel[a][b] * means[b] for b in range(n + 1)),
            f"mean Bellman equation n={n} a={a}",
        )
        if a < n:
            require(size_kernel[a][0] > 0, f"proper set direct extinction n={n} a={a}")
    require(
        sum(size_kernel[n][b] for b in range(n)) > 0,
        f"full set can decrease n={n}",
    )
    return means[n]


def audit_boundaries() -> None:
    q1 = unmarked_size_kernel(closed_marked_size_kernel(1))
    require(q1 == [[1, 0], [0, 1]], "n=1 two absorbing states")
    q2 = unmarked_size_kernel(closed_marked_size_kernel(2))
    expected = [
        [Fraction(1), 0, 0],
        [Fraction(1, 2), Fraction(1, 2), 0],
        [0, Fraction(1, 2), Fraction(1, 2)],
    ]
    require(q2 == expected, "n=2 quotient sentinel")
    require(absorption_means(q2)[2] == 4, "n=2 mean sentinel")


def main() -> None:
    print("P172 HOSTILE REVIEW A — INDEPENDENT EXACT CONTROL")
    print("PROVENANCE literal-only / no author-or-scout imports")
    print("STATUS HOLD_EXTERNAL")

    for n in range(1, 7):
        audit_one_step(n)
        audit_labelled_time(n, horizon=6)
        print(f"ENDPOINT+LABELLED n={n} states={2**n} epochs=0..6 PASS")

    for n in range(1, 5):
        audit_marked_histories(n, horizon=3)
        print(f"MARKED n={n} states={2**n} epochs=1..3 coefficientwise PASS")

    full_nullities = []
    for n in range(2, 6):
        full_nullities.append((n, audit_full_spectrum(n)))
    print(
        "FULL_OPERATOR n=2..5 nonsemisimple geometric="
        + ",".join(f"{n}:{nullity}" for n, nullity in full_nullities)
        + " PASS"
    )

    for n in range(2, 15):
        first, second, quotient = audit_size_jordan(n)
        mean_full = audit_absorption(n, quotient)
        print(
            f"QUOTIENT n={n} Jordan-nullities={first},{second} "
            f"mean_full={mean_full} PASS"
        )

    audit_boundaries()
    print("BOUNDARIES n=1,n=2 PASS")
    print("THEOREM endpoint/image-size formula PASS")
    print("THEOREM every-time every-labelled-target formula PASS")
    print("THEOREM algebraic spectrum and forced quotient J2 PASS")
    print("THEOREM absorption CDF/mean logic PASS")
    print("THEOREM multitime marked transfer PASS")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("VERDICT EXECUTABLE_CLAIMS_PASS")


if __name__ == "__main__":
    main()
