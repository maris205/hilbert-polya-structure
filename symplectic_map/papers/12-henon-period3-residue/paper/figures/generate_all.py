#!/usr/bin/env python3
"""Double-generate Paper 12 figures in isolated trees and freeze outputs."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from figure_data import load_contract, sha256_file


HERE = Path(__file__).resolve().parent
FORMATS = ("pdf", "png", "svg")
FIGURE_SCRIPTS = {
    "fig1_theorem_architecture": "gen_fig1_theorem_architecture.py",
    "fig2_weighted_two_term_law": "gen_fig2_weighted_two_term_law.py",
    "fig3_step9_certificate_pipeline": "gen_fig3_step9_certificate_pipeline.py",
}


def expected_names() -> list[str]:
    return sorted(
        f"{stem}.{extension}"
        for stem in FIGURE_SCRIPTS
        for extension in FORMATS
    )


def environment_for(mpl_config: Path) -> dict[str, str]:
    environment = os.environ.copy()
    environment.update(
        {
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONHASHSEED": "0",
            "SOURCE_DATE_EPOCH": "1471219200",
            "MPLCONFIGDIR": str(mpl_config),
        }
    )
    return environment


def generate_tree(tree: Path) -> dict[str, str]:
    output_dir = tree / "outputs"
    output_dir.mkdir(parents=True)
    mpl_config = tree / "mplconfig"
    mpl_config.mkdir()
    environment = environment_for(mpl_config)
    for script in FIGURE_SCRIPTS.values():
        subprocess.run(
            [
                sys.executable,
                "-B",
                str(HERE / script),
                "--output-dir",
                str(output_dir),
            ],
            cwd=HERE,
            env=environment,
            check=True,
        )
    observed = sorted(path.name for path in output_dir.iterdir() if path.is_file())
    if observed != expected_names():
        raise RuntimeError(
            f"isolated figure inventory mismatch: observed={observed}, expected={expected_names()}"
        )
    return {name: sha256_file(output_dir / name) for name in expected_names()}


def assert_no_bytecode() -> None:
    caches = list(HERE.rglob("__pycache__")) + list(HERE.rglob("*.pyc"))
    if caches:
        relative = [str(path.relative_to(HERE)) for path in caches]
        raise RuntimeError(f"bytecode cache in frozen package: {relative}")


def main() -> None:
    contract = load_contract()
    contract_stems = sorted(item["stem"] for item in contract["figures"])
    if contract_stems != sorted(FIGURE_SCRIPTS):
        raise RuntimeError("generator stems do not match figure contract")
    assert_no_bytecode()

    with tempfile.TemporaryDirectory(prefix="paper12-figures-run1-") as run_one_root:
        with tempfile.TemporaryDirectory(prefix="paper12-figures-run2-") as run_two_root:
            run_one_path = Path(run_one_root)
            run_two_path = Path(run_two_root)
            run_one = generate_tree(run_one_path)
            run_two = generate_tree(run_two_path)
            mismatches = sorted(
                name for name in expected_names() if run_one[name] != run_two[name]
            )
            if mismatches:
                raise RuntimeError(f"isolated-tree byte determinism failed: {mismatches}")
            for name in expected_names():
                shutil.copyfile(run_two_path / "outputs" / name, HERE / name)

    audit = {
        "byte_identical_outputs": True,
        "generated_utc": "2026-08-16T00:00:00Z",
        "isolated_generation_trees": 2,
        "mismatches": [],
        "outputs": [
            {
                "match": run_one[name] == run_two[name],
                "path": name,
                "sha256_run_one": run_one[name],
                "sha256_run_two": run_two[name],
            }
            for name in expected_names()
        ],
        "pass": True,
        "python_hash_seed": "0",
        "registered_or_scientific_runtime_used": False,
        "regeneration_count": 2,
        "schema": "paper12.figure_determinism.v1",
        "source_date_epoch": "1471219200",
    }
    (HERE / "DETERMINISM_AUDIT.json").write_text(
        json.dumps(audit, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    assert_no_bytecode()
    print("Paper 12 proof-only figure generation: PASS")
    print("isolated trees: 2")
    print("byte-identical outputs: 9")
    for name, digest in sorted(run_two.items()):
        print(f"{digest}  {name}")


if __name__ == "__main__":
    main()
