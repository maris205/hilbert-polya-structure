#!/usr/bin/env python3
"""Repaired-hash semantic mutation battery for HCS-C283."""
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
ORIGINAL = json.loads((ROOT / "results/c283_padic_evidence.json").read_text())


def payload_hash(data: dict) -> str:
    copy_data = dict(data)
    copy_data.pop("payload_sha256", None)
    raw = json.dumps(copy_data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def rejected(data: dict, repair: bool = True) -> bool:
    if repair:
        data["payload_sha256"] = payload_hash(data)
    with tempfile.TemporaryDirectory(prefix="c283-mut-") as directory:
        path = Path(directory) / "mutant.json"
        path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        env = dict(os.environ)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        env["C283_EVIDENCE_PATH"] = str(path)
        result = subprocess.run([sys.executable, "-B", str(ROOT / "code/c283_padic_checker.py")],
                                env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return result.returncode != 0


def main() -> None:
    attacks: list[tuple[dict, bool]] = []
    d = copy.deepcopy(ORIGINAL); d["source_commit"] = "0" * 40; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["scope_flags"]["euler_factors"] = True; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["route_a"]["tuple"][0] = "A0_ANALYTIC_ARITHMETIC_ORIGIN"; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["route_a"]["route_b_invocation_allowed"] = True; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["owner"]["normalization"] = "the Vladimirov operator"; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["theorem_contract"]["schatten"] = "all resolvents are trace class"; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["theorem_contract"]["boundaries"] = "alpha=0 remains compact"; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["regression"]["shell_cells"][0]["multiplicity"] += 1; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["regression"]["finite_quotient_cells"][0]["dft_hierarchical_max_error"] = "1"; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["regression"]["heat_trace_cells"][0]["heat_trace"] = "0"; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["regression"]["zeta_cells"][0]["closed_value"] = "9"; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["regression"]["pole_cells"][0]["residue"] = "0"; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["regression"]["counting_cells"][0]["N_at_eigenvalue"] = 0; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["regression"]["schatten_cells"][0]["in_S_q"] = True; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["regression"]["boundaries"][0]["convergence_from_alpha_positive"] = "operator_norm"; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["unknown_top_level"] = 1; attacks.append((d, True))
    d = copy.deepcopy(ORIGINAL); d["candidate_id"] = "HCS-C000"; attacks.append((d, False))
    passed = sum(rejected(data, repair) for data, repair in attacks)
    assert passed == len(attacks)
    print(f"C283 hostile mutation: PASS {passed}/{len(attacks)}")


if __name__ == "__main__":
    main()
