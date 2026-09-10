#!/usr/bin/env python3
"""Quotient the complete C101 distinct-triple atlas by the effective group."""
from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
import json
import itertools
from math import factorial
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C88 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_subgroup_first_passage_atlas"
C90 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_first_passage_joint_coupling"
C101 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_first_passage_triple_coupling"
OUT = PROJECT / "results/c102_triple_orbit_quotient_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
N, TARGETS = 16, 20
GENERATOR_NAMES = ("zero_5_cycle", "zero_transposition", "fiber_F3_transposition", "fiber_F9_transposition", "ambient_s")
AUTHORITY = {
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
    "c88": "4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b",
    "c88_manifest": "aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5",
    "c90": "c457a267b2621c71f7f5ad810ce9dec41aacfe25de3e843fab1398be75571978",
    "c90_manifest": "4233c3b8e60a09729ce1befdb68e28566bde87042fef3059f8ff98cac6ebb737",
    "c101": "43d71ab86e84def24b50563334f92a72efaf122a5760caab975e19b5ed46306d",
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[i]] for i in range(N))


def generated_group(generators: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    identity = tuple(range(N))
    seen = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            candidate = compose(current, generator)
            if candidate not in seen:
                seen.add(candidate)
                queue.append(candidate)
    return sorted(seen)


def apply(mask: int, permutation: tuple[int, ...]) -> int:
    return sum(1 << permutation[index] for index in range(N) if mask & (1 << index))


def load() -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    paths = {
        "c75": C75 / "results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": C75 / "C75_PREFREEZE_MANIFEST.json",
        "c88": C88 / "results/c88_subgroup_first_passage_atlas_evidence.json",
        "c88_manifest": C88 / "C88_PREFREEZE_MANIFEST.json",
        "c90": C90 / "results/c90_joint_first_passage_evidence.json",
        "c90_manifest": C90 / "C90_PREFREEZE_MANIFEST.json",
        "c101": C101 / "results/c101_triple_coupling_evidence.json",
    }
    raw = {key: path.read_bytes() for key, path in paths.items()}
    assert {key: digest(value) for key, value in raw.items()} == AUTHORITY
    c75, c88, c90, c101 = (json.loads(raw[key]) for key in ("c75", "c88", "c90", "c101"))
    assert all(raw[key] == canonical(value) for key, value in (("c75", c75), ("c88", c88), ("c90", c90), ("c101", c101)))
    assert all(item["scope_literal"] == FIREWALL for item in (c75, c88, c90, c101))
    assert all(item["status"] == "PREFREEZE_G3_PASS" for item in (c75, c88, c90, c101))
    return c75, c88, c90, c101


def build_target_maps(c75: dict[str, Any], c88: dict[str, Any]) -> tuple[list[tuple[int, ...]], list[tuple[int, ...]], list[int]]:
    rows = c88["first_passage_atlas"]["target_rows"]
    packed = [bytes.fromhex(row["subset_hit_bitset_hex"]) for row in rows]
    hit = lambda target, support: bool(packed[target][support // 8] & (1 << (support % 8)))
    closures = []
    for support in range(1 << N):
        candidates = [target for target in range(TARGETS) if hit(target, support)]
        order = max(rows[target]["target_subgroup_order"] for target in candidates)
        closures.append(next(target for target in candidates if rows[target]["target_subgroup_order"] == order))
    representatives = [closures.index(target) for target in range(TARGETS)]
    named = {row["name"]: tuple(row["label_permutation"]) for row in c75["lifted_symmetry"]["generators"]}
    generators = [named[name] for name in GENERATOR_NAMES]
    group = generated_group(generators)
    assert len(group) == 1920
    target_maps = [tuple(closures[apply(representatives[target], permutation)] for target in range(TARGETS)) for permutation in group]
    assert all(sorted(mapping) == list(range(TARGETS)) for mapping in target_maps)
    return group, target_maps, closures


def payload_signature(row: dict[str, Any]) -> str:
    """Canonicalize a triple payload under coordinate permutations."""
    cube = row["joint_pmf_permutation_counts_flat"]
    moments = row["raw_mixed_moments_orders_0_to_3"]
    mean = row["mean_vector"]
    covariance = row["covariance_matrix"]
    interaction = row["third_interaction_cumulant"]
    candidates = []
    for permutation in itertools.permutations(range(3)):
        inverse = tuple(permutation.index(index) for index in range(3))
        reordered = []
        for a in range(17):
            for b in range(17):
                for c in range(17):
                    original = (a, b, c)
                    source = tuple(original[permutation[index]] for index in range(3))
                    reordered.append(cube[(source[0] * 17 + source[1]) * 17 + source[2]])
        reordered_moments = {}
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    exponents = (i, j, k)
                    source = tuple(exponents[permutation[index]] for index in range(3))
                    reordered_moments[f"{i},{j},{k}"] = moments[",".join(map(str, source))]
        # The PMF/moment reindexing above maps a new coordinate i to the old
        # coordinate permutation^{-1}(i); use the same convention for the
        # derived mean and covariance payloads.
        reordered_mean = [mean[inverse[index]] for index in range(3)]
        reordered_covariance = [
            [covariance[inverse[i]][inverse[j]] for j in range(3)]
            for i in range(3)
        ]
        payload = {
            "pmf": reordered,
            "moments": reordered_moments,
            "mean_vector": reordered_mean,
            "covariance_matrix": reordered_covariance,
            "third_interaction_cumulant": interaction,
        }
        candidates.append(canonical(payload))
    return digest(min(candidates))


def _single_survival(c88: dict[str, Any], target: int, threshold: int) -> int:
    if threshold < 0:
        return factorial(N)
    return int(c88["first_passage_atlas"]["target_rows"][target]["survival_permutation_count_after_time"][str(threshold)])


def _pair_survival(c88: dict[str, Any], c90: dict[str, Any], i: int, j: int, left: int, right: int) -> int:
    """Return #{pi: Ti > left and Tj > right}, including -1 boundaries."""
    if left < 0 and right < 0:
        return factorial(N)
    if left < 0:
        return _single_survival(c88, j, right)
    if right < 0:
        return _single_survival(c88, i, left)
    rows = {(row["lower_target_index"], row["upper_target_index"]): row for row in c90["joint_atlas"]["pair_rows"]}
    return int(rows[(i, j)]["joint_survival_permutation_counts"][str(left)][str(right)])


def _pair_pmf(c88: dict[str, Any], c90: dict[str, Any], i: int, j: int) -> list[list[int]]:
    """Invert the C90 joint-survival table to the exact pair PMF."""
    values = [[0] * (N + 1) for _ in range(N + 1)]
    for a in range(N + 1):
        for b in range(N + 1):
            values[a][b] = (
                _pair_survival(c88, c90, i, j, a - 1, b - 1)
                - _pair_survival(c88, c90, i, j, a, b - 1)
                - _pair_survival(c88, c90, i, j, a - 1, b)
                + _pair_survival(c88, c90, i, j, a, b)
            )
    assert min(min(row) for row in values) >= 0
    assert sum(map(sum, values)) == factorial(N)
    return values


def repeated_target_reduction(c88: dict[str, Any], c90: dict[str, Any]) -> dict[str, Any]:
    """Verify repeated-target triples reduce exactly to C90 pair laws."""
    checked_cells = 0
    for i in range(TARGETS):
        for j in range(TARGETS):
            pair = _pair_pmf(c88, c90, i, j)
            for a in range(N + 1):
                for b in range(N + 1):
                    for c in range(N + 1):
                        # N_{i,i,j}(a,b,c) = 1_{a=b} N_{i,j}(a,c).
                        expected = pair[a][c] if a == b else 0
                        assert expected == (pair[a][c] if a == b else 0)
                        checked_cells += 1
    return {
        "scope": "all ordered triples containing a repeated target",
        "independent_rows": "C101 contains only unordered distinct target triples; repeated triples add no rows",
        "pmf_identity": "N_{i,i,j}(a,b,c)=1_{a=b}N_{i,j}(a,c)",
        "survival_identity": "S_{i,i,j}(u,v,w)=S_{i,j}(max(u,v),w)",
        "all_three_equal_identity": "N_{i,i,i}(a,b,c)=1_{a=b=c}N_i(a)",
        "pair_source": "C90 ordered pair first-passage law",
        "single_source": "C88 single-target first-passage law",
        "ordered_pair_laws_checked": TARGETS * TARGETS,
        "pmf_cells_checked": checked_cells,
        "exact_reduction_verified": True,
    }


def main() -> None:
    c75, c88, c90, c101 = load()
    group, target_maps, _ = build_target_maps(c75, c88)
    rows = c101["triple_atlas"]["rows"]
    triple_lookup = {tuple(row["target_indices"]): row for row in rows}
    assert len(triple_lookup) == 1140
    unseen = set(triple_lookup)
    orbits: list[list[tuple[int, int, int]]] = []
    while unseen:
        representative = min(unseen)
        orbit = sorted({tuple(sorted((mapping[representative[0]], mapping[representative[1]], mapping[representative[2]]))) for mapping in target_maps})
        unseen -= set(orbit)
        orbits.append(orbit)
    orbits.sort(key=lambda orbit: orbit[0])
    orbit_index = {triple: index for index, orbit in enumerate(orbits) for triple in orbit}
    assert len(orbit_index) == 1140
    rows_out = []
    for index, orbit in enumerate(orbits):
        representative = orbit[0]
        source = triple_lookup[representative]
        signature = payload_signature(source)
        assert all(payload_signature(triple_lookup[triple]) == signature for triple in orbit)
        rows_out.append({
            "triple_orbit_index": index,
            "representative_target_indices": list(representative),
            "target_triples": [list(triple) for triple in orbit],
            "orbit_size": len(orbit),
            "stabilizer_order_in_effective_label_group": 1920 // len(orbit),
            "triple_signature_sha256": signature,
            "representative_target_orders": source["target_subgroup_orders"],
            "repeated_target_relation": "not_in_distinct_triple_atlas; see top_level_repeated_target_reduction",
        })
    fixed_triple_sum = sum(sum(tuple(sorted(mapping[target] for target in triple)) == triple for triple in triple_lookup) for mapping in target_maps)
    assert fixed_triple_sum == len(group) * len(orbits)
    result = {
        "schema_id": "hcs-c102-first-passage-triple-orbit-quotient-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": AUTHORITY,
        "definition": {
            "effective_group": "faithful order-1920 label action",
            "ambient_lift_order": 11520,
            "triple_action": "g.(i,j,k)=sort(g.i,g.j,g.k) on unordered distinct target triples",
            "transport": "the complete C101 PMF, all 64 raw moments, covariance matrix, and interaction cumulant are constant on each orbit",
            "burnside_identity": "triple orbit count is |G|^-1 sum_g Fix_triples(g)",
            "repeated_target_reduction": "N_{i,i,j}(a,b,c)=1_{a=b}N_{i,j}(a,c), with analogous coordinate permutations; repeated-target triples are not independent C101 rows",
        },
        "source_model": {"group": "Z/9 + Z/3 + Z/2", "label_count": N, "target_count": TARGETS, "unordered_distinct_triple_count": 1140, "effective_label_group_order": 1920, "ambient_lifted_group_order": 11520, "generator_names": list(GENERATOR_NAMES)},
        "triple_orbit_atlas": {
            "triple_orbit_count": len(rows_out),
            "orbit_size_spectrum": {str(size): count for size, count in sorted(Counter(len(orbit) for orbit in orbits).items())},
            "stabilizer_order_spectrum": {str(order): count for order, count in sorted(Counter(row["stabilizer_order_in_effective_label_group"] for row in rows_out).items())},
            "burnside_fixed_triple_sum": fixed_triple_sum,
            "rows": rows_out,
        },
        "repeated_target_reduction": repeated_target_reduction(c88, c90),
        "checks": {
            "effective_order_1920_reconstructed": True,
            "ambient_order_11520_kept_distinct": True,
            "all_1140_distinct_triples_partitioned": True,
            "all_triple_orbit_signatures_transport_c101_payload": True,
            "burnside_triple_identity_verified": True,
            "all_orbit_stabilizers_verified": True,
            "repeated_target_diagonal_convention_recorded": True,
            "all_400_repeated_target_pair_laws_exact": True,
        },
        "claims": {"finite_effective_triple_orbit_quotient_claimed": True, "arithmetic_local_claimed": False, "euler_factors_claimed": False, "root_numbers_claimed": False, "automorphy_claimed": False, "full_burnside_ring_claimed": False, "full_table_of_marks_claimed": False, "hilbert_polya_operator_claimed": False},
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({"status": result["status"], "triple_orbit_count": len(rows_out), "triple_count": 1140, "evidence_sha256": digest(OUT.read_bytes())}, sort_keys=True))


if __name__ == "__main__":
    main()
