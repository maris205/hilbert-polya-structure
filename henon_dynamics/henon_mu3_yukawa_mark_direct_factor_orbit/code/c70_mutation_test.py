#!/usr/bin/env python3
"""Hostile semantic mutations for the C70 checker."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c70_direct_factor_orbit_evidence.json"
CHECKER = Path(__file__).resolve().parent / "c70_direct_factor_orbit_checker.py"


def mutate(source: dict, path: list[object], value: object) -> dict:
    out = deepcopy(source)
    node = out
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    return out


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations = {
        "status": mutate(original, ["status"], "RELEASED"),
        "scope": mutate(original, ["scope_literal"], "BAD_EULER_ALLOWED"),
        "source": mutate(original, ["authority", "c69_manifest"], "0" * 64),
        "C2_type": mutate(original, ["primary_types", "C2", 0], 3),
        "K2_type": mutate(original, ["primary_types", "K2", 0], 3),
        "conjugate": mutate(original, ["conjugate_partitions", "C2", 0], 14),
        "multiplicity": mutate(original, ["multiplicities", "C2", "1"], 9),
        "AutC": mutate(original, ["automorphism_orders", "Aut_C"], 384),
        "AutK": mutate(original, ["automorphism_orders", "Aut_K"], 108),
        "aut_factor": mutate(original, ["automorphism_prime_factorizations", "Aut_C", "2"], 193),
        "hom_direction": mutate(original, ["hom_exponents", "Hom_K_to_D"], 40),
        "hom_order": mutate(original, ["hom_orders", "Hom_K_to_D"], 2 ** 40),
        "pair_stabilizer": mutate(original, ["ordered_pair_stabilizer", "order"], 384),
        "setwise_structure": mutate(original, ["D_setwise_stabilizer", "structure"], "Aut(D) x Aut(K)"),
        "setwise_order": mutate(original, ["D_setwise_stabilizer", "order"], original["ordered_pair_stabilizer"]["order"]),
        "factor_count": mutate(original, ["direct_factor_count"], 5846893330431),
        "decomposition_count": mutate(original, ["ordered_decomposition_count"], 5846893330432),
        "complements": mutate(original, ["complements_per_direct_factor"], 2 ** 40),
        "hom_structure": mutate(original, ["hom_group_invariants", "Hom_K_to_D", 0], 4),
        "split_stabilizer": mutate(original, ["split_embedding_stabilizer", "order"], 384),
        "split_embeddings": mutate(original, ["split_embedding_count"], 2245207038885887),
        "all_subgroups": mutate(original, ["all_D_subgroup_count"], 8794482475007),
        "nondirect_subgroups": mutate(original, ["nondirect_D_subgroup_count"], 1),
        "monomorphisms": mutate(original, ["all_D_monomorphism_count"], 3377081270403071),
        "birkhoff": mutate(original, ["birkhoff_subgroup_count", "p_power_exponent"], 15),
        "mass": mutate(original, ["mass_identities", "ordered_equals_factors_times_complements"], False),
        "split_orbit": mutate(original, ["orbit_claims", "AutC_transitive_on_split_embeddings"], False),
        "all_subgroups": mutate(original, ["orbit_claims", "AutC_transitive_on_all_D_type_subgroups"], True),
        "counter_quotient": mutate(original, ["nondirect_counterexample", "quotient_2_type", 0], 4),
        "counter_direct": mutate(original, ["nondirect_counterexample", "is_direct_factor"], True),
        "canonical": mutate(original, ["claims", "canonical_decomposition_claimed"], True),
    }
    rejected = []
    with tempfile.TemporaryDirectory(prefix="c70-mutations-") as tmp:
        for name, doc in mutations.items():
            path = Path(tmp) / f"{name}.json"
            path.write_bytes((json.dumps(doc, sort_keys=True, separators=(",", ":")) + "\n").encode())
            run = subprocess.run([sys.executable, str(CHECKER), "--evidence", str(path)],
                                 cwd=PROJECT, capture_output=True, text=True)
            assert run.returncode != 0, f"mutation accepted: {name}"
            rejected.append(name)
    print(json.dumps({"status": "PASS", "mutations_rejected": len(rejected),
                      "names": sorted(rejected)}, sort_keys=True))


if __name__ == "__main__":
    main()
