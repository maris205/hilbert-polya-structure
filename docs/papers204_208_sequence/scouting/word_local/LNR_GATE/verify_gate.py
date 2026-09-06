#!/usr/bin/env python3
"""Independent LNR candidate audit: literal sources versus cyclic edge signs.

No author or historical checker, data, or canonical is loaded.  The author
proofs, not their implementations, supply the statements under test.  Main
inverse engine counts colorings of each edge-sign necklace by 3x3 strict-order
matrices; it does not use the author's zero-run kernels to produce fibres.
Only the Python standard library is used. Complete deterministic JSON stdout.
"""
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
import json

CHECKS = Counter()
IDENTITY = (1, 0, 0, 0, 1, 0, 0, 0, 1)
ZERO = (0,) * 9
SYMBOLS = (0, 1, 2)
EXPECTED = {
    (2,): (2, 1, 0, 1, 1, 0, 0, 0, 0),
    (1,): (0, 1, 1, 1, 0, 1, 1, 1, 0),
    (1, 1): (2, 1, 1, 1, 1, 0, 1, 0, 0),
    (1, 2): (1, 1, 0, 0, 0, 0, 0, 0, 0),
    (2, 1): (1, 0, 0, 1, 0, 0, 0, 0, 0),
    (1, 1, 1): (2, 1, 0, 1, 0, 0, 0, 0, 0),
    (1, 2, 1): (1, 0, 0, 0, 0, 0, 0, 0, 0),
    (1, 1, 1, 1): (1, 0, 0, 0, 0, 0, 0, 0, 0),
}


def demand(test, kind, context=None):
    CHECKS[kind] += 1
    if not test:
        raise AssertionError((kind, context))


def literal(x):
    return tuple(int(x[i - 1] < value) + int(x[(i + 1) % len(x)] < value)
                 for i, value in enumerate(x))


def trace(a):
    return a[0] + a[4] + a[8]


def multiply(a, b):
    return tuple(sum(a[3 * i + t] * b[3 * t + j] for t in SYMBOLS)
                 for i in SYMBOLS for j in SYMBOLS)


def sign_step(matrix, sign):
    """Right multiply by I, strictly upper ones, or strictly lower ones."""
    if sign == 0:
        return matrix
    if sign == 1:
        return tuple(v for i in (0, 3, 6)
                     for v in (0, matrix[i], matrix[i] + matrix[i + 1]))
    return tuple(v for i in (0, 3, 6)
                 for v in (matrix[i + 1] + matrix[i + 2], matrix[i + 2], 0))


def sign_target(signs):
    return tuple(int(signs[i - 1] == 1) + int(s == -1)
                 for i, s in enumerate(signs))


def edge_signs(x):
    return tuple((x[(i + 1) % len(x)] > v) - (x[(i + 1) % len(x)] < v)
                 for i, v in enumerate(x))


def sign_coloring_set(signs):
    """Independent backtracking, used only for n <= 7 inverse-set comparison."""
    found = set()
    for first in SYMBOLS:
        partial = [first]

        def walk():
            if len(partial) == len(signs):
                closing = (first > partial[-1]) - (first < partial[-1])
                if closing == signs[-1]:
                    found.add(tuple(partial))
                return
            previous = partial[-1]
            for nxt in SYMBOLS:
                if (nxt > previous) - (nxt < previous) == signs[len(partial) - 1]:
                    partial.append(nxt)
                    walk()
                    partial.pop()

        walk()
    return found


def sign_atlas(n, literal_sets):
    fibres = Counter()
    sign_counts = {}
    reconstructed = defaultdict(set)
    signword = []

    def walk(matrix):
        if len(signword) == n:
            word = tuple(signword)
            count = trace(matrix)
            target = sign_target(word)
            sign_counts[word] = count
            if count:
                fibres[target] += count
            if n <= 7:
                choices = sign_coloring_set(word)
                demand(len(choices) == count, "edge_sign_coloring_count", word)
                demand(not (choices & reconstructed[target]), "disjoint_sign_strata", word)
                reconstructed[target].update(choices)
            return
        for sign in (-1, 0, 1):
            signword.append(sign)
            walk(sign_step(matrix, sign))
            signword.pop()

    walk(IDENTITY)
    if n <= 7:
        for target in product(SYMBOLS, repeat=n):
            demand(reconstructed[target] == literal_sets[target],
                   "full_inverse_set", target)
    return fibres, sign_counts


def lucas(t):
    a, b = 2, 1
    for _ in range(t):
        a, b = b, a + b
    return a


def rotations(x):
    return {x[i:] + x[:i] for i in range(len(x))}


def equality_targets(n):
    if n % 2 == 0:
        return rotations((0, 2) * (n // 2))
    m = n // 2
    result = rotations((0, 0) + (2, 0) * (m - 1) + (2,))
    result |= rotations((0, 1, 1) + (0, 2) * (m - 1))
    if n == 3:
        result.add((0, 0, 0))
    return result


def positive_blocks(y):
    if 0 not in y:
        return None
    start = y.index(0)
    rotated = y[start:] + y[:start] + (0,)
    result, block = [], []
    for value in rotated:
        if value:
            block.append(value)
        elif block:
            result.append(tuple(block))
            block = []
    return result


def fixed_language(y):
    blocks = positive_blocks(y)
    return blocks is not None and all(w in {(2,), (1, 1), (1, 2), (2, 1), (1, 2, 1)}
                                      for w in blocks)


def local_kernels():
    """Derive all positive-run kernels anew by a boundary finite search."""
    output = {}
    rows = []
    for length in range(1, 8):
        counts = defaultdict(lambda: [0] * 9)
        for a, b in product(SYMBOLS, repeat=2):
            for source in product(SYMBOLS, repeat=length):
                if a > source[0] or b > source[-1]:
                    continue
                extended = (a,) + source + (b,)
                target = tuple(int(extended[i - 1] < extended[i])
                               + int(extended[i + 1] < extended[i])
                               for i in range(1, length + 1))
                if 0 not in target:
                    counts[target][3 * a + b] += 1
        for word in product((1, 2), repeat=length):
            derived = tuple(counts[word])
            demand(derived == EXPECTED.get(word, ZERO), "complete_local_kernel", word)
            if any(derived):
                output[word] = derived
                rows.append({"word": ''.join(map(str, word)), "matrix": list(derived)})
    return output, rows


def kernel_trace(y, kernels):
    blocks = positive_blocks(y)
    if blocks is None:
        return 0
    if not blocks:
        return 3
    p = IDENTITY
    for block in blocks:
        p = multiply(p, kernels.get(block, ZERO))
        if p == ZERO:
            return 0
    return trace(p)


def matrix_word_pressure(kernels):
    words = sorted(kernels)
    census = []
    for r in range(2, 6):
        total, ties = 0, 0
        for indices in product(range(len(words)), repeat=r):
            blocks = [words[i] for i in indices]
            p, minimum_length = IDENTITY, r
            for w in blocks:
                p = multiply(p, kernels[w])
                minimum_length += len(w)
            count = trace(p)
            for padding in (0, 1, 2):
                n = minimum_length + padding
                target = tuple(v for w in blocks for v in (0,) + w) + (0,) * padding
                bound = lucas(2 * (n // 2))
                demand(count <= bound, "mixed_kernel_upper", (blocks, padding))
                demand((count == bound) == (target in equality_targets(n)),
                       "mixed_kernel_equality", (blocks, padding))
                total += 1
                ties += count == bound
        census.append({"blocks": r, "products_with_padding": total, "equality_cases": ties})
    return census


def audit_length(n, kernels):
    literal_fibres = Counter()
    literal_signs = Counter()
    literal_sets = defaultdict(set)
    heights = Counter()
    fixed = 0
    for x in product(SYMBOLS, repeat=n):
        y = literal(x)
        literal_fibres[y] += 1
        signs = edge_signs(x)
        literal_signs[signs] += 1
        demand(sign_target(signs) == y, "literal_edge_target", x)
        demand(sum(y) == sum(s != 0 for s in signs), "strict_edge_budget", x)
        demand(not all(v == 1 for v in y), "all_one_image_excluded", x)
        demand(all(not (y[i - 1] == y[i] == 2) for i in range(n)),
               "adjacent_two_excluded", x)
        if n <= 7:
            literal_sets[y].add(x)
        seen, state = {}, x
        while state not in seen:
            seen[state] = len(seen)
            state = literal(state)
        transient, period = seen[state], len(seen) - seen[state]
        demand(period == 1, "all_recurrent_fixed", x)
        demand(transient <= (1 if n == 3 else 3), "sharp_upper", x)
        heights[transient] += 1
        demand((y == x) == fixed_language(x), "fixed_language", x)
        fixed += y == x
    demand(max(heights) == (1 if n == 3 else 3), "height_attainment", n)
    fibres, sign_counts = sign_atlas(n, literal_sets)
    for s, count in sign_counts.items():
        demand(count == literal_signs[s], "all_edge_sign_counts", (n, s))
    max_fibre = max(literal_fibres.values())
    equality = set()
    all_counts = []
    for target in product(SYMBOLS, repeat=n):
        observed = literal_fibres[target]
        demand(fibres[target] == observed, "all_target_edge_inverse", target)
        demand(kernel_trace(target, kernels) == observed, "all_target_kernel_trace", target)
        demand(observed <= lucas(2 * (n // 2)), "all_target_upper", target)
        if observed == max_fibre:
            equality.add(target)
        all_counts.append(observed)
    demand(max_fibre == lucas(2 * (n // 2)), "maximum_value", n)
    demand(equality == equality_targets(n), "all_equality_targets", n)
    demand(sum(fibres.values()) == 3 ** n, "inverse_partition", n)
    return {
        "n": n, "states_and_targets": 3 ** n, "fixed_states": fixed,
        "entrance_distribution": dict(sorted(heights.items())),
        "image_size": len(fibres), "max_fibre": max_fibre,
        "fibre_distribution": dict(sorted(Counter(all_counts).items())),
        "all_target_fibre_count_vector_sha256": sha256(json.dumps(all_counts, separators=(',', ':')).encode()).hexdigest(),
        "equality_targets": [''.join(map(str, w)) for w in sorted(equality)],
        "full_inverse_sets_compared": n <= 7,
    }


def main():
    kernels, local_rows = local_kernels()
    lengths = [audit_length(n, kernels) for n in range(3, 12)]
    pressure = matrix_word_pressure(kernels)
    witnesses = []
    for n in range(4, 129):
        x = (0,) * (n - 3) + (1, 2, 2)
        orbit = [x]
        for _ in range(4):
            orbit.append(literal(orbit[-1]))
        demand(orbit[3] == orbit[4] and orbit[1] != orbit[2] and orbit[2] != orbit[3],
               "long_sharp_witness", n)
        witnesses.append(n)
    print(json.dumps({"status": "FINITE_CHECKS_PASS_NOT_A_NOVELTY_VERDICT",
                      "producer": "independent cyclic edge-sign coloring atlas",
                      "source_and_target_range": [3, 11],
                      "inverse_set_range": [3, 7], "local_positive_run_lengths": [1, 7],
                      "derived_local_kernels": local_rows, "lengths": lengths,
                      "mixed_kernel_pressure": pressure, "long_sharp_witness_lengths": witnesses,
                      "assertions_by_kind": dict(sorted(CHECKS.items())),
                      "assertions": sum(CHECKS.values())}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
