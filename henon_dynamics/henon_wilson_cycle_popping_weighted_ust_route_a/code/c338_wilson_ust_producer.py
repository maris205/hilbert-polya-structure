#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C338."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c338_wilson_ust_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C338/2026-09-03.yaml"
SOURCE = "db2c816b7b6bd450f51f79b91842cb882b0bd773"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
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


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {
    key: [(tag, rx) for tag, rx in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("duplicate or non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def encode(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def determinant(matrix):
    n = len(matrix)
    if n == 0:
        return Fraction(1)
    work = [[Fraction(value) for value in row] for row in matrix]
    answer = Fraction(1)
    for column in range(n):
        pivot = next((row for row in range(column, n) if work[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            answer = -answer
        value = work[column][column]
        answer *= value
        for j in range(column, n):
            work[column][j] /= value
        for row in range(column + 1, n):
            factor = work[row][column]
            if factor:
                for j in range(column, n):
                    work[row][j] -= factor * work[column][j]
    return answer


def inverse(matrix):
    n = len(matrix)
    if n == 0:
        return []
    work = [[Fraction(value) for value in row] + [Fraction(i == j) for j in range(n)]
            for i, row in enumerate(matrix)]
    for column in range(n):
        pivot = next(row for row in range(column, n) if work[row][column])
        work[column], work[pivot] = work[pivot], work[column]
        value = work[column][column]
        work[column] = [item / value for item in work[column]]
        for row in range(n):
            if row == column:
                continue
            factor = work[row][column]
            if factor:
                work[row] = [work[row][j] - factor * work[column][j] for j in range(2 * n)]
    return [row[n:] for row in work]


def connected(n, edges):
    if n == 1:
        return True
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v, *_ in edges:
        a, b = find(u), find(v)
        if a != b:
            parent[a] = b
    return len({find(vertex) for vertex in range(n)}) == 1


def is_tree(n, edges, mask):
    if mask.bit_count() != n - 1:
        return False
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for index, edge in enumerate(edges):
        if not (mask >> index) & 1:
            continue
        u, v = edge[:2]
        a, b = find(u), find(v)
        if a == b:
            return False
        parent[a] = b
    return n == 1 or len({find(vertex) for vertex in range(n)}) == 1


def laplacian(n, edges, weights):
    matrix = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for (u, v, *_), weight in zip(edges, weights):
        matrix[u][u] += weight
        matrix[v][v] += weight
        matrix[u][v] -= weight
        matrix[v][u] -= weight
    return matrix


def reduced(matrix, root):
    return [[value for j, value in enumerate(row) if j != root]
            for i, row in enumerate(matrix) if i != root]


def transfer_kernel(n, edges, weights, root):
    lap = laplacian(n, edges, weights)
    inv = inverse(reduced(lap, root))
    vectors = []
    for u, v, *_ in edges:
        full = [Fraction(0) for _ in range(n)]
        full[u], full[v] = Fraction(1), Fraction(-1)
        vectors.append([value for index, value in enumerate(full) if index != root])
    kernel = []
    for i, left in enumerate(vectors):
        row = []
        for j, right in enumerate(vectors):
            bilinear = sum(left[a] * inv[a][b] * right[b]
                           for a in range(n - 1) for b in range(n - 1))
            # Store the conductance-weighted, nonsymmetric transfer-current
            # kernel H_ef=c_f b_e^T L^+b_f.  Principal minors equal those of
            # the symmetric square-root kernel and remain rational.
            row.append(bilinear * weights[j])
        kernel.append(row)
    return lap, kernel


def tree_ledger(n, edges, weights):
    rows = []
    for mask in range(1 << len(edges)):
        if is_tree(n, edges, mask):
            weight = math.prod(weights[index] for index in range(len(edges)) if (mask >> index) & 1)
            rows.append((mask, int(weight)))
    return rows


def inclusion_numerators(edge_count, trees):
    return [sum(weight for tree, weight in trees if tree & subset == subset)
            for subset in range(1 << edge_count)]


def simple_graph_rows():
    rows = []
    for n in range(1, 6):
        complete = [(u, v) for u in range(n) for v in range(u + 1, n)]
        for graph_mask in range(1 << len(complete)):
            edges = [complete[index] for index in range(len(complete)) if (graph_mask >> index) & 1]
            if not connected(n, edges):
                continue
            weights = [1] * len(edges)
            lap, kernel = transfer_kernel(n, edges, weights, 0)
            trees = tree_ledger(n, edges, weights)
            rows.append({
                "n": n,
                "graph_mask": graph_mask,
                "oriented_edges": [[u, v] for u, v in edges],
                "root": 0,
                "tree_masks": [mask for mask, _ in trees],
                "tree_partition": sum(weight for _, weight in trees),
                "reduced_laplacian_determinant": int(determinant(reduced(lap, 0))),
                "transfer_current_kernel": [[encode(value) for value in row] for row in kernel],
                "all_subset_inclusion_numerators": inclusion_numerators(len(edges), trees),
            })
    return rows


def weighted_cases():
    rows = []
    for case in range(24):
        n = 2 + case % 4
        endpoints = [(vertex, vertex + 1) for vertex in range(n - 1)]
        endpoints.append((0, 1))  # a labelled parallel edge, including n=2
        if n >= 3:
            endpoints.append((0, n - 1))
        if n >= 4:
            endpoints.extend([(0, 2), (1, 3)])
        if n == 5:
            endpoints.append((2, 4))
            if case % 2:
                endpoints.append((0, 3))
        edges = [(u, v, f"e{index}") for index, (u, v) in enumerate(endpoints)]
        weights = [1 + ((3 * case + 5 * index) % 9) for index in range(len(edges))]
        root = case % n
        lap, kernel = transfer_kernel(n, edges, weights, root)
        trees = tree_ledger(n, edges, weights)
        rows.append({
            "case": case,
            "n": n,
            "root": root,
            "oriented_labelled_edges": [[u, v, label, weights[index]]
                                          for index, (u, v, label) in enumerate(edges)],
            "weighted_tree_rows": [{"mask": mask, "weight": weight} for mask, weight in trees],
            "tree_partition": sum(weight for _, weight in trees),
            "reduced_laplacian_determinant": int(determinant(reduced(lap, root))),
            "transfer_current_kernel": [[encode(value) for value in row] for row in kernel],
            "all_subset_inclusion_numerators": inclusion_numerators(len(edges), trees),
        })
    return rows


def stack_targets(n, edges, root, stacks, counts, vertices):
    targets, visible = {}, {}
    for index, vertex in enumerate(vertices):
        edge_index = stacks[index][counts[index]]
        u, v = edges[edge_index]
        targets[vertex] = v if vertex == u else u
        visible[vertex] = edge_index
    return targets, visible


def visible_cycles(targets, root):
    cycles = set()
    done = set()
    for start in sorted(targets):
        if start in done:
            continue
        path, position = [], {}
        vertex = start
        while vertex != root and vertex in targets and vertex not in done:
            if vertex in position:
                cycle = tuple(path[position[vertex]:])
                rotations = [cycle[index:] + cycle[:index] for index in range(len(cycle))]
                cycles.add(min(rotations))
                break
            position[vertex] = len(path)
            path.append(vertex)
            vertex = targets[vertex]
        done.update(path)
    return sorted(cycles)


def explore_stack(n, edges, root, stacks, depth):
    vertices = tuple(vertex for vertex in range(n) if vertex != root)
    memo = {}

    def visit(counts):
        if counts in memo:
            return memo[counts]
        if any(value >= depth for value in counts):
            answer = (frozenset(), True)
            memo[counts] = answer
            return answer
        targets, visible = stack_targets(n, edges, root, stacks, counts, vertices)
        cycles = visible_cycles(targets, root)
        if not cycles:
            terminal = (counts, tuple(visible[vertex] for vertex in vertices))
            answer = (frozenset({terminal}), False)
            memo[counts] = answer
            return answer
        terminals, exhausted = set(), False
        index_of = {vertex: index for index, vertex in enumerate(vertices)}
        for cycle in cycles:
            changed = list(counts)
            for vertex in cycle:
                changed[index_of[vertex]] += 1
            child_terminals, child_exhausted = visit(tuple(changed))
            terminals.update(child_terminals)
            exhausted = exhausted or child_exhausted
        answer = (frozenset(terminals), exhausted)
        memo[counts] = answer
        return answer

    return visit((0,) * len(vertices))


def canonical_wilson(n, edges, root, stacks, depth):
    vertices = tuple(vertex for vertex in range(n) if vertex != root)
    index_of = {vertex: index for index, vertex in enumerate(vertices)}
    counts = [0] * len(vertices)
    accepted, tree = {}, {root}
    for start in range(n):
        if start in tree:
            continue
        path = [start]
        position = {start: 0}
        while path[-1] not in tree:
            vertex = path[-1]
            slot = index_of[vertex]
            if counts[slot] >= depth:
                return None
            edge_index = stacks[slot][counts[slot]]
            u, v = edges[edge_index]
            target = v if vertex == u else u
            if target in tree:
                for path_vertex in path:
                    path_slot = index_of[path_vertex]
                    accepted[path_vertex] = stacks[path_slot][counts[path_slot]]
                tree.update(path)
                break
            if target in position:
                first = position[target]
                for cycle_vertex in path[first:]:
                    counts[index_of[cycle_vertex]] += 1
                    if counts[index_of[cycle_vertex]] >= depth:
                        return None
                path = path[:first + 1]
                position = {value: index for index, value in enumerate(path)}
            else:
                position[target] = len(path)
                path.append(target)
    return tuple(counts), tuple(accepted[vertex] for vertex in vertices)


def stack_audit():
    depth = 2
    totals = {n: {"n": n, "rooted_graphs": 0, "stack_tables": 0,
                  "terminating_tables": 0, "exhausted_tables": 0,
                  "abelian_failures": 0, "wilson_failures": 0,
                  "maximum_popped_cards": 0} for n in range(1, 5)}
    for n in range(1, 5):
        complete = [(u, v) for u in range(n) for v in range(u + 1, n)]
        for graph_mask in range(1 << len(complete)):
            edges = [complete[index] for index in range(len(complete)) if (graph_mask >> index) & 1]
            if not connected(n, edges):
                continue
            incident = {vertex: [index for index, (u, v) in enumerate(edges) if vertex in (u, v)]
                        for vertex in range(n)}
            for root in range(n):
                totals[n]["rooted_graphs"] += 1
                vertices = tuple(vertex for vertex in range(n) if vertex != root)
                options = [list(itertools.product(incident[vertex], repeat=depth)) for vertex in vertices]
                table_iterator = itertools.product(*options) if options else [()]
                for stacks in table_iterator:
                    totals[n]["stack_tables"] += 1
                    terminals, exhausted = explore_stack(n, edges, root, stacks, depth)
                    canonical = canonical_wilson(n, edges, root, stacks, depth)
                    if exhausted:
                        totals[n]["exhausted_tables"] += 1
                    if terminals:
                        totals[n]["terminating_tables"] += 1
                        if len(terminals) != 1 or exhausted:
                            totals[n]["abelian_failures"] += 1
                        terminal = next(iter(terminals))
                        if canonical != terminal:
                            totals[n]["wilson_failures"] += 1
                        totals[n]["maximum_popped_cards"] = max(
                            totals[n]["maximum_popped_cards"], sum(terminal[0]))
                    elif canonical is not None:
                        totals[n]["wilson_failures"] += 1
    return list(totals.values())


def leaves(value):
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def produce(evaluation_path: Path):
    evaluation = strict_yaml(evaluation_path)
    graphs = simple_graph_rows()
    weighted = weighted_cases()
    stacks = stack_audit()
    data = {
        "schema": "hcs-c338-wilson-weighted-ust-v1",
        "candidate_id": "HCS-C338",
        "obstruction_id": "HEN-O322",
        "evaluation_date": "2026-09-03",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR,
                      "authority": "flow_systems/skills/route-a-evaluator.md"},
        "model": {
            "graph": "finite connected loopless undirected multigraph with distinctly labelled parallel edges",
            "conductances": "one positive conductance c_e per labelled edge",
            "root": "one arbitrary vertex r; root has no stack",
            "stack_law": "independent infinite outgoing-edge stacks with probability c_e/c(v)",
            "legal_update": "pop every visible card on any currently visible directed cycle",
            "wilson_rule": "fixed increasing vertex order with chronological loop erasure",
            "edge_orientation": "one frozen arbitrary orientation per labelled undirected edge",
            "laplacian": "L=B diag(c) B^T for incidence columns b_e=delta_tail-delta_head",
            "transfer_current": "H_ef=c_f b_e^T L^+ b_f; principal minors equal the symmetric sqrt(c) kernel minors",
        },
        "theorem_contract": {
            "abelian": "if one legal cycle-pop sequence terminates then every legal order terminates with identical pop counts and terminal tree",
            "termination": "for independent infinite stacks every legal cycle-pop order terminates almost surely",
            "lerw": "the canonical legal pop order is Wilson chronological loop-erased random walk for every vertex order",
            "tree_law": "Pr(T)=product_{e in T} c_e/Z_c for every labelled spanning tree",
            "matrix_tree": "Z_c=det L^(r) for every root r",
            "transfer_current": "Pr(e_1,...,e_k in T)=det(H_{e_i,e_j}) for distinct labelled edges",
            "boundaries": "singleton, already-a-tree, parallel-edge, and root-change cases are included",
        },
        "finite_grid": {
            "simple_graphs": "all connected labelled simple graphs on one through five vertices",
            "weighted_cases": 24,
            "stack_depth": 2,
            "stack_graphs": "all connected labelled simple graphs on one through four vertices and all roots",
            "arithmetic": "exact integers and rational Gaussian elimination",
        },
        "graph_rows": graphs,
        "weighted_case_rows": weighted,
        "stack_audit_rows": stacks,
        "route_a_yaml": {
            "relative_path": "evaluations/route_a/HCS-C338/2026-09-03.yaml",
            "raw_sha256": hashlib.sha256(evaluation_path.read_bytes()).hexdigest(),
            "semantic_sha256": hashlib.sha256(json.dumps(
                evaluation, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest(),
        },
        "collision_boundary": {
            "C176": "sandpile translations and recurrent-state Fourier spectra, not random spanning-tree sampling or edge determinants",
            "C181": "deterministic rotor-router torsors, not independent resampling stacks or the weighted UST law",
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": FLAGS,
        "nonclaims": [
            "The spanning-tree partition polynomial is a source combinatorial normalization, not a target Euler factor or target zeta function.",
            "Finite enumeration audits conventions and implementations but does not prove the infinite-stack theorem.",
            "No target arithmetic local data, root number, automorphy, target divisor, functional equation, target zero match, literature priority, or Hilbert--Polya operator is asserted.",
            "No infinite graph, directed nonreversible chain, negative conductance, or unlabelled-parallel-edge quotient is claimed.",
        ],
        "references": [
            {"authors": "David Bruce Wilson", "title": "Generating random spanning trees more quickly than the cover time", "identifier": "DOI:10.1145/237814.237880"},
            {"authors": "Robert Burton and Robin Pemantle", "title": "Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings Via Transfer-Impedances", "identifier": "DOI:10.1214/aop/1176989121"},
            {"authors": "Gustav Kirchhoff", "title": "Ueber die Aufloesung der Gleichungen, auf welche man bei der Untersuchung der linearen Vertheilung galvanischer Stroeme gefuehrt wird", "identifier": "DOI:10.1002/andp.18471481202"},
            {"authors": "Seth Chaiken", "title": "A Combinatorial Proof of the All Minors Matrix Tree Theorem", "identifier": "DOI:10.1137/0603033"},
            {"authors": "Russell Lyons and Yuval Peres", "title": "Probability on Trees and Networks", "identifier": "ISBN:978-1-107-16015-6"},
        ],
    }
    simple_subset_events = sum(len(row["all_subset_inclusion_numerators"]) for row in graphs)
    weighted_subset_events = sum(len(row["all_subset_inclusion_numerators"]) for row in weighted)
    counted = dict(data)
    data["enumeration"] = {
        "connected_simple_graphs": len(graphs),
        "simple_graph_tree_pairs": sum(len(row["tree_masks"]) for row in graphs),
        "simple_transfer_subset_events": simple_subset_events,
        "weighted_multigraph_cases": len(weighted),
        "weighted_tree_rows": sum(len(row["weighted_tree_rows"]) for row in weighted),
        "weighted_transfer_subset_events": weighted_subset_events,
        "rooted_stack_graphs": sum(row["rooted_graphs"] for row in stacks),
        "finite_stack_tables": sum(row["stack_tables"] for row in stacks),
        "audited_leaf_count": leaves(counted),
    }
    body = dict(data)
    data["payload_sha256"] = hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    return data


def main():
    if sys.flags.optimize:
        raise RuntimeError("C338 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    data = produce(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C338_PRODUCER_PASS graphs={data['enumeration']['connected_simple_graphs']} "
          f"tree_pairs={data['enumeration']['simple_graph_tree_pairs']} "
          f"subset_events={data['enumeration']['simple_transfer_subset_events']} "
          f"stack_tables={data['enumeration']['finite_stack_tables']}")


if __name__ == "__main__":
    main()
