#!/usr/bin/env python3
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("round2_reduction_orders.py")
SPEC = importlib.util.spec_from_file_location("p27_round2", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Round2ReductionOrderTests(unittest.TestCase):
    def test_frozen_elements(self):
        for element in MODULE.ELEMENTS:
            matrix = element["matrix"]
            self.assertEqual(MODULE.determinant(matrix), 1)
            self.assertTrue(MODULE.gamma3_member(matrix))
            self.assertGreater(matrix[0][0] + matrix[1][1], 2)
            self.assertTrue(MODULE.primitive_word(element["word"]))

    def test_all_levels_and_crosschecks(self):
        rows = MODULE.build_rows()
        self.assertEqual(len(rows), 24)
        self.assertTrue(all(row["order_crosscheck"] == "true" for row in rows))
        self.assertTrue(all(row["bonding_compatibility"] == "true" for row in rows))
        self.assertTrue(all(row["previous_order_divides"] == "true" for row in rows))
        transitions = [row for row in rows if int(row["level_n"]) > 1]
        self.assertEqual(len(transitions), 21)
        self.assertTrue(all(row["bonding_compatibility"] == "true" for row in transitions))
        self.assertTrue(all(row["previous_order_divides"] == "true" for row in transitions))

    def test_frozen_order_sequences(self):
        rows = MODULE.build_rows()
        observed = {
            element["element_id"]: [
                int(row["psl_order_sequential"])
                for row in rows
                if row["element_id"] == element["element_id"]
            ]
            for element in MODULE.ELEMENTS
        }
        self.assertEqual(observed["G3-A"], [1, 3, 3, 6, 6, 36, 72, 288])
        self.assertEqual(observed["G3-B"], [1, 1, 3, 12, 60, 360, 360, 2880])
        self.assertEqual(observed["G3-C"], [1, 2, 6, 12, 12, 72, 72, 576])

    def test_owner_firewall(self):
        rows = MODULE.build_rows()
        self.assertTrue(
            all(row["statistic_owner"] == "FINITE_CONGRUENCE_TOWER_REDUCTION_DIAGNOSTIC" for row in rows)
        )
        self.assertTrue(all(row["inverse_limit_flow_credit"] == "FORBIDDEN" for row in rows))

    def test_serialization_is_deterministic(self):
        self.assertEqual(MODULE.build_artifacts(), MODULE.build_artifacts())
        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory)
            MODULE.generate(output_dir)
            self.assertEqual(MODULE.verify(output_dir)["status"], "PASS")
            manifest_path = output_dir / "manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["source_files"]["round2_reduction_orders.py"]["sha256"] = "0" * 64
            manifest_path.write_text(
                json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            verification = MODULE.verify(output_dir)
            self.assertEqual(verification["status"], "FAIL")
            self.assertIn(
                "source_manifest_hash:round2_reduction_orders.py",
                verification["mismatches"],
            )


if __name__ == "__main__":
    unittest.main()
