#!/usr/bin/env python3
"""MNC author verification; all full cyclic boxes remain at the intake n=3..9.

New standard-library implementation, no historical or other author checker
imports, no canonical/runtime data. This is author evidence, not a review.
"""
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
import json

ALPHABET = range(3)
CHECKS = Counter()
I3 = (1, 0, 0, 0, 1, 0, 0, 0, 1)
R = (I3, (0, 1, 0, 1, 0, 1, 0, 1, 0), (0, 0, 1, 0, 0, 0, 1, 0, 0))
Q = (0, 1, 1, 1, 0, 1, 1, 1, 0)
T = (0, 2, 0, 1, 0, 1, 1, 0, 0)


def check(test, label, evidence=None):
    CHECKS[label] += 1
    if not test:
        raise AssertionError((label, evidence))


def mul(a, b):
    return tuple(sum(a[3 * i + k] * b[3 * k + j] for k in ALPHABET)
                 for i in ALPHABET for j in ALPHABET)


def add(a, b):
    return tuple(u + v for u, v in zip(a, b))


def power(a, n):
    result = I3
    for _ in range(n):
        result = mul(result, a)
    return result


def trace(a):
    return a[0] + a[4] + a[8]


def rule(a, b, c):
    return min(abs(a - b), abs(c - b))


def step(x):
    return tuple(rule(x[i - 1], v, x[(i + 1) % len(x)]) for i, v in enumerate(x))


def distances(x):
    return tuple(abs(x[i] - x[(i + 1) % len(x)]) for i in range(len(x)))


def minima(d):
    return tuple(min(d[i - 1], d[i]) for i in range(len(d)))


def explicit_weight(d):
    u, v = d.count(1), d.count(2)
    if u == 0:
        return 3 if v == 0 else (2 if v % 2 == 0 else 0)
    if u % 2:
        return 0
    if v == 0:
        return 2 ** (u // 2 + 1)
    first = d.index(2)
    rotated = d[first:] + d[:first] + (2,)
    parity = 0
    for value in rotated[1:]:
        if value == 1:
            parity ^= 1
        elif value == 2:
            if parity:
                return 0
            parity = 0
    return 2 ** (u // 2)


def color_walks(d):
    """Return actual labeled sources, for n <= 7 only."""
    out = set()
    for first in ALPHABET:
        word = [first]

        def extend():
            if len(word) == len(d):
                if abs(word[-1] - first) == d[-1]:
                    out.add(tuple(word))
                return
            for nxt in ALPHABET:
                if abs(word[-1] - nxt) == d[len(word) - 1]:
                    word.append(nxt)
                    extend()
                    word.pop()

        extend()
    return out


def zero_count(n):
    periodic_c = (2, 1, -1, -2, -1, 1)
    return 2 ** n + (-1) ** n + 2 * periodic_c[n % 6]


def all_one_count(n):
    return trace(power(T, n))


def singleton_mask(x):
    return tuple(int(x[i - 1] != v and x[(i + 1) % len(x)] != v)
                 for i, v in enumerate(x))


def relaxed_count(mask):
    n, k = len(mask), sum(mask)
    if k == 0:
        return zero_count(n)
    if k == n:
        return 2 ** n + 2 * (-1) ** n
    start = mask.index(1)
    rotated = mask[start:] + mask[:start] + (1,)
    lengths, size = [], 0
    for bit in rotated:
        if not bit:
            size += 1
        elif size:
            lengths.append(size)
            size = 0
    if 1 in lengths:
        return 0
    a_product, e_product = 1, 1
    for length in lengths:
        a_product *= (2 ** (length - 1) + (-1) ** length) // 3
        e_product *= (1, 1, 0, -1, -1, 0)[(length - 2) % 6]
    r = len(lengths)
    return 2 ** (k + r) * a_product + 2 * (-1) ** (k + r) * e_product


def is_fixed_pulse_word(x):
    return all(v == 0 or all(x[(i + offset) % len(x)] == 0 for offset in (-2, -1, 1, 2))
               for i, v in enumerate(x))


def rotations(x):
    return {x[i:] + x[:i] for i in range(len(x))}


def local_block_checks():
    matrices = {2: I3, 3: I3}
    rows = []
    for length in range(2, 9):
        if length >= 4:
            matrices[length] = add(matrices[length - 1], mul(Q, matrices[length - 2]))
        actual = [0] * 9
        for x in product(ALPHABET, repeat=length):
            if x[0] != x[1] or x[-1] != x[-2]:
                continue
            if any(x[i - 1] != x[i] and x[i + 1] != x[i] for i in range(1, length - 1)):
                continue
            actual[3 * x[0] + x[-1]] += 1
        check(tuple(actual) == matrices[length], "zero_block_endpoint_matrix", length)
        a = (2 ** (length - 1) + (-1) ** length) // 3
        e = (1, 1, 0, -1, -1, 0)[(length - 2) % 6]
        check(all(sum(actual[3 * i:3 * i + 3]) == a for i in ALPHABET),
              "zero_block_constant_eigenvalue", length)
        check(actual[0] - actual[1] == e and actual[4] - actual[3] == e,
              "zero_block_transverse_eigenvalue", length)
        rows.append({"length": length, "matrix": actual, "a": a, "e": e})
    return rows


def audit(n):
    source_fibres, d_counts, mask_counts, heights = Counter(), Counter(), Counter(), Counter()
    literal_sets = defaultdict(set)
    image = set()
    fixed = 0
    for x in product(ALPHABET, repeat=n):
        y, d = step(x), distances(x)
        mask = singleton_mask(x)
        source_fibres[y] += 1
        d_counts[d] += 1
        mask_counts[mask] += 1
        image.add(y)
        check(minima(d) == y, "literal_edge_factor", x)
        check(tuple(int(v > 0) for v in y) == mask, "exact_singleton_support", x)
        check(all(v != 0 or y[i - 1] == 0 or y[(i + 1) % n] == 0
                  for i, v in enumerate(y)), "paired_image_zeros", x)
        check((x == y) == is_fixed_pulse_word(x), "complete_fixed_language", x)
        fixed += x == y
        if n <= 7:
            literal_sets[y].add(x)
        seen, current = {}, x
        while current not in seen:
            seen[current] = len(seen)
            current = step(current)
        height = seen[current]
        check(len(seen) - height == 1, "no_nontrivial_cycles", x)
        check(height <= (2 if n <= 4 else 3), "temporal_upper", x)
        heights[height] += 1
    decoded_counts = Counter()
    decoded_sets = defaultdict(set)
    for d in product(ALPHABET, repeat=n):
        p = I3
        for value in d:
            p = mul(p, R[value])
        weight = explicit_weight(d)
        check(weight == trace(p), "distance_closed_weight_vs_matrix", d)
        check(weight == d_counts[d], "distance_closed_weight_vs_sources", d)
        b = minima(d)
        decoded_counts[b] += weight
        if n <= 7:
            choices = color_walks(d)
            check(len(choices) == weight, "distance_full_source_choices", d)
            check(not choices & decoded_sets[b], "distance_source_strata_disjoint", d)
            decoded_sets[b].update(choices)
    for mask in product((0, 1), repeat=n):
        count = relaxed_count(mask)
        check(count == mask_counts[mask], "all_relaxed_singleton_sets", mask)
        if 0 < sum(mask) < n:
            check(count <= 2 ** (n - 1) + 2, "relaxed_mixed_upper", mask)
    full_vector = []
    for b in product(ALPHABET, repeat=n):
        count = source_fibres[b]
        check(decoded_counts[b] == count, "every_target_inverse", b)
        if n <= 7:
            check(decoded_sets[b] == literal_sets[b], "every_target_inverse_set", b)
        if n >= 4 and any(b):
            check(count < zero_count(n), "every_nonzero_target_strict", b)
        if 0 in b and any(b):
            check(count <= relaxed_count(tuple(int(v > 0) for v in b)),
                  "actual_fibre_subset_relaxed", b)
        if 0 not in b and 2 in b:
            check(count <= 2 ** (n - 2), "all_positive_with_two_upper", b)
        full_vector.append(count)
    check(source_fibres[(0,) * n] == zero_count(n), "zero_fibre_formula", n)
    check(source_fibres[(1,) * n] == all_one_count(n), "all_one_fibre_formula", n)
    maximum = max(source_fibres.values())
    maximizers = sorted(b for b in image if source_fibres[b] == maximum)
    expected = [(1, 1, 1)] if n == 3 else [(0,) * n]
    check(maximizers == expected, "complete_maximum_equality", n)
    check(maximum == (6 if n == 3 else zero_count(n)), "sharp_maximum_value", n)
    check(max(heights) == (2 if n <= 4 else 3), "sharp_height_value", n)
    if n == 3:
        expected_image = {(0, 0, 0), (1, 1, 1)} | rotations((0, 0, 1)) | rotations((0, 0, 2))
        check(image == expected_image, "complete_three_image", n)
        check(literal_sets[(1, 1, 1)] == set(product(ALPHABET, repeat=3)) &
              {x for x in product(ALPHABET, repeat=3) if len(set(x)) == 3},
              "three_maximum_full_sources", n)
    if n == 4:
        expected_image = {(0,) * 4, (1,) * 4, (2,) * 4}
        for base in ((0, 0, 0, 1), (0, 0, 0, 2), (0, 0, 1, 1), (2, 1, 1, 1)):
            expected_image |= rotations(base)
        check(image == expected_image, "complete_four_image", n)
    return {"n": n, "states": 3 ** n, "image_size": len(image),
            "fixed_states": fixed, "height_histogram": dict(sorted(heights.items())),
            "fibre_histogram": dict(sorted(Counter(full_vector).items())),
            "zero_fibre": zero_count(n), "all_one_fibre": all_one_count(n),
            "maximum": maximum, "maximizers": [''.join(map(str, b)) for b in maximizers],
            "full_inverse_sets_checked": n <= 7,
            "lexicographic_fibre_vector_sha256": sha256(json.dumps(full_vector, separators=(',', ':')).encode()).hexdigest()}


def local_identity_checks():
    for values in product(ALPHABET, repeat=9):
        row = values
        for _ in range(3):
            row = tuple(rule(row[i - 1], row[i], row[i + 1]) for i in range(1, len(row) - 1))
        f3 = row[1]
        f4 = rule(*row)
        check(f3 == f4, "all_n_local_radius_four_identity", values)
    def binary_rule(a, b, c):
        return (a ^ b) & (b ^ c)
    check(sum(binary_rule(a, b, c) * 2 ** (4 * a + 2 * b + c)
              for a, b, c in product((0, 1), repeat=3)) == 36, "binary_ECA36_table")
    for values in product((0, 1), repeat=7):
        row = values
        for _ in range(2):
            row = tuple(binary_rule(row[i - 1], row[i], row[i + 1]) for i in range(1, len(row) - 1))
        check(row[1] == binary_rule(*row), "deducted_ECA36_second_stabilization", values)


def scalar_checks():
    check(power(T, 3) == add(tuple(2 * x for x in T), tuple(2 * x for x in I3)),
          "all_one_characteristic_identity")
    rows = []
    for n in range(4, 65):
        z, t = zero_count(n), all_one_count(n)
        check(2 ** (n - 1) + 2 < z, "scalar_mixed_strictness", n)
        check(2 ** (n - 2) < z, "scalar_positive_two_strictness", n)
        check(t < z and 4 * t <= 3 * 2 ** n, "scalar_all_one_strictness", n)
        source = (0, 0, 1, 2) if n == 4 else (0,) * (n - 4) + (1, 1, 0, 2)
        orbit = [source]
        for _ in range(4):
            orbit.append(step(orbit[-1]))
        expected_height = 2 if n == 4 else 3
        check(all(orbit[i] != orbit[i + 1] for i in range(expected_height))
              and orbit[expected_height] == orbit[expected_height + 1], "explicit_witness_orbit", n)
        if n <= 9:
            rows.append({"n": n, "Z_n": z, "t_n": t,
                         "mixed_upper": 2 ** (n - 1) + 2,
                         "positive_two_upper": 2 ** (n - 2),
                         "witness_orbit": [''.join(map(str, x)) for x in orbit]})
    return rows


def main():
    local_rows = local_block_checks()
    boxes = [audit(n) for n in range(3, 10)]
    local_identity_checks()
    scalar_rows = scalar_checks()
    table = [rule(a, b, c) for a, b, c in product(ALPHABET, repeat=3)]
    print(json.dumps({"status": "AUTHOR_FINITE_CHECKS_PASS_NOT_ADMISSION",
                      "full_cyclic_source_target_boxes": [3, 9],
                      "full_inverse_source_set_boxes": [3, 7],
                      "local_identity_input_length": 9,
                      "scalar_and_witness_only_lengths": [4, 64],
                      "rule_table_lex_abc": table,
                      "ternary_little_endian_rule_code": sum(v * 3 ** i for i, v in enumerate(table)),
                      "zero_block_endpoint_matrices": local_rows,
                      "boxes": boxes, "scalar_examples": scalar_rows,
                      "assertions_by_kind": dict(sorted(CHECKS.items())),
                      "assertions": sum(CHECKS.values())}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
