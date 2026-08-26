#!/usr/bin/env python3
"""Hostile repaired-hash and stale-hash mutations for C186."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c186_euler_top_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c186_euler_top_checker.py"


def canonical_hash(data: dict) -> str:
    body = deepcopy(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def rejected(data: dict) -> bool:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(data, f, sort_keys=True, indent=2)
        f.write("\n")
        path = Path(f.name)
    try:
        run = subprocess.run([sys.executable, str(CHECKER), str(path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return run.returncode != 0
    finally:
        path.unlink(missing_ok=True)


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = []

    def add(name, change):
        d = deepcopy(original); change(d); d["payload_sha256"] = canonical_hash(d); mutations.append((name, d))

    add("scope", lambda d: d["metadata"].__setitem__("scope_literal", "BROKEN"))
    add("source", lambda d: d["metadata"]["primary_sources"][0].__setitem__("doi", "broken"))
    add("row_id", lambda d: d["regular_rows"][0].__setitem__("row_id", "collision"))
    add("energy", lambda d: d["regular_rows"][1].__setitem__("normalized_energy_e_equals_2E_over_G2", "0/1"))
    add("amplitude", lambda d: d["regular_rows"][2]["amplitude_squares"].__setitem__("A2", "1/1"))
    add("modulus", lambda d: d["regular_rows"][3].__setitem__("modulus_square", "1/1"))
    add("frequency", lambda d: d["regular_rows"][4].__setitem__("frequency_square", "0/1"))
    add("period", lambda d: d["regular_rows"][5].__setitem__("minimal_period", "0.0"))
    add("action", lambda d: d["regular_rows"][6].__setitem__("normalized_kks_cap_action", "0.0"))
    add("residual", lambda d: d["regular_rows"][7]["exact_residuals"].__setitem__(0, "1/1"))
    add("component", lambda d: d["regular_rows"][8].__setitem__("component_count", 1))
    add("linearization", lambda d: d["equilibrium_rows"][0].__setitem__("tangent_rate_square", "1/1"))
    add("stability", lambda d: d["equilibrium_rows"][1].__setitem__("classification", "elliptic_stable"))
    add("separatrix", lambda d: d["separatrix_rows"][0].__setitem__("heteroclinic_branches", 2))
    add("divergence", lambda d: d["period_divergence_rows"][0].__setitem__("periods", list(reversed(d["period_divergence_rows"][0]["periods"]))))
    add("fixed_set", lambda d: d["fixed_time_map"].__setitem__("fixed_component_dimension", 0))
    add("poisson_convention", lambda d: d["theorem"].__setitem__("poisson_convention", "BROKEN"))
    add("canonical_chart", lambda d: d["theorem"].__setitem__("canonical_action_charts", "BROKEN"))
    add("route", lambda d: d["route_a"].__setitem__("A0", "A0_STRUCTURAL_ARITHMETIC_RELATION"))
    add("summary", lambda d: d["summary"].__setitem__("regular_rows", 179))

    failed = [name for name, data in mutations if not rejected(data)]
    stale = deepcopy(original); stale["regular_rows"][0]["component_count"] = 7
    stale_rejected = rejected(stale)
    if failed or not stale_rejected:
        raise AssertionError({"unrejected_repaired_hash": failed, "stale_hash_rejected": stale_rejected})
    print(json.dumps({"status": "C186_MUTATION_PASS", "repaired_hash_rejections": len(mutations), "stale_hash_rejections": 1}, sort_keys=True))


if __name__ == "__main__":
    main()
