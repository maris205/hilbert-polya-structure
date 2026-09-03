#!/usr/bin/env python3
"""Canonical exact-evidence producer for HCS-C342."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c342_derrw_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C342/2026-09-03.yaml"
SOURCE = "e2d94f886963cbe3d42b83f6ef542413a163d3a4"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
YAML_RAW = "0783cb2f38d0c4910fe97574024b73e3cc553fbcd4e04419628267008c5072fd"
YAML_SEMANTIC = "ed7246a3042d6864bb758abbe0a5550ece71372ca9528103c8c5920ae1797448"


def duplicate_pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("duplicate key")
        result[key] = value
    return result


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
            raise ValueError("merge key")
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
            raise ValueError("anchors forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def fstr(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def rising(a, count):
    value = Fraction(1)
    for offset in range(count):
        value *= a + offset
    return value


def graph_panel():
    return [
        {"graph_id": "loop_bridge", "vertex_count": 2, "start": 0,
         "edges": [(0, 0, 1), (0, 1, 2), (1, 0, 3), (1, 1, 1)]},
        {"graph_id": "parallel_triangle", "vertex_count": 3, "start": 0,
         "edges": [(0, 1, 1), (0, 1, 2), (0, 2, 1), (1, 0, 2),
                   (1, 2, 1), (2, 0, 1), (2, 1, 2)]},
        {"graph_id": "polya_loops", "vertex_count": 1, "start": 0,
         "edges": [(0, 0, 1), (0, 0, 2), (0, 0, 4)]},
    ]


def outgoing(graph):
    answer = {v: [] for v in range(graph["vertex_count"])}
    for index, (tail, _head, _alpha) in enumerate(graph["edges"]):
        answer[tail].append(index)
    return answer


def path_probability(graph, path):
    edges = graph["edges"]
    alpha_vertex = [sum(alpha for tail, _head, alpha in edges if tail == v)
                    for v in range(graph["vertex_count"])]
    edge_counts = [0] * len(edges)
    departure_counts = [0] * graph["vertex_count"]
    value = Fraction(1)
    vertex = graph["start"]
    for edge_index in path:
        tail, head, alpha = edges[edge_index]
        if tail != vertex:
            raise AssertionError("illegal path")
        value *= Fraction(alpha + edge_counts[edge_index],
                          alpha_vertex[tail] + departure_counts[tail])
        edge_counts[edge_index] += 1
        departure_counts[tail] += 1
        vertex = head
    grouped = Fraction(1)
    for v in range(graph["vertex_count"]):
        grouped *= Fraction(
            1 if not outgoing(graph)[v] else
            _product(rising(edges[e][2], edge_counts[e]) for e in outgoing(graph)[v]),
            rising(alpha_vertex[v], departure_counts[v]))
    posterior_sum = sum(Fraction(edges[e][2] + edge_counts[e],
                                 alpha_vertex[vertex] + departure_counts[vertex])
                        for e in outgoing(graph)[vertex])
    return vertex, edge_counts, value, grouped, posterior_sum


def _product(values):
    result = Fraction(1)
    for value in values:
        result *= value
    return result


def enumerate_paths(graph, max_length=8):
    out = outgoing(graph)
    active = [(graph["start"], ())]
    rows = []
    summaries = []
    for length in range(max_length + 1):
        probabilities = Fraction(0)
        groups = {}
        for terminal, path in active:
            endpoint, counts, sequential, grouped, posterior = path_probability(graph, path)
            if endpoint != terminal or sequential != grouped or posterior != 1:
                raise AssertionError("path identity")
            probabilities += sequential
            signature = tuple(counts)
            groups.setdefault(signature, set()).add(sequential)
            rows.append({
                "graph_id": graph["graph_id"], "length": length, "path": list(path),
                "terminal_vertex": terminal, "edge_counts": counts,
                "reinforced_probability": fstr(sequential),
                "dirichlet_moment_probability": fstr(grouped),
                "posterior_predictive_sum": fstr(posterior),
            })
        if probabilities != 1 or any(len(values) != 1 for values in groups.values()):
            raise AssertionError("path level normalization/exchangeability")
        summaries.append({
            "graph_id": graph["graph_id"], "length": length,
            "legal_path_count": len(active), "count_signatures": len(groups),
            "probability_sum": fstr(probabilities), "exchangeability_failures": 0,
        })
        active = [(graph["edges"][edge][1], path + (edge,))
                  for vertex, path in active for edge in out[vertex]]
    return rows, summaries


def moment_rows(graph):
    edges = graph["edges"]
    means, covariances = [], []
    for vertex, indices in outgoing(graph).items():
        total = sum(edges[index][2] for index in indices)
        for index in indices:
            alpha = edges[index][2]
            mean = Fraction(alpha, total)
            second = Fraction(alpha * (alpha + 1), total * (total + 1))
            variance = Fraction(alpha * (total - alpha), total * total * (total + 1))
            means.append({
                "graph_id": graph["graph_id"], "vertex": vertex, "edge": index,
                "mean": fstr(mean), "second_moment": fstr(second), "variance": fstr(variance),
            })
        for left_position, left in enumerate(indices):
            for right in indices[left_position + 1:]:
                covariance = Fraction(-edges[left][2] * edges[right][2],
                                      total * total * (total + 1))
                mixed = Fraction(edges[left][2] * edges[right][2], total * (total + 1))
                covariances.append({
                    "graph_id": graph["graph_id"], "vertex": vertex,
                    "left_edge": left, "right_edge": right,
                    "mixed_moment": fstr(mixed), "covariance": fstr(covariance),
                })
    return means, covariances


def solve_stationary(matrix):
    n = len(matrix)
    augmented = []
    for equation in range(n - 1):
        augmented.append([matrix[column][equation] - Fraction(column == equation)
                          for column in range(n)] + [Fraction(0)])
    augmented.append([Fraction(1)] * n + [Fraction(1)])
    for column in range(n):
        pivot = next(row for row in range(column, n) if augmented[row][column])
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scale = augmented[column][column]
        augmented[column] = [x / scale for x in augmented[column]]
        for row in range(n):
            if row != column and augmented[row][column]:
                scale = augmented[row][column]
                augmented[row] = [augmented[row][j] - scale * augmented[column][j]
                                  for j in range(n + 1)]
    return [augmented[i][-1] for i in range(n)]


def environment_rows(graphs):
    weights = {
        "loop_bridge": [Fraction(1, 3), Fraction(2, 3), Fraction(3, 4), Fraction(1, 4)],
        "parallel_triangle": [Fraction(1, 4), Fraction(1, 2), Fraction(1, 4),
                              Fraction(2, 3), Fraction(1, 3),
                              Fraction(1, 3), Fraction(2, 3)],
        "polya_loops": [Fraction(1, 7), Fraction(2, 7), Fraction(4, 7)],
    }
    answer = []
    for graph in graphs:
        omega = weights[graph["graph_id"]]
        n = graph["vertex_count"]
        matrix = [[Fraction(0) for _ in range(n)] for _ in range(n)]
        for index, (tail, head, _alpha) in enumerate(graph["edges"]):
            matrix[tail][head] += omega[index]
        if any(sum(row) != 1 for row in matrix):
            raise AssertionError("environment rows")
        stationary = solve_stationary(matrix)
        flows = [stationary[tail] * omega[index]
                 for index, (tail, _head, _alpha) in enumerate(graph["edges"])]
        incoming = [sum(flows[i] for i, (_tail, head, _a) in enumerate(graph["edges"]) if head == v)
                    for v in range(n)]
        if incoming != stationary or sum(stationary) != 1 or sum(flows) != 1:
            raise AssertionError("stationary flow")
        answer.append({
            "graph_id": graph["graph_id"],
            "arc_probabilities": [fstr(x) for x in omega],
            "vertex_kernel": [[fstr(x) for x in row] for row in matrix],
            "stationary_distribution": [fstr(x) for x in stationary],
            "labelled_edge_flows": [fstr(x) for x in flows],
            "balance_failures": 0,
        })
    return answer


def row_hash(rows):
    return hashlib.sha256(canonical(rows)).hexdigest()


def build(evaluation):
    raw = evaluation.read_bytes()
    semantic = strict_yaml(evaluation)
    if hashlib.sha256(raw).hexdigest() != YAML_RAW:
        raise AssertionError("evaluation raw hash")
    if hashlib.sha256(canonical(semantic)).hexdigest() != YAML_SEMANTIC:
        raise AssertionError("evaluation semantic hash")
    graphs = graph_panel()
    graph_rows = []
    path_rows, summaries = [], []
    means, covariances = [], []
    for graph in graphs:
        outdegrees = [len(outgoing(graph)[v]) for v in range(graph["vertex_count"])]
        graph_rows.append({
            "graph_id": graph["graph_id"], "vertex_count": graph["vertex_count"],
            "start_vertex": graph["start"],
            "labelled_edges": [[i, *edge] for i, edge in enumerate(graph["edges"])],
            "outdegrees": outdegrees,
            "parallel_arc_pairs": sum(
                graph["edges"][i][:2] == graph["edges"][j][:2]
                for i in range(len(graph["edges"])) for j in range(i + 1, len(graph["edges"]))),
        })
        rows, level = enumerate_paths(graph)
        path_rows.extend(rows)
        summaries.extend(level)
        row_means, row_covariances = moment_rows(graph)
        means.extend(row_means)
        covariances.extend(row_covariances)
    environments = environment_rows(graphs)
    data = {
        "schema": "hcs-c342-derrw-evidence-v1",
        "candidate_id": "HCS-C342",
        "obstruction_id": "HEN-O326",
        "evaluation_date": "2026-09-03",
        "source_commit": SOURCE,
        "fixed_epoch": 1788393600,
        "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md",
                      "version": "0.2.0", "sha256": EVALUATOR},
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C342/2026-09-03.yaml",
                         "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC},
        "model": {
            "graph": "finite strongly connected directed labelled multigraph",
            "outgoing_requirement": "every vertex has at least one outgoing labelled arc",
            "parameters": "strictly positive initial weight on every labelled arc",
            "reinforcement": "increment only the traversed outgoing labelled arc",
            "denominator": "vertex-local total initial weight plus departures from that vertex",
            "environment": "independent Dirichlet row at every vertex",
        },
        "theorem_contract": {
            "path_law": "all legal paths have the exact vertex-wise rising-factorial law",
            "mixture": "exact annealed equality with independent-row Dirichlet environment",
            "posterior": "independent conjugate rows after every finite history",
            "limits": "almost-sure transition, vertex occupation, and labelled edge occupation limits",
            "moments": "complete row means, variances, covariances, and cross-row independence",
            "boundaries": "outdegree one, labelled parallel arcs, nonempty one-vertex loops, empty outgoing rows, reducibility, and zero weights",
        },
        "finite_grid": {
            "graph_count": len(graphs), "maximum_path_length": 8,
            "path_rows": len(path_rows), "summary_rows": len(summaries),
            "moment_rows": len(means), "covariance_rows": len(covariances),
            "environment_rows": len(environments),
        },
        "collision_boundary": {
            "C263": "one global Polya urn, not a walker-selected family of transition rows",
            "C181": "deterministic rotor routing without Bayesian reinforcement",
            "C338": "fixed-conductance Wilson stacks rather than traversal reinforcement",
            "undirected_ERRW": "different mixing law and magic formula, both excluded",
        },
        "nonclaims": [
            "no theorem for undirected ERRW, vertex reinforcement, or nonlinear reinforcement",
            "no infinite-graph, time-reversal, ballisticity, or directional-transience claim",
            "no target arithmetic local data or Euler-factor interpretation",
            "no root number, automorphy, target zero match, Hilbert-Polya operator, or Route B",
        ],
        "references": [
            {"authors": "Enriquez and Sabot", "year": 2002,
             "identifier": "DOI:10.1016/S1631-073X(02)02580-3",
             "role": "primary directed reinforcement and RWRE correspondence"},
            {"authors": "Diaconis and Freedman", "year": 1980,
             "identifier": "Project-Euclid:aop/1176994828",
             "role": "primary Markov partial-exchangeability lineage"},
            {"authors": "Sabot and Tournier", "year": 2017,
             "identifier": "DOI:10.5802/afst.1542",
             "role": "authoritative Dirichlet-environment overview"},
        ],
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
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
        "graph_rows": graph_rows,
        "path_rows": path_rows,
        "path_summary_rows": summaries,
        "dirichlet_moment_rows": means,
        "dirichlet_covariance_rows": covariances,
        "environment_rows": environments,
        "enumeration": {
            "graph_rows_sha256": row_hash(graph_rows),
            "path_rows_sha256": row_hash(path_rows),
            "path_summary_rows_sha256": row_hash(summaries),
            "moment_rows_sha256": row_hash(means),
            "covariance_rows_sha256": row_hash(covariances),
            "environment_rows_sha256": row_hash(environments),
            "all_probabilities_exact": True,
        },
    }
    data["payload_sha256"] = hashlib.sha256(canonical(data)).hexdigest()
    return data


def main():
    if sys.flags.optimize:
        raise RuntimeError("C342 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C342_PRODUCER_PASS paths={len(data['path_rows'])} summaries={len(data['path_summary_rows'])} "
          f"moments={len(data['dirichlet_moment_rows']) + len(data['dirichlet_covariance_rows'])} "
          f"payload={data['payload_sha256']}")


if __name__ == "__main__":
    main()
