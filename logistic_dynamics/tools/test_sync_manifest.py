from __future__ import annotations

import subprocess
import sys
from pathlib import Path
import unittest

import yaml


STREAM_ROOT = Path(__file__).resolve().parents[1]
MIRROR_ROOT = STREAM_ROOT.parent
SOURCE_ROOT = MIRROR_ROOT.parent / "find_dyna"
MANIFEST = STREAM_ROOT / "sync_manifest.yaml"
SYNC = STREAM_ROOT / "tools" / "sync_from_riemann_dyna.py"


class SyncManifestTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.manifest = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))

    def test_unique_stage_and_project_ids(self) -> None:
        stages = self.manifest["stages"]
        stage_ids = [stage["stage_id"] for stage in stages]
        projects = [stage["project"] for stage in stages]
        self.assertEqual(len(stage_ids), len(set(stage_ids)))
        self.assertEqual(len(projects), len(set(projects)))
        self.assertEqual(len(stages), 31)

    def test_reproduction_modes_and_source_bound_inputs(self) -> None:
        allowed = {"mirror_portable", "source_bound"}
        for stage in self.manifest["stages"]:
            mode = stage.get("reproduction_mode", "mirror_portable")
            self.assertIn(mode, allowed, stage["stage_id"])
            if mode == "source_bound":
                tests = stage.get("tests", [])
                if isinstance(tests, str):
                    tests = [tests]
                self.assertTrue(tests, stage["stage_id"])
                for relative in tests:
                    self.assertTrue((SOURCE_ROOT / relative).is_file(), relative)

    def test_no_follow_ledgers_do_not_vendor_unrelated_stages(self) -> None:
        unrelated = "formal/obstructions/th_0001_single_phase_caustic.md"
        for stage in self.manifest["stages"]:
            passive = stage.get("no_follow_files", [])
            if isinstance(passive, str):
                passive = [passive]
            if not passive:
                continue
            provenance = yaml.safe_load(
                (STREAM_ROOT / stage["project"] / "SOURCE_PROVENANCE.yaml").read_text(
                    encoding="utf-8"
                )
            )
            mirrored = {item["path"] for item in provenance["source_files"]}
            self.assertTrue(set(passive).issubset(mirrored), stage["stage_id"])
            self.assertNotIn(unrelated, mirrored, stage["stage_id"])

    def test_source_commit_is_bound(self) -> None:
        head = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=SOURCE_ROOT, text=True
        ).strip()
        self.assertEqual(head, self.manifest["source_commit"])

    def test_every_project_has_canonical_records(self) -> None:
        for stage in self.manifest["stages"]:
            project = STREAM_ROOT / stage["project"]
            self.assertTrue((project / "README.md").is_file(), stage["stage_id"])
            self.assertTrue(
                (project / "SOURCE_PROVENANCE.yaml").is_file(), stage["stage_id"]
            )
            self.assertTrue(
                (project / "results" / "SOURCE_HASHES.sha256").is_file(),
                stage["stage_id"],
            )
            if stage.get("source_locks"):
                self.assertTrue((project / "source_lock.yaml").is_file())
            if stage.get("evaluations"):
                self.assertTrue((project / "route_a_evaluation.yaml").is_file())

    def test_all_mirrored_yaml_parses(self) -> None:
        paths = [MANIFEST]
        paths.extend(STREAM_ROOT.glob("projects/*/source_lock.yaml"))
        paths.extend(STREAM_ROOT.glob("projects/*/route_a_evaluation.yaml"))
        paths.extend(STREAM_ROOT.glob("projects/*/SOURCE_PROVENANCE.yaml"))
        for path in paths:
            with self.subTest(path=path):
                yaml.safe_load(path.read_text(encoding="utf-8"))

    def test_generated_index_links_resolve(self) -> None:
        for stage in self.manifest["stages"]:
            target = STREAM_ROOT / stage["project"] / "README.md"
            self.assertTrue(target.is_file(), target)

    def test_byte_for_byte_sync_check(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(SYNC), "--check"],
            cwd=MIRROR_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)


if __name__ == "__main__":
    unittest.main()
