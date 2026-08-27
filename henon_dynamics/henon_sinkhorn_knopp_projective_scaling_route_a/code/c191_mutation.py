#!/usr/bin/env python3
"""Repaired-hash semantic and stale-hash attacks against the C191 checker."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
from typing import Any, Callable

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c191_sinkhorn_evidence.json"
CHECKER_PATH = ROOT / "code/c191_sinkhorn_checker.py"


def load_checker():
    spec = importlib.util.spec_from_file_location("c191_independent_checker", CHECKER_PATH)
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


def replace_gram_by_square_spectrum(data: dict[str, Any]) -> None:
    case = data["finite_regression"]["positive_cases"][-1]
    matrix = sp.Matrix([[sp.Rational(value) for value in row] for row in case["target_doubly_stochastic"]])
    wrong = (matrix * matrix).eigenvals()
    case["local_gram_spectrum"] = [
        {"eigenvalue": str(value), "multiplicity": int(multiplicity)}
        for value, multiplicity in sorted(wrong.items(), key=lambda pair: str(pair[0]))
    ]


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
    for key in ["pattern_row_count", "positive_case_count", "boundary_case_count", "iteration_step_count", "cross_ratio_count"]:
        paths.append(("finite_regression", key))
    for n in ("2", "3"):
        for key in finite["pattern_counts"][n]:
            paths.append(("finite_regression", "pattern_counts", n, key))
    for row_index in (0, len(finite["pattern_rows"]) // 2, len(finite["pattern_rows"]) - 1):
        for key in ["dimension", "mask", "positive_edge_count", "positive_diagonal_count", "support", "total_support", "fully_indecomposable"]:
            paths.append(("finite_regression", "pattern_rows", row_index, key))
        paths.append(("finite_regression", "pattern_rows", row_index, "pattern", 0, 0))
    for case_index, case in enumerate(finite["positive_cases"]):
        base = ("finite_regression", "positive_cases", case_index)
        paths += [base + ("case_id",), base + ("dimension",), base + ("source_matrix", 0, 0), base + ("target_doubly_stochastic", 0, 0), base + ("left_scaling", 0), base + ("right_scaling", 0), base + ("projective_theta",), base + ("birkhoff_kappa",), base + ("full_cycle_contraction_bound",), base + ("local_projective_rate",)]
        paths += [base + ("cross_ratios", 0, "value"), base + ("cross_ratios", 0, "indices", 0)]
        paths += [base + ("local_gram_spectrum", 0, "eigenvalue"), base + ("local_gram_spectrum", 0, "multiplicity")]
        paths += [base + ("iteration_steps", 0, key) for key in ("iteration", "row_error", "column_error", "l1_to_target")]
    for case_index, case in enumerate(finite["boundary_cases"]):
        base = ("finite_regression", "boundary_cases", case_index)
        for key in ["case_id", "support", "total_support", "fully_indecomposable", "positive_diagonal_count"]:
            paths.append(base + (key,))
        paths.append(base + ("pattern", 0, 0))
        if case["iteration_steps"]:
            paths += [base + ("iteration_steps", 0, key) for key in ("iteration", "row_error", "column_error")]
            paths.append(base + ("last_iterate", 0, 0))

    mutations: list[tuple[str, Callable[[dict[str, Any]], None]]] = []
    for index, path in enumerate(paths):
        mutations.append((f"scalar_{index:03d}_{'_'.join(map(str, path))}", lambda data, p=path: change_scalar(data, p)))
    mutations += [
        ("route_tuple", lambda data: data["route_a"]["tuple"].__setitem__(0, "A0_PASS")),
        ("source_population", lambda data: data["source_registry"].append(deepcopy(data["source_registry"][0]))),
        ("author_population", lambda data: data["source_registry"][0]["authors"].append("Invented Author")),
        ("nonclaim_population", lambda data: data["nonclaims"].append("INVENTED_BOUNDARY")),
        ("pattern_population", lambda data: data["finite_regression"]["pattern_rows"].pop()),
        ("positive_population", lambda data: data["finite_regression"]["positive_cases"].pop()),
        ("boundary_population", lambda data: data["finite_regression"]["boundary_cases"].pop()),
        ("cross_ratio_population", lambda data: data["finite_regression"]["positive_cases"][0]["cross_ratios"].pop()),
        ("iteration_population", lambda data: data["finite_regression"]["positive_cases"][0]["iteration_steps"].pop()),
        ("spectrum_population", lambda data: data["finite_regression"]["positive_cases"][0]["local_gram_spectrum"].pop()),
        ("transpose_blind_spot_S_squared", replace_gram_by_square_spectrum),
        ("pattern_row_order", lambda data: data["finite_regression"]["pattern_rows"].reverse()),
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
        "status": "C191_MUTATION_PASS",
        "repaired_hash_rejections": rejected,
        "stale_hash_rejections": stale_rejected,
        "total_rejections": rejected + stale_rejected,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
