#!/usr/bin/env python3
"""Independent exact verifier for the hostile gate on random alphabet erasure.

This file deliberately imports nothing from the scouting implementation.  All
counts are integers (or exact Fractions for expectations), and every finite box
includes unreachable targets rather than only targets observed in simulation.
"""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations, product
from math import comb, factorial


ASSERTIONS = 0


def check(statement, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not statement:
        raise AssertionError(message)


@lru_cache(None)
def stirling2(n, k):
    if n == 0:
        return int(k == 0)
    if k == 0:
        return 0
    return k * stirling2(n - 1, k) + stirling2(n - 1, k - 1)


def falling(q, s):
    out = 1
    for j in range(s):
        out *= q - j
    return out


@lru_cache(None)
def words_exact(q, n):
    return tuple(product(range(q), repeat=n))


@lru_cache(None)
def words_upto(q, cap):
    return tuple(w for n in range(cap + 1) for w in words_exact(q, n))


def erase(word, letter):
    return tuple(x for x in word if x != letter)


def apply_history(word, history):
    out = word
    for letter in history:
        out = erase(out, letter)
    return out


def project(word, keep):
    return tuple(x for x in word if x in keep)


def kernel_formula(q, t, source, target):
    bset = set(target)
    uset = set(source)
    if not bset.issubset(uset) or project(source, bset) != target:
        return 0
    d = len(uset - bset)
    b = len(bset)
    return sum((-1) ** j * comb(d, j) * (q - b - j) ** t
               for j in range(d + 1))


def fibre_formula(q, t, n, target):
    m = len(target)
    if n < m:
        return 0
    b = len(set(target))
    return comb(n, m) * sum(
        falling(q - b, s) * stirling2(t, s) * s ** (n - m)
        for s in range(min(q - b, t) + 1)
    )


def mat_identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def mat_mul(a, b):
    rows, mid, cols = len(a), len(b), len(b[0])
    return [[sum(a[i][k] * b[k][j] for k in range(mid))
             for j in range(cols)] for i in range(rows)]


def mat_shift(a, scalar):
    return [[a[i][j] - scalar * int(i == j) for j in range(len(a))]
            for i in range(len(a))]


def verify_semigroup_and_history():
    boxes = ((2, 5, 5), (3, 4, 4), (4, 3, 3))
    for q, cap, tmax in boxes:
        alphabet = set(range(q))
        for word in words_upto(q, cap):
            for a in range(q):
                check(erase(erase(word, a), a) == erase(word, a),
                      "idempotence")
                for b in range(q):
                    check(erase(erase(word, a), b) ==
                          erase(erase(word, b), a), "commutation")
            for t in range(tmax + 1):
                for history in product(range(q), repeat=t):
                    check(apply_history(word, history) ==
                          project(word, alphabet - set(history)),
                          "history projection")
    return len(boxes)


def verify_every_source_every_target_kernel():
    boxes = ((2, 5, 5), (3, 4, 4), (4, 3, 3))
    zero_cells = 0
    positive_cells = 0
    for q, cap, tmax in boxes:
        for source in words_upto(q, cap):
            candidates = words_upto(q, len(source) + 1)
            for t in range(tmax + 1):
                observed = Counter(apply_history(source, h)
                                   for h in product(range(q), repeat=t))
                for target in candidates:
                    expected = kernel_formula(q, t, source, target)
                    check(observed[target] == expected, "transition kernel")
                    if expected:
                        positive_cells += 1
                    else:
                        zero_cells += 1
                check(sum(observed.values()) == q ** t, "kernel mass")
    check(zero_cells > positive_cells > 0, "zero-cell coverage")
    return len(boxes), zero_cells, positive_cells


def verify_absorption_and_last_survivor():
    # Literal finite-time CDF, including b=0, against inclusion-exclusion.
    cdf_boxes = 0
    for q in range(2, 7):
        for b in range(q + 1):
            wanted = set(range(b))
            for t in range(6):
                literal = sum(wanted.issubset(set(h))
                              for h in product(range(q), repeat=t))
                formula = sum((-1) ** j * comb(b, j) * (q - j) ** t
                              for j in range(b + 1))
                check(literal == formula, "coupon CDF")
                cdf_boxes += 1

            # An independent first-step recurrence, not a second spelling of
            # the harmonic sum.
            e = Fraction(0)
            for remaining in range(1, b + 1):
                next_e = (Fraction(q, remaining) + e)
                check(Fraction(remaining, q) * next_e ==
                      1 + Fraction(remaining, q) * e,
                      "first-step hitting recursion")
                e = next_e
            check(e == q * sum((Fraction(1, j) for j in range(1, b + 1)),
                               Fraction(0)), "coupon mean")

            # The relative first-occurrence order of the b relevant letters
            # is a uniform permutation; this directly checks the last coupon.
            if b:
                last = Counter(p[-1] for p in permutations(range(b)))
                for a in range(b):
                    check(last[a] == factorial(b - 1), "last survivor")
    return cdf_boxes


def verify_history_support_and_operator_images():
    boxes = 0
    image_collisions = 0
    for q in range(2, 5):
        for cap in range(5):
            carrier = words_upto(q, cap)
            for t in range(5):
                support_hist = Counter()
                image_hist = Counter()
                for history in product(range(q), repeat=t):
                    s = len(set(history))
                    support_hist[s] += 1
                    outputs = {apply_history(w, history) for w in carrier}
                    image_size = len(outputs)
                    predicted = sum((q - s) ** m for m in range(cap + 1))
                    check(image_size == predicted, "operator image size")
                    image_hist[image_size] += 1
                predicted_hist = Counter()
                for s in range(min(q, t) + 1):
                    count = falling(q, s) * stirling2(t, s)
                    check(support_hist[s] == count, "history support law")
                    size = sum((q - s) ** m for m in range(cap + 1))
                    predicted_hist[size] += count
                check(image_hist == predicted_hist, "image pushforward law")
                if cap == 0 and len(support_hist) > 1:
                    check(len(image_hist) == 1, "L=0 image-size collision")
                    image_collisions += 1
                boxes += 1
    check(image_collisions > 0, "boundary aggregation exercised")
    return boxes, image_collisions


def verify_all_source_every_target_fibres():
    boxes = ((2, 6, 5), (3, 5, 4), (4, 5, 3))
    cells = 0
    zero_cells = 0
    for q, nmax, tmax in boxes:
        for n in range(nmax + 1):
            sources = words_exact(q, n)
            candidates = words_upto(q, n + 1)  # also exercise n < |v|.
            for t in range(tmax + 1):
                observed = Counter()
                for source in sources:
                    for history in product(range(q), repeat=t):
                        observed[apply_history(source, history)] += 1
                for target in candidates:
                    expected = fibre_formula(q, t, n, target)
                    check(observed[target] == expected, "all-source fibre")
                    cells += 1
                    zero_cells += int(expected == 0)
                check(sum(observed.values()) == q ** (n + t),
                      "global source-history mass")
    check(zero_cells > 0, "zero fibre coverage")

    # Directly expose the dependence of the advertised second axis on the
    # first: it is the source-layer column sum of the transition kernel.
    column_cells = 0
    for q in (2, 3):
        for n in range(5):
            sources = words_exact(q, n)
            for t in range(4):
                for target in words_upto(q, n + 1):
                    column = sum(kernel_formula(q, t, source, target)
                                 for source in sources)
                    check(column == fibre_formula(q, t, n, target),
                          "fibre is kernel column sum")
                    column_cells += 1
    return len(boxes), cells, zero_cells, column_cells


def verify_insertion_ogf_and_target_classes():
    coefficient_cells = 0
    target_class_cells = 0
    for q in range(2, 6):
        for m in range(6):
            actual_supports = Counter(len(set(w)) for w in words_exact(q, m))
            for b in range(min(q, m) + 1):
                expected = falling(q, b) * stirling2(m, b)
                check(actual_supports[b] == expected, "target support class")
                target_class_cells += 1

            for target in words_exact(q, m):
                b = len(set(target))
                for t in range(5):
                    # Coefficient of z^n in z^m sum_s c_s/(1-sz)^(m+1).
                    for n in range(m, m + 7):
                        coeff = sum(
                            falling(q - b, s) * stirling2(t, s) *
                            comb(n, m) * s ** (n - m)
                            for s in range(min(q - b, t) + 1)
                        )
                        check(coeff == fibre_formula(q, t, n, target),
                              "insertion OGF coefficient")
                        coefficient_cells += 1
    return coefficient_cells, target_class_cells


def verify_capped_operator_spectrum():
    boxes = ((2, 4), (3, 3), (4, 2))
    dimensions = []
    for q, cap in boxes:
        carrier = words_upto(q, cap)
        index = {w: i for i, w in enumerate(carrier)}
        dim = len(carrier)
        cmat = [[0] * dim for _ in range(dim)]
        for i, word in enumerate(carrier):
            for a in range(q):
                cmat[i][index[erase(word, a)]] += 1

        # Ordering by length makes C lower triangular.  Its diagonal and the
        # support census therefore give the algebraic multiplicities.
        for i, word in enumerate(carrier):
            check(cmat[i][i] == q - len(set(word)), "spectral diagonal")
            for j in range(i + 1, dim):
                check(cmat[i][j] == 0, "triangularity")
        for b in range(min(q, cap) + 1):
            actual = sum(len(set(w)) == b for w in carrier)
            expected = sum(falling(q, b) * stirling2(n, b)
                           for n in range(b, cap + 1))
            check(actual == expected, "spectral multiplicity")

        # Commuting idempotents make the average diagonalizable; the squarefree
        # annihilating polynomial is checked directly over the integers.
        polynomial = mat_identity(dim)
        for b in range(min(q, cap) + 1):
            polynomial = mat_mul(polynomial, mat_shift(cmat, q - b))
        for row in polynomial:
            for entry in row:
                check(entry == 0, "squarefree spectral annihilator")
        dimensions.append(dim)
    return dimensions


def main():
    semigroup_boxes = verify_semigroup_and_history()
    kernel_boxes, kernel_zero, kernel_positive = (
        verify_every_source_every_target_kernel())
    absorption_cells = verify_absorption_and_last_survivor()
    operator_boxes, lzero_collisions = (
        verify_history_support_and_operator_images())
    fibre_boxes, fibre_cells, fibre_zero, column_cells = (
        verify_all_source_every_target_fibres())
    ogf_cells, target_class_cells = verify_insertion_ogf_and_target_classes()
    spectral_dimensions = verify_capped_operator_spectrum()

    print("RAE_HOSTILE_GATE_INDEPENDENT_V1")
    print("author_sha256_scout=f3008b01c98604ab24f185c38bb729e798d6a93321e0b45282774242f244d365")
    print("author_sha256_owner=371e9173f9ab762763559e073fd5b30ad23f04463bc97b5d984266a7c98f0487")
    print("author_sha256_verifier=c44ae347a25262870af4ba3b9b32f1cd8e9217517dd218c48fb2be7851487f8b")
    print("author_sha256_canonical=a974af3288ee2fc5b830ad34511355ee20c299667116fc316643c2d9856ed459")
    print(f"semigroup_boxes={semigroup_boxes}; kernel_boxes={kernel_boxes}; "
          f"kernel_zero_cells={kernel_zero}; kernel_positive_cells={kernel_positive}")
    print(f"absorption_cells={absorption_cells}; operator_boxes={operator_boxes}; "
          f"L0_image_collisions={lzero_collisions}")
    print(f"fibre_boxes={fibre_boxes}; fibre_cells={fibre_cells}; "
          f"fibre_zero_cells={fibre_zero}; column_sum_cells={column_cells}")
    print(f"ogf_coefficient_cells={ogf_cells}; target_class_cells={target_class_cells}")
    print("spectral_dimensions=" + ",".join(map(str, spectral_dimensions)))
    print(f"assertions={ASSERTIONS}")
    print("MATHEMATICS PASS")
    print("INDEPENDENT_AXIS FAIL_COLUMN_SUM_AND_SEMILATTICE_SUBTRACTION")
    print("DECISION KILL")
    print("EXTERNAL HOLD_EXTERNAL")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
