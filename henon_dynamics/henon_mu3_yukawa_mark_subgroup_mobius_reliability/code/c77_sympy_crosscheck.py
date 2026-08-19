#!/usr/bin/env python3
"""Independent SymPy cross-check for the C77 subgroup Möbius certificate.

The checker rebuilds the twenty subgroup poset from the source-bound C75
coordinates, computes its exact incidence Möbius function, and compares
Möbius-inverted closure probabilities with a direct enumeration of all
``2**16`` retained-label supports.
"""

from __future__ import annotations

from collections import Counter
from math import comb
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C76 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas"
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C73 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability"
EVIDENCE = PROJECT / "results/c77_subgroup_mobius_reliability_evidence.json"

FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
C76_EVIDENCE_SHA256 = "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94"
C76_MANIFEST_SHA256 = "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5"
C75_HASHES = {
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
}
C76_HASHES = {"c76": C76_EVIDENCE_SHA256, "c76_manifest": C76_MANIFEST_SHA256}
C73_HASHES = {
    "c73": "e91c8e6dcf1de5362b1a052ada83eb758b2c2d75520c1e8bdbd37ab055c725e5",
    "c73_manifest": "a50b5707d36f8b94b463e6c5fc4b5b7f6d6df7eb5e87d70bfc82d2b1a653cd8d",
}

Q = sp.Symbol("q")
ZERO = (0, 0, 0)
MODULI = (9, 3, 2)
TOP_COEFFICIENTS = {"0": 1, "1": -1, "4": -1, "5": 1, "7": -1,
                    "8": -1, "9": 5, "10": -3}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((x + y) % modulus for x, y, modulus in zip(left, right, MODULI))


def multiple(coefficient: int, value: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(coefficient * x % modulus for x, modulus in zip(value, MODULI))


def point_order(value: tuple[int, ...]) -> int:
    for candidate in range(1, 55):
        if multiple(candidate, value) == ZERO:
            return candidate
    raise AssertionError("finite point order not found")


def cyclic_subgroup(value: tuple[int, ...]) -> frozenset[tuple[int, ...]]:
    return frozenset(multiple(k, value) for k in range(point_order(value)))


def extend(left: frozenset[tuple[int, ...]], right: frozenset[tuple[int, ...]]) -> frozenset[tuple[int, ...]]:
    return frozenset(add(x, y) for x in left for y in right)


def coefficient_map(poly: sp.Expr) -> dict[str, int]:
    result: dict[str, int] = {}
    for powers, coefficient in sp.Poly(sp.expand(poly), Q).terms():
        value = int(coefficient)
        if value:
            result[str(powers[0])] = value
    return result


def polynomial(value: Any) -> sp.Expr:
    """Decode a producer polynomial stored as text, coefficients, or a wrapper."""
    if isinstance(value, sp.Basic):
        return sp.expand(value)
    if isinstance(value, str):
        text = value.replace("^", "**")
        return sp.expand(sp.sympify(text, locals={"q": Q}))
    if isinstance(value, (int, float)):
        return sp.Integer(value)
    if isinstance(value, list):
        return sp.expand(sum(sp.Integer(coefficient) * Q ** index
                             for index, coefficient in enumerate(value)))
    if isinstance(value, dict):
        for wrapper in ("polynomial", "expanded", "expression", "coefficients"):
            if wrapper in value:
                return polynomial(value[wrapper])
        return sp.expand(sum(sp.Integer(coefficient) * Q ** int(power)
                             for power, coefficient in value.items()))
    raise TypeError(f"unsupported polynomial encoding: {type(value)!r}")


def as_int_map(value: Any) -> dict[str, int]:
    if isinstance(value, dict):
        for wrapper in ("coefficients", "expanded", "polynomial"):
            if wrapper in value:
                return coefficient_map(polynomial(value[wrapper]))
        return {str(key): int(number) for key, number in value.items() if int(number)}
    return coefficient_map(polynomial(value))


def unwrap_matrix(value: Any) -> list[list[int]]:
    if isinstance(value, dict):
        for key in ("matrix", "rows", "values"):
            if key in value:
                return unwrap_matrix(value[key])
    assert isinstance(value, list) and len(value) == 20
    matrix = [list(map(int, row)) for row in value]
    assert all(len(row) == 20 for row in matrix)
    return matrix


def normalize_counts(value: Any, size: int = 20) -> list[int]:
    if isinstance(value, dict):
        if "counts" in value:
            return normalize_counts(value["counts"], size)
        return [int(value.get(str(index), value.get(index, 0))) for index in range(size)]
    return [int(number) for number in value]


def assert_equal_if_present(container: dict[str, Any], keys: tuple[str, ...], expected: Any) -> None:
    for key in keys:
        if key in container:
            actual = container[key]
            if isinstance(expected, sp.Basic):
                assert sp.expand(polynomial(actual) - expected) == 0, (key, actual, expected)
            elif isinstance(expected, dict):
                assert as_int_map(actual) == expected, (key, actual, expected)
            else:
                assert actual == expected, (key, actual, expected)
            return


def main() -> None:
    c76_raw = (C76 / "results/c76_closure_orbit_atlas_evidence.json").read_bytes()
    c76_manifest_raw = (C76 / "C76_PREFREEZE_MANIFEST.json").read_bytes()
    assert digest(c76_raw) == C76_EVIDENCE_SHA256
    assert digest(c76_manifest_raw) == C76_MANIFEST_SHA256
    c76 = json.loads(c76_raw)
    c76_manifest = json.loads(c76_manifest_raw)
    assert c76_raw == canonical(c76)
    assert c76["status"] == "PREFREEZE_G3_PASS"
    assert c76["scope_literal"] == FIREWALL
    assert c76["authority"].get("c75") == C75_HASHES["c75"]
    assert c76["authority"].get("c75_manifest") == C75_HASHES["c75_manifest"]
    assert c76_manifest["scope_literal"] == FIREWALL

    c75_raw = (C75 / "results/c75_closure_incidence_lift_evidence.json").read_bytes()
    c75_manifest_raw = (C75 / "C75_PREFREEZE_MANIFEST.json").read_bytes()
    assert digest(c75_raw) == C75_HASHES["c75"]
    assert digest(c75_manifest_raw) == C75_HASHES["c75_manifest"]
    c75 = json.loads(c75_raw)
    assert c75["status"] == "PREFREEZE_G3_PASS"
    assert c75["scope_literal"] == FIREWALL
    coordinates = [tuple(row) for row in c75["named_coordinate_source"]["coordinates"]]
    assert len(coordinates) == 16
    c73_raw = (C73 / "results/c73_generation_blocker_reliability_evidence.json").read_bytes()
    c73_manifest_raw = (C73 / "C73_PREFREEZE_MANIFEST.json").read_bytes()
    assert digest(c73_raw) == C73_HASHES["c73"]
    assert digest(c73_manifest_raw) == C73_HASHES["c73_manifest"]
    c73 = json.loads(c73_raw)
    assert c73["status"] == "PREFREEZE_G3_PASS"
    assert c73["scope_literal"] == FIREWALL
    assert c73["exact_reliability"]["homogeneous_expanded_coefficients"] == TOP_COEFFICIENTS

    evidence_raw = EVIDENCE.read_bytes()
    evidence = json.loads(evidence_raw)
    assert evidence_raw == canonical(evidence)
    assert evidence["schema_id"] == "hcs-c77-subgroup-mobius-reliability-prefreeze-v1"
    assert evidence["status"] == "PREFREEZE_G3_PASS"
    assert evidence["scope_literal"] == FIREWALL
    for name, expected_hash in C76_HASHES.items():
        assert evidence["authority"].get(name) == expected_hash
    for name, expected_hash in C75_HASHES.items():
        assert evidence["authority"].get(name) == expected_hash
    for name, expected_hash in C73_HASHES.items():
        assert evidence["authority"].get(name) == expected_hash

    rows = c75["closure_incidence"]["all_subgroups"]
    assert len(rows) == 20
    subgroups = [frozenset(tuple(point) for point in row["subgroup_points"]) for row in rows]
    assert len(set(subgroups)) == 20
    subgroup_index = {subgroup: index for index, subgroup in enumerate(subgroups)}
    cyclics = [cyclic_subgroup(point) for point in coordinates]
    n_values = [sum(cyclic <= subgroup for cyclic in cyclics) for subgroup in subgroups]
    assert n_values == [5, 6, 7, 6, 7, 6, 8, 7, 8, 7, 11, 7, 7, 8, 12, 8, 8, 9, 15, 16]
    subgroup_poset = evidence["subgroup_poset"]
    assert subgroup_poset["subgroup_count"] == 20
    if "n_H_vector" in subgroup_poset:
        assert list(map(int, subgroup_poset["n_H_vector"])) == n_values
    inclusion = [
        [int(subgroups[left] <= subgroups[right]) for right in range(20)]
        for left in range(20)
    ]
    if "inclusion_matrix" in subgroup_poset:
        assert subgroup_poset["inclusion_matrix"] == inclusion

    # Incidence Möbius function: rows are K, columns are H.
    order_indices = sorted(range(20), key=lambda index: (len(subgroups[index]), index))
    mu = [[0 for _ in range(20)] for _ in range(20)]
    for h in order_indices:
        mu[h][h] = 1
        for k in order_indices:
            if k == h or not subgroups[k] < subgroups[h]:
                continue
            mu[k][h] = -sum(mu[k][j] for j in order_indices
                             if subgroups[k] <= subgroups[j] < subgroups[h])
    for k in range(20):
        for h in range(20):
            if subgroups[k] <= subgroups[h]:
                assert sum(mu[k][j] for j in range(20)
                           if subgroups[k] <= subgroups[j] <= subgroups[h]) == (1 if k == h else 0)
            else:
                assert mu[k][h] == 0

    mobius_section = evidence["mobius_matrix"]
    stored_mu = unwrap_matrix(mobius_section)
    assert stored_mu == mu

    # Generate every closure and retain both total and cardinality-resolved counts.
    closure_of = [subgroup_index[frozenset({ZERO})]] * (1 << 16)
    for mask in range(1, 1 << 16):
        low = mask & -mask
        label = low.bit_length() - 1
        closure_of[mask] = subgroup_index[extend(subgroups[closure_of[mask ^ low]], cyclics[label])]
    direct_counts = Counter(closure_of)
    direct_by_cardinality = [Counter() for _ in range(20)]
    retained_totals = [0] * 17
    for mask, subgroup in enumerate(closure_of):
        cardinality = mask.bit_count()
        retained_totals[cardinality] += 1
        direct_by_cardinality[subgroup][cardinality] += 1
    assert retained_totals == [comb(16, cardinality) for cardinality in range(17)]
    assert sum(direct_counts.values()) == 1 << 16

    direct_section = evidence["direct_enumeration"]
    assert direct_section["support_count"] == 1 << 16
    stored_total_counts = normalize_counts(direct_section["generated_support_count_by_subgroup"])
    assert stored_total_counts == [direct_counts[index] for index in range(20)]
    retained_key = ("retained_cardinality_totals"
                    if "retained_cardinality_totals" in direct_section
                    else "retained_cardinality_total")
    stored_retained_totals = normalize_counts(direct_section[retained_key], 17)
    assert stored_retained_totals == retained_totals

    subgroup_rows = subgroup_poset["rows"]
    assert len(subgroup_rows) == 20
    q = Q
    exact_polynomials: list[sp.Expr] = []
    leq_polynomials: list[sp.Expr] = []
    for index, row in enumerate(subgroup_rows):
        assert int(row.get("index", row.get("subgroup_index"))) == index
        assert int(row["subgroup_order"]) == len(subgroups[index])
        if "subgroup_points" in row:
            assert frozenset(tuple(point) for point in row["subgroup_points"]) == subgroups[index]
        assert int(row["n_H"]) == n_values[index]
        leq = q ** (16 - n_values[index])
        exact = sp.expand(sum(mu[k][index] * q ** (16 - n_values[k])
                              for k in range(20) if mu[k][index]))
        direct = sp.expand(sum(direct_by_cardinality[index][cardinality]
                               * q ** (16 - cardinality) * (1 - q) ** cardinality
                               for cardinality in range(17)))
        assert sp.expand(exact - direct) == 0
        leq_polynomials.append(leq)
        exact_polynomials.append(exact)
        assert_equal_if_present(
            row, ("P_leq", "p_leq", "P_leq_polynomial", "at_most_polynomial"), leq
        )
        assert_equal_if_present(
            row, ("P_eq", "p_eq", "P_eq_polynomial", "exact_polynomial"), exact
        )
        if "direct_support_count" in row:
            assert int(row["direct_support_count"]) == direct_counts[index]
        if "direct_by_retained_cardinality" in row:
            assert normalize_counts(row["direct_by_retained_cardinality"], 17) == [
                direct_by_cardinality[index][cardinality] for cardinality in range(17)
            ]

    assert sp.expand(sum(exact_polynomials)) == 1
    reliability = evidence["reliability"]
    assert_equal_if_present(reliability, ("sum_polynomial", "sum_exact_polynomial"), sp.Integer(1))
    top = exact_polynomials[19]
    assert coefficient_map(top) == TOP_COEFFICIENTS
    assert_equal_if_present(reliability, ("top_polynomial", "top_exact_polynomial"), top)
    if "top_matches_c73" in reliability:
        assert reliability["top_matches_c73"] is True
    # Optional grid/nonnegativity certificate: independently evaluate all rows.
    grid_key = ("rational_grid" if "rational_grid" in reliability
                else "rational_grid_points" if "rational_grid_points" in reliability
                else None)
    if grid_key is not None:
        if "rational_grid_denominator" in reliability:
            denominator = int(reliability["rational_grid_denominator"])
            assert denominator > 0
            assert reliability[grid_key] == [str(sp.Rational(index, denominator))
                                              for index in range(denominator + 1)]
        for point in reliability[grid_key]:
            value = sp.Rational(point["q"] if isinstance(point, dict) else point)
            assert all(sp.N(poly.subs(q, value)) >= -sp.Rational(1, 10**12)
                       for poly in exact_polynomials)
    for key in ("nonnegative", "nonnegative_on_rational_grid"):
        if key in reliability:
            assert reliability[key] is True
    claims = evidence["claims"]
    assert claims["all_20_actual_subgroups_enumerated"] is True
    assert claims["exact_mobius_inversion"] is True
    assert claims["direct_65536_support_semantics"] is True
    assert claims["top_polynomial_matches_c73"] is True

    print(json.dumps({
        "status": "SYMPY_CROSSCHECK_PASS",
        "c76_evidence_sha256": C76_EVIDENCE_SHA256,
        "c76_manifest_sha256": C76_MANIFEST_SHA256,
        "subgroup_count": 20,
        "support_count": 1 << 16,
        "mobius_matrix_verified": True,
        "sum_polynomial": "1",
        "top_polynomial_coefficients": TOP_COEFFICIENTS,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
