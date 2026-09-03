#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C342."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c342_derrw_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C342/2026-09-03.yaml"
SOURCE = "e2d94f886963cbe3d42b83f6ef542413a163d3a4"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW = "0783cb2f38d0c4910fe97574024b73e3cc553fbcd4e04419628267008c5072fd"
YAML_SEMANTIC = "ed7246a3042d6864bb758abbe0a5550ece71372ca9528103c8c5920ae1797448"
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


def duplicate_pairs(items):
    answer = {}
    for key, value in items:
        if key in answer:
            raise ValueError("duplicate JSON key")
        answer[key] = value
    return answer


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
            raise ValueError("duplicate/non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors/aliases forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def need(condition, label):
    if not condition:
        raise AssertionError(label)


def exact_keys(value, keys, label):
    need(type(value) is dict and set(value) == set(keys), f"{label} keys")


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def text_fraction(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def product(values):
    answer = Fraction(1)
    for value in values:
        answer *= value
    return answer


def factorial_rise(alpha, count):
    return product(Fraction(alpha + j) for j in range(count))


def panel():
    return [
        ("loop_bridge", 2, 0, [(0, 0, 1), (0, 1, 2), (1, 0, 3), (1, 1, 1)]),
        ("parallel_triangle", 3, 0, [(0, 1, 1), (0, 1, 2), (0, 2, 1),
                                     (1, 0, 2), (1, 2, 1), (2, 0, 1), (2, 1, 2)]),
        ("polya_loops", 1, 0, [(0, 0, 1), (0, 0, 2), (0, 0, 4)]),
    ]


def departures(vertices, edges):
    result = [[] for _ in range(vertices)]
    for index, (tail, _head, _alpha) in enumerate(edges):
        result[tail].append(index)
    return result


def evaluate_path(vertices, start, edges, path):
    out = departures(vertices, edges)
    alpha_row = [sum(edges[i][2] for i in out[v]) for v in range(vertices)]
    counts = [0] * len(edges)
    visits = [0] * vertices
    current = start
    sequential = Fraction(1)
    for index in path:
        tail, head, alpha = edges[index]
        need(tail == current, "legal path")
        sequential *= Fraction(alpha + counts[index], alpha_row[tail] + visits[tail])
        counts[index] += 1
        visits[tail] += 1
        current = head
    grouped = product(
        Fraction(product(factorial_rise(edges[i][2], counts[i]) for i in out[v]),
                 factorial_rise(alpha_row[v], visits[v]))
        for v in range(vertices))
    posterior_total = sum(Fraction(edges[i][2] + counts[i],
                                   alpha_row[current] + visits[current]) for i in out[current])
    return current, counts, sequential, grouped, posterior_total


def expected_paths(graph_id, vertices, start, edges):
    out = departures(vertices, edges)
    frontier = [(start, ())]
    rows, summaries = [], []
    for length in range(9):
        total = Fraction(0)
        signatures = {}
        for endpoint, path in frontier:
            current, counts, sequential, integrated, posterior = evaluate_path(
                vertices, start, edges, path)
            need(endpoint == current, "endpoint")
            total += sequential
            signatures.setdefault(tuple(counts), set()).add(sequential)
            rows.append({
                "graph_id": graph_id, "length": length, "path": list(path),
                "terminal_vertex": endpoint, "edge_counts": counts,
                "reinforced_probability": text_fraction(sequential),
                "dirichlet_moment_probability": text_fraction(integrated),
                "posterior_predictive_sum": text_fraction(posterior),
            })
        need(total == 1 and all(len(values) == 1 for values in signatures.values()), "level")
        summaries.append({"graph_id": graph_id, "length": length,
                          "legal_path_count": len(frontier),
                          "count_signatures": len(signatures),
                          "probability_sum": "1", "exchangeability_failures": 0})
        frontier = [(edges[index][1], path + (index,))
                    for vertex, path in frontier for index in out[vertex]]
    return rows, summaries


def expected_moments(graph_id, vertices, edges):
    means, covariances = [], []
    for vertex, indices in enumerate(departures(vertices, edges)):
        total = sum(edges[i][2] for i in indices)
        for index in indices:
            alpha = edges[index][2]
            means.append({"graph_id": graph_id, "vertex": vertex, "edge": index,
                          "mean": text_fraction(Fraction(alpha, total)),
                          "second_moment": text_fraction(Fraction(alpha * (alpha + 1),
                                                                 total * (total + 1))),
                          "variance": text_fraction(Fraction(alpha * (total - alpha),
                                                             total * total * (total + 1)))})
        for position, left in enumerate(indices):
            for right in indices[position + 1:]:
                covariances.append({
                    "graph_id": graph_id, "vertex": vertex,
                    "left_edge": left, "right_edge": right,
                    "mixed_moment": text_fraction(Fraction(edges[left][2] * edges[right][2],
                                                           total * (total + 1))),
                    "covariance": text_fraction(Fraction(-edges[left][2] * edges[right][2],
                                                         total * total * (total + 1))),
                })
    return means, covariances


def linear_stationary(kernel):
    n = len(kernel)
    matrix = []
    for equation in range(n - 1):
        matrix.append([kernel[column][equation] - Fraction(column == equation)
                       for column in range(n)] + [Fraction(0)])
    matrix.append([Fraction(1)] * n + [Fraction(1)])
    # Gauss-Jordan, selecting pivots independently of the producer's loop.
    for col in range(n):
        candidates = [row for row in range(col, n) if matrix[row][col] != 0]
        need(bool(candidates), "stationary pivot")
        pivot = candidates[-1]
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        divisor = matrix[col][col]
        for j in range(col, n + 1):
            matrix[col][j] /= divisor
        for row in range(n):
            if row == col:
                continue
            multiple = matrix[row][col]
            for j in range(col, n + 1):
                matrix[row][j] -= multiple * matrix[col][j]
    return [matrix[row][n] for row in range(n)]


def expected_environments(graphs):
    table = {
        "loop_bridge": [Fraction(1, 3), Fraction(2, 3), Fraction(3, 4), Fraction(1, 4)],
        "parallel_triangle": [Fraction(1, 4), Fraction(1, 2), Fraction(1, 4),
                              Fraction(2, 3), Fraction(1, 3),
                              Fraction(1, 3), Fraction(2, 3)],
        "polya_loops": [Fraction(1, 7), Fraction(2, 7), Fraction(4, 7)],
    }
    answer = []
    for graph_id, vertices, _start, edges in graphs:
        omega = table[graph_id]
        kernel = [[Fraction(0) for _ in range(vertices)] for _ in range(vertices)]
        for index, (tail, head, _alpha) in enumerate(edges):
            kernel[tail][head] += omega[index]
        stationary = linear_stationary(kernel)
        flows = [stationary[tail] * omega[index]
                 for index, (tail, _head, _alpha) in enumerate(edges)]
        incoming = [sum(flows[i] for i, (_tail, head, _alpha) in enumerate(edges) if head == v)
                    for v in range(vertices)]
        need(incoming == stationary and sum(stationary) == 1, "stationarity")
        answer.append({"graph_id": graph_id,
                       "arc_probabilities": [text_fraction(x) for x in omega],
                       "vertex_kernel": [[text_fraction(x) for x in row] for row in kernel],
                       "stationary_distribution": [text_fraction(x) for x in stationary],
                       "labelled_edge_flows": [text_fraction(x) for x in flows],
                       "balance_failures": 0})
    return answer


def main():
    if sys.flags.optimize:
        raise RuntimeError("C342 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    yaml_raw = args.evaluation.read_bytes()
    evaluation = strict_yaml(args.evaluation)
    need(hashlib.sha256(yaml_raw).hexdigest() == YAML_RAW, "YAML raw digest")
    need(hashlib.sha256(canonical(evaluation)).hexdigest() == YAML_SEMANTIC, "YAML semantic digest")
    exact_keys(data, ["schema", "candidate_id", "obstruction_id", "evaluation_date",
        "source_commit", "fixed_epoch", "scope_literal", "evaluator", "route_a_yaml",
        "model", "theorem_contract", "finite_grid", "collision_boundary", "nonclaims",
        "references", "route_a", "scope_flags", "graph_rows", "path_rows",
        "path_summary_rows", "dirichlet_moment_rows", "dirichlet_covariance_rows",
        "environment_rows", "enumeration", "payload_sha256"], "top")
    body = dict(data)
    claimed = body.pop("payload_sha256")
    need(type(claimed) is str and claimed == hashlib.sha256(canonical(body)).hexdigest(), "payload hash")
    need(data["schema"] == "hcs-c342-derrw-evidence-v1", "schema")
    need(data["candidate_id"] == "HCS-C342" and data["obstruction_id"] == "HEN-O326", "ids")
    need(data["evaluation_date"] == "2026-09-03", "date")
    need(data["source_commit"] == SOURCE and data["fixed_epoch"] == 1788393600, "source")
    need(data["scope_literal"] == SCOPE, "scope")
    need(data["evaluator"] == {"authority": "flow_systems/skills/route-a-evaluator.md",
         "version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    need(data["route_a_yaml"] == {
        "relative_path": "evaluations/route_a/HCS-C342/2026-09-03.yaml",
        "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC}, "YAML binding")
    need(data["model"] == {
        "graph": "finite strongly connected directed labelled multigraph",
        "outgoing_requirement": "every vertex has at least one outgoing labelled arc",
        "parameters": "strictly positive initial weight on every labelled arc",
        "reinforcement": "increment only the traversed outgoing labelled arc",
        "denominator": "vertex-local total initial weight plus departures from that vertex",
        "environment": "independent Dirichlet row at every vertex"}, "model")
    need(data["theorem_contract"] == {
        "path_law": "all legal paths have the exact vertex-wise rising-factorial law",
        "mixture": "exact annealed equality with independent-row Dirichlet environment",
        "posterior": "independent conjugate rows after every finite history",
        "limits": "almost-sure transition, vertex occupation, and labelled edge occupation limits",
        "moments": "complete row means, variances, covariances, and cross-row independence",
        "boundaries": "outdegree one, labelled parallel arcs, nonempty one-vertex loops, empty outgoing rows, reducibility, and zero weights"}, "contract")
    need(data["collision_boundary"] == {
        "C263": "one global Polya urn, not a walker-selected family of transition rows",
        "C181": "deterministic rotor routing without Bayesian reinforcement",
        "C338": "fixed-conductance Wilson stacks rather than traversal reinforcement",
        "undirected_ERRW": "different mixing law and magic formula, both excluded"}, "collision")
    need(data["nonclaims"] == [
        "no theorem for undirected ERRW, vertex reinforcement, or nonlinear reinforcement",
        "no infinite-graph, time-reversal, ballisticity, or directional-transience claim",
        "no target arithmetic local data or Euler-factor interpretation",
        "no root number, automorphy, target zero match, Hilbert-Polya operator, or Route B"], "nonclaims")
    need(data["references"] == [
        {"authors": "Enriquez and Sabot", "year": 2002,
         "identifier": "DOI:10.1016/S1631-073X(02)02580-3",
         "role": "primary directed reinforcement and RWRE correspondence"},
        {"authors": "Diaconis and Freedman", "year": 1980,
         "identifier": "Project-Euclid:aop/1176994828",
         "role": "primary Markov partial-exchangeability lineage"},
        {"authors": "Sabot and Tournier", "year": 2017,
         "identifier": "DOI:10.5802/afst.1542",
         "role": "authoritative Dirichlet-environment overview"}], "references")
    need(data["route_a"] == {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
         "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}, "route A")
    need(data["scope_flags"] == FLAGS, "flags")
    graphs = panel()
    graph_rows, path_rows, summaries, means, covariances = [], [], [], [], []
    for graph_id, vertices, start, edges in graphs:
        out = departures(vertices, edges)
        graph_rows.append({"graph_id": graph_id, "vertex_count": vertices,
                           "start_vertex": start,
                           "labelled_edges": [[i, *edge] for i, edge in enumerate(edges)],
                           "outdegrees": [len(row) for row in out],
                           "parallel_arc_pairs": sum(edges[i][:2] == edges[j][:2]
                               for i in range(len(edges)) for j in range(i + 1, len(edges)))})
        rows, level_rows = expected_paths(graph_id, vertices, start, edges)
        path_rows.extend(rows)
        summaries.extend(level_rows)
        row_means, row_covariances = expected_moments(graph_id, vertices, edges)
        means.extend(row_means)
        covariances.extend(row_covariances)
    environments = expected_environments(graphs)
    need(data["graph_rows"] == graph_rows, "graph ledger")
    need(data["path_rows"] == path_rows, "path ledger")
    need(data["path_summary_rows"] == summaries, "summary ledger")
    need(data["dirichlet_moment_rows"] == means, "moment ledger")
    need(data["dirichlet_covariance_rows"] == covariances, "covariance ledger")
    need(data["environment_rows"] == environments, "environment ledger")
    need(data["finite_grid"] == {"graph_count": 3, "maximum_path_length": 8,
         "path_rows": 12018, "summary_rows": 27, "moment_rows": 14,
         "covariance_rows": 10, "environment_rows": 3}, "finite grid")
    need(data["enumeration"] == {
        "graph_rows_sha256": hashlib.sha256(canonical(graph_rows)).hexdigest(),
        "path_rows_sha256": hashlib.sha256(canonical(path_rows)).hexdigest(),
        "path_summary_rows_sha256": hashlib.sha256(canonical(summaries)).hexdigest(),
        "moment_rows_sha256": hashlib.sha256(canonical(means)).hexdigest(),
        "covariance_rows_sha256": hashlib.sha256(canonical(covariances)).hexdigest(),
        "environment_rows_sha256": hashlib.sha256(canonical(environments)).hexdigest(),
        "all_probabilities_exact": True}, "enumeration")
    need(evaluation["candidate_id"] == "HCS-C342" and evaluation["obstruction_id"] == "HEN-O326", "YAML ids")
    need(evaluation["source_commit"] == SOURCE and evaluation["evaluation_date"] == "2026-09-03", "YAML source/date")
    need(evaluation["candidate_definition"] ==
         "linear reinforcement on labelled outgoing arcs of a finite strongly connected directed multigraph with every outgoing row nonempty",
         "YAML outgoing-row definition")
    need(evaluation["parameters"] ==
         "finite strongly connected labelled directed multigraph, at least one outgoing arc per vertex, and positive real arc weights",
         "YAML outgoing-row parameters")
    need(evaluation["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md"
         and evaluation["evaluator_authority_sha256"] == EVALUATOR, "YAML evaluator")
    need(evaluation["scope_literal"] == SCOPE and evaluation["scope_flags"] == FLAGS, "YAML scope")
    need(evaluation["tuple"] == data["route_a"]["tuple"]
         and evaluation["overall_verdict"] == "ROUTE_A_REJECTED", "YAML verdict")
    need(evaluation["route_b_invocation_allowed"] is False
         and evaluation["theorem_status"] == "PROVABLE_AS_STATED", "YAML theorem")
    need(evaluation["finite_evidence_role"] == "convention and implementation receipt, not proof", "finite role")
    print(f"C342 independent DERRW checker: PASS {len(path_rows)} paths "
          f"{len(means) + len(covariances)} moments {len(environments)} environments")


if __name__ == "__main__":
    main()
