#!/usr/bin/env python3
"""Semantic repaired-hash and stale-hash attacks for HCS-C196."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c196_calogero_moser_evidence.json"
CHECKER = ROOT / "code/c196_calogero_moser_checker.py"


def rehash(data: dict) -> None:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()


def rejected(data: dict) -> bool:
    with tempfile.TemporaryDirectory(prefix="c196-mutation-") as temporary:
        path = Path(temporary) / "mutated.json"
        path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        result = subprocess.run(
            [sys.executable, str(CHECKER), str(path)],
            capture_output=True,
            text=True,
        )
        return result.returncode != 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    def add(name, attack) -> None:
        item = deepcopy(base)
        attack(item)
        rehash(item)
        mutations.append((name, item))

    for name, key, value in [
        ("schema", "schema", "hcs-c000-v1"),
        ("candidate", "candidate_id", "HCS-C000"),
        ("date", "date_utc", "2026-08-26"),
        ("commit", "source_commit", "0" * 40),
        ("scope", "scope_literal", "BROKEN_SCOPE"),
    ]:
        add(name, lambda d, key=key, value=value: d.__setitem__(key, value))
    add("schema_extra_top_level", lambda d: d.__setitem__("claimed_target_divisor", True))
    add("schema_extra_finite", lambda d: d["finite_regression"].__setitem__("all_N_proved_by_grid", True))
    add("schema_extra_case_row", lambda d: d["finite_regression"]["rows"][0].__setitem__("target_fit", True))
    add("schema_extra_pencil_row", lambda d: d["finite_regression"]["rows"][0]["pencil_rows"][0].__setitem__("zero_match", True))
    add("schema_extra_scattering", lambda d: d["finite_regression"]["rows"][0]["scattering"].__setitem__("prime_owner", True))
    for name, key, value in [
        ("evaluator_path", "path", "wrong.md"),
        ("evaluator_version", "version", "9.9.9"),
        ("evaluator_sha", "sha256", "0" * 64),
    ]:
        add(name, lambda d, key=key, value=value: d["evaluator"].__setitem__(key, value))

    for key in base["source_lock"]:
        add(f"source_lock_{key}", lambda d, key=key: d["source_lock"].__setitem__(key, "BROKEN"))
    for key in base["attribution"]:
        add(f"attribution_{key}", lambda d, key=key: d["attribution"].__setitem__(key, "BROKEN"))
    for key in base["theorem"]:
        add(f"theorem_{key}", lambda d, key=key: d["theorem"].__setitem__(key, "BROKEN"))
    for key in base["progress_and_boundary"]:
        add(f"boundary_{key}", lambda d, key=key: d["progress_and_boundary"].__setitem__(key, "BROKEN"))

    for index in range(5):
        add(f"route_tuple_{index}", lambda d, index=index: d["route_a"]["tuple"].__setitem__(index, "A0_PASS"))
    for key in [
        "overall", "A0_qualification", "A1_qualification", "A2_qualification",
        "A3_qualification", "A4_qualification", "route_b_invocation_allowed",
    ]:
        replacement = True if key == "route_b_invocation_allowed" else "BROKEN"
        add(f"route_{key}", lambda d, key=key, replacement=replacement: d["route_a"].__setitem__(key, replacement))

    for key in base["scope_flags"]:
        add(f"scope_flag_{key}", lambda d, key=key: d["scope_flags"].__setitem__(key, True))
    for record, source in enumerate(base["source_registry"]):
        for key in source:
            replacement = 1900 if key == "year" else "BROKEN"
            add(
                f"source_{record}_{key}",
                lambda d, record=record, key=key, replacement=replacement:
                    d["source_registry"][record].__setitem__(key, replacement),
            )
    for index in range(len(base["nonclaims"])):
        add(f"nonclaim_{index}", lambda d, index=index: d["nonclaims"].__setitem__(index, "BROKEN"))

    finite_attacks = {
        "role": "FINITE_PROVES_ALL_N",
        "n_values": [2],
        "seeds": [0],
        "time_grid": [0],
        "asymptotic_time": 1,
        "case_count": 1,
        "pencil_row_count": 1,
        "exact_hermitian_entry_check_count": 1,
        "exact_commutator_entry_check_count": 1,
        "exact_trace_and_energy_check_count": 1,
        "minimum_sampled_pencil_gap": "0.000000000000e+00",
        "maximum_sampled_newton_residual": "1.000000000000e+00",
        "maximum_atlas_matrix_residual": "1.000000000000e+00",
        "maximum_inverse_position_residual": "1.000000000000e+00",
        "maximum_positive_position_error_at_T": "1.000000000000e+00",
        "maximum_negative_position_error_at_T": "1.000000000000e+00",
        "maximum_positive_velocity_error_at_T": "1.000000000000e+00",
        "maximum_negative_velocity_error_at_T": "1.000000000000e+00",
    }
    for key, value in finite_attacks.items():
        add(f"finite_{key}", lambda d, key=key, value=value: d["finite_regression"].__setitem__(key, value))

    row_attacks = [
        ("row_case_id", lambda r: r.__setitem__("case_id", "BROKEN")),
        ("row_N", lambda r: r.__setitem__("N", 99)),
        ("row_seed", lambda r: r.__setitem__("seed", 99)),
        ("row_q", lambda r: r["q"].__setitem__(0, "99")),
        ("row_p", lambda r: r["p"].__setitem__(0, "99")),
        ("row_g", lambda r: r.__setitem__("g", "99")),
        ("row_H", lambda r: r.__setitem__("hamiltonian", "99")),
        ("row_trace", lambda r: r["trace_invariants"].__setitem__(0, "99")),
        ("row_trace_L2", lambda r: r.__setitem__("trace_L2_equals_2H", "99")),
        ("row_hermitian_count", lambda r: r.__setitem__("exact_hermitian_entry_checks", 99)),
        ("row_commutator_count", lambda r: r.__setitem__("exact_commutator_entry_checks", 99)),
        ("pencil_time", lambda r: r["pencil_rows"][0].__setitem__("time", 99)),
        ("pencil_position", lambda r: r["pencil_rows"][0]["positions"].__setitem__(0, "9.900000000000e+01")),
        ("pencil_velocity", lambda r: r["pencil_rows"][0]["velocities"].__setitem__(0, "9.900000000000e+01")),
        ("pencil_gap", lambda r: r["pencil_rows"][0].__setitem__("minimum_gap", "9.900000000000e+01")),
        ("pencil_newton", lambda r: r["pencil_rows"][0].__setitem__("newton_residual", "1.000000000000e+00")),
        ("scatter_lambda", lambda r: r["scattering"]["ordered_velocities"].__setitem__(0, "9.900000000000e+01")),
        ("scatter_intercept", lambda r: r["scattering"]["intercepts"].__setitem__(0, "9.900000000000e+01")),
        ("scatter_gauge", lambda r: r["scattering"].__setitem__("gauge_overlap_max_error", "1.000000000000e+00")),
        ("scatter_atlas", lambda r: r["scattering"].__setitem__("atlas_matrix_max_residual", "1.000000000000e+00")),
        ("scatter_inverse", lambda r: r["scattering"].__setitem__("inverse_position_max_residual", "1.000000000000e+00")),
        ("scatter_T", lambda r: r["scattering"].__setitem__("asymptotic_time", 1)),
        ("scatter_pos_x", lambda r: r["scattering"].__setitem__("positive_position_max_error", "9.900000000000e+01")),
        ("scatter_neg_x", lambda r: r["scattering"].__setitem__("negative_position_max_error", "9.900000000000e+01")),
        ("scatter_pos_v", lambda r: r["scattering"].__setitem__("positive_velocity_max_error", "9.900000000000e+01")),
        ("scatter_neg_v", lambda r: r["scattering"].__setitem__("negative_velocity_max_error", "9.900000000000e+01")),
        ("scatter_in_v", lambda r: r["scattering"]["incoming_velocity_order"].__setitem__(0, "9.900000000000e+01")),
        ("scatter_out_v", lambda r: r["scattering"]["outgoing_velocity_order"].__setitem__(0, "9.900000000000e+01")),
        ("scatter_in_a", lambda r: r["scattering"]["incoming_intercept_order"].__setitem__(0, "9.900000000000e+01")),
        ("scatter_out_a", lambda r: r["scattering"]["outgoing_intercept_order"].__setitem__(0, "9.900000000000e+01")),
    ]
    for name, attack in row_attacks:
        add(name, lambda d, attack=attack: attack(d["finite_regression"]["rows"][0]))

    repaired = 0
    for name, item in mutations:
        if not rejected(item):
            raise AssertionError(f"checker accepted repaired-hash mutation {name}")
        repaired += 1

    stale = deepcopy(base)
    stale["finite_regression"]["rows"][0]["pencil_rows"][0]["positions"][0] = "9.900000000000e+01"
    if not rejected(stale):
        raise AssertionError("checker accepted stale-hash mutation")

    print(json.dumps({
        "status": "C196_MUTATION_PASS",
        "repaired_hash_rejections": repaired,
        "stale_hash_rejections": 1,
        "total_rejections": repaired + 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
