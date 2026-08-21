#!/usr/bin/env python3
"""Independently enumerate admissible set partitions of the four-cycle."""

from __future__ import annotations

import hashlib
import json
from itertools import product


EDGES = {(0, 1), (1, 2), (2, 3), (0, 3)}


def restricted_growth_words(n: int):
    for word in product(range(n), repeat=n):
        if word[0] != 0:
            continue
        if all(word[i] <= 1 + max(word[:i]) for i in range(1, n)):
            yield word


def blocks(word):
    return tuple(
        tuple(i for i, value in enumerate(word) if value == label)
        for label in range(max(word) + 1)
    )


def admissible(partition) -> bool:
    owner = {vertex: index for index, block in enumerate(partition)
             for vertex in block}
    return all(owner[a] != owner[b] for a, b in EDGES)


parts = sorted(
    (blocks(word) for word in restricted_growth_words(4)),
    key=lambda item: (-len(item), item),
)
accepted = [part for part in parts if admissible(part)]
expected = [
    ((0,), (1,), (2,), (3,)),
    ((0, 2), (1,), (3,)),
    ((0,), (1, 3), (2,)),
    ((0, 2), (1, 3)),
]
if set(accepted) != set(expected):
    raise SystemExit("C4 admissible-partition mismatch")

cover_edges = []
for fine in accepted:
    fine_owner = {v: i for i, block in enumerate(fine) for v in block}
    for coarse in accepted:
        if len(fine) != len(coarse) + 1:
            continue
        coarse_owner = {v: i for i, block in enumerate(coarse) for v in block}
        if all(
            coarse_owner[a] == coarse_owner[b]
            for a in range(4) for b in range(4)
            if fine_owner[a] == fine_owner[b]
        ):
            cover_edges.append((fine, coarse))
if len(cover_edges) != 4:
    raise SystemExit("C4 Hasse-edge mismatch")

payload = {
    "admissible_count": len(accepted),
    "all_partition_count": len(parts),
    "cover_edge_count": len(cover_edges),
    "partitions": accepted,
    "status": "PASS",
}
encoded = json.dumps(payload, indent=2, sort_keys=True).encode() + b"\n"
print(encoded.decode(), end="")
print("sha256=" + hashlib.sha256(encoded).hexdigest())
