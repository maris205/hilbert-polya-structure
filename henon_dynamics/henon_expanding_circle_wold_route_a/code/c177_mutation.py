#!/usr/bin/env python3
"""Adversarial repaired-hash and stale-hash mutations for HCS-C177."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c177_expanding_circle_evidence.json"
CHECKER = ROOT / "code/c177_expanding_circle_checker.py"


def rehash(data: dict) -> None:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()


def rejected(data: dict) -> bool:
    with tempfile.TemporaryDirectory(prefix="c177-mutation-") as tmp:
        path = Path(tmp) / "mutated.json"
        path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        result = subprocess.run([sys.executable, str(CHECKER), str(path)], capture_output=True, text=True)
        return result.returncode != 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    mutations = []

    def add(name: str, mutate) -> None:
        item = deepcopy(base)
        mutate(item)
        rehash(item)
        mutations.append((name, item))

    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C000"))
    add("source_commit", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("scope", lambda d: d.__setitem__("scope_literal", "BROKEN"))
    add("evaluator", lambda d: d["evaluator"].__setitem__("version", "9.9"))
    add("family", lambda d: d["source_lock"].__setitem__("family", "b=1"))
    add("fixed", lambda d: d["finite_replay"]["periodic_rows"][0].__setitem__("fixed_points", 2))
    add("exact", lambda d: d["finite_replay"]["periodic_rows"][25].__setitem__("exact_period_points", 7))
    add("cycles", lambda d: d["finite_replay"]["periodic_rows"][80].__setitem__("primitive_cycles", 0))
    add("wold_output", lambda d: d["finite_replay"]["wold_rows"][100].__setitem__("output_mode", 999))
    add("wold_root", lambda d: d["finite_replay"]["wold_rows"][500].__setitem__("chain_root", 0))
    add("adjoint", lambda d: d["finite_replay"]["wold_rows"][900].__setitem__("adjoint_output", 3))
    add("correlation", lambda d: d["finite_replay"]["correlation_rows"][100].__setitem__("normalized_correlation_denominator", 1))
    add("basis", lambda d: d["operator_theorem"].__setitem__("basis_action", "false"))
    add("zeta", lambda d: d["periodic_theorem"].__setitem__("artin_mazur_zeta", "1"))
    add("A0", lambda d: d["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("A4", lambda d: d["route_a"]["tuple"].__setitem__(4, "A4_NATURAL_QUANTIZATION"))
    add("route_b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("target_flag", lambda d: d["scope_flags"].__setitem__("used_target_prime_table", True))

    repaired = 0
    for name, item in mutations:
        if not rejected(item):
            raise AssertionError(f"checker accepted repaired-hash mutation {name}")
        repaired += 1

    stale = deepcopy(base)
    stale["finite_replay"]["periodic_rows"][1]["fixed_points"] = 123
    if not rejected(stale):
        raise AssertionError("checker accepted stale-hash mutation")
    print(json.dumps({
        "status": "C177_MUTATION_PASS",
        "repaired_hash_rejections": repaired,
        "stale_hash_rejections": 1,
        "total_rejections": repaired + 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
