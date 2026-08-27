#!/usr/bin/env python3
"""Repaired-hash semantic and stale-hash attacks for C194."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c194_holte_evidence.json"
CHECKER_PATH = ROOT / "code/c194_holte_checker.py"


def load_checker():
    spec = importlib.util.spec_from_file_location("c194_independent_checker", CHECKER_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def repair(document: dict[str, Any]) -> None:
    document.pop("payload_sha256", None)
    raw = json.dumps(document, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    document["payload_sha256"] = sha256(raw).hexdigest()


def locate(document: Any, path: tuple[Any, ...]) -> tuple[Any, Any]:
    parent = document
    for key in path[:-1]:
        parent = parent[key]
    return parent, path[-1]


def change_scalar(document: dict[str, Any], path: tuple[Any, ...]) -> None:
    parent, key = locate(document, path)
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
    scalar_paths: list[tuple[Any, ...]] = [
        ("schema",), ("candidate_id",), ("evaluation_date",), ("source_commit",),
        ("evaluator", "version"), ("evaluator", "path"), ("evaluator", "sha256"),
        ("scope_literal",),
    ]
    scalar_paths += [("source_lock", key) for key in released["source_lock"]]
    scalar_paths += [("attribution", key) for key in released["attribution"]]
    scalar_paths += [("theorem_lock", key) for key in released["theorem_lock"]]
    scalar_paths += [("route_a", "qualifications", key) for key in released["route_a"]["qualifications"]]
    scalar_paths += [("route_a", "overall"), ("route_a", "route_b_invocation_allowed")]
    scalar_paths += [("forbidden_claims", key) for key in released["forbidden_claims"]]
    scalar_paths += [("finite_regression", key) for key, value in released["finite_regression"].items() if isinstance(value, (bool, int, str))]
    scalar_paths += [("nonclaims", index) for index in range(len(released["nonclaims"]))]
    for source_index, source in enumerate(released["source_registry"]):
        for key, value in source.items():
            if isinstance(value, (bool, int, str)):
                scalar_paths.append(("source_registry", source_index, key))
            elif key == "authors":
                scalar_paths.append(("source_registry", source_index, "authors", 0))
            elif key == "theorem_locators":
                scalar_paths.append(("source_registry", source_index, "theorem_locators", 0))

    mutations: list[tuple[str, Callable[[dict[str, Any]], None]]] = []
    for index, path in enumerate(scalar_paths):
        mutations.append((f"scalar_{index:03d}_{'_'.join(map(str, path))}", lambda data, p=path: change_scalar(data, p)))

    for case_index in (0, len(released["cases"]) // 2, len(released["cases"]) - 1):
        base = ("cases", case_index)
        paths = [
            base + ("n",), base + ("base",), base + ("base_class",), base + ("denominator",),
            base + ("transition_numerators", 0, 0), base + ("transition_matrix", 0, 0),
            base + ("eulerian_numbers", 0), base + ("stationary_distribution", 0),
            base + ("eigenvalues", 0), base + ("charpoly_ascending", 0),
            base + ("det_I_minus_zP_ascending", 0), base + ("trace",),
            base + ("power_traces", 1, "direct"), base + ("power_traces", 1, "spectral"),
            base + ("convergence", 0, "worst_total_variation"),
            base + ("convergence", 0, "from_zero_distribution", 0),
            base + ("convergence", 0, "state_total_variation", 0),
        ]
        for path in paths:
            mutations.append((f"case_{case_index}_{'_'.join(map(str, path[2:]))}", lambda data, p=path: change_scalar(data, p)))

    mutations.extend([
        ("route_tuple", lambda data: data["route_a"]["tuple"].__setitem__(0, "A0_ANALYTIC_ARITHMETIC_ORIGIN")),
        ("source_population", lambda data: data["source_registry"].append(deepcopy(data["source_registry"][0]))),
        ("source_author_population", lambda data: data["source_registry"][0]["authors"].append("Invented Author")),
        ("source_locator_population", lambda data: data["source_registry"][0]["theorem_locators"].append("Theorem 99")),
        ("case_population", lambda data: data["cases"].pop()),
        ("case_order", lambda data: data["cases"].reverse()),
        ("matrix_row_population", lambda data: data["cases"][1]["transition_matrix"].pop()),
        ("matrix_column_population", lambda data: data["cases"][1]["transition_matrix"][0].pop()),
        ("power_population", lambda data: data["cases"][1]["power_traces"].pop()),
        ("convergence_population", lambda data: data["cases"][1]["convergence"].pop()),
        ("nonclaim_population", lambda data: data["nonclaims"].append("TARGET_OPERATOR_FOUND")),
        ("attribution_status", lambda data: data["attribution"].__setitem__("status", "NEW_THEOREM_CLAIMED")),
        ("owner_absolute", lambda data: data["attribution"].__setitem__("all_family_proof_owner", "HCS-C194")),
        ("code_role_absolute", lambda data: data["attribution"].__setitem__("code_role", "all-family proof")),
        ("prime_control_overclaim", lambda data: data["theorem_lock"].__setitem__("boundary", data["theorem_lock"]["boundary"] + "; primes are privileged")),
    ])

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
        "status": "C194_MUTATION_PASS",
        "repaired_hash_rejections": rejected,
        "stale_hash_rejections": stale_rejected,
        "total_rejections": rejected + stale_rejected,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
