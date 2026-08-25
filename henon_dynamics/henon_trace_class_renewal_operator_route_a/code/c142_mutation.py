#!/usr/bin/env python3
"""Hostile semantic mutations for the independent C142 checker."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c142_renewal_evidence.json"
CHECKER = ROOT / "code/c142_renewal_checker.py"


def repair_hash(data: dict) -> None:
    work = dict(data)
    work.pop("payload_sha256", None)
    raw = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()


def set_path(data: dict, path: tuple, value) -> None:
    node = data
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value


def rejected(data: dict) -> bool:
    with tempfile.TemporaryDirectory(prefix="c142-mutation-") as tmp:
        path = Path(tmp) / "mutant.json"
        path.write_text(json.dumps(data, sort_keys=True, indent=2) + "\n")
        proc = subprocess.run([sys.executable, str(CHECKER), str(path)], capture_output=True, text=True)
        return proc.returncode != 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    cases = [
        (("schema",), "bad"),
        (("candidate_id",), "HCS-C000"),
        (("scope_literal",), "BAD_SCOPE"),
        (("source_lock", "precision"), "floating"),
        (("source_lock", "normalization"), "fitted"),
        (("source_lock", "determinant_convention"), "1/D"),
        (("source_lock", "cutoff", "trace"), 11),
        (("coefficient_ledger", 0, "c_m"), "1/3"),
        (("coefficient_ledger", 5, "triangular_exponent"), 20),
        (("trace_ledger", 3, "trace_Tn"), "0"),
        (("primitive_ledger", 5, "count"), 999),
        (("primitive_ledger", 7, "weight_sum"), "0"),
        (("operator_theorem", "shift_trace_norm"), "2"),
        (("operator_theorem", "return_trace_norm"), "1"),
        (("operator_theorem", "fredholm_determinant_formula"), "formal only"),
        (("operator_theorem", "entire_order"), "1"),
        (("negative_control", "formal_scalar_determinant"), "1"),
        (("negative_control", "verdict"), "TRACE_CLASS"),
        (("route_a", "tuple"), ["A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FAIL"]),
        (("route_a", "overall"), "ROUTE_A_SUCCESS_ROUTE_B_READY"),
        (("route_a", "route_b_invocation_allowed"), True),
        (("claim_boundary", "target_divisor_matching"), True),
        (("claim_boundary", "euler_factors"), True),
        (("claim_boundary", "hilbert_polya_operator"), True),
    ]
    repaired = 0
    for path, value in cases:
        mutant = deepcopy(base)
        set_path(mutant, path, value)
        repair_hash(mutant)
        if not rejected(mutant):
            raise SystemExit(f"semantic mutant survived: {path}")
        repaired += 1
    stale = deepcopy(base)
    stale["operator_theorem"]["entire_order"] = "2"
    if not rejected(stale):
        raise SystemExit("stale-hash mutant survived")
    print(json.dumps({"status": "PASS", "repaired_hash_rejections": repaired, "stale_hash_rejections": 1, "total": repaired + 1}, sort_keys=True))


if __name__ == "__main__":
    main()
