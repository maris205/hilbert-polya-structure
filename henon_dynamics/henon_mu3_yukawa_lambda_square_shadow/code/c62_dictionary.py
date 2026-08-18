#!/usr/bin/env python3
"""C62 G4 fixed-field type dictionary from complete stabilizer sets."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from c62_lambda import closure, from_one, inverse, small_generators

PROJECT = Path(__file__).resolve().parents[1]
C61 = PROJECT.parent / "henon_mu3_yukawa_tensor_fourier_descent"
ATLAS = PROJECT / "results/c62_atlas_evidence.json"
INPUT = C61 / "results/c61_group_evidence.json"
OUTPUT = PROJECT / "results/c62_dictionary_evidence.json"


def compose(left, right):
    return tuple(left[right[i]] for i in range(len(left)))


def conj(g, h):
    return compose(compose(g, h), inverse(g))


def group_from_item(item):
    return frozenset(tuple(x - 1 for x in row) for row in item["stabilizer_elements_one_based"])


def group_digest(group):
    raw = json.dumps([[x + 1 for x in p] for p in sorted(group)], separators=(",", ":")) + "\n"
    return hashlib.sha256(raw.encode()).hexdigest()


def conjugate_subgroup(ambient, source, target):
    if len(source) != len(target):
        return False
    gens = small_generators(source)
    for g in ambient:
        if all(conj(g, h) in target for h in gens):
            return True
    return False


def main():
    source = json.loads(INPUT.read_text())
    atlas = json.loads(ATLAS.read_text())
    ambient_data = source["python_projection"]["ambient"]
    generators = from_one(ambient_data["W_generators_one_based"])
    ambient = closure(generators)
    types = []

    def classify(item):
        subgroup = group_from_item(item)
        for entry in types:
            if conjugate_subgroup(ambient, subgroup, entry["representative"]):
                return entry["type_id"]
        type_id = f"S{len(types) + 1}"
        types.append({
            "type_id": type_id,
            "representative": subgroup,
            "representative_sha256": group_digest(subgroup),
            "order": len(subgroup),
            "core_order": item["core_order"],
            "normalizer_order": item["normalizer_order"],
            "field_degree": 51840 // len(subgroup),
        })
        return type_id

    rows = {}
    for kind, table in atlas["atlases"].items():
        rows[kind] = {}
        for side in ("plus", "minus"):
            out = []
            for row in table["rows"]:
                item = row[side]
                out.append({
                    "orbit_size": row["orbit_size"],
                    "seed": item["seed"],
                    "field_degree": item["field_degree"],
                    "field_type": classify(item),
                    "stabilizer_order": item["stabilizer_order"],
                    "core_order": item["core_order"],
                    "normalizer_order": item["normalizer_order"],
                    "stabilizer_sha256": item["stabilizer_sha256"],
                })
            rows[kind][side] = out

    type_public = []
    for entry in types:
        type_public.append({k: v for k, v in entry.items() if k != "representative"})
    result = {
        "schema_id": "hcs-c62-fixed-field-dictionary-prefreeze-v1",
        "status": "PREFREEZE_G4_PASS",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "authority": {
            "c61_group_evidence_sha256": hashlib.sha256(INPUT.read_bytes()).hexdigest(),
            "c62_atlas_evidence_sha256": hashlib.sha256(ATLAS.read_bytes()).hexdigest(),
            "ambient_order": len(ambient),
        },
        "field_dictionary_policy": "core_free_fixed_fields_grouped_by_ambient_conjugacy; extension criterion remains explicit",
        "type_count": len(type_public),
        "types": type_public,
        "rows": rows,
    }
    OUTPUT.write_bytes((json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode())
    print(json.dumps({
        "status": result["status"],
        "type_count": result["type_count"],
        "exterior_plus_types": sorted({x["field_type"] for x in rows["exterior_square"]["plus"]}),
        "exterior_minus_types": sorted({x["field_type"] for x in rows["exterior_square"]["minus"]}),
        "symmetric_plus_types": sorted({x["field_type"] for x in rows["symmetric_square"]["plus"]}),
        "symmetric_minus_types": sorted({x["field_type"] for x in rows["symmetric_square"]["minus"]}),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
