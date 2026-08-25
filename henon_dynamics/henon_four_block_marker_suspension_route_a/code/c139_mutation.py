#!/usr/bin/env python3
"""Repaired-hash and stale-hash mutation audit for C139."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c139_marker_evidence.json"
CHECKER = ROOT / "code/c139_marker_checker.py"


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
        ("schema", ("schema",), "HCS-C139-v0"),
        ("date", ("date_utc",), "2026-08-24"),
        ("scope", ("scope_literal",), "BROKEN_SCOPE"),
        ("roof", ("source_lock", "base_edge_roof", 0, 1), "sqrt(5)"),
        ("marker", ("source_lock", "marker"), "0110"),
        ("eta", ("source_lock", "eta"), "sqrt(7)"),
        ("normalization", ("source_lock", "normalization"), "reverse count"),
        ("det_convention", ("source_lock", "determinant_convention"), "det(I+M)"),
        ("cutoff", ("source_lock", "cutoff"), "theorem ends at 12"),
        ("states", ("frozen_model", "states", 0), "111"),
        ("transition", ("frozen_model", "transition_rule"), "forged transition"),
        ("determinant", ("frozen_model", "formal_determinant"), "Delta=1-x00"),
        ("det_receipt", ("frozen_model", "formal_determinant_receipt", "1,1,1,1,1"), 1),
        ("specialization", ("frozen_model", "edge_roof_specialization"), "forged specialization"),
        ("clock", ("frozen_model", "clock_formula"), "forged clock"),
        ("basis", ("frozen_model", "basis_independence"), "dependent"),
        ("reduction", ("frozen_model", "y_equals_one_reduction"), "not C135"),
        ("trace", ("all_period_identity", "trace_formula"), "forged trace"),
        ("logdet", ("all_period_identity", "log_determinant"), "forged log"),
        ("product", ("all_period_identity", "primitive_product"), "forged product"),
        ("suspension", ("all_period_identity", "suspension_product"), "forged suspension"),
        ("all_period", ("all_period_identity", "all_period"), False),
        ("row_trace", ("replay_prefix", "rows", 7, "weighted_trace_coefficients", "0,2,2,4,0"), 9),
        ("row_representative", ("replay_prefix", "rows", 5, "primitive_representatives", 0), "000000"),
        ("rooted_total", ("replay_prefix", "rooted_closed_words_total"), 8189),
        ("primitive_total", ("replay_prefix", "primitive_cycles_total"), 746),
        ("rooted_cells", ("replay_prefix", "rooted_feature_cells_total"), 257),
        ("primitive_cells", ("replay_prefix", "primitive_feature_cells_total"), 228),
        ("memory_pair", ("minimal_memory_theorem", "pair", 1), "001011"),
        ("trigram", ("minimal_memory_theorem", "common_3_block_counts", 0), 1),
        ("marker_counts", ("minimal_memory_theorem", "marker_counts", 1), 0),
        ("memory_boundary", ("minimal_memory_theorem", "coding_boundary"), "cohomology invariant"),
        ("minimal_receipt", ("controls", "minimal_pair_receipts", 1, "marker_count_0011"), 0),
        ("residual_pair", ("controls", "residual_collision_pair", 1), "0101111"),
        ("residual_vector", ("controls", "residual_feature_vector", 4), 1),
        ("residual_nonrotation", ("controls", "residual_pair_nonrotation"), False),
        ("first_collision", ("controls", "first_same_feature_primitive_collision_period"), 6),
        ("nonlattice", ("controls", "nonlattice_witness"), "rational cycles"),
        ("progress", ("progress_and_boundary", "progress_over_C135"), "forged progress"),
        ("obstruction", ("progress_and_boundary", "remaining_internal_obstruction"), "injective"),
        ("target", ("progress_and_boundary", "target_obstruction"), "target matched"),
        ("A2", ("route_a", "tuple", 1), "A2_PASS"),
        ("A3", ("route_a", "A3_qualification"), "TARGET_FE"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("prime_flag", ("scope_flags", "uses_prime_table"), True),
        ("root_flag", ("scope_flags", "claims_root_number"), True),
        ("nonclaim", ("nonclaims", 1), "primitive injectivity"),
        ("extra_key", ("controls", "forged"), True),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c139-mutations-") as temporary:
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
    print(json.dumps({"status": "C139_MUTATION_PASS", "repaired_hash_rejected": len(repaired), "stale_hash_rejected": 1, "total": len(repaired) + 1, "names": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
