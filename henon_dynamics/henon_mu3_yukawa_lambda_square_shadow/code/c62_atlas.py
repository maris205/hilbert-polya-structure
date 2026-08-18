#!/usr/bin/env python3
"""C62 G2 prefreeze atlas: complete stabilizers, cores, and normalizers."""

from __future__ import annotations

import json
from pathlib import Path

from c62_lambda import (
    C61,
    Cosets,
    OUTPUT as LAMBDA_OUTPUT,
    closure,
    compose,
    digest,
    from_one,
    group_digest,
    inverse,
    small_generators,
)

PROJECT = Path(__file__).resolve().parents[1]
INPUT = C61 / "results/c61_group_evidence.json"
OUTPUT = PROJECT / "results/c62_atlas_evidence.json"


def conjugate(g, h):
    return compose(compose(g, h), inverse(g))


def core(ambient_gens, subgroup):
    current = subgroup
    gens = tuple(ambient_gens) + tuple(inverse(g) for g in ambient_gens)
    while True:
        nxt = frozenset(
            h for h in current
            if all(conjugate(g, h) in subgroup for g in gens)
        )
        if nxt == current:
            return current
        current = nxt


def normalizer(ambient, subgroup):
    gens = small_generators(subgroup)
    return frozenset(
        g for g in ambient
        if all(conjugate(g, h) in subgroup for h in gens)
    )


def canonical_group(group):
    return [[x + 1 for x in p] for p in sorted(group)]


def rebuild_atlas(group, generators, subgroup, *, symmetric):
    from c62_lambda import orbit_atlas
    action = Cosets(group, subgroup)
    return orbit_atlas(action, generators, group, symmetric=symmetric)


def public_row(row, group, generators):
    stab = row["stabilizer"]
    cr = core(generators, stab)
    nrm = normalizer(group, stab)
    return {
        "orbit_size": row["orbit_size"],
        "seed": row["seed"],
        "field_degree": len(group) // len(stab),
        "stabilizer_order": len(stab),
        "stabilizer_sha256": group_digest(stab),
        "stabilizer_elements_one_based": canonical_group(stab),
        "core_order": len(cr),
        "core_sha256": group_digest(cr),
        "core_elements_one_based": canonical_group(cr),
        "normalizer_order": len(nrm),
        "normalizer_sha256": group_digest(nrm),
        "normalizer_elements_one_based": canonical_group(nrm),
        "automorphism_order": len(nrm) // len(stab),
    }


def main():
    data = json.loads(INPUT.read_text())
    ambient_data = data["python_projection"]["ambient"]
    generators = from_one(ambient_data["W_generators_one_based"])
    group = closure(generators)
    hp = closure(from_one(ambient_data["Hplus_generators_one_based"]))
    hm = closure(from_one(ambient_data["Hminus_generators_one_based"]))
    if len(group) != 51840 or len(hp) != 162 or len(hm) != 162:
        raise RuntimeError("C61 authority dimensions drifted")

    tables = {}
    for kind, symmetric in (("exterior_square", False), ("symmetric_square", True)):
        plus = rebuild_atlas(group, generators, hp, symmetric=symmetric)
        minus = rebuild_atlas(group, generators, hm, symmetric=symmetric)
        rows = []
        for p, m in zip(plus, minus):
            ps = p["stabilizer"]
            ms = m["stabilizer"]
            rows.append({
                "orbit_size": p["orbit_size"],
                "plus": public_row(p, group, generators),
                "minus": public_row(m, group, generators),
                "stabilizers_conjugate": any(
                    all(conjugate(g, h) in ps for h in small_generators(ms))
                    for g in group
                ),
            })
        tables[kind] = {
            "orbit_count": len(rows),
            "total_size": sum(row["orbit_size"] for row in rows),
            "rows": rows,
        }

    result = {
        "schema_id": "hcs-c62-complete-atlas-prefreeze-v1",
        "status": "PREFREEZE_G2_PASS",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "authority": {
            "c61_group_evidence_sha256": __import__("hashlib").sha256(INPUT.read_bytes()).hexdigest(),
            "ambient_order": len(group),
            "hplus_order": len(hp),
            "hminus_order": len(hm),
            "coset_degree": 320,
        },
        "lambda_evidence_sha256": __import__("hashlib").sha256(LAMBDA_OUTPUT.read_bytes()).hexdigest(),
        "atlases": tables,
    }
    OUTPUT.write_bytes((json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n").encode())
    print(json.dumps({
        "status": result["status"],
        "exterior_rows": tables["exterior_square"]["orbit_count"],
        "symmetric_rows": tables["symmetric_square"]["orbit_count"],
        "exterior_nonconjugate": sum(not x["stabilizers_conjugate"] for x in tables["exterior_square"]["rows"]),
        "symmetric_nonconjugate": sum(not x["stabilizers_conjugate"] for x in tables["symmetric_square"]["rows"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()

