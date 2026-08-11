#!/usr/bin/env python3
"""Run every mirrored project regression in parallel and report one summary."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
from pathlib import Path
import re
import subprocess
import sys

import yaml


STREAM_ROOT = Path(__file__).resolve().parents[1]
PROJECTS_ROOT = STREAM_ROOT / "projects"
MIRROR_ROOT = STREAM_ROOT.parent
DEFAULT_SOURCE_ROOT = MIRROR_ROOT.parent / "find_dyna"
MANIFEST = STREAM_ROOT / "sync_manifest.yaml"


def as_list(value: object) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list) and all(isinstance(item, str) for item in value):
        return value
    raise TypeError(f"expected a path string or list, got {value!r}")


def load_manifest() -> dict[str, object]:
    return yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))


def stages_by_project(manifest: dict[str, object]) -> dict[str, dict[str, object]]:
    return {
        Path(stage["project"]).name: stage
        for stage in manifest["stages"]
    }


def run_project(
    project: Path,
    stage: dict[str, object],
    source_root: Path,
) -> tuple[str, int, int, str, str]:
    tests = project / "tests"
    if not tests.is_dir() or not any(tests.glob("test_*.py")):
        return project.name, 0, 0, "SKIP no tests", "mirror_portable"
    environment = os.environ.copy()
    environment["PYTHONPATH"] = "."
    mode = str(stage.get("reproduction_mode", "mirror_portable"))
    if mode == "source_bound":
        command = [
            sys.executable,
            "-m",
            "unittest",
            *as_list(stage.get("tests")),
        ]
        cwd = source_root
    elif mode == "mirror_portable":
        command = [
            sys.executable,
            "-m",
            "unittest",
            "discover",
            "-s",
            "tests",
            "-p",
            "test_*.py",
        ]
        cwd = project
    else:
        return project.name, 2, 0, f"unknown reproduction mode: {mode}", mode
    completed = subprocess.run(
        command,
        cwd=cwd,
        env=environment,
        check=False,
        capture_output=True,
        text=True,
    )
    transcript = completed.stdout + completed.stderr
    match = re.search(r"Ran (\d+) tests?", transcript)
    count = int(match.group(1)) if match else 0
    tail = "\n".join(transcript.strip().splitlines()[-12:])
    return project.name, completed.returncode, count, tail, mode


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs", type=int, default=min(8, os.cpu_count() or 1))
    parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE_ROOT)
    parser.add_argument("--project", action="append", default=[])
    args = parser.parse_args()
    manifest = load_manifest()
    stages = stages_by_project(manifest)
    requested = set(args.project)
    unknown = requested - set(stages)
    if unknown:
        parser.error(f"unknown project(s): {', '.join(sorted(unknown))}")
    projects = sorted(
        path
        for path in PROJECTS_ROOT.iterdir()
        if path.is_dir() and (not requested or path.name in requested)
    )
    source_root = args.source_root.resolve()
    if any(
        stages[project.name].get("reproduction_mode") == "source_bound"
        for project in projects
    ):
        actual_source_commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=source_root, text=True
        ).strip()
        if actual_source_commit != manifest["source_commit"]:
            parser.error(
                "source HEAD mismatch: "
                f"manifest={manifest['source_commit']} actual={actual_source_commit}"
            )
    failures: list[tuple[str, str]] = []
    total_tests = 0
    skipped = 0
    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as executor:
        futures = {
            executor.submit(run_project, project, stages[project.name], source_root): project
            for project in projects
        }
        for future in as_completed(futures):
            name, returncode, count, tail, mode = future.result()
            if tail.startswith("SKIP"):
                skipped += 1
                print(f"SKIP {name}")
            elif returncode == 0:
                total_tests += count
                label = "SOURCE-PASS" if mode == "source_bound" else "PASS"
                print(f"{label} {name}: {count} tests")
            else:
                failures.append((name, tail))
                print(f"FAIL {name}")
    if failures:
        print("\nFailure transcripts:")
        for name, tail in failures:
            print(f"\n--- {name} ---\n{tail}")
        return 1
    print(
        f"all mirrored project regressions passed: {total_tests} tests, "
        f"{skipped} project(s) without standalone tests"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
