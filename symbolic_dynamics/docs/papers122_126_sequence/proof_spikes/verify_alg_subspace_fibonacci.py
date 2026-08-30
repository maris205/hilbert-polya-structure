#!/usr/bin/env python3
"""Independent exact verifier for the subspace-Fibonacci proof spike.

This program intentionally does not import the algebraic scouting pilot.  It
represents subspaces by reduced-row-echelon bases over prime fields, whereas
the scouting program used binary membership bitsets.  It exhausts several
small state spaces and separately checks the proposed uniform sharp witness.
"""

from functools import lru_cache
from itertools import combinations, product


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def rref(vectors, p, d):
    matrix = [[x % p for x in row] for row in vectors]
    matrix = [row for row in matrix if any(row)]
    pivot_row = 0
    for column in range(d):
        source = next(
            (i for i in range(pivot_row, len(matrix)) if matrix[i][column]),
            None,
        )
        if source is None:
            continue
        matrix[pivot_row], matrix[source] = matrix[source], matrix[pivot_row]
        inverse = pow(matrix[pivot_row][column], -1, p)
        matrix[pivot_row] = [(inverse * x) % p for x in matrix[pivot_row]]
        for i in range(len(matrix)):
            if i == pivot_row or matrix[i][column] == 0:
                continue
            coefficient = matrix[i][column]
            matrix[i] = [
                (x - coefficient * y) % p
                for x, y in zip(matrix[i], matrix[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return tuple(tuple(row) for row in matrix if any(row))


def all_subspaces(p, d):
    answer = []
    columns = tuple(range(d))
    for rank in range(d + 1):
        for pivots in combinations(columns, rank):
            nonpivots = tuple(j for j in columns if j not in pivots)
            free = tuple(
                (i, j)
                for i, pivot in enumerate(pivots)
                for j in nonpivots
                if j > pivot
            )
            for values in product(range(p), repeat=len(free)):
                rows = [[0] * d for _ in range(rank)]
                for i, pivot in enumerate(pivots):
                    rows[i][pivot] = 1
                for value, (i, j) in zip(values, free):
                    rows[i][j] = value
                basis = tuple(tuple(row) for row in rows)
                check(rref(basis, p, d) == basis, f"enumerator emitted non-RREF p={p},d={d}")
                answer.append(basis)
    check(len(answer) == len(set(answer)), f"duplicate subspace p={p},d={d}")
    return tuple(answer)


def gaussian_binomial(n, k, q):
    if k < 0 or k > n:
        return 0
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= q ** (n - i) - 1
        denominator *= q ** (k - i) - 1
    return numerator // denominator


def lane(p, d):
    spaces = all_subspaces(p, d)
    expected_spaces = sum(gaussian_binomial(d, r, p) for r in range(d + 1))
    check(len(spaces) == expected_spaces, f"Gaussian count p={p},d={d}")

    @lru_cache(maxsize=None)
    def join(left, right):
        return rref(left + right, p, d)

    @lru_cache(maxsize=None)
    def n_image(space):
        shifted = tuple((0,) + row[:-1] for row in space)
        return rref(shifted, p, d)

    @lru_cache(maxsize=None)
    def n_power(space, exponent):
        result = space
        for _ in range(exponent):
            result = n_image(result)
        return result

    def subset(left, right):
        return join(left, right) == right

    def step(state):
        u, v = state
        return v, join(u, n_image(v))

    def is_recurrent(state):
        u, v = state
        return subset(n_image(u), v) and subset(n_image(v), u)

    def closed_term(u, v, t):
        if t == 0:
            return u
        if t == 1:
            return v
        answer = ()
        if t % 2 == 0:
            r = t // 2
            for j in range(r):
                answer = join(answer, n_power(u, 2 * j))
                answer = join(answer, n_power(v, 2 * j + 1))
        else:
            r = (t - 1) // 2
            for j in range(r):
                answer = join(answer, n_power(u, 2 * j + 1))
            for j in range(r + 1):
                answer = join(answer, n_power(v, 2 * j))
        return answer

    fixed = 0
    recurrent = 0
    maximum_depth = 0
    for u in spaces:
        for v in spaces:
            state = (u, v)
            literal_terms = [u, v]
            for _ in range(2 * d + 2):
                literal_terms.append(join(literal_terms[-2], n_image(literal_terms[-1])))
            for t, literal in enumerate(literal_terms):
                check(literal == closed_term(u, v, t), f"closed term p={p},d={d},t={t}")

            recurrence_conditions = subset(n_image(u), v) and subset(n_image(v), u)
            check(is_recurrent(state) == recurrence_conditions, f"condition p={p},d={d}")
            check(is_recurrent(state) == (step(step(state)) == state), f"T2 criterion p={p},d={d}")

            current = state
            depth = None
            for t in range(d + 1):
                if is_recurrent(current):
                    depth = t
                    break
                current = step(current)
            check(depth is not None, f"depth bound p={p},d={d}")
            maximum_depth = max(maximum_depth, depth)
            recurrent += depth == 0
            fixed += step(state) == state

    expected_depth = 0 if d == 1 else d
    check(maximum_depth == expected_depth, f"sharp maximum p={p},d={d}")
    check(fixed == d + 1, f"fixed count p={p},d={d}")
    return len(spaces), len(spaces) ** 2, fixed, recurrent, maximum_depth


def witness_check(p, d):
    # Jordan chain e_0 -> e_1 -> ... -> e_{d-1} -> 0.
    e0 = ((1,) + (0,) * (d - 1),)
    zero = ()

    @lru_cache(maxsize=None)
    def join(left, right):
        return rref(left + right, p, d)

    @lru_cache(maxsize=None)
    def n_image(space):
        return rref(tuple((0,) + row[:-1] for row in space), p, d)

    def recurrent(state):
        u, v = state
        return join(n_image(u), v) == v and join(n_image(v), u) == u

    def step(state):
        u, v = state
        return v, join(u, n_image(v))

    state = (e0, zero)
    first = None
    for t in range(d + 1):
        if recurrent(state):
            first = t
            break
        state = step(state)
    expected = 0 if d == 1 else d
    check(first == expected, f"uniform witness p={p},d={d}: {first} != {expected}")
    return first


def main():
    summaries = []
    lanes = ((2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
             (3, 1), (3, 2), (3, 3), (3, 4),
             (5, 1), (5, 2), (5, 3))
    for p, d in lanes:
        spaces, pairs, fixed, recurrent, maximum_depth = lane(p, d)
        summaries.append(
            f"p={p} d={d} subspaces={spaces} pairs={pairs} fixed={fixed} "
            f"recurrent={recurrent} max_depth={maximum_depth}"
        )

    witness_lanes = 0
    for p in (2, 3, 5, 7):
        for d in range(1, 13):
            witness_check(p, d)
            witness_lanes += 1

    print("ALG_SUBSPACE_FIBONACCI VERIFIER: PASS")
    print(f"assertions={ASSERTIONS}")
    print("representation=independent_RREF_over_prime_fields")
    print(f"exhaustive_lanes={len(lanes)} witness_lanes={witness_lanes}")
    for summary in summaries:
        print(summary)


if __name__ == "__main__":
    main()
