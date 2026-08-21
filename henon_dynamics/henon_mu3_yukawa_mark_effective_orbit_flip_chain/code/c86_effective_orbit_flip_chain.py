#!/usr/bin/env python3
"""Produce the exact effective-orbit one-bit flip quotient certificate."""

from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
HD = ROOT / "henon_dynamics"
C75 = HD / "henon_mu3_yukawa_mark_closure_incidence_lift"
C76 = HD / "henon_mu3_yukawa_mark_closure_orbit_atlas"
C78 = HD / "henon_mu3_yukawa_mark_repair_distance_geometry"
C81 = HD / "henon_mu3_yukawa_mark_effective_orbit_repair_profile"
C82 = HD / "henon_mu3_yukawa_mark_bitflip_noise_fourier_spectrum"
OUT = PROJECT / "results/c86_effective_orbit_flip_chain_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
ALL = (1 << 16) - 1

HASHES = {
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
    "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
    "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
    "c78": "728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae",
    "c78_manifest": "955b5ce23bf811d7377c0e41afd8d7dbc384a467790647e04cf0dadc98347c60",
    "c81": "c3cc35f45e1c8f7c9d4ecaecca820bf9dbc4db1c6a5769c20c75bad21f32fd9f",
    "c81_manifest": "ff3028fd68817795b08ff24332ef44de4cf520ccba543f053fbd78140ac1b512",
    "c82": "6fc49cad02956f463b1e37d017506f437edce6717414da74770ad94913ccefa1",
    "c82_manifest": "5934de3a933e559e941fc636860db2f9f5ceca181acd9d4915396e9facdc8f8b",
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(16))


def generate_group(generators: list[tuple[int, ...]]) -> list[tuple[int, ...]]:
    identity = tuple(range(16))
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


def apply_mask(mask: int, permutation: tuple[int, ...]) -> int:
    result = 0
    while mask:
        low = mask & -mask
        result |= 1 << permutation[low.bit_length() - 1]
        mask ^= low
    return result


def repair_distance(retained: int) -> int:
    deleted = ALL ^ retained
    blocks = (
        1 << 0,
        1 << 15,
        (1 << 6) | (1 << 14),
        sum(1 << index for index in (2, 3, 7, 10, 11)),
    )
    fully_deleted = sum((deleted & block) == block for block in blocks)
    return int(bool(deleted & (1 << 8))) + max(0, fully_deleted - 2)


def source_paths() -> dict[str, Path]:
    return {
        "c75": C75 / "results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": C75 / "C75_PREFREEZE_MANIFEST.json",
        "c76": C76 / "results/c76_closure_orbit_atlas_evidence.json",
        "c76_manifest": C76 / "C76_PREFREEZE_MANIFEST.json",
        "c78": C78 / "results/c78_repair_distance_geometry_evidence.json",
        "c78_manifest": C78 / "C78_PREFREEZE_MANIFEST.json",
        "c81": C81 / "results/c81_effective_orbit_repair_profile_evidence.json",
        "c81_manifest": C81 / "C81_PREFREEZE_MANIFEST.json",
        "c82": C82 / "results/c82_bitflip_noise_fourier_evidence.json",
        "c82_manifest": C82 / "C82_PREFREEZE_MANIFEST.json",
    }


def main() -> None:
    paths = source_paths()
    raw = {name: path.read_bytes() for name, path in paths.items()}
    observed = {name: digest(value) for name, value in raw.items()}
    assert observed == HASHES, (observed, HASHES)
    source = {name: json.loads(raw[name]) for name in ("c75", "c76", "c78", "c81", "c82")}
    assert all(document["status"] == "PREFREEZE_G3_PASS" for document in source.values())
    assert all(document["scope_literal"] == FIREWALL for document in source.values())
    assert source["c75"]["lifted_symmetry"]["lifted_group_order"] == 11520
    assert source["c76"]["source_model"]["effective_label_group_order"] == 1920
    assert source["c76"]["source_model"]["c75_ambient_c6_kernel_order"] == 6
    assert source["c81"]["source_model"]["effective_label_group_order"] == 1920

    generator_rows = {row["name"]: row for row in source["c75"]["lifted_symmetry"]["generators"]}
    generator_names = (
        "zero_5_cycle",
        "zero_transposition",
        "fiber_F3_transposition",
        "fiber_F9_transposition",
        "ambient_s",
    )
    generators = [tuple(generator_rows[name]["label_permutation"]) for name in generator_names]
    group = generate_group(generators)
    assert len(group) == 1920

    unseen = set(range(1 << 16))
    orbits: list[list[int]] = []
    orbit_index = [-1] * (1 << 16)
    while unseen:
        representative = min(unseen)
        orbit = sorted({apply_mask(representative, permutation) for permutation in group})
        index = len(orbits)
        for mask in orbit:
            orbit_index[mask] = index
        unseen.difference_update(orbit)
        orbits.append(orbit)
    assert len(orbits) == 3024
    assert all(index >= 0 for index in orbit_index)

    c76_rows = source["c76"]["support_orbit_atlas"]["rows"]
    assert [(orbit[0], len(orbit)) for orbit in orbits] == [
        (row["representative_mask"], row["orbit_size"]) for row in c76_rows
    ]
    c81_rows = source["c81"]["orbit_quotient"]["rows"]
    assert [(orbit[0], len(orbit), repair_distance(orbit[0])) for orbit in orbits] == [
        (row["representative_mask"], row["orbit_size"], row["profile"]["rho"])
        for row in c81_rows
    ]

    quotient: list[Counter[int]] = []
    orbit_rows: list[dict[str, Any]] = []
    neighbor_spectrum: Counter[int] = Counter()
    entry_spectrum: Counter[int] = Counter()
    for index, orbit in enumerate(orbits):
        representative = orbit[0]
        transitions = Counter(orbit_index[representative ^ (1 << bit)] for bit in range(16))
        assert sum(transitions.values()) == 16
        assert index not in transitions
        for mask in orbit:
            assert Counter(orbit_index[mask ^ (1 << bit)] for bit in range(16)) == transitions
        quotient.append(transitions)
        neighbor_spectrum[len(transitions)] += 1
        entry_spectrum.update(transitions.values())
        orbit_rows.append({
            "orbit_index": index,
            "representative_mask": representative,
            "support_size": representative.bit_count(),
            "orbit_size": len(orbit),
            "stabilizer_order": len(group) // len(orbit),
            "repair_distance": repair_distance(representative),
            "neighbor_orbit_count": len(transitions),
            "transitions": [
                {"target_orbit_index": target, "multiplicity": multiplicity}
                for target, multiplicity in sorted(transitions.items())
            ],
        })

    assert sum(len(row) for row in quotient) == 30240
    assert all(
        len(orbits[left]) * multiplicity
        == len(orbits[right]) * quotient[right][left]
        for left, transitions in enumerate(quotient)
        for right, multiplicity in transitions.items()
    )
    assert dict(sorted(neighbor_spectrum.items())) == {
        7: 128, 8: 384, 9: 480, 10: 800, 11: 864, 12: 336, 13: 32,
    }
    assert dict(sorted(entry_spectrum.items())) == {1: 19296, 2: 7344, 3: 1008, 4: 1584, 5: 1008}

    actual_flow: Counter[tuple[int, int]] = Counter()
    quotient_arc_flow: Counter[tuple[int, int]] = Counter()
    for left, transitions in enumerate(quotient):
        left_rho = orbit_rows[left]["repair_distance"]
        for right, multiplicity in transitions.items():
            right_rho = orbit_rows[right]["repair_distance"]
            quotient_arc_flow[(left_rho, right_rho)] += 1
            actual_flow[(left_rho, right_rho)] += len(orbits[left]) * multiplicity
    assert sum(actual_flow.values()) == 16 * (1 << 16)
    assert actual_flow[(0, 0)] == source["c82"]["bitflip_noise"]["autocorrelation_by_distance"]["1"]
    expected_repair_counts = {int(key): value for key, value in source["c78"]["bivariate_generating_function"]["P_1_at_y"].items()}
    assert Counter(repair_distance(mask) for mask in range(1 << 16)) == Counter(expected_repair_counts)

    multiplicities = [sum(orbit[0].bit_count() == degree for orbit in orbits) for degree in range(17)]
    assert multiplicities == source["c76"]["support_orbit_atlas"]["orbit_count_by_cardinality"]
    spectrum = [
        {"degree": degree, "eigenvalue": 16 - 2 * degree, "multiplicity": multiplicity}
        for degree, multiplicity in enumerate(multiplicities)
    ]
    assert sum(row["multiplicity"] for row in spectrum) == len(orbits)
    assert sum(row["eigenvalue"] * row["multiplicity"] for row in spectrum) == 0
    assert sum(row["eigenvalue"] ** 2 * row["multiplicity"] for row in spectrum) == 77760

    result: dict[str, Any] = {
        "schema_id": "hcs-c86-effective-orbit-one-bit-flip-chain-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": HASHES,
        "definition": {
            "state_space": "3024 orbits of 16-label support masks under the faithful effective action",
            "transition": "toggle exactly one label",
            "quotient_entry": "q_ij=#{labels ell:A xor {ell} in O_j}, A in O_i",
            "reversible_weight": "orbit size |O_i|",
            "ambient_lift_order": 11520,
            "ambient_label_kernel_order": 6,
            "effective_label_group_order": 1920,
        },
        "quotient_chain": {
            "support_count": 1 << 16,
            "orbit_count": len(orbits),
            "directed_nonzero_arc_count": sum(len(row) for row in quotient),
            "unoriented_orbit_pair_count": sum(len(row) for row in quotient) // 2,
            "row_sum": 16,
            "orbit_size_spectrum": {
                str(size): count for size, count in sorted(Counter(len(orbit) for orbit in orbits).items())
            },
            "neighbor_orbit_count_spectrum": {
                str(size): count for size, count in sorted(neighbor_spectrum.items())
            },
            "positive_entry_multiplicity_spectrum": {
                str(value): count for value, count in sorted(entry_spectrum.items())
            },
            "weighted_detailed_balance_verified": True,
            "strong_lumpability_verified_on_all_supports": True,
            "rows": orbit_rows,
        },
        "repair_flow": {
            "support_orbit_count_by_repair_distance": {
                str(distance): count
                for distance, count in sorted(Counter(row["repair_distance"] for row in orbit_rows).items())
            },
            "actual_directed_edge_count": {
                f"{left},{right}": count for (left, right), count in sorted(actual_flow.items())
            },
            "quotient_directed_arc_count": {
                f"{left},{right}": count for (left, right), count in sorted(quotient_arc_flow.items())
            },
            "full_core_distance_one_ordered_pair_count": actual_flow[(0, 0)],
            "c82_distance_one_recovered": True,
        },
        "invariant_walsh_spectrum": {
            "basis": "effective-group orbit sums of Walsh characters",
            "eigenvalue_formula": "lambda_k=16-2k",
            "multiplicity_rule": "number of effective-group orbits on k-subsets",
            "rows": spectrum,
            "dimension": sum(row["multiplicity"] for row in spectrum),
            "first_moment": sum(row["eigenvalue"] * row["multiplicity"] for row in spectrum),
            "second_moment": sum(row["eigenvalue"] ** 2 * row["multiplicity"] for row in spectrum),
        },
        "claims": {
            "all_65536_supports_partitioned": True,
            "effective_1920_action_used": True,
            "ambient_11520_action_not_substituted": True,
            "exact_strong_orbit_quotient": True,
            "weighted_detailed_balance": True,
            "complete_invariant_walsh_spectrum": True,
            "c82_distance_one_identity": True,
            "full_burnside_ring_claimed": False,
            "arithmetic_local_claimed": False,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "orbit_count": len(orbits),
        "directed_arcs": result["quotient_chain"]["directed_nonzero_arc_count"],
        "full_core_distance_one": actual_flow[(0, 0)],
        "evidence_sha256": digest(OUT.read_bytes()),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
