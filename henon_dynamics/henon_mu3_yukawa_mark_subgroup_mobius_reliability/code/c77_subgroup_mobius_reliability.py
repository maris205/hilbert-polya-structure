#!/usr/bin/env python3
"""Produce the C77 subgroup-Möbius reliability certificate.

For each actual subgroup H of Q, n_H is the number of named coordinates in
H.  Independent deletion with probability q gives
P_{<=H}(q) = q^(16-n_H).  Möbius inversion on the subgroup inclusion poset
then gives the exact probability that the generated subgroup is H.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C76 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas"
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C73 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability"
OUT = PROJECT / "results/c77_subgroup_mobius_reliability_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
MODULI = (9, 3, 2)
LABELS = tuple(f"S{i}" for i in range(1, 17))
HASHES = {
    "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
    "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
    "c73": "e91c8e6dcf1de5362b1a052ada83eb758b2c2d75520c1e8bdbd37ab055c725e5",
    "c73_manifest": "a50b5707d36f8b94b463e6c5fc4b5b7f6d6df7eb5e87d70bfc82d2b1a653cd8d",
}
Point = tuple[int, int, int]


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def add(left: Point, right: Point) -> Point:
    return tuple((x + y) % modulus for x, y, modulus in zip(left, right, MODULI))  # type: ignore[return-value]


def multiple(coefficient: int, value: Point) -> Point:
    return tuple(coefficient * x % modulus for x, modulus in zip(value, MODULI))  # type: ignore[return-value]


def point_order(value: Point) -> int:
    for candidate in range(1, 55):
        if multiple(candidate, value) == (0, 0, 0):
            return candidate
    raise AssertionError("point order search failed")


def cyclic_subgroup(value: Point) -> frozenset[Point]:
    return frozenset(multiple(k, value) for k in range(point_order(value)))


def polynomial_terms(terms: dict[int, int]) -> dict[str, int]:
    return {str(power): int(coefficient) for power, coefficient in sorted(terms.items()) if coefficient}


def polynomial_add(target: dict[int, int], power: int, coefficient: int) -> None:
    target[power] = target.get(power, 0) + coefficient
    if target[power] == 0:
        del target[power]


def evaluate(polynomial: dict[int, int], q: Fraction) -> Fraction:
    return sum(Fraction(coefficient) * q ** power for power, coefficient in polynomial.items())


def main() -> None:
    source_paths = {
        "c76": C76 / "results/c76_closure_orbit_atlas_evidence.json",
        "c76_manifest": C76 / "C76_PREFREEZE_MANIFEST.json",
        "c75": C75 / "results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": C75 / "C75_PREFREEZE_MANIFEST.json",
        "c73": C73 / "results/c73_generation_blocker_reliability_evidence.json",
        "c73_manifest": C73 / "C73_PREFREEZE_MANIFEST.json",
    }
    raw = {name: path.read_bytes() for name, path in source_paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == HASHES
    c76 = json.loads(raw["c76"])
    c75 = json.loads(raw["c75"])
    c73 = json.loads(raw["c73"])
    assert c76["status"] == "PREFREEZE_G3_PASS"
    assert c75["status"] == "PREFREEZE_G3_PASS"
    assert c73["status"] == "PREFREEZE_G3_PASS"
    assert c76["scope_literal"] == c75["scope_literal"] == c73["scope_literal"] == FIREWALL
    assert c76["authority"] == {"c75": HASHES["c75"], "c75_manifest": HASHES["c75_manifest"]}
    assert c76["source_model"]["support_count"] == 1 << 16
    assert c76["closure_atlas"]["subgroup_count"] == 20
    assert c73["exact_reliability"]["homogeneous_expanded_coefficients"] == {
        "0": 1, "1": -1, "4": -1, "5": 1, "7": -1, "8": -1, "9": 5, "10": -3,
    }

    subgroup_rows = c75["closure_incidence"]["all_subgroups"]
    coordinates = [tuple(row) for row in c75["named_coordinate_source"]["coordinates"]]
    assert len(subgroup_rows) == 20 and len(coordinates) == 16
    subgroups = [frozenset(tuple(point) for point in row["subgroup_points"]) for row in subgroup_rows]
    assert len(set(subgroups)) == 20
    subgroup_index = {subgroup: index for index, subgroup in enumerate(subgroups)}
    assert all(subgroup_index[subgroup] == index for index, subgroup in enumerate(subgroups))

    n_values = [sum(point in subgroup for point in coordinates) for subgroup in subgroups]
    assert n_values == [5, 6, 7, 6, 7, 6, 8, 7, 8, 7, 11, 7, 7, 8, 12, 8, 8, 9, 15, 16]

    lower = [[index for index, subgroup in enumerate(subgroups) if subgroup <= subgroups[upper]]
             for upper in range(20)]
    mobius = [[0 for _ in range(20)] for _ in range(20)]
    for upper in range(20):
        for lower_index in sorted(lower[upper], key=lambda index: (len(subgroups[index]), index)):
            if lower_index == upper:
                mobius[lower_index][upper] = 1
            else:
                mobius[lower_index][upper] = -sum(
                    mobius[lower_index][middle]
                    for middle in lower[upper]
                    if middle != upper
                    and subgroups[lower_index] <= subgroups[middle]
                    and subgroups[middle] < subgroups[upper]
                )

    # Build the exact closure table and enumerate all retained supports.
    points = list(product(range(9), range(3), range(2)))
    cyclic = [cyclic_subgroup(point) for point in coordinates]
    def extend(left: frozenset[Point], right: frozenset[Point]) -> frozenset[Point]:
        return frozenset(add(a, b) for a in left for b in right)
    extension = [[subgroup_index[extend(subgroup, cyclic[label])] for label in range(16)]
                 for subgroup in subgroups]
    zero_index = subgroup_index[frozenset({(0, 0, 0)})]
    closure_index = [zero_index] * (1 << 16)
    for mask in range(1, 1 << 16):
        low = mask & -mask
        label = low.bit_length() - 1
        closure_index[mask] = extension[closure_index[mask ^ low]][label]
    direct_counts = [0] * 20
    direct_by_retained = [Counter() for _ in range(20)]
    for mask, subgroup in enumerate(closure_index):
        direct_counts[subgroup] += 1
        direct_by_retained[subgroup][mask.bit_count()] += 1
    assert sum(direct_counts) == 1 << 16

    subgroup_certificates: list[dict[str, Any]] = []
    exact_polynomials: list[dict[int, int]] = []
    for upper, subgroup in enumerate(subgroups):
        subset_poly = {16 - n_values[upper]: 1}
        exact_poly: dict[int, int] = {}
        for lower_index in lower[upper]:
            polynomial_add(exact_poly, 16 - n_values[lower_index], mobius[lower_index][upper])
        exact_polynomials.append(exact_poly)
        direct_poly: dict[int, int] = {}
        for retained, count in direct_by_retained[upper].items():
            for deleted in range(retained + 1):
                # q^(16-retained) (1-q)^retained, expanded in q.
                coefficient = count * ((-1) ** deleted)
                from math import comb
                polynomial_add(direct_poly, 16 - retained + deleted, coefficient * comb(retained, deleted))
        assert direct_poly == exact_poly
        assert evaluate(exact_poly, Fraction(1, 2)) == Fraction(direct_counts[upper], 1 << 16)
        subgroup_certificates.append({
            "subgroup_index": upper,
            "subgroup_order": len(subgroup),
            "subgroup_points": [list(point) for point in sorted(subgroup)],
            "n_H": n_values[upper],
            "P_leq_polynomial": polynomial_terms(subset_poly),
            "P_eq_polynomial": polynomial_terms(exact_poly),
            "direct_support_count": direct_counts[upper],
            "direct_by_retained_cardinality": {
                str(size): direct_by_retained[upper][size]
                for size in sorted(direct_by_retained[upper])
            },
        })

    sum_poly: dict[int, int] = {}
    for polynomial in exact_polynomials:
        for power, coefficient in polynomial.items():
            polynomial_add(sum_poly, power, coefficient)
    assert sum_poly == {0: 1}
    top_poly = exact_polynomials[-1]
    top_expected = {0: 1, 1: -1, 4: -1, 5: 1, 7: -1, 8: -1, 9: 5, 10: -3}
    assert top_poly == top_expected

    grid = [Fraction(index, 20) for index in range(21)]
    grid_nonnegative = all(evaluate(poly, q) >= 0 for poly in exact_polynomials for q in grid)
    assert grid_nonnegative
    result: dict[str, Any] = {
        "schema_id": "hcs-c77-subgroup-mobius-reliability-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": HASHES,
        "subgroup_poset": {
            "subgroup_count": 20,
            "rows": subgroup_certificates,
            "n_H_vector": n_values,
            "inclusion_matrix": [[int(subgroups[left] <= subgroups[right]) for right in range(20)] for left in range(20)],
        },
        "mobius_matrix": mobius,
        "direct_enumeration": {
            "support_count": 1 << 16,
            "generated_support_count_by_subgroup": {str(index): count for index, count in enumerate(direct_counts)},
            "retained_cardinality_total": [sum(counter[size] for counter in direct_by_retained) for size in range(17)],
        },
        "reliability": {
            "deletion_probability_variable": "q",
            "formula": "P_{<=H}(q)=q^(16-n_H); P_{=H}(q)=sum_{K<=H} mu(K,H) q^(16-n_K)",
            "sum_exact_polynomial": polynomial_terms(sum_poly),
            "top_subgroup_index": 19,
            "top_polynomial": polynomial_terms(top_poly),
            "top_matches_c73": True,
            "rational_grid_denominator": 20,
            "rational_grid_points": [str(q) for q in grid],
            "nonnegative_on_rational_grid": grid_nonnegative,
        },
        "claims": {
            "all_20_actual_subgroups_enumerated": True,
            "exact_mobius_inversion": True,
            "direct_65536_support_semantics": True,
            "top_polynomial_matches_c73": True,
            "full_burnside_ring_claimed": False,
            "full_table_of_marks_claimed": False,
            "arithmetic_local_claimed": False,
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "subgroup_count": 20,
        "support_count": 1 << 16,
        "n_H_vector": n_values,
        "top_polynomial": polynomial_terms(top_poly),
        "sum_polynomial": polynomial_terms(sum_poly),
        "nonnegative_on_rational_grid": grid_nonnegative,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
