#!/usr/bin/env python3
"""Produce the exact Walsh/noise certificate for the C78 full-core predicate."""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
C73 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability"
C76 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas"
C78 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_repair_distance_geometry"
OUT = PROJECT / "results/c82_bitflip_noise_fourier_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
N = 16
ALL = (1 << N) - 1
EXPECTED = {
    "c73": "e91c8e6dcf1de5362b1a052ada83eb758b2c2d75520c1e8bdbd37ab055c725e5",
    "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
    "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
    "c78": "728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae",
    "c78_manifest": "955b5ce23bf811d7377c0e41afd8d7dbc384a467790647e04cf0dadc98347c60",
}


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def fwht(values: list[int]) -> list[int]:
    result = values[:]
    width = 1
    while width < len(result):
        for start in range(0, len(result), 2 * width):
            for index in range(start, start + width):
                left, right = result[index], result[index + width]
                result[index], result[index + width] = left + right, left - right
        width *= 2
    return result


def main() -> None:
    paths = {
        "c73": C73 / "results/c73_generation_blocker_reliability_evidence.json",
        "c76": C76 / "results/c76_closure_orbit_atlas_evidence.json",
        "c76_manifest": C76 / "C76_PREFREEZE_MANIFEST.json",
        "c78": C78 / "results/c78_repair_distance_geometry_evidence.json",
        "c78_manifest": C78 / "C78_PREFREEZE_MANIFEST.json",
    }
    raw = {name: path.read_bytes() for name, path in paths.items()}
    assert {name: digest(value) for name, value in raw.items()} == EXPECTED
    c73 = json.loads(raw["c73"])
    c76 = json.loads(raw["c76"])
    c78 = json.loads(raw["c78"])
    assert all(doc["scope_literal"] == FIREWALL for doc in (c73, c76, c78))
    assert c78["status"] == "PREFREEZE_G3_PASS"
    assert c78["claims"]["all_65536_deletion_sets_enumerated"]
    assert c76["source_model"]["support_count"] == 1 << N
    blocks = [
        [int(label[1:]) - 1 for label in labels]
        for labels in c78["definition"]["direction_blocks"]
    ]
    pivot = int(c78["definition"]["pivot"][1:]) - 1
    dummies = [int(label[1:]) - 1 for label in c78["definition"]["dummy_labels"]]
    assert [len(block) for block in blocks] == [1, 1, 2, 5]
    assert pivot == 8 and len(dummies) == 6

    def generates(retained: int) -> bool:
        return bool(retained & (1 << pivot)) and sum(
            bool(retained & sum(1 << i for i in block)) for block in blocks
        ) >= 2

    truth = [int(generates(mask)) for mask in range(1 << N)]
    assert sum(truth) == 30400
    # C78's exact distance-zero boundary is checked mask-by-mask, not merely
    # by comparing the marginal distribution.  This prevents a swapped
    # deletion/retained convention from passing the receipt.
    block_masks = [sum(1 << i for i in block) for block in blocks]
    pivot_bit = 1 << pivot
    for retained in range(1 << N):
        deleted = ALL ^ retained
        rho = int(bool(deleted & pivot_bit)) + max(
            0, sum((deleted & block) == block for block in block_masks) - 2
        )
        assert (truth[retained] == 1) == (rho == 0)

    walsh = fwht(truth)
    spectrum = Counter(walsh)
    nonzero_masks = [mask for mask, coefficient in enumerate(walsh) if coefficient]
    assert len(nonzero_masks) == 1024
    assert max(mask.bit_count() for mask in nonzero_masks) == 10
    energy_by_degree = Counter()
    for mask, coefficient in enumerate(walsh):
        energy_by_degree[mask.bit_count()] += coefficient * coefficient
    squared = [coefficient * coefficient for coefficient in walsh]
    autocorrelation_transform = fwht(squared)
    autocorrelation = [value // (1 << N) for value in autocorrelation_transform]
    assert all(value >= 0 for value in autocorrelation)
    noise_by_distance = Counter()
    for mask, value in enumerate(autocorrelation):
        noise_by_distance[mask.bit_count()] += value
    assert sum(noise_by_distance.values()) == sum(truth) ** 2
    assert sum(energy_by_degree.values()) == (1 << N) * sum(truth)

    result: dict[str, Any] = {
        "schema_id": "hcs-c82-bitflip-noise-fourier-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": EXPECTED,
        "predicate": {
            "name": "full_core_generation_indicator",
            "variable": "A retained support",
            "definition": "F(A)=1 iff A contains S9 and meets at least two projective direction blocks",
            "pivot": "S9",
            "direction_blocks": c78["definition"]["direction_blocks"],
            "dummy_labels": c78["definition"]["dummy_labels"],
            "support_count": 1 << N,
            "one_count": sum(truth),
        },
        "walsh_transform": {
            "convention": "W(S)=sum_A F(A)(-1)^|A cap S|",
            "nonzero_coefficient_count": len(nonzero_masks),
            "maximum_fourier_degree": max(mask.bit_count() for mask in nonzero_masks),
            "coefficient_spectrum": {str(value): count for value, count in sorted(spectrum.items())},
            "energy_by_degree": {str(degree): energy_by_degree[degree] for degree in range(N + 1)},
        },
        "bitflip_noise": {
            "ordered_pair_convention": "C_h=sum_{d_H(A,B)=h} F(A)F(B)",
            "autocorrelation_by_distance": {str(distance): noise_by_distance[distance] for distance in range(N + 1)},
            "normalized_noise_formula": "NS(epsilon)=2^-16 sum_h C_h epsilon^h(1-epsilon)^(16-h)",
            "fourier_noise_formula": "NS(epsilon)=2^-32 sum_S W(S)^2(1-2epsilon)^|S|",
            "parseval_total": sum(energy_by_degree.values()),
        },
        "claims": {
            "all_65536_supports_enumerated": True,
            "exact_integer_walsh_spectrum": True,
            "exact_bitflip_autocorrelation": True,
            "arithmetic_local_claimed": False,
            "full_burnside_ring_claimed": False,
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "support_count": 1 << N,
        "one_count": sum(truth),
        "nonzero_walsh": len(nonzero_masks),
        "maximum_fourier_degree": max(mask.bit_count() for mask in nonzero_masks),
        "noise_by_distance": result["bitflip_noise"]["autocorrelation_by_distance"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
