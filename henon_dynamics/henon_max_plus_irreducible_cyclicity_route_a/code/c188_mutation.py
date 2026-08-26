#!/usr/bin/env python3
"""Repaired-hash semantic and stale-hash attacks against the C188 checker."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c188_max_plus_evidence.json"
CHECKER_PATH = ROOT / "code/c188_max_plus_checker.py"


def load_checker():
    spec = importlib.util.spec_from_file_location("c188_independent_checker", CHECKER_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def repair(data: dict) -> None:
    data.pop("payload_sha256", None)
    raw = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()


def locate(data: Any, path: tuple[Any, ...]) -> tuple[Any, Any]:
    parent = data
    for key in path[:-1]:
        parent = parent[key]
    return parent, path[-1]


def change_scalar(data: dict, path: tuple[Any, ...]) -> None:
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
    for source_index, source in enumerate(released["source_registry"]):
        for key, value in source.items():
            if key == "authors":
                paths.append(("source_registry", source_index, "authors", 0))
            else:
                paths.append(("source_registry", source_index, key))
    paths += [("nonclaims", index) for index in range(len(released["nonclaims"]))]
    for key in [
        "matrix_count", "vector_row_count", "simple_cycle_count",
        "critical_component_count", "csr_cells_checked", "propagation_cells_checked",
    ]:
        paths.append(("finite_regression", key))

    row_path = ("finite_regression", "matrix_rows", 0)
    paths += [
        row_path + ("matrix_id",), row_path + ("dimension",), row_path + ("support_edge_count",),
        row_path + ("lambda",), row_path + ("gamma",), row_path + ("minimal_matrix_power_period",),
        row_path + ("minimal_transient",), row_path + ("csr_transient",), row_path + ("primitive",),
        row_path + ("simple_cycles", 0, "length"), row_path + ("simple_cycles", 0, "weight"),
        row_path + ("simple_cycles", 0, "mean"), row_path + ("simple_cycles", 0, "critical"),
        row_path + ("critical_components", 0, "cyclicity"),
    ]
    vector_path = ("finite_regression", "vector_rows", 0)
    paths += [
        vector_path + ("matrix_id",), vector_path + ("vector_id",),
        vector_path + ("eventual_period",), vector_path + ("eventual_transient",),
        vector_path + ("projective_period",), vector_path + ("projective_transient",),
    ]
    paths += [
        ("finite_regression", "unbounded_transient_family", 0, "m"),
        ("finite_regression", "unbounded_transient_family", 0, "minimal_transient"),
        ("finite_regression", "unbounded_transient_family", 0, "bottom_right_formula_at_t"),
        ("finite_regression", "reducible_boundary", "conclusion"),
        ("finite_regression", "reducible_boundary", "component_growth_rates", 0),
    ]

    mutations = []
    for index, path in enumerate(paths):
        mutations.append((f"scalar_{index:03d}_{'_'.join(map(str, path))}", lambda data, p=path: change_scalar(data, p)))

    mutations += [
        ("route_tuple", lambda d: d["route_a"]["tuple"].__setitem__(0, "A0_PASS")),
        ("source_author_population", lambda d: d["source_registry"][1]["authors"].append("Invented Author")),
        ("nonclaim_population", lambda d: d["nonclaims"].append("INVENTED_BOUNDARY")),
        ("matrix_tags", lambda d: d["finite_regression"]["matrix_rows"][0]["tags"].append("invented")),
        ("matrix_A_cell", lambda d: d["finite_regression"]["matrix_rows"][0]["A"][0].__setitem__(0, "17")),
        ("matrix_B_cell", lambda d: d["finite_regression"]["matrix_rows"][0]["B"][0].__setitem__(0, "17")),
        ("cycle_node", lambda d: d["finite_regression"]["matrix_rows"][0]["simple_cycles"][0]["nodes"].__setitem__(0, 1)),
        ("critical_edge", lambda d: d["finite_regression"]["matrix_rows"][0]["critical_edges"][0].__setitem__(0, 1)),
        ("critical_component_node", lambda d: d["finite_regression"]["matrix_rows"][0]["critical_components"][0]["nodes"].__setitem__(0, 1)),
        ("C_cell", lambda d: d["finite_regression"]["matrix_rows"][0]["C"][0].__setitem__(0, "17")),
        ("S_cell", lambda d: d["finite_regression"]["matrix_rows"][0]["S"][0].__setitem__(0, "17")),
        ("R_cell", lambda d: d["finite_regression"]["matrix_rows"][0]["R"][0].__setitem__(0, "17")),
        ("power_T_cell", lambda d: d["finite_regression"]["matrix_rows"][0]["power_at_transient"][0].__setitem__(0, "17")),
        ("power_T_gamma_cell", lambda d: d["finite_regression"]["matrix_rows"][0]["power_one_period_later"][0].__setitem__(0, "17")),
        ("vector_x", lambda d: d["finite_regression"]["vector_rows"][0]["x"].__setitem__(0, "17")),
        ("vector_attraction", lambda d: d["finite_regression"]["vector_rows"][0]["attraction_divisors"].append(999)),
        ("projective_attraction", lambda d: d["finite_regression"]["vector_rows"][0]["projective_attraction_divisors"].append(999)),
        ("transient_family_population", lambda d: d["finite_regression"]["unbounded_transient_family"].pop()),
        ("reducible_A", lambda d: d["finite_regression"]["reducible_boundary"]["A"][0].__setitem__(0, "17")),
        ("reducible_power", lambda d: d["finite_regression"]["reducible_boundary"]["powers_t_1_to_5"][0][0].__setitem__(0, "17")),
    ]

    rejected = 0
    for name, mutate in mutations:
        attacked = deepcopy(released)
        mutate(attacked)
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
        "status": "C188_MUTATION_PASS",
        "repaired_hash_rejections": rejected,
        "stale_hash_rejections": stale_rejected,
        "total_rejections": rejected + stale_rejected,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
