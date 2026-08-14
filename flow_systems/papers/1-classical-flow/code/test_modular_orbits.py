#!/usr/bin/env python3
import math
import unittest

from modular_orbits import (
    R,
    S,
    determinant,
    inverse_code,
    is_primitive_word,
    matmul,
    oriented_canonical,
    prime_sieve,
    trace_abs,
    unoriented_canonical,
    word_matrix,
)


class ModularOrbitTests(unittest.TestCase):
    def test_group_relations_hold_projectively(self) -> None:
        minus_identity = ((-1, 0), (0, -1))
        self.assertEqual(matmul(S, S), minus_identity)
        self.assertEqual(matmul(matmul(R, R), R), minus_identity)

    def test_shortest_hyperbolic_code(self) -> None:
        matrix = word_matrix((1, 2))
        self.assertEqual(determinant(matrix), 1)
        self.assertEqual(trace_abs(matrix), 3)
        length = 2.0 * math.acosh(1.5)
        self.assertAlmostEqual(length, 1.9248473002384139)

    def test_primitivity(self) -> None:
        self.assertTrue(is_primitive_word((1, 1, 2)))
        self.assertFalse(is_primitive_word((1, 2, 1, 2)))

    def test_orientation_quotient_is_idempotent(self) -> None:
        word = (2, 1, 1, 2, 1)
        canonical = unoriented_canonical(word)
        self.assertEqual(unoriented_canonical(canonical), canonical)
        self.assertEqual(unoriented_canonical(inverse_code(word)), canonical)

    def test_inverse_preserves_trace(self) -> None:
        for word in ((1, 2), (1, 1, 2), (1, 2, 2, 1, 2)):
            self.assertEqual(trace_abs(word_matrix(word)), trace_abs(word_matrix(inverse_code(word))))

    def test_norm_identity(self) -> None:
        trace = 9
        discriminant = trace * trace - 4
        q = trace * trace - 2
        norm = 0.5 * (q + trace * math.sqrt(discriminant))
        self.assertAlmostEqual(norm + 1.0 / norm, q, places=12)
        self.assertAlmostEqual(math.log(norm), 2.0 * math.acosh(trace / 2.0), places=12)

    def test_oriented_canonical_rotation(self) -> None:
        self.assertEqual(oriented_canonical((2, 1, 2, 1, 1)), (1, 1, 2, 1, 2))

    def test_every_integer_trace_is_represented(self) -> None:
        # The primitive word 1^(t-2)2 has absolute trace t.
        for trace in range(3, 51):
            word = (1,) * (trace - 2) + (2,)
            self.assertTrue(is_primitive_word(word))
            self.assertEqual(trace_abs(word_matrix(word)), trace)

    def test_orientation_count_identity(self) -> None:
        for size in range(2, 9):
            words = []
            for mask in range(1 << size):
                word = tuple(1 + ((mask >> index) & 1) for index in range(size))
                if not is_primitive_word(word) or trace_abs(word_matrix(word)) <= 2:
                    continue
                if word == oriented_canonical(word):
                    words.append(word)
            unoriented = {unoriented_canonical(word) for word in words}
            self_reverse = sum(oriented_canonical(word) == oriented_canonical(inverse_code(word)) for word in words)
            self.assertEqual(len(words), 2 * len(unoriented) - self_reverse)

    def test_small_prime_sieve(self) -> None:
        sieve = prime_sieve(30)
        self.assertEqual([index for index, flag in enumerate(sieve) if flag], [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])


if __name__ == "__main__":
    unittest.main()
