#!/usr/bin/env python3
"""Generate neutral Paper 34 finite exact artifacts."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from source_core import (
    code_clock_audit,
    exhaustive_graph_census,
    marker_ledger,
    neutral_recurrent_system,
)


def write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        raise ValueError(f"empty CSV payload for {path.name}")
    fields = list(rows[0]) + sorted(
        set().union(*(row.keys() for row in rows)) - set(rows[0])
    )
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    arguments = parser.parse_args()
    output = Path(arguments.output)
    output.mkdir(parents=True, exist_ok=False)

    graph = exhaustive_graph_census()
    write_csv(output / "graph_census.csv", graph["rows"])
    write_csv(output / "graph_witness_samples.csv", graph["samples"])
    write_json(
        output / "graph_witness_summary.json",
        {
            "schema_version": "P34-graph-witness-v1",
            "witness_sha256": graph["witness_sha256"],
            "failure_count": len(graph["failures"]),
            "failures": graph["failures"],
            "strict_external_connector_failure_count": len(
                graph["construction_counterexamples"]
            ),
        },
    )
    write_csv(
        output / "connector_construction_counterexamples.csv",
        graph["construction_counterexamples"],
    )

    code_clock = code_clock_audit()
    write_csv(output / "kraft_clock_summary.csv", code_clock["summary"])
    write_csv(output / "code_clock_ledger.csv", code_clock["ledger"])

    write_json(output / "neutral_recognizer.json", neutral_recurrent_system())
    write_csv(output / "marker_ledger.csv", marker_ledger())
    write_json(
        output / "parameters.json",
        {
            "schema_version": "P34-parameters-v1",
            "exhaustive_vertex_counts": [1, 2, 3, 4],
            "hash_graph_controls": 64,
            "hash_graph_vertex_counts": [5, 6, 7, 8],
            "code_alphabet_sizes": [2, 3, 4],
            "code_cutoffs": [31, 127, 511, 2047],
            "neutral_values": [2, 18],
            "weight_exponent": 2,
            "result_timestamps": False,
            "external_dependencies": [],
            "external_data": False,
        },
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
