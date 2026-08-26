#!/usr/bin/env python3
"""Repaired-hash semantic and stale-hash attacks for HCS-C171."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c171_ehrenfest_evidence.json"
CHECKER = ROOT / "code/c171_ehrenfest_checker.py"


def digest(data: dict) -> str:
    work = dict(data)
    work.pop("payload_sha256", None)
    raw = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def put(data: object, path: tuple[object, ...], value: object) -> None:
    target = data
    for key in path[:-1]:
        target = target[key]  # type: ignore[index]
    target[path[-1]] = value  # type: ignore[index]


def main() -> None:
    source = json.loads(EVIDENCE.read_text())
    mutations = [
        ("schema", ("schema",), "forged"),
        ("candidate", ("candidate_id",), "HCS-X"),
        ("date", ("evaluation_date",), "2026-01-01"),
        ("scope", ("scope_literal",), "expanded"),
        ("commit", ("source_commit",), "0"*40),
        ("top_extra", ("forged",), True),
        ("object", ("source_lock","object"), "fitted"),
        ("parameter", ("source_lock","parameters"), "prime d"),
        ("clock", ("source_lock","clock"), "two steps"),
        ("cutoff", ("source_lock","cutoff","d_max"), 17),
        ("precision", ("source_lock","precision"), "float"),
        ("walsh", ("walsh_spectral_theorem","eigenvalue"), "1"),
        ("basis", ("walsh_spectral_theorem","complete_orthogonal_basis"), False),
        ("am", ("trace_determinant_theorem","family_uniform_artin_mazur_interpretation"), True),
        ("return", ("return_theorem","odd_times_zero"), False),
        ("kernel", ("lumping_theorem","kernel"), "forged"),
        ("compression", ("lumping_theorem","spectral_compression"), "none"),
        ("control", ("arithmetic_controls",0,"name"), "prime fit"),
        ("ledger_delete", ("finite_ledgers",), deepcopy(source["finite_ledgers"][:-1])),
        ("row_d", ("finite_ledgers",4,"d"), 99),
        ("dimension", ("finite_ledgers",5,"dimension"), 1),
        ("eigenvalue", ("finite_ledgers",6,"distinct_eigenvalues",2), "9"),
        ("multiplicity", ("finite_ledgers",7,"multiplicities",2), 999),
        ("trace", ("finite_ledgers",8,"trace_n_0_to_24",4), "999"),
        ("return_probability", ("finite_ledgers",9,"return_probability_n_0_to_24",6), "999"),
        ("odd", ("finite_ledgers",10,"odd_return_probabilities_zero"), False),
        ("factor", ("finite_ledgers",11,"determinant_factors",0,"exponent"), 0),
        ("balance", ("finite_ledgers",12,"detailed_balance_edge_weights",0), "0"),
        ("similarity", ("finite_ledgers",13,"symmetric_offdiagonal_squared",0), "0"),
        ("checksum", ("finite_ledgers",14,"krawtchouk_endpoint_checksum",0), 999),
        ("route", ("route_a","tuple",0), "A0_ANALYTIC_ARITHMETIC_ORIGIN"),
        ("route_b", ("route_a","route_b_invocation_allowed"), True),
        ("target", ("claim_boundary","target_divisor_matching"), True),
        ("euler", ("claim_boundary","euler_factors"), True),
        ("hp", ("claim_boundary","hilbert_polya_operator"), True),
        ("proof", ("claim_boundary","finite_ledgers_are_proof"), True),
        ("gate", ("integrity","hard_gate_status"), "FAIL"),
        ("review", ("integrity","external_reviewer_simulated"), True),
    ]
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c171-mutations-") as temporary:
        for name, path, value in mutations:
            candidate = deepcopy(source)
            put(candidate, path, value)
            candidate["payload_sha256"] = digest(candidate)
            output = Path(temporary) / f"{name}.json"
            output.write_text(json.dumps(candidate, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
            result = subprocess.run([sys.executable, str(CHECKER), str(output), "--mutation-fast"],
                                    capture_output=True, text=True)
            if result.returncode == 0:
                raise AssertionError(f"checker accepted repaired mutation {name}")
            rejected.append(name)
        stale = deepcopy(source)
        stale["payload_sha256"] = "0"*64
        output = Path(temporary) / "stale.json"
        output.write_text(json.dumps(stale, sort_keys=True, indent=2, ensure_ascii=False)+"\n")
        result = subprocess.run([sys.executable, str(CHECKER), str(output), "--mutation-fast"],
                                capture_output=True, text=True)
        if result.returncode == 0:
            raise AssertionError("checker accepted stale hash")
    print(json.dumps({"status": "C171_MUTATION_PASS", "repaired_hash_rejected": len(rejected),
                      "stale_hash_rejected": 1, "total": len(rejected)+1, "names": rejected}, sort_keys=True))


if __name__ == "__main__":
    main()
