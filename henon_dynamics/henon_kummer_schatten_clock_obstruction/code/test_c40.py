import unittest

from code.c40_schatten_checker import certificate, schatten_status


class SchattenTests(unittest.TestCase):
    def test_exact_thresholds(self) -> None:
        self.assertEqual(schatten_status(1, 2, 2), "DIVERGES_AT_PRIME_HARMONIC_BOUNDARY")
        self.assertEqual(schatten_status(51, 100, 2), "IN_S_q")
        self.assertEqual(schatten_status(49, 100, 2), "NOT_IN_S_q")
        self.assertEqual(schatten_status(101, 100, 1), "IN_S_q")

    def test_certificate(self) -> None:
        result = certificate(50_000)
        self.assertEqual(result["block_rank"], 3)
        self.assertEqual(result["good_prime_artin_conductor_exponent"], 0)


if __name__ == "__main__":
    unittest.main()
