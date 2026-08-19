#!/usr/bin/env python3
"""Produce the C73 blocker geometry and exact erasure-reliability certificate."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C71 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_complement_geometry"
C72 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_coordinate_core_atlas"
OUT = PROJECT / "results/c73_generation_blocker_reliability_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
HASHES = {
    "c71": "a7498081bed5a6f8177825e4d556084bd2421da613ed22835c31e537c49579bc",
    "c71_manifest": "d5ec7bf6bc36cc87dcc2f23c838b0ae7ac997b3c442c0640f486b813fb431715",
    "c72": "8fd56a3441047122765a42c8490a1cb4e84161a68734202cfe0f9852c5d3cb51",
    "c72_manifest": "5e1fbc4029dff7cdd90181d62cb9247d023a6881d549185c2a8e945e09699d6b",
}
LABELS = tuple(f"S{index}" for index in range(1, 17))


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def label_key(label: str) -> int:
    return int(label[1:])


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def projective_direction(vector: tuple[int, int]) -> tuple[int, int] | None:
    left, right = (vector[0] % 3, vector[1] % 3)
    if left == right == 0:
        return None
    if left:
        inverse = 1 if left == 1 else 2
        return (1, right * inverse % 3)
    return (0, 1)


def polynomial_product(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def main() -> None:
    paths = {
        "c71": C71 / "results/c71_complement_geometry_evidence.json",
        "c71_manifest": C71 / "C71_PREFREEZE_MANIFEST.json",
        "c72": C72 / "results/c72_coordinate_core_atlas_evidence.json",
        "c72_manifest": C72 / "C72_PREFREEZE_MANIFEST.json",
    }
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == HASHES
    c71 = json.loads(raw["c71"])
    c72 = json.loads(raw["c72"])
    assert c71["status"] == c72["status"] == "PREFREEZE_G3_PASS"
    assert c71["scope_literal"] == c72["scope_literal"] == FIREWALL
    assert c72["core"]["invariant_factors"] == [3, 18]

    coordinates = [tuple(row) for row in c72["coordinate_realization"]["coordinates"]]
    pivot_index = 8
    assert coordinates[pivot_index] == (0, 0, 1)
    assert all(row[2] == 0 for index, row in enumerate(coordinates) if index != pivot_index)
    blocks: dict[tuple[int, int], list[str]] = {}
    dummy_labels = []
    for index, coordinate in enumerate(coordinates):
        if index == pivot_index:
            continue
        direction = projective_direction(coordinate[:2])
        if direction is None:
            dummy_labels.append(LABELS[index])
        else:
            blocks.setdefault(direction, []).append(LABELS[index])
    direction_order = ((1, 0), (1, 1), (1, 2), (0, 1))
    direction_blocks = [blocks[direction] for direction in direction_order]
    assert direction_blocks == [
        ["S1"], ["S16"], ["S7", "S15"],
        ["S3", "S4", "S8", "S11", "S12"],
    ]
    assert dummy_labels == ["S2", "S5", "S6", "S10", "S13", "S14"]

    label_to_block = {
        label: block_index
        for block_index, block in enumerate(direction_blocks)
        for label in block
    }

    def generates(mask: int) -> bool:
        if not mask & (1 << pivot_index):
            return False
        hit = {
            label_to_block[label]
            for index, label in enumerate(LABELS)
            if mask & (1 << index) and label in label_to_block
        }
        return len(hit) >= 2

    minimal_edges = []
    for first in range(4):
        for second in range(first + 1, 4):
            for left in direction_blocks[first]:
                for right in direction_blocks[second]:
                    minimal_edges.append(sorted([left, right, "S9"], key=label_key))
    minimal_edges.sort(key=lambda edge: [label_key(label) for label in edge])
    assert len(minimal_edges) == 25
    assert minimal_edges == c72["generation_complex"]["minimal_generating_supports"]

    minimal_blockers = [["S9"]]
    for surviving_block in range(4):
        blocker = sorted(
            [label for block_index, block in enumerate(direction_blocks)
             if block_index != surviving_block for label in block],
            key=label_key,
        )
        minimal_blockers.append(blocker)
    minimal_blockers.sort(key=lambda blocker: (len(blocker), [label_key(label) for label in blocker]))
    assert [len(blocker) for blocker in minimal_blockers] == [1, 4, 7, 8, 8]

    deletion_rows = []
    destructive_masks = []
    surviving_masks = []
    for deletion_mask in range(1 << 16):
        retained_mask = ((1 << 16) - 1) ^ deletion_mask
        if generates(retained_mask):
            surviving_masks.append(deletion_mask)
        else:
            destructive_masks.append(deletion_mask)
    destructive_by_size = Counter(mask.bit_count() for mask in destructive_masks)
    surviving_by_size = Counter(mask.bit_count() for mask in surviving_masks)
    for size in range(17):
        deletion_rows.append({
            "deleted_count": size,
            "destructive_count": destructive_by_size[size],
            "surviving_count": surviving_by_size[size],
            "total": comb(16, size),
        })
        assert destructive_by_size[size] + surviving_by_size[size] == comb(16, size)
    assert len(destructive_masks) == 35136
    assert len(surviving_masks) == 30400

    # I_Gamma(z)=1+sum_j((1+z)^|B_j|-1), then reverse coefficients for covers.
    independent = [1]
    for size in map(len, direction_blocks):
        if len(independent) <= size:
            independent.extend([0] * (size + 1 - len(independent)))
        for degree in range(1, size + 1):
            independent[degree] += comb(size, degree)
    assert independent == [1, 9, 11, 10, 5, 1]
    vertex_cover = [0] * 10
    for degree, coefficient in enumerate(independent):
        vertex_cover[9 - degree] = coefficient
    assert vertex_cover == [0, 0, 0, 0, 1, 5, 10, 11, 9, 1]
    destructive_polynomial = [0] * 17
    for degree in range(16):
        destructive_polynomial[degree + 1] += comb(15, degree)
    dummy_factor = [comb(6, degree) for degree in range(7)]
    cover_with_dummy = polynomial_product(vertex_cover, dummy_factor)
    destructive_polynomial = [
        destructive_polynomial[degree]
        + (cover_with_dummy[degree] if degree < len(cover_with_dummy) else 0)
        for degree in range(17)
    ]
    assert destructive_polynomial == [destructive_by_size[size] for size in range(17)]

    importance_rows = []
    n = 16
    for index, label in enumerate(LABELS):
        pivotal = 0
        shapley = Fraction(0)
        for mask in range(1 << n):
            if mask & (1 << index):
                continue
            if not generates(mask) and generates(mask | (1 << index)):
                pivotal += 1
                size = mask.bit_count()
                shapley += Fraction(factorial(size) * factorial(n - size - 1), factorial(n))
        importance_rows.append({
            "label": label,
            "pivotal_coalition_count": pivotal,
            "uniform_banzhaf_influence": fraction_text(Fraction(pivotal, 2 ** 15)),
            "shapley_value": fraction_text(shapley),
        })
    by_label = {row["label"]: row for row in importance_rows}
    expected_orbits = [
        (["S9"], "475/512", "271/360"),
        (["S1", "S16"], "35/512", "61/1260"),
        (["S7", "S15"], "33/512", "2/45"),
        (["S3", "S4", "S8", "S11", "S12"], "5/512", "31/2520"),
        (dummy_labels, "0", "0"),
    ]
    for orbit, banzhaf, shapley in expected_orbits:
        assert all(by_label[label]["uniform_banzhaf_influence"] == banzhaf for label in orbit)
        assert all(by_label[label]["shapley_value"] == shapley for label in orbit)
    assert sum(Fraction(row["shapley_value"]) for row in importance_rows) == 1

    result: dict[str, Any] = {
        "schema_id": "hcs-c73-generation-blocker-reliability-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": HASHES,
        "type_order": list(LABELS),
        "generation_structure": {
            "pivot": "S9",
            "projective_direction_blocks": [
                {"direction": f"[{direction[0]}:{direction[1]}]", "labels": block}
                for direction, block in zip(direction_order, direction_blocks)
            ],
            "dummy_labels": dummy_labels,
            "nonzero_frattini_dummy": "S2",
            "criterion": "a support generates 8C iff it contains S9 and meets at least two direction blocks",
            "base_graph": "complete multipartite K_{1,1,2,5}",
            "base_graph_vertex_count": 9,
            "base_graph_edge_count": len(minimal_edges),
            "minimal_generation_hypergraph":
                "16-vertex hypergraph with six isolated dummy vertices whose non-isolated part "
                "is the cone over K_{1,1,2,5} with apex S9",
            "minimal_generating_edges": minimal_edges,
        },
        "blocker_geometry": {
            "minimal_blocker_count": len(minimal_blockers),
            "minimal_blockers": minimal_blockers,
            "minimal_blocker_polynomial_coefficients": {"1": 1, "4": 1, "7": 1, "8": 2},
            "independent_set_polynomial_coefficients": {
                str(degree): coefficient for degree, coefficient in enumerate(independent)
            },
            "vertex_cover_polynomial_coefficients": {
                str(degree): coefficient for degree, coefficient in enumerate(vertex_cover)
                if coefficient
            },
            "destructive_transversal_formula": "T(x)=x(1+x)^15+(1+x)^6 C_Gamma(x)",
            "destructive_transversal_count": len(destructive_masks),
        },
        "deletion_spectrum": {
            "rows": deletion_rows,
            "destructive_total": len(destructive_masks),
            "surviving_total": len(surviving_masks),
        },
        "exact_reliability": {
            "homogeneous_deletion_probability_variable": "q",
            "homogeneous_factorization": "R(q)=(1-q)(1-q^4-q^7-2q^8+3q^9)",
            "homogeneous_expanded_coefficients": {
                "0": 1, "1": -1, "4": -1, "5": 1,
                "7": -1, "8": -1, "9": 5, "10": -3,
            },
            "heterogeneous_direction_failure_formula":
                "R=(1-q9)(1-sum_j product_{k!=j} Q_k+3 product_j Q_j)",
            "Q_definition": "Q_j is the product of deletion probabilities in direction block j",
            "dummy_probabilities_cancel": True,
        },
        "robustness_parameters": {
            "unprotected_worst_case_deletion_tolerance": 0,
            "S9_protected_worst_case_deletion_tolerance": 3,
            "maximum_deletions_with_some_surviving_support": 13,
            "surviving_supports_at_maximum_deletions": 25,
        },
        "coordinate_importance": {
            "definition": "uniform Banzhaf influence and Shapley value of the monotone generation game",
            "rows": importance_rows,
            "symmetry_orbits": [orbit for orbit, _, _ in expected_orbits],
        },
        "hypergraph_symmetry": {
            "abstract_hypergraph_automorphism_order": 345600,
            "factorization": "6! * 2! * 2! * 5!",
            "identified_with_core_group_automorphisms": False,
            "identified_with_label_preserving_symmetry": False,
        },
        "claims": {
            "blocker_geometry_beyond_C72_coefficient_reversal": True,
            "heterogeneous_reliability_proved": True,
            "three_robustness_notions_distinguished": True,
            "hypergraph_automorphisms_are_core_automorphisms_claimed": False,
            "full_burnside_ring_claimed": False,
            "arithmetic_local_claimed": False,
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "direction_block_sizes": list(map(len, direction_blocks)),
        "minimal_generation_edges": len(minimal_edges),
        "minimal_blockers": len(minimal_blockers),
        "destructive_transversals": len(destructive_masks),
        "surviving_deletion_sets": len(surviving_masks),
        "robustness": result["robustness_parameters"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
