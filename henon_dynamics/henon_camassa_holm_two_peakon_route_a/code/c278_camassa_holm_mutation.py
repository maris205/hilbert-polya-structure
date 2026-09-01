#!/usr/bin/env python3
"""Repaired-hash semantic mutation suite for HCS-C278."""
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
EVIDENCE = ROOT / "results/c278_camassa_holm_evidence.json"
CHECKER = ROOT / "code/c278_camassa_holm_checker.py"


def ph(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def accepted(data: dict) -> bool:
    with tempfile.TemporaryDirectory(prefix="c278-mut-") as directory:
        path = Path(directory) / "evidence.json"
        path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        environment = dict(os.environ)
        environment["PYTHONDONTWRITEBYTECODE"] = "1"
        environment["C278_EVIDENCE_PATH"] = str(path)
        completed = subprocess.run(
            [sys.executable, "-B", str(CHECKER)], env=environment,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
        return completed.returncode == 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    assert accepted(base)
    mutations = []

    def add(name: str, edit) -> None:
        candidate = copy.deepcopy(base)
        edit(candidate)
        candidate["payload_sha256"] = ph(candidate)
        mutations.append((name, candidate))

    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C277"))
    add("schema", lambda d: d.__setitem__("schema", "hcs-c278-broken"))
    add("top_extra", lambda d: d.__setitem__("undeclared", True))
    add("source", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("epoch", lambda d: d.__setitem__("fixed_epoch", 0))
    add("scope", lambda d: d.__setitem__("scope_literal", "WIDENED"))
    add("tuple", lambda d: d["route_a"]["tuple"].__setitem__(1, "A1_PASS_ANALYTIC"))
    add("overall", lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_PARTIAL"))
    add("route_b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("forbidden_flag", lambda d: d["scope_flags"].__setitem__("euler_factors", True))
    add("scope_key_removed", lambda d: d["scope_flags"].pop("root_numbers"))
    add("scope_key_added", lambda d: d["scope_flags"].__setitem__("undeclared", False))
    add("counts", lambda d: d["regression"]["counts"].__setitem__("same_sign_rows", 14))
    add("regression_extra_key", lambda d: d["regression"].__setitem__("undeclared", []))
    add("model_distribution_identity", lambda d: d["model"].__setitem__("distribution_identity", "(1-partial_x^2)exp(-|x-q|)=delta_q"))
    add("model_equation", lambda d: d["model"].__setitem__("equation", "broken"))
    add("reduction", lambda d: d["theorem_contract"].__setitem__("reduction", "broken"))
    add("chamber_partition", lambda d: d["theorem_contract"].__setitem__("chamber_partition", "broken"))
    add("profile_contract", lambda d: d["proof_contract"].__setitem__("profile_limit", "broken"))
    add("proof_weak_reduction", lambda d: d["proof_contract"].__setitem__("weak_reduction", "broken"))
    add("proof_global_scope", lambda d: d["proof_contract"].__setitem__("global_scope", "broken"))
    add("nonclaim", lambda d: d["nonclaims"].__setitem__(0, "broadened"))
    add("boundary", lambda d: d["regression"]["boundaries"][0].__setitem__("law", "broken"))
    add("reference", lambda d: d["references"][0].__setitem__("doi", "10.fake/doi"))
    add("reference_venue", lambda d: d["references"][0].__setitem__("venue", "Physical Review Letters 71(11) (1993), 1661-1663"))
    add("same_y", lambda d: d["regression"]["same_sign_rows"][0].__setitem__("y", "2"))
    add("same_p", lambda d: d["regression"]["same_sign_rows"][0].__setitem__("p", "0"))
    add("same_energy", lambda d: d["regression"]["same_sign_rows"][0].__setitem__("energy", "0"))
    add("same_centre", lambda d: d["regression"]["same_sign_rows"][0].__setitem__("centre", "0"))
    add("same_q1", lambda d: d["regression"]["same_sign_rows"][0].__setitem__("q1", "0"))
    add("same_q2", lambda d: d["regression"]["same_sign_rows"][0].__setitem__("q2", "0"))
    add("same_row_schema", lambda d: d["regression"]["same_sign_rows"][0].__setitem__("undeclared", 0))
    add("opposite_p", lambda d: d["regression"]["opposite_sign_rows"][0].__setitem__("p", "1"))
    add("opposite_coefficient", lambda d: d["regression"]["opposite_sign_rows"][0].__setitem__("gap_quadratic_coefficient", "0"))
    add("opposite_scaled_gap", lambda d: d["regression"]["opposite_sign_rows"][0].__setitem__("scaled_gap", "0"))
    add("opposite_scaled_amplitude", lambda d: d["regression"]["opposite_sign_rows"][0].__setitem__("scaled_amplitude_difference", "0"))
    add("opposite_row_schema", lambda d: d["regression"]["opposite_sign_rows"][0].__setitem__("undeclared", 0))
    add("alpha_state", lambda d: d["regression"]["alpha_rows"][-1].__setitem__("postcollision_state", "signed_pair"))
    add("alpha_row_schema", lambda d: d["regression"]["alpha_rows"][0].__setitem__("undeclared", 0))
    add("reference_title", lambda d: d["references"][0].__setitem__("title", "broken"))
    add("reference_schema", lambda d: d["references"][0].__setitem__("undeclared", "broken"))
    for name, candidate in mutations:
        assert not accepted(candidate), name
    stale = copy.deepcopy(base)
    stale["candidate_id"] = "HCS-C277"
    assert not accepted(stale)
    print(f"C278 mutation suite: PASS {len(mutations)}/{len(mutations)} repaired-hash attacks; stale-hash control PASS")


if __name__ == "__main__":
    main()
