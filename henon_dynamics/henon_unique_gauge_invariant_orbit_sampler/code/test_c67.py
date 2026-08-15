import json
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
CERT = json.loads((PROJECT / "results" / "c67_certificate.json").read_text())
INDEPENDENT = json.loads((PROJECT / "results" / "c67_independent_check.json").read_text())


class Tests(unittest.TestCase):
    def test_check(self): self.assertTrue(CERT["check"] and INDEPENDENT["check"])
    def test_ranks(self): self.assertEqual([r["difference_rank"] for r in CERT["sampler_rows"]], list(range(1, 12)))
    def test_uniform(self): self.assertTrue(all(len(set(r["normalized_solution"])) == 1 for r in CERT["sampler_rows"]))
    def test_nonuniform(self): self.assertTrue(all(r["nonuniform_anomaly"] != "0" for r in CERT["sampler_rows"]))
    def test_telescope(self): self.assertTrue(all(r["coboundary_orbit_sum"] == "0" for r in CERT["packet_rows"]))
    def test_status(self): self.assertEqual(CERT["claim_status"]["canonical_sampler_uniqueness"], "PROVED")
    def test_mutations(self): self.assertEqual(CERT["mutation_audit"]["attempted"], 21)
    def test_firewall(self): self.assertEqual(CERT["claim_status"]["arithmetic_advance"], "NO"); self.assertFalse(CERT["claim_status"]["route_b_authorized"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
