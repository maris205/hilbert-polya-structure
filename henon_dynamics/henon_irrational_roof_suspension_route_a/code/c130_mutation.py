#!/usr/bin/env python3
"""Hostile repaired-hash and stale-hash mutation suite for C130."""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results" / "c130_suspension_evidence.json"
CHECKER = ROOT / "code" / "c130_suspension_checker.py"


def set_path(data: dict, path: tuple[object, ...], value: object) -> None:
    node: object = data
    for key in path[:-1]:
        node = node[key]  # type: ignore[index]
    node[path[-1]] = value  # type: ignore[index]


def repair_hash(data: dict) -> None:
    data.pop("payload_sha256", None)
    payload = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = hashlib.sha256(payload).hexdigest()


def main() -> None:
    source = json.loads(EVIDENCE.read_text())
    mutations = [
        ("schema", ("schema",), "HCS-C999-v1", True),
        ("candidate", ("candidate_id",), "HCS-C999", True),
        ("date", ("date_utc",), "2026-08-23", True),
        ("scope", ("scope_literal",), "ALLOW_FORBIDDEN", True),
        ("base", ("source_lock", "base"), "one-state shift", True),
        ("roof_lock", ("source_lock", "roof"), "tau=(1,2)", True),
        ("clock_lock", ("source_lock", "clock"), "base return count only", True),
        ("normalization", ("source_lock", "normalization"), "weighted", True),
        ("determinant_convention_lock", ("source_lock", "determinant_convention"), "zeta_tau(s)", True),
        ("B", ("frozen_model", "adjacency_B", 1, 1), 0, True),
        ("roof_value", ("frozen_model", "roof_values", 1), "2", True),
        ("matrix", ("frozen_model", "bivariate_transfer_matrix", 0, 1), "u", True),
        ("determinant", ("frozen_model", "bivariate_determinant"), "1-u-v-uv", True),
        ("specialization", ("frozen_model", "exponential_polynomial"), "1-exp(-s)", True),
        ("all_period", ("all_period_identity", "all_period"), False, True),
        ("trace_formula_bivariate", ("all_period_identity", "trace_formula_bivariate"), "Tr(M^n)=u^n+v^n", True),
        ("trace_formula_specialized", ("all_period_identity", "trace_formula_specialized"), "cutoff-only trace", True),
        ("Euler_identity", ("all_period_identity", "primitive_euler_identity"), "forged", True),
        ("convergence", ("all_period_identity", "convergence_domain"), "global absolute", True),
        ("period_row", ("replay_prefix", "rows", 7, "period"), 9, True),
        ("rooted_count", ("replay_prefix", "rows", 9, "rooted_closed_words"), 1023, True),
        ("primitive_count", ("replay_prefix", "rows", 5, "primitive_cycles"), 8, True),
        ("sector_multiplicity", ("replay_prefix", "rows", 5, "trace_sectors", 3, "multiplicity"), 19, True),
        ("representative", ("replay_prefix", "primitive_representatives", "6", 4), "010101", True),
        ("primitive_total", ("replay_prefix", "primitive_cycles_total"), 225, True),
        ("same_sector", ("clock_sector_separation", "same_sector_primitive_example_period_6", 1), "001101", True),
        ("sector_injectivity", ("clock_sector_separation", "sector_injectivity"), "all primitive orbits are injective", True),
        ("nonperiodicity", ("clock_sector_separation", "imaginary_period_statement"), "periodic", True),
        ("control_roof", ("rational_roof_control", "roof_values", 1), "3", True),
        ("collision_time", ("rational_roof_control", "cross_sector_collision", "common_roof_time"), 3, True),
        ("control_period", ("rational_roof_control", "periodicity"), "none", True),
        ("tuple", ("route_a", "tuple"), ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], True),
        ("route_overall", ("route_a", "overall"), "ROUTE_A_ANALYTIC_CANDIDATE", True),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True, True),
        ("progress_headline", ("progress_and_boundary", "progress"), "target match proved", True),
        ("scope_flag", ("scope_flags", "claims_root_number"), True, True),
        ("orbit_nonclaim", ("nonclaims", 3), "orbit injectivity", True),
        ("top_level_extra_key", ("unexpected_top_level_key",), True, True),
        ("source_extra_key", ("source_lock", "unexpected"), True, True),
        ("all_period_extra_key", ("all_period_identity", "unexpected"), True, True),
        ("clock_sector_extra_key", ("clock_sector_separation", "unexpected"), True, True),
        ("progress_extra_key", ("progress_and_boundary", "unexpected"), True, True),
        ("route_extra_key", ("route_a", "unexpected"), True, True),
        ("stale_hash", ("payload_sha256",), "0" * 64, False),
    ]

    repaired_rejected: list[str] = []
    stale_rejected: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c130-mutations-") as tmp:
        for name, path, value, repair in mutations:
            data = deepcopy(source)
            set_path(data, path, value)
            if repair:
                repair_hash(data)
            candidate = Path(tmp) / f"{name}.json"
            candidate.write_text(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
            completed = subprocess.run([sys.executable, str(CHECKER), str(candidate)], capture_output=True, text=True)
            if completed.returncode == 0:
                raise AssertionError(f"checker accepted hostile mutation {name}")
            if repair:
                repaired_rejected.append(name)
            else:
                stale_rejected.append(name)
    assert len(repaired_rejected) + len(stale_rejected) == len(mutations)
    print(json.dumps({
        "status": "C130_REPAIRED_AND_STALE_HASH_MUTATION_PASS",
        "repaired_hash_mutations_rejected": len(repaired_rejected),
        "stale_hash_mutations_rejected": len(stale_rejected),
        "total_mutations_rejected": len(mutations),
        "repaired_names": repaired_rejected,
        "stale_names": stale_rejected,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
