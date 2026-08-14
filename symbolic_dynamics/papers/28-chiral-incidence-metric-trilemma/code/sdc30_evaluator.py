#!/usr/bin/env python3
"""Separated deterministic source fixtures for SD-C30 controls."""

from __future__ import annotations

from dataclasses import dataclass
import random

from sdc30_chiral_incidence import divisibility_relation


@dataclass(frozen=True)
class Fixture:
    name: str
    labels: tuple[int, ...]
    relation: tuple[tuple[bool, ...], ...]
    selected_count: int
    interpretation: str


def transitive_closure(
    adjacency: tuple[tuple[bool, ...], ...],
) -> tuple[tuple[bool, ...], ...]:
    size = len(adjacency)
    closure = [list(row) for row in adjacency]
    for index in range(size):
        closure[index][index] = True
    for middle in range(size):
        for left in range(size):
            if closure[left][middle]:
                for right in range(size):
                    closure[left][right] = (
                        closure[left][right] or closure[middle][right]
                    )
    return tuple(tuple(row) for row in closure)


def standard_fixture() -> Fixture:
    labels = tuple(range(1, 31))
    return Fixture(
        "standard_divisibility_N30",
        labels,
        divisibility_relation(labels),
        3,
        "INTEGER_SOURCE_BASELINE",
    )


def mutated_fixture() -> Fixture:
    labels = tuple(range(1, 13))
    mutable = [list(row) for row in divisibility_relation(labels)]
    mutable[1][5] = False
    mutable[2][5] = False
    relation = tuple(tuple(row) for row in mutable)
    return Fixture(
        "mutated_divisibility_N12",
        labels,
        relation,
        4,
        "PROVES_TOO_MUCH",
    )


def composite_fixture() -> Fixture:
    labels = (1, 4, 6, 9, 12, 18, 36)
    return Fixture(
        "composite_only_divisibility_subposet",
        labels,
        divisibility_relation(labels),
        3,
        "PROVES_TOO_MUCH",
    )


def seeded_dag_fixture(seed: int = 2801, size: int = 10) -> Fixture:
    generator = random.Random(seed)
    adjacency = [[False] * size for _ in range(size)]
    for index in range(size):
        adjacency[index][index] = True
    forced_atoms = (1, 2, 3)
    for atom in forced_atoms:
        adjacency[0][atom] = True
    for right in range(4, size):
        parent = generator.randrange(1, right)
        adjacency[parent][right] = True
        for left in range(1, right):
            if generator.random() < 0.34:
                adjacency[left][right] = True
    for atom in forced_atoms:
        adjacency[atom][size - 1] = True
    labels = (1, 10, 14, 21, 25, 31, 37, 44, 53, 61)
    return Fixture(
        "seeded_random_locally_finite_DAG",
        labels,
        transitive_closure(tuple(tuple(row) for row in adjacency)),
        3,
        "PROVES_TOO_MUCH",
    )


def all_fixtures() -> tuple[Fixture, ...]:
    return (
        standard_fixture(),
        mutated_fixture(),
        composite_fixture(),
        seeded_dag_fixture(),
    )
