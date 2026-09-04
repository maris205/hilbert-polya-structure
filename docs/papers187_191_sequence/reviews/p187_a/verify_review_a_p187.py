#!/usr/bin/env python3
"""Process-separated hostile Review-A control for P187.

This program deliberately does not import the author verifier.  Exponent
words are generated from packed base-q integers.  Fibres are reconstructed as
closed oriented edge walks, and only then compared with the manuscript's
matrix trace.  The forward clock is attacked through the frozen-peak/residual
decomposition rather than inferred from orbit histograms.
"""

from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
from math import comb, gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
INPUTS = {
    "papers/187-cyclic-divisor-quotient/main.tex":
        "e4dd2c5afb6381563476c6b6735f94c932403492165b8f21adeee6a448f7b83d",
    "papers/187-cyclic-divisor-quotient/main_round0_original.pdf":
        "399ee1fd64a569ef3076e1049a5151e5b4b07d03d2c1592f84c5b2a811fbb8a1",
    "papers/187-cyclic-divisor-quotient/code/verify_p187.py":
        "bb171bd84a5f614b868c6fd6e6008c646a282045bef484d4552081967743cf1e",
    "papers/187-cyclic-divisor-quotient/code/CANONICAL.txt":
        "b48c1753908ca9b168803cb6406499945bb59a82ac16d0f1f87e9ef278f8bb8d",
    "papers/187-cyclic-divisor-quotient/PROOF_PACKAGE.md":
        "095d2370f9c4f4b5d62e909a773f9a2fc05f2577ea8313b39472843b6071955d",
    "papers/187-cyclic-divisor-quotient/SOURCE_VERIFICATION.md":
        "cdf97a65b4df3ac1f1ea4a3c8959d2db0ffc367777d3e00080c8c9bd854eedac",
}

ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def bind_inputs():
    for relative, expected in INPUTS.items():
        path = ROOT / relative
        check(path.is_file(), ("missing pinned input", relative))
        check(sha256(path.read_bytes()).hexdigest() == expected,
              ("pinned-input drift", relative))


def unpack(code, q, m):
    word = []
    for _ in range(m):
        word.append(code % q)
        code //= q
    return tuple(word)


def exponent_words(a, m):
    q = a + 1
    for code in range(q ** m):
        yield unpack(code, q, m)


def positive_difference(word):
    m = len(word)
    return tuple(max(word[i] - word[(i + 1) % m], 0)
                 for i in range(m))


def iterate(word, t):
    for _ in range(t):
        word = positive_difference(word)
    return word


def tail(word):
    seen = set()
    time = 0
    while positive_difference(word) != word:
        check(word not in seen, ("nonfixed cycle", word))
        seen.add(word)
        word = positive_difference(word)
        time += 1
        check(time <= 1 + max(word, default=0) + len(word),
              ("orbit guard", word))
    return time


def edge_allowed(left, right, output):
    return max(left - right, 0) == output


def closed_edge_walk_count(a, target):
    """Count oriented cyclic lifts without matrix multiplication."""
    q = a + 1
    total = 0
    for initial in range(q):
        layer = {initial: 1}
        for output in target:
            following = defaultdict(int)
            for left, multiplicity in layer.items():
                for right in range(q):
                    if edge_allowed(left, right, output):
                        following[right] += multiplicity
            layer = following
        total += layer.get(initial, 0)
    return total


def local_matrix(a, output):
    return [[int(edge_allowed(left, right, output))
             for right in range(a + 1)]
            for left in range(a + 1)]


def matrix_product(left, right):
    q = len(left)
    return [[sum(left[i][k] * right[k][j] for k in range(q))
             for j in range(q)] for i in range(q)]


def manuscript_trace(a, target):
    q = a + 1
    result = [[int(i == j) for j in range(q)] for i in range(q)]
    for output in target:
        result = matrix_product(result, local_matrix(a, output))
    return sum(result[i][i] for i in range(q))


def cyclic_support_weight(a, m):
    total = 0
    for mask in range(1 << m):
        if all(not ((mask >> i) & 1 and
                    (mask >> ((i + 1) % m)) & 1)
               for i in range(m)):
            total += a ** mask.bit_count()
    return total


def cyclic_polynomial_closed(a, m):
    return sum((m * comb(m - k, k) // (m - k)) * a ** k
               for k in range(m // 2 + 1))


def frozen_peak_attack(word):
    h = max(word, default=0)
    z = positive_difference(word)
    peaks = {i for i, value in enumerate(z) if h > 0 and value == h}
    m = len(word)
    residual = tuple(0 if i in peaks else z[i] for i in range(m))
    frozen = tuple(h if i in peaks else 0 for i in range(m))

    check(max(residual, default=0) <= max(0, h - 1),
          ("residual height", word))
    for i in peaks:
        check(z[(i - 1) % m] == 0 and z[(i + 1) % m] == 0,
              ("top peak lacks zero collar", word, i))
    split = tuple(frozen[i] + positive_difference(residual)[i]
                  for i in range(m))
    check(positive_difference(z) == split, ("one-step split", word))
    for time in range(h + 2):
        expected = tuple(frozen[i] + iterate(residual, time)[i]
                         for i in range(m))
        check(iterate(z, time) == expected,
              ("iterated frozen split", word, time))


def exponent_box(a, m):
    fibres = Counter()
    maximum_tail = 0
    fixed = 0
    words = tuple(exponent_words(a, m))
    for word in words:
        target = positive_difference(word)
        fibres[target] += 1
        frozen_peak_attack(word)
        time = tail(word)
        maximum_tail = max(maximum_tail, time)
        check(time <= max(word, default=0), ("pointwise height bound", word))
        support_fixed = all(word[i] == 0 or word[(i + 1) % m] == 0
                            for i in range(m))
        check((target == word) == support_fixed,
              ("fixed support criterion", word))
        fixed += int(target == word)

    expected_height = 0 if a == 0 else (1 if m <= 2 else a)
    check(maximum_tail == expected_height, ("sharp height", a, m))
    if a > 0 and m >= 3:
        witness = (0,) * (m - 2) + (a, 1)
        check(tail(witness) == a, ("sharp witness", a, m))

    predicted_mass = 0
    for target in words:
        edge_count = closed_edge_walk_count(a, target)
        trace_count = manuscript_trace(a, target)
        check(edge_count == fibres[target],
              ("oriented edge-walk fibre", a, m, target))
        check(trace_count == edge_count,
              ("matrix orientation/trace", a, m, target))
        predicted_mass += trace_count
    check(predicted_mass == (a + 1) ** m, ("primewise mass", a, m))
    check(sum(fibres.values()) == (a + 1) ** m,
          ("literal primewise mass", a, m))

    weighted = cyclic_support_weight(a, m)
    check(fixed == weighted, ("weighted cyclic polynomial", a, m))
    if m == 1:
        check(weighted == 1, ("I1 convention", a))
    if m == 2:
        check(weighted == 1 + 2 * a, ("I2 convention", a))
    if m >= 2:
        check(weighted == cyclic_polynomial_closed(a, m),
              ("closed cyclic polynomial", a, m))
    if m >= 3:
        check(weighted == cyclic_support_weight(a, m - 1)
              + a * cyclic_support_weight(a, m - 2),
              ("cyclic polynomial recurrence", a, m))
    return len(words), maximum_tail, fixed, len(fibres)


def local_and_short_boundary_attack():
    for a in range(0, 7):
        q = a + 1
        for left in range(q):
            for right in range(q):
                hits = 0
                for output in range(q):
                    entry = local_matrix(a, output)[left][right]
                    check(entry == int(max(left - right, 0) == output),
                          ("row/column orientation", a, left, right, output))
                    hits += entry
                check(hits == 1, ("sum L_b equals J", a, left, right))
        for b0 in range(q):
            for b1 in range(q):
                actual = closed_edge_walk_count(a, (b0, b1))
                if b0 == b1 == 0:
                    expected = a + 1
                elif b0 > 0 and b1 == 0:
                    expected = a - b0 + 1
                elif b1 > 0 and b0 == 0:
                    expected = a - b1 + 1
                else:
                    expected = 0
                check(actual == expected, ("m=2 fibre", a, b0, b1))
        check(closed_edge_walk_count(a, (0,)) == a + 1,
              ("m=1 zero fibre", a))
        for b in range(1, q):
            check(closed_edge_walk_count(a, (b,)) == 0,
                  ("m=1 positive fibre", a, b))

    check(matrix_product(local_matrix(1, 0), local_matrix(1, 1)) !=
          matrix_product(local_matrix(1, 1), local_matrix(1, 0)),
          "local transfer matrices really are order-sensitive")


def factor(n):
    factors = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            exponent = 0
            while n % p == 0:
                n //= p
                exponent += 1
            factors.append((p, exponent))
        p += 1
    if n > 1:
        factors.append((n, 1))
    return tuple(factors)


def divisors(n):
    values = [1]
    for p, a in factor(n):
        values = [old * p ** e for old in values for e in range(a + 1)]
    return tuple(sorted(values))


def valuation(value, p):
    exponent = 0
    while value % p == 0:
        value //= p
        exponent += 1
    return exponent


def divisor_update(word):
    m = len(word)
    return tuple(word[i] // gcd(word[i], word[(i + 1) % m])
                 for i in range(m))


def divisor_tail(word):
    time = 0
    seen = set()
    while divisor_update(word) != word:
        check(word not in seen, ("composite nonfixed cycle", word))
        seen.add(word)
        word = divisor_update(word)
        time += 1
        check(time < 20, ("composite orbit guard", word))
    return time


def composite_box(n, m):
    alphabet = divisors(n)
    states = tuple(product(alphabet, repeat=m))
    fibres = Counter(divisor_update(word) for word in states)
    fixed = 0
    maximum_tail = 0
    factors = factor(n)
    for word in states:
        image = divisor_update(word)
        time = divisor_tail(word)
        maximum_tail = max(maximum_tail, time)
        fixed += int(time == 0)
        for p, _a in factors:
            source_plane = tuple(valuation(value, p) for value in word)
            image_plane = tuple(valuation(value, p) for value in image)
            check(image_plane == positive_difference(source_plane),
                  ("valuation conjugacy", n, m, p, word))

    if n == 1:
        expected_height = 0
    elif m <= 2:
        expected_height = 1
    else:
        expected_height = max(a for _p, a in factors)
    check(maximum_tail == expected_height, ("composite height", n, m))
    expected_fixed = 1
    for _p, a in factors:
        expected_fixed *= cyclic_support_weight(a, m)
    check(fixed == expected_fixed, ("composite fixed census", n, m))

    predicted_mass = 0
    for target in states:
        predicted = 1
        for p, a in factors:
            target_plane = tuple(valuation(value, p) for value in target)
            predicted *= closed_edge_walk_count(a, target_plane)
        check(predicted == fibres[target],
              ("prime-product every-target fibre", n, m, target))
        predicted_mass += predicted
    check(predicted_mass == len(states), ("composite mass", n, m))
    return len(states), maximum_tail, fixed, len(fibres)


def main():
    bind_inputs()
    local_and_short_boundary_attack()

    exponent_signatures = []
    exponent_states = 0
    for a in range(0, 6):
        for m in range(1, 7):
            signature = exponent_box(a, m)
            exponent_signatures.append((a, m) + signature)
            exponent_states += signature[0]

    composite_signatures = []
    composite_states = 0
    for n in (1, 8, 12, 20, 72):
        for m in range(1, 5):
            signature = composite_box(n, m)
            composite_signatures.append((n, m) + signature)
            composite_states += signature[0]

    print("P187_HOSTILE_REVIEW_A_EXACT_CONTROL")
    print("REPRESENTATION=packed_base_q_words_and_oriented_closed_edge_walks")
    print(f"PINNED_INPUTS={len(INPUTS)}")
    print(f"EXPONENT_BOXES={len(exponent_signatures)} "
          f"STATES={exponent_states} LAST={exponent_signatures[-1]}")
    print(f"COMPOSITE_BOXES={len(composite_signatures)} "
          f"STATES={composite_states} LAST={composite_signatures[-1]}")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("CRITICAL_FINDINGS=0")
    print("MAJOR_FINDINGS=0")
    print("MINOR_FINDINGS=0")
    print("VERDICT=PROVABLE_AS_STATED")
    print("FINITE_CONTROL_IS_NOT_PROOF_OR_NOVELTY=true")
    print("STATUS=HOLD_EXTERNAL")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
