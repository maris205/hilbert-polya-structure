#!/usr/bin/env python3
"""Independent hostile exact audit for P158.

This reviewer-owned program does not import or call the paper-local verifier.
It evaluates the literal successive cut intersections before comparing them
with the complementary-word description.  Separate lanes attack every
labelled target fibre, the n=5,t=2 resource boundary, the A_R finite sum and
EGF, the labelled image EGF, the first-hit/CDF normalization, and the mean
tail-sum offset.  These finite checks are counterexample pressure, not proof
or source clearance.
"""

from __future__ import annotations

from collections import Counter, deque
from fractions import Fraction
from itertools import product
from math import comb, factorial


ASSERTIONS = 0


def require(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def edges(n: int) -> list[tuple[int, int]]:
    return [(u, v) for u in range(n) for v in range(u + 1, n)]


def literal_intersection(words: tuple[int, ...], t: int) -> int:
    """Run the t cuts successively, without using word complementation."""
    edge_list = edges(len(words))
    current = (1 << len(edge_list)) - 1
    for epoch in range(t):
        cut = 0
        for index, (u, v) in enumerate(edge_list):
            if ((words[u] >> epoch) & 1) != ((words[v] >> epoch) & 1):
                cut |= 1 << index
        current &= cut
    return current


def complement_graph(words: tuple[int, ...], t: int) -> int:
    target = (1 << t) - 1
    mask = 0
    for index, (u, v) in enumerate(edges(len(words))):
        if words[u] ^ words[v] == target:
            mask |= 1 << index
    return mask


def first_empty_epoch(words: tuple[int, ...], t: int) -> int | None:
    edge_list = edges(len(words))
    current = (1 << len(edge_list)) - 1
    for epoch in range(t):
        cut = 0
        for index, (u, v) in enumerate(edge_list):
            if ((words[u] >> epoch) & 1) != ((words[v] >> epoch) & 1):
                cut |= 1 << index
        current &= cut
        if current == 0:
            return epoch + 1
    return None


def a_inclusion_exclusion(r: int, m: int) -> int:
    return sum(
        (-1) ** (r - j) * comb(r, j) * (2**j) * (j**m)
        for j in range(r + 1)
    )


def falling(r: int, k: int) -> int:
    value = 1
    for j in range(k):
        value *= r - j
    return value


def target_profile(n: int, mask: int) -> tuple[bool, int, int]:
    """Return (bicluster-plus-isolates, nontrivial components, isolates)."""
    neighbours = [set() for _ in range(n)]
    for index, (u, v) in enumerate(edges(n)):
        if mask & (1 << index):
            neighbours[u].add(v)
            neighbours[v].add(u)

    isolates = sum(len(row) == 0 for row in neighbours)
    visited: set[int] = set()
    components = 0
    for root in range(n):
        if root in visited or not neighbours[root]:
            continue
        colour = {root: 0}
        queue = deque([root])
        visited.add(root)
        vertices: list[int] = []
        while queue:
            u = queue.popleft()
            vertices.append(u)
            for v in neighbours[u]:
                if v not in colour:
                    colour[v] = 1 - colour[u]
                    visited.add(v)
                    queue.append(v)
                elif colour[v] == colour[u]:
                    return False, 0, isolates
        for i, u in enumerate(vertices):
            for v in vertices[i + 1 :]:
                expected = colour[u] != colour[v]
                if (v in neighbours[u]) != expected:
                    return False, 0, isolates
        components += 1
    return True, components, isolates


def fibre_formula(n: int, t: int, mask: int) -> int:
    valid, component_count, isolate_count = target_profile(n, mask)
    pair_count = 1 << (t - 1)
    if not valid or component_count > pair_count:
        return 0
    return (
        falling(pair_count, component_count)
        * (2**component_count)
        * a_inclusion_exclusion(pair_count - component_count, isolate_count)
    )


def polynomial_product(
    left: list[Fraction], right: list[Fraction], degree: int
) -> list[Fraction]:
    answer = [Fraction(0) for _ in range(degree + 1)]
    for i, a in enumerate(left):
        for j, b in enumerate(right[: degree - i + 1]):
            answer[i + j] += a * b
    return answer


def polynomial_power(base: list[Fraction], exponent: int, degree: int) -> list[Fraction]:
    answer = [Fraction(1)] + [Fraction(0) for _ in range(degree)]
    for _ in range(exponent):
        answer = polynomial_product(answer, base, degree)
    return answer


def a_from_egf(r: int, m: int) -> int:
    base = [Fraction(1)] + [Fraction(2, factorial(k)) for k in range(1, m + 1)]
    coefficient = polynomial_power(base, r, m)[m] * factorial(m)
    require(coefficient.denominator == 1, "A_R EGF coefficient not integral")
    return coefficient.numerator


def image_from_egf(n: int, r: int) -> int:
    exp_series = [Fraction(1, factorial(k)) for k in range(n + 1)]
    biclique = [Fraction(0), Fraction(0)] + [
        Fraction((1 << (k - 1)) - 1, factorial(k)) for k in range(2, n + 1)
    ]
    biclique = biclique[: n + 1]
    powers = [polynomial_power(biclique, j, n) for j in range(r + 1)]
    below_cap = [Fraction(0) for _ in range(n + 1)]
    for j in range(r):
        for k in range(n + 1):
            below_cap[k] += powers[j][k] / factorial(j)
    series = polynomial_product(exp_series, below_cap, n)
    for k in range(n + 1):
        series[k] += powers[r][k] / factorial(r)
    coefficient = series[n] * factorial(n)
    require(coefficient.denominator == 1, "image EGF coefficient not integral")
    return coefficient.numerator


def every_target_lane() -> list[str]:
    rows: list[str] = []
    cases = [(2, 1), (3, 2), (4, 3), (5, 2), (5, 4), (6, 3)]
    for n, t in cases:
        observed: Counter[int] = Counter()
        alphabet = 1 << t
        for words in product(range(alphabet), repeat=n):
            literal = literal_intersection(words, t)
            require(literal == complement_graph(words, t), f"pathwise n={n} t={t}")
            observed[literal] += 1

        predicted_mass = 0
        predicted_image = 0
        for mask in range(1 << comb(n, 2)):
            predicted = fibre_formula(n, t, mask)
            require(
                observed.get(mask, 0) == predicted,
                f"fibre n={n} t={t} mask={mask}",
            )
            predicted_mass += predicted
            predicted_image += predicted > 0

        histories = alphabet**n
        pair_count = 1 << (t - 1)
        require(predicted_mass == histories, f"mass n={n} t={t}")
        require(len(observed) == predicted_image, f"image condition n={n} t={t}")
        require(len(observed) == image_from_egf(n, pair_count), f"image EGF n={n} t={t}")
        require(observed[0] == a_inclusion_exclusion(pair_count, n), f"CDF n={n} t={t}")
        require(observed[0] == a_from_egf(pair_count, n), f"A EGF n={n} t={t}")
        require(sum(observed.values()) == histories, f"history count n={n} t={t}")
        rows.append(
            f"n={n},t={t},histories={histories},image={len(observed)},empty={observed[0]}"
        )
    return rows


def perfect_matchings(vertices: tuple[int, ...]) -> list[tuple[tuple[int, int], ...]]:
    if not vertices:
        return [tuple()]
    first = vertices[0]
    answer: list[tuple[tuple[int, int], ...]] = []
    for index in range(1, len(vertices)):
        partner = vertices[index]
        rest = vertices[1:index] + vertices[index + 1 :]
        for suffix in perfect_matchings(rest):
            answer.append(((first, partner),) + suffix)
    return answer


def mask_from_pairs(n: int, selected: tuple[tuple[int, int], ...]) -> int:
    wanted = {tuple(sorted(pair)) for pair in selected}
    return sum(1 << index for index, pair in enumerate(edges(n)) if pair in wanted)


def resource_boundary_lane() -> None:
    n, t = 5, 2
    observed: Counter[int] = Counter(
        literal_intersection(words, t)
        for words in product(range(1 << t), repeat=n)
    )
    targets: set[int] = set()
    for isolate in range(n):
        remaining = tuple(v for v in range(n) if v != isolate)
        for matching in perfect_matchings(remaining):
            mask = mask_from_pairs(n, matching)
            targets.add(mask)
            valid, component_count, isolate_count = target_profile(n, mask)
            require(valid, "boundary target left bicluster class")
            require(component_count == 2 and isolate_count == 1, "boundary profile")
            require(fibre_formula(n, t, mask) == 0, "boundary formula nonzero")
            require(observed.get(mask, 0) == 0, "boundary target attained")
    require(len(targets) == 15, "two-edge-plus-isolate target census")


def temporal_lane() -> None:
    require(a_inclusion_exclusion(0, 0) == 1, "A_0(0)")
    for m in range(1, 13):
        require(a_inclusion_exclusion(0, m) == 0, "A_0(m>0)")
    for r in range(1, 17):
        require(a_inclusion_exclusion(r, 0) == 1, "A_R(0)")
    for r in range(0, 17):
        for m in range(0, 13):
            require(a_inclusion_exclusion(r, m) == a_from_egf(r, m), "A formula/EGF")

    n, horizon = 4, 4
    counts: Counter[int | None] = Counter()
    alphabet = 1 << horizon
    for words in product(range(alphabet), repeat=n):
        counts[first_empty_epoch(words, horizon)] += 1
    total = alphabet**n
    previous_cumulative = 0
    for time in range(1, horizon + 1):
        pair_count = 1 << (time - 1)
        cumulative = a_inclusion_exclusion(pair_count, n) * (
            1 << ((horizon - time) * n)
        )
        observed_cumulative = sum(counts[s] for s in range(1, time + 1))
        require(observed_cumulative == cumulative, f"CDF coupling t={time}")
        require(counts[time] == cumulative - previous_cumulative, f"first hit t={time}")
        previous_cumulative = cumulative
    require(sum(counts.values()) == total, "temporal histories lost")

    capped_time_sum = sum(
        (epoch if epoch is not None else horizon + 1) * count
        for epoch, count in counts.items()
    )
    tail_sum_numerator = total + sum(
        total - sum(counts[s] for s in range(1, time + 1))
        for time in range(1, horizon + 1)
    )
    require(capped_time_sum == tail_sum_numerator, "positive-time mean offset")

    for vertex_count in range(2, 21):
        for time in range(1, 13):
            pair_count = 1 << (time - 1)
            denominator = 1 << (time * vertex_count)
            empty = a_inclusion_exclusion(pair_count, vertex_count)
            require(0 <= empty <= denominator, "CDF range")
            require(
                (denominator - empty) * (1 << time)
                <= comb(vertex_count, 2) * denominator,
                "geometric union bound",
            )


def main() -> None:
    rows = every_target_lane()
    resource_boundary_lane()
    temporal_lane()
    print("P158_HOSTILE_REVIEW_A_EXACT_V1")
    print("LITERAL successive_cut_intersection_equals_complement_histories")
    for row in rows:
        print("ATLAS", row)
    print("BOUNDARY n=5,t=2,two_disjoint_edges_plus_isolate:15/15_zero_fibres")
    print("FIBRE (R)_r*2^r*A_(R-r)(z):every_target_in_all_boxes")
    print("EGF A_R_and_labelled_image_coefficients_exact")
    print("TEMPORAL CDF_first_hit_tail_and_positive_mean_offset_exact")
    print(f"ASSERTIONS={ASSERTIONS}")
    print("STATUS=PASS")


if __name__ == "__main__":
    main()
