#!/usr/bin/env python3
"""Repaired-hash and stale-hash hostile tests for HCS-C146."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c146_heisenberg_evidence.json"
CHECKER = ROOT / "code/c146_heisenberg_checker.py"


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
        ("matrix", ("source_lock", "matrix_A", 0, 0), 3),
        ("group", ("source_lock", "group_law"), "abelian"),
        ("cutoff", ("source_lock", "cutoff", "iterate_ledger"), 19),
        ("precision", ("source_lock", "precision"), "float"),
        ("power", ("iterate_ledger", 4, "A_power", 0, 0), 999),
        ("trace", ("iterate_ledger", 7, "trace"), 0),
        ("lucas", ("iterate_ledger", 9, "lucas_L_2n"), 1),
        ("det", ("iterate_ledger", 11, "det_A_power_minus_I"), 1),
        ("torus", ("iterate_ledger", 13, "toral_isolated_fixed_points"), 0),
        ("circle", ("iterate_ledger", 15, "certified_nilmanifold_fixed_circle_lower_bound"), 2),
        ("multiplier", ("iterate_ledger", 17, "central_multiplier"), 2),
        ("denominator", ("iterate_ledger", 19, "ordinary_isolated_denominator"), "1"),
        ("lefschetz", ("iterate_ledger", 2, "lefschetz_number"), 1),
        ("fixed", ("clean_fixed_circle_theorem", "fixed_by_every_positive_iterate"), False),
        ("nondiscrete", ("clean_fixed_circle_theorem", "fixed_set_is_never_discrete"), False),
        ("factor", ("clean_fixed_circle_theorem", "isolated_stability_denominator_all_iterates"), "nonzero"),
        ("witness", ("rejected_naive_component_lift", "horizontal_class", 0), "2/5"),
        ("shift", ("rejected_naive_component_lift", "A2v_minus_v", 0), "1"),
        ("condition", ("rejected_naive_component_lift", "left_quotient_vertical_fixed_condition_value"), "0"),
        ("overclaim", ("rejected_naive_component_lift", "full_nilmanifold_component_count_through_20"), 1),
        ("koopman", ("formal_lift_hint", "unitary"), False),
        ("bridge", ("formal_lift_hint", "isolated_orbit_weight_bridge_constructed"), True),
        ("a1", ("route_a", "tuple", 0), "A1_WEAK"),
        ("a4", ("route_a", "tuple", 3), "A4_NATURAL_QUANTIZATION"),
        ("routeb", ("route_a", "route_b_invocation_allowed"), True),
        ("flag", ("claim_boundary", "full_fixed_component_count_claimed"), True),
        ("extra", ("route_a", "forged"), True),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c146-mutations-") as temporary:
        for name, path, value in mutations:
            candidate = deepcopy(source)
            set_path(candidate, path, value)
            candidate["payload_sha256"] = payload_hash(candidate)
            path_out = Path(temporary) / f"{name}.json"
            path_out.write_text(json.dumps(candidate, sort_keys=True, indent=2) + "\n")
            result = subprocess.run([sys.executable, str(CHECKER), str(path_out)], capture_output=True, text=True)
            if result.returncode == 0:
                raise AssertionError(f"checker accepted repaired mutation {name}")
            rejected.append(name)
        stale = deepcopy(source)
        stale["payload_sha256"] = "0" * 64
        stale_path = Path(temporary) / "stale.json"
        stale_path.write_text(json.dumps(stale, sort_keys=True, indent=2) + "\n")
        result = subprocess.run([sys.executable, str(CHECKER), str(stale_path)], capture_output=True, text=True)
        if result.returncode == 0:
            raise AssertionError("checker accepted stale hash")
    print(json.dumps({"status": "C146_MUTATION_PASS", "repaired_hash_rejected": len(rejected), "stale_hash_rejected": 1, "total": len(rejected) + 1, "names": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
