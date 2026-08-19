#!/usr/bin/env python3
"""Independent projective-rank checker for the C73 reliability certificate."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from hashlib import sha256
import json
from math import comb, factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c73_generation_blocker_reliability_evidence.json"
SOURCES = {
    "c71": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_complement_geometry/results/c71_complement_geometry_evidence.json",
    "c71_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_complement_geometry/C71_PREFREEZE_MANIFEST.json",
    "c72": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_coordinate_core_atlas/results/c72_coordinate_core_atlas_evidence.json",
    "c72_manifest": ROOT / "henon_dynamics/henon_mu3_yukawa_mark_coordinate_core_atlas/C72_PREFREEZE_MANIFEST.json",
}
HASHES = {
    "c71": "a7498081bed5a6f8177825e4d556084bd2421da613ed22835c31e537c49579bc",
    "c71_manifest": "d5ec7bf6bc36cc87dcc2f23c838b0ae7ac997b3c442c0640f486b813fb431715",
    "c72": "8fd56a3441047122765a42c8490a1cb4e84161a68734202cfe0f9852c5d3cb51",
    "c72_manifest": "5e1fbc4029dff7cdd90181d62cb9247d023a6881d549185c2a8e945e09699d6b",
}
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
LABELS = tuple(f"S{index}" for index in range(1, 17))


def canon(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def label_key(label: str) -> int:
    return int(label[1:])


def fraction_text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    raw = args.evidence.read_bytes()
    document = json.loads(raw)
    assert raw == canon(document)
    assert document["schema_id"] == "hcs-c73-generation-blocker-reliability-prefreeze-v1"
    assert document["status"] == "PREFREEZE_G3_PASS"
    assert document["scope_literal"] == FIREWALL
    assert {name: digest(path.read_bytes()) for name, path in SOURCES.items()} == HASHES
    assert document["authority"] == HASHES
    c72 = json.loads(SOURCES["c72"].read_text())
    coordinates = [tuple(row) for row in c72["coordinate_realization"]["coordinates"]]
    pivot = 8

    def determinant(left: tuple[int, int], right: tuple[int, int]) -> int:
        return (left[0] * right[1] - left[1] * right[0]) % 3

    vectors = [(row[0] % 3, row[1] % 3) for row in coordinates]

    def generates(mask: int) -> bool:
        if not mask & (1 << pivot):
            return False
        selected = [vectors[index] for index in range(16)
                    if index != pivot and mask & (1 << index) and vectors[index] != (0, 0)]
        return any(determinant(selected[i], selected[j])
                   for i in range(len(selected)) for j in range(i + 1, len(selected)))

    graph_vertices = [index for index in range(16)
                      if index != pivot and vectors[index] != (0, 0)]
    graph_edges = [(left, right) for position, left in enumerate(graph_vertices)
                   for right in graph_vertices[position + 1:]
                   if determinant(vectors[left], vectors[right])]
    assert len(graph_vertices) == 9 and len(graph_edges) == 25
    # Equal projective directions are the equivalence classes of nonadjacency.
    unassigned = set(graph_vertices)
    blocks = []
    while unassigned:
        seed = min(unassigned)
        block = sorted(index for index in unassigned
                       if determinant(vectors[seed], vectors[index]) == 0)
        blocks.append(block)
        unassigned.difference_update(block)
    blocks.sort(key=lambda block: (len(block), block))
    block_labels = [[LABELS[index] for index in block] for block in blocks]
    assert sorted(map(len, blocks)) == [1, 1, 2, 5]
    expected_direction_sets = {
        frozenset(row["labels"])
        for row in document["generation_structure"]["projective_direction_blocks"]
    }
    assert {frozenset(block) for block in block_labels} == expected_direction_sets
    dummy = [LABELS[index] for index in range(16)
             if index != pivot and vectors[index] == (0, 0)]

    hyperedges = [sorted(["S9", LABELS[left], LABELS[right]], key=label_key)
                  for left, right in graph_edges]
    hyperedges.sort(key=lambda edge: [label_key(label) for label in edge])
    structure = document["generation_structure"]
    assert structure["pivot"] == "S9"
    assert structure["dummy_labels"] == dummy == ["S2", "S5", "S6", "S10", "S13", "S14"]
    assert structure["nonzero_frattini_dummy"] == "S2"
    assert structure["criterion"] == (
        "a support generates 8C iff it contains S9 and meets at least two direction blocks"
    )
    assert structure["base_graph"] == "complete multipartite K_{1,1,2,5}"
    assert structure["base_graph_vertex_count"] == 9
    assert structure["base_graph_edge_count"] == 25
    assert structure["minimal_generation_hypergraph"] == (
        "16-vertex hypergraph with six isolated dummy vertices whose non-isolated part "
        "is the cone over K_{1,1,2,5} with apex S9"
    )
    assert structure["minimal_generating_edges"] == hyperedges
    assert hyperedges == c72["generation_complex"]["minimal_generating_supports"]

    all_mask = (1 << 16) - 1
    destructive = []
    surviving = []
    minimal_blockers = []
    for deletion in range(1 << 16):
        if generates(all_mask ^ deletion):
            surviving.append(deletion)
        else:
            destructive.append(deletion)
            if all(generates(all_mask ^ (deletion ^ (1 << index)))
                   for index in range(16) if deletion & (1 << index)):
                minimal_blockers.append(deletion)
    blocker_labels = [
        [LABELS[index] for index in range(16) if blocker & (1 << index)]
        for blocker in minimal_blockers
    ]
    blocker_labels.sort(key=lambda blocker: (len(blocker), [label_key(label) for label in blocker]))
    blocker = document["blocker_geometry"]
    assert blocker["minimal_blocker_count"] == 5
    assert blocker["minimal_blockers"] == blocker_labels
    assert blocker["minimal_blocker_polynomial_coefficients"] == {"1": 1, "4": 1, "7": 1, "8": 2}
    independent = Counter({0: 1})
    for block in blocks:
        for degree in range(1, len(block) + 1):
            independent[degree] += comb(len(block), degree)
    assert blocker["independent_set_polynomial_coefficients"] == {
        str(degree): independent[degree] for degree in range(max(independent) + 1)
    }
    covers = {9 - degree: coefficient for degree, coefficient in independent.items()}
    assert blocker["vertex_cover_polynomial_coefficients"] == {
        str(degree): covers[degree] for degree in sorted(covers)
    }
    assert blocker["destructive_transversal_formula"] == "T(x)=x(1+x)^15+(1+x)^6 C_Gamma(x)"
    assert blocker["destructive_transversal_count"] == len(destructive) == 35136

    destructive_by_size = Counter(mask.bit_count() for mask in destructive)
    surviving_by_size = Counter(mask.bit_count() for mask in surviving)
    expected_rows = [{
        "deleted_count": size,
        "destructive_count": destructive_by_size[size],
        "surviving_count": surviving_by_size[size],
        "total": comb(16, size),
    } for size in range(17)]
    assert document["deletion_spectrum"] == {
        "rows": expected_rows,
        "destructive_total": len(destructive),
        "surviving_total": len(surviving),
    }
    assert [surviving_by_size[size] for size in range(17)] == [
        1, 15, 105, 455, 1364, 2992, 4950, 6269, 6095,
        4504, 2461, 940, 224, 25, 0, 0, 0,
    ]

    reliability = document["exact_reliability"]
    assert reliability == {
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
    }
    assert document["robustness_parameters"] == {
        "unprotected_worst_case_deletion_tolerance": 0,
        "S9_protected_worst_case_deletion_tolerance": 3,
        "maximum_deletions_with_some_surviving_support": 13,
        "surviving_supports_at_maximum_deletions": 25,
    }

    importance = []
    for index, label in enumerate(LABELS):
        pivotal = 0
        shapley = Fraction(0)
        for mask in range(1 << 16):
            if mask & (1 << index):
                continue
            if not generates(mask) and generates(mask | (1 << index)):
                pivotal += 1
                size = mask.bit_count()
                shapley += Fraction(factorial(size) * factorial(15 - size), factorial(16))
        importance.append({
            "label": label,
            "pivotal_coalition_count": pivotal,
            "uniform_banzhaf_influence": fraction_text(Fraction(pivotal, 2 ** 15)),
            "shapley_value": fraction_text(shapley),
        })
    assert document["coordinate_importance"]["rows"] == importance
    assert document["coordinate_importance"]["definition"] == (
        "uniform Banzhaf influence and Shapley value of the monotone generation game"
    )
    assert sum(Fraction(row["shapley_value"]) for row in importance) == 1
    assert document["hypergraph_symmetry"] == {
        "abstract_hypergraph_automorphism_order": 345600,
        "factorization": "6! * 2! * 2! * 5!",
        "identified_with_core_group_automorphisms": False,
        "identified_with_label_preserving_symmetry": False,
    }
    assert document["claims"] == {
        "blocker_geometry_beyond_C72_coefficient_reversal": True,
        "heterogeneous_reliability_proved": True,
        "three_robustness_notions_distinguished": True,
        "hypergraph_automorphisms_are_core_automorphisms_claimed": False,
        "full_burnside_ring_claimed": False,
        "arithmetic_local_claimed": False,
    }
    print(json.dumps({
        "status": "PASS",
        "base_graph": "K_{1,1,2,5}",
        "minimal_edges": len(hyperedges),
        "minimal_blockers": len(blocker_labels),
        "destructive_transversals": len(destructive),
        "surviving_deletion_sets": len(surviving),
        "shapley_sum": "1",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
