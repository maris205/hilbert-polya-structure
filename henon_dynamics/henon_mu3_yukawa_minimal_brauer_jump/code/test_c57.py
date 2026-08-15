#!/usr/bin/env python3
"""Hostile unit and transaction tests for the HCS-C57 machine package."""

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

import c57_atomic_promote as atomic
import c57_checker as checker
from c57_exact import (
    StrictDataError,
    canonical_json_bytes,
    deep_exact,
    deterministic_gzip,
    require_canonical_compact_json,
    strict_json_loads,
)
import c57_hash_manifest as manifest
import c57_producer as producer
import c57_pipeline as pipeline


CODE = Path(__file__).resolve().parent


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
        self.assertEqual(observed, set(checker.CODE_SOURCE_FILES))
        self.assertEqual(len(observed), 18)
        self.assertNotIn("__pycache__", observed)

    def test_no_duplicate_literal_dict_keys(self) -> None:
        for name in checker.CODE_SOURCE_FILES:
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
        tree = ast.parse((CODE / "c57_checker.py").read_text(encoding="utf-8"))
        forbidden_modules = {
            "c57_producer",
            "c57_group",
            "c57_incidence_bridge",
            "c57_incidence_char0_verify",
            "c57_resolver_replay",
            "c57_irreducibility",
            "c57_a12_reconstruction",
            "c57_flint_carrier_identity",
            "c57_quartic_pivot",
        }
        forbidden_calls = {"run_canonical_report", "producer_exact_reports", "rerun_reports"}
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                self.assertFalse({alias.name for alias in node.names} & forbidden_modules)
            if isinstance(node, ast.ImportFrom):
                self.assertNotIn(node.module, forbidden_modules)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                self.assertNotIn(node.func.id, forbidden_calls)

    def test_producer_checker_payload_shapes_are_exact(self) -> None:
        backends = {"backend": "sentinel"}
        source = {"source": "sentinel"}
        g0 = {"g0": "sentinel"}
        artifacts = {"artifacts": "sentinel"}
        reports = checker.EXPECTED_PRODUCER_EXACT_REPORTS
        with (
            patch.object(producer, "normalized_backends", return_value=backends),
            patch.object(producer, "c57_source_contract", return_value=source),
            patch.object(producer, "source_lock", return_value=g0),
            patch.object(producer, "artifacts", return_value=artifacts),
            patch.object(producer, "producer_exact_reports", return_value=reports),
        ):
            actual = producer.build_payload(
                Path("/sentinel"), Path("/pari"), Path("/flint"), Path("/singular")
            )
        expected = checker.expected_payload(backends, source, g0, artifacts)
        self.assertTrue(deep_exact(actual, expected))
        self.assertEqual([key for key in actual if key.startswith("G")], [
            "G0_C56_source_lock",
            "G1_exact_incidence",
            "G2_group_and_H1",
            "G3_resolvers_and_fixed_field",
            "G4_orientation_quadratic",
            "G5_degree_12_carrier",
            "G6_determinant_quartic_and_rank",
            "G7_divisor_and_quaternion",
        ])

    def test_manifest_constants(self) -> None:
        manifest._validate_constants()
        self.assertEqual(len(manifest.SCOPED_RELATIVES), 28)
        self.assertEqual(len(manifest.LIVE_RELATIVES), 29)
        self.assertEqual(manifest.PROMOTED_NAMES, atomic.EXPECTED_TARGET_NAMES)

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
        stage = results / ".c57-stage-unit"
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
        stage = results / ".c57-stage-unit"
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
        self.assertFalse(any(path.name.startswith(".c57-transaction-") for path in results.iterdir()))

    def test_all_nine_injected_failures_restore_absent_existing_and_mixed(self) -> None:
        for state in ("absent", "existing", "mixed"):
            for failure in range(1, 10):
                with self.subTest(state=state, failure=failure), tempfile.TemporaryDirectory() as temporary:
                    results, _, pairs, before = self.make_layout(Path(temporary), state)
                    with self.assertRaisesRegex(RuntimeError, "test-injected"):
                        self.promote(pairs, results, fail_after=failure)
                    self.assert_preimage(results, before)

    def test_success_promotes_all_nine(self) -> None:
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
            original_bound_fsync = atomic._fsync_bound_directory
            original_result_fsync = atomic._fsync_directory
            original_fingerprint = atomic.fingerprint
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

            def tracked_bound(path, identity):
                value = original_bound_fsync(path, identity)
                if renamed:
                    events.append("transaction-fsync")
                return value

            def tracked_result(path):
                value = original_result_fsync(path)
                if renamed and Path(path) == results:
                    events.append("result-fsync")
                return value

            def fail_placed(path, label="file"):
                nonlocal injected
                if label == "placed target" and not injected:
                    injected = True
                    self.assertEqual(
                        events[-3:], ["rename", "transaction-fsync", "result-fsync"]
                    )
                    raise RuntimeError("post-rename fingerprint injection")
                return original_fingerprint(path, label)

            with (
                patch.object(atomic.os, "replace", side_effect=tracked_replace),
                patch.object(atomic, "_fsync_bound_directory", side_effect=tracked_bound),
                patch.object(atomic, "_fsync_directory", side_effect=tracked_result),
                patch.object(atomic, "fingerprint", side_effect=fail_placed),
                self.assertRaisesRegex(RuntimeError, "post-rename"),
            ):
                self.promote(pairs, results)
            self.assertTrue(injected)
            self.assert_preimage(results, before)

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
                any(path.name.startswith(".c57-transaction-") for path in results.iterdir())
            )
            self.assertFalse((results / atomic.LOCK_NAME).exists())

        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, _ = self.make_layout(Path(temporary), "existing")
            expected = {name: _snapshot(source) for source, name in pairs}
            original_release = atomic.release_lock

            def foreign_release(lock):
                held = lock.path.with_name(".held-original-lock")
                lock.path.rename(held)
                lock.path.write_bytes(b"foreign-lock\n")
                return original_release(lock)

            with patch.object(atomic, "release_lock", side_effect=foreign_release):
                with self.assertRaisesRegex(atomic.PostCommitError, "COMMITTED_WITH_DEBRIS"):
                    self.promote(pairs, results)
            for name, snapshot in expected.items():
                self.assertEqual(_snapshot(results / name), snapshot)
            self.assertEqual((results / atomic.LOCK_NAME).read_bytes(), b"foreign-lock\n")
            self.assertFalse(
                any(path.name.startswith(".c57-transaction-") for path in results.iterdir())
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
            argv = ["c57_atomic_promote.py", "--result-dir", str(results)]
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
        for debris in (".c57-stage-stale", ".c57-transaction-stale", atomic.LOCK_NAME):
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

            def mutate_target(entries):
                entries[0].target.write_bytes(b"hostile-target\n")
                return original(entries)

            with patch.object(atomic, "_verify_precommit_preimages", side_effect=mutate_target):
                with self.assertRaises(atomic.RollbackError):
                    self.promote(pairs, results)
            # The hostile precommit mutation is deliberately not overwritten:
            # no live replacement had yet been authorized.
            self.assertEqual((results / pairs[0][1]).read_bytes(), b"hostile-target\n")
            self.assertTrue(any(path.name.startswith(".c57-transaction-") for path in results.iterdir()))

        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, before = self.make_layout(Path(temporary), "existing")
            original = atomic._verify_precommit_preimages

            def mutate_source(entries):
                original(entries)
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
            original = atomic.fingerprint
            replaced = False

            def replace_before_rollback(path, label="file"):
                nonlocal replaced
                if label == "rollback target" and not replaced:
                    replaced = True
                    snapshot = _snapshot(path)
                    assert snapshot is not None
                    raw, mode, mtime_ns = snapshot
                    foreign = path.with_name(".foreign-identical")
                    _write(foreign, raw, mode, mtime_ns)
                    os.replace(foreign, path)
                return original(path, label)

            with patch.object(atomic, "fingerprint", side_effect=replace_before_rollback):
                with self.assertRaises(atomic.RollbackError):
                    self.promote(pairs, results, fail_after=1)
            transactions = [path for path in results.iterdir() if path.name.startswith(".c57-transaction-")]
            self.assertEqual(len(transactions), 1)
            self.assertTrue(any(path.name.startswith("old-") for path in transactions[0].iterdir()))

    def test_foreign_backup_substitution_before_restore_is_retained(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results, _, pairs, _ = self.make_layout(Path(temporary), "existing")
            original = atomic.fingerprint
            replaced = False

            def replace_backup(path, label="file"):
                nonlocal replaced
                if label == "rollback backup" and not replaced:
                    replaced = True
                    raw, mode, mtime_ns = _snapshot(path)  # type: ignore[misc]
                    foreign = path.with_name(".foreign-backup")
                    _write(foreign, raw, mode, mtime_ns)
                    os.replace(foreign, path)
                return original(path, label)

            with patch.object(atomic, "fingerprint", side_effect=replace_backup):
                with self.assertRaises(atomic.RollbackError):
                    self.promote(pairs, results, fail_after=1)
            self.assertTrue(replaced)
            transactions = [
                path for path in results.iterdir() if path.name.startswith(".c57-transaction-")
            ]
            self.assertEqual(len(transactions), 1)
            self.assertTrue((transactions[0] / "old-00").exists())

    def test_transaction_cleanup_validates_every_resident_before_deleting(self) -> None:
        for mutation in ("missing", "substitution", "extra", "dangling-directory"):
            with self.subTest(mutation=mutation), tempfile.TemporaryDirectory() as temporary:
                results = Path(temporary) / "results"
                results.mkdir()
                transaction = results / ".c57-transaction-unit"
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
                with self.assertRaises(StrictDataError):
                    atomic._cleanup_transaction([entry], transaction, identity, results)
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
            with patch.object(atomic.os, "write", return_value=0):
                with self.assertRaisesRegex(StrictDataError, "short"):
                    atomic.acquire_lock(results)
            self.assertFalse((results / atomic.LOCK_NAME).exists())

    def test_stage_cleanup_rejects_replacement_and_extension_is_exact(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            results = Path(temporary) / "results"
            results.mkdir()
            stage = results / ".c57-stage-unit"
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
            lock = atomic.acquire_lock(results)
            held = results / ".held-original-lock"
            lock.path.rename(held)
            lock.path.write_bytes(b"foreign\n")
            with self.assertRaisesRegex(StrictDataError, "foreign lock retained"):
                atomic.release_lock(lock)
            self.assertEqual(lock.path.read_bytes(), b"foreign\n")
            lock.path.unlink()
            held.unlink()

    def test_optimized_python_and_environment_rejected(self) -> None:
        source = (
            "import pathlib,sys;sys.path.insert(0," + repr(str(CODE)) + ");"
            "from c57_exact import reject_optimized_python;reject_optimized_python()"
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
        for kind in ("file", "directory", "symlink", "fifo"):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                code, results = self.make_project(root)
                hostile = results / "hostile"
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
            argv = ["c57_hash_manifest.py", "--write", "--manifest", str(results / "scoped_hash_manifest.json")]
            with p1, p2, p3, p4, patch.object(sys, "argv", argv), self.assertRaises(StrictDataError):
                manifest.main()

    def test_stage_inode_swap_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            code, results = self.make_project(root)
            # A refresh may have any fixed live targets, but its one active
            # stage must supply all eight nonmanifest promoted inputs.
            stage = results / ".c57-stage-unit"
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
            stage = results / ".c57-stage-unit"
            stage.mkdir()
            for name in manifest.PROMOTED_NAMES[:-1]:
                (stage / name).write_bytes(b"stage\n")
            original = manifest.manifest_bytes

            def swap_after_bytes(active):
                raw = original(active)
                old = active.with_name(active.name + "-old")
                active.rename(old)
                active.mkdir()
                return raw

            argv = [
                "c57_hash_manifest.py",
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

    def test_missing_backends_fail_closed(self) -> None:
        missing = Path("/definitely/missing/hcs-c57-backend")
        with self.assertRaises((StrictDataError, FileNotFoundError)):
            pipeline.python_preflight(missing, Path(sys.executable))
        with self.assertRaises((StrictDataError, FileNotFoundError)):
            pipeline.python_preflight(Path("/usr/bin/python3"), missing)
        with self.assertRaises((StrictDataError, FileNotFoundError)):
            pipeline.singular_preflight(missing)


if __name__ == "__main__":
    if sys.flags.optimize or "PYTHONOPTIMIZE" in os.environ:
        raise SystemExit("optimized Python is forbidden")
    unittest.main(verbosity=2)
