#!/usr/bin/env python3
"""Repaired-hash, unknown-key, and stale-hash attacks for HCS-C202."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c202_fisher_kpp_evidence.json"
CHECKER = ROOT / "code/c202_fisher_kpp_checker.py"


def rehash(data: dict) -> None:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()


def rejected(data: dict) -> bool:
    with tempfile.TemporaryDirectory(prefix="c202-mutation-") as temporary:
        path = Path(temporary) / "mutated.json"
        path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        result = subprocess.run([sys.executable, str(CHECKER), str(path)], capture_output=True, text=True)
        return result.returncode != 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    def add(name, attack) -> None:
        item = deepcopy(base)
        attack(item)
        rehash(item)
        mutations.append((name, item))

    for name, key, replacement in [
        ("schema", "schema", "broken"), ("candidate", "candidate_id", "HCS-C000"),
        ("date", "evaluation_date", "2026-08-26"), ("commit", "source_commit", "0" * 40),
        ("scope", "scope_literal", "BROKEN_SCOPE"),
    ]:
        add(name, lambda d, key=key, replacement=replacement: d.__setitem__(key, replacement))
    for name, key, replacement in [
        ("evaluator_path", "path", "wrong.md"), ("evaluator_version", "version", "9.9.9"),
        ("evaluator_sha", "sha256", "0" * 64),
    ]:
        add(name, lambda d, key=key, replacement=replacement: d["evaluator"].__setitem__(key, replacement))

    # Explicit recursive schema-injection attacks.
    add("unknown_top", lambda d: d.__setitem__("claimed_target_divisor", True))
    add("unknown_finite", lambda d: d["finite_regression"].__setitem__("all_speeds_proved_by_grid", True))
    add("unknown_speed", lambda d: d["finite_regression"]["speed_rows"][0].__setitem__("prime_owner", True))
    add("unknown_phase", lambda d: d["finite_regression"]["phase_rows"][0].__setitem__("zero_fit", True))
    add("unknown_trapping", lambda d: d["finite_regression"]["trapping_rows"][0].__setitem__("shooting_proof", True))
    add("unknown_oval", lambda d: d["finite_regression"]["hamiltonian_oval_rows"][0].__setitem__("target_cycle", True))
    add("unknown_az", lambda d: d["finite_regression"]["az_rows"][0].__setitem__("general_speed_formula", True))
    add("unknown_physical", lambda d: d["finite_regression"]["physical_scalings"][0].__setitem__("arithmetic_place", True))

    for section in ("source_lock", "attribution", "theorem", "proof_boundary"):
        for key in base[section]:
            replacement = True if isinstance(base[section][key], bool) else "BROKEN"
            add(f"{section}_{key}", lambda d, section=section, key=key, replacement=replacement: d[section].__setitem__(key, replacement))

    for index in range(5):
        add(f"route_tuple_{index}", lambda d, index=index: d["route_a"]["tuple"].__setitem__(index, "A4_ROUTE_B_READY"))
    for key in ("overall", "A0_qualification", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"):
        replacement = True if key == "route_b_invocation_allowed" else "BROKEN"
        add(f"route_{key}", lambda d, key=key, replacement=replacement: d["route_a"].__setitem__(key, replacement))
    for key in base["scope_flags"]:
        add(f"scope_{key}", lambda d, key=key: d["scope_flags"].__setitem__(key, True))

    add("source_fisher_doi", lambda d: d["source_registry"][0].__setitem__("doi", "10.fake/fisher"))
    add("source_kpp_translation", lambda d: d["source_registry"][1].__setitem__("translation_locator", "missing"))
    add("source_az_doi", lambda d: d["source_registry"][2].__setitem__("doi", "10.fake/az"))
    for index in range(len(base["nonclaims"])):
        add(f"nonclaim_{index}", lambda d, index=index: d["nonclaims"].__setitem__(index, "BROKEN"))
    for key in base["summary"]:
        add(f"summary_{key}", lambda d, key=key: d["summary"].__setitem__(key, 999))

    add("speed_value", lambda d: d["finite_regression"]["speed_rows"][0].__setitem__("dimensionless_speed", "99"))
    add("speed_class", lambda d: d["finite_regression"]["speed_rows"][8].__setitem__("zero_equilibrium_type", "target_spectrum"))
    add("phase_vector", lambda d: d["finite_regression"]["phase_rows"][0].__setitem__("V_prime", "99"))
    add("phase_energy", lambda d: d["finite_regression"]["phase_rows"][0].__setitem__("energy_derivative", "99"))
    add("trapping_inward", lambda d: d["finite_regression"]["trapping_rows"][0].__setitem__("boundary_G_prime", "-1"))
    add("trapping_slope", lambda d: d["finite_regression"]["trapping_rows"][0].__setitem__("slow_slope_q", "99"))
    add("oval_root", lambda d: d["finite_regression"]["hamiltonian_oval_rows"][0].__setitem__("negative_turning_point", "99"))
    add("oval_energy", lambda d: d["finite_regression"]["hamiltonian_oval_rows"][0].__setitem__("energy", "1"))
    add("az_residual", lambda d: d["finite_regression"]["az_rows"][0].__setitem__("ode_residual", "1"))
    add("az_speed_term", lambda d: d["finite_regression"]["az_rows"][0].__setitem__("speed_times_U_xi", "1"))
    add("physical_threshold", lambda d: d["finite_regression"]["physical_scalings"][0].__setitem__("minimal_speed_2sqrt_Dr", "99"))
    add("physical_az", lambda d: d["finite_regression"]["physical_scalings"][0].__setitem__("az_speed_5sqrt_Dr_over_sqrt6", "99"))

    repaired = 0
    for name, item in mutations:
        if not rejected(item):
            raise AssertionError(f"checker accepted repaired-hash mutation {name}")
        repaired += 1

    stale = deepcopy(base)
    stale["finite_regression"]["az_rows"][0]["ode_residual"] = "1"
    if not rejected(stale):
        raise AssertionError("checker accepted stale-hash mutation")

    print(json.dumps({
        "status": "C202_MUTATION_PASS",
        "repaired_hash_rejections": repaired,
        "unknown_key_rejections": 8,
        "stale_hash_rejections": 1,
        "total_rejections": repaired + 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
