#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C279.

The implementation follows the block-coalescence description of the
unweighted path-graph total-variation flow.  All dynamics use Fraction; no
floating-point comparison enters the event ledger.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "results/c279_path_tv_evidence.json"
SOURCE = "51fb3d46f96b854314811c1ad62d3103cd5d54e5"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788220800
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


MODEL = {
    "graph": "unweighted path P_n on vertices 1,...,n, n>=1",
    "incidence": "(Dx)_i=x_{i+1}-x_i for i=1,...,n-1",
    "energy": "J(x)=sum_{i=1}^{n-1}|x_{i+1}-x_i|",
    "flow": "x'(t) in -partial J(x(t)), x(0)=x^0 in R^n",
    "clock": "maximal-monotone semigroup time t>=0",
    "rof": "R_t(x^0)=argmin_y (1/2)||y-x^0||_2^2+t J(y)",
}

THEOREM_CONTRACT = {
    "wellposedness": "for every n>=1 and x^0 in R^n there is one unique global absolutely continuous gradient-flow solution",
    "block_velocity": "a maximal constant block B=[l,r] has velocity (s_r-s_{l-1})/|B|, with exterior jump signs and missing endpoint signs equal to zero",
    "coalescence": "maximal blocks never split; adjacent collisions merge jointly, including simultaneous multi-collisions, so at most n-1 distinct event times occur",
    "consensus": "the mean is preserved and exact consensus is reached in finite time T<=sqrt(n)||x^0-mean(x^0)1||_2",
    "rof_equivalence": "for every t>=0 the flow value equals the unique path ROF minimizer R_t(x^0)",
    "dissipation": "outside event times, d||x-mean(x^0)1||_2^2/(2dt)=-J(x) and dJ(x)/dt=-||x'(t)||_2^2",
    "boundary": "n=1, constant data, endpoint blocks, rational data, and simultaneous mergers are included; no equivalence theorem is asserted for general branched or cyclic graphs",
}

PROOF_CONTRACT = {
    "classification": "PROVABLE AS STATED for every finite unweighted path P_n and every real initial vector",
    "maximal_monotone": "finite convex continuous J has maximal monotone subdifferential and therefore a unique contraction semigroup",
    "minimal_flux": "on each zero-jump block the minimal-norm edge flux linearly interpolates its two exterior signs, giving one common block velocity",
    "no_splitting": "the interpolating flux stays in [-1,1], so an existing plateau is a valid common-velocity facet until it collides and can thereafter only join a larger facet",
    "rof_kkt": "average the flow subgradient from 0 to t; final nonzero edges never merged and retain their sign, while averages on final zero edges remain in [-1,1]",
    "finite_extinction": "one-homogeneity gives r r'=-J and ||x-mean(x)1||_2<=sqrt(n)J, hence r'<=-1/sqrt(n) until consensus",
    "finite_evidence_role": "exact enumeration audits the event algorithm and KKT witnesses but does not replace the all-real analytic proof",
}

ROUTE_A = {
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

NONCLAIMS = [
    "The finite grid is regression evidence and is not a proof for arbitrary real initial data.",
    "The ROF-equals-flow theorem is path-specific; it is not asserted for general branched or cyclic graphs.",
    "The convex semigroup and ROF resolvent are not a primitive-orbit determinant, arithmetic Euler product, or Hilbert-Polya operator.",
]

REFERENCES = [
    {
        "id": "Brezis1973",
        "title": "Operateurs maximaux monotones et semi-groupes de contractions dans les espaces de Hilbert",
        "authors": "Haim Brezis",
        "venue": "North-Holland Mathematics Studies 5, North-Holland, 1973",
        "identifier": "MR0348562",
        "url": "https://mathscinet.ams.org/mathscinet-getitem?mr=0348562",
    },
    {
        "id": "RudinOsherFatemi1992",
        "title": "Nonlinear total variation based noise removal algorithms",
        "authors": "Leonid I. Rudin, Stanley Osher, and Emad Fatemi",
        "venue": "Physica D 60 (1992), 259-268",
        "identifier": "10.1016/0167-2789(92)90242-F",
        "url": "https://doi.org/10.1016/0167-2789(92)90242-F",
    },
    {
        "id": "KirisitsScherzerSetterqvist2019",
        "title": "Invariant phi-Minimal Sets and Total Variation Denoising on Graphs",
        "authors": "Clemens Kirisits, Otmar Scherzer, and Eric Setterqvist",
        "venue": "SIAM Journal on Imaging Sciences 12(4) (2019), 1643-1668",
        "identifier": "10.1137/19M124126X",
        "url": "https://doi.org/10.1137/19M124126X",
    },
    {
        "id": "MazonSoleraToledo2020",
        "title": "The Total Variation Flow in Metric Random Walk Spaces",
        "authors": "Jose M. Mazon, Marcos Solera, and Julian Toledo",
        "venue": "Calculus of Variations and Partial Differential Equations 59 (2020), article 29",
        "identifier": "10.1007/s00526-019-1684-z",
        "url": "https://doi.org/10.1007/s00526-019-1684-z",
    },
]


@dataclass(frozen=True)
class Block:
    lo: int
    hi: int
    value: Fraction

    @property
    def size(self) -> int:
        return self.hi - self.lo + 1


def sign(value: Fraction) -> int:
    return (value > 0) - (value < 0)


def frac(value: Fraction) -> str:
    return str(value)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def blocks_from_values(values: list[Fraction]) -> list[Block]:
    blocks: list[Block] = []
    lo = 0
    for index in range(1, len(values) + 1):
        if index == len(values) or values[index] != values[lo]:
            blocks.append(Block(lo, index - 1, values[lo]))
            lo = index
    return blocks


def expand(blocks: list[Block]) -> list[Fraction]:
    values: list[Fraction] = []
    for block in blocks:
        values.extend([block.value] * block.size)
    return values


def partition(blocks: list[Block]) -> list[list[int]]:
    return [[block.lo + 1, block.hi + 1] for block in blocks]


def total_variation(values: list[Fraction]) -> Fraction:
    return sum((abs(values[i + 1] - values[i]) for i in range(len(values) - 1)), Fraction(0))


def velocities(blocks: list[Block]) -> list[Fraction]:
    result: list[Fraction] = []
    for index, block in enumerate(blocks):
        left = 0 if index == 0 else sign(block.value - blocks[index - 1].value)
        right = 0 if index + 1 == len(blocks) else sign(blocks[index + 1].value - block.value)
        result.append(Fraction(right - left, block.size))
    return result


def coordinate_velocity(blocks: list[Block], block_velocity: list[Fraction]) -> list[Fraction]:
    result: list[Fraction] = []
    for block, speed in zip(blocks, block_velocity):
        result.extend([speed] * block.size)
    return result


def minimal_flux(values: list[Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    """Return edge flux z and g=D^T z of minimal Euclidean norm."""
    n = len(values)
    if n == 1:
        return [], [Fraction(0)]
    blocks = blocks_from_values(values)
    z = [Fraction(0) for _ in range(n - 1)]
    for block_index, block in enumerate(blocks):
        left = 0 if block_index == 0 else sign(block.value - blocks[block_index - 1].value)
        right = 0 if block_index + 1 == len(blocks) else sign(blocks[block_index + 1].value - block.value)
        for edge in range(block.lo, block.hi):
            step = edge - block.lo + 1
            z[edge] = Fraction(left) + Fraction(step, block.size) * (right - left)
        if block.hi < n - 1:
            z[block.hi] = Fraction(right)
    g = [-z[0]]
    g.extend(z[i - 1] - z[i] for i in range(1, n - 1))
    g.append(z[-1])
    return z, g


def rof_kkt(initial: list[Fraction], state: list[Fraction], time: Fraction) -> bool:
    if time == 0:
        return state == initial
    g = [(a - b) / time for a, b in zip(initial, state)]
    if sum(g, Fraction(0)) != 0:
        return False
    z: list[Fraction] = []
    cumulative = Fraction(0)
    for coordinate in g[:-1]:
        cumulative += coordinate
        z.append(-cumulative)
    if g[-1] != (z[-1] if z else 0):
        return False
    for edge, flux in enumerate(z):
        jump = state[edge + 1] - state[edge]
        if jump and flux != sign(jump):
            return False
        if not jump and abs(flux) > 1:
            return False
    return True


def trace(initial: tuple[Fraction, ...]) -> dict:
    values0 = list(initial)
    blocks = blocks_from_values(values0)
    initial_partition = partition(blocks)
    time = Fraction(0)
    events: list[dict] = []
    pair_merges = 0
    mean = sum(values0, Fraction(0)) / len(values0)

    while len(blocks) > 1:
        speeds = velocities(blocks)
        values = expand(blocks)
        coordinate_speeds = coordinate_velocity(blocks, speeds)
        flux, gradient = minimal_flux(values)
        assert all(abs(item) <= 1 for item in flux)
        assert coordinate_speeds == [-item for item in gradient]
        assert sum(values, Fraction(0)) == sum(values0, Fraction(0))
        assert sum(gradient, Fraction(0)) == 0
        assert sum((gradient[i] * values[i] for i in range(len(values))), Fraction(0)) == total_variation(values)
        centred = [item - mean for item in values]
        assert sum((centred[i] * coordinate_speeds[i] for i in range(len(values))), Fraction(0)) == -total_variation(values)
        jump_derivative = sum(
            sign(values[i + 1] - values[i]) * (coordinate_speeds[i + 1] - coordinate_speeds[i])
            for i in range(len(values) - 1)
            if values[i + 1] != values[i]
        )
        assert jump_derivative == -sum((speed * speed for speed in coordinate_speeds), Fraction(0))

        candidates: list[Fraction] = []
        for index in range(len(blocks) - 1):
            denominator = speeds[index] - speeds[index + 1]
            if denominator:
                candidate = (blocks[index + 1].value - blocks[index].value) / denominator
                if candidate > 0:
                    candidates.append(candidate)
        assert candidates
        delta = min(candidates)
        midpoint_state = [value + speed * delta / 2 for value, speed in zip(values, coordinate_speeds)]
        assert rof_kkt(values0, midpoint_state, time + delta / 2)

        advanced = [
            Block(block.lo, block.hi, block.value + speed * delta)
            for block, speed in zip(blocks, speeds)
        ]
        before = len(advanced)
        merged: list[Block] = []
        for block in advanced:
            if merged and merged[-1].value == block.value:
                previous = merged.pop()
                merged.append(Block(previous.lo, block.hi, block.value))
            else:
                merged.append(block)
        merged_count = before - len(merged)
        assert merged_count >= 1
        pair_merges += merged_count
        time += delta
        blocks = merged
        state = expand(blocks)
        assert rof_kkt(values0, state, time)
        events.append({
            "time": frac(time),
            "state": [frac(item) for item in state],
            "partition": partition(blocks),
            "pair_merges": merged_count,
            "energy": frac(total_variation(state)),
        })
        assert len(events) <= len(values0) - 1

    consensus = blocks[0].value
    assert consensus == mean
    radius_squared = sum(((item - mean) ** 2 for item in values0), Fraction(0))
    assert time * time <= len(values0) * radius_squared
    assert pair_merges == len(initial_partition) - 1
    return {
        "initial_partition": initial_partition,
        "events": events,
        "event_times": len(events),
        "pair_merges": pair_merges,
        "consensus_time": frac(time),
        "consensus_value": frac(consensus),
    }


def compact_record(initial: tuple[Fraction, ...], result: dict) -> dict:
    return {
        "input": [frac(item) for item in initial],
        "initial_partition": result["initial_partition"],
        "event_schedule": [
            [event["time"], event["partition"], event["pair_merges"]]
            for event in result["events"]
        ],
        "consensus_time": result["consensus_time"],
        "consensus_value": result["consensus_value"],
    }


def digest_update(hasher: "hashlib._Hash", record: dict) -> None:
    raw = json.dumps(record, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    hasher.update(raw.encode() + b"\n")


def exhaustive_enumeration() -> tuple[list[dict], str, int]:
    alphabet = range(-2, 3)
    digest = hashlib.sha256()
    by_n: list[dict] = []
    raw_total = 0
    for n in range(1, 7):
        input_count = 0
        constant_count = 0
        total_event_times = 0
        total_pair_merges = 0
        simultaneous_event_times = 0
        max_event_times = 0
        max_consensus_time = Fraction(0)
        histogram: dict[int, int] = {}
        for raw in itertools.product(alphabet, repeat=n):
            initial = tuple(Fraction(value) for value in raw)
            result = trace(initial)
            digest_update(digest, compact_record(initial, result))
            input_count += 1
            raw_total += 1
            constant_count += int(result["event_times"] == 0)
            total_event_times += result["event_times"]
            total_pair_merges += result["pair_merges"]
            simultaneous_event_times += sum(event["pair_merges"] > 1 for event in result["events"])
            max_event_times = max(max_event_times, result["event_times"])
            max_consensus_time = max(max_consensus_time, Fraction(result["consensus_time"]))
            histogram[result["event_times"]] = histogram.get(result["event_times"], 0) + 1
        by_n.append({
            "n": n,
            "input_count": input_count,
            "constant_count": constant_count,
            "total_event_times": total_event_times,
            "total_pair_merges": total_pair_merges,
            "simultaneous_event_times": simultaneous_event_times,
            "max_event_times": max_event_times,
            "max_consensus_time": frac(max_consensus_time),
            "event_count_histogram": {str(key): histogram[key] for key in sorted(histogram)},
        })
    return by_n, digest.hexdigest(), raw_total


STRESS_INPUTS = [
    ["-5/3", "2/7", "11/5", "-9/4", "0", "7/6", "-1/8", "13/9"],
    ["0", "0", "5/2", "5/2", "-7/3", "1/9", "1/9", "4", "-2"],
    ["3/5", "-8/7", "2", "-1/3", "11/6", "-5/4", "7/8", "0", "9/10", "-2/11"],
    ["-1", "2", "-1", "2", "-1", "2", "-1", "2", "-1", "2", "-1"],
    ["4/3", "4/3", "-2/5", "-2/5", "7/9", "7/9", "-11/8", "3/2", "3/2", "0", "5/7", "-4/9"],
]

WITNESS_INPUTS = [
    ("singleton", ["3"]),
    ("constant", ["-2", "-2", "-2", "-2"]),
    ("endpoint_facet", ["0", "3", "3"]),
    ("single_simultaneous_merger", ["0", "2", "0"]),
    ("two_simultaneous_mergers", ["0", "2", "0", "2", "0"]),
    ("mixed_plateaus", ["2", "2", "-1", "-1", "3", "0", "0"]),
    ("generic_cascade", ["-2", "2", "1", "-1", "2", "-2"]),
    ("rational_cascade", ["-3/2", "1/3", "1/3", "7/4", "-2/5", "9/8"]),
]


def build() -> dict:
    by_n, grid_digest, raw_total = exhaustive_enumeration()
    stress_digest = hashlib.sha256()
    stress_event_times = 0
    stress_pair_merges = 0
    for raw in STRESS_INPUTS:
        initial = tuple(Fraction(value) for value in raw)
        result = trace(initial)
        digest_update(stress_digest, compact_record(initial, result))
        stress_event_times += result["event_times"]
        stress_pair_merges += result["pair_merges"]

    witnesses = []
    for name, raw in WITNESS_INPUTS:
        initial = tuple(Fraction(value) for value in raw)
        witnesses.append({
            "name": name,
            "input": [frac(value) for value in initial],
            "trace": trace(initial),
        })

    data = {
        "schema": "hcs-c279-path-graph-total-variation-flow-v1",
        "candidate_id": "HCS-C279",
        "evaluation_date": "2026-09-01",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": MODEL,
        "theorem_contract": THEOREM_CONTRACT,
        "proof_contract": PROOF_CONTRACT,
        "enumeration": {
            "arithmetic": "exact fractions only",
            "alphabet": [-2, -1, 0, 1, 2],
            "n_min": 1,
            "n_max": 6,
            "raw_input_count": raw_total,
            "by_n": by_n,
            "trace_sha256": grid_digest,
            "stress_input_count": len(STRESS_INPUTS),
            "stress_dimensions": [len(row) for row in STRESS_INPUTS],
            "stress_event_times": stress_event_times,
            "stress_pair_merges": stress_pair_merges,
            "stress_trace_sha256": stress_digest.hexdigest(),
            "violations": {
                "mass": 0,
                "subgradient_flux": 0,
                "block_split": 0,
                "event_bound": 0,
                "rof_kkt": 0,
                "dissipation": 0,
                "consensus_mean": 0,
                "consensus_time_bound": 0,
            },
        },
        "witnesses": witnesses,
        "references": REFERENCES,
        "route_a": ROUTE_A,
        "scope_flags": SCOPE_FLAGS,
        "nonclaims": NONCLAIMS,
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C279_PRODUCER_PASS",
        "raw_inputs": data["enumeration"]["raw_input_count"],
        "stress_inputs": data["enumeration"]["stress_input_count"],
        "payload_sha256": data["payload_sha256"],
        "trace_sha256": data["enumeration"]["trace_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
