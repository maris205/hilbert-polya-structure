#!/usr/bin/env python3
"""Single reproducible entry point for preregistered SD-C01/02/03 runs.

Run from the Session 4 repository root with:

    python finite_state_arithmetic_skeleton/experiments/run_session4_core.py

The script runs all unit tests first, executes each frozen experiment once,
and writes a deterministic manifest plus JSON/CSV artifacts under the three
candidate result directories.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import subprocess
import sys
from pathlib import Path


SESSION_ID = "SD-S4-2026-08-12"
FROZEN_PRECISION = 80


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run_tests(root: Path) -> list[dict[str, object]]:
    projects = (
        "finite_state_arithmetic_skeleton",
        "squarefree_admissible_shift",
        "renewal_inverse_design_obstruction",
    )
    reports: list[dict[str, object]] = []
    for project in projects:
        code_dir = root / project / "code"
        command = [sys.executable, "-m", "unittest", "discover", "-s", str(code_dir), "-p", "test_*.py"]
        completed = subprocess.run(command, cwd=root, text=True, capture_output=True, check=False)
        reports.append(
            {
                "project": project,
                "command": " ".join(command),
                "returncode": completed.returncode,
                "status": "passed" if completed.returncode == 0 else "failed",
            }
        )
        if completed.returncode != 0:
            raise RuntimeError(f"tests failed for {project}:\n{completed.stdout}\n{completed.stderr}")
    return reports


def import_experiment(root: Path, project: str, module: str):
    code_dir = root / project / "code"
    sys.path.insert(0, str(code_dir))
    try:
        return importlib.import_module(module)
    finally:
        sys.path.pop(0)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skip-tests",
        action="store_true",
        help="Skip the sanity-first unit tests (the default and archived run include them).",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[2]
    test_reports = [] if args.skip_tests else run_tests(root)

    c01 = import_experiment(root, "finite_state_arithmetic_skeleton", "c01_experiment")
    c02 = import_experiment(root, "squarefree_admissible_shift", "c02_experiment")
    c03 = import_experiment(root, "renewal_inverse_design_obstruction", "c03_experiment")

    c01_result = c01.write_results(root / "finite_state_arithmetic_skeleton" / "results", FROZEN_PRECISION)
    c02_result = c02.write_results(root / "squarefree_admissible_shift" / "results")
    c03_result = c03.write_results(root / "renewal_inverse_design_obstruction" / "results", FROZEN_PRECISION)

    expected_artifacts = (
        root / "finite_state_arithmetic_skeleton" / "results" / "sd_c01_results.json",
        root / "finite_state_arithmetic_skeleton" / "results" / "sd_c01_exact_counts.csv",
        root / "squarefree_admissible_shift" / "results" / "sd_c02_results.json",
        root / "squarefree_admissible_shift" / "results" / "sd_c02_periodic_census.csv",
        root / "renewal_inverse_design_obstruction" / "results" / "sd_c03_results.json",
        root / "renewal_inverse_design_obstruction" / "results" / "sd_c03_controls.csv",
    )
    manifest = {
        "schema_version": "1.0.0",
        "session_id": SESSION_ID,
        "run_id": "SD-S4-core-frozen-v1",
        "command": "python finite_state_arithmetic_skeleton/experiments/run_session4_core.py",
        "seed_ledger": {
            "master": 20260812,
            "renewal_on_circle": 20260813,
            "renewal_off_circle": 20260814,
            "unitary_cocycle": 20260815,
            "shuffled_word": 20260816,
        },
        "precision_decimal_digits": FROZEN_PRECISION,
        "cutoffs": {
            "SD-C01_formula_degree": c01.FORMULA_DEGREE_CUTOFF,
            "SD-C01_root_count_T": list(c01.ROOT_COUNT_T_VALUES),
            "SD-C02_exact_period": c02.EXACT_PERIOD_CUTOFF,
            "SD-C02_brute_period": c02.BRUTE_PERIOD_CUTOFF,
            "SD-C02_window": c02.WINDOW_CUTOFF,
            "SD-C03_target_degree": c03.TARGET_DEGREE,
        },
        "sanity_tests": test_reports,
        "status": {
            "SD-C01": bool(c01_result["exact"]["all_computational_identities_pass"]),
            "SD-C02": bool(c02_result["exact"]["periodic_point_theorem"]["all_brute_counts_equal_one"])
            and bool(c02_result["exact"]["finite_modulus_approximants"]["all_brute_validations_pass"]),
            "SD-C03": bool(c03_result["exact"]["all_exact_reconstructions_pass"]),
        },
        "artifact_sha256": {str(path.relative_to(root)): sha256_file(path) for path in expected_artifacts},
        "riemann_zero_data_used": False,
        "route_b_invocation_allowed": False,
    }
    manifest_path = root / "finite_state_arithmetic_skeleton" / "results" / "session4_core_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"manifest": str(manifest_path), "status": manifest["status"]}, indent=2, sort_keys=True))
    return 0 if all(manifest["status"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
