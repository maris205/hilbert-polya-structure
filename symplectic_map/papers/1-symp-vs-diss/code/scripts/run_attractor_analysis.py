#!/usr/bin/env python3
"""Run the post-validation, nonconfirmatory attractor diagnostics."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
from typing import Any

import numpy as np


CODE_ROOT = Path(__file__).resolve().parents[1]
PAPER_ROOT = CODE_ROOT.parent
if str(CODE_ROOT) not in sys.path:
    sys.path.insert(0, str(CODE_ROOT))

from symplectic_henon.attractors import (  # noqa: E402
    DIAGNOSTIC_SEED,
    EXPLORATORY_RHO_GRID,
    generate_diagnostic_parent_ensemble,
    positive_fixed_point_flip_threshold,
    positive_fixed_point_jury_margins,
    positive_fixed_point_multipliers,
    simulate_and_classify_attractors,
    summarize_attractor_run,
)
from symplectic_henon.symbolic import FROZEN_A  # noqa: E402


DEFAULT_A_VALUES = (FROZEN_A, 1.50, 1.52, 1.56, 1.58)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Classify dissipative attractor periods on a separate, "
            "post-validation diagnostic ensemble."
        )
    )
    parser.add_argument("--a-values", type=float, nargs="+", default=list(DEFAULT_A_VALUES))
    parser.add_argument("--rhos", type=float, nargs="+", default=list(EXPLORATORY_RHO_GRID))
    parser.add_argument("--seed", type=int, default=DIAGNOSTIC_SEED)
    parser.add_argument("--n-trajectories", type=int, default=256)
    parser.add_argument("--parent-burn-in", type=int, default=4096)
    parser.add_argument("--attractor-burn-in", type=int, default=16_384)
    parser.add_argument("--tail-length", type=int, default=2048)
    parser.add_argument("--escape-bound", type=float, default=100.0)
    parser.add_argument("--max-period", type=int, default=32)
    parser.add_argument("--absolute-tolerance", type=float, default=1e-9)
    parser.add_argument("--relative-tolerance", type=float, default=1e-9)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PAPER_ROOT / "results" / "attractors",
    )
    parser.add_argument("--run-label", default="attractor_diagnostics_v1")
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def validate_arguments(arguments: argparse.Namespace) -> None:
    if not arguments.a_values or any(
        not math.isfinite(a) or a <= 0.0 for a in arguments.a_values
    ):
        raise ValueError("all --a-values must be finite and positive")
    if not arguments.rhos or any(
        not math.isfinite(rho) or rho < 0.0 for rho in arguments.rhos
    ):
        raise ValueError("all --rhos must be finite and nonnegative")
    if len(set(arguments.a_values)) != len(arguments.a_values):
        raise ValueError("a values must be unique")
    if len(set(arguments.rhos)) != len(arguments.rhos):
        raise ValueError("rho values must be unique")
    if arguments.n_trajectories <= 0:
        raise ValueError("--n-trajectories must be positive")
    if arguments.parent_burn_in < 1 or arguments.attractor_burn_in < 0:
        raise ValueError("burn-in lengths are invalid")
    if arguments.tail_length <= arguments.max_period:
        raise ValueError("--tail-length must exceed --max-period")
    if arguments.max_period <= 0:
        raise ValueError("--max-period must be positive")
    if arguments.escape_bound <= 0.0 or not math.isfinite(arguments.escape_bound):
        raise ValueError("--escape-bound must be finite and positive")
    if arguments.absolute_tolerance < 0.0 or arguments.relative_tolerance < 0.0:
        raise ValueError("recurrence tolerances must be nonnegative")
    if not arguments.run_label or Path(arguments.run_label).name != arguments.run_label:
        raise ValueError("--run-label must be a nonempty filename stem")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _json_safe(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): _json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_safe(item) for item in value]
    if isinstance(value, np.ndarray):
        return _json_safe(value.tolist())
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating, float)):
        number = float(value)
        return number if math.isfinite(number) else None
    return value


def main() -> int:
    arguments = parse_arguments()
    validate_arguments(arguments)

    output_dir = arguments.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / f"{arguments.run_label}.json"
    summary_path = output_dir / f"{arguments.run_label}_summary.csv"
    trajectory_path = output_dir / f"{arguments.run_label}_trajectories.csv"
    targets = (json_path, summary_path, trajectory_path)
    if not arguments.overwrite and any(path.exists() for path in targets):
        existing = ", ".join(str(path) for path in targets if path.exists())
        raise FileExistsError(f"refusing to overwrite existing outputs: {existing}")

    runs = []
    summaries: list[dict[str, object]] = []
    for a in arguments.a_values:
        initial_states = generate_diagnostic_parent_ensemble(
            a=a,
            n_trajectories=arguments.n_trajectories,
            parent_burn_in=arguments.parent_burn_in,
            seed=arguments.seed,
        )
        for rho in arguments.rhos:
            run = simulate_and_classify_attractors(
                initial_states,
                a=a,
                rho=rho,
                burn_in=arguments.attractor_burn_in,
                tail_length=arguments.tail_length,
                escape_bound=arguments.escape_bound,
                max_period=arguments.max_period,
                absolute_tolerance=arguments.absolute_tolerance,
                relative_tolerance=arguments.relative_tolerance,
            )
            runs.append(run)
            summaries.append(summarize_attractor_run(run))

    summary_fieldnames = list(summaries[0])
    with summary_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=summary_fieldnames)
        writer.writeheader()
        writer.writerows(summaries)

    trajectory_fieldnames = [
        "a",
        "rho",
        "trajectory_id",
        "label",
        "period",
        "recurrence_residual",
        "escape_step",
        "final_x",
        "final_y",
    ]
    with trajectory_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=trajectory_fieldnames)
        writer.writeheader()
        for run in runs:
            for trajectory_id in range(run.n_trajectories):
                writer.writerow(
                    {
                        "a": run.a,
                        "rho": run.rho,
                        "trajectory_id": trajectory_id,
                        "label": str(run.labels[trajectory_id]),
                        "period": int(run.periods[trajectory_id]),
                        "recurrence_residual": _json_safe(
                            run.recurrence_residuals[trajectory_id]
                        ),
                        "escape_step": int(run.escape_steps[trajectory_id]),
                        "final_x": _json_safe(run.final_states[trajectory_id, 0]),
                        "final_y": _json_safe(run.final_states[trajectory_id, 1]),
                    }
                )

    theory = []
    for a in arguments.a_values:
        threshold = positive_fixed_point_flip_threshold(a)
        endpoint_multipliers = positive_fixed_point_multipliers(a, 1.0)
        theory.append(
            {
                "a": a,
                "rho_flip": threshold,
                "threshold_in_open_dissipative_interval": 0.0 < threshold < 1.0,
                "jury_margins_just_below": positive_fixed_point_jury_margins(
                    a, max(0.0, threshold - 1e-6)
                ),
                "jury_margins_just_above": positive_fixed_point_jury_margins(
                    a, min(1.0, threshold + 1e-6)
                ),
                "rho1_multipliers": [
                    {"real": float(value.real), "imag": float(value.imag)}
                    for value in endpoint_multipliers
                ],
            }
        )

    module_path = CODE_ROOT / "symplectic_henon" / "attractors.py"
    script_path = Path(__file__).resolve()
    payload = {
        "analysis_status": "secondary_post_validation_nonconfirmatory",
        "scope": (
            "Mechanistic attractor-period diagnosis only; no primes, zeros, "
            "or confirmatory test-split access."
        ),
        "protocol": {
            "map": "H_{a,rho}(x,y)=(1-a*x^2-rho*y,x)",
            "a_values": arguments.a_values,
            "rhos": arguments.rhos,
            "seed": arguments.seed,
            "n_trajectories": arguments.n_trajectories,
            "parent_burn_in": arguments.parent_burn_in,
            "attractor_burn_in": arguments.attractor_burn_in,
            "tail_length": arguments.tail_length,
            "escape_bound": arguments.escape_bound,
            "max_period": arguments.max_period,
            "absolute_tolerance": arguments.absolute_tolerance,
            "relative_tolerance": arguments.relative_tolerance,
            "initialization": (
                "Separate PCG64 diagnostic draw, burned under the rho=0 "
                "parent map; it is not a primary split."
            ),
        },
        "theory": theory,
        "summaries": summaries,
        "source_hashes_sha256": {
            str(module_path.relative_to(PAPER_ROOT)): _sha256(module_path),
            str(script_path.relative_to(PAPER_ROOT)): _sha256(script_path),
        },
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "platform": platform.platform(),
        },
        "files": {
            "summary_csv": summary_path.name,
            "trajectory_csv": trajectory_path.name,
        },
    }
    json_path.write_text(
        json.dumps(_json_safe(payload), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json_path)
    print(summary_path)
    print(trajectory_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
