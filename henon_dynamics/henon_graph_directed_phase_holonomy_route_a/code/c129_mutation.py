#!/usr/bin/env python3
"""Repaired-hash hostile mutation suite for the independent C129 checker."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c129_phase_evidence.json"
CHECKER = ROOT / "code/c129_phase_checker.py"


def claims_hash(claims: dict) -> str:
    raw = json.dumps(claims, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def main() -> None:
    source = json.loads(EVIDENCE.read_text())

    def set_path(data: dict, path: tuple[object, ...], value: object) -> None:
        target: object = data
        for key in path[:-1]:
            target = target[key]  # type: ignore[index]
        target[path[-1]] = value  # type: ignore[index]

    mutations = [
        ("schema", ("schema",), "hcs-c129-forged"),
        ("scope", ("scope_literal",), "ALLOW_FORBIDDEN_DATA"),
        ("candidate", ("claims", "source_lock", "candidate_id"), "HCS-X"),
        ("determinant_convention", ("claims", "source_lock", "determinant_convention"), "det(I+zL)"),
        ("A_entry", ("claims", "frozen_model", "A", 0, 0), "1/4"),
        ("graph_edge", ("claims", "frozen_model", "B", 0, 2), "1"),
        ("weight", ("claims", "frozen_model", "weights", 1), "1/4"),
        ("translation", ("claims", "frozen_model", "translations", 0), "-3"),
        ("holonomy", ("claims", "frozen_model", "holonomy_exponents_mod5", 0), 2),
        ("operator_headline", ("claims", "frozen_model", "operator"), "FORGED_OPERATOR"),
        ("frozen_model_extra_key", ("claims", "frozen_model", "forged_operator"), "FORGED_OPERATOR"),
        ("separation", ("claims", "geometry", "pairwise_gap"), "0"),
        ("rooted_count", ("claims", "periodic_orbits", "rooted_counts_n1_to_8", "8"), 133),
        ("primitive_rep", ("claims", "periodic_orbits", "primitive_representatives_n1_to_8", "3", 1), "011"),
        ("histogram", ("claims", "periodic_orbits", "primitive_holonomy_histogram_original_n1_to_8", "8", 0), 99),
        ("cycle_point", ("claims", "periodic_orbits", "example_phase_points", 0, 0), "0"),
        ("trace_class", ("claims", "trace_and_fredholm", "trace_class"), False),
        ("trace_formula_headline", ("claims", "trace_and_fredholm", "all_order_trace_formula"), "FORGED_TRACE"),
        ("trace_fredholm_extra_key", ("claims", "trace_and_fredholm", "forged_trace"), "FORGED_TRACE"),
        ("delta", ("claims", "trace_and_fredholm", "symbolic_delta_original_z0_to_z3", 1, "group_ring_Z5_e0_to_e4", 3), "-1/3"),
        ("trace", ("claims", "trace_and_fredholm", "power_traces_original_n1_to_8", "1", "group_ring_Z5_e0_to_e4", 3), "1"),
        ("fredholm", ("claims", "trace_and_fredholm", "fredholm_coefficients_original_z0_to_z8", 1, "primitive_zeta5_basis_1_zeta_zeta2_zeta3", 3), "0"),
        ("control_phase", ("claims", "controls", "control_holonomy_exponents_mod5", 1), 2),
        ("control_point", ("claims", "controls", "control_example_phase_points", 0, 0), "0"),
        ("untwisted_control", ("claims", "controls", "same_untwisted_all_order_trace_and_determinant"), False),
        ("trivial_character_control", ("claims", "controls", "trivial_character_degenerates_to_C124"), False),
        ("positive_control_headline", ("claims", "controls", "positive_control"), "FORGED_CONTROL"),
        ("controls_extra_key", ("claims", "controls", "forged_control"), "FORGED_CONTROL"),
        ("progress_over_C124", ("claims", "progress_over_prior_gate", "over_C124"), "FORGED_PROGRESS"),
        ("progress_remaining_obstruction", ("claims", "progress_over_prior_gate", "remaining_obstruction"), "FORGED_OBSTRUCTION"),
        ("progress_extra_key", ("claims", "progress_over_prior_gate", "forged_progress"), "FORGED_PROGRESS"),
        ("claims_extra_key", ("claims", "forged_headline"), "FORGED_HEADLINE"),
        ("A4_promotion", ("claims", "verdict", "A4"), "A4_PASS"),
        ("route_b", ("claims", "verdict", "route_b_invocation_allowed"), True),
        ("nonclaim", ("claims", "nonclaims", 0), "complete recovery"),
    ]

    rejected = []
    with tempfile.TemporaryDirectory(prefix="c129-mutations-") as tmp:
        for name, path, value in mutations:
            data = deepcopy(source)
            set_path(data, path, value)
            # Repair the content hash so rejection cannot be attributed to a
            # stale checksum. Top-level mutations need no claim-hash change.
            data["claims_sha256"] = claims_hash(data["claims"])
            candidate = Path(tmp) / f"{name}.json"
            candidate.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            completed = subprocess.run(
                [sys.executable, str(CHECKER), str(candidate)],
                capture_output=True,
                text=True,
            )
            if completed.returncode == 0:
                raise AssertionError(f"checker accepted repaired-hash mutation: {name}")
            rejected.append(name)

    print(json.dumps({
        "status": "C129_REPAIRED_HASH_MUTATION_PASS",
        "rejected": len(rejected),
        "total": len(mutations),
        "names": rejected,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
