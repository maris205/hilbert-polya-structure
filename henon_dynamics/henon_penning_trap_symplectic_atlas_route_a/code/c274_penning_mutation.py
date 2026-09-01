#!/usr/bin/env python3
"""Repaired-payload-hash hostile mutations for HCS-C274."""
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
SRC = json.loads((ROOT / "results/c274_penning_evidence.json").read_text())


def phash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    mutants = []

    def add(name, mutate) -> None:
        data = copy.deepcopy(SRC)
        mutate(data)
        data["payload_sha256"] = phash(data)
        mutants.append((name, data))

    add("schema", lambda d: d.update(schema="wrong"))
    add("candidate", lambda d: d.update(candidate_id="HCS-C000"))
    add("source", lambda d: d.update(source_commit="0"*40))
    add("epoch", lambda d: d.update(fixed_epoch=0))
    add("scope", lambda d: d.update(scope_literal="BAD_SCOPE"))
    add("evaluator", lambda d: d["evaluator"].update(sha256="0"*64))
    add("route_overall", lambda d: d["route_a"].update(overall="ROUTE_A_PASS"))
    add("route_b", lambda d: d["route_a"].update(route_b_invocation_allowed=True))
    add("route_tuple", lambda d: d["route_a"]["tuple"].__setitem__(1, "A1_PASS_ANALYTIC"))
    add("scope_flag", lambda d: d["scope_flags"].update(root_numbers=True))
    add("state_order", lambda d: d["model_contract"].update(state_order="wrong"))
    add("delta", lambda d: d["model_contract"].update(delta="Delta=c^2+2*zeta^2"))
    add("flow_dimension", lambda d: d["flow_contract"].update(dimension=4))
    add("normal_form_sign", lambda d: d["mode_contract"].update(normal_form="H=omega_+ I_++omega_- I_-+zeta I_z"))
    add("sign_reversal", lambda d: d["regime_contract"].update(sign_reversal="wrong"))
    add("proof_status", lambda d: d["proof_contract"].update(status="UNPROVED"))
    add("primary_doi", lambda d: d["sources"][0].update(doi="10.fake/doi"))
    add("flow_matrix_cell", lambda d: d["regression"]["flow_rows"][17]["matrix"].__setitem__(22, "99"))
    add("flow_det", lambda d: d["regression"]["flow_rows"][31].update(determinant="2"))
    add("mode_energy", lambda d: d["regression"]["mode_rows"][13].update(normal_form_energy="99"))
    add("mode_krein", lambda d: d["regression"]["mode_rows"][8].update(krein_signs=[1, 1, 1]))
    add("strobe_dimension", lambda d: d["regression"]["strobe_rows"][4].update(fixed_dimension=6))
    add("period_gate", lambda d: d["regression"]["period_rows"][6].update(commensurate=True))
    add("boundary_dimension", lambda d: d["regression"]["boundary_rows"][3].update(bounded_dimension=6))
    add("numeric_schema", lambda d: d["regression"]["numeric_field_schema"]["flow_rows"].remove("matrix"))
    add("counts", lambda d: d["regression"]["counts"].update(numeric_cells=1))

    rejected = 0
    for name, mutant in mutants:
        with tempfile.TemporaryDirectory(prefix="c274_mutant_") as tmp:
            path = Path(tmp) / "mutant.json"
            path.write_text(json.dumps(mutant, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            env = dict(os.environ)
            env["C274_EVIDENCE_IN"] = str(path)
            env["PYTHONDONTWRITEBYTECODE"] = "1"
            run = subprocess.run(
                [sys.executable, "-B", str(ROOT / "code/c274_penning_checker.py")],
                env=env, capture_output=True, text=True,
            )
            if run.returncode:
                rejected += 1
            else:
                raise AssertionError(f"mutation survived: {name}")
    print(f"C274 hostile repaired-hash mutations: PASS {rejected}/{len(mutants)}")


if __name__ == "__main__":
    main()
