#!/usr/bin/env python3
"""Independent exact hostile verifier for alternating tropical normalization.

No author module is imported.  The literal update, inverse counters, weighted
fibres, inclusion--exclusion counts, and depth census are rebuilt here using
only the Python standard library.
"""

from collections import Counter
from itertools import product
from math import comb


ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def states(n, q):
    return product(range(q), repeat=n * n)


def rows(matrix, n):
    return tuple(tuple(matrix[n * i + j] for j in range(n)) for i in range(n))


def flatten(row_matrix):
    return tuple(x for row in row_matrix for x in row)


def transposed(matrix, n):
    a = rows(matrix, n)
    return tuple(a[i][j] for j in range(n) for i in range(n))


def normalize_rows(matrix, n):
    out = []
    for row in rows(matrix, n):
        minimum = min(row)
        out.append(tuple(x - minimum for x in row))
    return flatten(out)


def update(matrix, n):
    return transposed(normalize_rows(matrix, n), n)


def closed_second_update(matrix, n):
    b = rows(normalize_rows(matrix, n), n)
    column_minima = tuple(min(b[i][j] for i in range(n)) for j in range(n))
    return tuple(b[i][j] - column_minima[j]
                 for i in range(n) for j in range(n))


def row_zero(matrix, n):
    return all(min(row) == 0 for row in rows(matrix, n))


def column_zero(matrix, n):
    a = rows(matrix, n)
    return all(min(a[i][j] for i in range(n)) == 0 for j in range(n))


def in_core(matrix, n):
    return row_zero(matrix, n) and column_zero(matrix, n)


def convolution(left, right):
    answer = Counter()
    for e1, c1 in left.items():
        for e2, c2 in right.items():
            answer[e1 + e2] += c1 * c2
    return answer


def predicted_one_fibre(target, n, q):
    if not column_zero(target, n):
        return Counter()
    a = rows(target, n)
    polynomial = Counter({sum(target): 1})
    for column in range(n):
        height = max(a[i][column] for i in range(n))
        polynomial = convolution(
            polynomial,
            Counter({n * offset: 1 for offset in range(q - height)}),
        )
    return polynomial


def admissible_potentials(target, n, q):
    if not in_core(target, n):
        return
    a = rows(target, n)
    caps = tuple(q - 1 - max(a[i][j] for i in range(n)) for j in range(n))
    for potential in product(*(range(cap + 1) for cap in caps)):
        if all(any(a[i][j] == 0 and potential[j] == 0 for j in range(n))
               for i in range(n)):
            yield potential


def predicted_two_fibre(target, n, q):
    if not in_core(target, n):
        return Counter()
    a = rows(target, n)
    answer = Counter()
    for potential in admissible_potentials(target, n, q):
        polynomial = Counter({sum(target) + n * sum(potential): 1})
        for i in range(n):
            maximum = max(a[i][j] + potential[j] for j in range(n))
            polynomial = convolution(
                polynomial,
                Counter({n * offset: 1 for offset in range(q - maximum)}),
            )
        answer.update(polynomial)
    return answer


def core_ie(n, q):
    answer = 0
    for missing_rows in range(n + 1):
        for missing_columns in range(n + 1):
            forced_nonzero = (
                n * (missing_rows + missing_columns)
                - missing_rows * missing_columns
            )
            free = (n - missing_rows) * (n - missing_columns)
            answer += (
                (-1) ** (missing_rows + missing_columns)
                * comb(n, missing_rows)
                * comb(n, missing_columns)
                * (q - 1) ** forced_nonzero
                * q ** free
            )
    return answer


def fixed_ie(n, q):
    upper = n * (n + 1) // 2
    answer = 0
    for missing_rows in range(n + 1):
        complement = n - missing_rows
        free = complement * (complement + 1) // 2
        answer += (
            (-1) ** missing_rows
            * comb(n, missing_rows)
            * (q - 1) ** (upper - free)
            * q ** free
        )
    return answer


def one_image_count(n, q):
    return (q ** n - (q - 1) ** n) ** n


def one_row_avoiding_minima(n, q, forbidden_columns):
    """Rows in which no forbidden position attains the row minimum."""
    k = forbidden_columns
    return sum(
        ((r + 1) ** (n - k) - r ** (n - k)) * r ** k
        for r in range(q)
    )


def depth_le_one_closed(n, q):
    """IE over columns missed by the union of all row-minimum positions."""
    return sum(
        (-1) ** k
        * comb(n, k)
        * one_row_avoiding_minima(n, q, k) ** n
        for k in range(n + 1)
    )


def check_source_coordinate_bijection(source, n, q):
    a = rows(source, n)
    row_offsets = tuple(min(row) for row in a)
    b = rows(normalize_rows(source, n), n)
    column_offsets = tuple(min(b[i][j] for i in range(n)) for j in range(n))
    target = closed_second_update(source, n)
    c = rows(target, n)

    check(in_core(target, n), (n, q, source, "coordinate target core"))
    check(all(0 <= column_offsets[j] <=
              q - 1 - max(c[i][j] for i in range(n))
              for j in range(n)), (n, q, source, "column caps"))
    check(all(any(c[i][j] == 0 and column_offsets[j] == 0
                      for j in range(n))
              for i in range(n)), (n, q, source, "zero cover"))
    check(all(0 <= row_offsets[i] <=
              q - 1 - max(c[i][j] + column_offsets[j] for j in range(n))
              for i in range(n)), (n, q, source, "row caps"))
    rebuilt = tuple(c[i][j] + column_offsets[j] + row_offsets[i]
                    for i in range(n) for j in range(n))
    check(rebuilt == source, (n, q, source, "coordinate reconstruction"))


def exhaustive_box(n, q):
    state_list = tuple(states(n, q))
    first_count = Counter()
    second_count = Counter()
    first_weight = {}
    second_weight = {}
    first_weight = {x: Counter() for x in state_list}
    second_weight = {x: Counter() for x in state_list}
    image_one = set()
    image_two = set()
    depth = Counter()

    for source in state_list:
        first = update(source, n)
        second = update(first, n)
        third = update(second, n)
        fourth = update(third, n)
        closed = closed_second_update(source, n)

        image_one.add(first)
        image_two.add(second)
        first_count[first] += 1
        second_count[second] += 1
        first_weight[first][sum(source)] += 1
        second_weight[second][sum(source)] += 1

        check(first == transposed(normalize_rows(source, n), n),
              (n, q, source, "literal update"))
        check(second == closed, (n, q, source, "closed second iterate"))
        check(column_zero(first, n), (n, q, source, "first image support"))
        check(in_core(second, n), (n, q, source, "second image support"))
        check(third == transposed(second, n), (n, q, source, "core transpose"))
        check(fourth == second, (n, q, source, "T4=T2"))
        check_source_coordinate_bijection(source, n, q)

        if in_core(source, n):
            d = 0
        elif in_core(first, n):
            d = 1
        else:
            d = 2
        depth[d] += 1
        check(in_core((source, first, second)[d], n),
              (n, q, source, "depth landing"))
        if d:
            check(not in_core((source, first)[d - 1], n),
                  (n, q, source, "depth minimal"))

    recurrent = sum(in_core(x, n) for x in state_list)
    fixed = sum(in_core(x, n) and x == transposed(x, n) for x in state_list)
    strict_two_points = sum(
        in_core(x, n) and x != transposed(x, n) for x in state_list
    )

    check(image_one == {x for x in state_list if column_zero(x, n)},
          (n, q, "first image characterization"))
    check(image_two == {x for x in state_list if in_core(x, n)},
          (n, q, "second image characterization"))
    check(len(image_one) == one_image_count(n, q), (n, q, "image formula"))
    check(recurrent == core_ie(n, q), (n, q, "core IE"))
    check(fixed == fixed_ie(n, q), (n, q, "fixed IE"))
    check(strict_two_points == recurrent - fixed, (n, q, "two-period points"))
    check(strict_two_points % 2 == 0, (n, q, "two-cycle integrality"))

    for target in state_list:
        one = predicted_one_fibre(target, n, q)
        two = predicted_two_fibre(target, n, q)
        check(one.total() == first_count[target], (n, q, target, "one fibre"))
        check(two.total() == second_count[target], (n, q, target, "two fibre"))
        check(one == first_weight[target], (n, q, target, "one weighted"))
        check(two == second_weight[target], (n, q, target, "two weighted"))
        check(bool(one) == column_zero(target, n),
              (n, q, target, "one support iff"))
        check(bool(two) == in_core(target, n),
              (n, q, target, "two support iff"))

    depth_le_one = depth_le_one_closed(n, q)
    check(depth[0] == recurrent, (n, q, "depth zero"))
    check(depth[0] + depth[1] == depth_le_one,
          (n, q, "closed depth <=1"))
    check(depth[2] == q ** (n * n) - depth_le_one,
          (n, q, "closed depth two"))
    check(sum(first_count.values()) == q ** (n * n), (n, q, "first mass"))
    check(sum(second_count.values()) == q ** (n * n), (n, q, "second mass"))

    for iterate in range(1, 7):
        actual = 0
        for source in state_list:
            y = source
            for _ in range(iterate):
                y = update(y, n)
            actual += y == source
        expected = fixed if iterate % 2 else recurrent
        check(actual == expected, (n, q, iterate, "fixed iterate census"))

    return (
        len(state_list), len(image_one), recurrent, fixed,
        depth[0], depth[1], depth[2],
    )


def structural_and_boundary_checks():
    structural = 0
    for n in range(1, 11):
        for q in range(1, 11):
            recurrent = core_ie(n, q)
            fixed = fixed_ie(n, q)
            image = one_image_count(n, q)
            depth_one = depth_le_one_closed(n, q)
            total = q ** (n * n)
            check(1 <= fixed <= recurrent <= depth_one <= total,
                  (n, q, "structural recurrent/depth order"))
            check(recurrent <= image <= total,
                  (n, q, "structural image order"))
            check((recurrent - fixed) % 2 == 0,
                  (n, q, "structural cycle parity"))
            structural += 1

    # n=1: zero is fixed and all positive scalars have exact depth one.
    n_one = 0
    for q in range(1, 9):
        literal_depths = Counter()
        for x in states(1, q):
            y = update(x, 1)
            check(y == (0,), (q, x, "n=1 update"))
            literal_depths[0 if x == (0,) else 1] += 1
        check(literal_depths[0] == 1, (q, "n=1 depth zero"))
        check(literal_depths[1] == q - 1, (q, "n=1 depth one"))
        check(core_ie(1, q) == fixed_ie(1, q) == 1,
              (q, "n=1 IE boundary"))
        check(depth_le_one_closed(1, q) == q,
              (q, "n=1 depth formula"))
        n_one += 1

    # q=1: the all-zero matrix is the unique fixed state for every n.
    q_one = 0
    for n in range(1, 9):
        zero = (0,) * (n * n)
        check(update(zero, n) == zero, (n, "q=1 fixed"))
        check(core_ie(n, 1) == fixed_ie(n, 1) == 1,
              (n, "q=1 IE boundary"))
        check(one_image_count(n, 1) == depth_le_one_closed(n, 1) == 1,
              (n, "q=1 image/depth boundary"))
        q_one += 1

    # The source scout's sharp family, checked beyond the exhaustive boxes.
    witnesses = 0
    for n in range(2, 13):
        for q in range(2, 13):
            source = tuple(0 if j == 0 else 1
                           for _i in range(n) for j in range(n))
            first = update(source, n)
            second = update(first, n)
            check(not in_core(source, n), (n, q, "witness starts outside"))
            check(not in_core(first, n), (n, q, "witness exact depth >1"))
            check(in_core(second, n), (n, q, "witness lands"))
            witnesses += 1
    return structural, n_one, q_one, witnesses


def zero_incidence_witness():
    n, q = 3, 3
    left = (0, 0, 0,
            0, 0, 1,
            0, 1, 2)
    right = (0, 0, 0,
             0, 1, 0,
             0, 1, 2)
    a = rows(left, n)
    b = rows(right, n)
    left_row_max = tuple(map(max, a))
    right_row_max = tuple(map(max, b))
    left_column_max = tuple(max(a[i][j] for i in range(n)) for j in range(n))
    right_column_max = tuple(max(b[i][j] for i in range(n)) for j in range(n))
    check(in_core(left, n) and in_core(right, n), "incidence witness core")
    check(left_row_max == right_row_max, "incidence witness row maxima")
    check(left_column_max == right_column_max, "incidence witness column maxima")
    check(sum(left) == sum(right), "incidence witness sum")
    check(left.count(0) == right.count(0), "incidence witness zero count")
    left_fibre = predicted_two_fibre(left, n, q).total()
    right_fibre = predicted_two_fibre(right, n, q).total()
    check((left_fibre, right_fibre) == (10, 8), "incidence witness fibres")
    return left_fibre, right_fibre


def main():
    boxes = ((2, 2), (2, 3), (2, 4), (2, 5),
             (3, 2), (3, 3), (4, 2))
    summaries = []
    for n, q in boxes:
        summaries.append((n, q, exhaustive_box(n, q)))
    structural, n_one, q_one, witnesses = structural_and_boundary_checks()
    incidence = zero_incidence_witness()

    print("ATR_HOSTILE_GATE_INDEPENDENT_V1")
    print("author_sha256_scout=bde8b45b6a5adb8ebe2eedb2010e4521d2ebdfefd690f1910dd353068b45ce29")
    print("author_sha256_owner=6e284561a464f21064293416489a5fa8a4dd72dd8f73eb60cf89253b22d476b6")
    print("author_sha256_verifier=a38cd29feb6dd6396f186186d7992845eceb759479b03675ee05ac5fa8f85fa0")
    print("author_sha256_canonical=e7b73348dfdcf039e8f8ecd16a9d6514abf2520cc6b16499fc5e58c4778ed43d")
    for n, q, stats in summaries:
        print(
            f"box n={n} q={q} states={stats[0]} image1={stats[1]} "
            f"recurrent={stats[2]} fixed={stats[3]} "
            f"depths={stats[4]},{stats[5]},{stats[6]}"
        )
    print(f"structural_boxes={structural}; n1_boundaries={n_one}; "
          f"q1_boundaries={q_one}; sharp_witnesses={witnesses}")
    print(f"zero_incidence_fibre_witness={incidence[0]},{incidence[1]}")
    print(f"assertions={ASSERTIONS}")
    print("MATHEMATICS PASS")
    print("OWNER_SUBTRACTION TEMPORAL_SPINE_ZERO_CREDIT")
    print("INTERNAL_COLLISION P143_CORE_TRANSPOSE_INVERSE_ATLAS")
    print("DECISION KILL")
    print("EXTERNAL HOLD_EXTERNAL")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
