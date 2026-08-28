#!/usr/bin/env python3
"""Hostile repaired-hash and stale-hash mutations for C221."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c221_nls_evidence.json"
CHECKER = ROOT / "code/c221_nls_checker.py"


def digest_payload(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def set_path(data: dict, path: tuple, value) -> None:
    obj = data
    for key in path[:-1]:
        obj = obj[key]
    obj[path[-1]] = value


def rejected(data: dict, repair_hash: bool) -> bool:
    if repair_hash:
        data["payload_sha256"] = digest_payload(data)
    with tempfile.TemporaryDirectory(prefix="c221-mut-") as td:
        path = Path(td) / "mutated.json"
        path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        proc = subprocess.run([sys.executable, "-B", str(CHECKER), "--evidence", str(path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return proc.returncode != 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    mutations = [
        ("candidate_id", ("candidate_id",), "HCS-C999"),
        ("source_commit", ("source_commit",), "deadbeef"),
        ("scope_literal", ("scope_literal",), "BAD_SCOPE"),
        ("equation", ("frozen_object", "equation"), "i psi_t + psi_xx - 2|psi|^2psi=0"),
        ("profile_value", ("regression", "profile_rows", 0, "Q"), "0"),
        ("profile_residual", ("regression", "profile_rows", 0, "standing_wave_residual"), "1"),
        ("mass", ("regression", "integral_rows", 0, "mass"), "0"),
        ("vk", ("regression", "integral_rows", 0, "vk_slope"), "0"),
        ("eigenvalue", ("regression", "spectrum_rows", 0, "Lplus_phi2_eigenvalue"), "0"),
        ("threshold", ("regression", "spectrum_rows", 0, "essential_threshold"), "99"),
        ("factorization", ("regression", "factorization_rows", 0, "P2_minus_A2starA2_plus3"), "1"),
        ("citation_claim", ("citations", 2, "claim"), "unbounded priority claim"),
        ("route_tuple", ("route_a", "tuple"), ["A0_FAIL"]),
        ("scope_flag", ("scope_flags", "uses_prime_table"), True),
        ("summary_count", ("summary", "profile_row_count"), 0),
    ]
    rejected_count = 0
    for _, path, value in mutations:
        trial = deepcopy(base)
        # Resolve integer list indices as well as mapping keys.
        obj = trial
        for key in path[:-1]:
            obj = obj[key]
        obj[path[-1]] = value
        if rejected(trial, True):
            rejected_count += 1
        else:
            raise AssertionError(f"accepted repaired-hash mutation: {path}")

    unknown = deepcopy(base)
    unknown["unexpected_root_key"] = 1
    if rejected(unknown, True):
        rejected_count += 1
    else:
        raise AssertionError("accepted unknown-key mutation")

    stale = deepcopy(base)
    stale["regression"]["profile_rows"][0]["Q"] = "0"
    if rejected(stale, False):
        rejected_count += 1
    else:
        raise AssertionError("accepted stale-hash mutation")

    total = len(mutations) + 2
    print(json.dumps({"status": "C221_MUTATION_PASS", "repaired_hash_rejections": len(mutations) + 1, "stale_hash_rejections": 1, "total_rejections": rejected_count, "mutation_total": total}, sort_keys=True))


if __name__ == "__main__":
    main()
