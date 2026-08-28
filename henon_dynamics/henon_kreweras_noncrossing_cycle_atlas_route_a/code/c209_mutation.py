#!/usr/bin/env python3
"""Hostile repaired-hash and stale-hash tests for the C209 checker."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c209_kreweras_evidence.json"
CHECKER = ROOT / "code/c209_kreweras_checker.py"


def rehash(data: dict) -> None:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()


def rejected(data: dict) -> bool:
    with tempfile.TemporaryDirectory(prefix="c209-mutation-") as directory:
        path = Path(directory) / "mutated.json"
        path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        result = subprocess.run(
            [sys.executable, str(CHECKER), str(path)],
            capture_output=True,
            text=True,
            env={**__import__("os").environ, "C209_MUTATION_FAST": "1"},
        )
        return result.returncode != 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    def add(name: str, change) -> None:
        item = deepcopy(base)
        change(item)
        rehash(item)
        mutations.append((name, item))

    add("schema", lambda d: d.__setitem__("schema", "HCS-C000-v1"))
    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C000"))
    add("commit", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("scope", lambda d: d.__setitem__("scope_literal", "BROKEN"))
    add("evaluator_hash", lambda d: d["evaluator"].__setitem__("sha256", "0" * 64))
    add("source_clock", lambda d: d["source_lock"].__setitem__("clock", "post-hoc clock"))
    add("source_forbidden", lambda d: d["source_lock"].__setitem__("forbidden_data", "target primes"))
    add("attribution", lambda d: d["attribution"].__setitem__("status", "NEW_THEOREM"))
    add("theorem_fixed", lambda d: d["theorem"].__setitem__("fixed_count", "all zero"))
    add("route_a0", lambda d: d["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("route_a4", lambda d: d["route_a"]["tuple"].__setitem__(4, "A4_HILBERT_POLYA"))
    add("route_overall", lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_SUCCESS"))
    add("scope_prime", lambda d: d["scope_flags"].__setitem__("used_target_prime_table", True))
    add("scope_route_b", lambda d: d["scope_flags"].__setitem__("route_b_invocation_allowed", True))
    add("n_row_count", lambda d: d["finite_replay"].__setitem__("n_row_count", 99))
    add("fixed_row_count", lambda d: d["finite_replay"].__setitem__("fixed_row_count", 99))
    add("n_catalan", lambda d: d["finite_replay"]["n_rows"][5].__setitem__("catalan", 999))
    add("n_order", lambda d: d["finite_replay"]["n_rows"][5].__setitem__("clock_order", 999))
    add("fixed_coordinate", lambda d: d["finite_replay"]["fixed_rows"][10].__setitem__("iterate", 999))
    add("fixed_value", lambda d: d["finite_replay"]["fixed_rows"][10].__setitem__("fixed_count", 999))
    add("period_population", lambda d: d["finite_replay"]["period_rows"][10].__setitem__("exact_period_population", 999))
    add("period_cycle", lambda d: d["finite_replay"]["period_rows"][10].__setitem__("cycle_count", 999))
    add("spectral_value", lambda d: d["finite_replay"]["spectral_rows"][10].__setitem__("multiplicity", 999))
    add("rank_value", lambda d: d["finite_replay"]["rank_rows"][10].__setitem__("count", 999))
    add("q_coefficient", lambda d: d["finite_replay"]["q_catalan_rows"][5]["coefficients"].__setitem__(0, 999))
    add("q_hash", lambda d: d["finite_replay"]["q_catalan_rows"][5].__setitem__("sha256", "0" * 64))
    add("ledger_cycle", lambda d: d["finite_replay"]["n_rows"][5]["cycle_ledger"][0].__setitem__("cycles", 999))
    add("zeta_factor", lambda d: d["finite_replay"]["n_rows"][5]["zeta_factors"][0].__setitem__("exponent", 999))
    add("det_factor", lambda d: d["finite_replay"]["n_rows"][5]["koopman_determinant_factors"][0].__setitem__("exponent", 999))
    add("rank_row_coordinate", lambda d: d["finite_replay"]["rank_rows"][10].__setitem__("blocks", 99))
    add("q_degree", lambda d: d["finite_replay"]["q_catalan_rows"][5].__setitem__("degree", 999))
    add("structural_reflection", lambda d: d["finite_replay"]["structural_rows"][5].__setitem__("reflection_count", 999))

    for name, item in mutations:
        if not rejected(item):
            raise AssertionError(f"checker accepted repaired-hash mutation: {name}")

    stale = deepcopy(base)
    stale["finite_replay"]["fixed_rows"][0]["fixed_count"] = 999
    if not rejected(stale):
        raise AssertionError("checker accepted stale-hash mutation")

    print(json.dumps({
        "status": "C209_MUTATION_PASS",
        "repaired_hash_rejections": len(mutations),
        "stale_hash_rejections": 1,
        "total_rejections": len(mutations) + 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
