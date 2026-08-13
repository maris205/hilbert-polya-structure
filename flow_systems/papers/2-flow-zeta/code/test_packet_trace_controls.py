#!/usr/bin/env python3
import math
import tempfile
import unittest
from pathlib import Path

from packet_trace_controls import (
    first_return_mass,
    packet_log_product,
    packet_mass,
    primes_up_to,
    run,
)


class PacketTraceControlsTest(unittest.TestCase):
    def test_prime_sieve(self) -> None:
        self.assertEqual(primes_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_mass_models(self) -> None:
        self.assertEqual(packet_mass("unit", 5), 1.0)
        self.assertAlmostEqual(packet_mass("decay_half", 4), 0.5)
        self.assertEqual(packet_mass("growth_linear", 7), 7.0)
        self.assertEqual(packet_mass("mod4_sign", 3), -1.0)
        self.assertEqual(packet_mass("mod4_sign", 5), 1.0)

    def test_log_product_formula(self) -> None:
        primes = [2, 3]
        observed = packet_log_product(primes, 2.0, "unit")
        expected = math.log((1.0 - 2.0 ** -2) ** -1 * (1.0 - 3.0 ** -2) ** -1)
        self.assertAlmostEqual(observed, expected)

    def test_absolute_majorant_uses_absolute_weights(self) -> None:
        self.assertEqual(first_return_mass([3, 5], 1.0, "mod4_sign"), 1 / 3 + 1 / 5)

    def test_outputs_and_hashes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            manifest = run(output, 1_000)
            self.assertEqual(manifest["prime_count"], 168)
            for artifact in manifest["artifacts"]:
                self.assertTrue((output / artifact).is_file())


if __name__ == "__main__":
    unittest.main()
