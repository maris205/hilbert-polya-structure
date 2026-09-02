#!/usr/bin/env python3
"""Produce canonical exact evidence for HCS-C307."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c307_connectivity_evidence.json"
SOURCE = "c0259978b1d7ebae63fe7b39fce1af2655b8529d"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600


def choose(n: int, k: int) -> int:
    return math.comb(n, k) if 0 <= k <= n else 0


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def rat(value: Fraction | int) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def connected_table(n_max: int) -> list[list[int]]:
    tables: list[list[int]] = [[], [1]]
    for n in range(2, n_max + 1):
        K = choose(n, 2)
        row = []
        for m in range(K + 1):
            disconnected = 0
            for s in range(1, n):
                rest_edges = choose(n - s, 2)
                inner = 0
                for j, count in enumerate(tables[s]):
                    inner += count * choose(rest_edges, m - j)
                disconnected += choose(n - 1, s - 1) * inner
            value = choose(K, m) - disconnected
            if value < 0:
                raise ArithmeticError("negative connected count")
            row.append(value)
        tables.append(row)
    return tables


def finite_rows(n_max: int = 12) -> tuple[list[dict], int]:
    tables = connected_table(n_max)
    rows = []
    cells = 0
    for n in range(1, n_max + 1):
        K = choose(n, 2)
        counts = tables[n]
        entries = []
        previous = Fraction(0)
        tails: list[Fraction] = []
        for m, count in enumerate(counts):
            total = choose(K, m)
            cdf = Fraction(count, total)
            pmf = cdf - previous
            tail = 1 - cdf
            entries.append({
                "m": m,
                "connected_count": count,
                "total_graph_count": total,
                "cdf": rat(cdf),
                "pmf": rat(pmf),
                "tail": rat(tail),
            })
            previous = cdf
            tails.append(tail)
        moments = []
        for order in range(1, 5):
            moment = sum((Fraction((m + 1) ** order - m ** order) * tails[m]
                          for m in range(K)), Fraction())
            moments.append({"order": order, "raw_moment": rat(moment)})
        first = 0 if n == 1 else n - 1
        last = 0 if n == 1 else choose(n - 1, 2) + 1
        rows.append({
            "n": n,
            "K": K,
            "cell_count": len(entries),
            "first_possible_hitting_m": first,
            "last_possible_hitting_m": last,
            "tree_endpoint_count": 1 if n == 1 else n ** (n - 2),
            "complete_endpoint_count": 1,
            "entries": entries,
            "moment_count": len(moments),
            "moments": moments,
        })
        cells += len(entries)
    return rows, cells


def isolated_factorial_moment(n: int, m: int, r: int) -> float:
    K = choose(n, 2)
    allowed = choose(n - r, 2)
    if m > allowed:
        return 0.0
    log_value = sum(math.log(n - j) for j in range(r))
    removed = K - allowed
    for i in range(m):
        log_value += math.log1p(-removed / (K - i))
    return math.exp(log_value)


def asymptotic_rows() -> list[dict]:
    out = []
    for n in (50, 100, 200, 400, 800):
        K = choose(n, 2)
        for c in (-1, 0, 1):
            m = math.floor(0.5 * n * (math.log(n) + c))
            for r in range(1, 5):
                actual = isolated_factorial_moment(n, m, r)
                target = math.exp(-r * c)
                out.append({
                    "n": n,
                    "c": c,
                    "m": m,
                    "r": r,
                    "within_edge_range": 0 <= m <= K,
                    "factorial_moment_decimal_12": f"{actual:.12f}",
                    "poisson_target_decimal_12": f"{target:.12f}",
                    "absolute_error_decimal_12": f"{abs(actual - target):.12f}",
                })
    return out


def build_payload() -> dict:
    rows, cells = finite_rows()
    diagnostics = asymptotic_rows()
    payload = {
        "schema": "hcs-c307-erdos-renyi-connectivity-hitting-evidence-v1",
        "candidate_id": "HCS-C307",
        "obstruction_id": "HEN-O291",
        "title": "Connectivity hitting in the random graph process: exact finite laws and the Gumbel window",
        "evaluation_date": "2026-09-03",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator_authority_sha256": EVALUATOR,
        "model": {
            "edges": "a uniformly random permutation of the K=binom(n,2) edges of the complete labeled graph",
            "state": "G_m contains the first m edges and is uniform on G(n,m)",
            "hitting_time": "tau_conn=min{m:G_m is connected}, with tau_conn=0 for n=1",
            "monotonicity": "edges are added without replacement and connectivity is absorbing",
        },
        "theorem": {
            "recurrence": "C(n,m)=binom(K,m)-sum_{s=1}^{n-1}binom(n-1,s-1)sum_j C(s,j)binom(binom(n-s,2),m-j)",
            "base": "C(1,0)=1 and out-of-range binomial coefficients are zero",
            "support": "for n>=2, C(n,m)=0 below n-1, C(n,n-1)=n^(n-2), and C(n,K)=1",
            "cdf": "P(tau_conn<=m)=C(n,m)/binom(K,m)",
            "pmf": "P(tau_conn=m)=F_n(m)-F_n(m-1), with F_n(-1)=0",
            "tails": "P(tau_conn>m)=1-C(n,m)/binom(K,m)",
            "moments": "E[tau_conn^r]=sum_{m=0}^{K-1}((m+1)^r-m^r)P(tau_conn>m), r>=1",
            "last_support": "for n>=2, tau_conn<=binom(n-1,2)+1",
            "window": "m_n(c)=floor((n/2)(log n+c))",
            "gumbel": "P(2 tau_conn/n-log n<=c) tends to exp(-exp(-c)) for every real c",
        },
        "proof_certificates": {
            "component_of_one": "a disconnected graph is uniquely decomposed by the size and internal edges of the component containing vertex 1",
            "uniform_slice": "the first m positions of a uniform edge permutation form a uniform m-edge subset",
            "isolated_factorial": "E[(I_n)_{r↓}]=(n)_{r↓} binom(binom(n-r,2),m)/binom(K,m), where (x)_{r↓}=x(x-1)...(x-r+1)",
            "poisson": "at m_n(c), every fixed factorial moment tends to exp(-rc), so I_n converges to Poisson(exp(-c))",
            "other_components": "a spanning-tree union bound over component sizes 2 through floor(n/2), split at n/log n, is o(1)",
            "rounding": "tau_conn is integer, so {2 tau_conn/n-log n<=c}={tau_conn<=m_n(c)} exactly",
        },
        "finite_connected_atlas": {
            "n_min": 1,
            "n_max": 12,
            "row_count": len(rows),
            "coefficient_cells": cells,
            "rows": rows,
        },
        "isolated_vertex_diagnostics": {
            "row_count": len(diagnostics),
            "n_values": [50, 100, 200, 400, 800],
            "c_values": [-1, 0, 1],
            "orders": [1, 2, 3, 4],
            "rows": diagnostics,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall_verdict": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "obstruction": "the edge-addition process and its connected-graph counts provide no target arithmetic local carrier, primitive-orbit Euler ledger, intrinsic prime clock, target determinant, or same-clock self-adjoint zero lift",
        },
        "scope_flags": {
            "claims_target_arithmetic_local_data": False,
            "claims_target_euler_factors": False,
            "claims_root_number": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_counting_law": False,
            "claims_target_functional_equation": False,
            "claims_target_zero_match": False,
            "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "boundaries": [
            "The finite process adds edges without replacement; it is not the independent-edge G(n,p) process.",
            "No pathwise identity with the disappearance time of the last isolated vertex is claimed.",
            "The Gumbel theorem is distributional; convergence of unbounded moments is not claimed.",
            "For fixed c, m_n(c) lies in [0,K] for all sufficiently large n; finite implementations clip only outside that asymptotic regime.",
            "The cases n=1 and n=2 have tau_conn=0 and tau_conn=1 respectively.",
        ],
        "collision_boundary": {
            "C301": "C301 is a parallel fair-bit partition-refinement birthday process; C307 is a without-replacement graph-edge growth process stopped at connectivity.",
            "C291": "C291 is random greedy dimer adsorption on finite paths and cycles; C307 adds unused complete-graph edges and stops at the absorbing connectivity upper set.",
            "C276": "C276 samples a whole uniform random mapping and studies functional-graph components; C307 evolves simple graphs one edge at a time with exact connected-graph counts.",
        },
        "source_owner_tokens": ["primary:https://static.renyi.hu/~p_erdos/1960-10.pdf"],
        "regression_summary": {
            "finite_n_max": 12,
            "finite_rows": len(rows),
            "coefficient_cells": cells,
            "moment_cells": 4 * len(rows),
            "exhaustive_n_max": 6,
            "exhaustive_graph_masks": sum(2 ** choose(n, 2) for n in range(1, 7)),
            "isolated_diagnostic_rows": len(diagnostics),
        },
    }
    payload["payload_sha256"] = canonical_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    payload = build_payload()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    summary = payload["regression_summary"]
    print(f"C307 producer PASS n_rows={summary['finite_rows']} coefficient_cells={summary['coefficient_cells']} diagnostics={summary['isolated_diagnostic_rows']}")
    print("payload_sha256=" + payload["payload_sha256"])


if __name__ == "__main__":
    main()
