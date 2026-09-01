#!/usr/bin/env python3
"""Repaired-hash semantic mutations and stale-hash control for HCS-C279."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c279_path_tv_evidence.json"
CHECKER = ROOT / "code/c279_path_tv_checker.py"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def accepted(data: dict) -> bool:
    with tempfile.TemporaryDirectory(prefix="c279-mut-") as directory:
        path = Path(directory) / "evidence.json"
        path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        environment = dict(os.environ)
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        environment["C279_EVIDENCE_PATH"] = str(path)
        completed = subprocess.run(
            [sys.executable, "-B", str(CHECKER)],
            env=environment, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        return completed.returncode == 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    assert accepted(base)
    mutations: list[tuple[str, dict]] = []

    def add(name: str, edit) -> None:
        candidate = copy.deepcopy(base)
        edit(candidate)
        candidate["payload_sha256"] = payload_hash(candidate)
        mutations.append((name, candidate))

    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C278"))
    add("schema", lambda d: d.__setitem__("schema", "hcs-c279-broken"))
    add("top_extra", lambda d: d.__setitem__("undeclared", True))
    add("source", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("epoch", lambda d: d.__setitem__("fixed_epoch", 0))
    add("scope", lambda d: d.__setitem__("scope_literal", "WIDENED"))
    add("evaluator_version", lambda d: d["evaluator"].__setitem__("version", "0.1.0"))
    add("evaluator_hash", lambda d: d["evaluator"].__setitem__("sha256", "0" * 64))
    add("model_graph", lambda d: d["model"].__setitem__("graph", "cycle C_n"))
    add("model_incidence", lambda d: d["model"].__setitem__("incidence", "broken"))
    add("model_energy", lambda d: d["model"].__setitem__("energy", "quadratic Dirichlet energy"))
    add("model_flow", lambda d: d["model"].__setitem__("flow", "explicit Euler"))
    add("model_clock", lambda d: d["model"].__setitem__("clock", "event count"))
    add("model_rof", lambda d: d["model"].__setitem__("rof", "broken"))
    add("theorem_wellposedness", lambda d: d["theorem_contract"].__setitem__("wellposedness", "heuristic"))
    add("theorem_velocity", lambda d: d["theorem_contract"].__setitem__("block_velocity", "signs reversed"))
    add("theorem_no_split", lambda d: d["theorem_contract"].__setitem__("coalescence", "blocks may split"))
    add("theorem_consensus", lambda d: d["theorem_contract"].__setitem__("consensus", "asymptotic only"))
    add("theorem_rof", lambda d: d["theorem_contract"].__setitem__("rof_equivalence", "all finite graphs"))
    add("theorem_dissipation", lambda d: d["theorem_contract"].__setitem__("dissipation", "wrong sign"))
    add("theorem_boundary", lambda d: d["theorem_contract"].__setitem__("boundary", "cycles included"))
    add("proof_classification", lambda d: d["proof_contract"].__setitem__("classification", "PROVABLE on all graphs"))
    add("proof_flux", lambda d: d["proof_contract"].__setitem__("minimal_flux", "constant zero flux"))
    add("proof_no_split", lambda d: d["proof_contract"].__setitem__("no_splitting", "omitted"))
    add("proof_kkt", lambda d: d["proof_contract"].__setitem__("rof_kkt", "postulated"))
    add("proof_extinction", lambda d: d["proof_contract"].__setitem__("finite_extinction", "no Poincare bound"))
    add("tuple", lambda d: d["route_a"]["tuple"].__setitem__(0, "A0_ANALYTIC_ARITHMETIC_ORIGIN"))
    add("overall", lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_SUCCESS_ROUTE_B_READY"))
    add("route_b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("forbidden_flag", lambda d: d["scope_flags"].__setitem__("euler_factors", True))
    add("scope_key_removed", lambda d: d["scope_flags"].pop("root_numbers"))
    add("scope_key_added", lambda d: d["scope_flags"].__setitem__("undeclared", False))
    add("nonclaim", lambda d: d["nonclaims"].__setitem__(1, "ROF equivalence holds on every graph."))
    add("enumeration_extra", lambda d: d["enumeration"].__setitem__("undeclared", 0))
    add("alphabet", lambda d: d["enumeration"].__setitem__("alphabet", [-1, 0, 1]))
    add("nmax", lambda d: d["enumeration"].__setitem__("n_max", 7))
    add("raw_count", lambda d: d["enumeration"].__setitem__("raw_input_count", 19531))
    add("by_n_schema", lambda d: d["enumeration"]["by_n"][0].__setitem__("undeclared", 0))
    add("by_n_count", lambda d: d["enumeration"]["by_n"][-1].__setitem__("input_count", 0))
    add("histogram", lambda d: d["enumeration"]["by_n"][-1]["event_count_histogram"].__setitem__("0", 0))
    add("trace_digest", lambda d: d["enumeration"].__setitem__("trace_sha256", "0" * 64))
    add("stress_dimensions", lambda d: d["enumeration"]["stress_dimensions"].__setitem__(0, 7))
    add("stress_events", lambda d: d["enumeration"].__setitem__("stress_event_times", 0))
    add("violation", lambda d: d["enumeration"]["violations"].__setitem__("rof_kkt", 1))
    add("witness_name", lambda d: d["witnesses"][0].__setitem__("name", "not_singleton"))
    add("witness_input", lambda d: d["witnesses"][6]["input"].__setitem__(0, "99"))
    add("witness_trace_schema", lambda d: d["witnesses"][6]["trace"].__setitem__("undeclared", 0))
    add("witness_initial_partition", lambda d: d["witnesses"][6]["trace"]["initial_partition"].__setitem__(0, [1, 2]))
    add("witness_event_time", lambda d: d["witnesses"][6]["trace"]["events"][0].__setitem__("time", "999"))
    add("witness_event_state", lambda d: d["witnesses"][6]["trace"]["events"][0]["state"].__setitem__(0, "999"))
    add("witness_event_partition", lambda d: d["witnesses"][6]["trace"]["events"][0]["partition"].__setitem__(0, [1, 6]))
    add("witness_event_merges", lambda d: d["witnesses"][6]["trace"]["events"][0].__setitem__("pair_merges", 9))
    add("witness_event_energy", lambda d: d["witnesses"][6]["trace"]["events"][0].__setitem__("energy", "999"))
    add("witness_consensus", lambda d: d["witnesses"][6]["trace"].__setitem__("consensus_value", "999"))
    add("reference_identifier", lambda d: d["references"][2].__setitem__("identifier", "10.fake/doi"))
    add("reference_venue", lambda d: d["references"][2].__setitem__("venue", "SIAM Journal on Imaging Sciences 12(4) (2019), 1643-1667"))
    add("reference_title", lambda d: d["references"][3].__setitem__("title", "Broken title"))
    add("reference_schema", lambda d: d["references"][0].__setitem__("undeclared", "broken"))

    for name, candidate in mutations:
        assert not accepted(candidate), name

    stale = copy.deepcopy(base)
    stale["candidate_id"] = "HCS-C278"
    assert not accepted(stale)
    print(
        f"C279 mutation suite: PASS {len(mutations)}/{len(mutations)} "
        "repaired-hash attacks; stale-hash control PASS"
    )


if __name__ == "__main__":
    main()
