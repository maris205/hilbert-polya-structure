#!/usr/bin/env python3
"""Independent C79 checker.

This checker reconstructs the actual C75 point-set closure table and counts
minimum restoration subsets directly.  It does not use C73's block formula
to obtain either rho or W; the block formula is checked only after the direct
enumeration has produced the canonical evidence table.
"""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
from itertools import combinations, product
from math import comb
from pathlib import Path
import json
import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
ROOT = PROJECT.parents[1]
EVIDENCE = PROJECT / "results/c79_repair_witness_multiplicity_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
MODULI = (9, 3, 2)
ALL_MASK = (1 << 16) - 1
HASHES = {
    "c73": "e91c8e6dcf1de5362b1a052ada83eb758b2c2d75520c1e8bdbd37ab055c725e5",
    "c73_manifest": "a50b5707d36f8b94b463e6c5fc4b5b7f6d6df7eb5e87d70bfc82d2b1a653cd8d",
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
    "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
    "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
    "c77": "f7e2db84698ec61bf6283175368d2749d7f17ac77baeda37fd0a5cb8caf1c634",
    "c77_manifest": "bcc3273b481123f89ed5bf10c216bcae7a2ac3ff77685edcba976ea959e84dbc",
    "c78": "728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae",
    "c78_manifest": "955b5ce23bf811d7377c0e41afd8d7dbc384a467790647e04cf0dadc98347c60",
}

C73 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability"
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C76 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas"
C77 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_subgroup_mobius_reliability"
C78 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_repair_distance_geometry"


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw):
    return sha256(raw).hexdigest()


def add(left, right):
    return tuple((x + y) % modulus for x, y, modulus in zip(left, right, MODULI))


def multiple(coefficient, value):
    return tuple(coefficient * x % modulus for x, modulus in zip(value, MODULI))


def order(value):
    for candidate in range(1, 55):
        if multiple(candidate, value) == (0, 0, 0):
            return candidate
    raise AssertionError(value)


def cyclic(value):
    return frozenset(multiple(k, value) for k in range(order(value)))


def mask_for(labels):
    return sum(1 << (int(label[1:]) - 1) for label in labels)


def coefficient_table_from_evidence(value):
    return {
        tuple(int(part) for part in key.split(",")): int(number)
        for key, number in value.items()
    }


def sparse_counter(counter):
    return {
        f"{rho},{witness}": counter[(rho, witness)]
        for rho, witness in sorted(counter)
        if counter[(rho, witness)]
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    evidence_raw = args.evidence.read_bytes()
    evidence = json.loads(evidence_raw)
    assert evidence_raw == canonical(evidence)
    assert evidence["schema_id"] == "hcs-c79-repair-witness-multiplicity-prefreeze-v1"
    assert evidence["status"] == "PREFREEZE_G3_PASS"
    assert evidence["scope_literal"] == FIREWALL

    source_paths = {
        "c73": C73 / "results/c73_generation_blocker_reliability_evidence.json",
        "c73_manifest": C73 / "C73_PREFREEZE_MANIFEST.json",
        "c75": C75 / "results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": C75 / "C75_PREFREEZE_MANIFEST.json",
        "c76": C76 / "results/c76_closure_orbit_atlas_evidence.json",
        "c76_manifest": C76 / "C76_PREFREEZE_MANIFEST.json",
        "c77": C77 / "results/c77_subgroup_mobius_reliability_evidence.json",
        "c77_manifest": C77 / "C77_PREFREEZE_MANIFEST.json",
        "c78": C78 / "results/c78_repair_distance_geometry_evidence.json",
        "c78_manifest": C78 / "C78_PREFREEZE_MANIFEST.json",
    }
    assert {name: digest(path.read_bytes()) for name, path in source_paths.items()} == HASHES
    assert evidence["authority"] == HASHES
    c73 = json.loads(source_paths["c73"].read_text())
    c75 = json.loads(source_paths["c75"].read_text())
    c76 = json.loads(source_paths["c76"].read_text())
    c77 = json.loads(source_paths["c77"].read_text())
    c78 = json.loads(source_paths["c78"].read_text())
    assert all(doc["status"] == "PREFREEZE_G3_PASS" for doc in (c73, c75, c76, c77, c78))
    assert all(doc["scope_literal"] == FIREWALL for doc in (c73, c75, c76, c77, c78))

    rows = c75["closure_incidence"]["all_subgroups"]
    coordinates = [tuple(row) for row in c75["named_coordinate_source"]["coordinates"]]
    subgroups = [frozenset(tuple(point) for point in row["subgroup_points"]) for row in rows]
    index = {subgroup: i for i, subgroup in enumerate(subgroups)}
    cyclics = [cyclic(point) for point in coordinates]

    def extend(left, right):
        return frozenset(add(a, b) for a in left for b in right)

    extension = [[index[extend(subgroup, cyclics[label])] for label in range(16)]
                 for subgroup in subgroups]
    zero = index[frozenset({(0, 0, 0)})]
    full = index[frozenset(product(range(9), range(3), range(2)))]
    closure = [zero] * (1 << 16)
    for mask in range(1, 1 << 16):
        low = mask & -mask
        closure[mask] = extension[closure[mask ^ low]][low.bit_length() - 1]
    full_minimal = [
        mask for mask in range(1 << 16)
        if closure[mask] == full and all(
            closure[mask ^ (1 << bit)] != full
            for bit in range(16) if mask & (1 << bit)
        )
    ]
    assert len(full_minimal) == 25

    # Direct minimum-witness calculation.  Every restoration subset is tested
    # against the independently reconstructed closure table.
    table = Counter()
    by_deleted = [Counter() for _ in range(17)]
    by_retained = [Counter() for _ in range(17)]
    global_rho_witness = Counter()
    distance_masks = {rho: [] for rho in range(4)}
    witness_masks = {witness: [] for witness in (1, 4, 7, 8, 25)}
    for deleted in range(1 << 16):
        retained = ALL_MASK ^ deleted
        minimum = None
        witness_count = None
        deleted_labels = [bit for bit in range(16) if deleted & (1 << bit)]
        for size in range(len(deleted_labels) + 1):
            witnesses = []
            for chosen in combinations(deleted_labels, size):
                restoration = sum(1 << bit for bit in chosen)
                if closure[retained | restoration] == full:
                    witnesses.append(restoration)
            if witnesses:
                minimum = size
                witness_count = len(witnesses)
                break
        assert minimum is not None and witness_count is not None
        key = (deleted.bit_count(), minimum, witness_count)
        table[key] += 1
        by_deleted[deleted.bit_count()][(minimum, witness_count)] += 1
        by_retained[retained.bit_count()][(minimum, witness_count)] += 1
        global_rho_witness[(minimum, witness_count)] += 1
        distance_masks[minimum].append(deleted)
        witness_masks[witness_count].append(deleted)

    assert global_rho_witness == Counter({
        (0, 1): 30400,
        (1, 1): 30400,
        (1, 4): 1984,
        (1, 7): 192,
        (1, 8): 128,
        (2, 4): 1984,
        (2, 7): 192,
        (2, 8): 128,
        (2, 25): 64,
        (3, 25): 64,
    })
    assert evidence["witness_multiplicity_atlas"]["global_rho_witness_counts"] == sparse_counter(global_rho_witness)
    assert evidence["witness_multiplicity_atlas"]["distance_three_masks"] == sorted(distance_masks[3])
    assert evidence["witness_multiplicity_atlas"]["max_witness_masks"] == witness_masks[25]
    assert evidence["witness_multiplicity_atlas"]["max_witness_multiplicity"] == 25
    assert evidence["witness_multiplicity_atlas"]["witness_value_counts"] == {
        str(witness): sum(value for (rho, witness_value), value in global_rho_witness.items()
                          if witness_value == witness)
        for witness in (1, 4, 7, 8, 25)
    }
    assert evidence["witness_multiplicity_atlas"]["distance_value_counts"] == {
        str(rho): sum(value for (rho_value, witness), value in global_rho_witness.items()
                      if rho_value == rho)
        for rho in range(4)
    }

    definition = evidence["definition"]
    assert definition == {
        "deleted_set": "D",
        "retained_set": "A=L\\D",
        "repair_distance": "rho(D)=min{|R|: R subset D and Phi((L\\D) union R)=Q}",
        "witness_multiplicity": "W(D)=#{R subset D: |R|=rho(D), Phi((L\\D) union R)=Q}",
        "pivot": "S9",
        "direction_blocks": [["S1"], ["S16"], ["S7", "S15"], ["S3", "S4", "S8", "S11", "S12"]],
        "direction_block_sizes": [1, 1, 2, 5],
        "dummy_labels": ["S2", "S5", "S6", "S10", "S13", "S14"],
        "rho_formula": "rho(D)=1_{S9 in D}+max(0,t(D)-2)",
        "witness_formula": (
            "W(D)=1 for t<=2; W=sum sizes of fully deleted blocks for t=3; "
            "W=sum pairwise size products for t=4"
        ),
        "maximum_repair_distance": 3,
        "witness_values": [1, 4, 7, 8, 25],
    }
    polynomial = evidence["trivariate_generating_function"]
    assert polynomial["x_convention"] == "x marks deleted labels"
    assert polynomial["u_convention"] == "u marks repair distance rho(D)"
    assert polynomial["v_convention"] == "v marks minimum-restoration witness multiplicity W(D)"
    assert polynomial["definition"] == "G(x,u,v)=sum_D x^|D| u^rho(D) v^W(D)"
    assert polynomial["block_state_formula"].startswith("G=(1+x)^6 sum_{I subset")
    assert evidence["claims"] == {
        "all_65536_deletion_sets_enumerated": True,
        "exact_minimum_restoration_witness_count": True,
        "structural_witness_formula_verified": True,
        "rho_at_most_three": True,
        "witness_values_exact": True,
        "full_burnside_ring_claimed": False,
        "arithmetic_local_claimed": False,
    }

    expected_deleted_rows = [
        {"deleted_count": size, "rho_witness_counts": sparse_counter(by_deleted[size])}
        for size in range(17)
    ]
    expected_retained_rows = [
        {"retained_count": size, "rho_witness_counts": sparse_counter(by_retained[size])}
        for size in range(17)
    ]
    atlas = evidence["witness_multiplicity_atlas"]
    assert atlas["by_deleted_cardinality"] == expected_deleted_rows
    assert atlas["by_retained_cardinality"] == expected_retained_rows
    assert all(sum(row["rho_witness_counts"].values()) == comb(16, row["deleted_count"])
               for row in expected_deleted_rows)

    actual_coefficients = dict(table)
    expected_coefficients = coefficient_table_from_evidence(
        evidence["trivariate_generating_function"]["coefficient_table"]
    )
    assert actual_coefficients == expected_coefficients
    assert evidence["trivariate_generating_function"]["P_x_at_u1_v1"] == {
        str(k): comb(16, k) for k in range(17)
    }
    assert evidence["trivariate_generating_function"]["P_1_at_u_v1"] == {
        "0": 30400, "1": 32704, "2": 2368, "3": 64
    }

    # Check the C78 structural formula and C79 witness formula separately.
    blocks = [row["labels"] for row in c73["generation_structure"]["projective_direction_blocks"]]
    sizes = [len(block) for block in blocks]
    block_masks = [mask_for(block) for block in blocks]
    pivot = mask_for([c73["generation_structure"]["pivot"]])
    structural = Counter()
    for deleted in range(1 << 16):
        flags = [(deleted & block) == block for block in block_masks]
        full_indices = [i for i, flag in enumerate(flags) if flag]
        rho = int(bool(deleted & pivot)) + max(0, len(full_indices) - 2)
        if len(full_indices) <= 2:
            witness = 1
        elif len(full_indices) == 3:
            witness = sum(sizes[i] for i in full_indices)
        else:
            witness = sum(sizes[i] * sizes[j] for i, j in combinations(full_indices, 2))
        structural[(deleted.bit_count(), rho, witness)] += 1
    assert structural == actual_coefficients

    # SymPy expands the block-state formula and compares every coefficient.
    x, u, v = sp.symbols("x u v")
    block_poly = 0
    for state in product((0, 1), repeat=4):
        chosen = [i for i, full_flag in enumerate(state) if full_flag]
        term = x ** sum(sizes[i] for i in chosen)
        for i, full_flag in enumerate(state):
            if not full_flag:
                term *= (1 + x) ** sizes[i] - x ** sizes[i]
        rho_block = max(0, len(chosen) - 2)
        if len(chosen) <= 2:
            witness = 1
        elif len(chosen) == 3:
            witness = sum(sizes[i] for i in chosen)
        else:
            witness = sum(sizes[i] * sizes[j] for i, j in combinations(chosen, 2))
        block_poly += term * u ** rho_block * v ** witness
    predicted = sp.expand((1 + x) ** 6 * (1 + x * u) * block_poly)
    actual = sp.expand(sum(value * x ** k * u ** rho * v ** witness
                            for (k, rho, witness), value in actual_coefficients.items()))
    assert predicted == actual
    assert sp.expand(predicted.subs({u: 1, v: 1})) == sp.expand((1 + x) ** 16)
    assert sp.expand(predicted.subs({x: 1, v: 1})) == 30400 + 32704 * u + 2368 * u ** 2 + 64 * u ** 3

    print(json.dumps({
        "status": "SYMPY_CROSSCHECK_PASS",
        "support_count": 65536,
        "full_minimal_support_count": len(full_minimal),
        "global_rho_witness_counts": sparse_counter(global_rho_witness),
        "P_x_at_u1_v1": "(1+x)^16",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
