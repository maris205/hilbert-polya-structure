#!/usr/bin/env python3
"""Independent semantic reconstruction of the complete C97 receipt."""
from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c97_pair_orbit_quotient_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
N, TARGETS, SUPPORTS = 16, 20, 1 << 16
NAMES = ("zero_5_cycle", "zero_transposition", "fiber_F3_transposition", "fiber_F9_transposition", "ambient_s")
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


def image(mask: int, permutation: tuple[int, ...]) -> int:
    return sum(1 << permutation[index] for index in range(N) if mask & (1 << index))


def group(generators: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    identity = tuple(range(N))
    found = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            candidate = compose(current, generator)
            if candidate not in found:
                found.add(candidate)
                queue.append(candidate)
    return sorted(found)


def source_paths() -> dict[str, Path]:
    base = ROOT / "henon_dynamics"
    return {
        "c75": base / "henon_mu3_yukawa_mark_closure_incidence_lift/results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": base / "henon_mu3_yukawa_mark_closure_incidence_lift/C75_PREFREEZE_MANIFEST.json",
        "c76": base / "henon_mu3_yukawa_mark_closure_orbit_atlas/results/c76_closure_orbit_atlas_evidence.json",
        "c76_manifest": base / "henon_mu3_yukawa_mark_closure_orbit_atlas/C76_PREFREEZE_MANIFEST.json",
        "c88": base / "henon_mu3_yukawa_mark_subgroup_first_passage_atlas/results/c88_subgroup_first_passage_atlas_evidence.json",
        "c88_manifest": base / "henon_mu3_yukawa_mark_subgroup_first_passage_atlas/C88_PREFREEZE_MANIFEST.json",
        "c90": base / "henon_mu3_yukawa_mark_first_passage_joint_coupling/results/c90_joint_first_passage_evidence.json",
        "c90_manifest": base / "henon_mu3_yukawa_mark_first_passage_joint_coupling/C90_PREFREEZE_MANIFEST.json",
        "c93": base / "henon_mu3_yukawa_mark_first_passage_orbit_quotient/results/c93_first_passage_orbit_quotient_evidence.json",
        "c93_manifest": base / "henon_mu3_yukawa_mark_first_passage_orbit_quotient/C93_PREFREEZE_MANIFEST.json",
    }


def signature(row: dict[str, Any]) -> bytes:
    return canonical({key: row[key] for key in (
        "joint_survival_permutation_counts",
        "joint_survival_probabilities",
        "mixed_raw_moments",
        "covariance",
    )})


def build_expected() -> tuple[dict[str, Any], dict[str, Any]]:
    raw = {name: path.read_bytes() for name, path in source_paths().items()}
    assert {name: digest(value) for name, value in raw.items()} == AUTHORITY
    c75, c76, c88, c90, c93 = [json.loads(raw[name]) for name in ("c75", "c76", "c88", "c90", "c93")]
    for name in ("c75", "c76", "c88", "c90", "c93"):
        assert raw[name] == canonical(json.loads(raw[name]))
    assert all(item["scope_literal"] == FIREWALL and item["status"] == "PREFREEZE_G3_PASS" for item in (c75, c76, c88, c90, c93))

    rows88 = c88["first_passage_atlas"]["target_rows"]
    inclusion = c88["target_poset"]["inclusion_matrix"]
    packed = [bytes.fromhex(row["subset_hit_bitset_hex"]) for row in rows88]
    hit = lambda target, support: bool(packed[target][support // 8] & (1 << (support % 8)))

    # Independent closure decoder: the hit vector of a support is exactly a
    # column of the C88 subgroup-inclusion matrix.  This avoids the producer's
    # maximal-order selection rule.
    columns = {tuple(bool(inclusion[left][right]) for left in range(TARGETS)): right for right in range(TARGETS)}
    assert len(columns) == TARGETS
    closure: list[int] = []
    representatives: list[int | None] = [None] * TARGETS
    for support in range(SUPPORTS):
        vector = tuple(hit(target, support) for target in range(TARGETS))
        target = columns[vector]
        closure.append(target)
        if representatives[target] is None:
            representatives[target] = support
    assert all(value is not None for value in representatives)
    reps = [int(value) for value in representatives]

    named = {row["name"]: tuple(row["label_permutation"]) for row in c75["lifted_symmetry"]["generators"]}
    generators = [named[name] for name in NAMES]
    label_group = group(generators)
    assert len(label_group) == 1920
    assert c76["source_model"]["effective_label_group_order"] == 1920
    target_maps = [tuple(closure[image(reps[target], permutation)] for target in range(TARGETS)) for permutation in label_group]
    assert all(sorted(target_map) == list(range(TARGETS)) for target_map in target_maps)

    for generator in generators:
        target_map = target_maps[label_group.index(generator)]
        for target in range(TARGETS):
            assert all(hit(target, support) == hit(target_map[target], image(support, generator)) for support in range(SUPPORTS))

    source_pairs = {(row["lower_target_index"], row["upper_target_index"]): row for row in c90["joint_atlas"]["pair_rows"]}
    assert len(source_pairs) == TARGETS * TARGETS
    unseen = {(left, right) for left in range(TARGETS) for right in range(TARGETS)}
    orbits: list[list[tuple[int, int]]] = []
    while unseen:
        pair = min(unseen)
        orbit = sorted({(target_map[pair[0]], target_map[pair[1]]) for target_map in target_maps})
        unseen -= set(orbit)
        orbits.append(orbit)
    orbits.sort(key=lambda orbit: orbit[0])
    index_of = {pair: index for index, orbit in enumerate(orbits) for pair in orbit}
    assert len(index_of) == 400

    target_orbits: list[list[int]] = []
    remaining = set(range(TARGETS))
    while remaining:
        target = min(remaining)
        orbit = sorted({target_map[target] for target_map in target_maps})
        remaining -= set(orbit)
        target_orbits.append(orbit)
    assert target_orbits == [row["target_orbit"] for row in c93["target_orbit_atlas"]["rows"]]

    def relation(pair: tuple[int, int]) -> str:
        left, right = pair
        if left == right:
            return "diagonal"
        if inclusion[left][right]:
            return "forward_comparable"
        if inclusion[right][left]:
            return "reverse_comparable"
        return "incomparable"

    output_rows: list[dict[str, Any]] = []
    for orbit_index, orbit in enumerate(orbits):
        representative = orbit[0]
        law = signature(source_pairs[representative])
        assert all(signature(source_pairs[pair]) == law for pair in orbit)
        relation_type = relation(representative)
        assert all(relation(pair) == relation_type for pair in orbit)
        output_rows.append({
            "pair_orbit_index": orbit_index,
            "representative_ordered_pair": list(representative),
            "ordered_target_pairs": [list(pair) for pair in orbit],
            "orbit_size": len(orbit),
            "stabilizer_order_in_effective_label_group": 1920 // len(orbit),
            "relation_type": relation_type,
            "transpose_orbit_index": index_of[(representative[1], representative[0])],
            "joint_law_sha256": digest(law),
            "representative_covariance": source_pairs[representative]["covariance"],
        })
    assert all(output_rows[row["transpose_orbit_index"]]["transpose_orbit_index"] == row["pair_orbit_index"] for row in output_rows)
    fixed_sum = sum(sum(target_map[target] == target for target in range(TARGETS)) ** 2 for target_map in target_maps)
    assert fixed_sum == 1920 * len(orbits)

    expected = {
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
            "ordered_target_pair_count": 400,
            "effective_label_group_order": 1920,
            "ambient_lifted_group_order": 11520,
            "generator_names": list(NAMES),
        },
        "pair_orbit_atlas": {
            "pair_orbit_count": len(output_rows),
            "target_orbit_count_recovered_from_c93": len(target_orbits),
            "orbit_size_spectrum": {str(size): count for size, count in sorted(Counter(map(len, orbits)).items())},
            "stabilizer_order_spectrum": {str(order): count for order, count in sorted(Counter(row["stabilizer_order_in_effective_label_group"] for row in output_rows).items())},
            "relation_type_spectrum": dict(sorted(Counter(row["relation_type"] for row in output_rows).items())),
            "self_transpose_orbit_count": sum(row["transpose_orbit_index"] == row["pair_orbit_index"] for row in output_rows),
            "burnside_fixed_ordered_pair_sum": fixed_sum,
            "rows": output_rows,
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
    return expected, {"pair_orbit_count": len(output_rows), "label_group_order": len(label_group)}


def validate_evidence_path(path: Path = EVIDENCE, built: dict[str, Any] | None = None) -> dict[str, Any]:
    expected, diagnostics = build_expected() if built is None else (built, {})
    raw = path.read_bytes()
    observed = json.loads(raw)
    assert raw == canonical(observed)
    assert observed == expected
    return {"status": "C97_INDEPENDENT_CHECK_PASS", **diagnostics, "evidence_sha256": digest(raw)}


def main() -> None:
    print(json.dumps(validate_evidence_path(), sort_keys=True))


if __name__ == "__main__":
    main()
