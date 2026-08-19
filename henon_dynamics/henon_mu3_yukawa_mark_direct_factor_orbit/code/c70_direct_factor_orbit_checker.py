#!/usr/bin/env python3
"""Independent checker for the C70 orbit and mass certificate."""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from math import prod
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c70_direct_factor_orbit_evidence.json"
SOURCES = {
    "c66": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_cokernel/results/c66_mark_snf_evidence.json",
    "c66_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_cokernel/C66_PREFREEZE_MANIFEST.json",
    "c69": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_defect_splitting/results/c69_defect_splitting_evidence.json",
    "c69_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_defect_splitting/C69_PREFREEZE_MANIFEST.json",
}
HASHES = {
    "c66": "ce74edeec04b245637e5b12165a7fcdeb42475b0dead7373b1bcf3e37f22beb1",
    "c66_manifest": "aa9a750fd87cfd09948167e0af93145823dff7d34c7bdb1ed13d1a8df493c626",
    "c69": "388c250bc8eb475c5bb7bd556376e69d964c7820c5386cd1b51d09b984e136c9",
    "c69_manifest": "55ace9cd2236a4e053f8d4c1c66e21c686118a720f62662050622b612ff70f42",
}
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"


def canon(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def aut_by_blocks(p: int, exponents: list[int]) -> int:
    """Count endomorphisms, then impose invertible equal-exponent blocks mod p."""
    end_exp = sum(min(a, b) for a in exponents for b in exponents)
    multiplicities = Counter(exponents)
    diagonal_dimension = sum(m * m for m in multiplicities.values())
    gl_product = prod(prod(p ** m - p ** i for i in range(m))
                      for m in multiplicities.values())
    return p ** (end_exp - diagonal_dimension) * gl_product


def factor(value: int) -> dict[str, int]:
    out: dict[str, int] = {}
    p = 2
    while p * p <= value:
        while value % p == 0:
            out[str(p)] = out.get(str(p), 0) + 1
            value //= p
        p = 3 if p == 2 else p + 2
    if value > 1:
        out[str(value)] = out.get(str(value), 0) + 1
    return out


def gaussian_binomial_recursive(n: int, k: int, q: int) -> int:
    values = [0] * (k + 1)
    values[0] = 1
    for level in range(1, n + 1):
        old = values[:]
        for j in range(1, min(level, k) + 1):
            values[j] = old[j - 1] + q ** j * old[j]
    return values[k]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    raw = args.evidence.read_bytes()
    doc = json.loads(raw)
    assert raw == canon(doc)
    assert doc["schema_id"] == "hcs-c70-direct-factor-orbit-prefreeze-v1"
    assert doc["status"] == "PREFREEZE_G3_PASS"
    assert doc["scope_literal"] == FIREWALL
    assert {name: digest(path.read_bytes()) for name, path in SOURCES.items()} == HASHES
    assert doc["authority"] == HASHES
    c66 = json.loads(SOURCES["c66"].read_text())
    c69 = json.loads(SOURCES["c69"].read_text())

    types = {
        "C2": [4, 3] + [2] * 3 + [1] * 10,
        "C3": [2, 1], "D2": [3, 1, 1],
        "K2": [4] + [2] * 3 + [1] * 8, "K3": [2, 1],
    }
    assert doc["primary_types"] == types
    assert c66["primary_invariants"]["2"] == sorted([2 ** e for e in types["C2"]])
    assert c66["primary_invariants"]["3"] == sorted([3 ** e for e in types["C3"]])
    assert c69["defect_invariants"] == sorted([2 ** e for e in types["D2"]])
    expected_conjugates = {name: [sum(e >= r for e in values)
                                  for r in range(1, max(values) + 1)]
                           for name, values in types.items()}
    assert doc["conjugate_partitions"] == expected_conjugates
    expected_multiplicities = {name: {str(k): v for k, v in sorted(Counter(values).items())}
                                 for name, values in types.items()}
    assert doc["multiplicities"] == expected_multiplicities

    orders = {
        "Aut_C2": aut_by_blocks(2, types["C2"]),
        "Aut_C3": aut_by_blocks(3, types["C3"]),
        "Aut_D": aut_by_blocks(2, types["D2"]),
        "Aut_K2": aut_by_blocks(2, types["K2"]),
        "Aut_K3": aut_by_blocks(3, types["K3"]),
    }
    orders["Aut_C"] = orders["Aut_C2"] * orders["Aut_C3"]
    orders["Aut_K"] = orders["Aut_K2"] * orders["Aut_K3"]
    assert doc["automorphism_orders"] == orders
    assert doc["automorphism_prime_factorizations"] == {k: factor(v) for k, v in orders.items()}
    assert orders["Aut_C3"] == orders["Aut_K3"] == 108
    assert orders["Aut_D"] == 384

    kd_exp = sum(min(a, b) for a in types["K2"] for b in types["D2"])
    dk_exp = sum(min(a, b) for a in types["D2"] for b in types["K2"])
    assert doc["hom_exponents"] == {"Hom_D_to_K": dk_exp, "Hom_K_to_D": kd_exp}
    assert kd_exp == dk_exp == 41
    assert doc["hom_orders"] == {"Hom_D_to_K": 2 ** dk_exp, "Hom_K_to_D": 2 ** kd_exp}
    hom_invariants = [2] * 32 + [4] * 3 + [8]
    assert doc["hom_group_invariants"] == {"Hom_D_to_K": hom_invariants,
                                            "Hom_K_to_D": hom_invariants}
    assert c69["complement_count"] == 2 ** kd_exp

    pair_stabilizer = orders["Aut_D"] * orders["Aut_K"]
    factor_stabilizer = pair_stabilizer * 2 ** kd_exp
    assert doc["ordered_pair_stabilizer"] == {
        "structure": "Aut(D) x Aut(K)", "order": pair_stabilizer,
        "prime_factorization": factor(pair_stabilizer),
    }
    assert doc["D_setwise_stabilizer"] == {
        "structure": "Hom(K,D) semidirect (Aut(D) x Aut(K))",
        "order": factor_stabilizer, "prime_factorization": factor(factor_stabilizer),
    }
    factors = orders["Aut_C"] // factor_stabilizer
    decompositions = orders["Aut_C"] // pair_stabilizer
    assert factors == doc["direct_factor_count"] == 5846893330432
    assert decompositions == doc["ordered_decomposition_count"] == 12857454406351852314558464
    assert doc["direct_factor_count_prime_factorization"] == factor(factors)
    assert doc["ordered_decomposition_count_prime_factorization"] == factor(decompositions)
    assert doc["complements_per_direct_factor"] == 2 ** 41
    split_embedding_stabilizer = orders["Aut_K"] * 2 ** 41
    split_embeddings = factors * orders["Aut_D"]
    assert doc["split_embedding_stabilizer"] == {
        "structure": "Hom(K,D) semidirect Aut(K)",
        "order": split_embedding_stabilizer,
        "prime_factorization": factor(split_embedding_stabilizer),
    }
    assert doc["split_embedding_count"] == split_embeddings == 2245207038885888
    assert doc["split_embedding_count_prime_factorization"] == factor(split_embeddings)

    lam = expected_conjugates["C2"]
    mu = expected_conjugates["D2"] + [0, 0]
    birkhoff_exp = sum(mu[i + 1] * (lam[i] - mu[i]) for i in range(len(lam)))
    gaussian_factors = [gaussian_binomial_recursive(lam[i] - mu[i + 1],
                                                     mu[i] - mu[i + 1], 2)
                        for i in range(len(lam))]
    all_subgroups = 2 ** birkhoff_exp * prod(gaussian_factors)
    assert doc["birkhoff_subgroup_count"] == {
        "p_power_exponent": 16,
        "gaussian_binomial_factors": [44731051, 1, 3, 1],
    }
    assert all_subgroups == doc["all_D_subgroup_count"] == 8794482475008
    assert doc["all_D_subgroup_count_prime_factorization"] == factor(all_subgroups)
    assert doc["nondirect_D_subgroup_count"] == all_subgroups - factors == 2947589144576
    assert doc["all_D_monomorphism_count"] == all_subgroups * orders["Aut_D"] == 3377081270403072
    assert all(doc["mass_identities"].values()) and len(doc["mass_identities"]) == 4
    assert decompositions == factors * 2 ** 41
    assert orders["Aut_C"] == factors * factor_stabilizer == decompositions * pair_stabilizer
    assert orders["Aut_C"] == split_embeddings * split_embedding_stabilizer

    assert doc["orbit_claims"] == {
        "AutC_transitive_on_D_type_direct_factors": True,
        "AutC_transitive_on_all_D_type_subgroups": False,
        "AutC_transitive_on_ordered_DK_decompositions": True,
        "AutC_transitive_on_split_embeddings": True,
    }
    counter = doc["nondirect_counterexample"]
    assert counter == {
        "ambient_2_type": types["C2"],
        "subgroup_generators": ["2*g4", "f1", "f2"],
        "subgroup_type": types["D2"],
        "quotient_2_type": [3] + [2] * 3 + [1] * 9,
        "required_complement_2_type": types["K2"],
        "is_direct_factor": False,
    }
    assert counter["quotient_2_type"] != counter["required_complement_2_type"]
    assert doc["claims"] == {
        "all_isomorphic_subgroups_claimed": False,
        "arithmetic_local_claimed": False,
        "canonical_decomposition_claimed": False,
        "full_burnside_ring_claimed": False,
        "restricted_finite_abelian_orbits_only": True,
    }
    print(json.dumps({"status": "PASS", "direct_factor_count": factors,
                      "ordered_decomposition_count": decompositions,
                      "split_embedding_count": split_embeddings,
                      "all_D_subgroup_count": all_subgroups,
                      "nondirect_D_subgroup_count": all_subgroups - factors,
                      "complements_per_direct_factor": 2 ** 41,
                      "counterexample": "VERIFIED"}, sort_keys=True))


if __name__ == "__main__":
    main()
