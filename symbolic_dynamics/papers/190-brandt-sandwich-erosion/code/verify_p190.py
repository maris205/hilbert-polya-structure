#!/usr/bin/env python3
"""Exact author-side regression control for P190.

The verifier is paper-local, standard-library only, deterministic, and writes
no files.  It directly enumerates the literal Brandt update and independently
reconstructs labelled target fibres as cyclic paths in output matrices.
Finite exhaustion is falsification pressure, not proof or novelty evidence.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import product


ZERO = (-1, -1)


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def equal(self, got, expected, label: str) -> None:
        self.assertions += 1
        if got != expected:
            raise AssertionError(f"{label}: got={got!r}, expected={expected!r}")

    def true(self, condition: bool, label: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)


AUDIT = Audit()


def alphabet(n: int) -> tuple[tuple[int, int], ...]:
    return (ZERO,) + tuple((a, b) for a in range(n) for b in range(n))


def inverse_unit(x: tuple[int, int]) -> tuple[int, int]:
    return ZERO if x == ZERO else (x[1], x[0])


def multiply(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    if x == ZERO or y == ZERO or x[1] != y[0]:
        return ZERO
    return (x[0], y[1])


def local_output(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    return multiply(multiply(x, y), x)


def step(word: tuple[tuple[int, int], ...]) -> tuple[tuple[int, int], ...]:
    m = len(word)
    return tuple(local_output(word[i], word[(i + 1) % m]) for i in range(m))


def good_edges(word: tuple[tuple[int, int], ...]) -> tuple[bool, ...]:
    m = len(word)
    return tuple(word[i] != ZERO and word[(i + 1) % m] == inverse_unit(word[i])
                 for i in range(m))


def closed_iterate(word: tuple[tuple[int, int], ...], time: int):
    good = good_edges(word)
    m = len(word)
    return tuple(
        word[i] if all(good[(i + j) % m] for j in range(time)) else ZERO
        for i in range(m)
    )


def longest_cyclic_run(bits: tuple[bool, ...]) -> int:
    if all(bits):
        return len(bits)
    best = run = 0
    for bit in bits + bits:
        run = run + 1 if bit else 0
        best = max(best, run)
    return min(best, len(bits) - 1)


def predicted_tail(word: tuple[tuple[int, int], ...]) -> int:
    if all(x == ZERO for x in word):
        return 0
    good = good_edges(word)
    return 0 if all(good) else longest_cyclic_run(good) + 1


def literal_tail_period(word: tuple[tuple[int, int], ...]) -> tuple[int, int]:
    seen = {}
    current = word
    while current not in seen:
        seen[current] = len(seen)
        current = step(current)
    return seen[current], len(seen) - seen[current]


def matrix_multiply(a, b):
    size = len(a)
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(size))
                       for j in range(size)) for i in range(size))


def matrix_vector(a, v):
    return tuple(sum(row[j] * v[j] for j in range(len(v))) for row in a)


def output_matrix(output, letters):
    return tuple(tuple(int(local_output(left, right) == output) for right in letters)
                 for left in letters)


def trace_product(target, matrices):
    size = len(next(iter(matrices.values())))
    current = tuple(tuple(int(i == j) for j in range(size)) for i in range(size))
    for output in target:
        current = matrix_multiply(current, matrices[output])
    return sum(current[i][i] for i in range(size))


def cyclic_path_fibre(target, letters):
    """Direct cyclic path count with row=current source, column=next source."""
    total = 0
    for first in letters:
        paths = {first: 1}
        for output in target[:-1]:
            following = {}
            for left, count in paths.items():
                for right in letters:
                    if local_output(left, right) == output:
                        following[right] = following.get(right, 0) + count
            paths = following
        total += sum(count for left, count in paths.items()
                     if local_output(left, first) == target[-1])
    return total


def spectral_attack(n: int, letters, zero_matrix) -> None:
    """Check the claimed invariant-space decomposition over the integers."""
    q = len(letters)
    r = n * n
    index = {x: i for i, x in enumerate(letters)}
    zero_basis = (1,) + (0,) * r
    unit_sum = (0,) + (1,) * r
    for vector in (zero_basis, unit_sum):
        av = matrix_vector(zero_matrix, vector)
        aav = matrix_vector(zero_matrix, av)
        AUDIT.equal(aav, tuple(r * av[i] + vector[i] for i in range(q)),
                    f"exceptional quadratic n={n}")

    unseen = set(letters[1:])
    inversion_orbits = []
    while unseen:
        x = min(unseen)
        orbit = tuple(sorted({x, inverse_unit(x)}))
        inversion_orbits.append(orbit)
        unseen.difference_update(orbit)
    base = inversion_orbits[0]
    plus_count = 0
    for orbit in inversion_orbits[1:]:
        vector = [0] * q
        for x in orbit:
            vector[index[x]] += len(base)
        for x in base:
            vector[index[x]] -= len(orbit)
        av = matrix_vector(zero_matrix, tuple(vector))
        AUDIT.equal(av, tuple(-x for x in vector), f"minus-one eigenspace n={n}")
        plus_count += 1
    minus_count = 0
    for orbit in inversion_orbits:
        if len(orbit) == 2:
            vector = [0] * q
            vector[index[orbit[0]]] = 1
            vector[index[orbit[1]]] = -1
            av = matrix_vector(zero_matrix, tuple(vector))
            AUDIT.equal(av, tuple(vector), f"plus-one eigenspace n={n}")
            minus_count += 1
    AUDIT.equal(plus_count, (r + n) // 2 - 1, f"minus-one multiplicity n={n}")
    AUDIT.equal(minus_count, (r - n) // 2, f"plus-one multiplicity n={n}")
    AUDIT.equal(2 + plus_count + minus_count, q, f"spectral dimension n={n}")


def expected_zero_fibre(n: int, m: int) -> int:
    r = n * n
    previous, current = 2, r
    for _ in range(2, m + 1):
        previous, current = current, r * current + previous
    exceptional_trace = current
    return (exceptional_trace
            + (-1) ** m * ((r + n) // 2 - 1)
            + (r - n) // 2)


def image_criterion(target) -> bool:
    m = len(target)
    anchors = [i for i, output in enumerate(target) if output != ZERO]
    if not anchors:
        return True
    for j, position in enumerate(anchors):
        following = anchors[(j + 1) % len(anchors)]
        gap = (following - position - 1) % m
        if gap == 0 and target[following] != inverse_unit(target[position]):
            return False
        if gap == 1 and target[following] == target[position]:
            return False
    return True


def verify_case(n: int, m: int) -> str:
    letters = alphabet(n)
    states = tuple(product(letters, repeat=m))
    fibres = Counter()
    tails = Counter()
    transition_digest = sha256()
    fixed = 0
    state_index = {x: i for i, x in enumerate(states)}

    for source in states:
        current = source
        for time in range(m + 2):
            AUDIT.equal(current, closed_iterate(source, time),
                        f"all-time normal form n={n} m={m} t={time}")
            current = step(current)
        tail, period = literal_tail_period(source)
        AUDIT.equal(period, 1, f"fixed recurrence n={n} m={m}")
        AUDIT.equal(tail, predicted_tail(source), f"pointwise tail n={n} m={m}")
        tails[tail] += 1
        target = step(source)
        fibres[target] += 1
        fixed += int(target == source)
        transition_digest.update(f"{state_index[source]}>{state_index[target]};".encode())

    fixed_formula = 1 + (n if m % 2 else n * n)
    AUDIT.equal(fixed, fixed_formula, f"fixed formula n={n} m={m}")
    sharp_tail = max(0, m - 1) if n == 1 else (m if m % 2 else m - 1)
    AUDIT.equal(max(tails), sharp_tail, f"sharp tail n={n} m={m}")

    matrices = {output: output_matrix(output, letters) for output in letters}
    a0 = matrices[ZERO]
    if m == 1:
        spectral_attack(n, letters, a0)
    q = len(letters)
    identity = tuple(tuple(int(i == j) for j in range(q)) for i in range(q))
    powers = [identity]
    for _ in range(m):
        powers.append(matrix_multiply(powers[-1], a0))
    index = {x: i for i, x in enumerate(letters)}
    transfer_fibres = {}
    for target in states:
        transfer = cyclic_path_fibre(target, letters)
        transfer_fibres[target] = transfer
        AUDIT.equal(transfer, fibres.get(target, 0),
                    f"every-target trace n={n} m={m}")
        if len(states) <= 125:
            AUDIT.equal(trace_product(target, matrices), transfer,
                        f"dense matrix direction n={n} m={m}")
        anchors = [i for i, output in enumerate(target) if output != ZERO]
        if anchors:
            gap_product = 1
            for j, position in enumerate(anchors):
                following = anchors[(j + 1) % len(anchors)]
                gap = (following - position - 1) % m
                gap_product *= powers[gap][index[inverse_unit(target[position])]][index[target[following]]]
            AUDIT.equal(gap_product, transfer, f"anchor gap product n={n} m={m}")
        AUDIT.equal(transfer > 0, image_criterion(target),
                    f"image gap criterion n={n} m={m}")

    all_zero = (ZERO,) * m
    matrix_trace = sum(powers[m][i][i] for i in range(q))
    AUDIT.equal(transfer_fibres[all_zero], matrix_trace,
                f"zero target trace n={n} m={m}")
    AUDIT.equal(matrix_trace, expected_zero_fibre(n, m),
                f"zero target spectrum n={n} m={m}")
    AUDIT.equal(sum(transfer_fibres.values()), q**m,
                f"target fibre mass n={n} m={m}")
    all_matrices = tuple(tuple(sum(matrices[y][i][j] for y in letters)
                               for j in range(q)) for i in range(q))
    AUDIT.equal(all_matrices, tuple(tuple(1 for _ in range(q)) for _ in range(q)),
                f"sum output matrices n={n} m={m}")

    if m == 1:
        AUDIT.equal(fibres[all_zero], n * n - n + 1, f"m=1 zero fibre n={n}")
        for y in letters[1:]:
            AUDIT.equal(fibres.get((y,), 0), int(y == inverse_unit(y)),
                        f"m=1 target boundary n={n} y={y}")
    if m == 2:
        AUDIT.equal(fibres[all_zero], q * q - n * n, f"m=2 zero fibre n={n}")
        for y in letters[1:]:
            target = (y, inverse_unit(y))
            AUDIT.equal(fibres[target], 1, f"m=2 alternating target n={n} y={y}")

    image = len(fibres)
    max_fibre = max(fibres.values())
    return (
        f"n={n} m={m} states={len(states)} image={image} fixed={fixed} "
        f"max_tail={max(tails)} zero_fibre={fibres[all_zero]} "
        f"empty_targets={len(states)-image} max_fibre={max_fibre} "
        f"transition_sha256={transition_digest.hexdigest()}"
    )


def main() -> None:
    print("P190_EXACT_AUTHOR_CONTROL")
    print("scope=finite_falsification_not_proof_not_novelty")
    cases = (
        *((1, m) for m in range(1, 11)),
        *((2, m) for m in range(1, 8)),
        *((3, m) for m in range(1, 5)),
        *((4, m) for m in range(1, 4)),
        *((5, m) for m in range(1, 3)),
    )
    AUDIT.equal(len(cases), 26, "published parameter-box count")
    for n, m in cases:
        print(verify_case(n, m))
    print(f"BOXES={len(cases)}")
    print(f"ASSERTIONS={AUDIT.assertions}")
    print("STATUS=HOLD_EXTERNAL")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
