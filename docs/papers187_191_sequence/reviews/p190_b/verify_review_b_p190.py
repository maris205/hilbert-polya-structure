#!/usr/bin/env python3
"""Process-separated Hostile Review B exact control for frozen P190 Round 1.

This script does not import the author verifier or any reviewer code. It
rebuilds fibres by anchor-gap decomposition: each nonzero output fixes an
anchor letter, and each zero block is counted by a reviewer-owned dynamic
program over literal zero-producing transitions.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import product
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PAPER = ROOT / "papers" / "190-brandt-sandwich-erosion"
FORMAL_REVIEW_A = ROOT / "docs" / "papers187_191_sequence" / "reviews" / "p190_a"

ZERO = (-1, -1)

PINNED_PAPER = {
    "main_round1.pdf": "81c785768621a2c3450fc67eeabc9b91d8cfda67d1061aad851844b5dd68905d",
    "main.tex": "73cb3d23aa88247ecbc22a75651f48f94aaf94113ccb649b1f13d64f9c37d300",
    "references.bib": "3bca1bf9c1f5bff1717e0c84a8263cf71d0763902389f9f647d436bf860a4dc9",
    "code/verify_p190.py": "99bccb56fd9324409f7ee23742dbceda04c76cb887cac7bd8553a1ee84b4f081",
    "code/CANONICAL.txt": "9652d76deed795b561f9ceddd28ff4db1f296215f920d97ad4014b3ca75e6b2f",
    "PROOF_PACKAGE.md": "01ab488f347c91c41650c860ac8e396b6054bcb749e98efa0a83228cbffa6628",
    "SOURCE_VERIFICATION.md": "e873ff99bac17675c124b16a5b5107266e9736f12493bc7f317a5d7de768285c",
}

PINNED_REVIEW_A = {
    "verify_p190_review_a.py": "37cb9f0aa6ba41a9f2dfb337ecbd73e16ca341abf1b7a11288b5a5f7f626f538",
    "CANONICAL.txt": "0a81802b457a69fca9b02a51b12820a7cc0bb5a53bc971f637aa7d5053adc54a",
}

CASES = (
    *((1, m) for m in range(1, 11)),
    *((2, m) for m in range(1, 8)),
    *((3, m) for m in range(1, 5)),
    *((4, m) for m in range(1, 4)),
    *((5, m) for m in range(1, 3)),
)


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


def check_pinned_inputs() -> None:
    for name, expected in PINNED_PAPER.items():
        AUDIT.check(digest(PAPER / name) == expected, f"pinned paper artifact changed: {name}")
    for name, expected in PINNED_REVIEW_A.items():
        AUDIT.check(
            digest(FORMAL_REVIEW_A / name) == expected,
            f"pinned Review-A artifact changed: {name}",
        )

    round1 = PAPER / "main_round1.pdf"
    round2 = PAPER / "main_round2.pdf"
    live = PAPER / "main.pdf"
    AUDIT.check(round2.read_bytes() == round1.read_bytes(), "Round-2 PDF differs from Round-1 receipt")
    AUDIT.check(live.read_bytes() == round1.read_bytes(), "live PDF differs from Round-1 receipt")

    source = (PAPER / "main.tex").read_text(encoding="utf-8")
    bibliography = (PAPER / "references.bib").read_text(encoding="utf-8")
    proof_package = (PAPER / "PROOF_PACKAGE.md").read_text(encoding="utf-8")
    source_verification = (PAPER / "SOURCE_VERIFICATION.md").read_text(encoding="utf-8")
    for needle in (
        "good-run normal form",
        "zero-fibre spectrum",
        "1,555,420",
        r"HOLD\_EXTERNAL",
    ):
        AUDIT.check(
            needle in source or needle in proof_package or needle in source_verification,
            f"contract missing: {needle}",
        )
    AUDIT.check("OWNER_AMBER / HOLD_EXTERNAL" in source_verification, "owner gate missing in source ledger")
    cited = {
        key.strip()
        for group in re.findall(r"\\cite[A-Za-z*]*(?:\s*\[[^\]]*\]){0,2}\s*\{([^{}]+)\}", source)
        for key in group.split(",")
        if key.strip()
    }
    bib = {
        match.group(1).strip()
        for match in re.finditer(
            r"@(?!comment\b|string\b|preamble\b)[A-Za-z]+\s*\{\s*([^,\s]+)",
            bibliography,
            flags=re.IGNORECASE,
        )
    }
    AUDIT.check(cited == bib, "citation/bibliography key mismatch")
    AUDIT.check(len(bib) == 5, "unexpected bibliography cardinality")


def alphabet(n: int) -> tuple[tuple[int, int], ...]:
    return (ZERO,) + tuple((a, b) for a in range(n) for b in range(n))


def inverse_unit(symbol: tuple[int, int]) -> tuple[int, int]:
    return ZERO if symbol == ZERO else (symbol[1], symbol[0])


def multiply(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    if left == ZERO or right == ZERO or left[1] != right[0]:
        return ZERO
    return (left[0], right[1])


def local_output(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    return multiply(multiply(left, right), left)


def step(word: tuple[tuple[int, int], ...]) -> tuple[tuple[int, int], ...]:
    m = len(word)
    return tuple(local_output(word[i], word[(i + 1) % m]) for i in range(m))


def good_edges(word: tuple[tuple[int, int], ...]) -> tuple[bool, ...]:
    m = len(word)
    return tuple(word[i] != ZERO and word[(i + 1) % m] == inverse_unit(word[i]) for i in range(m))


def closed_iterate(word: tuple[tuple[int, int], ...], time: int) -> tuple[tuple[int, int], ...]:
    goods = good_edges(word)
    m = len(word)
    return tuple(
        word[i] if all(goods[(i + j) % m] for j in range(time)) else ZERO
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
    goods = good_edges(word)
    return 0 if all(goods) else longest_cyclic_run(goods) + 1


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
    frontier = Counter({start: 1})
    for _ in range(gap):
        next_frontier: Counter[tuple[int, int]] = Counter()
        for left, count in frontier.items():
            for right in zero_neighbors(n, left):
                next_frontier[right] += count
        frontier = next_frontier
    return frontier[end]


def anchored_fibre(target: tuple[tuple[int, int], ...], n: int) -> int:
    letters = alphabet(n)
    anchors = [i for i, output in enumerate(target) if output != ZERO]
    m = len(target)
    if not anchors:
        return sum(zero_segment_count(n, start, start, m) for start in letters)
    product_value = 1
    for index, left_anchor in enumerate(anchors):
        right_anchor = anchors[(index + 1) % len(anchors)]
        gap = (right_anchor - left_anchor - 1) % m
        start = inverse_unit(target[left_anchor])
        end = target[right_anchor]
        product_value *= zero_segment_count(n, start, end, gap)
    return product_value


def image_criterion(target: tuple[tuple[int, int], ...]) -> bool:
    m = len(target)
    anchors = [i for i, output in enumerate(target) if output != ZERO]
    if not anchors:
        return True
    for index, left_anchor in enumerate(anchors):
        right_anchor = anchors[(index + 1) % len(anchors)]
        gap = (right_anchor - left_anchor - 1) % m
        if gap == 0 and target[right_anchor] != inverse_unit(target[left_anchor]):
            return False
        if gap == 1 and target[right_anchor] == target[left_anchor]:
            return False
    return True


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


def verify_case(n: int, m: int) -> str:
    letters = alphabet(n)
    states = tuple(product(letters, repeat=m))
    indegree: Counter[tuple[tuple[int, int], ...]] = Counter()
    tails: dict[tuple[tuple[int, int], ...], int] = {}
    fixed = 0
    transition_digest = sha256()

    for source in states:
        current = source
        for time in range(m + 2):
            AUDIT.check(current == closed_iterate(source, time), f"all-time iterate n={n} m={m} t={time}")
            current = step(current)

        tail, period = tail_period(source)
        AUDIT.check(period == 1, f"period-one recurrence n={n} m={m}")
        AUDIT.check(tail == predicted_tail(source), f"pointwise tail n={n} m={m}")

        target = step(source)
        indegree[target] += 1
        tails[source] = tail
        fixed += int(target == source)
        transition_digest.update(repr((source, target)).encode("ascii"))

    AUDIT.check(fixed == 1 + (n if m % 2 else n * n), f"fixed formula n={n} m={m}")
    AUDIT.check(max(tails.values()) == (max(0, m - 1) if n == 1 else (m if m % 2 else m - 1)),
                f"sharp tail n={n} m={m}")

    total_mass = 0
    empty_targets = 0
    for target in states:
        predicted = anchored_fibre(target, n)
        actual = indegree.get(target, 0)
        AUDIT.check(predicted == actual, f"every-target gap fibre n={n} m={m}")
        AUDIT.check((predicted > 0) == image_criterion(target), f"image criterion n={n} m={m}")
        total_mass += predicted
        if predicted == 0:
            empty_targets += 1

    all_zero = (ZERO,) * m
    AUDIT.check(indegree[all_zero] == expected_zero_fibre(n, m), f"zero fibre formula n={n} m={m}")
    AUDIT.check(total_mass == len(states), f"mass identity n={n} m={m}")

    if m == 1:
        AUDIT.check(indegree[all_zero] == n * n - n + 1, f"m=1 zero fibre n={n}")
        for symbol in letters[1:]:
            AUDIT.check(
                indegree.get((symbol,), 0) == int(symbol == inverse_unit(symbol)),
                f"m=1 boundary n={n} symbol={symbol}",
            )
    if m == 2:
        AUDIT.check(indegree[all_zero] == (n * n + 1) ** 2 - n * n, f"m=2 zero fibre n={n}")
        for symbol in letters[1:]:
            AUDIT.check(
                indegree[(symbol, inverse_unit(symbol))] == 1,
                f"m=2 alternating fibre n={n} symbol={symbol}",
            )

    return (
        f"n={n} m={m} states={len(states)} fixed={fixed} max_tail={max(tails.values())} "
        f"zero_fibre={indegree[all_zero]} image={len(indegree)} empty_targets={empty_targets} "
        f"transition_sha256={transition_digest.hexdigest()}"
    )


def main() -> None:
    check_pinned_inputs()
    AUDIT.check(len(CASES) == 26, "published box count")
    print("P190 process-separated hostile Review B")
    print("reviewer_representation=anchor_gap_zero_transition_dp")
    print(f"pinned_input_count={len(PINNED_PAPER) + len(PINNED_REVIEW_A)}")
    print("formal_review_a_root=docs/papers187_191_sequence/reviews/p190_a")
    print(f"frozen_round1_pdf_sha256={PINNED_PAPER['main_round1.pdf']}")
    print(f"frozen_main_tex_sha256={PINNED_PAPER['main.tex']}")
    print(f"frozen_references_bib_sha256={PINNED_PAPER['references.bib']}")
    print(f"frozen_author_verifier_sha256={PINNED_PAPER['code/verify_p190.py']}")
    print(f"frozen_author_canonical_sha256={PINNED_PAPER['code/CANONICAL.txt']}")
    print(f"frozen_proof_package_sha256={PINNED_PAPER['PROOF_PACKAGE.md']}")
    print(f"frozen_source_verification_sha256={PINNED_PAPER['SOURCE_VERIFICATION.md']}")
    print(f"formal_review_a_verifier_sha256={PINNED_REVIEW_A['verify_p190_review_a.py']}")
    print(f"formal_review_a_canonical_sha256={PINNED_REVIEW_A['CANONICAL.txt']}")
    print(f"case_count={len(CASES)}")
    for n, m in CASES:
        print(verify_case(n, m))
    print(f"exact_assertions={AUDIT.assertions}")
    print("critical_findings=0")
    print("major_findings=0")
    print("minor_findings=0")
    print("verdict=PASS")
    print("external_status=OWNER_AMBER/HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
