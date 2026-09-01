#!/usr/bin/env python3
"""Independent exact checker for HCS-C273; it does not import the producer."""
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
DEFAULT = ROOT / "results/c273_sparre_andersen_evidence.json"
SOURCE = "9cb7483e97ef82fdc06d45ecb3043f183ce22391"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]
mp.mp.dps = 90


def central(n: int) -> Fraction:
    return Fraction(math.comb(2 * n, n), 1 << (2 * n))


def parse(value: str) -> Fraction:
    numerator, denominator = value.split("/")
    return Fraction(int(numerator), int(denominator))


def payload_hash(data: dict) -> str:
    copy = dict(data)
    copy.pop("payload_sha256", None)
    encoded = json.dumps(copy, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(encoded.encode()).hexdigest()


def rebuild_control(n: int) -> tuple[int, int, int, list[int], list[int]]:
    values = tuple(3**j for j in range(n))
    pos = Counter()
    argmax = Counter()
    survival = ties = total = 0
    for ordering in itertools.permutations(values):
        for mask in range(1 << n):
            total += 1
            path = [0]
            for j, magnitude in enumerate(ordering):
                sign = 1 if (mask >> j) & 1 else -1
                path.append(path[-1] + sign * magnitude)
            pos[sum(x > 0 for x in path[1:])] += 1
            top = max(path)
            locations = [j for j, x in enumerate(path) if x == top]
            if len(locations) == 1:
                argmax[locations[0]] += 1
            else:
                ties += 1
            survival += int(min(path[1:]) > 0)
    return total, survival, ties, [pos[j] for j in range(n + 1)], [argmax[j] for j in range(n + 1)]


def rebuild_atomic(n: int) -> dict:
    pos = Counter()
    argmax = Counter()
    ties = weak = strict = 0
    for mask in range(1 << n):
        path = [0]
        for j in range(n):
            step = 1 if (mask >> j) & 1 else -1
            path.append(path[-1] + step)
        pos[sum(x > 0 for x in path[1:])] += 1
        top = max(path)
        locations = [j for j, x in enumerate(path) if x == top]
        if len(locations) == 1:
            argmax[locations[0]] += 1
        else:
            ties += 1
        weak += int(min(path[1:]) >= 0)
        strict += int(min(path[1:]) > 0)
    return {
        "n": n,
        "histories": 1 << n,
        "strict_positive_count_histogram": [pos[j] for j in range(n + 1)],
        "unique_maximum_time_histogram": [argmax[j] for j in range(n + 1)],
        "tied_maximum_histories": ties,
        "nonnegative_survival_count": weak,
        "strict_survival_count": strict,
    }


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(path.read_text())
    assertions = 0

    def check(condition: bool) -> None:
        nonlocal assertions
        assert condition
        assertions += 1

    check(data["schema"] == "hcs-c273-sparre-andersen-v1")
    check(data["candidate_id"] == "HCS-C273")
    check(data["source_commit"] == SOURCE)
    check(data["fixed_epoch"] == 1788134400)
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    check(data["evaluator"]["sha256"] == EVALUATOR)
    check(data["payload_sha256"] == payload_hash(data))
    check(data["route_a"]["tuple"] == TUPLE)
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED")
    check(data["route_a"]["route_b_invocation_allowed"] is False)
    for value in data["scope_flags"].values():
        check(value is False)

    model = data["model"]
    check(model["survival"].startswith("q_n=P(S_1>0"))
    check("unique argmax" in model["maximum_time"])
    check("continuous" in model["increments"] and "symmetric" in model["increments"])
    theorem = data["theorem_contract"]
    check(theorem["survival"] == "q_n=binom(2n,n)/4^n")
    check("q_k q_{n-k}" in theorem["discrete_arcsine"])
    check("Beta(1/2,1/2)" in theorem["scaling"])

    rows = data["regression"]["q_rows"]
    check(len(rows) == 41)
    for n, row in enumerate(rows):
        value = central(n)
        first = Fraction(0) if n == 0 else central(n - 1) - value
        conv = sum((central(k) * central(n - k) for k in range(n + 1)), Fraction(0))
        check(row["n"] == n)
        check(parse(row["q_n"]) == value)
        check(parse(row["first_strict_descent_n"]) == first)
        check(parse(row["arcsine_convolution"]) == conv == 1)
        if n:
            check(first == central(n - 1) / (2 * n))
            check(sum((central(j - 1) - central(j) for j in range(1, n + 1)), Fraction(0)) + value == 1)

    arc_rows = data["regression"]["arcsine_rows"]
    check(len(arc_rows) == 33)
    arc_cells = 0
    for row in arc_rows:
        n = row["n"]
        cells = [parse(x) for x in row["cells"]]
        arc_cells += len(cells)
        check(len(cells) == n + 1)
        check(cells == [central(k) * central(n - k) for k in range(n + 1)])
        check(sum(cells, Fraction(0)) == 1)
        check(cells == list(reversed(cells)))

    controls = data["regression"]["permutation_controls"]
    check([row["n"] for row in controls] == list(range(1, 8)))
    history_count = 0
    for row in controls:
        n = row["n"]
        total, survival, ties, pos, maximum = rebuild_control(n)
        history_count += total
        check(row["magnitudes"] == [3**j for j in range(n)])
        check(row["histories"] == total == math.factorial(n) * 2**n)
        check(row["survival_count"] == survival)
        check(row["ties"] == ties == 0)
        check(row["positive_count_histogram"] == pos)
        check(row["maximum_time_histogram"] == maximum)
        expected = [central(k) * central(n - k) * total for k in range(n + 1)]
        check(all(x.denominator == 1 for x in expected))
        check(pos == maximum == [x.numerator for x in expected])
        check(Fraction(survival, total) == central(n))

    atomic = data["regression"]["atomic_controls"]
    check(atomic == [rebuild_atomic(n) for n in range(1, 9)])
    n2 = atomic[1]
    check(n2["nonnegative_survival_count"] == 2)
    check(Fraction(n2["nonnegative_survival_count"], 4) != central(2))
    check(n2["strict_positive_count_histogram"] == [2, 1, 1])
    check(n2["tied_maximum_histories"] > 0)

    for row in data["regression"]["scaling_receipts"]:
        n, k = row["n"], row["k"]
        mass = central(k) * central(n - k)
        x = mp.mpf(k) / n
        scaled = mp.mpf(n * mass.numerator) / mass.denominator
        density = 1 / (mp.pi * mp.sqrt(x * (1 - x)))
        check(parse(row["mass"]) == mass)
        check(abs(mp.mpf(row["n_times_mass"]) - scaled) < mp.mpf("1e-68"))
        check(abs(mp.mpf(row["arcsine_density"]) - density) < mp.mpf("1e-68"))
        check(abs(mp.mpf(row["absolute_error"]) - abs(scaled - density)) < mp.mpf("1e-68"))

    counts = data["regression"]["counts"]
    check(counts["q_rows"] == len(rows))
    check(counts["arcsine_rows"] == len(arc_rows))
    check(counts["arcsine_cells"] == arc_cells)
    check(counts["permutation_histories"] == history_count)
    check(counts["scaling_receipts"] == 12)
    source = data["source"]
    check(source["author"] == "Erik Sparre Andersen")
    check(source["doi"] == "10.7146/math.scand.a-10385")
    check(source["year"] == 1953 and source["pages"] == "263--285")
    check(len(data["analytic_proof_obligations"]) == 7)
    check(len(data["nonclaims"]) == 3)
    print(f"C273 independent checker: PASS ({assertions} assertions)")


if __name__ == "__main__":
    main()
