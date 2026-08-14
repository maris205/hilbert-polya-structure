#!/usr/bin/env python3
"""Fail-closed, mutation, scalar-inventory, and atomicity tests for HCS-C55."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


CODE = Path(__file__).resolve().parent
PROJECT = CODE.parent
CHECKER_PATH = CODE / "c55_checker.py"
PRODUCER_PATH = CODE / "c55_producer.py"
ATOMIC_PATH = CODE / "c55_atomic_promote.py"
RUNNER_PATH = CODE / "run_c55.sh"


def load_module(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(specification)
    if specification.loader is None:
        raise AssertionError("module loader unavailable")
    specification.loader.exec_module(module)
    return module


checker = load_module("c55_checker_for_tests", CHECKER_PATH)
atomic = load_module("c55_atomic_for_tests", ATOMIC_PATH)


def canonical_json(value) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def assign_path(root, path: tuple, value) -> None:
    target = root
    for component in path[:-1]:
        target = target[component]
    target[path[-1]] = value


def same_type_mutant(value):
    if type(value) is bool:
        return not value
    if type(value) is int:
        return value + 1
    if type(value) is str:
        return value + "__MUTATED"
    raise TypeError(f"no same-type scalar mutant for {type(value).__name__}")


class CertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        certificate_path = Path(
            os.environ.get(
                "C55_CERTIFICATE", str(PROJECT / "results/c55_certificate.json")
            )
        )
        cls.raw = certificate_path.read_bytes()
        cls.certificate = checker.strict_load(cls.raw)

    def rebound_verify(self, certificate):
        original_payload = checker.EXPECTED_PAYLOAD_SHA256
        original_schema = checker.EXPECTED_SCHEMA_SHA256
        try:
            payload_sha = hashlib.sha256(canonical_json(certificate["payload"])).hexdigest()
            certificate["payload_sha256"] = payload_sha
            checker.EXPECTED_PAYLOAD_SHA256 = payload_sha
            checker.EXPECTED_SCHEMA_SHA256 = hashlib.sha256(
                canonical_json(checker.schema_descriptor(certificate["payload"]))
            ).hexdigest()
            return checker.verify(certificate, canonical_json(certificate) + b"\n")
        finally:
            checker.EXPECTED_PAYLOAD_SHA256 = original_payload
            checker.EXPECTED_SCHEMA_SHA256 = original_schema

    def assert_rebound_rejected(self, path, value, pattern: str | None = None):
        certificate = copy.deepcopy(self.certificate)
        assign_path(certificate["payload"], path, value)
        context = (
            self.assertRaisesRegex(AssertionError, pattern)
            if pattern is not None
            else self.assertRaises(AssertionError)
        )
        with context:
            self.rebound_verify(certificate)

    def test_000_valid_certificate_and_executed_gate_equality(self):
        result = checker.verify(copy.deepcopy(self.certificate), self.raw)
        self.assertEqual(result["result"], "PASS")
        self.assertEqual(result["semantic_gate_count"], len(checker.GATE_NAMES))
        self.assertEqual(result["executed_gate_names"], list(checker.GATE_NAMES))
        self.assertEqual(result["central_semantic_leaf_count"], 292)
        self.assertEqual(result["derived_scalar_leaf_count"], 1296)
        self.assertEqual(result["nonsemantic_allowlist_count"], 1)
        self.assertEqual(result["total_scalar_leaf_count"], 1589)
        self.assertEqual(
            result["total_scalar_leaf_count"],
            result["central_semantic_leaf_count"]
            + result["derived_scalar_leaf_count"]
            + result["nonsemantic_allowlist_count"],
        )

    def test_001_duplicate_json_key_rejected(self):
        duplicate = self.raw.replace(
            b'  "schema":', b'  "schema": "duplicate",\n  "schema":', 1
        )
        with self.assertRaisesRegex(ValueError, "duplicate JSON key"):
            checker.strict_load(duplicate)

    def test_002_envelope_and_payload_schema_fail_closed(self):
        certificate = copy.deepcopy(self.certificate)
        certificate["unexpected"] = False
        with self.assertRaisesRegex(AssertionError, "envelope keys"):
            self.rebound_verify(certificate)
        certificate = copy.deepcopy(self.certificate)
        certificate["payload"]["unexpected"] = False
        with self.assertRaises(AssertionError):
            self.rebound_verify(certificate)
        certificate = copy.deepcopy(self.certificate)
        certificate["payload"]["twist_and_Hodge"]["twisted_weight"] = 3.0
        with self.assertRaises(AssertionError):
            self.rebound_verify(certificate)

    def test_003_every_central_scalar_rejects_after_payload_and_schema_rebind(self):
        leaves, central, derived, nonsemantic, _, _ = checker.central_inventory_rows(
            self.certificate["payload"]
        )
        self.assertEqual((len(leaves), len(central), len(derived), len(nonsemantic)), (1589, 292, 1296, 1))
        for path in sorted(central, key=repr):
            with self.subTest(path="/".join(map(str, path))):
                certificate = copy.deepcopy(self.certificate)
                assign_path(
                    certificate["payload"], path, same_type_mutant(leaves[path])
                )
                with self.assertRaisesRegex(
                    AssertionError, "central semantic projection mismatch"
                ):
                    self.rebound_verify(certificate)

    def test_004_only_architecture_hash_is_nonsemantic_chronology(self):
        certificate = copy.deepcopy(self.certificate)
        path = ("pre_release_chronology", "architecture_report_sha256")
        assign_path(certificate["payload"], path, "0" * 64)
        inventory = checker.validate_scalar_inventory(certificate["payload"])
        self.assertEqual(
            inventory,
            {"total": 1589, "central": 292, "derived": 1296, "nonsemantic": 1},
        )
        self.assertEqual(set(checker.NONSEMANTIC_ALLOWLIST), {path})

    def test_005_explicit_scope_and_role_overclaims_rebound_rejected(self):
        mutations = {
            "motive": (
                ("realization_firewalls", "finite_prime_matches_prove_motive"),
                True,
            ),
            "honest_CY3": (
                ("realization_firewalls", "honest_CY3_realization_claimed"),
                True,
            ),
            "fixed_Hilbert_four": (
                (
                    "complete_intersection_controls",
                    "fixed_Hilbert_tangent_dimension_claimed_to_be_four",
                ),
                True,
            ),
            "literal_family": (
                (
                    "equivariant_tangent",
                    "class_role_firewall",
                    "not_a_literal_linear_equivariant_family",
                ),
                False,
            ),
            "contracted_multiplication": (
                (
                    "equivariant_tangent",
                    "class_role_firewall",
                    "direct_multiplication_of_contracted_R_2_minus3_classes_used",
                ),
                True,
            ),
            "wrong_z_descent": (
                ("ambient_group_action_descent", "Cayley_extension", "D_z"),
                "rho^2*z",
            ),
            "wrong_raw_x_phase": (
                (
                    "cayley_Yukawa",
                    "top_line_semilinear_descent",
                    "compatibility_identity",
                ),
                "raw x6^2*x7^2 -> rho^2*x1^2*x2^2",
            ),
            "wrong_raw_z_power": (
                (
                    "cayley_Yukawa",
                    "top_line_semilinear_descent",
                    "compatibility_identity",
                ),
                "raw z^5 -> rho^2*z^4",
            ),
            "wrong_raw_total_prefactor": (
                (
                    "cayley_Yukawa",
                    "top_line_semilinear_descent",
                    "compatibility_identity",
                ),
                "raw total prefactor rho before quotient",
            ),
            "Q2": (("twist_and_Hodge", "Q2_twist_used"), True),
            "all_24_Q": (
                ("ambient_group_action_descent", "all_24_geometric_matrices_Q_rational"),
                True,
            ),
        }
        for name, (path, value) in mutations.items():
            with self.subTest(name=name):
                self.assert_rebound_rejected(
                    path, value, "central semantic projection mismatch"
                )

    def test_006_redundant_provenance_leaf_is_derived_but_exactly_bound(self):
        self.assert_rebound_rejected(
            (
                "source_lock",
                "committed_release_provenance",
                2,
                "tuple_authority",
            ),
            "mutable live tuple",
            "complete committed release tuple mutation",
        )

    def test_007_complete_tangent_operator_subtree_is_exactly_bound(self):
        self.assert_rebound_rejected(
            (
                "equivariant_tangent",
                "tangent_operator_component",
                "operator_classes",
            ),
            "[y^2*p_i]",
            "complete tangent operator certificate mutation",
        )

    def test_008_direct_cube_metadata_and_common_scale_are_bound(self):
        self.assert_rebound_rejected(
            ("cayley_Yukawa", "producer_direct_cube", "direct_reductions"),
            19,
            "direct-cube metadata mutation",
        )
        current = self.certificate["payload"]["rational_cubic_surface"][
            "common_K_trace_scale"
        ]["a"][0]
        self.assert_rebound_rejected(
            ("rational_cubic_surface", "common_K_trace_scale", "a", 0),
            current + 4,
            "common scale/top fixed generator mismatch",
        )

    def test_009_producer_smoothness_subtree_is_bound_after_independent_replay(self):
        self.assert_rebound_rejected(
            (
                "rational_cubic_surface",
                "producer_smoothness_backend",
                "ordering",
            ),
            "lex",
            "producer smoothness subtree mutation",
        )

    def test_010_checker_optimized_mode_and_stale_output_fail_closed(self):
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary) / "certificate.json"
            output = Path(temporary) / "check.json"
            source.write_bytes(self.raw)
            output.write_text('{"result":"PASS"}\n', encoding="utf-8")
            environment = dict(os.environ)
            environment["PYTHONOPTIMIZE"] = "1"
            process = subprocess.run(
                [sys.executable, str(CHECKER_PATH), str(source), "--output", str(output)],
                env=environment,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(process.returncode, 0)
            self.assertFalse(output.exists())
            self.assertIn("optimized Python", process.stderr)

    def test_011_producer_optimized_mode_and_stale_output_fail_closed(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "certificate.json"
            output.write_text('{"result":"STALE"}\n', encoding="utf-8")
            environment = dict(os.environ)
            environment["PYTHONOPTIMIZE"] = "1"
            process = subprocess.run(
                [sys.executable, str(PRODUCER_PATH), "--output", str(output)],
                env=environment,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(process.returncode, 0)
            self.assertFalse(output.exists())
            self.assertIn("optimized Python", process.stderr)

    def test_012_checker_failure_removes_stale_pass_output(self):
        with tempfile.TemporaryDirectory() as temporary:
            certificate = copy.deepcopy(self.certificate)
            certificate["payload"]["artifact_status"] = "PREFREEZE_PAPER_PENDING"
            source = Path(temporary) / "certificate.json"
            output = Path(temporary) / "check.json"
            source.write_bytes(canonical_json(certificate) + b"\n")
            output.write_text('{"result":"PASS"}\n', encoding="utf-8")
            process = subprocess.run(
                [sys.executable, str(CHECKER_PATH), str(source), "--output", str(output)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(process.returncode, 0)
            self.assertFalse(output.exists())

    def test_013_atomic_group_success_and_injected_rollback(self):
        # Eight rollback groups: existing versus initially absent targets,
        # crossed with injected failures after each of the four moves.
        for initially_existing in (True, False):
            for failure_stage in (1, 2, 3, 4):
                with self.subTest(
                    initially_existing=initially_existing,
                    failure_stage=failure_stage,
                ), tempfile.TemporaryDirectory() as temporary:
                    root = Path(temporary)
                    sources = [root / f"source-{index}" for index in range(4)]
                    targets = [root / f"target-{index}" for index in range(4)]
                    for index, source in enumerate(sources):
                        source.write_bytes(f"new-{index}".encode())
                    if initially_existing:
                        for index, target in enumerate(targets):
                            target.write_bytes(f"old-{index}".encode())
                    self.assertFalse(
                        atomic.promote(
                            list(zip(sources, targets)),
                            inject_failure_after=failure_stage,
                        )
                    )
                    if initially_existing:
                        self.assertEqual(
                            [target.read_bytes() for target in targets],
                            [f"old-{index}".encode() for index in range(4)],
                        )
                    else:
                        self.assertTrue(all(not target.exists() for target in targets))
                    self.assertFalse(list(root.glob(".*.new")))
                    self.assertFalse(list(root.glob(".*.bak")))

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            sources = [root / f"source-{index}" for index in range(4)]
            targets = [root / f"target-{index}" for index in range(4)]
            for index, (source, target) in enumerate(zip(sources, targets)):
                source.write_bytes(f"new-{index}".encode())
                target.write_bytes(f"old-{index}".encode())
            pairs = list(zip(sources, targets))
            self.assertTrue(atomic.promote(pairs))
            self.assertEqual(
                [target.read_bytes() for target in targets],
                [f"new-{index}".encode() for index in range(4)],
            )
            self.assertFalse(list(root.glob(".*.new")))
            self.assertFalse(list(root.glob(".*.bak")))
            with self.assertRaises(ValueError):
                atomic.promote([(sources[0], targets[0]), (sources[1], targets[0])])

    def test_014_runner_guards_optimized_mode_and_refresh_pairing(self):
        environment = dict(os.environ)
        environment["PYTHONOPTIMIZE"] = "1"
        process = subprocess.run(
            [str(RUNNER_PATH)],
            cwd=PROJECT,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(process.returncode, 2)
        self.assertIn("PYTHONOPTIMIZE", process.stderr)
        environment.pop("PYTHONOPTIMIZE")
        process = subprocess.run(
            [str(RUNNER_PATH), "--refresh-results"],
            cwd=PROJECT,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(process.returncode, 2)
        self.assertIn("requires --refresh-manifest", process.stderr)


if __name__ == "__main__":
    unittest.main()
