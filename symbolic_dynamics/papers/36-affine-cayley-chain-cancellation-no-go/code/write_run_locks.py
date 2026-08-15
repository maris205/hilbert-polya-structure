#!/usr/bin/env python3
"""Write deterministic execution, dependency, and parameter locks for SD-C38."""

from __future__ import annotations

import argparse
import importlib.metadata
import json
from pathlib import Path
import platform


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-dir", required=True)
    arguments = parser.parse_args()
    result_dir = Path(arguments.result_dir)
    result_dir.mkdir(parents=True, exist_ok=True)

    environment = {
        "schema": "SD-C38-environment-lock-v1",
        "candidate_id": "SD-C38",
        "python": platform.python_version(),
        "implementation": platform.python_implementation(),
        "platform_family": platform.system(),
        "cpu_only": True,
        "network_used": False,
        "external_data_used": False,
        "result_timestamps": False,
        "pythonhashseed": "0",
        "pythondontwritebytecode": "1",
    }
    dependencies = {
        "schema": "SD-C38-dependency-lock-v1",
        "scientific_dependencies": [],
        "scientific_runtime": "Python standard library only",
        "seal_audit_dependencies": {
            "PyYAML": importlib.metadata.version("PyYAML"),
        },
        "dependency_roles": {
            "PyYAML": "strict Route-A YAML parsing and integrity audit only",
        },
    }
    parameters = {
        "schema": "SD-C38-run-parameters-v1",
        "candidate_id": "SD-C38",
        "main_r": [2, 3, 4, 5],
        "baseline_r": 4,
        "balanced_r": 1,
        "max_word_length": 12,
        "alphabet": ["u", "U", "v", "V"],
        "damping_theta": "1/2",
        "finite_cases": [
            [1, 4, 3],
            [2, 3, 2],
            [3, 4, 2],
            [4, 5, 2],
            [4, 7, 3],
            [5, 6, 2],
        ],
        "target_zero_data": "none",
        "route_b_invocation_allowed": False,
        "pipeline": [
            "source_generator.py",
            "audit_source_separation.py",
            "evaluate_results.py",
            "run_tests.py",
            "analyze_results.py",
        ],
    }
    write_json(result_dir / "environment_lock.json", environment)
    write_json(result_dir / "dependency_lock.json", dependencies)
    write_json(result_dir / "run_parameters.json", parameters)
    print(
        json.dumps(
            {
                "candidate_id": "SD-C38",
                "locks": 3,
                "scientific_dependencies": 0,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
