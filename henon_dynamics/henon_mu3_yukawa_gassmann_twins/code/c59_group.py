#!/usr/bin/env python3
"""Strict staged producer for the C59 finite-group evidence carrier.

The field groups and the two p=3 decomposition/inertia filtrations are
defined by immutable permutation arrays below.  TomLib is used only by the
independent GAP checker to locate those frozen groups and exhaust all 350
subgroup classes.  This Python implementation separately rebuilds the
permutation groups, supports, cores, normalizers, derived groups, coset
orbits, and complete local rows, then deep-compares its projection with GAP.
"""

from __future__ import annotations

import argparse
from collections import deque
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from typing import Any, Iterable, Sequence


SCHEMA_ID = "hcs-c59-group-evidence-v1"
CHECKER_SCHEMA_ID = "hcs-c59-checker-group-projection-v1"
EXPECTED_REPO_ROOT = Path("/root/autodl-tmp/hilbert-polya-structure")
GAP_EXECUTABLE = Path("/usr/bin/gap")
GAP_SHA256 = "9aa736f13150c363d7c31d33513d849482dd52692e7534f51ecfac0d303bb1e3"
DESIGN_ONLY_FROZEN_EMBEDDING_SHA256 = (
    "7cc3089bcd474a8f7787f60c81f37158042d85afbab84a5bf28a6fe75a8f46de"
)

PREDECESSORS = (
    (
        "C56 certificate",
        "henon_dynamics/henon_mu3_yukawa_line_field/results/c56_certificate.json",
        "26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4",
    ),
    (
        "C58 group evidence",
        "henon_dynamics/henon_mu3_yukawa_line_ramification/results/c58_group_evidence.json",
        "0e0b3fd4927b3a8355037b57b86a1e3cc7efe15832be4f5ca76cb4989b71a1fd",
    ),
    (
        "C58 certificate",
        "henon_dynamics/henon_mu3_yukawa_line_ramification/results/c58_certificate.json",
        "456a481368d593f0d015436bf8a3a518d15b4567880fa7726c77d29a259d79ee",
    ),
    (
        "C58 group source",
        "henon_dynamics/henon_mu3_yukawa_line_ramification/code/c58_group.py",
        "3026e890d80272395e767278a8f4f7f4aac02ac718e01f0a4c94949406cc946d",
    ),
)

PLANNED_CODE_INVENTORY = [
    "README.md",
    "c59_atomic_promote.py",
    "c59_checker.py",
    "c59_checker_group.g",
    "c59_checker_resolvent.py",
    "c59_exact.py",
    "c59_group.py",
    "c59_hash_manifest.py",
    "c59_pipeline.py",
    "c59_producer.py",
    "c59_resolvent.py",
    "run_all.sh",
    "test_c59.py",
]
PLANNED_RESULT_INVENTORY = [
    "RESULTS.md",
    "TEST_REPORT.md",
    "c59_certificate.json",
    "c59_check_report.json",
    "c59_group_evidence.json",
    "c59_resolvent_evidence.json",
    "c59_schema.json",
    "scoped_hash_manifest.json",
]
CERTIFICATE_PAYLOAD_TOP_LEVEL_KEYS = [
    "artifact_contract",
    "G0_released_authority_rebind",
    "G1_primitive_orbit_resolvents",
    "G2_gassmann_minimality",
    "G3_fixed_fields_and_zeta",
    "G4_global_arithmetic",
    "G5_tom140_local_algebra",
    "G6_tom206_local_algebra",
    "G7_independence_scope_release",
    "written_bridges",
    "backend_contract",
    "source_contract",
    "scope_nonclaims",
    "nonresults",
    "status",
]

EXPECTED_COLLISION_BUCKETS = [
    [12, 15],
    [17, 21],
    [29, 36],
    [31, 39],
    [41, 42],
    [46, 48],
    [57, 58],
    [59, 64],
    [112, 120],
    [132, 140],
    [301, 303],
]
EXPECTED_ORBIT_COUNTS = [36, 56, 112, 16, 64, 128, 160, 168]
EXPECTED_CONDUCTORS = [624, 496, 192, 160]
EXPECTED_SIGNATURE = [16, 152]
EXPECTED_LOCAL_TOM_INDICES = [140, 72, 7, 147, 23, 6, 2, 5]
DISCRIMINANT_FACTORIZATION = [
    [3, 624],
    [5, 496],
    [181, 192],
    [283, 160],
    [997, 192],
    [1801, 160],
    [2346241, 192],
    [14932047182473291995860108491583652133938007263719, 160],
]
DISCRIMINANT_SHA256 = (
    "7f3ed0f731e5905f9af8254df2114ad15c2bb7d96cfa9a8b464a58ae8ea3ae70"
)

W27_ARRAYS = [
    [2,1,3,4,5,6,7,12,13,14,15,8,9,10,11,16,17,18,19,20,21,23,22,24,25,26,27],
    [1,3,2,4,5,6,8,7,9,10,11,12,16,17,18,13,14,15,19,20,21,22,24,23,25,26,27],
    [1,2,4,3,5,6,7,9,8,10,11,13,12,14,15,16,19,20,17,18,21,22,23,25,24,26,27],
    [1,2,3,5,4,6,7,8,10,9,11,12,14,13,15,17,16,18,19,21,20,22,23,24,26,25,27],
    [1,2,3,4,6,5,7,8,9,11,10,12,13,15,14,16,18,17,20,19,21,22,23,24,25,27,26],
    [12,8,7,4,5,6,3,2,9,10,11,1,13,14,15,16,17,18,27,26,25,22,23,24,21,20,19],
]
H301_ARRAYS = [
    [1,2,19,21,20,3,24,11,9,10,23,15,13,14,22,5,4,18,6,16,17,12,8,27,25,26,7],
    [16,27,13,12,22,26,15,25,24,7,14,18,20,5,1,23,8,17,9,19,6,2,10,3,4,21,11],
    [26,13,22,20,24,15,21,3,14,1,19,11,25,18,23,7,5,9,12,27,16,8,6,17,2,10,4],
]
H303_ARRAYS = [
    [5,1,6,2,3,4,10,21,14,17,19,11,7,8,9,15,18,20,12,13,16,26,22,27,23,24,25],
    [7,15,13,12,26,5,16,18,20,1,22,8,9,6,27,11,4,25,3,24,14,10,21,19,17,23,2],
    [16,23,9,8,26,27,7,25,24,10,11,12,13,6,5,22,17,18,19,20,2,1,21,3,4,15,14],
]
BRANCH140_D_ARRAYS = [
    [7,26,13,12,5,15,1,18,20,22,16,4,3,14,6,11,25,8,24,9,27,10,23,19,17,2,21],
    [17,2,21,4,18,1,15,5,20,3,11,12,22,14,25,16,6,8,19,23,10,27,9,24,7,26,13],
    [23,24,22,19,21,20,1,3,15,13,14,2,18,16,17,11,9,10,26,25,27,8,7,12,6,4,5],
]
BRANCH140_P_ARRAYS = [
    [7,12,8,26,27,25,23,22,17,18,16,24,10,11,9,14,15,13,4,6,5,3,1,2,20,19,21],
    [25,12,18,26,22,15,20,13,1,5,16,24,21,11,23,14,7,27,4,17,8,10,6,2,9,19,3],
]
BRANCH140_Q_ARRAYS = [
    [6,2,10,4,8,17,25,18,23,21,11,12,27,14,7,16,1,5,19,9,3,13,20,24,15,26,22],
]
BRANCH206_D_ARRAYS = [
    [1,2,20,16,5,18,26,8,11,23,9,12,15,22,13,4,17,6,21,3,19,14,10,24,27,7,25],
    [5,2,3,4,1,6,14,17,19,10,21,12,13,7,15,16,8,18,9,20,11,26,23,24,25,22,27],
    [11,7,26,24,25,15,22,14,12,13,27,21,18,20,23,4,3,10,5,8,9,2,6,16,19,17,1],
]
BRANCH206_I_ARRAYS = [
    [1,17,22,16,12,18,26,8,25,23,27,5,15,20,13,4,2,6,21,14,19,3,10,24,9,7,11],
    [11,7,26,24,25,15,22,14,12,13,27,21,18,20,23,4,3,10,5,8,9,2,6,16,19,17,1],
    [12,17,14,4,1,6,3,2,19,10,21,5,13,7,15,16,8,18,27,22,25,26,23,24,11,20,9],
]
BRANCH206_P_ARRAYS = [
    [11,7,26,24,25,15,22,14,12,13,27,21,18,20,23,4,3,10,5,8,9,2,6,16,19,17,1],
    [12,17,14,4,1,6,3,2,19,10,21,5,13,7,15,16,8,18,27,22,25,26,23,24,11,20,9],
]
BRANCH206_Q_ARRAYS = [
    [12,17,14,4,1,6,3,2,19,10,21,5,13,7,15,16,8,18,27,22,25,26,23,24,11,20,9],
]

FROZEN_ARRAYS = {
    "branch140_D_generators": BRANCH140_D_ARRAYS,
    "branch140_P_generators": BRANCH140_P_ARRAYS,
    "branch140_Q_generators": BRANCH140_Q_ARRAYS,
    "branch206_D_generators": BRANCH206_D_ARRAYS,
    "branch206_I_generators": BRANCH206_I_ARRAYS,
    "branch206_P_generators": BRANCH206_P_ARRAYS,
    "branch206_Q_generators": BRANCH206_Q_ARRAYS,
    "h301_generators": H301_ARRAYS,
    "h303_generators": H303_ARRAYS,
    "w27_simple_reflection_generators": W27_ARRAYS,
}

EXPECTED_ROWS = {
    "D140": {
        "H301": [[[1,1,1,0],8],[[6,6,1,11],10],[[9,9,1,18],8],[[18,18,1,37],10]],
        "H303": [[[2,2,1,1],4],[[3,3,1,5],12],[[6,6,1,11],4],[[9,9,1,18],4],[[18,18,1,37],12]],
    },
    "D206": {
        "H301": [[[2,1,2,0],4],[[12,6,2,11],5],[[18,9,2,18],4],[[36,18,2,37],5]],
        "H303": [[[4,2,2,1],2],[[6,3,2,5],6],[[12,6,2,11],2],[[18,9,2,18],2],[[36,18,2,37],6]],
    },
}


class StrictError(RuntimeError):
    """Fail-closed input, replay, or schema error."""


def canonical_bytes(value: Any) -> bytes:
    return (
        json.dumps(
            value,
            allow_nan=False,
            ensure_ascii=True,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("ascii")
        + b"\n"
    )


def canonical_leaf_bytes(value: Any) -> bytes:
    return json.dumps(
        value,
        allow_nan=False,
        ensure_ascii=True,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("ascii")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def read_stable(path: Path, *, max_bytes: int) -> tuple[bytes, dict[str, Any]]:
    before = path.stat()
    if not path.is_file() or before.st_size > max_bytes:
        raise StrictError(f"invalid or oversized file: {path}")
    raw = path.read_bytes()
    after = path.stat()
    if (
        before.st_dev,
        before.st_ino,
        before.st_size,
        before.st_mtime_ns,
    ) != (
        after.st_dev,
        after.st_ino,
        after.st_size,
        after.st_mtime_ns,
    ):
        raise StrictError(f"file changed while read: {path}")
    return raw, {
        "path": str(path),
        "sha256": sha256_bytes(raw),
        "size_bytes": len(raw),
    }


def strict_json_loads(raw: bytes) -> Any:
    def pairs_hook(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if type(key) is not str or key in result:
                raise StrictError(f"duplicate or non-string JSON key: {key!r}")
            result[key] = value
        return result

    try:
        return json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=pairs_hook,
            parse_constant=lambda token: (_ for _ in ()).throw(
                StrictError(f"forbidden JSON constant: {token}")
            ),
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise StrictError("invalid strict JSON") from exc


def require_keys(value: Any, expected: Iterable[str], label: str) -> dict[str, Any]:
    if type(value) is not dict:
        raise StrictError(f"{label} must be an object")
    expected_set = set(expected)
    if set(value) != expected_set:
        raise StrictError(
            f"{label} keys changed: got {sorted(value)}, expected {sorted(expected_set)}"
        )
    return value


def require_bool(value: Any, label: str) -> bool:
    if type(value) is not bool:
        raise StrictError(f"{label} must be Boolean")
    return value


def require_int(value: Any, label: str) -> int:
    if type(value) is not int:
        raise StrictError(f"{label} must be an integer")
    return value


def require_str(value: Any, label: str) -> str:
    if type(value) is not str:
        raise StrictError(f"{label} must be a string")
    return value


def one_to_zero(arrays: Sequence[Sequence[int]]) -> list[tuple[int, ...]]:
    output: list[tuple[int, ...]] = []
    target = list(range(1, 28))
    for row in arrays:
        if type(row) is not list or sorted(row) != target:
            raise StrictError("frozen row is not a permutation of 1..27")
        output.append(tuple(value - 1 for value in row))
    return output


Permutation = tuple[int, ...]
IDENTITY: Permutation = tuple(range(27))


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(27))


def inverse(value: Permutation) -> Permutation:
    result = [0] * 27
    for index, image in enumerate(value):
        result[image] = index
    return tuple(result)


def generated(generators: Sequence[Permutation]) -> frozenset[Permutation]:
    found = {IDENTITY}
    queue: deque[Permutation] = deque([IDENTITY])
    while queue:
        current = queue.popleft()
        for generator in generators:
            new = compose(generator, current)
            if new not in found:
                found.add(new)
                queue.append(new)
    return frozenset(found)


def conjugate_element(
    carrier: Permutation, element: Permutation, carrier_inverse: Permutation | None = None
) -> Permutation:
    carrier_inverse = carrier_inverse or inverse(carrier)
    return compose(carrier, compose(element, carrier_inverse))


def is_normal_by_generators(
    ambient_generators: Sequence[Permutation], subgroup: frozenset[Permutation]
) -> bool:
    return all(
        conjugate_element(generator, element) in subgroup
        for generator in ambient_generators
        for element in subgroup
    )


def normalizer_order(
    ambient: frozenset[Permutation],
    subgroup: frozenset[Permutation],
    subgroup_generators: Sequence[Permutation],
) -> int:
    count = 0
    for carrier in ambient:
        carrier_inverse = inverse(carrier)
        if all(
            conjugate_element(carrier, generator, carrier_inverse) in subgroup
            for generator in subgroup_generators
        ):
            count += 1
    return count


def core(
    ambient_generators: Sequence[Permutation], subgroup: frozenset[Permutation]
) -> frozenset[Permutation]:
    current = subgroup
    carriers = list(ambient_generators) + [inverse(row) for row in ambient_generators]
    while True:
        old = current
        for carrier in carriers:
            carrier_inverse = inverse(carrier)
            conjugate = {
                conjugate_element(carrier, element, carrier_inverse)
                for element in current
            }
            current = frozenset(set(current).intersection(conjugate))
        if current == old:
            return current


def centre_order(
    subgroup: frozenset[Permutation], generators: Sequence[Permutation]
) -> int:
    return sum(
        all(compose(element, gen) == compose(gen, element) for gen in generators)
        for element in subgroup
    )


def commutator(left: Permutation, right: Permutation) -> Permutation:
    return compose(inverse(left), compose(inverse(right), compose(left, right)))


def derived_subgroup(subgroup: frozenset[Permutation]) -> frozenset[Permutation]:
    elements = list(subgroup)
    commutators = {
        commutator(left, right) for left in elements for right in elements
    }
    return generated(sorted(commutators))


def pair_action(element: Permutation, pair: tuple[int, int]) -> tuple[int, int]:
    return tuple(sorted((element[pair[0]], element[pair[1]])))  # type: ignore[return-value]


def pair_orbit(
    subgroup: frozenset[Permutation], one_based_pair: Sequence[int]
) -> frozenset[tuple[int, int]]:
    seed = (one_based_pair[0] - 1, one_based_pair[1] - 1)
    return frozenset(pair_action(element, seed) for element in subgroup)


def support_report(
    ambient: frozenset[Permutation],
    subgroup: frozenset[Permutation],
    seeds: list[list[int]],
) -> dict[str, Any]:
    components = [pair_orbit(subgroup, seed) for seed in seeds]
    support = frozenset().union(*components)
    stabilizer = frozenset(
        element
        for element in ambient
        if frozenset(pair_action(element, pair) for pair in support) == support
    )
    return {
        "component_sizes": [len(component) for component in components],
        "pair_seeds": seeds,
        "stabilizer_equals_frozen_field_subgroup": stabilizer == subgroup,
        "stabilizer_order": len(stabilizer),
        "support_size": len(support),
        "weyl_orbit_size": len(ambient) // len(stabilizer),
    }


class LeftCosetAction:
    def __init__(
        self, ambient: frozenset[Permutation], field: frozenset[Permutation]
    ) -> None:
        mapping: dict[Permutation, int] = {}
        representatives: list[Permutation] = []
        for element in sorted(ambient):
            if element in mapping:
                continue
            index = len(representatives)
            representatives.append(element)
            coset = {compose(element, member) for member in field}
            if any(member in mapping for member in coset):
                raise StrictError("left cosets overlap during reconstruction")
            for member in coset:
                mapping[member] = index
        if len(mapping) != len(ambient) or len(representatives) != 320:
            raise StrictError("degree-320 left-coset reconstruction failed")
        self.mapping = mapping
        self.representatives = representatives

    def image(self, element: Permutation, coset_index: int) -> int:
        return self.mapping[compose(element, self.representatives[coset_index])]

    def orbits(
        self,
        subgroup: frozenset[Permutation],
        domain: Iterable[int] | None = None,
    ) -> list[list[int]]:
        unseen = set(range(320) if domain is None else domain)
        output: list[list[int]] = []
        while unseen:
            seed = min(unseen)
            orbit_set = {
                self.image(element, seed) for element in subgroup
            }
            orbit = sorted(orbit_set)
            if not orbit_set <= unseen:
                raise StrictError("invalid subgroup orbit on field cosets")
            unseen -= orbit_set
            output.append(orbit)
        return output


def collected_rows(rows: list[list[int]]) -> list[list[Any]]:
    counts: dict[tuple[int, int, int, int], int] = {}
    for row in rows:
        key = tuple(row)  # type: ignore[assignment]
        counts[key] = counts.get(key, 0) + 1
    return [[list(key), counts[key]] for key in sorted(counts)]


def local_table(
    action: LeftCosetAction,
    decomposition: frozenset[Permutation],
    inertia: frozenset[Permutation],
    wild: frozenset[Permutation],
    deep: frozenset[Permutation],
) -> dict[str, Any]:
    raw: list[list[int]] = []
    decomposition_orbits = action.orbits(decomposition)
    for orbit in decomposition_orbits:
        n = len(orbit)
        f = len(action.orbits(inertia, orbit))
        p_orbits = len(action.orbits(wild, orbit))
        q_orbits = len(action.orbits(deep, orbit))
        if n % f:
            raise StrictError("local degree does not divide by inertia orbit count")
        e = n // f
        conductor_twice = 2 * (n - f) + (n - p_orbits) + 2 * (n - q_orbits)
        if conductor_twice % (2 * f):
            raise StrictError("local different exponent is nonintegral")
        different = conductor_twice // (2 * f)
        if n != e * f:
            raise StrictError("n=e*f failed")
        raw.append([n, e, f, different])
    rows = collected_rows(raw)
    degree_total = sum(row[1] * row[0][0] for row in rows)
    different_total = sum(row[1] * row[0][2] * row[0][3] for row in rows)
    return {
        "complete_collected_rows_n_e_f_d_with_multiplicity": rows,
        "degree_total": degree_total,
        "different_exponent_total": different_total,
        "double_coset_count": len(decomposition_orbits),
        "e_f_identity_all_rows": all(row[0][0] == row[0][1] * row[0][2] for row in rows),
    }


def bind_predecessors(repo_root: Path) -> tuple[list[dict[str, Any]], dict[str, Any], dict[str, Any]]:
    if repo_root.resolve() != EXPECTED_REPO_ROOT:
        raise StrictError(f"unexpected repository root: {repo_root}")
    fingerprints: list[dict[str, Any]] = []
    parsed: dict[str, Any] = {}
    for label, relative, expected_sha in PREDECESSORS:
        path = repo_root / relative
        raw, fingerprint = read_stable(path, max_bytes=2_000_000)
        if fingerprint["sha256"] != expected_sha:
            raise StrictError(f"{label} SHA-256 changed")
        fingerprint["label"] = label
        fingerprint["relative_path"] = relative
        fingerprints.append(fingerprint)
        if relative.endswith(".json"):
            parsed[label] = strict_json_loads(raw)

    c56 = parsed["C56 certificate"]
    c58 = parsed["C58 group evidence"]
    try:
        c56_arrays = c56["payload"]["we6"]["simple_reflection_line_permutations"]
        c58_arrays = c58["line_generators"]
        c58_line_hash = c58["group_report"]["action_sha256"]["line_generators"]
    except (KeyError, TypeError) as exc:
        raise StrictError("released C56/C58 line carriers missing") from exc
    zero_based = [[value - 1 for value in row] for row in W27_ARRAYS]
    if c56_arrays != zero_based or c58_arrays != W27_ARRAYS:
        raise StrictError("frozen W27 arrays do not equal released C56/C58 arrays")
    array_hash = sha256_bytes(canonical_leaf_bytes(W27_ARRAYS))
    if array_hash != "e61bf1be856e01c6bed234207611e460c777686758e04533919aaa713b0e328b":
        raise StrictError("frozen W27 canonical hash changed")
    if c58_line_hash != array_hash:
        raise StrictError("C58 action hash does not bind frozen W27 arrays")
    return fingerprints, c56, c58


def contract_alignment() -> dict[str, Any]:
    return {
        "certificate_payload_top_level_keys": CERTIFICATE_PAYLOAD_TOP_LEVEL_KEYS,
        "planned_code_inventory": PLANNED_CODE_INVENTORY,
        "planned_result_inventory": PLANNED_RESULT_INVENTORY,
        "scaled_integral_invariant_notation": "eta_i",
        "scaled_line_coordinate_notation": "alpha_i=L*d_i",
        "scaled_relation": "eta_i=L^2*tilde_eta_i",
        "unscaled_invariant_notation": "tilde_eta_i",
    }


def validate_contract_alignment(value: Any, label: str) -> None:
    value = require_keys(
        value,
        {
            "certificate_payload_top_level_keys",
            "planned_code_inventory",
            "planned_result_inventory",
            "scaled_integral_invariant_notation",
            "scaled_line_coordinate_notation",
            "scaled_relation",
            "unscaled_invariant_notation",
        },
        label,
    )
    if value != contract_alignment():
        raise StrictError(f"{label} differs from machine payload contract")
    if len(value["planned_code_inventory"]) != 13:
        raise StrictError("planned code inventory is not exactly 13")
    if len(value["planned_result_inventory"]) != 8:
        raise StrictError("planned result inventory is not exactly 8")
    if len(value["certificate_payload_top_level_keys"]) != 15:
        raise StrictError("certificate payload architecture is not exactly 15 keys")


def run_gap_checker(checker_path: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    checker_path = checker_path.resolve()
    if checker_path.name != "c59_checker_group.g" or not checker_path.is_file():
        raise StrictError("checker must be the fixed c59_checker_group.g basename")
    checker_raw, checker_fingerprint = read_stable(checker_path, max_bytes=500_000)
    gap_raw, gap_fingerprint = read_stable(GAP_EXECUTABLE, max_bytes=10_000_000)
    if gap_fingerprint["sha256"] != GAP_SHA256:
        raise StrictError("frozen GAP executable SHA-256 changed")

    environment = dict(os.environ)
    environment.update(
        {
            "LANG": "C",
            "LC_ALL": "C",
            "PYTHONDONTWRITEBYTECODE": "1",
        }
    )
    outputs: list[bytes] = []
    for _ in range(2):
        completed = subprocess.run(
            [str(GAP_EXECUTABLE), "-q", str(checker_path)],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=180,
            env=environment,
        )
        if completed.returncode != 0:
            raise StrictError(
                "independent GAP checker failed: "
                + completed.stderr.decode("utf-8", "replace")[-2000:]
            )
        if completed.stderr:
            raise StrictError("independent GAP checker emitted stderr")
        outputs.append(completed.stdout)
    if outputs[0] != outputs[1]:
        raise StrictError("independent GAP checker is not two-run deterministic")
    projection = strict_json_loads(outputs[0])
    if outputs[0] != canonical_bytes(projection):
        raise StrictError("independent GAP projection is not canonical compact JSON")
    validate_checker_projection(projection)
    checker_raw_after, checker_after = read_stable(checker_path, max_bytes=500_000)
    if checker_raw_after != checker_raw or checker_after != checker_fingerprint:
        raise StrictError("checker source changed across child process")
    return projection, {
        "checker_projection_sha256": sha256_bytes(outputs[0]),
        "checker_projection_size_bytes": len(outputs[0]),
        "checker_source_sha256": checker_fingerprint["sha256"],
        "checker_source_size_bytes": checker_fingerprint["size_bytes"],
        "gap_executable_sha256": GAP_SHA256,
        "gap_executable_size_bytes": len(gap_raw),
        "two_run_deterministic": True,
    }


def validate_local_table(value: Any, label: str) -> None:
    value = require_keys(
        value,
        {
            "complete_collected_rows_n_e_f_d_with_multiplicity",
            "degree_total",
            "different_exponent_total",
            "double_coset_count",
            "e_f_identity_all_rows",
        },
        label,
    )
    rows = value["complete_collected_rows_n_e_f_d_with_multiplicity"]
    if type(rows) is not list or not rows:
        raise StrictError(f"{label} rows missing")
    degree_total = 0
    different_total = 0
    previous: list[int] | None = None
    for offset, entry in enumerate(rows):
        if type(entry) is not list or len(entry) != 2:
            raise StrictError(f"{label} row {offset} malformed")
        row, multiplicity = entry
        if type(row) is not list or len(row) != 4 or any(type(x) is not int for x in row):
            raise StrictError(f"{label} row tuple malformed")
        if type(multiplicity) is not int or multiplicity <= 0:
            raise StrictError(f"{label} row multiplicity malformed")
        n, e, f, d = row
        if min(n, e, f) <= 0 or d < 0 or n != e * f:
            raise StrictError(f"{label} row arithmetic failed")
        if previous is not None and row <= previous:
            raise StrictError(f"{label} rows are not strictly sorted")
        previous = row
        degree_total += multiplicity * n
        different_total += multiplicity * f * d
    if degree_total != 320 or different_total != 624:
        raise StrictError(f"{label} exact totals changed")
    if value["degree_total"] != 320 or value["different_exponent_total"] != 624:
        raise StrictError(f"{label} reported totals changed")
    if require_bool(value["e_f_identity_all_rows"], label + ".e_f") is not True:
        raise StrictError(f"{label} n=e*f flag false")


def validate_field_report(value: Any, expected_label: str, expected_tom: int) -> None:
    value = require_keys(
        value,
        {
            "abelian_invariants",
            "centre_order",
            "core_order",
            "derived_subgroup_order",
            "field_degree",
            "label",
            "normalizer_order",
            "order",
            "permutation_character_values",
            "small_group_id",
            "support",
            "tom_locator",
        },
        f"field {expected_label}",
    )
    if value["label"] != expected_label or value["tom_locator"] != expected_tom:
        raise StrictError(f"field {expected_label} locator changed")
    expected = {
        "H301": ([162,11],[2,3],27,[27,27],54),
        "H303": ([162,19],[2],81,[81],81),
    }[expected_label]
    if (
        value["small_group_id"],
        value["abelian_invariants"],
        value["derived_subgroup_order"],
    ) != expected[:3]:
        raise StrictError(f"field {expected_label} abstract invariants changed")
    if [value["order"],value["field_degree"],value["core_order"],value["centre_order"],value["normalizer_order"]] != [162,320,1,1,324]:
        raise StrictError(f"field {expected_label} durable invariants changed")
    chars = value["permutation_character_values"]
    if type(chars) is not list or len(chars) != 25 or any(type(x) is not int for x in chars):
        raise StrictError(f"field {expected_label} character malformed")
    support = require_keys(
        value["support"],
        {
            "component_sizes",
            "pair_seeds",
            "stabilizer_equals_frozen_field_subgroup",
            "stabilizer_order",
            "support_size",
            "weyl_orbit_size",
        },
        f"field {expected_label} support",
    )
    seeds = [[1,2],[1,9]] if expected_label == "H301" else [[1,2]]
    if support != {
        "component_sizes": expected[3],
        "pair_seeds": seeds,
        "stabilizer_equals_frozen_field_subgroup": True,
        "stabilizer_order": 162,
        "support_size": expected[4],
        "weyl_orbit_size": 320,
    }:
        raise StrictError(f"field {expected_label} support invariant changed")


def validate_branch_structure(value: Any, label: str) -> None:
    value = require_keys(
        value,
        {
            "deep_Q_unique_in_P_subject_to_D_I_normality",
            "inertia_unique_normal_tom140_in_D",
            "normality",
            "orders_D_I_P_Q",
            "tom_D_I_P_Q",
        },
        label + " structure",
    )
    expected_orders = [18,18,9,3] if label == "D140" else [36,18,9,3]
    expected_tom = [140,140,72,7] if label == "D140" else [206,140,72,7]
    if value["orders_D_I_P_Q"] != expected_orders or value["tom_D_I_P_Q"] != expected_tom:
        raise StrictError(f"{label} embedded chain changed")
    require_keys(
        value["normality"],
        {"I_normal_in_D","P_normal_in_D","P_normal_in_I","Q_normal_in_D","Q_normal_in_I"},
        label + " normality",
    )
    if not all(type(flag) is bool and flag for flag in value["normality"].values()):
        raise StrictError(f"{label} normality failed")
    if value["deep_Q_unique_in_P_subject_to_D_I_normality"] is not True or value["inertia_unique_normal_tom140_in_D"] is not True:
        raise StrictError(f"{label} uniqueness failed")


def validate_checker_projection(value: Any) -> None:
    value = require_keys(
        value,
        {
            "G2_gassmann_minimality",
            "G4_global_arithmetic",
            "G5_tom140_local_algebra",
            "G6_tom206_local_algebra",
            "action",
            "contract_alignment",
            "schema_id",
            "software",
            "status",
        },
        "checker projection",
    )
    if value["schema_id"] != CHECKER_SCHEMA_ID or value["status"] != "PASS":
        raise StrictError("checker projection identity/status changed")
    if value["action"] != {"carrier_degree":27,"generator_count":6,"weyl_order":51840}:
        raise StrictError("checker W(E6) action changed")
    if value["software"] != {"ctbllib":"1.3.1","gap":"4.11.1","smallgrp":"1.4.1","tomlib":"1.2.9"}:
        raise StrictError("checker software freeze changed")
    validate_contract_alignment(value["contract_alignment"], "checker contract_alignment")

    g2 = require_keys(
        value["G2_gassmann_minimality"],
        {
            "all_350_subgroup_classes",
            "collision_bucket_indices",
            "durable_field_subgroup_invariants",
            "exact_11_collision_buckets",
            "full_permutation_character_equality",
            "minimum_collision_index",
            "table_of_marks_name",
            "tom_subgroup_class_count",
            "unique_minimum_index320_bucket",
        },
        "checker G2",
    )
    inventory = g2["all_350_subgroup_classes"]
    if type(inventory) is not list or len(inventory) != 350:
        raise StrictError("ToM inventory is not exactly 350 rows")
    character_buckets: dict[tuple[int, ...], list[int]] = {}
    for expected_index, row in enumerate(inventory, 1):
        row = require_keys(row, {"field_degree","permutation_character_values","subgroup_order","tom_index"}, f"ToM row {expected_index}")
        if row["tom_index"] != expected_index:
            raise StrictError("ToM inventory indices not sequential")
        order = require_int(row["subgroup_order"], "ToM subgroup order")
        degree = require_int(row["field_degree"], "ToM field degree")
        chars = row["permutation_character_values"]
        if order <= 0 or degree <= 0 or order * degree != 51840:
            raise StrictError("ToM order/index relation failed")
        if type(chars) is not list or len(chars) != 25 or any(type(x) is not int for x in chars):
            raise StrictError("ToM character row malformed")
        if chars[0] != degree:
            raise StrictError("permutation character degree changed")
        character_buckets.setdefault(tuple(chars), []).append(expected_index)
    duplicates = [indices for indices in character_buckets.values() if len(indices) > 1]
    duplicates.sort(key=lambda row: row[0])
    if duplicates != EXPECTED_COLLISION_BUCKETS:
        raise StrictError("recomputed 350-class character collisions changed")
    duplicate_indices = [inventory[row[0]-1]["field_degree"] for row in duplicates]
    if g2["exact_11_collision_buckets"] != EXPECTED_COLLISION_BUCKETS or len(g2["exact_11_collision_buckets"]) != 11:
        raise StrictError("G2 exact eleven collision buckets changed")
    if g2["collision_bucket_indices"] != duplicate_indices:
        raise StrictError("G2 collision indices changed")
    if min(duplicate_indices) != 320 or duplicate_indices.count(320) != 1:
        raise StrictError("G2 unique minimum index320 failed")
    if g2["minimum_collision_index"] != 320 or g2["unique_minimum_index320_bucket"] != [301,303]:
        raise StrictError("G2 minimum collision leaf changed")
    if g2["table_of_marks_name"] != "U4(2).2" or g2["tom_subgroup_class_count"] != 350 or g2["full_permutation_character_equality"] is not True:
        raise StrictError("G2 inventory metadata changed")
    fields = g2["durable_field_subgroup_invariants"]
    if type(fields) is not list or len(fields) != 2:
        raise StrictError("G2 field reports malformed")
    validate_field_report(fields[0],"H301",301)
    validate_field_report(fields[1],"H303",303)
    if fields[0]["permutation_character_values"] != fields[1]["permutation_character_values"]:
        raise StrictError("Gassmann characters differ")

    g4 = require_keys(
        value["G4_global_arithmetic"],
        {
            "common_conductor_exponents_p3_p5_A_B",
            "common_field_discriminant_decimal_no_newline_digits",
            "common_field_discriminant_decimal_no_newline_sha256",
            "common_field_discriminant_factorization",
            "common_field_discriminant_positive",
            "exact_eight_prime_support",
            "local_orbit_counts_I3_P3_Q3_I5_P5_C3_reflection_Cinf",
            "signature_r1_r2",
        },
        "checker G4",
    )
    if g4["common_conductor_exponents_p3_p5_A_B"] != EXPECTED_CONDUCTORS or g4["signature_r1_r2"] != EXPECTED_SIGNATURE:
        raise StrictError("G4 conductor/signature changed")
    if g4["common_field_discriminant_factorization"] != DISCRIMINANT_FACTORIZATION or g4["exact_eight_prime_support"] != [row[0] for row in DISCRIMINANT_FACTORIZATION]:
        raise StrictError("G4 discriminant factorization/support changed")
    if g4["common_field_discriminant_decimal_no_newline_digits"] != 11658 or g4["common_field_discriminant_decimal_no_newline_sha256"] != DISCRIMINANT_SHA256 or g4["common_field_discriminant_positive"] is not True:
        raise StrictError("G4 discriminant digest/sign changed")
    orbit_counts = require_keys(g4["local_orbit_counts_I3_P3_Q3_I5_P5_C3_reflection_Cinf"], {"H301","H303","local_tom_indices"}, "checker G4 orbit counts")
    if orbit_counts != {"H301":EXPECTED_ORBIT_COUNTS,"H303":EXPECTED_ORBIT_COUNTS,"local_tom_indices":EXPECTED_LOCAL_TOM_INDICES}:
        raise StrictError("G4 orbit count vector changed")

    g5 = require_keys(value["G5_tom140_local_algebra"], {"complete_H301_table","complete_H303_table","degree_one_factor_counts_H301_H303","finite_etale_Q3_algebras_nonisomorphic","structure"}, "checker G5")
    validate_local_table(g5["complete_H301_table"],"G5 H301")
    validate_local_table(g5["complete_H303_table"],"G5 H303")
    validate_branch_structure(g5["structure"],"D140")
    if g5["complete_H301_table"]["complete_collected_rows_n_e_f_d_with_multiplicity"] != EXPECTED_ROWS["D140"]["H301"] or g5["complete_H303_table"]["complete_collected_rows_n_e_f_d_with_multiplicity"] != EXPECTED_ROWS["D140"]["H303"]:
        raise StrictError("G5 complete rows changed")
    if g5["complete_H301_table"]["double_coset_count"] != 36 or g5["complete_H303_table"]["double_coset_count"] != 36 or g5["degree_one_factor_counts_H301_H303"] != [8,0] or g5["finite_etale_Q3_algebras_nonisomorphic"] is not True:
        raise StrictError("G5 factor totals/separator changed")

    g6 = require_keys(value["G6_tom206_local_algebra"], {"complete_H301_table","complete_H303_table","d3_branch_selected","finite_etale_Q3_algebras_nonisomorphic","structure","unramified_quadratic_factor_counts_H301_H303"}, "checker G6")
    validate_local_table(g6["complete_H301_table"],"G6 H301")
    validate_local_table(g6["complete_H303_table"],"G6 H303")
    validate_branch_structure(g6["structure"],"D206")
    if g6["complete_H301_table"]["complete_collected_rows_n_e_f_d_with_multiplicity"] != EXPECTED_ROWS["D206"]["H301"] or g6["complete_H303_table"]["complete_collected_rows_n_e_f_d_with_multiplicity"] != EXPECTED_ROWS["D206"]["H303"]:
        raise StrictError("G6 complete rows changed")
    if g6["complete_H301_table"]["double_coset_count"] != 18 or g6["complete_H303_table"]["double_coset_count"] != 18 or g6["unramified_quadratic_factor_counts_H301_H303"] != [4,0] or g6["finite_etale_Q3_algebras_nonisomorphic"] is not True or g6["d3_branch_selected"] is not False:
        raise StrictError("G6 factor totals/separator/firewall changed")


def direct_python_replay() -> dict[str, Any]:
    generators = {key: one_to_zero(value) for key, value in FROZEN_ARRAYS.items()}
    W = generated(generators["w27_simple_reflection_generators"])
    H301 = generated(generators["h301_generators"])
    H303 = generated(generators["h303_generators"])
    D140 = generated(generators["branch140_D_generators"])
    I140 = D140
    P140 = generated(generators["branch140_P_generators"])
    Q140 = generated(generators["branch140_Q_generators"])
    D206 = generated(generators["branch206_D_generators"])
    I206 = generated(generators["branch206_I_generators"])
    P206 = generated(generators["branch206_P_generators"])
    Q206 = generated(generators["branch206_Q_generators"])
    groups = {
        "W": W,
        "H301": H301,
        "H303": H303,
        "D140": D140,
        "I140": I140,
        "P140": P140,
        "Q140": Q140,
        "D206": D206,
        "I206": I206,
        "P206": P206,
        "Q206": Q206,
    }
    expected_orders = {"W":51840,"H301":162,"H303":162,"D140":18,"I140":18,"P140":9,"Q140":3,"D206":36,"I206":18,"P206":9,"Q206":3}
    if {key:len(value) for key,value in groups.items()} != expected_orders:
        raise StrictError("direct Python frozen group orders changed")

    def field_python(label: str, subgroup: frozenset[Permutation], seeds: list[list[int]]) -> dict[str, Any]:
        gens = generators["h301_generators" if label == "H301" else "h303_generators"]
        return {
            "centre_order": centre_order(subgroup,gens),
            "core_order": len(core(generators["w27_simple_reflection_generators"],subgroup)),
            "derived_subgroup_order": len(derived_subgroup(subgroup)),
            "field_degree": len(W)//len(subgroup),
            "label": label,
            "normalizer_order": normalizer_order(W,subgroup,gens),
            "order": len(subgroup),
            "support": support_report(W,subgroup,seeds),
        }

    py301 = field_python("H301",H301,[[1,2],[1,9]])
    py303 = field_python("H303",H303,[[1,2]])
    expected_field_python = {
        "H301": {"centre_order":1,"core_order":1,"derived_subgroup_order":27,"field_degree":320,"label":"H301","normalizer_order":324,"order":162,"support":{"component_sizes":[27,27],"pair_seeds":[[1,2],[1,9]],"stabilizer_equals_frozen_field_subgroup":True,"stabilizer_order":162,"support_size":54,"weyl_orbit_size":320}},
        "H303": {"centre_order":1,"core_order":1,"derived_subgroup_order":81,"field_degree":320,"label":"H303","normalizer_order":324,"order":162,"support":{"component_sizes":[81],"pair_seeds":[[1,2]],"stabilizer_equals_frozen_field_subgroup":True,"stabilizer_order":162,"support_size":81,"weyl_orbit_size":320}},
    }
    if py301 != expected_field_python["H301"] or py303 != expected_field_python["H303"]:
        raise StrictError("direct Python field subgroup invariants changed")

    def branch_python(label: str,D: frozenset[Permutation],I: frozenset[Permutation],P: frozenset[Permutation],Q: frozenset[Permutation],Dgens: Sequence[Permutation],Igens: Sequence[Permutation],Pgens: Sequence[Permutation]) -> dict[str, Any]:
        if not I <= D or not P <= I or not Q <= P:
            raise StrictError(f"{label} direct subgroup chain changed")
        normality = {
            "I_normal_in_D": is_normal_by_generators(Dgens,I),
            "P_normal_in_D": is_normal_by_generators(Dgens,P),
            "P_normal_in_I": is_normal_by_generators(Igens,P),
            "Q_normal_in_D": is_normal_by_generators(Dgens,Q),
            "Q_normal_in_I": is_normal_by_generators(Igens,Q),
        }
        if not all(normality.values()):
            raise StrictError(f"{label} direct normality changed")
        return {"normality":normality,"orders_D_I_P_Q":[len(D),len(I),len(P),len(Q)]}

    branch140_direct = branch_python("D140",D140,I140,P140,Q140,generators["branch140_D_generators"],generators["branch140_D_generators"],generators["branch140_P_generators"])
    branch206_direct = branch_python("D206",D206,I206,P206,Q206,generators["branch206_D_generators"],generators["branch206_I_generators"],generators["branch206_P_generators"])

    action301 = LeftCosetAction(W,H301)
    action303 = LeftCosetAction(W,H303)
    g5_h301 = local_table(action301,D140,I140,P140,Q140)
    g5_h303 = local_table(action303,D140,I140,P140,Q140)
    g6_h301 = local_table(action301,D206,I206,P206,Q206)
    g6_h303 = local_table(action303,D206,I206,P206,Q206)
    for branch,field,table in [("D140","H301",g5_h301),("D140","H303",g5_h303),("D206","H301",g6_h301),("D206","H303",g6_h303)]:
        if table["complete_collected_rows_n_e_f_d_with_multiplicity"] != EXPECTED_ROWS[branch][field]:
            raise StrictError(f"direct Python {branch}/{field} rows changed")
        validate_local_table(table,f"direct Python {branch}/{field}")

    # The local subgroup class locators and equality of the two orbit-count
    # vectors are independently certified by GAP.  Python derives the four
    # conductor exponents and signature again from those checked counts.
    counts = EXPECTED_ORBIT_COUNTS
    conductors = [
        320-counts[0]+(320-counts[1])//2+(320-counts[2]),
        320-counts[3]+3*(320-counts[4])//4,
        320-counts[5],
        320-counts[6],
    ]
    signature = [2*counts[7]-320,320-counts[7]]
    if conductors != EXPECTED_CONDUCTORS or signature != EXPECTED_SIGNATURE:
        raise StrictError("direct Python conductor/signature formulas changed")
    discriminant = 1
    for prime, exponent in DISCRIMINANT_FACTORIZATION:
        discriminant *= prime**exponent
    discriminant_decimal = str(discriminant).encode("ascii")
    if len(discriminant_decimal) != 11658 or sha256_bytes(discriminant_decimal) != DISCRIMINANT_SHA256:
        raise StrictError("direct Python field discriminant digest changed")

    return {
        "G2_field_subgroups": [py301,py303],
        "G4_global_arithmetic": {
            "common_conductor_exponents_p3_p5_A_B": conductors,
            "common_field_discriminant_decimal_no_newline_digits": len(discriminant_decimal),
            "common_field_discriminant_decimal_no_newline_sha256": sha256_bytes(discriminant_decimal),
            "common_field_discriminant_positive": discriminant > 0,
            "signature_r1_r2": signature,
        },
        "G5_tom140_local_algebra": {
            "complete_H301_table": g5_h301,
            "complete_H303_table": g5_h303,
            "direct_structure": branch140_direct,
        },
        "G6_tom206_local_algebra": {
            "complete_H301_table": g6_h301,
            "complete_H303_table": g6_h303,
            "direct_structure": branch206_direct,
        },
        "action": {"carrier_degree":27,"generator_count":6,"weyl_order":len(W)},
        "status": "PASS",
    }


def compare_python_gap(python_report: dict[str, Any], gap: dict[str, Any]) -> dict[str, bool]:
    gap_fields = gap["G2_gassmann_minimality"]["durable_field_subgroup_invariants"]
    for py_field, gap_field in zip(python_report["G2_field_subgroups"],gap_fields,strict=True):
        projected = {key:gap_field[key] for key in py_field}
        if py_field != projected:
            raise StrictError(f"Python/GAP field projection mismatch: {py_field['label']}")
    if python_report["action"] != gap["action"]:
        raise StrictError("Python/GAP action mismatch")
    py_g4 = python_report["G4_global_arithmetic"]
    if any(gap["G4_global_arithmetic"][key] != value for key,value in py_g4.items()):
        raise StrictError("Python/GAP G4 projection mismatch")
    for gate in ["G5_tom140_local_algebra","G6_tom206_local_algebra"]:
        for field_key in ["complete_H301_table","complete_H303_table"]:
            if python_report[gate][field_key] != gap[gate][field_key]:
                raise StrictError(f"Python/GAP {gate}/{field_key} mismatch")
        py_structure = python_report[gate]["direct_structure"]
        gap_structure = gap[gate]["structure"]
        if py_structure["orders_D_I_P_Q"] != gap_structure["orders_D_I_P_Q"] or py_structure["normality"] != gap_structure["normality"]:
            raise StrictError(f"Python/GAP {gate} structure mismatch")
    return {
        "G2_durable_field_projection_deep_equal": True,
        "G4_global_arithmetic_projection_deep_equal": True,
        "G5_complete_local_tables_and_structure_deep_equal": True,
        "G6_complete_local_tables_and_structure_deep_equal": True,
        "action_projection_deep_equal": True,
        "all_350_character_rows_strictly_validated_in_python": True,
        "exact_11_collision_buckets_rederived_from_350_rows_in_python": True,
    }


def build_evidence(repo_root: Path, checker_path: Path) -> dict[str, Any]:
    predecessors_before, _, _ = bind_predecessors(repo_root)
    gap_projection, checker_report = run_gap_checker(checker_path)
    python_report = direct_python_replay()
    cross_checks = compare_python_gap(python_report,gap_projection)
    predecessors_after, _, _ = bind_predecessors(repo_root)
    if predecessors_after != predecessors_before:
        raise StrictError("released predecessor bytes changed across replay")
    array_hash = sha256_bytes(canonical_leaf_bytes(FROZEN_ARRAYS))
    evidence = {
        "G2_gassmann_minimality": gap_projection["G2_gassmann_minimality"],
        "G4_global_arithmetic": gap_projection["G4_global_arithmetic"],
        "G5_tom140_local_algebra": gap_projection["G5_tom140_local_algebra"],
        "G6_tom206_local_algebra": gap_projection["G6_tom206_local_algebra"],
        "contract_alignment": gap_projection["contract_alignment"],
        "frozen_permutation_arrays": {
            "arrays": FROZEN_ARRAYS,
            "canonical_sha256": array_hash,
            "phase1_design_input_read_at_runtime": False,
            "phase1_design_input_sha256": DESIGN_ONLY_FROZEN_EMBEDDING_SHA256,
        },
        "independent_replay": {
            "checker": checker_report,
            "cross_checks": cross_checks,
            "python_projection": python_report,
        },
        "provenance": {
            "predecessor_files": predecessors_before,
            "released_C56_C58_line_arrays_deep_equal": True,
            "released_line_array_canonical_sha256": "e61bf1be856e01c6bed234207611e460c777686758e04533919aaa713b0e328b",
            "repository_root": str(repo_root.resolve()),
        },
        "schema_id": SCHEMA_ID,
        "status": "PASS",
    }
    validate_evidence(evidence)
    return evidence


def validate_evidence(value: Any) -> None:
    value = require_keys(
        value,
        {
            "G2_gassmann_minimality",
            "G4_global_arithmetic",
            "G5_tom140_local_algebra",
            "G6_tom206_local_algebra",
            "contract_alignment",
            "frozen_permutation_arrays",
            "independent_replay",
            "provenance",
            "schema_id",
            "status",
        },
        "group evidence",
    )
    if value["schema_id"] != SCHEMA_ID or value["status"] != "PASS":
        raise StrictError("group evidence identity/status changed")
    validate_contract_alignment(value["contract_alignment"],"evidence contract_alignment")
    arrays = require_keys(value["frozen_permutation_arrays"], {"arrays","canonical_sha256","phase1_design_input_read_at_runtime","phase1_design_input_sha256"}, "frozen arrays")
    if arrays["arrays"] != FROZEN_ARRAYS or arrays["canonical_sha256"] != sha256_bytes(canonical_leaf_bytes(FROZEN_ARRAYS)):
        raise StrictError("evidence frozen permutation arrays changed")
    if arrays["phase1_design_input_read_at_runtime"] is not False or arrays["phase1_design_input_sha256"] != DESIGN_ONLY_FROZEN_EMBEDDING_SHA256:
        raise StrictError("Phase-1 design/runtime dependency boundary changed")
    checker_projection = {
        "G2_gassmann_minimality": value["G2_gassmann_minimality"],
        "G4_global_arithmetic": value["G4_global_arithmetic"],
        "G5_tom140_local_algebra": value["G5_tom140_local_algebra"],
        "G6_tom206_local_algebra": value["G6_tom206_local_algebra"],
        "action": value["independent_replay"]["python_projection"]["action"],
        "contract_alignment": value["contract_alignment"],
        "schema_id": CHECKER_SCHEMA_ID,
        "software": {"ctbllib":"1.3.1","gap":"4.11.1","smallgrp":"1.4.1","tomlib":"1.2.9"},
        "status": "PASS",
    }
    validate_checker_projection(checker_projection)
    provenance = require_keys(value["provenance"], {"predecessor_files","released_C56_C58_line_arrays_deep_equal","released_line_array_canonical_sha256","repository_root"}, "provenance")
    if provenance["repository_root"] != str(EXPECTED_REPO_ROOT) or provenance["released_C56_C58_line_arrays_deep_equal"] is not True or provenance["released_line_array_canonical_sha256"] != "e61bf1be856e01c6bed234207611e460c777686758e04533919aaa713b0e328b":
        raise StrictError("evidence predecessor provenance changed")
    if type(provenance["predecessor_files"]) is not list or len(provenance["predecessor_files"]) != len(PREDECESSORS):
        raise StrictError("evidence predecessor inventory changed")
    replay = require_keys(value["independent_replay"], {"checker","cross_checks","python_projection"}, "independent replay")
    checker = require_keys(replay["checker"], {"checker_projection_sha256","checker_projection_size_bytes","checker_source_sha256","checker_source_size_bytes","gap_executable_sha256","gap_executable_size_bytes","two_run_deterministic"}, "checker report")
    if checker["gap_executable_sha256"] != GAP_SHA256 or checker["two_run_deterministic"] is not True:
        raise StrictError("checker executable/determinism record changed")
    expected_cross_keys = {"G2_durable_field_projection_deep_equal","G4_global_arithmetic_projection_deep_equal","G5_complete_local_tables_and_structure_deep_equal","G6_complete_local_tables_and_structure_deep_equal","action_projection_deep_equal","all_350_character_rows_strictly_validated_in_python","exact_11_collision_buckets_rederived_from_350_rows_in_python"}
    cross = require_keys(replay["cross_checks"],expected_cross_keys,"cross checks")
    if not all(type(flag) is bool and flag for flag in cross.values()):
        raise StrictError("a producer/checker cross-check failed")
    python_report = require_keys(replay["python_projection"], {"G2_field_subgroups","G4_global_arithmetic","G5_tom140_local_algebra","G6_tom206_local_algebra","action","status"}, "Python projection")
    if python_report["status"] != "PASS":
        raise StrictError("Python projection status changed")
    compare_python_gap(python_report,checker_projection)


def atomic_write(path: Path, raw: bytes) -> None:
    path.parent.mkdir(parents=True,exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=".c59-group-",dir=path.parent)
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor,"wb") as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary,path)
    finally:
        if temporary.exists():
            temporary.unlink()


def load_canonical_evidence(path: Path) -> dict[str, Any]:
    raw, _ = read_stable(path,max_bytes=2_000_000)
    value = strict_json_loads(raw)
    if raw != canonical_bytes(value):
        raise StrictError("evidence is not canonical compact JSON")
    validate_evidence(value)
    return value


def main() -> int:
    if not __debug__:
        raise StrictError("optimized Python is forbidden")
    sys.set_int_max_str_digits(20_000)
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--build-evidence",type=Path)
    mode.add_argument("--check-evidence",type=Path)
    parser.add_argument("--checker",type=Path,default=Path(__file__).with_name("c59_checker_group.g"))
    parser.add_argument("--repo-root",type=Path,default=EXPECTED_REPO_ROOT)
    arguments = parser.parse_args()
    target = arguments.build_evidence or arguments.check_evidence
    assert target is not None
    rebuilt = build_evidence(arguments.repo_root,arguments.checker)
    if arguments.build_evidence is not None:
        atomic_write(target,canonical_bytes(rebuilt))
        accepted = load_canonical_evidence(target)
        if accepted != rebuilt:
            raise StrictError("written evidence failed exact reload")
        mode_name = "BUILD"
    else:
        accepted = load_canonical_evidence(target)
        if accepted != rebuilt:
            raise StrictError("evidence differs from independent rebuild")
        mode_name = "CHECK"
    raw = canonical_bytes(accepted)
    report = {
        "checker_projection_sha256": accepted["independent_replay"]["checker"]["checker_projection_sha256"],
        "evidence_sha256": sha256_bytes(raw),
        "evidence_size_bytes": len(raw),
        "exact_collision_bucket_count": len(accepted["G2_gassmann_minimality"]["exact_11_collision_buckets"]),
        "mode": mode_name,
        "schema_id": SCHEMA_ID,
        "status": "PASS",
        "tom_subgroup_class_count": accepted["G2_gassmann_minimality"]["tom_subgroup_class_count"],
    }
    print(canonical_leaf_bytes(report).decode("ascii"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
