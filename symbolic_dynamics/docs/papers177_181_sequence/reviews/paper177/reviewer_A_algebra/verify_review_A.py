#!/usr/bin/env python3
"""Independent hostile checks for P177.

This reviewer implementation uses tuples of field coordinates and incidence
words.  It imports no author or scouting module.  Ordered form words are
expanded literally, while the spectrum is checked by a separate Walsh sum
over every Boolean character in the declared boxes.
"""

from collections import Counter
from fractions import Fraction
from itertools import product


class Audit:
    def __init__(self):
        self.assertions = 0

    def equal(self, left, right, label=""):
        self.assertions += 1
        if left != right:
            raise AssertionError(f"{label}: {left!r} != {right!r}")

    def true(self, value, label=""):
        self.assertions += 1
        if not value:
            raise AssertionError(label or "assertion failed")


def vectors(d):
    return tuple(product((0, 1), repeat=d))


def add(left, right):
    return tuple(a ^ b for a, b in zip(left, right))


def add_many(words, width):
    total = (0,) * width
    for word in words:
        total = add(total, word)
    return total


def dot(left, right):
    return sum(a * b for a, b in zip(left, right)) & 1


def evaluation(form, points):
    return tuple(dot(form, point) for point in points)


def hyperplane_mask(form, points):
    return tuple(1 ^ dot(form, point) for point in points)


def history_formula(q, t, form_sum_is_zero):
    n = q - 1
    numerator = n**t + n * ((-1) ** t) if form_sum_is_zero else n**t - ((-1) ** t)
    if numerator % q:
        raise AssertionError("nonintegral history formula")
    return numerator // q


def sum_field_vectors(items, d):
    return add_many(items, d)


def all_histories(forms, d, t):
    counts = Counter()
    increments = Counter()
    points = tuple(v for v in vectors(d) if any(v))
    masks = {ell: hyperplane_mask(ell, points) for ell in forms}
    for history in product(forms, repeat=t):
        total_form = sum_field_vectors(history, d)
        total_mask = add_many((masks[ell] for ell in history), len(points))
        counts[total_form] += 1
        increments[(total_form, total_mask)] += 1
    return counts, increments


def tv(dist, uniform):
    keys = set(dist) | set(uniform)
    return sum(abs(dist.get(k, Fraction(0)) - uniform.get(k, Fraction(0))) for k in keys) / 2


def main():
    audit = Audit()
    rows = []

    # The excluded d=1 map is literally the identity because its only mask is empty.
    d = 1
    pts = tuple(v for v in vectors(d) if any(v))
    ell = pts[0]
    empty_mask = hyperplane_mask(ell, pts)
    audit.equal(empty_mask, (0,), "d=1 mask")
    for state in product((0, 1), repeat=1):
        audit.equal(add(state, empty_mask), state, "d=1 identity")

    for d in (2, 3, 4):
        all_v = vectors(d)
        forms = tuple(v for v in all_v if any(v))
        points = forms
        q = 2**d
        n = q - 1
        m = n
        zero_word = (0,) * m
        one_word = (1,) * m
        code = {a: evaluation(a, points) for a in all_v}
        masks = {ell: hyperplane_mask(ell, points) for ell in forms}
        w_coordinates = {
            add((epsilon,) * m, code[a])
            for epsilon in (0, 1)
            for a in all_v
        }

        audit.equal(len(set(code.values())), q, f"code injective d={d}")
        audit.true(one_word not in set(code.values()), f"one outside code d={d}")
        audit.equal(len(w_coordinates), 2 * q, f"augmented code size d={d}")
        for ell in forms:
            audit.equal(masks[ell], add(one_word, code[ell]), f"mask identity d={d}")

        # Generate the increment subgroup by breadth-first closure, independently
        # of the displayed coordinate parametrization.
        generated = {zero_word}
        frontier = [zero_word]
        while frontier:
            current = frontier.pop()
            for mask in masks.values():
                nxt = add(current, mask)
                if nxt not in generated:
                    generated.add(nxt)
                    frontier.append(nxt)
        audit.equal(generated, w_coordinates, f"generated subgroup d={d}")

        # Literal carrier cosets and class sizes.  Tuple minimization supplies a
        # canonical representative without using the author's bit-mask model.
        cosets = Counter()
        for state in product((0, 1), repeat=m):
            representative = min(add(state, word) for word in generated)
            cosets[representative] += 1
        expected_k = 2 ** (m - d - 1)
        audit.equal(len(cosets), expected_k, f"component count d={d}")
        for size in cosets.values():
            audit.equal(size, 2 * q, f"component size d={d}")

        # Coordinate neighborhoods are exactly all opposite-side vertices except
        # the matched one; every move reverses parity and repeating it returns.
        for epsilon in (0, 1):
            for a in all_v:
                state = add((epsilon,) * m, code[a])
                observed = set()
                for ell in forms:
                    neighbor = add(state, masks[ell])
                    expected = add(((epsilon ^ 1),) * m, code[add(a, ell)])
                    audit.equal(neighbor, expected, f"crown coordinate d={d}")
                    audit.equal(sum(neighbor) & 1, (sum(state) ^ 1) & 1,
                                f"parity flip d={d}")
                    audit.equal(add(neighbor, masks[ell]), state, f"two-step return d={d}")
                    observed.add(neighbor)
                forbidden = add(((epsilon ^ 1),) * m, code[a])
                audit.equal(len(observed), n, f"crown degree d={d}")
                audit.true(forbidden not in observed, f"deleted matching d={d}")

        # Literal ordered histories, not a recurrence or imported convolution.
        t_max = {2: 7, 3: 5, 4: 4}[d]
        for t in range(t_max + 1):
            counts, paired = all_histories(forms, d, t)
            audit.equal(sum(counts.values()), n**t, f"history mass d={d},t={t}")
            for L in all_v:
                audit.equal(counts[L], history_formula(q, t, not any(L)),
                            f"history formula d={d},t={t},L={L}")
            for (L, increment), multiplicity in paired.items():
                expected_increment = add(((t & 1),) * m, code[L])
                audit.equal(increment, expected_increment,
                            f"endpoint increment d={d},t={t}")
                audit.true(multiplicity > 0, "recorded history has positive count")

        # Both TV metrics are recomputed from rational point masses.
        for t in range(1, 11):
            phase_dist = {
                L: Fraction(history_formula(q, t, not any(L)), n**t)
                for L in all_v
            }
            phase_uniform = {L: Fraction(1, q) for L in all_v}
            phase_value = tv(phase_dist, phase_uniform)
            audit.equal(phase_value, Fraction(1, q * n ** (t - 1)),
                        f"phase TV d={d},t={t}")

            full_dist = {(0, L): probability for L, probability in phase_dist.items()}
            full_uniform = {
                (side, L): Fraction(1, 2 * q)
                for side in (0, 1)
                for L in all_v
            }
            ordinary = tv(full_dist, full_uniform)
            expected_ordinary = Fraction(1, 2) + (Fraction(1, 2 * q) if t == 1 else 0)
            audit.equal(ordinary, expected_ordinary, f"ordinary TV d={d},t={t}")

        # Full-carrier Walsh eigenvalues and multiplicities.  This visits every
        # character but never constructs or diagonalizes the author's matrix.
        spectrum = Counter()
        rank_fibres = Counter()
        for subset_word in product((0, 1), repeat=m):
            parity = sum(subset_word) & 1
            selected = [point for bit, point in zip(subset_word, points) if bit]
            sigma = add_many(selected, d)
            numerator = sum(
                -1 if (sum(bit * h for bit, h in zip(subset_word, masks[ell])) & 1) else 1
                for ell in forms
            )
            eigenvalue = Fraction(numerator, n)
            expected_eigenvalue = (
                Fraction((-1) ** parity, 1)
                if not any(sigma)
                else Fraction((-1) ** (parity + 1), n)
            )
            audit.equal(eigenvalue, expected_eigenvalue, f"Walsh eigenvalue d={d}")
            spectrum[eigenvalue] += 1
            rank_fibres[(parity, sigma)] += 1

        k = expected_k
        expected_spectrum = Counter({Fraction(1): k, Fraction(-1): k,
                                     Fraction(1, n): n * k, Fraction(-1, n): n * k})
        audit.equal(spectrum, expected_spectrum, f"global spectrum d={d}")
        audit.equal(sum(spectrum.values()), 2**m, f"spectral mass d={d}")
        audit.equal(len(rank_fibres), 2 * q, f"rank-map surjectivity d={d}")
        for size in rank_fibres.values():
            audit.equal(size, k, f"rank-map fibre d={d}")

        rows.append((d, q, n, expected_k, t_max, tuple(sorted((str(x), y) for x, y in spectrum.items()))))

    # Hostile support sentinels: these refute the old bare endpoint condition
    # and confirm that the repaired manuscript's t=0/t=1 guards are necessary.
    d = 2
    all_v = vectors(d)
    nonzero = next(v for v in all_v if any(v))
    q = 2**d
    audit.equal(history_formula(q, 0, False), 0, "t=0 nonzero-sum sentinel")
    audit.equal(history_formula(q, 1, True), 0, "t=1 zero-sum sentinel")

    print("P177_REVIEW_A_TUPLE_WALSH_AUDIT")
    for d, q, n, k, t_max, spectrum in rows:
        print(f"d={d} q={q} N={n} components={k} literal_history_t_max={t_max} spectrum={spectrum}")
    print("BOUNDARY_D1=IDENTITY_PASS")
    print("TV_PHASE_AND_ORDINARY=PASS;t=1..10")
    print("SUPPORT_COUNTEREXAMPLES=t0_nonzero_L_and_t1_zero_L_have_endpoint_form_but_zero_histories")
    print(f"ASSERTIONS={audit.assertions}")
    print("RESULT=PASS_WITH_REPAIRED_SUPPORT_BOUNDARIES_CONFIRMED")
    print("EXTERNAL_STATUS=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
