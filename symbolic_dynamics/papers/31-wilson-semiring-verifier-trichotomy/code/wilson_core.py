#!/usr/bin/env python3
"""Oracle-free source-side Wilson recurrence for SD-C33."""

from __future__ import annotations


def source_remainder(value: int, modulus: int) -> int:
    """Canonical least residue; `%` implements the semiring quotient scan."""
    if modulus < 2 or value < 0:
        raise ValueError("frozen source requires modulus >= 2 and value >= 0")
    return value % modulus


def wilson_residues(n: int) -> tuple[int, ...]:
    """Return (1! mod n, ..., (n-1)! mod n) without a prime oracle."""
    if n < 2:
        raise ValueError("Wilson objects start at n=2")
    residue = 1
    rows = [residue]
    for successor_index in range(2, n):
        residue = source_remainder(residue * successor_index, n)
        rows.append(residue)
    return tuple(rows)


def wilson_accept(n: int) -> bool:
    """Candidate terminal congruence; deliberately calls no evaluator."""
    return wilson_residues(n)[-1] == n - 1
