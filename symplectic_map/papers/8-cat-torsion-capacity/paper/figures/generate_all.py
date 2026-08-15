#!/usr/bin/env python3
"""Generate and verify all three manifest-bound Paper 8 figures twice."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from build_figure_manifest import FIGURES, FORMATS, write_manifest
from figure_data import sha256_file, validate_source_hashes


HERE = Path(__file__).resolve().parent


def output_hashes() -> dict[str, str]:
    return {
        f"{stem}.{extension}": sha256_file(HERE / f"{stem}.{extension}")
        for stem in FIGURES
        for extension in FORMATS
    }


def generate_once() -> dict[str, str]:
    environment = os.environ.copy()
    environment.update(
        {
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONHASHSEED": "0",
            "SOURCE_DATE_EPOCH": "1471132800",
            "MPLCONFIGDIR": "/tmp/paper8_figures_mplconfig",
        }
    )
    for script in FIGURES.values():
        subprocess.run(
            [sys.executable, "-B", str(HERE / script), "--output-dir", str(HERE)],
            cwd=HERE,
            env=environment,
            check=True,
        )
    hashes = output_hashes()
    if len(hashes) != 9:
        raise RuntimeError("expected exactly nine figure-format outputs")
    return hashes


def assert_no_bytecode_cache() -> None:
    caches = list(HERE.rglob("__pycache__")) + list(HERE.rglob("*.pyc"))
    if caches:
        names = [str(path.relative_to(HERE)) for path in caches]
        raise RuntimeError(f"bytecode cache present in figure package: {names}")


def main() -> None:
    validate_source_hashes()
    assert_no_bytecode_cache()
    run_one = generate_once()
    run_two = generate_once()
    if run_one != run_two:
        differing = sorted(key for key in run_one if run_one[key] != run_two[key])
        raise RuntimeError(f"two-run byte determinism failed: {differing}")
    manifest = write_manifest(run_one, run_two, HERE / "FIGURE_MANIFEST.json")
    assert_no_bytecode_cache()
    print("Paper 8 figure package: PASS")
    print(f"two-run byte-identical outputs: {len(run_two)}")
    for name, digest in sorted(run_two.items()):
        print(f"{digest}  {name}")
    print(f"manifest status: {manifest['status']}")


if __name__ == "__main__":
    main()
