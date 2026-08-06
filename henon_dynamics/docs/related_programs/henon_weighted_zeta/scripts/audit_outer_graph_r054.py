#!/usr/bin/env python3
"""Build exploratory directed graphs from the exact R053 outer rectangles."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from fractions import Fraction
from pathlib import Path
from typing import Iterable

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from scripts.audit_exact_closed_cover import (
    A_VALUE,
    CONFIGURATIONS,
    ETA,
    MAX_SUBDIVISIONS,
    RADIUS,
    _direction_metrics,
    exact_edge_vector,
    uncapped_adaptive_subdivisions_exact,
)

PROTOCOL = PROJECT_ROOT / "research" / "refine-logs" / "R054_OUTER_GRAPH_PROTOCOL.json"
AREA_BOUND = Fraction(5, 4)
GRAPH_VARIANTS = ("all_closed_graph", "positive_area_graph", "mutual_graph")
LARGEST_SCC_SELECTION_RULE = (
    "maximum_size_then_lexicographically_smallest_sorted_global_node_ids"
)
SCC_NODE_ID_SCHEMA = "sorted_unique_row_major_global_node_ids"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-stem", default="outer_graph_r054")
    parser.add_argument("--output-dir", type=Path, default=PROJECT_ROOT / "results")
    parser.add_argument("--workers", type=int, default=1)
    return parser.parse_args()


def validate_protocol(payload: dict[str, object]) -> None:
    """Refuse production if the frozen R054 protocol was edited inconsistently."""

    protocol_configurations = tuple(
        (int(item["grid"]), Fraction(str(item["grid_offset"])))
        for item in payload["configurations"]  # type: ignore[index]
    )
    code_configurations = tuple((grid, offset) for _, grid, offset in CONFIGURATIONS)
    checks = {
        "run_id": payload.get("run_id") == "R054_OUTER_GRAPH",
        "source_protocol": payload.get("source_protocol")
        == "R053_EXACT_CLOSED_COVER_PROTOCOL.json",
        "a": Fraction(str(payload.get("a"))) == A_VALUE,
        "radius": Fraction(str(payload.get("radius"))) == RADIUS,
        "eta": Fraction(str(payload.get("eta"))) == ETA,
        "maximum_subdivisions": int(payload.get("maximum_subdivisions"))
        == MAX_SUBDIVISIONS,
        "configurations": protocol_configurations == code_configurations,
    }
    if not all(checks.values()):
        raise SystemExit(f"R054 code/protocol mismatch: {checks}")


def edge_hash(
    edges: Iterable[tuple[int, int, str]], direction: str
) -> str:
    """Hash edges using the canonical R053 direction/source/target format."""

    if direction not in {"F", "B"}:
        raise ValueError("direction must be F or B")
    digest = hashlib.sha256()
    for source, target, label in sorted(edges):
        digest.update(
            f"{direction},{source},{target},{label}\n".encode("ascii")
        )
    return digest.hexdigest()


def node_hash(nodes: Iterable[int]) -> str:
    """Hash a sorted row-major node-ID set for cross-run identity checks."""

    digest = hashlib.sha256()
    for node in sorted(nodes):
        digest.update(f"{node}\n".encode("ascii"))
    return digest.hexdigest()


def strongly_connected_components(adjacency: list[set[int]]) -> list[list[int]]:
    """Iterative Kosaraju SCC decomposition for a finite directed graph."""

    count = len(adjacency)
    reverse: list[list[int]] = [[] for _ in range(count)]
    for source, targets in enumerate(adjacency):
        for target in targets:
            reverse[target].append(source)

    visited = [False] * count
    order: list[int] = []
    for start in range(count):
        if visited[start]:
            continue
        visited[start] = True
        stack: list[tuple[int, object]] = [
            (start, iter(sorted(adjacency[start])))
        ]
        while stack:
            node, iterator = stack[-1]
            try:
                target = next(iterator)  # type: ignore[arg-type]
            except StopIteration:
                order.append(node)
                stack.pop()
                continue
            if not visited[target]:
                visited[target] = True
                stack.append((target, iter(sorted(adjacency[target]))))

    components: list[list[int]] = []
    assigned = [False] * count
    for start in reversed(order):
        if assigned[start]:
            continue
        assigned[start] = True
        component: list[int] = []
        stack = [start]
        while stack:
            node = stack.pop()
            component.append(node)
            for source in sorted(reverse[node]):
                if not assigned[source]:
                    assigned[source] = True
                    stack.append(source)
        components.append(component)
    return components


def graph_stats(adjacency: list[set[int]], active: set[int]) -> dict[str, object]:
    active_nodes = sorted(active)
    index = {node: position for position, node in enumerate(active_nodes)}
    restricted = [
        {index[target] for target in adjacency[node] if target in index}
        for node in active_nodes
    ]
    components = strongly_connected_components(restricted)
    global_components = [
        sorted(active_nodes[local_node] for local_node in component)
        for component in components
    ]
    # Canonicalize independently of set traversal and Kosaraju discovery
    # order.  Equal-size SCCs are resolved by the lexicographically smallest
    # sorted list of global row-major node IDs.
    global_components.sort(key=lambda nodes: (-len(nodes), tuple(nodes)))
    sizes = [len(nodes) for nodes in global_components]
    largest_node_ids = global_components[0] if global_components else []
    largest_size = len(largest_node_ids)
    largest_tie_count = sum(
        len(nodes) == largest_size for nodes in global_components
    )
    nontrivial = [
        component
        for component in components
        if len(component) > 1 or component[0] in restricted[component[0]]
    ]
    recurrent_nodes = sum(len(component) for component in nontrivial)
    return {
        "active_node_count": len(active_nodes),
        "induced_edge_count": sum(len(targets) for targets in restricted),
        "scc_count": len(components),
        "largest_scc_size": largest_size,
        "nontrivial_scc_count": len(nontrivial),
        "recurrent_node_count": recurrent_nodes,
        "recurrent_node_fraction_of_active": (
            recurrent_nodes / len(active) if active else 0.0
        ),
        "largest_scc_fraction_of_active": (
            (sizes[0] / len(active)) if sizes and active else 0.0
        ),
        "top_scc_sizes": sizes[:10],
        "largest_scc_selection_rule": LARGEST_SCC_SELECTION_RULE,
        "largest_scc_tie_count": largest_tie_count,
        "largest_scc_node_id_schema": SCC_NODE_ID_SCHEMA,
        "largest_scc_node_id_count": len(largest_node_ids),
        "largest_scc_node_ids_sha256": node_hash(largest_node_ids),
        "largest_scc_node_ids": largest_node_ids,
    }


def summarize_configuration(configuration: tuple[str, int, Fraction]) -> dict[str, object]:
    name, grid, offset = configuration
    edges = exact_edge_vector(RADIUS, grid, offset)
    widths = [upper - lower for lower, upper in zip(edges, edges[1:])]
    minimum_width = min(widths)
    k_values = [
        uncapped_adaptive_subdivisions_exact(
            edges[index], edges[index + 1], minimum_width
        )
        for index in range(grid)
    ]
    if max(k_values) > MAX_SUBDIVISIONS:
        raise AssertionError("R054 encountered a truncated adaptive K")

    total = grid * grid
    forward_all: list[set[int]] = [set() for _ in range(total)]
    backward_all: list[set[int]] = [set() for _ in range(total)]
    forward_positive: list[set[int]] = [set() for _ in range(total)]
    backward_positive: list[set[int]] = [set() for _ in range(total)]
    two_sided: set[int] = set()
    for source_y in range(grid):
        source_y_interval = (edges[source_y], edges[source_y + 1])
        for source_x in range(grid):
            source_x_interval = (edges[source_x], edges[source_x + 1])
            source_id = source_y * grid + source_x
            forward = _direction_metrics(
                edges,
                source_x_interval,
                source_y_interval,
                k_values[source_x],
                minimum_width,
                False,
            )
            backward = _direction_metrics(
                edges,
                source_x_interval,
                source_y_interval,
                k_values[source_y],
                minimum_width,
                True,
            )
            if forward["area_ratio"] > AREA_BOUND or backward["area_ratio"] > AREA_BOUND:
                raise AssertionError("R054 inherited exact area bound failed")
            forward_all[source_id] = set(forward["target_classes"])
            backward_all[source_id] = set(backward["target_classes"])
            forward_positive[source_id] = {
                target for target, positive in forward["target_classes"].items() if positive
            }
            backward_positive[source_id] = {
                target for target, positive in backward["target_classes"].items() if positive
            }
            if forward["inside"] and backward["inside"]:
                two_sided.add(source_id)

    forward_edges = [
        (source, target, "P" if target in forward_positive[source] else "T")
        for source in range(total)
        for target in sorted(forward_all[source])
    ]
    backward_edges = [
        (source, target, "P" if target in backward_positive[source] else "T")
        for source in range(total)
        for target in sorted(backward_all[source])
    ]
    mutual = [
        target
        for source in range(total)
        for target in forward_all[source]
        if source in backward_all[target]
    ]
    mutual_adjacency = [set() for _ in range(total)]
    for source in range(total):
        mutual_adjacency[source] = {
            target for target in forward_all[source] if source in backward_all[target]
        }

    all_stats = graph_stats(forward_all, two_sided)
    positive_stats = graph_stats(forward_positive, two_sided)
    mutual_stats = graph_stats(mutual_adjacency, two_sided)
    return {
        "configuration": name,
        "grid": grid,
        "grid_offset": float(offset),
        "grid_offset_fraction": str(offset.numerator)
        if offset.denominator == 1
        else f"{offset.numerator}/{offset.denominator}",
        "state_count": total,
        "two_sided_in_box_node_count": len(two_sided),
        "two_sided_in_box_node_fraction": len(two_sided) / total,
        "two_sided_in_box_node_ids_sha256": node_hash(two_sided),
        "forward_closed_edge_count": len(forward_edges),
        "backward_closed_edge_count": len(backward_edges),
        "forward_positive_edge_count": sum(1 for _, _, label in forward_edges if label == "P"),
        "backward_positive_edge_count": sum(1 for _, _, label in backward_edges if label == "P"),
        "mutual_edge_count": len(mutual),
        "forward_closed_edge_hash": edge_hash(forward_edges, "F"),
        "backward_closed_edge_hash": edge_hash(backward_edges, "B"),
        "all_closed_graph": all_stats,
        "positive_area_graph": positive_stats,
        "mutual_graph": mutual_stats,
        "closed_contains_positive": all(
            forward_positive[source] <= forward_all[source]
            for source in range(total)
        ),
        "mutual_subset_closed": all(
            target in forward_all[source]
            for source in range(total)
            for target in mutual_adjacency[source]
        ),
    }


def main() -> None:
    args = parse_args()
    protocol = json.loads(PROTOCOL.read_text(encoding="utf-8"))
    validate_protocol(protocol)
    configurations = [
        (f"n{item['grid']}_d0" if item["grid_offset"] == "0" else f"n{item['grid']}_d{'m1q' if item['grid_offset'] == '-0.25' else 'p1q'}", int(item["grid"]), Fraction(str(item["grid_offset"])))
        for item in protocol["configurations"]
    ]
    if args.workers <= 0:
        raise SystemExit("--workers must be positive")
    workers = min(args.workers, len(configurations))
    if workers == 1:
        records = [summarize_configuration(configuration) for configuration in configurations]
    else:
        with ProcessPoolExecutor(max_workers=workers) as executor:
            records = list(executor.map(summarize_configuration, configurations))
    output = {
        "run_id": "R054_OUTER_GRAPH",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "protocol": str(PROTOCOL.relative_to(PROJECT_ROOT)),
        "records": records,
        "scope": "exact finite outer-cover graph diagnostic; no invariant-set or operator claim",
    }
    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_json = args.output_dir / f"{args.output_stem}.json"
    output_csv = args.output_dir / f"{args.output_stem}.csv"
    output_json.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with output_csv.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    print(json.dumps({"json": str(output_json), "csv": str(output_csv), "workers": workers}, indent=2))


if __name__ == "__main__":
    main()
