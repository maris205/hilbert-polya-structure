#!/usr/bin/env python3
"""Hostile Review A exact control for P173.

This implementation is deliberately independent of the paper's verifier and
of the scouting programs.  Literal subspaces are represented by canonical
RREF row bases over prime fields, and endomorphisms are tuples of field
entries.  The update is computed from annihilator coordinates of V/U; no
materialized point sets, bit masks, or imported project code are used.

Finite checks are falsification controls, not evidence of novelty or a
replacement for the all-parameter proofs.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product


ASSERTIONS = 0


def require(statement: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not statement:
        raise AssertionError(label)


def rref(rows, width: int, prime: int):
    """Canonical reduced row basis over a prime field."""
    work = [[entry % prime for entry in row] for row in rows]
    work = [row for row in work if any(row)]
    lead_row = 0
    for column in range(width):
        pivot = next(
            (index for index in range(lead_row, len(work)) if work[index][column]),
            None,
        )
        if pivot is None:
            continue
        work[lead_row], work[pivot] = work[pivot], work[lead_row]
        inverse = pow(work[lead_row][column], -1, prime)
        work[lead_row] = [(inverse * entry) % prime for entry in work[lead_row]]
        for index in range(len(work)):
            if index == lead_row or not work[index][column]:
                continue
            scale = work[index][column]
            work[index] = [
                (left - scale * right) % prime
                for left, right in zip(work[index], work[lead_row])
            ]
        lead_row += 1
        if lead_row == len(work):
            break
    return tuple(tuple(row) for row in work[:lead_row])


def nullspace(rows, width: int, prime: int):
    reduced = rref(rows, width, prime)
    pivots = []
    for row in reduced:
        pivots.append(next(index for index, entry in enumerate(row) if entry))
    free = [column for column in range(width) if column not in pivots]
    basis = []
    for free_column in free:
        vector = [0] * width
        vector[free_column] = 1
        for row, pivot in zip(reduced, pivots):
            vector[pivot] = (-row[free_column]) % prime
        basis.append(tuple(vector))
    return tuple(basis)


def all_rref_spaces(dimension: int, prime: int):
    """Enumerate each subspace once by its unique RREF row basis."""
    spaces = []
    columns = tuple(range(dimension))
    for rank in range(dimension + 1):
        for pivots in combinations(columns, rank):
            slots = [
                (row, column)
                for row, pivot in enumerate(pivots)
                for column in columns
                if column not in pivots and column > pivot
            ]
            for values in product(range(prime), repeat=len(slots)):
                rows = [[0] * dimension for _ in range(rank)]
                for row, pivot in enumerate(pivots):
                    rows[row][pivot] = 1
                for (row, column), value in zip(slots, values):
                    rows[row][column] = value
                basis = tuple(tuple(row) for row in rows)
                require(rref(basis, dimension, prime) == basis,
                        f"RREF generator q={prime} n={dimension} rank={rank}")
                spaces.append(basis)
    spaces.sort(key=lambda basis: (len(basis), basis))
    return tuple(spaces)


def is_contained(small, large, width: int, prime: int) -> bool:
    return len(rref(tuple(large) + tuple(small), width, prime)) == len(large)


def row_times_matrix(vector, matrix, prime: int):
    width = len(vector)
    return tuple(
        sum(vector[row] * matrix[row][column] for row in range(width)) % prime
        for column in range(width)
    )


def linear_combination(coefficients, basis, prime: int):
    width = len(basis[0]) if basis else 0
    return tuple(
        sum(coefficients[row] * basis[row][column] for row in range(len(basis)))
        % prime
        for column in range(width)
    )


def quotient_leak_and_kernel(source, matrix, ambient: int, prime: int):
    """Return annihilator-coordinate leak matrix and its ambient kernel."""
    annihilator = nullspace(source, ambient, prime)
    images = [row_times_matrix(vector, matrix, prime) for vector in source]
    leak_rows = tuple(
        tuple(sum(image[i] * normal[i] for i in range(ambient)) % prime
              for image in images)
        for normal in annihilator
    )
    coefficient_kernel = nullspace(leak_rows, len(source), prime)
    ambient_rows = tuple(
        linear_combination(coefficients, source, prime)
        for coefficients in coefficient_kernel
    )
    return leak_rows, rref(ambient_rows, ambient, prime)


def all_matrices(n: int, prime: int):
    for entries in product(range(prime), repeat=n * n):
        yield tuple(tuple(entries[row * n:(row + 1) * n]) for row in range(n))


@lru_cache(maxsize=None)
def gaussian(n: int, k: int, q: int) -> int:
    """Gaussian number, built by the incidence recurrence."""
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return gaussian(n - 1, k, q) + q ** (n - k) * gaussian(n - 1, k - 1, q)


def injective_maps(domain: int, codomain: int, q: int) -> int:
    if domain > codomain:
        return 0
    count = 1
    for index in range(domain):
        count *= q ** codomain - q ** index
    return count


def endpoint_quotient_maps(n: int, a: int, b: int, q: int) -> int:
    return injective_maps(a - b, n - a, q)


def identity(size: int):
    return [[Fraction(row == column) for column in range(size)] for row in range(size)]


def multiply(left, right):
    return [
        [sum(left[row][middle] * right[middle][column]
             for middle in range(len(right)))
         for column in range(len(right[0]))]
        for row in range(len(left))
    ]


def power(matrix, exponent: int):
    answer = identity(len(matrix))
    factor = matrix
    while exponent:
        if exponent & 1:
            answer = multiply(answer, factor)
        factor = multiply(factor, factor)
        exponent //= 2
    return answer


def rank_over_q(matrix) -> int:
    work = [[Fraction(entry) for entry in row] for row in matrix]
    height = len(work)
    width = len(work[0]) if height else 0
    pivot_row = 0
    for column in range(width):
        pivot = next(
            (row for row in range(pivot_row, height) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        divisor = work[pivot_row][column]
        work[pivot_row] = [entry / divisor for entry in work[pivot_row]]
        for row in range(pivot_row + 1, height):
            if not work[row][column]:
                continue
            scale = work[row][column]
            work[row] = [
                entry - scale * pivot_entry
                for entry, pivot_entry in zip(work[row], work[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == height:
            break
    return pivot_row


def nullity_over_q(matrix) -> int:
    return (len(matrix[0]) if matrix else 0) - rank_over_q(matrix)


def shift(matrix, value: Fraction):
    return [
        [entry - (value if row == column else 0)
         for column, entry in enumerate(entries)]
        for row, entries in enumerate(matrix)
    ]


def matrix_vector(matrix, vector):
    return [sum(entry * value for entry, value in zip(row, vector)) for row in matrix]


def dimension_chain(n: int, q: int):
    chain = [[Fraction(0) for _ in range(n + 1)] for _ in range(n + 1)]
    for a in range(n + 1):
        denominator = q ** (a * (n - a))
        for b in range(a + 1):
            chain[a][b] = Fraction(
                gaussian(a, b, q) * endpoint_quotient_maps(n, a, b, q),
                denominator,
            )
        require(sum(chain[a]) == 1, f"Q stochastic q={q} n={n} a={a}")
    return chain


def literal_control(n: int, prime: int, epochs: int):
    spaces = all_rref_spaces(n, prime)
    expected_census = sum(gaussian(n, rank, prime) for rank in range(n + 1))
    require(len(spaces) == expected_census, f"subspace census q={prime} n={n}")
    location = {space: index for index, space in enumerate(spaces)}
    total_maps = prime ** (n * n)
    transitions = [[Fraction(0) for _ in spaces] for _ in spaces]

    for source_index, source in enumerate(spaces):
        a = len(source)
        target_counts = Counter()
        leak_counts = Counter()
        for matrix in all_matrices(n, prime):
            leak, target = quotient_leak_and_kernel(source, matrix, n, prime)
            signature = tuple(entry for row in leak for entry in row)
            leak_counts[signature] += 1
            require(target in location,
                    f"kernel is catalogued q={prime} n={n} U={source_index}")
            require(is_contained(target, source, n, prime),
                    f"nested update q={prime} n={n} U={source_index}")
            target_counts[target] += 1

        quotient_dimension = a * (n - a)
        expected_lifts = prime ** (n * n - quotient_dimension)
        require(len(leak_counts) == prime ** quotient_dimension,
                f"quotient-map surjection q={prime} n={n} U={source_index}")
        for count in leak_counts.values():
            require(count == expected_lifts,
                    f"uniform ambient lifts q={prime} n={n} U={source_index}")

        for target_index, target in enumerate(spaces):
            b = len(target)
            contained = is_contained(target, source, n, prime)
            expected = (
                expected_lifts * endpoint_quotient_maps(n, a, b, prime)
                if contained else 0
            )
            require(target_counts[target] == expected,
                    f"every-target fibre q={prime} n={n} U={source_index} B={target_index}")
            transitions[source_index][target_index] = Fraction(
                target_counts[target], total_maps
            )
        require(sum(transitions[source_index]) == 1,
                f"literal stochastic row q={prime} n={n} U={source_index}")
        require(transitions[source_index][source_index]
                == Fraction(1, prime ** quotient_dimension),
                f"literal self-loop q={prime} n={n} U={source_index}")

    diagonal_histogram = Counter(
        transitions[index][index] for index in range(len(spaces))
    )
    predicted_histogram = Counter()
    for a in range(n + 1):
        predicted_histogram[Fraction(1, prime ** (a * (n - a)))] += gaussian(n, a, prime)
    require(diagonal_histogram == predicted_histogram,
            f"full algebraic diagonal multiset q={prime} n={n}")

    quotient = dimension_chain(n, prime)
    for exponent in range(epochs + 1):
        literal_power = power(transitions, exponent)
        quotient_power = power(quotient, exponent)
        for source_index, source in enumerate(spaces):
            a = len(source)
            for target_index, target in enumerate(spaces):
                b = len(target)
                expected = (
                    quotient_power[a][b] / gaussian(a, b, prime)
                    if is_contained(target, source, n, prime) else 0
                )
                require(literal_power[source_index][target_index] == expected,
                        f"labelled division q={prime} n={n} t={exponent} "
                        f"U={source_index} B={target_index}")
    return len(spaces), total_maps


def jordan_control(n: int, q: int):
    chain = dimension_chain(n, q)
    diagonal = [Fraction(1, q ** (a * (n - a))) for a in range(n + 1)]
    pair_kinds = Counter()

    # The endpoint eigenvalue has a genuine degenerate exception at n=0.
    endpoint_shift = shift(chain, Fraction(1))
    if n == 0:
        require(nullity_over_q(endpoint_shift) == 1, f"n=0 one endpoint block q={q}")
    else:
        require(nullity_over_q(endpoint_shift) == 2,
                f"endpoint geometric multiplicity q={q} n={n}")
        require(nullity_over_q(multiply(endpoint_shift, endpoint_shift)) == 2,
                f"endpoint semisimple q={q} n={n}")
        constant = [Fraction(1) for _ in range(n + 1)]
        top_indicator = [Fraction(0) for _ in range(n)] + [Fraction(1)]
        require(matrix_vector(chain, constant) == constant,
                f"constant endpoint eigenvector q={q} n={n}")
        require(matrix_vector(chain, top_indicator) == top_indicator,
                f"V-indicator endpoint eigenvector q={q} n={n}")

    for b in range(1, (n + 1) // 2):
        a = n - b
        eigenvalue = diagonal[b]
        require(diagonal[a] == eigenvalue,
                f"complementary equality q={q} n={n} b={b}")
        operator = shift(chain, eigenvalue)
        square = multiply(operator, operator)
        cube = multiply(square, operator)
        require(nullity_over_q(operator) == 1,
                f"paired eigenspace q={q} n={n} b={b}")
        require(nullity_over_q(square) == 2,
                f"paired generalized eigenspace q={q} n={n} b={b}")
        require(nullity_over_q(cube) == 2,
                f"no longer chain q={q} n={n} b={b}")

        # Reconstruct the failed eigenvector born at b.  This catches the
        # indirect-coupling cases for which Q[a,b] itself vanishes.
        vector = [Fraction(0) for _ in range(n + 1)]
        vector[b] = 1
        for k in range(b + 1, a):
            require(diagonal[k] < eigenvalue,
                    f"strict interior separation q={q} n={n} b={b} k={k}")
            numerator = sum(chain[k][j] * vector[j] for j in range(k))
            vector[k] = numerator / (eigenvalue - diagonal[k])
            require(vector[k] > 0,
                    f"positive recursive coordinate q={q} n={n} b={b} k={k}")
        obstruction = sum(chain[a][j] * vector[j] for j in range(a))
        require(obstruction > 0,
                f"terminal compatibility obstruction q={q} n={n} b={b}")
        if chain[a][b]:
            pair_kinds["direct"] += 1
        else:
            pair_kinds["indirect"] += 1
            require(a - b > n - a,
                    f"indirect one-step rank obstruction q={q} n={n} b={b}")

    if n and n % 2 == 0:
        middle = n // 2
        require(nullity_over_q(shift(chain, diagonal[middle])) == 1,
                f"simple midpoint q={q} n={n}")

    expected_blocks = 2 if n else 1
    expected_blocks += 2 * len(range(1, (n + 1) // 2))
    if n and n % 2 == 0:
        expected_blocks += 1
    require(expected_blocks == n + 1, f"Jordan blocks exhaust dimension q={q} n={n}")
    return pair_kinds


def absorption_control(n: int, q: int, horizon: int):
    chain = dimension_chain(n, q)
    require(chain[0] == [Fraction(1)] + [Fraction(0)] * n,
            f"zero fixed q={q} n={n}")
    require(chain[n] == [Fraction(0)] * n + [Fraction(1)],
            f"V fixed q={q} n={n}")

    means = [Fraction(0) for _ in range(n + 1)]
    for a in range(1, n):
        require(chain[a][a] == Fraction(1, q ** (a * (n - a))),
                f"proper self-loop q={q} n={n} a={a}")
        require(chain[a][a] < 1 and chain[a][a - 1] > 0,
                f"strict-loss route q={q} n={n} a={a}")
        means[a] = (
            1 + sum(chain[a][b] * means[b] for b in range(a))
        ) / (1 - chain[a][a])
        require(means[a] > 0, f"finite positive mean q={q} n={n} a={a}")
        require(means[a] == 1 + sum(chain[a][b] * means[b] for b in range(a + 1)),
                f"mean first-step equation q={q} n={n} a={a}")

        previous = Fraction(0)
        for exponent in range(horizon + 1):
            cdf = power(chain, exponent)[a][0]
            require(previous <= cdf <= 1,
                    f"absorption CDF monotone q={q} n={n} a={a} t={exponent}")
            previous = cdf
    if n == 2:
        require(chain[1][0] == Fraction(q - 1, q), f"n=2 drop q={q}")
        require(chain[1][1] == Fraction(1, q), f"n=2 stay q={q}")
        require(means[1] == Fraction(q, q - 1), f"n=2 mean q={q}")


def main() -> None:
    print("P173 HOSTILE REVIEW A — INDEPENDENT RREF/ANNIHILATOR CONTROL")
    print("STATUS SPIKE_2_COLLISION_RISK / HOLD_EXTERNAL")
    print("NO AUTHOR OR SCOUT IMPORTS")

    literal_boxes = ((2, 0, 6), (2, 1, 6), (2, 2, 6), (2, 3, 6),
                     (3, 0, 5), (3, 1, 5), (3, 2, 5))
    for prime, n, epochs in literal_boxes:
        census, matrices = literal_control(n, prime, epochs)
        print(f"LITERAL q={prime} n={n} RREF_spaces={census} matrices={matrices} "
              f"epochs=0..{epochs} PASS")

    totals = Counter()
    fields = (2, 3, 4, 5, 7, 8, 9, 11)
    for q in fields:
        for n in range(0, 15):
            totals.update(jordan_control(n, q))
            absorption_control(n, q, 7)
        print(f"QUOTIENT q={q} n=0..14 spectrum/Jordan/absorption PASS")

    # Exhibit both routes rather than hiding the zero direct transition.
    q, n, b = 2, 7, 1
    chain = dimension_chain(n, q)
    require(chain[n - b][b] == 0, "exhibited indirect complementary coupling")
    print(f"JORDAN coupling_pairs direct={totals['direct']} indirect={totals['indirect']} PASS")
    print("JORDAN indirect witness q=2 n=7 pair=(1,6): Q[6,1]=0 but nullities=(1,2,2) PASS")

    require(nullity_over_q(shift(dimension_chain(0, 2), Fraction(1))) == 1,
            "explicit n=0 endpoint inventory")
    print("BOUNDARY n=0: one state and one J1(1), not two — MANUSCRIPT REPAIR REQUIRED")
    print("BOUNDARY n=1: two distinct fixed states and two J1(1) blocks PASS")
    print("BOUNDARY n=2: exact transient row and mean PASS")
    print("THEOREM quotient uniformity / ambient lift exponent PASS")
    print("THEOREM every-target fibres / dimension quotient / labelled powers PASS")
    print("THEOREM full algebraic spectrum / corrected quotient Jordan inventory PASS")
    print("THEOREM absorption CDF / mean recurrence PASS")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("RESULT CONTROL_PASS_WITH_MANUSCRIPT_BOUNDARY_REPAIR")


if __name__ == "__main__":
    main()
