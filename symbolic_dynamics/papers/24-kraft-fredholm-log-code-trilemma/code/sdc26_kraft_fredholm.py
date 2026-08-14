#!/usr/bin/env python3
"""Target-blind exact core for the SD-C26 Kraft--Fredholm audit.

This module contains only finite local codes, positive roof allocations,
weighted-cycle identities, trie closure, and primitive-necklace arithmetic.
Inventory predicates live in ``sdc26_evaluator.py``.
"""

from __future__ import annotations

import hashlib
import math
from fractions import Fraction
from typing import Callable, Iterable, Sequence


def raw_binary_code(n: int) -> str:
    if n < 1:
        raise ValueError("n must be positive")
    return format(n, "b")


def elias_gamma_code(n: int) -> str:
    bits = raw_binary_code(n)
    return "0" * (len(bits) - 1) + bits


def elias_delta_code(n: int) -> str:
    bits = raw_binary_code(n)
    return elias_gamma_code(len(bits)) + bits[1:]


def framed_binary_code(n: int) -> str:
    bits = raw_binary_code(n)
    return "1" * len(bits) + "0" + bits


ENCODERS: dict[str, Callable[[int], str]] = {
    "raw_binary": raw_binary_code,
    "elias_gamma": elias_gamma_code,
    "elias_delta": elias_delta_code,
    "framed_binary": framed_binary_code,
}
PREFIX_ENCODERS = ("elias_gamma", "elias_delta", "framed_binary")


def marked_local_word(n: int, encoder_name: str) -> str:
    """The return edge carries '#', making the finite local alphabet size 3."""
    return ENCODERS[encoder_name](n) + "#"


def cyclic_normal_form(word: str) -> str:
    if not word:
        raise ValueError("cyclic word must be nonempty")
    return min(word[index:] + word[:index] for index in range(len(word)))


def cyclic_collision_count(words: Sequence[str]) -> int:
    forms = [cyclic_normal_form(word) for word in words]
    return len(forms) - len(set(forms))


def prefix_collision_pairs(words: Sequence[str]) -> tuple[int, list[tuple[str, str]]]:
    word_set = set(words)
    if len(word_set) != len(words):
        raise ValueError("codes must be unique")
    count = 0
    examples: list[tuple[str, str]] = []
    for word in sorted(words, key=lambda value: (len(value), value)):
        for stop in range(1, len(word)):
            prefix = word[:stop]
            if prefix in word_set:
                count += 1
                if len(examples) < 5:
                    examples.append((prefix, word))
    return count, examples


def kraft_mass(words: Iterable[str]) -> Fraction:
    return sum((Fraction(1, 2 ** len(word)) for word in words), Fraction(0))


def finite_word_capacity(alphabet_size: int, max_length: int) -> int:
    return sum(alphabet_size**length for length in range(1, max_length + 1))


def theorem_code_lower_bound(atom: int, alphabet_size: int = 3) -> float:
    return math.log(atom) / (4 * math.log(alphabet_size))


def equal_shares(length: int, atom: int) -> list[Fraction]:
    del atom
    return [Fraction(1, length)] * length


def concentrated_positive_shares(length: int, atom: int) -> list[Fraction]:
    del atom
    tiny = Fraction(1, length * length)
    return [tiny] * (length - 1) + [1 - tiny * (length - 1)]


def hashed_positive_shares(length: int, atom: int) -> list[Fraction]:
    raw: list[int] = []
    for edge in range(length):
        digest = hashlib.sha256(f"SD-C26-ROOF:{atom}:{edge}".encode("ascii")).digest()
        raw.append(1 + int.from_bytes(digest[:2], "big") % 251)
    total = sum(raw)
    return [Fraction(value, total) for value in raw]


ALLOCATORS = {
    "equal": equal_shares,
    "concentrated_positive": concentrated_positive_shares,
    "hashed_positive": hashed_positive_shares,
}


def disjoint_cycle_metrics(
    atom: int,
    encoder_name: str,
    allocation: str,
    sigma: int,
) -> dict[str, object]:
    word = marked_local_word(atom, encoder_name)
    length = len(word)
    shares = ALLOCATORS[allocation](length, atom)
    if min(shares) <= 0 or sum(shares, Fraction(0)) != 1:
        raise AssertionError("positive roof shares must total one")
    values = [math.exp(-sigma * float(share) * math.log(atom)) for share in shares]
    universal = math.exp(-sigma * math.log(atom) / length)
    return {
        "atom": atom,
        "visible_word": word,
        "cycle_length": length,
        "min_roof_share": min(shares),
        "max_roof_share": max(shares),
        "max_singular_value": max(values),
        "min_singular_value": min(values),
        "universal_max_sv_lower_bound": universal,
        "block_s1_norm": sum(values),
        "amgm_block_s1_lower_bound": length * universal,
    }


def mobius(n: int) -> int:
    value = n
    prime_count = 0
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            value //= divisor
            prime_count += 1
            if value % divisor == 0:
                return 0
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


def divisors(n: int) -> list[int]:
    return [divisor for divisor in range(1, n + 1) if n % divisor == 0]


def primitive_necklace_count(alphabet_size: int, length: int) -> int:
    numerator = sum(
        mobius(divisor) * alphabet_size ** (length // divisor)
        for divisor in divisors(length)
    )
    if numerator % length:
        raise AssertionError("necklace quotient must be integral")
    return numerator // length


def primitive_word_root(word: Sequence[int]) -> tuple[tuple[int, ...], int]:
    data = tuple(word)
    for root_length in divisors(len(data)):
        root = data[:root_length]
        exponent = len(data) // root_length
        if root * exponent == data:
            return root, exponent
    raise AssertionError("every finite word has a primitive root")


def build_prefix_trie(codes: dict[int, str]) -> dict[str, object]:
    nodes = {""}
    bit_edges: set[tuple[str, str]] = set()
    terminals: dict[str, int] = {}
    for atom, code in sorted(codes.items()):
        prefix = ""
        for bit in code:
            target = prefix + bit
            nodes.add(target)
            bit_edges.add((prefix, target))
            prefix = target
        if prefix in terminals:
            raise AssertionError("duplicate terminal")
        terminals[prefix] = atom
    collisions, examples = prefix_collision_pairs(list(codes.values()))
    return {
        "nodes": nodes,
        "bit_edges": bit_edges,
        "terminals": terminals,
        "prefix_collision_count": collisions,
        "prefix_collision_examples": examples,
    }


def trie_determinant_identity(codes: dict[int, str], sigma: int = 2) -> tuple[str, str]:
    """Exact finite determinant for the root-return prefix trie."""
    import sympy as sp

    trie = build_prefix_trie(codes)
    nodes = sorted(trie["nodes"], key=lambda value: (len(value), value))
    index = {node: position for position, node in enumerate(nodes)}
    adjacency = sp.zeros(len(nodes), len(nodes))
    for source, target in sorted(trie["bit_edges"]):
        adjacency[index[target], index[source]] += 1
    for terminal, atom in sorted(trie["terminals"].items()):
        adjacency[index[""], index[terminal]] += sp.Rational(1, atom**sigma)
    z = sp.symbols("z")
    actual = sp.factor((sp.eye(len(nodes)) - z * adjacency).det())
    expected = sp.factor(
        1
        - sum(
            sp.Rational(1, atom**sigma) * z ** (len(code) + 1)
            for atom, code in sorted(codes.items())
        )
    )
    if sp.expand(actual - expected) != 0:
        raise AssertionError("trie determinant differs from first-return formula")
    return str(actual), str(expected)


def finite_roof_inventory_rank(log_atoms: Sequence[int]) -> int:
    """Formal rank of distinct prime-log generators in the audited fixture."""
    if len(set(log_atoms)) != len(log_atoms):
        raise ValueError("formal atom generators must be distinct")
    return len(log_atoms)


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def float_text(value: float) -> str:
    return format(value, ".17g")
