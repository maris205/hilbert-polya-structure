#!/usr/bin/env python3
"""Independent exhaustive checker for C181; imports no producer code."""
from __future__ import annotations

import argparse
from functools import reduce
from hashlib import sha256
from itertools import permutations, product
import json
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c181_rotor_router_evidence.json"
SOURCE = "bbb809ee198bc9ad5f196383baab1e3d9de38e43"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"


def canonical_hash(payload: dict) -> str:
    work = dict(payload)
    work.pop("payload_sha256", None)
    return sha256(json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def digest_rows(rows: list[str]) -> str:
    return sha256(("\n".join(rows) + "\n").encode()).hexdigest()


def require(ok: bool, message: str, count: list[int]) -> None:
    count[0] += 1
    if not ok:
        raise AssertionError(message)


def det_leibniz(a: list[list[int]]) -> int:
    n = len(a)
    if n == 0:
        return 1
    total = 0
    for p in permutations(range(n)):
        inversions = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = -1 if inversions & 1 else 1
        for i in range(n):
            term *= a[i][p[i]]
        total += term
    return total


def connected(n: int, arcs: list[tuple[int, int]]) -> bool:
    adj = [[] for _ in range(n)]
    for u, v in arcs:
        adj[u].append(v)
    for start in range(n):
        seen, stack = {start}, [start]
        while stack:
            for v in adj[stack.pop()]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        if len(seen) != n:
            return False
    return True


def invariants(n: int, arcs: list[tuple[int, int]]) -> tuple[list[int], list[int], list[int], int, int, int, bool]:
    a = [[0] * n for _ in range(n)]
    outd, ind = [0] * n, [0] * n
    for u, v in arcs:
        a[u][v] += 1
        outd[u] += 1
        ind[v] += 1
    lap = [[(outd[u] if u == v else 0) - a[u][v] for v in range(n)] for u in range(n)]
    trees = [det_leibniz([[lap[i][j] for j in range(n) if j != r] for i in range(n) if i != r]) for r in range(n)]
    common = reduce(gcd, trees)
    states = sum(outd[v] * trees[v] for v in range(n))
    return outd, ind, trees, common, states // common, states, outd == ind


def all_orders(n: int, arcs: list[tuple[int, int]]) -> list[tuple[tuple[int, ...], ...]]:
    choices = []
    for v in range(n):
        ids = [j for j, (u, _) in enumerate(arcs) if u == v]
        anchor = min(ids)
        choices.append([(anchor, *tail) for tail in permutations([x for x in ids if x != anchor])])
    return [tuple(x) for x in product(*choices)]


def cycle_vertices(successor: list[int]) -> list[tuple[int, ...]]:
    cycles: set[tuple[int, ...]] = set()
    n = len(successor)
    for start in range(n):
        path, index, u = [], {}, start
        while u not in index:
            index[u] = len(path)
            path.append(u)
            u = successor[u]
        raw = path[index[u] :]
        rotations = [tuple(raw[j:] + raw[:j]) for j in range(len(raw))]
        cycles.add(min(rotations))
    return sorted(cycles)


def states_for(n: int, arcs: list[tuple[int, int]], order: tuple[tuple[int, ...], ...]) -> list[tuple[int, ...]]:
    answer = []
    for positions in product(*(range(len(order[v])) for v in range(n))):
        successor = [arcs[order[v][positions[v]]][1] for v in range(n)]
        cycles = cycle_vertices(successor)
        if len(cycles) == 1:
            answer.extend((chip, *positions) for chip in cycles[0])
    return sorted(answer)


def transition(state: tuple[int, ...], arcs: list[tuple[int, int]], order: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], int]:
    chip = state[0]
    pos = list(state[1:])
    pos[chip] = (pos[chip] + 1) % len(order[chip])
    edge = order[chip][pos[chip]]
    return (arcs[edge][1], *pos), edge


def validate_order(row: dict, graph: dict, count: list[int]) -> None:
    n = graph["n"]
    arcs = [tuple(x) for x in graph["arcs"]]
    order = tuple(tuple(x) for x in row["cyclic_orders"])
    require(row["graph_id"] == graph["graph_id"], "order graph id", count)
    require(order in all_orders(n, arcs), "illegal cyclic order", count)
    require(row["cyclic_order_digest"] == digest_rows([f"{v}:{','.join(map(str, x))}" for v, x in enumerate(order)]), "order digest", count)
    states = states_for(n, arcs, order)
    require(len(states) == graph["unicycle_state_count"] == row["unicycle_states"], "unicycle count", count)
    nxt, edge = {}, {}
    for state in states:
        nxt[state], edge[state] = transition(state, arcs, order)
        require(nxt[state] in set(states), "closed recurrent set", count)
    require(len(set(nxt.values())) == len(states), "recurrent permutation", count)
    outd, _, trees, common, period, _, _ = invariants(n, arcs)
    unseen = set(states)
    encodings, lengths = [], []
    while unseen:
        start = min(unseen)
        orbit, state = [], start
        while state not in orbit:
            orbit.append(state)
            state = nxt[state]
        require(state == start, "cycle closure", count)
        unseen.difference_update(orbit)
        lengths.append(len(orbit))
        visits, uses = [0] * n, [0] * len(arcs)
        for state in orbit:
            visits[state[0]] += 1
            uses[edge[state]] += 1
        expected_visits = [outd[v] * trees[v] // common for v in range(n)]
        expected_uses = [trees[u] // common for u, _ in arcs]
        require(visits == expected_visits, "visit frequencies", count)
        require(uses == expected_uses, "arc frequencies", count)
        encodings.append(f"{','.join(':'.join(map(str, s)) for s in orbit)}|v={visits}|e={uses}")
    require(len(lengths) == common == row["orbit_count"], "orbit count", count)
    require(set(lengths) == {period} and row["orbit_length"] == period, "common length", count)
    require(row["vertex_visits_per_orbit"] == [outd[v] * trees[v] // common for v in range(n)], "stored visits", count)
    require(row["arc_traversals_per_orbit"] == [trees[u] // common for u, _ in arcs], "stored edge uses", count)
    require(row["orbit_digest"] == digest_rows(sorted(encodings)), "orbit digest", count)


def validate(payload: dict) -> int:
    count = [0]
    require(payload.get("payload_sha256") == canonical_hash(payload), "payload hash", count)
    require(payload.get("schema") == "hcs-c181-rotor-router-strong-digraph-v1", "schema", count)
    require(payload.get("candidate_id") == "HCS-C181", "candidate", count)
    require(payload.get("evaluation_date") == "2026-08-26", "date", count)
    require(payload.get("scope_literal") == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope", count)
    require(payload.get("source_commit") == SOURCE, "source", count)
    require(payload["evaluator"]["authority_sha256"] == EVALUATOR, "evaluator", count)
    require(payload["evaluator"]["skill_version"] == "0.2.0", "version", count)
    require("every finite nonempty strongly connected directed multigraph" in payload["source_lock"]["family"], "full family", count)
    require(
        payload["source_lock"]["arithmetic_origin"]
        == "directed spanning-tree and Laplacian data only; no rational-prime or prime-power orbit correspondence is intrinsic",
        "arithmetic-origin lock",
        count,
    )
    require("no sink" in payload["source_lock"]["forbidden_recast"], "sandpile firewall", count)
    require(payload["route_a_verdict"] == {
        "A0": "A0_FAIL", "A1": "A1_WEAK", "A2": "A2_FAIL", "A3": "A3_FAIL",
        "A4": "A4_NATURAL_QUANTIZATION", "overall": "ROUTE_A_REJECTED",
        "a0_failure_forces_rejection": True, "route_b_invocation_allowed": False,
    }, "route tuple", count)
    require(len(payload["nonclaims"]) == 5, "nonclaims", count)

    graphs = payload["graph_rows"]
    require(len(graphs) == 1629, "graph row count", count)
    expected_simple_ids = []
    for n in range(2, 5):
        universe = [(u, v) for u in range(n) for v in range(n) if u != v]
        for mask in range(1, 1 << len(universe)):
            arcs = [arc for bit, arc in enumerate(universe) if mask & (1 << bit)]
            if connected(n, arcs):
                expected_simple_ids.append(f"simple-n{n}-mask{mask:0{len(universe)}b}")
    require(len(expected_simple_ids) == 1625, "strong graph census", count)
    require([x["graph_id"] for x in graphs[:1625]] == expected_simple_ids, "complete simple ledger", count)
    expected_multi = {
        "multi-one-vertex-three-loops": (1, [(0, 0), (0, 0), (0, 0)]),
        "multi-two-vertex-loops-parallel": (2, [(0, 0), (0, 1), (0, 1), (1, 0), (1, 1)]),
        "multi-three-cycle-parallel": (3, [(0, 1), (0, 1), (1, 2), (2, 0), (2, 0), (2, 2)]),
        "multi-two-vertex-eulerian-double": (2, [(0, 1), (0, 1), (1, 0), (1, 0)]),
    }
    require([x["graph_id"] for x in graphs[1625:]] == list(expected_multi), "multigraph sentinels", count)

    n4_rank = 0
    expected_audit_counts = {}
    for i, graph in enumerate(graphs):
        gid, n = graph["graph_id"], graph["n"]
        arcs = [tuple(x) for x in graph["arcs"]]
        require(connected(n, arcs), f"strong {gid}", count)
        if i < 1625:
            universe = [(u, v) for u in range(n) for v in range(n) if u != v]
            require(arcs == [arc for bit, arc in enumerate(universe) if graph["mask"] & (1 << bit)], "mask reconstruction", count)
            require(graph["kind"] == "labeled simple loopless exhaustive", "simple kind", count)
        else:
            require((n, arcs) == expected_multi[gid], "multi reconstruction", count)
            require(graph["kind"] == "directed multigraph sentinel with distinguished arcs", "multi kind", count)
        outd, ind, trees, common, period, states, eulerian = invariants(n, arcs)
        expected = {
            "outdegree": outd, "indegree": ind, "arborescence_t": trees, "M_gcd": common,
            "common_orbit_length_L": period, "unicycle_state_count": states, "eulerian": eulerian,
            "eulerian_tree_constant": trees[0] if eulerian else None,
        }
        for key, value in expected.items():
            require(graph[key] == value, f"{gid}:{key}", count)
        orders = all_orders(n, arcs)
        require(graph["all_cyclic_order_count"] == len(orders), "order count", count)
        if i >= 1625 or n <= 3:
            audited = len(orders)
        elif n == 4 and n4_rank < 128:
            audited = len(orders)
        else:
            audited = 1
        if n == 4 and i < 1625:
            n4_rank += 1
        require(graph["audited_cyclic_order_count"] == audited, "audited order count", count)
        expected_audit_counts[gid] = audited
        if eulerian:
            require(len(set(trees)) == 1 and period == len(arcs) and common == trees[0], "Eulerian degeneration", count)

    order_rows = payload["cyclic_order_rows"]
    require(len(order_rows) == 1697, "order ledger count", count)
    grouped: dict[str, list[dict]] = {}
    for row in order_rows:
        grouped.setdefault(row["graph_id"], []).append(row)
    require(set(grouped) == {g["graph_id"] for g in graphs}, "every graph audited", count)
    graph_map = {g["graph_id"]: g for g in graphs}
    for gid, rows in grouped.items():
        graph = graph_map[gid]
        all_os = all_orders(graph["n"], [tuple(x) for x in graph["arcs"]])
        require(len(rows) == expected_audit_counts[gid], "group audit count", count)
        require([r["order_index"] for r in rows] == list(range(len(rows))), "order indices", count)
        require([tuple(tuple(x) for x in r["cyclic_orders"]) for r in rows] == all_os[: len(rows)], "order prefix", count)
        for row in rows:
            validate_order(row, graph, count)

    counts = payload["counts"]
    require(counts["simple_strong_graphs_by_n"] == {"2": 1, "3": 18, "4": 1606}, "census", count)
    require(counts["simple_strong_graphs_total"] == 1625, "simple total", count)
    require(counts["multigraph_sentinels"] == 4 and counts["graph_rows_total"] == 1629, "graph totals", count)
    require(counts["cyclic_order_audits"] == 1697, "audit total", count)
    require(counts["unicycle_states_audited"] == sum(r["unicycle_states"] for r in order_rows), "state total", count)
    require(counts["rotor_orbits_audited"] == sum(r["orbit_count"] for r in order_rows), "orbit total", count)
    require(counts["extra_all_order_n4_graphs"] == 128, "n4 all-order cutoff", count)
    require(payload["theorem"]["zeta"] == "zeta_AM(z)=(1-z^L)^(-M), det(I-zU)=(1-z^L)^M", "zeta theorem", count)
    require("exactly M orbits" in payload["theorem"]["orbit_classification"], "orbit theorem", count)
    require("every arc is traversed once" in payload["theorem"]["eulerian"], "Eulerian theorem", count)
    return count[0]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path, default=DEFAULT_EVIDENCE)
    args = parser.parse_args()
    payload = json.loads(args.evidence.read_text())
    checks = validate(payload)
    print(json.dumps({"status": "C181_CHECKER_PASS", "assertions": checks, "payload_sha256": payload["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
