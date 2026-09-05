"""Regression checks for interpretation failures, independent of producer code."""
import json
import unittest
from pathlib import Path
class C380Smoke(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.x=json.loads((Path(__file__).resolve().parents[1]/"results/c380_blaschke_evidence.json").read_text())
    def test_linear_parent_not_rank_one(self):
        matrix=self.x["parameter_rows"][0]["positive_section_0_to_10"]
        self.assertEqual(matrix[1][2],[1,1]);self.assertEqual(matrix[2][4],[1,1])
    def test_odd_trace_has_negative_multiplier_sign(self):
        self.assertEqual(self.x["parameter_rows"][3]["trace_n_1_to_16"][0],[1,3])
        self.assertEqual(self.x["parameter_rows"][3]["trace_n_1_to_16"][1],[5,3])
    def test_primitive_and_root_multiplicity(self):
        self.assertEqual(self.x["census"][1]["primitive_cycles"],1)
        row=self.x["parameter_rows"][3]["zero_census"][2]
        self.assertEqual(row["zero_count_with_boundary"],3)
if __name__=="__main__":unittest.main()
