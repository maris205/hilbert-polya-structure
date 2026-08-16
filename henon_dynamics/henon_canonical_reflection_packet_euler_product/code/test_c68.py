#!/usr/bin/env python3

import json
import sys
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT / "code"))
import c68_packet_euler as c68  # noqa: E402


class PacketEulerTests(unittest.TestCase):
    def test_counts(self):
        self.assertEqual([c68.reflection_count(n) for n in range(1, 12, 2)], [2, 2, 6, 14, 28, 62])

    def test_mobius_inversion(self):
        for n in range(1, 42, 2):
            self.assertEqual(sum(c68.reflection_count(d) for d in c68.divisors(n)), c68.fixed_count(n))

    def test_product_log_derivative(self):
        product = c68.product_series(41)
        self.assertEqual(c68.recover_log_derivative(product), c68.logarithmic_derivative_coefficients(41))

    def test_even_repetitions_present(self):
        ledger = c68.logarithmic_derivative_coefficients(8)
        self.assertEqual(ledger[2], 2)
        self.assertEqual(ledger[6], 8)

    def test_boundary_constants(self):
        core = c68.core_payload()
        self.assertEqual(core["unweighted_radius"], "2^(-1/2)")
        self.assertEqual(core["boundary_type"], "EXPONENTIAL_ESSENTIAL_SINGULARITY")

    def test_status(self):
        core = c68.core_payload()
        self.assertEqual(core["claim_status"]["arithmetic_advance"], "NO")
        self.assertFalse(core["claim_status"]["route_b_authorized"])

    def test_mutations(self):
        audit = c68.mutation_audit(c68.core_payload())
        self.assertEqual(audit["attempted"], 25)
        self.assertTrue(audit["all_rejected"])

    def test_frozen_certificate_if_present(self):
        path = PROJECT / "results" / "c68_certificate.json"
        if path.exists():
            self.assertTrue(json.loads(path.read_text(encoding="utf-8"))["check"])


if __name__ == "__main__":
    unittest.main()
