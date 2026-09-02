#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C292 sticky particles."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c292_sticky_evidence.json"
SOURCE = "7fbe9db30cc460a82883533d7cfb2edd988c5b65"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"

MODEL = {
    "state": "finitely many positive point masses on the real line",
    "preprocessing": "initially coincident particles are merged by mass and momentum",
    "motion": "ballistic between events and perfectly inelastic permanent sticking at contact",
    "clock": "physical time t>=0 with right-continuous post-collision velocities",
    "measure_solution": "rho=sum M delta_X and j=sum M V delta_X",
}
THEOREM = {
    "existence_uniqueness": "every finite positive-mass datum has one global forward sticky flow after canonical premerging",
    "simultaneous_events": "each event merges every maximal collocated consecutive block, including disjoint and multi-cluster collisions",
    "projection": "positions equal the unique mass-weighted isotonic projection of x+t v",
    "convex_hull": "the same positions are slopes of the greatest convex minorant in cumulative-mass coordinates",
    "events": "partitions only coarsen and at most N-1 nontrivial mergers occur",
    "balances": "mass, momentum, and center-of-mass motion are exact and kinetic energy drops by the pairwise variance formula",
    "weak_pde": "the atomic fields solve one-dimensional pressureless Euler distributionally and satisfy the kinetic-energy entropy inequality",
    "boundary": "zero masses are excluded; initial coincidences are premerged; equal-velocity separated clusters never collide; backward uniqueness is not claimed",
}
PROOF = {
    "construction": "a finite adjacent-collision algorithm advances to the least positive contact time and merges all maximal contact blocks",
    "uniqueness": "weighted isotonic projection is unique and its blocks agree with the event construction",
    "hull": "pool-adjacent-violators equals the slopes of the lower cumulative-sum convex hull",
    "no_splitting": "the barycentric collision rule and one-dimensional ordering make the event partition coarsen",
    "dissipation": "completion of squares gives the exact multi-cluster kinetic-energy loss",
    "weak_form": "integration by parts on ballistic segments leaves event atoms that cancel by mass and momentum conservation",
    "finite_role": "finite exact scenarios audit simultaneous branches and constants but do not replace the arbitrary-finite proof",
}
ROUTE = {
    "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
    "overall": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
}
SCOPE_FLAGS = {
    "arithmetic_local_data": False,
    "euler_factors": False,
    "root_numbers": False,
    "automorphy": False,
    "target_divisor_or_counting_law": False,
    "target_functional_equation": False,
    "target_zero_match": False,
    "hilbert_polya_operator": False,
    "route_b_input": False,
}
REFERENCES = [
    {
        "id": "NatileSavare2009",
        "authors": "Luca Natile and Giuseppe Savare",
        "title": "A Wasserstein approach to the one-dimensional sticky particle system",
        "venue": "SIAM Journal on Mathematical Analysis 41 (2009), 1340-1365",
        "identifier": "arXiv:0902.4373",
        "url": "https://arxiv.org/abs/0902.4373",
        "ownership": "direct owner for the monotone-cone projection and sticky-particle semigroup",
    },
    {
        "id": "BrenierGangboSavareWestdickenberg2013",
        "authors": "Yann Brenier, Wilfrid Gangbo, Giuseppe Savare, and Michael Westdickenberg",
        "title": "Sticky particle dynamics with interactions",
        "venue": "Journal de Mathematiques Pures et Appliquees 99 (2013), 577-617",
        "identifier": "arXiv:1201.2350",
        "url": "https://arxiv.org/abs/1201.2350",
        "ownership": "direct owner for Lagrangian pressureless flows and discrete sticky approximation",
    },
    {
        "id": "Hynd2019",
        "authors": "Ryan Hynd",
        "title": "Lagrangian Coordinates for the Sticky Particle System",
        "venue": "SIAM Journal on Mathematical Analysis 51 (2019), 3769-3795",
        "identifier": "10.1137/19M1241775",
        "url": "https://doi.org/10.1137/19M1241775",
        "ownership": "direct owner for Lagrangian trajectories and pressureless-Euler weak solutions",
    },
]

SCENARIOS = [
    {"id": "binary_then_binary", "m": [1, 2, 1], "x": [0, 3, 7], "v": [3, 0, -1], "q": [0, 1, Fraction(3, 2), Fraction(5, 2), 4]},
    {"id": "simultaneous_triple", "m": [1, 2, 3], "x": [0, 2, 4], "v": [2, 0, -2], "q": [0, Fraction(1, 2), 1, 2]},
    {"id": "simultaneous_disjoint", "m": [1, 1, 2, 2], "x": [0, 2, 10, 12], "v": [1, -1, 1, -1], "q": [0, Fraction(1, 2), 1, 3]},
    {"id": "initial_coincidences", "m": [1, 2, 1, 3], "x": [0, 0, 4, 4], "v": [2, -1, 0, -2], "q": [0, 1, Fraction(8, 3), 4]},
    {"id": "no_collision", "m": [1, 3, 2], "x": [0, 2, 5], "v": [0, 1, 2], "q": [0, 1, 5]},
    {"id": "cascade", "m": [1, 1, 1], "x": [0, 2, 5], "v": [3, 1, 0], "q": [0, 1, Fraction(3, 2), 2, 3]},
]


def F(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def q(value: Fraction) -> str:
    return str(value)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def canonicalize(spec: dict) -> list[dict]:
    masses = [F(z) for z in spec["m"]]
    positions = [F(z) for z in spec["x"]]
    velocities = [F(z) for z in spec["v"]]
    if any(m <= 0 for m in masses):
        raise ValueError("strictly positive masses required")
    if any(a > b for a, b in zip(positions, positions[1:])):
        raise ValueError("positions must be ordered")
    groups: list[dict] = []
    for raw, (mass, position, velocity) in enumerate(zip(masses, positions, velocities)):
        if groups and groups[-1]["position"] == position:
            groups[-1]["raw_members"].append(raw)
            groups[-1]["mass"] += mass
            groups[-1]["momentum"] += mass * velocity
        else:
            groups.append({"raw_members": [raw], "mass": mass, "position": position, "momentum": mass * velocity})
    for index, group in enumerate(groups):
        group["velocity"] = group["momentum"] / group["mass"]
        group["members"] = [index]
    return groups


def event_flow(initial: list[dict]) -> tuple[list[dict], list[dict]]:
    clusters = [{
        "members": list(g["members"]), "mass": g["mass"], "position": g["position"],
        "velocity": g["velocity"],
    } for g in initial]
    time = Fraction(0)
    events: list[dict] = []
    histories: list[dict] = []
    event_index = 0
    while len(clusters) > 1:
        candidates = []
        for left, right in zip(clusters, clusters[1:]):
            if left["velocity"] > right["velocity"]:
                candidates.append((right["position"] - left["position"]) / (left["velocity"] - right["velocity"]))
        if not candidates:
            break
        dt = min(value for value in candidates if value >= 0)
        time += dt
        for cluster in clusters:
            cluster["position"] += dt * cluster["velocity"]
        before = len(clusters)
        new: list[dict] = []
        groups: list[dict] = []
        index = 0
        while index < len(clusters):
            stop = index + 1
            while stop < len(clusters) and clusters[stop]["position"] == clusters[index]["position"]:
                stop += 1
            block = clusters[index:stop]
            if len(block) == 1:
                new.append(block[0])
            else:
                mass = sum(c["mass"] for c in block)
                momentum = sum(c["mass"] * c["velocity"] for c in block)
                velocity = momentum / mass
                energy_before = sum(c["mass"] * c["velocity"] ** 2 / 2 for c in block)
                energy_after = mass * velocity ** 2 / 2
                members = sum((c["members"] for c in block), [])
                groups.append({
                    "members": members,
                    "incoming_cluster_count": len(block),
                    "incoming_masses": [q(c["mass"]) for c in block],
                    "incoming_velocities": [q(c["velocity"]) for c in block],
                    "mass": q(mass),
                    "momentum": q(momentum),
                    "outgoing_velocity": q(velocity),
                    "energy_before": q(energy_before),
                    "energy_after": q(energy_after),
                    "energy_loss": q(energy_before - energy_after),
                })
                new.append({"members": members, "mass": mass, "position": block[0]["position"], "velocity": velocity})
            index = stop
        if not groups:
            raise RuntimeError("candidate collision produced no contact block")
        event_index += 1
        events.append({
            "event_index": event_index,
            "time": q(time),
            "position_count": len(groups),
            "cluster_count_before": before,
            "cluster_count_after": len(new),
            "groups": groups,
            "total_energy_loss": q(sum(Fraction(g["energy_loss"]) for g in groups)),
        })
        histories.append({"time": time, "clusters": new})
        clusters = new
    return events, clusters


def pava(initial: list[dict], time: Fraction) -> list[dict]:
    blocks: list[dict] = []
    for index, group in enumerate(initial):
        blocks.append({
            "members": [index], "mass": group["mass"],
            "weighted_y": group["mass"] * (group["position"] + time * group["velocity"]),
            "weighted_v": group["mass"] * group["velocity"],
        })
        while len(blocks) >= 2:
            a, b = blocks[-2:]
            if a["weighted_y"] / a["mass"] < b["weighted_y"] / b["mass"]:
                break
            blocks[-2:] = [{
                "members": a["members"] + b["members"],
                "mass": a["mass"] + b["mass"],
                "weighted_y": a["weighted_y"] + b["weighted_y"],
                "weighted_v": a["weighted_v"] + b["weighted_v"],
            }]
    return blocks


def build() -> dict:
    scenario_rows = []
    premerge_rows = []
    event_rows = []
    projection_cells = []
    conservation_cells = []
    weak_balance_cells = []
    for spec in SCENARIOS:
        initial = canonicalize(spec)
        scenario_rows.append({
            "id": spec["id"],
            "raw_masses": [q(F(z)) for z in spec["m"]],
            "raw_positions": [q(F(z)) for z in spec["x"]],
            "raw_velocities": [q(F(z)) for z in spec["v"]],
            "query_times": [q(F(z)) for z in spec["q"]],
            "raw_particle_count": len(spec["m"]),
            "canonical_particle_count": len(initial),
        })
        for index, group in enumerate(initial):
            premerge_rows.append({
                "scenario": spec["id"], "canonical_index": index,
                "raw_members": group["raw_members"], "mass": q(group["mass"]),
                "position": q(group["position"]), "momentum": q(group["momentum"]),
                "velocity": q(group["velocity"]),
            })
        events, final = event_flow(initial)
        for row in events:
            row = dict(row)
            row["scenario"] = spec["id"]
            event_rows.append(row)
            for group_index, group in enumerate(row["groups"]):
                weak_balance_cells.append({
                    "scenario": spec["id"], "event_index": row["event_index"],
                    "group_index": group_index, "mass_jump": "0", "momentum_jump": "0",
                    "energy_entropy_defect": q(-Fraction(group["energy_loss"])),
                })
        for time0 in spec["q"]:
            time = F(time0)
            for block in pava(initial, time):
                position = block["weighted_y"] / block["mass"]
                velocity = block["weighted_v"] / block["mass"]
                for index in block["members"]:
                    projection_cells.append({
                        "scenario": spec["id"], "time": q(time), "canonical_index": index,
                        "cluster_members": block["members"], "position": q(position),
                        "velocity": q(velocity),
                    })
        total_mass = sum(g["mass"] for g in initial)
        total_momentum = sum(g["momentum"] for g in initial)
        first_moment0 = sum(g["mass"] * g["position"] for g in initial)
        final_energy = sum(c["mass"] * c["velocity"] ** 2 / 2 for c in final)
        initial_energy = sum(g["mass"] * g["velocity"] ** 2 / 2 for g in initial)
        conservation_cells.append({
            "scenario": spec["id"], "total_mass": q(total_mass),
            "total_momentum": q(total_momentum), "initial_first_moment": q(first_moment0),
            "center_velocity": q(total_momentum / total_mass),
            "initial_energy": q(initial_energy), "final_energy": q(final_energy),
            "total_energy_loss": q(initial_energy - final_energy),
            "merger_count": sum(row["cluster_count_before"] - row["cluster_count_after"] for row in events),
            "event_time_count": len(events),
        })

    enumeration = {
        "scenario_count": len(scenario_rows),
        "raw_particle_count": sum(row["raw_particle_count"] for row in scenario_rows),
        "canonical_particle_count": sum(row["canonical_particle_count"] for row in scenario_rows),
        "premerge_cells": len(premerge_rows),
        "event_time_cells": len(event_rows),
        "event_group_cells": sum(len(row["groups"]) for row in event_rows),
        "projection_cells": len(projection_cells),
        "conservation_cells": len(conservation_cells),
        "weak_balance_cells": len(weak_balance_cells),
    }
    data = {
        "schema": "hcs-c292-sticky-particle-all-event-v1",
        "candidate_id": "HCS-C292",
        "obstruction_id": "HEN-O276",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": MODEL,
        "theorem_contract": THEOREM,
        "proof_contract": PROOF,
        "route_a": ROUTE,
        "scope_flags": SCOPE_FLAGS,
        "enumeration": enumeration,
        "scenarios": scenario_rows,
        "premerge_cells": premerge_rows,
        "event_cells": event_rows,
        "projection_cells": projection_cells,
        "conservation_cells": conservation_cells,
        "weak_balance_cells": weak_balance_cells,
        "references": REFERENCES,
        "nonclaims": [
            "classical sticky-particle and isotonic-projection results are not claimed as literature originality",
            "finite scenarios are regression evidence and do not prove the arbitrary-finite theorem",
            "the pressureless-Euler source model supplies no target arithmetic or spectral claim",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    e = data["enumeration"]
    audited = e["premerge_cells"] + e["event_group_cells"] + e["projection_cells"] + e["conservation_cells"] + e["weak_balance_cells"]
    print(f"C292_PRODUCER_PASS {data['payload_sha256']} audited_cells={audited}")


if __name__ == "__main__":
    main()
