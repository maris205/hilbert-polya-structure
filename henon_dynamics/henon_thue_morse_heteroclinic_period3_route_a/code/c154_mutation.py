#!/usr/bin/env python3
"""Repaired-hash semantic mutation audit for C154."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c154_heteroclinic_evidence.json"
CHECKER = ROOT / "code/c154_heteroclinic_checker.py"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def set_path(container, path, value) -> None:
    current = container
    for item in path[:-1]:
        current = current[item]
    current[path[-1]] = value


def main() -> None:
    source = json.loads(EVIDENCE.read_text())
    repaired = [
        ("schema", ("schema",), "HCS-C154-v0"), ("candidate", ("candidate_id",), "HCS-C000"),
        ("date", ("date_utc",), "2026-08-24"), ("commit", ("source_commit",), "0" * 40),
        ("scope", ("scope_literal",), "BROKEN"), ("object", ("source_lock", "object"), "forged"),
        ("map", ("source_lock", "map"), "right shift"), ("clock", ("source_lock", "clock"), "two shifts"),
        ("cutoff", ("source_lock", "cutoff"), "theorem cutoff 60"),
        ("alphabet", ("frozen_configuration", "alphabet"), [0, 1, 2, 3]),
        ("background", ("frozen_configuration", "periodic_background"), "period two"),
        ("interface", ("frozen_configuration", "interface_rule"), "reversed"),
        ("pair", ("frozen_configuration", "interface_pair"), [2, 0]),
        ("injective", ("frozen_configuration", "orbit_is_injective"), False),
        ("isolated", ("frozen_configuration", "interface_cylinder_isolates_each_orbit_point"), False),
        ("cert_limit", ("frozen_configuration", "tm_period_certificate_limit"), 31),
        ("cert_d", ("frozen_configuration", "tm_period_certificates", 7, "multiple_d"), 1),
        ("decomposition", ("orbit_closure_theorem", "exact_decomposition"), "X=X_TM"),
        ("positive", ("orbit_closure_theorem", "positive_escape"), "no limits"),
        ("negative", ("orbit_closure_theorem", "negative_escape"), "four phases"),
        ("other", ("orbit_closure_theorem", "no_other_limits"), "unknown"),
        ("dense", ("orbit_closure_theorem", "dense_full_orbit"), "not dense"),
        ("forward_tt", ("orbit_closure_theorem", "forward_transitivity_failure"), "standard forward transitive"),
        ("minimal", ("orbit_closure_theorem", "not_minimal"), "minimal"),
        ("wandering", ("orbit_closure_theorem", "wandering_interface"), "recurrent"),
        ("omega", ("orbit_closure_theorem", "nonwandering_set"), "Omega=X"),
        ("tm_periodic", ("periodic_orbit_theorem", "tm_periodic_points"), 1),
        ("interface_periodic", ("periodic_orbit_theorem", "interface_orbit_periodic_points"), 1),
        ("periodic_class", ("periodic_orbit_theorem", "periodic_points_exactly"), "none"),
        ("fixed_formula", ("periodic_orbit_theorem", "fixed_count"), "Fix=0"),
        ("exact_formula", ("periodic_orbit_theorem", "exact_period_points"), "P=0"),
        ("primitive", ("periodic_orbit_theorem", "primitive_cycles", 0, "primitive_cycles"), 2),
        ("zeta", ("periodic_orbit_theorem", "artin_mazur_zeta"), "1"),
        ("interface_row", ("finite_replay", "interface_rows", 36, "interface_pair"), [4, 1]),
        ("positive_row", ("finite_replay", "positive_shift_windows", 2, "central_word", 0), 4),
        ("negative_row", ("finite_replay", "negative_shift_windows", 3, "period_three_check"), False),
        ("period_limit", ("finite_replay", "period_limit"), 59),
        ("fixed", ("finite_replay", "fixed_rows", 2, "fixed_points"), 0),
        ("exact", ("finite_replay", "fixed_rows", 2, "exact_period_points"), 0),
        ("zeta_coeff", ("finite_replay", "zeta_coefficients", 12), 0),
        ("progress", ("progress_and_boundary", "progress"), "none"),
        ("A1", ("route_a", "tuple", 0), "A1_PASS"), ("overall", ("route_a", "overall"), "ROUTE_A_PASSED"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("prime", ("scope_flags", "uses_prime_table"), True), ("root", ("scope_flags", "claims_root_number"), True),
        ("nonclaim", ("nonclaims", 0), "X is minimal"),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c154-mutations-") as temporary:
        for name, path, value in repaired:
            candidate_data = deepcopy(source)
            set_path(candidate_data, path, value)
            candidate_data["payload_sha256"] = payload_hash(candidate_data)
            candidate = Path(temporary) / f"{name}.json"
            candidate.write_text(json.dumps(candidate_data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            result = subprocess.run([sys.executable, str(CHECKER), str(candidate)], capture_output=True, text=True)
            if result.returncode == 0:
                raise AssertionError(f"checker accepted repaired mutation {name}")
            rejected.append(name)
        stale = deepcopy(source)
        stale["payload_sha256"] = "0" * 64
        candidate = Path(temporary) / "stale.json"
        candidate.write_text(json.dumps(stale, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        result = subprocess.run([sys.executable, str(CHECKER), str(candidate)], capture_output=True, text=True)
        if result.returncode == 0:
            raise AssertionError("checker accepted stale hash")
    print(json.dumps({"status": "C154_MUTATION_PASS", "repaired_hash_rejected": len(repaired), "stale_hash_rejected": 1, "total": len(repaired) + 1, "names": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
