#!/usr/bin/env python3
"""Hostile semantic and repaired-hash mutations for C251."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c251_majority_evidence.json"
CHECKER = ROOT / "code/c251_majority_checker.py"


def repair(item: dict) -> dict:
    body = dict(item)
    body.pop("payload_sha256", None)
    item["payload_sha256"] = sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    return item


def main() -> None:
    pristine = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    def add(name: str, change, repaired: bool = False) -> None:
        item = deepcopy(pristine)
        change(item)
        mutations.append((name, repair(item) if repaired else item))

    # Provenance and frozen object.
    add("schema", lambda x: x.__setitem__("schema", "wrong"))
    add("candidate", lambda x: x.__setitem__("candidate_id", "HCS-C000"))
    add("date", lambda x: x.__setitem__("evaluation_date", "2026-08-31"))
    add("source_commit", lambda x: x.__setitem__("source_commit", "0" * 40))
    add("evaluator", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("fixed_epoch", lambda x: x.__setitem__("fixed_epoch", 0))
    add("map_repaired", lambda x: x["frozen_object"].__setitem__("map", "asynchronous update"), True)
    add("clock_repaired", lambda x: x["frozen_object"].__setitem__("clock", "random clock"), True)
    add("wall_repaired", lambda x: x["frozen_object"].__setitem__("wall_coordinate", "none"), True)
    add("normalization", lambda x: x["frozen_object"].__setitem__("normalization", "unlabelled only"))
    # Theorem text and transfer receipts.
    add("theorem_wall", lambda x: x["theorem"].__setitem__("wall_update", "wrong"))
    add("theorem_bound", lambda x: x["theorem"].__setitem__("transient_bound", "unbounded"))
    add("matrix_cell", lambda x: x["regression"]["fixed_debruijn_matrix"][0].__setitem__(0, 99), True)
    add("matrix_charpoly", lambda x: x["regression"].__setitem__("fixed_matrix_characteristic_polynomial", "lambda"), True)
    add("fixed_trace", lambda x: x["regression"]["fixed_formula_rows"][7].__setitem__("fixed_count_trace", 999), True)
    add("lucas", lambda x: x["regression"]["fixed_formula_rows"][5].__setitem__("lucas_number", 999), True)
    add("cosine", lambda x: x["regression"]["fixed_formula_rows"][3].__setitem__("sixth_root_trace", 999), True)
    add("period_two", lambda x: x["regression"]["fixed_formula_rows"][1].__setitem__("period_two_orbit_count", 2), True)
    add("wall_plain", lambda x: x["regression"]["wall_run_rows"][12].__setitem__("cyclic_wall_words_all_parities", 999), True)
    add("wall_even", lambda x: x["regression"]["wall_run_rows"][17].__setitem__("cyclic_wall_words_even_parity", 999), True)
    add("wall_bound", lambda x: x["regression"]["wall_run_rows"][21].__setitem__("max_run_bound", 99), True)
    add("finite_state", lambda x: x["regression"]["finite_state_rows"][7].__setitem__("max_entry_time", 99), True)
    add("depth_hist", lambda x: x["regression"]["finite_state_rows"][8]["depth_histogram_fixed_at_t"].__setitem__(1, 999), True)
    add("wall_hist", lambda x: x["regression"]["finite_state_rows"][9]["wall_run_histogram"].__setitem__(2, 999), True)
    add("alternating", lambda x: x["regression"]["finite_state_rows"][5].__setitem__("alternating_states", []), True)
    add("sample", lambda x: x["regression"]["sample_trajectories"][0]["trajectory"].append("11111111"), True)
    add("truth", lambda x: x["regression"]["rule_truth_table"][0].__setitem__("output", 1), True)
    add("grid", lambda x: x["regression"]["parameter_grid"][2].__setitem__("n", 99), True)
    add("row_count", lambda x: x["regression"]["row_counts"].__setitem__("wall_run", 1), True)
    # Route, scope, citations, and structural attacks.
    add("identity_formula", lambda x: x["exact_identities"][0].__setitem__("formula", "wrong"))
    add("route_tuple", lambda x: x["route_a"]["tuple"].__setitem__(1, "A1_FAIL"), True)
    add("route_overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True), True)
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_euler_factors", True), True)
    add("citation_doi", lambda x: x["citations"][0].__setitem__("doi", "10.0000/fake"), True)
    add("citation_url", lambda x: x["citations"][1].__setitem__("url", "https://example.invalid"))
    add("nonclaim", lambda x: x["nonclaims"].__setitem__(0, "we claim a target divisor"), True)
    add("unknown_key", lambda x: x["theorem"].__setitem__("unexpected", True))
    add("stale_hash", lambda x: x.__setitem__("payload_sha256", "0" * 64))
    add("missing_rows", lambda x: x["regression"]["fixed_formula_rows"].pop())

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    caught: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c251-majority-mutations-") as td:
        for name, item in mutations:
            path = Path(td) / f"{name}.json"
            path.write_text(json.dumps(item, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            proc = subprocess.run([sys.executable, "-B", str(CHECKER), "--input", str(path)], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if proc.returncode != 0:
                caught.append(name)
    assert len(caught) == len(mutations), f"uncaught mutations: {set(name for name, _ in mutations) - set(caught)}"
    print(f"C251 hostile mutations: PASS {len(caught)}/{len(mutations)}")
    print("caught=" + ",".join(caught))


if __name__ == "__main__":
    main()
