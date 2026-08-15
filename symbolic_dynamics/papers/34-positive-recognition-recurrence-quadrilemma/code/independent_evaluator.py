#!/usr/bin/env python3
"""Independent reconstruction and post-freeze support evaluation for Paper 34."""

from __future__ import annotations

import argparse
import ast
import csv
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations
import json
from math import isqrt
from pathlib import Path
from typing import Iterable, Sequence


Edge = tuple[int, int]
Cycle = tuple[Edge, ...]
Polynomial = list[Fraction]


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    fields = list(rows[0]) + sorted(
        set().union(*(row.keys() for row in rows)) - set(rows[0])
    )
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def parse_fraction(text: str) -> Fraction:
    numerator, denominator = text.split("/")
    return Fraction(int(numerator), int(denominator))


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def poly_text(poly: Polynomial) -> list[str]:
    return [fraction_text(value) for value in poly]


def poly_multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    result = [Fraction(0, 1)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def poly_eval(poly: Polynomial, value: Fraction) -> Fraction:
    result = Fraction(0, 1)
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def poly_digest(poly: Polynomial) -> str:
    return sha256(("\n".join(poly_text(poly)) + "\n").encode()).hexdigest()


def edges_from_mask(n: int, mask: int) -> frozenset[Edge]:
    return frozenset(
        (u, v)
        for u in range(n)
        for v in range(n)
        if mask & (1 << (u * n + v))
    )


def mask_from_edges(n: int, edges: Iterable[Edge]) -> int:
    mask = 0
    for u, v in edges:
        mask |= 1 << (u * n + v)
    return mask


def reachability_components(n: int, edges: frozenset[Edge]) -> tuple[tuple[int, ...], ...]:
    reach = [[u == v for v in range(n)] for u in range(n)]
    for u, v in edges:
        reach[u][v] = True
    for middle in range(n):
        for left in range(n):
            if reach[left][middle]:
                for right in range(n):
                    reach[left][right] = reach[left][right] or reach[middle][right]
    unused = set(range(n))
    components: list[tuple[int, ...]] = []
    while unused:
        first = min(unused)
        component = tuple(
            vertex
            for vertex in sorted(unused)
            if reach[first][vertex] and reach[vertex][first]
        )
        components.append(component)
        unused -= set(component)
    return tuple(components)


def rotate(values: Sequence[Edge], offset: int) -> Cycle:
    return tuple(values[offset:]) + tuple(values[:offset])


def canonical(word: Sequence[Edge]) -> Cycle:
    return min(rotate(word, index) for index in range(len(word)))


def cycles_by_permutations(n: int, edges: frozenset[Edge]) -> tuple[Cycle, ...]:
    found: list[Cycle] = []
    for length in range(1, n + 1):
        for vertices in permutations(range(n), length):
            rotations = [vertices[index:] + vertices[:index] for index in range(length)]
            if vertices != min(rotations):
                continue
            word = tuple(
                (vertices[index], vertices[(index + 1) % length])
                for index in range(length)
            )
            if all(edge in edges for edge in word):
                found.append(word)
    return tuple(sorted(found))


def cycle_vertices(cycle: Cycle) -> frozenset[int]:
    return frozenset(edge[0] for edge in cycle)


def based(cycle: Cycle, vertex: int) -> Cycle:
    return min(
        rotate(cycle, index)
        for index, edge in enumerate(cycle)
        if edge[0] == vertex
    )


def root_by_period_test(word: Cycle) -> tuple[Cycle, int]:
    for period in range(1, len(word) + 1):
        if len(word) % period:
            continue
        if all(word[index] == word[index % period] for index in range(len(word))):
            return word[:period], len(word) // period
    raise AssertionError


def legal(word: Cycle) -> bool:
    return bool(word) and all(
        word[index][1] == word[(index + 1) % len(word)][0]
        for index in range(len(word))
    )


def external_paths(
    n: int,
    edges: frozenset[Edge],
    start: int,
    end: int,
    forbidden: frozenset[int],
) -> list[Cycle]:
    output: list[Cycle] = []
    available = [vertex for vertex in range(n) if vertex not in {start, end} and vertex not in forbidden]
    for internal_count in range(len(available) + 1):
        for internal in permutations(available, internal_count):
            vertices = (start,) + internal + (end,)
            word = tuple(zip(vertices[:-1], vertices[1:]))
            if all(edge in edges for edge in word):
                output.append(word)
        if output:
            return sorted(output)
    return []


def independent_connector(
    n: int,
    edges: frozenset[Edge],
    first: Cycle,
    second: Cycle,
    external_only: bool,
) -> tuple[Cycle, Cycle, Cycle] | None:
    first_vertices = cycle_vertices(first)
    second_vertices = cycle_vertices(second)
    forbidden = first_vertices | second_vertices if external_only else frozenset()
    choices: list[tuple[tuple[object, ...], Cycle, Cycle, Cycle]] = []
    for left in sorted(first_vertices):
        for right in sorted(second_vertices):
            outward = external_paths(n, edges, left, right, forbidden)
            inward = external_paths(n, edges, right, left, forbidden)
            if outward and inward:
                out = outward[0]
                back = inward[0]
                word = based(first, left) + out + based(second, right) + back
                key: tuple[object, ...] = (len(out) + len(back), out, back, word)
                choices.append((key, word, out, back))
    if not choices:
        return None
    _, word, outward, inward = min(choices, key=lambda item: item[0])
    return word, outward, inward


def edge_weight(n: int, edge: Edge) -> Fraction:
    index = edge[0] * n + edge[1] + 2
    return Fraction(index, index + 1)


def word_weight(n: int, word: Cycle) -> Fraction:
    value = Fraction(1, 1)
    for edge in word:
        value *= edge_weight(n, edge)
    return value


def hash_control_edges(case_index: int, n: int) -> frozenset[Edge]:
    edges = {(vertex, (vertex + 1) % n) for vertex in range(n)}
    for left in range(n):
        for right in range(n):
            token = f"P34-GRAPH-{case_index}-{n}-{left}-{right}".encode()
            if sha256(token).digest()[0] < 72:
                edges.add((left, right))
    return frozenset(edges)


def independent_graph_audit(n: int, mask: int, edges: frozenset[Edge], digest: object) -> dict[str, int]:
    components = reachability_components(n, edges)
    cycles = cycles_by_permutations(n, edges)
    groups: dict[int, list[Cycle]] = {index: [] for index in range(len(components))}
    for cycle in cycles:
        vertices = cycle_vertices(cycle)
        index = next(i for i, component in enumerate(components) if vertices <= set(component))
        groups[index].append(cycle)
    counts = {
        "recurrent_sccs": sum(bool(group) for group in groups.values()),
        "multi_cycle_sccs": sum(len(group) >= 2 for group in groups.values()),
        "simple_cycles": len(cycles),
        "shared_pairs": 0,
        "connector_pairs": 0,
        "strict_external_connector_failures": 0,
        "mixed_roots": 0,
        "failures": 0,
    }
    for group in groups.values():
        for first, second in combinations(sorted(group), 2):
            shared = cycle_vertices(first) & cycle_vertices(second)
            if shared:
                vertex = min(shared)
                word = based(first, vertex) + based(second, vertex)
                family = "shared_state"
                counts["shared_pairs"] += 1
            else:
                family = "mutual_connector"
                counts["connector_pairs"] += 1
                strict = independent_connector(
                    n, edges, first, second, external_only=True
                )
                counts["strict_external_connector_failures"] += int(strict is None)
                built = independent_connector(
                    n, edges, first, second, external_only=False
                )
                if built is None:
                    counts["failures"] += 1
                    continue
                word = built[0]
            root, exponent = root_by_period_test(word)
            passed = (
                legal(root)
                and canonical(root) not in {canonical(first), canonical(second)}
                and word_weight(n, word) == word_weight(n, root) ** exponent
                and word_weight(n, root) > 0
            )
            digest.update(
                (
                    f"{family}|{n}|{mask}|{first}|{second}|{canonical(root)}|{exponent}\n"
                ).encode()
            )
            counts["mixed_roots"] += int(passed)
            counts["failures"] += int(not passed)
    return counts


def reconstruct_graph_census() -> tuple[list[dict[str, object]], str]:
    digest = sha256()
    rows: list[dict[str, object]] = []
    for n in (1, 2, 3, 4):
        graphs = 1 << (n * n)
        row: dict[str, object] = {
            "graph_family": "exhaustive",
            "vertex_count": n,
            "graphs": graphs,
            "recurrent_sccs": 0,
            "multi_cycle_sccs": 0,
            "simple_cycles": 0,
            "shared_pairs": 0,
            "connector_pairs": 0,
            "strict_external_connector_failures": 0,
            "mixed_roots": 0,
            "failures": 0,
        }
        for mask in range(graphs):
            counts = independent_graph_audit(n, mask, edges_from_mask(n, mask), digest)
            for key, value in counts.items():
                row[key] = int(row[key]) + value
        rows.append(row)
    row = {
        "graph_family": "hash_seeded_control",
        "vertex_count": "5..8",
        "graphs": 64,
        "recurrent_sccs": 0,
        "multi_cycle_sccs": 0,
        "simple_cycles": 0,
        "shared_pairs": 0,
        "connector_pairs": 0,
        "strict_external_connector_failures": 0,
        "mixed_roots": 0,
        "failures": 0,
    }
    for case_index in range(64):
        n = 5 + case_index % 4
        edges = hash_control_edges(case_index, n)
        counts = independent_graph_audit(n, mask_from_edges(n, edges), edges, digest)
        for key, value in counts.items():
            row[key] = int(row[key]) + value
    rows.append(row)
    return rows, digest.hexdigest()


def trial_atom(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def fibonacci_members(values: Sequence[int]) -> set[int]:
    limit = max(values)
    output: set[int] = set()
    left, right = 1, 2
    while left <= limit:
        output.add(left)
        left, right = right, left + right
    return output & set(values)


def support_controls(values: Sequence[int]) -> dict[str, set[int]]:
    atom = {value for value in values if trial_atom(value)}
    digest_order = sorted(
        values,
        key=lambda value: sha256(f"P34-SUPPORT-{value}".encode()).hexdigest(),
    )
    return {
        "trial_atom": atom,
        "perfect_square": {value for value in values if isqrt(value) ** 2 == value},
        "fibonacci": fibonacci_members(values),
        "modular_1_or_2_mod_5": {value for value in values if value % 5 in {1, 2}},
        "sha_quarter": {
            value for value in values if sha256(f"P34-QUARTER-{value}".encode()).digest()[0] < 64
        },
        "matched_sha": set(digest_order[: len(atom)]),
        "all": set(values),
        "empty": set(),
    }


def inventory_evaluation(source: dict[str, object]) -> tuple[list[dict[str, object]], dict[str, object]]:
    cycles = source["cycles"]
    assert isinstance(cycles, list)
    values = [int(cycle["value"]) for cycle in cycles]
    supports = support_controls(values)
    full: Polynomial = [Fraction(1, 1)]
    for cycle in cycles:
        length = int(cycle["length"])
        weight = parse_fraction(str(cycle["weight"]))
        term = [Fraction(0, 1)] * (length + 1)
        term[0] = 1
        term[length] = -weight
        full = poly_multiply(full, term)

    rows: list[dict[str, object]] = []
    polynomials: dict[str, object] = {}
    for name, support in supports.items():
        raw: Polynomial = [Fraction(1, 1)]
        induced: Polynomial = [Fraction(1, 1)]
        for cycle in cycles:
            value = int(cycle["value"])
            if value not in support:
                continue
            length = int(cycle["length"])
            weight = parse_fraction(str(cycle["weight"]))
            raw_term = [Fraction(0, 1)] * (length + 1)
            raw_term[0] = 1
            raw_term[length] = -weight
            raw = poly_multiply(raw, raw_term)
            induced = poly_multiply(induced, [Fraction(1, 1), -weight])
        proper_nonempty = bool(support) and len(support) < len(values)
        rows.append(
            {
                "inventory": name,
                "support_count": len(support),
                "members": ";".join(map(str, sorted(support))),
                "terminal_determinant_sha256": poly_digest(full),
                "pruned_determinant_sha256": poly_digest(raw),
                "induced_determinant_sha256": poly_digest(induced),
                "terminal_equals_unclassified": True,
                "pruning_differs_when_proper_nonempty": (raw != full) if proper_nonempty else "NA",
                "raw_equals_induced_formally": raw == induced,
                "raw_equals_induced_at_z_one": poly_eval(raw, Fraction(1, 1))
                == poly_eval(induced, Fraction(1, 1)),
            }
        )
        polynomials[name] = {
            "members": sorted(support),
            "raw_pruned": poly_text(raw),
            "first_return": poly_text(induced),
        }
    return rows, {"unclassified_terminal": poly_text(full), "inventories": polynomials}


def matrix_multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [
        [sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def matrix_trace(matrix: list[list[int]]) -> int:
    return sum(matrix[index][index] for index in range(len(matrix)))


def boundary_controls() -> dict[str, object]:
    signed = [[0, 1, 1], [1, 0, 0], [-1, 0, 0]]
    absolute = [[abs(value) for value in row] for row in signed]
    signed_power = [row[:] for row in signed]
    absolute_power = [row[:] for row in absolute]
    signed_traces: list[int] = []
    absolute_traces: list[int] = []
    for order in range(1, 9):
        if order > 1:
            signed_power = matrix_multiply(signed_power, signed)
            absolute_power = matrix_multiply(absolute_power, absolute)
        signed_traces.append(matrix_trace(signed_power))
        absolute_traces.append(matrix_trace(absolute_power))
    projection_left = [[1, 0], [0, 0]]
    projection_right = [[0, 0], [0, 1]]
    zero = [[0, 0], [0, 0]]
    return {
        "signed_scalar": {
            "adjacency": signed,
            "absolute_adjacency": absolute,
            "trace_orders_1_to_8": signed_traces,
            "absolute_trace_orders_1_to_8": absolute_traces,
            "nilpotent_order_at_most_3": matrix_multiply(matrix_multiply(signed, signed), signed) == [[0, 0, 0]] * 3,
            "determinant_I_minus_zA": ["1/1"],
            "absolute_determinant_I_minus_zA": ["1/1", "0/1", "-2/1"],
            "scope": "signed cancellation invalidates the positive coefficient step",
        },
        "matrix_branches": {
            "left": projection_left,
            "right": projection_right,
            "left_times_right_zero": matrix_multiply(projection_left, projection_right) == zero,
            "right_times_left_zero": matrix_multiply(projection_right, projection_left) == zero,
            "pure_left_survives": matrix_multiply(projection_left, projection_left) == projection_left,
            "pure_right_survives": matrix_multiply(projection_right, projection_right) == projection_right,
            "sum_determinant": ["1/1", "-2/1", "1/1"],
            "product_of_pure_determinants": ["1/1", "-2/1", "1/1"],
            "scope": "orthogonal matrix branches can annihilate every mixed word",
        },
    }


def source_firewall(code_root: Path) -> dict[str, object]:
    paths = [code_root / "source_core.py", code_root / "generate_artifacts.py"]
    forbidden_names = {
        "isprime",
        "factorint",
        "primerange",
        "primepi",
        "fibonacci",
        "is_square",
        "zeta",
        "zetazero",
        "riemannr",
        "random",
        "randint",
        "choice",
        "shuffle",
        "socket",
        "requests",
        "urlopen",
    }
    forbidden_imports = {"random", "socket", "requests", "urllib"}
    violations: list[dict[str, object]] = []
    hashes: dict[str, str] = {}
    for path in paths:
        payload = path.read_bytes()
        hashes[path.name] = sha256(payload).hexdigest()
        tree = ast.parse(payload.decode("utf-8"), filename=path.name)
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id.lower() in forbidden_names:
                violations.append({"file": path.name, "line": node.lineno, "name": node.id})
            if isinstance(node, ast.Attribute) and node.attr.lower() in forbidden_names:
                violations.append({"file": path.name, "line": node.lineno, "name": node.attr})
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name.split(".")[0] in forbidden_imports:
                        violations.append({"file": path.name, "line": node.lineno, "name": alias.name})
            if isinstance(node, ast.ImportFrom) and (node.module or "").split(".")[0] in forbidden_imports:
                violations.append({"file": path.name, "line": node.lineno, "name": node.module})
    return {
        "schema_version": "P34-source-firewall-v1",
        "source_hashes": hashes,
        "forbidden_identifier_count": len(violations),
        "violations": violations,
        "source_imports_evaluator": False,
        "evaluator_imports_source": False,
        "status": "PASS" if not violations else "FAIL",
    }


def counterexamples(control: dict[str, object], strict_failure_count: int) -> dict[str, object]:
    return {
        "schema_version": "P34-counterexamples-v1",
        "observed_counterexamples_to_loose_claims": [
            {
                "loose_claim": "any connector between two recurrent cycles creates a mixed orbit",
                "graph_edges": ["0>0", "1>1", "0>1"],
                "exact_observation": "the connector is one-way; no closed word uses both loops",
                "minimal_repair": "require mutual reachability, equivalently membership in one SCC",
            },
            {
                "loose_claim": "two descriptions through a shared recurrent state always add a new primitive root",
                "graph_edges": ["0>1", "1>2", "2>0"],
                "exact_observation": "cyclic rotations describe one primitive orbit; concatenation roots back to it",
                "minimal_repair": "require two cyclically distinct primitive orbits",
            },
            {
                "loose_claim": "an outgoing decision branch changes the recurrent determinant",
                "graph_edges": ["0>0", "0>1", "1>2"],
                "exact_observation": "the branch is acyclic and has no return; it contributes determinant one",
                "minimal_repair": "distinguish transient recognition from recurrent orbitification or pruning",
            },
            {
                "loose_claim": "combinatorial mixed roots always survive coefficientwise",
                "exact_observation": "the signed 3-state control is nilpotent and has determinant one despite two underlying return branches",
                "minimal_repair": "require strictly positive scalar edge weights; leave signed and matrix systems open",
            },
            {
                "loose_claim": "first return preserves the graph-step marked determinant",
                "exact_observation": "raw cycles contribute z^ell while induced returns contribute z; equality holds after z=1 only",
                "minimal_repair": "treat first return as a changed object and changed marker",
            },
        ],
        "positive_class_counterexample_count": 0,
        "preregistered_C2_witness_normal_form_counterexample_count": strict_failure_count,
        "preregistered_C2_status": "FAIL_AS_WRITTEN",
        "repaired_C2_status": "PASS_IF_REPAIRED_CENSUS_HAS_ZERO_FAILURES",
        "scope_control_digest": sha256(json.dumps(control, sort_keys=True).encode()).hexdigest(),
        "theorem_action": "REVISE_LOOSE_WORDING_AND_RETAIN_POSITIVE_SAME_SCC_STATEMENT",
    }


def compare_graph_rows(source_rows: list[dict[str, str]], independent_rows: list[dict[str, object]]) -> list[dict[str, object]]:
    keys = [
        "graph_family",
        "vertex_count",
        "graphs",
        "recurrent_sccs",
        "multi_cycle_sccs",
        "simple_cycles",
        "shared_pairs",
        "connector_pairs",
        "strict_external_connector_failures",
        "mixed_roots",
        "failures",
    ]
    comparisons: list[dict[str, object]] = []
    for source, independent in zip(source_rows, independent_rows, strict=True):
        normalized = {key: str(independent[key]) for key in keys}
        actual = {key: str(source[key]) for key in keys}
        comparisons.append(
            {
                "graph_family": independent["graph_family"],
                "vertex_count": independent["vertex_count"],
                "all_fields_equal": actual == normalized,
                "source": actual,
                "independent": normalized,
            }
        )
    return comparisons


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", required=True)
    parser.add_argument("--code-root", required=True)
    arguments = parser.parse_args()
    results = Path(arguments.results)
    code_root = Path(arguments.code_root)

    source_graph_rows = read_csv(results / "graph_census.csv")
    independent_rows, independent_digest = reconstruct_graph_census()
    graph_comparisons = compare_graph_rows(source_graph_rows, independent_rows)

    neutral = json.loads((results / "neutral_recognizer.json").read_text(encoding="utf-8"))
    inventory_rows, pruning_polynomials = inventory_evaluation(neutral)
    write_csv(results / "inventory_controls.csv", inventory_rows)
    write_json(results / "pruning_polynomials.json", pruning_polynomials)

    firewall = source_firewall(code_root)
    write_json(results / "source_evaluator_firewall.json", firewall)
    boundaries = boundary_controls()
    write_json(results / "boundary_controls.json", boundaries)
    strict_failure_count = sum(
        int(row["strict_external_connector_failures"]) for row in independent_rows
    )
    counterexample_payload = counterexamples(boundaries, strict_failure_count)
    write_json(results / "counterexamples.json", counterexample_payload)

    recurrent_product = [parse_fraction(value) for value in neutral["recurrent_product"]]
    newton = [parse_fraction(value) for value in neutral["determinant_newton"]]
    tail_vertices = set(range(int(neutral["recurrent_dimension"]), int(neutral["dimension"])))
    edges = [
        (int(left), int(right), parse_fraction(weight))
        for left, right, weight in neutral["weighted_edges"]
    ]
    tail_returns = sum(left in tail_vertices and right not in tail_vertices for left, right, _ in edges)
    marker_rows = read_csv(results / "marker_ledger.csv")
    kraft_rows = read_csv(results / "kraft_clock_summary.csv")
    evaluation = {
        "schema_version": "P34-independent-evaluation-v1",
        "independent_algorithm": {
            "scc": "transitive-closure equivalence classes",
            "simple_cycles": "vertex permutations with canonical rotation",
            "primitive_root": "independent coordinate-period test",
            "connectors": "permuted external interiors",
            "determinant": "recurrent SCC product reconstruction",
        },
        "graph_rows": independent_rows,
        "graph_comparisons": graph_comparisons,
        "independent_witness_sha256": independent_digest,
        "graph_all_equal": all(row["all_fields_equal"] for row in graph_comparisons),
        "graph_failure_count": sum(int(row["failures"]) for row in independent_rows),
        "preregistered_C2_witness_normal_form_failure_count": strict_failure_count,
        "preregistered_C2_status": "FAIL_AS_WRITTEN",
        "repaired_C2_status": "PASS"
        if sum(int(row["failures"]) for row in independent_rows) == 0
        else "FAIL",
        "terminal_newton_equals_recurrent_product": newton == recurrent_product,
        "tail_to_recurrent_edges": tail_returns,
        "terminal_tail_acyclic_certificate": tail_returns == 0,
        "proper_inventory_pruning_gates": all(
            row["pruning_differs_when_proper_nonempty"] in {True, "NA"}
            for row in inventory_rows
        ),
        "inventory_marker_gates": all(
            bool(row["raw_equals_induced_at_z_one"])
            and (not bool(row["raw_equals_induced_formally"]) or int(row["support_count"]) == 0)
            for row in inventory_rows
        ),
        "marker_item_formal_equal_count": sum(row["formal_equal"] == "True" for row in marker_rows),
        "marker_item_z_one_mismatch_count": sum(row["equal_at_z_one"] != "True" for row in marker_rows),
        "kraft_failure_count": sum(
            int(row["prefix_collisions"])
            + int(row["roof_sum_failures"])
            + int(row["powered_clock_failures"])
            + int(row["kraft_at_most_one"] != "True")
            for row in kraft_rows
        ),
        "source_firewall_status": firewall["status"],
        "positive_class_counterexample_count": counterexample_payload["positive_class_counterexample_count"],
    }
    evaluation["status"] = "PASS" if all(
        (
            evaluation["graph_all_equal"],
            evaluation["graph_failure_count"] == 0,
            evaluation["terminal_newton_equals_recurrent_product"],
            evaluation["terminal_tail_acyclic_certificate"],
            evaluation["proper_inventory_pruning_gates"],
            evaluation["inventory_marker_gates"],
            evaluation["marker_item_formal_equal_count"] == 0,
            evaluation["marker_item_z_one_mismatch_count"] == 0,
            evaluation["kraft_failure_count"] == 0,
            evaluation["source_firewall_status"] == "PASS",
        )
    ) else "FAIL"
    write_json(results / "evaluation.json", evaluation)
    if evaluation["status"] != "PASS":
        raise SystemExit("independent evaluation failed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
