#!/usr/bin/env python3
"""Exact candidate core for the SD-C30 chiral incidence completion.

The core accepts an arbitrary finite locally finite poset relation and numeric
source labels. It contains no prime table, target-zero data, or fitted spectral
information.
"""

from __future__ import annotations

from fractions import Fraction

import sympy as sp


def divisibility_relation(labels: tuple[int, ...]) -> tuple[tuple[bool, ...], ...]:
    return tuple(
        tuple(labels[right] % labels[left] == 0 for right in range(len(labels)))
        for left in range(len(labels))
    )


def zeta_matrix(relation: tuple[tuple[bool, ...], ...]) -> sp.Matrix:
    return sp.Matrix([[int(value) for value in row] for row in relation])


def incidence_inverse_topological(
    relation: tuple[tuple[bool, ...], ...],
) -> sp.Matrix:
    size = len(relation)
    mobius = sp.zeros(size)
    for left in range(size - 1, -1, -1):
        mobius[left, left] = 1
        for right in range(left + 1, size):
            if relation[left][right]:
                mobius[left, right] = -sum(
                    mobius[left, middle]
                    for middle in range(left, right)
                    if relation[left][middle] and relation[middle][right]
                )
    return mobius


def coordinate(size: int, index: int) -> sp.Matrix:
    result = sp.zeros(size)
    result[index, index] = 1
    return result


def compile_idempotents(
    relation: tuple[tuple[bool, ...], ...],
) -> tuple[sp.Matrix, sp.Matrix, list[sp.Matrix]]:
    zeta = zeta_matrix(relation)
    mobius = incidence_inverse_topological(relation)
    compiled = [
        zeta * coordinate(len(relation), index) * mobius
        for index in range(len(relation))
    ]
    return zeta, mobius, compiled


def covers_bottom(
    relation: tuple[tuple[bool, ...], ...],
) -> tuple[int, ...]:
    atoms: list[int] = []
    for right in range(1, len(relation)):
        strict_middle = any(
            middle != right
            and relation[0][middle]
            and relation[middle][right]
            for middle in range(1, len(relation))
        )
        if relation[0][right] and not strict_middle:
            atoms.append(right)
    return tuple(atoms)


def weighted_sharp(matrix: sp.Matrix, label_weights: tuple[int, ...]) -> sp.Matrix:
    weight = sp.diag(*label_weights)
    return weight.inv() * matrix.T * weight


def native_gram(
    left: sp.Matrix, right: sp.Matrix, label_weights: tuple[int, ...]
) -> sp.Expr:
    return sp.cancel(sp.trace(left * weighted_sharp(right, label_weights)))


def phase_symbols(count: int) -> tuple[sp.Symbol, ...]:
    return tuple(sp.symbols(f"x0:{count}", nonzero=True))


def native_chiral_block(
    selected: tuple[int, ...],
    labels: tuple[int, ...],
    compiled: list[sp.Matrix],
    label_weights: tuple[int, ...],
) -> tuple[sp.Matrix, tuple[sp.Symbol, ...]]:
    symbols = phase_symbols(len(selected))
    size = compiled[0].rows
    upper = sp.zeros(size)
    lower = sp.zeros(size)
    for phase, index in zip(symbols, selected):
        scale = sp.sqrt(labels[index])
        upper += phase * compiled[index] / scale
        lower += weighted_sharp(compiled[index], label_weights) / (phase * scale)
    block = sp.zeros(2 * size)
    block[:size, size:] = upper
    block[size:, :size] = lower
    return block, symbols


def gram_matrix(
    selected: tuple[int, ...],
    compiled: list[sp.Matrix],
    label_weights: tuple[int, ...],
) -> sp.Matrix:
    return sp.Matrix(
        [
            [
                native_gram(compiled[left], compiled[right], label_weights)
                for right in selected
            ]
            for left in selected
        ]
    )


def b2_from_gram(
    selected: tuple[int, ...],
    labels: tuple[int, ...],
    gram: sp.Matrix,
    symbols: tuple[sp.Symbol, ...],
) -> sp.Expr:
    return sp.expand(
        2
        * sum(
            gram[left, right]
            * symbols[left]
            / (
                symbols[right]
                * sp.sqrt(labels[selected[left]] * labels[selected[right]])
            )
            for left in range(len(selected))
            for right in range(len(selected))
        )
    )


def full_positive_metric(mobius: sp.Matrix) -> tuple[sp.Matrix, sp.Matrix]:
    diagonal = sp.diag(*range(1, mobius.rows + 1))
    return mobius.T * diagonal * mobius, diagonal


def active_positive_metric(
    mobius: sp.Matrix, active: tuple[int, ...]
) -> tuple[sp.Matrix, sp.Matrix, tuple[int, int]]:
    """A positive K commuting only with active coordinates, not all of them."""
    size = mobius.rows
    dormant = [index for index in range(size) if index not in active]
    if len(dormant) < 2:
        raise ValueError("active metric control needs two dormant coordinates")
    first, second = dormant[:2]
    conjugated = sp.diag(*range(2, size + 2))
    conjugated[first, second] = 1
    conjugated[second, first] = 1
    metric = mobius.T * conjugated * mobius
    return metric, conjugated, (first, second)


def is_selfadjoint_in_metric(matrix: sp.Matrix, metric: sp.Matrix) -> bool:
    return matrix.T * metric == metric * matrix


def orthogonal_chiral_block(
    selected_labels: tuple[int, ...],
) -> tuple[sp.Matrix, tuple[sp.Symbol, ...]]:
    symbols = phase_symbols(len(selected_labels))
    count = len(selected_labels)
    upper = sp.diag(
        *[
            symbols[index] / sp.sqrt(selected_labels[index])
            for index in range(count)
        ]
    )
    lower = sp.diag(
        *[
            1 / (symbols[index] * sp.sqrt(selected_labels[index]))
            for index in range(count)
        ]
    )
    block = sp.zeros(2 * count)
    block[:count, count:] = upper
    block[count:, :count] = lower
    return block, symbols


def orthogonal_det3_factor(label: int, z: sp.Symbol) -> sp.Expr:
    return (1 - z**2 / label) * sp.exp(z**2 / label)


def gamma_length(label: int) -> int:
    return 2 * (label.bit_length() - 1) + 1


def marker_exponent(label: int, repetition: int) -> int:
    return repetition * gamma_length(label)


def fraction_text(value: sp.Expr) -> str:
    return str(sp.cancel(value))
