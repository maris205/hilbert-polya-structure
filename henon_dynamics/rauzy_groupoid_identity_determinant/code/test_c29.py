#!/usr/bin/env python3
"""Regression and mutation tests for the HCS-C29 Phase-2 certificate.

The producer and checker are deliberately loaded as separate modules.  The
checker performs its own graph reconstruction and exact arithmetic.  During
this test suite its expensive length-nine census is computed once and then
deep-copied for mutation tests; the command-line checker does not use this
cache and always recomputes the census from scratch.
"""

from __future__ import annotations

import copy
import ast
import hashlib
import importlib.util
import json
import random
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


CODE = Path(__file__).resolve().parent
PROJECT = CODE.parent


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


producer = load_module("c29_producer_under_test", CODE / "c29_producer.py")
checker = load_module("c29_checker_under_test", CODE / "c29_independent_check.py")
manifest = load_module("c29_manifest_under_test", CODE / "c29_hash_manifest.py")


def canonical_sha256(value: object) -> str:
    """Independent canonical serializer used only by the mutation harness."""

    encoded = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


class C29ExactCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temporary_directory = tempfile.TemporaryDirectory(prefix="c29-tests-")
        cls.temp = Path(cls.temporary_directory.name)
        cls.certificate = producer.run()
        cls.certificate_path = cls.temp / "certificate.json"
        cls._write(cls.certificate, cls.certificate_path)

        # One genuinely independent exact length-nine census per test run.
        cls.original_exact_census = checker.exact_census
        census_cache: dict[tuple[str, int], object] = {}

        def cached_exact_census(darts, max_length=9):
            key = (canonical_sha256(darts), max_length)
            if key not in census_cache:
                census_cache[key] = cls.original_exact_census(darts, max_length)
            return copy.deepcopy(census_cache[key])

        checker.exact_census = cached_exact_census
        cls.base_report = checker.run(cls.certificate_path)

    @classmethod
    def tearDownClass(cls) -> None:
        checker.exact_census = cls.original_exact_census
        cls.temporary_directory.cleanup()

    @staticmethod
    def _write(value: object, path: Path) -> None:
        path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    def mutated(self, mutation, *, refresh_payload_hash: bool = True) -> dict[str, object]:
        value = copy.deepcopy(self.certificate)
        mutation(value["payload"])
        if refresh_payload_hash:
            value["payload_sha256"] = canonical_sha256(value["payload"])
        return value

    def assert_checker_rejects(
        self,
        mutation,
        expected_gate: str,
        *,
        refresh_payload_hash: bool = True,
    ) -> None:
        value = self.mutated(mutation, refresh_payload_hash=refresh_payload_hash)
        path = self.temp / f"mutation-{expected_gate}.json"
        self._write(value, path)
        with self.assertRaises(checker.GateFailure) as caught:
            checker.run(path)
        gates = getattr(caught.exception, "audit_gates", {})
        self.assertEqual(gates.get(expected_gate), "FAIL", f"unexpected gate map: {gates}")

    def test_01_independent_replay_passes_all_fourteen_gates(self) -> None:
        self.assertTrue(self.base_report["all_pass"])
        self.assertEqual(len(self.base_report["gates"]), 14)
        self.assertEqual(set(self.base_report["gates"].values()), {"PASS"})
        self.assertEqual(self.base_report["payload_sha256"], self.certificate["payload_sha256"])

    def test_02_producer_is_deterministic_and_environment_free(self) -> None:
        replay = producer.run()
        self.assertEqual(replay, self.certificate)
        runtime = replay["payload"]["runtime"]
        self.assertFalse(runtime["environment_fields_in_canonical_payload"])
        serialized = json.dumps(replay, sort_keys=True)
        for forbidden in ("platform.platform", "python_version", "hostname", "cwd"):
            self.assertNotIn(forbidden, serialized)

    def test_03_exact_c25_census_keeps_all_and_primitive_categories_separate(self) -> None:
        census = self.certificate["payload"]["c25_identity_census"]
        expected_marked = [0, 0, 0, 0, 0, 24, 0, 32, 144]
        self.assertEqual(census["all_marked_identity"], expected_marked)
        self.assertEqual(census["primitive_marked_identity"], expected_marked)
        self.assertEqual(census["determinant_moments_use"], "all_marked_identity")
        self.assertTrue(census["primitive_filter_is_not_used_for_N_n"])
        self.assertEqual(census["exact_log_coefficient_u6"], {"numerator": -4, "denominator": 1})

    def test_04_c25_witnesses_are_primitive_nonbacktracking_identity_cycles(self) -> None:
        witnesses = self.certificate["payload"]["c25_identity_witnesses"]
        for name in ("C1", "C2"):
            witness = witnesses[name]
            self.assertEqual(witness["length"], 6)
            self.assertTrue(witness["closed"])
            self.assertTrue(witness["linear_nonbacktracking"])
            self.assertTrue(witness["cyclic_nonbacktracking"])
            self.assertTrue(witness["primitive"])
            self.assertTrue(witness["identity_holonomy"])
            self.assertFalse(witness["inverse_is_rotation"])
        self.assertEqual(witnesses["proof_level_marked_lower_bound_N6"], 24)

    def test_05_c26_relation_is_derived_and_only_gives_a_lower_bound(self) -> None:
        relation = self.certificate["payload"]["c26_branch_relation"]
        self.assertTrue(relation["factorization"]["B_equals_AHA"])
        self.assertTrue(relation["factorization"]["C_equals_AKA"])
        self.assertTrue(relation["rank_one_braid"]["KYK_equals_YKY"])
        self.assertTrue(relation["word_derivation"]["derived_not_postulated"])
        self.assertEqual(relation["word_checks"]["length"], 24)
        self.assertTrue(relation["word_checks"]["cyclically_reduced"])
        self.assertTrue(relation["word_checks"]["primitive"])
        self.assertTrue(relation["word_checks"]["identity_product"])
        self.assertEqual(relation["marked_identity_lower_bound_N24"], 48)
        self.assertFalse(relation["N24_C26_is_exact_total"])

    def test_06_repetition_and_torsion_are_not_miscounted(self) -> None:
        repetitions = self.certificate["payload"]["repetition_controls"]
        identity = repetitions["identity_repetition"]
        torsion = repetitions["torsion_repetition"]
        self.assertTrue(identity["enters_all_cycle_moment"])
        self.assertFalse(identity["enters_primitive_census"])
        self.assertFalse(identity["primitive"])
        self.assertTrue(torsion["Delta_fourth_power_identity"])
        self.assertEqual(torsion["correct_character_atom"], "Theta_p(Delta^4)")
        self.assertEqual(torsion["forbidden_replacement"], "Theta_p(Delta)^4")

    def test_07_normalized_determinant_is_only_a_log0_germ(self) -> None:
        determinant = self.certificate["payload"]["normalized_determinant_germ"]
        self.assertEqual(determinant["common_strict_disc"], "|u|<1/5")
        self.assertEqual(determinant["N_n_definition"], "all marked cyclically nonbacktracking closed paths with identity holonomy")
        self.assertFalse(determinant["ordinary_infinite_dimensional_Fredholm_claimed"])
        self.assertFalse(determinant["positive_Fuglede_Kadison_claimed"])
        self.assertFalse(determinant["finite_order_primitive_factor"]["global_Euler_product_claimed"])

    def test_08_route_and_natural_extension_firewalls_are_explicit(self) -> None:
        payload = self.certificate["payload"]
        natural = payload["natural_extension_control"]
        scope = payload["scope_decisions"]
        self.assertEqual(natural["result"], "POSITIVE_PERIODIC_PRODUCT_GERM_ONE")
        self.assertFalse(natural["two_sided_transfer_operator_constructed"])
        self.assertEqual(natural["symmetric_object_scope"], "NEW_SYMMETRIC_DYNAMICS_NOT_NATURAL_EXTENSION")
        self.assertEqual(scope["route_A_promotion"], "STOP_BEFORE_INTRINSIC_ROOF_AND_TWO_SIDED_TRACE_THEOREM")
        self.assertFalse(scope["route_B_authorized"])
        self.assertFalse(scope["xi_divisor_or_RH_claimed"])

    def test_09_integer_inverse_implementations_agree_on_unimodular_fuzz(self) -> None:
        rng = random.Random(290811)
        for _ in range(250):
            matrix = producer.eye()
            for _ in range(12):
                target, source = rng.sample(range(4), 2)
                coefficient = rng.choice((-3, -2, -1, 1, 2, 3))
                elementary = producer.eye()
                elementary[target][source] = coefficient
                matrix = producer.matmul(elementary, matrix)
            inverse_a = producer.inverse_unimodular(matrix)
            tuple_matrix = tuple(tuple(row) for row in matrix)
            inverse_b = checker.inverse_unimodular(tuple_matrix)
            self.assertEqual(tuple(tuple(row) for row in inverse_a), inverse_b)
            self.assertEqual(producer.matmul(matrix, inverse_a), producer.eye())

    def test_10_runner_and_manifest_are_fail_closed(self) -> None:
        runner = (CODE / "run_c29.sh").read_text(encoding="utf-8")
        guarded = "if [[ $refresh_manifest == true ]]"
        write_call = 'c29_hash_manifest.py" --write'
        self.assertIn(guarded, runner)
        self.assertIn(write_call, runner)
        self.assertGreater(runner.index(write_call), runner.index(guarded))
        self.assertIn("PYTHONDONTWRITEBYTECODE=1", runner)
        self.assertIn("python3 -I -S -B", runner)
        self.assertIn("mktemp -d", runner)
        self.assertIn("cmp \"$c29_temp_dir/c29_certificate.json\"", runner)
        tracked = manifest.tracked_files()
        self.assertNotIn(manifest.MANIFEST, tracked)
        self.assertFalse(any("__pycache__" in path.parts for path in tracked))

    def test_11_stale_payload_digest_is_rejected(self) -> None:
        self.assert_checker_rejects(
            lambda p: p.__setitem__("candidate_name", "tampered"),
            "G13_payload_envelope",
            refresh_payload_hash=False,
        )

    def test_12_source_lock_mutation_is_rejected_after_rehash(self) -> None:
        def mutate(payload):
            payload["source_lock"]["files"]["C25_certificate"]["sha256"] = "0" * 64

        self.assert_checker_rejects(mutate, "G0_source_lock")

    def test_13_formal_inverse_opposite_edge_collapse_is_rejected(self) -> None:
        def mutate(payload):
            payload["c25_graph_reconstruction"]["formal_inverse_opposite_arrow_sentinel"]["positive_edge_id_retained"] = "3b"

        self.assert_checker_rejects(mutate, "G3_formal_inverse_semantics")

    def test_14_chronology_mutation_is_rejected(self) -> None:
        def mutate(payload):
            payload["conventions"]["chronology_id"] = "WRITTEN_ORDER_LEFT_TO_RIGHT"

        self.assert_checker_rejects(mutate, "G4_chronology")

    def test_15_identity_witness_token_mutation_is_rejected(self) -> None:
        def mutate(payload):
            payload["c25_identity_witnesses"]["C1"]["tokens_path_order"][-1] = "3b"

        self.assert_checker_rejects(mutate, "G6_C25_exact_witnesses_and_gauge")

    def test_16_primitive_moment_substitution_is_rejected(self) -> None:
        def mutate(payload):
            payload["c25_identity_census"]["determinant_moments_use"] = "primitive_marked_identity"

        self.assert_checker_rejects(mutate, "G7_all_vs_primitive_census")

    def test_17_c26_matrix_mutation_is_rejected(self) -> None:
        def mutate(payload):
            payload["c26_branch_relation"]["matrices"]["Delta"][0][0] += 1

        self.assert_checker_rejects(mutate, "G8_C26_braid_and_length24_relation")

    def test_18_c26_total_count_overclaim_is_rejected(self) -> None:
        def mutate(payload):
            payload["c26_branch_relation"]["N24_C26_is_exact_total"] = True

        self.assert_checker_rejects(mutate, "G8_C26_braid_and_length24_relation")

    def test_19_character_power_repetition_error_is_rejected(self) -> None:
        def mutate(payload):
            payload["repetition_controls"]["torsion_repetition"]["correct_character_atom"] = "Theta_p(Delta)^4"

        self.assert_checker_rejects(mutate, "G9_repetition_and_torsion")

    def test_20_prime_limit_order_mutation_is_rejected(self) -> None:
        def mutate(payload):
            payload["finite_weil_limit"]["fixed_length_before_prime_limit"] = False

        self.assert_checker_rejects(mutate, "G10_finite_weil_fixed_length_limit")

    def test_21_ordinary_fredholm_overclaim_is_rejected(self) -> None:
        def mutate(payload):
            payload["normalized_determinant_germ"]["ordinary_infinite_dimensional_Fredholm_claimed"] = True

        self.assert_checker_rejects(mutate, "G11_normalized_Log0_determinant")

    def test_22_global_euler_product_overclaim_is_rejected(self) -> None:
        def mutate(payload):
            payload["normalized_determinant_germ"]["finite_order_primitive_factor"]["global_Euler_product_claimed"] = True

        self.assert_checker_rejects(mutate, "G11_normalized_Log0_determinant")

    def test_23_natural_extension_identity_claim_is_rejected(self) -> None:
        def mutate(payload):
            payload["natural_extension_control"]["symmetric_object_scope"] = "GENUINE_AGY_NATURAL_EXTENSION"

        self.assert_checker_rejects(mutate, "G12_semantic_scope_firewalls")

    def test_24_intrinsic_roof_overclaim_is_rejected(self) -> None:
        def mutate(payload):
            payload["scope_decisions"]["intrinsic_inverse_AGY_roof_constructed"] = True

        self.assert_checker_rejects(mutate, "G12_semantic_scope_firewalls")

    def test_25_unknown_payload_field_is_rejected(self) -> None:
        def mutate(payload):
            payload["unreviewed_claim"] = True

        self.assert_checker_rejects(mutate, "G12_semantic_scope_firewalls")

    def test_26_json_integer_to_boolean_matrix_mutation_is_rejected(self) -> None:
        def mutate(payload):
            payload["c26_branch_relation"]["matrices"]["K"][0][0] = True

        self.assert_checker_rejects(mutate, "G8_C26_braid_and_length24_relation")

    def test_27_json_integer_to_float_matrix_mutation_is_rejected(self) -> None:
        def mutate(payload):
            value = payload["c26_branch_relation"]["matrices"]["A"][0][0]
            payload["c26_branch_relation"]["matrices"]["A"][0][0] = float(value)

        self.assert_checker_rejects(mutate, "G8_C26_braid_and_length24_relation")

    def test_28_material_passport_mutation_is_rejected(self) -> None:
        def mutate(payload):
            payload["material_passport"]["AI_assistance_disclosure_required"] = False

        self.assert_checker_rejects(mutate, "G12_semantic_scope_firewalls")

    def test_29_prime_scope_mutation_is_rejected(self) -> None:
        def mutate(payload):
            payload["source_lock"]["prime_scope"] = "all primes and all lengths simultaneously"

        self.assert_checker_rejects(mutate, "G0_source_lock")

    def test_30_runtime_environment_field_is_rejected(self) -> None:
        def mutate(payload):
            payload["runtime"]["cwd"] = "/tmp/unreviewed"

        self.assert_checker_rejects(mutate, "G12_semantic_scope_firewalls")

    def test_31_unknown_graph_field_is_rejected(self) -> None:
        def mutate(payload):
            payload["c25_graph_reconstruction"]["unreviewed_count"] = 28

        self.assert_checker_rejects(mutate, "G3_formal_inverse_semantics")

    def test_32_unknown_witness_field_is_rejected(self) -> None:
        def mutate(payload):
            payload["c25_identity_witnesses"]["unreviewed_class"] = "C3"

        self.assert_checker_rejects(mutate, "G6_C25_exact_witnesses_and_gauge")

    def test_33_checker_report_does_not_embed_input_path(self) -> None:
        second = self.temp / "different-root" / "renamed-certificate.json"
        second.parent.mkdir(parents=True)
        self._write(self.certificate, second)
        replay = checker.run(second)
        self.assertEqual(replay, self.base_report)
        self.assertNotIn("certificate", replay)

    def test_34_manifest_tracks_unknown_release_files_and_excludes_caches(self) -> None:
        root = self.temp / "manifest-tree"
        for relative in manifest.REQUIRED_RELATIVE_PATHS:
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"required:{relative}\n", encoding="utf-8")
        unknown = root / "UNLISTED_RELEASE_NOTE.md"
        unknown.write_text("must be tracked\n", encoding="utf-8")
        excluded = [
            root / "code" / "__pycache__" / "old.pyc",
            root / "paper" / "build" / "ignored.pdf",
            root / "paper" / "example.run.xml",
            root / "paper" / "example.synctex.gz",
            root / ".env.local",
            root / "code" / "native.pyd",
            root / ".venv" / "private.dat",
        ]
        for path in excluded:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b"cache")
        original_project, original_manifest = manifest.PROJECT, manifest.MANIFEST
        try:
            manifest.PROJECT = root
            manifest.MANIFEST = root / "results" / "ARTIFACT_HASHES.sha256"
            tracked = manifest.tracked_files()
        finally:
            manifest.PROJECT, manifest.MANIFEST = original_project, original_manifest
        self.assertIn(unknown, tracked)
        self.assertTrue(all(path not in tracked for path in excluded))

    def test_35_manifest_refresh_rejects_missing_required_artifact(self) -> None:
        root = self.temp / "manifest-missing"
        omitted = "PHASE2_SOURCE_VERIFICATION.md"
        for relative in manifest.REQUIRED_RELATIVE_PATHS - {omitted}:
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"required:{relative}\n", encoding="utf-8")
        original_project, original_manifest = manifest.PROJECT, manifest.MANIFEST
        try:
            manifest.PROJECT = root
            manifest.MANIFEST = root / "results" / "ARTIFACT_HASHES.sha256"
            with self.assertRaises(SystemExit) as caught:
                manifest.tracked_files()
        finally:
            manifest.PROJECT, manifest.MANIFEST = original_project, original_manifest
        self.assertIn(omitted, str(caught.exception))

    def test_36_manifest_detects_protected_file_change(self) -> None:
        root = self.temp / "manifest-change"
        for relative in manifest.REQUIRED_RELATIVE_PATHS:
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(f"required:{relative}\n", encoding="utf-8")
        original_project, original_manifest = manifest.PROJECT, manifest.MANIFEST
        try:
            manifest.PROJECT = root
            manifest.MANIFEST = root / "results" / "ARTIFACT_HASHES.sha256"
            before = manifest.render()
            (root / "THEOREM_PACKAGE.md").write_text("changed\n", encoding="utf-8")
            after = manifest.render()
        finally:
            manifest.PROJECT, manifest.MANIFEST = original_project, original_manifest
        self.assertNotEqual(before, after)

    def test_37_checker_import_firewall_is_ast_locked(self) -> None:
        source = (CODE / "c29_independent_check.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        allowed_roots = {
            "__future__",
            "argparse",
            "hashlib",
            "json",
            "collections",
            "fractions",
            "pathlib",
            "typing",
        }
        imported_roots: set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                imported_roots.add((node.module or "").split(".")[0])
            elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotIn(node.func.id, {"eval", "exec", "__import__"})
        self.assertLessEqual(imported_roots, allowed_roots)
        self.assertNotIn("c29_producer", imported_roots)
        self.assertNotIn("importlib", imported_roots)

    def test_38_checker_cli_pass_and_fail_are_regression_locked(self) -> None:
        executable = [sys.executable, "-I", "-S", "-B", str(CODE / "c29_independent_check.py")]
        pass_output = self.temp / "cli-pass.json"
        passed = subprocess.run(
            [*executable, "--certificate", str(self.certificate_path), "--output", str(pass_output)],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(passed.returncode, 0, passed.stderr)
        self.assertTrue(json.loads(pass_output.read_text(encoding="utf-8"))["all_pass"])

        failed_certificate = self.mutated(
            lambda payload: payload["source_lock"].__setitem__("prime_scope", "tampered")
        )
        failed_path = self.temp / "cli-fail-certificate.json"
        failed_output = self.temp / "cli-fail-report.json"
        self._write(failed_certificate, failed_path)
        failed = subprocess.run(
            [*executable, "--certificate", str(failed_path), "--output", str(failed_output)],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(failed.returncode, 1)
        failure_report = json.loads(failed_output.read_text(encoding="utf-8"))
        self.assertFalse(failure_report["all_pass"])
        self.assertEqual(failure_report["gates"].get("G0_source_lock"), "FAIL")


if __name__ == "__main__":
    unittest.main()
