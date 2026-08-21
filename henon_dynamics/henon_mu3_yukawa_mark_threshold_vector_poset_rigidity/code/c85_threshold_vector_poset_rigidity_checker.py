#!/usr/bin/env python3
"""Independent point-set and antichain checker for the C85 receipt.

Unlike the producer, this checker enumerates the twenty subgroups from the
54-point group law and reconstructs every threshold through target-minimal
support antichains.  The producer's closure-class grouping is not imported.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C76 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas"
C80 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_threshold_repair_atlas"
EVIDENCE = PROJECT / "results/c85_threshold_vector_poset_rigidity_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
MODULI = (9, 3, 2)
SUPPORT_COUNT = 1 << 16
AUTHORITY = {
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
    "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
    "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
    "c80": "8d27428b14dbd7354e9c8308ad76b1108e3f551702165833301509cd52de7df5",
    "c80_manifest": "a674116ab6f8f9478130219cc525478525f10f2e42f515e71418a3066e2b229c",
}

Point = tuple[int, int, int]
Subgroup = frozenset[Point]


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def add(left: Point, right: Point) -> Point:
    return tuple((x + y) % modulus for x, y, modulus in zip(left, right, MODULI))  # type: ignore[return-value]


def multiple(coefficient: int, value: Point) -> Point:
    return tuple(coefficient * x % modulus for x, modulus in zip(value, MODULI))  # type: ignore[return-value]


def cyclic(value: Point) -> Subgroup:
    for order in range(1, 55):
        if multiple(order, value) == (0, 0, 0):
            return frozenset(multiple(coefficient, value) for coefficient in range(order))
    raise AssertionError("finite order search failed")


def subgroup_sum(left: Subgroup, right: Subgroup) -> Subgroup:
    return frozenset(add(x, y) for x in left for y in right)


def subgroup_key(subgroup: Subgroup) -> tuple[int, tuple[Point, ...]]:
    return len(subgroup), tuple(sorted(subgroup))


def enumerate_subgroups(points: list[Point]) -> list[Subgroup]:
    zero = frozenset({(0, 0, 0)})
    cyclics = [cyclic(point) for point in points]
    found = {zero}
    queue = deque([zero])
    while queue:
        subgroup = queue.popleft()
        for cyclic_subgroup in cyclics:
            candidate = subgroup_sum(subgroup, cyclic_subgroup)
            if candidate not in found:
                found.add(candidate)
                queue.append(candidate)
    return sorted(found, key=subgroup_key)


def source_paths() -> dict[str, Path]:
    return {
        "c75": C75 / "results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": C75 / "C75_PREFREEZE_MANIFEST.json",
        "c76": C76 / "results/c76_closure_orbit_atlas_evidence.json",
        "c76_manifest": C76 / "C76_PREFREEZE_MANIFEST.json",
        "c80": C80 / "results/c80_threshold_repair_atlas_evidence.json",
        "c80_manifest": C80 / "C80_PREFREEZE_MANIFEST.json",
    }


def build_expected() -> tuple[dict[str, Any], list[int]]:
    paths = source_paths()
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == AUTHORITY
    c75, c76, c80 = (json.loads(raw[name]) for name in ("c75", "c76", "c80"))
    assert all(raw[name] == canonical(value) for name, value in zip(
        ("c75", "c76", "c80"), (c75, c76, c80)
    ))
    assert c75["status"] == c76["status"] == c80["status"] == "PREFREEZE_G3_PASS"
    assert c75["scope_literal"] == c76["scope_literal"] == c80["scope_literal"] == FIREWALL
    assert c75["lifted_symmetry"]["lifted_group_order"] == 11520
    assert c76["source_model"]["effective_label_group_order"] == 1920

    points = list(product(range(9), range(3), range(2)))
    subgroups = enumerate_subgroups(points)
    assert len(subgroups) == 20
    c75_subgroups = [
        frozenset(tuple(point) for point in row["subgroup_points"])
        for row in c75["closure_incidence"]["all_subgroups"]
    ]
    assert subgroups == c75_subgroups
    subgroup_index = {subgroup: index for index, subgroup in enumerate(subgroups)}
    coordinates = [tuple(point) for point in c75["named_coordinate_source"]["coordinates"]]
    cyclics = [cyclic(point) for point in coordinates]
    transition = [
        [subgroup_index[subgroup_sum(subgroup, cyclic_subgroup)] for cyclic_subgroup in cyclics]
        for subgroup in subgroups
    ]
    closure = [subgroup_index[frozenset({(0, 0, 0)})]] * SUPPORT_COUNT
    for support in range(1, SUPPORT_COUNT):
        low = support & -support
        closure[support] = transition[closure[support ^ low]][low.bit_length() - 1]

    inclusion = [
        [int(subgroups[left] <= subgroups[right]) for right in range(20)]
        for left in range(20)
    ]
    minimal_by_target: list[list[int]] = []
    for target in range(20):
        minimal = []
        for support in range(SUPPORT_COUNT):
            if not inclusion[target][closure[support]]:
                continue
            if all(
                not (support & (1 << bit))
                or not inclusion[target][closure[support ^ (1 << bit)]]
                for bit in range(16)
            ):
                minimal.append(support)
        assert minimal
        minimal_by_target.append(minimal)

    profile_vectors: list[tuple[int, ...]] = []
    source_profiles = c80["target_atlas"]["profile_rows"]
    assert len(source_profiles) == SUPPORT_COUNT
    for support in range(SUPPORT_COUNT):
        vector = tuple(
            min((minimal & ~support).bit_count() for minimal in minimal_by_target[target])
            for target in range(20)
        )
        source_row = source_profiles[support]
        assert source_row["retained_mask"] == support
        assert source_row["deletion_mask"] == SUPPORT_COUNT - 1 - support
        assert source_row["thresholds"] == list(vector)
        profile_vectors.append(vector)

    vectors_by_closure: list[set[tuple[int, ...]]] = [set() for _ in range(20)]
    representatives: list[int | None] = [None] * 20
    for support, closed in enumerate(closure):
        vectors_by_closure[closed].add(profile_vectors[support])
        if representatives[closed] is None:
            representatives[closed] = support
    assert all(len(values) == 1 for values in vectors_by_closure)
    vectors = [next(iter(values)) for values in vectors_by_closure]
    assert len(set(vectors)) == 20

    zero_ideals = []
    for closed, vector in enumerate(vectors):
        zero_coordinates = [target for target, value in enumerate(vector) if value == 0]
        principal_ideal = [target for target in range(20) if inclusion[target][closed]]
        assert zero_coordinates == principal_ideal
        zero_ideals.append(zero_coordinates)

    coordinatewise_ge = [
        [int(all(left_value >= right_value for left_value, right_value in zip(vectors[left], vectors[right])))
         for right in range(20)]
        for left in range(20)
    ]
    assert coordinatewise_ge == inclusion
    covers = [
        [left, right]
        for left in range(20)
        for right in range(20)
        if left != right and inclusion[left][right]
        and not any(
            middle not in (left, right)
            and inclusion[left][middle]
            and inclusion[middle][right]
            for middle in range(20)
        )
    ]

    class_counts = Counter(closure)
    c76_counts = {
        int(index): count
        for index, count in c76["closure_atlas"]["support_count_by_closure_index"].items()
    }
    assert dict(sorted(class_counts.items())) == dict(sorted(c76_counts.items()))
    fibre_sizes = [class_counts[index] for index in range(20)]
    fibre_spectrum = Counter(fibre_sizes)
    assert dict(sorted(fibre_spectrum.items())) == {
        32: 6, 64: 4, 96: 4, 192: 2, 1760: 2, 30400: 2,
    }

    subgroup_rows = c75["closure_incidence"]["all_subgroups"]
    vector_rows = [
        {
            "closure_subgroup_index": closed,
            "closure_subgroup_order": subgroup_rows[closed]["subgroup_order"],
            "representative_mask": representatives[closed],
            "threshold_vector": list(vectors[closed]),
            "zero_coordinate_indices": zero_ideals[closed],
            "closure_principal_ideal_indices": zero_ideals[closed],
            "fibre_size": fibre_sizes[closed],
        }
        for closed in range(20)
    ]
    expected: dict[str, Any] = {
        "schema_id": "hcs-c85-threshold-vector-subgroup-poset-rigidity-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": AUTHORITY,
        "definition": {
            "support_convention": "A is the retained 16-label support; D=L\\A",
            "threshold_vector": "v(A)=(tau_H(D)) in C75 subgroup-index order",
            "zero_ideal": "I0(v)={H_i:v_i=0}",
            "coordinate_order": list(range(20)),
            "order_reversal": "H0<=H1 iff v(H0)>=v(H1) coordinatewise",
        },
        "source_model": {
            "group": "Z/9 + Z/3 + Z/2",
            "label_count": 16,
            "support_count": SUPPORT_COUNT,
            "subgroup_count": 20,
            "ambient_lifted_group_order": 11520,
            "effective_label_group_order": 1920,
            "c80_threshold_matrix_sha256": digest(canonical([list(vector) for vector in profile_vectors])),
        },
        "rigidity": {
            "distinct_vector_count": 20,
            "closure_class_count": 20,
            "support_class_indices": closure,
            "vector_rows": vector_rows,
            "fibre_sizes_by_closure_index": fibre_sizes,
            "fibre_spectrum": {str(size): count for size, count in sorted(fibre_spectrum.items())},
            "threshold_vector_depends_only_on_closure": True,
            "zero_ideal_recovers_closure": True,
            "closure_to_vector_bijection": True,
        },
        "poset": {
            "relation_convention": "matrix[i][j]=1 iff H_i is a subgroup of H_j",
            "inclusion_matrix": inclusion,
            "coordinatewise_ge_matrix": coordinatewise_ge,
            "cover_relations": covers,
            "comparable_ordered_pair_count_including_reflexive": sum(map(sum, inclusion)),
            "order_reversing_embedding": True,
        },
        "checks": {
            "all_65536_supports_enumerated": True,
            "exactly_20_threshold_vectors": True,
            "all_20_actual_subgroups_recovered": True,
            "c76_closure_fibres_match": True,
            "zero_coordinate_principal_ideals_match": True,
            "all_400_order_pairs_checked": True,
        },
        "claims": {
            "arithmetic_local_claimed": False,
            "full_burnside_ring_claimed": False,
            "full_table_of_marks_claimed": False,
            "hilbert_polya_operator_claimed": False,
        },
    }
    return expected, [len(values) for values in minimal_by_target]


def validate_evidence_path(
    path: Path,
    expected: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], list[int]]:
    raw = path.read_bytes()
    evidence = json.loads(raw)
    assert raw == canonical(evidence)
    if expected is None:
        expected, minimal_counts = build_expected()
    else:
        minimal_counts = []
    assert evidence == expected
    return evidence, minimal_counts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    evidence, minimal_counts = validate_evidence_path(args.evidence)
    print(json.dumps({
        "status": "C85_INDEPENDENT_CHECK_PASS",
        "support_count": SUPPORT_COUNT,
        "distinct_vector_count": evidence["rigidity"]["distinct_vector_count"],
        "fibre_spectrum": evidence["rigidity"]["fibre_spectrum"],
        "cover_relation_count": len(evidence["poset"]["cover_relations"]),
        "minimal_support_counts": minimal_counts,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
