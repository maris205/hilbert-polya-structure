#!/usr/bin/env python3
"""Repaired-hash semantic mutation audit for HCS-C165."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c165_margolus_evidence.json"
CHECKER = ROOT / "code/c165_margolus_checker.py"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def set_path(container, path, value) -> None:
    current = container
    for item in path[:-1]:
        current = current[item]
    current[path[-1]] = value


def main() -> None:
    source = json.loads(EVIDENCE.read_text())
    repaired = [
        ("schema", ("schema",), "HCS-C165-v0"),
        ("candidate", ("candidate_id",), "HCS-C000"),
        ("date", ("date_utc",), "2026-01-01"),
        ("commit", ("source_commit",), "0" * 40),
        ("scope", ("scope_literal",), "BROKEN"),
        ("object", ("source_lock", "object"), "one rotation"),
        ("family", ("source_lock", "family"), "m<=16 theorem"),
        ("clock", ("source_lock", "clock"), "A alone"),
        ("normalization", ("source_lock", "normalization"), "unlabeled"),
        ("determinant", ("source_lock", "determinant_convention"), "scalar fit"),
        ("cutoff", ("source_lock", "cutoff"), "finite only"),
        ("precision", ("source_lock", "precision"), "floating point"),
        ("allowed", ("source_lock", "allowed_data"), "target table"),
        ("forbidden", ("source_lock", "forbidden_data"), "none"),
        ("pivot_candidate", ("pivot_record", "rejected_candidate"), "none"),
        ("pivot_reason", ("pivot_record", "reason"), "aesthetic"),
        ("pivot_replacement", ("pivot_record", "replacement"), "Rule 90"),
        ("pivot_reframe", ("pivot_record", "failed_claim_reframed_as_progress"), True),
        ("layers", ("site_permutation_theorem", "layers"), "A=B"),
        ("full_tick", ("site_permutation_theorem", "full_tick"), "T=A"),
        ("motion", ("site_permutation_theorem", "cell_motion"), "all sites +2"),
        ("order", ("site_permutation_theorem", "order"), "tau^(m-1)=identity"),
        ("pairing", ("necklace_conjugacy_theorem", "pairing"), "adjacent pairs"),
        ("intertwining", ("necklace_conjugacy_theorem", "intertwining"), "heuristic"),
        ("fixed_theorem", ("necklace_conjugacy_theorem", "fixed_count"), "#Fix=2^gcd"),
        ("chaos", ("necklace_conjugacy_theorem", "complexity_boundary"), "chaotic"),
        ("support", ("period_theorem", "support"), "all periods"),
        ("exact_formula", ("period_theorem", "exact_points"), "P=4^d"),
        ("cycle_formula", ("period_theorem", "primitive_cycles"), "C=P"),
        ("zeta", ("period_theorem", "zeta"), "zeta=1"),
        ("short_bound", ("concentration_theorem", "short_bound"), "Pr<=4^-m"),
        ("full_bound", ("concentration_theorem", "full_bound"), "Pr=1"),
        ("bound_proof", ("concentration_theorem", "proof_boundary"), "finite evidence"),
        ("reflection", ("reversibility_and_koopman", "reflection"), "r*tau=tau"),
        ("koopman_space", ("reversibility_and_koopman", "koopman_space"), "infinite target space"),
        ("koopman", ("reversibility_and_koopman", "koopman"), "self-adjoint"),
        ("antiunitary", ("reversibility_and_koopman", "antiunitary"), "Theta U Theta=U"),
        ("operator_boundary", ("reversibility_and_koopman", "operator_boundary"), "Hilbert--Polya operator"),
        ("m_max", ("finite_replay", "m_max"), 15),
        ("permutation_row", ("finite_replay", "family_rows", 4, "full_tick_site_permutation", 0), 0),
        ("pair_row", ("finite_replay", "family_rows", 5, "four_letter_pairing", 0, 1), 3),
        ("fixed_row", ("finite_replay", "family_rows", 6, "fixed_rows", 2, "fixed_configurations"), 3),
        ("period_row", ("finite_replay", "family_rows", 7, "period_rows", 2, "exact_period_configurations"), 0),
        ("short_row", ("finite_replay", "family_rows", 8, "short_period_configurations"), 0),
        ("bound_row", ("finite_replay", "family_rows", 9, "uniform_bound", "numerator"), 99),
        ("m1", ("finite_replay", "boundary_m1", "exact_period_one"), 3),
        ("m2", ("finite_replay", "boundary_m2", "primitive_two_cycles"), 5),
        ("progress", ("progress_and_boundary", "progress"), "finite table"),
        ("obstruction", ("progress_and_boundary", "route_a_obstruction"), "none"),
        ("A1", ("route_a", "tuple", 0), "A1_PASS_ANALYTIC"),
        ("overall", ("route_a", "overall"), "ROUTE_A_SUCCESS_ROUTE_B_READY"),
        ("A4", ("route_a", "A4_qualification"), "HILBERT_POLYA"),
        ("route_b", ("route_a", "route_b_invocation_allowed"), True),
        ("prime_flag", ("scope_flags", "uses_prime_table"), True),
        ("hilbert_flag", ("scope_flags", "claims_hilbert_polya"), True),
        ("chaos_flag", ("scope_flags", "claims_chaos_or_interaction"), True),
        ("nonclaim", ("nonclaims", 0), "chaos established"),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c165-mutations-") as temporary:
        for name, path, value in repaired:
            candidate = deepcopy(source)
            set_path(candidate, path, value)
            candidate["payload_sha256"] = payload_hash(candidate)
            target = Path(temporary) / f"{name}.json"
            target.write_text(json.dumps(candidate, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            result = subprocess.run([sys.executable, str(CHECKER), str(target)], capture_output=True, text=True)
            if result.returncode == 0:
                raise AssertionError(f"checker accepted repaired mutation {name}")
            rejected.append(name)
        stale = deepcopy(source)
        stale["payload_sha256"] = "0" * 64
        target = Path(temporary) / "stale.json"
        target.write_text(json.dumps(stale, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        result = subprocess.run([sys.executable, str(CHECKER), str(target)], capture_output=True, text=True)
        if result.returncode == 0:
            raise AssertionError("checker accepted stale hash")
    print(json.dumps({
        "status": "C165_MUTATION_PASS", "repaired_hash_rejected": len(repaired),
        "stale_hash_rejected": 1, "total": len(repaired) + 1, "names": rejected,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
