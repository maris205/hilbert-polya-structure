#!/usr/bin/env python3
"""Adversarial repaired-hash and stale-hash mutations for HCS-C169."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c169_skew_shift_evidence.json"
CHECKER = ROOT / "code/c169_skew_shift_checker.py"


def rehash(data: dict) -> None:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()


def rejected(data: dict) -> bool:
    with tempfile.TemporaryDirectory(prefix="c169-mutation-") as tmp:
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
    add("family", lambda d: d["source_lock"].__setitem__("family", "rational alpha"))
    add("iterate", lambda d: d["finite_replay"]["iterate_rows"][7].__setitem__("y_coefficient_alpha", 999))
    add("fixed", lambda d: d["finite_replay"]["iterate_rows"][0].__setitem__("fixed_points", 1))
    add("fourier_phase", lambda d: d["finite_replay"]["fourier_rows"][100].__setitem__("phase_alpha_coefficient", 99))
    add("fourier_index", lambda d: d["finite_replay"]["fourier_rows"][200].__setitem__("output_m", 99))
    add("sector", lambda d: d["finite_replay"]["sector_rows"][3].__setitem__("bilateral_shift_copies", 99))
    add("reversor", lambda d: d["reversibility_and_operator_boundary"].__setitem__("reversor", "false"))
    add("fredholm", lambda d: d["reversibility_and_operator_boundary"].__setitem__("fredholm_boundary", "defined"))
    add("A0", lambda d: d["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("A1", lambda d: d["route_a"]["tuple"].__setitem__(1, "A1_WEAK"))
    add("A4", lambda d: d["route_a"].__setitem__("A4_qualification", "POST_HOC"))
    add("route_b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("target_flag", lambda d: d["scope_flags"].__setitem__("used_target_prime_table", True))

    repaired_rejections = 0
    for name, item in mutations:
        if not rejected(item):
            raise AssertionError(f"checker accepted repaired-hash mutation {name}")
        repaired_rejections += 1

    stale = deepcopy(base)
    stale["finite_replay"]["iterate_rows"][1]["x_coefficient_alpha"] = 123
    if not rejected(stale):
        raise AssertionError("checker accepted stale-hash mutation")
    print(json.dumps({
        "status": "C169_MUTATION_PASS", "repaired_hash_rejections": repaired_rejections,
        "stale_hash_rejections": 1, "total_rejections": repaired_rejections + 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
