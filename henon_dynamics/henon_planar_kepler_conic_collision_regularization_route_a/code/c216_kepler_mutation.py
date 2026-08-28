#!/usr/bin/env python3
"""Hostile repaired-hash, stale-hash, and unknown-key tests for C216."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c216_kepler_evidence.json"
CHECKER = ROOT / "code/c216_kepler_checker.py"


def rehash(data: dict) -> None:
    body = deepcopy(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()


def rejected(data: dict) -> bool:
    with tempfile.TemporaryDirectory(prefix="c216-mutation-") as directory:
        path = Path(directory) / "mutated.json"
        path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        env = {**__import__("os").environ, "C216_MUTATION_FAST": "1"}
        run = subprocess.run([sys.executable, str(CHECKER), str(path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=env)
        return run.returncode != 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    def add(name: str, change) -> None:
        item = deepcopy(base)
        change(item)
        rehash(item)
        mutations.append((name, item))

    add("schema", lambda d: d.__setitem__("schema", "hcs-c000"))
    add("source_commit", lambda d: d["metadata"].__setitem__("source_commit", "0" * 40))
    add("evaluator_hash", lambda d: d["metadata"]["evaluator"].__setitem__("sha256", "0" * 64))
    add("scope", lambda d: d["metadata"].__setitem__("scope_literal", "BROKEN"))
    add("mu", lambda d: d["orbit_rows"][0].__setitem__("mu", "2/1"))
    add("q", lambda d: d["orbit_rows"][1]["q"].__setitem__(0, "5/1"))
    add("p", lambda d: d["orbit_rows"][2]["p"].__setitem__(1, "7/3"))
    add("energy", lambda d: d["orbit_rows"][3].__setitem__("energy", "0/1"))
    add("angular_momentum", lambda d: d["orbit_rows"][4].__setitem__("angular_momentum", "2/1"))
    add("runge_lenz", lambda d: d["orbit_rows"][5]["runge_lenz"].__setitem__(0, "9/1"))
    add("eccentricity", lambda d: d["orbit_rows"][6].__setitem__("eccentricity_square", "1/1"))
    add("identity_residual", lambda d: d["orbit_rows"][7].__setitem__("energy_identity_residual", "1/1"))
    add("conic_type", lambda d: d["orbit_rows"][8].__setitem__("conic_type", "ellipse"))
    add("period", lambda d: d["orbit_rows"][0].__setitem__("negative_energy_period", "0"))
    add("radial_action", lambda d: d["orbit_rows"][1].__setitem__("radial_action_formula", "0"))
    add("scattering", lambda d: d["orbit_rows"][6].__setitem__("hyperbolic_scattering_angle", "0"))
    add("collision_time", lambda d: d["radial_collision_rows"][0].__setitem__("collision_time", "0"))
    add("lc_constraint", lambda d: d["levi_civita_rows"][0].__setitem__("constraint_residual", "1/1"))
    add("lc_velocity", lambda d: d["levi_civita_rows"][1]["u_prime"].__setitem__(0, "9/1"))
    add("fixed_dimension", lambda d: d["fixed_set_rows"][0].__setitem__("fixed_set_dimension", 0))
    add("route_tuple", lambda d: d["route_a"]["tuple"].__setitem__(0, "A0_STRUCTURAL_ARITHMETIC_RELATION"))
    add("attribution", lambda d: d["attribution"].__setitem__("status", "NEW_THEOREM"))
    add("summary", lambda d: d["summary"].__setitem__("orbit_row_count", 9))
    add("unknown_root_key", lambda d: d.__setitem__("unexpected", True))

    failed = [name for name, item in mutations if not rejected(item)]
    stale = deepcopy(base)
    stale["orbit_rows"][0]["conic_type"] = "hyperbola"
    stale_rejected = rejected(stale)
    if failed or not stale_rejected:
        raise AssertionError({"unrejected_repaired_hash": failed, "stale_hash_rejected": stale_rejected})
    print(json.dumps({
        "status": "C216_MUTATION_PASS",
        "repaired_hash_rejections": len(mutations),
        "stale_hash_rejections": 1,
        "unknown_key_mutation_included": True,
        "total_rejections": len(mutations) + 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
