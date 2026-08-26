#!/usr/bin/env python3
"""Semantic repaired-hash and stale-hash attacks for the C185 checker."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c185_brockett_evidence.json"
CHECKER = ROOT / "code/c185_brockett_checker.py"


def canonical_hash(payload: dict) -> str:
    work = dict(payload)
    work.pop("payload_sha256", None)
    return sha256(json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def set_path(payload: object, path: tuple[object, ...], value: object) -> None:
    cursor = payload
    for key in path[:-1]:
        cursor = cursor[key]  # type: ignore[index]
    cursor[path[-1]] = value  # type: ignore[index]


def rejected(payload: dict, repaired: bool) -> bool:
    if repaired:
        payload["payload_sha256"] = canonical_hash(payload)
    with tempfile.TemporaryDirectory(prefix="c185-mutation-") as tmp:
        path = Path(tmp) / "attacked.json"
        path.write_text(json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        proc = subprocess.run([sys.executable, str(CHECKER), str(path)], capture_output=True, text=True)
        return proc.returncode != 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    attacks: list[tuple[str, tuple[object, ...], object]] = [
        ("candidate", ("candidate_id",), "HCS-C999"),
        ("date", ("evaluation_date",), "1900-01-01"),
        ("commit", ("source_commit",), "0" * 40),
        ("scope", ("scope_literal",), "BROKEN_SCOPE"),
        ("evaluator_version", ("evaluator", "skill_version"), "9.9.9"),
        ("evaluator_path", ("evaluator", "authority_path"), "BROKEN"),
        ("evaluator_hash", ("evaluator", "authority_sha256"), "0" * 64),
        ("artifact_path", ("artifact_path_base",), "wrong/package"),
        ("family", ("source_lock", "family"), "n=7 only"),
        ("flow", ("source_lock", "flow"), "dH/dt=0"),
        ("arithmetic", ("source_lock", "arithmetic_origin"), "prime owner"),
        ("clock", ("source_lock", "clock"), "log p"),
        ("normalization", ("source_lock", "normalization"), "BROKEN"),
        ("determinant", ("source_lock", "determinant_convention"), "target determinant"),
        ("cutoff", ("source_lock", "cutoff"), "n<=999"),
        ("precision", ("source_lock", "precision"), "floating point"),
        ("forbidden", ("source_lock", "forbidden_data"), "none"),
        ("global", ("theorem", "global_existence"), "finite n only"),
        ("isospectral", ("theorem", "isospectrality"), "BROKEN"),
        ("lyapunov", ("theorem", "lyapunov_identity"), "dF/dt=-1"),
        ("equilibria", ("theorem", "equilibria"), "one equilibrium"),
        ("linearization", ("theorem", "pair_linearization"), "BROKEN"),
        ("morse", ("theorem", "morse_index"), "all indices zero"),
        ("generic", ("theorem", "generic_sorting"), "all initial data sort"),
        ("recurrence", ("theorem", "no_recurrence"), "periodic orbits exist"),
        ("boundary_theorem", ("theorem", "boundary"), "simple theorem includes repetitions"),
        ("n_max", ("regression_cutoff", "n_max"), 999),
        ("target_cutoff", ("regression_cutoff", "target_diagonal"), "BROKEN"),
        ("perm", ("permutation_rows", 0, "permutation", 0), 9),
        ("height", ("permutation_rows", 10, "height_Tr_DN"), 999),
        ("inversion", ("permutation_rows", 100, "inversions"), 999),
        ("mode_rate", ("permutation_rows", 1000, "pair_modes", 0, 2), 999),
        ("mode_sign", ("permutation_rows", 2000, "pair_modes", 0, 3), "zero"),
        ("mode_digest", ("permutation_rows", 3000, "pair_mode_digest"), "0" * 64),
        ("summary", ("size_summaries", 5, "permutation_count"), 999),
        ("matrix_digest", ("matrix_regressions", 5, "H_sha256"), "0" * 64),
        ("matrix_derivative", ("matrix_regressions", 5, "d_Tr_HN_dt"), "0/1"),
        ("boundary_status", ("boundary_controls", "status"), "MAIN_THEOREM"),
        ("boundary_source", ("boundary_controls", "repeated_source_spectrum", "distinct_diagonal_equilibria"), 6),
        ("boundary_source_tangent", ("boundary_controls", "repeated_source_spectrum", "zero_rate_interpretation"), "genuine tangent zero mode"),
        ("boundary_target", ("boundary_controls", "repeated_target_spectrum", "commutator_is_zero"), False),
        ("boundary_nonclaim", ("boundary_controls", "nonclaim"), "full Bruhat closure proved"),
        ("count_perm", ("counts", "permutation_rows"), 999),
        ("count_modes", ("counts", "pair_mode_rows"), 999),
        ("source_key", ("source_registry", 0, "key"), "broken"),
        ("source_authors", ("source_registry", 0, "authors"), "Unknown"),
        ("source_title", ("source_registry", 0, "title"), "Broken title"),
        ("source_journal", ("source_registry", 0, "journal"), "Broken journal"),
        ("source_volume", ("source_registry", 0, "volume"), 999),
        ("source_pages", ("source_registry", 0, "pages"), "1--2"),
        ("source_year", ("source_registry", 0, "year"), 1900),
        ("source_doi", ("source_registry", 0, "doi"), "BROKEN"),
        ("source_role", ("source_registry", 0, "role"), "novel package theorem"),
        ("attribution", ("attribution_boundary", "classical"), "package owns Brockett theorem"),
        ("A0", ("route_a_verdict", "A0"), "A0_ANALYTIC_ARITHMETIC_ORIGIN"),
        ("A1", ("route_a_verdict", "A1"), "A1_PASS_ANALYTIC"),
        ("A2", ("route_a_verdict", "A2"), "A2_ANALYTIC_DETERMINANT"),
        ("A3", ("route_a_verdict", "A3"), "A3_WEIL_COMPRESSION_COMPATIBLE"),
        ("A4", ("route_a_verdict", "A4"), "A4_ROUTE_B_READY"),
        ("overall", ("route_a_verdict", "overall"), "ROUTE_A_STRONG_CANDIDATE"),
        ("route_b", ("route_a_verdict", "route_b_invocation_allowed"), True),
        ("scope_euler", ("scope_flags", "claimed_euler_factor"), True),
        ("scope_root", ("scope_flags", "claimed_root_number"), True),
        ("scope_target", ("scope_flags", "used_target_zero_table"), True),
        ("nonclaim", ("nonclaims", 1), "full Bruhat closure theorem"),
        ("finite_proof", ("integrity", "finite_regressions_are_proof"), True),
        ("external_review", ("integrity", "external_reviewer_simulated"), True),
    ]
    repaired_rejections = 0
    for name, path, value in attacks:
        attacked = deepcopy(base)
        set_path(attacked, path, value)
        if not rejected(attacked, repaired=True):
            raise AssertionError(f"repaired-hash attack accepted: {name}")
        repaired_rejections += 1
    stale = deepcopy(base)
    stale["candidate_id"] = "HCS-C999"
    if not rejected(stale, repaired=False):
        raise AssertionError("stale-hash attack accepted")
    print(json.dumps({
        "status": "C185_MUTATION_PASS",
        "repaired_hash_rejections": repaired_rejections,
        "stale_hash_rejections": 1,
        "total_rejections": repaired_rejections + 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
