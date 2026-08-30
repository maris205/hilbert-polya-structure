#!/usr/bin/env python3
"""Stage-4 direct localization tests for Round-8 canonical-state invariants."""

from __future__ import annotations

from collections import defaultdict
import itertools
from pathlib import Path
import sys
import unittest


CODE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CODE_DIR))
import build_round8_control_systole_certificate as builder  # noqa: E402


def apply_word(word: tuple[int, ...]) -> builder.State:
    state = builder.IDENTITY
    generators = builder.generator_numerators()
    for step in word:
        state = builder.multiply_state(state, generators[step])
    return state


class Stage4Round8InvariantTests(unittest.TestCase):
    def test_repeated_delta_cancellation_reaches_fixed_point(self) -> None:
        delta_squared = builder.poly_pow(builder.DELTA, 2)
        scaled_identity = (
            delta_squared,
            builder.ZERO,
            builder.ZERO,
            delta_squared,
        )
        normalized = builder.canonical_state(0, 2, scaled_identity)
        self.assertEqual(normalized, builder.IDENTITY)
        self.assertEqual(builder.canonical_state(*normalized), normalized)

    def test_global_negation_normalization_is_idempotent(self) -> None:
        state = apply_word((0, 1, 2))
        parity, exponent, matrix = state
        negated = tuple(builder.poly_neg(entry) for entry in matrix)
        self.assertEqual(builder.canonical_state(parity, exponent, negated), state)
        self.assertEqual(builder.canonical_state(*state), state)

    def test_generator_inverse_multiplication_orders_both_close(self) -> None:
        for index in range(4):
            self.assertEqual(apply_word((index, index + 4)), builder.IDENTITY)
            self.assertEqual(apply_word((index + 4, index)), builder.IDENTITY)

    def test_sampled_distinct_words_have_canonical_state_collisions(self) -> None:
        words = [()]
        for length in range(1, 4):
            words.extend(itertools.product(range(8), repeat=length))
        owners: dict[builder.State, list[tuple[int, ...]]] = defaultdict(list)
        for word in words:
            owners[apply_word(tuple(word))].append(tuple(word))
        collision_buckets = [bucket for bucket in owners.values() if len(bucket) > 1]
        self.assertGreater(len(collision_buckets), 0)
        self.assertGreaterEqual(len(owners[builder.IDENTITY]), 9)
        self.assertTrue(any(len(bucket) >= 3 for bucket in collision_buckets))


if __name__ == "__main__":
    unittest.main()
