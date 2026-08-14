#!/usr/bin/env python3
"""Mutation, strict-JSON, mathematical, and atomicity tests for HCS-C54."""

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
CHECKER_PATH = CODE / "c54_checker.py"
PRODUCER_PATH = CODE / "c54_producer.py"
ATOMIC_PATH = CODE / "c54_atomic_promote.py"


def load_module(name: str, path: Path):
    specification = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(specification)
    assert specification.loader is not None
    specification.loader.exec_module(module)
    return module


checker = load_module("c54_checker_for_tests", CHECKER_PATH)
atomic = load_module("c54_atomic_for_tests", ATOMIC_PATH)


def canonical_json(value) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def assign_path(root, path: tuple, value) -> None:
    target = root
    for component in path[:-1]:
        target = target[component]
    target[path[-1]] = value


def semantic_mutant(value):
    if type(value) is bool:
        return not value
    if type(value) is int:
        return value + 1
    if type(value) is str:
        return value + "__MUTATED"
    if type(value) is list:
        return value + ["__MUTATED"]
    if type(value) is dict:
        changed = copy.deepcopy(value)
        changed["__MUTATED"] = False
        return changed
    raise TypeError(type(value))


MUTATIONS = {
    "closing_edge": (("source_family", "closing_edge_coefficient"), "1"),
    "phase_normalization": (("full_projective_monomial_group", "phase_normalization"), "e_i arbitrary"),
    "quadric_scale_arbitrary": (("full_projective_monomial_group", "phase_and_scale_derivation", "quadric_scale_in_mu3"), False),
    "missing_edge_ratio_derivation": (("full_projective_monomial_group", "phase_and_scale_derivation", "quadric_edge_ratio_step"), "assume scale=rho^q"),
    "ideal_line_lemma": (("full_projective_monomial_group", "ideal_to_equation_lines", "both_equation_lines_preserved"), False),
    "edge_recurrence": (("full_projective_monomial_group", "edge_recurrence"), "e_(j+1)=q-e_j"),
    "closure_parity": (("full_projective_monomial_group", "closure_condition"), "every cycle support closes"),
    "group_order": (("full_projective_monomial_group", "order"), "2n"),
    "support_rotation_count": (("full_projective_monomial_group", "surviving_support_counts", "rotations"), "2n"),
    "rotation_order": (("full_projective_monomial_group", "generators", "r_exact_order"), "n"),
    "dihedral_relation": (("full_projective_monomial_group", "generators", "srs"), "r"),
    "nonmonomial_claim": (("full_projective_monomial_group", "nonmonomial_automorphisms_classified"), True),
    "delta_s": (("rational_group_form", "delta_s"), "s"),
    "fixed_count": (("rational_group_form", "Q_rational_point_count"), 6),
    "constant_group_scheme": (("rational_group_form", "group_scheme"), "constant Q-group scheme"),
    "rotation_only_average": (("rational_group_form", "Reynolds", "graphs_used"), "3n rotations"),
    "reynolds_denominator": (("rational_group_form", "Reynolds", "denominator"), "3n"),
    "transfer_denominator": (("rational_group_form", "quadratic_transfer", "denominator"), 6),
    "merge_denominators": (("rational_group_form", "quadratic_transfer", "distinct_from_Reynolds_denominator"), False),
    "certify_n5": (("claim_scope", "certified_packet_rows"), [2, 3, 4, 5]),
    "semisimple_packet_definition": (("claim_scope", "packet_admissibility_definition"), "actual semisimple compatible systems"),
    "claim_c53_semisimple": (("claim_scope", "C53_semisimplicity_claimed"), True),
    "assume_source_semisimple": (("split_denominator_rigidity", "restriction_argument", "source_semisimplicity_assumed"), True),
    "omit_semisimplification": (("split_denominator_rigidity", "restriction_argument", "semisimplification_passage"), "not needed"),
    "weight_collapse": (("split_denominator_rigidity", "packet_weights", "O_n"), 0),
    "rank_relation": (("split_denominator_rigidity", "packet_ranks", "relation"), "o_n=e_n"),
    "old_exponent": (("split_denominator_rigidity", "split_exponent_after_Q_descent"), "2/n"),
    "K0_identity": (("split_denominator_rigidity", "restriction_argument", "K0_identity"), "n[V]=2[E]+2[O]"),
    "purity_separation": (("split_denominator_rigidity", "restriction_argument", "pure_weight_separation"), False),
    "accept_total_rank": (("split_denominator_rigidity", "total_rank_trap_n3", "proof_route_accepted"), True),
    "retain_n8": (("split_denominator_rigidity", "surviving_rows"), [2, 4, 8]),
    "direct_converse": (("split_denominator_rigidity", "converse_matches_every_power_trace"), False),
    "claim_n5_packet": (("split_denominator_rigidity", "n_ge_5_packet_status"), "CONSTRUCTED"),
    "globalize_split": (("split_denominator_rigidity", "global_fractional_root_claimed"), True),
    "inert_square": (("split_denominator_rigidity", "inert_factor_generally_square_claimed"), True),
    "cayley_dimension": (("n3_equivariant_character", "cayley_jacobian", "quotient_dimension_H21"), 19),
    "residue_orientation": (("n3_equivariant_character", "cayley_jacobian", "residue_action_factor"), "det(A_g)/det(M_g)"),
    "scalar_lift": (("n3_equivariant_character", "cayley_jacobian", "projective_scalar_lift_invariant"), False),
    "H21_trace": (("n3_equivariant_character", "H21_character", "rotation_traces_k0_to_k8"), [20, 0, -1, 2, -1, -1, 2, -1, -1]),
    "O3_multiplicity": (("n3_equivariant_character", "O3_character", "irreducible_multiplicities", "U3"), 3),
    "rational_orbit_split": (("n3_equivariant_character", "coefficient_field_orbit_blocks", 2, "sectors"), ["U1"]),
    "common_sector": (("n3_equivariant_character", "central_sector_test", "nonzero_common_integral_sector_exists"), True),
    "fermat_form_conflation": (("n3_equivariant_character", "rational_form_caveat", "Fermat_standard_Q_form_equals_M3_twisted_form_claimed"), True),
    "virtual_injective": (("counterpacket_firewall", "virtual_restriction_injective_claimed"), True),
    "counterpacket_category_overbroad": (("counterpacket_firewall", "K0_ss_category"), "all finite-dimensional G_Q representations"),
    "absolute_density_one": (("counterpacket_firewall", "Q_split_primes_absolute_density"), "1"),
    "wrong_relative_density": (("counterpacket_firewall", "trace_zero_hypothesis_density"), "absolute density one among all rational primes"),
    "generic_or_zero_kernel_example": (("counterpacket_firewall", "virtual_kernel_example"), "U-U tensor chi_(K/Q)"),
    "kernel_example_zero": (("counterpacket_firewall", "example_nonzero_virtual_class"), False),
    "kernel_example_restricts_nonzero": (("counterpacket_firewall", "example_restriction_zero"), False),
    "actual_counterpacket": (("counterpacket_firewall", "actual_invisible_counterpacket"), "nonzero twist"),
    "kernel_rank": (("counterpacket_firewall", "every_kernel_class_rank"), 1),
    "kernel_changes_rail": (("counterpacket_firewall", "kernel_can_change_K_rail_rank"), True),
    "full_PGL": (("exclusions", "full_PGL_automorphism_group"), True),
    "all_n_smooth": (("exclusions", "smoothness_all_n"), True),
    "automorphy": (("exclusions", "automorphy"), True),
    "functional_equation": (("exclusions", "functional_equation"), True),
    "RH": (("exclusions", "Riemann_hypothesis"), True),
    "fixed_prime": (("exclusions", "fixed_Frobenius_prime_theorem_input"), True),
    "source_lock": (("source_family", "C53_source_lock", "certificate_sha256"), "0" * 64),
    "source_semisimplicity_status": (("source_family", "C53_source_lock", "semisimplicity_certified_by_C53"), True),
    "source_implementation_commit": (("source_family", "C53_source_lock", "implementation_commit"), "208feef86365cd92ace8dad02904acff6623eeec"),
    "source_provenance_commit": (("source_family", "C53_source_lock", "provenance_commit"), "0" * 40),
    "source_route_path": (("source_family", "C53_source_lock", "route_path"), "live/route_a_evaluation.yaml"),
    "source_route_sha": (("source_family", "C53_source_lock", "route_sha256"), "0" * 64),
    "source_route_check_hash": (("source_family", "C53_source_lock", "route_release_tuple", "independent_check_sha256"), "0" * 64),
    "source_route_manifest_hash": (("source_family", "C53_source_lock", "route_release_tuple", "code_results_manifest_sha256"), "0" * 64),
    "source_route_lock_status": (("source_family", "C53_source_lock", "commit_lock_status"), "VERIFIED_LIVE_ROUTE_SUBSTRING"),
    "reconnaissance_promoted_to_input": (("primary_source_controls", "pre_c54_reconnaissance", "status"), "PRIMARY_THEOREM_INPUT"),
    "reconnaissance_counted_as_gate": (("primary_source_controls", "pre_c54_reconnaissance", "counts_as_source_or_semantic_proof_gate"), True),
    "artifact_status_regression": (("artifact_status",), "PREFREEZE"),
}


class CertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        certificate_path = Path(
            os.environ.get(
                "C54_CERTIFICATE", str(PROJECT / "results/c54_certificate.json")
            )
        )
        cls.raw = certificate_path.read_bytes()
        cls.certificate = checker.strict_load(cls.raw)

    def checker_subprocess(self, raw: bytes) -> subprocess.CompletedProcess:
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary) / "certificate.json"
            output = Path(temporary) / "check.json"
            source.write_bytes(raw)
            process = subprocess.run(
                [sys.executable, str(CHECKER_PATH), str(source), "--output", str(output)],
                capture_output=True,
                text=True,
                check=False,
            )
            if process.returncode != 0:
                self.assertFalse(output.exists())
            return process

    def test_000_valid_certificate(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "check.json"
            result = checker.verify(copy.deepcopy(self.certificate), self.raw)
            self.assertEqual(result["result"], "PASS")
            self.assertEqual(result["semantic_gate_count"], len(checker.GATE_NAMES))
            self.assertEqual(
                result["central_semantic_leaf_count"], len(checker.SEMANTIC_EXPECTED)
            )
            self.assertEqual(result["central_semantic_leaf_count"], 198)
            self.assertEqual(result["nonsemantic_allowlist_count"], 4)
            self.assertEqual(
                result["total_scalar_leaf_count"],
                result["central_semantic_leaf_count"]
                + result["derived_scalar_leaf_count"]
                + result["nonsemantic_allowlist_count"],
            )

    def test_001_duplicate_key_rejected(self):
        duplicate = self.raw.replace(
            b'  "schema":', b'  "schema": "duplicate",\n  "schema":', 1
        )
        process = self.checker_subprocess(duplicate)
        self.assertNotEqual(process.returncode, 0)
        self.assertIn("duplicate JSON key", process.stderr)

    def test_002_unknown_envelope_key_rejected(self):
        certificate = copy.deepcopy(self.certificate)
        certificate["unexpected"] = False
        process = self.checker_subprocess((json.dumps(certificate) + "\n").encode())
        self.assertNotEqual(process.returncode, 0)

    def test_003_unknown_payload_key_rejected(self):
        certificate = copy.deepcopy(self.certificate)
        certificate["payload"]["unexpected"] = False
        certificate["payload_sha256"] = hashlib.sha256(
            canonical_json(certificate["payload"]).encode()
        ).hexdigest()
        process = self.checker_subprocess((json.dumps(certificate) + "\n").encode())
        self.assertNotEqual(process.returncode, 0)

    def test_004_exact_json_type_lock(self):
        certificate = copy.deepcopy(self.certificate)
        certificate["payload"]["rational_group_form"]["Q_rational_point_count"] = 2.0
        certificate["payload_sha256"] = hashlib.sha256(
            canonical_json(certificate["payload"]).encode()
        ).hexdigest()
        process = self.checker_subprocess((json.dumps(certificate) + "\n").encode())
        self.assertNotEqual(process.returncode, 0)

    def test_005_internal_payload_digest_rejected(self):
        certificate = copy.deepcopy(self.certificate)
        certificate["payload_sha256"] = "0" * 64
        process = self.checker_subprocess((json.dumps(certificate) + "\n").encode())
        self.assertNotEqual(process.returncode, 0)

    def test_006_all_targeted_mutations_rejected_with_hash_and_schema_locks_rebound(self):
        # Bypass both immutable digests in-process.  Every targeted mutation
        # must still be rejected by a mathematical/scope assertion.
        original_hash = checker.EXPECTED_PAYLOAD_SHA256
        original_schema_hash = checker.EXPECTED_SCHEMA_SHA256
        try:
            for name, (path, value) in MUTATIONS.items():
                with self.subTest(name=name):
                    certificate = copy.deepcopy(self.certificate)
                    assign_path(certificate["payload"], path, value)
                    changed_hash = hashlib.sha256(
                        canonical_json(certificate["payload"]).encode()
                    ).hexdigest()
                    certificate["payload_sha256"] = changed_hash
                    checker.EXPECTED_PAYLOAD_SHA256 = changed_hash
                    checker.EXPECTED_SCHEMA_SHA256 = hashlib.sha256(
                        canonical_json(
                            checker.schema_descriptor(certificate["payload"])
                        ).encode()
                    ).hexdigest()
                    with self.assertRaises(AssertionError):
                        checker.verify(certificate, (json.dumps(certificate) + "\n").encode())
        finally:
            checker.EXPECTED_PAYLOAD_SHA256 = original_hash
            checker.EXPECTED_SCHEMA_SHA256 = original_schema_hash

    def test_007_checker_optimized_python_fails_closed_and_removes_stale_output(self):
        with tempfile.TemporaryDirectory() as temporary:
            source = Path(temporary) / "certificate.json"
            output = Path(temporary) / "check.json"
            source.write_bytes(self.raw)
            output.write_text('{"result":"PASS"}\n')
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

    def test_007a_every_semantic_scalar_leaf_rejects_with_both_digests_rebound(self):
        original_hash = checker.EXPECTED_PAYLOAD_SHA256
        original_schema_hash = checker.EXPECTED_SCHEMA_SHA256
        try:
            for path, expected in checker.SEMANTIC_EXPECTED.items():
                with self.subTest(path="/".join(map(str, path))):
                    certificate = copy.deepcopy(self.certificate)
                    assign_path(
                        certificate["payload"], path, semantic_mutant(expected)
                    )
                    changed_hash = hashlib.sha256(
                        canonical_json(certificate["payload"]).encode()
                    ).hexdigest()
                    certificate["payload_sha256"] = changed_hash
                    checker.EXPECTED_PAYLOAD_SHA256 = changed_hash
                    checker.EXPECTED_SCHEMA_SHA256 = hashlib.sha256(
                        canonical_json(
                            checker.schema_descriptor(certificate["payload"])
                        ).encode()
                    ).hexdigest()
                    with self.assertRaisesRegex(
                        AssertionError, "central semantic leaf mismatch"
                    ):
                        checker.verify(
                            certificate, (json.dumps(certificate) + "\n").encode()
                        )
        finally:
            checker.EXPECTED_PAYLOAD_SHA256 = original_hash
            checker.EXPECTED_SCHEMA_SHA256 = original_schema_hash

    def test_007b_every_scalar_leaf_has_an_explicit_disjoint_classification(self):
        actual = {path for path, _ in checker.scalar_leaves(self.certificate["payload"])}
        semantic = set(checker.SEMANTIC_EXPECTED)
        nonsemantic = set(checker.NONSEMANTIC_ALLOWLIST)
        derived = {path for path in actual if checker.is_derived_scalar_path(path)}
        self.assertEqual(len(actual), 1078)
        self.assertEqual(len(semantic), 198)
        self.assertEqual(len(nonsemantic), 4)
        self.assertFalse(semantic & nonsemantic)
        self.assertFalse((semantic | nonsemantic) & derived)
        self.assertEqual(actual, semantic | nonsemantic | derived)
        self.assertEqual(
            nonsemantic,
            {
                (
                    "primary_source_controls",
                    "pre_c54_reconnaissance",
                    "historical_sha256",
                    "theorem_planning_note",
                ),
                (
                    "primary_source_controls",
                    "pre_c54_reconnaissance",
                    "historical_sha256",
                    "architecture_planning_note",
                ),
                (
                    "primary_source_controls",
                    "pre_c54_reconnaissance",
                    "historical_sha256",
                    "general_group_exploration",
                ),
                (
                    "primary_source_controls",
                    "pre_c54_reconnaissance",
                    "historical_sha256",
                    "n3_exploration",
                ),
            },
        )
        self.assertEqual(
            checker.validate_scalar_inventory(self.certificate["payload"]),
            {
                "total": 1078,
                "semantic": 198,
                "derived": 876,
                "nonsemantic": 4,
            },
        )

    def test_008_checker_mutation_removes_stale_pass_output(self):
        with tempfile.TemporaryDirectory() as temporary:
            certificate = copy.deepcopy(self.certificate)
            certificate["payload"]["full_projective_monomial_group"]["order"] = "2n"
            certificate["payload_sha256"] = hashlib.sha256(
                canonical_json(certificate["payload"]).encode()
            ).hexdigest()
            source = Path(temporary) / "certificate.json"
            output = Path(temporary) / "check.json"
            source.write_text(json.dumps(certificate) + "\n")
            output.write_text('{"result":"PASS"}\n')
            process = subprocess.run(
                [sys.executable, str(CHECKER_PATH), str(source), "--output", str(output)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertNotEqual(process.returncode, 0)
            self.assertFalse(output.exists())

    def test_009_producer_optimized_python_fails_closed_and_removes_stale_output(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "certificate.json"
            output.write_text('{"payload":"stale"}\n')
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

    def test_010_runner_rejects_pythonoptimize_before_replay(self):
        environment = dict(os.environ)
        environment["PYTHONOPTIMIZE"] = "1"
        process = subprocess.run(
            [str(CODE / "run_c54.sh")],
            cwd=PROJECT,
            env=environment,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(process.returncode, 2)
        self.assertIn("PYTHONOPTIMIZE", process.stderr)


def make_mutation_test(name, path, value):
    def test(self):
        certificate = copy.deepcopy(self.certificate)
        assign_path(certificate["payload"], path, value)
        certificate["payload_sha256"] = hashlib.sha256(
            canonical_json(certificate["payload"]).encode()
        ).hexdigest()
        process = self.checker_subprocess((json.dumps(certificate) + "\n").encode())
        self.assertNotEqual(process.returncode, 0)

    test.__name__ = f"test_mutation_{name}"
    return test


for mutation_name, (mutation_path, mutation_value) in MUTATIONS.items():
    setattr(
        CertificateTests,
        f"test_mutation_{mutation_name}",
        make_mutation_test(mutation_name, mutation_path, mutation_value),
    )


class AtomicPromotionTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.sources = [self.root / f"source-{index}" for index in range(4)]
        self.targets = [self.root / f"target-{index}" for index in range(4)]
        for index, path in enumerate(self.sources):
            path.write_bytes(f"new-{index}".encode())
        for index, path in enumerate(self.targets):
            path.write_bytes(f"old-{index}".encode())

    def tearDown(self):
        self.temporary.cleanup()

    def pairs(self):
        return list(zip(self.sources, self.targets))

    def test_atomic_commit(self):
        self.assertTrue(atomic.promote(self.pairs()))
        self.assertEqual(
            [path.read_bytes() for path in self.targets],
            [b"new-0", b"new-1", b"new-2", b"new-3"],
        )

    def test_atomic_rollback_after_move_1(self):
        self.assertFalse(atomic.promote(self.pairs(), 1))
        self.assertEqual(
            [path.read_bytes() for path in self.targets],
            [b"old-0", b"old-1", b"old-2", b"old-3"],
        )

    def test_atomic_rollback_after_move_2(self):
        self.assertFalse(atomic.promote(self.pairs(), 2))
        self.assertEqual(
            [path.read_bytes() for path in self.targets],
            [b"old-0", b"old-1", b"old-2", b"old-3"],
        )

    def test_atomic_rollback_after_move_3(self):
        self.assertFalse(atomic.promote(self.pairs(), 3))
        self.assertEqual(
            [path.read_bytes() for path in self.targets],
            [b"old-0", b"old-1", b"old-2", b"old-3"],
        )

    def test_atomic_rollback_after_move_4(self):
        self.assertFalse(atomic.promote(self.pairs(), 4))
        self.assertEqual(
            [path.read_bytes() for path in self.targets],
            [b"old-0", b"old-1", b"old-2", b"old-3"],
        )

    def test_atomic_missing_target_restored_as_missing(self):
        self.targets[3].unlink()
        self.assertFalse(atomic.promote(self.pairs(), 4))
        self.assertEqual(self.targets[0].read_bytes(), b"old-0")
        self.assertEqual(self.targets[1].read_bytes(), b"old-1")
        self.assertEqual(self.targets[2].read_bytes(), b"old-2")
        self.assertFalse(self.targets[3].exists())

    def test_atomic_missing_source_changes_nothing(self):
        self.sources[1].unlink()
        self.assertFalse(atomic.promote(self.pairs()))
        self.assertEqual(
            [path.read_bytes() for path in self.targets],
            [b"old-0", b"old-1", b"old-2", b"old-3"],
        )

    def test_atomic_duplicate_target_rejected(self):
        with self.assertRaises(ValueError):
            atomic.promote([(self.sources[0], self.targets[0]), (self.sources[1], self.targets[0])])

    def test_atomic_invalid_failure_stage_rejected(self):
        with self.assertRaises(ValueError):
            atomic.promote(self.pairs(), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
