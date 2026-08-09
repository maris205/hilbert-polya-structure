import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from flint import arb, ctx
import yaml

from src import log_0001_lower_growth as lower


class Log0001LowerGrowthTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.report = lower.build_report()
        cls.root = Path(__file__).resolve().parents[1]

    def test_all_target_free_gates_pass(self) -> None:
        self.assertEqual(self.report["candidate_id"], "LOG-0001")
        self.assertEqual(
            self.report["audit_id"], "LOG-0001-LOWER-GROWTH"
        )
        self.assertTrue(self.report["formal_candidate"])
        self.assertTrue(self.report["computed_gates_passed"])
        self.assertTrue(all(self.report["computed_gates"].values()))
        firewall = self.report["data_firewall"]
        self.assertTrue(all(not value for value in firewall.values()))

    def test_exact_bracket_and_cauchy_geometry(self) -> None:
        exact = self.report["exact_bracket_and_cauchy_certificate"]
        self.assertEqual(exact["U_c_bracket_decimal_digits"], 100)
        self.assertEqual(exact["U_c_bracket_width"], "1/10^100")
        self.assertEqual(
            exact["critical_polynomial_derivative_discriminant"], -8
        )
        self.assertEqual(exact["lower_endpoint_polynomial_sign"], -1)
        self.assertEqual(exact["upper_endpoint_polynomial_sign"], 1)
        self.assertEqual(exact["safe_real_point"], 2)
        self.assertEqual(exact["Cauchy_radius"], "R-2")
        self.assertEqual(exact["radial_factor"], "1/2")
        self.assertTrue(all(exact["computed_gates"].values()))

    def test_arb_derivative_and_maximum_modulus_floors(self) -> None:
        intervals = self.report["arb_interval_certificate"]
        gates = intervals["computed_gates"]
        self.assertTrue(gates["c_2_is_above_published_derivative_floor"])
        self.assertTrue(gates["half_c_2_is_above_published_radial_floor"])
        self.assertGreaterEqual(
            intervals["c_2_relative_accuracy_bits"], 300
        )
        self.assertEqual(intervals["working_decimal_digits_floor"], 300)
        self.assertEqual(
            intervals["inherited_root_bracket_decimal_digits"], 100
        )
        self.assertGreater(
            arb(intervals["c_2_ball"]), arb(213) / 10000
        )
        self.assertGreater(
            arb(intervals["c_2_half_ball"]), arb(213) / 20000
        )
        before = ctx.prec
        try:
            ctx.prec = lower.ARB_BITS
            u = lower.root_ball()
            alpha_0 = u**2 / 4
            tau_star = -alpha_0.log()
            b_2 = -(1 - 2 * alpha_0**2).log() / (1 - alpha_0)
            c_2 = (-b_2).exp() * tau_star * alpha_0**2 / (1 - alpha_0)
            self.assertGreater(c_2, arb(213) / 10000)
            self.assertGreater(c_2 / 2, arb(213) / 20000)
            self.assertTrue(c_2.overlaps(arb(intervals["c_2_ball"])))
        finally:
            ctx.prec = before

    def test_same_object_signed_ledger_and_claim_boundary(self) -> None:
        ledger = self.report["analytic_ledger"]
        self.assertTrue(ledger["all_real_derivative_summands_strictly_positive"])
        self.assertTrue(ledger["orientation_signs_preserved"])
        self.assertTrue(
            ledger["retained_term_is_a_proof_lower_bound_not_a_truncation"]
        )
        self.assertEqual(ledger["pure_left_ledger"]["matching_factor"], 1)
        consequence = self.report["maximum_modulus_consequence"]
        self.assertTrue(consequence["transcendental_entire"])
        self.assertTrue(consequence["qualitative_super_polynomial_growth"])
        self.assertTrue(
            any(
                "positive or exact entire-function order" in item
                for item in self.report["claim_boundary"]["not_established"]
            )
        )

    def test_source_lock_and_route_a_boundary(self) -> None:
        lock = yaml.safe_load(
            (self.root / lower.SOURCE_LOCK).read_text(encoding="utf-8")
        )
        self.assertEqual(lock["candidate_id"], "LOG-0001")
        self.assertEqual(lock["audit_id"], "LOG-0001-LOWER-GROWTH")
        self.assertIn(
            "s_0=2", lock["candidate_definition"]["scalar_anchor"]
        )
        self.assertEqual(
            lock["cutoff"]["retained_lower_bound_term"],
            "n=1 pure-left based word L",
        )
        self.assertEqual(lock["precision"]["arb_bits"], 1024)
        self.assertEqual(lock["precision"]["python_version"], "3.12.3")
        self.assertEqual(
            lock["precision"]["derivative_safe_floor"], "0.0213"
        )
        self.assertEqual(
            lock["precision"]["radial_linear_safe_floor"], "0.01065"
        )
        self.assertEqual(
            lock["determinant_convention"]["candidate_determinant"],
            "D_pol(s)=Delta(1,s)",
        )
        self.assertIn(
            "T_gamma=sum tau=log|(G^n)'|",
            lock["clock"]["determinant_clock"],
        )
        forbidden = "\n".join(lock["forbidden_data"])
        self.assertIn("prime tables", forbidden)
        self.assertIn("Fredholm determinant values", forbidden)
        self.assertIn("auxiliary lambda expansion", forbidden)
        evaluation = yaml.safe_load(
            (self.root / lower.EVALUATION).read_text(encoding="utf-8")
        )
        self.assertEqual(
            evaluation["analytic_route_tuple"],
            [
                "A1_WEAK",
                "A2_ANALYTIC_DETERMINANT",
                "A3_PARTIAL_ANALYTIC_STRUCTURE",
                "A4_FAIL",
            ],
        )
        self.assertEqual(
            evaluation["riemann_target_tuple"],
            ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        )
        self.assertFalse(evaluation["route_b_invocation_allowed"])
        self.assertEqual(
            evaluation["a3"]["metrics"]["D_pol_prime_at_2"],
            ">0.0213",
        )

    def test_lock_evaluation_and_result_copies_are_identical(self) -> None:
        pairs = [
            (lower.SOURCE_LOCK, lower.COMPAT_SOURCE_LOCK),
            (lower.EVALUATION, lower.COMPAT_EVALUATION),
            (lower.FORMAL_RESULT, lower.COMPAT_FORMAL_RESULT),
        ]
        for primary, compatibility in pairs:
            self.assertEqual(
                (self.root / primary).read_bytes(),
                (self.root / compatibility).read_bytes(),
                f"copy drift: {primary} != {compatibility}",
            )

    def test_committed_artifact_reproduces_exactly(self) -> None:
        artifact = self.root / lower.ARTIFACT
        self.assertTrue(artifact.exists())
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "certificate.json"
            completed = subprocess.run(
                [
                    sys.executable,
                    lower.GENERATOR,
                    "--quiet",
                    "--output",
                    str(output),
                ],
                cwd=self.root,
                check=False,
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            self.assertEqual(output.read_bytes(), artifact.read_bytes())

    def test_artifact_hashes_and_environment(self) -> None:
        provenance = self.report["provenance"]
        environment = self.report["validated_environment"]
        self.assertFalse(provenance["external_target_data_used"])
        self.assertEqual(
            environment["python"], lower.EXPECTED_PYTHON_VERSION
        )
        self.assertEqual(
            environment["python_flint"], lower.EXPECTED_PYTHON_FLINT_VERSION
        )
        self.assertEqual(environment["flint"], lower.EXPECTED_FLINT_VERSION)
        self.assertEqual(environment["arb_bits"], lower.ARB_BITS)
        expected_inputs = {
            lower.SOURCE_LOCK,
            lower.COMPAT_SOURCE_LOCK,
            lower.FORMAL_RESULT,
            lower.COMPAT_FORMAL_RESULT,
            lower.EVALUATION,
            lower.COMPAT_EVALUATION,
            lower.INHERITED_GROWTH_ARTIFACT,
        }
        self.assertEqual(
            set(provenance["source_inputs_sha256"]), expected_inputs
        )
        for relative, expected in provenance["source_inputs_sha256"].items():
            actual = hashlib.sha256(
                (self.root / relative).read_bytes()
            ).hexdigest()
            self.assertEqual(actual, expected, relative)
        generator_hash = hashlib.sha256(
            (self.root / lower.GENERATOR).read_bytes()
        ).hexdigest()
        self.assertEqual(generator_hash, provenance["generator_sha256"])

    def test_generator_has_no_external_support_dependency(self) -> None:
        source = (self.root / lower.GENERATOR).read_text(encoding="utf-8")
        self.assertNotIn("p4_logistic_uc_first_return_support", source)
        self.assertNotIn("from experiments", source)
        self.assertNotIn("import experiments", source)
        self.assertEqual(
            self.report["self_contained_inputs"]["external_support_modules"],
            [],
        )
        self.assertTrue(
            self.report["self_contained_inputs"][
                "U_c_bracket_frozen_in_generator"
            ]
        )
        inherited = json.loads(
            (self.root / lower.INHERITED_GROWTH_ARTIFACT).read_text(
                encoding="utf-8"
            )
        )
        self.assertEqual(inherited["audit_id"], "LOG-0001-GROWTH-ORDER")
        self.assertFalse(
            inherited["data_firewall"]["Fredholm_determinant_evaluated"]
        )
        self.assertFalse(inherited["data_firewall"]["Riemann_zero_tables_used"])

    def test_convenience_artifact_matches_canonical_artifact(self) -> None:
        canonical = self.root / lower.ARTIFACT
        convenience = self.root / lower.CONVENIENCE_ARTIFACT
        self.assertTrue(canonical.exists())
        self.assertTrue(convenience.exists())
        self.assertEqual(canonical.read_bytes(), convenience.read_bytes())

    def test_arb_context_is_restored(self) -> None:
        before = ctx.prec
        lower.build_report()
        self.assertEqual(ctx.prec, before)


if __name__ == "__main__":
    unittest.main()
