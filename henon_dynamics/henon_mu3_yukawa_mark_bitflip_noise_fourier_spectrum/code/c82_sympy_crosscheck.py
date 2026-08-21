#!/usr/bin/env python3
"""Independent symbolic Walsh cross-check for C82."""

from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c82_bitflip_noise_fourier_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"


def main():
    evidence = json.loads(EVIDENCE.read_text())
    assert evidence["schema_id"] == "hcs-c82-bitflip-noise-fourier-prefreeze-v1"
    assert evidence["status"] == "PREFREEZE_G3_PASS"
    assert evidence["scope_literal"] == FIREWALL

    # Active coordinates are [S1,S3,S4,S7,S8,S9,S11,S12,S15,S16].  The six
    # omitted labels are dummy variables and contribute a factor 2^6 to every
    # nonzero Walsh coefficient.  This mapping is intentionally explicit.
    blocks = [[0], [9], [3, 8], [1, 2, 4, 6, 7]]
    pivot = 5
    bits = sp.symbols("b0:10")
    signs = sp.symbols("z0:10")
    hits = [1 - sp.prod(1 - bits[i] for i in block) for block in blocks]
    at_least_two = sum(hits[i] * hits[j] for i in range(4) for j in range(i + 1, 4))
    at_least_two -= 2 * sum(hits[i] * hits[j] * hits[k]
                            for i in range(4) for j in range(i + 1, 4)
                            for k in range(j + 1, 4))
    at_least_two += 3 * sp.prod(hits)
    predicate = sp.expand(bits[pivot] * at_least_two)
    signed = sp.Poly(sp.expand(predicate.subs({bits[i]: (1 - signs[i]) / 2
                                                for i in range(10)})), *signs)
    active = {}
    for monomial, coefficient in signed.terms():
        mask = sum(1 << i for i, exponent in enumerate(monomial) if exponent)
        active[mask] = int(sp.expand(coefficient * (1 << 10)))
    full = {mask: value * (1 << 6) for mask, value in active.items() if value}
    spectrum = Counter(full.values())
    # Every Walsh mask not represented by a nonzero active monomial has zero
    # coefficient, including masks containing one of the six dummy bits.
    spectrum[0] += (1 << 16) - len(full)
    energy = Counter()
    for mask, value in full.items():
        energy[mask.bit_count()] += value * value
    assert {str(k): int(v) for k, v in sorted(spectrum.items())} == \
        evidence["walsh_transform"]["coefficient_spectrum"]
    assert len(full) == 1024
    assert max(mask.bit_count() for mask in full) == 10
    assert {str(k): int(energy[k]) for k in range(17)} == \
        evidence["walsh_transform"]["energy_by_degree"]
    assert sum(energy.values()) == (1 << 16) * 30400
    print(json.dumps({"status": "C82_SYMPY_CROSSCHECK_PASS",
                      "active_variables": 10, "dummy_factor": 64,
                      "nonzero_walsh": len(full), "energy_identity": True}, sort_keys=True))


if __name__ == "__main__":
    main()
