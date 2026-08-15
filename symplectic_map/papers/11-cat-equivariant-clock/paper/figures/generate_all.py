#!/usr/bin/env python3
"""Generate, double-run, and mechanically verify all Paper 11 figures."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from build_asset_tree import write_asset_tree
from build_figure_manifest import FIGURES, FORMATS, write_manifest
from figure_data import load_frozen_payload, sha256_file


HERE = Path(__file__).resolve().parent


def expected_output_names() -> set[str]:
    return {
        f"{stem}.{extension}"
        for stem in FIGURES
        for extension in FORMATS
    }


def assert_exact_output_inventory() -> None:
    observed = {
        path.name
        for extension in FORMATS
        for path in HERE.glob(f"fig[0-9]*.{extension}")
        if path.is_file()
    }
    expected = expected_output_names()
    if observed != expected:
        raise RuntimeError(
            f"figure inventory is not exactly three stems/nine files: "
            f"missing={sorted(expected - observed)}, unexpected={sorted(observed - expected)}"
        )


def output_hashes() -> dict[str, str]:
    return {
        name: sha256_file(HERE / name)
        for name in sorted(expected_output_names())
    }


def generation_environment() -> dict[str, str]:
    environment = os.environ.copy()
    environment.update(
        {
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONHASHSEED": "0",
            "SOURCE_DATE_EPOCH": "1471132800",
            "MPLCONFIGDIR": "/tmp/paper11_figures_mplconfig",
        }
    )
    return environment


def generate_once() -> dict[str, str]:
    environment = generation_environment()
    for script in FIGURES.values():
        subprocess.run(
            [sys.executable, "-B", str(HERE / script), "--output-dir", str(HERE)],
            cwd=HERE,
            env=environment,
            check=True,
        )
    assert_exact_output_inventory()
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
    load_frozen_payload()
    assert_no_bytecode_cache()
    run_one = generate_once()
    run_two = generate_once()
    mismatches = sorted(name for name in run_one if run_one[name] != run_two[name])
    audit = {
        "schema": "paper11.figure_determinism.v1",
        "generated_utc": "2026-08-15T00:00:00Z",
        "pass": not mismatches,
        "regeneration_count": 2,
        "byte_identical_outputs": not mismatches,
        "mismatches": mismatches,
        "outputs": [
            {
                "path": name,
                "sha256_run_one": run_one[name],
                "sha256_run_two": run_two[name],
                "match": run_one[name] == run_two[name],
            }
            for name in sorted(run_one)
        ],
    }
    (HERE / "DETERMINISM_AUDIT.json").write_text(
        json.dumps(audit, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    if mismatches:
        raise RuntimeError(f"two-run byte determinism failed: {mismatches}")
    write_asset_tree(HERE / "ASSET_TREE.json")
    manifest = write_manifest(run_one, run_two, HERE / "FIGURE_MANIFEST.json")
    assert_no_bytecode_cache()
    print("Paper 11 figure package: PASS")
    print("two-run byte-identical outputs: 9")
    for name, digest in sorted(run_two.items()):
        print(f"{digest}  {name}")
    print(f"manifest status: {manifest['status']}")


if __name__ == "__main__":
    main()
