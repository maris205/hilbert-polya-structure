#!/usr/bin/env python3
"""Produce the C97 effective-group quotient of ordered first-passage pairs."""
from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C76 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas"
C88 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_subgroup_first_passage_atlas"
C90 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_first_passage_joint_coupling"
C93 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_first_passage_orbit_quotient"
OUT = PROJECT / "results/c97_pair_orbit_quotient_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
N = 16
TARGETS = 20
SUPPORTS = 1 << N
GENERATOR_NAMES = (
    "zero_5_cycle",
    "zero_transposition",
    "fiber_F3_transposition",
    "fiber_F9_transposition",
    "ambient_s",
)
AUTHORITY = {
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
    "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
    "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
    "c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b",
    "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5",
    "c90": "c457a267b2621c71f7f5ad810ce9dec41aacfe25de3e843fab1398be75571978",
    "c90_manifest": "4233c3b8e60a09729ce1befdb68e28566bde87042fef3059f8ff98cac6ebb737",
    "c93": "4104f181b88d83666c9fcff814a7029a148c498e6393ad181c60fe5133adb9fe",
    "c93_manifest": "a60e0855482e205b0174281c4a20b8f86d2eb9531a3f980cb76d92fcfb77c608",
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(N))


def apply_mask(mask: int, permutation: tuple[int, ...]) -> int:
    image = 0
    for index in range(N):
        if mask & (1 << index):
            image |= 1 << permutation[index]
    return image


def generated_group(generators: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    identity = tuple(range(N))
    group = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            product = compose(current, generator)
            if product not in group:
                group.add(product)
                queue.append(product)
    return sorted(group)


def source_paths() -> dict[str, Path]:
    return {
        "c75": C75 / "results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": C75 / "C75_PREFREEZE_MANIFEST.json",
        "c76": C76 / "results/c76_closure_orbit_atlas_evidence.json",
        "c76_manifest": C76 / "C76_PREFREEZE_MANIFEST.json",
        "c88": C88 / "results/c88_subgroup_first_passage_atlas_evidence.json",
        "c88_manifest": C88 / "C88_PREFREEZE_MANIFEST.json",
        "c90": C90 / "results/c90_joint_first_passage_evidence.json",
        "c90_manifest": C90 / "C90_PREFREEZE_MANIFEST.json",
        "c93": C93 / "results/c93_first_passage_orbit_quotient_evidence.json",
        "c93_manifest": C93 / "C93_PREFREEZE_MANIFEST.json",
    }


def load_sources() -> tuple[dict[str, Any], ...]:
    raw = {name: path.read_bytes() for name, path in source_paths().items()}
    assert {name: digest(value) for name, value in raw.items()} == AUTHORITY
    data = tuple(json.loads(raw[name]) for name in ("c75", "c76", "c88", "c90", "c93"))
    assert all(raw[name] == canonical(json.loads(raw[name])) for name in ("c75", "c76", "c88", "c90", "c93"))
    assert all(item["scope_literal"] == FIREWALL for item in data)
    assert all(item["status"] == "PREFREEZE_G3_PASS" for item in data)
    return data


def joint_signature(row: dict[str, Any]) -> bytes:
    payload = {
        "joint_survival_permutation_counts": row["joint_survival_permutation_counts"],
        "joint_survival_probabilities": row["joint_survival_probabilities"],
        "mixed_raw_moments": row["mixed_raw_moments"],
        "covariance": row["covariance"],
    }
    return canonical(payload)


def main() -> None:
    c75, c76, c88, c90, c93 = load_sources()
    rows88 = c88["first_passage_atlas"]["target_rows"]
    inclusion = c88["target_poset"]["inclusion_matrix"]
    assert len(rows88) == TARGETS

    hits: list[list[bool]] = []
    for row in rows88:
        packed = bytes.fromhex(row["subset_hit_bitset_hex"])
        hits.append([bool(packed[support // 8] & (1 << (support % 8))) for support in range(SUPPORTS)])

    # Every support has one exact closure target.  It is the unique contained
    # target of maximal order among its C88 hit indicators.
    closure_of: list[int] = []
    for support in range(SUPPORTS):
        candidates = [target for target in range(TARGETS) if hits[target][support]]
        maximal_order = max(rows88[target]["target_subgroup_order"] for target in candidates)
        maximal = [target for target in candidates if rows88[target]["target_subgroup_order"] == maximal_order]
        assert len(maximal) == 1
        closure_of.append(maximal[0])
    representatives = [next(support for support, target in enumerate(closure_of) if target == wanted) for wanted in range(TARGETS)]

    named = {row["name"]: tuple(row["label_permutation"]) for row in c75["lifted_symmetry"]["generators"]}
    generators = [named[name] for name in GENERATOR_NAMES]
    label_group = generated_group(generators)
    assert len(label_group) == 1920
    assert c76["source_model"]["effective_label_group_order"] == 1920

    target_maps: list[tuple[int, ...]] = []
    for permutation in label_group:
        target_map = tuple(closure_of[apply_mask(representatives[target], permutation)] for target in range(TARGETS))
        assert sorted(target_map) == list(range(TARGETS))
        target_maps.append(target_map)

    # The five named generators preserve both the C88 containment upsets and
    # the target inclusion relation.  Generation then gives full equivariance.
    for generator in generators:
        target_map = target_maps[label_group.index(generator)]
        for target in range(TARGETS):
            for support in range(SUPPORTS):
                assert hits[target][support] == hits[target_map[target]][apply_mask(support, generator)]
        for left in range(TARGETS):
            for right in range(TARGETS):
                assert bool(inclusion[left][right]) == bool(inclusion[target_map[left]][target_map[right]])

    source_pairs = {
        (row["lower_target_index"], row["upper_target_index"]): row
        for row in c90["joint_atlas"]["pair_rows"]
    }
    assert len(source_pairs) == TARGETS * TARGETS

    unseen = {(left, right) for left in range(TARGETS) for right in range(TARGETS)}
    pair_orbits: list[list[tuple[int, int]]] = []
    while unseen:
        representative = min(unseen)
        orbit = sorted({(target_map[representative[0]], target_map[representative[1]]) for target_map in target_maps})
        unseen -= set(orbit)
        pair_orbits.append(orbit)
    pair_orbits.sort(key=lambda orbit: orbit[0])
    orbit_index = {pair: index for index, orbit in enumerate(pair_orbits) for pair in orbit}
    assert len(orbit_index) == TARGETS * TARGETS

    c93_orbits = [row["target_orbit"] for row in c93["target_orbit_atlas"]["rows"]]
    derived_target_orbits: list[list[int]] = []
    pending = set(range(TARGETS))
    while pending:
        target = min(pending)
        orbit = sorted({target_map[target] for target_map in target_maps})
        pending -= set(orbit)
        derived_target_orbits.append(orbit)
    assert derived_target_orbits == c93_orbits

    def relation(pair: tuple[int, int]) -> str:
        left, right = pair
        if left == right:
            return "diagonal"
        if inclusion[left][right]:
            return "forward_comparable"
        if inclusion[right][left]:
            return "reverse_comparable"
        return "incomparable"

    rows_out: list[dict[str, Any]] = []
    for index, orbit in enumerate(pair_orbits):
        representative = orbit[0]
        signature = joint_signature(source_pairs[representative])
        assert all(joint_signature(source_pairs[pair]) == signature for pair in orbit)
        relation_type = relation(representative)
        assert all(relation(pair) == relation_type for pair in orbit)
        size = len(orbit)
        assert 1920 % size == 0
        rows_out.append({
            "pair_orbit_index": index,
            "representative_ordered_pair": list(representative),
            "ordered_target_pairs": [list(pair) for pair in orbit],
            "orbit_size": size,
            "stabilizer_order_in_effective_label_group": 1920 // size,
            "relation_type": relation_type,
            "transpose_orbit_index": orbit_index[(representative[1], representative[0])],
            "joint_law_sha256": digest(signature),
            "representative_covariance": source_pairs[representative]["covariance"],
        })

    assert all(rows_out[row["transpose_orbit_index"]]["transpose_orbit_index"] == row["pair_orbit_index"] for row in rows_out)
    fixed_pair_sum = sum(sum(1 for target in range(TARGETS) if target_map[target] == target) ** 2 for target_map in target_maps)
    assert fixed_pair_sum == len(label_group) * len(pair_orbits)

    result: dict[str, Any] = {
        "schema_id": "hcs-c97-first-passage-pair-orbit-quotient-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": AUTHORITY,
        "definition": {
            "effective_group": "faithful order-1920 action on the sixteen frozen labels",
            "ambient_lift_order": 11520,
            "ordered_pair_action": "g.(i,j)=(g.i,g.j) under the diagonal induced target action",
            "joint_law_transport": "the complete C90 joint-survival, mixed-moment, and covariance payload is constant on each ordered-pair orbit",
            "burnside_identity": "number of ordered-pair orbits is |G|^-1 sum_g Fix_targets(g)^2",
            "transpose": "(i,j) maps to (j,i), inducing an involution on pair orbits",
        },
        "source_model": {
            "group": "Z/9 + Z/3 + Z/2",
            "label_count": N,
            "support_count": SUPPORTS,
            "target_count": TARGETS,
            "ordered_target_pair_count": TARGETS * TARGETS,
            "effective_label_group_order": len(label_group),
            "ambient_lifted_group_order": 11520,
            "generator_names": list(GENERATOR_NAMES),
        },
        "pair_orbit_atlas": {
            "pair_orbit_count": len(rows_out),
            "target_orbit_count_recovered_from_c93": len(derived_target_orbits),
            "orbit_size_spectrum": {str(size): count for size, count in sorted(Counter(len(orbit) for orbit in pair_orbits).items())},
            "stabilizer_order_spectrum": {str(order): count for order, count in sorted(Counter(row["stabilizer_order_in_effective_label_group"] for row in rows_out).items())},
            "relation_type_spectrum": dict(sorted(Counter(row["relation_type"] for row in rows_out).items())),
            "self_transpose_orbit_count": sum(row["transpose_orbit_index"] == row["pair_orbit_index"] for row in rows_out),
            "burnside_fixed_ordered_pair_sum": fixed_pair_sum,
            "rows": rows_out,
        },
        "checks": {
            "effective_order_1920_label_group_reconstructed": True,
            "ambient_order_11520_kept_distinct": True,
            "all_target_maps_are_permutations": True,
            "all_400_ordered_pairs_partitioned": True,
            "all_pair_orbits_preserve_c88_relation_type": True,
            "all_pair_orbits_preserve_complete_c90_joint_payload": True,
            "c93_single_target_orbits_recovered_exactly": True,
            "burnside_ordered_pair_identity_verified": True,
            "transpose_orbit_involution_verified": True,
        },
        "claims": {
            "finite_effective_pair_orbit_quotient_claimed": True,
            "arithmetic_local_claimed": False,
            "euler_factors_claimed": False,
            "root_numbers_claimed": False,
            "automorphy_claimed": False,
            "full_burnside_ring_claimed": False,
            "full_table_of_marks_claimed": False,
            "hilbert_polya_operator_claimed": False,
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "pair_orbit_count": len(rows_out),
        "self_transpose_orbit_count": result["pair_orbit_atlas"]["self_transpose_orbit_count"],
        "evidence_sha256": digest(OUT.read_bytes()),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
