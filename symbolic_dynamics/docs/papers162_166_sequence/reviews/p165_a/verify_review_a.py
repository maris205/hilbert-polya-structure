#!/usr/bin/env python3
"""Independent hostile verifier A for P165.

All codes are generated independently in reduced row-echelon form.  The
program implements F_2, F_3, and the genuine nonprime field
F_4=F_2[x]/(x^2+x+1), starts from the literal padded-shortening map, and does
not import or inspect the author verifier.
"""

from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
from math import factorial, floor, log2
from pathlib import Path


ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


class FiniteField:
    def __init__(self, q):
        if q not in (2, 3, 4):
            raise ValueError("review field not implemented")
        self.q = q
        self.elements = tuple(range(q))

    def add(self, a, b):
        if self.q in (2, 4):
            return a ^ b
        return (a + b) % self.q

    def mul(self, a, b):
        if self.q in (2, 3):
            return (a * b) % self.q
        # Bits encode a0+a1*x and x^2=x+1 in F_2[x]/(x^2+x+1).
        a0, a1 = a & 1, (a >> 1) & 1
        b0, b1 = b & 1, (b >> 1) & 1
        p0 = a0 & b0
        p1 = (a0 & b1) ^ (a1 & b0)
        p2 = a1 & b1
        return (p0 ^ p2) | ((p1 ^ p2) << 1)

    def pow(self, a, exponent):
        out = 1
        base = a
        e = exponent
        while e:
            if e & 1:
                out = self.mul(out, base)
            base = self.mul(base, base)
            e >>= 1
        return out

    def inv(self, a):
        if a == 0:
            raise ZeroDivisionError
        return self.pow(a, self.q - 2)


def validate_field(field):
    q = field.q
    zero = 0
    one = 1
    for a, b, c in product(field.elements, repeat=3):
        check(field.add(field.add(a, b), c) == field.add(a, field.add(b, c)),
              f"add associativity F{q}")
        check(field.mul(field.mul(a, b), c) == field.mul(a, field.mul(b, c)),
              f"mul associativity F{q}")
        check(field.mul(a, field.add(b, c)) ==
              field.add(field.mul(a, b), field.mul(a, c)),
              f"distributivity F{q}")
    for a, b in product(field.elements, repeat=2):
        check(field.add(a, b) == field.add(b, a), f"add commutativity F{q}")
        check(field.mul(a, b) == field.mul(b, a), f"mul commutativity F{q}")
    for a in field.elements:
        check(field.add(a, zero) == a, f"zero F{q}")
        check(field.mul(a, one) == a, f"one F{q}")
        if a:
            check(field.mul(a, field.inv(a)) == one, f"inverse F{q}")


def vector_add(left, right, field):
    return tuple(field.add(a, b) for a, b in zip(left, right))


def scalar_vector(scalar, vector, field):
    return tuple(field.mul(scalar, x) for x in vector)


def zero_word(n):
    return (0,) * n


def word_support(word):
    mask = 0
    for index, value in enumerate(word):
        if value:
            mask |= 1 << index
    return mask


def word_weight(word):
    return sum(value != 0 for value in word)


def span_rows(rows, n, field):
    code = {zero_word(n)}
    for row in rows:
        multiples = [scalar_vector(a, row, field) for a in field.elements]
        code = {
            vector_add(word, multiple, field)
            for word in code
            for multiple in multiples
        }
    return frozenset(code)


def enumerate_codes(n, field):
    """Enumerate each subspace once from its unique RREF generator matrix."""
    codes = []
    for dimension in range(n + 1):
        for pivots in combinations(range(n), dimension):
            pivot_set = set(pivots)
            free_cells = [
                (row, column)
                for row, pivot in enumerate(pivots)
                for column in range(pivot + 1, n)
                if column not in pivot_set
            ]
            for values in product(field.elements, repeat=len(free_cells)):
                rows = [[0] * n for _ in range(dimension)]
                for row, pivot in enumerate(pivots):
                    rows[row][pivot] = 1
                for (row, column), value in zip(free_cells, values):
                    rows[row][column] = value
                codes.append(span_rows(tuple(map(tuple, rows)), n, field))
    check(len(codes) == len(set(codes)), f"RREF uniqueness F{field.q} n={n}")
    return tuple(codes)


def gaussian_binomial(n, k, q):
    if k < 0 or k > n:
        return 0
    numerator = 1
    denominator = 1
    for i in range(k):
        numerator *= q ** (n - i) - 1
        denominator *= q ** (k - i) - 1
    check(numerator % denominator == 0, "Gaussian integrality")
    return numerator // denominator


def code_dimension(code, q):
    size = len(code)
    dimension = 0
    while size > 1:
        check(size % q == 0, "code cardinality is q-power")
        size //= q
        dimension += 1
    return dimension


def code_support(code):
    out = 0
    for word in code:
        out |= word_support(word)
    return out


def code_distance(code):
    weights = [word_weight(word) for word in code if any(word)]
    return min(weights) if weights else None


def purge_support(code):
    distance = code_distance(code)
    if distance is None:
        return 0
    out = 0
    for word in code:
        weight = word_weight(word)
        if 0 < weight < 2 * distance:
            out |= word_support(word)
    return out


def literal_shortening(code):
    if code_distance(code) is None:
        return code
    purge = purge_support(code)
    return frozenset(
        word for word in code if word_support(word) & purge == 0
    )


def iterate_code(code, t):
    state = code
    for _ in range(t):
        state = literal_shortening(state)
    return state


def tau(code):
    steps = 0
    state = code
    while code_distance(state) is not None:
        state = literal_shortening(state)
        steps += 1
        check(steps <= 64, "termination sentinel")
    return steps


def sum_codes(components, n, field):
    out = frozenset({zero_word(n)})
    for component in components:
        out = frozenset(
            vector_add(left, right, field)
            for left in out
            for right in component
        )
    return out


def full_support_lines(block, n, field):
    block = tuple(sorted(block))
    if not block:
        return ()
    lines = []
    first = block[0]
    for tail in product(range(1, field.q), repeat=len(block) - 1):
        word = [0] * n
        word[first] = 1
        for coordinate, value in zip(block[1:], tail):
            word[coordinate] = value
        lines.append(span_rows((tuple(word),), n, field))
    check(len(lines) == (field.q - 1) ** (len(block) - 1),
          f"full-support line count F{field.q} block={block}")
    return tuple(lines)


def ordered_dyadic_blocks(available, t):
    available = tuple(sorted(available))

    def recurse(index, remaining, chosen):
        if index == t:
            yield tuple(chosen)
            return
        size = 1 << index
        for block in combinations(remaining, size):
            block_set = set(block)
            next_remaining = tuple(x for x in remaining if x not in block_set)
            yield from recurse(index + 1, next_remaining, chosen + [block])

    yield from recurse(0, available, [])


def constructed_extremizers(target, t, n, field):
    zeros = [i for i in range(n) if not ((code_support(target) >> i) & 1)]
    needed = (1 << t) - 1
    if len(zeros) < needed:
        return set()
    sources = set()
    for blocks in ordered_dyadic_blocks(zeros, t):
        line_families = [full_support_lines(block, n, field) for block in blocks]
        for lines in product(*line_families):
            sources.add(sum_codes((target,) + lines, n, field))
    return sources


def count_formula(zero_coordinates, t, q):
    needed = (1 << t) - 1
    if zero_coordinates < needed:
        return 0
    denominator = factorial(zero_coordinates - needed)
    for i in range(t):
        denominator *= factorial(1 << i)
    block_count = factorial(zero_coordinates) // denominator
    return block_count * (q - 1) ** (needed - t)


def check_extremal_structure(source, target, t, n, field):
    current = source
    reconstructed = [target]
    seen_purge = 0
    for i in range(t):
        next_code = literal_shortening(current)
        purge = purge_support(current)
        check(purge & seen_purge == 0, "extremal purge disjoint")
        check(purge & code_support(target) == 0, "extremal purge outside target")
        check(purge.bit_count() == 1 << i, "extremal dyadic block size")
        check(code_distance(current) == 1 << i, "extremal exact distance")
        line = frozenset(
            word for word in current if word_support(word) & ~purge == 0
        )
        check(len(line) == field.q, "extremal pure one-dimensional line")
        check(all(word_weight(word) == (1 << i)
                  for word in line if any(word)),
              "extremal line full support")
        check(code_dimension(current, field.q) ==
              code_dimension(next_code, field.q) + 1,
              "extremal codimension one")
        check(sum_codes((next_code, line), n, field) == current,
              "extremal direct-sum reconstruction")
        reconstructed.append(line)
        seen_purge |= purge
        current = next_code
    check(current == target, "extremal terminal target")
    check(sum_codes(tuple(reconstructed), n, field) == source,
          "extremal global reconstruction")


def check_box(q, n):
    field = FiniteField(q)
    codes = enumerate_codes(n, field)
    code_set = set(codes)
    expected_total = sum(gaussian_binomial(n, k, q) for k in range(n + 1))
    check(len(codes) == expected_total, f"subspace total F{q} n={n}")

    zero = frozenset({zero_word(n)})
    metadata = {}
    next_map = {}
    for code in codes:
        dimension = code_dimension(code, q)
        distance = code_distance(code)
        support = code_support(code)
        target = literal_shortening(code)
        check(target in code_set, f"shortening closure F{q} n={n}")
        check(target <= code, f"padded subcode F{q} n={n}")
        next_map[code] = target
        metadata[code] = (dimension, distance, support)
        if code != zero:
            check(target != code, f"strict descent F{q} n={n}")
            check(len(target) < len(code), f"proper cardinality F{q} n={n}")
            if target != zero:
                check(code_distance(target) >= 2 * distance,
                      f"distance doubling F{q} n={n}")

    fixed = {code for code in codes if next_map[code] == code}
    check(fixed == {zero}, f"unique recurrent fixed state F{q} n={n}")
    depths = {code: tau(code) for code in codes}
    height = floor(log2(n + 1))
    check(max(depths.values()) == height, f"sharp height F{q} n={n}")
    for code, depth in depths.items():
        check(iterate_code(code, depth) == zero, "tau reaches zero")
        if depth:
            check(iterate_code(code, depth - 1) != zero, "tau is first zero")

    all_iterations = {
        t: {source: iterate_code(source, t) for source in codes}
        for t in range(height + 2)
    }
    full_coordinate_mask = (1 << n) - 1
    equality_checks = 0
    for t, mapping in all_iterations.items():
        image = set(mapping.values())
        check(zero in image, f"zero in image F{q} n={n} t={t}")
        if (1 << t) - 1 > n:
            check(image == {zero}, f"post-positive cap F{q} n={n} t={t}")

        equality_sources = defaultdict(set)
        for source, target in mapping.items():
            if target == zero:
                check((target == zero) == (depths[source] <= t),
                      f"zero fibre depth identity F{q} n={n} t={t}")
                continue
            source_dim, _, source_support = metadata[source]
            target_dim, _, target_support = metadata[target]
            check(target <= source, f"iterate remains subcode F{q} n={n} t={t}")
            dim_drop = source_dim - target_dim
            new_support = (source_support & ~target_support).bit_count()
            check(dim_drop >= t, f"dimension lower bound F{q} n={n} t={t}")
            check(new_support >= (1 << t) - 1,
                  f"support lower bound F{q} n={n} t={t}")
            if dim_drop == t and new_support == (1 << t) - 1:
                equality_sources[target].add(source)
                check_extremal_structure(source, target, t, n, field)
                equality_checks += 1

        for target in codes:
            if target == zero:
                continue
            _, distance, support = metadata[target]
            zeros = n - support.bit_count()
            criterion = distance >= (1 << t) and zeros >= (1 << t) - 1
            check((target in image) == criterion,
                  f"nonzero image iff F{q} n={n} t={t}")
            expected_sources = constructed_extremizers(target, t, n, field) \
                if criterion else set()
            actual_sources = equality_sources[target]
            check(actual_sources == expected_sources,
                  f"extremizer iff classification F{q} n={n} t={t}")
            expected_count = count_formula(zeros, t, q) if criterion else 0
            check(len(actual_sources) == expected_count,
                  f"extremizer count F{q} n={n} t={t}")

            if t == 0:
                check(actual_sources == {target},
                      f"time-zero unique extremizer F{q} n={n}")
            if support == full_coordinate_mask and t > 0:
                check(target not in image,
                      f"full-support no positive preimage F{q} n={n} t={t}")

    # Exact-depth, zero-target simultaneous minimizers.
    exact_depth_counts = []
    for t in range(1, height + 1):
        actual = {
            code for code in codes
            if depths[code] == t
            and code_dimension(code, q) == t
            and code_support(code).bit_count() == (1 << t) - 1
        }
        constructed = constructed_extremizers(zero, t, n, field)
        check(actual == constructed,
              f"zero-target exact-depth block form F{q} n={n} t={t}")
        check(len(actual) == count_formula(n, t, q),
              f"zero-target exact-depth count F{q} n={n} t={t}")
        exact_depth_counts.append(len(actual))

    # The strict '<2d' convention differs from '<=2d' in the smallest useful
    # dyadic two-block witness whenever n>=3.
    if n >= 3:
        block0 = full_support_lines((0,), n, field)[0]
        block1 = full_support_lines((1, 2), n, field)[0]
        witness = sum_codes((block0, block1), n, field)
        strict_target = literal_shortening(witness)
        weak_purge = 0
        distance = code_distance(witness)
        for word in witness:
            if 0 < word_weight(word) <= 2 * distance:
                weak_purge |= word_support(word)
        weak_target = frozenset(
            word for word in witness if word_support(word) & weak_purge == 0
        )
        check(strict_target != weak_target, f"strict-boundary sentinel F{q} n={n}")

    print("BOX", f"F{q}", n, len(codes), height,
          ",".join(map(str, exact_depth_counts)) if exact_depth_counts else "-")
    return len(codes), equality_checks


def check_frozen_inputs():
    root = Path(__file__).resolve().parents[4]
    paper = root / "papers" / "165-low-weight-support-shortening"
    expected = {
        "main.tex": "bf245d0d0e968edf921af76bae15a77fc8068c3e196b0e880f48ec2a4e3275e4",
        "references.bib": "4e91997ae671fcade364a1057c31a7751aef863850f87df52e6277628df4b2a1",
        "main.pdf": "f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a",
        "main_round0_original.pdf": "f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a",
    }
    for name, digest in expected.items():
        actual = sha256((paper / name).read_bytes()).hexdigest()
        check(actual == digest, f"frozen input {name}")
    print("ARTIFACTS Round0/main/source PASS")


def main():
    check_frozen_inputs()
    for q in (2, 3, 4):
        validate_field(FiniteField(q))
    check(FiniteField(4).mul(2, 2) == 3, "F4 alpha squared alpha+1")
    check(FiniteField(4).mul(2, 3) == 1, "F4 primitive inverse")
    print("FIELDS F2/F3/F4 axioms PASS; F4=x^2+x+1")

    total_codes = 0
    total_equalities = 0
    print("BOX field/n/codes/height/exact-depth-minimizers")
    for n in range(8):
        count, equalities = check_box(2, n)
        total_codes += count
        total_equalities += equalities
    for n in range(5):
        count, equalities = check_box(3, n)
        total_codes += count
        total_equalities += equalities
    for n in range(4):
        count, equalities = check_box(4, n)
        total_codes += count
        total_equalities += equalities

    print("TOTAL_CODES", total_codes)
    print("STRUCTURAL_EQUALITY_SOURCES", total_equalities)
    print(f"ASSERTIONS {ASSERTIONS}")
    print("THEOREM descent/doubling/height/image/lower/equality/count PASS")
    print("BOUNDARIES D=0/t=0/n=0/full-support/strict-cut PASS")
    print("FINDINGS 0_CRITICAL 0_MAJOR 0_MINOR")
    print("VERDICT ACCEPT_INTERNAL HOLD_EXTERNAL")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
