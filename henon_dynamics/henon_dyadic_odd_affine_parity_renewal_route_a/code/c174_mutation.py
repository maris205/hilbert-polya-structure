#!/usr/bin/env python3
"""Demand rejection of repaired-hash semantic mutations and a stale hash."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def payload_hash(payload: dict) -> str:
    work = dict(payload)
    work.pop("payload_sha256", None)
    raw = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def set_path(document: dict, path: tuple[object, ...], value: object) -> None:
    cursor: object = document
    for key in path[:-1]:
        cursor = cursor[key]  # type: ignore[index]
    cursor[path[-1]] = value  # type: ignore[index]


def checker_rejects(checker: Path, artifact: Path) -> bool:
    run = subprocess.run(
        [sys.executable, str(checker), "--evidence", str(artifact)],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return run.returncode != 0


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    checker = root / "code/c174_parity_renewal_checker.py"
    source = json.loads((root / "results/c174_parity_renewal_evidence.json").read_text())
    mutations: list[tuple[str, tuple[object, ...], object]] = [
        ("source_commit", ("source_commit",), "0" * 40),
        ("scope", ("scope_literal",), "ALLOW_TARGET_DATA"),
        ("evaluator_hash", ("evaluator", "authority_sha256"), "f" * 64),
        ("arithmetic_origin", ("source_lock", "arithmetic_origin"), "prime table"),
        ("word_cutoff", ("source_lock", "cutoffs", "word_n_max"), 7),
        ("prior_ownership", ("classical_foundation", "ownership"), "novel conjugacy"),
        ("fixed_count", ("fixed_word_theorem", "aggregate_rows", 0, "fixed_point_count"), 3),
        ("fixed_digest", ("fixed_word_theorem", "aggregate_rows", 1, "word_point_digest"), "0" * 64),
        ("zeta", ("fixed_word_theorem", "artin_mazur_zeta"), "1/(1-z)"),
        ("inverse_digest", ("inverse_conjugacy_sentinels", "aggregate_rows", 0, "inverse_prefix_digest"), "1" * 64),
        ("mobius", ("period_ledger", 5, "exact_period_points"), 1),
        ("stability", ("stability_theorem", "weighted_zeta"), "1/(1-2*z)"),
        ("exceptional", ("first_return_theorem", "exceptional_set"), "empty"),
        ("return_point", ("first_return_theorem", "finite_rows", 0, "fixed_point"), "7"),
        ("return_law", ("first_return_theorem", "finite_rows", 1, "conditional_haar_probability"), "1/3"),
        ("roof_count", ("original_clock_recovery", "finite_rows", 4, "roof_fixed_count"), 0),
        ("roof_zeta", ("original_clock_recovery", "roof_zeta"), "1/(1-z)"),
        ("operator", ("operator_boundary", "compact"), True),
        ("extension", ("operator_boundary", "natural_extension"), "same phase space"),
        ("even_boundary", ("parameter_and_boundary_audit", "even_a_boundary"), "still a self-map"),
        ("collatz_cycle", ("parameter_and_boundary_audit", "three_x_plus_one_boundary", "z2_cycle", 0), "1"),
        ("route_tuple", ("route_a", "tuple", 0), "A0_ANALYTIC_ARITHMETIC_ORIGIN"),
        ("overall", ("route_a", "overall"), "ROUTE_A_ACCEPTED"),
        ("forbidden_claim", ("claim_boundary", "hilbert_polya_operator"), True),
        ("external_review", ("integrity", "external_reviewer_simulated"), True),
    ]
    repaired_rejections = 0
    with tempfile.TemporaryDirectory(prefix="c174-mutations-") as tmp:
        tmpdir = Path(tmp)
        for index, (name, path, value) in enumerate(mutations):
            mutant = deepcopy(source)
            set_path(mutant, path, value)
            mutant["payload_sha256"] = payload_hash(mutant)
            artifact = tmpdir / f"{index:02d}_{name}.json"
            artifact.write_text(json.dumps(mutant, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            if not checker_rejects(checker, artifact):
                raise AssertionError(f"checker accepted repaired-hash mutation: {name}")
            repaired_rejections += 1

        stale = deepcopy(source)
        stale["route_a"]["overall"] = "ROUTE_A_ACCEPTED"
        stale_artifact = tmpdir / "stale_hash.json"
        stale_artifact.write_text(json.dumps(stale, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        stale_rejected = checker_rejects(checker, stale_artifact)
        if not stale_rejected:
            raise AssertionError("checker accepted stale-hash mutation")

    print(
        json.dumps(
            {
                "status": "C174_MUTATION_PASS",
                "repaired_hash_rejections": repaired_rejections,
                "stale_hash_rejections": int(stale_rejected),
                "total_rejections": repaired_rejections + int(stale_rejected),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
