#!/usr/bin/env python3
"""Hostile semantic-mutation tests for the independent C173 checker."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
CHECKER = ROOT / "code/c173_lyness_checker.py"
EVIDENCE = ROOT / "results/c173_lyness_evidence.json"


def canonical_hash(payload: dict) -> str:
    work = dict(payload)
    work.pop("payload_sha256", None)
    return sha256(
        json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def set_path(payload: object, path: tuple[object, ...], value: object) -> None:
    cursor = payload
    for key in path[:-1]:
        cursor = cursor[key]  # type: ignore[index]
    cursor[path[-1]] = value  # type: ignore[index]


MUTATIONS: list[tuple[str, tuple[object, ...], object]] = [
    ("schema", ("schema",), "hcs-c173-mutated"),
    ("candidate", ("candidate_id",), "HCS-C000"),
    ("date", ("evaluation_date",), "2026-08-25"),
    ("source", ("source_commit",), "0" * 40),
    ("scope", ("scope_literal",), "BROKEN_SCOPE"),
    ("map", ("source_lock", "map"), "F(x,y)=(x,y)"),
    ("clock", ("source_lock", "clock"), "five ticks"),
    ("measure", ("source_lock", "measure"), "dx*dy"),
    ("convention", ("source_lock", "koopman_convention"), "U f=f o F^(-1)"),
    ("cutoff", ("source_lock", "cutoffs", "fixed_set_n_max"), 49),
    ("training", ("source_lock", "training_data"), "target fitted"),
    ("F1", ("iterate_theorem", "F1"), ["x", "y"]),
    ("F2", ("iterate_theorem", "F2"), ["bad", "bad"]),
    ("F3", ("iterate_theorem", "F3"), ["bad", "bad"]),
    ("F4", ("iterate_theorem", "F4"), ["bad", "bad"]),
    ("F5", ("iterate_theorem", "F5"), ["y", "x"]),
    ("identity", ("iterate_theorem", "global_identity"), "F^4=id_X"),
    ("fixed_point", ("periodic_structure", "fixed_point"), ["1", "1"]),
    ("least_periods", ("periodic_structure", "least_periods"), [1, 4]),
    ("period_five", ("periodic_structure", "all_nonfixed_points_have_exact_period_five"), False),
    ("first_failed", ("zeta_obstruction", "first_failed_coefficient"), 10),
    ("am_zeta", ("zeta_obstruction", "classical_artin_mazur_zeta_defined"), True),
    ("euler_product", ("zeta_obstruction", "finite_orbit_euler_product_defined"), True),
    ("jacobian", ("geometry", "jacobian_determinant"), "1"),
    ("density", ("geometry", "density_pullback_identity"), "0"),
    ("inverse", ("geometry", "inverse"), "F"),
    ("reversor", ("geometry", "reversor_identity"), "R*F*R=F"),
    ("unitary", ("koopman_theorem", "unitary"), False),
    ("order", ("koopman_theorem", "finite_order"), "U^4=I"),
    ("projection_sign", ("koopman_theorem", "spectral_projection"), "positive sign"),
    ("projection_range", ("koopman_theorem", "projection_range"), "wrong eigenspace"),
    ("infinite_dimensional", ("koopman_theorem", "all_five_eigenspaces_infinite_dimensional"), False),
    ("compact", ("koopman_theorem", "compact"), True),
    ("trace_class", ("koopman_theorem", "trace_class"), True),
    ("fredholm", ("koopman_theorem", "ordinary_fredholm_determinant_available"), True),
    ("self_adjoint", ("koopman_theorem", "self_adjoint"), True),
    ("grid_return", ("finite_regression_sentinels", "rational_grid", 0, "returns_at_five"), False),
    ("grid_iterate", ("finite_regression_sentinels", "rational_grid", 7, "iterates_1_through_5"), []),
    ("fixed_set", ("finite_regression_sentinels", "fixed_set_ledger", 4, "fixed_set"), "singleton_phi"),
    ("fixed_count", ("finite_regression_sentinels", "fixed_set_ledger", 4, "finite_fixed_count"), 1),
    ("route_tuple", ("route_a", "tuple"), []),
    ("route_overall", ("route_a", "overall"), "ROUTE_A_SUCCESS_ROUTE_B_READY"),
    ("route_b", ("route_a", "route_b_invocation_allowed"), True),
    ("prime_claim", ("claim_boundary", "prime_like_correspondence"), True),
    ("euler_claim", ("claim_boundary", "euler_factors"), True),
    ("hp_claim", ("claim_boundary", "hilbert_polya_operator"), True),
    ("hard_gate", ("integrity", "hard_gate_status"), "FAIL"),
    ("finite_proof", ("integrity", "finite_ledgers_are_proof"), True),
    ("citation_population", ("integrity", "citation_population"), 1),
]


def checker_rejects(payload: dict, path: Path) -> bool:
    path.write_text(json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    completed = subprocess.run(
        [sys.executable, str(CHECKER), "--input", str(path)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return completed.returncode != 0


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    repaired_rejections = 0
    with tempfile.TemporaryDirectory(prefix="c173-mutation-") as directory:
        path = Path(directory) / "mutated.json"
        for label, field_path, replacement in MUTATIONS:
            mutated = deepcopy(original)
            set_path(mutated, field_path, replacement)
            mutated["payload_sha256"] = canonical_hash(mutated)
            if not checker_rejects(mutated, path):
                raise AssertionError(f"checker accepted repaired-hash semantic mutation: {label}")
            repaired_rejections += 1

        stale = deepcopy(original)
        stale["iterate_theorem"]["global_identity"] = "F^6=id_X"
        stale_rejected = checker_rejects(stale, path)
        if not stale_rejected:
            raise AssertionError("checker accepted stale-hash mutation")

    print(
        json.dumps(
            {
                "status": "C173_MUTATION_PASS",
                "repaired_hash_mutation_rejections": repaired_rejections,
                "stale_hash_mutation_rejections": int(stale_rejected),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
