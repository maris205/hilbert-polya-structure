#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C276."""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c276_random_mapping_evidence.json"
SOURCE = "418bcec5afb1f9e5905cc6e2ba7f9e099fef2e02"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
TOP_KEYS = {
    "schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator", "model", "theorem_contract", "proof_contract",
    "regression", "analytic_proof_obligations", "route_a", "scope_flags",
    "nonclaims", "sources", "payload_sha256",
}
mp.mp.dps = 90


def falling(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    value = 1
    for j in range(k):
        value *= n - j
    return value


def parse(value: str) -> Fraction:
    numerator, denominator = value.split("/")
    return Fraction(int(numerator), int(denominator))


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def stirling_first(n: int) -> list[list[int]]:
    rows = [[0] * (n + 1) for _ in range(n + 1)]
    rows[0][0] = 1
    for size in range(n):
        for cycles in range(size + 1):
            rows[size + 1][cycles + 1] += rows[size][cycles]
            rows[size + 1][cycles] += size * rows[size][cycles]
    return rows


def forest(n: int, roots: int) -> int:
    if n == roots:
        return 1
    return roots * n ** (n - roots - 1)


def independent_signature(mapping: tuple[int, ...]) -> tuple[int, int, Counter, int, int]:
    """Trace every orbit and canonicalize cycles; intentionally unlike producer DFS."""
    n = len(mapping)
    cycles: set[tuple[int, ...]] = set()
    for start in range(n):
        order: dict[int, int] = {}
        path: list[int] = []
        vertex = start
        while vertex not in order:
            order[vertex] = len(path)
            path.append(vertex)
            vertex = mapping[vertex]
        cycle = tuple(sorted(path[order[vertex]:]))
        cycles.add(cycle)

    order = {}
    vertex = 0
    while vertex not in order:
        order[vertex] = len(order)
        vertex = mapping[vertex]
    total = len(order)
    mu = order[vertex]
    lam = total - mu
    lengths = Counter(len(cycle) for cycle in cycles)
    return sum(lengths[length] * length for length in lengths), len(cycles), lengths, mu, lam


def rebuild(n: int) -> tuple[Counter, Counter, Counter]:
    joint: Counter[tuple[int, int]] = Counter()
    marked: Counter[tuple[int, int]] = Counter()
    lengths: Counter[int] = Counter()
    for entries in itertools.product(range(n), repeat=n):
        cyclic, components, cycles, mu, lam = independent_signature(entries)
        joint[(cyclic, components)] += 1
        marked[(mu, lam)] += 1
        lengths.update(cycles)
    return joint, marked, lengths


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(path.read_text())
    assertions = 0

    def check(condition: bool) -> None:
        nonlocal assertions
        assert condition
        assertions += 1

    check(set(data) == TOP_KEYS)
    check(data["schema"] == "hcs-c276-uniform-random-mapping-v1")
    check(data["candidate_id"] == "HCS-C276")
    check(data["evaluation_date"] == "2026-09-01")
    check(data["source_commit"] == SOURCE)
    check(data["fixed_epoch"] == 1788220800)
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    check(data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR})
    check(data["payload_sha256"] == payload_hash(data))
    check(data["route_a"]["tuple"] == TUPLE)
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED")
    check(data["route_a"]["route_b_invocation_allowed"] is False)
    check(set(data["scope_flags"]) == {
        "arithmetic_local_data", "euler_factors", "root_numbers", "automorphy",
        "target_divisor", "functional_equation", "hilbert_polya_operator",
    })
    for value in data["scope_flags"].values():
        check(value is False)

    model = data["model"]
    check(model["state_space"] == "all functions f:[n]->[n], each with probability n^(-n)")
    check("R=mu+lambda" in model["marked_orbit"])
    theorem = data["theorem_contract"]
    check("binom(n,k)c(k,r)" in theorem["joint_count"])
    check(theorem["cyclic_distribution"].startswith("P(C_n=k)="))
    check("same law" in theorem["distribution_identity"])
    check("exp(-(x+y)^2/2)" in theorem["joint_limit"])
    check(len(data["analytic_proof_obligations"]) == 8)
    check(len(data["nonclaims"]) == 3)
    sources = data["sources"]
    check(len(sources) == 2)
    check(sources[0]["author"] == "Bernard Harris")
    check(sources[0]["year"] == 1960)
    check(sources[0]["doi"] == "10.1214/aoms/1177705677")
    check(sources[1]["author"] == "Philippe Flajolet and Andrew M. Odlyzko")
    check(sources[1]["year"] == 1990)
    check(sources[1]["doi"] == "10.1007/3-540-46885-4_34")

    stirling = stirling_first(40)
    enumeration = data["regression"]["enumeration"]
    check([row["n"] for row in enumeration] == list(range(1, 8)))
    maps_total = joint_cells = tail_cells = cycle_cells = 0
    for row in enumeration:
        n = row["n"]
        check(row["maps"] == n**n)
        expected_joint_schema = n * (n + 1) // 2
        check(len(row["joint_cells"]) == expected_joint_schema)
        check(len(row["tail_cycle_cells"]) == expected_joint_schema)
        check(len(row["cycle_length_cells"]) == n)
        rebuilt_joint, rebuilt_tail, rebuilt_lengths = rebuild(n)
        maps_total += n**n
        joint_cells += len(row["joint_cells"])
        tail_cells += len(row["tail_cycle_cells"])
        cycle_cells += len(row["cycle_length_cells"])

        observed_joint_sum = 0
        for cell in row["joint_cells"]:
            k, components = cell["cyclic_points"], cell["components"]
            formula = math.comb(n, k) * stirling[k][components] * forest(n, k)
            check(cell["count"] == rebuilt_joint[(k, components)])
            check(cell["formula_count"] == formula == cell["count"])
            observed_joint_sum += cell["count"]
        check(observed_joint_sum == n**n)

        observed_tail_sum = 0
        for cell in row["tail_cycle_cells"]:
            mu, lam = cell["tail"], cell["cycle"]
            total = mu + lam
            formula = falling(n - 1, total - 1) * n ** (n - total)
            check(cell["count"] == rebuilt_tail[(mu, lam)])
            check(cell["formula_count"] == formula == cell["count"])
            observed_tail_sum += cell["count"]
        check(observed_tail_sum == n**n)

        for cell in row["cycle_length_cells"]:
            ell = cell["length"]
            total_formula = falling(n, ell) // ell * n ** (n - ell)
            mean_formula = Fraction(falling(n, ell), ell * n**ell)
            check(cell["aggregate_cycle_count"] == rebuilt_lengths[ell])
            check(cell["formula_aggregate"] == total_formula == rebuilt_lengths[ell])
            check(parse(cell["mean_cycles"]) == mean_formula)

        cyclic_from_joint = Counter()
        for (k, components), count in rebuilt_joint.items():
            cyclic_from_joint[k] += count
        collision_from_tail = Counter()
        for (mu, lam), count in rebuilt_tail.items():
            collision_from_tail[mu + lam] += count
        check(cyclic_from_joint == collision_from_tail)

    atlas = data["regression"]["formula_atlas"]
    check([row["n"] for row in atlas] == list(range(1, 33)))
    cyclic_formula_cells = collision_survival_cells = cycle_expectation_formula_cells = 0
    for row in atlas:
        n = row["n"]
        cyclic = [parse(value) for value in row["cyclic_point_probabilities"]]
        survival = [parse(value) for value in row["marked_collision_survival"]]
        cycles = [parse(value) for value in row["expected_cycles_by_length"]]
        cyclic_formula_cells += len(cyclic)
        collision_survival_cells += len(survival)
        cycle_expectation_formula_cells += len(cycles)
        check(cyclic == [Fraction(falling(n, k) * k, n ** (k + 1)) for k in range(1, n + 1)])
        check(sum(cyclic, Fraction()) == 1)
        check(survival == [Fraction(falling(n - 1, m), n**m) for m in range(n + 1)])
        check(survival[0] == 1 and survival[-1] == 0)
        check([survival[k - 1] - survival[k] for k in range(1, n + 1)] == cyclic)
        check(cycles == [Fraction(falling(n, ell), ell * n**ell) for ell in range(1, n + 1)])

    for row in data["regression"]["cyclic_scaling_receipts"]:
        n, k = row["n"], row["k"]
        x = mp.mpf(row["x"])
        mass = Fraction(falling(n, k) * k, n ** (k + 1))
        scaled = mp.sqrt(n) * mass.numerator / mass.denominator
        density = x * mp.e ** (-(x**2) / 2)
        check(parse(row["mass"]) == mass)
        check(abs(mp.mpf(row["sqrt_n_times_mass"]) - scaled) < mp.mpf("1e-68"))
        check(abs(mp.mpf(row["rayleigh_density"]) - density) < mp.mpf("1e-68"))
        check(abs(mp.mpf(row["absolute_error"]) - abs(scaled - density)) < mp.mpf("1e-68"))

    for row in data["regression"]["joint_scaling_receipts"]:
        n, mu, lam = row["n"], row["tail"], row["cycle"]
        x, y = mp.mpf(row["x"]), mp.mpf(row["y"])
        mass = Fraction(falling(n - 1, mu + lam - 1), n ** (mu + lam))
        scaled = mp.mpf(n * mass.numerator) / mass.denominator
        density = mp.e ** (-((x + y) ** 2) / 2)
        check(parse(row["mass"]) == mass)
        check(abs(mp.mpf(row["n_times_mass"]) - scaled) < mp.mpf("1e-68"))
        check(abs(mp.mpf(row["joint_density"]) - density) < mp.mpf("1e-68"))
        check(abs(mp.mpf(row["absolute_error"]) - abs(scaled - density)) < mp.mpf("1e-68"))

    counts = data["regression"]["counts"]
    check(counts["enumerated_sizes"] == 7)
    check(counts["enumerated_maps"] == maps_total == 873612)
    check(counts["joint_enumeration_cells"] == joint_cells == 84)
    check(counts["tail_cycle_enumeration_cells"] == tail_cells == 84)
    check(counts["cycle_length_enumeration_cells"] == cycle_cells == 28)
    check(counts["formula_sizes"] == 32)
    check(counts["cyclic_formula_cells"] == cyclic_formula_cells == 528)
    check(counts["collision_survival_cells"] == collision_survival_cells == 560)
    check(counts["cycle_expectation_formula_cells"] == cycle_expectation_formula_cells == 528)
    check(counts["cyclic_scaling_receipts"] == 16)
    check(counts["joint_scaling_receipts"] == 12)

    print(f"C276 independent checker: PASS ({assertions} assertions)")


if __name__ == "__main__":
    main()
