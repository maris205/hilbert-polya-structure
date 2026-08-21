#!/usr/bin/env python3
"""Independent checker for the C82 Walsh/noise certificate."""

from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c82_bitflip_noise_fourier_evidence.json"
C73 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_generation_blocker_reliability"
C76 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas"
C78 = ROOT / "henon_dynamics/henon_mu3_yukawa_mark_repair_distance_geometry"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
N = 16
ALL = (1 << N) - 1
HASHES = {
    "c73": "e91c8e6dcf1de5362b1a052ada83eb758b2c2d75520c1e8bdbd37ab055c725e5",
    "c76": "42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94",
    "c76_manifest": "55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5",
    "c78": "728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae",
    "c78_manifest": "955b5ce23bf811d7377c0e41afd8d7dbc384a467790647e04cf0dadc98347c60",
}


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw):
    return sha256(raw).hexdigest()


def fwht(values):
    result = values[:]
    width = 1
    while width < len(result):
        for start in range(0, len(result), 2 * width):
            for i in range(start, start + width):
                a, b = result[i], result[i + width]
                result[i], result[i + width] = a + b, a - b
        width *= 2
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    raw = args.evidence.read_bytes()
    evidence = json.loads(raw)
    assert raw == canonical(evidence)
    assert evidence["schema_id"] == "hcs-c82-bitflip-noise-fourier-prefreeze-v1"
    assert evidence["status"] == "PREFREEZE_G3_PASS"
    assert evidence["scope_literal"] == FIREWALL
    paths = {
        "c73": C73 / "results/c73_generation_blocker_reliability_evidence.json",
        "c76": C76 / "results/c76_closure_orbit_atlas_evidence.json",
        "c76_manifest": C76 / "C76_PREFREEZE_MANIFEST.json",
        "c78": C78 / "results/c78_repair_distance_geometry_evidence.json",
        "c78_manifest": C78 / "C78_PREFREEZE_MANIFEST.json",
    }
    assert {name: digest(path.read_bytes()) for name, path in paths.items()} == HASHES
    assert evidence["authority"] == HASHES
    c73, c76, c78 = (json.loads(paths[n].read_text()) for n in ("c73", "c76", "c78"))
    assert c73["scope_literal"] == c76["scope_literal"] == c78["scope_literal"] == FIREWALL
    assert c76["source_model"]["support_count"] == 1 << N
    blocks = [[int(label[1:]) - 1 for label in labels]
              for labels in c78["definition"]["direction_blocks"]]
    pivot = int(c78["definition"]["pivot"][1:]) - 1
    assert [len(block) for block in blocks] == [1, 1, 2, 5]
    assert pivot == 8
    assert evidence["predicate"] == {
        "name": "full_core_generation_indicator",
        "variable": "A retained support",
        "definition": "F(A)=1 iff A contains S9 and meets at least two projective direction blocks",
        "pivot": "S9",
        "direction_blocks": c78["definition"]["direction_blocks"],
        "dummy_labels": c78["definition"]["dummy_labels"],
        "support_count": 65536,
        "one_count": 30400,
    }

    def generates(retained):
        return bool(retained & (1 << pivot)) and sum(
            bool(retained & sum(1 << i for i in block)) for block in blocks
        ) >= 2

    truth = [int(generates(mask)) for mask in range(1 << N)]
    assert sum(truth) == 30400
    block_masks = [sum(1 << i for i in block) for block in blocks]
    for retained in range(1 << N):
        deleted = ALL ^ retained
        rho = int(bool(deleted & (1 << pivot))) + max(
            0, sum((deleted & block) == block for block in block_masks) - 2
        )
        assert (truth[retained] == 1) == (rho == 0)

    walsh = fwht(truth)
    spectrum = {str(value): count for value, count in sorted(Counter(walsh).items())}
    nonzero = [mask for mask, value in enumerate(walsh) if value]
    assert len(nonzero) == 1024
    assert max(mask.bit_count() for mask in nonzero) == 10
    energy = Counter()
    for mask, value in enumerate(walsh):
        energy[mask.bit_count()] += value * value
    corr_by_mask = [value // (1 << N) for value in fwht([v * v for v in walsh])]
    distance = Counter()
    for mask, value in enumerate(corr_by_mask):
        assert value >= 0
        distance[mask.bit_count()] += value
    assert sum(distance.values()) == 30400 ** 2
    assert sum(energy.values()) == (1 << N) * 30400

    assert evidence["predicate"]["one_count"] == 30400
    assert evidence["walsh_transform"]["coefficient_spectrum"] == spectrum
    assert evidence["walsh_transform"]["nonzero_coefficient_count"] == 1024
    assert evidence["walsh_transform"]["maximum_fourier_degree"] == 10
    assert evidence["walsh_transform"]["energy_by_degree"] == {
        str(k): energy[k] for k in range(N + 1)
    }
    assert evidence["bitflip_noise"]["autocorrelation_by_distance"] == {
        str(k): distance[k] for k in range(N + 1)
    }
    assert evidence["bitflip_noise"]["parseval_total"] == (1 << N) * 30400
    assert evidence["claims"] == {
        "all_65536_supports_enumerated": True,
        "exact_integer_walsh_spectrum": True,
        "exact_bitflip_autocorrelation": True,
        "arithmetic_local_claimed": False,
        "full_burnside_ring_claimed": False,
    }
    print(json.dumps({
        "status": "C82_INDEPENDENT_CHECK_PASS", "support_count": 65536,
        "one_count": 30400, "nonzero_walsh": len(nonzero),
        "maximum_fourier_degree": 10,
        "noise_by_distance": {str(k): distance[k] for k in range(N + 1)},
    }, sort_keys=True))


if __name__ == "__main__":
    main()
