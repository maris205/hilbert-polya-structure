#!/usr/bin/env python3
"""Hostile semantic mutations for the C77 independent checker."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile


PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c77_subgroup_mobius_reliability_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c77_subgroup_mobius_reliability_checker.py"


def mutate(document: dict, path: list[object], value: object) -> dict:
    result = deepcopy(document)
    node = result
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    return result


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = {
        "schema": mutate(original, ["schema_id"], "hcs-c77-mutated-v1"),
        "status": mutate(original, ["status"], "RELEASED"),
        "scope": mutate(original, ["scope_literal"], "BAD_EULER_ALLOWED"),
        "c76_authority": mutate(original, ["authority", "c76"], "0" * 64),
        "c76_manifest_authority": mutate(original, ["authority", "c76_manifest"], "1" * 64),
        "c75_authority": mutate(original, ["authority", "c75"], "2" * 64),
        "c73_authority": mutate(original, ["authority", "c73"], "3" * 64),
        "c73_manifest_authority": mutate(original, ["authority", "c73_manifest"], "4" * 64),
        "row_index": mutate(original, ["subgroup_poset", "rows", 0, "subgroup_index"], 1),
        "n_H_vector": mutate(original, ["subgroup_poset", "n_H_vector", 19], 15),
        "inclusion_matrix": mutate(original, ["subgroup_poset", "inclusion_matrix", 0, 19], 0),
        "mobius_diagonal": mutate(original, ["mobius_matrix", 19, 19], 0),
        "row_n_H": mutate(original, ["subgroup_poset", "rows", 19, "n_H"], 15),
        "P_leq": mutate(original, ["subgroup_poset", "rows", 19, "P_leq_polynomial", "0"], 0),
        "P_eq": mutate(original, ["subgroup_poset", "rows", 19, "P_eq_polynomial", "0"], 2),
        "direct_count": mutate(original, ["subgroup_poset", "rows", 19, "direct_support_count"], 0),
        "direct_cardinality": mutate(
            original,
            ["subgroup_poset", "rows", 19, "direct_by_retained_cardinality", "3"],
            0,
        ),
        "generated_count": mutate(
            original, ["direct_enumeration", "generated_support_count_by_subgroup", "19"], 0
        ),
        "retained_total": mutate(
            original, ["direct_enumeration", "retained_cardinality_total", 3], 1
        ),
        "sum_polynomial": mutate(original, ["reliability", "sum_exact_polynomial", "0"], 2),
        "top_polynomial": mutate(original, ["reliability", "top_polynomial", "0"], 2),
        "top_match": mutate(original, ["reliability", "top_matches_c73"], False),
        "grid_denominator": mutate(original, ["reliability", "rational_grid_denominator"], 19),
        "nonnegative": mutate(original, ["reliability", "nonnegative_on_rational_grid"], False),
        "semantics_claim": mutate(original, ["claims", "direct_65536_support_semantics"], False),
    }

    rejected: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c77-mutations-") as temporary:
        for name, document in mutations.items():
            path = Path(temporary) / f"{name}.json"
            path.write_bytes((json.dumps(document, sort_keys=True, separators=(",", ":")) + "\n").encode())
            run = subprocess.run(
                [sys.executable, str(CHECKER), "--evidence", str(path)],
                cwd=PROJECT,
                capture_output=True,
                text=True,
            )
            assert run.returncode != 0, f"mutation accepted: {name}\nstdout={run.stdout}\nstderr={run.stderr}"
            rejected.append(name)

    print(json.dumps({
        "status": "MUTATION_TEST_PASS",
        "mutations_rejected": len(rejected),
        "names": sorted(rejected),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
