#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C276."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "results/c276_random_mapping_evidence.json"
SOURCE = "418bcec5afb1f9e5905cc6e2ba7f9e099fef2e02"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788220800
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
mp.mp.dps = 90


def falling(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    return math.prod(range(n - k + 1, n + 1))


def qstr(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def stirling_table(n: int) -> list[list[int]]:
    table = [[0] * (n + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for i in range(1, n + 1):
        for r in range(1, i + 1):
            table[i][r] = table[i - 1][r - 1] + (i - 1) * table[i - 1][r]
    return table


def forest_count(n: int, roots: int) -> int:
    return 1 if roots == n else roots * n ** (n - roots - 1)


def analyze_mapping(mapping: tuple[int, ...]) -> tuple[int, int, Counter, int, int]:
    """Color-walk decomposition used only by the producer."""
    n = len(mapping)
    state = [0] * n
    position = [-1] * n
    cycle_lengths: list[int] = []
    for start in range(n):
        if state[start] != 0:
            continue
        path: list[int] = []
        vertex = start
        while state[vertex] == 0:
            state[vertex] = 1
            position[vertex] = len(path)
            path.append(vertex)
            vertex = mapping[vertex]
        if state[vertex] == 1:
            cycle_lengths.append(len(path) - position[vertex])
        for vertex in path:
            state[vertex] = 2
            position[vertex] = -1

    seen: dict[int, int] = {}
    vertex = 0
    while vertex not in seen:
        seen[vertex] = len(seen)
        vertex = mapping[vertex]
    total = len(seen)
    mu = seen[vertex]
    lam = total - mu
    return sum(cycle_lengths), len(cycle_lengths), Counter(cycle_lengths), mu, lam


def exhaustive_row(n: int, stirling: list[list[int]]) -> dict:
    joint: Counter[tuple[int, int]] = Counter()
    tail_cycle: Counter[tuple[int, int]] = Counter()
    cycle_totals: Counter[int] = Counter()
    maps = n**n
    for mapping in itertools.product(range(n), repeat=n):
        cyclic, components, cycle_lengths, mu, lam = analyze_mapping(mapping)
        joint[(cyclic, components)] += 1
        tail_cycle[(mu, lam)] += 1
        cycle_totals.update(cycle_lengths)

    joint_cells = []
    for k in range(1, n + 1):
        for components in range(1, k + 1):
            expected = (
                math.comb(n, k)
                * stirling[k][components]
                * forest_count(n, k)
            )
            joint_cells.append(
                {
                    "cyclic_points": k,
                    "components": components,
                    "count": joint[(k, components)],
                    "formula_count": expected,
                }
            )

    tail_cells = []
    for total in range(1, n + 1):
        for mu in range(total):
            lam = total - mu
            expected = falling(n - 1, total - 1) * n ** (n - total)
            tail_cells.append(
                {
                    "tail": mu,
                    "cycle": lam,
                    "count": tail_cycle[(mu, lam)],
                    "formula_count": expected,
                }
            )

    cycle_cells = []
    for ell in range(1, n + 1):
        expected_total = falling(n, ell) // ell * n ** (n - ell)
        expected_mean = Fraction(falling(n, ell), ell * n**ell)
        cycle_cells.append(
            {
                "length": ell,
                "aggregate_cycle_count": cycle_totals[ell],
                "formula_aggregate": expected_total,
                "mean_cycles": qstr(expected_mean),
            }
        )
    return {
        "n": n,
        "maps": maps,
        "joint_cells": joint_cells,
        "tail_cycle_cells": tail_cells,
        "cycle_length_cells": cycle_cells,
    }


def formula_row(n: int) -> dict:
    cyclic = [
        qstr(Fraction(falling(n, k) * k, n ** (k + 1)))
        for k in range(1, n + 1)
    ]
    survival = [
        qstr(Fraction(falling(n - 1, m), n**m))
        for m in range(0, n + 1)
    ]
    expected_cycles = [
        qstr(Fraction(falling(n, ell), ell * n**ell))
        for ell in range(1, n + 1)
    ]
    return {
        "n": n,
        "cyclic_point_probabilities": cyclic,
        "marked_collision_survival": survival,
        "expected_cycles_by_length": expected_cycles,
    }


def cyclic_scaling_receipt(n: int, x: str) -> dict:
    target = mp.mpf(x)
    k = max(1, min(n, int(mp.nint(target * mp.sqrt(n)))))
    mass = Fraction(falling(n, k) * k, n ** (k + 1))
    scaled = mp.sqrt(n) * mp.mpf(mass.numerator) / mass.denominator
    density = target * mp.e ** (-(target**2) / 2)
    return {
        "n": n,
        "x": x,
        "k": k,
        "mass": qstr(mass),
        "sqrt_n_times_mass": mp.nstr(scaled, 70),
        "rayleigh_density": mp.nstr(density, 70),
        "absolute_error": mp.nstr(abs(scaled - density), 70),
    }


def joint_scaling_receipt(n: int, x: str, y: str) -> dict:
    xx, yy = mp.mpf(x), mp.mpf(y)
    mu = max(0, int(mp.nint(xx * mp.sqrt(n))))
    lam = max(1, int(mp.nint(yy * mp.sqrt(n))))
    total = mu + lam
    mass = Fraction(falling(n - 1, total - 1), n**total)
    scaled = mp.mpf(n * mass.numerator) / mass.denominator
    density = mp.e ** (-((xx + yy) ** 2) / 2)
    return {
        "n": n,
        "x": x,
        "y": y,
        "tail": mu,
        "cycle": lam,
        "mass": qstr(mass),
        "n_times_mass": mp.nstr(scaled, 70),
        "joint_density": mp.nstr(density, 70),
        "absolute_error": mp.nstr(abs(scaled - density), 70),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    stirling = stirling_table(40)
    enumeration = [exhaustive_row(n, stirling) for n in range(1, 8)]
    formulas = [formula_row(n) for n in range(1, 33)]
    cyclic_scaling = [
        cyclic_scaling_receipt(n, x)
        for n in (64, 256, 1024, 4096)
        for x in ("0.5", "1.0", "1.5", "2.0")
    ]
    joint_scaling = [
        joint_scaling_receipt(n, x, y)
        for n in (256, 1024, 4096)
        for x, y in (("0.25", "0.75"), ("0.5", "0.5"), ("1.0", "0.5"), ("0.5", "1.5"))
    ]

    data = {
        "schema": "hcs-c276-uniform-random-mapping-v1",
        "candidate_id": "HCS-C276",
        "evaluation_date": "2026-09-01",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": {
            "state_space": "all functions f:[n]->[n], each with probability n^(-n)",
            "functional_graph": "one directed edge v->f(v) from every labelled vertex",
            "cyclic_points": "C_n is the number of vertices on directed cycles",
            "components": "K_n is the number of weak components, equivalently directed cycles",
            "marked_orbit": "from vertex 1, mu is the tail length, lambda the eventual cycle length, and R=mu+lambda",
        },
        "theorem_contract": {
            "joint_count": "N(n,k,r)=binom(n,k)c(k,r) k n^(n-k-1), with the rooted-forest factor interpreted as 1 at k=n",
            "cyclic_distribution": "P(C_n=k)=(n)_k k/n^(k+1), 1<=k<=n",
            "cycle_expectation": "E[number of ell-cycles]=(n)_ell/(ell n^ell)",
            "marked_joint": "P(mu=u,lambda=l)=(n-1)_(u+l-1)/n^(u+l)",
            "distribution_identity": "C_n and R_n=mu+lambda have the same law",
            "rayleigh": "C_n/sqrt(n) and R_n/sqrt(n) converge to Rayleigh density x exp(-x^2/2)",
            "joint_limit": "(mu,lambda)/sqrt(n) has limiting density exp(-(x+y)^2/2) on x,y>=0",
        },
        "proof_contract": {
            "forest": "the all-minors directed matrix-tree determinant is det(nI-J)=k n^(n-k-1)",
            "decomposition": "choose cyclic labels, a permutation with r cycles, then a rooted forest into those labels",
            "marked_orbit": "choose an ordered collision-free prefix and force its closing edge",
            "rayleigh": "the no-collision tail product converges after the square-root scaling",
            "joint_limit": "a two-dimensional local product limit plus tightness gives the stated density",
            "finite_evidence_role": "exhaustive enumeration is regression evidence and not a proof of the all-n theorem",
        },
        "regression": {
            "enumeration": enumeration,
            "formula_atlas": formulas,
            "cyclic_scaling_receipts": cyclic_scaling,
            "joint_scaling_receipts": joint_scaling,
            "counts": {
                "enumerated_sizes": 7,
                "enumerated_maps": sum(row["maps"] for row in enumeration),
                "joint_enumeration_cells": sum(len(row["joint_cells"]) for row in enumeration),
                "tail_cycle_enumeration_cells": sum(len(row["tail_cycle_cells"]) for row in enumeration),
                "cycle_length_enumeration_cells": sum(len(row["cycle_length_cells"]) for row in enumeration),
                "formula_sizes": len(formulas),
                "cyclic_formula_cells": sum(len(row["cyclic_point_probabilities"]) for row in formulas),
                "collision_survival_cells": sum(len(row["marked_collision_survival"]) for row in formulas),
                "cycle_expectation_formula_cells": sum(len(row["expected_cycles_by_length"]) for row in formulas),
                "cyclic_scaling_receipts": len(cyclic_scaling),
                "joint_scaling_receipts": len(joint_scaling),
            },
        },
        "analytic_proof_obligations": [
            "functional-graph cycle plus in-tree decomposition",
            "rooted-forest determinant including k=n",
            "unsigned Stirling cycle refinement",
            "marked tail-cycle prefix count",
            "C_n equals marked collision length in distribution",
            "one-dimensional Rayleigh tightness and tail limit",
            "two-dimensional local limit and boundary tightness",
            "n=1 and pure-permutation boundary faces",
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "target_divisor": False,
            "functional_equation": False,
            "hilbert_polya_operator": False,
        },
        "nonclaims": [
            "Workspace ownership is not a literature-priority claim.",
            "Ensemble averages are not the orbit zeta or determinant of one deterministic map.",
            "No canonical same-clock operator is inferred from the random ensemble.",
        ],
        "sources": [
            {
                "author": "Bernard Harris",
                "title": "Probability Distributions Related to Random Mappings",
                "journal": "The Annals of Mathematical Statistics",
                "volume": "31",
                "year": 1960,
                "pages": "1045--1062",
                "doi": "10.1214/aoms/1177705677",
                "role": "primary uniform-random-mapping source",
            },
            {
                "author": "Philippe Flajolet and Andrew M. Odlyzko",
                "title": "Random Mapping Statistics",
                "venue": "EUROCRYPT 1989, LNCS 434",
                "year": 1990,
                "pages": "329--354",
                "doi": "10.1007/3-540-46885-4_34",
                "role": "primary systematic asymptotic source",
            },
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    )
    counts = data["regression"]["counts"]
    print(
        "C276_PRODUCER_PASS "
        f"maps={counts['enumerated_maps']} joint={counts['joint_enumeration_cells']} "
        f"tail={counts['tail_cycle_enumeration_cells']} payload={data['payload_sha256']}"
    )


if __name__ == "__main__":
    main()
