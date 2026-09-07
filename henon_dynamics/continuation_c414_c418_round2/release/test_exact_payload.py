"""Adversarial temporary-fixture tests; never seals the real release tree."""

import copy
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

import exact_payload as release


def snapshot(root):
    """Names, types, link targets, modes and bytes; deliberately excludes atime."""
    result = {}
    for directory, names, files in os.walk(root, followlinks=False):
        for name in sorted(names + files):
            path = Path(directory) / name
            relative = path.relative_to(root).as_posix()
            info = path.lstat()
            if stat.S_ISLNK(info.st_mode):
                data = os.readlink(path)
            elif stat.S_ISREG(info.st_mode):
                data = path.read_bytes()
            else:
                data = None
            result[relative] = (info.st_mode, info.st_nlink, data)
    return result


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="c414-release-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "payload"
        self.root.mkdir()
        (self.root / "papers" / "build_author").mkdir(parents=True)
        (self.root / "paper.tex").write_bytes(b"approved proof\n")
        (self.root / ".gitignore").write_bytes(b"build_author/\n*.pyc\n")
        (self.root / "papers" / "build_author" / "main.aux").write_bytes(b"\\relax\n")
        (self.root / "papers" / "build_author" / "page.png").write_bytes(b"\x89PNG\r\n\x00\xff")
        (self.root / "cached.pyc").write_bytes(b"\x00\xff\x13\n")
        self.raw = release.inventory(self.root)
        self.pin = release.sha256(self.raw)
        self.ledger = json.loads(self.raw)
        (self.root / release.LEDGER).write_bytes(self.raw)

    def fail_seal_without_writes(self, pin=None):
        before = snapshot(self.root)
        with mock.patch.object(release, "publish_manifest") as publish:
            with self.assertRaises((release.InvalidRelease, OSError, ValueError)):
                release.seal(self.root, self.pin if pin is None else pin)
            publish.assert_not_called()
        self.assertEqual(snapshot(self.root), before)

    def fail_verify_without_writes(self, pin=None):
        before = snapshot(self.root)
        with self.assertRaises((release.InvalidRelease, OSError, ValueError)):
            release.preflight(self.root, self.pin if pin is None else pin, sealed=True)
        self.assertEqual(snapshot(self.root), before)

    def replace_ledger(self, value):
        raw = release.canonical(value)
        (self.root / release.LEDGER).write_bytes(raw)
        return release.sha256(raw)

    def test_inventory_includes_ignored_hidden_and_binary_files(self):
        names = {entry["path"] for entry in self.ledger["files"]}
        self.assertEqual(names, {".gitignore", "cached.pyc", "paper.tex",
                               "papers/build_author/main.aux", "papers/build_author/page.png"})
        before = snapshot(self.root)
        self.assertEqual(release.inventory(self.root), self.raw)
        release.preflight(self.root, self.pin)
        self.assertEqual(snapshot(self.root), before)

    def test_success_manifest_includes_ledger_excludes_itself_and_preserves_payload(self):
        before = snapshot(self.root)
        release.seal(self.root, self.pin)
        release.preflight(self.root, self.pin, sealed=True)
        manifest = (self.root / release.MANIFEST).read_bytes()
        self.assertEqual(manifest, release.expected_manifest(self.ledger, self.pin))
        lines = manifest.decode("ascii").splitlines()
        self.assertEqual(len(lines), self.ledger["payload_count"] + 1)
        self.assertIn(f"{self.pin}  {release.LEDGER}", lines)
        self.assertFalse(any(line.endswith("  " + release.MANIFEST) for line in lines))
        after = snapshot(self.root)
        after.pop(release.MANIFEST)
        self.assertEqual(after, before)
        self.assertEqual(release.inventory(self.root), self.raw)

    def test_same_length_payload_tamper_rejected(self):
        (self.root / "paper.tex").write_bytes(b"modified proof\n")
        self.fail_seal_without_writes()

    def test_recomputed_manifest_cannot_bless_payload_tamper(self):
        release.seal(self.root, self.pin)
        (self.root / "paper.tex").write_bytes(b"modified proof\n")
        changed = json.loads(release.inventory(self.root))
        (self.root / release.MANIFEST).write_bytes(release.expected_manifest(changed, self.pin))
        self.fail_verify_without_writes()

    def test_recomputed_ledger_and_manifest_cannot_bless_payload_with_old_pin(self):
        release.seal(self.root, self.pin)
        (self.root / "paper.tex").write_bytes(b"modified proof\n")
        new_raw = release.inventory(self.root)
        new_pin = release.sha256(new_raw)
        (self.root / release.LEDGER).write_bytes(new_raw)
        (self.root / release.MANIFEST).write_bytes(
            release.expected_manifest(json.loads(new_raw), new_pin))
        self.fail_verify_without_writes()

    def test_recomputed_ledger_cannot_bless_unsealed_tamper_with_old_pin(self):
        (self.root / "paper.tex").write_bytes(b"modified proof\n")
        (self.root / release.LEDGER).write_bytes(release.inventory(self.root))
        self.fail_seal_without_writes()

    def test_missing_and_unexpected_members(self):
        target = self.root / "cached.pyc"
        original = target.read_bytes()
        target.unlink()
        self.fail_seal_without_writes()
        target.write_bytes(original)
        unexpected = self.root / "papers" / "build_author" / "unexpected.log"
        unexpected.write_bytes(b"ignored is still a member\n")
        self.fail_seal_without_writes()

    def test_malformed_json_rejected_even_with_matching_pin(self):
        cases = [b"{", b"\xff", b"[]\n", b"null\n", b"{\"x\":NaN}\n",
                 b'{"schema": "x", "schema": "y"}\n']
        for raw in cases:
            with self.subTest(raw=raw):
                (self.root / release.LEDGER).write_bytes(raw)
                self.fail_seal_without_writes(release.sha256(raw))

    def test_schema_types_totals_order_and_entry_shapes(self):
        mutations = [
            lambda v: v.update(extra="forbidden"),
            lambda v: v.pop("schema"),
            lambda v: v.update(schema="other"),
            lambda v: v.update(files={}),
            lambda v: v.update(payload_count=True),
            lambda v: v.update(payload_count=5.0),
            lambda v: v.update(payload_count=-1),
            lambda v: v.update(payload_count=99),
            lambda v: v.update(payload_bytes=True),
            lambda v: v.update(payload_bytes=-1),
            lambda v: v.update(payload_bytes=999),
            lambda v: v["files"][0].update(bytes=True),
            lambda v: v["files"][0].update(bytes=1.0),
            lambda v: v["files"][0].update(bytes=-1),
            lambda v: v["files"][0].update(sha256="F" * 64),
            lambda v: v["files"][0].update(sha256="0" * 63),
            lambda v: v["files"][0].update(sha256=False),
            lambda v: v["files"][0].update(extra=0),
            lambda v: v["files"][0].pop("bytes"),
            lambda v: v["files"].reverse(),
            lambda v: v["files"].append(copy.deepcopy(v["files"][0])),
            lambda v: v["files"].__setitem__(0, None),
        ]
        for index, mutate in enumerate(mutations):
            with self.subTest(index=index):
                value = copy.deepcopy(self.ledger)
                mutate(value)
                self.fail_seal_without_writes(self.replace_ledger(value))

    def test_unsafe_and_self_referential_ledger_paths(self):
        for path in ["", "/abs", "../up", "a/../up", "a//b", "./a", "a/./b", "a/",
                     "space name", "x\\y", "x\ny", "x\ty", "x\x00y", "é", "C:x",
                     release.LEDGER, release.MANIFEST, True]:
            with self.subTest(path=path):
                value = copy.deepcopy(self.ledger)
                value["files"][0]["path"] = path
                self.fail_seal_without_writes(self.replace_ledger(value))

    def test_noncanonical_ledger_rejected_with_matching_pin(self):
        for raw in [self.raw.rstrip(b"\n"), self.raw + b"\n",
                    json.dumps(self.ledger).encode(), self.raw.replace(b"\n", b"\r\n")]:
            with self.subTest(raw=raw[:30]):
                (self.root / release.LEDGER).write_bytes(raw)
                self.fail_seal_without_writes(release.sha256(raw))

    def test_missing_ledger_and_invalid_pin(self):
        for pin in [None, "", "0" * 64, "F" * 64, "0" * 63, True]:
            with self.subTest(pin=pin):
                selected = "" if pin is None else pin
                self.fail_seal_without_writes(selected)
        (self.root / release.LEDGER).unlink()
        self.fail_seal_without_writes()

    def test_file_directory_dangling_and_metadata_symlinks(self):
        for target in ["paper.tex", "papers", "does-not-exist"]:
            with self.subTest(target=target):
                link = self.root / "alias"
                link.symlink_to(target)
                self.fail_seal_without_writes()
                link.unlink()
        ledger_path = self.root / release.LEDGER
        ledger_path.unlink()
        ledger_path.symlink_to("paper.tex")
        self.fail_seal_without_writes()

    def test_root_and_ancestor_symlinks(self):
        link = Path(self.temporary.name) / "root-link"
        link.symlink_to(self.root, target_is_directory=True)
        before = snapshot(self.root)
        for root in (link, link / "papers"):
            with self.subTest(root=root):
                with self.assertRaises((release.InvalidRelease, OSError)):
                    release.inventory(root)
        self.assertEqual(snapshot(self.root), before)

    def test_fifo_hardlink_empty_directory_and_unsafe_actual_name(self):
        special = self.root / "special"
        os.mkfifo(special)
        self.fail_seal_without_writes()
        special.unlink()
        os.link(self.root / "paper.tex", special)
        self.fail_seal_without_writes()
        special.unlink()
        special.mkdir()
        self.fail_seal_without_writes()
        special.rmdir()
        (self.root / "unsafe name").write_bytes(b"x")
        self.fail_seal_without_writes()

    def test_manifest_corruptions_and_existing_manifest_never_overwritten(self):
        release.seal(self.root, self.pin)
        good = (self.root / release.MANIFEST).read_bytes()
        self.fail_seal_without_writes()
        lines = good.splitlines(keepends=True)
        cases = [b"", good.rstrip(b"\n"), good + lines[0], b"".join(reversed(lines)),
                 b"".join(line for line in lines if not line.endswith(
                     b"  " + release.LEDGER.encode() + b"\n")),
                 good + b"0" * 64 + b"  " + release.MANIFEST.encode() + b"\n",
                 good.replace(b"  paper.tex\n", b"  unexpected.tex\n"),
                 good.replace(b"  ", b" *"), good.replace(b"\n", b"\r\n")]
        for index, raw in enumerate(cases):
            with self.subTest(index=index):
                (self.root / release.MANIFEST).write_bytes(raw)
                self.fail_verify_without_writes()
                self.fail_seal_without_writes()
        (self.root / release.MANIFEST).unlink()
        self.fail_verify_without_writes()

    def test_no_replace_publication_cleans_only_own_temporary(self):
        existing = self.root / release.MANIFEST
        existing.write_bytes(b"keep existing bytes\n")
        before = snapshot(self.root)
        with self.assertRaises(FileExistsError):
            release.publish_manifest(self.root, b"new bytes\n")
        self.assertEqual(snapshot(self.root), before)

    def test_second_preflight_failure_cannot_publish(self):
        real_preflight = release.preflight
        count = 0

        def changing_preflight(*args, **kwargs):
            nonlocal count
            count += 1
            if count == 2:
                raise release.InvalidRelease("injected second-pass change")
            return real_preflight(*args, **kwargs)

        with mock.patch.object(release, "preflight", side_effect=changing_preflight):
            self.fail_seal_without_writes()
        self.assertEqual(count, 2)

    def test_optimized_python_still_rejects_tamper_without_writes(self):
        (self.root / "paper.tex").write_bytes(b"modified proof\n")
        before = snapshot(self.root)
        result = subprocess.run([sys.executable, "-B", "-O", release.__file__, "seal",
                                 str(self.root), "--ledger-sha256", self.pin],
                                capture_output=True, text=True, timeout=10, check=False)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("payload bytes/digest mismatch", result.stderr)
        self.assertEqual(snapshot(self.root), before)

    def test_cli_inventory_and_missing_pin_are_read_only(self):
        before = snapshot(self.root)
        command = [sys.executable, "-B", release.__file__]
        result = subprocess.run(command + ["inventory", str(self.root)], capture_output=True,
                                timeout=10, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, self.raw)
        result = subprocess.run(command + ["seal", str(self.root)], capture_output=True,
                                timeout=10, check=False)
        self.assertEqual(result.returncode, 1)
        self.assertEqual(snapshot(self.root), before)

    def test_cli_check_seal_verify_and_reseal_lifecycle(self):
        command = [sys.executable, "-B", release.__file__]
        for action in ("check", "seal", "verify"):
            with self.subTest(action=action):
                result = subprocess.run(command + [action, str(self.root),
                                        "--ledger-sha256", self.pin],
                                        capture_output=True, text=True, timeout=10,
                                        check=False)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertTrue(result.stdout.startswith(f"PASS {action}: "))
                self.assertEqual(result.stderr, "")
        before = snapshot(self.root)
        result = subprocess.run(command + ["seal", str(self.root),
                                "--ledger-sha256", self.pin],
                                capture_output=True, text=True, timeout=10, check=False)
        self.assertEqual(result.returncode, 1)
        self.assertIn("never overwrites", result.stderr)
        self.assertEqual(snapshot(self.root), before)


if __name__ == "__main__":
    unittest.main(verbosity=2)
