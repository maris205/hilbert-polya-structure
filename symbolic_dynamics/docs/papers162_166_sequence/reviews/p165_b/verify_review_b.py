#!/usr/bin/env python3
"""Independent hostile verifier for P165 low-weight support shortening.

This implementation imports neither the author verifier nor Review-A code.
It enumerates subspaces from unique RREF matrices, constructs the shortening
map literally from all codewords, and includes a native polynomial model of
GF(4)=GF(2)[a]/(a^2+a+1).
"""

from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
from math import factorial, prod


ASSERTIONS = 0


def check(condition: bool, message: str = "") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


class Field:
    def __init__(self, name, elements, add, multiply):
        self.name = name
        self.elements = tuple(elements)
        self.q = len(self.elements)
        self.add = add
        self.multiply = multiply
        self.nonzero = tuple(x for x in self.elements if x != 0)
        self.inverse = {}
        for x in self.nonzero:
            candidates = [y for y in self.nonzero if multiply(x, y) == 1]
            check(len(candidates) == 1, f"{name}: inverse of {x}")
            self.inverse[x] = candidates[0]


def prime_field(p: int) -> Field:
    return Field(
        f"F{p}",
        range(p),
        lambda x, y: (x + y) % p,
        lambda x, y: (x * y) % p,
    )


def f4_add(x: int, y: int) -> int:
    return x ^ y


def f4_multiply(x: int, y: int) -> int:
    # Integers encode c0+c1*a in bits (c0,c1); a^2=a+1.
    x0, x1 = x & 1, (x >> 1) & 1
    y0, y1 = y & 1, (y >> 1) & 1
    quadratic = x1 & y1
    constant = (x0 & y0) ^ quadratic
    linear = (x0 & y1) ^ (x1 & y0) ^ quadratic
    return constant | (linear << 1)


F4 = Field("F4", range(4), f4_add, f4_multiply)


def field_axiom_checks(field: Field) -> None:
    E = field.elements
    for x, y, z in product(E, repeat=3):
        check(field.add(field.add(x, y), z) == field.add(x, field.add(y, z)))
        check(field.multiply(field.multiply(x, y), z) == field.multiply(x, field.multiply(y, z)))
        check(
            field.multiply(x, field.add(y, z))
            == field.add(field.multiply(x, y), field.multiply(x, z))
        )
    for x, y in product(E, repeat=2):
        check(field.add(x, y) == field.add(y, x))
        check(field.multiply(x, y) == field.multiply(y, x))
    for x in E:
        check(field.add(x, 0) == x)
        check(field.multiply(x, 1) == x)
        check(any(field.add(x, y) == 0 for y in E))
        if x:
            check(field.multiply(x, field.inverse[x]) == 1)


def vector_add(field: Field, left, right):
    return tuple(field.add(x, y) for x, y in zip(left, right))


def scalar_vector(field: Field, scalar, vector):
    return tuple(field.multiply(scalar, x) for x in vector)


def span(field: Field, basis, n: int):
    zero = (0,) * n
    words = {zero}
    for row in basis:
        words = {
            vector_add(field, word, scalar_vector(field, scalar, row))
            for word in words
            for scalar in field.elements
        }
    return frozenset(words)


def rref_subspaces(field: Field, n: int):
    answer = {}
    columns = tuple(range(n))
    for dimension in range(n + 1):
        for pivots in combinations(columns, dimension):
            free = tuple(j for j in columns if j not in pivots)
            positions = tuple(
                (row, column)
                for row, pivot in enumerate(pivots)
                for column in free
                if column > pivot
            )
            for values in product(field.elements, repeat=len(positions)):
                matrix = [[0] * n for _ in range(dimension)]
                for row, pivot in enumerate(pivots):
                    matrix[row][pivot] = 1
                for (row, column), value in zip(positions, values):
                    matrix[row][column] = value
                basis = tuple(tuple(row) for row in matrix)
                code = span(field, basis, n)
                check(code not in answer, "RREF uniqueness")
                answer[code] = basis
    return answer


def gaussian_binomial(n: int, k: int, q: int) -> int:
    if not 0 <= k <= n:
        return 0
    numerator = prod(q ** (n - j) - 1 for j in range(k))
    denominator = prod(q ** (k - j) - 1 for j in range(k))
    return numerator // denominator


def weight(word) -> int:
    return sum(x != 0 for x in word)


def support(code):
    if not code:
        return frozenset()
    n = len(next(iter(code)))
    return frozenset(j for j in range(n) if any(word[j] != 0 for word in code))


def distance(code):
    nonzero_weights = [weight(word) for word in code if any(word)]
    return min(nonzero_weights) if nonzero_weights else None


def shortening(code):
    d = distance(code)
    if d is None:
        return code, frozenset()
    low_words = [word for word in code if 0 < weight(word) < 2 * d]
    purge = frozenset(j for word in low_words for j, x in enumerate(word) if x != 0)
    target = frozenset(word for word in code if all(word[j] == 0 for j in purge))
    return target, purge


def weak_shortening(code):
    d = distance(code)
    if d is None:
        return code
    low_words = [word for word in code if 0 < weight(word) <= 2 * d]
    purge = frozenset(j for word in low_words for j, x in enumerate(word) if x != 0)
    return frozenset(word for word in code if all(word[j] == 0 for j in purge))


def iterate(code, time: int):
    for _ in range(time):
        code = shortening(code)[0]
    return code


def full_support_line_vectors(field: Field, block, n: int):
    block = tuple(sorted(block))
    if not block:
        return ()
    answer = []
    for tail in product(field.nonzero, repeat=len(block) - 1):
        word = [0] * n
        word[block[0]] = 1
        for coordinate, value in zip(block[1:], tail):
            word[coordinate] = value
        answer.append(tuple(word))
    return tuple(answer)


def ordered_blocks(available, sizes):
    available = tuple(sorted(available))
    sizes = tuple(sizes)
    if not sizes:
        yield ()
        return
    first = sizes[0]
    for block in combinations(available, first):
        remaining = tuple(x for x in available if x not in block)
        for tail in ordered_blocks(remaining, sizes[1:]):
            yield (tuple(block),) + tail


def constructed_extremizers(field: Field, target, target_basis, time: int, n: int):
    if time == 0:
        return {target}
    sizes = tuple(1 << i for i in range(time))
    available = tuple(j for j in range(n) if j not in support(target))
    if sum(sizes) > len(available):
        return set()
    answer = set()
    for blocks in ordered_blocks(available, sizes):
        line_families = tuple(full_support_line_vectors(field, block, n) for block in blocks)
        for generators in product(*line_families):
            answer.add(span(field, target_basis + tuple(generators), n))
    return answer


def expected_extremal_count(q: int, zero_count: int, time: int) -> int:
    support_budget = (1 << time) - 1
    if support_budget > zero_count:
        return 0
    block_denominator = prod(factorial(1 << i) for i in range(time))
    block_count = factorial(zero_count) // (
        factorial(zero_count - support_budget) * block_denominator
    )
    return block_count * (q - 1) ** (support_budget - time)


def orbit_data(code):
    states = [code]
    purges = []
    while distance(states[-1]) is not None:
        target, purge = shortening(states[-1])
        purges.append(purge)
        states.append(target)
        check(len(states) < 100, "orbit termination")
    return tuple(states), tuple(purges)


def stable_code_key(code):
    return tuple(sorted(code))


def verify_box(field: Field, n: int):
    code_basis = rref_subspaces(field, n)
    codes = tuple(sorted(code_basis, key=stable_code_key))
    wanted_total = sum(gaussian_binomial(n, k, field.q) for k in range(n + 1))
    check(len(codes) == wanted_total, "Gaussian subspace count")
    for code, basis in code_basis.items():
        check(len(code) == field.q ** len(basis))

    transitions = {}
    orbits = {}
    depths = Counter()
    transition_rows = []
    zero = frozenset({(0,) * n})
    for code in codes:
        target, purge = shortening(code)
        check(target in code_basis)
        transitions[code] = target
        states, purges = orbit_data(code)
        orbits[code] = states
        depth = len(states) - 1
        depths[depth] += 1
        check(states[-1] == zero)
        check((target == code) == (code == zero), "unique fixed point")
        if code != zero:
            check(len(target) < len(code), "strict subcode descent")
            check(bool(purge), "nonzero purge")
            check(len(purge) >= distance(code))
            if target != zero:
                check(distance(target) >= 2 * distance(code), "distance doubling")
        transition_rows.append(
            (field.name, n, stable_code_key(code), stable_code_key(target), tuple(sorted(purge)), depth)
        )

    cap = (n + 1).bit_length() - 1
    check(max(depths) == cap, "sharp global height")
    if n == 0:
        check(depths == Counter({0: 1}))

    target_interfaces = 0
    extremal_interfaces = 0
    for time in range(cap + 3):
        fibres = defaultdict(set)
        for code in codes:
            target = orbits[code][time] if time < len(orbits[code]) else zero
            fibres[target].add(code)
        check(zero in fibres)
        positive_image = {target for target in fibres if target != zero}
        if time == 0:
            check(all(fibres[target] == {target} for target in codes), "time-zero identity")
        if time > cap:
            check(not positive_image, "post-cap image has only zero")

        support_budget = (1 << time) - 1
        for target in codes:
            if target == zero:
                continue
            target_distance = distance(target)
            zeros = n - len(support(target))
            predicted = target_distance >= (1 << time) and zeros >= support_budget
            check((target in positive_image) == predicted, "all-time image iff")
            if time >= 1 and zeros == 0:
                check(target not in positive_image, "full-support target")
            target_interfaces += 1
            observed_extreme = set()
            for source in fibres.get(target, ()):
                dimension_gap = len(code_basis[source]) - len(code_basis[target])
                new_support = len(support(source) - support(target))
                check(dimension_gap >= time, "dimension lower bound")
                check(new_support >= support_budget, "support lower bound")
                if dimension_gap == time and new_support == support_budget:
                    observed_extreme.add(source)
            expected_extreme = constructed_extremizers(
                field, target, code_basis[target], time, n
            ) if predicted else set()
            check(observed_extreme == expected_extreme, "simultaneous equality classification")
            check(
                len(expected_extreme)
                == (expected_extremal_count(field.q, zeros, time) if predicted else 0),
                "prime-power extremal count",
            )
            extremal_interfaces += 1

    # Zero-target boundary: exact-depth simultaneous dimension/support minima.
    zero_boundary = []
    for time in range(cap + 1):
        budget = (1 << time) - 1
        observed = {
            code for code in codes
            if len(orbits[code]) - 1 == time
            and len(code_basis[code]) == time
            and len(support(code)) == budget
        }
        expected = constructed_extremizers(field, zero, (), time, n)
        check(observed == expected, "zero-target exact-depth minimizers")
        check(len(observed) == expected_extremal_count(field.q, n, time))
        zero_boundary.append((time, len(observed)))

    # Full-support line census over this actual field, including GF(4).
    line_counts = []
    for block_size in range(1, n + 1):
        lines = full_support_line_vectors(field, tuple(range(block_size)), block_size)
        line_codes = {span(field, (generator,), block_size) for generator in lines}
        check(len(lines) == (field.q - 1) ** (block_size - 1))
        check(len(line_codes) == len(lines))
        check(all(len(support(line)) == block_size for line in line_codes))
        line_counts.append(len(lines))

    return (
        field.name,
        n,
        len(codes),
        tuple(sorted(depths.items())),
        target_interfaces,
        extremal_interfaces,
        tuple(zero_boundary),
        tuple(line_counts),
    ), transition_rows


def strict_boundary_sentinel(field: Field):
    n = 3
    first = (1, 0, 0)
    second = (0, 1, 1)
    code = span(field, (first, second), n)
    strict = shortening(code)[0]
    weak = weak_shortening(code)
    expected_strict = span(field, (second,), n)
    zero = frozenset({(0, 0, 0)})
    check(strict == expected_strict, "weight exactly 2d survives strict rule")
    check(weak == zero, "weight exactly 2d is purged by weak rule")
    return len(code), len(strict), len(weak)


def main():
    fields = (prime_field(2), prime_field(3), F4, prime_field(5))
    for field in fields:
        field_axiom_checks(field)
    alpha = 2
    check(F4.multiply(alpha, alpha) == F4.add(alpha, 1))
    check(F4.multiply(F4.multiply(alpha, alpha), alpha) == 1)

    ranges = {
        "F2": range(0, 8),
        "F3": range(0, 6),
        "F4": range(0, 5),
        "F5": range(0, 5),
    }
    rows = []
    transition_rows = []
    for field in fields:
        for n in ranges[field.name]:
            row, transitions = verify_box(field, n)
            rows.append(row)
            transition_rows.extend(transitions)
    sentinels = tuple((field.name, strict_boundary_sentinel(field)) for field in fields)
    transition_hash = sha256(repr(transition_rows).encode()).hexdigest()

    print("P165 HOSTILE REVIEW B — INDEPENDENT EXACT VERIFIER")
    print("lifecycle=HOLD_EXTERNAL")
    print("implementation=independent_RREF_plus_native_GF4")
    print("F4_model=a^2+a+1=0; a^2=a+1; a^3=1")
    print("rows: field,n,codes,depth_hist,target_interfaces,extremal_interfaces,zero_minima,full_support_lines")
    for row in rows:
        print("BOX", row)
    print("strict_boundary: field,(source_words,strict_words,weak_words)")
    for row in sentinels:
        print("STRICT", row)
    print("transition_sha256=" + transition_hash)
    print("assertions=" + str(ASSERTIONS))
    print("P165_REVIEW_B_EXACT_PASS")


if __name__ == "__main__":
    main()
