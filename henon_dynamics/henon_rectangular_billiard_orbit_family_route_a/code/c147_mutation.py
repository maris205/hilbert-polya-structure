#!/usr/bin/env python3
"""Repaired-hash and stale-hash hostile tests for HCS-C147."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c147_billiard_evidence.json"
CHECKER = ROOT / "code/c147_billiard_checker.py"


def payload_hash(data):
    work = dict(data)
    work.pop("payload_sha256", None)
    return sha256(json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def set_path(data, path, value):
    target = data
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value


def main():
    source = json.loads(EVIDENCE.read_text())
    mutations = [
        ("schema", ("schema",), "forged"),
        ("candidate", ("candidate_id",), "HCS-X"),
        ("scope", ("scope_literal",), "BAD_SCOPE"),
        ("orientation", ("source_lock", "primitive_direction"), "unfrozen"),
        ("axis", ("source_lock", "axis_boundary_classes"), "included"),
        ("clock", ("source_lock", "clock"), "time rescaled"),
        ("cutoff", ("source_lock", "cutoff", "m_max"), 39),
        ("precision", ("source_lock", "precision"), "float"),
        ("row_m", ("primitive_direction_ledger", 0, "m"), 2),
        ("row_gcd", ("primitive_direction_ledger", 10, "gcd"), 2),
        ("row_disp", ("primitive_direction_ledger", 30, "unfolded_displacement", 0), 0),
        ("row_length", ("primitive_direction_ledger", 50, "length_squared"), 1),
        ("row_phase", ("primitive_direction_ledger", 70, "dirichlet_reflection_phase"), -1),
        ("row_family", ("primitive_direction_ledger", 90, "family_dimension"), 0),
        ("count", ("count_certificate", "positive_primitive_direction_count"), 0),
        ("mobius", ("count_certificate", "mobius_formula_value"), 0),
        ("axes", ("count_certificate", "axis_boundary_class_count"), 4),
        ("oriented", ("count_certificate", "full_signed_oriented_sector_count"), 0),
        ("time_reversal", ("count_certificate", "full_signed_time_reversal_quotient_sector_count"), 0),
        ("degeneracy", ("length_square_degeneracy_groups", 0, "m2_plus_n2"), 0),
        ("minimal", ("minimal_nontrivial_collision", "m2_plus_n2"), 5),
        ("witness", ("minimal_nontrivial_collision", "witness", 0, 1), 7),
        ("multiplier", ("family_theorem", "family_tangent_multiplier"), 2),
        ("denominator", ("family_theorem", "ordinary_isolated_denominator"), "1"),
        ("phase", ("family_theorem", "dirichlet_reflection_phase"), "-1"),
        ("aspect", ("aspect_ratio_control", "height_squared"), "2"),
        ("aspect_collision", ("aspect_ratio_control", "distinct_positive_direction_collisions"), 1),
        ("quantization", ("natural_quantization", "status"), "POST_HOC"),
        ("time_reversal_quantum", ("natural_quantization", "antiunitary_time_reversal"), "NONE"),
        ("target", ("natural_quantization", "target_matching"), True),
        ("a1", ("route_a", "tuple", 0), "A1_PASS_ANALYTIC"),
        ("a4", ("route_a", "tuple", 3), "A4_ROUTE_B_READY"),
        ("routeb", ("route_a", "route_b_invocation_allowed"), True),
        ("flag", ("claim_boundary", "isolated_periodic_orbits"), True),
        ("extra", ("route_a", "forged"), True),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c147-mutations-") as temporary:
        for name, path, value in mutations:
            candidate = deepcopy(source)
            set_path(candidate, path, value)
            candidate["payload_sha256"] = payload_hash(candidate)
            output = Path(temporary) / f"{name}.json"
            output.write_text(json.dumps(candidate, sort_keys=True, indent=2) + "\n")
            result = subprocess.run([sys.executable, str(CHECKER), str(output)], capture_output=True, text=True)
            if result.returncode == 0:
                raise AssertionError(f"checker accepted repaired mutation {name}")
            rejected.append(name)
        stale = deepcopy(source)
        stale["payload_sha256"] = "0" * 64
        output = Path(temporary) / "stale.json"
        output.write_text(json.dumps(stale, sort_keys=True, indent=2) + "\n")
        result = subprocess.run([sys.executable, str(CHECKER), str(output)], capture_output=True, text=True)
        if result.returncode == 0:
            raise AssertionError("checker accepted stale payload hash")
    print(json.dumps({"status": "C147_MUTATION_PASS", "repaired_hash_rejected": len(rejected), "stale_hash_rejected": 1, "total": len(rejected) + 1, "names": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
