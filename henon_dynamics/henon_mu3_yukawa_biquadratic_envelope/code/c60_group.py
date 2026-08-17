#!/usr/bin/env python3
"""Strict C60 producer for the W(E6) biquadratic normalizer envelope.

The Python lane rebuilds every distinguished permutation group, the exact
label transport, point/pair orbit partitions, the V4 Brauer relation on all
51,840 group elements, and both complete relative local towers.  An
independent GAP/TomLib checker exhausts all 350 subgroup classes and all
eleven Gassmann collisions.  The two projections are compared fail-closed.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from typing import Any, Iterable, Sequence

if hasattr(sys,"set_int_max_str_digits"):
    sys.set_int_max_str_digits(50_000)


SCHEMA_ID = "hcs-c60-group-evidence-v1"
GAP_SCHEMA_ID = "hcs-c60-gap-normalizer-projection-v1"
EXPECTED_REPO_ROOT = Path("/root/autodl-tmp/hilbert-polya-structure")
RELEASE_COMMIT = "961c45f4b0c66ec94d2f069fd9ecc9d4b529d03a"
C59_PROJECT = Path("henon_dynamics/henon_mu3_yukawa_gassmann_twins")
C59_GROUP_RELATIVE = C59_PROJECT / "results/c59_group_evidence.json"
C59_MANIFEST_RELATIVE = C59_PROJECT / "FULL_PROJECT_HASHES.sha256"
C59_GROUP_SHA256 = "0b01f9d47e5141d2bff88fbe4d58ed049d88751cbf8ab1df5469009b684c4958"
C59_MANIFEST_SHA256 = "4d756452d5b6d981e5fe4de3991cf6b7838f74fb8c411027a91dc2cf89a8d1a4"
GAP_EXECUTABLE = Path("/usr/bin/gap")
GAP_EXECUTABLE_SHA256 = "9aa736f13150c363d7c31d33513d849482dd52692e7534f51ecfac0d303bb1e3"
EXPECTED_GAP_PROJECTION_SHA256 = "77061a473c504925d24cfb2cedc26f7d4bc7057d4ee84615474cfa154323aba0"
EXPECTED_COLLISION_BUCKETS = [
    [12,15],[17,21],[29,36],[31,39],[41,42],[46,48],
    [57,58],[59,64],[112,120],[132,140],[301,303],
]
FIELD_ORDER = ["N","H301","H302","H303","J"]
RELATIVE_FIELD_ORDER = ["H301","H302","H303","J"]
EXPECTED_GROUP_ORDERS = {
    "W":51840,"N":324,"N303":324,"H301":162,"H302":162,
    "H303":162,"H303c":162,"J":81,"D140":18,"I140":18,
    "P140":9,"Q140":3,"D206":36,"I206":18,"P206":9,"Q206":3,
}
FROZEN_ARRAYS = {
    "H301_generators": [
        [
            1,
            2,
            19,
            21,
            20,
            3,
            24,
            11,
            9,
            10,
            23,
            15,
            13,
            14,
            22,
            5,
            4,
            18,
            6,
            16,
            17,
            12,
            8,
            27,
            25,
            26,
            7
        ],
        [
            16,
            27,
            13,
            12,
            22,
            26,
            15,
            25,
            24,
            7,
            14,
            18,
            20,
            5,
            1,
            23,
            8,
            17,
            9,
            19,
            6,
            2,
            10,
            3,
            4,
            21,
            11
        ],
        [
            26,
            13,
            22,
            20,
            24,
            15,
            21,
            3,
            14,
            1,
            19,
            11,
            25,
            18,
            23,
            7,
            5,
            9,
            12,
            27,
            16,
            8,
            6,
            17,
            2,
            10,
            4
        ]
    ],
    "H302_generators": [
        [
            2,
            18,
            23,
            21,
            20,
            11,
            24,
            15,
            26,
            25,
            22,
            3,
            9,
            10,
            19,
            5,
            4,
            1,
            8,
            16,
            17,
            6,
            12,
            27,
            14,
            13,
            7
        ],
        [
            13,
            9,
            6,
            16,
            27,
            19,
            17,
            23,
            10,
            2,
            8,
            22,
            14,
            1,
            12,
            24,
            20,
            26,
            3,
            7,
            5,
            15,
            11,
            4,
            18,
            25,
            21
        ],
        [
            15,
            12,
            4,
            14,
            25,
            7,
            10,
            27,
            8,
            6,
            17,
            24,
            11,
            3,
            21,
            26,
            13,
            22,
            5,
            18,
            1,
            20,
            16,
            2,
            19,
            23,
            9
        ],
        [
            1,
            2,
            19,
            21,
            20,
            3,
            24,
            11,
            9,
            10,
            23,
            15,
            13,
            14,
            22,
            5,
            4,
            18,
            6,
            16,
            17,
            12,
            8,
            27,
            25,
            26,
            7
        ],
        [
            20,
            5,
            3,
            2,
            9,
            11,
            10,
            8,
            7,
            4,
            6,
            23,
            24,
            21,
            19,
            26,
            18,
            16,
            15,
            13,
            1,
            22,
            12,
            14,
            17,
            27,
            25
        ]
    ],
    "H303_generators": [
        [
            5,
            1,
            6,
            2,
            3,
            4,
            10,
            21,
            14,
            17,
            19,
            11,
            7,
            8,
            9,
            15,
            18,
            20,
            12,
            13,
            16,
            26,
            22,
            27,
            23,
            24,
            25
        ],
        [
            7,
            15,
            13,
            12,
            26,
            5,
            16,
            18,
            20,
            1,
            22,
            8,
            9,
            6,
            27,
            11,
            4,
            25,
            3,
            24,
            14,
            10,
            21,
            19,
            17,
            23,
            2
        ],
        [
            16,
            23,
            9,
            8,
            26,
            27,
            7,
            25,
            24,
            10,
            11,
            12,
            13,
            6,
            5,
            22,
            17,
            18,
            19,
            20,
            2,
            1,
            21,
            3,
            4,
            15,
            14
        ]
    ],
    "J_generators": [
        [
            1,
            2,
            6,
            17,
            16,
            19,
            27,
            23,
            9,
            10,
            8,
            22,
            13,
            14,
            12,
            20,
            21,
            18,
            3,
            5,
            4,
            15,
            11,
            7,
            25,
            26,
            24
        ],
        [
            2,
            18,
            11,
            4,
            5,
            8,
            7,
            12,
            26,
            25,
            15,
            6,
            9,
            10,
            3,
            16,
            17,
            1,
            23,
            20,
            21,
            19,
            22,
            24,
            14,
            13,
            27
        ],
        [
            3,
            6,
            5,
            2,
            1,
            4,
            18,
            17,
            12,
            8,
            16,
            21,
            15,
            11,
            20,
            14,
            10,
            19,
            7,
            13,
            9,
            24,
            27,
            26,
            23,
            22,
            25
        ]
    ],
    "N_generators": [
        [
            1,
            18,
            22,
            16,
            17,
            12,
            27,
            8,
            25,
            26,
            23,
            6,
            14,
            13,
            19,
            4,
            5,
            2,
            15,
            21,
            20,
            3,
            11,
            24,
            9,
            10,
            7
        ],
        [
            15,
            12,
            4,
            14,
            25,
            7,
            10,
            27,
            8,
            6,
            17,
            24,
            11,
            3,
            21,
            26,
            13,
            22,
            5,
            18,
            1,
            20,
            16,
            2,
            19,
            23,
            9
        ],
        [
            1,
            2,
            19,
            21,
            20,
            3,
            24,
            11,
            9,
            10,
            23,
            15,
            13,
            14,
            22,
            5,
            4,
            18,
            6,
            16,
            17,
            12,
            8,
            27,
            25,
            26,
            7
        ],
        [
            14,
            10,
            3,
            7,
            4,
            6,
            5,
            8,
            2,
            9,
            11,
            12,
            1,
            13,
            15,
            17,
            27,
            25,
            19,
            21,
            24,
            22,
            23,
            20,
            26,
            18,
            16
        ],
        [
            18,
            1,
            15,
            4,
            5,
            12,
            7,
            6,
            13,
            14,
            3,
            8,
            26,
            25,
            11,
            16,
            17,
            2,
            22,
            20,
            21,
            23,
            19,
            24,
            10,
            9,
            27
        ],
        [
            1,
            13,
            16,
            12,
            6,
            5,
            8,
            7,
            9,
            26,
            27,
            4,
            2,
            18,
            17,
            3,
            15,
            14,
            20,
            19,
            22,
            21,
            24,
            23,
            25,
            10,
            11
        ]
    ],
    "W27_generators": [
        [
            2,
            1,
            3,
            4,
            5,
            6,
            7,
            12,
            13,
            14,
            15,
            8,
            9,
            10,
            11,
            16,
            17,
            18,
            19,
            20,
            21,
            23,
            22,
            24,
            25,
            26,
            27
        ],
        [
            1,
            3,
            2,
            4,
            5,
            6,
            8,
            7,
            9,
            10,
            11,
            12,
            16,
            17,
            18,
            13,
            14,
            15,
            19,
            20,
            21,
            22,
            24,
            23,
            25,
            26,
            27
        ],
        [
            1,
            2,
            4,
            3,
            5,
            6,
            7,
            9,
            8,
            10,
            11,
            13,
            12,
            14,
            15,
            16,
            19,
            20,
            17,
            18,
            21,
            22,
            23,
            25,
            24,
            26,
            27
        ],
        [
            1,
            2,
            3,
            5,
            4,
            6,
            7,
            8,
            10,
            9,
            11,
            12,
            14,
            13,
            15,
            17,
            16,
            18,
            19,
            21,
            20,
            22,
            23,
            24,
            26,
            25,
            27
        ],
        [
            1,
            2,
            3,
            4,
            6,
            5,
            7,
            8,
            9,
            11,
            10,
            12,
            13,
            15,
            14,
            16,
            18,
            17,
            20,
            19,
            21,
            22,
            23,
            24,
            25,
            27,
            26
        ],
        [
            12,
            8,
            7,
            4,
            5,
            6,
            3,
            2,
            9,
            10,
            11,
            1,
            13,
            14,
            15,
            16,
            17,
            18,
            27,
            26,
            25,
            22,
            23,
            24,
            21,
            20,
            19
        ]
    ],
    "branch140_D_generators": [
        [
            7,
            26,
            13,
            12,
            5,
            15,
            1,
            18,
            20,
            22,
            16,
            4,
            3,
            14,
            6,
            11,
            25,
            8,
            24,
            9,
            27,
            10,
            23,
            19,
            17,
            2,
            21
        ],
        [
            17,
            2,
            21,
            4,
            18,
            1,
            15,
            5,
            20,
            3,
            11,
            12,
            22,
            14,
            25,
            16,
            6,
            8,
            19,
            23,
            10,
            27,
            9,
            24,
            7,
            26,
            13
        ],
        [
            23,
            24,
            22,
            19,
            21,
            20,
            1,
            3,
            15,
            13,
            14,
            2,
            18,
            16,
            17,
            11,
            9,
            10,
            26,
            25,
            27,
            8,
            7,
            12,
            6,
            4,
            5
        ]
    ],
    "branch140_P_generators": [
        [
            7,
            12,
            8,
            26,
            27,
            25,
            23,
            22,
            17,
            18,
            16,
            24,
            10,
            11,
            9,
            14,
            15,
            13,
            4,
            6,
            5,
            3,
            1,
            2,
            20,
            19,
            21
        ],
        [
            25,
            12,
            18,
            26,
            22,
            15,
            20,
            13,
            1,
            5,
            16,
            24,
            21,
            11,
            23,
            14,
            7,
            27,
            4,
            17,
            8,
            10,
            6,
            2,
            9,
            19,
            3
        ]
    ],
    "branch140_Q_generators": [
        [
            6,
            2,
            10,
            4,
            8,
            17,
            25,
            18,
            23,
            21,
            11,
            12,
            27,
            14,
            7,
            16,
            1,
            5,
            19,
            9,
            3,
            13,
            20,
            24,
            15,
            26,
            22
        ]
    ],
    "branch206_D_generators": [
        [
            1,
            2,
            20,
            16,
            5,
            18,
            26,
            8,
            11,
            23,
            9,
            12,
            15,
            22,
            13,
            4,
            17,
            6,
            21,
            3,
            19,
            14,
            10,
            24,
            27,
            7,
            25
        ],
        [
            5,
            2,
            3,
            4,
            1,
            6,
            14,
            17,
            19,
            10,
            21,
            12,
            13,
            7,
            15,
            16,
            8,
            18,
            9,
            20,
            11,
            26,
            23,
            24,
            25,
            22,
            27
        ],
        [
            11,
            7,
            26,
            24,
            25,
            15,
            22,
            14,
            12,
            13,
            27,
            21,
            18,
            20,
            23,
            4,
            3,
            10,
            5,
            8,
            9,
            2,
            6,
            16,
            19,
            17,
            1
        ]
    ],
    "branch206_I_generators": [
        [
            1,
            17,
            22,
            16,
            12,
            18,
            26,
            8,
            25,
            23,
            27,
            5,
            15,
            20,
            13,
            4,
            2,
            6,
            21,
            14,
            19,
            3,
            10,
            24,
            9,
            7,
            11
        ],
        [
            11,
            7,
            26,
            24,
            25,
            15,
            22,
            14,
            12,
            13,
            27,
            21,
            18,
            20,
            23,
            4,
            3,
            10,
            5,
            8,
            9,
            2,
            6,
            16,
            19,
            17,
            1
        ],
        [
            12,
            17,
            14,
            4,
            1,
            6,
            3,
            2,
            19,
            10,
            21,
            5,
            13,
            7,
            15,
            16,
            8,
            18,
            27,
            22,
            25,
            26,
            23,
            24,
            11,
            20,
            9
        ]
    ],
    "branch206_P_generators": [
        [
            11,
            7,
            26,
            24,
            25,
            15,
            22,
            14,
            12,
            13,
            27,
            21,
            18,
            20,
            23,
            4,
            3,
            10,
            5,
            8,
            9,
            2,
            6,
            16,
            19,
            17,
            1
        ],
        [
            12,
            17,
            14,
            4,
            1,
            6,
            3,
            2,
            19,
            10,
            21,
            5,
            13,
            7,
            15,
            16,
            8,
            18,
            27,
            22,
            25,
            26,
            23,
            24,
            11,
            20,
            9
        ]
    ],
    "branch206_Q_generators": [
        [
            12,
            17,
            14,
            4,
            1,
            6,
            3,
            2,
            19,
            10,
            21,
            5,
            13,
            7,
            15,
            16,
            8,
            18,
            27,
            22,
            25,
            26,
            23,
            24,
            11,
            20,
            9
        ]
    ],
    "normalizer_conjugator": [
        1,
        15,
        14,
        13,
        22,
        12,
        27,
        26,
        25,
        7,
        24,
        16,
        17,
        6,
        19,
        18,
        5,
        20,
        4,
        21,
        3,
        2,
        11,
        10,
        9,
        23,
        8
    ]
}


class StrictError(RuntimeError):
    """Fail-closed evidence, provenance, schema, or replay error."""


def canonical_bytes(value: Any) -> bytes:
    return (
        json.dumps(value,allow_nan=False,ensure_ascii=True,
                   separators=(",",":"),sort_keys=True).encode("ascii")
        + b"\n"
    )


def canonical_leaf_bytes(value: Any) -> bytes:
    return json.dumps(value,allow_nan=False,ensure_ascii=True,
                      separators=(",",":"),sort_keys=True).encode("ascii")


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def digest(value: Any) -> str:
    """SHA-256 of a canonical JSON value without a trailing newline."""
    return sha256_bytes(canonical_leaf_bytes(value))


def strict_json_loads(raw: bytes) -> Any:
    def pairs_hook(pairs: list[tuple[str,Any]]) -> dict[str,Any]:
        answer: dict[str,Any] = {}
        for key,value in pairs:
            if type(key) is not str or key in answer:
                raise StrictError(f"duplicate or non-string JSON key: {key!r}")
            answer[key] = value
        return answer
    try:
        return json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=pairs_hook,
            parse_constant=lambda token: (_ for _ in ()).throw(
                StrictError(f"forbidden JSON constant: {token}")
            ),
        )
    except (UnicodeDecodeError,json.JSONDecodeError) as exc:
        raise StrictError("invalid strict JSON") from exc


def require_keys(value: Any, expected: Iterable[str], label: str) -> dict[str,Any]:
    if type(value) is not dict:
        raise StrictError(f"{label} must be an object")
    expected_set = set(expected)
    if set(value) != expected_set:
        raise StrictError(
            f"{label} keys changed: got {sorted(value)}, expected {sorted(expected_set)}"
        )
    return value


def read_stable(path: Path, *, max_bytes: int) -> tuple[bytes,dict[str,Any]]:
    before = path.stat()
    if not path.is_file() or before.st_size > max_bytes:
        raise StrictError(f"invalid or oversized file: {path}")
    raw = path.read_bytes()
    after = path.stat()
    if (before.st_dev,before.st_ino,before.st_size,before.st_mtime_ns) != (
        after.st_dev,after.st_ino,after.st_size,after.st_mtime_ns
    ):
        raise StrictError(f"file changed while read: {path}")
    return raw,{"path":str(path),"sha256":sha256_bytes(raw),"size_bytes":len(raw)}


Permutation = tuple[int,...]
IDENTITY: Permutation = tuple(range(27))


def one_to_zero(arrays: Sequence[Sequence[int]]) -> list[Permutation]:
    target = list(range(1,28))
    output: list[Permutation] = []
    for row in arrays:
        if type(row) is not list or sorted(row) != target:
            raise StrictError("frozen row is not a permutation of 1..27")
        output.append(tuple(value-1 for value in row))
    return output


def compose(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(27))


def inverse(value: Permutation) -> Permutation:
    answer = [0]*27
    for index,image in enumerate(value):
        answer[image] = index
    return tuple(answer)


def conjugate_element(carrier: Permutation, element: Permutation) -> Permutation:
    return compose(carrier,compose(element,inverse(carrier)))


def generated(generators: Sequence[Permutation]) -> frozenset[Permutation]:
    found = {IDENTITY}
    queue: deque[Permutation] = deque([IDENTITY])
    while queue:
        current = queue.popleft()
        for generator in generators:
            new = compose(generator,current)
            if new not in found:
                found.add(new)
                queue.append(new)
    return frozenset(found)


def normalizer_set(
    ambient: frozenset[Permutation],
    subgroup: frozenset[Permutation],
    subgroup_generators: Sequence[Permutation],
) -> frozenset[Permutation]:
    answer: set[Permutation] = set()
    for carrier in ambient:
        carrier_inverse = inverse(carrier)
        if all(
            compose(carrier,compose(generator,carrier_inverse)) in subgroup
            for generator in subgroup_generators
        ):
            answer.add(carrier)
    return frozenset(answer)


def is_normal_by_generators(
    ambient_generators: Sequence[Permutation], subgroup: frozenset[Permutation]
) -> bool:
    return all(
        conjugate_element(generator,element) in subgroup
        for generator in ambient_generators
        for element in subgroup
    )


def core(
    ambient_generators: Sequence[Permutation], subgroup: frozenset[Permutation]
) -> frozenset[Permutation]:
    current = subgroup
    carriers = list(ambient_generators)+[inverse(x) for x in ambient_generators]
    while True:
        old = current
        for carrier in carriers:
            conjugate = {conjugate_element(carrier,x) for x in current}
            current = frozenset(set(current).intersection(conjugate))
        if current == old:
            return current


def commutator(left: Permutation, right: Permutation) -> Permutation:
    return compose(inverse(left),compose(inverse(right),compose(left,right)))


def derived_subgroup(subgroup: frozenset[Permutation]) -> frozenset[Permutation]:
    elements = list(subgroup)
    return generated(sorted({commutator(a,b) for a in elements for b in elements}))


def canonical_group_arrays(group: frozenset[Permutation]) -> list[list[int]]:
    return [[image+1 for image in element] for element in sorted(group)]


def partition_orbits(
    group: frozenset[Permutation], domain: Iterable[Any], action: Any
) -> list[list[Any]]:
    unseen = set(domain)
    blocks: list[list[Any]] = []
    while unseen:
        seed = min(unseen)
        block_set = {action(element,seed) for element in group}
        if not block_set <= unseen:
            raise StrictError("orbit blocks overlap")
        unseen -= block_set
        blocks.append(sorted(block_set))
    return sorted(blocks)


def point_action(element: Permutation, point: int) -> int:
    return element[point]


def pair_action(element: Permutation, pair: tuple[int,int]) -> tuple[int,int]:
    return tuple(sorted((element[pair[0]],element[pair[1]])))  # type: ignore[return-value]


def point_partition(group: frozenset[Permutation]) -> list[list[int]]:
    return [[point+1 for point in block]
            for block in partition_orbits(group,range(27),point_action)]


def pair_partition(group: frozenset[Permutation]) -> list[list[list[int]]]:
    domain = [(i,j) for i in range(27) for j in range(i+1,27)]
    return [[[i+1,j+1] for i,j in block]
            for block in partition_orbits(group,domain,pair_action)]


class CosetAction:
    """Canonical left-coset action, equivalent to GAP right cosets by inversion."""

    def __init__(self, ambient: frozenset[Permutation],
                 subgroup: frozenset[Permutation]) -> None:
        mapping: dict[Permutation,int] = {}
        representatives: list[Permutation] = []
        for element in sorted(ambient):
            if element in mapping:
                continue
            index = len(representatives)
            representatives.append(element)
            coset = {compose(element,member) for member in subgroup}
            if any(member in mapping for member in coset):
                raise StrictError("coset overlap")
            for member in coset:
                mapping[member] = index
        if len(mapping) != len(ambient):
            raise StrictError("coset action did not cover ambient group")
        self.mapping = mapping
        self.representatives = representatives
        self.degree = len(representatives)

    def image(self, element: Permutation, coset: int) -> int:
        return self.mapping[compose(element,self.representatives[coset])]

    def orbits(
        self, subgroup: frozenset[Permutation], domain: Iterable[int] | None=None
    ) -> list[list[int]]:
        unseen = set(range(self.degree) if domain is None else domain)
        answer: list[list[int]] = []
        while unseen:
            seed = min(unseen)
            block = {self.image(element,seed) for element in subgroup}
            if not block <= unseen:
                raise StrictError("coset orbit overlap")
            unseen -= block
            answer.append(sorted(block))
        return answer


def freeze_nested(value: Any) -> Any:
    if type(value) is list:
        return tuple(freeze_nested(item) for item in value)
    return value


def collected_nested(rows: list[Any]) -> list[list[Any]]:
    counts = Counter(freeze_nested(row) for row in rows)
    def thaw(value: Any) -> Any:
        if type(value) is tuple:
            return [thaw(item) for item in value]
        return value
    return [[thaw(key),counts[key]] for key in sorted(counts)]


def local_prime_rows(
    action: CosetAction, D: frozenset[Permutation], I: frozenset[Permutation],
    P: frozenset[Permutation], Q: frozenset[Permutation],
) -> list[tuple[list[int],list[int]]]:
    answer: list[tuple[list[int],list[int]]] = []
    for orbit in action.orbits(D):
        n = len(orbit)
        f = len(action.orbits(I,orbit))
        p_count = len(action.orbits(P,orbit))
        q_count = len(action.orbits(Q,orbit))
        if n % f:
            raise StrictError("local e is not integral")
        e = n//f
        conductor_twice = 2*(n-f)+(n-p_count)+2*(n-q_count)
        if conductor_twice % (2*f):
            raise StrictError("local different is not integral")
        d = conductor_twice//(2*f)
        answer.append((orbit,[n,e,f,d]))
    return answer


def local_table(
    action: CosetAction, D: frozenset[Permutation], I: frozenset[Permutation],
    P: frozenset[Permutation], Q: frozenset[Permutation],
) -> dict[str,Any]:
    prime_rows = local_prime_rows(action,D,I,P,Q)
    collected = collected_nested([row for _,row in prime_rows])
    return {
        "degree_total":sum(multiplicity*row[0] for row,multiplicity in collected),
        "different_total":sum(
            multiplicity*row[2]*row[3] for row,multiplicity in collected
        ),
        "factor_count":len(prime_rows),
        "rows_n_e_f_d_with_multiplicity":collected,
    }


def relative_tower(
    action_N: CosetAction, field_actions: dict[str,CosetAction],
    D: frozenset[Permutation], I: frozenset[Permutation],
    P: frozenset[Permutation], Q: frozenset[Permutation],
) -> dict[str,Any]:
    base_primes = local_prime_rows(action_N,D,I,P,Q)
    base_coset_to_prime: dict[int,int] = {}
    for base_index,(orbit,_) in enumerate(base_primes):
        for coset in orbit:
            base_coset_to_prime[coset] = base_index
    field_primes: dict[str,list[tuple[list[int],list[int]]]] = {
        label:local_prime_rows(action,D,I,P,Q)
        for label,action in field_actions.items()
    }
    rows: list[Any] = []
    quotient_orders = {"H301":2,"H302":2,"H303":2,"J":4}
    for base_index,(base_orbit,base_row) in enumerate(base_primes):
        relative: list[list[int]] = []
        for label in RELATIVE_FIELD_ORDER:
            action = field_actions[label]
            selected: list[list[int]] = []
            for orbit,absolute in field_primes[label]:
                images = {
                    base_coset_to_prime[action_N.mapping[action.representatives[c]]]
                    for c in orbit
                }
                if len(images) != 1:
                    raise StrictError("a field prime maps to multiple base primes")
                if next(iter(images)) == base_index:
                    selected.append(absolute)
            if not selected:
                raise StrictError("base prime has no prime above it")
            rel_rows: list[list[int]] = []
            for absolute in selected:
                if absolute[1] % base_row[1] or absolute[2] % base_row[2]:
                    raise StrictError("relative e or f is nonintegral")
                e_rel = absolute[1]//base_row[1]
                f_rel = absolute[2]//base_row[2]
                d_rel = absolute[3]-e_rel*base_row[3]
                rel_rows.append([len(selected),e_rel,f_rel,d_rel])
            if any(row != rel_rows[0] for row in rel_rows):
                raise StrictError("relative rows above one base prime disagree")
            row = rel_rows[0]
            if row[0]*row[1]*row[2] != quotient_orders[label] or row[3] < 0:
                raise StrictError("relative tower identity failed")
            relative.append(row)
        rows.append([base_row,relative])
    rows.sort()
    return {
        "base_prime_count":len(rows),
        "collected_base_n_e_f_d_and_relative_g_e_f_d_H301_H302_H303_J":
            collected_nested(rows),
        "relative_factor_counts_H301_H302_H303_J":[
            sum(row[1][position][0] for row in rows) for position in range(4)
        ],
        "rows_base_n_e_f_d_then_relative_g_e_f_d_H301_H302_H303_J":rows,
    }


def character_map(
    action: CosetAction, subgroup: frozenset[Permutation]
) -> dict[Permutation,int]:
    counts: Counter[Permutation] = Counter()
    for representative in action.representatives:
        representative_inverse = inverse(representative)
        for member in subgroup:
            element = compose(
                representative,compose(member,representative_inverse)
            )
            counts[element] += 1
    return dict(counts)


def bind_c59(repo_root: Path) -> dict[str,Any]:
    repo_root = repo_root.resolve()
    if repo_root != EXPECTED_REPO_ROOT:
        raise StrictError(f"unexpected repository root: {repo_root}")
    ancestry = subprocess.run(
        ["git","merge-base","--is-ancestor",RELEASE_COMMIT,"HEAD"],
        cwd=repo_root,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,check=False,
    )
    if ancestry.returncode != 0 or ancestry.stdout or ancestry.stderr:
        raise StrictError("released C59 commit is not an ancestor of HEAD")
    records: dict[str,Any] = {}
    released_bytes: dict[str,bytes] = {}
    for label,relative,expected in [
        ("group_evidence",C59_GROUP_RELATIVE,C59_GROUP_SHA256),
        ("project_manifest",C59_MANIFEST_RELATIVE,C59_MANIFEST_SHA256),
    ]:
        shown = subprocess.run(
            ["git","show",f"{RELEASE_COMMIT}:{relative.as_posix()}"],
            cwd=repo_root,stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,check=False,
        )
        if shown.returncode != 0 or shown.stderr:
            raise StrictError(f"cannot read released C59 {label}")
        working,_ = read_stable(repo_root/relative,max_bytes=5_000_000)
        if shown.stdout != working or sha256_bytes(working) != expected:
            raise StrictError(f"released/working C59 {label} bytes changed")
        released_bytes[label] = working
        records[label] = {
            "path":relative.as_posix(),"sha256":expected,"size_bytes":len(working)
        }
    group_value = strict_json_loads(released_bytes["group_evidence"])
    if released_bytes["group_evidence"] != canonical_bytes(group_value):
        raise StrictError("C59 group evidence is not canonical JSON")
    if group_value.get("schema_id") != "hcs-c59-group-evidence-v1" or (
        group_value.get("status") != "PASS"
    ):
        raise StrictError("C59 group evidence identity/status changed")
    lines = released_bytes["project_manifest"].decode("ascii").splitlines()
    entries: dict[str,str] = {}
    for line in lines:
        if len(line) < 67 or line[64:66] != "  ":
            raise StrictError("malformed C59 full-project manifest line")
        file_hash,path = line[:64],line[66:]
        if path in entries or len(file_hash) != 64:
            raise StrictError("duplicate or malformed C59 manifest entry")
        entries[path] = file_hash
    if len(entries) != 63 or "FULL_PROJECT_HASHES.sha256" in entries:
        raise StrictError("C59 full-project manifest inventory changed")
    group_manifest_key = "results/c59_group_evidence.json"
    if entries.get(group_manifest_key) != C59_GROUP_SHA256:
        raise StrictError("C59 group evidence/manifest binding changed")
    for path,expected in entries.items():
        raw,_ = read_stable(repo_root/C59_PROJECT/path,max_bytes=20_000_000)
        if sha256_bytes(raw) != expected:
            raise StrictError(f"C59 manifest verification failed: {path}")
    return {
        "release_commit":RELEASE_COMMIT,
        "release_commit_is_ancestor_of_head":True,
        "files":records,
        "full_project_manifest_entries_verified":len(entries),
        "group_evidence_manifest_entry_verified":True,
    }


def validate_gap_projection(value: Any) -> None:
    value = require_keys(value,{
        "action","character_relation","coefficient_orbit_partitions",
        "collision_normalizer_scan","frozen_permutation_arrays",
        "global_arithmetic","local_arithmetic","normalizer_tower",
        "schema_id","software","status",
    },"GAP projection")
    if value["schema_id"] != GAP_SCHEMA_ID or value["status"] != "PASS":
        raise StrictError("GAP projection identity/status changed")
    if value["action"] != {
        "carrier_degree":27,"generator_count":6,"weyl_order":51840
    }:
        raise StrictError("W(E6) action changed")
    if value["frozen_permutation_arrays"] != FROZEN_ARRAYS:
        raise StrictError("GAP/Python frozen arrays differ")
    software = value["software"]
    if software != {
        "ctbllib":"1.3.1","gap":"4.11.1",
        "smallgrp":"1.4.1","tomlib":"1.2.9",
    }:
        raise StrictError("GAP software lock changed")
    scan = value["collision_normalizer_scan"]
    if scan["exact_11_collision_buckets"] != EXPECTED_COLLISION_BUCKETS:
        raise StrictError("eleven collision buckets changed")
    if len(scan["rows"]) != 11:
        raise StrictError("collision normalizer row count changed")
    theorem_qualifiers: list[list[int]] = []
    for row in scan["rows"]:
        derived = (
            row["normalizers_conjugate_in_W"] is True
            and row["normalizer_indices_over_subgroups"] == [2,2]
        )
        if row["normalizers_conjugate_and_index_two_over_both"] is not derived:
            raise StrictError("collision row index-two/conjugacy leaf is not derived")
        if derived:
            theorem_qualifiers.append(row["bucket"])
    if theorem_qualifiers != [[301,303]] or (
        scan[
            "qualifying_buckets_normalizers_conjugate_and_index_two_over_both"
        ] != theorem_qualifiers
    ):
        raise StrictError("collision conjugate-index-two theorem gate changed")
    tower = value["normalizer_tower"]
    N = tower["common_normalizer"]
    if N != {
        "abelian_invariants":[2,2],"core_order_in_W":1,"derived_order":81,
        "id_group":[324,39],"index_in_W":160,"normalizer_order_in_W":324,
        "order":324,"quotient_by_J_id_group":[4,2],"tom_locator":327,
    }:
        raise StrictError("common normalizer invariants changed")
    if [row["tom_locator"] for row in tower["fields"]] != [301,302,303]:
        raise StrictError("index-two field locators changed")
    if [row["id_group"] for row in tower["fields"]] != [
        [162,11],[162,10],[162,19]
    ]:
        raise StrictError("index-two SmallGroup IDs changed")
    if not all(row["normal_in_N"] and row["normalizer_equals_N"]
               for row in tower["fields"]):
        raise StrictError("index-two normality/normalizer equality changed")
    intersection = tower["intersection"]
    if any([
        intersection["order"] != 81,intersection["tom_locator"] != 266,
        intersection["core_order_in_W"] != 1,
        intersection["normalizer_order_in_W"] != 324,
        intersection["equals_derived_subgroup_of_N"] is not True,
        intersection["normal_in_N"] is not True,
    ]):
        raise StrictError("common intersection J changed")
    if tower["pairwise_generated_orders"] != [324,324,324] or (
        tower["pairwise_intersection_orders"] != [81,81,81]
    ) or tower["pairwise_intersections_equal_J"] is not True:
        raise StrictError("V4 subgroup lattice changed")
    transport = tower["normalizer_transport"]
    if transport["right_action_equation"] != "(i^h)^x=(i^x)^(h^x)" or (
        transport["right_action_equation_checked_pairs"] != 8748
    ) or transport["right_action_equation_holds"] is not True or (
        transport["transported_normalizer_equals_N"] is not True
    ) or transport["H303_transport_contained_in_N"] is not True:
        raise StrictError("mutable label transport changed")
    relation = value["character_relation"]
    if relation["class_count"] != 25 or (
        relation["coefficient_order_H301_H302_H303_J_N"] != [-1,-1,-1,1,2]
    ) or relation["relation_zero_on_every_class"] is not True or (
        relation["H301_equals_H303"] is not True
    ) or relation["H301_equals_H302"] is not False:
        raise StrictError("V4 character relation changed")
    partitions = value["coefficient_orbit_partitions"]
    if partitions["field_order"] != FIELD_ORDER or (
        partitions["H302_point_partition_equals_N"] is not True
    ) or partitions["H302_pair_partition_equals_N"] is not True or (
        partitions["transported_N303_point_partition_equals_N"] is not True
    ) or partitions["transported_N303_pair_partition_equals_N"] is not True:
        raise StrictError("coefficient orbit partition transport changed")
    if partitions["point_partitions"][2] != partitions["point_partitions"][0] or (
        partitions["pair_partitions"][2] != partitions["pair_partitions"][0]
    ):
        raise StrictError("H302 and N actual degree<=2 partitions differ")
    if partitions["transported_N303_point_partition"] != (
        partitions["point_partitions"][0]
    ) or partitions["transported_N303_pair_partition"] != (
        partitions["pair_partitions"][0]
    ):
        raise StrictError("transported partitions are not actually equal")
    arithmetic = value["global_arithmetic"]
    if arithmetic["exact_prime_support"] != [
        3,5,181,283,997,1801,2346241,
        14932047182473291995860108491583652133938007263719,
    ] or [row["field"] for row in arithmetic["fields"]] != FIELD_ORDER:
        raise StrictError("global discriminant support/order changed")
    expected_arithmetic = {
        "N":(160,[308,248,96,80],[16,72]),
        "H301":(320,[624,496,192,160],[16,152]),
        "H302":(320,[632,496,192,160],[0,160]),
        "H303":(320,[624,496,192,160],[16,152]),
        "J":(640,[1264,992,384,320],[0,320]),
    }
    for row in arithmetic["fields"]:
        degree,conductors,signature = expected_arithmetic[row["field"]]
        if row["degree"] != degree or (
            row["conductor_exponents_p3_p5_A_B"] != conductors
        ) or row["signature_r1_r2"] != signature or (
            row["discriminant_positive"] is not True
        ):
            raise StrictError(f"global arithmetic changed: {row['field']}")
    local = value["local_arithmetic"]
    if local["relative_field_order"] != RELATIVE_FIELD_ORDER:
        raise StrictError("relative field order changed")
    for branch,base_count in [("tom140",22),("tom206",11)]:
        lane = local[branch]
        if lane["decomposition_tom_locator"] != int(branch[3:]):
            raise StrictError(f"{branch} locator changed")
        if [row["field"] for row in lane["absolute_tables"]] != FIELD_ORDER:
            raise StrictError(f"{branch} absolute table field order changed")
        relative = lane["relative_tower_over_N"]
        if relative["base_prime_count"] != base_count or len(
            relative["rows_base_n_e_f_d_then_relative_g_e_f_d_H301_H302_H303_J"]
        ) != base_count:
            raise StrictError(f"{branch} full relative row count changed")
    if sha256_bytes(canonical_bytes(value)) != EXPECTED_GAP_PROJECTION_SHA256:
        raise StrictError("exact canonical GAP projection digest changed")


def run_gap_checker(checker_path: Path) -> tuple[dict[str,Any],dict[str,Any]]:
    checker_path = checker_path.resolve()
    if checker_path.name != "c60_checker_group.g" or not checker_path.is_file():
        raise StrictError("checker must have basename c60_checker_group.g")
    source_raw,source = read_stable(checker_path,max_bytes=1_000_000)
    gap_raw,gap = read_stable(GAP_EXECUTABLE,max_bytes=10_000_000)
    if gap["sha256"] != GAP_EXECUTABLE_SHA256:
        raise StrictError("GAP executable digest changed")
    environment = dict(os.environ)
    environment.update({"LANG":"C","LC_ALL":"C","PYTHONDONTWRITEBYTECODE":"1"})
    outputs: list[bytes] = []
    for _ in range(2):
        completed = subprocess.run(
            [str(GAP_EXECUTABLE),"-q",str(checker_path)],
            stdin=subprocess.DEVNULL,stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,check=False,timeout=240,env=environment,
        )
        if completed.returncode != 0:
            raise StrictError(
                "independent GAP checker failed: "
                + completed.stderr.decode("utf-8","replace")[-2000:]
            )
        if completed.stderr:
            raise StrictError("independent GAP checker emitted stderr")
        outputs.append(completed.stdout)
    if outputs[0] != outputs[1]:
        raise StrictError("GAP checker is not two-run deterministic")
    value = strict_json_loads(outputs[0])
    if outputs[0] != canonical_bytes(value):
        raise StrictError("GAP projection is not compact canonical JSON")
    validate_gap_projection(value)
    source_after_raw,source_after = read_stable(checker_path,max_bytes=1_000_000)
    if source_raw != source_after_raw or source != source_after:
        raise StrictError("GAP checker source changed during replay")
    return value,{
        "checker_projection_sha256":sha256_bytes(outputs[0]),
        "checker_projection_size_bytes":len(outputs[0]),
        "checker_source_sha256":source["sha256"],
        "checker_source_size_bytes":source["size_bytes"],
        "gap_executable_sha256":GAP_EXECUTABLE_SHA256,
        "gap_executable_size_bytes":len(gap_raw),
        "two_run_deterministic":True,
    }


def direct_python_replay(gap: dict[str,Any]) -> dict[str,Any]:
    generators = {key:one_to_zero(value) for key,value in FROZEN_ARRAYS.items()
                  if key.endswith("_generators")}
    W = generated(generators["W27_generators"])
    N = generated(generators["N_generators"])
    H301 = generated(generators["H301_generators"])
    H302 = generated(generators["H302_generators"])
    H303 = generated(generators["H303_generators"])
    J = generated(generators["J_generators"])
    x = one_to_zero([FROZEN_ARRAYS["normalizer_conjugator"]])[0]
    H303c = generated([conjugate_element(x,h)
                       for h in generators["H303_generators"]])
    N303 = frozenset(conjugate_element(inverse(x),n) for n in N)
    D140 = generated(generators["branch140_D_generators"])
    I140 = D140
    P140 = generated(generators["branch140_P_generators"])
    Q140 = generated(generators["branch140_Q_generators"])
    D206 = generated(generators["branch206_D_generators"])
    I206 = generated(generators["branch206_I_generators"])
    P206 = generated(generators["branch206_P_generators"])
    Q206 = generated(generators["branch206_Q_generators"])
    groups = {
        "W":W,"N":N,"N303":N303,"H301":H301,"H302":H302,
        "H303":H303,"H303c":H303c,"J":J,"D140":D140,
        "I140":I140,"P140":P140,"Q140":Q140,"D206":D206,
        "I206":I206,"P206":P206,"Q206":Q206,
    }
    if {label:len(group) for label,group in groups.items()} != EXPECTED_GROUP_ORDERS:
        raise StrictError("Python frozen group orders changed")
    normalizer301 = normalizer_set(W,H301,generators["H301_generators"])
    normalizer303 = normalizer_set(W,H303,generators["H303_generators"])
    if normalizer301 != N or normalizer303 != N303:
        raise StrictError("Python normalizer reconstruction differs from frozen N")
    if frozenset(conjugate_element(x,h) for h in normalizer303) != N:
        raise StrictError("Python transported normalizer differs from N")
    if not all(x[h[i]] == conjugate_element(x,h)[x[i]]
               for h in N303 for i in range(27)):
        raise StrictError("Python right-action label transport equation failed")
    if not (H301 <= N and H302 <= N and H303c <= N and J <= N):
        raise StrictError("Python normalizer tower containment failed")
    if not all(is_normal_by_generators(generators["N_generators"],H)
               for H in [H301,H302,H303c,J]):
        raise StrictError("Python normalizer tower normality failed")
    pairs = [(H301,H302),(H301,H303c),(H302,H303c)]
    if [len(a&b) for a,b in pairs] != [81,81,81] or any(a&b != J for a,b in pairs):
        raise StrictError("Python pairwise intersection/J identity failed")
    if [len(generated(list(a)+list(b))) for a,b in pairs] != [324,324,324]:
        raise StrictError("Python pairwise generation/N identity failed")
    derived_N = derived_subgroup(N)
    if derived_N != J:
        raise StrictError("Python [N,N]=J identity failed")
    if len(core(generators["W27_generators"],N)) != 1 or (
        len(core(generators["W27_generators"],J)) != 1
    ):
        raise StrictError("Python faithful N/J action failed")

    partition_groups = {"N":N,"H301":H301,"H302":H302,"H303":H303c,"J":J}
    point_partitions = [point_partition(partition_groups[label])
                        for label in FIELD_ORDER]
    pair_partitions = [pair_partition(partition_groups[label])
                       for label in FIELD_ORDER]
    gap_partitions = gap["coefficient_orbit_partitions"]
    if point_partitions != gap_partitions["point_partitions"] or (
        pair_partitions != gap_partitions["pair_partitions"]
    ):
        raise StrictError("Python/GAP actual point/pair partitions differ")
    if point_partitions[2] != point_partitions[0] or (
        pair_partitions[2] != pair_partitions[0]
    ):
        raise StrictError("Python H302/N degree<=2 partitions differ")
    source_points = point_partition(N303)
    transported_points = sorted([
        sorted(x[point-1]+1 for point in block) for block in source_points
    ])
    source_pairs = pair_partition(N303)
    transported_pairs = sorted([
        sorted([
            sorted([x[pair[0]-1]+1,x[pair[1]-1]+1])
            for pair in block
        ]) for block in source_pairs
    ])
    if transported_points != point_partitions[0] or (
        transported_pairs != pair_partitions[0]
    ):
        raise StrictError("Python transported actual partitions differ from N")

    actions = {label:CosetAction(W,partition_groups[label])
               for label in FIELD_ORDER}
    characters = {
        label:character_map(actions[label],partition_groups[label])
        for label in FIELD_ORDER
    }
    if any(
        characters["J"].get(element,0)+2*characters["N"].get(element,0) !=
        characters["H301"].get(element,0)+characters["H302"].get(element,0)+
        characters["H303"].get(element,0)
        for element in W
    ):
        raise StrictError("Python V4 Brauer relation failed on a W element")
    direct_distribution = Counter(
        tuple(characters[label].get(element,0) for label in
              ["H301","H302","H303","J","N"])
        for element in W
    )
    relation = gap["character_relation"]
    expected_distribution: Counter[tuple[int,...]] = Counter()
    for index,class_size in enumerate(relation["class_sizes"]):
        expected_distribution[tuple(
            relation["vectors"][label][index]
            for label in ["H301","H302","H303","J","N"]
        )] += class_size
    if direct_distribution != expected_distribution:
        raise StrictError("Python/GAP character tuple distribution differs")

    branches = {
        "tom140":(D140,I140,P140,Q140),
        "tom206":(D206,I206,P206,Q206),
    }
    local_cross: dict[str,bool] = {}
    relative_hashes: dict[str,str] = {}
    for branch,(D,I,P,Q) in branches.items():
        direct_tables = [
            {"field":label,"table":local_table(actions[label],D,I,P,Q)}
            for label in FIELD_ORDER
        ]
        gap_lane = gap["local_arithmetic"][branch]
        if direct_tables != gap_lane["absolute_tables"]:
            raise StrictError(f"Python/GAP {branch} absolute local tables differ")
        relative = relative_tower(
            actions["N"],{label:actions[label] for label in RELATIVE_FIELD_ORDER},
            D,I,P,Q,
        )
        if relative != gap_lane["relative_tower_over_N"]:
            raise StrictError(f"Python/GAP {branch} full relative tower differs")
        local_cross[branch] = True
        relative_hashes[branch] = digest(relative)

    discriminants: dict[str,Any] = {}
    for row in gap["global_arithmetic"]["fields"]:
        value = 1
        for prime,exponent in row["discriminant_factorization"]:
            value *= prime**exponent
        raw = str(value).encode("ascii")
        discriminants[row["field"]] = {
            "decimal_no_newline_digits":len(raw),
            "decimal_no_newline_sha256":sha256_bytes(raw),
            "factorization_sha256":digest(row["discriminant_factorization"]),
            "positive":value > 0,
        }
    direct_projection = {
        "character_tuple_distribution":[
            [list(key),direct_distribution[key]]
            for key in sorted(direct_distribution)
        ],
        "discriminants":discriminants,
        "group_element_set_sha256":{
            label:digest(canonical_group_arrays(group))
            for label,group in [
                ("W",W),("N",N),("N303",N303),("H301",H301),
                ("H302",H302),("H303",H303c),("J",J),
            ]
        },
        "group_orders":{label:len(groups[label]) for label in sorted(groups)},
        "local_tower_sha256":relative_hashes,
        "pair_partition_sha256":{
            label:digest(pair_partitions[index])
            for index,label in enumerate(FIELD_ORDER)
        },
        "point_partition_sha256":{
            label:digest(point_partitions[index])
            for index,label in enumerate(FIELD_ORDER)
        },
        "transport":{
            "equation":"x[h[i]]=conjugate(x,h)[x[i]]",
            "equation_checked_pairs":len(N303)*27,
            "equation_holds":True,
            "transported_N303_element_set_equals_N":True,
            "transported_pair_partition_equals_N":True,
            "transported_point_partition_equals_N":True,
        },
    }
    return {
        "direct_projection":direct_projection,
        "direct_projection_sha256":digest(direct_projection),
        "checks":{
            "actual_point_partitions_deep_equal":True,
            "actual_pair_partitions_deep_equal":True,
            "all_51840_element_character_relation":True,
            "character_class_distribution_deep_equal":True,
            "derived_subgroup_equals_J":True,
            "exact_normalizers_deep_equal":True,
            "full_tom140_absolute_and_relative_tables_deep_equal":
                local_cross["tom140"],
            "full_tom206_absolute_and_relative_tables_deep_equal":
                local_cross["tom206"],
            "mutable_label_transport_deep_equal":True,
        },
        "status":"PASS",
    }


def build_evidence(repo_root: Path, checker_path: Path) -> dict[str,Any]:
    producer_path = Path(__file__).resolve()
    producer_raw,producer = read_stable(producer_path,max_bytes=1_000_000)
    source_before = bind_c59(repo_root)
    gap,gap_report = run_gap_checker(checker_path)
    python_report = direct_python_replay(gap)
    source_after = bind_c59(repo_root)
    if source_after != source_before:
        raise StrictError("C59 source contract changed during replay")
    tower = gap["normalizer_tower"]
    conductors = {
        row["field"]:row["conductor_exponents_p3_p5_A_B"]
        for row in gap["global_arithmetic"]["fields"]
    }
    relative_discriminants = []
    for label,relative_degree in [("H301",2),("H302",2),("H303",2),("J",4)]:
        relative_discriminants.append({
            "field":label,
            "relative_degree_over_N":relative_degree,
            "relative_discriminant_exponents_p3_p5_A_B":[
                conductors[label][position]
                - relative_degree*conductors["N"][position]
                for position in range(4)
            ],
        })
    evidence = {
        "G1_common_normalizer_uniqueness":{
            "action":gap["action"],
            "collision_normalizer_scan":gap["collision_normalizer_scan"],
            "common_normalizer":tower["common_normalizer"],
            "normalizer_transport":tower["normalizer_transport"],
        },
        "G3_orbit_partition_obstruction":gap[
            "coefficient_orbit_partitions"
        ],
        "G4_biquadratic_tower_characters":{
            "character_relation":gap["character_relation"],
            "fields":tower["fields"],
            "intersection":tower["intersection"],
            "pairwise_generated_orders":tower["pairwise_generated_orders"],
            "pairwise_intersection_orders":tower[
                "pairwise_intersection_orders"
            ],
            "pairwise_intersections_equal_J":tower[
                "pairwise_intersections_equal_J"
            ],
        },
        "G5_global_relative_discriminants":{
            "global_arithmetic":gap["global_arithmetic"],
            "relative_discriminants_over_N":relative_discriminants,
        },
        "G6_two_local_branches":gap["local_arithmetic"],
        "backend_contract":{
            "gap_executable":str(GAP_EXECUTABLE),
            "gap_executable_sha256":GAP_EXECUTABLE_SHA256,
            "producer_source_sha256":producer["sha256"],
            "producer_source_size_bytes":producer["size_bytes"],
            "python_implementation":"stdlib-only",
            "software":gap["software"],
        },
        "frozen_permutation_arrays":{
            "arrays":FROZEN_ARRAYS,
            "canonical_sha256":digest(FROZEN_ARRAYS),
            "runtime_tmp_dependency":False,
        },
        "independent_replay":{
            "cross_checks":{
                "C59_bytes_stable_across_replay":True,
                "GAP_two_run_deterministic":True,
                "Python_and_GAP_character_relation_agree":True,
                "Python_and_GAP_local_towers_deep_equal":True,
                "Python_and_GAP_orbit_partitions_deep_equal":True,
                "Python_and_GAP_tower_groups_deep_equal":True,
            },
            "gap_checker":gap_report,
            "python":python_report,
        },
        "schema_id":SCHEMA_ID,
        "source_contract":{"released_C59":source_before},
        "status":"PASS",
    }
    producer_after_raw,producer_after = read_stable(
        producer_path,max_bytes=1_000_000
    )
    if producer_after_raw != producer_raw or producer_after != producer:
        raise StrictError("Python producer source changed during replay")
    validate_evidence(evidence)
    return evidence


def validate_evidence(value: Any) -> None:
    value = require_keys(value,{
        "G1_common_normalizer_uniqueness","G3_orbit_partition_obstruction",
        "G4_biquadratic_tower_characters",
        "G5_global_relative_discriminants","G6_two_local_branches",
        "backend_contract","frozen_permutation_arrays","independent_replay",
        "schema_id","source_contract","status",
    },"C60 group evidence")
    if value["schema_id"] != SCHEMA_ID or value["status"] != "PASS":
        raise StrictError("C60 evidence identity/status changed")
    arrays = require_keys(value["frozen_permutation_arrays"],{
        "arrays","canonical_sha256","runtime_tmp_dependency"
    },"frozen arrays")
    if arrays["arrays"] != FROZEN_ARRAYS or (
        arrays["canonical_sha256"] != digest(FROZEN_ARRAYS)
    ) or arrays["runtime_tmp_dependency"] is not False:
        raise StrictError("frozen array contract changed")
    backend = value["backend_contract"]
    producer_raw,producer = read_stable(Path(__file__).resolve(),max_bytes=1_000_000)
    if backend != {
        "gap_executable":str(GAP_EXECUTABLE),
        "gap_executable_sha256":GAP_EXECUTABLE_SHA256,
        "producer_source_sha256":producer["sha256"],
        "producer_source_size_bytes":len(producer_raw),
        "python_implementation":"stdlib-only",
        "software":{
            "ctbllib":"1.3.1","gap":"4.11.1",
            "smallgrp":"1.4.1","tomlib":"1.2.9",
        },
    }:
        raise StrictError("backend contract changed")
    source = require_keys(value["source_contract"],{"released_C59"},"source")
    released = source["released_C59"]
    if released["release_commit"] != RELEASE_COMMIT or (
        released["release_commit_is_ancestor_of_head"] is not True
    ) or released["full_project_manifest_entries_verified"] != 63 or (
        released["group_evidence_manifest_entry_verified"] is not True
    ):
        raise StrictError("C59 release binding changed")
    if released["files"]["group_evidence"]["sha256"] != C59_GROUP_SHA256 or (
        released["files"]["project_manifest"]["sha256"] != C59_MANIFEST_SHA256
    ):
        raise StrictError("C59 source hashes changed")
    replay = require_keys(value["independent_replay"],{
        "cross_checks","gap_checker","python"
    },"independent replay")
    if not all(type(flag) is bool and flag
               for flag in replay["cross_checks"].values()):
        raise StrictError("a cross-check flag failed")
    gap_report = replay["gap_checker"]
    if gap_report["checker_projection_sha256"] != (
        EXPECTED_GAP_PROJECTION_SHA256
    ) or gap_report["two_run_deterministic"] is not True or (
        gap_report["gap_executable_sha256"] != GAP_EXECUTABLE_SHA256
    ):
        raise StrictError("GAP replay report changed")
    python_report = replay["python"]
    if python_report["status"] != "PASS" or not all(
        type(flag) is bool and flag for flag in python_report["checks"].values()
    ) or python_report["direct_projection_sha256"] != digest(
        python_report["direct_projection"]
    ):
        raise StrictError("Python replay report changed")
    g1 = require_keys(value["G1_common_normalizer_uniqueness"],{
        "action","collision_normalizer_scan","common_normalizer",
        "normalizer_transport",
    },"G1")
    g4 = require_keys(value["G4_biquadratic_tower_characters"],{
        "character_relation","fields","intersection",
        "pairwise_generated_orders","pairwise_intersection_orders",
        "pairwise_intersections_equal_J",
    },"G4")
    g5 = require_keys(value["G5_global_relative_discriminants"],{
        "global_arithmetic","relative_discriminants_over_N",
    },"G5")
    expected_relative = [
        {"field":"H301","relative_degree_over_N":2,
         "relative_discriminant_exponents_p3_p5_A_B":[8,0,0,0]},
        {"field":"H302","relative_degree_over_N":2,
         "relative_discriminant_exponents_p3_p5_A_B":[16,0,0,0]},
        {"field":"H303","relative_degree_over_N":2,
         "relative_discriminant_exponents_p3_p5_A_B":[8,0,0,0]},
        {"field":"J","relative_degree_over_N":4,
         "relative_discriminant_exponents_p3_p5_A_B":[32,0,0,0]},
    ]
    if g5["relative_discriminants_over_N"] != expected_relative:
        raise StrictError("relative discriminant exponent ledger changed")
    tower = {
        "common_normalizer":g1["common_normalizer"],
        "fields":g4["fields"],
        "intersection":g4["intersection"],
        "normalizer_transport":g1["normalizer_transport"],
        "pairwise_generated_orders":g4["pairwise_generated_orders"],
        "pairwise_intersection_orders":g4["pairwise_intersection_orders"],
        "pairwise_intersections_equal_J":g4[
            "pairwise_intersections_equal_J"
        ],
    }
    reconstructed_gap = {
        "action":g1["action"],
        "character_relation":g4["character_relation"],
        "coefficient_orbit_partitions":value[
            "G3_orbit_partition_obstruction"
        ],
        "collision_normalizer_scan":g1["collision_normalizer_scan"],
        "frozen_permutation_arrays":arrays["arrays"],
        "global_arithmetic":g5["global_arithmetic"],
        "local_arithmetic":value["G6_two_local_branches"],
        "normalizer_tower":tower,
        "schema_id":GAP_SCHEMA_ID,
        "software":backend["software"],
        "status":"PASS",
    }
    validate_gap_projection(reconstructed_gap)


def atomic_write(path: Path, raw: bytes) -> None:
    path.parent.mkdir(parents=True,exist_ok=True)
    descriptor,name = tempfile.mkstemp(prefix=".c60-group-",dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(descriptor,"wb") as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary,path)
        directory = os.open(path.parent,os.O_RDONLY)
        try:
            os.fsync(directory)
        finally:
            os.close(directory)
    finally:
        if temporary.exists():
            temporary.unlink()


def load_canonical_evidence(path: Path) -> dict[str,Any]:
    raw,_ = read_stable(path,max_bytes=10_000_000)
    value = strict_json_loads(raw)
    if raw != canonical_bytes(value):
        raise StrictError("saved evidence is not compact canonical JSON")
    validate_evidence(value)
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root",type=Path,default=EXPECTED_REPO_ROOT)
    parser.add_argument(
        "--checker",type=Path,
        default=Path(__file__).resolve().with_name("c60_checker_group.g"),
    )
    parser.add_argument("--output",type=Path)
    parser.add_argument("--verify",type=Path)
    parser.add_argument("--replay",action="store_true")
    args = parser.parse_args()
    if args.verify is not None:
        saved = load_canonical_evidence(args.verify)
        if args.replay:
            rebuilt = build_evidence(args.repo_root,args.checker)
            if canonical_bytes(saved) != canonical_bytes(rebuilt):
                raise StrictError("saved evidence differs from fresh replay")
        print(json.dumps({
            "schema_id":saved["schema_id"],"sha256":sha256_bytes(canonical_bytes(saved)),
            "size_bytes":len(canonical_bytes(saved)),"status":"PASS",
        },sort_keys=True,separators=(",",":")))
        return 0
    if args.output is None:
        parser.error("--output is required unless --verify is used")
    evidence = build_evidence(args.repo_root,args.checker)
    raw = canonical_bytes(evidence)
    atomic_write(args.output.resolve(),raw)
    print(json.dumps({
        "schema_id":SCHEMA_ID,"sha256":sha256_bytes(raw),
        "size_bytes":len(raw),"status":"PASS",
    },sort_keys=True,separators=(",",":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
