#!/usr/bin/env python3
"""SymPy/GAP cross-check for the C70 group orders and orbit masses."""

from __future__ import annotations

from collections import Counter
import json
from math import prod
from pathlib import Path
import subprocess

import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c70_direct_factor_orbit_evidence.json"


def gl_order(p: int, dimension: int) -> int:
    return prod(p ** dimension - p ** i for i in range(dimension))


def aut_order(p: int, exponents: list[int]) -> int:
    endomorphisms_exp = sum(min(a, b) for a in exponents for b in exponents)
    blocks = Counter(exponents)
    return p ** (endomorphisms_exp - sum(m * m for m in blocks.values())) * prod(
        gl_order(p, m) for m in blocks.values())


def qbinomial(n: int, k: int, q: int) -> int:
    numerator = prod(q ** (n - i) - 1 for i in range(k))
    denominator = prod(q ** (k - i) - 1 for i in range(k))
    return numerator // denominator


def main() -> None:
    ev = json.loads(EVIDENCE.read_text())
    t = ev["primary_types"]
    aut_c = aut_order(2, t["C2"]) * aut_order(3, t["C3"])
    aut_d = aut_order(2, t["D2"])
    aut_k = aut_order(2, t["K2"]) * aut_order(3, t["K3"])
    gap = subprocess.run(
        ["gap", "-q"],
        input='D:=AbelianGroup([2,2,8]);; Print(Size(AutomorphismGroup(D)),"\\n"); QUIT;\n',
        capture_output=True, text=True, check=True,
    )
    assert int(gap.stdout.strip()) == aut_d == 384
    assert {str(p): e for p, e in sp.factorint(aut_c).items()} == ev["automorphism_prime_factorizations"]["Aut_C"]
    assert {str(p): e for p, e in sp.factorint(aut_k).items()} == ev["automorphism_prime_factorizations"]["Aut_K"]
    hom = 2 ** sum(min(a, b) for a in t["K2"] for b in t["D2"])
    factors = aut_c // (aut_d * aut_k * hom)
    decompositions = aut_c // (aut_d * aut_k)
    assert factors == ev["direct_factor_count"]
    assert decompositions == ev["ordered_decomposition_count"] == factors * hom
    split_embeddings = factors * aut_d
    all_subgroups = 2 ** 16 * qbinomial(14, 2, 2) * qbinomial(2, 1, 2)
    assert split_embeddings == ev["split_embedding_count"]
    assert all_subgroups == ev["all_D_subgroup_count"]
    assert all_subgroups - factors == ev["nondirect_D_subgroup_count"]
    print(json.dumps({"status": "GROUP_CROSSCHECK_PASS", "gap_Aut_D": aut_d,
                      "direct_factor_count": factors,
                      "ordered_decomposition_count": decompositions,
                      "split_embedding_count": split_embeddings,
                      "all_D_subgroup_count": all_subgroups,
                      "hom_K_D": hom}, sort_keys=True))


if __name__ == "__main__":
    main()
