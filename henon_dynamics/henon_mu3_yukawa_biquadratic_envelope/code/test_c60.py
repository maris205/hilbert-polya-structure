#!/usr/bin/env python3
"""Hostile source, transaction, and release-scaffold tests for HCS-C60."""

from __future__ import annotations

import ast
import hashlib
import io
import json
from contextlib import redirect_stderr, redirect_stdout
import inspect
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import c60_atomic_promote as atomic
import c60_checker as checker
import c60_checker_resolvent as checker_resolver
from c60_exact import (
    StrictDataError,
    canonical_json_bytes,
    canonical_leaf_bytes,
    deep_exact,
    strict_json_loads,
)
import c60_hash_manifest as manifest
import c60_pipeline as pipeline
import c60_producer as producer
import c60_resolvent as producer_resolver


CODE = Path(__file__).resolve().parent
RESULTS = CODE.parent / "results"
TEST_EVIDENCE_ENV = "C60_TEST_EVIDENCE_DIR"
EVIDENCE_NAMES = (
    "c60_group_evidence.json",
    "c60_resolvent_evidence.json",
)
STAGE_NAME_PATTERN = re.compile(r"^\.c60-stage-[A-Za-z0-9]{8}$")

FROZEN_SUPPORT_SOURCE_HASHES = {
    "c60_group.py": "fd3e75913db3cf5d71f7fd95a3e260edae19bc53a748767f28773d008121536b",
    "c60_checker_group.g": "4338ad0e2af9a0fe096cbb6514de6c8d5227386a2ffadeac487a858fb160dde3",
    "c60_resolvent.py": "61b157e8c3e5a68bf304f9499bc176f60fe16bf7c5e5f6d021fbec17d7d9465e",
    "c60_checker_resolvent.py": "5f4070831d4734ba3be93ae578d7a2be893f46676ab40cdaa4a2de6b8d3fb672",
}
FROZEN_EVIDENCE_HASHES = {
    "c60_group_evidence.json": "dcdb9a8be954d4ea5376220d55fcbae9bbb08eb49d03d98d57d790c319ad5fb2",
    "c60_resolvent_evidence.json": "f115125725c9160ee3d02f1996147098c234226bdc81eaa670460802a8d827da",
}

# Independently written machine sources sealed for the prefreeze candidate.
# This is a source-integrity latch, not refresh or release authorization.
FROZEN_MACHINE_SOURCE_HASHES: dict[str, str] | None = {
    "c60_producer.py": "0b0dda0eddf0f5ec483cd34ae2c8c285d22b47886d231a126a5849a5162e179b",
    "c60_checker.py": "49b94955cf96862aaefabd5a5988c52b41975e8716a155e1f2ee33af55c7fd46",
}

PAYLOAD_KEYS = (
    "artifact_contract",
    "G0_released_authority_rebind",
    "G1_common_normalizer_lattice",
    "G2_primitive_integral_carriers",
    "G3_formal_invariant_degree_gap",
    "G4_tower_characters_and_zeta",
    "G5_absolute_relative_arithmetic",
    "G6_both_relative_local_towers",
    "G7_independence_scope_release",
    "written_bridges",
    "backend_contract",
    "source_contract",
    "scope_nonclaims",
    "nonresults",
    "status",
)
SCOPE_NONCLAIM_KEYS = (
    "target_selection_pilot_is_theorem_authority",
    "raw_tom_defines_fields",
    "finite_g_sets_isomorphic_from_character_relation",
    "formal_invariant_statement_after_root_relations",
    "expanded_characteristic_zero_resolvent_claimed",
    "characteristic_zero_coefficient_hash_claimed",
    "integral_basis_claimed",
    "maximal_order_claimed",
    "monogenicity_claimed",
    "class_number_claimed",
    "regulator_claimed",
    "trace_form_claimed",
    "d3_branch_selected",
    "local_fields_classified_by_nefd_rows",
    "decomposition_frobenius_claimed",
    "bad_artin_euler_claimed",
    "local_epsilon_factor_claimed",
    "local_root_number_claimed",
    "global_root_number_claimed",
    "artin_holomorphy_claimed",
    "automorphy_claimed",
    "rational_point_claimed",
    "hasse_principle_claimed",
    "weak_approximation_claimed",
    "brauer_manin_claimed",
    "motive_claimed",
    "rh_claimed",
    "hilbert_polya_operator_claimed",
    "paper_complete_claimed",
    "release_claimed",
)

CANONICAL_G7_COUNTS = {
    "payload_scalar_leaf_count": 9310,
    "schema_scalar_leaf_count": 27,
    "value_mutation_count_expected": 9339,
    "type_mutation_count_expected": 9339,
    "structural_mutation_count_expected": 14,
    # This certificate field counts the ten self-consistent mutations of the
    # two full evidence documents.  The checker must additionally exercise
    # the two artifact-row digest mutations, for twelve actual hostile cases.
    "evidence_rebound_mutation_count_expected": 10,
}
ACTUAL_DEEP_EVIDENCE_AND_ARTIFACT_HOSTILE_CASES = 12


def _fixture_evidence_paths() -> tuple[Path, Path]:
    """Bind the shared fixture to live evidence or the runner's active stage."""

    results = RESULTS.absolute()
    if (
        results.is_symlink()
        or not results.is_dir()
        or results.resolve(strict=True) != results
    ):
        raise StrictDataError("fixture results authority must be one real directory")
    selected = os.environ.get(TEST_EVIDENCE_ENV)
    directory = results
    if selected is not None:
        candidate = Path(selected)
        if (
            not candidate.is_absolute()
            or not STAGE_NAME_PATTERN.fullmatch(candidate.name)
            or candidate.parent != results
            or candidate.is_symlink()
            or not candidate.is_dir()
            or candidate.resolve(strict=True) != candidate
        ):
            raise StrictDataError(
                "test evidence override must be one canonical real direct "
                "PROJECT/results/.c60-stage-[A-Za-z0-9]{8} directory"
            )
        if {entry.name for entry in candidate.iterdir()} != set(EVIDENCE_NAMES):
            raise StrictDataError(
                "test evidence stage must contain exactly the two fixed evidence files"
            )
        directory = candidate

    paths = tuple(directory / name for name in EVIDENCE_NAMES)
    directory_before = directory.stat()
    identities: list[tuple[int, int, int, int, int, int, int]] = []
    for path in paths:
        metadata = path.lstat()
        if (
            path.is_symlink()
            or not stat.S_ISREG(metadata.st_mode)
            or metadata.st_nlink != 1
        ):
            raise StrictDataError(
                "fixture evidence must be fixed regular non-symlink link-count-one files"
            )
        identities.append(
            (
                metadata.st_dev,
                metadata.st_ino,
                metadata.st_mode,
                metadata.st_nlink,
                metadata.st_size,
                metadata.st_mtime_ns,
                metadata.st_ctime_ns,
            )
        )
    directory_after = directory.stat()
    if (
        not stat.S_ISDIR(directory_after.st_mode)
        or (directory_before.st_dev, directory_before.st_ino)
        != (directory_after.st_dev, directory_after.st_ino)
    ):
        raise StrictDataError("fixture evidence directory changed during binding")
    for path, expected in zip(paths, identities):
        metadata = path.lstat()
        observed = (
            metadata.st_dev,
            metadata.st_ino,
            metadata.st_mode,
            metadata.st_nlink,
            metadata.st_size,
            metadata.st_mtime_ns,
            metadata.st_ctime_ns,
        )
        if observed != expected:
            raise StrictDataError("fixture evidence changed during binding")
    return paths  # type: ignore[return-value]


def _fixture_evidence_documents() -> tuple[dict[str, object], dict[str, object]]:
    paths = _fixture_evidence_paths()
    directory = paths[0].parent
    directory_before = directory.stat()
    seals: list[tuple[int, int, int, int, int, int, int]] = []
    blobs: list[bytes] = []
    for path in paths:
        before = path.lstat()
        blob = path.read_bytes()
        after = path.lstat()
        before_seal = (
            before.st_dev,
            before.st_ino,
            before.st_mode,
            before.st_nlink,
            before.st_size,
            before.st_mtime_ns,
            before.st_ctime_ns,
        )
        after_seal = (
            after.st_dev,
            after.st_ino,
            after.st_mode,
            after.st_nlink,
            after.st_size,
            after.st_mtime_ns,
            after.st_ctime_ns,
        )
        if before_seal != after_seal or len(blob) != after.st_size:
            raise StrictDataError("fixture evidence changed while being read")
        seals.append(after_seal)
        blobs.append(blob)
    directory_after = directory.stat()
    if (
        (directory_before.st_dev, directory_before.st_ino)
        != (directory_after.st_dev, directory_after.st_ino)
        or _fixture_evidence_paths() != paths
    ):
        raise StrictDataError("fixture evidence directory changed during read")
    for path, expected in zip(paths, seals):
        metadata = path.lstat()
        observed = (
            metadata.st_dev,
            metadata.st_ino,
            metadata.st_mode,
            metadata.st_nlink,
            metadata.st_size,
            metadata.st_mtime_ns,
            metadata.st_ctime_ns,
        )
        if observed != expected:
            raise StrictDataError("fixture evidence changed after read")
    group = strict_json_loads(blobs[0], max_bytes=2_000_000)
    resolvent = strict_json_loads(blobs[1], max_bytes=5_000_000)
    if type(group) is not dict or type(resolvent) is not dict:
        raise StrictDataError("fixture evidence documents must be objects")
    return group, resolvent


def _fixture_backend_contract() -> dict[str, object]:
    """Return the exact locked backend value without launching a child."""

    math = pipeline.EXPECTED_BACKENDS["math"]
    return {
        "gap": dict(pipeline.EXPECTED_GAP),
        "math_python": {
            "executable_sha256": math["executable_sha256"],
            "executable_size_bytes": math["executable_size_bytes"],
            "resolved_executable": str(
                Path("/root/miniconda3/bin/python3").resolve(strict=True)
            ),
            "versions": {
                "backend": "FLINT_SYMPY_NETWORKX",
                "python": math["python"],
                "flint": math["flint"],
                "sympy": math["sympy"],
                "networkx": math["networkx"],
                "jsonschema": math["jsonschema"],
            },
        },
        "pari_dependency": False,
        "schema_id": "hcs-c60-backend-contract-v1",
        "singular_dependency": False,
        "two_run_deterministic": True,
    }


def _imports(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=path.name)
    answer: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            answer.update(alias.name.split(".", 1)[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module is not None:
            answer.add(node.module.split(".", 1)[0])
    return answer


def _literal_string_dicts(path: Path) -> list[tuple[int, list[str]]]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=path.name)
    answer = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        keys = [
            key.value
            for key in node.keys
            if isinstance(key, ast.Constant) and isinstance(key.value, str)
        ]
        answer.append((node.lineno, keys))
    return answer


def _semantic_diff_count(left: object, right: object) -> int:
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
    def test_noncanonical_json_and_type_confusion_rejected(self) -> None:
        for raw in (b'{"x":-0}', b'{"x":01}', b'{"x":1.0}', b'{"x":1,"x":2}'):
            with self.subTest(raw=raw), self.assertRaises(StrictDataError):
                strict_json_loads(raw, max_bytes=100)
        self.assertFalse(deep_exact(True, 1))
        self.assertFalse(deep_exact({"x": [1]}, {"x": [True]}))

    def test_hundred_thousand_digit_integer(self) -> None:
        raw = b'{"x":' + b"9" * 100_000 + b"}"
        value = strict_json_loads(raw, max_bytes=len(raw))
        self.assertIs(type(value["x"]), int)


class SourceArchitectureTests(unittest.TestCase):
    def test_exact_inventory_and_manifest_contract(self) -> None:
        observed = {path.name for path in CODE.iterdir()}
        self.assertEqual(observed, set(manifest.CODE_NAMES))
        self.assertEqual(len(observed), 13)
        self.assertNotIn("__pycache__", observed)
        manifest._validate_constants()
        self.assertEqual(len(manifest.SCOPED_RELATIVES), 20)
        self.assertEqual(len(manifest.LIVE_RELATIVES), 21)
        self.assertEqual(manifest.PROMOTED_NAMES, atomic.EXPECTED_TARGET_NAMES)
        self.assertEqual(
            manifest.PROMOTED_NAMES,
            (
                "c60_group_evidence.json",
                "c60_resolvent_evidence.json",
                "c60_schema.json",
                "c60_certificate.json",
                "c60_check_report.json",
                "scoped_hash_manifest.json",
            ),
        )
        producer_sources = getattr(
            producer, "CODE_SOURCE_NAMES", set(getattr(producer, "CODE_FILES"))
        )
        self.assertEqual(set(producer_sources), set(manifest.CODE_NAMES))
        self.assertEqual(getattr(checker, "CODE_SOURCE_NAMES"), set(manifest.CODE_NAMES))
        self.assertEqual(
            tuple(getattr(producer, "ARTIFACT_NAMES")),
            manifest.PROMOTED_NAMES[:2],
        )
        self.assertEqual(
            tuple(getattr(checker, "ARTIFACT_NAMES")),
            manifest.PROMOTED_NAMES[:2],
        )
        for name in manifest.CODE_NAMES:
            metadata = (CODE / name).lstat()
            expected_mode = 0o755 if name == "run_all.sh" else 0o644
            self.assertTrue(stat.S_ISREG(metadata.st_mode), name)
            self.assertEqual(stat.S_IMODE(metadata.st_mode), expected_mode, name)
            self.assertEqual(metadata.st_nlink, 1, name)

    def test_machine_sources_are_explicitly_frozen(self) -> None:
        self.assertIsNotNone(
            FROZEN_MACHINE_SOURCE_HASHES,
            "producer/checker SOURCE_STABLE seal has not yet been installed",
        )
        assert FROZEN_MACHINE_SOURCE_HASHES is not None
        self.assertEqual(set(FROZEN_MACHINE_SOURCE_HASHES), {"c60_producer.py", "c60_checker.py"})
        for name, expected in FROZEN_MACHINE_SOURCE_HASHES.items():
            self.assertEqual(hashlib.sha256((CODE / name).read_bytes()).hexdigest(), expected)

    def test_independent_source_contracts_match(self) -> None:
        produced = producer.source_contract()
        independently_rebuilt = checker.exact_source_contract()
        self.assertTrue(
            deep_exact(produced, independently_rebuilt),
            "producer/checker exact13 source contracts differ",
        )
        self.assertEqual(
            set(produced),
            {
                "schema_id", "entry_count", "exact_code_inventory",
                "exact_code_path_allowlist", "entries", "mode_policy",
                "self_reference_policy",
            },
        )
        self.assertEqual(
            produced["mode_policy"],
            "ONLY_code/run_all.sh_IS_0755_ALL_OTHER_CODE_FILES_0644",
        )
        self.assertEqual(
            [row["path"] for row in produced["entries"]],
            sorted(row["path"] for row in produced["entries"]),
        )
        for row in produced["entries"]:
            self.assertEqual(set(row), {"path", "sha256", "size_bytes", "mode_octal"})

    def test_independent_g0_contracts_match(self) -> None:
        produced = producer.rebuild_g0()[0]
        guard = checker.SnapshotGuard(())
        independently_rebuilt = checker.rebuild_g0(guard)
        self.assertTrue(
            deep_exact(produced, independently_rebuilt),
            "producer/checker G0 released-authority contracts differ",
        )
        self.assertEqual(
            set(produced),
            {
                "all_released_full_inventories_rebound",
                "batch_target_lock",
                "fixed_predecessor_paths_only",
                "formal_target_lock",
                "protected_guard",
                "released_C59",
                "schema_id",
            },
        )
        self.assertGreaterEqual(guard.rebind_checks, 2)

    def test_no_duplicate_literal_dictionary_keys(self) -> None:
        for name in manifest.CODE_NAMES:
            if not name.endswith(".py"):
                continue
            for line, keys in _literal_string_dicts(CODE / name):
                self.assertEqual(len(keys), len(set(keys)), (name, line))

    def test_producer_checker_theorem_call_graphs_are_disjoint(self) -> None:
        producer_imports = _imports(CODE / "c60_producer.py")
        checker_imports = _imports(CODE / "c60_checker.py")
        self.assertEqual(
            producer_imports & {name for name in producer_imports if name.startswith("c60_")},
            {"c60_exact", "c60_pipeline", "c60_group", "c60_resolvent"},
        )
        self.assertEqual(
            checker_imports & {name for name in checker_imports if name.startswith("c60_")},
            {"c60_exact", "c60_pipeline", "c60_checker_resolvent"},
        )
        self.assertNotIn("c60_checker", producer_imports)
        self.assertNotIn("c60_checker_group", producer_imports)
        self.assertNotIn("c60_checker_resolvent", producer_imports)
        self.assertNotIn("c60_producer", checker_imports)
        self.assertNotIn("c60_group", checker_imports)
        self.assertNotIn("c60_resolvent", checker_imports)
        checker_source = (CODE / "c60_checker.py").read_text(encoding="utf-8")
        self.assertIn("c60_checker_group.g", checker_source)

    def test_payload_key_scope_and_written_bridge_contract(self) -> None:
        self.assertEqual(tuple(getattr(producer, "PAYLOAD_KEYS")), PAYLOAD_KEYS)
        self.assertEqual(tuple(getattr(checker, "PAYLOAD_KEYS")), PAYLOAD_KEYS)
        self.assertEqual(
            set(getattr(producer, "SCOPE_NONCLAIM_KEYS")), set(SCOPE_NONCLAIM_KEYS)
        )
        self.assertEqual(
            set(getattr(checker, "SCOPE_NONCLAIM_KEYS")), set(SCOPE_NONCLAIM_KEYS)
        )
        self.assertEqual(len(SCOPE_NONCLAIM_KEYS), 30)
        expected_bridges = {
            "released_C59_transport_to_C60_fixed_fields",
            "orbit_noncollision_to_primitive_fixed_fields",
            "coefficient_orbit_partitions_to_degree_two_obstruction",
            "subgroup_lattice_to_biquadratic_and_automorphisms",
            "v4_character_relation_to_zeta_identity",
            "conductors_to_signed_absolute_and_relative_discriminants",
            "double_cosets_to_relative_local_towers_and_tameness",
        }
        self.assertEqual(
            set(getattr(producer, "WRITTEN_BRIDGE_KEYS")), expected_bridges
        )
        self.assertEqual(
            set(getattr(checker, "WRITTEN_BRIDGE_KEYS")), expected_bridges
        )

    def test_support_sources_and_evidence_are_frozen_and_scratch_free(self) -> None:
        for name, expected in FROZEN_SUPPORT_SOURCE_HASHES.items():
            raw = (CODE / name).read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), expected)
            self.assertNotIn("/tmp", raw.decode("utf-8"))
        for path in _fixture_evidence_paths():
            self.assertEqual(
                hashlib.sha256(path.read_bytes()).hexdigest(),
                FROZEN_EVIDENCE_HASHES[path.name],
            )
        self.assertTrue(
            deep_exact(
                producer_resolver.SCHEMA_DESCRIPTOR,
                checker_resolver.SCHEMA_DESCRIPTOR,
            )
        )
        self.assertEqual(
            producer_resolver.compact_sha256(producer_resolver.SCHEMA_DESCRIPTOR),
            checker_resolver.compact_sha256(checker_resolver.SCHEMA_DESCRIPTOR),
        )
        self.assertEqual(
            producer_resolver.SCHEMA_BASENAME, "c60_resolvent_schema.json"
        )
        self.assertNotIn(producer_resolver.SCHEMA_BASENAME, manifest.PROMOTED_NAMES)
        self.assertNotIn(
            "c60_resolvent", _imports(CODE / "c60_checker_resolvent.py")
        )

    def test_resolver_cli_path_helpers_enforce_canonical_results_stage(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "project"
            code = project / "code"
            results = project / "results"
            code.mkdir(parents=True)
            results.mkdir()
            stage = results / ".c60-stage-A1b2C3d4"
            stage.mkdir()
            paths = {
                "c60_resolvent_evidence.json": stage / "c60_resolvent_evidence.json",
                "c60_resolvent_schema.json": stage / "c60_resolvent_schema.json",
                "c60_resolvent_check_report.json": stage / "c60_resolvent_check_report.json",
            }
            producer_file = code / "c60_resolvent.py"
            checker_file = code / "c60_checker_resolvent.py"
            with (
                patch.object(producer_resolver, "__file__", str(producer_file)),
                patch.object(checker_resolver, "__file__", str(checker_file)),
            ):
                for basename in (
                    "c60_resolvent_evidence.json",
                    "c60_resolvent_schema.json",
                ):
                    self.assertEqual(
                        producer_resolver.staged_path(str(paths[basename]), basename)[1],
                        stage,
                    )
                for basename, path in paths.items():
                    self.assertEqual(
                        checker_resolver.staged_path(str(path), basename)[1], stage
                    )

                outside = project / "outside" / ".c60-stage-Ou7s1d34"
                nested = results / "arbitrary" / ".c60-stage-N3st3d99"
                punctuation = results / ".c60-stage-Abcd123!"
                overlong = results / ".c60-stage-ABCDEFGHI"
                for parent in (outside, nested, punctuation, overlong):
                    parent.mkdir(parents=True)
                real_stage = project / "real-stage"
                real_stage.mkdir()
                symlink_stage = results / ".c60-stage-Syml1nk2"
                symlink_stage.symlink_to(real_stage, target_is_directory=True)
                for parent in (
                    code,
                    results,
                    outside,
                    nested,
                    punctuation,
                    overlong,
                    symlink_stage,
                ):
                    for helper, basenames in (
                        (
                            producer_resolver.staged_path,
                            ("c60_resolvent_evidence.json", "c60_resolvent_schema.json"),
                        ),
                        (checker_resolver.staged_path, tuple(paths)),
                    ):
                        for basename in basenames:
                            with self.subTest(
                                helper=helper.__module__, parent=parent, basename=basename
                            ), self.assertRaises(ValueError):
                                helper(str(parent / basename), basename)

        producer_source = (CODE / "c60_resolvent.py").read_text(encoding="utf-8")
        producer_main = producer_source.index("def main()")
        self.assertLess(
            producer_source.index("staged_path(", producer_main),
            producer_source.index("build_document(", producer_main),
        )
        checker_source = (CODE / "c60_checker_resolvent.py").read_text(
            encoding="utf-8"
        )
        checker_main = checker_source.index("def main()")
        self.assertLess(
            checker_source.index("staged_path(", checker_main),
            checker_source.index("reconstruct_and_validate(", checker_main),
        )

    def test_resolver_clis_write_replay_and_reject_hostile_stage_parents(self) -> None:
        def invoke(entrypoint: object, argv: list[str]) -> dict[str, object]:
            output = io.StringIO()
            with patch.object(sys, "argv", argv), redirect_stdout(output):
                entrypoint()  # type: ignore[operator]
            return json.loads(output.getvalue())

        def snapshot(path: Path) -> tuple[bytes, int, int, int, int, int, int]:
            metadata = path.stat()
            return (
                path.read_bytes(),
                metadata.st_dev,
                metadata.st_ino,
                metadata.st_mode,
                metadata.st_size,
                metadata.st_mtime_ns,
                metadata.st_ctime_ns,
            )

        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "project"
            code = project / "code"
            results = project / "results"
            code.mkdir(parents=True)
            results.mkdir()
            stage = results / ".c60-stage-A1b2C3d4"
            stage.mkdir()
            evidence = stage / "c60_resolvent_evidence.json"
            schema = stage / "c60_resolvent_schema.json"
            report = stage / "c60_resolvent_check_report.json"
            input_paths: list[Path] = []
            for name in (
                "c59_resolvent.py",
                "c59_resolvent_evidence.json",
                "FULL_PROJECT_HASHES.sha256",
                "route_a_evaluation.yaml",
                "route_a_archive.yaml",
            ):
                path = project / name
                path.write_bytes((name + "\n").encode())
                input_paths.append(path)
            producer_file = code / "c60_resolvent.py"
            producer_file.write_bytes(b"# frozen producer resolver fixture\n")
            checker_file = code / "c60_checker_resolvent.py"
            checker_file.write_bytes(b"# frozen checker resolver fixture\n")
            document = {
                "payload": {},
                "payload_sha256": "0" * 64,
                "schema_id": "fixture",
                "schema_sha256": "1" * 64,
            }
            authority_args = [
                "--c59-resolvent-module", str(input_paths[0]),
                "--c59-resolvent-evidence", str(input_paths[1]),
                "--c59-full-manifest", str(input_paths[2]),
                "--c59-route", str(input_paths[3]),
                "--c59-route-archive", str(input_paths[4]),
            ]
            producer_base = ["c60_resolvent.py", *authority_args]
            with (
                patch.object(producer_resolver, "__file__", str(producer_file)),
                patch.object(
                    producer_resolver, "build_document", return_value=document
                ) as build_document,
            ):
                written = invoke(
                    producer_resolver.main,
                    producer_base
                    + ["--output", str(evidence), "--schema-output", str(schema)],
                )
                evidence_snapshot = snapshot(evidence)
                schema_snapshot = snapshot(schema)
                replayed = invoke(
                    producer_resolver.main,
                    producer_base
                    + [
                        "--check-existing", str(evidence),
                        "--check-existing-schema", str(schema),
                    ],
                )
                self.assertEqual(snapshot(evidence), evidence_snapshot)
                self.assertEqual(snapshot(schema), schema_snapshot)
                self.assertEqual(written["mode"], "write")
                self.assertEqual(replayed["mode"], "replay")
                self.assertEqual(build_document.call_count, 2)

                outside = project / "outside" / ".c60-stage-Ou7s1d34"
                nested = results / "arbitrary" / ".c60-stage-N3st3d99"
                punctuation = results / ".c60-stage-Abcd123!"
                overlong = results / ".c60-stage-ABCDEFGHI"
                for parent in (outside, nested, punctuation, overlong):
                    parent.mkdir(parents=True)
                real_stage = project / "real-stage"
                real_stage.mkdir()
                symlink_stage = results / ".c60-stage-Syml1nk2"
                symlink_stage.symlink_to(real_stage, target_is_directory=True)
                rejected_parents = (
                    code, results, outside, nested, punctuation, overlong, symlink_stage
                )
                before_hostile_calls = build_document.call_count
                for parent in rejected_parents:
                    hostile_evidence = parent / evidence.name
                    hostile_schema = parent / schema.name
                    for destination in (
                        ["--output", str(hostile_evidence), "--schema-output", str(schema)],
                        ["--output", str(evidence), "--schema-output", str(hostile_schema)],
                    ):
                        with self.subTest(cli="producer", target=destination[-1]), self.assertRaises(ValueError):
                            invoke(producer_resolver.main, producer_base + destination)
                self.assertEqual(build_document.call_count, before_hostile_calls)

            checker_base = [
                "c60_checker_resolvent.py",
                "--evidence", str(evidence),
                "--schema", str(schema),
                *authority_args,
            ]
            with (
                patch.object(checker_resolver, "__file__", str(checker_file)),
                patch.object(
                    checker_resolver,
                    "reconstruct_and_validate",
                    return_value={"checks": {"fixture": True}},
                ) as reconstruct,
            ):
                written = invoke(
                    checker_resolver.main,
                    checker_base + ["--report", str(report)],
                )
                evidence_snapshot = snapshot(evidence)
                schema_snapshot = snapshot(schema)
                report_snapshot = snapshot(report)
                replayed = invoke(
                    checker_resolver.main,
                    checker_base + ["--check-existing-report", str(report)],
                )
                self.assertEqual(snapshot(evidence), evidence_snapshot)
                self.assertEqual(snapshot(schema), schema_snapshot)
                self.assertEqual(snapshot(report), report_snapshot)
                self.assertEqual(written["mode"], "write")
                self.assertEqual(replayed["mode"], "replay")
                self.assertEqual(reconstruct.call_count, 2)

                before_hostile_calls = reconstruct.call_count
                for parent in rejected_parents:
                    candidates = (
                        ["--evidence", str(parent / evidence.name), "--schema", str(schema), "--report", str(report)],
                        ["--evidence", str(evidence), "--schema", str(parent / schema.name), "--report", str(report)],
                        ["--evidence", str(evidence), "--schema", str(schema), "--report", str(parent / report.name)],
                    )
                    for destination in candidates:
                        argv = ["c60_checker_resolvent.py", *destination, *authority_args]
                        with self.subTest(cli="checker", target=destination[-1]), self.assertRaises(ValueError):
                            invoke(checker_resolver.main, argv)
                self.assertEqual(reconstruct.call_count, before_hostile_calls)

    def test_checker_accepts_only_one_canonical_direct_stage_parent(self) -> None:
        def namespace(parent: Path) -> SimpleNamespace:
            for name in (
                "c60_certificate.json",
                "c60_schema.json",
                "c60_group_evidence.json",
                "c60_resolvent_evidence.json",
            ):
                (parent / name).write_bytes((name + "\n").encode())
            return SimpleNamespace(
                certificate=parent / "c60_certificate.json",
                schema=parent / "c60_schema.json",
                group_evidence=parent / "c60_group_evidence.json",
                resolvent_evidence=parent / "c60_resolvent_evidence.json",
                output=parent / "c60_check_report.json",
            )

        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "project"
            results = project / "results"
            results.mkdir(parents=True)
            stage = results / ".c60-stage-A1b2C3d4"
            stage.mkdir()
            arguments = namespace(stage)
            with patch.object(checker, "PROJECT", project):
                accepted = checker.validate_fixed_paths(arguments)
            self.assertEqual(accepted[-1], stage)

            direct = namespace(results)
            with (
                patch.object(checker, "PROJECT", project),
                self.assertRaises(StrictDataError),
            ):
                checker.validate_fixed_paths(direct)

            nested = results / "arbitrary" / ".c60-stage-N3st3d99"
            nested.mkdir(parents=True)
            nested_arguments = namespace(nested)
            with (
                patch.object(checker, "PROJECT", project),
                self.assertRaises(StrictDataError),
            ):
                checker.validate_fixed_paths(nested_arguments)

        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "project"
            results = project / "results"
            results.mkdir(parents=True)
            real_stage = results / ".real-stage"
            real_stage.mkdir()
            symlink_stage = results / ".c60-stage-Syml1nk2"
            symlink_stage.symlink_to(real_stage, target_is_directory=True)
            symlink_arguments = namespace(symlink_stage)
            with (
                patch.object(checker, "PROJECT", project),
                self.assertRaises(StrictDataError),
            ):
                checker.validate_fixed_paths(symlink_arguments)

    def test_checker_rejects_stage_symlink_swap_during_validation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "project"
            results = project / "results"
            results.mkdir(parents=True)
            stage = results / ".c60-stage-A1b2C3d4"
            stage.mkdir()
            foreign = results / "foreign"
            foreign.mkdir()
            (foreign / "sentinel").write_bytes(b"foreign-must-not-change\n")
            for name in (
                "c60_certificate.json",
                "c60_schema.json",
                "c60_group_evidence.json",
                "c60_resolvent_evidence.json",
            ):
                (stage / name).write_bytes((name + "\n").encode())
            arguments = SimpleNamespace(
                certificate=stage / "c60_certificate.json",
                schema=stage / "c60_schema.json",
                group_evidence=stage / "c60_group_evidence.json",
                resolvent_evidence=stage / "c60_resolvent_evidence.json",
                output=stage / "c60_check_report.json",
            )
            original = checker.seal_directory
            calls = 0

            def swap_on_rebind(path: Path):
                nonlocal calls
                calls += 1
                if calls == 2:
                    held = stage.with_name(stage.name + "-held")
                    stage.rename(held)
                    stage.symlink_to(foreign, target_is_directory=True)
                return original(path)

            with (
                patch.object(checker, "PROJECT", project),
                patch.object(checker, "seal_directory", side_effect=swap_on_rebind),
                self.assertRaises(StrictDataError),
            ):
                checker.validate_fixed_paths(arguments)
            self.assertEqual(
                (foreign / "sentinel").read_bytes(), b"foreign-must-not-change\n"
            )

    def test_producer_accepts_only_one_canonical_direct_stage_parent(self) -> None:
        def namespace(parent: Path) -> SimpleNamespace:
            (parent / "c60_group_evidence.json").write_bytes(b"group\n")
            (parent / "c60_resolvent_evidence.json").write_bytes(b"resolvent\n")
            return SimpleNamespace(
                artifact_dir=parent,
                output=parent / "c60_certificate.json",
                schema_output=parent / "c60_schema.json",
            )

        with tempfile.TemporaryDirectory() as temporary:
            results = Path(temporary) / "project" / "results"
            results.mkdir(parents=True)
            stage = results / ".c60-stage-A1b2C3d4"
            stage.mkdir()
            with patch.object(producer, "RESULTS", results):
                binding = producer.validate_fixed_paths(namespace(stage))
            self.assertEqual(binding.parent, stage)

            with (
                patch.object(producer, "RESULTS", results),
                self.assertRaises(StrictDataError),
            ):
                producer.validate_fixed_paths(namespace(results))

            nested = results / "arbitrary" / ".c60-stage-N3st3d99"
            nested.mkdir(parents=True)
            with (
                patch.object(producer, "RESULTS", results),
                self.assertRaises(StrictDataError),
            ):
                producer.validate_fixed_paths(namespace(nested))

        with tempfile.TemporaryDirectory() as temporary:
            results = Path(temporary) / "project" / "results"
            results.mkdir(parents=True)
            real_stage = results / ".real-stage"
            real_stage.mkdir()
            symlink_stage = results / ".c60-stage-Syml1nk2"
            symlink_stage.symlink_to(real_stage, target_is_directory=True)
            with (
                patch.object(producer, "RESULTS", results),
                self.assertRaises(StrictDataError),
            ):
                producer.validate_fixed_paths(namespace(symlink_stage))

    def test_producer_stage_binding_rejects_later_symlink_swap(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results = Path(temporary) / "project" / "results"
            results.mkdir(parents=True)
            stage = results / ".c60-stage-A1b2C3d4"
            stage.mkdir()
            (stage / "c60_group_evidence.json").write_bytes(b"group\n")
            (stage / "c60_resolvent_evidence.json").write_bytes(b"resolvent\n")
            arguments = SimpleNamespace(
                artifact_dir=stage,
                output=stage / "c60_certificate.json",
                schema_output=stage / "c60_schema.json",
            )
            with patch.object(producer, "RESULTS", results):
                binding = producer.validate_fixed_paths(arguments)
            held = stage.with_name(stage.name + "-held")
            foreign = results / "foreign"
            foreign.mkdir()
            (foreign / "sentinel").write_bytes(b"foreign-must-not-change\n")
            stage.rename(held)
            stage.symlink_to(foreign, target_is_directory=True)
            with self.assertRaises(StrictDataError):
                binding.assert_unchanged("unit symlink swap")
            self.assertEqual(
                (foreign / "sentinel").read_bytes(), b"foreign-must-not-change\n"
            )

    def test_backend_allowlist_excludes_extra_cas(self) -> None:
        self.assertEqual(
            set(pipeline.EXPECTED_BACKENDS),
            {"math"},
        )
        self.assertEqual(
            pipeline.EXPECTED_BACKENDS["math"]["python"], [3, 12, 3]
        )
        self.assertEqual(pipeline.EXPECTED_BACKENDS["math"]["flint"], "0.9.0")
        self.assertEqual(pipeline.EXPECTED_BACKENDS["math"]["sympy"], "1.14.0")
        self.assertEqual(pipeline.EXPECTED_BACKENDS["math"]["networkx"], "3.5")
        self.assertEqual(pipeline.EXPECTED_BACKENDS["math"]["jsonschema"], "4.25.0")
        self.assertEqual(pipeline.EXPECTED_GAP["gap_version"], "4.11.1")
        self.assertEqual(pipeline.EXPECTED_GAP["tomlib_version"], "1.2.9")
        self.assertEqual(pipeline.EXPECTED_GAP["smallgrp_version"], "1.4.1")
        self.assertEqual(pipeline.EXPECTED_GAP["ctbllib_version"], "1.3.1")
        runner = (CODE / "run_all.sh").read_text(encoding="utf-8").lower()
        for forbidden in ("pari_python", "cypari", "singular"):
            self.assertNotIn(forbidden, runner)
        self.assertIn('--math-python "$MATH_PYTHON"', (CODE / "run_all.sh").read_text())

    def test_clean_refresh_fixture_override_and_hostile_paths(self) -> None:
        source_paths = _fixture_evidence_paths()
        source_blobs = tuple(path.read_bytes() for path in source_paths)

        def populate(parent: Path) -> None:
            parent.mkdir(parents=True, exist_ok=True)
            for name, blob in zip(EVIDENCE_NAMES, source_blobs):
                (parent / name).write_bytes(blob)

        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary) / "project"
            code = project / "code"
            results = project / "results"
            code.mkdir(parents=True)
            results.mkdir()
            for name in manifest.CODE_NAMES:
                (code / name).write_bytes((name + "\n").encode())
            for name in ("RESULTS.md", "TEST_REPORT.md"):
                (results / name).write_bytes((name + "\n").encode())
            self.assertEqual(
                {path.name for path in code.iterdir()}, set(manifest.CODE_NAMES)
            )
            self.assertEqual(
                {path.name for path in results.iterdir() if path.is_file()},
                {"RESULTS.md", "TEST_REPORT.md"},
            )
            for name in EVIDENCE_NAMES:
                self.assertFalse((results / name).exists())

            stage = results / ".c60-stage-A1b2C3d4"
            populate(stage)
            module = sys.modules[__name__]
            with (
                patch.object(module, "RESULTS", results),
                patch.dict(os.environ, {TEST_EVIDENCE_ENV: str(stage)}),
            ):
                self.assertEqual(_fixture_evidence_paths(), tuple(stage / name for name in EVIDENCE_NAMES))
                group, resolvent = _fixture_evidence_documents()
            self.assertEqual(group["schema_id"], "hcs-c60-group-evidence-v1")
            self.assertEqual(
                resolvent["schema_id"], "hcs-c60-resolvent-evidence-v1"
            )

            outside = project / "outside" / ".c60-stage-Ou7s1d34"
            nested = results / "arbitrary" / ".c60-stage-N3st3d99"
            punctuation = results / ".c60-stage-Abcd123!"
            overlong = results / ".c60-stage-ABCDEFGHI"
            for parent in (outside, nested, punctuation, overlong):
                populate(parent)
            foreign = project / "foreign-stage"
            populate(foreign)
            symlink_stage = results / ".c60-stage-Syml1nk2"
            symlink_stage.symlink_to(foreign, target_is_directory=True)
            extra_stage = results / ".c60-stage-Extra123"
            populate(extra_stage)
            (extra_stage / "unexpected").write_bytes(b"hostile\n")
            file_symlink_stage = results / ".c60-stage-Link1234"
            file_symlink_stage.mkdir()
            (file_symlink_stage / EVIDENCE_NAMES[0]).write_bytes(source_blobs[0])
            (file_symlink_stage / EVIDENCE_NAMES[1]).symlink_to(source_paths[1])

            rejected = (
                code,
                results,
                outside,
                nested,
                punctuation,
                overlong,
                symlink_stage,
                extra_stage,
                file_symlink_stage,
                Path(".c60-stage-relative"),
            )
            with patch.object(module, "RESULTS", results):
                for candidate in rejected:
                    with (
                        self.subTest(candidate=candidate),
                        patch.dict(
                            os.environ, {TEST_EVIDENCE_ENV: str(candidate)}
                        ),
                        self.assertRaises(StrictDataError),
                    ):
                        _fixture_evidence_paths()

        runner = (CODE / "run_all.sh").read_text(encoding="utf-8")
        rejection = runner.index(
            "PYTHONPATH PYTHONHOME PYTHONSAFEPATH BASH_ENV ENV C60_TEST_EVIDENCE_DIR"
        )
        stage_only_assignment = runner.index(
            'C60_TEST_EVIDENCE_DIR="$STAGE_DIR"'
        )
        unittest_launch = runner.index("-m unittest discover")
        self.assertLess(rejection, stage_only_assignment)
        self.assertLess(stage_only_assignment, unittest_launch)
        self.assertEqual(runner.count('C60_TEST_EVIDENCE_DIR="$STAGE_DIR"'), 1)

    def test_actual_payload_builders_match_on_shared_fixture(self) -> None:
        evidence_paths = _fixture_evidence_paths()
        evidence_raw = tuple(path.read_bytes() for path in evidence_paths)
        group_evidence, resolvent_document = _fixture_evidence_documents()
        producer_artifact_contract = producer._artifact_contract_from_documents(
            group_evidence,
            resolvent_document,
            group_size_bytes=len(evidence_raw[0]),
            resolver_size_bytes=len(evidence_raw[1]),
        )
        checker_artifact_contract = checker.artifact_contract(
            evidence_paths[0],
            evidence_raw[0],
            group_evidence,
            evidence_paths[1],
            evidence_raw[1],
            resolvent_document,
        )
        self.assertTrue(
            deep_exact(producer_artifact_contract, checker_artifact_contract),
            "producer/checker artifact-contract projections differ",
        )
        self.assertEqual(
            set(producer_artifact_contract),
            {
                "artifact_count",
                "artifacts",
                "component_contracts",
                "immutable_inputs",
                "same_real_nonsymlink_parent",
                "schema_id",
                "source_owned_full_document_validation",
            },
        )
        self.assertEqual(
            set(producer_artifact_contract["artifacts"][0]),
            {
                "path", "format", "sha256", "size_bytes", "schema_id",
                "internal_report_sha256", "component_aggregate_sha256",
            },
        )
        self.assertEqual(
            set(producer_artifact_contract["artifacts"][1]),
            {
                "path", "format", "sha256", "size_bytes", "schema_id",
                "internal_report_sha256", "component_aggregate_sha256",
                "schema_descriptor_sha256",
            },
        )
        self.assertTrue(
            deep_exact(
                producer_artifact_contract["component_contracts"],
                {
                    "group": producer.GROUP_COMPONENT,
                    "primitive_resolvent": producer.RESOLVER_COMPONENT,
                },
            )
        )
        self.assertEqual(
            set(producer_artifact_contract["component_contracts"]["group"]),
            {
                "aggregate_sha256", "producer_sha256", "checker_sha256",
                "evidence_sha256", "replay_sha256", "schema_sha256",
                "artifact_count", "total_bytes",
            },
        )
        self.assertEqual(
            set(
                producer_artifact_contract["component_contracts"][
                    "primitive_resolvent"
                ]
            ),
            {
                "aggregate_sha256", "producer_sha256", "checker_sha256",
                "evidence_sha256", "payload_sha256", "artifact_count",
                "total_bytes",
            },
        )
        source_contract_value = producer.source_contract()
        g0 = producer.rebuild_g0()[0]
        checker_g0_guard = checker.SnapshotGuard(())
        checker_g0 = checker.rebuild_g0(checker_g0_guard)
        self.assertTrue(
            deep_exact(g0, checker_g0),
            "producer/checker G0 contracts differ in the actual shared fixture",
        )
        self.assertGreaterEqual(checker_g0_guard.rebind_checks, 2)
        shared = (
            source_contract_value,
            g0,
            producer_artifact_contract,
            group_evidence,
            resolvent_document,
            _fixture_backend_contract(),
            group_evidence["independent_replay"]["gap_checker"][
                "checker_projection_sha256"
            ],
            FROZEN_EVIDENCE_HASHES["c60_group_evidence.json"],
            FROZEN_EVIDENCE_HASHES["c60_resolvent_evidence.json"],
        )
        self.assertEqual(
            tuple(inspect.signature(producer.build_payload).parameters),
            tuple(inspect.signature(checker.expected_payload).parameters),
        )
        self.assertEqual(
            tuple(inspect.signature(producer.build_payload).parameters),
            (
                "source_contract_value",
                "g0",
                "artifact_contract_value",
                "group_evidence",
                "resolver_evidence",
                "backend_contract_value",
                "group_replay_sha256",
                "group_evidence_sha256",
                "resolver_evidence_sha256",
            ),
        )
        produced = producer.build_payload(*shared)
        rebuilt = checker.expected_payload(*shared)
        diff_count = _semantic_diff_count(produced, rebuilt)
        self.assertTrue(deep_exact(produced, rebuilt), f"payload diff_count={diff_count}")
        self.assertEqual(diff_count, 0)
        self.assertEqual(tuple(produced), PAYLOAD_KEYS)
        g7 = produced["G7_independence_scope_release"]
        self.assertEqual(
            {key: g7[key] for key in CANONICAL_G7_COUNTS},
            CANONICAL_G7_COUNTS,
        )
        self.assertEqual(
            g7["evidence_rebound_mutation_count_expected"],
            10,
            "G7 counts evidence-document rebounds only, not artifact cases",
        )
        self.assertEqual(ACTUAL_DEEP_EVIDENCE_AND_ARTIFACT_HOSTILE_CASES, 12)
        self.assertEqual(set(produced["scope_nonclaims"]), set(SCOPE_NONCLAIM_KEYS))
        self.assertTrue(
            all(value is False for value in produced["scope_nonclaims"].values())
        )
        self.assertEqual(
            produced["nonresults"]["semantic_firewall"],
            "NO_BAD_EULER_OR_ROOT_NUMBER",
        )

    def test_actual_evidence_and_artifact_hostile_case_count(self) -> None:
        evidence_paths = _fixture_evidence_paths()
        evidence_raw = tuple(path.read_bytes() for path in evidence_paths)
        group_evidence, resolvent_document = _fixture_evidence_documents()
        artifacts = producer._artifact_contract_from_documents(
            group_evidence,
            resolvent_document,
            group_size_bytes=len(evidence_raw[0]),
            resolver_size_bytes=len(evidence_raw[1]),
        )
        shared = (
            producer.source_contract(),
            producer.rebuild_g0()[0],
            artifacts,
            group_evidence,
            resolvent_document,
            _fixture_backend_contract(),
            group_evidence["independent_replay"]["gap_checker"][
                "checker_projection_sha256"
            ],
            FROZEN_EVIDENCE_HASHES["c60_group_evidence.json"],
            FROZEN_EVIDENCE_HASHES["c60_resolvent_evidence.json"],
        )
        expected = producer.build_payload(*shared)
        self.assertTrue(deep_exact(expected, checker.expected_payload(*shared)))
        self.assertEqual(
            {
                key: expected["G7_independence_scope_release"][key]
                for key in CANONICAL_G7_COUNTS
            },
            CANONICAL_G7_COUNTS,
        )
        schema = checker.schema_descriptor(expected)
        certificate = {
            "schema": schema,
            "schema_sha256": hashlib.sha256(
                canonical_leaf_bytes(schema)
            ).hexdigest(),
            "payload": expected,
            "payload_sha256": hashlib.sha256(
                canonical_leaf_bytes(expected)
            ).hexdigest(),
        }
        guard = checker.SnapshotGuard(())
        projection, projection_sha256, projection_size = (
            checker.run_group_projection(Path("/usr/bin/gap"), guard)
        )
        checker.validate_group_evidence(
            group_evidence,
            projection,
            projection_sha256,
            projection_size,
        )
        self.assertTrue(
            deep_exact(
                checker.validate_resolver_evidence(resolvent_document, guard),
                resolvent_document["payload"],
            )
        )
        observed = checker.evidence_rebound_suite(
            certificate,
            schema,
            expected,
            schema,
            group_evidence,
            projection,
            resolvent_document,
            guard,
        )
        self.assertEqual(
            observed,
            {
                "actual_group_verifier_mutations_rejected": 6,
                "actual_resolver_verifier_mutations_rejected": 4,
                "self_consistent_evidence_rebound_mutations_rejected": 10,
                "additional_artifact_hostile_rebounds_rejected": 2,
                "total_evidence_and_artifact_rebounds_rejected": 12,
            },
        )
        self.assertEqual(
            observed["actual_group_verifier_mutations_rejected"]
            + observed["actual_resolver_verifier_mutations_rejected"],
            CANONICAL_G7_COUNTS["evidence_rebound_mutation_count_expected"],
        )
        self.assertEqual(
            observed["self_consistent_evidence_rebound_mutations_rejected"]
            + observed["additional_artifact_hostile_rebounds_rejected"],
            ACTUAL_DEEP_EVIDENCE_AND_ARTIFACT_HOSTILE_CASES,
        )

    def test_runner_requires_post_checker_runtime_counter_validation(self) -> None:
        source = (CODE / "run_all.sh").read_text(encoding="utf-8")
        checker_call = source.index('"$MATH_PYTHON" -s -B "$CODE_DIR/c60_checker.py"')
        runtime_check = source.index("--verify-runtime-report")
        manifest_write = source.index("--write", runtime_check)
        self.assertLess(checker_call, runtime_check)
        self.assertLess(runtime_check, manifest_write)
        self.assertEqual(source.count("--verify-runtime-report"), 1)
        self.assertTrue(
            deep_exact(pipeline.RUNTIME_G7_COUNTS, CANONICAL_G7_COUNTS)
        )
        self.assertEqual(
            pipeline.RUNTIME_EVIDENCE_REBOUND_COUNTS,
            {
                "actual_group_verifier_mutations_rejected": 6,
                "actual_resolver_verifier_mutations_rejected": 4,
                "additional_artifact_hostile_rebounds_rejected": 2,
                "self_consistent_evidence_rebound_mutations_rejected": 10,
                "total_evidence_and_artifact_rebounds_rejected": 12,
            },
        )

    def test_runner_has_explicit_three_state_and_persistent_dirfd_contract(self) -> None:
        source = (CODE / "run_all.sh").read_text(encoding="utf-8")
        for token in (
            'RUN_STATE="STAGED_VERIFIED"',
            'RUN_STATE="LIVE_COMMITTED"',
            'RUN_STATE="RELEASE_VERIFIED"',
            "POSTCOMMIT_INCOMPLETE",
            "COMMITTED_WITH_DEBRIS—DO NOT RETRY",
            'exec {RESULTS_FD}<"$RESULTS_DIR"',
            'stat -Lc \'%d\' "/proc/self/fd/$RESULTS_FD"',
            'stat -Lc \'%i\' "/proc/self/fd/$RESULTS_FD"',
            "results pathname device/inode changed",
            "results parent identity changed; retaining all stage/transaction evidence",
        ):
            self.assertIn(token, source)
        self.assertGreaterEqual(source.count("verify_results_binding"), 20)
        self.assertIn(
            'mktemp -d "/proc/self/fd/$RESULTS_FD/.c60-stage-XXXXXXXX"', source
        )
        self.assertNotIn(
            'mktemp -d "$RESULTS_DIR/.c60-stage-XXXXXXXX"', source
        )
        self.assertIn(
            '--group-evidence "$STAGE_DIR/c60_group_evidence.json"', source
        )
        self.assertIn(
            '--resolvent-evidence "$STAGE_DIR/c60_resolvent_evidence.json"', source
        )
        self.assertNotIn('exec /usr/bin/bash -p "$CODE_DIR/run_all.sh"', source)
        self.assertIn('/usr/bin/bash -p "$CODE_DIR/run_all.sh"', source)
        match = re.search(
            r"classify_promotion_status\(\) \{.*?^\}",
            source,
            flags=re.MULTILINE | re.DOTALL,
        )
        self.assertIsNotNone(match)
        probe = (
            match.group(0)
            + "\nfor value in 0 74 75 1 2 129 137 143; do "
            + 'classify_promotion_status "$value"; '
            + 'printf "%s\\n" "$PROMOTION_CLASS"; done\n'
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

    def test_documented_no_concurrent_mutator_boundary_is_not_overclaimed(self) -> None:
        readme = " ".join(
            (CODE / "README.md").read_text(encoding="utf-8").split()
        )
        required = (
            "same-UID",
            "no concurrent pathname mutator",
            "between",
            "external producer child",
            "first path open",
            "inherited directory fds",
            "locked pre-documentation",
            "historical/frozen",
            "no claim that its producer or checker will live-replay",
            "later documentation layer",
            "reserved `C60_TEST_EVIDENCE_DIR` unset",
            "only to the unittest subprocess",
        )
        for token in required:
            self.assertIn(token, readme)
        self.assertTrue(
            "`IMPLEMENTATION_PENDING / NO_REFRESH`" in readme
            or "`PREFREEZE MACHINE CANDIDATE / NO_REFRESH`" in readme
        )


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
        stage = results / ".c60-stage-A1b2C3d4"
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
        stage = results / ".c60-stage-A1b2C3d4"
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
        self.assertFalse(any(path.name.startswith(".c60-transaction-") for path in results.iterdir()))

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
                if renamed and binding.path.name.startswith(".c60-transaction-"):
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
                        path.name.startswith(".c60-transaction-")
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
                any(path.name.startswith(".c60-transaction-") for path in results.iterdir())
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
                any(path.name.startswith(".c60-transaction-") for path in results.iterdir())
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
            argv = ["c60_atomic_promote.py", "--result-dir", str(results)]
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
        for debris in (".c60-stage-stale", ".c60-transaction-stale", atomic.LOCK_NAME):
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
            self.assertTrue(any(path.name.startswith(".c60-transaction-") for path in results.iterdir()))

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
            transactions = [path for path in results.iterdir() if path.name.startswith(".c60-transaction-")]
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
                path for path in results.iterdir() if path.name.startswith(".c60-transaction-")
            ]
            self.assertEqual(len(transactions), 1)
            self.assertTrue((transactions[0] / "old-00").exists())

    def test_transaction_cleanup_validates_every_resident_before_deleting(self) -> None:
        for mutation in ("missing", "substitution", "extra", "dangling-directory"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as temporary:
                results = Path(temporary) / "results"
                results.mkdir()
                transaction = results / ".c60-transaction-unit"
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
            stage = results / ".c60-stage-A1b2C3d4"
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
            "from c60_exact import reject_optimized_python;reject_optimized_python()"
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

    def test_stage_name_requires_exact_eight_alphanumeric_suffix(self) -> None:
        hostile_names = (
            ".c60-stage-ABC1234",
            ".c60-stage-ABCDEFGHI",
            ".c60-stage-ABC!2345",
        )
        for name in hostile_names:
            with self.subTest(layer="atomic", name=name), tempfile.TemporaryDirectory() as temporary:
                results = Path(temporary) / "results"
                results.mkdir()
                stage = results / name
                stage.mkdir()
                metadata = stage.stat()
                with self.assertRaises(StrictDataError):
                    atomic.stage_snapshot(
                        results,
                        stage,
                        expected_device=metadata.st_dev,
                        expected_inode=metadata.st_ino,
                    )

            with self.subTest(layer="manifest", name=name), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                code, results = self.make_project(root)
                stage = results / name
                stage.mkdir()
                p1, p2, p3, p4 = self.patched(root, code, results)
                with p1, p2, p3, p4, self.assertRaises(StrictDataError):
                    manifest.artifact_paths(stage)

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

    def test_out_of_scope_hardlink_to_code_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            code, results = self.make_project(root)
            os.link(code / "README.md", root / "outside-alias-to-code")
            p1, p2, p3, p4 = self.patched(root, code, results)
            with (
                p1,
                p2,
                p3,
                p4,
                self.assertRaisesRegex(StrictDataError, "hardlink"),
            ):
                manifest.artifact_paths()

    def test_out_of_scope_hardlink_to_result_rejected(self) -> None:
        for name in (
            "RESULTS.md",
            "c60_group_evidence.json",
            "scoped_hash_manifest.json",
        ):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                code, results = self.make_project(root)
                os.link(results / name, root / f"outside-alias-to-{name}")
                p1, p2, p3, p4 = self.patched(root, code, results)
                with (
                    p1,
                    p2,
                    p3,
                    p4,
                    self.assertRaisesRegex(StrictDataError, "hardlink"),
                ):
                    manifest.artifact_paths()

    def test_stage_promoted_hardlink_and_verified_manifest_hardlink_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            code, results = self.make_project(root)
            stage = results / ".c60-stage-A1b2C3d4"
            stage.mkdir()
            for name in manifest.PROMOTED_NAMES[:-1]:
                (stage / name).write_bytes(b"stage\n")
            os.link(
                stage / "c60_group_evidence.json",
                root / "outside-alias-to-stage-input",
            )
            p1, p2, p3, p4 = self.patched(root, code, results)
            with (
                p1,
                p2,
                p3,
                p4,
                self.assertRaisesRegex(StrictDataError, "hardlink"),
            ):
                manifest.artifact_paths(stage)

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            code, results = self.make_project(root)
            os.link(
                results / "scoped_hash_manifest.json",
                root / "outside-alias-to-verified-manifest",
            )
            p1, p2, p3, p4 = self.patched(root, code, results)
            with (
                p1,
                p2,
                p3,
                p4,
                self.assertRaisesRegex(StrictDataError, "link-count-one"),
            ):
                manifest.verify_manifest(results / "scoped_hash_manifest.json")

    def test_write_without_stage_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            code, results = self.make_project(root)
            p1, p2, p3, p4 = self.patched(root, code, results)
            argv = ["c60_hash_manifest.py", "--write", "--manifest", str(results / "scoped_hash_manifest.json")]
            with p1, p2, p3, p4, patch.object(sys, "argv", argv), self.assertRaises(StrictDataError):
                manifest.main()

    def test_stage_inode_swap_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            code, results = self.make_project(root)
            # A refresh may have any fixed live targets, but its one active
            # stage must supply all five nonmanifest promoted inputs.
            stage = results / ".c60-stage-A1b2C3d4"
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
            stage = results / ".c60-stage-A1b2C3d4"
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
                "c60_hash_manifest.py",
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
                TEST_EVIDENCE_ENV,
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

            injected_evidence_environment = {
                **clean_base,
                TEST_EVIDENCE_ENV: str(root / "hostile-stage"),
                "PYTHONDONTWRITEBYTECODE": "1",
            }
            injected_completed = subprocess.run(
                [str(CODE / "run_all.sh")],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=injected_evidence_environment,
                cwd="/",
            )
            self.assertEqual(injected_completed.returncode, 2)
            self.assertIn(
                b"C60_TEST_EVIDENCE_DIR must be completely unset",
                injected_completed.stderr,
            )

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
            'mktemp -d "/proc/self/fd/$RESULTS_FD/.c60-stage-XXXXXXXX"',
            runner_source,
        )
        self.assertNotIn(
            'mktemp -d "$RESULTS_DIR/.c60-stage-XXXXXXXX"', runner_source
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
STAGE_FD_PATH="$(/usr/bin/mktemp -d "/proc/self/fd/$RESULTS_FD/.c60-stage-XXXXXXXX")"
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
            self.assertRegex(stage_name, r"^\.c60-stage-[A-Za-z0-9]{8}$")
            self.assertTrue((results / stage_name).is_dir())
            self.assertEqual({path.name for path in foreign.iterdir()}, {"sentinel"})
            self.assertEqual(
                (foreign / "sentinel").read_bytes(), b"foreign-must-not-change\n"
            )

    def test_missing_backends_fail_closed(self) -> None:
        missing = Path("/definitely/missing/hcs-c60-backend")
        with self.assertRaises((StrictDataError, FileNotFoundError)):
            pipeline.python_preflight(missing)
        with self.assertRaises((StrictDataError, FileNotFoundError)):
            pipeline.python_preflight(missing)
        with self.assertRaises((StrictDataError, FileNotFoundError)):
            pipeline.gap_preflight(missing)


if __name__ == "__main__":
    if sys.flags.optimize or "PYTHONOPTIMIZE" in os.environ:
        raise SystemExit("optimized Python is forbidden")
    unittest.main(verbosity=2)
