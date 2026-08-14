#!/usr/bin/env python3
"""Deterministic tests for Paper 33 / SD-C35."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

from cycle_quotient_core import (
    adjacency_descent_certificate,
    build_action,
    component_count,
    cross_square_complex,
    cusp_rs_witness,
    permutation_orbits,
    random_transitive_action,
    relation_quotient_dimension,
)


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def read_csv(name: str) -> list[dict[str, str]]:
    with (RESULTS / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def require(condition: bool, name: str, failures: list[str]) -> None:
    if not condition:
        failures.append(name)


def main() -> int:
    failures: list[str] = []
    rows = read_csv("modulus_homology_census.csv")
    matched = read_csv("matched_clone.csv")
    random_rows = read_csv("random_action_controls.csv")
    twists = read_csv("twist_census.csv")
    summary = json.loads((RESULTS / "summary.json").read_text(encoding="utf-8"))
    cross = json.loads((RESULTS / "cross_square_complex.json").read_text(encoding="utf-8"))

    require(len(rows) == 191, "modulus row count", failures)
    require({int(row["modulus"]) for row in rows} == set(range(2, 193)), "modulus range", failures)

    for row in rows:
        n = int(row["modulus"])
        action = build_action(n)
        s_orbits = permutation_orbits(action.s_image)
        r_orbits = permutation_orbits(action.r_image)
        betti = relation_quotient_dimension(action.s_image, action.r_image)
        relation_rank, augmented_rank = adjacency_descent_certificate(action)
        c, y, end = cusp_rs_witness(action)
        require(int(row["state_count"]) == action.size, f"state count {n}", failures)
        require(int(row["s_orbits"]) == len(s_orbits), f"S orbit count {n}", failures)
        require(int(row["r_orbits"]) == len(r_orbits), f"R orbit count {n}", failures)
        require(int(row["relative_betti"]) == betti, f"relative betti {n}", failures)
        require(int(row["relation_rank"]) == relation_rank, f"relation rank {n}", failures)
        require(int(row["adjacency_augmented_rank"]) == augmented_rank, f"adjacency rank {n}", failures)
        require(c != y and c == end, f"cusp witness {n}", failures)
        require(int(row["adjacency_descends"]) == 0, f"non-descent {n}", failures)
        require(betti > 0, f"positive betti {n}", failures)

    require(all(int(row["transport_exact"]) == 1 for row in matched), "all matched relabels exact", failures)
    require(len(random_rows) == 64, "random row count", failures)
    for row in random_rows:
        seed = int(row["seed"])
        size = int(row["states"])
        s_image, r_image, _ = random_transitive_action(size, seed)
        residual = relation_quotient_dimension(s_image, r_image)
        require(component_count(s_image, r_image) == 1, f"random connected {seed}", failures)
        require(residual == int(row["residual_betti"]), f"random residual {seed}", failures)
        require(residual > 0, f"random nonzero {seed}", failures)

    honest = [row for row in twists if row["kind"] == "honest_character"]
    virtual = [row for row in twists if row["kind"] == "zero_superdimension_difference"]
    require(len(honest) == 6, "six honest characters", failures)
    require(sum(int(row["kills_identity_cycle_words"]) for row in honest) == 0, "honest cycle words survive", failures)
    require(sum(int(row["kills_both_chain_norms"]) for row in honest) == 2, "two honest chain norm killers", failures)
    require(len(virtual) == 15, "fifteen virtual differences", failures)
    require(all(int(row["kills_identity_cycle_words"]) == 1 for row in virtual), "virtual identity cancellation", failures)
    require(sum(int(row["kills_both_chain_norms"]) for row in virtual) == 2, "two virtual chain norm killers", failures)
    require(all(int(row["cusp_sr_nonzero"]) == 1 for row in virtual), "virtual cusp survives", failures)

    require(cross == cross_square_complex(192), "cross square complex", failures)
    require(cross["graph_betti_before_filling"] == cross["diamond_boundary_rank"], "diamond rank", failures)
    require(cross["homology_after_filling"] == 0, "filled cross H1 zero", failures)
    require(summary["all_blocks_relative_nonzero"] is True, "summary relative nonzero", failures)
    require(summary["all_tested_adjacencies_fail_to_descend"] is True, "summary non-descent", failures)
    require(summary["route_b"] == "LOCKED", "route B locked", failures)

    report = {
        "candidate_id": "SD-C35",
        "test_count": 25,
        "passes": 25 if not failures else 25 - len(failures),
        "failures": failures,
    }
    print(json.dumps(report, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
