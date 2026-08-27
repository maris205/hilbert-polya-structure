#!/usr/bin/env python3
"""Exact rational controls for finite-word cylinders of a fixed 4-IET."""

from fractions import Fraction
from itertools import product


PERMUTATION = (3, 2, 1, 0)  # reverse permutation, labels 0,1,2,3
ZERO_FORM = (0, 0, 0, 0)


def add_forms(left, right):
    return tuple(a + b for a, b in zip(left, right))


def subtract_forms(left, right):
    return tuple(a - b for a, b in zip(left, right))


def scale_form(multiplier, form):
    return tuple(multiplier * value for value in form)


def evaluate(form, lengths):
    return sum(coefficient * length for coefficient, length in zip(form, lengths))


def symbolic_iet_data():
    units = tuple(
        tuple(int(index == label) for index in range(4)) for label in range(4)
    )
    domain_left = tuple(
        tuple(int(index < label) for index in range(4)) for label in range(4)
    )
    range_left = tuple(
        tuple(int(PERMUTATION[index] < PERMUTATION[label]) for index in range(4))
        for label in range(4)
    )
    translations = tuple(
        subtract_forms(range_left[label], domain_left[label]) for label in range(4)
    )
    return units, domain_left, translations


def cylinder_forms(word):
    units, domain_left, translations = symbolic_iet_data()
    displacement = ZERO_FORM
    lower_forms = []
    upper_forms = []
    for label in word:
        lower = subtract_forms(domain_left[label], displacement)
        lower_forms.append(lower)
        upper_forms.append(add_forms(lower, units[label]))
        displacement = add_forms(displacement, translations[label])
    return tuple(lower_forms), tuple(upper_forms)


def starts(lengths):
    output = [Fraction(0)]
    for length in lengths[:-1]:
        output.append(output[-1] + length)
    return tuple(output)


def iet_data(lengths):
    domain_left = starts(lengths)
    range_order = sorted(range(4), key=lambda label: PERMUTATION[label])
    range_left = [Fraction(0)] * 4
    cursor = Fraction(0)
    for label in range_order:
        range_left[label] = cursor
        cursor += lengths[label]
    translations = tuple(range_left[label] - domain_left[label] for label in range(4))
    return domain_left, tuple(range_left), translations


def label_at(point, interval_left, lengths):
    for label in range(4):
        if interval_left[label] <= point < interval_left[label] + lengths[label]:
            return label
    raise AssertionError((point, interval_left, lengths))


def orbit_word(point, length, lengths):
    domain_left, _, translations = iet_data(lengths)
    word = []
    for _ in range(length):
        label = label_at(point, domain_left, lengths)
        word.append(label)
        point += translations[label]
    return tuple(word)


def cylinder(word, lengths):
    domain_left, _, translations = iet_data(lengths)
    displacement = Fraction(0)
    lower = Fraction(0)
    upper = Fraction(1)
    for label in word:
        lower = max(lower, domain_left[label] - displacement)
        upper = min(upper, domain_left[label] + lengths[label] - displacement)
        displacement += translations[label]
    return lower, upper


def inverse_image(point, lengths):
    _, range_left, translations = iet_data(lengths)
    label = label_at(point, range_left, lengths)
    return point - translations[label]


def language_from_discontinuities(length, lengths):
    domain_left, _, _ = iet_data(lengths)
    boundaries = {Fraction(0), Fraction(1)}
    current = set(domain_left[1:])
    for _ in range(length):
        boundaries.update(current)
        current = {inverse_image(point, lengths) for point in current}
    ordered = sorted(boundaries)
    return {
        orbit_word((left + right) / 2, length, lengths)
        for left, right in zip(ordered, ordered[1:])
        if left < right
    }


def language_from_cylinders(length, lengths):
    answer = set()
    for word in product(range(4), repeat=length):
        left, right = cylinder(word, lengths)
        if left < right:
            midpoint = (left + right) / 2
            assert orbit_word(midpoint, length, lengths) == word
            answer.add(word)
    return answer


def main():
    test_vectors = [
        (11, 17, 23, 37),
        (7, 13, 29, 47),
        (19, 31, 41, 53),
    ]
    total_checks = 0
    language_equalities = 0
    for integers in test_vectors:
        total = sum(integers)
        lengths = tuple(Fraction(value, total) for value in integers)
        for word_length in range(1, 7):
            direct = language_from_discontinuities(word_length, lengths)
            polyhedral = language_from_cylinders(word_length, lengths)
            assert direct == polyhedral
            language_equalities += 1
            total_checks += len(polyhedral)
            for word in product(range(4), repeat=word_length):
                lower_forms, upper_forms = cylinder_forms(word)
                left, right = cylinder(word, lengths)
                lower_values = tuple(evaluate(form, lengths) for form in lower_forms)
                upper_values = tuple(evaluate(form, lengths) for form in upper_forms)
                assert left == max(lower_values)
                assert right == min(upper_values)
                assert (left < right) == all(
                    lower < upper
                    for lower in lower_values
                    for upper in upper_values
                )

    # For the first test point, the generic reverse-IET complexity 3n+1 is
    # visible through the checked horizon.
    total = sum(test_vectors[0])
    lengths = tuple(Fraction(value, total) for value in test_vectors[0])
    profile = tuple(
        len(language_from_cylinders(word_length, lengths))
        for word_length in range(1, 7)
    )
    assert profile == (4, 7, 10, 13, 16, 19)

    # A genuine collapse wall for w=(1,2): the word occurs on the plus side,
    # has zero cylinder length on the wall, and is absent on the minus side.
    wall_word = (1, 2)
    wall = (Fraction(1, 5),) * 3 + (Fraction(2, 5),)
    epsilon = Fraction(1, 500)
    plus = (wall[0] + epsilon, wall[1], wall[2], wall[3] - epsilon)
    minus = (wall[0] - epsilon, wall[1], wall[2], wall[3] + epsilon)
    wall_gap = cylinder(wall_word, wall)[1] - cylinder(wall_word, wall)[0]
    plus_gap = cylinder(wall_word, plus)[1] - cylinder(wall_word, plus)[0]
    minus_gap = cylinder(wall_word, minus)[1] - cylinder(wall_word, minus)[0]
    assert wall_gap == 0 and plus_gap > 0 and minus_gap < 0

    # Weak inequalities need not equal the closure when the strict region is
    # empty.  For w=(0,1,2), a_0=0, a_2=2d, b_1=d with
    # d=lambda_0-lambda_2-lambda_3, so strict feasibility is impossible.
    weak_word = (0, 1, 2)
    lower_forms, upper_forms = cylinder_forms(weak_word)
    d_form = (1, 0, -1, -1)
    assert lower_forms[0] == ZERO_FORM
    assert lower_forms[2] == scale_form(2, d_form)
    assert upper_forms[1] == d_form
    weak_point = (
        Fraction(2, 5),
        Fraction(1, 5),
        Fraction(3, 10),
        Fraction(1, 10),
    )
    lower_values = tuple(evaluate(form, weak_point) for form in lower_forms)
    upper_values = tuple(evaluate(form, weak_point) for form in upper_forms)
    assert all(lower <= upper for lower in lower_values for upper in upper_values)
    assert not max(lower_values) < min(upper_values)

    raw_hyperplanes_through_six = sum(
        4**length * (2 * length * length - length) for length in range(1, 7)
    )
    assert raw_hyperplanes_through_six == 324644

    print(
        f"PASS: {language_equalities} cylinder/partition language equalities "
        f"({total_checks} positive cylinders)"
    )
    print("reverse 4-IET finite complexity profile:", profile)
    print("PASS: symbolic endpoint forms and all-pairs inequalities")
    print("PASS: essential collapse wall and weak-only closure negative control")
    print("raw listed hyperplanes through N=6:", raw_hyperplanes_through_six)


if __name__ == "__main__":
    main()
