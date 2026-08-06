import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("value_growth_audit.py")
SPEC = importlib.util.spec_from_file_location("value_growth_audit", MODULE_PATH)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = AUDIT
SPEC.loader.exec_module(AUDIT)


class ValueGrowthAuditTests(unittest.TestCase):
    def test_band_edge_product_growth(self):
        result = AUDIT.witness(0, 18)
        self.assertEqual(result["escape_triple_ending_at_k"], 5)
        self.assertTrue(all(row["abs_x_next_gt_abs_x_times_abs_x_prev"] for row in result["product_growth_checks"]))

    def test_discriminant_zero_product_growth(self):
        result = AUDIT.witness(-1, 18)
        self.assertEqual(result["escape_triple_ending_at_k"], 7)
        self.assertTrue(all(row["abs_x_next_gt_abs_x_times_abs_x_prev"] for row in result["product_growth_checks"]))

    def test_exact_values_are_already_far_beyond_exponential_scale(self):
        certificate = AUDIT.build_certificate(18)
        digit_counts = [row["final_numerator_decimal_digits"] for row in certificate["exact_witnesses"]]
        self.assertGreater(min(digit_counts), 100)

    def test_certificate_freezes_zero_radius_scope(self):
        certificate = AUDIT.build_certificate(18)
        self.assertEqual(
            certificate["decision"],
            "PROVED_ZERO_RADIUS_RENORMALIZATION_CLOCK_OBSTRUCTION_AT_EXACT_ESCAPE_ENERGIES",
        )
        self.assertIn("radius of convergence zero", certificate["theorem_scope"]["coefficient_series"])
        self.assertIn("indirect divisor correspondence", certificate["claim_boundary"]["not_excluded"][-1])
        self.assertIn("finite-periodic-approximant", certificate["witness_semantics"])
        self.assertIn("not asserted", certificate["witness_semantics"])


if __name__ == "__main__":
    unittest.main()
