#!/usr/bin/env python3
import json
import unittest
from collections import Counter

import stage4_loxodromic_profile as profile


class Stage4LoxodromicProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest, cls.manifest_raw = profile.load_manifest()
        cls.ledger_rows, cls.pooled_rows = profile.source_rows()
        cls.loxodromic_profile, cls.metrics = profile.build_payload()

    def test_01_manifest_and_authority_are_hash_pinned(self) -> None:
        self.assertEqual(profile.sha256(self.manifest_raw), profile.MANIFEST_SHA256)
        self.assertEqual(
            self.manifest["authorization"]["operation"],
            "derive a loxodromic-only collision profile from already frozen exact rows",
        )
        self.assertFalse(
            self.manifest["authorization"]["canonical_result_refresh_authorized"]
        )

    def test_02_frozen_source_census_and_exact_witnesses_are_unchanged(self) -> None:
        self.assertEqual(len(self.ledger_rows), 11481)
        self.assertEqual(
            Counter(row["matrix_class"] for row in self.ledger_rows),
            Counter({"IDENTITY": 1, "LOXODROMIC": 10976, "PARABOLIC": 504}),
        )
        self.assertTrue(all(row["determinant_one"] == "true" for row in self.ledger_rows))
        self.assertTrue(all(row["level3_membership"] == "true" for row in self.ledger_rows))
        self.assertTrue(
            all(row["all_exact_witnesses_pass"] == "true" for row in self.ledger_rows)
        )

    def test_03_loxodromic_partition_is_exactly_the_nonzero_d9_partition(self) -> None:
        selected = [row for row in self.ledger_rows if row["matrix_class"] == "LOXODROMIC"]
        excluded = [row for row in self.ledger_rows if row["matrix_class"] != "LOXODROMIC"]
        self.assertEqual(len(selected), 10976)
        self.assertEqual(len(excluded), 505)
        self.assertTrue(all(profile.d9_key(row) != (0, 0) for row in selected))
        self.assertTrue(all(profile.d9_key(row) == (0, 0) for row in excluded))

    def test_04_profile_is_a_byte_field_preserving_subset_of_round8(self) -> None:
        selected_keys = {
            profile.d9_key(row)
            for row in self.ledger_rows
            if row["matrix_class"] == "LOXODROMIC"
        }
        expected_rows = [
            row for row in self.pooled_rows if profile.d9_key(row) in selected_keys
        ]
        self.assertEqual(self.loxodromic_profile, expected_rows)
        self.assertEqual(len(self.pooled_rows), 145)
        self.assertEqual(len(self.loxodromic_profile), 144)
        self.assertNotIn((0, 0), {profile.d9_key(row) for row in self.loxodromic_profile})

    def test_05_exact_loxodromic_metrics_are_pinned(self) -> None:
        self.assertEqual(
            self.metrics["loxodromic_only_profile"],
            self.manifest["expected_exact_metrics"],
        )
        audit = self.metrics["loxodromic_only_profile"]
        self.assertEqual(audit["distinct_d9_values"], 144)
        self.assertEqual(audit["distinct_joint_d9_jet_descriptors"], 508)
        self.assertEqual(audit["joint_descriptor_collision_rows_beyond_first"], 10468)
        self.assertEqual(audit["maximum_d9_bucket"], 208)
        self.assertEqual(audit["maximum_joint_descriptor_bucket"], 84)
        self.assertEqual(audit["singleton_joint_descriptor_buckets"], 0)

    def test_06_pooled_to_loxodromic_delta_is_pinned(self) -> None:
        self.assertEqual(
            self.metrics["exact_delta_pooled_minus_loxodromic"],
            {
                "matrix_rows": 505,
                "distinct_d9_values": 1,
                "d9_collision_rows_beyond_first": 504,
                "distinct_joint_d9_jet_descriptors": 9,
                "joint_descriptor_collision_rows_beyond_first": 496,
                "collision_rows_separated_by_first_jet": 8,
                "maximum_d9_bucket": 297,
                "maximum_joint_descriptor_bucket": 0,
            },
        )
        self.assertEqual(
            self.metrics["derived_ratios"]["residual_joint_collision_share_fraction"],
            "2617/2708",
        )

    def test_07_owner_and_route_firewalls_remain_closed(self) -> None:
        self.assertEqual(
            self.metrics["interpretation"]["claim"],
            "FINITE_MATRIX_COMPRESSION_PROFILE_ONLY",
        )
        self.assertEqual(
            self.metrics["interpretation"]["primitive_owner_collision_witness"],
            "NOT_SUPPLIED",
        )
        self.assertEqual(self.metrics["formal_route_a_tuple"], [
            "A0_WEAK_ARITHMETIC_RELATION",
            "A1_WEAK",
            "A2_FAIL",
            "A3_FAIL",
            "A4_FAIL",
        ])
        self.assertEqual(self.metrics["full_bianchi_flow_route_tuple"], "UNASSIGNED")
        self.assertFalse(self.metrics["route_b_invocation_allowed"])
        self.assertFalse(self.metrics["canonical_results_refreshed"])
        self.assertFalse(self.metrics["registered_claim_surfaces_modified"])

    def test_08_output_scope_is_disjoint_from_every_protected_path(self) -> None:
        rendered = {path.as_posix() for path in profile.rendered_outputs()}
        self.assertEqual(rendered, set(self.manifest["new_output_paths"]))
        self.assertFalse(rendered & set(self.manifest["protected_paths"]))
        for relative, binding in self.manifest["source_bindings"].items():
            raw = profile.bound_path(relative).read_bytes()
            self.assertEqual(profile.sha256(raw), binding["sha256"])
            self.assertEqual(len(raw), binding["bytes"])

    def test_09_render_is_deterministic_and_receipt_binds_every_new_byte(self) -> None:
        first = profile.rendered_outputs()
        second = profile.rendered_outputs()
        self.assertEqual(first, second)
        receipt = json.loads(first[profile.RECEIPT_PATH])
        material = {path: data for path, data in first.items() if path != profile.RECEIPT_PATH}
        self.assertEqual(receipt["material_sha256"], profile.combined_hash(material))
        self.assertEqual(receipt["unit_tests"], {"expected": 10, "failed": 0})
        for relative, binding in receipt["output_bindings"].items():
            data = first[profile.Path(relative)]
            self.assertEqual(profile.sha256(data), binding["sha256"])
            self.assertEqual(len(data), binding["bytes"])

    def test_10_registered_claim_surfaces_remain_exact_in_the_anchored_base(self) -> None:
        claim_manifest = json.loads(
            profile.bound_path("notes/stage4_claim_surface_manifest.json").read_bytes()
        )
        base = profile.bound_path("notes/stage3_revision_base.tex").read_bytes()
        self.assertEqual(len(claim_manifest["surfaces"]), 10)
        for surface in claim_manifest["surfaces"]:
            observed = base[surface["utf8_start"]:surface["utf8_end"]]
            expected = surface["original_text"].encode("utf-8")
            self.assertEqual(observed, expected, surface["surface_id"])
            self.assertEqual(profile.sha256(observed), surface["original_text_sha256"])


if __name__ == "__main__":
    unittest.main()
