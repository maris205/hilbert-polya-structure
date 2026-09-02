#!/usr/bin/env python3
"""Independent hostile verifier B for P162.

The implementation starts from the literal subset update.  It imports no
paper-local or Review-A module, reads no precomputed transcript, and uses only
exact integers, Fractions, and exhaustive finite enumeration.
"""

from collections import Counter, defaultdict, deque
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb
from hashlib import sha256
from pathlib import Path


ASSERTIONS = 0


def check(condition, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def file_digest(path):
    digest = sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def check_frozen_artifacts():
    root = Path(__file__).resolve().parents[4]
    paper = root / "papers" / "162-random-translation-intersection"
    expected = {
        "main.tex": "98b54a3052dccb6168655e8f337921eef76547c73005d847338eb69fd5454e1d",
        "main.pdf": "730c4a57cb1c3f787c0cc8b142d4dbf62da4d2b06bc1c42d5c30d00eb8e20b62",
        "main_round1.pdf": "730c4a57cb1c3f787c0cc8b142d4dbf62da4d2b06bc1c42d5c30d00eb8e20b62",
        "main_round0_original.pdf": "e496ce1be3084e61616494cab2ca405238adfa575a6484db93029f8dae01de46",
    }
    for name, digest in expected.items():
        check(file_digest(paper / name) == digest, f"frozen hash {name}")
    source = (paper / "main.tex").read_text(encoding="utf-8")
    abstract = source.split("\\begin{abstract}", 1)[1].split("\\end{abstract}", 1)[0]
    check("sharp worst-non-full-source emptying clock" in abstract,
          "Review-A abstract repair present")
    check("sharp worst-source" not in abstract,
          "Review-A defective abstract phrase absent")
    print("ARTIFACTS Round0/Round1/Review-A-minor PASS")


def universe_size(d):
    return 1 << d


def full_subset(d):
    return (1 << universe_size(d)) - 1


@lru_cache(maxsize=None)
def translate_subset(a_mask, vector, d):
    out = 0
    rest = a_mask
    while rest:
        bit = rest & -rest
        point = bit.bit_length() - 1
        out |= 1 << (point ^ vector)
        rest ^= bit
    return out


def literal_update(a_mask, vector, d):
    return a_mask & translate_subset(a_mask, vector, d)


def literal_history(a_mask, history, d):
    state = a_mask
    for vector in history:
        state = literal_update(state, vector, d)
    return state


def span_point_mask(vectors):
    """Bit mask of the points in the F_2-span of vectors."""
    points = {0}
    for vector in vectors:
        if vector not in points:
            points |= {point ^ vector for point in tuple(points)}
    return sum(1 << point for point in points)


def subspace_dimension(h_mask):
    size = h_mask.bit_count()
    check(size > 0 and size & (size - 1) == 0, "subspace cardinality power")
    return size.bit_length() - 1


def erosion(a_mask, h_mask, d):
    out = full_subset(d)
    rest = h_mask
    while rest:
        bit = rest & -rest
        vector = bit.bit_length() - 1
        out &= translate_subset(a_mask, vector, d)
        rest ^= bit
    return out


@lru_cache(maxsize=None)
def all_subspaces(d):
    """Generate all subspaces as point masks by adjoining one vector."""
    zero = 1
    seen = {zero}
    queue = deque([zero])
    n = universe_size(d)
    while queue:
        h_mask = queue.popleft()
        for vector in range(n):
            if (h_mask >> vector) & 1:
                continue
            enlarged = h_mask | translate_subset(h_mask, vector, d)
            if enlarged not in seen:
                seen.add(enlarged)
                queue.append(enlarged)
    return tuple(sorted(seen, key=lambda mask: (mask.bit_count(), mask)))


@lru_cache(maxsize=None)
def stabilizer_mask(b_mask, d):
    return sum(
        1 << vector
        for vector in range(universe_size(d))
        if translate_subset(b_mask, vector, d) == b_mask
    )


def gaussian_binomial(m, r):
    if r < 0 or r > m:
        return 0
    r = min(r, m - r)
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator *= (1 << (m - i)) - 1
        denominator *= (1 << (r - i)) - 1
    check(numerator % denominator == 0, "Gaussian binomial integrality")
    return numerator // denominator


def onto_history_count(t, r):
    if r < 0 or r > t:
        return 0
    value = 1
    for i in range(r):
        value *= (1 << t) - (1 << i)
    return value


def polynomial_multiply(left, right, cap):
    out = [0] * (min(cap, len(left) + len(right) - 2) + 1)
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right):
            if i + j > cap:
                break
            if b:
                out[i + j] += a * b
    return out


def polynomial_power(base, exponent, cap):
    out = [1]
    factor = list(base)
    power = exponent
    while power:
        if power & 1:
            out = polynomial_multiply(out, factor, cap)
        power >>= 1
        if power:
            factor = polynomial_multiply(factor, factor, cap)
    return out


def shifted_polynomial(poly, shift, cap):
    out = [0] * (cap + 1)
    for degree, coefficient in enumerate(poly):
        if degree + shift <= cap:
            out[degree + shift] = coefficient
    return out


def fixed_span_formula(b_mask, h_mask, d):
    """Coefficient vector for sources A with E_H(A)=B."""
    n = universe_size(d)
    stab = stabilizer_mask(b_mask, d)
    if h_mask & ~stab:
        return [0] * (n + 1)
    coset_size = h_mask.bit_count()
    b = b_mask.bit_count()
    check(b % coset_size == 0, "stable target is union of H-cosets")
    outside = n // coset_size - b // coset_size
    proper_subset_poly = [comb(coset_size, k) for k in range(coset_size)]
    return shifted_polynomial(
        polynomial_power(proper_subset_poly, outside, n), b, n
    )


def every_history_formula(b_mask, d, t):
    n = universe_size(d)
    b = b_mask.bit_count()
    stab = stabilizer_mask(b_mask, d)
    s = subspace_dimension(stab)
    answer = [0] * (n + 1)
    for r in range(s + 1):
        history_factor = gaussian_binomial(s, r) * onto_history_count(t, r)
        if not history_factor:
            continue
        coset_size = 1 << r
        check(b % coset_size == 0, "stabilizer divisibility")
        outside = n // coset_size - b // coset_size
        base = [comb(coset_size, k) for k in range(coset_size)]
        term = shifted_polynomial(polynomial_power(base, outside, n), b, n)
        for degree, coefficient in enumerate(term):
            answer[degree] += history_factor * coefficient
    return answer


def check_subspaces_and_clock():
    known_counts = {0: 1, 1: 2, 2: 5, 3: 16, 4: 67, 5: 374, 6: 2825}
    print("SUBSPACES d/count/witness-sharp")
    for d in range(7):
        spaces = all_subspaces(d)
        check(len(spaces) == known_counts[d], f"subspace count d={d}")
        n = universe_size(d)
        whole = full_subset(d)
        witness = whole ^ 1  # V minus the zero point
        for h_mask in spaces:
            observed = erosion(witness, h_mask, d)
            expected = whole ^ h_mask
            check(observed == expected, f"sharp witness d={d}, H={h_mask}")
            check((observed == 0) == (h_mask == whole),
                  f"witness full-span iff d={d}, H={h_mask}")
        print("SUBSPACES", d, len(spaces), "PASS")

    print("FIXED d/state-count")
    for d in range(5):
        n = universe_size(d)
        whole = full_subset(d)
        fixed = []
        for a_mask in range(1 << n):
            universal = all(
                literal_update(a_mask, vector, d) == a_mask
                for vector in range(n)
            )
            if universal:
                fixed.append(a_mask)
            if a_mask != whole:
                check(erosion(a_mask, whole, d) == 0,
                      f"full span empties nonfull source d={d}, A={a_mask}")
        check(fixed == [0, whole], f"two fixed states d={d}")
        print("FIXED", d, len(fixed))


def check_rank_law_and_mean():
    print("RANK_ENUM d/t/history-count/full-rank-count")
    enum_boxes = []
    for d in range(4):
        enum_boxes.extend((d, t) for t in range(7))
    enum_boxes.extend((4, t) for t in range(5))
    printed = {(0, 0), (2, 1), (3, 3), (3, 6), (4, 4)}
    for d, t in enum_boxes:
        n = universe_size(d)
        histogram = Counter()
        for history in product(range(n), repeat=t):
            r = subspace_dimension(span_point_mask(history))
            histogram[r] += 1
        for r in range(d + 1):
            expected = gaussian_binomial(d, r) * onto_history_count(t, r)
            check(histogram[r] == expected,
                  f"rank law d={d}, t={t}, r={r}")
        check(sum(histogram.values()) == n ** t,
              f"rank mass d={d}, t={t}")
        full = histogram[d]
        if t < d:
            check(full == 0, f"full-rank support hole d={d}, t={t}")
        else:
            product_count = 1
            for i in range(d):
                product_count *= (1 << t) - (1 << i)
            check(full == product_count, f"full-rank product d={d}, t={t}")
        if (d, t) in printed:
            print("RANK_ENUM", d, t, n ** t, full)

    # Formula normalization and endpoint support beyond brute-force boxes.
    for d in range(9):
        n = universe_size(d)
        for t in range(13):
            counts = [
                gaussian_binomial(d, r) * onto_history_count(t, r)
                for r in range(d + 1)
            ]
            check(sum(counts) == n ** t, f"symbolic rank mass d={d}, t={t}")
            check((counts[d] == 0) == (t < d),
                  f"sharp full-rank support d={d}, t={t}")

    print("MEAN d/exact")
    for d in range(9):
        displayed = sum(
            (Fraction(1, 1 - Fraction(1 << r, 1 << d))
             for r in range(d)),
            Fraction(0),
        )
        remaining = Fraction(0)
        for r in range(d - 1, -1, -1):
            p_grow = Fraction((1 << d) - (1 << r), 1 << d)
            remaining = Fraction(1, p_grow) + remaining
        check(displayed == remaining, f"mean rank clock d={d}")
        if d <= 5:
            print("MEAN", d, str(displayed))


def check_fixed_span_polynomials():
    print("FIXED_SPAN d/subspaces/targets")
    for d in range(4):
        n = universe_size(d)
        spaces = all_subspaces(d)
        actual = {}
        for h_mask in spaces:
            target_polys = [[0] * (n + 1) for _ in range(1 << n)]
            for a_mask in range(1 << n):
                target = erosion(a_mask, h_mask, d)
                target_polys[target][a_mask.bit_count()] += 1
                check(h_mask & ~stabilizer_mask(target, d) == 0,
                      f"fixed-span necessity d={d}, H={h_mask}, A={a_mask}")
            for target in range(1 << n):
                formula = fixed_span_formula(target, h_mask, d)
                check(target_polys[target] == formula,
                      f"fixed-span polynomial d={d}, H={h_mask}, B={target}")
        print("FIXED_SPAN", d, len(spaces), 1 << n)


def check_literal_atlas():
    print("LITERAL d/t/source-history-pairs/targets")
    boxes = []
    for d in range(3):
        boxes.extend((d, t) for t in range(5))
    boxes.extend((3, t) for t in range(5))
    for d, t in boxes:
        n = universe_size(d)
        targets = 1 << n
        actual = [[0] * (n + 1) for _ in range(targets)]
        rank_hist = Counter()
        for history in product(range(n), repeat=t):
            h_mask = span_point_mask(history)
            rank_hist[subspace_dimension(h_mask)] += 1
            for source in range(targets):
                literal = literal_history(source, history, d)
                compressed = erosion(source, h_mask, d)
                check(literal == compressed,
                      f"history-span identity d={d}, t={t}, A={source}, hist={history}")
                actual[literal][source.bit_count()] += 1
        for target in range(targets):
            formula = every_history_formula(target, d, t)
            check(actual[target] == formula,
                  f"every-target polynomial d={d}, t={t}, B={target}")
        check(sum(sum(poly) for poly in actual) == targets * n ** t,
              f"source-history mass d={d}, t={t}")
        if t == 0:
            check(all(poly[target.bit_count()] == 1 and sum(poly) == 1
                      for target, poly in enumerate(actual)),
                  f"time-zero singleton fibres d={d}")
        print("LITERAL", d, t, targets * n ** t, targets)


def check_one_step_and_recovery():
    print("ONE_STEP d/targets/trivial-stabilizers")
    phase_sizes = []
    for d in range(5):
        n = universe_size(d)
        targets = 1 << n
        phase_sizes.append(targets)
        actual = [0] * targets
        for vector in range(n):
            for source in range(targets):
                actual[literal_update(source, vector, d)] += 1

        by_size = defaultdict(dict)
        trivial = 0
        for target in range(targets):
            b = target.bit_count()
            stab = stabilizer_mask(target, d)
            s = subspace_dimension(stab)
            check(stab in all_subspaces(d), f"stabilizer is subspace d={d}, B={target}")
            if s == 0:
                expected = 1
                recovered = 0
                trivial += 1
            else:
                check(b % (1 << s) == 0,
                      f"target size stabilizer divisibility d={d}, B={target}")
                exponent = (n - b) // 2
                scale = 3 ** exponent
                expected = 1 + ((1 << s) - 1) * scale
                quotient, remainder = divmod(expected - 1, scale)
                check(remainder == 0 and (quotient + 1) & quotient == 0,
                      f"recovery integral d={d}, B={target}")
                recovered = (quotient + 1).bit_length() - 1
            check(actual[target] == expected,
                  f"one-step boundary d={d}, B={target}")
            check(recovered == s, f"stabilizer recovery d={d}, B={target}")
            previous = by_size[b].get(s)
            check(previous in (None, expected), f"mass depends only d,b,s d={d}")
            by_size[b][s] = expected

        for b, cells in by_size.items():
            ordered = sorted(cells.items())
            check(all(ordered[i][1] < ordered[i + 1][1]
                      for i in range(len(ordered) - 1)),
                  f"strict recovery order d={d}, b={b}")
        print("ONE_STEP", d, targets, trivial)

    check(len(set(phase_sizes)) == len(phase_sizes), "phase sizes recover d")
    for d, phase in enumerate(phase_sizes):
        log_phase = phase.bit_length() - 1
        check(1 << log_phase == phase, f"phase power d={d}")
        recovered_d = log_phase.bit_length() - 1
        check(1 << recovered_d == log_phase, f"double-log phase d={d}")
        check(recovered_d == d, f"phase recovery d={d}")


def check_named_boundaries():
    print("BOUNDARIES d/t/B/status")
    for d in range(6):
        n = universe_size(d)
        targets = 1 << n
        for t in range(7):
            empty_poly = every_history_formula(0, d, t)
            full_poly = every_history_formula(targets - 1, d, t)
            check(empty_poly[0] == n ** t,
                  f"empty source/history constant d={d}, t={t}")
            check(sum(full_poly) == n ** t,
                  f"full target total d={d}, t={t}")
            check(full_poly[n] == n ** t and sum(full_poly[:n]) == 0,
                  f"full target unique source d={d}, t={t}")

    for d in range(5):
        n = universe_size(d)
        for target in range(1 << n):
            poly = every_history_formula(target, d, 0)
            check(poly[target.bit_count()] == 1 and sum(poly) == 1,
                  f"t=0 identity d={d}, B={target}")

    # The zero-dimensional phase has one point, one history symbol, and two
    # fixed states.  Both targets have trivial (zero-dimensional) stabilizer.
    for t in range(9):
        check(every_history_formula(0, 0, t) == [1, 0], f"d=0 empty t={t}")
        check(every_history_formula(1, 0, t) == [0, 1], f"d=0 full t={t}")
    print("BOUNDARIES d=0 t=0..8 B=empty,V PASS")
    print("BOUNDARIES s=0/t=0/t=1/B=empty,V PASS")


def main():
    check_frozen_artifacts()
    check_subspaces_and_clock()
    check_rank_law_and_mean()
    check_fixed_span_polynomials()
    check_literal_atlas()
    check_one_step_and_recovery()
    check_named_boundaries()
    print(f"ASSERTIONS {ASSERTIONS}")
    print("THEOREM history/rank/clock/fibres/recovery PASS")
    print("FINDINGS 0_CRITICAL 0_MAJOR 0_MINOR")
    print("VERDICT ACCEPT_INTERNAL HOLD_EXTERNAL")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
