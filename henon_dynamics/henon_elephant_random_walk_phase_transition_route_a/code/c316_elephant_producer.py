#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C316."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c316_elephant_evidence.json"
SOURCE = "1938bae19e5a92f9ce2411aafdc68323bd641bd0"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
NMAX = 14

P_VALUES = [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(2, 3),
            Fraction(3, 4), Fraction(4, 5), Fraction(1)]
Q_VALUES = [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)]
HISTORY_SPECS = [(Fraction(0), Fraction(1)), (Fraction(1, 2), Fraction(1, 4)),
                 (Fraction(3, 4), Fraction(1, 2)), (Fraction(4, 5), Fraction(1))]
SUPER_P = [Fraction(4, 5), Fraction(7, 8), Fraction(1)]
SUPER_Q = [Fraction(0), Fraction(1, 2), Fraction(1)]

FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False,
    "claims_root_number": False,
    "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False,
    "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}


def fs(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def product(n: int, c: Fraction) -> Fraction:
    out = Fraction(1)
    for j in range(1, n):
        out *= 1 + c / j
    return out


def harmonic(n: int) -> Fraction:
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0))


def expected_second(n: int, a: Fraction) -> Fraction:
    if a == Fraction(1, 2):
        return n * harmonic(n)
    return (2 * a * product(n, 2 * a) - n) / (2 * a - 1)


def step(dist: dict[int, Fraction], n: int, a: Fraction) -> dict[int, Fraction]:
    nxt: dict[int, Fraction] = {}
    for s, mass in dist.items():
        plus = (1 + a * Fraction(s, n)) / 2
        nxt[s + 1] = nxt.get(s + 1, Fraction(0)) + mass * plus
        nxt[s - 1] = nxt.get(s - 1, Fraction(0)) + mass * (1 - plus)
    return {s: mass for s, mass in nxt.items() if mass}


def pmf_rows(dist: dict[int, Fraction]) -> list[dict]:
    return [{"position": s, "probability": fs(dist[s])} for s in sorted(dist)]


def build_case(p: Fraction, q: Fraction) -> dict:
    a, b = 2 * p - 1, 2 * q - 1
    dist = {1: q, -1: 1 - q}
    dist = {s: mass for s, mass in dist.items() if mass}
    times = []
    for n in range(1, NMAX + 1):
        mean = sum((Fraction(s) * mass for s, mass in dist.items()), Fraction(0))
        second = sum((Fraction(s * s) * mass for s, mass in dist.items()), Fraction(0))
        predicted_mean = b * product(n, a)
        predicted_second = expected_second(n, a)
        times.append({
            "n": n,
            "pmf": pmf_rows(dist),
            "total_mass": fs(sum(dist.values(), Fraction(0))),
            "mean": fs(mean),
            "second_moment": fs(second),
            "variance": fs(second - mean * mean),
            "mean_formula": fs(predicted_mean),
            "second_formula": fs(predicted_second),
            "mean_product": fs(product(n, a)),
            "second_product": fs(product(n, 2 * a)),
        })
        if n < NMAX:
            dist = step(dist, n, a)
    if p < Fraction(3, 4):
        phase = "diffusive"
        normalization = "sqrt(n)"
        limit = f"Normal(0,{fs(1 / (3 - 4 * p))})"
    elif p == Fraction(3, 4):
        phase = "critical"
        normalization = "sqrt(n log n)"
        limit = "Normal(0,1)"
    else:
        phase = "superdiffusive"
        normalization = f"n^{fs(2 * p - 1)}"
        limit = "L with almost-sure and L4 convergence"
    return {
        "case_id": f"p-{p.numerator}-{p.denominator}-q-{q.numerator}-{q.denominator}",
        "p": fs(p), "q": fs(q), "a": fs(a), "initial_bias": fs(b),
        "phase": phase, "normalization": normalization, "limit_law": limit,
        "times": times,
    }


def martingale_rows() -> list[dict]:
    rows = []
    for p in P_VALUES:
        a = 2 * p - 1
        start = 2 if p == 0 else 1
        for n in range(start, 11):
            for s in range(-n, n + 1, 2):
                drift = (1 + a / n) * s
                if p == 0:
                    before = Fraction((n - 1) * s)
                    after = Fraction(n) * drift
                    normalization = "(n-1)S_n from n=2"
                else:
                    before = Fraction(s, 1) / product(n, a)
                    after = drift / product(n + 1, a)
                    normalization = "S_n/G_n(a)"
                rows.append({"p": fs(p), "n": n, "position": s,
                             "conditional_position_mean": fs(drift),
                             "normalized_before": fs(before),
                             "normalized_after_mean": fs(after),
                             "normalization": normalization})
    return rows


def history_terminal(p: Fraction, q: Fraction, terminal_n: int = 8) -> dict:
    a = 2 * p - 1
    histories: dict[tuple[int, ...], Fraction] = {}
    if q:
        histories[(1,)] = q
    if q != 1:
        histories[(-1,)] = 1 - q
    for n in range(1, terminal_n):
        nxt: dict[tuple[int, ...], Fraction] = {}
        for history, mass in histories.items():
            s = sum(history)
            plus = (1 + a * Fraction(s, n)) / 2
            if plus:
                nxt[history + (1,)] = mass * plus
            if plus != 1:
                nxt[history + (-1,)] = mass * (1 - plus)
        histories = nxt
    terminal: dict[int, Fraction] = {}
    for history, mass in histories.items():
        terminal[sum(history)] = terminal.get(sum(history), Fraction(0)) + mass
    return {"p": fs(p), "q": fs(q), "terminal_n": terminal_n,
            "positive_history_count": len(histories),
            "terminal_pmf": pmf_rows(terminal)}


def super_rows() -> list[dict]:
    rows = []
    for p in SUPER_P:
        for q in SUPER_Q:
            b = 2 * q - 1
            rows.append({
                "p": fs(p), "q": fs(q),
                "moment_1": {"prefactor": fs(b), "gamma_argument": fs(2 * p)},
                "moment_2": {"prefactor": fs(1 / (4 * p - 3)), "gamma_argument": fs(4 * p - 2)},
                "moment_3": {"prefactor": fs(2 * p * b / ((2 * p - 1) * (4 * p - 3))), "gamma_argument": fs(6 * p - 3)},
                "moment_4": {"prefactor": fs(6 * (8 * p * p - 4 * p - 1) / ((8 * p - 5) * (4 * p - 3) ** 2)), "gamma_argument": fs(8 * p - 4)},
                "endpoint_class": ("deterministic-sign" if p == 1 and q in (0, 1)
                                   else "two-point-sign" if p == 1 else "nondegenerate"),
            })
    return rows


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def leaf_count(value) -> int:
    if type(value) is dict:
        return sum(leaf_count(v) for v in value.values())
    if type(value) is list:
        return sum(leaf_count(v) for v in value)
    return 1


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C316 producer refuses optimized Python")
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    cases = [build_case(p, q) for p in P_VALUES for q in Q_VALUES]
    martingales = martingale_rows()
    histories = [history_terminal(p, q) for p, q in HISTORY_SPECS]
    superdiffusive = super_rows()
    data = {
        "schema": "hcs-c316-elephant-random-walk-v1",
        "candidate_id": "HCS-C316", "obstruction_id": "HEN-O300",
        "evaluation_date": "2026-09-03", "fixed_epoch": EPOCH,
        "source_commit": SOURCE, "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": {"increments": "+/-1", "initial_probability_plus": "q",
                  "memory_rule": "uniformly recall one past increment; copy with p and reverse with 1-p",
                  "position": "S_n=sum_{j<=n} X_j"},
        "theorem_contract": {
            "finite_laws": "exact conditional kernel and all-n first two moments",
            "martingale": "S_n/G_n(2p-1) for p>0; (n-1)S_n from n=2 when p=0",
            "phase_transition": "diffusive p<3/4, critical p=3/4, superdiffusive p>3/4",
            "endpoint": "at p=1, S_n=nX_1 and q=0 or 1 gives a deterministic limit",
            "evidence_boundary": "finite exact enumeration is regression evidence and does not prove a CLT",
        },
        "cases": cases, "martingale_rows": martingales,
        "history_crosschecks": histories, "superdiffusive_moment_rows": superdiffusive,
        "collision_boundary": {
            "C263": "the classical Polya urn is exchangeable with a Dirichlet limit; elephant increments have signed copying and a 3/4 scaling transition",
            "C273": "Sparre--Andersen treats iid symmetric increments; elephant increments retain full memory",
            "C302": "Quicksort has a recursive contraction limit rather than a memory-driven walk",
        },
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS,
        "nonclaims": [
            "No finite enumeration is presented as a proof of an asymptotic limit theorem.",
            "The stochastic memory clock has no rational-prime ownership or target determinant.",
            "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, zero match, or Hilbert--Polya operator is asserted.",
            "The package does not assert literature priority for the elephant-walk theorems.",
        ],
        "references": [
            {"identifier": "10.1103/PhysRevE.70.045101", "role": "original elephant random walk and finite moments"},
            {"identifier": "10.1088/1751-8121/aa95a6", "role": "martingale and three-regime limit theorems"},
        ],
    }
    data["enumeration"] = {"parameter_case_count": len(cases),
                           "time_slice_count": sum(len(row["times"]) for row in cases),
                           "pmf_cell_count": sum(len(t["pmf"]) for row in cases for t in row["times"]),
                           "martingale_cell_count": len(martingales),
                           "history_case_count": len(histories),
                           "superdiffusive_moment_case_count": len(superdiffusive)}
    data["enumeration"]["audited_leaf_count"] = leaf_count(data) + 1
    data["payload_sha256"] = payload_hash(data)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C316_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['audited_leaf_count']}")


if __name__ == "__main__":
    main()
