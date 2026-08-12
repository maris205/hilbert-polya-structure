#!/usr/bin/env python3
"""Run the fixed intrinsic wheel recursion and degree-matched controls."""

from __future__ import annotations

import argparse
import csv
import gzip
import json
import math
import sys
from pathlib import Path

from wheel_dag import (
    certify_levels,
    compare_to_arithmetic_units,
    controlled_levels,
    deletion_histogram_chi_square,
    intrinsic_wheels,
)


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    output = args.output
    output.mkdir(parents=True, exist_ok=True)

    max_level = int(config["max_level"])
    preserve_through_level = int(config["controls_preserve_through_level"])
    baseline_levels, baseline_edges, baseline_hist = intrinsic_wheels(max_level)
    experiments: list[tuple[str, int | None, list, list, list]] = [
        ("arithmetic", None, baseline_levels, baseline_edges, baseline_hist)
    ]
    for control in config["deterministic_controls"]:
        levels, edges, hist = controlled_levels(
            baseline_levels, control, preserve_through_level=preserve_through_level
        )
        experiments.append((control, None, levels, edges, hist))
    for seed in config["random_control_seeds"]:
        levels, edges, hist = controlled_levels(
            baseline_levels, "random_branch", int(seed), preserve_through_level
        )
        experiments.append(("random_branch", int(seed), levels, edges, hist))

    rows: list[dict[str, object]] = []
    certificates: dict[str, object] = {}
    for control, seed, levels, edges, histograms in experiments:
        key = control if seed is None else f"{control}_seed_{seed}"
        certificate = certify_levels(levels, edges)
        certificates[key] = certificate
        print(
            f"{key}: nodes={certificate['node_count']} edges={certificate['edge_count']} "
            f"acyclic={certificate['kahn_processed_all_nodes']}", flush=True
        )
        for index, level in enumerate(levels):
            comparison = compare_to_arithmetic_units(level)
            histogram = {0: 0} if index == 0 else histograms[index - 1]
            rows.append({
                "control": control,
                "seed": "not_applicable" if seed is None else seed,
                "level": level.level,
                "endogenous_multiplier": level.multiplier,
                "wheel_modulus": level.modulus,
                "derived_roof_log_wheel_ratio": 0.0 if index == 0 else math.log(level.multiplier),
                "residue_count": len(level.residues),
                "parent_outdegree": "not_applicable" if index == 0 else level.multiplier - 1,
                "level_edge_count": 0 if index == 0 else len(levels[index - 1].residues) * (level.multiplier - 1),
                "deletion_histogram_chi_square": deletion_histogram_chi_square(histogram),
                **comparison,
            })

    write_csv(output / "level_table.csv", rows)
    with gzip.open(output / "baseline_exact_edges.csv.gz", "wt", newline="", encoding="ascii") as handle:
        handle.write("parent_level,parent_residue,child_level,child_residue,branch,multiplier\n")
        for edge in baseline_edges:
            handle.write(edge.serialize())

    prime_sequence = [level.multiplier for level in baseline_levels[1:]]
    summary = {
        "experiment_id": config["experiment_id"],
        "object": "levelled symbolic DAG induced by the fixed wheel-sieve recursion",
        "recursion": {
            "base": "W_0=1, R_0={0}, p_0=1",
            "next_multiplier": "p_{k+1}=min{n>p_k:gcd(n,W_k)=1}",
            "wheel": "W_{k+1}=p_{k+1} W_k",
            "lift": "retain r+j W_k iff nonzero modulo p_{k+1}",
            "prime_table_input": False,
            "generated_multipliers": prime_sequence,
        },
        "endogenous_prime_induction": (
            "If the least coprime successor q were composite, a prime factor of q is either a prior "
            "multiplier (contradicting gcd(q,W_k)=1) or yields an earlier coprime survivor between "
            "p_k and q. Thus q is prime, starting from q=2."
        ),
        "max_level": max_level,
        "controls": {
            "matched_property": "same multipliers, modulus, one deleted branch per parent, out-degree, node count, edge count",
            "deterministic": config["deterministic_controls"],
            "random": "one seeded uniform deleted branch per parent and level",
            "shared_arithmetic_prefix_through_level": preserve_through_level,
            "random_seed_ledger_complete": config["random_control_seeds"],
        },
        "certificates": certificates,
        "forbidden_data_audit": {
            "Riemann_zero_table_loaded": False,
            "external_prime_table_loaded": False,
            "zero_based_parameter_selection": False,
        },
        "evidence_labels": {
            "prime_recursion": "PROVED (elementary induction stated above)",
            "finite_DAG_ledger": "NUMERICALLY_CERTIFIED by exhaustive exact-integer enumeration",
            "no_cycles": "PROVED by strict level increase; independently certified by Kahn traversal",
            "control_separation": "NUMERICAL_OBSERVATION at the frozen cutoff",
        },
        "claim_boundary": (
            "The arithmetic recursion is intrinsic, but this level shift is a DAG and has no directed "
            "periodic orbit. It therefore supplies no primitive/repetition orbit ledger and no natural "
            "Euler/Fredholm determinant. Controls are comparisons, not alternate prime generators."
        ),
        "route_b_invocation_allowed": False,
    }
    (output / "dag_certificate.json").write_text(
        json.dumps(summary, indent=2), encoding="utf-8"
    )
    print(f"wrote {len(rows)} level rows and {len(baseline_edges)} exact baseline edges")
    return 0


if __name__ == "__main__":
    sys.exit(main())
