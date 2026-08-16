#!/usr/bin/env python3
"""Hostile unit and transaction tests for the HCS-C58 machine package."""

from __future__ import annotations

import ast
import gzip
import io
from contextlib import redirect_stderr
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import c58_atomic_promote as atomic
import c58_checker as checker
import c58_group as group_helper
from c58_exact import (
    StrictDataError,
    canonical_json_bytes,
    deep_exact,
    deterministic_gzip,
    require_canonical_compact_json,
    strict_json_loads,
)
import c58_hash_manifest as manifest
import c58_producer as producer
import c58_pipeline as pipeline


CODE = Path(__file__).resolve().parent


def _literal_build_payload_field(name: str) -> object:
    """Read one literal firewall from the producer without running its math."""
    tree = ast.parse((CODE / "c58_producer.py").read_text(encoding="utf-8"))
    functions = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "build_payload"
    ]
    if len(functions) != 1:
        raise AssertionError("producer must define exactly one build_payload")
    matches = []
    for node in ast.walk(functions[0]):
        if not isinstance(node, ast.Return) or not isinstance(node.value, ast.Dict):
            continue
        for key, value in zip(node.value.keys, node.value.values):
            if isinstance(key, ast.Constant) and key.value == name:
                matches.append(ast.literal_eval(value))
    if len(matches) != 1:
        raise AssertionError(f"producer payload must contain one literal {name}")
    return matches[0]


def _literal_dict_shape(node: ast.AST) -> dict[str, object] | None:
    """Return literal dictionary-key structure; dynamic values are wildcards."""
    if not isinstance(node, ast.Dict):
        return None
    result: dict[str, object] = {}
    for key, value in zip(node.keys, node.values):
        if key is None:
            result["**dynamic_merge"] = None
            continue
        if not isinstance(key, ast.Constant) or not isinstance(key.value, str):
            raise AssertionError("payload dictionaries must use literal string keys")
        result[key.value] = _literal_dict_shape(value)
    return result


def _payload_shape(path: Path, function_name: str, *, assigned_name: str | None) -> dict[str, object]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    functions = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == function_name
    ]
    if len(functions) != 1:
        raise AssertionError(f"expected exactly one {function_name}")
    candidates: list[ast.AST] = []
    for node in ast.walk(functions[0]):
        if assigned_name is None and isinstance(node, ast.Return):
            candidates.append(node.value)
        elif assigned_name is not None and isinstance(node, ast.Assign):
            if any(
                isinstance(target, ast.Name) and target.id == assigned_name
                for target in node.targets
            ):
                candidates.append(node.value)
    shaped = [shape for node in candidates if (shape := _literal_dict_shape(node)) is not None]
    if len(shaped) != 1:
        raise AssertionError(f"expected one literal payload dictionary in {function_name}")
    return shaped[0]


def _assert_compatible_literal_shapes(
    case: unittest.TestCase, left: object, right: object, path: str = "payload"
) -> None:
    """Dynamic leaves are wildcards; two literal dictionaries must agree exactly."""
    if not isinstance(left, dict) or not isinstance(right, dict):
        return
    case.assertEqual(set(left), set(right), path)
    for key in left:
        _assert_compatible_literal_shapes(case, left[key], right[key], f"{path}/{key}")


def _semantic_diff_count(left: object, right: object) -> int:
    """Count strict structural/leaf disagreements (including bool/int type drift)."""
    if type(left) is not type(right):
        return 1
    if isinstance(left, dict):
        left_keys = set(left)
        right_keys = set(right)  # type: ignore[arg-type]
        return len(left_keys ^ right_keys) + sum(
            _semantic_diff_count(left[key], right[key])  # type: ignore[index]
            for key in left_keys & right_keys
        )
    if isinstance(left, list):
        right_list = right  # type: ignore[assignment]
        return abs(len(left) - len(right_list)) + sum(
            _semantic_diff_count(a, b) for a, b in zip(left, right_list)
        )
    return 0 if left == right else 1


class StrictDataTests(unittest.TestCase):
    def test_noncanonical_integer_and_duplicate_rejected(self) -> None:
        for raw in (b'{"x":-0}', b'{"x":01}', b'{"x":1.0}', b'{"x":1,"x":2}'):
            with self.assertRaises(StrictDataError):
                strict_json_loads(raw, max_bytes=100)

    def test_bool_is_not_integer_under_deep_exact(self) -> None:
        self.assertFalse(deep_exact(True, 1))
        self.assertFalse(deep_exact({"x": [1]}, {"x": [True]}))

    def test_hundred_thousand_digit_integer(self) -> None:
        raw = b'{"x":' + b"9" * 100_000 + b"}"
        value = strict_json_loads(raw, max_bytes=len(raw))
        self.assertIs(type(value["x"]), int)

    def test_deterministic_gzip_and_compact_json(self) -> None:
        raw = canonical_json_bytes({"b": [1, 2], "a": False})
        require_canonical_compact_json(raw)
        first = deterministic_gzip(raw)
        second = deterministic_gzip(raw)
        self.assertEqual(first, second)
        self.assertEqual(int.from_bytes(first[4:8], "little"), 0)
        with gzip.GzipFile(fileobj=io.BytesIO(first), mode="rb") as stream:
            self.assertEqual(stream.read(), raw)


class SourceArchitectureTests(unittest.TestCase):
    def test_exact_code_allowlist(self) -> None:
        observed = {path.name for path in CODE.iterdir()}
        self.assertEqual(observed, set(manifest.CODE_NAMES))
        self.assertEqual(checker.CODE_SOURCE_NAMES, set(manifest.CODE_NAMES))
        self.assertEqual(producer.CODE_SOURCE_NAMES, set(manifest.CODE_NAMES))
        self.assertEqual(len(observed), 14)
        self.assertNotIn("__pycache__", observed)

    def test_no_duplicate_literal_dict_keys(self) -> None:
        for name in manifest.CODE_NAMES:
            if not name.endswith(".py"):
                continue
            tree = ast.parse((CODE / name).read_text(encoding="utf-8"), filename=name)
            for node in ast.walk(tree):
                if not isinstance(node, ast.Dict):
                    continue
                keys = [
                    key.value
                    for key in node.keys
                    if isinstance(key, ast.Constant) and isinstance(key.value, str)
                ]
                self.assertEqual(len(keys), len(set(keys)), (name, node.lineno))

    def test_checker_call_graph_is_independent(self) -> None:
        tree = ast.parse((CODE / "c58_checker.py").read_text(encoding="utf-8"))
        forbidden_modules = {
            "c58_producer",
            "c58_group",
            "c58_arithmetic",
            "c58_surface",
        }
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                self.assertFalse({alias.name for alias in node.names} & forbidden_modules)
            if isinstance(node, ast.ImportFrom):
                self.assertNotIn(node.module, forbidden_modules)

        producer_tree = ast.parse(
            (CODE / "c58_producer.py").read_text(encoding="utf-8")
        )
        for node in ast.walk(producer_tree):
            if isinstance(node, ast.Import):
                self.assertNotIn(
                    "c58_checker", {alias.name for alias in node.names}
                )
            if isinstance(node, ast.ImportFrom):
                self.assertNotEqual(node.module, "c58_checker")

    def test_checker_pari_scratch_is_bound_to_verified_shared_parent(self) -> None:
        source = (CODE / "c58_checker.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        temporary_calls = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "tempfile"
            and node.func.attr == "TemporaryDirectory"
        ]
        self.assertEqual(len(temporary_calls), 1)
        temporary = temporary_calls[0]
        self.assertEqual(temporary.args, [])
        keywords = {keyword.arg: keyword.value for keyword in temporary.keywords}
        self.assertEqual(set(keywords), {"dir", "prefix"})
        self.assertIsInstance(keywords["prefix"], ast.Constant)
        self.assertEqual(keywords["prefix"].value, ".c58-checker-pari-")
        self.assertIsInstance(keywords["dir"], ast.Name)
        self.assertEqual(keywords["dir"].id, "scratch_parent")

        replay_calls = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "pari_replay"
        ]
        self.assertEqual(len(replay_calls), 1)
        self.assertIsInstance(replay_calls[0].args[-1], ast.Name)
        self.assertEqual(replay_calls[0].args[-1].id, "shared_parent")
        self.assertIn("not scratch_parent.is_absolute()", source)
        self.assertIn(
            "scratch_parent.resolve(strict=True) != scratch_parent", source
        )
        self.assertIn("shared_parent.resolve(strict=True) != shared_parent", source)
        for token in (
            "request_fingerprint_before",
            "request_fingerprint_after",
            "request_identity_before",
            "request_identity_after",
            "request_metadata_before.st_dev",
            "request_metadata_before.st_ino",
            "request_metadata_before.st_nlink",
            "request_metadata_after.st_dev",
            "request_metadata_after.st_ino",
            "request_metadata_after.st_nlink",
        ):
            self.assertIn(token, source)
        self.assertNotIn('TemporaryDirectory(prefix="c58-checker-pari-")', source)

    def test_checker_pari_request_inode_substitution_is_rejected(self) -> None:
        transformed = [1, 0, 1]
        basis = [[[1, 1]]]
        image_authority = {
            "common_denominator": 1,
            "numerators_low_to_high": [0],
        }
        evidence = {
            "degree36_local_factors": {"delta36": {}, "theta36": {}},
            "field_isomorphism": {
                "original_generator_image_canonical_sha256": checker.sha256_bytes(
                    checker.canonical_leaf_bytes(image_authority)
                ),
                "original_generator_image_common_denominator": 1,
                "original_generator_image_numerators_low_to_high": [0],
            },
            "local_prime_ideals": {
                str(prime): [] for prime in checker.DIRECT_PRIMES
            },
            "maximal_order": {
                "integral_basis_canonical_sha256": checker.sha256_bytes(
                    checker.canonical_leaf_bytes(basis)
                ),
                "integral_basis_coefficients_low_to_high_as_num_den": basis,
                "transformed_monic_polynomial_coefficients_low_to_high": transformed,
                "transformed_monic_polynomial_sha256": checker.sha256_bytes(
                    checker.canonical_leaf_bytes(transformed)
                ),
            },
            "padic_factor_degrees": {},
        }

        def substitute_request(_python, _script, arguments, **_keywords):
            request = Path(arguments[0])
            metadata = request.stat(follow_symlinks=False)
            replacement = request.with_name("foreign-request.json")
            replacement.write_bytes(request.read_bytes())
            replacement.chmod(stat.S_IMODE(metadata.st_mode))
            os.utime(
                replacement,
                ns=(metadata.st_atime_ns, metadata.st_mtime_ns),
            )
            os.replace(replacement, request)
            return {}, "0" * 64

        with tempfile.TemporaryDirectory() as temporary:
            scratch_parent = Path(temporary).resolve(strict=True)
            with (
                patch.object(
                    checker,
                    "run_canonical_report",
                    side_effect=substitute_request,
                ),
                self.assertRaisesRegex(
                    StrictDataError, "request changed across child replay"
                ),
            ):
                checker.pari_replay(
                    evidence,
                    [1, 0, 1],
                    {"delta36": [1, 1], "theta36": [1, 1]},
                    Path("/usr/bin/python3"),
                    scratch_parent,
                )

    def test_v2_gap_deep_pairs_and_order_two_class_map(self) -> None:
        evidence = strict_json_loads(
            (CODE.parent / "results/c58_group_evidence.json").read_bytes(),
            max_bytes=1_000_000,
        )
        validated = checker.validate_group_evidence(evidence)
        rich = validated["group_report"]
        deep = rich["p3"]["deep_C3_exhaustion"]
        self.assertEqual([row["tom_index"] for row in deep["profiles"]], [6, 7, 8])
        self.assertEqual(deep["selected_tom_index"], 7)
        self.assertEqual(
            deep["selected_profile_tame_action_by_inertia_tom_index"],
            {"140": "inversion", "142": "central"},
        )
        pair_rows = rich["p3"]["deep_C3_pair_normal_multiplicities"]
        self.assertEqual(
            [
                (row["decomposition_tom_index"], row["inertia_tom_index"])
                for row in pair_rows
            ],
            [(140, 140), (142, 142), (206, 140), (206, 142)],
        )
        for row in pair_rows:
            selected = next(
                profile for profile in row["profiles"] if profile["tom_index"] == 7
            )
            self.assertEqual(selected["normal_in_inertia_multiplicity"], 1)
            self.assertEqual(selected["normal_in_decomposition_multiplicity"], 1)
            self.assertEqual(
                selected["nonnegative_integer_solution_multiset"], [[1, 6]]
            )
            expected_action = (
                "inversion" if row["inertia_tom_index"] == 140 else "central"
            )
            self.assertEqual(selected["tame_actions"], [[expected_action, 1]])
        exhaustion = rich["tom_dual_action_exhaustion"]
        self.assertEqual(
            exhaustion["p3_valid_decomposition_inertia_pairs"],
            [[140, 140, 1], [142, 142, 1], [206, 140, 2], [206, 142, 2]],
        )
        self.assertEqual(
            exhaustion["p5_valid_decomposition_inertia_pairs"], [[147, 147, 1]]
        )
        self.assertEqual(
            [
                (
                    row["tom_index"],
                    row["character_table_element_class_index"],
                    row["element_class_size"],
                    row["normalizer_order"],
                    row["fixed_dimensions_V6_V20"],
                )
                for row in rich["order_two_tom_profiles"]
            ],
            [
                (2, 16, 36, 1440, [5, 15]),
                (3, 2, 45, 1152, [2, 12]),
                (4, 3, 270, 192, [4, 12]),
                (5, 17, 540, 96, [3, 11]),
            ],
        )

    def test_v2_pari_signature_polsturm_and_wild_theta_authority(self) -> None:
        arithmetic = strict_json_loads(
            gzip.decompress(
                (CODE.parent / "results/c58_arithmetic_evidence.json.gz").read_bytes()
            ),
            max_bytes=8_000_000,
        )
        validated = checker.validate_arithmetic_evidence(arithmetic)
        self.assertEqual(validated["archimedean"]["field_signature"], [3, 12])
        self.assertEqual(
            validated["archimedean"]["complex_conjugation_element_class_index"],
            17,
        )
        wild = validated["wild_degree36_theta_authority"]
        self.assertEqual(wild["certified_precisions"], [900, 950, 1000])
        self.assertEqual(wild["authority_role"], "KRASNER_CERTIFIED_AUTHORITY")
        for prime in ("3", "5"):
            row = wild["prime_records"][prime]
            self.assertIs(row["authority_bound_satisfied"], True)
            self.assertIs(row["factor_rows_stable_across_precisions"], True)
            self.assertEqual(row["factor_krasner_bounds_satisfied"], [True] * 3)
            self.assertEqual(row["resolver_separation_bounds_satisfied"], [True] * 3)
            self.assertEqual(
                row["minimum_multiplyback_valuations"], [900, 950, 1000]
            )
        pari_source = (CODE / "c58_checker_pari.py").read_text(encoding="utf-8")
        self.assertIn("nf.nf_get_sign()", pari_source)
        self.assertIn("pari.polsturm(resolver)", pari_source)

    def test_v2_reflection_hensel_six_boolean_bridge(self) -> None:
        arithmetic = strict_json_loads(
            gzip.decompress(
                (CODE.parent / "results/c58_arithmetic_evidence.json.gz").read_bytes()
            ),
            max_bytes=8_000_000,
        )
        self.assertEqual(
            checker.reflection_hensel_semantics(arithmetic),
            {
                "affine_hessian_units": True,
                "critical_points_hensel_lift_uniquely": True,
                "critical_values_congruent_to_integer_witness_mod_p_squared": True,
                "residue_characteristics_odd": True,
                "smoothing_parameter_valuation_exactly_one": True,
                "unique_geometric_singular_point_each_prime": True,
            },
        )

    def test_v2_ctbllib_131_preflight_and_cache_guard(self) -> None:
        self.assertEqual(
            pipeline.EXPECTED_GAP,
            {
                "resolved_executable": "/usr/bin/gap",
                "executable_sha256": "9aa736f13150c363d7c31d33513d849482dd52692e7534f51ecfac0d303bb1e3",
                "executable_size_bytes": 1942,
                "gap_version": "4.11.1",
                "tomlib_version": "1.2.9",
                "smallgrp_version": "1.4.1",
                "ctbllib_version": "1.3.1",
            },
        )
        pipeline_source = (CODE / "c58_pipeline.py").read_text(encoding="utf-8")
        gap_source = (CODE / "c58_checker_group.g").read_text(encoding="utf-8")
        self.assertIn('PackageInfo("ctbllib")[1].Version', pipeline_source)
        self.assertIn('LoadPackage("ctbllib")', gap_source)
        self.assertNotIn("__pycache__", {path.name for path in CODE.iterdir()})

    def test_producer_checker_payload_shapes_are_exact(self) -> None:
        expected = (
            "C58_source_contract",
            "G0_upstream_source_lock",
            "G1_bad_prime_exhaustion",
            "G2_local_order_exact",
            "G3_dual_action_classification",
            "G4_filtered_inertia",
            "G5_character_conductors",
            "G6_global_and_infinity",
            "G7_replay_and_scope",
            "artifact_contract",
            "backends",
            "documentation_contract",
            "nonresults_firewall",
            "scope_firewall",
            "status_contract",
        )
        self.assertEqual(checker.PAYLOAD_KEYS, expected)
        self.assertEqual(producer.PAYLOAD_KEYS, expected)
        producer_shape = _payload_shape(
            CODE / "c58_producer.py", "build_payload", assigned_name=None
        )
        checker_shape = _payload_shape(
            CODE / "c58_checker.py", "expected_payload", assigned_name="payload"
        )
        _assert_compatible_literal_shapes(self, producer_shape, checker_shape)
        checker_tree = ast.parse(
            (CODE / "c58_checker.py").read_text(encoding="utf-8")
        )
        rebound_function = next(
            node
            for node in checker_tree.body
            if isinstance(node, ast.FunctionDef)
            and node.name == "actual_verifier_rebound"
        )
        rebound_string_literals = {
            node.value
            for node in ast.walk(rebound_function)
            if isinstance(node, ast.Constant) and isinstance(node.value, str)
        }
        self.assertIn("tame_theta36_local_rows", rebound_string_literals)
        self.assertNotIn("theta36_local_rows", rebound_string_literals)

    def test_actual_payload_builders_match_on_one_shared_fixture(self) -> None:
        source = {"schema_id": "sentinel-source"}
        upstream = {"schema_id": "sentinel-upstream"}
        artifacts = {"schema_id": "sentinel-artifacts"}
        backends = {"schema_id": "sentinel-backends"}
        arithmetic = strict_json_loads(
            gzip.decompress(
                (CODE.parent / "results/c58_arithmetic_evidence.json.gz").read_bytes()
            ),
            max_bytes=8_000_000,
        )
        group_evidence = strict_json_loads(
            (CODE.parent / "results/c58_group_evidence.json").read_bytes(),
            max_bytes=1_000_000,
        )
        factorization = arithmetic["macaulay"]["factorization"]
        divided_sha = "2" * 64
        local_ideals_sha = "3" * 64
        field_sha = arithmetic["field_discriminant"]["decimal_newline_sha256"]
        reflections = arithmetic["reflection_witnesses"]
        reflection_sha = producer.sha256_bytes(
            producer.canonical_leaf_bytes(reflections)
        )
        A = 181 * 997 * 2346241
        B = 283 * 1801 * producer.Q
        conductor6_value = 3**11 * 5**7 * A**6 * B
        conductor20_value = 3**35 * 5**29 * A**12 * B**5
        self.assertEqual(
            arithmetic["field_discriminant"]["value"],
            conductor6_value * conductor20_value,
        )
        report_shas = {
            "arithmetic": "5" * 64,
            "group": "6" * 64,
            "surface_bareiss": "7" * 64,
            "surface_flint": "8" * 64,
        }
        reports = {
            "arithmetic": {
                "report": {
                    "basis_reused_exactly": True,
                    "degree36_hensel_product_congruences": {
                        "theta": {
                            str(prime): [20, 30, 40]
                            for prime in producer.DIRECT_PRIMES
                        }
                    },
                    "field_discriminant_decimal_newline_sha256": field_sha,
                    "field_discriminant_exponents_on_surface_bad_prime_envelope": list(
                        producer.FIELD_EXPONENTS
                    ),
                    "generator_image_proves_oriented_field_identity": True,
                    "line_field_signature": [3, 12],
                    "local_prime_ideals_sha256": local_ideals_sha,
                    "nfcertify_unresolved": [],
                    "surface_bad_prime_envelope_isprime": [True] * 9,
                    "theta36_real_root_count": 4,
                    "wild_degree36_theta_authority": arithmetic[
                        "wild_degree36_theta_authority"
                    ],
                },
                "report_sha256": report_shas["arithmetic"],
            },
            "group": {"report": {"status": "PASS"}, "report_sha256": report_shas["group"]},
            "surface_bareiss": {
                "report": {"status": "PASS"},
                "report_sha256": report_shas["surface_bareiss"],
            },
            "surface_flint": {
                "report": {
                    "divided_discriminant_decimal_newline_sha256": divided_sha,
                    "reflection_affine_hessian_units": True,
                    "reflection_chart0_reduced_point_bases_verified": True,
                    "reflection_critical_points_hensel_lift_uniquely": True,
                    "reflection_critical_values_congruent_to_integer_witness_mod_p_squared": True,
                    "reflection_residue_characteristics_odd": True,
                    "reflection_smoothing_parameter_valuation_exactly_one": True,
                    "reflection_unique_geometric_singular_point_each_prime": True,
                    "reflection_witnesses_sha256": reflection_sha,
                    "status": "PASS",
                },
                "report_sha256": report_shas["surface_flint"],
            },
        }
        with (
            patch.object(producer, "source_contract", return_value=source),
            patch.object(producer, "upstream_source_lock", return_value=upstream),
            patch.object(
                producer,
                "artifact_contract",
                return_value=(artifacts, arithmetic, group_evidence),
            ),
            patch.object(producer, "normalized_backends", return_value=backends),
            patch.object(producer, "exact_reports", return_value=reports),
        ):
            produced = producer.build_payload(
                Path("/fixture"), Path("/pari"), Path("/flint"), Path("/gap")
            )

        producer_g2 = produced["G2_local_order_exact"]
        producer_g4 = produced["G4_filtered_inertia"]
        producer_g5 = produced["G5_character_conductors"]
        producer_g6 = produced["G6_global_and_infinity"]
        pari_report = {
            "basis_reused_exactly": producer_g2["basis_reused_exactly"],
            "degree36_hensel_product_congruences": {
                "theta": {
                    str(prime): [20, 30, 40] for prime in checker.DIRECT_PRIMES
                }
            },
            "field_discriminant_decimal_newline_sha256": producer_g2[
                "field_discriminant_decimal_newline_sha256"
            ],
            "field_discriminant_exponents_on_surface_bad_prime_envelope": producer_g2[
                "field_discriminant_exponents_on_surface_bad_prime_envelope"
            ],
            "generator_image_proves_oriented_field_identity": producer_g2[
                "generator_image_proves_oriented_field_identity"
            ],
            "local_prime_ideals_sha256": producer_g2["local_prime_ideals_sha256"],
            "nfcertify_unresolved": producer_g2["nfcertify_unresolved"],
            "surface_bad_prime_envelope_isprime": [True] * 9,
        }
        rich_group = group_evidence["group_report"]
        compact_group = group_helper.compact_report(b"fixture\n", group_evidence)
        checker_group = {
            **group_helper.payload_group_projection(rich_group),
            "complex_conjugation_character_mapping": rich_group[
                "complex_conjugation"
            ]["character_table_match"],
            "deep_C3_exhaustion": compact_group["p3_deep_C3_exhaustion"],
            "deep_C3_normal_in_all_surviving_decomposition_groups": compact_group[
                "p3_deep_C3_normal_in_all_surviving_decomposition_groups"
            ],
            "line_action_faithful": rich_group["counts"]["line_action_faithful"],
            "order2_profiles": rich_group["order_two_tom_profiles"],
            "p3_all_tom_decomposition_pattern_hits": compact_group[
                "p3_all_tom_decomposition_pattern_hits"
            ],
            "p3_tame_quotient_filter_excludes_206_as_inertia": True,
            "p3_valid_decomposition_inertia_pairs": compact_group[
                "p3_valid_decomposition_inertia_pairs"
            ],
            "p5_all_tom_decomposition_pattern_hits": compact_group[
                "p5_all_tom_decomposition_pattern_hits"
            ],
            "p5_filtration_equation": compact_group["p5_filtration_equation"],
            "p5_valid_decomposition_inertia_pairs": compact_group[
                "p5_valid_decomposition_inertia_pairs"
            ],
            "p5_wild_normalizer_filter_unique": compact_group[
                "p5_wild_normalizer_filter_unique"
            ],
        }
        pari_report.update(
            {
                "field_signature": [3, 12],
                "theta36_real_root_count": 4,
                "wild_degree36_theta_authority": arithmetic[
                    "wild_degree36_theta_authority"
                ],
            }
        )
        global_report = {
            "archimedean": producer_g6["archimedean"],
            "archimedean_authority_chain": producer_g6[
                "archimedean_authority_chain"
            ],
            "conductors": {
                "V6": producer_g6["conductors"]["V6"],
                "V20": producer_g6["conductors"]["V20"],
            },
            "disc_E": producer_g6["disc_E"],
            "disc_K": producer_g6["disc_K"],
            "local": {
                "p3": {
                    "artin_V6_V20": producer_g5["p3"]["artin_V6_V20"],
                    "filtered_group_orders": producer_g4["p3"]["filtered_orders"],
                    "filtration_multiplicity_solution": producer_g4["p3"][
                        "filtration_multiplicity_solution"
                    ],
                    "swan_V6_V20": producer_g5["p3"]["swan_V6_V20"],
                },
                "p5": {
                    "artin_V6_V20": producer_g5["p5"]["artin_V6_V20"],
                    "filtered_group_orders": producer_g4["p5"]["filtered_orders"],
                    "filtration_multiplicity_solution": producer_g4["p5"][
                        "filtration_multiplicity_solution"
                    ],
                    "swan_V6_V20": producer_g5["p5"]["swan_V6_V20"],
                },
                "reflection_C2": producer_g5["reflection_C2"],
                "tame_C3": producer_g5["tame_C3"],
            },
            "normal_closure_ramified_support": producer_g6[
                "normal_closure_ramified_support"
            ],
            "reflection_picard_lefschetz_bridge": producer_g4[
                "reflection_picard_lefschetz_bridge"
            ],
            "serre_p3": {
                "deep_break": producer_g4["p3"]["serre_last_nonzero_grade"],
                "required_action": producer_g4["p3"]["serre_required_action"],
            },
            "support_exhausted_by_exact_DiscE_and_faithful_action": producer_g6[
                "support_exhausted_by_exact_DiscE_and_faithful_action"
            ],
        }
        rebuilt = checker.expected_payload(
            source_contract=source,
            g0=upstream,
            artifact_contract=artifacts,
            arithmetic=arithmetic,
            backends=backends,
            macaulay={
                "divided_discriminant_decimal_newline_sha256": divided_sha,
                "factorization": factorization,
            },
            reflections=reflections,
            pari_report=pari_report,
            pari_report_sha256="9" * 64,
            producer_exact_report_sha256=report_shas,
            group=checker_group,
            global_report=global_report,
        )
        diff_count = _semantic_diff_count(produced, rebuilt)
        self.assertTrue(deep_exact(produced, rebuilt), f"payload diff_count={diff_count}")
        self.assertEqual(diff_count, 0)
        schema = checker.schema_descriptor(rebuilt)
        schema_raw = checker.canonical_json_bytes(schema, pretty=True)
        envelope = {
            "canonical_schema_sha256": checker.sha256_bytes(
                checker.canonical_leaf_bytes(schema)
            ),
            "paper_status": "PAPER_PENDING",
            "payload": rebuilt,
            "payload_sha256": checker.sha256_bytes(
                checker.canonical_leaf_bytes(rebuilt)
            ),
            "schema_descriptor_id": "hcs-c58-certificate-schema-v1",
            "schema_id": "hcs-c58-certificate-v1",
            "schema_sha256": checker.sha256_bytes(schema_raw),
            "status": "PREFREEZE_CODE_RESULTS_PASS",
        }
        rebound = checker.actual_verifier_rebound(
            envelope, schema, rebuilt, schema
        )
        self.assertEqual(rebound["hostile_semantic_mutations"], 7)
        self.assertGreater(rebound["rebound_mutations_rejected"], 0)

    def test_scope_firewall_is_exact(self) -> None:
        self.assertEqual(
            _literal_build_payload_field("scope_firewall"),
            {
                "arithmetic_equivalence_claimed": False,
                "Artin_holomorphy_claimed": False,
                "automorphy_claimed": False,
                "bad_Euler_factors_beyond_filtered_inertia_claimed": False,
                "Brauer_Manin_obstruction_claimed": False,
                "Calabi_Yau_realization_claimed": False,
                "decomposition_Frobenius_claimed": False,
                "delta36_local_factorization_used_as_authority": False,
                "dynamics_claimed": False,
                "general_cubic_surface_theorem_claimed": False,
                "general_line_field_theorem_claimed": False,
                "Hilbert_Polya_operator_claimed": False,
                "local_epsilon_factors_claimed": False,
                "local_root_numbers_claimed": False,
                "p3_decomposition_order_unique_claimed": False,
                "paper_complete_claimed": False,
                "rational_or_local_points_claimed": False,
                "release_claimed": False,
                "Riemann_Hypothesis_claimed": False,
                "VHS_realization_claimed": False,
            },
        )

    def test_nonresults_firewall_is_closed(self) -> None:
        actual = _literal_build_payload_field("nonresults_firewall")
        self.assertIs(type(actual), dict)
        self.assertEqual(set(actual), {"delta36_local_lane", "p3_decomposition_order"})
        delta = actual["delta36_local_lane"]
        self.assertEqual(set(delta), {"certificate_dependency", "reason", "status"})
        self.assertIs(delta["certificate_dependency"], False)
        self.assertEqual(delta["status"], "BOUNDED_NON_RESULT_NONDEPENDENCY")
        self.assertRegex(
            delta["reason"],
            r"^precision_40_below_global_polynomial_discriminant_exponent_[1-9][0-9]*$",
        )
        p3 = actual["p3_decomposition_order"]
        self.assertEqual(
            p3,
            {
                "allowed_values": [18, 36],
                "character_conductor_dependency": False,
                "status": "UNRESOLVED_NONDEPENDENCY",
            },
        )

    def test_manifest_constants(self) -> None:
        manifest._validate_constants()
        self.assertEqual(len(manifest.SCOPED_RELATIVES), 21)
        self.assertEqual(len(manifest.LIVE_RELATIVES), 22)
        self.assertEqual(manifest.PROMOTED_NAMES, atomic.EXPECTED_TARGET_NAMES)
        self.assertEqual(checker.ARTIFACT_NAMES, manifest.PROMOTED_NAMES[:2])
        self.assertEqual(producer.ARTIFACT_NAMES, manifest.PROMOTED_NAMES[:2])

    def test_runner_has_explicit_three_state_postcommit_contract(self) -> None:
        source = (CODE / "run_all.sh").read_text(encoding="utf-8")
        for token in (
            'RUN_STATE="STAGED_VERIFIED"',
            'RUN_STATE="LIVE_COMMITTED"',
            'RUN_STATE="RELEASE_VERIFIED"',
            "POSTCOMMIT_INCOMPLETE",
            "COMMITTED_WITH_DEBRIS—DO NOT RETRY",
        ):
            self.assertIn(token, source)
        self.assertNotIn('exec /usr/bin/bash -p "$CODE_DIR/run_all.sh"', source)
        self.assertIn('/usr/bin/bash -p "$CODE_DIR/run_all.sh"', source)
        self.assertIn("PROMOTION_ACTIVE=1", source)
        self.assertIn(
            '--arithmetic-evidence "$STAGE_DIR/c58_arithmetic_evidence.json.gz"',
            source,
        )
        self.assertIn(
            '--group-evidence "$STAGE_DIR/c58_group_evidence.json"', source
        )
        self.assertIn('--gap "$GAP"', source)
        for token in (
            'exec {RESULTS_FD}<"$RESULTS_DIR"',
            'stat -Lc \'%d\' "/proc/self/fd/$RESULTS_FD"',
            'stat -Lc \'%i\' "/proc/self/fd/$RESULTS_FD"',
            "verify_results_binding()",
            "results pathname device/inode changed",
            "results parent identity changed; retaining all stage/transaction evidence",
        ):
            self.assertIn(token, source)
        self.assertGreaterEqual(source.count("verify_results_binding"), 20)
        atomic_call = source.index(
            '"$FLINT_GROUP_PYTHON" -s -B "$CODE_DIR/c58_atomic_promote.py" "${ATOMIC_ARGS[@]}"'
        )
        self.assertLess(
            source.rindex("verify_results_binding", 0, atomic_call), atomic_call
        )
        self.assertGreater(source.index("verify_results_binding", atomic_call), atomic_call)
        match = re.search(
            r"classify_promotion_status\(\) \{.*?^\}", source, flags=re.MULTILINE | re.DOTALL
        )
        self.assertIsNotNone(match)
        probe = (
            match.group(0)
            + "\nfor value in 0 74 75 1 2 129 137 143; do "
            + 'classify_promotion_status "$value"; printf "%s\\n" "$PROMOTION_CLASS"; done\n'
        )
        completed = subprocess.run(
            ["/usr/bin/bash", "-p", "-c", probe],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            env={"PATH": "/usr/bin:/bin"},
            cwd="/",
        )
        self.assertEqual(
            completed.stdout.splitlines(),
            [
                b"LIVE_COMMITTED",
                b"ROLLED_BACK_VERIFIED",
                b"LIVE_COMMITTED_WITH_DEBRIS",
                b"LIVE_STATE_UNCERTAIN",
                b"LIVE_STATE_UNCERTAIN",
                b"LIVE_STATE_UNCERTAIN",
                b"LIVE_STATE_UNCERTAIN",
                b"LIVE_STATE_UNCERTAIN",
            ],
        )
        handoff = source.index("PROMOTION_STATUS=$?")
        classification = source.index(
            'classify_promotion_status "$PROMOTION_STATUS"', handoff
        )
        state_assignment = source.index('RUN_STATE="LIVE_COMMITTED"', classification)
        active_clear = source.index("PROMOTION_ACTIVE=0", state_assignment)
        self.assertLess(handoff, classification)
        self.assertLess(classification, state_assignment)
        self.assertLess(state_assignment, active_clear)


def _write(path: Path, raw: bytes, mode: int, mtime_ns: int) -> None:
    path.write_bytes(raw)
    path.chmod(mode)
    os.utime(path, ns=(mtime_ns, mtime_ns))


def _snapshot(path: Path) -> tuple[bytes, int, int] | None:
    if not path.exists():
        return None
    metadata = path.stat()
    return path.read_bytes(), stat.S_IMODE(metadata.st_mode), metadata.st_mtime_ns


class AtomicPromotionTests(unittest.TestCase):
    def make_layout(self, root: Path, state: str) -> tuple[Path, Path, list[tuple[Path, str]], dict[str, tuple[bytes, int, int] | None]]:
        results = root / "results"
        results.mkdir()
        _write(results / "RESULTS.md", b"results\n", 0o644, 1_700_000_000_000_000_001)
        _write(results / "TEST_REPORT.md", b"tests\n", 0o644, 1_700_000_000_000_000_002)
        stage = results / ".c58-stage-unit"
        stage.mkdir()
        pairs = []
        before = {}
        for index, name in enumerate(atomic.EXPECTED_TARGET_NAMES):
            source = stage / name
            _write(
                source,
                f"new-{index}\n".encode(),
                0o600 + index % 4,
                1_710_000_000_000_000_000 + index,
            )
            target = results / name
            exists = state == "existing" or (state == "mixed" and index % 2 == 0)
            if exists:
                _write(
                    target,
                    f"old-{index}\n".encode(),
                    0o640 + index % 4,
                    1_690_000_000_000_000_000 + index,
                )
            before[name] = _snapshot(target)
            pairs.append((source, name))
        return results, stage, pairs, before

    def promote(
        self,
        pairs: list[tuple[Path, str]],
        results: Path,
        *,
        fail_after: int | None = None,
    ) -> None:
        stage = results / ".c58-stage-unit"
        metadata = stage.lstat()
        snapshot = atomic.stage_snapshot(
            results,
            stage,
            expected_device=metadata.st_dev,
            expected_inode=metadata.st_ino,
        )
        atomic.promote(
            pairs,
            results,
            expected_stage_snapshot=snapshot,
            fail_after=fail_after,
        )

    def assert_preimage(self, results: Path, before: dict[str, tuple[bytes, int, int] | None]) -> None:
        for name, expected in before.items():
            self.assertEqual(_snapshot(results / name), expected, name)
        self.assertFalse((results / atomic.LOCK_NAME).exists())
        self.assertFalse(any(path.name.startswith(".c58-transaction-") for path in results.iterdir()))

    def test_all_six_injected_failures_restore_absent_existing_and_mixed(self) -> None:
        for state in ("absent", "existing", "mixed"):
            for failure in range(1, 7):
                with self.subTest(state=state, failure=failure), tempfile.TemporaryDirectory() as temporary:
                    results, _, pairs, before = self.make_layout(Path(temporary), state)
                    with self.assertRaisesRegex(RuntimeError, "test-injected"):
                        self.promote(pairs, results, fail_after=failure)
                    self.assert_preimage(results, before)

    def test_success_promotes_all_six(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, _ = self.make_layout(Path(temporary), "mixed")
            expected = {name: _snapshot(source) for source, name in pairs}
            self.promote(pairs, results)
            for name, snapshot in expected.items():
                self.assertEqual(_snapshot(results / name), snapshot)

    def test_post_rename_failure_is_durable_and_rolled_back(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, before = self.make_layout(Path(temporary), "existing")
            original_replace = atomic.os.replace
            original_bound_fsync = atomic._fsync_directory_binding
            original_fingerprint = atomic._fingerprint_at
            events: list[str] = []
            renamed = False
            injected = False

            def tracked_replace(source, target, *args, **kwargs):
                nonlocal renamed
                value = original_replace(source, target, *args, **kwargs)
                if Path(source).name.startswith("new-"):
                    renamed = True
                    events.append("rename")
                return value

            def tracked_bound(binding, label):
                value = original_bound_fsync(binding, label)
                if renamed and binding.path.name.startswith(".c58-transaction-"):
                    events.append("transaction-fsync")
                elif renamed and binding.path == results:
                    events.append("result-fsync")
                return value

            def fail_placed(binding, name, label="file"):
                nonlocal injected
                if label == "placed target" and not injected:
                    injected = True
                    self.assertEqual(
                        events[-3:], ["rename", "transaction-fsync", "result-fsync"]
                    )
                    raise RuntimeError("post-rename fingerprint injection")
                return original_fingerprint(binding, name, label)

            with (
                patch.object(atomic.os, "replace", side_effect=tracked_replace),
                patch.object(atomic, "_fsync_directory_binding", side_effect=tracked_bound),
                patch.object(atomic, "_fingerprint_at", side_effect=fail_placed),
                self.assertRaisesRegex(RuntimeError, "post-rename"),
            ):
                self.promote(pairs, results)
            self.assertTrue(injected)
            self.assert_preimage(results, before)

    def test_result_parent_fd_rejects_rename_symlink_at_commit_boundaries(self) -> None:
        for boundary in ("precommit", "after-first-replacement"):
            with self.subTest(boundary=boundary), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                results, _, pairs, before = self.make_layout(root, "existing")
                held_results = root / "results-held"
                foreign = root / "foreign-results"
                foreign.mkdir()
                (foreign / "sentinel").write_bytes(b"foreign-must-not-change\n")

                def substitute_parent() -> None:
                    results.rename(held_results)
                    results.symlink_to(foreign, target_is_directory=True)

                if boundary == "precommit":
                    original_precommit = atomic._verify_precommit_preimages

                    def hostile_precommit(entries, result_binding, transaction_binding):
                        original_precommit(entries, result_binding, transaction_binding)
                        substitute_parent()

                    context = patch.object(
                        atomic,
                        "_verify_precommit_preimages",
                        side_effect=hostile_precommit,
                    )
                else:
                    original_replace = atomic.os.replace
                    substituted = False

                    def hostile_replace(source, target, *args, **kwargs):
                        nonlocal substituted
                        value = original_replace(source, target, *args, **kwargs)
                        if not substituted and Path(source).name.startswith("new-"):
                            substituted = True
                            substitute_parent()
                        return value

                    context = patch.object(
                        atomic.os, "replace", side_effect=hostile_replace
                    )

                with context, self.assertRaisesRegex(
                    atomic.RollbackError, "directory pathname identity changed"
                ):
                    self.promote(pairs, results)

                self.assertTrue(results.is_symlink())
                self.assertEqual(results.resolve(strict=True), foreign)
                self.assertEqual(
                    {path.name for path in foreign.iterdir()}, {"sentinel"}
                )
                self.assertEqual(
                    (foreign / "sentinel").read_bytes(), b"foreign-must-not-change\n"
                )
                self.assertTrue((held_results / atomic.LOCK_NAME).exists())
                self.assertTrue(
                    any(
                        path.name.startswith(".c58-transaction-")
                        for path in held_results.iterdir()
                    )
                )
                if boundary == "precommit":
                    for name, expected in before.items():
                        self.assertEqual(_snapshot(held_results / name), expected)

    def test_postcommit_cleanup_and_lock_failures_are_distinct_committed_outcomes(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, _ = self.make_layout(Path(temporary), "existing")
            expected = {name: _snapshot(source) for source, name in pairs}
            with patch.object(
                atomic, "_cleanup_transaction", side_effect=OSError("cleanup injection")
            ):
                with self.assertRaisesRegex(
                    atomic.PostCommitError, "COMMITTED_WITH_DEBRIS.*DO NOT RETRY"
                ):
                    self.promote(pairs, results)
            for name, snapshot in expected.items():
                self.assertEqual(_snapshot(results / name), snapshot)
            self.assertTrue(
                any(path.name.startswith(".c58-transaction-") for path in results.iterdir())
            )
            self.assertFalse((results / atomic.LOCK_NAME).exists())

        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, _ = self.make_layout(Path(temporary), "existing")
            expected = {name: _snapshot(source) for source, name in pairs}
            original_release = atomic.release_lock

            def foreign_release(lock, result_binding):
                held = lock.path.with_name(".held-original-lock")
                lock.path.rename(held)
                lock.path.write_bytes(b"foreign-lock\n")
                return original_release(lock, result_binding)

            with patch.object(atomic, "release_lock", side_effect=foreign_release):
                with self.assertRaisesRegex(atomic.PostCommitError, "COMMITTED_WITH_DEBRIS"):
                    self.promote(pairs, results)
            for name, snapshot in expected.items():
                self.assertEqual(_snapshot(results / name), snapshot)
            self.assertEqual((results / atomic.LOCK_NAME).read_bytes(), b"foreign-lock\n")
            self.assertFalse(
                any(path.name.startswith(".c58-transaction-") for path in results.iterdir())
            )

    def test_postcommit_cli_has_fixed_distinct_exit_code(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results, stage, pairs, _ = self.make_layout(Path(temporary), "absent")
            metadata = stage.stat()
            snapshot = atomic.stage_snapshot(
                results,
                stage,
                expected_device=metadata.st_dev,
                expected_inode=metadata.st_ino,
            )
            snapshot_argument = canonical_json_bytes(snapshot).decode().rstrip("\n")
            argv = ["c58_atomic_promote.py", "--result-dir", str(results)]
            for source, target in pairs:
                argv.extend(("--source", str(source), "--target", target))
            argv.extend(("--expected-stage-snapshot", snapshot_argument))
            stderr = io.StringIO()
            with (
                patch.object(sys, "argv", argv),
                patch.object(
                    atomic,
                    "promote",
                    side_effect=atomic.PostCommitError("COMMITTED_WITH_DEBRIS: test"),
                ),
                redirect_stderr(stderr),
            ):
                self.assertEqual(atomic.main(), atomic.POSTCOMMIT_EXIT_CODE)
            self.assertIn("COMMITTED_WITH_DEBRIS", stderr.getvalue())
            rollback_stderr = io.StringIO()
            with (
                patch.object(sys, "argv", argv),
                patch.object(
                    atomic,
                    "promote",
                    side_effect=atomic.RolledBackVerifiedError(
                        "ROLLED_BACK_VERIFIED: test"
                    ),
                ),
                redirect_stderr(rollback_stderr),
            ):
                self.assertEqual(atomic.main(), atomic.ROLLED_BACK_EXIT_CODE)
            self.assertIn("ROLLED_BACK_VERIFIED", rollback_stderr.getvalue())

    def test_wrong_count_order_name_and_duplicate_source_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, _ = self.make_layout(Path(temporary), "absent")
            hostile = (
                pairs[:-1],
                [pairs[1], pairs[0], *pairs[2:]],
                [*pairs[:-1], (pairs[-1][0], "wrong.json")],
                [pairs[0], (pairs[0][0], pairs[1][1]), *pairs[2:]],
            )
            for request in hostile:
                with self.subTest(request=[name for _, name in request]), self.assertRaises(StrictDataError):
                    self.promote(request, results)

    def test_symlink_fifo_and_hardlink_sources_rejected(self) -> None:
        mutations = ("symlink", "fifo", "hardlink")
        for mutation in mutations:
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                results, stage, pairs, _ = self.make_layout(root, "absent")
                source = pairs[0][0]
                source.unlink()
                if mutation == "symlink":
                    source.symlink_to(stage / atomic.EXPECTED_TARGET_NAMES[1])
                elif mutation == "fifo":
                    os.mkfifo(source)
                else:
                    _write(source, b"hardlinked\n", 0o600, 1_700_000_000_000_000_000)
                    os.link(source, root / "external-link")
                with self.assertRaises(StrictDataError):
                    self.promote(pairs, results)

    def test_cross_location_and_foreign_debris_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary, tempfile.TemporaryDirectory() as external:
            results, _, pairs, _ = self.make_layout(Path(temporary), "absent")
            foreign = Path(external) / "foreign"
            foreign.write_bytes(b"foreign")
            hostile_pairs = [(foreign, pairs[0][1]), *pairs[1:]]
            with self.assertRaises(StrictDataError):
                self.promote(hostile_pairs, results)
        for debris in (".c58-stage-stale", ".c58-transaction-stale", atomic.LOCK_NAME):
            with self.subTest(debris=debris), tempfile.TemporaryDirectory() as temporary:
                results, _, pairs, _ = self.make_layout(Path(temporary), "absent")
                path = results / debris
                if debris == atomic.LOCK_NAME:
                    path.write_bytes(b"stale\n")
                else:
                    path.mkdir()
                with self.assertRaisesRegex(StrictDataError, "debris"):
                    self.promote(pairs, results)

    def test_target_hardlink_result_symlink_parent_symlink_and_dangling_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            results, _, pairs, _ = self.make_layout(root, "existing")
            os.link(results / pairs[0][1], root / "target-hardlink")
            with self.assertRaises(StrictDataError):
                self.promote(pairs, results)
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            results, stage, pairs, _ = self.make_layout(root, "absent")
            alias = root / "results-alias"
            alias.symlink_to(results, target_is_directory=True)
            with self.assertRaises(StrictDataError):
                self.promote(pairs, alias)
            stage_alias = root / "stage-alias"
            stage_alias.symlink_to(stage, target_is_directory=True)
            hostile = [(stage_alias / source.name, name) for source, name in pairs]
            with self.assertRaises(StrictDataError):
                self.promote(hostile, results)
            pairs[0][0].unlink()
            pairs[0][0].symlink_to(root / "missing")
            with self.assertRaises(StrictDataError):
                self.promote(pairs, results)

    def test_precommit_target_and_final_source_mutations_are_rejected_and_rolled_back(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, before = self.make_layout(Path(temporary), "existing")
            original = atomic._verify_precommit_preimages

            def mutate_target(entries, result_binding, transaction_binding):
                entries[0].target.write_bytes(b"hostile-target\n")
                return original(entries, result_binding, transaction_binding)

            with patch.object(atomic, "_verify_precommit_preimages", side_effect=mutate_target):
                with self.assertRaises(atomic.RollbackError):
                    self.promote(pairs, results)
            # The hostile precommit mutation is deliberately not overwritten:
            # no live replacement had yet been authorized.
            self.assertEqual((results / pairs[0][1]).read_bytes(), b"hostile-target\n")
            self.assertTrue(any(path.name.startswith(".c58-transaction-") for path in results.iterdir()))

        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, before = self.make_layout(Path(temporary), "existing")
            original = atomic._verify_precommit_preimages

            def mutate_source(entries, result_binding, transaction_binding):
                original(entries, result_binding, transaction_binding)
                entries[0].source.write_bytes(b"hostile-source\n")

            with patch.object(atomic, "_verify_precommit_preimages", side_effect=mutate_source):
                with self.assertRaisesRegex(
                    atomic.RolledBackVerifiedError, "ROLLED_BACK_VERIFIED"
                ):
                    self.promote(pairs, results)
            self.assert_preimage(results, before)

    def test_foreign_identical_target_during_rollback_retains_backups(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, _ = self.make_layout(Path(temporary), "existing")
            original = atomic._fingerprint_at
            replaced = False

            def replace_before_rollback(binding, name, label="file"):
                nonlocal replaced
                if label == "rollback target" and not replaced:
                    replaced = True
                    path = binding.path / name
                    snapshot = _snapshot(path)
                    assert snapshot is not None
                    raw, mode, mtime_ns = snapshot
                    foreign = path.with_name(".foreign-identical")
                    _write(foreign, raw, mode, mtime_ns)
                    os.replace(foreign, path)
                return original(binding, name, label)

            with patch.object(atomic, "_fingerprint_at", side_effect=replace_before_rollback):
                with self.assertRaises(atomic.RollbackError):
                    self.promote(pairs, results, fail_after=1)
            transactions = [path for path in results.iterdir() if path.name.startswith(".c58-transaction-")]
            self.assertEqual(len(transactions), 1)
            self.assertTrue(any(path.name.startswith("old-") for path in transactions[0].iterdir()))

    def test_foreign_backup_substitution_before_restore_is_retained(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, _ = self.make_layout(Path(temporary), "existing")
            original = atomic._fingerprint_at
            replaced = False

            def replace_backup(binding, name, label="file"):
                nonlocal replaced
                if label == "rollback backup" and not replaced:
                    replaced = True
                    path = binding.path / name
                    raw, mode, mtime_ns = _snapshot(path)  # type: ignore[misc]
                    foreign = path.with_name(".foreign-backup")
                    _write(foreign, raw, mode, mtime_ns)
                    os.replace(foreign, path)
                return original(binding, name, label)

            with patch.object(atomic, "_fingerprint_at", side_effect=replace_backup):
                with self.assertRaises(atomic.RollbackError):
                    self.promote(pairs, results, fail_after=1)
            self.assertTrue(replaced)
            transactions = [
                path for path in results.iterdir() if path.name.startswith(".c58-transaction-")
            ]
            self.assertEqual(len(transactions), 1)
            self.assertTrue((transactions[0] / "old-00").exists())

    def test_transaction_cleanup_validates_every_resident_before_deleting(self) -> None:
        for mutation in ("missing", "substitution", "extra", "dangling-directory"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as temporary:
                results = Path(temporary) / "results"
                results.mkdir()
                transaction = results / ".c58-transaction-unit"
                transaction.mkdir()
                staged = transaction / "new-00"
                _write(staged, b"owned\n", 0o600, 1_700_000_000_000_000_000)
                owned = atomic.fingerprint(staged, "fixture")
                entry = atomic.Entry(
                    source=staged,
                    target=results / "target",
                    staged=staged,
                    backup=transaction / "old-00",
                    source_fingerprint=owned,
                    preimage=None,
                    staged_fingerprint=owned,
                    staged_resident=True,
                )
                identity = (transaction.stat().st_dev, transaction.stat().st_ino)
                result_binding = atomic._bind_directory(results, "fixture results")
                transaction_binding = atomic._bind_child_directory(
                    result_binding,
                    transaction.name,
                    transaction,
                    "fixture transaction",
                    expected_identity=identity,
                )
                old_transaction = None
                if mutation == "missing":
                    staged.unlink()
                elif mutation == "substitution":
                    raw, mode, mtime_ns = _snapshot(staged)  # type: ignore[misc]
                    foreign = transaction / ".foreign"
                    _write(foreign, raw, mode, mtime_ns)
                    os.replace(foreign, staged)
                elif mutation == "extra":
                    (transaction / "foreign").write_bytes(b"foreign\n")
                else:
                    old_transaction = transaction.with_name(transaction.name + "-old")
                    transaction.rename(old_transaction)
                    transaction.symlink_to(results / "missing", target_is_directory=True)
                try:
                    with self.assertRaises((StrictDataError, atomic.DirectoryIdentityError)):
                        atomic._cleanup_transaction(
                            [entry], transaction_binding, result_binding
                        )
                finally:
                    atomic._close_directory_binding(transaction_binding)
                    atomic._close_directory_binding(result_binding)
                evidence_root = old_transaction if old_transaction is not None else transaction
                if mutation != "missing":
                    self.assertTrue((evidence_root / "new-00").exists())

    def test_copy_uses_fd_utime_then_fsync_and_short_lock_write_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "source"
            destination = root / "destination"
            _write(source, b"copy\n", 0o640, 1_700_000_000_000_000_123)
            expected = atomic.fingerprint(source, "fixture source")
            original_utime = atomic.os.utime
            original_fsync = atomic.os.fsync
            events: list[str] = []

            def tracked_utime(path_or_fd, *args, **kwargs):
                self.assertIs(type(path_or_fd), int)
                events.append("fd-utime")
                return original_utime(path_or_fd, *args, **kwargs)

            def tracked_fsync(descriptor):
                events.append("fsync")
                return original_fsync(descriptor)

            with (
                patch.object(atomic.os, "utime", side_effect=tracked_utime),
                patch.object(atomic.os, "fsync", side_effect=tracked_fsync),
            ):
                copied = atomic._copy_stable(source, destination, expected)
            self.assertEqual(copied.restored_fields(), expected.restored_fields())
            self.assertLess(events.index("fd-utime"), len(events) - 1)
            self.assertIn("fsync", events[events.index("fd-utime") + 1 :])

        with tempfile.TemporaryDirectory() as temporary:
            results = Path(temporary)
            binding = atomic._bind_directory(results, "fixture results")
            try:
                with patch.object(atomic.os, "write", return_value=0):
                    with self.assertRaisesRegex(StrictDataError, "short"):
                        atomic.acquire_lock(binding)
            finally:
                atomic._close_directory_binding(binding)
            self.assertFalse((results / atomic.LOCK_NAME).exists())

    def test_stage_cleanup_rejects_replacement_and_extension_is_exact(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results = Path(temporary) / "results"
            results.mkdir()
            stage = results / ".c58-stage-unit"
            stage.mkdir()
            for name in atomic.EXPECTED_TARGET_NAMES[:-1]:
                (stage / name).write_bytes((name + "\n").encode())
            metadata = stage.stat()
            prior = atomic.stage_snapshot(
                results,
                stage,
                expected_device=metadata.st_dev,
                expected_inode=metadata.st_ino,
            )
            (stage / atomic.EXPECTED_TARGET_NAMES[-1]).write_bytes(b"manifest\n")
            current = atomic.stage_snapshot(
                results,
                stage,
                expected_device=metadata.st_dev,
                expected_inode=metadata.st_ino,
            )
            atomic.verify_stage_extension(prior, current)
            victim = stage / atomic.EXPECTED_TARGET_NAMES[0]
            raw, mode, mtime_ns = _snapshot(victim)  # type: ignore[misc]
            foreign = stage / ".foreign"
            _write(foreign, raw, mode, mtime_ns)
            os.replace(foreign, victim)
            with self.assertRaises(StrictDataError):
                atomic.cleanup_active_stage(results, stage, expected_snapshot=current)
            self.assertTrue(victim.exists())

        with tempfile.TemporaryDirectory() as temporary:
            results, stage, pairs, before = self.make_layout(Path(temporary), "absent")
            metadata = stage.stat()
            snapshot = atomic.stage_snapshot(
                results,
                stage,
                expected_device=metadata.st_dev,
                expected_inode=metadata.st_ino,
            )
            victim = pairs[0][0]
            raw, mode, mtime_ns = _snapshot(victim)  # type: ignore[misc]
            foreign = stage / ".foreign"
            _write(foreign, raw, mode, mtime_ns)
            os.replace(foreign, victim)
            with self.assertRaisesRegex(StrictDataError, "final owned stage snapshot"):
                atomic.promote(
                    pairs,
                    results,
                    expected_stage_snapshot=snapshot,
                )
            self.assert_preimage(results, before)

    def test_foreign_lock_replacement_is_retained(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results = Path(temporary)
            binding = atomic._bind_directory(results, "fixture results")
            try:
                lock = atomic.acquire_lock(binding)
                held = results / ".held-original-lock"
                lock.path.rename(held)
                lock.path.write_bytes(b"foreign\n")
                with self.assertRaisesRegex(StrictDataError, "foreign lock retained"):
                    atomic.release_lock(lock, binding)
                self.assertEqual(lock.path.read_bytes(), b"foreign\n")
                lock.path.unlink()
                held.unlink()
            finally:
                atomic._close_directory_binding(binding)

    def test_optimized_python_and_environment_rejected(self) -> None:
        source = (
            "import pathlib,sys;sys.path.insert(0," + repr(str(CODE)) + ");"
            "from c58_exact import reject_optimized_python;reject_optimized_python()"
        )
        for command, environment in (
            ([sys.executable, "-O", "-B", "-c", source], {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}),
            ([sys.executable, "-B", "-c", source], {**os.environ, "PYTHONOPTIMIZE": "1", "PYTHONDONTWRITEBYTECODE": "1"}),
        ):
            completed = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=environment)
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn(b"optimized Python", completed.stderr)


class ManifestHostileTests(unittest.TestCase):
    def make_project(self, root: Path) -> tuple[Path, Path]:
        code = root / "code"
        results = root / "results"
        code.mkdir()
        results.mkdir()
        for name in manifest.CODE_NAMES:
            (code / name).write_bytes((name + "\n").encode())
        for name in manifest.PROSE_NAMES + manifest.PROMOTED_NAMES:
            (results / name).write_bytes((name + "\n").encode())
        return code, results

    def patched(self, root: Path, code: Path, results: Path):
        return (
            patch.object(manifest, "PROJECT", root),
            patch.object(manifest, "CODE", code),
            patch.object(manifest, "RESULTS", results),
            patch.object(manifest, "DEFAULT_MANIFEST", results / manifest.PROMOTED_NAMES[-1]),
        )

    def test_unknown_file_directory_symlink_and_fifo_rejected(self) -> None:
        for location in ("code", "results"):
            for kind in ("file", "directory", "symlink", "fifo"):
                with self.subTest(
                    location=location, kind=kind
                ), tempfile.TemporaryDirectory() as temporary:
                    root = Path(temporary)
                    code, results = self.make_project(root)
                    hostile = (code if location == "code" else results) / "hostile"
                    if kind == "file":
                        hostile.write_bytes(b"x")
                    elif kind == "directory":
                        hostile.mkdir()
                    elif kind == "symlink":
                        hostile.symlink_to(results / "RESULTS.md")
                    else:
                        os.mkfifo(hostile)
                    p1, p2, p3, p4 = self.patched(root, code, results)
                    with p1, p2, p3, p4, self.assertRaises(StrictDataError):
                        manifest.artifact_paths()

    def test_write_without_stage_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            code, results = self.make_project(root)
            p1, p2, p3, p4 = self.patched(root, code, results)
            argv = ["c58_hash_manifest.py", "--write", "--manifest", str(results / "scoped_hash_manifest.json")]
            with p1, p2, p3, p4, patch.object(sys, "argv", argv), self.assertRaises(StrictDataError):
                manifest.main()

    def test_stage_inode_swap_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            code, results = self.make_project(root)
            # A refresh may have any fixed live targets, but its one active
            # stage must supply all five nonmanifest promoted inputs.
            stage = results / ".c58-stage-unit"
            stage.mkdir()
            for name in manifest.PROMOTED_NAMES[:-1]:
                (stage / name).write_bytes(b"stage\n")
            original = manifest._stage_sources

            def swap(active):
                value = original(active)
                old = active.with_name(active.name + "-old")
                active.rename(old)
                active.mkdir()
                return value

            p1, p2, p3, p4 = self.patched(root, code, results)
            with p1, p2, p3, p4, patch.object(manifest, "_stage_sources", side_effect=swap), self.assertRaises(StrictDataError):
                manifest.artifact_paths(stage)

    def test_manifest_write_rejects_stage_swap_after_byte_construction(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            code, results = self.make_project(root)
            stage = results / ".c58-stage-unit"
            stage.mkdir()
            for name in manifest.PROMOTED_NAMES[:-1]:
                (stage / name).write_bytes(b"stage\n")
            original = manifest.manifest_bytes

            def swap_after_bytes(active, **kwargs):
                raw = original(active, **kwargs)
                old = active.with_name(active.name + "-old")
                active.rename(old)
                active.mkdir()
                return raw

            argv = [
                "c58_hash_manifest.py",
                "--write",
                "--stage-dir",
                str(stage),
                "--manifest",
                str(stage / manifest.PROMOTED_NAMES[-1]),
            ]
            p1, p2, p3, p4 = self.patched(root, code, results)
            with (
                p1,
                p2,
                p3,
                p4,
                patch.object(manifest, "manifest_bytes", side_effect=swap_after_bytes),
                patch.object(sys, "argv", argv),
                self.assertRaises(StrictDataError),
            ):
                manifest.main()
            self.assertFalse((stage / manifest.PROMOTED_NAMES[-1]).exists())

    def test_manifest_result_parent_binding_rejects_rename_symlink(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            code, results = self.make_project(root)
            held_results = root / "results-held"
            foreign = root / "foreign-results"
            foreign.mkdir()
            (foreign / "sentinel").write_bytes(b"foreign-must-not-change\n")
            original = manifest.artifact_paths

            def swap_after_inventory(stage=None, **kwargs):
                paths = original(stage, **kwargs)
                results.rename(held_results)
                results.symlink_to(foreign, target_is_directory=True)
                return paths

            p1, p2, p3, p4 = self.patched(root, code, results)
            with (
                p1,
                p2,
                p3,
                p4,
                patch.object(
                    manifest, "artifact_paths", side_effect=swap_after_inventory
                ),
                self.assertRaises(atomic.DirectoryIdentityError),
            ):
                manifest.manifest_object()
            self.assertTrue(results.is_symlink())
            self.assertEqual(results.resolve(strict=True), foreign)
            self.assertEqual({path.name for path in foreign.iterdir()}, {"sentinel"})
            self.assertEqual(
                (foreign / "sentinel").read_bytes(), b"foreign-must-not-change\n"
            )
            for name in manifest.PROSE_NAMES + manifest.PROMOTED_NAMES:
                self.assertEqual(
                    (held_results / name).read_bytes(), (name + "\n").encode()
                )

    def test_runner_privileged_bootstrap_ignores_and_rejects_BASH_ENV(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            marker = root / "injected"
            payload = root / "bash-env"
            payload.write_text(f"/usr/bin/touch {marker}\n", encoding="utf-8")
            clean_base = dict(os.environ)
            for name in (
                "LD_PRELOAD",
                "LD_LIBRARY_PATH",
                "BASH_ENV",
                "ENV",
                "PYTHONOPTIMIZE",
                "PYTHONPATH",
                "PYTHONHOME",
                "PYTHONSAFEPATH",
            ):
                clean_base.pop(name, None)
            environment = {
                **clean_base,
                "BASH_ENV": str(payload),
                "PATH": str(root),
                "PYTHONDONTWRITEBYTECODE": "1",
            }
            self.assertEqual(
                (CODE / "run_all.sh").read_bytes().splitlines()[0],
                b"#!/usr/bin/bash -p",
            )
            completed = subprocess.run(
                [str(CODE / "run_all.sh")],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=environment,
                cwd="/",
            )
            self.assertEqual(completed.returncode, 2)
            self.assertIn(b"BASH_ENV must be completely unset", completed.stderr)
            self.assertFalse(marker.exists())

            loader_environment = {
                **clean_base,
                "LD_LIBRARY_PATH": str(root),
                "PYTHONDONTWRITEBYTECODE": "1",
            }
            loader_completed = subprocess.run(
                [str(CODE / "run_all.sh")],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=loader_environment,
                cwd="/",
            )
            self.assertEqual(loader_completed.returncode, 2)
            self.assertIn(
                b"unsafe parent environment already reached the dynamic loader",
                loader_completed.stderr,
            )

    def test_runner_fd_relative_stage_creation_survives_parent_symlink_aba(self) -> None:
        runner_source = (CODE / "run_all.sh").read_text(encoding="utf-8")
        self.assertIn(
            'mktemp -d "/proc/self/fd/$RESULTS_FD/.c58-stage-XXXXXXXX"',
            runner_source,
        )
        self.assertNotIn(
            'mktemp -d "$RESULTS_DIR/.c58-stage-XXXXXXXX"', runner_source
        )
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            results = root / "results"
            held = root / "results-held"
            foreign = root / "foreign-results"
            results.mkdir()
            foreign.mkdir()
            (foreign / "sentinel").write_bytes(b"foreign-must-not-change\n")
            probe = r'''
set -euo pipefail
RESULTS_DIR="$1"
HELD_RESULTS="$2"
FOREIGN_RESULTS="$3"
exec {RESULTS_FD}<"$RESULTS_DIR"
/usr/bin/mv -- "$RESULTS_DIR" "$HELD_RESULTS"
/usr/bin/ln -s -- "$FOREIGN_RESULTS" "$RESULTS_DIR"
STAGE_FD_PATH="$(/usr/bin/mktemp -d "/proc/self/fd/$RESULTS_FD/.c58-stage-XXXXXXXX")"
STAGE_BASENAME="${STAGE_FD_PATH##*/}"
/usr/bin/rm -- "$RESULTS_DIR"
/usr/bin/mv -- "$HELD_RESULTS" "$RESULTS_DIR"
/usr/bin/printf '%s\n' "$STAGE_BASENAME"
'''
            completed = subprocess.run(
                ["/usr/bin/bash", "-p", "-c", probe, "_", str(results), str(held), str(foreign)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
                env={"PATH": "/usr/bin:/bin"},
                cwd="/",
            )
            stage_name = completed.stdout.decode("ascii").strip()
            self.assertRegex(stage_name, r"^\.c58-stage-[A-Za-z0-9]{8}$")
            self.assertTrue((results / stage_name).is_dir())
            self.assertEqual({path.name for path in foreign.iterdir()}, {"sentinel"})
            self.assertEqual(
                (foreign / "sentinel").read_bytes(), b"foreign-must-not-change\n"
            )

    def test_missing_backends_fail_closed(self) -> None:
        missing = Path("/definitely/missing/hcs-c58-backend")
        with self.assertRaises((StrictDataError, FileNotFoundError)):
            pipeline.python_preflight(missing, Path(sys.executable))
        with self.assertRaises((StrictDataError, FileNotFoundError)):
            pipeline.python_preflight(Path("/usr/bin/python3"), missing)
        with self.assertRaises((StrictDataError, FileNotFoundError)):
            pipeline.gap_preflight(missing)


if __name__ == "__main__":
    if sys.flags.optimize or "PYTHONOPTIMIZE" in os.environ:
        raise SystemExit("optimized Python is forbidden")
    unittest.main(verbosity=2)
