#!/usr/bin/env python3
"""Repaired-hash and stale-hash mutation audit for C140."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c140_sofic_evidence.json"
CHECKER = ROOT / "code/c140_sofic_checker.py"


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def set_path(container, path, value):
    current = container
    for item in path[:-1]:
        current = current[item]
    current[path[-1]] = value


def main():
    source = json.loads(EVIDENCE.read_text())
    repaired = [
        ("schema", ("schema",), "HCS-C140-v0"),
        ("date", ("date_utc",), "2026-08-24"),
        ("scope", ("scope_literal",), "BROKEN_SCOPE"),
        ("object", ("source_lock", "object"), "even shift"),
        ("presentation", ("source_lock", "presentation"), "forged graph"),
        ("roof", ("source_lock", "roof", "label_0"), "sqrt(3)"),
        ("clock", ("source_lock", "clock"), "forged clock"),
        ("normalization", ("source_lock", "normalization"), "cover multiplicity"),
        ("det_convention", ("source_lock", "determinant_convention"), "D140=Dcov"),
        ("cutoff", ("source_lock", "cutoff"), "theorem ends at 15"),
        ("state", ("frozen_model", "states", 2), 3),
        ("transition", ("frozen_model", "labeled_transitions", 3, 1), 1),
        ("matrix", ("frozen_model", "cover_matrix", 2, 0), "u"),
        ("cover_det", ("frozen_model", "cover_determinant"), "D=1-u-v"),
        ("cover_zeta", ("frozen_model", "cover_zeta"), "1/(1-u-v)"),
        ("intrinsic_zeta", ("frozen_model", "intrinsic_zeta"), "1/(1-u-v^3)"),
        ("inverse", ("frozen_model", "intrinsic_inverse_zeta"), "D_cov"),
        ("specialization", ("frozen_model", "laplace_specialization"), "forged specialization"),
        ("entropy", ("frozen_model", "entropy_characterization"), "h=0"),
        ("not_sft", ("sofic_theorem", "strictly_sofic"), "X3 is SFT"),
        ("followers", ("sofic_theorem", "three_follower_sets"), "same futures"),
        ("minimal_cover", ("sofic_theorem", "minimal_cover"), "two states"),
        ("unique_lift", ("sofic_theorem", "unique_lift_off_exception"), "three lifts"),
        ("exception", ("sofic_theorem", "exceptional_point"), "one cover lift"),
        ("fixed_formula", ("all_period_identity", "weighted_fixed_formula"), "F=TrB"),
        ("correction_log", ("all_period_identity", "correction_log"), "zero"),
        ("log_zeta", ("all_period_identity", "log_zeta"), "forged log"),
        ("product", ("all_period_identity", "primitive_product"), "forged product"),
        ("suspension", ("all_period_identity", "suspension_product"), "forged suspension"),
        ("all_period", ("all_period_identity", "all_period"), False),
        ("row_cover", ("replay_prefix", "rows", 2, "cover_fixed_points"), 3),
        ("row_label", ("replay_prefix", "rows", 2, "label_fixed_points"), 4),
        ("row_correction", ("replay_prefix", "rows", 2, "all_zero_correction_coefficient"), 1),
        ("row_polynomial", ("replay_prefix", "rows", 2, "intrinsic_weighted_fixed_coefficients", "0,3"), 3),
        ("rooted_total", ("replay_prefix", "admissible_rooted_points_total"), 968),
        ("primitive_total", ("replay_prefix", "primitive_label_cycles_total"), 73),
        ("rooted_cells", ("replay_prefix", "rooted_feature_cells_total"), 59),
        ("primitive_cells", ("replay_prefix", "primitive_feature_cells_total"), 31),
        ("cover_sequence", ("controls", "cover_fixed_counts_periods_1_to_15", 14), 307),
        ("label_sequence", ("controls", "label_fixed_counts_periods_1_to_15", 14), 309),
        ("period1_correction", ("controls", "period_1_cover_to_label_correction"), 0),
        ("period3_correction", ("controls", "period_3_cover_to_label_correction"), 1),
        ("zero_label_period", ("controls", "all_zero_label_point_least_period"), 3),
        ("zero_cover_period", ("controls", "all_zero_cover_orbit_least_period"), 1),
        ("nonlattice", ("controls", "nonlattice_witness"), "rational"),
        ("progress", ("progress_and_boundary", "progress_over_full_shift_suspensions"), "forged progress"),
        ("owner", ("progress_and_boundary", "remaining_internal_obstruction"), "Fredholm owner proved"),
        ("A2", ("route_a", "tuple", 1), "A2_PASS"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("arithmetic_flag", ("scope_flags", "claims_arithmetic_euler_factors"), True),
        ("automorphy_flag", ("scope_flags", "claims_automorphy"), True),
        ("nonclaim", ("nonclaims", 0), "cover equals label"),
        ("extra_key", ("sofic_theorem", "forged"), True),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c140-mutations-") as temporary:
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
        stale_path = Path(temporary) / "stale_hash.json"
        stale_path.write_text(json.dumps(stale, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        result = subprocess.run([sys.executable, str(CHECKER), str(stale_path)], capture_output=True, text=True)
        if result.returncode == 0:
            raise AssertionError("checker accepted stale payload hash")
    print(json.dumps({"status": "C140_MUTATION_PASS", "repaired_hash_rejected": len(repaired), "stale_hash_rejected": 1, "total": len(repaired) + 1, "names": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
