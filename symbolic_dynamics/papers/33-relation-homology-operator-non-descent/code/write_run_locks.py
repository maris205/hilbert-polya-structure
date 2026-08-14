#!/usr/bin/env python3
"""Write deterministic Paper 33 run and research bridge locks."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


RESEARCH_HASHES = {
    "research_package_sha256": (
        "15c414149e4e06953be394f7175e98d504a688769bbad168365b86c853b8533f"
    ),
    "source_lock_sha256": (
        "d3653a9c8a663b5e9a89964f5e8ea2528e28f12384162963bc312c00e7173649"
    ),
    "derivation_package_sha256": (
        "38c426c80fae8764e0ece18eb36864acb31868388f36e3ac65f82673b3add2ce"
    ),
    "proof_package_sha256": (
        "610ca712bc011bad6cfac10f3ff05e0fbe256044c0a8f27adf8873b3dbf0ca8b"
    ),
    "literature_audit_sha256": (
        "382e1b44f51ef18868746855422541676aeb3a0512c2973754c1d18076218c27"
    ),
    "route_a_research_yaml_sha256": (
        "5f8c62144e3df01f0a0eabf1b46e229e31ea31e2a040563227e9dc6a5d1c90fd"
    ),
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, payload: object) -> None:
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-dir", default="results")
    args = parser.parse_args()

    result_dir = Path(args.result_dir)
    result_dir.mkdir(parents=True, exist_ok=True)
    root = Path(__file__).resolve().parents[1]
    plan = root / "experiments" / "EXPERIMENT_PLAN.md"
    code_dir = root / "code"

    environment = {
        "candidate_id": "SD-C35",
        "date_utc": "2026-08-15",
        "python": "python3",
        "platform": "linux",
        "execution": "exact CPU integer/finite-field audit; no GPU required",
        "line_endings": "LF",
        "python_cache_policy": "PYTHONDONTWRITEBYTECODE=1",
        "target_zero_data_used": False,
    }
    parameters = {
        "candidate_id": "SD-C35",
        "cutoff": 192,
        "coefficient_field_audit": "F_1000003",
        "matched_relabel_seed": "1003003+n",
        "random_seed_start": 330000,
        "random_trials": 64,
        "cross_multipliers": [2, 3],
        "target_zero_data": "none",
        "route_b_invocation_allowed": False,
        "pipeline": [
            "source_generator.py",
            "audit_source_separation.py",
            "post_census_classifier.py",
            "independent_evaluator.py",
            "run_tests.py",
        ],
    }
    research = {
        "candidate_id": "SD-C35",
        **RESEARCH_HASHES,
        "prototype_core_sha256": digest(
            code_dir / "cycle_quotient_core.py"
        ),
        "prototype_runner_sha256": digest(
            code_dir / "generate_results.py"
        ),
        "canonical_experiment_plan_sha256": digest(plan),
        "canonical_experiment_plan_precedes_outputs": True,
    }
    write_json(result_dir / "environment_lock.json", environment)
    write_json(result_dir / "run_parameters.json", parameters)
    write_json(result_dir / "research_lock.json", research)
    print(json.dumps({
        "candidate_id": "SD-C35",
        "locks": 3,
        "plan_sha256": research["canonical_experiment_plan_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
