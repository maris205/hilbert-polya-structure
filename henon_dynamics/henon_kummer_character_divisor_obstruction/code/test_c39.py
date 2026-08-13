import unittest

from code.c39_character_checker import certificate, character


class CharacterTests(unittest.TestCase):
    def test_fourier_inversion_sentinels(self) -> None:
        self.assertEqual(character((1, 0, 0), 1), (1, 0))
        self.assertEqual(character((0, 1, 0), 1), (0, 1))
        self.assertEqual(character((0, 0, 1), 1), (-1, -1))
        self.assertEqual(character((1, -1, 0), 3), (0, 0))
        self.assertNotEqual(character((1, -1, 0), 1), (0, 0))

    def test_certificate(self) -> None:
        result = certificate(bound=4, prime_limit=20_000)
        self.assertEqual(result["all_repetition_null_vectors"], [[0, 0, 0]])
        self.assertEqual(result["raw_all_prime_meromorphic_divisor"], "REFUTED_BY_INTERIOR_ACCUMULATION")


if __name__ == "__main__":
    unittest.main()
