#!/usr/bin/env python3
"""Repaired-hash semantic and stale-hash attacks against the C193 checker."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c193_markoff_evidence.json"
CHECKER_PATH = ROOT / "code/c193_markoff_checker.py"


def load_checker():
    spec = importlib.util.spec_from_file_location("c193_independent_checker", CHECKER_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def repair(data: dict[str, Any]) -> None:
    data.pop("payload_sha256", None)
    raw = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()


def locate(data: Any, path: tuple[Any, ...]) -> tuple[Any, Any]:
    parent = data
    for key in path[:-1]:
        parent = parent[key]
    return parent, path[-1]


def change_scalar(data: dict[str, Any], path: tuple[Any, ...]) -> None:
    parent, key = locate(data, path)
    value = parent[key]
    if isinstance(value, bool):
        parent[key] = not value
    elif isinstance(value, int):
        parent[key] = value + 1
    elif isinstance(value, str):
        parent[key] = value + "_MUTATED"
    else:
        raise TypeError((path, value))


def main() -> None:
    checker = load_checker()
    released = json.loads(EVIDENCE.read_text())
    paths: list[tuple[Any, ...]] = [
        ("schema",), ("candidate_id",), ("date_utc",), ("source_commit",),
        ("evaluator", "version"), ("evaluator", "path"), ("evaluator", "sha256"),
        ("scope_literal",),
    ]
    paths += [("source_lock", key) for key in released["source_lock"]]
    paths += [("attribution", key) for key in released["attribution"]]
    paths += [("theorem", key) for key in released["theorem"]]
    paths += [("route_a", key) for key in released["route_a"] if key != "tuple"]
    paths += [("scope_flags", key) for key in released["scope_flags"]]
    paths += [("progress_and_boundary", key) for key in released["progress_and_boundary"]]
    paths += [("nonclaims", index) for index in range(len(released["nonclaims"]))]
    for source_index, source in enumerate(released["source_registry"]):
        for key in source:
            if key == "authors":
                paths.append(("source_registry", source_index, "authors", 0))
            else:
                paths.append(("source_registry", source_index, key))

    finite = released["finite_regression"]
    for key in ["max_depth", "tree_row_count", "children_are_one_step_complete", "frontier_child_count", "word_semantics", "maximum_coordinate_digits", "invariance_tests", "brute_bound", "brute_solution_count", "descent_trace_count", "descent_steps_checked"]:
        paths.append(("finite_regression", key))
    for key in finite["level_counts"]:
        paths.append(("finite_regression", "level_counts", key))
    for row_index in (0, 1, len(finite["tree_rows"]) // 2, len(finite["tree_rows"]) - 1):
        row = finite["tree_rows"][row_index]
        base = ("finite_regression", "tree_rows", row_index)
        paths += [base + ("triple", 0), base + ("depth",), base + ("local_child_rank_word",), base + ("height",), base + ("coordinate_sum",), base + ("unique_maximum",)]
        if row["parent"] is not None:
            paths.append(base + ("parent", 0))
        if row["children"]:
            paths.append(base + ("children", 0, 0))
    for solution_index in (0, len(finite["brute_solutions"]) // 2, len(finite["brute_solutions"]) - 1):
        paths.append(("finite_regression", "brute_solutions", solution_index, 0))
    for trace_index in (0, len(finite["descent_traces"]) // 2, len(finite["descent_traces"]) - 1):
        trace = finite["descent_traces"][trace_index]
        base = ("finite_regression", "descent_traces", trace_index)
        paths += [base + ("seed", 0), base + ("depth",), base + ("trace", 0, 0)]

    mutations: list[tuple[str, Callable[[dict[str, Any]], None]]] = []
    for index, path in enumerate(paths):
        mutations.append((f"scalar_{index:03d}_{'_'.join(map(str, path))}", lambda data, p=path: change_scalar(data, p)))
    mutations += [
        ("route_tuple", lambda data: data["route_a"]["tuple"].__setitem__(0, "A0_ANALYTIC_ARITHMETIC_ORIGIN")),
        ("source_population", lambda data: data["source_registry"].append(deepcopy(data["source_registry"][0]))),
        ("author_population", lambda data: data["source_registry"][2]["authors"].append("Invented Author")),
        ("nonclaim_population", lambda data: data["nonclaims"].append("FROBENIUS_PROVED")),
        ("tree_population", lambda data: data["finite_regression"]["tree_rows"].pop()),
        ("tree_order", lambda data: data["finite_regression"]["tree_rows"].reverse()),
        ("child_population", lambda data: data["finite_regression"]["tree_rows"][1]["children"].pop()),
        ("brute_population", lambda data: data["finite_regression"]["brute_solutions"].pop()),
        ("trace_population", lambda data: data["finite_regression"]["descent_traces"].pop()),
        ("trace_length", lambda data: data["finite_regression"]["descent_traces"][-1]["trace"].pop()),
    ]

    rejected = 0
    for name, mutation in mutations:
        attacked = deepcopy(released)
        mutation(attacked)
        repair(attacked)
        try:
            checker.verify(attacked)
        except Exception:
            rejected += 1
        else:
            raise AssertionError(f"repaired-hash mutation accepted: {name}")

    stale = deepcopy(released)
    stale["route_a"]["overall"] = "ROUTE_A_ACCEPTED"
    try:
        checker.verify(stale)
    except Exception:
        stale_rejected = 1
    else:
        raise AssertionError("stale-hash mutation accepted")

    print(json.dumps({
        "status": "C193_MUTATION_PASS",
        "repaired_hash_rejections": rejected,
        "stale_hash_rejections": stale_rejected,
        "total_rejections": rejected + stale_rejected,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
