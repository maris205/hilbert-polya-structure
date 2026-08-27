#!/usr/bin/env python3
"""Enumerate Dyck--Motzkin normal forms and context-count formulas."""

from itertools import product


def alphabet(bracket_types, neutral_types):
    return tuple(
        [("o", colour) for colour in range(bracket_types)]
        + [("c", colour) for colour in range(bracket_types)]
        + [("n", colour) for colour in range(neutral_types)]
    )


def reduce_word(word, bracket_types):
    unmatched_closes = []
    opening_stack = []
    for symbol in word:
        kind, colour = symbol
        if kind == "o":
            opening_stack.append(colour)
        elif kind == "c":
            if opening_stack:
                if opening_stack[-1] != colour:
                    return None
                opening_stack.pop()
            else:
                unmatched_closes.append(colour)
        else:
            assert kind == "n" and 0 <= colour
    return tuple(unmatched_closes), tuple(opening_stack)


def enumerate_forms(bracket_types, neutral_types, length):
    symbols = alphabet(bracket_types, neutral_types)
    forms = set()
    for word in product(symbols, repeat=length):
        reduced = reduce_word(word, bracket_types)
        if reduced is not None:
            forms.add(reduced)
    return forms


def geometric_sum(base, length):
    return sum(base**power for power in range(length + 1))


def extender_formula(bracket_types, neutral_types, length):
    allowed_lengths = range(length + 1)
    if neutral_types == 0:
        allowed_lengths = [
            reduced_length
            for reduced_length in allowed_lengths
            if reduced_length % 2 == length % 2
        ]
    return sum(
        (reduced_length + 1) * bracket_types**reduced_length
        for reduced_length in allowed_lengths
    )


def run_family(bracket_types, neutral_types, maximum_length):
    for length in range(maximum_length + 1):
        forms = enumerate_forms(bracket_types, neutral_types, length)
        follower_stacks = {right for _, right in forms}
        predecessor_stacks = {left for left, _ in forms}
        expected_one_sided = geometric_sum(bracket_types, length)
        expected_extenders = extender_formula(
            bracket_types, neutral_types, length
        )
        assert len(follower_stacks) == expected_one_sided
        assert len(predecessor_stacks) == expected_one_sided
        assert len(forms) == expected_extenders
    return expected_one_sided, expected_extenders


def words_through(bracket_types, neutral_types, maximum_length):
    symbols = alphabet(bracket_types, neutral_types)
    return tuple(
        word
        for length in range(maximum_length + 1)
        for word in product(symbols, repeat=length)
        if reduce_word(word, bracket_types) is not None
    )


def direct_context_checks(bracket_types, neutral_types, maximum_word_length):
    """Group words by genuinely enumerated bounded context signatures."""
    symbols = alphabet(bracket_types, neutral_types)
    for length in range(maximum_word_length + 1):
        contexts = words_through(bracket_types, neutral_types, length + 1)
        legal_words = tuple(
            word
            for word in product(symbols, repeat=length)
            if reduce_word(word, bracket_types) is not None
        )
        followers = {
            bytes(
                reduce_word(word + right, bracket_types) is not None
                for right in contexts
            )
            for word in legal_words
        }
        predecessors = {
            bytes(
                reduce_word(left + word, bracket_types) is not None
                for left in contexts
            )
            for word in legal_words
        }
        expected = geometric_sum(bracket_types, length)
        assert len(followers) == expected
        assert len(predecessors) == expected

        if length <= 2:
            extenders = {
                bytes(
                    reduce_word(left + word + right, bracket_types) is not None
                    for left in contexts
                    for right in contexts
                )
                for word in legal_words
            }
            assert len(extenders) == extender_formula(
                bracket_types, neutral_types, length
            )


def main():
    dyck_2 = run_family(2, 0, 8)
    dyck_3 = run_family(3, 0, 7)
    motzkin_2 = run_family(2, 1, 8)
    motzkin_3 = run_family(3, 2, 7)
    assert dyck_2 == (511, 2845)
    assert motzkin_2 == (511, 4097)

    # These checks group words by contexts obtained directly from legal
    # concatenations, rather than by their stored normal forms.
    direct_context_checks(2, 0, 4)
    direct_context_checks(2, 1, 3)

    # Preserved negative control: at n=2 and exactly one close, the legal
    # words consist of M matched open-close words and M^2 close-open words.
    symbols = alphabet(2, 0)
    one_close_legal = [
        word
        for word in product(symbols, repeat=2)
        if sum(kind == "c" for kind, _ in word) == 1
        and reduce_word(word, 2) is not None
    ]
    assert len(one_close_legal) == 2 + 2**2 == 6

    print("PASS: Dyck M=2 through n=8:", dyck_2)
    print("PASS: Dyck M=3 through n=7:", dyck_3)
    print("PASS: Motzkin M=2,N=1 through n=8:", motzkin_2)
    print("PASS: Motzkin M=3,N=2 through n=7:", motzkin_3)
    print("PASS: follower, predecessor, and extender formulas")
    print("PASS: direct bounded context signatures and negative control")


if __name__ == "__main__":
    main()
