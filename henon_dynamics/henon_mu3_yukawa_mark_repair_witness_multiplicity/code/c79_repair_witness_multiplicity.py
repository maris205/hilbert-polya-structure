#!/usr/bin/env python3
"""Produce the C79 exact repair-witness multiplicity certificate.

For a deletion set ``D`` let ``A=L\\D`` be the retained labels.  The C78
repair distance is the least size of a restoration set ``R`` contained in
``D`` for which ``A union R`` generates the full named core.  C79 records
not only that distance, but also

    W(D) = #{R subset D : |R| = rho(D), Phi(A union R) = Q}.

The C73 cone-over-K_{1,1,2,5} criterion makes both quantities exact finite
block statistics.  The independent checker deliberately recomputes W by
the point-set closure table rather than accepting this structural formula.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import combinations
from math import comb
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
OUT = PROJECT / "results/c79_repair_witness_multiplicity_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
LABELS = tuple(f"S{i}" for i in range(1, 17))
ALL_MASK = (1 << 16) - 1

# These are the committed authorities at the start of C79.  They are kept
# literal so that an upstream replacement cannot silently change this paper.
EXPECTED = {
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


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def mask_for(labels: list[str]) -> int:
    return sum(1 << (int(label[1:]) - 1) for label in labels)


def witness_formula(full_flags: list[bool], sizes: list[int]) -> int:
    """Number of minimum ways to restore enough fully deleted blocks."""
    full = [index for index, flag in enumerate(full_flags) if flag]
    if len(full) <= 2:
        return 1
    if len(full) == 3:
        return sum(sizes[index] for index in full)
    assert len(full) == 4
    return sum(sizes[i] * sizes[j] for i, j in combinations(full, 2))


def key3(k: int, rho: int, witness: int) -> str:
    return f"{k},{rho},{witness}"


def key2(rho: int, witness: int) -> str:
    return f"{rho},{witness}"


def main() -> None:
    paths = {
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
    raw = {name: path.read_bytes() for name, path in paths.items()}
    observed = {name: digest(value) for name, value in raw.items()}
    assert observed == EXPECTED, (observed, EXPECTED)
    source = {name: json.loads(value) for name, value in raw.items() if not name.endswith("_manifest")}
    assert all(doc["status"] == "PREFREEZE_G3_PASS" for doc in source.values())
    assert all(doc["scope_literal"] == FIREWALL for doc in source.values())
    assert source["c73"]["generation_structure"]["criterion"] == (
        "a support generates 8C iff it contains S9 and meets at least two direction blocks"
    )
    assert source["c76"]["source_model"]["support_count"] == 65536
    assert source["c77"]["subgroup_poset"]["subgroup_count"] == 20
    assert source["c78"]["definition"]["maximum_distance"] == 3
    assert source["c78"]["authority"] == {
        name: value for name, value in EXPECTED.items()
        if name not in {"c78", "c78_manifest"}
    }

    blocks = [row["labels"] for row in source["c73"]["generation_structure"]["projective_direction_blocks"]]
    sizes = [len(block) for block in blocks]
    assert sizes == [1, 1, 2, 5]
    block_masks = [mask_for(block) for block in blocks]
    pivot_label = source["c73"]["generation_structure"]["pivot"]
    pivot_bit = mask_for([pivot_label])
    dummy_labels = source["c73"]["generation_structure"]["dummy_labels"]
    assert pivot_label == "S9" and len(dummy_labels) == 6
    assert source["c78"]["definition"]["direction_blocks"] == blocks

    distribution = Counter()
    by_deleted = [Counter() for _ in range(17)]
    by_retained = [Counter() for _ in range(17)]
    coefficient_table: Counter[tuple[int, int, int]] = Counter()
    masks_by_witness: dict[int, list[int]] = {w: [] for w in (1, 4, 7, 8, 25)}
    masks_by_rho: dict[int, list[int]] = {r: [] for r in range(4)}

    for deleted_mask in range(1 << 16):
        full_flags = [(deleted_mask & block) == block for block in block_masks]
        t = sum(full_flags)
        pivot_deleted = int(bool(deleted_mask & pivot_bit))
        rho = pivot_deleted + max(0, t - 2)
        witness = witness_formula(full_flags, sizes)
        assert 0 <= rho <= 3
        assert witness in masks_by_witness
        deleted_count = deleted_mask.bit_count()
        retained_count = (ALL_MASK ^ deleted_mask).bit_count()
        distribution[(rho, witness)] += 1
        by_deleted[deleted_count][(rho, witness)] += 1
        by_retained[retained_count][(rho, witness)] += 1
        coefficient_table[(deleted_count, rho, witness)] += 1
        masks_by_witness[witness].append(deleted_mask)
        masks_by_rho[rho].append(deleted_mask)

    expected_global = {
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
    }
    assert dict(distribution) == expected_global
    assert sum(distribution.values()) == 1 << 16
    assert max(rho for rho, _ in distribution) == 3
    assert set(witness for _, witness in distribution) == {1, 4, 7, 8, 25}
    assert {rho: len(masks) for rho, masks in masks_by_rho.items()} == {
        0: 30400, 1: 32704, 2: 2368, 3: 64
    }

    def sparse_counter(counter: Counter) -> dict[str, int]:
        return {key2(rho, witness): counter[(rho, witness)]
                for rho, witness in sorted(counter)
                if counter[(rho, witness)]}

    def sparse_coefficients(counter: Counter) -> dict[str, int]:
        return {key3(k, rho, witness): counter[(k, rho, witness)]
                for k, rho, witness in sorted(counter)
                if counter[(k, rho, witness)]}

    by_deleted_rows = [
        {"deleted_count": k, "rho_witness_counts": sparse_counter(by_deleted[k])}
        for k in range(17)
    ]
    by_retained_rows = [
        {"retained_count": k, "rho_witness_counts": sparse_counter(by_retained[k])}
        for k in range(17)
    ]
    assert all(sum(row["rho_witness_counts"].values()) == comb(16, row["deleted_count"])
               for row in by_deleted_rows)
    assert all(sum(row["rho_witness_counts"].values()) == comb(16, row["retained_count"])
               for row in by_retained_rows)

    polynomial = {
        "x_convention": "x marks deleted labels",
        "u_convention": "u marks repair distance rho(D)",
        "v_convention": "v marks minimum-restoration witness multiplicity W(D)",
        "definition": "G(x,u,v)=sum_D x^|D| u^rho(D) v^W(D)",
        "block_state_formula": (
            "G=(1+x)^6 sum_{I subset {1,1,2,5}} "
            "x^(sum_{i in I}s_i) product_{j notin I}((1+x)^s_j-x^s_j) "
            "u^max(0,|I|-2) v^w(I) (1+x*u), "
            "w(I)=1 if |I|<=2, sum_{i in I}s_i if |I|=3, "
            "sum_{i<j in I}s_i*s_j if |I|=4"
        ),
        "coefficient_table": sparse_coefficients(coefficient_table),
        "P_x_at_u1_v1": {str(k): comb(16, k) for k in range(17)},
        "P_1_at_u_v": {key2(rho, witness): distribution[(rho, witness)]
                        for rho, witness in sorted(distribution)},
        "P_1_1_at_v": {str(witness): sum(value for (rho, w), value in distribution.items()
                                           if w == witness)
                        for witness in sorted({w for _, w in distribution})},
        "P_1_at_u_v1": {str(rho): sum(value for (r, _), value in distribution.items()
                                       if r == rho)
                        for rho in range(4)},
    }
    result: dict[str, Any] = {
        "schema_id": "hcs-c79-repair-witness-multiplicity-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": EXPECTED,
        "definition": {
            "deleted_set": "D",
            "retained_set": "A=L\\D",
            "repair_distance": "rho(D)=min{|R|: R subset D and Phi((L\\D) union R)=Q}",
            "witness_multiplicity": "W(D)=#{R subset D: |R|=rho(D), Phi((L\\D) union R)=Q}",
            "pivot": pivot_label,
            "direction_blocks": blocks,
            "direction_block_sizes": sizes,
            "dummy_labels": dummy_labels,
            "rho_formula": "rho(D)=1_{S9 in D}+max(0,t(D)-2)",
            "witness_formula": (
                "W(D)=1 for t<=2; W=sum sizes of fully deleted blocks for t=3; "
                "W=sum pairwise size products for t=4"
            ),
            "maximum_repair_distance": 3,
            "witness_values": [1, 4, 7, 8, 25],
        },
        "witness_multiplicity_atlas": {
            "support_count": 65536,
            "global_rho_witness_counts": sparse_counter(distribution),
            "by_deleted_cardinality": by_deleted_rows,
            "by_retained_cardinality": by_retained_rows,
            "witness_value_counts": polynomial["P_1_1_at_v"],
            "distance_value_counts": polynomial["P_1_at_u_v1"],
            "max_witness_multiplicity": 25,
            "max_witness_masks": masks_by_witness[25],
            "distance_three_masks": sorted(masks_by_rho[3]),
        },
        "trivariate_generating_function": polynomial,
        "claims": {
            "all_65536_deletion_sets_enumerated": True,
            "exact_minimum_restoration_witness_count": True,
            "structural_witness_formula_verified": True,
            "rho_at_most_three": True,
            "witness_values_exact": True,
            "full_burnside_ring_claimed": False,
            "arithmetic_local_claimed": False,
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "support_count": 1 << 16,
        "global_rho_witness_counts": result["witness_multiplicity_atlas"]["global_rho_witness_counts"],
        "witness_value_counts": result["witness_multiplicity_atlas"]["witness_value_counts"],
        "coefficient_cells": len(polynomial["coefficient_table"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
