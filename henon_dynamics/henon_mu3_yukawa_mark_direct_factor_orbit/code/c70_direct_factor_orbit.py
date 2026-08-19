#!/usr/bin/env python3
"""Produce the exact C70 direct-factor orbit certificate."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from math import prod
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C66 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_cokernel"
C69 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_defect_splitting"
OUT = PROJECT / "results/c70_direct_factor_orbit_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
HASHES = {
    "c66": "ce74edeec04b245637e5b12165a7fcdeb42475b0dead7373b1bcf3e37f22beb1",
    "c66_manifest": "aa9a750fd87cfd09948167e0af93145823dff7d34c7bdb1ed13d1a8df493c626",
    "c69": "388c250bc8eb475c5bb7bd556376e69d964c7820c5386cd1b51d09b984e136c9",
    "c69_manifest": "55ace9cd2236a4e053f8d4c1c66e21c686118a720f62662050622b612ff70f42",
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def conjugate_partition(exponents: list[int]) -> list[int]:
    return [sum(value >= level for value in exponents)
            for level in range(1, max(exponents) + 1)]


def automorphism_order(p: int, exponents: list[int]) -> int:
    conjugate = conjugate_partition(exponents)
    value = Fraction(p ** sum(x * x for x in conjugate), 1)
    for multiplicity in Counter(exponents).values():
        for j in range(1, multiplicity + 1):
            value *= Fraction(p ** j - 1, p ** j)
    assert value.denominator == 1
    return value.numerator


def hom_exponent(source: list[int], target: list[int]) -> int:
    return sum(min(a, b) for a in source for b in target)


def gaussian_binomial(n: int, k: int, p: int) -> int:
    assert 0 <= k <= n
    numerator = prod(p ** (n - i) - 1 for i in range(k))
    denominator = prod(p ** (k - i) - 1 for i in range(k))
    assert numerator % denominator == 0
    return numerator // denominator


def subgroup_type_count(ambient_conjugate: list[int], subgroup_conjugate: list[int], p: int) -> tuple[int, int, list[int]]:
    mu = subgroup_conjugate + [0] * (len(ambient_conjugate) - len(subgroup_conjugate) + 1)
    exponent = sum(mu[i + 1] * (ambient_conjugate[i] - mu[i])
                   for i in range(len(ambient_conjugate)))
    q_bins = [gaussian_binomial(ambient_conjugate[i] - mu[i + 1],
                                mu[i] - mu[i + 1], p)
              for i in range(len(ambient_conjugate))]
    return p ** exponent * prod(q_bins), exponent, q_bins


def factor_integer(value: int) -> dict[str, int]:
    factors: dict[str, int] = {}
    divisor = 2
    while divisor * divisor <= value:
        while value % divisor == 0:
            key = str(divisor)
            factors[key] = factors.get(key, 0) + 1
            value //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if value > 1:
        factors[str(value)] = factors.get(str(value), 0) + 1
    return factors


def main() -> None:
    paths = {
        "c66": C66 / "results/c66_mark_snf_evidence.json",
        "c66_manifest": C66 / "C66_PREFREEZE_MANIFEST.json",
        "c69": C69 / "results/c69_defect_splitting_evidence.json",
        "c69_manifest": C69 / "C69_PREFREEZE_MANIFEST.json",
    }
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == HASHES
    c66 = json.loads(raw["c66"])
    c69 = json.loads(raw["c69"])
    for doc in (c66, c69):
        assert doc["status"] == "PREFREEZE_G3_PASS"
        assert doc["scope_literal"] == FIREWALL
    assert c66["primary_invariants"]["2"] == [2] * 10 + [4] * 3 + [8, 16]
    assert c66["primary_invariants"]["3"] == [3, 9]
    assert c69["defect_invariants"] == [2, 2, 8]
    assert c69["complement_smith_invariants"] == [1, 1, 1, 1] + [2] * 8 + [4, 4, 12, 144]
    assert c69["complement_count"] == 2 ** 41

    C2 = [4, 3] + [2] * 3 + [1] * 10
    C3 = [2, 1]
    D2 = [3, 1, 1]
    K2 = [4] + [2] * 3 + [1] * 8
    K3 = [2, 1]
    types = {"C2": C2, "C3": C3, "D2": D2, "K2": K2, "K3": K3}
    conjugates = {name: conjugate_partition(values) for name, values in types.items()}
    assert conjugates == {
        "C2": [15, 5, 2, 1], "C3": [2, 1], "D2": [3, 1, 1],
        "K2": [12, 4, 1, 1], "K3": [2, 1],
    }

    aut_c2 = automorphism_order(2, C2)
    aut_c3 = automorphism_order(3, C3)
    aut_d = automorphism_order(2, D2)
    aut_k2 = automorphism_order(2, K2)
    aut_k3 = automorphism_order(3, K3)
    assert aut_c3 == aut_k3 == 108
    aut_c = aut_c2 * aut_c3
    aut_k = aut_k2 * aut_k3
    hom_kd_exp = hom_exponent(K2, D2)
    hom_dk_exp = hom_exponent(D2, K2)
    assert hom_kd_exp == hom_dk_exp == 41
    hom_kd = 2 ** hom_kd_exp
    assert hom_kd == c69["complement_count"]

    pair_stabilizer = aut_d * aut_k
    factor_stabilizer = pair_stabilizer * hom_kd
    assert aut_c % factor_stabilizer == 0
    assert aut_c % pair_stabilizer == 0
    direct_factor_count = aut_c // factor_stabilizer
    ordered_decomposition_count = aut_c // pair_stabilizer
    assert direct_factor_count == 5846893330432
    assert ordered_decomposition_count == 12857454406351852314558464
    assert ordered_decomposition_count == direct_factor_count * hom_kd
    assert aut_c == direct_factor_count * factor_stabilizer
    assert aut_c == ordered_decomposition_count * pair_stabilizer

    split_embedding_count = direct_factor_count * aut_d
    split_embedding_stabilizer = aut_k * hom_kd
    assert split_embedding_count == 2245207038885888
    assert aut_c == split_embedding_count * split_embedding_stabilizer
    all_D_subgroup_count, birkhoff_exponent, gaussian_factors = subgroup_type_count(
        conjugates["C2"], conjugates["D2"], 2)
    assert birkhoff_exponent == 16
    assert gaussian_factors == [44731051, 1, 3, 1]
    assert all_D_subgroup_count == 8794482475008
    nondirect_D_subgroup_count = all_D_subgroup_count - direct_factor_count
    assert nondirect_D_subgroup_count == 2947589144576
    all_monomorphism_count = all_D_subgroup_count * aut_d
    assert all_monomorphism_count == 3377081270403072

    counterexample = {
        "ambient_2_type": C2,
        "subgroup_generators": ["2*g4", "f1", "f2"],
        "subgroup_type": D2,
        "quotient_2_type": [3] + [2] * 3 + [1] * 9,
        "required_complement_2_type": K2,
        "is_direct_factor": False,
    }
    assert counterexample["quotient_2_type"] != K2

    aut_orders = {
        "Aut_C2": aut_c2, "Aut_C3": aut_c3, "Aut_C": aut_c,
        "Aut_D": aut_d, "Aut_K2": aut_k2, "Aut_K3": aut_k3,
        "Aut_K": aut_k,
    }
    result: dict[str, Any] = {
        "schema_id": "hcs-c70-direct-factor-orbit-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": HASHES,
        "primary_types": types,
        "conjugate_partitions": conjugates,
        "multiplicities": {name: {str(k): v for k, v in sorted(Counter(values).items())}
                             for name, values in types.items()},
        "automorphism_orders": aut_orders,
        "automorphism_prime_factorizations": {name: factor_integer(value)
                                                for name, value in aut_orders.items()},
        "hom_exponents": {"Hom_K_to_D": hom_kd_exp, "Hom_D_to_K": hom_dk_exp},
        "hom_orders": {"Hom_K_to_D": hom_kd, "Hom_D_to_K": 2 ** hom_dk_exp},
        "hom_group_invariants": {"Hom_K_to_D": [2] * 32 + [4] * 3 + [8],
                                 "Hom_D_to_K": [2] * 32 + [4] * 3 + [8]},
        "ordered_pair_stabilizer": {
            "structure": "Aut(D) x Aut(K)",
            "order": pair_stabilizer,
            "prime_factorization": factor_integer(pair_stabilizer),
        },
        "D_setwise_stabilizer": {
            "structure": "Hom(K,D) semidirect (Aut(D) x Aut(K))",
            "order": factor_stabilizer,
            "prime_factorization": factor_integer(factor_stabilizer),
        },
        "direct_factor_count": direct_factor_count,
        "direct_factor_count_prime_factorization": factor_integer(direct_factor_count),
        "ordered_decomposition_count": ordered_decomposition_count,
        "ordered_decomposition_count_prime_factorization": factor_integer(ordered_decomposition_count),
        "complements_per_direct_factor": hom_kd,
        "split_embedding_stabilizer": {
            "structure": "Hom(K,D) semidirect Aut(K)",
            "order": split_embedding_stabilizer,
            "prime_factorization": factor_integer(split_embedding_stabilizer),
        },
        "split_embedding_count": split_embedding_count,
        "split_embedding_count_prime_factorization": factor_integer(split_embedding_count),
        "all_D_subgroup_count": all_D_subgroup_count,
        "all_D_subgroup_count_prime_factorization": factor_integer(all_D_subgroup_count),
        "nondirect_D_subgroup_count": nondirect_D_subgroup_count,
        "all_D_monomorphism_count": all_monomorphism_count,
        "birkhoff_subgroup_count": {
            "p_power_exponent": birkhoff_exponent,
            "gaussian_binomial_factors": gaussian_factors,
        },
        "mass_identities": {
            "ordered_equals_factors_times_complements": ordered_decomposition_count == direct_factor_count * hom_kd,
            "AutC_equals_factors_times_setwise_stabilizer": aut_c == direct_factor_count * factor_stabilizer,
            "AutC_equals_decompositions_times_pair_stabilizer": aut_c == ordered_decomposition_count * pair_stabilizer,
            "AutC_equals_split_embeddings_times_stabilizer": aut_c == split_embedding_count * split_embedding_stabilizer,
        },
        "orbit_claims": {
            "AutC_transitive_on_D_type_direct_factors": True,
            "AutC_transitive_on_ordered_DK_decompositions": True,
            "AutC_transitive_on_split_embeddings": True,
            "AutC_transitive_on_all_D_type_subgroups": False,
        },
        "nondirect_counterexample": counterexample,
        "claims": {
            "restricted_finite_abelian_orbits_only": True,
            "canonical_decomposition_claimed": False,
            "all_isomorphic_subgroups_claimed": False,
            "full_burnside_ring_claimed": False,
            "arithmetic_local_claimed": False,
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({"status": result["status"],
                      "direct_factor_count": direct_factor_count,
                      "ordered_decomposition_count": ordered_decomposition_count,
                      "split_embedding_count": split_embedding_count,
                      "all_D_subgroup_count": all_D_subgroup_count,
                      "nondirect_D_subgroup_count": nondirect_D_subgroup_count,
                      "complements_per_direct_factor": hom_kd,
                      "mass_identities": result["mass_identities"]}, sort_keys=True))


if __name__ == "__main__":
    main()
