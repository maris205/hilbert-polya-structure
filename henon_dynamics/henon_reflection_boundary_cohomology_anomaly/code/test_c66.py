import json
import unittest
from pathlib import Path
PROJECT = Path(__file__).resolve().parents[1]
CERT = json.loads((PROJECT / "results/c66_certificate.json").read_text())
INDEPENDENT = json.loads((PROJECT / "results/c66_independent_check.json").read_text())
class Tests(unittest.TestCase):
    def test_check(self): self.assertTrue(CERT["check"] and INDEPENDENT["check"])
    def test_norm(self): self.assertEqual(CERT["anomaly_operator_norm"], "2")
    def test_means(self): self.assertEqual([row["full_shifted_u_mean"] for row in CERT["rows"]], ["1/2", "1/4", "1/8", "1/16", "1/32"])
    def test_telescope(self): self.assertTrue(all(row["orbit_coboundary_sum"] == "0" for row in CERT["rows"]))
    def test_status(self): self.assertEqual(CERT["claim_status"]["canonical_sampler_uniqueness"], "OPEN")
    def test_mutations(self): self.assertEqual(CERT["mutation_audit"]["attempted"], 19)
    def test_firewall(self): self.assertEqual(CERT["claim_status"]["arithmetic_advance"], "NO"); self.assertFalse(CERT["claim_status"]["route_b_authorized"])
if __name__ == "__main__": unittest.main(verbosity=2)
