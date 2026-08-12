#!/usr/bin/env python3
"""Run the preregistered frozen-seed symbolic transport experiment.

Examples
--------
Development smoke run (safe default)::

    python code/scripts/run_transport.py --split dev

The confirmatory split cannot be read without both selecting it and supplying
the explicit unlock flag::

    python code/scripts/run_transport.py \
        --split test --unlock-confirmatory-test
"""

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

from symplectic_henon.symbolic import (  # noqa: E402
    CONFIRMATORY_EXPOSURE_GATE,
    CONFIRMATORY_MIN_GAPS,
    CONFIRMATORY_POLARITY_LOWER_BOUND,
    CONFIRMATORY_RHO,
    FROZEN_A,
    RHO_GRID,
    SPLIT_SEEDS,
    cluster_bootstrap,
    evaluate_confirmatory_endpoint,
    generate_parent_ensemble,
    simulate_transport,
    summarize_result,
)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Measure transport of the frozen parent-map L-return parity "
            "shadow through H_{a,rho}."
        )
    )
    parser.add_argument(
        "--split",
        choices=tuple(SPLIT_SEEDS),
        default="dev",
        help="frozen initial-condition split (default: dev)",
    )
    parser.add_argument(
        "--unlock-confirmatory-test",
        action="store_true",
        help=(
            "explicitly unlock the test split; has no effect on other splits"
        ),
    )
    parser.add_argument("--a", type=float, default=FROZEN_A)
    parser.add_argument(
        "--rhos",
        type=float,
        nargs="+",
        default=list(RHO_GRID),
        help="rho values; default includes singular reference 0 and endpoint 1",
    )
    parser.add_argument("--n-trajectories", type=int, default=2048)
    parser.add_argument("--burn-in", type=int, default=4096)
    parser.add_argument("--horizon", type=int, default=1024)
    parser.add_argument("--escape-bound", type=float, default=100.0)
    parser.add_argument("--bootstrap-replicates", type=int, default=2000)
    parser.add_argument("--ci-level", type=float, default=0.95)
    parser.add_argument(
        "--exposure-gate",
        type=float,
        default=CONFIRMATORY_EXPOSURE_GATE,
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PAPER_ROOT / "results" / "transport",
    )
    parser.add_argument(
        "--run-label",
        default=None,
        help="output stem (default: transport_<split>)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="replace output files with the same run label",
    )
    return parser.parse_args()


def validate_arguments(arguments: argparse.Namespace) -> None:
    if arguments.split == "test" and not arguments.unlock_confirmatory_test:
        raise PermissionError(
            "refusing to read the confirmatory test split without "
            "--unlock-confirmatory-test"
        )
    if arguments.n_trajectories <= 0:
        raise ValueError("--n-trajectories must be positive")
    if arguments.burn_in < 1:
        raise ValueError("--burn-in must be at least one")
    if arguments.horizon <= 0:
        raise ValueError("--horizon must be positive")
    if arguments.bootstrap_replicates <= 0:
        raise ValueError("--bootstrap-replicates must be positive")
    if not 0.0 < arguments.ci_level < 1.0:
        raise ValueError("--ci-level must lie strictly between zero and one")
    if not 0.0 <= arguments.exposure_gate <= 1.0:
        raise ValueError("--exposure-gate must lie between zero and one")
    if not arguments.rhos:
        raise ValueError("at least one --rhos value is required")
    if any((not math.isfinite(rho) or rho < 0) for rho in arguments.rhos):
        raise ValueError("all rho values must be finite and nonnegative")
    if len(set(arguments.rhos)) != len(arguments.rhos):
        raise ValueError("rho values must be unique")


def json_safe(value: Any) -> Any:
    """Recursively replace non-finite floats with JSON ``null``."""

    if isinstance(value, dict):
        return {str(key): json_safe(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating, float)):
        number = float(value)
        return number if math.isfinite(number) else None
    if isinstance(value, np.ndarray):
        return json_safe(value.tolist())
    return value


def write_summary_csv(path: Path, summaries: list[dict[str, Any]]) -> None:
    excluded = {"gap_histogram"}
    fieldnames = [key for key in summaries[0] if key not in excluded]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for summary in summaries:
            writer.writerow(
                {
                    key: json_safe(value)
                    for key, value in summary.items()
                    if key not in excluded
                }
            )


def write_cluster_csv(
    path: Path,
    *,
    rhos_and_results: list[tuple[float, Any]],
) -> None:
    fieldnames = [
        "rho",
        "trajectory_id",
        "exposure_steps",
        "survived",
        "escape_time",
        "left_visits",
        "even_gaps",
        "odd_gaps",
        "trans_RR",
        "trans_RL",
        "trans_LR",
        "trans_LL",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for rho, result in rhos_and_results:
            clusters = result.clusters
            for trajectory_id in range(clusters.n_trajectories):
                transition = clusters.transitions[trajectory_id]
                writer.writerow(
                    {
                        "rho": rho,
                        "trajectory_id": trajectory_id,
                        "exposure_steps": int(
                            clusters.exposure_steps[trajectory_id]
                        ),
                        "survived": int(clusters.survived[trajectory_id]),
                        "escape_time": int(result.escape_times[trajectory_id]),
                        "left_visits": int(clusters.left_visits[trajectory_id]),
                        "even_gaps": int(clusters.even_gaps[trajectory_id]),
                        "odd_gaps": int(clusters.odd_gaps[trajectory_id]),
                        "trans_RR": int(transition[0, 0]),
                        "trans_RL": int(transition[0, 1]),
                        "trans_LR": int(transition[1, 0]),
                        "trans_LL": int(transition[1, 1]),
                    }
                )


def output_paths(arguments: argparse.Namespace) -> tuple[Path, Path, Path]:
    stem = arguments.run_label or f"transport_{arguments.split}"
    if not stem or Path(stem).name != stem:
        raise ValueError("--run-label must be a nonempty filename stem")
    output_dir = arguments.output_dir.resolve()
    return (
        output_dir / f"{stem}.json",
        output_dir / f"{stem}_summary.csv",
        output_dir / f"{stem}_clusters.csv",
    )


def protocol_deviations(arguments: argparse.Namespace) -> list[str]:
    """List changes from the frozen confirmatory trajectory protocol."""

    expected = {
        "a": FROZEN_A,
        "rhos": list(RHO_GRID),
        "n_trajectories": 2048,
        "burn_in": 4096,
        "horizon": 1024,
        "escape_bound": 100.0,
        "bootstrap_replicates": 2000,
        "ci_level": 0.95,
        "exposure_gate": CONFIRMATORY_EXPOSURE_GATE,
    }
    observed = {
        "a": arguments.a,
        "rhos": list(arguments.rhos),
        "n_trajectories": arguments.n_trajectories,
        "burn_in": arguments.burn_in,
        "horizon": arguments.horizon,
        "escape_bound": arguments.escape_bound,
        "bootstrap_replicates": arguments.bootstrap_replicates,
        "ci_level": arguments.ci_level,
        "exposure_gate": arguments.exposure_gate,
    }
    return [
        f"{name}: expected {expected[name]!r}, observed {value!r}"
        for name, value in observed.items()
        if value != expected[name]
    ]


def main() -> int:
    arguments = parse_arguments()
    validate_arguments(arguments)
    json_path, summary_path, cluster_path = output_paths(arguments)
    paths = (json_path, summary_path, cluster_path)
    existing = [path for path in paths if path.exists()]
    if existing and not arguments.overwrite:
        joined = ", ".join(str(path) for path in existing)
        raise FileExistsError(
            f"refusing to overwrite {joined}; use --overwrite deliberately"
        )
    arguments.output_dir.mkdir(parents=True, exist_ok=True)

    initial_states = generate_parent_ensemble(
        split=arguments.split,
        n_trajectories=arguments.n_trajectories,
        burn_in=arguments.burn_in,
        a=arguments.a,
        allow_confirmatory_test=arguments.unlock_confirmatory_test,
    )

    summaries: list[dict[str, Any]] = []
    rhos_and_results: list[tuple[float, Any]] = []
    for rho_index, rho in enumerate(arguments.rhos):
        result = simulate_transport(
            initial_states,
            rho=rho,
            a=arguments.a,
            horizon=arguments.horizon,
            escape_bound=arguments.escape_bound,
        )
        intervals = cluster_bootstrap(
            result,
            n_replicates=arguments.bootstrap_replicates,
            seed=SPLIT_SEEDS[arguments.split] + 1_000_003 + 10_007 * rho_index,
            ci_level=arguments.ci_level,
        )
        summary = summarize_result(
            result,
            intervals=intervals,
            exposure_gate=arguments.exposure_gate,
        )
        summaries.append(summary)
        rhos_and_results.append((rho, result))
        print(
            f"rho={rho:g} exposure={result.exposure_fraction:.6f} "
            f"survival={result.survival_fraction:.6f} "
            f"P={result.parity_polarity:.6f} gaps={result.total_gaps}"
        )

    deviations = protocol_deviations(arguments)
    endpoint_summary = next(
        (
            summary
            for summary in summaries
            if math.isclose(
                float(summary["rho"]), CONFIRMATORY_RHO, rel_tol=0.0, abs_tol=1e-12
            )
        ),
        None,
    )
    if endpoint_summary is None:
        endpoint: dict[str, Any] = {
            "rho": CONFIRMATORY_RHO,
            "metric": "parity_polarity",
            "status": "not_run",
            "reason": "rho=1 was not included in this invocation",
        }
    else:
        endpoint = evaluate_confirmatory_endpoint(
            endpoint_summary,
            split=arguments.split,
            neighbor_specificity_passed=None,
            exposure_gate=arguments.exposure_gate,
            minimum_gaps=CONFIRMATORY_MIN_GAPS,
            polarity_lower_bound=CONFIRMATORY_POLARITY_LOWER_BOUND,
            protocol_deviations=deviations,
        )

    source_lock_path = PAPER_ROOT / "experiments" / "source_lock.json"
    source_lock_bytes = source_lock_path.read_bytes()

    payload = {
        "schema_version": 1,
        "experiment": "frozen_seed_symbolic_transport",
        "map": "H_{a,rho}(x,y)=(1-a*x^2-rho*y,x)",
        "singular_reference": (
            "rho=0 exactly recovers the scalar first coordinate and is not "
            "treated as a smooth symplectic continuation point"
        ),
        "primary_metric": (
            "L-return parity polarity P=(even_gaps-odd_gaps)/total_gaps, "
            "L={x<0}"
        ),
        "matched_null": (
            "two-state first-order Markov chain fitted to the observed "
            "within-trajectory transition counts"
        ),
        "uncertainty": (
            f"{arguments.ci_level:.1%} percentile intervals from "
            f"{arguments.bootstrap_replicates} whole-trajectory bootstrap replicates"
        ),
        "split": arguments.split,
        "split_seed": SPLIT_SEEDS[arguments.split],
        "confirmatory_test_unlocked": bool(
            arguments.split == "test" and arguments.unlock_confirmatory_test
        ),
        "source_lock": {
            "path": str(source_lock_path.relative_to(PAPER_ROOT)),
            "sha256": hashlib.sha256(source_lock_bytes).hexdigest(),
        },
        "protocol_deviations": deviations,
        "parameters": {
            "a": arguments.a,
            "rhos": arguments.rhos,
            "n_trajectories": arguments.n_trajectories,
            "burn_in": arguments.burn_in,
            "horizon": arguments.horizon,
            "escape_bound": arguments.escape_bound,
            "bootstrap_replicates": arguments.bootstrap_replicates,
            "ci_level": arguments.ci_level,
            "exposure_gate": arguments.exposure_gate,
        },
        "runtime": {
            "python": platform.python_version(),
            "numpy": np.__version__,
        },
        "confirmatory_endpoint": endpoint,
        "results": summaries,
    }

    json_path.write_text(
        json.dumps(json_safe(payload), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_summary_csv(summary_path, summaries)
    write_cluster_csv(cluster_path, rhos_and_results=rhos_and_results)
    print(f"wrote {json_path}")
    print(f"wrote {summary_path}")
    print(f"wrote {cluster_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
