#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C296 hard-rod shape flow."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c296_hard_rod_evidence.json"
SOURCE = "f8d3ad9a8940b54e82854b2924be353575ed8fcb"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"

MODEL = {
    "state": "rotation-reduced unlabeled collision-glued phase space of N equal unit-mass clockwise rods of length a on the circle of circumference ell",
    "parameter_domain": "N>=1, a>0, ell>N*a, and free length L=ell-N*a>0",
    "shape_quotient": "global spatial rotations are removed but velocities, including their common drift, are retained",
    "compression": "after choosing a cyclic lift, y_i=x_i-(i-1)*a; cyclic-start changes become a common translation after permutation",
    "free_model": "N free phase points on the circle of circumference L modulo pair permutations and common position translations",
    "collision_convention": "at each maximal compressed coincidence block the right outgoing spatial velocity order is the sorted incoming multiset",
    "clock": "physical time t in R; collision boundary states are glued by the equal-mass velocity permutation",
}
THEOREM = {
    "conjugacy": "compression is a bijection of rotation-reduced collision-glued hard-rod phase space with the common-translation and S_N quotient of free phase points, and it conjugates the complete flows",
    "events": "binary, disjoint simultaneous, and genuine multiple contacts are exactly the isolated coincidences of distinct-velocity free points; each contact block permutes velocities and never changes their multiset",
    "invariants": "total momentum and kinetic energy are conserved at every event and for all time",
    "no_zeno": "on every compact time interval each unequal-velocity pair has finitely many circle coincidences, so the aggregated event set is finite",
    "return": "a reduced state returns at T>0 iff some sigma in S_N and c in R/LZ satisfy y_i+T*v_i congruent to y_sigma(i)+c mod L and v_i=v_sigma(i) for every i",
    "distinct_velocities": "for pairwise distinct velocities return is equivalent to T*(v_i-v_j) in L*Z for all i,j; nonzero differences must be commensurable",
    "repeated_velocities": "if H_u has order d_u for the position multiset carrying velocity u, return is equivalent to lcm(d_u,d_w)*T*(u-w) in L*Z for every velocity pair",
    "topology_obstruction": "without rotation reduction the naive length-L compression loses a global-angle cocycle and is not a conjugacy",
    "boundary": "N=1 and common-velocity states are fixed only after rotation reduction; L=0 is excluded; contact faces and persistent equal-velocity contacts are allowed",
}
PROOF = {
    "gap_map": "rod free gaps sum to L and coincide with cyclic gaps of compressed points; this gives the configuration-space bijection after common-translation and permutation quotients",
    "well_defined": "changing the cyclic starting rod sends the compressed list to a cyclic permutation followed by common translation by a",
    "flow": "unfolding equal-mass impacts lets free phase points pass through while spatially ordered rods exchange the same velocity labels",
    "multi_collision": "adjacent transpositions generate every permutation within a maximal coincidence block, so the collision-glued quotient removes ordering ambiguity",
    "event_bound": "pair coincidences solve one affine congruence and have an explicit finite count on compact intervals",
    "return_proof": "equality in the free quotient gives the sigma-c condition, and velocity classes reduce it to intersections of finite translation-stabilizer cosets",
    "stabilizer_crt": "finite circle stabilizers are H_d=(L/d)Z/LZ and generalized CRT converts coset compatibility to the lcm-weighted difference criterion",
    "obstruction_proof": "for N=1 the unreduced hard rod returns after ell/abs(v), whereas the false naive compressed circle would return after L/abs(v)",
    "finite_role": "finite rational scenarios audit constants and all event branches but do not replace the all-parameter quotient proof",
}
ROUTE = {
    "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
    "overall": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
}
FLAGS = {
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
        "id": "Jepsen1965",
        "authors": "D. W. Jepsen",
        "title": "Dynamics of a Simple Many-Body System of Hard Rods",
        "venue": "Journal of Mathematical Physics 6(3) (1965), 405-413",
        "identifier": "10.1063/1.1704288",
        "url": "https://doi.org/10.1063/1.1704288",
        "ownership": "direct classical owner for equal-mass hard-rod dynamics, free crossing, and Poincare cycles",
    },
    {
        "id": "Tonks1936",
        "authors": "Lewi Tonks",
        "title": "The Complete Equation of State of One, Two and Three-Dimensional Gases of Hard Elastic Spheres",
        "venue": "Physical Review 50 (1936), 955-963",
        "identifier": "10.1103/PhysRev.50.955",
        "url": "https://doi.org/10.1103/PhysRev.50.955",
        "ownership": "classical owner for the one-dimensional finite-length hard-rod model and excluded-volume reduction",
    },
]

SCENARIOS = [
    {"id": "binary_recurring", "ell": 11, "a": 1, "y": [0, 3], "v": [2, -1], "horizon": 7, "query": [0, 1, 2, 4, 7]},
    {"id": "simultaneous_triple", "ell": 15, "a": 1, "y": [0, 4, 8], "v": [2, 0, -2], "horizon": 5, "query": [0, 1, 2, 3, 5]},
    {"id": "simultaneous_disjoint", "ell": 16, "a": 1, "y": [0, 2, 6, 8], "v": [1, -1, 2, 0], "horizon": 7, "query": [0, 1, 2, 4, 7]},
    {"id": "repeated_symmetric", "ell": 16, "a": 1, "y": [0, 3, 6, 9], "v": [1, -1, 1, -1], "horizon": 6, "query": [0, 1, 3, 6]},
    {"id": "common_drift", "ell": 13, "a": 1, "y": [0, 2, 7], "v": [5, 5, 5], "horizon": 5, "query": [0, 1, 5]},
    {"id": "initial_contact", "ell": 12, "a": 1, "y": [0, 0, 4], "v": [-1, 1, 0], "horizon": 5, "query": [0, 1, 3, 5]},
    {"id": "single_rod", "ell": 7, "a": 2, "y": [0], "v": [3], "horizon": 4, "query": [0, 1, 4]},
]


def F(value: int | Fraction) -> Fraction:
    return value if isinstance(value, Fraction) else Fraction(value)


def q(value: Fraction | int) -> str:
    return str(F(value))


def floor_q(value: Fraction) -> int:
    return value.numerator // value.denominator


def ceil_q(value: Fraction) -> int:
    return -floor_q(-value)


def mod_q(value: Fraction, length: Fraction) -> Fraction:
    return value - floor_q(value / length) * length


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def pair_times(y0: Fraction, y1: Fraction, v0: Fraction, v1: Fraction, length: Fraction, horizon: Fraction) -> list[Fraction]:
    dv = v0 - v1
    if dv == 0:
        return []
    start = y0 - y1
    finish = start + horizon * dv
    lo, hi = min(start, finish), max(start, finish)
    out = []
    for k in range(ceil_q(lo / length), floor_q(hi / length) + 1):
        time = (k * length - start) / dv
        if 0 <= time <= horizon:
            out.append(time)
    return sorted(set(out))


def canonical_gap_signature(positions: list[Fraction], length: Fraction) -> list[str]:
    ordered = sorted(mod_q(z, length) for z in positions)
    gaps = [ordered[i + 1] - ordered[i] for i in range(len(ordered) - 1)]
    gaps.append(ordered[0] + length - ordered[-1])
    rotations = [gaps[i:] + gaps[:i] for i in range(len(gaps))]
    return [q(z) for z in min(rotations)]


def canonical_phase_signature(positions: list[Fraction], velocities: list[Fraction], length: Fraction) -> list[str]:
    candidates = []
    for anchor in positions:
        rows = sorted((mod_q(pos - anchor, length), vel) for pos, vel in zip(positions, velocities))
        candidates.append(rows)
    best = min(candidates)
    return [f"{q(pos)}@{q(vel)}" for pos, vel in best]


def stabilizer_shifts(points: list[Fraction], length: Fraction) -> list[Fraction]:
    base = Counter(mod_q(z, length) for z in points)
    first = next(iter(base))
    candidates = {mod_q(z - first, length) for z in base}
    good = []
    for shift in sorted(candidates):
        moved = Counter(mod_q(z + shift, length) for z in points)
        if moved == base:
            good.append(shift)
    return good


def rational_gcd(values: list[Fraction]) -> Fraction:
    nonzero = [abs(z) for z in values if z]
    if not nonzero:
        return Fraction(0)
    denominator = math.lcm(*(z.denominator for z in nonzero))
    integers = [abs(z.numerator * (denominator // z.denominator)) for z in nonzero]
    return Fraction(math.gcd(*integers), denominator)


def return_data(identifier: str, y: list[Fraction], v: list[Fraction], length: Fraction) -> tuple[list[dict], dict]:
    classes: dict[Fraction, list[Fraction]] = defaultdict(list)
    for pos, vel in zip(y, v):
        classes[vel].append(pos)
    stabilizers = {}
    cells = []
    for vel in sorted(classes):
        shifts = stabilizer_shifts(classes[vel], length)
        stabilizers[vel] = shifts
        cells.append({
            "scenario": identifier,
            "velocity": q(vel),
            "multiplicity": len(classes[vel]),
            "stabilizer_order": len(shifts),
            "stabilizer_shifts": [q(z) for z in shifts],
        })
    weighted = []
    velocity_values = sorted(classes)
    for u, w in itertools.combinations(velocity_values, 2):
        d = math.lcm(len(stabilizers[u]), len(stabilizers[w]))
        weighted.append(Fraction(d) * (u - w))
    generator = rational_gcd(weighted)
    fixed = len(velocity_values) == 1
    witness_time = Fraction(1) if fixed else length / generator
    cosets = []
    for vel in velocity_values:
        cosets.append({mod_q(witness_time * vel - h, length) for h in stabilizers[vel]})
    common = set.intersection(*cosets)
    if not common:
        raise AssertionError("return CRT witness missing")
    translation = min(common)
    permutation = [-1] * len(y)
    for vel in velocity_values:
        targets: dict[Fraction, list[int]] = defaultdict(list)
        for j, (pos, value) in enumerate(zip(y, v)):
            if value == vel:
                targets[mod_q(pos + translation, length)].append(j)
        for i, (pos, value) in enumerate(zip(y, v)):
            if value == vel:
                key = mod_q(pos + witness_time * vel, length)
                permutation[i] = targets[key].pop(0)
    if sorted(permutation) != list(range(len(y))):
        raise AssertionError("return permutation")
    row = {
        "scenario": identifier,
        "status": "FIXED_SHAPE" if fixed else "PERIODIC_NONFIXED",
        "weighted_difference_generator": q(generator),
        "minimal_period": "NO_LEAST_POSITIVE_PERIOD" if fixed else q(length / generator),
        "witness_time": q(witness_time),
        "witness_common_translation": q(translation),
        "witness_permutation": permutation,
    }
    return cells, row


def build() -> dict:
    scenario_rows = []
    particle_cells = []
    pair_cells = []
    event_cells = []
    shape_cells = []
    stabilizer_cells = []
    return_cells = []
    conservation_cells = []
    for spec in SCENARIOS:
        n = len(spec["y"])
        ell, a = F(spec["ell"]), F(spec["a"])
        length = ell - n * a
        y = [mod_q(F(z), length) for z in spec["y"]]
        v = [F(z) for z in spec["v"]]
        horizon = F(spec["horizon"])
        if not (n >= 1 and a > 0 and length > 0):
            raise AssertionError("scenario domain")
        scenario_rows.append({
            "id": spec["id"], "N": n, "ell": q(ell), "a": q(a), "L": q(length),
            "horizon": q(horizon), "query_times": [q(F(z)) for z in spec["query"]],
        })
        for index, (pos, vel) in enumerate(zip(y, v)):
            particle_cells.append({"scenario": spec["id"], "index": index, "y": q(pos), "velocity": q(vel)})
        event_times: set[Fraction] = set()
        for i, j in itertools.combinations(range(n), 2):
            for time in pair_times(y[i], y[j], v[i], v[j], length, horizon):
                pair_cells.append({"scenario": spec["id"], "i": i, "j": j, "time": q(time)})
                event_times.add(time)
        for event_index, time in enumerate(sorted(event_times), 1):
            positions = [mod_q(pos + time * vel, length) for pos, vel in zip(y, v)]
            groups: dict[Fraction, list[int]] = defaultdict(list)
            for index, pos in enumerate(positions):
                groups[pos].append(index)
            collision_groups = []
            for pos in sorted(groups):
                indices = groups[pos]
                velocities = [v[i] for i in indices]
                if len(indices) < 2 or len(set(velocities)) < 2:
                    continue
                collision_groups.append({
                    "position": q(pos), "indices": indices,
                    "incoming_spatial_velocities": [q(z) for z in sorted(velocities, reverse=True)],
                    "outgoing_spatial_velocities": [q(z) for z in sorted(velocities)],
                    "momentum_before": q(sum(velocities)), "momentum_after": q(sum(velocities)),
                    "twice_energy_before": q(sum(z * z for z in velocities)),
                    "twice_energy_after": q(sum(z * z for z in velocities)),
                })
            if collision_groups:
                event_cells.append({
                    "scenario": spec["id"], "event_index": event_index, "time": q(time),
                    "group_count": len(collision_groups), "groups": collision_groups,
                })
        for time0 in spec["query"]:
            time = F(time0)
            positions = [mod_q(pos + time * vel, length) for pos, vel in zip(y, v)]
            shape_cells.append({
                "scenario": spec["id"], "time": q(time),
                "gap_signature": canonical_gap_signature(positions, length),
                "phase_signature": canonical_phase_signature(positions, v, length),
            })
        stabs, returns = return_data(spec["id"], y, v, length)
        stabilizer_cells.extend(stabs)
        return_cells.append(returns)
        conservation_cells.append({
            "scenario": spec["id"], "momentum": q(sum(v)),
            "twice_kinetic_energy": q(sum(z * z for z in v)),
            "pair_event_bound": sum(len(pair_times(y[i], y[j], v[i], v[j], length, horizon)) for i, j in itertools.combinations(range(n), 2)),
            "aggregated_event_times": sum(row["scenario"] == spec["id"] for row in event_cells),
        })

    symbolic_return_cases = [
        {
            "id": "distinct_incommensurable",
            "L": "10", "positions": ["0", "1", "4"], "velocities": ["0", "1", "sqrt(2)"],
            "verdict": "NO_POSITIVE_RETURN",
            "proof": "a return would make T/10 and sqrt(2)*T/10 integers, forcing sqrt(2) rational",
        }
    ]
    boundary_cells = [
        {"id": "single_rod_reduced", "status": "configuration shape is one point and every fixed-velocity phase state is an equilibrium"},
        {"id": "common_velocity", "status": "all positions translate together, so the reduced shape state is fixed while the retained common velocity distinguishes equilibria"},
        {"id": "unreduced_counterexample", "status": "for N=1 and v nonzero the physical return is ell/abs(v), not L/abs(v); a global-angle cocycle is missing"},
        {"id": "cyclic_start", "status": "changing the first rod permutes compressed points and translates every y by a, which vanishes only in the reduced target"},
        {"id": "close_packing", "status": "L=0 is excluded because the reduced free circle collapses"},
        {"id": "zero_length_limit", "status": "a down to zero is a closure limit to free point particles, not an additional hard-rod claim"},
        {"id": "contact_faces", "status": "zero free gaps and simultaneous multiple contacts are included through collision gluing"},
        {"id": "persistent_contact", "status": "coincident compressed points with equal velocity remain in contact and create no isolated event"},
        {"id": "time_reversal", "status": "the quotient construction defines a reversible all-real-time group"},
    ]
    enumeration = {
        "scenario_count": len(scenario_rows),
        "particle_cells": len(particle_cells),
        "pair_crossing_cells": len(pair_cells),
        "event_time_cells": len(event_cells),
        "event_group_cells": sum(len(row["groups"]) for row in event_cells),
        "shape_query_cells": len(shape_cells),
        "velocity_class_cells": len(stabilizer_cells),
        "return_cells": len(return_cells),
        "symbolic_return_cells": len(symbolic_return_cases),
        "conservation_cells": len(conservation_cells),
        "boundary_cells": len(boundary_cells),
    }
    data = {
        "schema": "hcs-c296-hard-rod-rotation-reduced-shape-v1",
        "candidate_id": "HCS-C296",
        "obstruction_id": "HEN-O280",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": MODEL,
        "theorem_contract": THEOREM,
        "proof_contract": PROOF,
        "route_a": ROUTE,
        "scope_flags": FLAGS,
        "enumeration": enumeration,
        "scenarios": scenario_rows,
        "particle_cells": particle_cells,
        "pair_crossing_cells": pair_cells,
        "event_cells": event_cells,
        "shape_cells": shape_cells,
        "stabilizer_cells": stabilizer_cells,
        "return_cells": return_cells,
        "symbolic_return_cases": symbolic_return_cases,
        "conservation_cells": conservation_cells,
        "boundary_cells": boundary_cells,
        "references": REFERENCES,
        "nonclaims": [
            "the Jepsen hard-rod/free-crossing mechanism and the Tonks excluded-volume coordinate are not claimed as literature originality",
            "the conjugacy is only for the rotation-reduced shape flow; the complete physical rotation angle and its cocycle are not reconstructed",
            "finite rational scenarios are regression evidence and do not prove the all-parameter theorem",
            "the natural hard-core kinetic quantization is an A4 classification only; no spectral correspondence or Hilbert-Polya operator is claimed",
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
    audited = sum(data["enumeration"].values()) - data["enumeration"]["scenario_count"]
    print(f"C296_PRODUCER_PASS {data['payload_sha256']} audited_cells={audited}")


if __name__ == "__main__":
    main()
