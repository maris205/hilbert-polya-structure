#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C279.

This file deliberately does not import the producer.  Its state engine works
in coordinates: it reconstructs the minimal edge flux on every current
plateau, applies -D^T z, and discovers the next vanishing jump.  The retained
producer instead evolves explicit blocks.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import os
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = Path(os.environ.get(
    "C279_EVIDENCE_PATH", ROOT / "results/c279_path_tv_evidence.json"
))
SOURCE = "51fb3d46f96b854314811c1ad62d3103cd5d54e5"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"

TOP_LEVEL_KEYS = {
    "schema", "candidate_id", "evaluation_date", "source_commit",
    "fixed_epoch", "scope_literal", "evaluator", "model",
    "theorem_contract", "proof_contract", "enumeration", "witnesses",
    "references", "route_a", "scope_flags", "nonclaims", "payload_sha256",
}
ENUMERATION_KEYS = {
    "arithmetic", "alphabet", "n_min", "n_max", "raw_input_count", "by_n",
    "trace_sha256", "stress_input_count", "stress_dimensions",
    "stress_event_times", "stress_pair_merges", "stress_trace_sha256",
    "violations",
}
BY_N_KEYS = {
    "n", "input_count", "constant_count", "total_event_times",
    "total_pair_merges", "simultaneous_event_times", "max_event_times",
    "max_consensus_time", "event_count_histogram",
}
WITNESS_KEYS = {"name", "input", "trace"}
TRACE_KEYS = {
    "initial_partition", "events", "event_times", "pair_merges",
    "consensus_time", "consensus_value",
}
EVENT_KEYS = {"time", "state", "partition", "pair_merges", "energy"}

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
STRESS_INPUTS = [
    ["-5/3", "2/7", "11/5", "-9/4", "0", "7/6", "-1/8", "13/9"],
    ["0", "0", "5/2", "5/2", "-7/3", "1/9", "1/9", "4", "-2"],
    ["3/5", "-8/7", "2", "-1/3", "11/6", "-5/4", "7/8", "0", "9/10", "-2/11"],
    ["-1", "2", "-1", "2", "-1", "2", "-1", "2", "-1", "2", "-1"],
    ["4/3", "4/3", "-2/5", "-2/5", "7/9", "7/9", "-11/8", "3/2", "3/2", "0", "5/7", "-4/9"],
]


def sign(value: Fraction) -> int:
    return (value > 0) - (value < 0)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def runs(values: list[Fraction]) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    lo = 0
    for index in range(1, len(values) + 1):
        if index == len(values) or values[index] != values[lo]:
            result.append((lo, index - 1))
            lo = index
    return result


def encoded_partition(current_runs: list[tuple[int, int]]) -> list[list[int]]:
    return [[lo + 1, hi + 1] for lo, hi in current_runs]


def variation(values: list[Fraction]) -> Fraction:
    return sum((abs(right - left) for left, right in zip(values, values[1:])), Fraction(0))


def flux_gradient(values: list[Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    """Solve the plateau flux interpolation in coordinates, not blocks."""
    n = len(values)
    if n == 1:
        return [], [Fraction(0)]
    z = [Fraction(0) for _ in range(n - 1)]
    current_runs = runs(values)
    for run_index, (lo, hi) in enumerate(current_runs):
        left = 0 if lo == 0 else sign(values[lo] - values[lo - 1])
        right = 0 if hi == n - 1 else sign(values[hi + 1] - values[hi])
        size = hi - lo + 1
        for edge in range(lo, hi):
            z[edge] = Fraction(left) + Fraction(edge - lo + 1, size) * (right - left)
        if hi < n - 1:
            z[hi] = Fraction(right)
    gradient = [-z[0]]
    gradient.extend(z[index - 1] - z[index] for index in range(1, n - 1))
    gradient.append(z[-1])
    return z, gradient


def kkt(initial: list[Fraction], state: list[Fraction], time: Fraction) -> bool:
    if time == 0:
        return initial == state
    gradient = [(left - right) / time for left, right in zip(initial, state)]
    if sum(gradient, Fraction(0)):
        return False
    cumulative = Fraction(0)
    flux: list[Fraction] = []
    for coordinate in gradient[:-1]:
        cumulative += coordinate
        flux.append(-cumulative)
    if gradient[-1] != (flux[-1] if flux else 0):
        return False
    for index, edge_flux in enumerate(flux):
        jump = state[index + 1] - state[index]
        if jump != 0 and edge_flux != sign(jump):
            return False
        if jump == 0 and abs(edge_flux) > 1:
            return False
    return True


def evolve(initial: tuple[Fraction, ...]) -> tuple[dict, int]:
    state = list(initial)
    initial_state = list(initial)
    current_runs = runs(state)
    initial_partition = encoded_partition(current_runs)
    time = Fraction(0)
    events: list[dict] = []
    pair_merges = 0
    local_checks = 0
    mean = sum(state, Fraction(0)) / len(state)

    while len(current_runs) > 1:
        flux, gradient = flux_gradient(state)
        velocity = [-entry for entry in gradient]
        local_checks += 1
        assert all(abs(entry) <= 1 for entry in flux)
        assert sum(gradient, Fraction(0)) == 0
        assert sum((gradient[i] * state[i] for i in range(len(state))), Fraction(0)) == variation(state)
        for lo, hi in current_runs:
            assert len(set(velocity[lo:hi + 1])) == 1
        local_checks += len(current_runs) + 2

        collision_times: list[Fraction] = []
        for left_run, right_run in zip(current_runs, current_runs[1:]):
            edge = left_run[1]
            denominator = velocity[edge] - velocity[edge + 1]
            if denominator:
                candidate = (state[edge + 1] - state[edge]) / denominator
                if candidate > 0:
                    collision_times.append(candidate)
        assert collision_times
        delta = min(collision_times)
        midpoint = [value + delta * speed / 2 for value, speed in zip(state, velocity)]
        assert kkt(initial_state, midpoint, time + delta / 2)
        local_checks += 2

        old_runs = current_runs
        state = [value + delta * speed for value, speed in zip(state, velocity)]
        time += delta
        current_runs = runs(state)
        merged_count = len(old_runs) - len(current_runs)
        assert merged_count >= 1
        for old_lo, old_hi in old_runs:
            assert any(new_lo <= old_lo and old_hi <= new_hi for new_lo, new_hi in current_runs)
        assert sum(state, Fraction(0)) == sum(initial_state, Fraction(0))
        assert kkt(initial_state, state, time)
        local_checks += len(old_runs) + 3
        pair_merges += merged_count
        events.append({
            "time": str(time),
            "state": [str(value) for value in state],
            "partition": encoded_partition(current_runs),
            "pair_merges": merged_count,
            "energy": str(variation(state)),
        })
        assert len(events) <= len(state) - 1

    consensus = state[0]
    radius_squared = sum(((value - mean) ** 2 for value in initial_state), Fraction(0))
    assert consensus == mean
    assert time * time <= len(state) * radius_squared
    assert pair_merges == len(initial_partition) - 1
    local_checks += 3
    return ({
        "initial_partition": initial_partition,
        "events": events,
        "event_times": len(events),
        "pair_merges": pair_merges,
        "consensus_time": str(time),
        "consensus_value": str(consensus),
    }, local_checks)


def compact(initial: tuple[Fraction, ...], result: dict) -> dict:
    return {
        "input": [str(value) for value in initial],
        "initial_partition": result["initial_partition"],
        "event_schedule": [
            [event["time"], event["partition"], event["pair_merges"]]
            for event in result["events"]
        ],
        "consensus_time": result["consensus_time"],
        "consensus_value": result["consensus_value"],
    }


def update_digest(hasher: "hashlib._Hash", record: dict) -> None:
    raw = json.dumps(record, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    hasher.update(raw.encode() + b"\n")


def reconstruct_grid() -> tuple[list[dict], str, int, int]:
    digest = hashlib.sha256()
    by_n: list[dict] = []
    raw_total = 0
    checks = 0
    for n in range(1, 7):
        count = constant_count = total_events = total_merges = simultaneous = max_events = 0
        max_time = Fraction(0)
        histogram: dict[int, int] = {}
        for raw in itertools.product(range(-2, 3), repeat=n):
            initial = tuple(Fraction(value) for value in raw)
            result, local_checks = evolve(initial)
            checks += local_checks
            update_digest(digest, compact(initial, result))
            count += 1
            raw_total += 1
            constant_count += result["event_times"] == 0
            total_events += result["event_times"]
            total_merges += result["pair_merges"]
            simultaneous += sum(event["pair_merges"] > 1 for event in result["events"])
            max_events = max(max_events, result["event_times"])
            max_time = max(max_time, Fraction(result["consensus_time"]))
            histogram[result["event_times"]] = histogram.get(result["event_times"], 0) + 1
        by_n.append({
            "n": n,
            "input_count": count,
            "constant_count": constant_count,
            "total_event_times": total_events,
            "total_pair_merges": total_merges,
            "simultaneous_event_times": simultaneous,
            "max_event_times": max_events,
            "max_consensus_time": str(max_time),
            "event_count_histogram": {str(key): histogram[key] for key in sorted(histogram)},
        })
    return by_n, digest.hexdigest(), raw_total, checks


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    checks = 0

    def ok(condition: bool) -> None:
        nonlocal checks
        assert condition
        checks += 1

    ok(set(data) == TOP_LEVEL_KEYS)
    ok(data["schema"] == "hcs-c279-path-graph-total-variation-flow-v1")
    ok(data["candidate_id"] == "HCS-C279")
    ok(data["evaluation_date"] == "2026-09-01")
    ok(data["source_commit"] == SOURCE)
    ok(data["fixed_epoch"] == 1788220800)
    ok(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    ok(data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR})
    ok(data["payload_sha256"] == payload_hash(data))
    ok(data["model"] == MODEL)
    ok(data["theorem_contract"] == THEOREM_CONTRACT)
    ok(data["proof_contract"] == PROOF_CONTRACT)
    ok(data["route_a"] == ROUTE_A)
    ok(data["scope_flags"] == SCOPE_FLAGS)
    ok(all(value is False for value in data["scope_flags"].values()))
    ok(data["nonclaims"] == NONCLAIMS)
    ok(data["references"] == REFERENCES)
    ok({reference["identifier"] for reference in data["references"]} == {
        "MR0348562", "10.1016/0167-2789(92)90242-F",
        "10.1137/19M124126X", "10.1007/s00526-019-1684-z",
    })

    enumeration = data["enumeration"]
    ok(set(enumeration) == ENUMERATION_KEYS)
    ok(enumeration["arithmetic"] == "exact fractions only")
    ok(enumeration["alphabet"] == [-2, -1, 0, 1, 2])
    ok(enumeration["n_min"] == 1 and enumeration["n_max"] == 6)
    ok(enumeration["raw_input_count"] == sum(5 ** n for n in range(1, 7)))
    ok(enumeration["stress_input_count"] == len(STRESS_INPUTS))
    ok(enumeration["stress_dimensions"] == [len(row) for row in STRESS_INPUTS])
    ok(set(enumeration["violations"]) == {
        "mass", "subgradient_flux", "block_split", "event_bound", "rof_kkt",
        "dissipation", "consensus_mean", "consensus_time_bound",
    })
    ok(all(value == 0 for value in enumeration["violations"].values()))
    ok(all(set(row) == BY_N_KEYS for row in enumeration["by_n"]))
    ok(len(enumeration["by_n"]) == 6)
    for expected_n, row in enumerate(enumeration["by_n"], start=1):
        ok(row["n"] == expected_n)
        ok(row["input_count"] == 5 ** expected_n)
        ok(row["constant_count"] == 5)
        ok(sum(row["event_count_histogram"].values()) == row["input_count"])
        ok(sum(int(key) * value for key, value in row["event_count_histogram"].items()) == row["total_event_times"])
        ok(max(map(int, row["event_count_histogram"])) == row["max_event_times"])

    for witness in data["witnesses"]:
        ok(set(witness) == WITNESS_KEYS)
        ok(set(witness["trace"]) == TRACE_KEYS)
        ok(all(set(event) == EVENT_KEYS for event in witness["trace"]["events"]))
        initial = tuple(Fraction(value) for value in witness["input"])
        reconstructed, local_checks = evolve(initial)
        checks += local_checks
        ok(reconstructed == witness["trace"])
    ok([witness["name"] for witness in data["witnesses"]] == [
        "singleton", "constant", "endpoint_facet", "single_simultaneous_merger",
        "two_simultaneous_mergers", "mixed_plateaus", "generic_cascade",
        "rational_cascade",
    ])

    stress_digest = hashlib.sha256()
    stress_events = stress_merges = 0
    for raw in STRESS_INPUTS:
        initial = tuple(Fraction(value) for value in raw)
        result, local_checks = evolve(initial)
        checks += local_checks
        update_digest(stress_digest, compact(initial, result))
        stress_events += result["event_times"]
        stress_merges += result["pair_merges"]
    ok(stress_digest.hexdigest() == enumeration["stress_trace_sha256"])
    ok(stress_events == enumeration["stress_event_times"])
    ok(stress_merges == enumeration["stress_pair_merges"])

    by_n, trace_sha, raw_total, grid_checks = reconstruct_grid()
    checks += grid_checks
    ok(by_n == enumeration["by_n"])
    ok(trace_sha == enumeration["trace_sha256"])
    ok(raw_total == enumeration["raw_input_count"] == 19530)
    print(
        f"C279 independent checker: PASS ({checks} assertions; "
        f"{raw_total} exact inputs; producer import forbidden)"
    )


if __name__ == "__main__":
    main()
