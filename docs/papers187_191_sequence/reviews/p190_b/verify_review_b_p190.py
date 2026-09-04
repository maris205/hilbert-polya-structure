#!/usr/bin/env python3
"""Process-separated Hostile Review B exact control for frozen P190 Round 1.

This script does not import the author verifier or Review-A harness.  It
rebuilds fibres by anchor-gap decomposition: each nonzero output fixes an
anchor letter, and every zero block is counted by a reviewer-owned dynamic
program over literal zero-producing transitions, not by matrix traces or the
Review-A integer-word implementation.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import product
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
PAPER = ROOT / "papers" / "190-brandt-sandwich-erosion"
REVIEW_A = ROOT / "docs" / "papers187_191_sequence" / "reviews" / "p190_a"

ZERO = (-1, -1)

FROZEN = {
    "main.tex": "73cb3d23aa88247ecbc22a75651f48f94aaf94113ccb649b1f13d64f9c37d300",
    "references.bib": "3bca1bf9c1f5bff1717e0c84a8263cf71d0763902389f9f647d436bf860a4dc9",
    "code/verify_p190.py": "99bccb56fd9324409f7ee23742dbceda04c76cb887cac7bd8553a1ee84b4f081",
    "code/CANONICAL.txt": "9652d76deed795b561f9ceddd28ff4db1f296215f920d97ad4014b3ca75e6b2f",
    "PROOF_PACKAGE.md": "01ab488f347c91c41650c860ac8e396b6054bcb749e98efa0a83228cbffa6628",
    "SOURCE_VERIFICATION.md": "e873ff99bac17675c124b16a5b5107266e9736f12493bc7f317a5d7de768285c",
    "main_round0_original.pdf": "5fb58fae99f49f14653f5eee283e2f66c3af87c06fca65e1b982e5936123eb66",
    "main_round1.pdf": "81c785768621a2c3450fc67eeabc9b91d8cfda67d1061aad851844b5dd68905d",
    "main.pdf": "81c785768621a2c3450fc67eeabc9b91d8cfda67d1061aad851844b5dd68905d",
}

FROZEN_REVIEW_A = {
    "REVIEW.md": "6f95da526e1b452cd5917d5a80549fd232cf2497e72022b53a1c15510d08ec52",
    "DELTA.md": "9238c5b2e3b16df8c9a926fd9b4924d1d8010510f65e9cd12454689ca1787b9a",
    "verify_p190_review_a.py": "69244d59d86c7706918471223eeb27f03624b7e71b564ca53ee64dcf45083d2e",
    "CANONICAL.txt": "a8efc0326e810b8884afad04ae7edbd6d303ff9079cc6e0f8a182a80c1432a5c",
}


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, message: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message)


AUDIT = Audit()


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def check_frozen_artifacts() -> None:
    for name, expected in FROZEN.items():
        AUDIT.check(digest(PAPER / name) == expected, f"frozen artifact changed: {name}")
    for name, expected in FROZEN_REVIEW_A.items():
        AUDIT.check(digest(REVIEW_A / name) == expected, f"Review-A artifact changed: {name}")

    AUDIT.check((PAPER / "main.pdf").read_bytes() == (PAPER / "main_round1.pdf").read_bytes(),
                "live PDF and Round-1 PDF differ")

    source = (PAPER / "main.tex").read_text(encoding="utf-8")
    bibliography = (PAPER / "references.bib").read_text(encoding="utf-8")
    for needle in (
        r"\texttt{HOLD\_EXTERNAL}",
        "1,555,420",
        r"\operatorname{im}",
        r"(uv)u",
    ):
        AUDIT.check(needle in source or needle in (PAPER / "README.md").read_text(encoding="utf-8"),
                    f"contract missing: {needle}")
    cited = {
        key.strip()
        for group in re.findall(r"\\cite[A-Za-z*]*(?:\s*\[[^\]]*\]){0,2}\s*\{([^{}]+)\}", source)
        for key in group.split(",")
        if key.strip()
    }
    bib = {
        match.group(1).strip()
        for match in re.finditer(r"@(?!comment\b|string\b|preamble\b)[A-Za-z]+\s*\{\s*([^,\s]+)",
                                 bibliography, flags=re.IGNORECASE)
    }
    AUDIT.check(cited == bib, "citation/bibliography key mismatch")
    AUDIT.check(len(bib) == 5, "unexpected bibliography cardinality")


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
    return tuple(word[i] != ZERO and word[(i + 1) % m] == inverse_unit(word[i]) for i in range(m))


def closed_iterate(word: tuple[tuple[int, int], ...], time: int) -> tuple[tuple[int, int], ...]:
    good = good_edges(word)
    m = len(word)
    return tuple(
        word[i] if all(good[(i + j) % m] for j in range(time)) else ZERO
        for i in range(m)
    )


def longest_cyclic_run(bits: tuple[bool, ...]) -> int:
    if all(bits):
        return len(bits)
    best = 0
    run = 0
    for bit in bits + bits:
        run = run + 1 if bit else 0
        best = max(best, run)
    return min(best, len(bits) - 1)


def predicted_tail(word: tuple[tuple[int, int], ...]) -> int:
    if all(letter == ZERO for letter in word):
        return 0
    good = good_edges(word)
    return 0 if all(good) else longest_cyclic_run(good) + 1


def tail_period(start: tuple[tuple[int, int], ...]) -> tuple[int, int]:
    seen = {}
    current = start
    while current not in seen:
        seen[current] = len(seen)
        current = step(current)
    return seen[current], len(seen) - seen[current]


@lru_cache(maxsize=None)
def zero_neighbors(n: int, left: tuple[int, int]) -> tuple[tuple[int, int], ...]:
    letters = alphabet(n)
    return tuple(right for right in letters if local_output(left, right) == ZERO)


@lru_cache(maxsize=None)
def zero_segment_count(n: int, start: tuple[int, int], end: tuple[int, int], gap: int) -> int:
    if gap == 0:
        return int(start == end)
    current = Counter({start: 1})
    for _ in range(gap):
        nxt: Counter[tuple[int, int]] = Counter()
        for left, count in current.items():
            for right in zero_neighbors(n, left):
                nxt[right] += count
        current = nxt
    return current[end]


def anchored_fibre(target: tuple[tuple[int, int], ...], n: int) -> int:
    letters = alphabet(n)
    anchors = [i for i, output in enumerate(target) if output != ZERO]
    m = len(target)
    if not anchors:
        return sum(zero_segment_count(n, first, first, m) for first in letters)
    total = 1
    for j, position in enumerate(anchors):
        next_position = anchors[(j + 1) % len(anchors)]
        gap = (next_position - position - 1) % m
        start = inverse_unit(target[position])
        end = target[next_position]
        total *= zero_segment_count(n, start, end, gap)
        if total == 0:
            return 0
    return total


def zero_exceptional_trace(n: int, m: int) -> int:
    r = n * n
    if m == 0:
        return 2
    if m == 1:
        return r
    previous, current = 2, r
    for _ in range(2, m + 1):
        previous, current = current, r * current + previous
    return current


def expected_zero_fibre(n: int, m: int) -> int:
    r = n * n
    return zero_exceptional_trace(n, m) + ((-1) ** m) * ((r + n) // 2 - 1) + (r - n) // 2


def image_criterion(target: tuple[tuple[int, int], ...]) -> bool:
    m = len(target)
    anchors = [i for i, output in enumerate(target) if output != ZERO]
    if not anchors:
        return True
    for j, position in enumerate(anchors):
        next_position = anchors[(j + 1) % len(anchors)]
        gap = (next_position - position - 1) % m
        if gap == 0 and target[next_position] != inverse_unit(target[position]):
            return False
        if gap == 1 and target[next_position] == target[position]:
            return False
    return True


def verify_case(n: int, m: int) -> str:
    letters = alphabet(n)
    states = tuple(product(letters, repeat=m))
    fibres: Counter[tuple[tuple[int, int], ...]] = Counter()
    fixed = 0
    tails: Counter[int] = Counter()
    digest_transitions = sha256()

    for source in states:
        current = source
        for time in range(m + 2):
            AUDIT.check(current == closed_iterate(source, time),
                        f"all-time normal form n={n} m={m} t={time}")
            current = step(current)

        tail, period = tail_period(source)
        AUDIT.check(period == 1, f"fixed recurrence only n={n} m={m}")
        AUDIT.check(tail == predicted_tail(source), f"pointwise tail n={n} m={m}")
        tails[tail] += 1

        target = step(source)
        fibres[target] += 1
        fixed += int(target == source)
        digest_transitions.update(repr(source).encode("ascii"))
        digest_transitions.update(b"->")
        digest_transitions.update(repr(target).encode("ascii"))
        digest_transitions.update(b";")

    expected_fixed = 1 + (n if m % 2 else n * n)
    AUDIT.check(fixed == expected_fixed, f"fixed-state formula n={n} m={m}")
    expected_tail = max(0, m - 1) if n == 1 else (m if m % 2 else m - 1)
    AUDIT.check(max(tails) == expected_tail, f"sharp tail n={n} m={m}")

    all_zero = (ZERO,) * m
    transfer_mass = 0
    empty_targets = 0
    for target in states:
        predicted = anchored_fibre(target, n)
        actual = fibres.get(target, 0)
        AUDIT.check(predicted == actual, f"anchored fibre n={n} m={m}")
        AUDIT.check((predicted > 0) == image_criterion(target), f"image criterion n={n} m={m}")
        if predicted == 0:
            empty_targets += 1
        transfer_mass += predicted

    AUDIT.check(fibres[all_zero] == expected_zero_fibre(n, m), f"zero-fibre spectrum n={n} m={m}")
    AUDIT.check(transfer_mass == len(states), f"fibre mass n={n} m={m}")

    if m == 1:
        AUDIT.check(fibres[all_zero] == n * n - n + 1, f"m=1 zero fibre n={n}")
        for y in letters[1:]:
            AUDIT.check(fibres.get((y,), 0) == int(y == inverse_unit(y)),
                        f"m=1 target boundary n={n} target={y}")
    if m == 2:
        q = len(letters)
        AUDIT.check(fibres[all_zero] == q * q - n * n, f"m=2 zero fibre n={n}")
        for y in letters[1:]:
            target = (y, inverse_unit(y))
            AUDIT.check(fibres[target] == 1, f"m=2 alternating target n={n} target={y}")

    return (
        f"n={n} m={m} states={len(states)} fixed={fixed} max_tail={max(tails)} "
        f"zero_fibre={fibres[all_zero]} image={len(fibres)} empty_targets={empty_targets} "
        f"transition_sha256={digest_transitions.hexdigest()}"
    )


def main() -> None:
    check_frozen_artifacts()
    print("P190 process-separated hostile Review B")
    print("reviewer_representation=anchor_gap_zero_transition_dp")
    print(f"frozen_main_tex_sha256={FROZEN['main.tex']}")
    print(f"frozen_round1_pdf_sha256={FROZEN['main_round1.pdf']}")
    print(f"review_a_canonical_sha256={FROZEN_REVIEW_A['CANONICAL.txt']}")
    cases = (
        *((1, m) for m in range(1, 11)),
        *((2, m) for m in range(1, 8)),
        *((3, m) for m in range(1, 5)),
        *((4, m) for m in range(1, 4)),
        *((5, m) for m in range(1, 3)),
    )
    AUDIT.check(len(cases) == 26, "parameter-box count changed")
    for n, m in cases:
        print(verify_case(n, m))
    print(f"exact_assertions={AUDIT.assertions}")
    print("verdict=PASS")
    print("external_status=OWNER_AMBER/HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
