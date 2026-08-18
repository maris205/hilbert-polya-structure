#!/usr/bin/env python3
"""C63 exact 16-type Burnside linearization kernel producer."""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Iterable

REPO = Path(__file__).resolve().parents[3]
C61 = REPO / "henon_dynamics/henon_mu3_yukawa_tensor_fourier_descent"
C62 = REPO / "henon_dynamics/henon_mu3_yukawa_lambda_square_shadow"
INPUT_C61 = C61 / "results/c61_group_evidence.json"
INPUT_ATLAS = C62 / "results/c62_atlas_evidence.json"
INPUT_DICT = C62 / "results/c62_dictionary_evidence.json"
OUTPUT = Path(__file__).resolve().parents[1] / "results/c63_kernel_evidence.json"

EXPECTED_C61_SHA256 = "f4be3a2c5990120a97264505ba9f21b55b8f8c330521044936a52f68e8cd89e9"
EXPECTED_ATLAS_SHA256 = "3c40a674779a0e2d6d1c69b7c4ccc9115c4b9a2ba049684e8c5204b94b621c40"
EXPECTED_DICT_SHA256 = "85dc05d043e3781631330083303b98995201c7c30b53aae2901d5fd874b6cd5e"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"

Perm = tuple[int, ...]


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def compose(left: Perm, right: Perm) -> Perm:
    return tuple(left[right[i]] for i in range(len(left)))


def inverse(p: Perm) -> Perm:
    out = [0] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def from_one(rows: Iterable[Iterable[int]]) -> tuple[Perm, ...]:
    return tuple(tuple(x - 1 for x in row) for row in rows)


def to_one(p: Perm) -> list[int]:
    return [x + 1 for x in p]


def closure(generators: Iterable[Perm]) -> frozenset[Perm]:
    gens = tuple(generators)
    if not gens:
        raise ValueError("empty generator list")
    identity = tuple(range(len(gens[0])))
    out = {identity}
    stack = [identity]
    while stack:
        x = stack.pop()
        for g in gens:
            y = compose(g, x)
            if y not in out:
                out.add(y)
                stack.append(y)
    return frozenset(out)


def subgroup_generators(group: frozenset[Perm]) -> tuple[Perm, ...]:
    identity = tuple(range(len(next(iter(group)))))
    chosen: list[Perm] = []
    current = frozenset({identity})
    for g in sorted(group):
        if g in current:
            continue
        chosen.append(g)
        current = closure(chosen)
        if current == group:
            return tuple(chosen)
    raise RuntimeError("failed to generate subgroup")


def group_digest(group: frozenset[Perm]) -> str:
    return sha256_bytes(canonical([[x + 1 for x in p] for p in sorted(group)]))


def conjugate_subgroup(ambient: frozenset[Perm], source: frozenset[Perm], target: frozenset[Perm]) -> bool:
    if len(source) != len(target):
        return False
    gens = subgroup_generators(source)
    for g in ambient:
        gi = inverse(g)
        if all(compose(compose(g, h), gi) in target for h in gens):
            return True
    return False


def conjugacy_classes(ambient: frozenset[Perm], generators: tuple[Perm, ...]) -> list[frozenset[Perm]]:
    inverses = tuple(inverse(g) for g in generators)
    unseen = set(ambient)
    classes: list[frozenset[Perm]] = []
    while unseen:
        seed = min(unseen)
        orbit = {seed}
        stack = [seed]
        while stack:
            z = stack.pop()
            for g, gi in zip(generators, inverses):
                y = compose(compose(g, z), gi)
                if y not in orbit:
                    orbit.add(y)
                    stack.append(y)
        unseen.difference_update(orbit)
        classes.append(frozenset(orbit))
    classes.sort(key=lambda c: min(c))
    return classes


def rank_q(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0
    a = [[Fraction(x) for x in row] for row in matrix]
    rows, cols = len(a), len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = a[rank][col]
        a[rank] = [x / scale for x in a[rank]]
        for r in range(rows):
            if r == rank or not a[r][col]:
                continue
            scale = a[r][col]
            a[r] = [x - scale * y for x, y in zip(a[r], a[rank])]
        rank += 1
        if rank == rows:
            break
    return rank


def vector_for_rows(rows: list[dict[str, object]], side_key: str, signs: dict[str, int], type_pos: dict[str, int]) -> list[int]:
    out = [0] * len(type_pos)
    for row in rows:
        for side, sign in signs.items():
            out[type_pos[row[side]["field_type"]]] += sign
    return out


def main() -> None:
    raw_c61 = INPUT_C61.read_bytes()
    raw_atlas = INPUT_ATLAS.read_bytes()
    raw_dict = INPUT_DICT.read_bytes()
    source_hashes = {
        "c61_group_evidence_sha256": sha256_bytes(raw_c61),
        "c62_atlas_evidence_sha256": sha256_bytes(raw_atlas),
        "c62_dictionary_evidence_sha256": sha256_bytes(raw_dict),
    }
    assert source_hashes["c61_group_evidence_sha256"] == EXPECTED_C61_SHA256
    assert source_hashes["c62_atlas_evidence_sha256"] == EXPECTED_ATLAS_SHA256
    assert source_hashes["c62_dictionary_evidence_sha256"] == EXPECTED_DICT_SHA256

    c61 = json.loads(raw_c61)
    atlas = json.loads(raw_atlas)
    dictionary = json.loads(raw_dict)
    assert atlas["schema_id"] == "hcs-c62-complete-atlas-prefreeze-v1"
    assert atlas["status"] == "PREFREEZE_G2_PASS"
    assert atlas["scope_literal"] == FIREWALL
    assert dictionary["schema_id"] == "hcs-c62-fixed-field-dictionary-prefreeze-v1"
    assert dictionary["status"] == "PREFREEZE_G4_PASS"
    assert dictionary["scope_literal"] == FIREWALL

    ambient_data = c61["python_projection"]["ambient"]
    wgens = from_one(ambient_data["W_generators_one_based"])
    ambient = closure(wgens)
    hplus = closure(from_one(ambient_data["Hplus_generators_one_based"]))
    hminus = closure(from_one(ambient_data["Hminus_generators_one_based"]))
    assert len(ambient) == 51840
    assert len(hplus) == len(hminus) == 162

    type_ids = sorted((item["type_id"] for item in dictionary["types"]), key=lambda x: int(x[1:]))
    assert type_ids == [f"S{i}" for i in range(1, 17)]
    type_pos = {type_id: i for i, type_id in enumerate(type_ids)}

    atlas_by_digest: dict[str, frozenset[Perm]] = {}
    for table in atlas["atlases"].values():
        for row in table["rows"]:
            for side in ("plus", "minus"):
                item = row[side]
                subgroup = frozenset(tuple(x - 1 for x in p) for p in item["stabilizer_elements_one_based"])
                assert group_digest(subgroup) == item["stabilizer_sha256"]
                atlas_by_digest[item["stabilizer_sha256"]] = subgroup

    type_subgroups: dict[str, frozenset[Perm]] = {}
    type_meta = {item["type_id"]: item for item in dictionary["types"]}
    for type_id in type_ids:
        meta = type_meta[type_id]
        subgroup = atlas_by_digest[meta["representative_sha256"]]
        assert len(subgroup) == meta["order"]
        assert meta["core_order"] == 1
        assert meta["field_degree"] * meta["order"] == 51840
        type_subgroups[type_id] = subgroup

    hplus_type = [t for t, s in type_subgroups.items() if conjugate_subgroup(ambient, hplus, s)]
    hminus_type = [t for t, s in type_subgroups.items() if conjugate_subgroup(ambient, hminus, s)]
    assert hplus_type == ["S15"]
    assert hminus_type == ["S16"]
    assert not conjugate_subgroup(ambient, hplus, hminus)

    classes = conjugacy_classes(ambient, wgens)
    assert len(classes) == 25 and sum(len(c) for c in classes) == len(ambient)
    class_pos = {g: i for i, c in enumerate(classes) for g in c}
    class_meta = []
    for i, c in enumerate(classes, start=1):
        class_meta.append({
            "class_id": i,
            "representative_one_based": to_one(min(c)),
            "size": len(c),
            "centralizer_order": len(ambient) // len(c),
        })

    def character(subgroup: frozenset[Perm]) -> list[int]:
        counts = [0] * len(classes)
        for x in subgroup:
            counts[class_pos[x]] += 1
        values = []
        for k, c in enumerate(classes):
            numerator = (len(ambient) // len(c)) * counts[k]
            assert numerator % len(subgroup) == 0
            values.append(numerator // len(subgroup))
        return values

    columns = [character(type_subgroups[t]) for t in type_ids]
    matrix = [list(row) for row in zip(*columns)]
    rank = rank_q(matrix)
    assert rank == 13

    def sparse(values: dict[str, int]) -> list[int]:
        out = [0] * len(type_ids)
        for key, value in values.items():
            out[type_pos[key]] = value
        return out

    z1 = sparse({"S10": 1, "S9": -1})
    z2 = sparse({"S2": -1, "S3": -1, "S5": -1, "S6": -1, "S11": 1, "S12": 1, "S13": 1, "S14": 1})
    z3 = sparse({"S16": 1, "S15": -1})
    relation_rows = {kind: dictionary["rows"][kind]["plus"] for kind in dictionary["rows"]}
    # Build plus-minus vectors directly from the full dictionary rows.
    def relation(kind: str) -> list[int]:
        out = [0] * len(type_ids)
        for row in dictionary["rows"][kind]["plus"]:
            out[type_pos[row["field_type"]]] += 1
        for row in dictionary["rows"][kind]["minus"]:
            out[type_pos[row["field_type"]]] -= 1
        return out

    q_ext = relation("exterior_square")
    q_sym = relation("symmetric_square")
    r_c61 = sparse({"S15": 1, "S16": -1})
    assert q_ext == sparse({"S2": 1, "S3": 1, "S5": 1, "S6": 1, "S11": -1, "S12": -1, "S13": -1, "S14": -1})
    assert q_sym == [a + b for a, b in zip(q_ext, r_c61)]
    primitive_support = [i for i, value in enumerate(q_ext) if value]
    support_matrix = [[row[i] for i in primitive_support] for row in matrix]
    support_rank = rank_q(support_matrix)
    assert len(primitive_support) == 8 and support_rank == 7
    exterior_pairing = []
    for row, minus in zip(dictionary["rows"]["exterior_square"]["plus"], dictionary["rows"]["exterior_square"]["minus"]):
        # The dictionary carries the conjugacy labels; equal labels cancel.
        exterior_pairing.append({
            "orbit_size": row["orbit_size"],
            "plus_type": row["field_type"],
            "minus_type": minus["field_type"],
            "nonconjugate_type_pair": row["field_type"] != minus["field_type"],
        })
    for vector in (z1, z2, z3, q_ext, q_sym, r_c61):
        assert all(sum(matrix[i][j] * vector[j] for j in range(len(type_ids))) == 0 for i in range(len(matrix)))
    assert rank_q([z1, z2, z3]) == 3
    common_hplus = character(hplus)
    common_hminus = character(hminus)
    assert common_hplus == common_hminus

    result = {
        "schema_id": "hcs-c63-burnside-kernel-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "authority": {**source_hashes, "ambient_order": len(ambient), "class_count": len(classes), "type_count": len(type_ids)},
        "types": [{
            "type_id": t,
            "subgroup_order": len(type_subgroups[t]),
            "field_degree": type_meta[t]["field_degree"],
            "stabilizer_sha256": type_meta[t]["representative_sha256"],
        } for t in type_ids],
        "hplus_type": hplus_type[0],
        "hminus_type": hminus_type[0],
        "conjugacy_classes": class_meta,
        "character_matrix": matrix,
        "column_order": type_ids,
        "common_hplus_hminus_character": common_hplus,
        "rank_over_Q": rank,
        "nullity_over_Q": len(type_ids) - rank,
        "nullspace_basis": {"z1": z1, "z2": z2, "z3": z3},
        "relation_vectors": {"r_c61": r_c61, "q_exterior": q_ext, "q_symmetric": q_sym},
        "primitive_support": {
            "type_ids": [type_ids[i] for i in primitive_support],
            "support_size": len(primitive_support),
            "restricted_rank_over_Q": support_rank,
            "restricted_nullity_over_Q": len(primitive_support) - support_rank,
            "exterior_pairing": exterior_pairing,
        },
        "matrix_sha256": sha256_bytes(canonical(matrix)),
        "claims": {
            "restricted_16_type_kernel_only": True,
            "full_burnside_ring_kernel_claimed": False,
            "arithmetic_local_claimed": False,
        },
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "ambient_order": len(ambient),
        "class_count": len(classes),
        "type_count": len(type_ids),
        "rank_over_Q": rank,
        "nullity_over_Q": len(type_ids) - rank,
        "matrix_sha256": result["matrix_sha256"],
        "hplus_type": result["hplus_type"],
        "hminus_type": result["hminus_type"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
