#!/usr/bin/env python3
"""Self-contained author LNR checks; no repository/data/canonical file reads.

Representation 1: edge-oriented literal source enumeration.
Representation 2: zero-block source decoder using the stated local lists.
Representation 3: evaluated kernel product for each labelled target.
Finite checks pressure, but do not prove, the all-n manuscript deduction.
"""
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
import json


ASSERTIONS = 0
RECORD = sha256()
ZERO = ((0, 0, 0),) * 3
IDENTITY = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
KERNELS = {
    (2,): ((2, 1, 0), (1, 1, 0), (0, 0, 0)),
    (1,): ((0, 1, 1), (1, 0, 1), (1, 1, 0)),
    (1, 1): ((2, 1, 1), (1, 1, 0), (1, 0, 0)),
    (1, 2): ((1, 1, 0), (0, 0, 0), (0, 0, 0)),
    (2, 1): ((1, 0, 0), (1, 0, 0), (0, 0, 0)),
    (1, 1, 1): ((2, 1, 0), (1, 0, 0), (0, 0, 0)),
    (1, 2, 1): ((1, 0, 0), (0, 0, 0), (0, 0, 0)),
    (1, 1, 1, 1): ((1, 0, 0), (0, 0, 0), (0, 0, 0)),
}
A, J, B = (KERNELS[w] for w in ((2,), (1,), (1, 1)))


def check(condition, detail):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(detail)


def record(obj):
    RECORD.update(json.dumps(obj, separators=(",", ":")).encode())
    RECORD.update(b"\n")


def literal_edges(x):
    y = [0] * len(x)
    for i in range(len(x)):
        j = (i + 1) % len(x)
        if x[i] > x[j]:
            y[i] += 1
        elif x[i] < x[j]:
            y[j] += 1
    return tuple(y)


def mul(m, q):
    return tuple(tuple(sum(m[i][k] * q[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


def trace(m):
    return sum(m[i][i] for i in range(3))


def lucas(t):
    a, b = 2, 1
    for _ in range(t):
        a, b = b, a + b
    return a


def rotations(x):
    return {x[i:] + x[:i] for i in range(len(x))}


def equality_targets(n):
    m = n // 2
    if n % 2 == 0:
        return rotations((0, 2) * m)
    ans = rotations((0, 0) + (2, 0) * (m - 1) + (2,))
    ans |= rotations((0, 1, 1) + (0, 2) * (m - 1))
    if n == 3:
        ans.add((0, 0, 0))
    return ans


def local_list(w, a, b):
    out = []
    if w == (2,):
        if a == b == 0:
            out.append((1,))
        if a < 2 and b < 2:
            out.append((2,))
    elif w == (1,):
        if (a, b) in ((0, 1), (1, 0)):
            out.append((1,))
        if (a, b) in ((0, 2), (1, 2), (2, 0), (2, 1)):
            out.append((2,))
    elif w == (1, 1):
        if a == b == 0:
            out.append((1, 1))
        if a < 2 and b < 2:
            out.append((2, 2))
        if (a, b) == (0, 2):
            out.append((1, 2))
        if (a, b) == (2, 0):
            out.append((2, 1))
    elif w == (1, 2):
        if a == 0 and b < 2:
            out.append((1, 2))
    elif w == (2, 1):
        if a < 2 and b == 0:
            out.append((2, 1))
    elif w == (1, 1, 1):
        if a == 0 and b < 2:
            out.append((1, 2, 2))
        if a < 2 and b == 0:
            out.append((2, 2, 1))
    elif w == (1, 2, 1):
        if a == b == 0:
            out.append((1, 2, 1))
    elif w == (1, 1, 1, 1):
        if a == b == 0:
            out.append((1, 2, 2, 1))
    return tuple(out)


def split_target(b):
    n = len(b)
    start = next(i for i in range(n) if b[i] == 0 and b[(i - 1) % n] > 0)
    offset, zeros, positives, words = 0, [], [], []
    while offset < n:
        z, p = [], []
        while offset < n and b[(start + offset) % n] == 0:
            z.append((start + offset) % n)
            offset += 1
        while offset < n and b[(start + offset) % n] > 0:
            p.append((start + offset) % n)
            offset += 1
        zeros.append(tuple(z))
        positives.append(tuple(p))
        words.append(tuple(b[i] for i in p))
    return zeros, positives, words


def decode_and_count(b):
    n = len(b)
    if 0 not in b:
        return set(), 0
    if not any(b):
        return {(v,) * n for v in range(3)}, 3
    zeros, positives, words = split_target(b)
    r = len(words)
    m = IDENTITY
    for w in words:
        m = mul(m, KERNELS.get(w, ZERO))
    sources = set()
    for heights in product(range(3), repeat=r):
        choices = [local_list(w, heights[j], heights[(j + 1) % r])
                   for j, w in enumerate(words)]
        if not all(choices):
            continue
        base = [-1] * n
        for j, z in enumerate(zeros):
            for i in z:
                base[i] = heights[j]
        for fillings in product(*choices):
            x = base.copy()
            for sites, letters in zip(positives, fillings):
                for i, letter in zip(sites, letters):
                    x[i] = letter
            sx = tuple(x)
            check(sx not in sources, ("decoder injection", b, heights, fillings))
            sources.add(sx)
    return sources, trace(m)


def check_local_tables():
    boxes = []
    for m in range(1, 7):
        inventory = defaultdict(set)
        attempts = 0
        for a, b in product(range(3), repeat=2):
            for u in product((1, 2), repeat=m):
                attempts += 1
                if not (a <= u[0] and b <= u[-1]):
                    continue
                v = (a,) + u + (b,)
                w = tuple(int(v[i - 1] < v[i]) + int(v[i + 1] < v[i])
                          for i in range(1, m + 1))
                if all(w):
                    inventory[w, a, b].add(u)
            for w in product((1, 2), repeat=m):
                stated = local_list(w, a, b)
                check(len(set(stated)) == len(stated), ("local injective", w, a, b))
                check(set(stated) == inventory[w, a, b], ("local list", w, a, b))
                check(len(stated) == KERNELS.get(w, ZERO)[a][b],
                      ("evaluated kernel", w, a, b))
                record(("local", w, a, b, sorted(stated)))
        boxes.append({"positive_run_length": m, "source_boundary_attempts": attempts,
                      "nonempty_boundary_fibres": sum(bool(v) for v in inventory.values())})
    return boxes


def check_full_inverses():
    boxes = []
    for n in range(3, 9):
        inverse = defaultdict(set)
        for x in product(range(3), repeat=n):
            inverse[literal_edges(x)].add(x)
        counts = {}
        for b in product(range(3), repeat=n):
            decoded, evaluated = decode_and_count(b)
            observed = inverse.get(b, set())
            check(decoded == observed, ("full labelled source set", b))
            check(evaluated == len(observed), ("kernel count", b))
            check(len(observed) <= lucas(2 * (n // 2)), ("global maximum bound", b))
            counts[b] = len(observed)
            record(("inverse", b, sorted(observed), evaluated))
        maximum = max(counts.values())
        equal = {b for b, count in counts.items() if count == maximum}
        check(maximum == lucas(2 * (n // 2)), ("maximum value", n))
        check(equal == equality_targets(n), ("all labelled equality targets", n))
        check(len(equal) == (7 if n == 3 else 2 if n % 2 == 0 else 2 * n),
              ("equality cardinality", n))
        check(sum(counts.values()) == 3 ** n, ("all sources counted", n))
        boxes.append({"n": n, "all_sources_and_targets_each": 3 ** n,
                      "image_size": len(inverse), "maximum_fibre": maximum,
                      "all_labelled_maximizers": sorted(equal),
                      "target_fibre_histogram_including_empty": sorted(Counter(counts.values()).items())})
    return boxes


def check_matrix_words():
    boxes = []
    for r in range(2, 11):
        counts = Counter()
        for labels in product(range(3), repeat=r):
            m = IDENTITY
            for label in labels:
                m = mul(m, (A, J, B)[label])
            k, j = labels.count(2), labels.count(1)
            value = trace(m)
            upper = lucas(2 * (r + k // 2))
            check(value <= upper, ("mixed kernel bound", labels, value))
            should_equal = k <= 1 and j == 0
            check((value == upper) == should_equal, ("mixed kernel strictness", labels, value))
            counts[(k, j, value == upper)] += 1
            record(("matrixword", labels, value))
        boxes.append({"product_length": r, "all_A_J_B_words": 3 ** r,
                      "equality_words": r + 1,
                      "by_B_count_J_count_equality": [list(key) + [val] for key, val in sorted(counts.items())]})
    p = A
    for r in range(2, 101):
        previous = p
        p = mul(p, A)
        check(trace(p) == lucas(2 * r), ("Lucas evaluation", r))
        check(trace(mul(B, previous)) == trace(p), ("one B identity", r))
        for w in ((1, 2), (2, 1), (1, 1, 1), (1, 2, 1), (1, 1, 1, 1)):
            check(trace(mul(KERNELS[w], previous)) < trace(p), ("dominated strict", r, w))
    # Rational certificates used for the displayed analytic constants; no floats.
    check(13 ** 2 < 3 * 13 * 5 - 5 ** 2, "13/5 below larger quadratic root")
    check(169 ** 3 > 270 * 25 ** 3, "3*cuberoot(10)<(13/5)^2")
    check(13 ** 3 > 10 * 5 ** 3, "10<lambda^3")
    check(13 ** 4 > 30 * 5 ** 4, "30<lambda^4")
    check(13 ** 4 > 9 * 5 ** 4, "9<lambda^4")
    return boxes


def check_classical_extremizer_adapter():
    boxes = []
    for m in range(2, 6):
        n = 2 * m
        b = (0, 2) * m
        literal_sources = {x for x in product(range(3), repeat=n) if literal_edges(x) == b}
        reconstructed, independent_sets = set(), 0
        for mask in product((0, 1), repeat=n):
            if any(mask[i] and mask[(i + 1) % n] for i in range(n)):
                continue
            independent_sets += 1
            # On valleys mark source height 1; on peaks mark source height 1.
            # Neighbouring marks are precisely the forbidden equality 1=1.
            x = tuple(mask[i] if i % 2 == 0 else 2 - mask[i] for i in range(n))
            reconstructed.add(x)
        check(reconstructed == literal_sources, ("full independent-set adapter", n))
        check(independent_sets == lucas(n), ("classical extremizer count", n))
        boxes.append({"n": n, "independent_sets": independent_sets,
                      "full_labelled_source_bijection": True})
    return boxes


def main():
    local = check_local_tables()
    inverse = check_full_inverses()
    mixed = check_matrix_words()
    classical = check_classical_extremizer_adapter()
    print(json.dumps({
        "status": "PASS", "kind": "author finite corroboration, not independent review or all-n proof",
        "no_input_file_reads": True, "literal": "strictly larger endpoint receives one per cyclic edge",
        "local_tables": local, "full_inverse_boxes": inverse,
        "mixed_matrix_words": mixed, "classical_adapter": classical,
        "matrix_identity_range": [2, 100], "assertions": ASSERTIONS,
        "ordered_checked_record_sha256": RECORD.hexdigest(),
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
