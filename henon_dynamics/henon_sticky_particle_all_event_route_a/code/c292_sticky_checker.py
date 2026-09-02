#!/usr/bin/env python3
"""Strict producer-independent checker for HCS-C292.

The checker reconstructs trajectories from exhaustive weighted isotonic
partitions and block-line intersections.  It imports no producer code and
does not use the producer's event-loop implementation.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import re
from fractions import Fraction
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c292_sticky_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C292/2026-09-02.yaml"
SOURCE = "7fbe9db30cc460a82883533d7cfb2edd988c5b65"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVALUATION_SHA = "54650acae7553edea8e073f2c0406aaa418659a4f5442898e515d4d29c8f3130"

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
ROUTE = {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
FLAGS = {
    "arithmetic_local_data": False, "euler_factors": False, "root_numbers": False,
    "automorphy": False, "target_divisor_or_counting_law": False,
    "target_functional_equation": False, "target_zero_match": False,
    "hilbert_polya_operator": False, "route_b_input": False,
}
TOP_KEYS = {
    "schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit",
    "fixed_epoch", "scope_literal", "evaluator", "model", "theorem_contract",
    "proof_contract", "route_a", "scope_flags", "enumeration", "scenarios",
    "premerge_cells", "event_cells", "projection_cells", "conservation_cells",
    "weak_balance_cells", "references", "nonclaims", "payload_sha256",
}
SCENARIO_KEYS = {"id", "raw_masses", "raw_positions", "raw_velocities", "query_times", "raw_particle_count", "canonical_particle_count"}
PRE_KEYS = {"scenario", "canonical_index", "raw_members", "mass", "position", "momentum", "velocity"}
EVENT_KEYS = {"scenario", "event_index", "time", "position_count", "cluster_count_before", "cluster_count_after", "groups", "total_energy_loss"}
GROUP_KEYS = {"members", "incoming_cluster_count", "incoming_masses", "incoming_velocities", "mass", "momentum", "outgoing_velocity", "energy_before", "energy_after", "energy_loss"}
PROJ_KEYS = {"scenario", "time", "canonical_index", "cluster_members", "position", "velocity"}
CONS_KEYS = {"scenario", "total_mass", "total_momentum", "initial_first_moment", "center_velocity", "initial_energy", "final_energy", "total_energy_loss", "merger_count", "event_time_count"}
WEAK_KEYS = {"scenario", "event_index", "group_index", "mass_jump", "momentum_jump", "energy_entropy_defect"}
REF_KEYS = {"id", "authors", "title", "venue", "identifier", "url", "ownership"}
ENUM_KEYS = {"scenario_count", "raw_particle_count", "canonical_particle_count", "premerge_cells", "event_time_cells", "event_group_cells", "projection_cells", "conservation_cells", "weak_balance_cells"}
EVALUATION_EXPECTED = {
    "schema": "route-a-evaluation-v0.2.0",
    "candidate_id": "HCS-C292",
    "obstruction_id": "HEN-O276",
    "evaluation_date": "2026-09-02",
    "source_commit": SOURCE,
    "fixed_epoch": 1788307200,
    "scope_literal": SCOPE,
    "evaluator_authority_sha256": EVALUATOR,
    "theorem_status": "PROVABLE AS STATED",
    "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
    "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "axes": {
        "A0": "no arithmetic local-data carrier",
        "A1": "no primitive-orbit repetition bridge",
        "A2": "no arithmetic clock",
        "A3": "no target analytic structure",
        "A4": "no relevant target quantization",
    },
    "scope_flags": FLAGS,
}


class Checks:
    def __init__(self) -> None:
        self.n = 0

    def ok(self, condition: bool, label: str) -> None:
        self.n += 1
        if not condition:
            raise AssertionError(label)


def reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def strict_load(path: Path) -> dict[str, Any]:
    def bad(token: str) -> None:
        raise ValueError(f"nonfinite JSON number: {token}")
    value = json.loads(path.read_text(), object_pairs_hook=reject_duplicate_keys, parse_constant=bad)
    if type(value) is not dict:
        raise TypeError("top level must be object")
    return value


class UniqueSafeLoader(yaml.SafeLoader):
    """Safe YAML loader with duplicate rejection and dates kept as strings."""


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def construct_unique_mapping(loader: UniqueSafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    loader.flatten_mapping(node)
    out: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            duplicate = key in out
        except TypeError as error:
            raise yaml.constructor.ConstructorError(None, None, "unhashable YAML key", key_node.start_mark) from error
        if duplicate:
            raise yaml.constructor.ConstructorError(None, None, f"duplicate YAML key: {key}", key_node.start_mark)
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique_mapping)


def strict_yaml_load(path: Path) -> dict[str, Any]:
    value = yaml.load(path.read_text(), Loader=UniqueSafeLoader)
    if type(value) is not dict:
        raise TypeError("evaluation YAML top level must be object")
    return value


def semantic_hash(value: dict[str, Any]) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def phash(data: dict[str, Any]) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def keys(c: Checks, value: Any, expected: set[str], label: str) -> None:
    c.ok(type(value) is dict, f"{label} object")
    c.ok(set(value) == expected, f"{label} exact keys")


def typ(c: Checks, value: Any, expected: type, label: str) -> None:
    c.ok(type(value) is expected, f"{label} exact type")


def require(value: Any, expected: type, label: str) -> None:
    if type(value) is not expected:
        raise TypeError(f"{label} exact type {expected.__name__}")


def exact_tree(c: Checks, value: Any, expected: Any, label: str) -> None:
    c.ok(type(value) is type(expected), f"{label} exact type")
    if type(expected) is dict:
        c.ok(set(value) == set(expected), f"{label} exact keys")
        for key in expected:
            exact_tree(c, value[key], expected[key], f"{label}.{key}")
    elif type(expected) is list:
        c.ok(len(value) == len(expected), f"{label} length")
        for index, item in enumerate(expected):
            exact_tree(c, value[index], item, f"{label}[{index}]")
    else:
        c.ok(value == expected, f"{label} value")


def frac(c: Checks, value: Any, label: str) -> Fraction:
    typ(c, value, str, label)
    try:
        result = Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise AssertionError(f"{label} rational") from error
    c.ok(str(result) == value, f"{label} canonical")
    return result


def string_list(value: Any, label: str) -> list[str]:
    require(value, list, label)
    for i, item in enumerate(value):
        require(item, str, f"{label}[{i}]")
    return value


def int_list(value: Any, label: str) -> list[int]:
    require(value, list, label)
    for i, item in enumerate(value):
        require(item, int, f"{label}[{i}]")
    return value


def canonical(m: list[Fraction], x: list[Fraction], v: list[Fraction]) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for i, (mi, xi, vi) in enumerate(zip(m, x, v)):
        if mi <= 0 or (i and xi < x[i - 1]):
            raise AssertionError("invalid frozen input")
        if out and out[-1]["x"] == xi:
            out[-1]["raw"].append(i)
            out[-1]["m"] += mi
            out[-1]["p"] += mi * vi
        else:
            out.append({"raw": [i], "m": mi, "x": xi, "p": mi * vi})
    for row in out:
        row["v"] = row["p"] / row["m"]
    return out


def exhaustive_partition(initial: list[dict[str, Any]], t: Fraction) -> list[dict[str, Any]]:
    """Enumerate every contiguous partition and minimize weighted square error."""
    n = len(initial)
    y = [row["x"] + t * row["v"] for row in initial]
    best_cost: Fraction | None = None
    best: list[dict[str, Any]] | None = None
    for mask in range(1 << max(0, n - 1)):
        cuts = [0] + [i + 1 for i in range(n - 1) if mask & (1 << i)] + [n]
        blocks = []
        feasible = True
        cost = Fraction(0)
        for a, b in zip(cuts, cuts[1:]):
            mass = sum(initial[i]["m"] for i in range(a, b))
            mean = sum(initial[i]["m"] * y[i] for i in range(a, b)) / mass
            velocity = sum(initial[i]["m"] * initial[i]["v"] for i in range(a, b)) / mass
            if blocks and blocks[-1]["position"] > mean:
                feasible = False
                break
            cost += sum(initial[i]["m"] * (y[i] - mean) ** 2 for i in range(a, b))
            blocks.append({"members": list(range(a, b)), "mass": mass, "position": mean, "velocity": velocity})
        if feasible and (best_cost is None or cost < best_cost):
            best_cost, best = cost, blocks
    assert best is not None
    merged: list[dict[str, Any]] = []
    for block in best:
        if merged and merged[-1]["position"] == block["position"]:
            left = merged.pop()
            mass = left["mass"] + block["mass"]
            merged.append({
                "members": left["members"] + block["members"], "mass": mass,
                "position": block["position"],
                "velocity": (left["mass"] * left["velocity"] + block["mass"] * block["velocity"]) / mass,
            })
        else:
            merged.append(block)
    return merged


def candidate_times(initial: list[dict[str, Any]]) -> list[Fraction]:
    out: set[Fraction] = set()
    n = len(initial)
    for a in range(n):
        for b in range(a + 1, n):
            for d in range(b + 1, n + 1):
                ml = sum(initial[i]["m"] for i in range(a, b))
                mr = sum(initial[i]["m"] for i in range(b, d))
                xl = sum(initial[i]["m"] * initial[i]["x"] for i in range(a, b)) / ml
                xr = sum(initial[i]["m"] * initial[i]["x"] for i in range(b, d)) / mr
                vl = sum(initial[i]["m"] * initial[i]["v"] for i in range(a, b)) / ml
                vr = sum(initial[i]["m"] * initial[i]["v"] for i in range(b, d)) / mr
                if vl > vr:
                    t = (xr - xl) / (vl - vr)
                    if t > 0:
                        out.add(t)
    return sorted(out)


def reconstructed_events(initial: list[dict[str, Any]]) -> list[dict[str, Any]]:
    candidates = candidate_times(initial)
    events = []
    previous_count = len(initial)
    event_index = 0
    for j, t in enumerate(candidates):
        left_gap = t - (candidates[j - 1] if j else Fraction(0))
        right_gap = (candidates[j + 1] - t) if j + 1 < len(candidates) else max(Fraction(1), t)
        epsilon = min(left_gap, right_gap) / 3
        before = exhaustive_partition(initial, t - epsilon)
        after = exhaustive_partition(initial, t + epsilon)
        if len(after) >= len(before):
            continue
        groups = []
        for block in after:
            incoming = [old for old in before if set(old["members"]).issubset(block["members"])]
            if len(incoming) < 2:
                continue
            mass = sum(old["mass"] for old in incoming)
            momentum = sum(old["mass"] * old["velocity"] for old in incoming)
            energy_before = sum(old["mass"] * old["velocity"] ** 2 / 2 for old in incoming)
            energy_after = momentum ** 2 / (2 * mass)
            groups.append({
                "members": block["members"], "incoming_cluster_count": len(incoming),
                "incoming_masses": [str(old["mass"]) for old in incoming],
                "incoming_velocities": [str(old["velocity"]) for old in incoming],
                "mass": str(mass), "momentum": str(momentum),
                "outgoing_velocity": str(momentum / mass),
                "energy_before": str(energy_before), "energy_after": str(energy_after),
                "energy_loss": str(energy_before - energy_after),
            })
        if groups:
            event_index += 1
            events.append({
                "event_index": event_index, "time": str(t), "position_count": len(groups),
                "cluster_count_before": len(before), "cluster_count_after": len(after),
                "groups": groups,
                "total_energy_loss": str(sum(Fraction(g["energy_loss"]) for g in groups)),
            })
            previous_count = len(after)
    if events:
        assert events[-1]["cluster_count_after"] == previous_count
    return events


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    data = strict_load(args.input)
    c = Checks()
    evaluation = strict_yaml_load(args.evaluation)
    exact_tree(c, evaluation, EVALUATION_EXPECTED, "evaluation")
    c.ok(semantic_hash(evaluation) == EVALUATION_SHA, "evaluation semantic hash")
    keys(c, data, TOP_KEYS, "top")
    typ(c, data["payload_sha256"], str, "payload hash")
    c.ok(re.fullmatch(r"[0-9a-f]{64}", data["payload_sha256"]) is not None, "hash syntax")
    c.ok(data["payload_sha256"] == phash(data), "payload hash")
    for field, expected in (
        ("schema", "hcs-c292-sticky-particle-all-event-v1"), ("candidate_id", "HCS-C292"),
        ("obstruction_id", "HEN-O276"), ("evaluation_date", "2026-09-02"),
        ("source_commit", SOURCE), ("scope_literal", SCOPE),
    ):
        typ(c, data[field], str, field)
        c.ok(data[field] == expected, f"{field} value")
    typ(c, data["fixed_epoch"], int, "epoch")
    c.ok(data["fixed_epoch"] == 1788307200, "epoch value")
    keys(c, data["evaluator"], {"version", "sha256"}, "evaluator")
    require(data["evaluator"]["version"], str, "evaluator version")
    require(data["evaluator"]["sha256"], str, "evaluator hash")
    c.ok(data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR}, "evaluator value")
    for label, value, expected in (("model", data["model"], MODEL), ("theorem", data["theorem_contract"], THEOREM), ("proof", data["proof_contract"], PROOF)):
        keys(c, value, set(expected), label)
        for key, item in value.items():
            require(item, str, f"{label}.{key}")
        c.ok(value == expected, f"{label} contract")
    keys(c, data["route_a"], set(ROUTE), "route")
    string_list(data["route_a"]["tuple"], "route tuple")
    require(data["route_a"]["overall"], str, "route overall")
    require(data["route_a"]["route_b_invocation_allowed"], bool, "route B")
    c.ok(data["route_a"] == ROUTE, "route value")
    keys(c, data["scope_flags"], set(FLAGS), "flags")
    for key, value in data["scope_flags"].items():
        require(value, bool, f"flag {key}")
    c.ok(data["scope_flags"] == FLAGS, "flag values")
    keys(c, data["enumeration"], ENUM_KEYS, "enumeration")
    for key, value in data["enumeration"].items():
        require(value, int, f"enumeration {key}")

    require(data["scenarios"], list, "scenarios")
    require(data["premerge_cells"], list, "premerge cells")
    require(data["event_cells"], list, "event cells")
    require(data["projection_cells"], list, "projection cells")
    require(data["conservation_cells"], list, "conservation cells")
    require(data["weak_balance_cells"], list, "weak cells")
    scenario_ids: set[str] = set()
    expected_pre = []
    expected_events: dict[str, list[dict[str, Any]]] = {}
    expected_proj = []
    expected_cons = []
    expected_weak = []
    total_raw = total_canonical = 0
    for si, row in enumerate(data["scenarios"]):
        keys(c, row, SCENARIO_KEYS, f"scenario {si}")
        require(row["id"], str, "scenario id")
        c.ok(row["id"] not in scenario_ids, "unique scenario")
        scenario_ids.add(row["id"])
        masses = [frac(c, z, f"scenario {si} mass") for z in string_list(row["raw_masses"], "raw masses")]
        positions = [frac(c, z, f"scenario {si} position") for z in string_list(row["raw_positions"], "raw positions")]
        velocities = [frac(c, z, f"scenario {si} velocity") for z in string_list(row["raw_velocities"], "raw velocities")]
        times = [frac(c, z, f"scenario {si} time") for z in string_list(row["query_times"], "query times")]
        require(row["raw_particle_count"], int, "raw count")
        require(row["canonical_particle_count"], int, "canonical count")
        c.ok(len(masses) == len(positions) == len(velocities) == row["raw_particle_count"], "raw array lengths")
        c.ok(all(m > 0 for m in masses), "positive masses")
        c.ok(all(a <= b for a, b in zip(positions, positions[1:])), "ordered positions")
        c.ok(times == sorted(set(times)) and times[0] == 0, "ordered unique query times")
        initial = canonical(masses, positions, velocities)
        c.ok(len(initial) == row["canonical_particle_count"], "canonical count")
        total_raw += len(masses)
        total_canonical += len(initial)
        for i, item in enumerate(initial):
            expected_pre.append({"scenario": row["id"], "canonical_index": i, "raw_members": item["raw"], "mass": str(item["m"]), "position": str(item["x"]), "momentum": str(item["p"]), "velocity": str(item["v"])})
        events = reconstructed_events(initial)
        expected_events[row["id"]] = events
        for event in events:
            for gi, group in enumerate(event["groups"]):
                expected_weak.append({"scenario": row["id"], "event_index": event["event_index"], "group_index": gi, "mass_jump": "0", "momentum_jump": "0", "energy_entropy_defect": str(-Fraction(group["energy_loss"]))})
        for t in times:
            blocks = exhaustive_partition(initial, t)
            for block in blocks:
                for i in block["members"]:
                    expected_proj.append({"scenario": row["id"], "time": str(t), "canonical_index": i, "cluster_members": block["members"], "position": str(block["position"]), "velocity": str(block["velocity"])})
        total_mass = sum(item["m"] for item in initial)
        total_momentum = sum(item["p"] for item in initial)
        first_moment = sum(item["m"] * item["x"] for item in initial)
        initial_energy = sum(item["m"] * item["v"] ** 2 / 2 for item in initial)
        loss = sum(Fraction(event["total_energy_loss"]) for event in events)
        expected_cons.append({
            "scenario": row["id"], "total_mass": str(total_mass), "total_momentum": str(total_momentum),
            "initial_first_moment": str(first_moment), "center_velocity": str(total_momentum / total_mass),
            "initial_energy": str(initial_energy), "final_energy": str(initial_energy - loss),
            "total_energy_loss": str(loss),
            "merger_count": sum(event["cluster_count_before"] - event["cluster_count_after"] for event in events),
            "event_time_count": len(events),
        })

    for i, row in enumerate(data["premerge_cells"]):
        keys(c, row, PRE_KEYS, f"premerge {i}")
        require(row["scenario"], str, "pre scenario"); require(row["canonical_index"], int, "pre index")
        int_list(row["raw_members"], "raw members")
        for field in ("mass", "position", "momentum", "velocity"): frac(c, row[field], f"pre {field}")
    c.ok(data["premerge_cells"] == expected_pre, "all premerge cells")
    c.ok(len({(r["scenario"], r["canonical_index"]) for r in data["premerge_cells"]}) == len(data["premerge_cells"]), "unique premerge grid")

    flat_expected_events = []
    for scenario in data["scenarios"]:
        for row in expected_events[scenario["id"]]:
            flat_expected_events.append({"scenario": scenario["id"], **row})
    for i, row in enumerate(data["event_cells"]):
        keys(c, row, EVENT_KEYS, f"event {i}")
        require(row["scenario"], str, "event scenario")
        for field in ("event_index", "position_count", "cluster_count_before", "cluster_count_after"): require(row[field], int, f"event {field}")
        frac(c, row["time"], "event time"); frac(c, row["total_energy_loss"], "event total loss")
        require(row["groups"], list, "event groups")
        for j, group in enumerate(row["groups"]):
            keys(c, group, GROUP_KEYS, f"event group {i}.{j}")
            int_list(group["members"], "group members")
            require(group["incoming_cluster_count"], int, "incoming count")
            for field in ("incoming_masses", "incoming_velocities"):
                for z in string_list(group[field], field): frac(c, z, field)
            for field in ("mass", "momentum", "outgoing_velocity", "energy_before", "energy_after", "energy_loss"): frac(c, group[field], f"group {field}")
            masses = [Fraction(z) for z in group["incoming_masses"]]
            velocities = [Fraction(z) for z in group["incoming_velocities"]]
            pair_loss = sum(masses[a] * masses[b] * (velocities[a] - velocities[b]) ** 2 for a in range(len(masses)) for b in range(a + 1, len(masses))) / sum(masses)
            c.ok(Fraction(group["energy_loss"]) == pair_loss / 2, "pairwise energy loss")
    c.ok(data["event_cells"] == flat_expected_events, "all independently reconstructed events")
    c.ok(len({(r["scenario"], r["event_index"]) for r in data["event_cells"]}) == len(data["event_cells"]), "unique event grid")

    for i, row in enumerate(data["projection_cells"]):
        keys(c, row, PROJ_KEYS, f"projection {i}")
        require(row["scenario"], str, "projection scenario"); require(row["canonical_index"], int, "projection index")
        int_list(row["cluster_members"], "cluster members")
        for field in ("time", "position", "velocity"): frac(c, row[field], f"projection {field}")
    c.ok(data["projection_cells"] == expected_proj, "all exhaustive isotonic cells")
    c.ok(len({(r["scenario"], r["time"], r["canonical_index"]) for r in data["projection_cells"]}) == len(data["projection_cells"]), "unique projection grid")

    for i, row in enumerate(data["conservation_cells"]):
        keys(c, row, CONS_KEYS, f"conservation {i}")
        require(row["scenario"], str, "conservation scenario")
        require(row["merger_count"], int, "merger count"); require(row["event_time_count"], int, "event time count")
        for field in CONS_KEYS - {"scenario", "merger_count", "event_time_count"}: frac(c, row[field], f"conservation {field}")
        c.ok(row["merger_count"] <= next(s["canonical_particle_count"] for s in data["scenarios"] if s["id"] == row["scenario"]) - 1, "N-1 merger bound")
    c.ok(data["conservation_cells"] == expected_cons, "all conservation cells")
    c.ok(len({r["scenario"] for r in data["conservation_cells"]}) == len(data["conservation_cells"]), "unique conservation grid")

    for i, row in enumerate(data["weak_balance_cells"]):
        keys(c, row, WEAK_KEYS, f"weak {i}")
        require(row["scenario"], str, "weak scenario"); require(row["event_index"], int, "weak event"); require(row["group_index"], int, "weak group")
        for field in ("mass_jump", "momentum_jump", "energy_entropy_defect"): frac(c, row[field], f"weak {field}")
        c.ok(Fraction(row["mass_jump"]) == Fraction(row["momentum_jump"]) == 0, "weak conservation residues")
        c.ok(Fraction(row["energy_entropy_defect"]) <= 0, "entropy sign")
    c.ok(data["weak_balance_cells"] == expected_weak, "all weak balance cells")
    c.ok(len({(r["scenario"], r["event_index"], r["group_index"]) for r in data["weak_balance_cells"]}) == len(data["weak_balance_cells"]), "unique weak grid")

    expected_enum = {
        "scenario_count": len(data["scenarios"]), "raw_particle_count": total_raw,
        "canonical_particle_count": total_canonical, "premerge_cells": len(expected_pre),
        "event_time_cells": len(flat_expected_events),
        "event_group_cells": sum(len(r["groups"]) for r in flat_expected_events),
        "projection_cells": len(expected_proj), "conservation_cells": len(expected_cons),
        "weak_balance_cells": len(expected_weak),
    }
    c.ok(data["enumeration"] == expected_enum, "enumeration value")

    require(data["references"], list, "references")
    c.ok(len(data["references"]) == 3, "reference count")
    for i, row in enumerate(data["references"]):
        keys(c, row, REF_KEYS, f"reference {i}")
        for key, value in row.items(): require(value, str, f"reference {i}.{key}")
    c.ok([r["identifier"] for r in data["references"]] == ["arXiv:0902.4373", "arXiv:1201.2350", "10.1137/19M1241775"], "reference identities")
    require(data["nonclaims"], list, "nonclaims")
    string_list(data["nonclaims"], "nonclaims")
    c.ok(len(data["nonclaims"]) == 3, "nonclaim count")
    print(
        f"C292 independent exhaustive-isotonic checker: PASS ({c.n} assertions; "
        f"strict duplicate-rejecting JSON/YAML schemas; evaluation-semantic-sha256={EVALUATION_SHA})"
    )


if __name__ == "__main__":
    main()
