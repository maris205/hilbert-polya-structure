#!/usr/bin/env python3
"""Produce the C84 minimum-repair matroid and basis-exchange atlas."""

from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
OUT = PROJECT / "results/c84_minimum_repair_matroid_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
LABELS = tuple(f"S{i}" for i in range(1, 17))
ALL_MASK = (1 << len(LABELS)) - 1

EXPECTED = {
    "c75": "8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98",
    "c75_manifest": "7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb",
    "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
    "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
    "c79": "147a9b77e0ee7459040a7cc3c026bb21bce950a806e4fbc3ce0441dc9bb6c879",
    "c79_manifest": "982cce509de371d59c4b87cda75af057d994c6fc36146daddc3b983c9c63246c",
}

C75 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift"
C76 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas"
C79 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_repair_witness_multiplicity"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def mask_for(labels: list[str]) -> int:
    return sum(1 << (int(label[1:]) - 1) for label in labels)


def labels_for(mask: int) -> list[str]:
    return [LABELS[index] for index in range(len(LABELS)) if mask & (1 << index)]


def bits(mask: int) -> list[int]:
    return [1 << index for index in range(len(LABELS)) if mask & (1 << index)]


def permutation_from_cycles(cycles: list[list[str]]) -> tuple[int, ...]:
    permutation = list(range(len(LABELS)))
    for cycle in cycles:
        indices = [int(label[1:]) - 1 for label in cycle]
        for source, target in zip(indices, indices[1:] + indices[:1]):
            permutation[source] = target
    return tuple(permutation)


def permute_mask(mask: int, permutation: tuple[int, ...]) -> int:
    result = 0
    for source, target in enumerate(permutation):
        if mask & (1 << source):
            result |= 1 << target
    return result


def orbit(seed: int, generators: list[tuple[int, ...]]) -> set[int]:
    seen = {seed}
    queue = deque([seed])
    while queue:
        current = queue.popleft()
        for generator in generators:
            image = permute_mask(current, generator)
            if image not in seen:
                seen.add(image)
                queue.append(image)
    return seen


def structural_bases(
    deleted: int,
    block_masks: list[int],
    block_bits: list[list[int]],
    pivot_bit: int,
) -> tuple[list[int], list[int], int, int, int]:
    full_indices = [
        index for index, block_mask in enumerate(block_masks)
        if deleted & block_mask == block_mask
    ]
    direction_rank = max(0, len(full_indices) - 2)
    pivot_component = pivot_bit if deleted & pivot_bit else 0
    direction_bases = []
    if direction_rank == 0:
        direction_bases.append(0)
    else:
        for selected_blocks in combinations(full_indices, direction_rank):
            for selected_bits in product(*(block_bits[index] for index in selected_blocks)):
                direction_bases.append(sum(selected_bits))
    bases = sorted(pivot_component | direction for direction in direction_bases)
    full_ground = 0
    for index in full_indices:
        full_ground |= block_masks[index]
    external_loops = deleted & ~(pivot_component | full_ground)
    return bases, full_indices, direction_rank, pivot_component, external_loops


def exchange_adjacency(bases: list[int]) -> list[set[int]]:
    adjacency = [set() for _ in bases]
    for left, right in combinations(range(len(bases)), 2):
        if (bases[left] ^ bases[right]).bit_count() == 2:
            adjacency[left].add(right)
            adjacency[right].add(left)
    return adjacency


def graph_invariants(bases: list[int]) -> dict[str, Any]:
    adjacency = exchange_adjacency(bases)
    degree_spectrum = Counter(len(neighbors) for neighbors in adjacency)
    distances: list[list[int]] = []
    for source in range(len(bases)):
        row = [-1] * len(bases)
        row[source] = 0
        queue = deque([source])
        while queue:
            current = queue.popleft()
            for target in adjacency[current]:
                if row[target] == -1:
                    row[target] = row[current] + 1
                    queue.append(target)
        distances.append(row)
    assert all(distance >= 0 for row in distances for distance in row)
    pair_distances = Counter(
        distances[left][right]
        for left in range(len(bases))
        for right in range(left + 1, len(bases))
    )
    eccentricities = [max(row) for row in distances]
    return {
        "vertex_count": len(bases),
        "edge_count": sum(len(neighbors) for neighbors in adjacency) // 2,
        "degree_spectrum": {
            str(degree): degree_spectrum[degree] for degree in sorted(degree_spectrum)
        },
        "connected": True,
        "diameter": max(eccentricities),
        "radius": min(eccentricities),
        "unordered_distinct_pair_distance_spectrum": {
            str(distance): pair_distances[distance] for distance in sorted(pair_distances)
        },
    }


def base_exchange_obligations(bases: list[int]) -> int:
    base_set = set(bases)
    obligations = 0
    for left in bases:
        for right in bases:
            for removed in bits(left & ~right):
                obligations += 1
                assert any(
                    ((left ^ removed) | inserted) in base_set
                    for inserted in bits(right & ~left)
                )
    return obligations


def graph_type(witness_count: int) -> str:
    if witness_count == 1:
        return "K1"
    if witness_count in (4, 7, 8):
        return f"K{witness_count}"
    assert witness_count == 25
    return "L(K_{1,1,2,5})"


def main() -> None:
    paths = {
        "c75": C75 / "results/c75_closure_incidence_lift_evidence.json",
        "c75_manifest": C75 / "C75_PREFREEZE_MANIFEST.json",
        "c76": C76 / "results/c76_closure_orbit_atlas_evidence.json",
        "c76_manifest": C76 / "C76_PREFREEZE_MANIFEST.json",
        "c79": C79 / "results/c79_repair_witness_multiplicity_evidence.json",
        "c79_manifest": C79 / "C79_PREFREEZE_MANIFEST.json",
    }
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == EXPECTED
    source = {
        name: json.loads(value)
        for name, value in raw.items()
        if not name.endswith("_manifest")
    }
    assert all(document["status"] == "PREFREEZE_G3_PASS" for document in source.values())
    assert all(document["scope_literal"] == FIREWALL for document in source.values())
    c75, c76, c79 = source["c75"], source["c76"], source["c79"]
    assert c75["lifted_symmetry"]["lifted_group_order"] == 11520
    assert c76["source_model"]["effective_label_group_order"] == 1920
    assert c79["claims"]["exact_minimum_restoration_witness_count"]

    definition = c79["definition"]
    blocks = definition["direction_blocks"]
    block_sizes = definition["direction_block_sizes"]
    dummy_labels = definition["dummy_labels"]
    pivot = definition["pivot"]
    assert blocks == [
        ["S1"], ["S16"], ["S7", "S15"],
        ["S3", "S4", "S8", "S11", "S12"],
    ]
    assert block_sizes == [1, 1, 2, 5]
    assert dummy_labels == ["S2", "S5", "S6", "S10", "S13", "S14"]
    assert pivot == "S9"
    block_masks = [mask_for(block) for block in blocks]
    block_bits = [bits(block_mask) for block_mask in block_masks]
    pivot_bit = mask_for([pivot])

    template_counts: Counter[tuple[int, int, str]] = Counter()
    graph_support_counts: Counter[str] = Counter()
    total_exchange_vertices = 0
    total_exchange_edges = 0
    total_base_exchange_obligations = 0
    maskwise_verified = 0
    all_deleted_bases: list[int] | None = None

    for deleted in range(1 << len(LABELS)):
        bases, full_indices, direction_rank, pivot_component, external_loops = structural_bases(
            deleted, block_masks, block_bits, pivot_bit
        )
        assert bases and len(set(bases)) == len(bases)
        assert all(base & ~deleted == 0 for base in bases)
        assert all(base.bit_count() == direction_rank + bool(pivot_component) for base in bases)
        assert external_loops & pivot_component == 0
        assert all(external_loops & base == 0 for base in bases)
        obligations = base_exchange_obligations(bases)
        adjacency = exchange_adjacency(bases)
        witness_count = len(bases)
        rho = bases[0].bit_count()
        kind = graph_type(witness_count)
        template_counts[(rho, witness_count, kind)] += 1
        graph_support_counts[kind] += 1
        total_exchange_vertices += witness_count
        total_exchange_edges += sum(len(neighbors) for neighbors in adjacency) // 2
        total_base_exchange_obligations += obligations
        maskwise_verified += 1
        if deleted == ALL_MASK:
            all_deleted_bases = bases
            assert len(full_indices) == 4 and direction_rank == 2 and pivot_component == pivot_bit

    assert maskwise_verified == 65536
    assert all_deleted_bases is not None and len(all_deleted_bases) == 25
    observed_rho_witness = Counter(
        {(rho, witness): count for (rho, witness, _), count in template_counts.items()}
    )
    expected_rho_witness = {
        tuple(int(part) for part in key.split(",")): value
        for key, value in c79["witness_multiplicity_atlas"]["global_rho_witness_counts"].items()
    }
    assert dict(observed_rho_witness) == expected_rho_witness
    assert graph_support_counts == Counter({
        "K1": 60800,
        "K4": 3968,
        "K7": 384,
        "K8": 256,
        "L(K_{1,1,2,5})": 128,
    })
    assert total_exchange_vertices == 84608
    assert total_exchange_edges == 55424

    effective_cycles = c76["source_model"]["effective_generator_cycles"]
    generators = [
        permutation_from_cycles(effective_cycles[name])
        for name in c76["source_model"]["effective_generator_names"]
    ]
    c76_minimal_masks: set[int] = set()
    c76_orbit_rows = c76["full_core_minimality"]["orbit_rows"]
    for row in c76_orbit_rows:
        current_orbit = orbit(row["representative_mask"], generators)
        assert len(current_orbit) == row["orbit_size"]
        c76_minimal_masks.update(current_orbit)
    assert len(c76_minimal_masks) == c76["full_core_minimality"]["support_count"] == 25
    assert c76_minimal_masks == set(all_deleted_bases)

    all_deleted_graph = graph_invariants(all_deleted_bases)
    all_deleted_adjacency = exchange_adjacency(all_deleted_bases)
    all_deleted_graph["degree_by_basis_mask"] = {
        str(mask): len(all_deleted_adjacency[index])
        for index, mask in enumerate(all_deleted_bases)
    }
    assert all_deleted_graph["vertex_count"] == 25
    assert all_deleted_graph["edge_count"] == 128
    assert all_deleted_graph["diameter"] == 2
    assert all_deleted_graph["radius"] == 2
    assert all_deleted_graph["degree_spectrum"] == {"9": 10, "10": 10, "13": 4, "14": 1}
    assert all_deleted_graph["unordered_distinct_pair_distance_spectrum"] == {"1": 128, "2": 172}

    representative_graphs = {
        "K1": [0],
        "K4": [1 << index for index in range(4)],
        "K7": [1 << index for index in range(7)],
        "K8": [1 << index for index in range(8)],
        "L(K_{1,1,2,5})": all_deleted_bases,
    }
    graph_rows = []
    for kind in ("K1", "K4", "K7", "K8", "L(K_{1,1,2,5})"):
        invariants = graph_invariants(representative_graphs[kind])
        graph_rows.append({
            "graph_type": kind,
            "support_count": graph_support_counts[kind],
            **invariants,
        })

    direction_rank_by_witness = {1: 0, 4: 1, 7: 1, 8: 1, 25: 2}
    full_block_description = {
        1: "all identity-block patterns with t<=2",
        4: "[1,1,2]",
        7: "[1,1,5]",
        8: "[1,2,5] (either singleton block)",
        25: "[1,1,2,5]",
    }
    block_pattern_multiplicity = {1: 11, 4: 1, 7: 1, 8: 2, 25: 1}
    template_rows = []
    for rho, witness_count, kind in sorted(template_counts):
        direction_rank = direction_rank_by_witness[witness_count]
        template_rows.append({
            "rho": rho,
            "witness_count": witness_count,
            "support_count": template_counts[(rho, witness_count, kind)],
            "pivot_deleted": bool(rho - direction_rank),
            "direction_rank": direction_rank,
            "fully_deleted_block_count_values": [0, 1, 2] if witness_count == 1 else [direction_rank + 2],
            "fully_deleted_block_size_pattern": full_block_description[witness_count],
            "identity_block_pattern_multiplicity": block_pattern_multiplicity[witness_count],
            "exchange_graph_type": kind,
        })
    assert len(template_rows) == 10 and len(graph_rows) == 5

    result: dict[str, Any] = {
        "schema_id": "hcs-c84-minimum-repair-matroid-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": EXPECTED,
        "source_model": {
            "label_count": 16,
            "pivot": pivot,
            "direction_blocks": blocks,
            "direction_block_sizes": block_sizes,
            "dummy_labels": dummy_labels,
            "c75_ambient_lifted_group_order": 11520,
            "c76_effective_label_group_order": 1920,
            "ambient_and_effective_actions_distinct": True,
        },
        "matroid_theorem": {
            "ground_set": "D",
            "fully_deleted_block_index_set": "I(D)={i:B_i subset D}",
            "fully_deleted_block_count": "t(D)=|I(D)|",
            "direction_rank": "r(D)=max(0,t(D)-2)",
            "external_loops": "D\\(({S9} intersect D) union (union_{i in I(D)} B_i))",
            "optional_pivot_coloop": "{S9} intersect D",
            "direction_component": "Tr_{r(D)}(direct_sum_{i in I(D)} U_{1,|B_i|})",
            "direct_sum_model": "external loops + optional pivot coloop + truncated partition matroid",
            "basis_identification": "Bases(M_D)={minimum restoration witnesses R subset D}",
            "exchange_adjacency": "R~R' iff |R triangle R'|=2",
        },
        "maskwise_verification": {
            "deletion_set_count": maskwise_verified,
            "partition_basis_family_count": maskwise_verified,
            "base_exchange_verified_count": maskwise_verified,
            "base_exchange_ordered_obligation_count": total_base_exchange_obligations,
            "total_exchange_graph_vertices": total_exchange_vertices,
            "total_exchange_graph_edges": total_exchange_edges,
        },
        "rho_witness_template_atlas": {
            "template_count": len(template_rows),
            "rows": template_rows,
        },
        "unlabeled_exchange_graph_atlas": {
            "graph_type_count": len(graph_rows),
            "rows": graph_rows,
        },
        "all_deleted_case": {
            "deleted_mask": ALL_MASK,
            "matroid_rank": 3,
            "basis_count": 25,
            "basis_masks": all_deleted_bases,
            "bases": [labels_for(mask) for mask in all_deleted_bases],
            "c76_full_core_minimal_support_count": 25,
            "c76_full_core_minimal_representative_masks": [
                row["representative_mask"] for row in c76_orbit_rows
            ],
            "c76_full_core_minimal_orbit_sizes": [row["orbit_size"] for row in c76_orbit_rows],
            "equals_c76_full_core_minimal_triples": True,
            "exchange_graph_type": "L(K_{1,1,2,5})",
            "exchange_graph": all_deleted_graph,
        },
        "claims": {
            "all_65536_deletion_sets_enumerated": True,
            "minimum_witness_families_are_matroid_bases": True,
            "base_exchange_verified_for_every_deletion_set": True,
            "ten_rho_witness_templates_exact": True,
            "five_unlabeled_exchange_graph_types_exact": True,
            "all_deleted_25_bases_equal_c76_minimal_triples": True,
            "full_burnside_ring_claimed": False,
            "arithmetic_local_claimed": False,
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "deletion_set_count": maskwise_verified,
        "template_count": len(template_rows),
        "graph_type_count": len(graph_rows),
        "all_deleted_basis_count": len(all_deleted_bases),
        "all_deleted_graph": {
            key: all_deleted_graph[key]
            for key in ("vertex_count", "edge_count", "diameter", "radius", "degree_spectrum")
        },
    }, sort_keys=True))


if __name__ == "__main__":
    main()
