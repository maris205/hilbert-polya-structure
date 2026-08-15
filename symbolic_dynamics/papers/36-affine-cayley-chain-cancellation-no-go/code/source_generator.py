#!/usr/bin/env python3
"""Generate neutral exact affine-presentation payloads for SD-C38."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path

from source_core import (
    affine_evaluate,
    affine_return_counts,
    finite_chain_data,
    free_return_counts,
    relation_marker_data,
)


MAIN_R = (2, 3, 4, 5)
FINITE_CASES = (
    (1, 4, 3),
    (2, 3, None),
    (3, 4, None),
    (4, 5, None),
    (4, 7, None),
    (5, 6, None),
)
MAX_LENGTH = 12


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def encode_finite(data: dict[str, object]) -> dict[str, object]:
    edges = [
        {
            "index": index,
            "origin": list(origin),
            "label": label,
        }
        for (origin, label), index in sorted(
            data["edge_index"].items(), key=lambda item: item[1]
        )
    ]
    return {
        "r": data["r"],
        "q": data["q"],
        "period": data["period"],
        "vertices": [list(vertex) for vertex in data["vertices"]],
        "edges": edges,
        "boundary_1": data["boundary1"],
        "affine_cell_columns": data["affine_cells"],
        "complete_cell_columns": data["full_cells"],
        "relation_word": data["relation_word"],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result-dir", required=True)
    arguments = parser.parse_args()
    result_dir = Path(arguments.result_dir)
    result_dir.mkdir(parents=True, exist_ok=True)

    free_counts = free_return_counts(MAX_LENGTH)
    affine_counts = {
        str(r): affine_return_counts(r, MAX_LENGTH) for r in (1, *MAIN_R)
    }
    markers = {str(r): relation_marker_data(r) for r in (1, *MAIN_R)}
    finite_rows = [
        encode_finite(finite_chain_data(r, q, period))
        for r, q, period in FINITE_CASES
    ]

    tests: list[dict[str, object]] = []
    for r in MAIN_R:
        relation = tuple(["v", "u", "V"] + ["U"] * r)
        tests.extend(
            [
                {
                    "name": f"source_relation_identity_r{r}",
                    "pass": affine_evaluate(r, relation) == (Fraction(0), 0),
                },
                {
                    "name": f"source_count_length_r{r}",
                    "pass": len(affine_counts[str(r)]) == MAX_LENGTH + 1,
                },
                {
                    "name": f"source_marker_failure_r{r}",
                    "pass": not markers[str(r)]["unit_step_marker_descends"],
                },
            ]
        )
    tests.extend(
        [
            {
                "name": "source_balanced_relation_identity",
                "pass": affine_evaluate(1, ("v", "u", "V", "U"))
                == (Fraction(0), 0),
            },
            {
                "name": "source_balanced_marker_descends",
                "pass": markers["1"]["unit_step_marker_descends"],
            },
            {
                "name": "source_free_count_length",
                "pass": len(free_counts) == MAX_LENGTH + 1,
            },
        ]
    )
    for row in finite_rows:
        vertices = len(row["vertices"])
        edges = len(row["edges"])
        tests.extend(
            [
                {
                    "name": f"source_finite_edges_r{row['r']}_q{row['q']}",
                    "pass": edges == 2 * vertices,
                },
                {
                    "name": f"source_affine_cells_r{row['r']}_q{row['q']}",
                    "pass": len(row["affine_cell_columns"]) == vertices,
                },
                {
                    "name": f"source_complete_cells_r{row['r']}_q{row['q']}",
                    "pass": len(row["complete_cell_columns"]) == 3 * vertices,
                },
            ]
        )

    raw = {
        "schema": "SD-C38-source-raw-v1",
        "parameters": {
            "main_r": list(MAIN_R),
            "baseline_r": 4,
            "balanced_r": 1,
            "max_word_length": MAX_LENGTH,
            "alphabet": ["u", "U", "v", "V"],
            "damping_theta": "1/2",
            "finite_cases": [
                [r, q, period if period is not None else "multiplicative_order"]
                for r, q, period in FINITE_CASES
            ],
        },
        "free_identity_counts": free_counts,
        "affine_identity_counts": affine_counts,
        "marker_data": markers,
        "finite_chain_data": finite_rows,
    }
    summary = {
        "schema": "SD-C38-source-summary-v1",
        "r_family_count": len(MAIN_R),
        "finite_case_count": len(finite_rows),
        "word_lengths_including_zero": MAX_LENGTH + 1,
        "source_checks_passed": sum(bool(row["pass"]) for row in tests),
        "source_checks_total": len(tests),
        "all_source_checks_pass": all(bool(row["pass"]) for row in tests),
    }
    test_report = {
        "schema": "SD-C38-source-test-report-v1",
        "tests": tests,
        "passed": summary["source_checks_passed"],
        "total": summary["source_checks_total"],
        "all_pass": summary["all_source_checks_pass"],
    }
    write_json(result_dir / "source_raw.json", raw)
    write_json(result_dir / "source_summary.json", summary)
    write_json(result_dir / "source_test_report.json", test_report)
    print(json.dumps(summary, sort_keys=True))
    if not summary["all_source_checks_pass"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
