#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C259."""
from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c259_kuramoto_evidence.json"
SOURCE = "98782afe1e754c311ad0736f72ce09dcc7c85c77"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788048000
FLAGS = {
    "uses_target_zero_table",
    "uses_prime_table",
    "claims_arithmetic_local_data",
    "claims_euler_factors",
    "claims_root_numbers",
    "claims_automorphy",
    "claims_target_divisor_or_functional_equation",
    "claims_hilbert_polya_operator",
    "invokes_route_b",
}


def q(value: str) -> F:
    return F(value)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return sha256(raw.encode()).hexdigest()


def prufer_edges(n: int, word: tuple[int, ...]) -> list[tuple[int, int]]:
    """Independent smallest-leaf decoder using a mutable multiset."""
    occurrences = {vertex: word.count(vertex) for vertex in range(n)}
    available = {vertex for vertex in range(n) if occurrences[vertex] == 0}
    answer = []
    for symbol in word:
        leaf = min(available)
        available.remove(leaf)
        answer.append(tuple(sorted((leaf, symbol))))
        occurrences[symbol] -= 1
        if occurrences[symbol] == 0:
            available.add(symbol)
    left = sorted(available)
    answer.append((left[0], left[1]))
    return sorted(answer)


def root_edges(n: int, edges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    adjacency = {i: set() for i in range(n)}
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    seen = {0}
    frontier = [0]
    directed = []
    while frontier:
        parent = frontier.pop(0)
        for child in sorted(adjacency[parent] - seen):
            seen.add(child)
            frontier.append(child)
            directed.append((parent, child))
    return directed


def descendants(n: int, rooted: list[tuple[int, int]], child: int) -> set[int]:
    children = {i: [] for i in range(n)}
    for parent, vertex in rooted:
        children[parent].append(vertex)
    result = set()
    stack = [child]
    while stack:
        vertex = stack.pop()
        result.add(vertex)
        stack.extend(children[vertex])
    return result


def validate(data: dict) -> int:
    count = 0

    def check(condition: bool, label: str) -> None:
        nonlocal count
        count += 1
        if not condition:
            raise AssertionError(label)

    check(data["schema"] == "hcs-c259-tree-kuramoto-locking-morse-v1", "schema")
    check(data["candidate_id"] == "HCS-C259", "candidate")
    check(data["evaluation_date"] == "2026-08-31", "date")
    check(data["source_commit"] == SOURCE, "source")
    check(data["fixed_epoch"] == EPOCH, "epoch")
    check(data["scope_literal"] == SCOPE, "scope")
    check(data["evaluator"] == {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVAL}, "evaluator")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "verdict")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "route B")
    check(set(data["scope_flags"]) == FLAGS and not any(data["scope_flags"].values()), "scope flags")
    check(len(data["exact_identities"]) == 14, "identity count")
    check(len(data["citations"]) == 1 and data["citations"][0]["url"] == "https://doi.org/10.1007/BFb0013365", "source citation")
    check(len(data["nonclaims"]) == 5, "nonclaims")

    rows = data["regression"]["rows"]
    expected_total = sum(n ** (n - 2) for n in range(2, 8))
    check(len(rows) == expected_total == 18248, "tree count")
    check(data["regression"]["tree_count"] == expected_total, "declared tree count")
    check(data["regression"]["tree_count_by_n"] == {str(n): n ** (n - 2) for n in range(2, 8)}, "counts by n")
    observed_regimes = {"strict": 0, "saturated": 0, "violated": 0}
    cursor = 0
    for n in range(2, 8):
        for tree_index, word in enumerate(itertools.product(range(n), repeat=n - 2)):
            row = rows[cursor]
            cursor += 1
            check(row["n"] == n and row["tree_index"] == tree_index and tuple(row["prufer"]) == word, f"row identity {cursor}")
            undirected = prufer_edges(n, word)
            rooted = root_edges(n, undirected)
            check([tuple(edge) for edge in row["undirected_edges"]] == undirected, f"undirected {cursor}")
            check([tuple(edge) for edge in row["rooted_edges"]] == rooted, f"rooted {cursor}")
            check(len(undirected) == n - 1 and len(set(undirected)) == n - 1, f"tree edge count {cursor}")
            eta = [q(value) for value in row["eta"]]
            omega = [q(value) for value in row["omega"]]
            mean = q(row["omega_mean"])
            flows = [q(value) for value in row["cut_flows"]]
            couplings = [q(value) for value in row["couplings"]]
            check(sum(eta) == 0 and sum(omega) == n * mean, f"centering {cursor}")
            check([value - mean for value in omega] == eta, f"omega eta {cursor}")
            incidence_flow = [F(0) for _ in range(n)]
            for (parent, child), flow in zip(rooted, flows):
                incidence_flow[parent] -= flow
                incidence_flow[child] += flow
            check(incidence_flow == eta, f"Bf eta {cursor}")
            for edge_index, ((_, child), flow) in enumerate(zip(rooted, flows)):
                subtree = descendants(n, rooted, child)
                check(sum(eta[vertex] for vertex in subtree) == flow, f"cut {cursor}:{edge_index}")

            strict = [i for i, (flow, coupling) in enumerate(zip(flows, couplings)) if abs(flow) < coupling]
            saturated = [i for i, (flow, coupling) in enumerate(zip(flows, couplings)) if abs(flow) == coupling]
            violated = [i for i, (flow, coupling) in enumerate(zip(flows, couplings)) if abs(flow) > coupling]
            regime = "violated" if violated else "saturated" if saturated else "strict"
            observed_regimes[regime] += 1
            check(row["regime"] == regime, f"regime {cursor}")
            check(row["strict_edges"] == strict and row["saturated_edges"] == saturated and row["violated_edges"] == violated, f"edge classes {cursor}")
            cosines = row["cosine_absolute"]
            for edge_index in strict:
                cosine = q(cosines[edge_index])
                check(cosine > 0 and (flows[edge_index] / couplings[edge_index]) ** 2 + cosine ** 2 == 1, f"unit circle {cursor}:{edge_index}")
            for edge_index in saturated:
                check(q(cosines[edge_index]) == 0, f"saturated cosine {cursor}:{edge_index}")
            for edge_index in violated:
                check(cosines[edge_index] is None, f"violated cosine {cursor}:{edge_index}")

            if violated:
                check(row["branch_count_mod_rotation"] == 0, f"no branches {cursor}")
                check(row["stable_branch_count"] == 0, f"no stable {cursor}")
                check(row["reduced_hessian_nullity"] is None, f"no Hessian {cursor}")
                check(row["morse_index_histogram"] == {}, f"no histogram {cursor}")
            else:
                histogram = {k: 0 for k in range(len(strict) + 1)}
                branch_count = 0
                for signs in itertools.product((1, -1), repeat=len(strict)):
                    index = sum(sign < 0 for sign in signs)
                    histogram[index] += 1
                    branch_count += 1
                check(branch_count == 2 ** len(strict) == row["branch_count_mod_rotation"], f"branch enumeration {cursor}")
                check({str(k): value for k, value in histogram.items()} == row["morse_index_histogram"], f"Morse histogram {cursor}")
                check(sum(histogram.values()) == row["branch_count_mod_rotation"], f"histogram total {cursor}")
                check(row["reduced_hessian_nullity"] == len(saturated), f"nullity {cursor}")
                check(row["stable_branch_count"] == (1 if not saturated else 0), f"stable branch {cursor}")
                check(all(histogram[k] == math.comb(len(strict), k) for k in histogram), f"binomial inertia {cursor}")

    check(cursor == expected_total, "cursor")
    check(observed_regimes == data["regression"]["regime_counts"], "regime counts")
    check(len(data["regression"]["boundary_rows"]) == data["regression"]["boundary_row_count"] == 6, "boundaries")
    check("No classification of all unlocked running states" in data["theorem"]["boundary_scope"], "running-state firewall")
    return count


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    assertions = validate(data)
    print(f"C259 independent checker: PASS ({assertions} assertions; all Prüfer trees, cut flows, branches, inertia and boundaries)")


if __name__ == "__main__":
    main()
