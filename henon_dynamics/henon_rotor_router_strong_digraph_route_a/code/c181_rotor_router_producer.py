#!/usr/bin/env python3
"""Produce exact C181 evidence for rotor-router dynamics on strong digraphs."""
from __future__ import annotations

import argparse
from fractions import Fraction
from functools import reduce
from hashlib import sha256
from itertools import permutations, product
import json
from math import gcd
from pathlib import Path


SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
SOURCE_COMMIT = "bbb809ee198bc9ad5f196383baab1e3d9de38e43"
EVALUATOR_PATH = "flow_systems/skills/route-a-evaluator.md"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EXTRA_ORDER_GRAPH_LIMIT = 128


def canonical_hash(payload: dict) -> str:
    work = dict(payload)
    work.pop("payload_sha256", None)
    return sha256(json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def digest_rows(rows: list[str]) -> str:
    return sha256(("\n".join(rows) + "\n").encode()).hexdigest()


def determinant(matrix: list[list[int]]) -> int:
    n = len(matrix)
    if n == 0:
        return 1
    a = [[Fraction(x) for x in row] for row in matrix]
    sign = 1
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            sign *= -1
        pv = a[col][col]
        for r in range(col + 1, n):
            factor = a[r][col] / pv
            for c in range(col, n):
                a[r][c] -= factor * a[col][c]
    value = Fraction(sign)
    for i in range(n):
        value *= a[i][i]
    assert value.denominator == 1
    return value.numerator


def graph_invariants(n: int, arcs: list[tuple[int, int]]) -> tuple[list[int], list[int], list[int], int, int, int, bool]:
    adjacency = [[0] * n for _ in range(n)]
    outdegree, indegree = [0] * n, [0] * n
    for u, v in arcs:
        adjacency[u][v] += 1
        outdegree[u] += 1
        indegree[v] += 1
    laplacian = [[-adjacency[u][v] for v in range(n)] for u in range(n)]
    for u in range(n):
        laplacian[u][u] += outdegree[u]
    trees = []
    for root in range(n):
        minor = [[laplacian[i][j] for j in range(n) if j != root] for i in range(n) if i != root]
        trees.append(determinant(minor))
    assert all(t > 0 for t in trees)
    common = reduce(gcd, trees)
    period = sum(outdegree[v] * trees[v] for v in range(n)) // common
    states = sum(outdegree[v] * trees[v] for v in range(n))
    return outdegree, indegree, trees, common, period, states, outdegree == indegree


def strongly_connected(n: int, arcs: list[tuple[int, int]]) -> bool:
    adjacency = [[] for _ in range(n)]
    reverse = [[] for _ in range(n)]
    for u, v in arcs:
        adjacency[u].append(v)
        reverse[v].append(u)

    def reach(graph: list[list[int]]) -> set[int]:
        seen, stack = {0}, [0]
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        return seen

    return len(reach(adjacency)) == n and len(reach(reverse)) == n


def cyclic_orders(n: int, arcs: list[tuple[int, int]]) -> list[tuple[tuple[int, ...], ...]]:
    outgoing = [[i for i, (u, _) in enumerate(arcs) if u == v] for v in range(n)]
    choices = []
    for ids in outgoing:
        first, rest = min(ids), [x for x in ids if x != min(ids)]
        choices.append([(first, *tail) for tail in permutations(rest)])
    return [tuple(order) for order in product(*choices)]


def functional_cycles(n: int, arcs: list[tuple[int, int]], orders: tuple[tuple[int, ...], ...], positions: tuple[int, ...]) -> list[tuple[int, ...]]:
    successor = [arcs[orders[v][positions[v]]][1] for v in range(n)]
    globally_seen: set[int] = set()
    cycles: list[tuple[int, ...]] = []
    for start in range(n):
        if start in globally_seen:
            continue
        local: dict[int, int] = {}
        path: list[int] = []
        u = start
        while u not in local and u not in globally_seen:
            local[u] = len(path)
            path.append(u)
            u = successor[u]
        if u in local:
            cycle = path[local[u] :]
            rotations = [tuple(cycle[j:] + cycle[:j]) for j in range(len(cycle))]
            cycles.append(min(rotations))
        globally_seen.update(path)
    return sorted(cycles)


def unicycle_states(n: int, arcs: list[tuple[int, int]], orders: tuple[tuple[int, ...], ...]) -> list[tuple[int, ...]]:
    states: list[tuple[int, ...]] = []
    for positions in product(*(range(len(orders[v])) for v in range(n))):
        cycles = functional_cycles(n, arcs, orders, positions)
        if len(cycles) == 1:
            for chip in cycles[0]:
                states.append((chip, *positions))
    return sorted(states)


def step_state(state: tuple[int, ...], arcs: list[tuple[int, int]], orders: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], int]:
    chip, positions = state[0], list(state[1:])
    positions[chip] = (positions[chip] + 1) % len(orders[chip])
    arc_id = orders[chip][positions[chip]]
    return (arcs[arc_id][1], *positions), arc_id


def audit_order(graph_id: str, n: int, arcs: list[tuple[int, int]], orders: tuple[tuple[int, ...], ...], order_index: int) -> dict:
    outdegree, _, trees, common, period, expected_states, _ = graph_invariants(n, arcs)
    states = unicycle_states(n, arcs, orders)
    assert len(states) == expected_states
    state_set = set(states)
    transition: dict[tuple[int, ...], tuple[int, ...]] = {}
    used_arc: dict[tuple[int, ...], int] = {}
    for state in states:
        target, arc_id = step_state(state, arcs, orders)
        assert target in state_set
        transition[state] = target
        used_arc[state] = arc_id
    assert len(set(transition.values())) == len(states)

    unseen = set(states)
    orbit_encodings: list[str] = []
    orbit_lengths: list[int] = []
    while unseen:
        start = min(unseen)
        orbit, state = [], start
        while state not in orbit:
            orbit.append(state)
            state = transition[state]
        assert state == start
        unseen.difference_update(orbit)
        orbit_lengths.append(len(orbit))
        vertex_visits = [0] * n
        edge_uses = [0] * len(arcs)
        for state in orbit:
            vertex_visits[state[0]] += 1
            edge_uses[used_arc[state]] += 1
        expected_visits = [outdegree[v] * trees[v] // common for v in range(n)]
        expected_edges = [trees[u] // common for u, _ in arcs]
        assert vertex_visits == expected_visits
        assert edge_uses == expected_edges
        orbit_encodings.append(
            f"{','.join(':'.join(map(str, s)) for s in orbit)}|v={vertex_visits}|e={edge_uses}"
        )
    assert len(orbit_lengths) == common and set(orbit_lengths) == {period}
    return {
        "graph_id": graph_id,
        "order_index": order_index,
        "cyclic_orders": [list(x) for x in orders],
        "cyclic_order_digest": digest_rows([f"{v}:{','.join(map(str, order))}" for v, order in enumerate(orders)]),
        "unicycle_states": len(states),
        "orbit_count": len(orbit_lengths),
        "orbit_length": period,
        "vertex_visits_per_orbit": [outdegree[v] * trees[v] // common for v in range(n)],
        "arc_traversals_per_orbit": [trees[u] // common for u, _ in arcs],
        "orbit_digest": digest_rows(sorted(orbit_encodings)),
    }


def simple_graph_rows() -> tuple[list[dict], list[dict]]:
    graph_rows: list[dict] = []
    order_rows: list[dict] = []
    for n in range(2, 5):
        universe = [(u, v) for u in range(n) for v in range(n) if u != v]
        strong_rank = 0
        for mask in range(1, 1 << len(universe)):
            arcs = [arc for j, arc in enumerate(universe) if mask & (1 << j)]
            if not strongly_connected(n, arcs):
                continue
            graph_id = f"simple-n{n}-mask{mask:0{len(universe)}b}"
            outdegree, indegree, trees, common, period, states, eulerian = graph_invariants(n, arcs)
            orders = cyclic_orders(n, arcs)
            selected = orders if n <= 3 or strong_rank < EXTRA_ORDER_GRAPH_LIMIT else orders[:1]
            graph_rows.append(
                {
                    "graph_id": graph_id,
                    "kind": "labeled simple loopless exhaustive",
                    "n": n,
                    "mask": mask,
                    "arcs": [list(x) for x in arcs],
                    "outdegree": outdegree,
                    "indegree": indegree,
                    "arborescence_t": trees,
                    "M_gcd": common,
                    "common_orbit_length_L": period,
                    "unicycle_state_count": states,
                    "all_cyclic_order_count": len(orders),
                    "audited_cyclic_order_count": len(selected),
                    "eulerian": eulerian,
                    "eulerian_tree_constant": trees[0] if eulerian else None,
                }
            )
            order_rows.extend(audit_order(graph_id, n, arcs, order, i) for i, order in enumerate(selected))
            strong_rank += 1
    return graph_rows, order_rows


def multigraph_rows() -> tuple[list[dict], list[dict]]:
    examples = [
        ("multi-one-vertex-three-loops", 1, [(0, 0), (0, 0), (0, 0)]),
        ("multi-two-vertex-loops-parallel", 2, [(0, 0), (0, 1), (0, 1), (1, 0), (1, 1)]),
        ("multi-three-cycle-parallel", 3, [(0, 1), (0, 1), (1, 2), (2, 0), (2, 0), (2, 2)]),
        ("multi-two-vertex-eulerian-double", 2, [(0, 1), (0, 1), (1, 0), (1, 0)]),
    ]
    graphs, audits = [], []
    for graph_id, n, arcs in examples:
        assert strongly_connected(n, arcs)
        outdegree, indegree, trees, common, period, states, eulerian = graph_invariants(n, arcs)
        orders = cyclic_orders(n, arcs)
        graphs.append(
            {
                "graph_id": graph_id,
                "kind": "directed multigraph sentinel with distinguished arcs",
                "n": n,
                "mask": None,
                "arcs": [list(x) for x in arcs],
                "outdegree": outdegree,
                "indegree": indegree,
                "arborescence_t": trees,
                "M_gcd": common,
                "common_orbit_length_L": period,
                "unicycle_state_count": states,
                "all_cyclic_order_count": len(orders),
                "audited_cyclic_order_count": len(orders),
                "eulerian": eulerian,
                "eulerian_tree_constant": trees[0] if eulerian else None,
            }
        )
        audits.extend(audit_order(graph_id, n, arcs, order, i) for i, order in enumerate(orders))
    return graphs, audits


def build_evidence() -> dict:
    simple_graphs, simple_orders = simple_graph_rows()
    multi_graphs, multi_orders = multigraph_rows()
    graphs = simple_graphs + multi_graphs
    orders = simple_orders + multi_orders
    by_n = {str(n): sum(row["n"] == n for row in simple_graphs) for n in range(2, 5)}
    payload = {
        "schema": "hcs-c181-rotor-router-strong-digraph-v1",
        "candidate_id": "HCS-C181",
        "evaluation_date": "2026-08-26",
        "scope_literal": SCOPE,
        "source_commit": SOURCE_COMMIT,
        "evaluator": {"skill_version": "0.2.0", "authority_path": EVALUATOR_PATH, "authority_sha256": EVALUATOR_SHA256},
        "artifact_path_base": "henon_dynamics/henon_rotor_router_strong_digraph_route_a",
        "source_lock": {
            "family": "every finite nonempty strongly connected directed multigraph with distinguished arcs and a cyclic order at each vertex",
            "arithmetic_origin": "directed spanning-tree and Laplacian data only; no rational-prime or prime-power orbit correspondence is intrinsic",
            "state": "a chip vertex and one currently selected outgoing arc at every vertex",
            "step": "advance the chip-vertex rotor, then move the chip along the newly selected arc",
            "recurrent_phase": "unicycle states only",
            "clock": "one rotor advance and chip move",
            "normalization": "unweighted recurrent permutation counts",
            "determinant_convention": "finite permutation determinant det(I-zU); Artin--Mazur zeta is its reciprocal",
            "forbidden_recast": "no sink, stabilization, recurrent sandpile torsor, or critical-group translation is used",
            "forbidden_data": "prime tables, target zeros or divisors, arithmetic local factors, Euler factors, root numbers, automorphy, Hilbert--Polya, and Route B",
        },
        "theorem": {
            "arborescences": "t_v is the number of directed spanning in-arborescences oriented toward v",
            "gcd": "M=gcd_v t_v",
            "period": "L=(1/M) sum_v d_v^+ t_v",
            "orbit_classification": "the recurrent unicycle permutation has exactly M orbits, every one of exact length L",
            "visits": "each orbit visits v exactly d_v^+ t_v/M times and traverses each distinguished outgoing arc at v exactly t_v/M times",
            "fixed_counts": "#Fix(R^n)=M*L if L divides n and 0 otherwise",
            "zeta": "zeta_AM(z)=(1-z^L)^(-M), det(I-zU)=(1-z^L)^M",
            "spectrum": "every L-th root of unity occurs with multiplicity M",
            "eulerian": "if the digraph is Eulerian then t_v=tau, M=tau, L=|E|, and every arc is traversed once per orbit",
        },
        "graph_rows": graphs,
        "cyclic_order_rows": orders,
        "counts": {
            "simple_strong_graphs_by_n": by_n,
            "simple_strong_graphs_total": len(simple_graphs),
            "multigraph_sentinels": len(multi_graphs),
            "graph_rows_total": len(graphs),
            "cyclic_order_audits": len(orders),
            "unicycle_states_audited": sum(row["unicycle_states"] for row in orders),
            "rotor_orbits_audited": sum(row["orbit_count"] for row in orders),
            "extra_all_order_n4_graphs": EXTRA_ORDER_GRAPH_LIMIT,
            "theorem_domain": "all finite nonempty strongly connected directed multigraphs",
        },
        "route_a_verdict": {
            "A0": "A0_FAIL", "A1": "A1_WEAK", "A2": "A2_FAIL", "A3": "A3_FAIL",
            "A4": "A4_NATURAL_QUANTIZATION", "overall": "ROUTE_A_REJECTED",
            "a0_failure_forces_rejection": True, "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "novelty of the classical rotor-router orbit theorem or Markov-chain tree theorem",
            "a sandpile-group translation model, sink stabilization, or critical-group torsor",
            "a source-canonical time-reversal operator; cycle reversors require orbit basepoints",
            "a rational-prime or prime-power orbit correspondence",
            "an arithmetic local factor, Euler factor, root number, automorphy, Hilbert--Polya operator, or Route B",
        ],
        "integrity": {"finite_ledgers_are_proof": False, "external_reviewer_simulated": False, "acceptance_rate_reported": False, "citation_population": 1},
    }
    payload["payload_sha256"] = canonical_hash(payload)
    return payload


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=Path(__file__).resolve().parents[1] / "results/c181_rotor_router_evidence.json")
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C181_PRODUCER_PASS", "graphs": len(payload["graph_rows"]), "order_audits": len(payload["cyclic_order_rows"]), "payload_sha256": payload["payload_sha256"], **payload["counts"]["simple_strong_graphs_by_n"]}, sort_keys=True))


if __name__ == "__main__":
    main()
