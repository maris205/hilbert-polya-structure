"""Regenerate every figure once and verify byte-identical outputs."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from figure_contract import sha256_file


FIG_DIR = Path(__file__).resolve().parent
SCRIPTS = [
    "gen_fig1_boundary_map.py",
    "gen_fig2_registered_ledger.py",
    "gen_fig3_frobenius_filter.py",
]
STEMS = [
    "fig1_boundary_map",
    "fig2_registered_ledger",
    "fig3_frobenius_filter",
]
OUTPUTS = [f"{stem}.{suffix}" for stem in STEMS for suffix in ("pdf", "svg", "png")]


def hashes() -> dict[str, str]:
    missing = [name for name in OUTPUTS if not (FIG_DIR / name).is_file()]
    if missing:
        raise RuntimeError(f"missing figure outputs before determinism audit: {missing}")
    return {name: sha256_file(FIG_DIR / name) for name in OUTPUTS}


def main() -> None:
    before = hashes()
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTHONHASHSEED"] = "0"
    for script in SCRIPTS:
        subprocess.run(
            [sys.executable, "-B", str(FIG_DIR / script)],
            cwd=FIG_DIR,
            env=env,
            check=True,
        )
    after = hashes()
    mismatches = [name for name in OUTPUTS if before[name] != after[name]]
    report = {
        "schema": "BASE2_FIGURE_DETERMINISM_V1",
        "pass": not mismatches,
        "regeneration_count": 2,
        "byte_identical_outputs": not mismatches,
        "mismatches": mismatches,
        "outputs": [
            {
                "path": name,
                "sha256_before": before[name],
                "sha256_after": after[name],
                "match": before[name] == after[name],
            }
            for name in OUTPUTS
        ],
    }
    (FIG_DIR / "DETERMINISM_AUDIT.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if mismatches:
        raise SystemExit(f"nondeterministic figure outputs: {mismatches}")


if __name__ == "__main__":
    main()

