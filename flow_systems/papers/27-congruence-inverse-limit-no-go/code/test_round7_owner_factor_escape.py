#!/usr/bin/env python3
import json
import unittest

import round7_owner_factor_escape as escape


class OwnerFactorEscapeRound7Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.freeze, cls.freeze_raw = escape.load_freeze()
        cls.cusped, cls.compact = escape.validate_inputs()
        cls.ledger, cls.prefix, cls.summary = escape.build_payload()

    def test_01_freeze_and_four_upstream_inputs_are_hash_locked(self) -> None:
        self.assertEqual(escape.sha256(self.freeze_raw), escape.FREEZE_SHA256)
        for name, (path, digest) in escape.INPUT_LOCKS.items():
            self.assertEqual(escape.sha256((escape.PROJECT_ROOT / path).read_bytes()), digest, name)
        self.assertTrue(all(value is False for value in self.freeze["forbidden_inputs"].values()))

    def test_02_upstream_ledgers_and_validation_states_are_replayed(self) -> None:
        self.assertEqual(len(self.cusped), 24)
        self.assertEqual(len(self.compact), 24)
        self.assertEqual({row["element_id"] for row in self.cusped}, {"G3-A", "G3-B", "G3-C"})
        self.assertEqual(
            {row["owner_id"] for row in self.compact},
            {"G2-H1-A", "G2-H1-AB", "G2-H1-ACD"},
        )

    def test_03_unified_ledger_has_six_owners_and_eight_levels_each(self) -> None:
        self.assertEqual(len(self.ledger), 48)
        owners = {row["owner_id"] for row in self.ledger}
        self.assertEqual(len(owners), 6)
        self.assertTrue(all(sum(row["owner_id"] == owner for row in self.ledger) == 8 for owner in owners))

    def test_04_exact_and_lower_bound_order_semantics_never_mix(self) -> None:
        cusped = [row for row in self.ledger if row["tower_type"].startswith("CUSPED")]
        compact = [row for row in self.ledger if row["tower_type"].startswith("COCOMPACT")]
        self.assertEqual(len(cusped), 24)
        self.assertEqual(len(compact), 24)
        self.assertTrue(all(row["order_evidence"] == "EXACT_FINITE_QUOTIENT_ORDER" for row in cusped))
        self.assertTrue(all(row["exact_quotient_order"] == row["certified_order_lower_bound"] for row in cusped))
        self.assertTrue(all(row["base_conjugacy_primitivity"] == "NOT_ESTABLISHED" for row in cusped))
        self.assertTrue(all("NOT_A_PRIMITIVE_ZETA_FACTOR" in row["factor_support_evidence"] for row in cusped))
        self.assertTrue(all(row["order_evidence"] == "CERTIFIED_HOMOLOGY_LOWER_BOUND_ONLY" for row in compact))
        self.assertTrue(all(row["exact_quotient_order"] == "NOT_ENUMERATED" for row in compact))
        self.assertTrue(all(row["base_conjugacy_primitivity"] == "PROVED_BY_PRIMITIVE_HOMOLOGY" for row in compact))

    def test_05_every_row_certifies_the_correct_zero_coefficient_prefix(self) -> None:
        for row in self.ledger:
            order_bound = int(row["certified_order_lower_bound"])
            self.assertEqual(int(row["certified_zero_coefficient_prefix_through_degree"]), order_bound - 1)
            self.assertEqual(row["coefficient_prefix_statement"], f"E=1 mod x^{order_bound}")

    def test_06_exact_owner_factor_has_no_terms_below_its_order(self) -> None:
        for order in (1, 2, 3, 6, 12, 288):
            coefficients = [int(degree % order == 0) for degree in range(0, 2 * order + 1)]
            self.assertEqual(coefficients[0], 1)
            self.assertTrue(all(value == 0 for value in coefficients[1:order]))
            self.assertEqual(coefficients[order], 1)

    def test_07_prefix_grid_has_one_row_per_owner_and_degree(self) -> None:
        self.assertEqual(self.freeze["diagnostic_prefix_degrees"], [1, 2, 4, 8, 16, 32, 64, 128, 256])
        self.assertEqual(len(self.prefix), 6 * 9)
        keys = {(row["owner_id"], row["fixed_prefix_degree_N"]) for row in self.prefix}
        self.assertEqual(len(keys), len(self.prefix))

    def test_08_known_degree_256_escape_witnesses_are_exact(self) -> None:
        degree_rows = {
            row["owner_id"]: row for row in self.prefix if row["fixed_prefix_degree_N"] == "256"
        }
        self.assertEqual(degree_rows["G3-A"]["first_certified_escape_level"], "8")
        self.assertEqual(degree_rows["G3-B"]["first_certified_escape_level"], "6")
        self.assertEqual(degree_rows["G3-C"]["first_certified_escape_level"], "8")
        self.assertEqual(degree_rows["G2-H1-A"]["first_certified_escape_level"], "6")
        self.assertEqual(degree_rows["G2-H1-AB"]["first_certified_escape_level"], "6")
        self.assertEqual(degree_rows["G2-H1-ACD"]["first_certified_escape_level"], "6")

    def test_09_finite_replay_does_not_claim_to_machine_prove_asymptotics(self) -> None:
        self.assertEqual(
            self.summary["general_order_escape_theorem"],
            "PROVED_IN_ROUND4_AND_ROUND5_NOT_FROM_FINITE_ROWS",
        )
        self.assertEqual(self.summary["owner_factor_escape_theorem"], "PROVED_IN_ROUND7_NOTE")
        self.assertEqual(self.summary["renormalized_collective_object"], "NOT_DEFINED_NOT_REFUTED_BY_THIS_THEOREM")

    def test_10_same_owner_route_and_human_source_firewalls_remain_closed(self) -> None:
        self.assertEqual(self.summary["formal_route_a_tuple"], list(escape.FORMAL_TUPLE))
        self.assertEqual(self.summary["overall_verdict"], "ROUTE_A_REJECTED")
        self.assertEqual(self.summary["a2_claim"], "SAME_OWNER_A2_REFUTED")
        self.assertFalse(self.summary["route_b_invocation_allowed"])
        self.assertFalse(self.summary["human_source_confirmations_inferred"])

    def test_11_render_is_byte_deterministic_and_source_bound(self) -> None:
        first = escape.rendered_outputs()
        second = escape.rendered_outputs()
        self.assertEqual(first, second)
        receipt = json.loads(first[escape.RECEIPT_PATH])
        for relative, binding in receipt["source_bindings"].items():
            payload = (escape.PROJECT_ROOT / relative).read_bytes()
            self.assertEqual(binding["sha256"], escape.sha256(payload))
            self.assertEqual(binding["bytes"], len(payload))

    def test_12_receipt_binds_core_outputs_and_route_boundary(self) -> None:
        rendered = escape.rendered_outputs()
        core = {path: rendered[path] for path in escape.RESULT_PATHS.values()}
        receipt = json.loads(rendered[escape.RECEIPT_PATH])
        self.assertEqual(receipt["core_sha256"], escape.combined_hash(core))
        self.assertEqual(receipt["formal_route_a_tuple"], list(escape.FORMAL_TUPLE))
        self.assertFalse(receipt["route_b_invocation_allowed"])
        for path, payload in core.items():
            self.assertEqual(receipt["files"][path.as_posix()]["sha256"], escape.sha256(payload))


if __name__ == "__main__":
    unittest.main()
