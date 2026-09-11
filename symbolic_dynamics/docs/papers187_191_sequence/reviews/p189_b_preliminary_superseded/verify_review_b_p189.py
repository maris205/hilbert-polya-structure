#!/usr/bin/env python3
"""Process-separated Hostile Review B control for frozen P189 Round 1.

This script does not import the author verifier or Review-A code.  It encodes
each matrix as a tuple of labelled row bitmasks, then rebuilds the dynamics
through row-sum vectors, partition conjugation, and Ferrers diagrams.  The
recurrent set and the two fibre laws are attacked through degree-sequence
combinatorics rather than the Review-A row-support graph search.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import combinations_with_replacement, product
from math import comb, factorial, prod
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PAPER = ROOT / "papers" / "189-transpose-row-compression"
REVIEW_A = PAPER / "reviews" / "round1" / "reviewer_a"

FROZEN = {
    "main.tex": "c9c4417012fcc9663ac3c3ac3fe9f5113fdf4fe4213846d2a6815b7657724457",
    "references.bib": "fbed4d833c2855548bc721b793ad74da2e5fcf994fccbc35e2fdbae74bb1ac4c",
    "code/verify_p189.py": "b87fde66e16b164544eb6bc0463e4b4d4e82fae8531b43c322cbb96df0db7a5c",
    "code/CANONICAL.txt": "9474855682c21a356876b12aef70d8cc12af929bb5846b3c259a4f037048ef25",
    "PROOF_PACKAGE.md": "a7d70011494b86d5369627a6cb84846074dc3bd01b49d2c36f9421b727c331b4",
    "SOURCE_VERIFICATION.md": "96a8457ffcffe79a6208ad6167699f30dc70a4390350a83108a9c252ee3c3250",
    "main_round0_original.pdf": "6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81",
    "main_round1.pdf": "6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81",
    "main.pdf": "6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81",
}

FROZEN_REVIEW_A = {
    "REVIEW.md": "c1231f3cd08882e636404cef43adf77e1cb8251fb67946df50bb5b96394dd7a0",
    "DELTA.md": "4ec9622020dc2f4e43d8f01916d3eb4f4d4ea9b4cc548ed3c94cfe0f5016e9f7",
    "verify_review_a.py": "4954766bcdf4a56f15544b7157f1be7afa607b5ea6ab58c419cbb87ab06d5b8b",
    "CANONICAL.txt": "7fed29f8dd04c2493772596e788a9763222dc5a31d7be70ecdbef28e8d717139",
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

    payloads = [
        (PAPER / "main.pdf").read_bytes(),
        (PAPER / "main_round0_original.pdf").read_bytes(),
        (PAPER / "main_round1.pdf").read_bytes(),
    ]
    AUDIT.check(payloads[0] == payloads[1] == payloads[2], "live and frozen PDFs differ")

    source = (PAPER / "main.tex").read_text(encoding="utf-8")
    bibliography = (PAPER / "references.bib").read_text(encoding="utf-8")
    readme = (PAPER / "README.md").read_text(encoding="utf-8")
    for needle in (
        r"F^4(A)=F^2(A)",
        r"\binom{2n}{n}",
        r"(n+1)^n",
        "HOLD_EXTERNAL",
        "5,336,613",
    ):
        AUDIT.check(needle in source or needle in readme,
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
    AUDIT.check(cited == bib, "citation and bibliography keys differ")
    AUDIT.check(len(bib) == 4, "unexpected bibliography cardinality")


State = tuple[int, ...]


@lru_cache(maxsize=None)
def states(n: int) -> tuple[State, ...]:
    rows = range(1 << n)
    return tuple(product(rows, repeat=n))


def row_sums(state: State, n: int) -> tuple[int, ...]:
    return tuple(row.bit_count() for row in state)


def diagram(column_heights: tuple[int, ...], n: int) -> State:
    rows = []
    for i in range(n):
        row = 0
        for j, height in enumerate(column_heights):
            if i < height:
                row |= 1 << j
        rows.append(row)
    return tuple(rows)


def step(state: State, n: int) -> State:
    return diagram(row_sums(state, n), n)


def conjugate(vector: tuple[int, ...], n: int) -> tuple[int, ...]:
    return tuple(sum(value >= level for value in vector) for level in range(1, n + 1))


def decreasing(vector: tuple[int, ...]) -> bool:
    return all(vector[i] >= vector[i + 1] for i in range(len(vector) - 1))


def column_heights(state: State, n: int) -> tuple[int, ...] | None:
    heights = []
    for j in range(n):
        height = 0
        while height < n and ((state[height] >> j) & 1):
            height += 1
        if any((state[i] >> j) & 1 for i in range(height, n)):
            return None
        heights.append(height)
    return tuple(heights)


def recurrent(state: State, n: int) -> bool:
    heights = column_heights(state, n)
    return heights is not None and decreasing(heights)


def predicted_depth(state: State, n: int) -> int:
    if recurrent(state, n):
        return 0
    if decreasing(row_sums(state, n)):
        return 1
    return 2


def literal_depth(state: State, n: int) -> int:
    current = state
    for depth in range(3):
        if recurrent(current, n):
            return depth
        current = step(current, n)
    raise AssertionError("depth exceeded two")


def first_fibre_formula(target: State, n: int) -> int:
    heights = column_heights(target, n)
    if heights is None:
        return 0
    return prod(comb(n, height) for height in heights)


def second_fibre_formula(target: State, n: int) -> int:
    heights = column_heights(target, n)
    if heights is None or not decreasing(heights):
        return 0
    required = conjugate(heights, n)
    multiplicities = Counter(required)
    arrangements = factorial(n) // prod(factorial(value) for value in multiplicities.values())
    return arrangements * prod(comb(n, value) for value in required)


def weak_row_sum_population(n: int) -> int:
    coefficients = [1] + [0] * n
    for k in range(n + 1):
        weight = comb(n, k)
        nxt = [0] * (n + 1)
        for old_degree, old_value in enumerate(coefficients):
            for multiplicity in range(n - old_degree + 1):
                nxt[old_degree + multiplicity] += old_value * (weight ** multiplicity)
        coefficients = nxt
    return coefficients[n]


def witness_checks() -> None:
    witness = (0b00, 0b01)
    first = step(witness, 2)
    second = step(first, 2)
    third = step(second, 2)
    AUDIT.check(second != first, "F^2=F false witness missing")
    AUDIT.check(third != first, "F^3=F false witness missing")
    AUDIT.check(step(step(third, 2), 2) == third, "witness post-height periodicity")


def verify_box(n: int) -> str:
    first_fibres: Counter[State] = Counter()
    second_fibres: Counter[State] = Counter()
    depths: Counter[int] = Counter()
    recurrent_count = 0
    fixed_count = 0
    transition_digest = sha256()

    for state in states(n):
        sums = row_sums(state, n)
        sorted_sums = tuple(sorted(sums, reverse=True))
        first = step(state, n)
        second = step(first, n)
        third = step(second, n)
        fourth = step(third, n)

        AUDIT.check(first == diagram(sums, n), f"time-one form n={n}")
        AUDIT.check(second == diagram(conjugate(sums, n), n), f"time-two form n={n}")
        AUDIT.check(third == diagram(sorted_sums, n), f"time-three form n={n}")
        AUDIT.check(fourth == second, f"F^4=F^2 n={n}")
        AUDIT.check(step(fourth, n) == third, f"odd tail phase n={n}")
        AUDIT.check(step(third, n) == fourth, f"even tail phase n={n}")

        literal_recurrent = recurrent(state, n)
        AUDIT.check(literal_recurrent == (second == state), f"recurrent criterion n={n}")
        if literal_recurrent:
            recurrent_count += 1
            AUDIT.check(step(step(state, n), n) == state, f"period-two recurrence n={n}")
        if first == state:
            fixed_count += 1
            heights = column_heights(state, n)
            AUDIT.check(heights is not None and heights == conjugate(heights, n),
                        f"fixed self-conjugacy n={n}")

        depth = literal_depth(state, n)
        AUDIT.check(depth == predicted_depth(state, n), f"depth predicate n={n}")
        depths[depth] += 1

        first_fibres[first] += 1
        second_fibres[second] += 1
        transition_digest.update(("".join(f"{row:0{n}b}" for row in state) + "->").encode("ascii"))
        transition_digest.update(("".join(f"{row:0{n}b}" for row in first) + ";").encode("ascii"))

    for target in states(n):
        AUDIT.check(first_fibres[target] == first_fibre_formula(target, n),
                    f"time-one fibre n={n}")
        AUDIT.check(second_fibres[target] == second_fibre_formula(target, n),
                    f"time-two fibre n={n}")

    total_states = 2 ** (n * n)
    AUDIT.check(sum(first_fibres.values()) == total_states, f"time-one mass n={n}")
    AUDIT.check(sum(second_fibres.values()) == total_states, f"time-two mass n={n}")
    AUDIT.check(sum(value > 0 for value in first_fibres.values()) == (n + 1) ** n,
                f"time-one image count n={n}")
    AUDIT.check(sum(value > 0 for value in second_fibres.values()) == comb(2 * n, n),
                f"time-two image count n={n}")
    AUDIT.check(recurrent_count == comb(2 * n, n), f"recurrent count n={n}")
    AUDIT.check(fixed_count == 2 ** n, f"fixed count n={n}")
    AUDIT.check((recurrent_count - fixed_count) % 2 == 0, f"two-cycle parity n={n}")

    weak = weak_row_sum_population(n)
    expected_depths = {
        0: comb(2 * n, n),
        1: weak - comb(2 * n, n),
        2: total_states - weak,
    }
    AUDIT.check(dict(depths) == {k: v for k, v in expected_depths.items() if v},
                f"depth counts n={n}")
    if n == 1:
        AUDIT.check(expected_depths == {0: 2, 1: 0, 2: 0}, "n=1 depth boundary")
    else:
        AUDIT.check(expected_depths[1] > 0 and expected_depths[2] > 0,
                    f"strict positive depth layers n={n}")

    return (
        f"n={n} states={total_states} recurrent={recurrent_count} fixed={fixed_count} "
        f"depths={expected_depths[0]},{expected_depths[1]},{expected_depths[2]} "
        f"image1={(n + 1) ** n} image2={comb(2 * n, n)} "
        f"transition_sha256={transition_digest.hexdigest()}"
    )


def transfer_checks() -> list[str]:
    rows = []
    for n in range(1, 13):
        weak = weak_row_sum_population(n)
        AUDIT.check(comb(2 * n, n) <= weak <= 2 ** (n * n), f"depth bounds n={n}")
        if n <= 10:
            partition_sum = sum(
                prod(comb(n, part) for part in tuple(reversed(parts)))
                for parts in combinations_with_replacement(range(n + 1), n)
            )
            AUDIT.check(weak == partition_sum, f"partition coefficient formula n={n}")
        rows.append(
            f"n={n} recurrent={comb(2 * n, n)} fixed={2 ** n} "
            f"depth_at_most_one={weak} depth_two={2 ** (n * n) - weak}"
        )
    return rows


def main() -> None:
    check_frozen_artifacts()
    witness_checks()
    print("P189 process-separated hostile Review B")
    print("reviewer_representation=labelled_row_bitmasks_degree_sequence")
    print(f"frozen_main_tex_sha256={FROZEN['main.tex']}")
    print(f"frozen_round1_pdf_sha256={FROZEN['main_round1.pdf']}")
    print(f"review_a_canonical_sha256={FROZEN_REVIEW_A['CANONICAL.txt']}")
    for n in range(1, 5):
        print(verify_box(n))
    for row in transfer_checks():
        print(row)
    print(f"exact_assertions={AUDIT.assertions}")
    print("verdict=PASS")
    print("external_status=OWNER_AMBER/HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
