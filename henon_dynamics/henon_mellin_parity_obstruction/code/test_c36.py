from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


CODE = Path(__file__).resolve().parent


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


producer = load("c36_producer", CODE / "c36_mellin_producer.py")
checker = load("c36_checker", CODE / "c36_mellin_checker.py")


def rehash(certificate):
    certificate["payload_sha256"] = hashlib.sha256(
        checker.canonical_json(certificate["payload"])
    ).hexdigest()


class C36Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = producer.build_certificate()

    def setUp(self):
        self.certificate = copy.deepcopy(self.base)

    def assert_rejected(self, mutation, *, update_hash=True):
        mutation(self.certificate)
        if update_hash:
            rehash(self.certificate)
        gates = checker.audit(self.certificate)
        self.assertTrue(any(row["status"] != "PASS" for row in gates), gates)

    def test_01_base_certificate_passes_all_gates(self):
        gates = checker.audit(self.certificate)
        self.assertEqual(len(gates), 9)
        self.assertTrue(all(row["status"] == "PASS" for row in gates), gates)

    def test_02_producer_is_deterministic(self):
        self.assertEqual(
            json.dumps(self.certificate, sort_keys=True),
            json.dumps(producer.build_certificate(), sort_keys=True),
        )

    def test_03_unrehashed_payload_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["object"].__setitem__("phase", "P6(u)=2*u^3+u"),
            update_hash=False,
        )

    def test_04_source_hash_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["source_lock"]["area_preserving_henon_model"].__setitem__(
                "sha256", "0" * 64
            )
        )

    def test_05_unknown_nested_key_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["certified_zero_disc"].__setitem__("rh_proved", True)
        )

    def test_06_runtime_bool_integer_confusion_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["runtime"].__setitem__("arb_decimal_digits", True)
        )

    def test_07_hypergeometric_argument_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["analytic_gate"].__setitem__(
                "hypergeometric_argument", "+2*pi^2/27"
            )
        )

    def test_08_recurrence_sign_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["analytic_gate"].__setitem__(
                "recurrence", "12*pi*kappa(z+3)+2*pi*kappa(z+1)=i*z*kappa(z)"
            )
        )

    def test_09_center_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["certified_zero_disc"].__setitem__("center_re", "3/4")
        )

    def test_10_radius_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["certified_zero_disc"].__setitem__(
                "radius", "1/100000000000"
            )
        )

    def test_11_noncanonical_fraction_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["certified_zero_disc"].__setitem__(
                "radius", "2/2000000000000"
            )
        )

    def test_12_threshold_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["certified_zero_disc"]["thresholds"].__setitem__(
                "A_prime_center_abs_lower", "1/10"
            )
        )

    def test_13_arb_enclosure_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["certified_zero_disc"]["arb_enclosures"].__setitem__(
                "A_center", "0"
            )
        )

    def test_14_second_derivative_overclaim_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["second_derivative_majorant"].__setitem__(
                "conclusion", "sup_D abs(A_second(z))<1"
            )
        )

    def test_15_rouche_lhs_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["certified_zero_disc"].__setitem__(
                "rouche_lhs_upper", "0"
            )
        )

    def test_16_zero_count_bool_confusion_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["certified_zero_disc"].__setitem__(
                "zero_count_with_multiplicity", True
            )
        )

    def test_17_simplicity_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["certified_zero_disc"].__setitem__("simple_zero", False)
        )

    def test_18_no_cancellation_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["no_cancellation_gate"].__setitem__(
                "B_on_disc_nonzero", False
            )
        )

    def test_19_route_a_promotion_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["route_a"].__setitem__("overall", "ROUTE_A_SUCCESS")
        )

    def test_20_route_b_promotion_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["route_a"].__setitem__(
                "route_b_invocation_allowed", True
            )
        )

    def test_21_posthoc_zero_removal_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["decisions"].__setitem__("posthoc_zero_removal", "ALLOWED")
        )

    def test_22_rh_scope_overclaim_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["scope"].__setitem__("no_RH_proof", False)
        )

    def test_23_riemann_table_scope_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["scope"].__setitem__(
                "no_Riemann_zero_table_used", False
            )
        )

    def test_24_duplicate_json_keys_are_rejected_by_parser(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"schema":"first","schema":"second"}\n', encoding="utf-8")
            with self.assertRaises(checker.DuplicateKeyError):
                checker.load_certificate(path)

    def test_25_completed_xi_nonvanishing_mutation_is_rejected(self):
        self.assert_rejected(
            lambda c: c["payload"]["no_cancellation_gate"].__setitem__(
                "completed_xi_on_disc_nonzero", False
            )
        )


if __name__ == "__main__":
    unittest.main()
