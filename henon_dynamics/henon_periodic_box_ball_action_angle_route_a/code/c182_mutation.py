#!/usr/bin/env python3
"""Hostile stale- and repaired-hash semantic mutations for C182."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "code/c182_periodic_bbs_checker.py"
EVIDENCE = ROOT / "results/c182_periodic_bbs_evidence.json"


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def set_path(data: object, path: tuple[object, ...], value: object) -> None:
    cursor = data
    for key in path[:-1]:
        cursor = cursor[key]  # type: ignore[index]
    cursor[path[-1]] = value  # type: ignore[index]


MUTATIONS: list[tuple[str, tuple[object, ...], object]] = [
    ("schema", ("schema",), "mutated"),
    ("candidate", ("candidate_id",), "HCS-C000"),
    ("date", ("evaluation_date",), "2026-08-25"),
    ("source_commit", ("source_commit",), "0" * 40),
    ("evaluator_skill", ("evaluator", "skill"), "wrong-evaluator"),
    ("evaluator_version", ("evaluator", "version"), "0.1.0"),
    ("evaluator_path", ("evaluator", "path"), "wrong/path"),
    ("evaluator_hash", ("evaluator", "sha256"), "0" * 64),
    ("scope", ("scope_literal",), "BROKEN_SCOPE"),
    ("source_verified", ("source_attribution", 0, "verified"), False),
    ("source_role", ("source_attribution", 1, "role"), "unverified folklore"),
    ("lock_object", ("source_lock", "object"), "identity map"),
    ("lock_family", ("source_lock", "family"), "one example only"),
    ("lock_phase", ("source_lock", "phase_space"), "R^2"),
    ("lock_dynamics", ("source_lock", "dynamics"), "random map"),
    ("lock_parameters", ("source_lock", "parameters"), "one fitted seed"),
    ("lock_provenance", ("source_lock", "parameter_provenance"), "post-hoc fitted"),
    ("lock_arithmetic", ("source_lock", "arithmetic_origin"), "prime table"),
    ("lock_clock", ("source_lock", "clock"), "log-prime time"),
    ("lock_normalization", ("source_lock", "normalization"), "fitted unfolding"),
    ("lock_determinant", ("source_lock", "determinant_convention"), "regularized unknown"),
    ("lock_cutoff", ("source_lock", "orbit_cutoff"), "best cutoff only"),
    ("lock_precision", ("source_lock", "precision"), "floating point"),
    ("lock_training", ("source_lock", "training_data"), "target zeros"),
    ("lock_allowed", ("source_lock", "allowed_data"), "unrestricted"),
    ("lock_forbidden", ("source_lock", "forbidden_data"), "none"),
    ("triage", ("theorem", "feasibility_triage"), "NOT CURRENTLY JUSTIFIED"),
    ("domain", ("theorem", "admissible_domain"), "L<2M"),
    ("symmetry", ("theorem", "internal_symmetry"), "alpha arbitrary"),
    ("matrix_theorem", ("theorem", "sector_matrix"), "F=I"),
    ("torus", ("theorem", "sector_torus"), "no quotient"),
    ("sector_mult", ("theorem", "sector_multiplicity"), "one component"),
    ("mobius", ("theorem", "mobius_count"), "no inversion"),
    ("snf", ("theorem", "snf_order"), "order=det always"),
    ("component_fixed", ("theorem", "component_fixed_points"), "always zero"),
    ("aggregate_fixed", ("theorem", "aggregate_fixed_points"), "not aggregated"),
    ("primitive", ("theorem", "primitive_cycles"), "fixed=primitive"),
    ("zeta", ("theorem", "zeta_koopman"), "zeta=det"),
    ("commutativity", ("theorem", "commutativity"), "maps do not commute"),
    ("saturation", ("theorem", "saturation"), "no saturation"),
    ("vacuum", ("theorem", "vacuum_boundary"), "vacuum omitted"),
    ("half_filling", ("theorem", "half_filling_boundary"), "half filling excluded"),
    ("novelty", ("theorem", "source_novelty_boundary"), "new KTT theorem"),
    ("sentinel_proof", ("finite_regression_sentinels", "sentinels_are_proof"), True),
    ("coverage", ("finite_regression_sentinels", "coverage", "L_max"), 13),
    ("content", ("finite_regression_sentinels", "level_rows", 7, "content", 0, "m_j"), 3),
    ("vacancy", ("finite_regression_sentinels", "level_rows", 7, "content", 0, "p_j"), 2),
    ("alpha", ("finite_regression_sentinels", "level_rows", 7, "sectors", 0, "alpha", 0), 999),
    ("lambda", ("finite_regression_sentinels", "level_rows", 7, "sectors", 0, "lambda_exact_counts", 0), 999),
    ("matrix", ("finite_regression_sentinels", "level_rows", 7, "sectors", 0, "F_alpha", 0, 0), 999),
    ("det", ("finite_regression_sentinels", "level_rows", 7, "sectors", 0, "det_F_alpha"), 999),
    ("smith", ("finite_regression_sentinels", "level_rows", 7, "sectors", 0, "smith_invariants", 0), 999),
    ("translation_h", ("finite_regression_sentinels", "level_rows", 7, "sectors", 0, "translations", 0, "h", 0), 999),
    ("translation_order", ("finite_regression_sentinels", "level_rows", 7, "sectors", 0, "translations", 0, "order"), 999),
    ("component_prefix", ("finite_regression_sentinels", "level_rows", 7, "sectors", 0, "translations", 0, "fixed_component_prefix", 0, "fixed_points_per_component"), 999),
    ("level_cardinality", ("finite_regression_sentinels", "level_rows", 7, "level_cardinality"), 999),
    ("cycle_points", ("finite_regression_sentinels", "level_rows", 7, "evolutions", 0, "cycle_spectrum", 0, "points"), 999),
    ("fixed_prefix", ("finite_regression_sentinels", "level_rows", 7, "evolutions", 0, "fixed_point_prefix", 0, "fixed_points"), 999),
    ("state_count", ("finite_regression_sentinels", "state_aggregate_rows", 0, "state_count"), 999),
    ("length_count", ("finite_regression_sentinels", "length_aggregate_rows", 0, "positive_weight_state_count"), 999),
    ("route_tuple", ("route_a", "tuple"), []),
    ("route_overall", ("route_a", "overall"), "ROUTE_A_SUCCESS_ROUTE_B_READY"),
    ("route_b", ("route_a", "route_b_invocation_allowed"), True),
    ("scope_flag", ("scope_flags", "claimed_euler_factor"), True),
]


def checker_rejects(data: dict, path: Path) -> bool:
    path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    completed = subprocess.run(
        [sys.executable, str(CHECKER), "--input", str(path)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return completed.returncode != 0


def main() -> None:
    if len(MUTATIONS) != 64:
        raise AssertionError(f"expected 64 repaired-hash mutations, found {len(MUTATIONS)}")
    original = json.loads(EVIDENCE.read_text())
    repaired = 0
    with tempfile.TemporaryDirectory(prefix="c182-mutation-") as directory:
        path = Path(directory) / "mutated.json"
        for label, field_path, value in MUTATIONS:
            mutated = deepcopy(original)
            set_path(mutated, field_path, value)
            mutated["payload_sha256"] = canonical_hash(mutated)
            if not checker_rejects(mutated, path):
                raise AssertionError(f"checker accepted repaired-hash mutation: {label}")
            repaired += 1

        stale = deepcopy(original)
        stale["theorem"]["snf_order"] = "stale-hash false order"
        stale_rejected = checker_rejects(stale, path)
        if not stale_rejected:
            raise AssertionError("checker accepted stale-hash mutation")

    print(
        json.dumps(
            {
                "status": "C182_MUTATION_PASS",
                "repaired_hash_mutation_rejections": repaired,
                "stale_hash_mutation_rejections": int(stale_rejected),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
