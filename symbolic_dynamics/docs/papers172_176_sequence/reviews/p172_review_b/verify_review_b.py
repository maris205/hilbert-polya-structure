#!/usr/bin/env python3
"""Hostile-review B exact controls for P172.

This program was written from the literal rule only.  It imports no author,
scout, Review-A, or earlier-paper module.  Its formulation differs in four
ways: it enumerates complete endomaps rather than restrictions; obtains
Stirling numbers by enumerating restricted-growth set partitions; checks the
full characteristic polynomial in SymPy; and encodes multiepoch marks by
Kronecker substitution in one polynomial exponent.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import comb, factorial

import sympy as sp


ASSERTIONS = 0
DIGEST = sha256()


def require(statement: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not statement:
        raise AssertionError(label)


def choose(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def states(n: int):
    return tuple(sorted(range(1 << n), key=lambda mask: (mask.bit_count(), mask)))


def contained(target: int, source: int) -> bool:
    return target & ~source == 0


def restricted_growth_words(length: int):
    """Enumerate set partitions by their canonical restricted-growth words."""
    if length == 0:
        yield ()
        return

    def extend(prefix, maximum):
        if len(prefix) == length:
            yield tuple(prefix)
            return
        for value in range(maximum + 2):
            prefix.append(value)
            yield from extend(prefix, max(maximum, value))
            prefix.pop()

    yield from extend([0], 0)


def partition_histogram(length: int) -> Counter:
    if length == 0:
        return Counter({0: 1})
    return Counter(max(word) + 1 for word in restricted_growth_words(length))


def marked_fixed_target_count(n: int, a: int, b: int, k: int, partitions) -> int:
    outside = k - b
    if not (0 <= b <= a <= n and 0 <= k <= a and 0 <= outside <= n - a):
        return 0
    return choose(n - a, outside) * factorial(k) * partitions[a].get(k, 0)


def unmarked_fixed_target_count_by_sieve(n: int, a: int, b: int) -> int:
    """Hit every one of b required internal boxes; avoid the other a-b."""
    return sum(
        (-1) ** omitted
        * comb(b, omitted)
        * (n - a + b - omitted) ** a
        for omitted in range(b + 1)
    )


def full_endomap_counts(n: int):
    """Count outcomes under all n^n complete maps [n] -> [n]."""
    ordered_states = states(n)
    counts = {source: Counter() for source in ordered_states}
    for function_tuple in product(range(n), repeat=n):
        for source in ordered_states:
            image = 0
            for point in range(n):
                if (source >> point) & 1:
                    image |= 1 << function_tuple[point]
            target = source & image
            counts[source][target, image.bit_count()] += 1
    return counts


def closed_quotient(n: int):
    matrix = []
    for a in range(n + 1):
        denominator = n**a if a else 1
        row = []
        for b in range(n + 1):
            numerator = (
                choose(a, b) * unmarked_fixed_target_count_by_sieve(n, a, b)
                if b <= a
                else 0
            )
            row.append(Fraction(numerator, denominator))
        require(sum(row, Fraction(0)) == 1, f"closed quotient row n={n} a={a}")
        matrix.append(row)
    return matrix


def to_sympy(matrix):
    return sp.Matrix(
        [[sp.Rational(value.numerator, value.denominator) for value in row] for row in matrix]
    )


def direct_full_matrix(n: int, counts):
    ordered_states = states(n)
    index = {state: position for position, state in enumerate(ordered_states)}
    denominator = n**n
    matrix = [[Fraction(0) for _ in ordered_states] for _ in ordered_states]
    for source in ordered_states:
        row = index[source]
        for (target, _mark), multiplicity in counts[source].items():
            matrix[row][index[target]] += Fraction(multiplicity, denominator)
    return ordered_states, matrix


def fraction_matrix_power(matrix, exponent: int):
    dimension = len(matrix)
    answer = [[Fraction(i == j) for j in range(dimension)] for i in range(dimension)]
    base = matrix
    while exponent:
        if exponent & 1:
            answer = fraction_matmul(answer, base)
        base = fraction_matmul(base, base)
        exponent //= 2
    return answer


def fraction_matmul(left, right):
    rows, middle, columns = len(left), len(right), len(right[0])
    return [
        [
            sum((left[i][k] * right[k][j] for k in range(middle)), Fraction(0))
            for j in range(columns)
        ]
        for i in range(rows)
    ]


def audit_literal_box(n: int):
    ordered_states = states(n)
    partitions = {a: partition_histogram(a) for a in range(n + 1)}
    counts = full_endomap_counts(n)
    full_map_count = n**n

    for source in ordered_states:
        a = source.bit_count()
        require(sum(counts[source].values()) == full_map_count, f"full map mass n={n} A={source}")
        for target in ordered_states:
            b = target.bit_count()
            for k in range(n + 1):
                actual = counts[source].get((target, k), 0)
                restriction_count = (
                    marked_fixed_target_count(n, a, b, k, partitions)
                    if contained(target, source)
                    else 0
                )
                expected = restriction_count * n ** (n - a)
                require(actual == expected, f"full-map marked count n={n} A={source} B={target} k={k}")
                DIGEST.update(f"{n}|{source}|{target}|{k}|{actual};".encode("ascii"))

        for b in range(a + 1):
            by_mark = sum(
                marked_fixed_target_count(n, a, b, k, partitions)
                for k in range(n + 1)
            )
            by_sieve = unmarked_fixed_target_count_by_sieve(n, a, b)
            require(by_mark == by_sieve, f"partition/sieve n={n} a={a} b={b}")

    ordered_states, full_matrix = direct_full_matrix(n, counts)
    quotient = closed_quotient(n)
    index = {state: position for position, state in enumerate(ordered_states)}

    for row, source in enumerate(ordered_states):
        a = source.bit_count()
        expected_diagonal = Fraction(factorial(a), n**a if a else 1)
        require(full_matrix[row][row] == expected_diagonal, f"full diagonal n={n} A={source}")
        require(sum(full_matrix[row], Fraction(0)) == 1, f"full row n={n} A={source}")
        for column, target in enumerate(ordered_states):
            require(
                full_matrix[row][column] == 0 or contained(target, source),
                f"nested support n={n} A={source} B={target}",
            )
            if column > row:
                require(full_matrix[row][column] == 0, f"lower triangle n={n} r={row} c={column}")

    # Check the invariant cardinality-function subspace: P L = L Q.
    lift = [
        [Fraction(source.bit_count() == a) for a in range(n + 1)]
        for source in ordered_states
    ]
    require(
        fraction_matmul(full_matrix, lift) == fraction_matmul(lift, quotient),
        f"intertwining P L = L Q n={n}",
    )

    for epoch in range(6):
        full_power = fraction_matrix_power(full_matrix, epoch)
        quotient_power = fraction_matrix_power(quotient, epoch)
        for source in ordered_states:
            a = source.bit_count()
            for target in ordered_states:
                b = target.bit_count()
                expected = (
                    quotient_power[a][b] / comb(a, b)
                    if contained(target, source) and b <= a
                    else Fraction(0)
                )
                require(
                    full_power[index[source]][index[target]] == expected,
                    f"labelled quotient n={n} t={epoch} A={source} B={target}",
                )

    # This is a genuine characteristic-polynomial check, not just a diagonal read.
    x = sp.Symbol("x")
    characteristic = to_sympy(full_matrix).charpoly(x).as_poly()
    expected_characteristic = sp.Poly(
        sp.prod(
            (x - sp.Rational(factorial(a), n**a if a else 1)) ** comb(n, a)
            for a in range(n + 1)
        ),
        x,
    )
    require(characteristic == expected_characteristic, f"full characteristic polynomial n={n}")
    DIGEST.update(str(characteristic.as_expr()).encode("ascii"))
    return counts, full_matrix, quotient


def poly_add(left, right):
    answer = Counter(left)
    for exponent, coefficient in right.items():
        answer[exponent] += coefficient
        if answer[exponent] == 0:
            del answer[exponent]
    return dict(answer)


def poly_mul(left, right):
    answer = Counter()
    for left_exponent, left_coefficient in left.items():
        for right_exponent, right_coefficient in right.items():
            answer[left_exponent + right_exponent] += left_coefficient * right_coefficient
    return {exponent: coefficient for exponent, coefficient in answer.items() if coefficient}


def poly_matrix_identity(dimension: int):
    return [[({0: Fraction(1)} if i == j else {}) for j in range(dimension)] for i in range(dimension)]


def poly_matrix_multiply(left, right):
    rows, middle, columns = len(left), len(right), len(right[0])
    answer = [[{} for _ in range(columns)] for _ in range(rows)]
    for i in range(rows):
        for k in range(middle):
            if not left[i][k]:
                continue
            for j in range(columns):
                if right[k][j]:
                    answer[i][j] = poly_add(answer[i][j], poly_mul(left[i][k], right[k][j]))
    return answer


def direct_marked_matrix(n: int, counts, place_value: int):
    ordered_states = states(n)
    index = {state: position for position, state in enumerate(ordered_states)}
    denominator = n**n
    matrix = [[{} for _ in ordered_states] for _ in ordered_states]
    for source in ordered_states:
        for (target, image_size), multiplicity in counts[source].items():
            row, column = index[source], index[target]
            exponent = image_size * place_value
            term = {exponent: Fraction(multiplicity, denominator)}
            matrix[row][column] = poly_add(matrix[row][column], term)
    return matrix


def closed_marked_quotient(n: int, place_value: int, partitions):
    matrix = [[{} for _ in range(n + 1)] for _ in range(n + 1)]
    for a in range(n + 1):
        denominator = n**a if a else 1
        for b in range(a + 1):
            terms = {}
            for k in range(n + 1):
                count = choose(a, b) * marked_fixed_target_count(n, a, b, k, partitions)
                if count:
                    terms[k * place_value] = Fraction(count, denominator)
            matrix[a][b] = terms
    return matrix


def divide_polynomial(polynomial, denominator: int):
    return {exponent: coefficient / denominator for exponent, coefficient in polynomial.items()}


def audit_multiepoch_marks(n: int, counts, horizon: int = 3):
    ordered_states = states(n)
    index = {state: position for position, state in enumerate(ordered_states)}
    partitions = {a: partition_histogram(a) for a in range(n + 1)}
    base = n + 1  # unique base expansion for histories (k_1,...,k_t)
    full_product = poly_matrix_identity(len(ordered_states))
    quotient_product = poly_matrix_identity(n + 1)

    for epoch in range(horizon):
        place = base**epoch
        full_product = poly_matrix_multiply(
            full_product, direct_marked_matrix(n, counts, place)
        )
        quotient_product = poly_matrix_multiply(
            quotient_product, closed_marked_quotient(n, place, partitions)
        )

        for source in ordered_states:
            a = source.bit_count()
            for target in ordered_states:
                b = target.bit_count()
                expected = (
                    divide_polynomial(quotient_product[a][b], comb(a, b))
                    if contained(target, source) and b <= a
                    else {}
                )
                actual = full_product[index[source]][index[target]]
                require(actual == expected, f"marked quotient n={n} t={epoch+1} A={source} B={target}")

        total = Counter()
        full_source = ordered_states[-1]
        for target in ordered_states:
            total.update(full_product[index[full_source]][index[target]])
        require(sum(total.values(), Fraction(0)) == 1, f"marked mass n={n} t={epoch+1}")
        DIGEST.update(repr(sorted(total.items())).encode("ascii"))


def recursive_means(quotient):
    n = len(quotient) - 1
    means = [Fraction(0) for _ in range(n + 1)]
    for a in range(1, n + 1):
        means[a] = (
            1 + sum(quotient[a][b] * means[b] for b in range(a))
        ) / (1 - quotient[a][a])
    return means


def audit_jordan_and_absorption(n: int):
    quotient = closed_quotient(n)
    qsym = to_sympy(quotient)
    lam = Fraction(factorial(n), n**n)
    require(lam == Fraction(factorial(n - 1), n ** (n - 1)), f"top collision n={n}")
    for a in range(n - 1):
        require(
            Fraction(factorial(a), n**a if a else 1)
            > Fraction(factorial(a + 1), n ** (a + 1)),
            f"strict spectrum n={n} a={a}",
        )
    require(quotient[n][n - 1] > 0, f"positive resonant coupling n={n}")

    shifted = qsym - sp.Rational(lam.numerator, lam.denominator) * sp.eye(n + 1)
    # DomainMatrix uses exact QQ-domain elimination and avoids expression swell.
    nullity_one = n + 1 - shifted.to_DM().rank()
    nullity_two = n + 1 - (shifted * shifted).to_DM().rank()
    require(nullity_one == 1, f"top eigenspace n={n}")
    require(nullity_two == 2, f"top generalized eigenspace n={n}")

    x = sp.Symbol("x")
    characteristic = qsym.charpoly(x).as_poly()
    expected_characteristic = sp.Poly(
        sp.prod(
            x - sp.Rational(factorial(a), n**a if a else 1)
            for a in range(n + 1)
        ),
        x,
    )
    require(characteristic == expected_characteristic, f"quotient characteristic n={n}")

    for a in range(1, n + 1):
        require(quotient[a][a] < 1, f"transient layer n={n} a={a}")
        if a < n:
            require(quotient[a][0] > 0, f"proper layer direct zero n={n} a={a}")
    require(sum(quotient[n][b] for b in range(n)) > 0, f"full layer loses n={n}")

    recursive = recursive_means(quotient)
    transient = sp.Matrix(
        [[sp.Rational(quotient[a][b].numerator, quotient[a][b].denominator)
          for b in range(1, n + 1)] for a in range(1, n + 1)]
    )
    solved = (sp.eye(n) - transient).inv() * sp.ones(n, 1)
    for a in range(1, n + 1):
        require(
            solved[a - 1] == sp.Rational(recursive[a].numerator, recursive[a].denominator),
            f"fundamental-matrix mean n={n} a={a}",
        )
    return nullity_one, nullity_two, recursive[n]


def audit_boundaries():
    q1 = closed_quotient(1)
    require(q1 == [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]], "n=1 identity")
    q2 = closed_quotient(2)
    expected = [
        [Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(1, 2), Fraction(1, 2), Fraction(0)],
        [Fraction(0), Fraction(1, 2), Fraction(1, 2)],
    ]
    require(q2 == expected, "n=2 quotient")
    require(recursive_means(q2)[2] == 4, "n=2 mean four")


def main() -> None:
    print("P172 HOSTILE REVIEW B — FORMULATION-INDEPENDENT CONTROL")
    print("PROVENANCE full-endomap tuples / RGS partitions / SymPy charpoly")
    print("IMPORTS no author, scout, Review-A, or earlier-paper code")
    print("STATUS HOLD_EXTERNAL")

    small_boxes = {}
    for n in range(1, 6):
        counts, full_matrix, quotient = audit_literal_box(n)
        small_boxes[n] = counts
        print(
            f"LITERAL n={n} full_maps={n**n} states={2**n} "
            f"epochs=0..5 charpoly=PASS"
        )

    for n in range(1, 5):
        audit_multiepoch_marks(n, small_boxes[n], horizon=3)
        print(f"MARKS n={n} epochs=1..3 Kronecker-coefficientwise=PASS")

    for n in range(2, 19):
        first, second, mean = audit_jordan_and_absorption(n)
        print(f"QUOTIENT n={n} nullities={first},{second} mean_full={mean} PASS")

    audit_boundaries()
    print("BOUNDARIES n=1 identity / n=2 quotient+mean PASS")
    print("CLAIM endpoint+total-image Stirling count PASS")
    print("CLAIM every-time labelled quotient PASS")
    print("CLAIM complete algebraic spectrum PASS")
    print("CLAIM forced top J2 PASS")
    print("CLAIM absorption and multiepoch marks PASS")
    print(f"DIGEST {DIGEST.hexdigest()}")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("VERDICT EXECUTABLE_CLAIMS_PASS_OWNER_REPAIR_REQUIRED")


if __name__ == "__main__":
    main()
