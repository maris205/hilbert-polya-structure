#!/usr/bin/env python3
"""Neutral exact constructions for the Paper 36 chain-quotient audit.

The source layer uses only presentation arithmetic.  It contains no primality,
factorisation, accepted-support, zeta-zero, or target-coefficient oracle.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import gcd


GENS = ("u", "U", "v", "V")


def affine_mul(r: int, left: tuple[Fraction, int], right: tuple[Fraction, int]):
    """Product in Z[1/r] semidirect Z: (x,k)(y,l)=(x+r^k y,k+l)."""
    x, k = left
    y, ell = right
    scale = Fraction(r**k, 1) if k >= 0 else Fraction(1, r ** (-k))
    return x + scale * y, k + ell


def affine_generator(symbol: str):
    return {
        "u": (Fraction(1), 0),
        "U": (Fraction(-1), 0),
        "v": (Fraction(0), 1),
        "V": (Fraction(0), -1),
    }[symbol]


def affine_evaluate(r: int, word):
    state = (Fraction(0), 0)
    for symbol in word:
        state = affine_mul(r, state, affine_generator(symbol))
    return state


def affine_return_counts(r: int, max_length: int):
    counts = [1]
    distribution = {(Fraction(0), 0): 1}
    for _ in range(max_length):
        nxt = defaultdict(int)
        for state, multiplicity in distribution.items():
            for symbol in GENS:
                nxt[affine_mul(r, state, affine_generator(symbol))] += multiplicity
        distribution = dict(nxt)
        counts.append(distribution.get((Fraction(0), 0), 0))
    return counts


def free_reduce_append(word: tuple[str, ...], symbol: str):
    inverse = {"u": "U", "U": "u", "v": "V", "V": "v"}
    if word and word[-1] == inverse[symbol]:
        return word[:-1]
    return word + (symbol,)


def free_return_counts(max_length: int):
    counts = [1]
    distribution = {(): 1}
    for _ in range(max_length):
        nxt = defaultdict(int)
        for word, multiplicity in distribution.items():
            for symbol in GENS:
                nxt[free_reduce_append(word, symbol)] += multiplicity
        distribution = dict(nxt)
        counts.append(distribution.get((), 0))
    return counts


def multiplicative_order(r: int, modulus: int):
    if modulus < 2 or gcd(r, modulus) != 1:
        raise ValueError("finite semidirect control requires modulus >=2 and gcd(r,q)=1")
    value = 1
    for order in range(1, modulus * modulus + 1):
        value = value * r % modulus
        if value == 1:
            return order
    raise AssertionError("Euler finiteness bound was not reached")


def finite_mul(r: int, q: int, period: int, left, right):
    b, k = left
    d, ell = right
    return (b + pow(r, k, q) * d) % q, (k + ell) % period


def finite_inv_generator(r: int, q: int, period: int, symbol: str):
    if symbol == "u":
        return (1 % q, 0)
    if symbol == "U":
        return ((-1) % q, 0)
    if symbol == "v":
        return (0, 1 % period)
    if symbol == "V":
        return (0, (-1) % period)
    raise ValueError(symbol)


def finite_chain_data(r: int, q: int, period_override: int | None = None):
    """Incidence and lifted-cell columns for Z/q semidirect Z/ord_q(r)."""
    period = multiplicative_order(r, q) if period_override is None else period_override
    if period < 1 or pow(r, period, q) != 1:
        raise ValueError("period must make multiplication by r periodic modulo q")
    vertices = [(b, k) for k in range(period) for b in range(q)]
    vertex_index = {vertex: idx for idx, vertex in enumerate(vertices)}
    edge_index = {}
    for vertex in vertices:
        for label in ("u", "v"):
            edge_index[(vertex, label)] = len(edge_index)

    def step(vertex, symbol):
        return finite_mul(r, q, period, vertex, finite_inv_generator(r, q, period, symbol))

    boundary1 = [[0 for _ in edge_index] for _ in vertices]
    for (origin, label), col in edge_index.items():
        target = step(origin, label)
        boundary1[vertex_index[origin]][col] -= 1
        boundary1[vertex_index[target]][col] += 1

    def path_chain(origin, word):
        vector = [0 for _ in edge_index]
        current = origin
        for symbol in word:
            if symbol in ("u", "v"):
                vector[edge_index[(current, symbol)]] += 1
                current = step(current, symbol)
            else:
                positive = symbol.lower()
                previous = step(current, symbol)
                vector[edge_index[(previous, positive)]] -= 1
                current = previous
        if current != origin:
            raise AssertionError((origin, word, current))
        return vector

    rho = tuple(["v", "u", "V"] + ["U"] * r)
    quotient_u = tuple(["u"] * q)
    quotient_v = tuple(["v"] * period)
    affine_cells = [path_chain(origin, rho) for origin in vertices]
    full_cells = affine_cells + [path_chain(origin, quotient_u) for origin in vertices]
    full_cells += [path_chain(origin, quotient_v) for origin in vertices]

    return {
        "r": r,
        "q": q,
        "period": period,
        "vertices": vertices,
        "edge_index": edge_index,
        "boundary1": boundary1,
        "affine_cells": affine_cells,
        "full_cells": full_cells,
        "relation_word": "".join(rho),
    }


def relation_marker_data(r: int):
    """Exact marker and a trace-class damped-Hashimoto cycle lower bound."""
    word = tuple(["v", "u", "V"] + ["U"] * r)
    assert affine_evaluate(r, word) == (Fraction(0), 0)
    relation_side_lengths = (2, r + 1)
    cycle_length = r + 3
    origin_exponent_sum = r * (r + 1) // 2 + 2 * r + 5
    theta = Fraction(1, 2)
    damped_cycle_weight = theta ** (2 * origin_exponent_sum)
    return {
        "r": r,
        "relation_word": "".join(word),
        "relation_side_lengths": relation_side_lengths,
        "cycle_length": cycle_length,
        "unit_step_marker_descends": relation_side_lengths[0] == relation_side_lengths[1],
        "damping_theta": str(theta),
        "origin_exponent_sum": origin_exponent_sum,
        "one_oriented_cycle_trace_weight": str(damped_cycle_weight),
    }
