#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C338."""
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
DEFAULT = ROOT / "results/c338_wilson_ust_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C338/2026-09-03.yaml"
SOURCE = "db2c816b7b6bd450f51f79b91842cb882b0bd773"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW = "6fb6f931958632647dc29888e728ba08fedb1657dee2bc529cbf87e23008a981"
YAML_SEMANTIC = "9555a89d78499a4125b90b0c9a3db1ac64a83f369cecbbea31e5a8da77d85325"
GRAPH_ROWS_SHA = "f7991907f9bf4c2e0fa8f43d945acdcb2ef7478f452ce1ce6ccc63535398fb8e"
WEIGHTED_ROWS_SHA = "8cceee0707240b3b2329b34946da97cc39ee43d5ffba03367ea65644328deccb"
STACK_ROWS_SHA = "8dd519d46da54731e0f879be754a168018e27813698259ec9496079d10ff8279"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
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
EXPECTED_EVALUATION = yaml.safe_load(r"""
schema: route-a-evaluation-v0.2.0
candidate_id: HCS-C338
title: Wilson cycle-popping, weighted spanning trees, and transfer current
evaluation_date: '2026-09-03'
source_commit: db2c816b7b6bd450f51f79b91842cb882b0bd773
fixed_epoch: 1788393600
scope_literal: NO_BAD_EULER_OR_ROOT_NUMBER
evaluator_authority: flow_systems/skills/route-a-evaluator.md
evaluator_version: 0.2.0
evaluator_authority_sha256: 6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c
obstruction_id: HEN-O322
candidate_definition: Wilson cycle-popping on a finite connected loopless undirected conductance multigraph
family: stochastic stack dynamics and weighted spanning-tree determinantal process
phase_space: independent infinite outgoing-edge stacks at every nonroot vertex
dynamics: pop all visible cards on any currently visible directed cycle
parameters: finite labelled multigraph, positive edge conductances, arbitrary root, arbitrary legal cycle rule
parameter_provenance: source graph and conductances only, never target-fitted
arithmetic_origin: none
clock: source number of popped stack cards or Wilson random-walk steps
normalization: weighted tree partition Z_c equals any reduced conductance-Laplacian determinant
determinant_convention: transfer current H_ef equals c_f times b_e transpose L pseudoinverse b_f for frozen edge orientations
orbit_cutoff: none; every finite graph theorem is exact and finite-stack enumeration is receipt-only
precision: exact integers and rational Gaussian elimination
training_data: none
forbidden_data: target arithmetic local data, Euler factors, root numbers, automorphy, target divisor or functional equation, target zeros, Hilbert-Polya operators, Route B
artifact_paths:
  - results/c338_wilson_ust_evidence.json
  - THEOREM_PACKAGE.md
  - paper/main.pdf
a0:
  verdict: A0_FAIL
  evidence_status: PROVED
  strongest_evidence: the conductance graph and spanning-tree law are exact source objects
  strongest_failure: no intrinsic rational-prime or prime-power correspondence, logarithmic prime clock, or arithmetic weight is present
a1:
  verdict: A1_FAIL
  evidence_status: PROVED
  strongest_evidence: cycle popping and loop erasure are exact stochastic path decompositions
  strongest_failure: popped directed cycles are resampling events rather than an isolated primitive-periodic-orbit ledger carrying arithmetic information
a2:
  verdict: A2_FAIL
  evidence_status: STOP_SCOPED
  strongest_evidence: the weighted tree partition is a finite source polynomial
  strongest_failure: no primitive-orbit dynamical zeta or target Fredholm determinant is defined
a3:
  verdict: A3_FAIL
  evidence_status: STOP_SCOPED
  strongest_evidence: transfer-current edge events form exact finite determinants
  strongest_failure: these source minors provide neither target analytic continuation nor a target divisor or Weil compression
a4:
  verdict: A4_FORMAL_HINT
  evidence_status: PROVED
  strongest_evidence: the symmetric square-root transfer-current kernel is an orthogonal projection on edge space
  strongest_failure: a finite determinantal projection is not a same-clock unitary, scattering, Hamiltonian, or Hilbert-Polya construction
tuple: [A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FORMAL_HINT]
overall_verdict: ROUTE_A_REJECTED
route_b_invocation_allowed: false
route_b_lock_reason: the finite projection hint is below A4_ROUTE_B_READY and all arithmetic and target determinant layers fail
scope_flags:
  claims_target_arithmetic_local_data: false
  claims_target_euler_factors: false
  claims_root_number: false
  claims_automorphy: false
  claims_target_divisor_or_counting_law: false
  claims_target_functional_equation: false
  claims_target_zero_match: false
  claims_hilbert_polya_operator: false
  invokes_route_b: false
theorem_status: PROVABLE_AS_STATED
finite_evidence_role: convention and implementation receipt, not proof
source_owner_tokens: [10.1145/237814.237880, 10.1214/aop/1176989121, 10.1002/andp.18471481202, 10.1137/0603033, 978-1-107-16015-6]
""")


def duplicate_pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def strict_json(path):
    value = json.loads(path.read_text(), object_pairs_hook=duplicate_pairs,
                       parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if type(value) is not dict:
        raise TypeError("JSON root")
    return value


class StrictLoader(yaml.SafeLoader):
    pass


StrictLoader.yaml_implicit_resolvers = {
    key: [(tag, rx) for tag, rx in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("duplicate or non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors or aliases forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def need(condition, label):
    if not condition:
        raise AssertionError(label)


def exact_keys(value, keys, label):
    need(type(value) is dict and set(value) == set(keys), f"{label} keys")


def parse_fraction(value):
    need(type(value) is str, "fraction type")
    return Fraction(value)


def det(matrix):
    size = len(matrix)
    if size == 0:
        return Fraction(1)
    work = [[Fraction(item) for item in row] for row in matrix]
    sign = 1
    for column in range(size):
        pivot = next((row for row in range(column, size) if work[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            work[pivot], work[column] = work[column], work[pivot]
            sign *= -1
        for row in range(column + 1, size):
            if work[row][column]:
                ratio = work[row][column] / work[column][column]
                for j in range(column, size):
                    work[row][j] -= ratio * work[column][j]
    return Fraction(sign) * math.prod(work[index][index] for index in range(size))


def solve_columns(matrix):
    size = len(matrix)
    if size == 0:
        return []
    columns = []
    for rhs_index in range(size):
        work = [[Fraction(matrix[i][j]) for j in range(size)] + [Fraction(i == rhs_index)]
                for i in range(size)]
        for column in range(size):
            pivot = next(row for row in range(column, size) if work[row][column])
            work[column], work[pivot] = work[pivot], work[column]
            scale = work[column][column]
            work[column] = [value / scale for value in work[column]]
            for row in range(size):
                if row != column and work[row][column]:
                    scale = work[row][column]
                    work[row] = [work[row][j] - scale * work[column][j]
                                 for j in range(size + 1)]
        columns.append([work[row][-1] for row in range(size)])
    return [[columns[j][i] for j in range(size)] for i in range(size)]


def components(n, edges):
    groups = [{vertex} for vertex in range(n)]
    for edge in edges:
        u, v = edge[:2]
        left = next(group for group in groups if u in group)
        right = next(group for group in groups if v in group)
        if left is not right:
            left.update(right)
            groups.remove(right)
    return len(groups)


def tree(n, edges, mask):
    chosen = [edge for index, edge in enumerate(edges) if (mask >> index) & 1]
    return len(chosen) == n - 1 and components(n, chosen) == 1


def lap_and_kernel(n, edges, weights, root):
    lap = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for edge, weight in zip(edges, weights):
        u, v = edge[:2]
        for i, j, sign in ((u, u, 1), (v, v, 1), (u, v, -1), (v, u, -1)):
            lap[i][j] += sign * weight
    minor = [[lap[i][j] for j in range(n) if j != root] for i in range(n) if i != root]
    inverse = solve_columns(minor)
    vectors = []
    for edge in edges:
        u, v = edge[:2]
        vector = [Fraction(index == u) - Fraction(index == v) for index in range(n) if index != root]
        vectors.append(vector)
    kernel = [[sum(vectors[i][a] * inverse[a][b] * vectors[j][b]
                       for a in range(n - 1) for b in range(n - 1)) * weights[j]
               for j in range(len(edges))] for i in range(len(edges))]
    return minor, kernel


def all_trees(n, edges, weights):
    return [(mask, math.prod(weights[i] for i in range(len(edges)) if (mask >> i) & 1))
            for mask in range(1 << len(edges)) if tree(n, edges, mask)]


def principal(matrix, mask):
    indices = [index for index in range(len(matrix)) if (mask >> index) & 1]
    return [[matrix[i][j] for j in indices] for i in indices]


def graph_specs():
    for n in range(1, 6):
        complete = [(u, v) for u in range(n) for v in range(u + 1, n)]
        for graph_mask in range(1 << len(complete)):
            edges = [edge for index, edge in enumerate(complete) if (graph_mask >> index) & 1]
            if components(n, edges) == 1:
                yield n, graph_mask, edges


def weighted_specs():
    for case in range(24):
        n = 2 + case % 4
        endpoints = [(v, v + 1) for v in range(n - 1)] + [(0, 1)]
        if n >= 3:
            endpoints += [(0, n - 1)]
        if n >= 4:
            endpoints += [(0, 2), (1, 3)]
        if n == 5:
            endpoints += [(2, 4)] + ([(0, 3)] if case % 2 else [])
        edges = [(u, v, f"e{i}") for i, (u, v) in enumerate(endpoints)]
        weights = [1 + ((3 * case + 5 * i) % 9) for i in range(len(edges))]
        yield case, n, case % n, edges, weights


def cycles_from_targets(targets, root):
    answer = set()
    for start in sorted(targets):
        trail, at = [], {}
        vertex = start
        while vertex != root and vertex in targets and vertex not in at:
            at[vertex] = len(trail)
            trail.append(vertex)
            vertex = targets[vertex]
        if vertex in at:
            cyc = tuple(trail[at[vertex]:])
            answer.add(min(cyc[i:] + cyc[:i] for i in range(len(cyc))))
    return sorted(answer)


def finite_outcomes(n, edges, root, stacks, depth):
    vertices = tuple(v for v in range(n) if v != root)
    position = {v: i for i, v in enumerate(vertices)}
    frontier = {(0,) * len(vertices)}
    visited, terminal, exhausted = set(), set(), False
    while frontier:
        counts = frontier.pop()
        if counts in visited:
            continue
        visited.add(counts)
        if any(value >= depth for value in counts):
            exhausted = True
            continue
        targets, visible = {}, []
        for i, vertex in enumerate(vertices):
            edge_index = stacks[i][counts[i]]
            u, v = edges[edge_index]
            targets[vertex] = v if vertex == u else u
            visible.append(edge_index)
        cycles = cycles_from_targets(targets, root)
        if not cycles:
            terminal.add((counts, tuple(visible)))
        for cycle in cycles:
            changed = list(counts)
            for vertex in cycle:
                changed[position[vertex]] += 1
            frontier.add(tuple(changed))
    return terminal, exhausted


def wilson_outcome(n, edges, root, stacks, depth):
    vertices = tuple(v for v in range(n) if v != root)
    position = {v: i for i, v in enumerate(vertices)}
    counts, accepted, built = [0] * len(vertices), {}, {root}
    for start in range(n):
        if start in built:
            continue
        walk, locations = [start], {start: 0}
        while walk[-1] not in built:
            vertex = walk[-1]
            slot = position[vertex]
            if counts[slot] >= depth:
                return None
            edge_index = stacks[slot][counts[slot]]
            u, v = edges[edge_index]
            target = v if u == vertex else u
            if target in built:
                for value in walk:
                    accepted[value] = stacks[position[value]][counts[position[value]]]
                built.update(walk)
                break
            if target in locations:
                first = locations[target]
                for value in walk[first:]:
                    counts[position[value]] += 1
                    if counts[position[value]] >= depth:
                        return None
                walk = walk[:first + 1]
                locations = {value: i for i, value in enumerate(walk)}
            else:
                locations[target] = len(walk)
                walk.append(target)
    return tuple(counts), tuple(accepted[v] for v in vertices)


def recompute_stack_rows():
    depth = 2
    rows = []
    for n in range(1, 5):
        row = {"n": n, "rooted_graphs": 0, "stack_tables": 0,
               "terminating_tables": 0, "exhausted_tables": 0,
               "abelian_failures": 0, "wilson_failures": 0,
               "maximum_popped_cards": 0}
        complete = [(u, v) for u in range(n) for v in range(u + 1, n)]
        for graph_mask in range(1 << len(complete)):
            edges = [edge for i, edge in enumerate(complete) if (graph_mask >> i) & 1]
            if components(n, edges) != 1:
                continue
            incident = {v: [i for i, edge in enumerate(edges) if v in edge] for v in range(n)}
            for root in range(n):
                row["rooted_graphs"] += 1
                vertices = tuple(v for v in range(n) if v != root)
                options = [list(itertools.product(incident[v], repeat=depth)) for v in vertices]
                tables = itertools.product(*options) if options else [()]
                for stacks in tables:
                    row["stack_tables"] += 1
                    terminals, exhausted = finite_outcomes(n, edges, root, stacks, depth)
                    canonical = wilson_outcome(n, edges, root, stacks, depth)
                    if exhausted:
                        row["exhausted_tables"] += 1
                    if terminals:
                        row["terminating_tables"] += 1
                        if len(terminals) != 1 or exhausted:
                            row["abelian_failures"] += 1
                        only = next(iter(terminals))
                        if canonical != only:
                            row["wilson_failures"] += 1
                        row["maximum_popped_cards"] = max(row["maximum_popped_cards"], sum(only[0]))
                    elif canonical is not None:
                        row["wilson_failures"] += 1
        rows.append(row)
    return rows


def leaves(value):
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def main():
    if sys.flags.optimize:
        raise RuntimeError("C338 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    root_keys = {"schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch",
                 "source_commit", "scope_literal", "evaluator", "model", "theorem_contract",
                 "finite_grid", "graph_rows", "weighted_case_rows", "stack_audit_rows",
                 "route_a_yaml", "collision_boundary", "route_a", "scope_flags", "nonclaims",
                 "references", "enumeration", "payload_sha256"}
    exact_keys(data, root_keys, "root")
    fixed = {"schema": "hcs-c338-wilson-weighted-ust-v1", "candidate_id": "HCS-C338",
             "obstruction_id": "HEN-O322", "evaluation_date": "2026-09-03",
             "fixed_epoch": 1788393600, "source_commit": SOURCE, "scope_literal": SCOPE}
    for key, expected in fixed.items():
        need(data[key] == expected, key)
    need(data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR,
                               "authority": "flow_systems/skills/route-a-evaluator.md"}, "evaluator")
    body = dict(data)
    claimed_payload = body.pop("payload_sha256")
    actual_payload = hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    need(claimed_payload == actual_payload, "payload hash")
    expected_model = {
        "graph": "finite connected loopless undirected multigraph with distinctly labelled parallel edges",
        "conductances": "one positive conductance c_e per labelled edge",
        "root": "one arbitrary vertex r; root has no stack",
        "stack_law": "independent infinite outgoing-edge stacks with probability c_e/c(v)",
        "legal_update": "pop every visible card on any currently visible directed cycle",
        "wilson_rule": "fixed increasing vertex order with chronological loop erasure",
        "edge_orientation": "one frozen arbitrary orientation per labelled undirected edge",
        "laplacian": "L=B diag(c) B^T for incidence columns b_e=delta_tail-delta_head",
        "transfer_current": "H_ef=c_f b_e^T L^+ b_f; principal minors equal the symmetric sqrt(c) kernel minors",
    }
    need(data["model"] == expected_model, "model")
    need(data["theorem_contract"] == {
        "abelian": "if one legal cycle-pop sequence terminates then every legal order terminates with identical pop counts and terminal tree",
        "termination": "for independent infinite stacks every legal cycle-pop order terminates almost surely",
        "lerw": "the canonical legal pop order is Wilson chronological loop-erased random walk for every vertex order",
        "tree_law": "Pr(T)=product_{e in T} c_e/Z_c for every labelled spanning tree",
        "matrix_tree": "Z_c=det L^(r) for every root r",
        "transfer_current": "Pr(e_1,...,e_k in T)=det(H_{e_i,e_j}) for distinct labelled edges",
        "boundaries": "singleton, already-a-tree, parallel-edge, and root-change cases are included",
    }, "theorem contract")
    need(data["finite_grid"] == {
        "simple_graphs": "all connected labelled simple graphs on one through five vertices",
        "weighted_cases": 24,
        "stack_depth": 2,
        "stack_graphs": "all connected labelled simple graphs on one through four vertices and all roots",
        "arithmetic": "exact integers and rational Gaussian elimination",
    }, "finite grid")
    expected_collisions = {
        "C176": "sandpile translations and recurrent-state Fourier spectra, not random spanning-tree sampling or edge determinants",
        "C181": "deterministic rotor-router torsors, not independent resampling stacks or the weighted UST law",
    }
    expected_nonclaims = [
        "The spanning-tree partition polynomial is a source combinatorial normalization, not a target Euler factor or target zeta function.",
        "Finite enumeration audits conventions and implementations but does not prove the infinite-stack theorem.",
        "No target arithmetic local data, root number, automorphy, target divisor, functional equation, target zero match, literature priority, or Hilbert--Polya operator is asserted.",
        "No infinite graph, directed nonreversible chain, negative conductance, or unlabelled-parallel-edge quotient is claimed.",
    ]
    expected_references = [
        {"authors": "David Bruce Wilson", "title": "Generating random spanning trees more quickly than the cover time", "identifier": "DOI:10.1145/237814.237880"},
        {"authors": "Robert Burton and Robin Pemantle", "title": "Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings Via Transfer-Impedances", "identifier": "DOI:10.1214/aop/1176989121"},
        {"authors": "Gustav Kirchhoff", "title": "Ueber die Aufloesung der Gleichungen, auf welche man bei der Untersuchung der linearen Vertheilung galvanischer Stroeme gefuehrt wird", "identifier": "DOI:10.1002/andp.18471481202"},
        {"authors": "Seth Chaiken", "title": "A Combinatorial Proof of the All Minors Matrix Tree Theorem", "identifier": "DOI:10.1137/0603033"},
        {"authors": "Russell Lyons and Yuval Peres", "title": "Probability on Trees and Networks", "identifier": "ISBN:978-1-107-16015-6"},
    ]
    need(data["collision_boundary"] == expected_collisions, "collision boundary")
    need(data["nonclaims"] == expected_nonclaims, "nonclaims")
    need(data["references"] == expected_references, "references")
    need(data["route_a"] == {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
                              "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}, "route A")
    need(data["scope_flags"] == FLAGS, "scope flags")
    section_hash = lambda value: hashlib.sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    need(section_hash(data["graph_rows"]) == GRAPH_ROWS_SHA, "graph rows ownership digest")
    need(section_hash(data["weighted_case_rows"]) == WEIGHTED_ROWS_SHA, "weighted rows ownership digest")
    need(section_hash(data["stack_audit_rows"]) == STACK_ROWS_SHA, "stack rows ownership digest")
    need(data["enumeration"] == {
        "connected_simple_graphs": 772,
        "simple_graph_tree_pairs": 8136,
        "simple_transfer_subset_events": 55895,
        "weighted_multigraph_cases": 24,
        "weighted_tree_rows": 846,
        "weighted_transfer_subset_events": 7032,
        "rooted_stack_graphs": 167,
        "finite_stack_tables": 12754,
        "audited_leaf_count": 112184,
    }, "early enumeration ownership")

    evaluation = strict_yaml(args.evaluation)
    raw_hash = hashlib.sha256(args.evaluation.read_bytes()).hexdigest()
    semantic_hash = hashlib.sha256(json.dumps(
        evaluation, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    need(raw_hash == YAML_RAW and semantic_hash == YAML_SEMANTIC, "YAML digest")
    need(evaluation == EXPECTED_EVALUATION, "YAML semantics")
    need(data["route_a_yaml"] == {
        "relative_path": "evaluations/route_a/HCS-C338/2026-09-03.yaml",
        "raw_sha256": YAML_RAW,
        "semantic_sha256": YAML_SEMANTIC,
    }, "nested YAML lock")

    checks = 70
    specs = list(graph_specs())
    need(len(data["graph_rows"]) == len(specs) == 772, "graph row length")
    total_trees = total_subsets = 0
    for row, (n, graph_mask, edges) in zip(data["graph_rows"], specs):
        exact_keys(row, {"n", "graph_mask", "oriented_edges", "root", "tree_masks",
                         "tree_partition", "reduced_laplacian_determinant",
                         "transfer_current_kernel", "all_subset_inclusion_numerators"}, "graph row")
        need(row["n"] == n and row["graph_mask"] == graph_mask and row["root"] == 0, "graph coordinate")
        need(row["oriented_edges"] == [list(edge) for edge in edges], "simple edges")
        trees = all_trees(n, edges, [1] * len(edges))
        masks = [mask for mask, _ in trees]
        partition = len(trees)
        need(row["tree_masks"] == masks and row["tree_partition"] == partition, "simple tree ledger")
        minor, kernel = lap_and_kernel(n, edges, [1] * len(edges), 0)
        need(row["reduced_laplacian_determinant"] == det(minor) == partition, "simple matrix tree")
        stored_kernel = [[parse_fraction(value) for value in stored] for stored in row["transfer_current_kernel"]]
        need(stored_kernel == kernel, "simple kernel")
        numerators = [sum(weight for tree_mask, weight in trees if tree_mask & subset == subset)
                      for subset in range(1 << len(edges))]
        need(row["all_subset_inclusion_numerators"] == numerators, "simple inclusion ledger")
        for subset, numerator in enumerate(numerators):
            need(det(principal(kernel, subset)) == Fraction(numerator, partition), "simple transfer determinant")
            checks += 1
        for other_root in range(n):
            other_minor, other_kernel = lap_and_kernel(n, edges, [1] * len(edges), other_root)
            need(det(other_minor) == partition and other_kernel == kernel, "simple root change")
            checks += 1
        total_trees += partition
        total_subsets += len(numerators)
        checks += 8 + len(edges) ** 2

    weighted_specs_list = list(weighted_specs())
    need(len(data["weighted_case_rows"]) == len(weighted_specs_list) == 24, "weighted rows")
    weighted_trees = weighted_subsets = 0
    for row, spec in zip(data["weighted_case_rows"], weighted_specs_list):
        case, n, root, edges, weights = spec
        exact_keys(row, {"case", "n", "root", "oriented_labelled_edges", "weighted_tree_rows",
                         "tree_partition", "reduced_laplacian_determinant",
                         "transfer_current_kernel", "all_subset_inclusion_numerators"}, "weighted row")
        need((row["case"], row["n"], row["root"]) == (case, n, root), "weighted coordinate")
        expected_edges = [[u, v, label, weights[i]] for i, (u, v, label) in enumerate(edges)]
        need(row["oriented_labelled_edges"] == expected_edges, "weighted edges")
        trees = all_trees(n, edges, weights)
        expected_tree_rows = [{"mask": mask, "weight": weight} for mask, weight in trees]
        need(row["weighted_tree_rows"] == expected_tree_rows, "weighted tree ledger")
        partition = sum(weight for _, weight in trees)
        minor, kernel = lap_and_kernel(n, edges, weights, root)
        need(row["tree_partition"] == row["reduced_laplacian_determinant"] == partition == det(minor), "weighted matrix tree")
        stored_kernel = [[parse_fraction(value) for value in stored] for stored in row["transfer_current_kernel"]]
        need(stored_kernel == kernel, "weighted kernel")
        numerators = [sum(weight for mask, weight in trees if mask & subset == subset)
                      for subset in range(1 << len(edges))]
        need(row["all_subset_inclusion_numerators"] == numerators, "weighted inclusion ledger")
        for subset, numerator in enumerate(numerators):
            need(det(principal(kernel, subset)) == Fraction(numerator, partition), "weighted transfer determinant")
            checks += 1
        for other_root in range(n):
            other_minor, other_kernel = lap_and_kernel(n, edges, weights, other_root)
            need(det(other_minor) == partition and other_kernel == kernel, "weighted root change")
            checks += 1
        # Distinct parallel labels cannot simultaneously occur in a tree; the
        # corresponding two-edge transfer minor is therefore exactly zero.
        for i, first in enumerate(edges):
            for j in range(i + 1, len(edges)):
                if first[:2] == edges[j][:2]:
                    mask = (1 << i) | (1 << j)
                    need(numerators[mask] == 0 and det(principal(kernel, mask)) == 0, "parallel boundary")
                    checks += 1
        weighted_trees += len(trees)
        weighted_subsets += len(numerators)
        checks += 8 + len(edges) ** 2

    stack_rows = recompute_stack_rows()
    need(data["stack_audit_rows"] == stack_rows, "stack audit")
    need(all(row["abelian_failures"] == row["wilson_failures"] == 0 for row in stack_rows), "stack failures")
    expected_enumeration = {
        "connected_simple_graphs": 772,
        "simple_graph_tree_pairs": total_trees,
        "simple_transfer_subset_events": total_subsets,
        "weighted_multigraph_cases": 24,
        "weighted_tree_rows": weighted_trees,
        "weighted_transfer_subset_events": weighted_subsets,
        "rooted_stack_graphs": sum(row["rooted_graphs"] for row in stack_rows),
        "finite_stack_tables": sum(row["stack_tables"] for row in stack_rows),
        "audited_leaf_count": leaves({key: value for key, value in data.items()
                                       if key not in {"enumeration", "payload_sha256"}}),
    }
    need(data["enumeration"] == expected_enumeration, "enumeration")
    need(total_trees == 8136 and total_subsets == 55895, "historic simple totals")
    need(weighted_trees == 846 and weighted_subsets == 7032, "weighted totals")
    need(expected_enumeration["finite_stack_tables"] == 12754, "stack total")
    checks += expected_enumeration["audited_leaf_count"] + expected_enumeration["finite_stack_tables"]
    print(f"C338 independent Wilson/UST checker: PASS {checks} exact checks")


if __name__ == "__main__":
    main()
