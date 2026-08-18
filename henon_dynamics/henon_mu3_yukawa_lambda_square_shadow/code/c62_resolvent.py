#!/usr/bin/env python3
"""C62 G3 product-form marker resolvents and split-prime noncollision."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from c62_lambda import Cosets, closure, digest, from_one, inverse

PROJECT = Path(__file__).resolve().parents[1]
C61 = PROJECT.parent / "henon_mu3_yukawa_tensor_fourier_descent"
INPUT = C61 / "results/c61_group_evidence.json"
OUTPUT = PROJECT / "results/c62_resolvent_evidence.json"
PRIME = 692717
BASE = 512


def orbit_rows(action, generators, symmetric):
    n = action.degree
    unseen = {(i, j) for i in range(n) for j in range(i, n if symmetric else n) if symmetric or i < j}
    gens = tuple(generators) + tuple(inverse(g) for g in generators)
    rows = []
    while unseen:
        seed = min(unseen)
        seen = {seed}
        stack = [seed]
        while stack:
            a, b = stack.pop()
            for g in gens:
                x, y = action.image(g, a), action.image(g, b)
                z = (x, y) if x <= y else (y, x)
                if z not in seen:
                    seen.add(z)
                    stack.append(z)
        unseen.difference_update(seen)
        rows.append((len(seen), seed, sorted(seen)))
    return sorted(rows, key=lambda row: (row[0], row[1]))


def marker(pair):
    i, j = pair
    return BASE * (i + 1) + (j + 1)


def build_table(group, generators, subgroup, symmetric):
    action = Cosets(group, subgroup)
    table = []
    for size, seed, pairs in orbit_rows(action, generators, symmetric):
        values = [marker(pair) % PRIME for pair in pairs]
        table.append({
            "orbit_size": size,
            "seed": list(seed),
            "orbit_pairs": [list(pair) for pair in pairs],
            "carrier": {
                "kind": "product_form_marker",
                "variable": "T",
                "factor": f"T-({BASE}*X_i+X_j)",
                "terms": size,
                "monic": True,
                "expanded_characteristic_zero_coefficients_claimed": False,
            },
            "marker_base": BASE,
            "marker_values_mod_prime": values,
            "marker_values_sha256": hashlib.sha256(
                (json.dumps(values, separators=(",", ":")) + "\n").encode()
            ).hexdigest(),
            "noncollision_count": len(set(values)),
            "formal_orbit_sha256": digest([list(pair) for pair in pairs]),
        })
    return table


def main():
    source = json.loads(INPUT.read_text())
    ambient = source["python_projection"]["ambient"]
    generators = from_one(ambient["W_generators_one_based"])
    group = closure(generators)
    hp = closure(from_one(ambient["Hplus_generators_one_based"]))
    hm = closure(from_one(ambient["Hminus_generators_one_based"]))
    tables = {}
    for kind, symmetric in (("exterior_square", False), ("symmetric_square", True)):
        tables[kind] = {
            "plus": build_table(group, generators, hp, symmetric),
            "minus": build_table(group, generators, hm, symmetric),
        }
    for table in tables.values():
        for side in table.values():
            for row in side:
                if row["noncollision_count"] != row["orbit_size"]:
                    raise RuntimeError("marker noncollision failed")
                if max(row["marker_values_mod_prime"]) >= PRIME:
                    raise RuntimeError("marker escaped split-prime range")
    result = {
        "schema_id": "hcs-c62-product-form-resolvent-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "authority": {
            "c61_group_evidence_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
            "ambient_order": len(group),
            "hplus_order": len(hp),
            "hminus_order": len(hm),
            "coset_degree": 320,
        },
        "marker_contract": {
            "prime": PRIME,
            "base": BASE,
            "encoding": "512*(zero_based_pair_first+1)+(zero_based_pair_second+1)",
            "expanded_characteristic_zero_coefficients_claimed": False,
        },
        "tables": tables,
    }
    OUTPUT.write_bytes((json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode())
    print(json.dumps({
        "status": result["status"],
        "exterior_rows": len(tables["exterior_square"]["plus"]),
        "symmetric_rows": len(tables["symmetric_square"]["plus"]),
        "all_noncollision": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
