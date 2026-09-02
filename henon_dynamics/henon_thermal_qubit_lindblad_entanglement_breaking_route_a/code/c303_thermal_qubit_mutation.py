#!/usr/bin/env python3
"""Hostile semantic/type/path mutations that the independent checker must reject."""
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
EVIDENCE = ROOT / "results/c303_thermal_qubit_evidence.json"
CHECKER = ROOT / "code/c303_thermal_qubit_checker.py"


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    mutations = []

    def add(name, fn, repair=True):
        value = copy.deepcopy(base)
        fn(value)
        if repair:
            value["payload_sha256"] = payload_hash(value)
        mutations.append((name, json.dumps(value, sort_keys=True, indent=2) + "\n"))

    add("candidate", lambda x: x.__setitem__("candidate_id", "HCS-C302"))
    add("obstruction", lambda x: x.__setitem__("obstruction_id", "HEN-O286"))
    add("source", lambda x: x.__setitem__("source_commit", "0" * 40))
    add("epoch_bool", lambda x: x.__setitem__("fixed_epoch", True))
    add("scope", lambda x: x.__setitem__("scope_literal", "EXPANDED"))
    add("evaluator", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("eval_file", lambda x: x.__setitem__("evaluation_file_sha256", "0" * 64))
    add("dephasing_factor", lambda x: x["model"].__setitem__("dephasing_convention", "isolated rate is 2 gamma_phi"))
    add("generator_factor", lambda x: x["model"].__setitem__("generator", x["model"]["generator"].replace("gamma_phi/2", "gamma_phi")))
    add("Gamma2", lambda x: x["model"].__setitem__("Gamma2", "Gamma1/2+2gamma_phi"))
    add("coherence_sign", lambda x: x["theorem_contract"].__setitem__("coherence", "rho_01(t)=exp((-Gamma2-i*omega)*t)rho_01(0)"))
    add("ppt_direction", lambda x: x["theorem_contract"].__setitem__("choi_ppt", "p(1-p)(1-eta)^2<=eta^q"))
    add("route_tuple", lambda x: x["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_root_number", True))
    add("nonclaim", lambda x: x["nonclaims"].pop())
    add("collision", lambda x: x["collision_boundary"].__setitem__("C298", "same"))
    add("reference", lambda x: x["references"][0].__setitem__("identifier", "fake"))
    add("reference_unknown", lambda x: x["references"][0].__setitem__("url", "https://example.invalid"))
    add("choi_a", lambda x: x["choi_exact_rows"][7].__setitem__("a", "1/9"))
    add("choi_bool_int", lambda x: x["choi_exact_rows"][3].__setitem__("choi_positive", 1))
    add("choi_unknown", lambda x: x["choi_exact_rows"][0].__setitem__("extra", 0))
    add("liouvillian_coeff", lambda x: x["liouvillian_rows"][4]["characteristic_coefficients_descending"].__setitem__(2, "9/1"))
    add("stationary_dimension_bool", lambda x: x["liouvillian_rows"][0].__setitem__("stationary_dimension", True))
    add("trace_winner", lambda x: x["trace_contraction_rows"][0].__setitem__("winning_axis", "longitudinal"))
    add("trace_strict_int", lambda x: x["trace_contraction_rows"][0].__setitem__("strict_for_positive_t", 1))
    add("semigroup", lambda x: x["semigroup_rows"][0].__setitem__("eta_composed", "1/5"))
    add("threshold_bracket", lambda x: x["threshold_rows"][0].__setitem__("eta_lower", "9.0e-1"))
    add("threshold_q_bool", lambda x: x["threshold_rows"][0].__setitem__("q", True))
    add("endpoint_eb", lambda x: x["boundary_rows"][1].__setitem__("finite_EB", True))
    add("summary", lambda x: x["summary"].__setitem__("audited_rows", 123))
    add("top_unknown", lambda x: x.__setitem__("unknown", "attack"))
    add("stale_payload", lambda x: x["choi_exact_rows"][0].__setitem__("q", 2), repair=False)

    raw_duplicate = EVIDENCE.read_text().replace('"candidate_id": "HCS-C303",', '"candidate_id": "HCS-C303",\n  "candidate_id": "HCS-C303",', 1)
    raw_nan = EVIDENCE.read_text().replace('"fixed_epoch": 1788307200', '"fixed_epoch": NaN', 1)
    mutations.extend([("duplicate_key", raw_duplicate), ("nonfinite", raw_nan)])

    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c303-mutations-") as td:
        for number, (name, raw) in enumerate(mutations):
            path = Path(td) / f"{number:02d}-{name}.json"
            path.write_text(raw)
            proc = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(path)], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            assert proc.returncode != 0, name
            rejected += 1
    print(f"C303 hostile mutation suite: PASS {rejected}/{len(mutations)}")


if __name__ == "__main__":
    main()
