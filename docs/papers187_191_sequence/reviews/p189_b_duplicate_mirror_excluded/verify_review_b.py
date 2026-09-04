#!/usr/bin/env python3
"""Process-separated hostile verifier for P189 Round 1.

Representation firewall: matrices are tuples of column bit-tuples, not the
author's packed integers and not Review A's row-support frozensets.  The
literal update is rebuilt from row sums into initial-segment columns, while
recurrence and depth are recovered by memoized orbit repeat detection rather
than indegree peeling.  Partition conjugation is also checked independently via
explicit Ferrers cell reflection.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import product
from math import comb, factorial, prod
from pathlib import Path
import re
import subprocess


REVIEW_DATE = "2026-09-04"
EXPECTED_TEX_SHA = "c9c4417012fcc9663ac3c3ac3fe9f5113fdf4fe4213846d2a6815b7657724457"
EXPECTED_PDF_SHA = "6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81"
EXPECTED_BIB_SHA = "fbed4d833c2855548bc721b793ad74da2e5fcf994fccbc35e2fdbae74bb1ac4c"
EXPECTED_AUTHOR_VERIFY_SHA = "b87fde66e16b164544eb6bc0463e4b4d4e82fae8531b43c322cbb96df0db7a5c"
EXPECTED_AUTHOR_CANON_SHA = "9474855682c21a356876b12aef70d8cc12af929bb5846b3c259a4f037048ef25"
EXPECTED_REVIEW_A_VERIFY_SHA = "4954766bcdf4a56f15544b7157f1be7afa607b5ea6ab58c419cbb87ab06d5b8b"
EXPECTED_REVIEW_A_CANON_SHA = "7fed29f8dd04c2493772596e788a9763222dc5a31d7be70ecdbef28e8d717139"
EXPECTED_CITE_KEYS = {
    "Andrews1998",
    "DasDasSen2016",
    "KouteckyOnn2020",
    "Miller2013",
}


Column = tuple[int, ...]
Matrix = tuple[Column, ...]
Shape = tuple[int, ...]


class Audit:
    def __init__(self) -> None:
        self.count = 0

    def require(self, condition: bool, label: str) -> None:
        self.count += 1
        if not condition:
            raise AssertionError(label)


AUDIT = Audit()


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def column_patterns(n: int) -> tuple[Column, ...]:
    return tuple(product((0, 1), repeat=n))


def matrices(n: int) -> tuple[Matrix, ...]:
    return tuple(product(column_patterns(n), repeat=n))


def row_sums(matrix: Matrix, n: int) -> Shape:
    return tuple(sum(matrix[column][row] for column in range(n)) for row in range(n))


def column_from_height(height: int, n: int) -> Column:
    return tuple(1 if row < height else 0 for row in range(n))


def diagram(heights: Shape, n: int) -> Matrix:
    return tuple(column_from_height(height, n) for height in heights)


def update(matrix: Matrix, n: int) -> Matrix:
    return diagram(row_sums(matrix, n), n)


def initial_heights(matrix: Matrix, n: int) -> Shape | None:
    heights = []
    for column in matrix:
        height = 0
        while height < n and column[height] == 1:
            height += 1
        if any(column[row] for row in range(height, n)):
            return None
        heights.append(height)
    return tuple(heights)


def weakly_decreasing(values: Shape) -> bool:
    return all(left >= right for left, right in zip(values, values[1:]))


def threshold(heights: Shape, n: int) -> Shape:
    return tuple(sum(height >= level for height in heights) for level in range(1, n + 1))


def ferrers_cells(shape: Shape) -> frozenset[tuple[int, int]]:
    return frozenset(
        (row, column)
        for row, part in enumerate(shape)
        for column in range(part)
    )


def conjugate_partition(shape: Shape, n: int) -> Shape:
    cells = ferrers_cells(shape)
    return tuple(sum((column, row) in cells for column in range(n)) for row in range(n))


def ferrers(matrix: Matrix, n: int) -> bool:
    heights = initial_heights(matrix, n)
    return heights is not None and weakly_decreasing(heights)


def fixed_predicate(matrix: Matrix, n: int) -> bool:
    heights = initial_heights(matrix, n)
    return heights is not None and weakly_decreasing(heights) and threshold(heights, n) == heights


def first_fibre_formula(target: Matrix, n: int) -> int:
    heights = initial_heights(target, n)
    if heights is None:
        return 0
    return prod(comb(n, height) for height in heights)


def second_fibre_formula(target: Matrix, n: int) -> int:
    mu = initial_heights(target, n)
    if mu is None or not weakly_decreasing(mu):
        return 0
    lam = conjugate_partition(mu, n)
    multiplicity = Counter(lam)
    return (
        factorial(n) // prod(factorial(value) for value in multiplicity.values())
        * prod(comb(n, part) for part in lam)
    )


def encode(matrix: Matrix, n: int) -> str:
    return "/".join(
        "".join(str(matrix[column][row]) for column in range(n))
        for row in range(n)
    )


def single_one(n: int, row: int, column: int) -> Matrix:
    return tuple(
        tuple(1 if (r == row and c == column) else 0 for r in range(n))
        for c in range(n)
    )


def orbit_profile(
    state: Matrix,
    successor: dict[Matrix, Matrix],
    memo: dict[Matrix, tuple[tuple[Matrix, ...], int]],
) -> tuple[tuple[Matrix, ...], int]:
    if state in memo:
        return memo[state]

    trail: list[Matrix] = []
    positions: dict[Matrix, int] = {}
    cursor = state
    while cursor not in memo and cursor not in positions:
        positions[cursor] = len(trail)
        trail.append(cursor)
        cursor = successor[cursor]

    if cursor in memo:
        cycle, depth = memo[cursor]
        current_depth = depth
        for item in reversed(trail):
            current_depth += 1
            memo[item] = (cycle, current_depth)
        return memo[state]

    cycle_start = positions[cursor]
    cycle = tuple(trail[cycle_start:])
    for item in cycle:
        memo[item] = (cycle, 0)

    depth = 0
    for item in reversed(trail[:cycle_start]):
        depth += 1
        memo[item] = (cycle, depth)
    return memo[state]


def partition_vectors(n: int):
    def descend(prefix: Shape, ceiling: int):
        if len(prefix) == n:
            yield prefix
            return
        for value in range(ceiling, -1, -1):
            yield from descend(prefix + (value,), value)

    yield from descend((), n)


def weighted_partition_sum(n: int) -> int:
    return sum(prod(comb(n, part) for part in shape) for shape in partition_vectors(n))


def weighted_coefficient(n: int) -> int:
    coefficients = [1] + [0] * n
    for k in range(n + 1):
        weight = comb(n, k)
        replacement = [0] * (n + 1)
        for degree, value in enumerate(coefficients):
            if value == 0:
                continue
            for multiplicity in range(n - degree + 1):
                replacement[degree + multiplicity] += value * (weight ** multiplicity)
        coefficients = replacement
    return coefficients[n]


def artifact_gate() -> tuple[dict[str, str], dict[str, str], int]:
    review_dir = Path(__file__).resolve().parent
    paper_dir = review_dir.parents[2]

    tex = paper_dir / "main.tex"
    pdf = paper_dir / "main_round1.pdf"
    bib = paper_dir / "references.bib"
    author_verify = paper_dir / "code" / "verify_p189.py"
    author_canon = paper_dir / "code" / "CANONICAL.txt"
    review_a_verify = paper_dir / "reviews" / "round1" / "reviewer_a" / "verify_review_a.py"
    review_a_canon = paper_dir / "reviews" / "round1" / "reviewer_a" / "CANONICAL.txt"

    hashes = {
        "tex": file_sha(tex),
        "pdf": file_sha(pdf),
        "bib": file_sha(bib),
        "author_verify": file_sha(author_verify),
        "author_canon": file_sha(author_canon),
        "review_a_verify": file_sha(review_a_verify),
        "review_a_canon": file_sha(review_a_canon),
    }

    AUDIT.require(hashes["tex"] == EXPECTED_TEX_SHA, "main.tex drift")
    AUDIT.require(hashes["pdf"] == EXPECTED_PDF_SHA, "main_round1.pdf drift")
    AUDIT.require(hashes["bib"] == EXPECTED_BIB_SHA, "references.bib drift")
    AUDIT.require(hashes["author_verify"] == EXPECTED_AUTHOR_VERIFY_SHA, "author verifier drift")
    AUDIT.require(hashes["author_canon"] == EXPECTED_AUTHOR_CANON_SHA, "author canonical drift")
    AUDIT.require(hashes["review_a_verify"] == EXPECTED_REVIEW_A_VERIFY_SHA, "review A verifier drift")
    AUDIT.require(hashes["review_a_canon"] == EXPECTED_REVIEW_A_CANON_SHA, "review A canonical drift")

    source = tex.read_text(encoding="utf-8")
    bibliography = bib.read_text(encoding="utf-8")
    cite_keys = set()
    for group in re.findall(r"\\cite\{([^}]*)\}", source):
        cite_keys.update(key.strip() for key in group.split(","))
    bib_keys = set(re.findall(r"^@\w+\{([^,]+),", bibliography, flags=re.MULTILINE))
    AUDIT.require(cite_keys == EXPECTED_CITE_KEYS, "manuscript cite keys")
    AUDIT.require(bib_keys == EXPECTED_CITE_KEYS, "bibliography key set")
    AUDIT.require("F^4=F^2" in source, "F^4=F^2 missing from source")
    AUDIT.require("owner\\_amber / hold\\_external" in source.lower(), "HOLD_EXTERNAL missing from source")

    pdfinfo_output = subprocess.run(
        ["pdfinfo", str(pdf)],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()
    pdfinfo_data = {}
    for line in pdfinfo_output:
        if ":" in line:
            key, value = line.split(":", 1)
            pdfinfo_data[key.strip()] = value.strip()

    AUDIT.require(pdfinfo_data["Pages"] == "4", "unexpected page count")
    AUDIT.require(pdfinfo_data["Page size"].endswith("(A4)"), "unexpected page size")
    AUDIT.require(pdfinfo_data["Encrypted"] == "no", "PDF unexpectedly encrypted")
    AUDIT.require(pdfinfo_data["Form"] == "none", "PDF unexpectedly contains forms")
    AUDIT.require(pdfinfo_data["JavaScript"] == "no", "PDF unexpectedly contains JavaScript")
    AUDIT.require(pdfinfo_data["Metadata Stream"] == "no", "PDF unexpectedly contains a metadata stream")
    AUDIT.require(
        all(pdfinfo_data[field] == "" for field in ("Title", "Subject", "Keywords", "Author", "Creator", "Producer")),
        "PDF metadata fields not blank",
    )

    font_rows = subprocess.run(
        ["pdffonts", str(pdf)],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.splitlines()[2:]
    font_rows = [line for line in font_rows if line.strip()]
    AUDIT.require(len(font_rows) == 29, "unexpected font-row count")
    AUDIT.require(
        all(" yes yes yes " in f" {line} " for line in font_rows),
        "not all fonts are embedded/subsetted/Unicode-mapped",
    )

    pdf_text = subprocess.run(
        ["pdftotext", str(pdf), "-"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.lower()
    for needle in (
        "four-iterate collapse",
        "every-target fibres at times one and two",
        "references",
        "owner_amber / hold_external",
    ):
        AUDIT.require(needle in pdf_text, f"rendered text missing {needle}")

    return hashes, pdfinfo_data, len(font_rows)


def exhaustive_box(n: int, transition_digest: sha256) -> tuple[dict[str, object], dict[str, str]]:
    states = matrices(n)
    successor = {state: update(state, n) for state in states}
    memo: dict[Matrix, tuple[tuple[Matrix, ...], int]] = {}
    first_indegree = Counter(successor.values())
    second_indegree = Counter(successor[successor[state]] for state in states)
    recurrent_states: set[Matrix] = set()
    fixed_count = 0
    depths = Counter()
    witness_f2 = None
    witness_f3 = None
    hole_target = None
    positive_f_zero_f2 = None

    for state in states:
        first = successor[state]
        second = successor[first]
        third = successor[second]
        fourth = successor[third]
        fifth = successor[fourth]
        sums = row_sums(state, n)
        starred = threshold(sums, n)
        decreasing = tuple(sorted(sums, reverse=True))

        transition_digest.update(
            f"{n}:{encode(state, n)}>{encode(first, n)}>{encode(second, n)}>{encode(third, n)}\n".encode("ascii")
        )

        AUDIT.require(first == diagram(sums, n), f"F formula n={n}")
        AUDIT.require(second == diagram(starred, n), f"F^2 formula n={n}")
        AUDIT.require(third == diagram(decreasing, n), f"F^3 formula n={n}")
        AUDIT.require(fourth == second, f"F^4=F^2 n={n}")
        AUDIT.require(fifth == third, f"odd-phase alternation n={n}")
        AUDIT.require(initial_heights(first, n) == sums, f"time-one decoding n={n}")
        AUDIT.require(initial_heights(second, n) == starred, f"time-two decoding n={n}")
        AUDIT.require(initial_heights(third, n) == decreasing, f"time-three decoding n={n}")
        AUDIT.require(threshold(starred, n) == decreasing, f"double threshold sorts n={n}")

        cycle, depth = orbit_profile(state, successor, memo)
        depths[depth] += 1
        if depth == 0:
            recurrent_states.add(state)
            AUDIT.require(second == state, f"recurrent state not fixed by F^2 n={n}")
            if first != state:
                AUDIT.require(successor[first] == state, f"strict recurrent orbit not length two n={n}")

        AUDIT.require((depth == 0) == ferrers(state, n), f"recurrent characterization n={n}")
        AUDIT.require((first == state) == fixed_predicate(state, n), f"fixed characterization n={n}")
        expected_depth = 0 if ferrers(state, n) else 1 if weakly_decreasing(sums) else 2
        AUDIT.require(depth == expected_depth, f"depth classification n={n}")
        AUDIT.require(depth <= (0 if n == 1 else 2), f"height bound n={n}")

        if first == state:
            fixed_count += 1
        if witness_f2 is None and second != first:
            witness_f2 = encode(state, n)
        if witness_f3 is None and third != first:
            witness_f3 = encode(state, n)

        heights = initial_heights(state, n)
        if hole_target is None and heights is None:
            hole_target = encode(state, n)
        if positive_f_zero_f2 is None and heights is not None and not weakly_decreasing(heights):
            positive_f_zero_f2 = encode(state, n)

    for target in states:
        actual_one = first_indegree.get(target, 0)
        actual_two = second_indegree.get(target, 0)
        AUDIT.require(actual_one == first_fibre_formula(target, n), f"time-one fibre n={n}")
        AUDIT.require(actual_two == second_fibre_formula(target, n), f"time-two fibre n={n}")

    recurrent_expected = comb(2 * n, n)
    fixed_expected = 2 ** n
    weak = weighted_coefficient(n)
    AUDIT.require(len(recurrent_states) == recurrent_expected, f"recurrent count n={n}")
    AUDIT.require(fixed_count == fixed_expected, f"fixed count n={n}")
    AUDIT.require(
        (len(recurrent_states) - fixed_count) // 2 == (recurrent_expected - fixed_expected) // 2,
        f"strict two-cycle count n={n}",
    )
    AUDIT.require(len(first_indegree) == (n + 1) ** n, f"time-one image size n={n}")
    AUDIT.require(len(second_indegree) == recurrent_expected, f"time-two image size n={n}")
    AUDIT.require(sum(first_indegree.values()) == len(states), f"time-one mass n={n}")
    AUDIT.require(sum(second_indegree.values()) == len(states), f"time-two mass n={n}")
    AUDIT.require(depths[0] == recurrent_expected, f"L0 count n={n}")
    AUDIT.require(depths[1] == weak - recurrent_expected, f"L1 count n={n}")
    AUDIT.require(depths[2] == len(states) - weak, f"L2 count n={n}")

    if n == 1:
        AUDIT.require(depths[1] == 0 and depths[2] == 0, "n=1 boundary")
    else:
        AUDIT.require(
            orbit_profile(single_one(n, 0, n - 1), successor, memo)[1] == 1,
            f"depth-one witness n={n}",
        )
        AUDIT.require(
            orbit_profile(single_one(n, 1, 0), successor, memo)[1] == 2,
            f"depth-two witness n={n}",
        )

    return (
        {
            "n": n,
            "states": len(states),
            "image1": len(first_indegree),
            "image2": len(second_indegree),
            "recurrent": len(recurrent_states),
            "fixed": fixed_count,
            "cycles2": (len(recurrent_states) - fixed_count) // 2,
            "depths": (depths[0], depths[1], depths[2]),
            "max_fibre1": max(first_indegree.values()),
            "max_fibre2": max(second_indegree.values()),
        },
        {
            "F2_ne_F": witness_f2,
            "F3_ne_F": witness_f3,
            "hole_target": hole_target,
            "F_positive_F2_zero": positive_f_zero_f2,
        },
    )


def partition_controls() -> tuple[list[tuple[int, int, int, int, int]], list[tuple[int, int, int, int]]]:
    transfer_rows = []
    partition_rows = []

    for n in range(1, 13):
        recurrent = comb(2 * n, n)
        fixed = 2 ** n
        weak = weighted_coefficient(n)
        AUDIT.require(recurrent <= weak <= 2 ** (n * n), f"W_n bounds n={n}")
        AUDIT.require(
            sum(comb(n, k) for k in range(n + 1)) ** n == 2 ** (n * n),
            f"time-one mass identity n={n}",
        )

        if n <= 10:
            partitions = tuple(partition_vectors(n))
            AUDIT.require(len(partitions) == recurrent, f"partition census n={n}")
            AUDIT.require(weighted_partition_sum(n) == weak, f"W_n coefficient identity n={n}")

            self_conjugate = 0
            time_two_mass = 0
            for mu in partitions:
                lam = conjugate_partition(mu, n)
                AUDIT.require(weakly_decreasing(lam), f"conjugate partition monotonicity n={n}")
                AUDIT.require(conjugate_partition(lam, n) == mu, f"conjugation involution n={n}")
                if mu == lam:
                    self_conjugate += 1
                multiplicity = Counter(lam)
                time_two_mass += (
                    factorial(n) // prod(factorial(value) for value in multiplicity.values())
                    * prod(comb(n, part) for part in lam)
                )

            AUDIT.require(self_conjugate == fixed, f"self-conjugate count n={n}")
            AUDIT.require(time_two_mass == 2 ** (n * n), f"time-two mass identity n={n}")
            partition_rows.append((n, len(partitions), self_conjugate, time_two_mass))

        transfer_rows.append((n, recurrent, fixed, weak, 2 ** (n * n) - weak))

    return transfer_rows, partition_rows


def main() -> None:
    hashes, pdfinfo_data, font_row_count = artifact_gate()
    transition_digest = sha256()
    boxes = []
    witnesses = {}

    for n in range(1, 5):
        before = AUDIT.count
        summary, local_witnesses = exhaustive_box(n, transition_digest)
        boxes.append((summary, AUDIT.count - before))
        if n == 2:
            witnesses = local_witnesses

    transfer_rows, partition_rows = partition_controls()

    print("P189 process-separated Hostile Review B verifier")
    print(f"review_date_utc={REVIEW_DATE}")
    print(f"tex_sha256={hashes['tex']}")
    print(f"pdf_sha256={hashes['pdf']}")
    print(f"bib_sha256={hashes['bib']}")
    print(f"author_verify_sha256={hashes['author_verify']}")
    print(f"author_canon_sha256={hashes['author_canon']}")
    print(f"review_a_verify_sha256={hashes['review_a_verify']}")
    print(f"review_a_canon_sha256={hashes['review_a_canon']}")
    print("representation=column-bit-tuples;orbits=memoized-repeat-detection")
    print(f"pdf_pages={pdfinfo_data['Pages']}")
    print(f"pdf_page_size={pdfinfo_data['Page size']}")
    print(f"pdf_font_rows={font_row_count}")
    print("pdf_all_fonts_embedded_subset_unicode=yes")
    print(f"witness_F2_ne_F_n2={witnesses['F2_ne_F']}")
    print(f"witness_F3_ne_F_n2={witnesses['F3_ne_F']}")
    print(f"witness_hole_target_n2={witnesses['hole_target']}")
    print(f"witness_F_positive_F2_zero_n2={witnesses['F_positive_F2_zero']}")
    for summary, assertion_delta in boxes:
        print(f"box={summary};assertions={assertion_delta}")
    print("transfer=n,recurrent,fixed,depth_le_1,depth_2")
    for row in transfer_rows:
        print("transfer=" + ",".join(map(str, row)))
    print("partition_controls=n,partitions,self_conjugate,time2_mass")
    for row in partition_rows:
        print("partition=" + ",".join(map(str, row)))
    print(f"transition_digest={transition_digest.hexdigest()}")
    print(f"exact_assertions={AUDIT.count}")
    print("critical_findings=0")
    print("major_findings=0")
    print("minor_findings=0")
    print("verdict=PASS")
    print("external_status=OWNER_AMBER/HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
