#!/usr/bin/env python3
"""Process-separated hostile verifier for P189 Round 0.

Representation firewall: matrices are tuples of row-support frozensets.  The
carrier is generated as a Cartesian product of subsets, the literal update is
performed by explicit row left-compression followed by set-theoretic
transposition, and recurrence/depth are recovered by indegree peeling and
reverse breadth-first search.  No author or scouting module is imported.
"""

from __future__ import annotations

from collections import Counter, deque
from hashlib import sha256
from itertools import combinations, product
from math import comb, factorial, prod
from pathlib import Path
import re
from typing import Dict, FrozenSet, Iterable, Iterator, List, Optional, Tuple


Row = FrozenSet[int]
Matrix = Tuple[Row, ...]

EXPECTED_TEX_SHA = "c9c4417012fcc9663ac3c3ac3fe9f5113fdf4fe4213846d2a6815b7657724457"
EXPECTED_PDF_SHA = "6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81"
EXPECTED_BIB_KEYS = {
    "Andrews1998",
    "DasDasSen2016",
    "KouteckyOnn2020",
    "Miller2013",
}


class Checks:
    def __init__(self) -> None:
        self.count = 0

    def require(self, condition: bool, label: str) -> None:
        self.count += 1
        if not condition:
            raise AssertionError(label)


CHECKS = Checks()


def file_sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def artifact_gate() -> Tuple[str, str, str, str]:
    review_dir = Path(__file__).resolve().parent
    paper_dir = review_dir.parents[2]
    tex = paper_dir / "main.tex"
    frozen = paper_dir / "main_round0_original.pdf"
    live = paper_dir / "main.pdf"
    bib = paper_dir / "references.bib"

    tex_sha = file_sha(tex)
    frozen_sha = file_sha(frozen)
    live_sha = file_sha(live)
    bib_sha = file_sha(bib)
    CHECKS.require(tex_sha == EXPECTED_TEX_SHA, "Round0 main.tex drift")
    CHECKS.require(frozen_sha == EXPECTED_PDF_SHA, "Round0 PDF drift")
    CHECKS.require(live_sha == EXPECTED_PDF_SHA, "live PDF differs from Round0")
    CHECKS.require(frozen.read_bytes() == live.read_bytes(), "live/frozen bytes differ")

    source = tex.read_text(encoding="utf-8")
    bibliography = bib.read_text(encoding="utf-8")
    cite_keys = set()
    for group in re.findall(r"\\cite\{([^}]*)\}", source):
        cite_keys.update(key.strip() for key in group.split(","))
    bib_keys = set(re.findall(r"^@\w+\{([^,]+),", bibliography, flags=re.MULTILINE))
    CHECKS.require(cite_keys == EXPECTED_BIB_KEYS, "unexpected manuscript cite-key set")
    CHECKS.require(bib_keys == EXPECTED_BIB_KEYS, "unexpected bibliography key set")
    CHECKS.require("F^4=F^2" in source, "collapse claim missing from bound source")
    CHECKS.require("hold\\_external" in source.lower(), "HOLD_EXTERNAL missing")
    return tex_sha, frozen_sha, live_sha, bib_sha


def row_types(n: int) -> Tuple[Row, ...]:
    """Subsets ordered by cardinality and then lexicographically."""

    return tuple(
        frozenset(choice)
        for size in range(n + 1)
        for choice in combinations(range(n), size)
    )


def matrices(n: int) -> Tuple[Matrix, ...]:
    return tuple(product(row_types(n), repeat=n))


def left_compress_then_transpose(source: Matrix, n: int) -> Matrix:
    """Literal update using explicit support sets, not an integer encoding."""

    compressed = tuple(frozenset(range(len(row))) for row in source)
    return tuple(
        frozenset(row_index for row_index, row in enumerate(compressed) if i in row)
        for i in range(n)
    )


def row_sizes(matrix: Matrix) -> Tuple[int, ...]:
    return tuple(len(row) for row in matrix)


def columns(matrix: Matrix, n: int) -> Tuple[Row, ...]:
    return tuple(
        frozenset(i for i, row in enumerate(matrix) if j in row)
        for j in range(n)
    )


def stack_from_heights(heights: Tuple[int, ...], n: int) -> Matrix:
    return tuple(
        frozenset(j for j, height in enumerate(heights) if i < height)
        for i in range(n)
    )


def threshold(heights: Tuple[int, ...], n: int) -> Tuple[int, ...]:
    """Transpose a cell set and read its row lengths."""

    cells = frozenset(
        (i, j)
        for j, height in enumerate(heights)
        for i in range(height)
    )
    return tuple(sum((i, j) in cells for j in range(n)) for i in range(n))


def initial_column_heights(matrix: Matrix, n: int) -> Optional[Tuple[int, ...]]:
    answer: List[int] = []
    for column in columns(matrix, n):
        height = len(column)
        if column != frozenset(range(height)):
            return None
        answer.append(height)
    return tuple(answer)


def weakly_decreasing(values: Tuple[int, ...]) -> bool:
    return all(left >= right for left, right in zip(values, values[1:]))


def ferrers(matrix: Matrix, n: int) -> bool:
    heights = initial_column_heights(matrix, n)
    return heights is not None and weakly_decreasing(heights)


def predicted_fixed(matrix: Matrix, n: int) -> bool:
    heights = initial_column_heights(matrix, n)
    return (
        heights is not None
        and weakly_decreasing(heights)
        and threshold(heights, n) == heights
    )


def predicted_depth(matrix: Matrix, n: int) -> int:
    if ferrers(matrix, n):
        return 0
    if weakly_decreasing(row_sizes(matrix)):
        return 1
    return 2


def first_fibre_formula(target: Matrix, n: int) -> int:
    heights = initial_column_heights(target, n)
    if heights is None:
        return 0
    return prod(comb(n, height) for height in heights)


def second_fibre_formula(target: Matrix, n: int) -> int:
    heights = initial_column_heights(target, n)
    if heights is None or not weakly_decreasing(heights):
        return 0
    row_sum_partition = threshold(heights, n)
    multiplicity = Counter(row_sum_partition)
    assignments = factorial(n) // prod(factorial(value) for value in multiplicity.values())
    supports = prod(comb(n, size) for size in row_sum_partition)
    return assignments * supports


def partition_vectors(n: int) -> Iterator[Tuple[int, ...]]:
    """Partitions in an n-square, built by a descending recursive walk."""

    def visit(prefix: Tuple[int, ...], ceiling: int) -> Iterator[Tuple[int, ...]]:
        if len(prefix) == n:
            yield prefix
            return
        for value in range(ceiling, -1, -1):
            yield from visit(prefix + (value,), value)

    yield from visit((), n)


def weighted_partition_sum(n: int) -> int:
    return sum(prod(comb(n, part) for part in shape) for shape in partition_vectors(n))


def weighted_coefficient(n: int) -> int:
    """Coefficient of z^n in product_k (1-C(n,k)z)^(-1)."""

    coefficients = [1] + [0] * n
    for k in range(n + 1):
        weight = comb(n, k)
        replacement = [0] * (n + 1)
        for old_degree, old_value in enumerate(coefficients):
            for multiplicity in range(n - old_degree + 1):
                replacement[old_degree + multiplicity] += old_value * weight ** multiplicity
        coefficients = replacement
    return coefficients[n]


def encode(matrix: Matrix, n: int) -> str:
    return "/".join(
        "".join("1" if j in row else "0" for j in range(n))
        for row in matrix
    )


def functional_graph(
    states: Tuple[Matrix, ...], successor: Dict[Matrix, Matrix]
) -> Tuple[set[Matrix], Dict[Matrix, int]]:
    """Recover cycles by indegree peeling and tails by reverse BFS."""

    indegree = {state: 0 for state in states}
    predecessors: Dict[Matrix, List[Matrix]] = {state: [] for state in states}
    for state, target in successor.items():
        indegree[target] += 1
        predecessors[target].append(state)

    queue = deque(state for state in states if indegree[state] == 0)
    peeled = set()
    while queue:
        state = queue.popleft()
        peeled.add(state)
        target = successor[state]
        indegree[target] -= 1
        if indegree[target] == 0:
            queue.append(target)
    cyclic = set(states).difference(peeled)

    distance = {state: 0 for state in cyclic}
    queue = deque(cyclic)
    while queue:
        state = queue.popleft()
        for predecessor in predecessors[state]:
            if predecessor not in distance:
                distance[predecessor] = distance[state] + 1
                queue.append(predecessor)
    CHECKS.require(len(distance) == len(states), "reverse BFS missed a state")
    return cyclic, distance


def exhaustive_box(n: int, transition_digest) -> Tuple[dict, dict]:
    states = matrices(n)
    state_set = set(states)
    successor = {state: left_compress_then_transpose(state, n) for state in states}
    CHECKS.require(len(states) == 2 ** (n * n), f"carrier size n={n}")
    CHECKS.require(len(state_set) == len(states), f"carrier duplicates n={n}")
    CHECKS.require(set(successor.values()).issubset(state_set), f"closure n={n}")

    cyclic, distance = functional_graph(states, successor)
    first_indegree = Counter(successor.values())
    second_indegree = Counter(successor[successor[state]] for state in states)
    fixed = {state for state in states if successor[state] == state}
    strict_cycle_states = cyclic.difference(fixed)
    CHECKS.require(len(strict_cycle_states) % 2 == 0, f"cycle parity n={n}")

    witness_f2 = None
    witness_f3 = None
    for state in states:
        first = successor[state]
        second = successor[first]
        third = successor[second]
        fourth = successor[third]
        fifth = successor[fourth]
        sixth = successor[fifth]
        sizes = row_sizes(state)
        starred = threshold(sizes, n)
        decreasing = tuple(sorted(sizes, reverse=True))

        transition_digest.update(f"{n}:{encode(state,n)}>{encode(first,n)}\n".encode("ascii"))
        CHECKS.require(first == stack_from_heights(sizes, n), f"F formula n={n}")
        CHECKS.require(second == stack_from_heights(starred, n), f"F2 formula n={n}")
        CHECKS.require(third == stack_from_heights(decreasing, n), f"F3 formula n={n}")
        CHECKS.require(fourth == second, f"F4=F2 n={n}")
        CHECKS.require(fifth == third, f"odd recurrent phase n={n}")
        CHECKS.require(sixth == second, f"even recurrent phase n={n}")
        CHECKS.require(
            threshold(threshold(sizes, n), n) == decreasing,
            f"double threshold sorting n={n}",
        )
        CHECKS.require((state in cyclic) == ferrers(state, n), f"recurrent set n={n}")
        CHECKS.require((state in fixed) == predicted_fixed(state, n), f"fixed set n={n}")
        CHECKS.require(distance[state] == predicted_depth(state, n), f"depth set n={n}")
        CHECKS.require(distance[state] <= 2, f"height bound n={n}")
        if state in strict_cycle_states:
            CHECKS.require(successor[successor[state]] == state, f"strict period two n={n}")

        if witness_f2 is None and second != first:
            witness_f2 = encode(state, n)
        if witness_f3 is None and third != first:
            witness_f3 = encode(state, n)

    for target in states:
        actual_one = first_indegree.get(target, 0)
        actual_two = second_indegree.get(target, 0)
        formula_one = first_fibre_formula(target, n)
        formula_two = second_fibre_formula(target, n)
        CHECKS.require(actual_one == formula_one, f"every-target F fibre n={n}")
        CHECKS.require(actual_two == formula_two, f"every-target F2 fibre n={n}")
        CHECKS.require((actual_one > 0) == (target in first_indegree), f"F image n={n}")
        CHECKS.require((actual_two > 0) == (target in second_indegree), f"F2 image n={n}")

    recurrent_expected = comb(2 * n, n)
    fixed_expected = 2**n
    weak = weighted_coefficient(n)
    depths = Counter(distance.values())
    CHECKS.require(len(cyclic) == recurrent_expected, f"recurrent count n={n}")
    CHECKS.require(len(fixed) == fixed_expected, f"fixed count n={n}")
    CHECKS.require(len(strict_cycle_states) // 2 == (recurrent_expected - fixed_expected) // 2,
                   f"strict cycle count n={n}")
    CHECKS.require(len(first_indegree) == (n + 1) ** n, f"F image count n={n}")
    CHECKS.require(len(second_indegree) == recurrent_expected, f"F2 image count n={n}")
    CHECKS.require(sum(first_indegree.values()) == len(states), f"F mass n={n}")
    CHECKS.require(sum(second_indegree.values()) == len(states), f"F2 mass n={n}")
    CHECKS.require(depths[0] == recurrent_expected, f"L0 count n={n}")
    CHECKS.require(depths[1] == weak - recurrent_expected, f"L1 count n={n}")
    CHECKS.require(depths[2] == len(states) - weak, f"L2 count n={n}")
    CHECKS.require(max(distance.values()) == (0 if n == 1 else 2), f"sharp height n={n}")

    summary = {
        "n": n,
        "states": len(states),
        "image1": len(first_indegree),
        "image2": len(second_indegree),
        "recurrent": len(cyclic),
        "fixed": len(fixed),
        "cycles2": len(strict_cycle_states) // 2,
        "depths": (depths[0], depths[1], depths[2]),
        "max_fibre1": max(first_indegree.values()),
        "max_fibre2": max(second_indegree.values()),
    }
    witnesses = {"F2_ne_F": witness_f2, "F3_ne_F": witness_f3}
    return summary, witnesses


def transfer_checks() -> List[Tuple[int, int, int, int, int]]:
    rows = []
    for n in range(1, 13):
        recurrent = comb(2 * n, n)
        fixed = 2**n
        weak = weighted_coefficient(n)
        CHECKS.require(recurrent <= weak <= 2 ** (n * n), f"weighted bounds n={n}")
        CHECKS.require((recurrent - fixed) % 2 == 0, f"cycle integrality n={n}")
        if n <= 10:
            partitions = tuple(partition_vectors(n))
            CHECKS.require(len(partitions) == recurrent, f"partition census n={n}")
            CHECKS.require(weighted_partition_sum(n) == weak, f"two W formulas n={n}")
            self_conjugate = 0
            inverse_mass = 0
            for shape in partitions:
                conjugate = threshold(shape, n)
                CHECKS.require(weakly_decreasing(conjugate), f"conjugate partition n={n}")
                CHECKS.require(threshold(conjugate, n) == shape, f"conjugation involution n={n}")
                self_conjugate += conjugate == shape
                multiplicity = Counter(conjugate)
                inverse_mass += (
                    factorial(n) // prod(factorial(v) for v in multiplicity.values())
                    * prod(comb(n, part) for part in conjugate)
                )
            CHECKS.require(self_conjugate == fixed, f"self-conjugate count n={n}")
            CHECKS.require(inverse_mass == 2 ** (n * n), f"F2 formula mass n={n}")
        CHECKS.require(sum(comb(n, k) for k in range(n + 1)) ** n == 2 ** (n * n),
                       f"F formula mass n={n}")
        rows.append((n, recurrent, fixed, weak, 2 ** (n * n) - weak))
    return rows


def main() -> None:
    tex_sha, frozen_sha, live_sha, bib_sha = artifact_gate()
    transition_digest = sha256()
    summaries = []
    witnesses = None
    for n in range(1, 5):
        before = CHECKS.count
        summary, local_witnesses = exhaustive_box(n, transition_digest)
        summaries.append((summary, CHECKS.count - before))
        if n == 2:
            witnesses = local_witnesses

    CHECKS.require(witnesses is not None, "n=2 witness box absent")
    CHECKS.require(witnesses["F2_ne_F"] is not None, "F2 != F witness absent")
    CHECKS.require(witnesses["F3_ne_F"] is not None, "F3 != F witness absent")
    transfer = transfer_checks()

    print("P189 process-separated Hostile Review A verifier")
    print(f"round0_main_tex_sha256={tex_sha}")
    print(f"round0_pdf_sha256={frozen_sha}")
    print(f"live_pdf_sha256={live_sha}")
    print(f"references_bib_sha256={bib_sha}")
    print("representation=row-support-frozensets;recurrence=indegree-peeling+reverse-BFS")
    print(f"witness_F2_ne_F_n2={witnesses['F2_ne_F']}")
    print(f"witness_F3_ne_F_n2={witnesses['F3_ne_F']}")
    for summary, assertion_delta in summaries:
        print(f"box={summary};assertions={assertion_delta}")
    print("transfer=n,recurrent,fixed,depth_le_1,depth_2")
    for row in transfer:
        print("transfer=" + ",".join(map(str, row)))
    print(f"transition_digest={transition_digest.hexdigest()}")
    print(f"exact_assertions={CHECKS.count}")
    print("critical_findings=0")
    print("major_findings=0")
    print("minor_findings=0")
    print("verdict=PASS")
    print("external_status=OWNER_AMBER/HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
