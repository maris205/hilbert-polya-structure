from __future__ import annotations

import copy
import csv
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE_PATH = PROJECT / "results" / "c19_certificate.json"
CHECK_PATH = PROJECT / "results" / "c19_independent_check.json"
NEIGHBOR_CERTIFICATE_PATH = PROJECT / "results" / "c19_neighbor_correspondence.json"
NEIGHBOR_CHECK_PATH = PROJECT / "results" / "c19_neighbor_independent_check.json"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


CHECKER = load_module("c19_independent_check_for_tests", PROJECT / "code" / "c19_independent_check.py")
NEIGHBOR_CHECKER = load_module(
    "c19_neighbor_independent_check_for_tests",
    PROJECT / "code" / "c19_neighbor_independent_check.py",
)


class C19Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.certificate_bytes = CERTIFICATE_PATH.read_bytes()
        cls.certificate = json.loads(cls.certificate_bytes)
        cls.independent = json.loads(CHECK_PATH.read_text(encoding="utf-8"))
        cls.neighbor_certificate_bytes = NEIGHBOR_CERTIFICATE_PATH.read_bytes()
        cls.neighbor_certificate = json.loads(cls.neighbor_certificate_bytes)
        cls.neighbor_independent = json.loads(NEIGHBOR_CHECK_PATH.read_text(encoding="utf-8"))
        CHECKER.validate_certificate_schema(cls.certificate)
        CHECKER.validate_independent_report(cls.independent, cls.certificate, cls.certificate_bytes)
        NEIGHBOR_CHECKER.validate_neighbor_certificate_schema(cls.neighbor_certificate)
        NEIGHBOR_CHECKER.validate_neighbor_independent_report(
            cls.neighbor_independent,
            cls.neighbor_certificate,
            cls.neighbor_certificate_bytes,
        )

    def test_source_correction_witness(self) -> None:
        correction = self.certificate["symbolic"]["source_correction"]
        self.assertEqual(correction["status"], "EXACT_SPECIALIZATION_CERTIFIED_APPARENT_PRINT_ERROR")
        self.assertFalse(correction["journal_erratum_claimed"])
        witness = correction["exact_witness"]
        self.assertEqual(witness["field"], "F_103")
        self.assertEqual(witness["corrected_coordinate_roots"], [10, 17, 31, 54, 58, 67, 98])
        self.assertEqual(witness["literal_printed_roots"], [55, 60])
        self.assertTrue(witness["cycles_are_reversal_pair"])

    def test_genus_certificate(self) -> None:
        symbolic = self.certificate["symbolic"]
        self.assertEqual(
            symbolic["riemann_hurwitz"],
            {"degree": 7, "genus": 3, "total_ramification": 18, "twice_genus_minus_two": 4},
        )
        self.assertEqual(
            symbolic["plane_genus_cross_check"],
            {"arithmetic_genus": 15, "finite_node_delta": 1, "geometric_genus": 3, "infinity_delta": 11},
        )

    def test_frobenius_rows(self) -> None:
        expected = {
            5: ([9, 39, 147], [1, 3, 11, 31, 55, 75, 125]),
            11: ([19, 167, 1171], [1, 7, 47, 161, 517, 847, 1331]),
            13: ([16, 242, 2131], [1, 2, 38, 51, 494, 338, 2197]),
        }
        rows = {row["prime"]: row for row in self.certificate["frobenius"]}
        self.assertEqual(set(rows), set(expected))
        for prime, (counts, polynomial) in expected.items():
            self.assertEqual(rows[prime]["normalization_counts_r1_r3"], counts)
            self.assertEqual(rows[prime]["l_polynomial_coefficients_ascending"], polynomial)
            self.assertLess(rows[prime]["maximum_reciprocal_root_modulus_error"], 2.2e-15)

    def test_independent_report_anchors_current_certificate(self) -> None:
        self.assertTrue(self.independent["all_checks_passed"])
        self.assertEqual(
            self.independent["source_certificate"]["sha256"],
            hashlib.sha256(self.certificate_bytes).hexdigest(),
        )
        self.assertTrue(self.independent["direct_p5_r4_check"]["matches_prediction"])
        self.assertEqual(self.independent["direct_p5_r4_check"]["normalization_count"], 547)

    def test_neighbor_checker_recomputes_to_temporary_report(self) -> None:
        # This is the suite's one expensive independent recomputation.  The
        # Frobenius report is still validated exhaustively above, but is not
        # redundantly point-counted again in the same default test process.
        with tempfile.TemporaryDirectory(prefix="hcs-c19-neighbor-check-") as directory:
            output = Path(directory) / "neighbor-independent.json"
            fresh = NEIGHBOR_CHECKER.run(NEIGHBOR_CERTIFICATE_PATH, output)
            self.assertTrue(output.is_file())
            NEIGHBOR_CHECKER.validate_neighbor_independent_report(
                fresh,
                self.neighbor_certificate,
                self.neighbor_certificate_bytes,
            )
            self.assertEqual(
                fresh["verified_certificate_content"],
                self.neighbor_independent["verified_certificate_content"],
            )

    def test_csv_matches_certificate_exactly(self) -> None:
        csv_path = PROJECT / "results" / "frobenius_counts.csv"
        with csv_path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            self.assertEqual(
                reader.fieldnames,
                [
                    "prime",
                    "extension_degree",
                    "affine_count",
                    "node_splits",
                    "normalization_count",
                    "frobenius_power_sum",
                ],
            )
            actual = list(reader)
        expected = []
        for row in self.certificate["frobenius"]:
            for index, degree in enumerate((1, 2, 3)):
                expected.append(
                    {
                        "prime": str(row["prime"]),
                        "extension_degree": str(degree),
                        "affine_count": str(row["affine_counts_r1_r3"][index]),
                        "node_splits": str(int(row["node_splits_r1_r3"][index])),
                        "normalization_count": str(row["normalization_counts_r1_r3"][index]),
                        "frobenius_power_sum": str(row["frobenius_power_sums_r1_r3"][index]),
                    }
                )
        self.assertEqual(actual, expected)

    def test_checker_has_no_producer_or_galois_import(self) -> None:
        for filename in ("c19_independent_check.py", "c19_neighbor_independent_check.py"):
            with self.subTest(filename=filename):
                source = (PROJECT / "code" / filename).read_text(encoding="utf-8")
                self.assertNotIn("import c19_producer", source)
                self.assertNotIn("from c19_producer", source)
                self.assertNotIn("import c19_neighbor_correspondence", source)
                self.assertNotIn("from c19_neighbor_correspondence", source)
                self.assertNotIn("import galois", source)

    def test_strict_schema_rejects_extra_key(self) -> None:
        tampered = copy.deepcopy(self.certificate)
        tampered["unexpected"] = True
        with self.assertRaises(AssertionError):
            CHECKER.validate_certificate_schema(tampered)

    def test_symbolic_tamper_is_detected(self) -> None:
        tampered = copy.deepcopy(self.certificate)
        tampered["symbolic"]["source_correction"]["exact_witness"]["corrected_coordinate_roots"][0] = 9
        CHECKER.validate_certificate_schema(tampered)
        with self.assertRaises(AssertionError):
            CHECKER.symbolic_checks(tampered)

    def test_semantic_certificate_tampers_are_rejected(self) -> None:
        def parameter_relation(payload):
            payload["symbolic"]["parameter_relation"] = "a = 0"

        def generic_witness(payload):
            payload["symbolic"]["generic_irreducibility"]["irreducible"] = False

        def q6_flag(payload):
            payload["symbolic"]["q6_irreducible"] = False

        def ramification(payload):
            payload["symbolic"]["q6_ramification"]["ramification_index"] = -2

        def infinity(payload):
            payload["symbolic"]["infinity"]["ramification"] = 999

        def orientation(payload):
            payload["symbolic"]["orientation_boundary"]["full_chronology_claimed"] = True

        def l_string(payload):
            payload["frobenius"][0]["l_polynomial"] = "0"

        def l_irreducibility(payload):
            payload["frobenius"][0]["irreducible_over_q"] = False

        def weil_residual(payload):
            payload["frobenius"][0]["maximum_reciprocal_root_modulus_error"] = 1e100

        mutations = {
            "parameter relation": parameter_relation,
            "generic witness": generic_witness,
            "Q6 flag": q6_flag,
            "ramification ledger": ramification,
            "infinity ramification": infinity,
            "orientation boundary": orientation,
            "L string": l_string,
            "L irreducibility": l_irreducibility,
            "Weil residual": weil_residual,
        }
        for name, mutate in mutations.items():
            with self.subTest(name=name):
                tampered = copy.deepcopy(self.certificate)
                mutate(tampered)
                with self.assertRaises(AssertionError):
                    CHECKER.validate_certificate_schema(tampered)

    def test_independent_report_tampers_are_rejected(self) -> None:
        def symbolic(payload):
            payload["symbolic_checks"] = {"tampered": True}

        def frobenius(payload):
            payload["frobenius_recomputations"][0]["affine_counts_r1_r3"] = [-1, -1, -1]

        def comparison(payload):
            payload["frobenius_recomputations"][0]["producer_comparisons"]["affine_counts_match"] = False

        def runtime(payload):
            payload["runtime_seconds"] = -1.0

        for name, mutate in {
            "symbolic body": symbolic,
            "Frobenius body": frobenius,
            "comparison flag": comparison,
            "negative runtime": runtime,
        }.items():
            with self.subTest(name=name):
                tampered = copy.deepcopy(self.independent)
                mutate(tampered)
                with self.assertRaises(AssertionError):
                    CHECKER.validate_independent_report(
                        tampered,
                        self.certificate,
                        self.certificate_bytes,
                        expected_symbolic=self.independent["symbolic_checks"],
                    )

    def test_neighbor_certificate_schema_and_tampers(self) -> None:
        def extra_key(payload):
            payload["unexpected"] = True

        def good_reduction_overclaim(payload):
            payload["claim_boundary"]["selected_prime_good_reduction_claimed"] = True

        def degree_pattern(payload):
            payload["symbolic"]["subresultant_reduction"][-1]["zero_mod_Px"] = False

        def control_roots(payload):
            payload["regular_split_fibre_control"]["roots"][0] = 9

        for name, mutate in {
            "extra key": extra_key,
            "selected-prime good-reduction overclaim": good_reduction_overclaim,
            "subresultant degree pattern": degree_pattern,
            "F43 control roots": control_roots,
        }.items():
            with self.subTest(name=name):
                tampered = copy.deepcopy(self.neighbor_certificate)
                mutate(tampered)
                with self.assertRaises(AssertionError):
                    NEIGHBOR_CHECKER.validate_neighbor_certificate_schema(tampered)

        tampered_hash = copy.deepcopy(self.neighbor_certificate)
        tampered_hash["symbolic"]["quadratic_subresultant_sha256"] = "0" * 64
        NEIGHBOR_CHECKER.validate_neighbor_certificate_schema(tampered_hash)
        with self.assertRaises(AssertionError):
            NEIGHBOR_CHECKER.compare_certificate_to_audit(
                tampered_hash,
                self.neighbor_independent["verified_certificate_content"],
            )

    def test_neighbor_independent_report_tampers_are_rejected(self) -> None:
        def verified_body(payload):
            payload["verified_certificate_content"]["regular_split_fibre_control"]["exact_tau_order"] = 1

        def source_hash(payload):
            payload["source_certificate"]["sha256"] = "0" * 64

        def runtime(payload):
            payload["runtime_seconds"] = -1.0

        for name, mutate in {
            "verified body": verified_body,
            "source hash": source_hash,
            "negative runtime": runtime,
        }.items():
            with self.subTest(name=name):
                tampered = copy.deepcopy(self.neighbor_independent)
                mutate(tampered)
                with self.assertRaises(AssertionError):
                    NEIGHBOR_CHECKER.validate_neighbor_independent_report(
                        tampered,
                        self.neighbor_certificate,
                        self.neighbor_certificate_bytes,
                    )


if __name__ == "__main__":
    unittest.main()
