#!/usr/bin/env python3
"""Deterministic exact controls for P156.

Literal enumeration checks the finite functional graph, target images, and
fibres.  A separate exact audit checks the canonical right-inverse tower.
Finite computation supplies counterexample pressure only: it is neither an
all-parameter proof nor an ownership or novelty certificate.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial


class Audit:
    def __init__(self) -> None:
        self.assertions = 0
        self.boxes = 0

    def check(self, condition: bool, message: object = "") -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(message or f"assertion {self.assertions} failed")

    def box(self) -> None:
        self.boxes += 1


A = Audit()


def identity(n: int) -> tuple[int, ...]:
    return tuple(range(1, n + 1))


def standardize(values) -> tuple[int, ...]:
    values = tuple(values)
    rank = {value: i + 1 for i, value in enumerate(sorted(values))}
    return tuple(rank[value] for value in values)


def wex(p: tuple[int, ...]) -> tuple[int, ...]:
    return standardize(value for i, value in enumerate(p, 1) if value >= i)


def maxdrop(p: tuple[int, ...]) -> int:
    return max((i - value for i, value in enumerate(p, 1)), default=0)


@lru_cache(None)
def tail(p: tuple[int, ...]) -> int:
    q = wex(p)
    if q == p:
        A.check(p == identity(len(p)), ("nonidentity fixed point", p))
        return 0
    return 1 + tail(q)


def section(sigma: tuple[int, ...], n: int) -> tuple[int, ...]:
    h = n - len(sigma)
    A.check(h >= 0)
    return tuple(value + h for value in sigma) + tuple(range(1, h + 1))


def deficient_completion_count(B: tuple[int, ...], Q: tuple[int, ...]) -> int:
    answer = 1
    for j, q in enumerate(Q, 1):
        answer *= sum(value < q for value in B) - (j - 1)
        if answer <= 0:
            return 0
    return answer


def fibre_formula(sigma: tuple[int, ...], n: int) -> int:
    m = len(sigma)
    if m > n:
        return 0
    universe = tuple(range(1, n + 1))
    answer = 0
    for selected_values in combinations(universe, m):
        selected_value_set = set(selected_values)
        B = tuple(value for value in universe if value not in selected_value_set)
        for selected_positions in combinations(universe, m):
            if any(selected_positions[i] > selected_values[sigma[i] - 1]
                   for i in range(m)):
                continue
            selected_position_set = set(selected_positions)
            Q = tuple(position for position in universe
                      if position not in selected_position_set)
            answer += deficient_completion_count(B, Q)
    return answer


def fib(k: int) -> int:
    a, b = 0, 1
    for _ in range(k):
        a, b = b, a + b
    return a


def bell(n: int) -> int:
    # Standard Bell triangle; kept separate from the permutation audit.
    triangle = [[1]]
    for r in range(1, n + 1):
        new = [triangle[-1][-1]]
        for j in range(1, r + 1):
            new.append(new[-1] + triangle[-1][j - 1])
        triangle.append(new)
    return triangle[n][0]


def main() -> None:
    literal_images: dict[int, set[tuple[int, ...]]] = {}
    literal_fibres: dict[int, Counter[tuple[int, ...]]] = {}
    maxima: list[int] = []
    censuses: list[dict[int, int]] = []
    image_counts: list[int] = []
    states = 0

    for n in range(1, 10):
        A.box()
        fibres: Counter[tuple[int, ...]] = Counter()
        census: Counter[int] = Counter()
        fixed = 0
        for p in permutations(range(1, n + 1)):
            states += 1
            q = wex(p)
            A.check(sorted(q) == list(range(1, len(q) + 1)))
            A.check(1 <= len(q) <= n)
            if q == p:
                fixed += 1
                A.check(p == identity(n))
            else:
                A.check(len(q) < n, ("rank failed to drop", p, q))
            fibres[q] += 1
            census[tail(p)] += 1
        A.check(fixed == 1, ("fixed count", n, fixed))
        A.check(sum(fibres.values()) == factorial(n))
        literal_images[n] = set(fibres)
        if n <= 7:
            literal_fibres[n] = fibres
        maxima.append(max(census))
        censuses.append(dict(sorted(census.items())))
        image_counts.append(len(fibres))

    A.check(maxima == [0, 1, 2, 2, 3, 3, 3, 4, 4], maxima)

    image_cells = 0
    section_cells = 0
    for m in range(1, 9):
        A.box()
        for sigma in permutations(range(1, m + 1)):
            d = maxdrop(sigma)
            A.check((d == 0) == (sigma == identity(m)))
            threshold = m + d
            for n in range(m, 10):
                expected = n >= threshold
                A.check((sigma in literal_images[n]) == expected,
                        ("image", sigma, n, threshold))
                image_cells += 1
                if expected:
                    source = section(sigma, n)
                    A.check(sorted(source) == list(range(1, n + 1)))
                    A.check(wex(source) == sigma, ("section", sigma, n, source))
                    section_cells += 1

    fibre_cells = 0
    bell_checks = 0
    for n in range(1, 8):
        A.box()
        identity_basin = 0
        for m in range(1, n + 1):
            for sigma in permutations(range(1, m + 1)):
                formula = fibre_formula(sigma, n)
                literal = literal_fibres[n].get(sigma, 0)
                A.check(formula == literal, ("fibre", n, sigma, formula, literal))
                fibre_cells += 1
                if sigma == identity(m):
                    identity_basin += formula
        A.check(identity_basin == bell(n), ("Bell owner control", n, identity_basin))
        bell_checks += 1

    # Quantified fibre boundaries kept separate from the n>=m board lane.
    # For n<m the formula is literally zero and no rank-n image can contain a
    # rank-m word.  At n=m only the identity has a same-rank predecessor.
    fibre_n_lt_m_boundary_cells = 0
    fibre_n_eq_m_boundary_cells = 0
    for m in range(1, 9):
        A.box()
        for sigma in permutations(range(1, m + 1)):
            for n in range(1, m):
                A.check(fibre_formula(sigma, n) == 0 and
                        sigma not in literal_images[n],
                        ("n<m fibre boundary", n, sigma))
                fibre_n_lt_m_boundary_cells += 1
            expected = int(sigma == identity(m))
            A.check(fibre_formula(sigma, m) == expected and
                    ((sigma in literal_images[m]) == bool(expected)),
                    ("n=m fibre boundary", m, sigma, expected))
            fibre_n_eq_m_boundary_cells += 1

    # Exact canonical inverse towers.  Every edge uses the one-step minimum
    # source rank supplied by the image theorem; no global t-step optimum is
    # asserted or tested.
    tower_targets = 0
    tower_levels = 6
    for m in range(1, 9):
        A.box()
        for sigma in permutations(range(1, m + 1)):
            if sigma == identity(m):
                continue
            tower_targets += 1
            initial_m = m
            initial_d = maxdrop(sigma)
            initial_tail = tail(sigma)
            current = sigma
            for t in range(1, tower_levels + 1):
                old_m = len(current)
                old_d = maxdrop(current)
                source = section(current, old_m + old_d)
                A.check(wex(source) == current)
                A.check(len(source) == old_m + old_d)
                A.check(maxdrop(source) == old_m)
                A.check(len(source) == fib(t + 1) * initial_m +
                        fib(t) * initial_d)
                A.check(maxdrop(source) == fib(t) * initial_m +
                        fib(t - 1) * initial_d)
                A.check(tail(source) == initial_tail + t)
                current = source

    # Reproduce, rather than conceal, the counterexample that delimits the
    # withdrawn pointwise drop-clock claim.
    counterexample = (11, 10, 9, 4, 1, 2, 3, 8, 5, 6, 7)
    target = wex(counterexample)
    rank_four_max = max(tail(p) for p in permutations(range(1, 5)))
    A.check(target == (5, 4, 3, 1, 2))
    A.check(maxdrop(counterexample) == 4)
    A.check(tail(target) == 3)
    A.check(rank_four_max == 2)
    A.check(tail(target) > rank_four_max)

    print("P156_WEAK_EXCEDANCE_EXTRACTION_EXACT_CONTROL")
    print("external_status=HOLD_EXTERNAL")
    print(f"literal_states_through_rank_9={states}")
    print(f"max_tail_ranks_1_to_9={maxima}")
    print(f"tail_censuses={censuses}")
    print(f"image_counts_ranks_1_to_9={image_counts}")
    print(f"image_target_rank_cells={image_cells}")
    print(f"constructive_section_cells={section_cells}")
    print(f"every_target_fibre_cells={fibre_cells}")
    print(f"fibre_n_lt_m_boundary_cells={fibre_n_lt_m_boundary_cells}")
    print(f"fibre_n_eq_m_boundary_cells={fibre_n_eq_m_boundary_cells}")
    print(f"bell_identity_basin_checks_zero_credit={bell_checks}")
    print(f"tower_targets_through_rank_8={tower_targets}")
    print(f"tower_levels_per_target={tower_levels}")
    print("pointwise_drop_clock=FALSE_COUNTEREXAMPLE_REPRODUCED")
    print("global_maximum_clock=NOT_CLAIMED")
    print("global_iterated_preimage_minimality=NOT_CLAIMED")
    print("enumeration_role=COUNTEREXAMPLE_PRESSURE_ONLY")
    print(f"boxes={A.boxes}")
    print(f"assertions={A.assertions}")
    print("status=PASS")


if __name__ == "__main__":
    main()
