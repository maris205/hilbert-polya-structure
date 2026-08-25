#!/usr/bin/env python3
"""Semantic repaired-hash and stale-hash mutation tests for C141."""
from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c141_quadratic_ruelle_evidence.json"
CHECKER = ROOT / "code/c141_quadratic_ruelle_checker.py"


def repair(data: dict) -> None:
    data.pop("payload_sha256", None)
    payload = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    data["payload_sha256"] = hashlib.sha256(payload).hexdigest()


def rejected(data: dict) -> bool:
    with tempfile.TemporaryDirectory(prefix="c141-mutation-") as directory:
        path = Path(directory) / "mutated.json"
        path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n")
        result = subprocess.run([sys.executable, str(CHECKER), "--fast", str(path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return result.returncode != 0


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutators = [
        lambda d: d.__setitem__("schema", "bad"),
        lambda d: d.__setitem__("candidate_id", "HCS-C000"),
        lambda d: d.__setitem__("date_utc", "2026-08-24"),
        lambda d: d.__setitem__("scope", "BROADER_SCOPE"),
        lambda d: d["source_lock"].__setitem__("forward_map", "F(z)=z^2-5"),
        lambda d: d["source_lock"].__setitem__("domain", "D_3"),
        lambda d: d["source_lock"].__setitem__("square_root_convention", "unspecified"),
        lambda d: d["source_lock"].__setitem__("space", "unspecified"),
        lambda d: d["source_lock"].__setitem__("operator_family", "changed"),
        lambda d: d["source_lock"].__setitem__("headline_weight", "m=1"),
        lambda d: d["source_lock"].__setitem__("clock", "two branches per iterate"),
        lambda d: d["source_lock"].__setitem__("determinant_convention", "changed"),
        lambda d: d["source_lock"].__setitem__("cutoff", "n<=6 theorem"),
        lambda d: d["geometry_and_nuclearity"].__setitem__("trace_class", False),
        lambda d: d["geometry_and_nuclearity"].__setitem__("trace_norm_upper_bound", "1"),
        lambda d: d["all_period_theorem"].__setitem__("periodic_points_exhausted", False),
        lambda d: d["all_period_theorem"].__setitem__("escape_bound", "changed"),
        lambda d: d["all_period_theorem"].__setitem__("power_trace_formula", "changed"),
        lambda d: d["all_period_theorem"].__setitem__("headline_trace_formula", "changed"),
        lambda d: d["all_period_theorem"].__setitem__("simple_roots", "changed"),
        lambda d: d["weight_ladder_controls"].__setitem__("m0_trace_formula", "Tr=0"),
        lambda d: d["weight_ladder_controls"].__setitem__("m1_trace_formula", "Tr=1"),
        lambda d: d["weight_ladder_controls"].__setitem__("first_nontrivial_stability_weight", "m=3"),
        lambda d: d["headline_exact_prefix"]["periods"][0].__setitem__("trace_L2_power", "0/1"),
        lambda d: d["headline_exact_prefix"]["periods"][5].__setitem__("primitive_orbits", 10),
        lambda d: d["headline_exact_prefix"]["fredholm_coefficients_c0_through_c6"].__setitem__(2, "0/1"),
        lambda d: d["primitive_product"].__setitem__("inner_index_starts_at", 1),
        lambda d: d["primitive_product"].__setitem__("raw_product_absolute_convergence_domain", "all u"),
        lambda d: d["primitive_product"].__setitem__("global_statement", "raw product entire"),
        lambda d: d["negative_control"].__setitem__("same_D4_branch_model_valid", True),
        lambda d: d["progress"].__setitem__("headline", "overclaim"),
        lambda d: d["route_a"].__setitem__("tuple", ["A1_STRONG", "A2_PASS", "A3_PASS", "A4_PASS"]),
        lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_COMPLETE"),
        lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True),
        lambda d: d["scope_flags"].__setitem__("claims_hilbert_polya", True),
        lambda d: d["scope_flags"].__setitem__("uses_zero_table", True),
    ]
    for index, mutate in enumerate(mutators, 1):
        changed = copy.deepcopy(original)
        mutate(changed)
        repair(changed)
        assert rejected(changed), f"repaired-hash mutation {index} escaped"

    stale = copy.deepcopy(original)
    stale["source_lock"]["forward_map"] = "F(z)=z^2-5"
    assert rejected(stale), "stale-hash sentinel escaped"
    print(f"C141 mutation suite: PASS ({len(mutators)} repaired-hash + 1 stale-hash rejections)")


if __name__ == "__main__":
    main()
