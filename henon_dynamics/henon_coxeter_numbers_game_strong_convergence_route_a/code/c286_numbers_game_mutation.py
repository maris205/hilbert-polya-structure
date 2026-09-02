#!/usr/bin/env python3
"""Raw-duplicate, repaired-hash, schema/type, and stale-hash attacks for C286."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results/c286_numbers_game_evidence.json"
CHECKER = ROOT / "code/c286_numbers_game_checker.py"


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def set_path(data: object, path: tuple[object, ...], value: object) -> None:
    target = data
    for key in path[:-1]:
        target = target[key]  # type: ignore[index]
    target[path[-1]] = value  # type: ignore[index]


def delete_path(data: object, path: tuple[object, ...]) -> None:
    target = data
    for key in path[:-1]:
        target = target[key]  # type: ignore[index]
    del target[path[-1]]  # type: ignore[index]


def run(candidate: Path) -> bool:
    env = dict(os.environ)
    env["C286_EVIDENCE"] = str(candidate)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(
        [sys.executable, "-B", str(CHECKER)],
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    return result.returncode != 0


def main() -> None:
    base = json.loads(SOURCE.read_text())
    mutations: list[tuple[str, tuple[object, ...], object]] = [
        ("source", ("source_commit",), "0" * 40),
        ("epoch", ("fixed_epoch",), 1),
        ("date", ("evaluation_date",), "2026-09-01"),
        ("scope", ("scope_literal",), "BROKEN"),
        ("evaluator", ("evaluator", "sha256"), "0" * 64),
        ("proof_status", ("proof_contract", "status"), "HEURISTIC"),
        ("proof_scope", ("proof_contract", "scope"), "affine systems too"),
        ("model_rule", ("model_contract", "legal_move"), "fire nonnegative coordinates"),
        ("model_update", ("model_contract", "coordinate_update"), "transpose omitted"),
        ("theorem_length", ("theorem_contract", "length"), "every play has |Phi+| moves"),
        ("theorem_coset", ("theorem_contract", "cumulative_element"), "some representative"),
        ("route_a", ("route_a", "tuple", 0), "A0_WEAK_ARITHMETIC_RELATION"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("scope_flag", ("scope_flags", "euler_factors"), True),
        ("headline", ("headline",), "tampered rehashed headline"),
        ("nonclaim", ("nonclaims", 0), "new theorem claimed"),
        ("nonclaim_second", ("nonclaims", 1), "affine systems are included"),
        ("analytic_obligation", ("analytic_proof_obligations", 2), "skip the weak-order ascent proof"),
        ("collision", ("collision_contract", "registry_range"), "HCS-C1 only"),
        ("collision_distinction", ("collision_contract", "closest_distinctions", 0), "C192 is identical"),
        ("count_case", ("regression", "counts", "case_rows"), 22),
        ("count_branch", ("regression", "counts", "branch_rows"), 3331),
        ("case_components", ("regression", "case_rows", 0, "components"), ["B1"]),
        ("case_cartan", ("regression", "case_rows", 2, "cartan", 0, 1), -2),
        ("case_initial", ("regression", "case_rows", 3, "initial_coordinates"), [1, 1]),
        ("case_zero_set", ("regression", "case_rows", 3, "zero_set"), []),
        ("case_strict", ("regression", "case_rows", 3, "strict_dominant"), True),
        ("case_length", ("regression", "case_rows", 6, "observed_length"), 9),
        ("case_terminal", ("regression", "case_rows", 18, "observed_terminal_coordinates"), [0, -1]),
        ("case_branches", ("regression", "case_rows", 16, "complete_branch_count"), 1),
        ("case_digest", ("regression", "case_rows", 4, "branch_sha256"), "0" * 64),
        ("rank_one_zero", ("regression", "case_rows", 1, "observed_length"), 1),
        ("disconnected", ("regression", "case_rows", 20, "observed_length"), 3),
        ("branch_node", ("regression", "branch_rows", 0, "sequence"), [2]),
        ("branch_length", ("regression", "branch_rows", 2, "length"), 2),
        ("branch_terminal", ("regression", "branch_rows", 10, "terminal_coordinates"), [0, 0, 0]),
        ("branch_index", ("regression", "branch_rows", 1, "branch_index"), 99),
        ("level_depth", ("regression", "level_rows", 3, "depth"), 99),
        ("level_prefix", ("regression", "level_rows", 20, "word_prefixes"), 999),
        ("level_edges", ("regression", "level_rows", 40, "outgoing_legal_edges_from_states"), 0),
        ("boundary_semantic", ("regression", "boundary_rows", 1, "status"), "walls have full length"),
        ("boundary_scope", ("regression", "boundary_rows", 7, "status"), "affine included"),
        ("unexpected_top", ("unexpected_top_level",), True),
        ("unexpected_nested", ("regression", "unexpected_nested"), True),
        ("unexpected_row", ("regression", "case_rows", 0, "unexpected"), True),
        ("unexpected_evaluator", ("evaluator", "unexpected"), True),
        ("unexpected_proof", ("proof_contract", "unexpected"), True),
        ("unexpected_collision", ("collision_contract", "unexpected"), True),
        ("type_epoch_float", ("fixed_epoch",), 1788307200.0),
        ("type_scope_flag_int", ("scope_flags", "euler_factors"), 0),
        ("type_route_b_int", ("route_a", "route_b_invocation_allowed"), 0),
        ("type_case_rank_bool", ("regression", "case_rows", 0, "rank"), True),
        ("type_case_cartan_float", ("regression", "case_rows", 0, "cartan", 0, 0), 2.0),
        ("type_case_length_bool", ("regression", "case_rows", 0, "observed_length"), True),
        ("type_branch_index_bool", ("regression", "branch_rows", 0, "branch_index"), False),
        ("type_branch_sequence_float", ("regression", "branch_rows", 0, "sequence", 0), 1.0),
        ("type_level_depth_bool", ("regression", "level_rows", 0, "depth"), False),
        ("type_boundary_face_int", ("regression", "boundary_rows", 0, "face"), 1),
        ("type_count_float", ("regression", "counts", "case_rows"), 23.0),
    ]
    drops = [
        ("drop_nonclaim", ("nonclaims",)),
        ("drop_nonclaim_item", ("nonclaims", 1)),
        ("drop_analytic_item", ("analytic_proof_obligations", 2)),
        ("drop_collision_item", ("collision_contract", "closest_distinctions", 0)),
        ("drop_model", ("model_contract", "word_convention")),
        ("drop_proof", ("proof_contract", "finite_evidence_role")),
        ("drop_collision_field", ("collision_contract", "registry_range")),
        ("drop_route_field", ("route_a", "overall")),
        ("drop_count_field", ("regression", "counts", "level_rows")),
        ("drop_case_field", ("regression", "case_rows", 0, "zero_set")),
        ("drop_branch_field", ("regression", "branch_rows", 0, "terminal_coordinates")),
        ("drop_level_field", ("regression", "level_rows", 0, "word_prefixes")),
        ("drop_boundary_field", ("regression", "boundary_rows", 0, "status")),
    ]

    repaired_trials: list[tuple[str, dict]] = []
    for name, path, value in mutations:
        trial = copy.deepcopy(base)
        set_path(trial, path, value)
        trial["payload_sha256"] = payload_hash(trial)
        repaired_trials.append((name, trial))
    for name, path in drops:
        trial = copy.deepcopy(base)
        delete_path(trial, path)
        trial["payload_sha256"] = payload_hash(trial)
        repaired_trials.append((name, trial))

    # Same-size duplicate/drop-replace attacks for every major row family.
    for family in ("case_rows", "branch_rows", "level_rows", "boundary_rows"):
        trial = copy.deepcopy(base)
        trial["regression"][family][-1] = copy.deepcopy(trial["regression"][family][0])
        trial["payload_sha256"] = payload_hash(trial)
        repaired_trials.append((f"duplicate_replace_{family}", trial))
    for name, path in (
        ("duplicate_replace_nonclaims", ("nonclaims",)),
        ("duplicate_replace_analytic", ("analytic_proof_obligations",)),
        ("duplicate_replace_collision_distinctions", ("collision_contract", "closest_distinctions")),
    ):
        trial = copy.deepcopy(base)
        target = trial
        for key in path:
            target = target[key]
        target[-1] = copy.deepcopy(target[0])
        trial["payload_sha256"] = payload_hash(trial)
        repaired_trials.append((name, trial))
    trial = copy.deepcopy(base)
    trial["regression"]["branch_rows"][0], trial["regression"]["branch_rows"][1] = (
        trial["regression"]["branch_rows"][1], trial["regression"]["branch_rows"][0]
    )
    trial["payload_sha256"] = payload_hash(trial)
    repaired_trials.append(("branch_order_swap", trial))

    # Raw duplicate keys are invisible to ordinary ``json.loads`` because its
    # last value wins.  Each attack leaves the last value and therefore the
    # parsed payload hash unchanged; only a duplicate-rejecting loader closes
    # this syntax-level escape.
    raw = SOURCE.read_text()
    raw_trials = [
        (
            "raw_duplicate_top",
            raw.replace(
                '  "candidate_id": "HCS-C286",',
                '  "candidate_id": "BROKEN",\n  "candidate_id": "HCS-C286",',
                1,
            ),
        ),
        (
            "raw_duplicate_nested",
            raw.replace(
                '    "version": "0.2.0"',
                '    "version": "BROKEN",\n    "version": "0.2.0"',
                1,
            ),
        ),
        (
            "raw_duplicate_row",
            raw.replace(
                '      "branch_index": 0,',
                '      "branch_index": 999,\n      "branch_index": 0,',
                1,
            ),
        ),
    ]
    assert all(text != raw for _, text in raw_trials)

    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c286-numbers-mutation-") as temp:
        directory = Path(temp)
        accepted: list[str] = []
        for index, (name, trial) in enumerate(repaired_trials):
            candidate = directory / f"{index:02d}_{name}.json"
            candidate.write_text(json.dumps(trial, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            was_rejected = run(candidate)
            rejected += was_rejected
            if not was_rejected:
                accepted.append(name)

        for offset, (name, text) in enumerate(raw_trials, start=len(repaired_trials)):
            candidate = directory / f"{offset:02d}_{name}.json"
            candidate.write_text(text)
            was_rejected = run(candidate)
            rejected += was_rejected
            if not was_rejected:
                accepted.append(name)

        stale = copy.deepcopy(base)
        stale["headline"] += " stale tamper"
        stale_path = directory / "stale_hash_control.json"
        stale_path.write_text(json.dumps(stale, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        rejected += run(stale_path)

    total = len(repaired_trials) + len(raw_trials) + 1
    assert not accepted, f"accepted repaired-hash mutations: {accepted}"
    assert rejected == total
    print(
        f"C286 hostile mutation audit: PASS {rejected}/{total} "
        "(raw duplicate keys, repaired-hash semantic/schema/type mutations, "
        "and stale-hash control)"
    )


if __name__ == "__main__":
    main()
