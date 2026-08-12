"""Exact finite symbolic-orbit ledger for the Gauss continued-fraction shift.

Only the 2x2 monodromy and combinatorial orbit data are exact.  Roofs and
finite orbit sums are high-precision numerical evaluations of those exact
integers.  Nothing in this module computes a Fredholm determinant or claims
analytic continuation.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import product
from math import gcd
from typing import Iterable, Iterator, Sequence

import mpmath as mp


Matrix2 = tuple[int, int, int, int]
Word = tuple[int, ...]


IDENTITY: Matrix2 = (1, 0, 0, 1)


def digit_matrix(a: int) -> Matrix2:
    if a < 1:
        raise ValueError("continued-fraction digits must be positive")
    return (a, 1, 1, 0)


def matmul(left: Matrix2, right: Matrix2) -> Matrix2:
    a, b, c, d = left
    e, f, g, h = right
    return (a * e + b * g, a * f + b * h,
            c * e + d * g, c * f + d * h)


def matpow(matrix: Matrix2, exponent: int) -> Matrix2:
    if exponent < 0:
        raise ValueError("only nonnegative exact powers are supported")
    result = IDENTITY
    base = matrix
    power = exponent
    while power:
        if power & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        power >>= 1
    return result


def monodromy(word: Sequence[int]) -> Matrix2:
    result = IDENTITY
    for digit in word:
        result = matmul(result, digit_matrix(int(digit)))
    return result


def trace(matrix: Matrix2) -> int:
    return matrix[0] + matrix[3]


def determinant(matrix: Matrix2) -> int:
    return matrix[0] * matrix[3] - matrix[1] * matrix[2]


def rotations(word: Word) -> tuple[Word, ...]:
    return tuple(word[index:] + word[:index] for index in range(len(word)))


def canonical_rotation(word: Sequence[int]) -> Word:
    value = tuple(word)
    if not value:
        raise ValueError("empty words do not define periodic orbits")
    return min(rotations(value))


def least_period(word: Sequence[int]) -> int:
    value = tuple(word)
    n = len(value)
    for period in range(1, n + 1):
        if n % period == 0 and value == value[:period] * (n // period):
            return period
    raise AssertionError("a finite word always has a period")


def is_primitive(word: Sequence[int]) -> bool:
    return least_period(word) == len(word)


def primitive_necklaces(alphabet: Sequence[int], length: int) -> Iterator[Word]:
    """Enumerate each primitive cyclic word exactly once."""
    if length < 1:
        return
    symbols = tuple(alphabet)
    if not symbols or any(a < 1 for a in symbols) or len(set(symbols)) != len(symbols):
        raise ValueError("alphabet must contain distinct positive digits")
    for word in product(symbols, repeat=length):
        if is_primitive(word) and word == canonical_rotation(word):
            yield word


def mobius(n: int) -> int:
    if n < 1:
        raise ValueError("mobius expects a positive integer")
    value = n
    factors = 0
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            factors += 1
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        factors += 1
    return -1 if factors % 2 else 1


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def primitive_necklace_count(alphabet_size: int, length: int) -> int:
    return sum(mobius(d) * alphabet_size ** (length // d)
               for d in divisors(length)) // length


def expanding_eigenvalue(matrix: Matrix2) -> mp.mpf:
    tr = mp.mpf(trace(matrix))
    det = mp.mpf(determinant(matrix))
    return (tr + mp.sqrt(tr * tr - 4 * det)) / 2


def intrinsic_roof(matrix: Matrix2) -> mp.mpf:
    """Return 2 log(lambda_+) from the exact characteristic polynomial."""
    return 2 * mp.log(expanding_eigenvalue(matrix))


def additive_log1p_roof(word: Sequence[int]) -> mp.mpf:
    """Predeclared neighboring-roof control; it is not the Gauss roof."""
    return 2 * mp.fsum(mp.log(int(a) + 1) for a in word)


@dataclass(frozen=True)
class Orbit:
    word: Word
    matrix: Matrix2
    trace: int
    determinant: int
    roof: mp.mpf
    additive_roof: mp.mpf

    @property
    def length(self) -> int:
        return len(self.word)

    @property
    def reverse_orbit(self) -> Word:
        return canonical_rotation(tuple(reversed(self.word)))


def enumerate_orbits(alphabet: Sequence[int], max_length: int) -> list[Orbit]:
    records: list[Orbit] = []
    for length in range(1, max_length + 1):
        for word in primitive_necklaces(alphabet, length):
            matrix = monodromy(word)
            records.append(
                Orbit(
                    word=word,
                    matrix=matrix,
                    trace=trace(matrix),
                    determinant=determinant(matrix),
                    roof=intrinsic_roof(matrix),
                    additive_roof=additive_log1p_roof(word),
                )
            )
    return records


def cyclic_invariance_failures(orbit: Orbit) -> int:
    expected = (orbit.trace, orbit.determinant)
    return sum(
        (trace(monodromy(rotated)), determinant(monodromy(rotated))) != expected
        for rotated in rotations(orbit.word)
    )


def reversal_identity_holds(orbit: Orbit) -> bool:
    reverse_matrix = monodromy(tuple(reversed(orbit.word)))
    a, b, c, d = orbit.matrix
    return reverse_matrix == (a, c, b, d)


def repetition_identity_holds(orbit: Orbit, repetition: int = 2) -> bool:
    repeated_word_matrix = monodromy(orbit.word * repetition)
    return repeated_word_matrix == matpow(orbit.matrix, repetition)


def _reversal_classes(group: Iterable[Orbit]) -> set[tuple[Word, Word]]:
    classes: set[tuple[Word, Word]] = set()
    for orbit in group:
        reverse = orbit.reverse_orbit
        classes.add(tuple(sorted((orbit.word, reverse))))
    return classes


def summarize(orbits: Sequence[Orbit], s_grid: Sequence[complex]) -> dict[str, object]:
    if not orbits:
        raise ValueError("cannot summarize an empty orbit ledger")
    word_set = {orbit.word for orbit in orbits}
    trace_groups: dict[tuple[int, int], list[Orbit]] = defaultdict(list)
    for orbit in orbits:
        trace_groups[(orbit.trace, orbit.determinant)].append(orbit)

    collision_groups = [group for group in trace_groups.values() if len(group) > 1]
    nonreversal_groups = [
        group for group in collision_groups if len(_reversal_classes(group)) > 1
    ]
    intrinsic_sums: dict[str, dict[str, float]] = {}
    additive_sums: dict[str, dict[str, float]] = {}
    for s in s_grid:
        key = format_complex(s)
        intrinsic_terms = [mp.exp(-mp.mpc(s) * orbit.roof) for orbit in orbits]
        additive_terms = [mp.exp(-mp.mpc(s) * orbit.additive_roof) for orbit in orbits]
        intrinsic_sums[key] = complex_parts(mp.fsum(intrinsic_terms))
        additive_sums[key] = complex_parts(mp.fsum(additive_terms))

    return {
        "orbit_count": len(orbits),
        "even_orbit_count": sum(orbit.length % 2 == 0 for orbit in orbits),
        "odd_orbit_count": sum(orbit.length % 2 == 1 for orbit in orbits),
        "self_reversal_count": sum(orbit.reverse_orbit == orbit.word for orbit in orbits),
        "reversal_pair_count": sum(orbit.reverse_orbit != orbit.word for orbit in orbits) // 2,
        "missing_reverse_orbits": sum(orbit.reverse_orbit not in word_set for orbit in orbits),
        "cyclic_invariance_failures": sum(cyclic_invariance_failures(orbit) for orbit in orbits),
        "reversal_transpose_failures": sum(not reversal_identity_holds(orbit) for orbit in orbits),
        "repetition_matrix_failures": sum(not repetition_identity_holds(orbit) for orbit in orbits),
        "trace_collision_group_count": len(collision_groups),
        "trace_collision_orbit_excess": sum(len(group) - 1 for group in collision_groups),
        "nonreversal_collision_group_count": len(nonreversal_groups),
        "nonreversal_collision_class_excess": sum(
            len(_reversal_classes(group)) - 1 for group in nonreversal_groups
        ),
        "roof_min": float(min(orbit.roof for orbit in orbits)),
        "roof_max": float(max(orbit.roof for orbit in orbits)),
        "orbit_sum_intrinsic": intrinsic_sums,
        "orbit_sum_additive_log1p_control": additive_sums,
    }


def signed_parity_sums(orbits: Sequence[Orbit], s_grid: Sequence[complex]) -> dict[str, object]:
    output: dict[str, object] = {}
    for s in s_grid:
        terms = [mp.exp(-mp.mpc(s) * orbit.roof) for orbit in orbits]
        even = mp.fsum(term for term, orbit in zip(terms, orbits) if orbit.length % 2 == 0)
        odd = mp.fsum(term for term, orbit in zip(terms, orbits) if orbit.length % 2 == 1)
        output[format_complex(s)] = {
            "unsigned": complex_parts(even + odd),
            "even_only": complex_parts(even),
            "odd_only": complex_parts(odd),
            "parity_twist_even_minus_odd": complex_parts(even - odd),
        }
    return output


def collision_examples(orbits: Sequence[Orbit], limit: int = 25) -> list[dict[str, object]]:
    groups: dict[tuple[int, int], list[Orbit]] = defaultdict(list)
    for orbit in orbits:
        groups[(orbit.trace, orbit.determinant)].append(orbit)
    examples: list[dict[str, object]] = []
    for (tr, det), group in sorted(groups.items()):
        classes = _reversal_classes(group)
        if len(classes) <= 1:
            continue
        examples.append({
            "trace": tr,
            "determinant": det,
            "roof": mp.nstr(group[0].roof, 30),
            "orbit_count": len(group),
            "reversal_class_count": len(classes),
            "words": [list(orbit.word) for orbit in group],
        })
        if len(examples) >= limit:
            break
    return examples


def complex_parts(value: mp.mpc | complex | mp.mpf) -> dict[str, float]:
    number = mp.mpc(value)
    return {"re": float(number.real), "im": float(number.imag)}


def format_complex(value: complex) -> str:
    number = complex(value)
    sign = "+" if number.imag >= 0 else "-"
    return f"{number.real:g}{sign}{abs(number.imag):g}j"


def parse_complex_grid(values: Sequence[object]) -> list[complex]:
    parsed: list[complex] = []
    for value in values:
        if isinstance(value, (int, float)):
            parsed.append(complex(value))
        elif isinstance(value, dict):
            parsed.append(complex(float(value["re"]), float(value.get("im", 0.0))))
        else:
            parsed.append(complex(str(value).replace("i", "j")))
    return parsed
