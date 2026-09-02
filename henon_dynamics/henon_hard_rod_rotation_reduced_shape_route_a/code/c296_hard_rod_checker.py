#!/usr/bin/env python3
"""Strict producer-independent checker for HCS-C296.

The checker imports no producer code.  It independently reconstructs pair
coincidences, simultaneous blocks, quotient signatures, stabilizers, and
return witnesses from the frozen scenario table.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import re
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c296_hard_rod_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C296/2026-09-02.yaml"
SOURCE = "f8d3ad9a8940b54e82854b2924be353575ed8fcb"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVALUATION_SHA = "5e0c4609143ece03f46cab5822ba104af41b2513698dba999f8d4bf86b6e8ed1"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
OBSTRUCTION = "HEN-O280"

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
ROUTE = {"tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
FLAGS = {
    "arithmetic_local_data": False, "euler_factors": False, "root_numbers": False,
    "automorphy": False, "target_divisor_or_counting_law": False,
    "target_functional_equation": False, "target_zero_match": False,
    "hilbert_polya_operator": False, "route_b_input": False,
}
BOUNDARIES = [
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
REFERENCES = [
    {
        "authors": "D. W. Jepsen",
        "id": "Jepsen1965",
        "identifier": "10.1063/1.1704288",
        "ownership": "direct classical owner for equal-mass hard-rod dynamics, free crossing, and Poincare cycles",
        "title": "Dynamics of a Simple Many-Body System of Hard Rods",
        "url": "https://doi.org/10.1063/1.1704288",
        "venue": "Journal of Mathematical Physics 6(3) (1965), 405-413",
    },
    {
        "authors": "Lewi Tonks",
        "id": "Tonks1936",
        "identifier": "10.1103/PhysRev.50.955",
        "ownership": "classical owner for the one-dimensional finite-length hard-rod model and excluded-volume reduction",
        "title": "The Complete Equation of State of One, Two and Three-Dimensional Gases of Hard Elastic Spheres",
        "url": "https://doi.org/10.1103/PhysRev.50.955",
        "venue": "Physical Review 50 (1936), 955-963",
    },
]
NONCLAIMS = [
    "the Jepsen hard-rod/free-crossing mechanism and the Tonks excluded-volume coordinate are not claimed as literature originality",
    "the conjugacy is only for the rotation-reduced shape flow; the complete physical rotation angle and its cocycle are not reconstructed",
    "finite rational scenarios are regression evidence and do not prove the all-parameter theorem",
    "the natural hard-core kinetic quantization is an A4 classification only; no spectral correspondence or Hilbert-Polya operator is claimed",
]
FROZEN = [
    ("binary_recurring", 11, 1, [0, 3], [2, -1], 7, [0, 1, 2, 4, 7]),
    ("simultaneous_triple", 15, 1, [0, 4, 8], [2, 0, -2], 5, [0, 1, 2, 3, 5]),
    ("simultaneous_disjoint", 16, 1, [0, 2, 6, 8], [1, -1, 2, 0], 7, [0, 1, 2, 4, 7]),
    ("repeated_symmetric", 16, 1, [0, 3, 6, 9], [1, -1, 1, -1], 6, [0, 1, 3, 6]),
    ("common_drift", 13, 1, [0, 2, 7], [5, 5, 5], 5, [0, 1, 5]),
    ("initial_contact", 12, 1, [0, 0, 4], [-1, 1, 0], 5, [0, 1, 3, 5]),
    ("single_rod", 7, 2, [0], [3], 4, [0, 1, 4]),
]
EVALUATION_EXPECTED = {
    "schema": "route-a-evaluation-v0.2.0", "candidate_id": "HCS-C296",
    "obstruction_id": OBSTRUCTION,
    "evaluation_date": "2026-09-02", "source_commit": SOURCE,
    "fixed_epoch": EPOCH, "scope_literal": SCOPE,
    "evaluator_authority_sha256": EVALUATOR,
    "theorem_status": "PROVABLE AS CORRECTED",
    "tuple": ROUTE["tuple"], "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "axes": {
        "A0": "no arithmetic local-data carrier",
        "A1": "exact reduced periodic-return classification but no prime-like orbit bridge",
        "A2": "no arithmetic clock or target dynamical determinant",
        "A3": "no target analytic structure",
        "A4": "natural hard-core kinetic quantization on the reduced collision chamber",
    },
    "scope_flags": FLAGS,
}
TOP_KEYS = {
    "schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit",
    "fixed_epoch", "scope_literal", "evaluator", "model", "theorem_contract",
    "proof_contract", "route_a", "scope_flags", "enumeration", "scenarios",
    "particle_cells", "pair_crossing_cells", "event_cells", "shape_cells",
    "stabilizer_cells", "return_cells", "symbolic_return_cases",
    "conservation_cells", "boundary_cells", "references", "nonclaims", "payload_sha256",
}
ENUM_KEYS = {
    "scenario_count", "particle_cells", "pair_crossing_cells", "event_time_cells",
    "event_group_cells", "shape_query_cells", "velocity_class_cells", "return_cells",
    "symbolic_return_cells", "conservation_cells", "boundary_cells",
}
SCENARIO_KEYS = {"id", "N", "ell", "a", "L", "horizon", "query_times"}
PARTICLE_KEYS = {"scenario", "index", "y", "velocity"}
PAIR_KEYS = {"scenario", "i", "j", "time"}
EVENT_KEYS = {"scenario", "event_index", "time", "group_count", "groups"}
GROUP_KEYS = {"position", "indices", "incoming_spatial_velocities", "outgoing_spatial_velocities", "momentum_before", "momentum_after", "twice_energy_before", "twice_energy_after"}
SHAPE_KEYS = {"scenario", "time", "gap_signature", "phase_signature"}
STAB_KEYS = {"scenario", "velocity", "multiplicity", "stabilizer_order", "stabilizer_shifts"}
RETURN_KEYS = {"scenario", "status", "weighted_difference_generator", "minimal_period", "witness_time", "witness_common_translation", "witness_permutation"}
SYMBOLIC_KEYS = {"id", "L", "positions", "velocities", "verdict", "proof"}
CONSERVATION_KEYS = {"scenario", "momentum", "twice_kinetic_energy", "pair_event_bound", "aggregated_event_times"}
BOUNDARY_KEYS = {"id", "status"}
REFERENCE_KEYS = {"id", "authors", "title", "venue", "identifier", "url", "ownership"}


class Checks:
    def __init__(self) -> None:
        self.n = 0

    def ok(self, condition: bool, label: str) -> None:
        self.n += 1
        if not condition:
            raise AssertionError(label)


def reject_duplicate_keys(pairs: list[tuple[Any, Any]]) -> dict[Any, Any]:
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def reject_constant(value: str) -> None:
    raise ValueError(f"non-finite JSON constant: {value}")


def strict_load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(), object_pairs_hook=reject_duplicate_keys, parse_constant=reject_constant)
    if type(value) is not dict:
        raise TypeError("evidence top level must be object")
    return value


class UniqueSafeLoader(yaml.SafeLoader):
    """Safe YAML loader with duplicate rejection and timestamps kept as strings."""


UniqueSafeLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def construct_unique_mapping(loader: UniqueSafeLoader, node: yaml.MappingNode, deep: bool = False) -> dict:
    loader.flatten_mapping(node)
    out = {}
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


def payload_hash(data: dict[str, Any]) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return semantic_hash(body)


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


def keys(c: Checks, value: Any, expected: set[str], label: str) -> None:
    c.ok(type(value) is dict, f"{label} object")
    c.ok(set(value) == expected, f"{label} exact keys")


def require_type(c: Checks, value: Any, expected: type, label: str) -> None:
    c.ok(type(value) is expected, f"{label} exact {expected.__name__}")


def frac(c: Checks, value: Any, label: str) -> Fraction:
    require_type(c, value, str, label)
    try:
        result = Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise AssertionError(f"{label} rational") from error
    c.ok(str(result) == value, f"{label} canonical rational")
    return result


def string_list(c: Checks, value: Any, label: str) -> list[str]:
    require_type(c, value, list, label)
    for i, item in enumerate(value):
        require_type(c, item, str, f"{label}[{i}]")
    return value


def int_list(c: Checks, value: Any, label: str) -> list[int]:
    require_type(c, value, list, label)
    for i, item in enumerate(value):
        require_type(c, item, int, f"{label}[{i}]")
    return value


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def residue(value: Fraction, length: Fraction) -> Fraction:
    return value - floor_fraction(value / length) * length


def roots_by_integer_scan(y_i: Fraction, y_j: Fraction, v_i: Fraction, v_j: Fraction, length: Fraction, horizon: Fraction) -> list[Fraction]:
    if v_i == v_j:
        return []
    # A deliberately loose finite range is independent of the producer's
    # endpoint floor/ceiling implementation.
    span = 3 + math.ceil(float((abs(y_i-y_j) + horizon*abs(v_i-v_j)) / length))
    roots = []
    for winding in range(-span, span + 1):
        time = (Fraction(winding) * length - (y_i-y_j)) / (v_i-v_j)
        if 0 <= time <= horizon:
            roots.append(time)
    return sorted(set(roots))


def independent_gap_signature(positions: list[Fraction], length: Fraction) -> list[str]:
    ordered = sorted(residue(z, length) for z in positions)
    gaps = [ordered[i+1]-ordered[i] for i in range(len(ordered)-1)]
    gaps.append(ordered[0]+length-ordered[-1])
    options = [tuple(gaps[(i+j) % len(gaps)] for j in range(len(gaps))) for i in range(len(gaps))]
    return [str(z) for z in min(options)]


def independent_phase_signature(positions: list[Fraction], velocities: list[Fraction], length: Fraction) -> list[str]:
    options = []
    for shift in positions:
        options.append(tuple(sorted((residue(pos-shift, length), vel) for pos, vel in zip(positions, velocities))))
    return [f"{pos}@{vel}" for pos, vel in min(options)]


def translations_fixing(points: list[Fraction], length: Fraction) -> list[Fraction]:
    target = Counter(residue(z, length) for z in points)
    seeds = list(target)
    possibilities = {residue(b-a, length) for a in seeds for b in seeds}
    return sorted(h for h in possibilities if Counter(residue(z+h, length) for z in points) == target)


def gcd_fraction(values: list[Fraction]) -> Fraction:
    values = [abs(z) for z in values if z]
    if not values:
        return Fraction(0)
    common_denominator = 1
    for z in values:
        common_denominator = math.lcm(common_denominator, z.denominator)
    integers = [z.numerator * (common_denominator // z.denominator) for z in values]
    common_numerator = 0
    for z in integers:
        common_numerator = math.gcd(common_numerator, abs(z))
    return Fraction(common_numerator, common_denominator)


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
    require_type(c, data["payload_sha256"], str, "payload hash")
    c.ok(re.fullmatch(r"[0-9a-f]{64}", data["payload_sha256"]) is not None, "payload hash syntax")
    c.ok(data["payload_sha256"] == payload_hash(data), "payload hash value")
    fixed_strings = {
        "schema": "hcs-c296-hard-rod-rotation-reduced-shape-v1", "candidate_id": "HCS-C296",
        "obstruction_id": OBSTRUCTION, "evaluation_date": "2026-09-02",
        "source_commit": SOURCE, "scope_literal": SCOPE,
    }
    for field, expected in fixed_strings.items():
        require_type(c, data[field], str, field)
        c.ok(data[field] == expected, f"{field} value")
    require_type(c, data["fixed_epoch"], int, "fixed epoch")
    c.ok(data["fixed_epoch"] == EPOCH, "fixed epoch value")
    exact_tree(c, data["evaluator"], {"version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    exact_tree(c, data["model"], MODEL, "model")
    exact_tree(c, data["theorem_contract"], THEOREM, "theorem")
    exact_tree(c, data["proof_contract"], PROOF, "proof")
    exact_tree(c, data["route_a"], ROUTE, "route")
    exact_tree(c, data["scope_flags"], FLAGS, "scope flags")
    keys(c, data["enumeration"], ENUM_KEYS, "enumeration")
    for field, value in data["enumeration"].items():
        require_type(c, value, int, f"enumeration.{field}")

    require_type(c, data["scenarios"], list, "scenarios")
    require_type(c, data["particle_cells"], list, "particle cells")
    expected_scenarios = []
    expected_particles = []
    frozen_by_id = {}
    for identifier, ell0, a0, y0, v0, horizon0, queries0 in FROZEN:
        n = len(y0); length = Fraction(ell0 - n*a0)
        expected_scenarios.append({
            "id": identifier, "N": n, "ell": str(ell0), "a": str(a0), "L": str(length),
            "horizon": str(horizon0), "query_times": [str(Fraction(t)) for t in queries0],
        })
        ys = [residue(Fraction(z), length) for z in y0]
        vs = [Fraction(z) for z in v0]
        frozen_by_id[identifier] = (Fraction(ell0), Fraction(a0), length, ys, vs, Fraction(horizon0), [Fraction(t) for t in queries0])
        for index, (pos, vel) in enumerate(zip(ys, vs)):
            expected_particles.append({"scenario": identifier, "index": index, "y": str(pos), "velocity": str(vel)})
    for i, row in enumerate(data["scenarios"]):
        keys(c, row, SCENARIO_KEYS, f"scenario {i}")
        require_type(c, row["id"], str, "scenario id")
        require_type(c, row["N"], int, "scenario N")
        for field in ("ell", "a", "L", "horizon"):
            frac(c, row[field], f"scenario {i}.{field}")
        string_list(c, row["query_times"], f"scenario {i}.query")
    c.ok(data["scenarios"] == expected_scenarios, "frozen scenario table")
    for i, row in enumerate(data["particle_cells"]):
        keys(c, row, PARTICLE_KEYS, f"particle {i}")
        require_type(c, row["scenario"], str, "particle scenario")
        require_type(c, row["index"], int, "particle index")
        frac(c, row["y"], "particle y"); frac(c, row["velocity"], "particle velocity")
    c.ok(data["particle_cells"] == expected_particles, "all particle cells")
    c.ok(len({(r["scenario"], r["index"]) for r in data["particle_cells"]}) == len(data["particle_cells"]), "unique particle grid")

    expected_pairs = []
    expected_events = []
    expected_shapes = []
    expected_stabilizers = []
    expected_returns = []
    expected_conservation = []
    for scenario in expected_scenarios:
        identifier = scenario["id"]
        _ell, _a, length, ys, vs, horizon, queries = frozen_by_id[identifier]
        roots = set()
        for i, j in itertools.combinations(range(len(ys)), 2):
            times = roots_by_integer_scan(ys[i], ys[j], vs[i], vs[j], length, horizon)
            c.ok(len(times) <= math.floor(float(horizon*abs(vs[i]-vs[j])/length)) + 2, f"compact pair bound {identifier} {i} {j}")
            for time in times:
                expected_pairs.append({"scenario": identifier, "i": i, "j": j, "time": str(time)})
                roots.add(time)
        for event_index, time in enumerate(sorted(roots), 1):
            positions = [residue(y+time*v, length) for y, v in zip(ys, vs)]
            at_position: dict[Fraction, list[int]] = defaultdict(list)
            for index, pos in enumerate(positions):
                at_position[pos].append(index)
            groups = []
            for pos, indices in sorted(at_position.items()):
                incoming = [vs[i] for i in indices]
                if len(indices) >= 2 and len(set(incoming)) >= 2:
                    groups.append({
                        "position": str(pos), "indices": indices,
                        "incoming_spatial_velocities": [str(z) for z in sorted(incoming, reverse=True)],
                        "outgoing_spatial_velocities": [str(z) for z in sorted(incoming)],
                        "momentum_before": str(sum(incoming)), "momentum_after": str(sum(incoming)),
                        "twice_energy_before": str(sum(z*z for z in incoming)),
                        "twice_energy_after": str(sum(z*z for z in incoming)),
                    })
            if groups:
                expected_events.append({"scenario": identifier, "event_index": event_index, "time": str(time), "group_count": len(groups), "groups": groups})
        for time in queries:
            positions = [residue(y+time*v, length) for y, v in zip(ys, vs)]
            expected_shapes.append({
                "scenario": identifier, "time": str(time),
                "gap_signature": independent_gap_signature(positions, length),
                "phase_signature": independent_phase_signature(positions, vs, length),
            })
        classes: dict[Fraction, list[Fraction]] = defaultdict(list)
        for pos, vel in zip(ys, vs):
            classes[vel].append(pos)
        stabilizers = {}
        for vel in sorted(classes):
            shifts = translations_fixing(classes[vel], length)
            stabilizers[vel] = shifts
            expected_stabilizers.append({
                "scenario": identifier, "velocity": str(vel), "multiplicity": len(classes[vel]),
                "stabilizer_order": len(shifts), "stabilizer_shifts": [str(z) for z in shifts],
            })
            c.ok(shifts == [Fraction(k)*length/len(shifts) for k in range(len(shifts))], f"cyclic H_d {identifier} {vel}")
            c.ok(len(shifts) <= len(classes[vel]) and len(classes[vel]) % len(shifts) == 0, f"stabilizer divides multiplicity {identifier}")
        velocities = sorted(classes)
        weighted = [Fraction(math.lcm(len(stabilizers[u]), len(stabilizers[w]))) * (u-w) for u, w in itertools.combinations(velocities, 2)]
        generator = gcd_fraction(weighted)
        fixed = len(velocities) == 1
        witness_time = Fraction(1) if fixed else length/generator
        cosets = [{residue(witness_time*u-h, length) for h in stabilizers[u]} for u in velocities]
        intersection = set.intersection(*cosets)
        c.ok(bool(intersection), f"CRT intersection {identifier}")
        common = min(intersection)
        permutation = [-1]*len(ys)
        for u in velocities:
            available: dict[Fraction, list[int]] = defaultdict(list)
            for j, (pos, vel) in enumerate(zip(ys, vs)):
                if vel == u:
                    available[residue(pos+common, length)].append(j)
            for i, (pos, vel) in enumerate(zip(ys, vs)):
                if vel == u:
                    permutation[i] = available[residue(pos+witness_time*u, length)].pop(0)
        expected_returns.append({
            "scenario": identifier, "status": "FIXED_SHAPE" if fixed else "PERIODIC_NONFIXED",
            "weighted_difference_generator": str(generator),
            "minimal_period": "NO_LEAST_POSITIVE_PERIOD" if fixed else str(length/generator),
            "witness_time": str(witness_time), "witness_common_translation": str(common),
            "witness_permutation": permutation,
        })
        if generator:
            integer_weights = [z/generator for z in weighted if z]
            c.ok(all(z.denominator == 1 for z in integer_weights), f"integer normalized differences {identifier}")
            c.ok(math.gcd(*(abs(z.numerator) for z in integer_weights)) == 1, f"primitive difference generator {identifier}")
        scenario_pair_count = sum(r["scenario"] == identifier for r in expected_pairs)
        scenario_event_count = sum(r["scenario"] == identifier for r in expected_events)
        expected_conservation.append({
            "scenario": identifier, "momentum": str(sum(vs)),
            "twice_kinetic_energy": str(sum(z*z for z in vs)),
            "pair_event_bound": scenario_pair_count, "aggregated_event_times": scenario_event_count,
        })

    for i, row in enumerate(data["pair_crossing_cells"]):
        keys(c, row, PAIR_KEYS, f"pair {i}")
        require_type(c, row["scenario"], str, "pair scenario")
        require_type(c, row["i"], int, "pair i"); require_type(c, row["j"], int, "pair j")
        frac(c, row["time"], "pair time")
    c.ok(data["pair_crossing_cells"] == expected_pairs, "all pair crossing cells")
    c.ok(len({(r["scenario"], r["i"], r["j"], r["time"]) for r in data["pair_crossing_cells"]}) == len(data["pair_crossing_cells"]), "unique pair crossings")
    for i, row in enumerate(data["event_cells"]):
        keys(c, row, EVENT_KEYS, f"event {i}")
        require_type(c, row["scenario"], str, "event scenario")
        require_type(c, row["event_index"], int, "event index"); require_type(c, row["group_count"], int, "group count")
        frac(c, row["time"], "event time"); require_type(c, row["groups"], list, "event groups")
        c.ok(row["group_count"] == len(row["groups"]), "event group count")
        for j, group in enumerate(row["groups"]):
            keys(c, group, GROUP_KEYS, f"group {i}.{j}")
            frac(c, group["position"], "group position")
            int_list(c, group["indices"], "group indices")
            incoming = [frac(c, z, "incoming velocity") for z in string_list(c, group["incoming_spatial_velocities"], "incoming velocities")]
            outgoing = [frac(c, z, "outgoing velocity") for z in string_list(c, group["outgoing_spatial_velocities"], "outgoing velocities")]
            c.ok(incoming == sorted(incoming, reverse=True), "incoming spatial order")
            c.ok(outgoing == sorted(outgoing), "outgoing spatial order")
            c.ok(Counter(incoming) == Counter(outgoing), "velocity multiset conserved")
            for field in ("momentum_before", "momentum_after", "twice_energy_before", "twice_energy_after"):
                frac(c, group[field], f"group {field}")
            c.ok(group["momentum_before"] == group["momentum_after"], "event momentum")
            c.ok(group["twice_energy_before"] == group["twice_energy_after"], "event energy")
    c.ok(data["event_cells"] == expected_events, "all simultaneous event cells")
    c.ok(len({(r["scenario"], r["time"]) for r in data["event_cells"]}) == len(data["event_cells"]), "unique event-time grid")
    for i, row in enumerate(data["shape_cells"]):
        keys(c, row, SHAPE_KEYS, f"shape {i}")
        require_type(c, row["scenario"], str, "shape scenario"); frac(c, row["time"], "shape time")
        for z in string_list(c, row["gap_signature"], "gap signature"): frac(c, z, "gap")
        string_list(c, row["phase_signature"], "phase signature")
    c.ok(data["shape_cells"] == expected_shapes, "all quotient shape signatures")
    c.ok(len({(r["scenario"], r["time"]) for r in data["shape_cells"]}) == len(data["shape_cells"]), "unique shape grid")
    for i, row in enumerate(data["stabilizer_cells"]):
        keys(c, row, STAB_KEYS, f"stabilizer {i}")
        require_type(c, row["scenario"], str, "stabilizer scenario"); frac(c, row["velocity"], "stabilizer velocity")
        require_type(c, row["multiplicity"], int, "stabilizer multiplicity"); require_type(c, row["stabilizer_order"], int, "stabilizer order")
        for z in string_list(c, row["stabilizer_shifts"], "stabilizer shifts"): frac(c, z, "stabilizer shift")
    c.ok(data["stabilizer_cells"] == expected_stabilizers, "all velocity-class stabilizers")
    c.ok(len({(r["scenario"], r["velocity"]) for r in data["stabilizer_cells"]}) == len(data["stabilizer_cells"]), "unique stabilizer grid")
    for i, row in enumerate(data["return_cells"]):
        keys(c, row, RETURN_KEYS, f"return {i}")
        require_type(c, row["scenario"], str, "return scenario"); require_type(c, row["status"], str, "return status")
        frac(c, row["weighted_difference_generator"], "return generator")
        require_type(c, row["minimal_period"], str, "minimal period")
        frac(c, row["witness_time"], "witness time"); frac(c, row["witness_common_translation"], "witness common translation")
        int_list(c, row["witness_permutation"], "witness permutation")
    c.ok(data["return_cells"] == expected_returns, "all return classifications and witnesses")

    require_type(c, data["symbolic_return_cases"], list, "symbolic return cases")
    c.ok(len(data["symbolic_return_cases"]) == 1, "one symbolic return case")
    symbolic = data["symbolic_return_cases"][0]
    keys(c, symbolic, SYMBOLIC_KEYS, "symbolic case")
    exact_symbolic = {
        "id": "distinct_incommensurable", "L": "10", "positions": ["0", "1", "4"],
        "velocities": ["0", "1", "sqrt(2)"], "verdict": "NO_POSITIVE_RETURN",
        "proof": "a return would make T/10 and sqrt(2)*T/10 integers, forcing sqrt(2) rational",
    }
    exact_tree(c, symbolic, exact_symbolic, "symbolic case exact")

    for i, row in enumerate(data["conservation_cells"]):
        keys(c, row, CONSERVATION_KEYS, f"conservation {i}")
        require_type(c, row["scenario"], str, "conservation scenario")
        frac(c, row["momentum"], "conservation momentum"); frac(c, row["twice_kinetic_energy"], "conservation energy")
        require_type(c, row["pair_event_bound"], int, "pair event bound"); require_type(c, row["aggregated_event_times"], int, "event count")
        c.ok(row["aggregated_event_times"] <= row["pair_event_bound"], "aggregated event count bounded")
    c.ok(data["conservation_cells"] == expected_conservation, "all conservation and no-Zeno counts")
    c.ok(len({r["scenario"] for r in data["conservation_cells"]}) == len(data["conservation_cells"]), "unique conservation grid")

    require_type(c, data["boundary_cells"], list, "boundary cells")
    c.ok(len(data["boundary_cells"]) == 9, "boundary count")
    expected_boundary_ids = ["single_rod_reduced", "common_velocity", "unreduced_counterexample", "cyclic_start", "close_packing", "zero_length_limit", "contact_faces", "persistent_contact", "time_reversal"]
    for i, row in enumerate(data["boundary_cells"]):
        keys(c, row, BOUNDARY_KEYS, f"boundary {i}")
        require_type(c, row["id"], str, "boundary id"); require_type(c, row["status"], str, "boundary status")
    c.ok([r["id"] for r in data["boundary_cells"]] == expected_boundary_ids, "boundary identities")
    c.ok("ell/abs(v), not L/abs(v)" in data["boundary_cells"][2]["status"], "N=1 topology counterexample")
    exact_tree(c, data["boundary_cells"], BOUNDARIES, "canonical boundaries")

    expected_enum = {
        "scenario_count": len(expected_scenarios), "particle_cells": len(expected_particles),
        "pair_crossing_cells": len(expected_pairs), "event_time_cells": len(expected_events),
        "event_group_cells": sum(len(r["groups"]) for r in expected_events),
        "shape_query_cells": len(expected_shapes), "velocity_class_cells": len(expected_stabilizers),
        "return_cells": len(expected_returns), "symbolic_return_cells": 1,
        "conservation_cells": len(expected_conservation), "boundary_cells": len(data["boundary_cells"]),
    }
    c.ok(data["enumeration"] == expected_enum, "enumeration value")

    require_type(c, data["references"], list, "references")
    c.ok(len(data["references"]) == 2, "reference count")
    for i, row in enumerate(data["references"]):
        keys(c, row, REFERENCE_KEYS, f"reference {i}")
        for field, value in row.items(): require_type(c, value, str, f"reference {i}.{field}")
    c.ok([r["identifier"] for r in data["references"]] == ["10.1063/1.1704288", "10.1103/PhysRev.50.955"], "verified reference identifiers")
    exact_tree(c, data["references"], REFERENCES, "canonical references")
    exact_tree(c, data["nonclaims"], NONCLAIMS, "canonical nonclaims")

    print(
        f"C296 independent quotient/event checker: PASS ({c.n} assertions; "
        f"strict duplicate-rejecting JSON/YAML schemas; evaluation-semantic-sha256={EVALUATION_SHA})"
    )


if __name__ == "__main__":
    main()
