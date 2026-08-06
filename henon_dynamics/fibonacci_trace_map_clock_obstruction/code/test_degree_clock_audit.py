import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("degree_clock_audit.py")
SPEC = importlib.util.spec_from_file_location("degree_clock_audit", MODULE_PATH)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = AUDIT
SPEC.loader.exec_module(AUDIT)


class DegreeClockAuditTests(unittest.TestCase):
    def test_exact_symbolic_degrees(self):
        rows = AUDIT.exact_symbolic_degree_check(10)
        self.assertEqual(rows[-1], {"k": 10, "q_k": 144, "degree_d_k": 144})

    def test_registered_growth(self):
        rows = AUDIT.required_local_degree_rows(30)
        self.assertEqual(len(rows), 30)
        self.assertEqual(rows[-1]["physical_length_q_k"], 2_178_309)
        self.assertEqual(
            rows[-1]["minimum_uniform_edge_degree_for_closed_trace_at_level_k"],
            72_611,
        )

    def test_required_local_degree_is_unbounded(self):
        rows = AUDIT.required_local_degree_rows(100)
        required = [row["minimum_uniform_edge_degree_for_closed_trace_at_level_k"] for row in rows]
        self.assertGreater(required[-1], required[29])
        self.assertGreater(required[-1], 10**17)

    def test_certificate_states_escape_routes(self):
        cert = AUDIT.build_certificate(30, 10)
        self.assertIn("physical-time models indexed by q_k", cert["claim_boundary"]["not_excluded"])
        self.assertIn("does not refute every weighted Fredholm determinant", cert["claim_boundary"]["not_a_claim"])
        self.assertIn("N_k may grow without restriction", cert["theorem_scope"]["model_class"])
        self.assertIn("increasing N_k alone", cert["theorem_scope"]["determinant_coefficients"])


if __name__ == "__main__":
    unittest.main()
