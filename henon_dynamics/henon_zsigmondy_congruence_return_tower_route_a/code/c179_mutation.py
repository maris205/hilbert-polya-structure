#!/usr/bin/env python3
"""Hostile repaired-hash semantic mutations for the HCS-C179 checker."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "code/c179_zsigmondy_return_checker.py"
EVIDENCE = ROOT / "results/c179_zsigmondy_return_evidence.json"


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
    ("source", ("source_commit",), "0" * 40),
    ("evaluator_version", ("evaluator", "version"), "0.1.0"),
    ("evaluator_hash", ("evaluator", "sha256"), "0" * 64),
    ("scope", ("scope_literal",), "BROKEN_SCOPE"),
    ("source_object", ("source_lock", "object"), "identity map"),
    ("source_origin", ("source_lock", "arithmetic_origin"), "fitted data"),
    ("source_domain", ("source_lock", "parameter_domain"), "one example"),
    ("source_clock", ("source_lock", "clock"), "log-prime time"),
    ("source_normalization", ("source_lock", "normalization"), "weighted"),
    ("source_determinant", ("source_lock", "determinant_convention"), "regularized target"),
    ("source_globalizations", ("source_lock", "globalizations"), "identified"),
    ("source_precision", ("source_lock", "precision"), "floating point"),
    ("source_training", ("source_lock", "training_data"), "target table"),
    ("source_allowed", ("source_lock", "allowed_data"), "all external tables"),
    ("source_forbidden", ("source_lock", "forbidden_data"), "none"),
    ("citation_doi", ("attribution_registry", 0, "doi"), "10.0000/fake"),
    ("citation_year", ("attribution_registry", 1, "year"), 1905),
    ("attribution_status_novelty", ("attribution_registry", 0, "status"), "NEW_THEOREM_CLAIMED"),
    ("primitive_theorem", ("theorem_ledger", "primitive_return_equivalence"), "false"),
    ("zsigmondy_theorem", ("theorem_ledger", "zsigmondy_scope"), "claimed new"),
    ("lift_theorem", ("theorem_ledger", "prime_power_lift"), "wrong formula"),
    ("fiber_theorem", ("theorem_ledger", "finite_fiber"), "wrong cycles"),
    ("union_theorem", ("theorem_ledger", "disjoint_union"), "zero fixed points"),
    ("profinite_theorem", ("theorem_ledger", "profinite_limit"), "all fixed"),
    ("owner_theorem", ("theorem_ledger", "owner_nonuniqueness"), "unique owner"),
    (
        "owner_theorem_absolute_enlarged_impossibility",
        ("theorem_ledger", "owner_nonuniqueness"),
        "finite congruence fibers have incompatible fixed ledgers, therefore every possible enlarged determinant owner is absolutely impossible",
    ),
    ("pair_limit", ("finite_regression_sentinels", "pair_a_max"), 13),
    ("time_limit", ("finite_regression_sentinels", "time_max"), 9),
    ("z_difference", ("finite_regression_sentinels", "zsigmondy_rows", 0, "difference"), 4),
    ("z_exception", ("finite_regression_sentinels", "zsigmondy_rows", 4, "exception"), None),
    ("z_primitive", ("finite_regression_sentinels", "zsigmondy_rows", 8, "primitive_primes"), []),
    ("global_fixed", ("finite_regression_sentinels", "global_rows", 0, "disjoint_union_fixed_count"), 0),
    ("global_profinite", ("finite_regression_sentinels", "global_rows", 0, "profinite_fixed_count"), 1),
    ("global_cycles", ("finite_regression_sentinels", "global_rows", 9, "primitive_cycle_count"), -1),
    ("fiber_multiplier", ("finite_regression_sentinels", "finite_fiber_rows", 0, "multiplier"), 0),
    ("fiber_order", ("finite_regression_sentinels", "finite_fiber_rows", 20, "order"), 999),
    ("fiber_zeta", ("finite_regression_sentinels", "finite_fiber_rows", 30, "zeta_factor"), "1"),
    ("fiber_reversor", ("finite_regression_sentinels", "finite_fiber_rows", 40, "inversion_reversor_verified"), False),
    ("lift_valuation", ("finite_regression_sentinels", "prime_power_lift_rows", 0, "base_valuation"), 99),
    ("lift_order", ("finite_regression_sentinels", "prime_power_lift_rows", 30, "predicted_order"), 1),
    ("route_tuple", ("route_a", "tuple"), []),
    ("route_overall", ("route_a", "overall"), "ROUTE_A_SUCCESS"),
    ("route_A0", ("route_a", "A0_qualification"), "A0_PASS"),
    (
        "route_A0_appended_log_clock",
        ("route_a", "A0_qualification"),
        "RATIONAL_PRIMES_EMERGE_AS_FIRST_RETURN_MODULI_BUT_NO_SINGLE_GLOBAL_PRIME_ORBIT_OWNER_OR_LOG_P_CLOCK_AND_LOG_P_CLOCK_ASSIGNED",
    ),
    ("route_A1", ("route_a", "A1_qualification"), "A1_PASS"),
    ("route_A2", ("route_a", "A2_qualification"), "A2_PASS"),
    ("route_A3", ("route_a", "A3_qualification"), "A3_PASS"),
    ("route_A4", ("route_a", "A4_qualification"), "A4_FAIL"),
    (
        "route_A4_appended_target_operator",
        ("route_a", "A4_qualification"),
        "FINITE_PERMUTATION_AND_PROFINITE_HAAR_KOOPMAN_LIFTS_ARE_NATURAL_SAME_CLOCK_UNITARIES_AND_TARGET_OPERATOR_IDENTIFIED",
    ),
    ("route_B", ("route_a", "route_b_invocation_allowed"), True),
    ("scope_zero", ("scope_flags", "used_target_zero_table"), True),
    ("scope_log", ("scope_flags", "assigned_log_p_roof"), True),
    ("scope_euler", ("scope_flags", "claimed_local_euler_factor"), True),
    ("scope_root", ("scope_flags", "claimed_root_number"), True),
    ("scope_hp", ("scope_flags", "claimed_hilbert_polya"), True),
    ("integrity_proof", ("integrity", "finite_ledgers_are_proof"), True),
    ("integrity_novelty", ("integrity", "zsigmondy_theorem_claimed_new"), True),
    ("integrity_lift", ("integrity", "order_lift_proved_in_package"), False),
    ("integrity_citations", ("integrity", "citation_population"), 0),
    ("integrity_review", ("integrity", "external_reviewer_simulated"), True),
    ("integrity_owner", ("integrity", "global_owner_uniqueness_claimed"), True),
]

REQUIRED_CONTRACT_ATTACKS = {
    "attribution_status_novelty",
    "owner_theorem_absolute_enlarged_impossibility",
    "route_A0_appended_log_clock",
    "route_A4_appended_target_operator",
}


def checker_rejects(data: dict, path: Path) -> bool:
    path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    completed = subprocess.run(
        [sys.executable, str(CHECKER), "--input", str(path)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return completed.returncode != 0


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    repaired = 0
    labels = {label for label, _, _ in MUTATIONS}
    if not REQUIRED_CONTRACT_ATTACKS <= labels:
        raise AssertionError("required exact-match contract attacks are missing")
    with tempfile.TemporaryDirectory(prefix="c179-mutation-") as directory:
        path = Path(directory) / "mutated.json"
        for label, field_path, value in MUTATIONS:
            mutated = deepcopy(original)
            set_path(mutated, field_path, value)
            mutated["payload_sha256"] = canonical_hash(mutated)
            if not checker_rejects(mutated, path):
                raise AssertionError(f"checker accepted repaired-hash mutation: {label}")
            repaired += 1

        stale = deepcopy(original)
        stale["theorem_ledger"]["prime_power_lift"] = "stale-hash mutation"
        stale_rejected = checker_rejects(stale, path)
        if not stale_rejected:
            raise AssertionError("checker accepted stale-hash mutation")

    print(
        json.dumps(
            {
                "status": "C179_MUTATION_PASS",
                "repaired_hash_mutation_rejections": repaired,
                "stale_hash_mutation_rejections": int(stale_rejected),
                "required_contract_attack_rejections": sorted(REQUIRED_CONTRACT_ATTACKS),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
