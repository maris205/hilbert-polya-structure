#!/usr/bin/env python3
"""Freeze the R059 primitive symbolic words without loading orbit data."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    PROJECT_ROOT
    / "research"
    / "refine-logs"
    / "R059_EXPECTED_SYMBOLIC_WORDS.json"
)
STATE_ORDER = ("--", "-+", "+-", "++")
ADJACENCY = (
    (1, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 1),
    (0, 1, 0, 0),
)
EXPECTED_PRIMITIVE_COUNTS = (1, 0, 1, 2, 2, 2, 4, 5, 8, 11, 18, 25)
EXPECTED_TRACES = (1, 1, 4, 9, 11, 16, 29, 49, 76, 121, 199, 324)


def canonical_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[shift:] + word[:shift] for shift in range(len(word)))


def primitive_period(word: tuple[int, ...]) -> int:
    for period in range(1, len(word) + 1):
        if len(word) % period == 0 and all(
            word[index] == word[index % period]
            for index in range(len(word))
        ):
            return period
    raise AssertionError("finite word has no period")


def closed_words(period: int) -> list[tuple[int, ...]]:
    words: list[tuple[int, ...]] = []
    for first in range(len(STATE_ORDER)):
        stack = [(first, (first,))]
        while stack:
            current, word = stack.pop()
            if len(word) == period:
                if ADJACENCY[current][first]:
                    words.append(word)
                continue
            for target in range(len(STATE_ORDER) - 1, -1, -1):
                if ADJACENCY[current][target]:
                    stack.append((target, word + (target,)))
    return words


def main() -> None:
    word_lists: dict[str, list[str]] = {}
    traces: dict[str, int] = {}
    primitive_counts: dict[str, int] = {}
    for period in range(1, 13):
        closed = closed_words(period)
        primitive = sorted(
            {
                canonical_rotation(word)
                for word in closed
                if primitive_period(word) == period
            }
        )
        traces[str(period)] = len(closed)
        primitive_counts[str(period)] = len(primitive)
        word_lists[str(period)] = [
            "|".join(STATE_ORDER[state] for state in word)
            for word in primitive
        ]

    if tuple(traces[str(period)] for period in range(1, 13)) != EXPECTED_TRACES:
        raise AssertionError("trace(A^n) table mismatch")
    if (
        tuple(primitive_counts[str(period)] for period in range(1, 13))
        != EXPECTED_PRIMITIVE_COUNTS
    ):
        raise AssertionError("primitive symbolic count table mismatch")

    canonical_payload = json.dumps(
        word_lists,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    payload = {
        "run_id": "R059_EXPECTED_SYMBOLIC_WORDS",
        "source": "four-state adjacency matrix only; no orbit catalog loaded",
        "state_order": list(STATE_ORDER),
        "adjacency_matrix": [list(row) for row in ADJACENCY],
        "trace_A_power": traces,
        "primitive_orbit_counts": primitive_counts,
        "total_primitive_orbits_through_12": sum(primitive_counts.values()),
        "canonical_word_serialization": "period-keyed JSON; words use | separators; lexicographically minimal cyclic rotation in frozen state order",
        "canonical_word_set_sha256": hashlib.sha256(canonical_payload).hexdigest(),
        "primitive_words": word_lists,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(
        json.dumps(
            {
                "output": str(OUTPUT.relative_to(PROJECT_ROOT)),
                "word_set_sha256": payload["canonical_word_set_sha256"],
                "total": payload["total_primitive_orbits_through_12"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
