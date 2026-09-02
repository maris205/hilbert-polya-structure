#!/usr/bin/env python3
"""Independent hostile/value verifier for complemented-shadow dynamics.

The implementation represents a subset of [n] by its literal bit mask and a
set family by a second bit mask whose positions are those subsets.  It imports
nothing from the reserve scout.  In addition to reconstructing the frozen
contract, it audits the proposed new support-resolved deepest-shell theorem.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from math import comb


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def check(self, condition: bool, witness: object) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(witness)

    def equal(self, left: object, right: object, witness: object) -> None:
        self.check(left == right, (witness, left, right))


A = Audit()


def pc(value: int) -> int:
    return value.bit_count()


@lru_cache(maxsize=None)
def rank_atoms(n: int, k: int) -> tuple[int, ...]:
    return tuple(atom for atom in range(1 << n) if pc(atom) == k)


def members(family: int) -> tuple[int, ...]:
    return tuple(atom for atom in range(family.bit_length()) if family >> atom & 1)


def rank_slice(family: int, n: int, k: int) -> tuple[int, ...]:
    return tuple(atom for atom in rank_atoms(n, k) if family >> atom & 1)


def atomic_step(n: int, atom: int) -> int:
    """Literal complemented lower shadow of one atom."""
    if atom == 0:
        return 0
    full = (1 << n) - 1
    image = 0
    remaining = atom
    while remaining:
        bit = remaining & -remaining
        remaining ^= bit
        target = full ^ (atom ^ bit)
        image |= 1 << target
    return image


@lru_cache(maxsize=None)
def atomic_steps(n: int) -> tuple[int, ...]:
    return tuple(atomic_step(n, atom) for atom in range(1 << n))


def family_step(n: int, family: int) -> int:
    image = 0
    kernels = atomic_steps(n)
    remaining = family
    while remaining:
        atom_bit = remaining & -remaining
        atom = atom_bit.bit_length() - 1
        remaining ^= atom_bit
        image |= kernels[atom]
    return image


def family_iterate(n: int, family: int, t: int) -> int:
    current = family
    for _ in range(t):
        current = family_step(n, current)
    return current


def atomic_closed(n: int, atom: int, t: int) -> int:
    if atom == 0:
        return 1 if t == 0 else 0
    k = pc(atom)
    answer = 0
    if t % 2 == 0:
        radius = t // 2
        for target in rank_atoms(n, k):
            if k - pc(atom & target) <= radius:
                answer |= 1 << target
    else:
        radius = (t - 1) // 2
        for target in rank_atoms(n, n - k + 1):
            if pc(atom & target) <= radius + 1:
                answer |= 1 << target
    return answer


def even_ball_volume(n: int, k: int, radius: int) -> int:
    diameter = min(k, n - k)
    return sum(comb(k, j) * comb(n - k, j) for j in range(min(radius, diameter) + 1))


def odd_kernel_volume(n: int, k: int, radius: int) -> int:
    upper = min(radius + 1, k, n - k + 1)
    return sum(comb(k, j) * comb(n - k, j - 1) for j in range(1, upper + 1))


def actual_tail_period(n: int, family: int) -> tuple[int, int]:
    seen: dict[int, int] = {}
    current = family
    time = 0
    while current not in seen:
        seen[current] = time
        current = family_step(n, current)
        time += 1
    return seen[current], time - seen[current]


def radii_and_support(n: int, family: int) -> tuple[int, int, int]:
    even_radii: list[int] = []
    odd_radii: list[int] = []
    support = 0
    for k in range(1, n + 1):
        source = rank_slice(family, n, k)
        if not source:
            continue
        support |= 1 << (k - 1)
        even_radii.append(
            max(min(k - pc(left & right) for left in source) for right in rank_atoms(n, k))
        )
        dual_rank = n - k + 1
        odd_radii.append(
            max(
                min(pc(left & right) - 1 for left in source)
                for right in rank_atoms(n, dual_rank)
            )
        )
    if not even_radii:
        return -1, -1, support
    return max(even_radii), max(odd_radii), support


def support_dual(n: int, support: int) -> int:
    answer = 0
    for k in range(1, n + 1):
        if support >> (k - 1) & 1:
            answer |= 1 << (n - k)
    return answer


def predicted_tail_period(n: int, family: int) -> tuple[int, int]:
    even_radius, odd_radius, support = radii_and_support(n, family)
    if support == 0:
        return (1, 1) if family & 1 else (0, 1)
    tail = min(2 * even_radius, 2 * odd_radius + 1)
    if family & 1:
        tail = max(1, tail)
    period = 1 if support_dual(n, support) == support else 2
    return tail, period


def rank_union(n: int, support: int) -> int:
    family = 0
    for k in range(1, n + 1):
        if support >> (k - 1) & 1:
            for atom in rank_atoms(n, k):
                family |= 1 << atom
    return family


def middle_rank(n: int) -> int:
    return (n + 1) // 2


def deepest_predicate(n: int, family: int) -> bool:
    return len(rank_slice(family, n, middle_rank(n))) == 1


def deepest_count(n: int) -> int:
    if n == 2:
        return 12
    middle_size = comb(n, middle_rank(n))
    return middle_size * 2 ** ((1 << n) - middle_size)


def support_resolved_deepest_count(n: int, support: int) -> int:
    k_star = middle_rank(n)
    if not (support >> (k_star - 1) & 1):
        return 0
    answer = 2 * comb(n, k_star)  # optional silent atom; singleton middle slice
    for k in range(1, n + 1):
        if k == k_star:
            continue
        if support >> (k - 1) & 1:
            answer *= 2 ** comb(n, k) - 1
    return answer


def deepest_period_one_count(n: int) -> int:
    k_star = middle_rank(n)
    answer = 2 * comb(n, k_star)
    visited: set[int] = set()
    for k in range(1, n + 1):
        if k in visited:
            continue
        mate = n - k + 1
        orbit = {k, mate}
        visited |= orbit
        if k_star in orbit:
            for rank in orbit - {k_star}:
                answer *= 2 ** comb(n, rank) - 1
        else:
            nonempty = 1
            for rank in orbit:
                nonempty *= 2 ** comb(n, rank) - 1
            answer *= 1 + nonempty
    return answer


def predicted_atomic_depth(n: int, k: int) -> int:
    return min(2 * min(k, n - k), 2 * min(k - 1, n - k) + 1)


def atomic_audit(max_n: int = 9) -> tuple[int, list[str]]:
    boxes = 0
    rows: list[str] = []
    for n in range(1, max_n + 1):
        depth_histogram: Counter[int] = Counter()
        for atom in range(1 << n):
            for t in range(0, 2 * n + 3):
                literal = family_iterate(n, 1 << atom, t)
                closed = atomic_closed(n, atom, t)
                A.equal(literal, closed, ("atomic closed kernel", n, atom, t))
                boxes += 1
                if atom:
                    k = pc(atom)
                    if t % 2 == 0:
                        A.equal(pc(closed), even_ball_volume(n, k, t // 2),
                                ("even volume", n, atom, t))
                    else:
                        A.equal(pc(closed), odd_kernel_volume(n, k, (t - 1) // 2),
                                ("odd volume", n, atom, t))

            tail, period = actual_tail_period(n, 1 << atom)
            if atom == 0:
                A.equal((tail, period), (1, 1), ("silent singleton", n))
            else:
                expected = predicted_atomic_depth(n, pc(atom))
                A.equal(tail, expected, ("atomic depth", n, atom))
                A.check(period in (1, 2), ("atomic eventual period", n, atom))
                depth_histogram[tail] += 1

        expected_histogram = Counter(
            {depth: comb(n, (depth + 1) // 2) for depth in range(n)}
        )
        A.equal(depth_histogram, expected_histogram, ("atomic depth census", n))
        rows.append(
            f"atomic_n={n}|nonempty_atoms={(1 << n)-1}|"
            f"depths={','.join(f'{d}:{depth_histogram[d]}' for d in sorted(depth_histogram))}"
        )
    return boxes, rows


def mobius_cover_counts(n: int, kernels: tuple[int, ...]) -> list[int]:
    """Generic cover IE, used only as a zero-credit falsification control."""
    target_count = 1 << (1 << n)
    values = [0] * target_count
    for target in range(target_count):
        admissible = sum(1 for atom in range(1, 1 << n) if kernels[atom] & ~target == 0)
        values[target] = 1 << admissible
    for bit_index in range(1 << n):
        bit = 1 << bit_index
        for target in range(target_count):
            if target & bit:
                values[target] -= values[target ^ bit]
    return [2 * value for value in values]


def atlas_audit(n: int, iterates: list[list[int]]) -> tuple[list[int], int]:
    state_count = 1 << (1 << n)
    image_sizes: list[int] = [state_count]
    atlas_boxes = 0

    for t in range(1, n + 3):
        actual = [0] * state_count
        for source in range(state_count):
            actual[iterates[t][source]] += 1

        kernels = tuple(atomic_closed(n, atom, t) for atom in range(1 << n))
        predicted = mobius_cover_counts(n, kernels)
        A.equal(actual, predicted, ("every-target inverse IE", n, t))

        image_size = 0
        for target in range(state_count):
            reconstructed = 0
            for atom in range(1, 1 << n):
                if kernels[atom] & ~target == 0:
                    reconstructed |= kernels[atom]
            criterion = reconstructed == target
            A.equal(actual[target] > 0, criterion, ("image criterion", n, t, target))
            image_size += actual[target] > 0
            atlas_boxes += 1
        image_sizes.append(image_size)

        if t >= n - 1:
            recurrent_targets = {rank_union(n, support) for support in range(1 << n)}
            A.equal({target for target, count in enumerate(actual) if count}, recurrent_targets,
                    ("stable image", n, t))
            for support in range(1 << n):
                target = rank_union(n, support)
                source_support = support if t % 2 == 0 else support_dual(n, support)
                expected = 2
                for k in range(1, n + 1):
                    if source_support >> (k - 1) & 1:
                        expected *= 2 ** comb(n, k) - 1
                A.equal(actual[target], expected, ("stable fibre", n, t, support))

    return image_sizes, atlas_boxes


def phase_audit(max_n: int = 4) -> tuple[int, int, list[str]]:
    phase_boxes = 0
    atlas_boxes = 0
    rows: list[str] = []
    for n in range(0, max_n + 1):
        state_count = 1 << (1 << n)
        next_map = [family_step(n, family) for family in range(state_count)]
        iterates = [list(range(state_count))]
        for _ in range(n + 2):
            iterates.append([next_map[value] for value in iterates[-1]])

        actual_depths: Counter[int] = Counter()
        actual_periods: Counter[int] = Counter()
        recurrent: set[int] = set()
        fixed: set[int] = set()
        deep_supports: Counter[int] = Counter()
        for family in range(state_count):
            actual = actual_tail_period(n, family)
            predicted = predicted_tail_period(n, family)
            A.equal(actual, predicted, ("tail/period", n, family))
            for t, values in enumerate(iterates):
                reconstructed = 0
                for atom in members(family):
                    reconstructed |= atomic_closed(n, atom, t)
                A.equal(values[family], reconstructed, ("family union iterate", n, family, t))
            actual_depths[actual[0]] += 1
            actual_periods[actual[1]] += 1
            if actual[0] == 0:
                recurrent.add(family)
            if next_map[family] == family:
                fixed.add(family)
            if n >= 3:
                is_deep = actual[0] == n - 1
                A.equal(is_deep, deepest_predicate(n, family), ("deepest iff singleton", n, family))
                if is_deep:
                    _, _, support = radii_and_support(n, family)
                    deep_supports[support] += 1
            phase_boxes += 1

        expected_recurrent = {rank_union(n, support) for support in range(1 << n)}
        A.equal(recurrent, expected_recurrent, ("recurrent core", n))
        expected_fixed = {
            rank_union(n, support)
            for support in range(1 << n)
            if support_dual(n, support) == support
        }
        A.equal(fixed, expected_fixed, ("fixed core", n))
        A.equal(len(recurrent), 1 << n, ("recurrent count", n))
        A.equal(len(fixed), 1 << ((n + 1) // 2), ("fixed count", n))

        if n == 0:
            A.equal(max(actual_depths), 1, "n=0 exceptional height")
            image_sizes = [state_count, len(set(next_map)), len(set(next_map[value] for value in next_map))]
        elif n == 1:
            A.equal(max(actual_depths), 1, "n=1 exceptional height")
            image_sizes, boxes = atlas_audit(n, iterates)
            atlas_boxes += boxes
        elif n == 2:
            A.equal(max(actual_depths), 1, ("global height", n))
            A.equal(actual_depths[1], 12, "n=2 exceptional deepest census")
            period_one = sum(
                count for depth_period, count in Counter(
                    actual_tail_period(n, family) for family in range(state_count)
                ).items()
                if depth_period == (1, 1)
            )
            A.equal(period_one, 6, "n=2 deepest period-one census")
            image_sizes, boxes = atlas_audit(n, iterates)
            atlas_boxes += boxes
        else:
            A.equal(max(actual_depths), n - 1, ("global height", n))
            A.equal(actual_depths[n - 1], deepest_count(n), ("deepest census", n))
            for support in range(1 << n):
                A.equal(deep_supports[support], support_resolved_deepest_count(n, support),
                        ("support-resolved deepest census", n, support))
            period_one = sum(
                count for support, count in deep_supports.items()
                if support_dual(n, support) == support
            )
            A.equal(period_one, deepest_period_one_count(n), ("deepest period-one census", n))
            A.equal(actual_depths[n - 1] - period_one,
                    deepest_count(n) - deepest_period_one_count(n),
                    ("deepest strict-two-cycle census", n))
            image_sizes, boxes = atlas_audit(n, iterates)
            atlas_boxes += boxes

        rows.append(
            f"phase_n={n}|states={state_count}|height={max(actual_depths)}|"
            f"recurrent={len(recurrent)}|fixed={len(fixed)}|"
            f"depths={','.join(f'{d}:{actual_depths[d]}' for d in sorted(actual_depths))}|"
            f"images={','.join(map(str, image_sizes))}"
        )
        if n == 2:
            rows.append("deep_n=2|exception=all_nonrecurrent|count=12|period1=6|period2=6")
        elif n >= 3:
            rows.append(
                f"deep_n={n}|kstar={middle_rank(n)}|count={deepest_count(n)}|"
                f"period1={deepest_period_one_count(n)}|"
                f"period2={deepest_count(n)-deepest_period_one_count(n)}"
            )
    return phase_boxes, atlas_boxes, rows


def structural_deepest_audit(max_n: int = 12) -> int:
    """Check the extremal-radius logic without enumerating the huge phase."""
    boxes = 0
    for n in range(2, max_n + 1):
        k_star = middle_rank(n)
        for k in range(1, n + 1):
            e_max = min(k, n - k)
            o_max = min(k - 1, n - k)
            A.check(e_max <= n // 2, ("even radius upper bound", n, k))
            A.check(o_max <= (n - 1) // 2, ("odd radius upper bound", n, k))
            boxes += 2

        # Singleton middle slices attain the two bounds that force height n-1.
        for atom in rank_atoms(n, k_star):
            singleton = 1 << atom
            e, o, _ = radii_and_support(n, singleton)
            A.equal(min(2 * e, 2 * o + 1), n - 1,
                    ("middle singleton extremal", n, atom))
            boxes += 1

        # Exhaust every central pair while the layer is small.  The proof for
        # arbitrary size uses the explicit antipode argument recorded in the
        # gate; this computation is only an independent finite falsifier.
        if n <= 8:
            central = rank_atoms(n, k_star)
            for index, left in enumerate(central):
                for right in central[index + 1:]:
                    e, o, _ = radii_and_support(n, (1 << left) | (1 << right))
                    A.check(min(2 * e, 2 * o + 1) < n - 1,
                            ("central pair below deepest", n, left, right))
                    boxes += 1
    return boxes


def main() -> None:
    atomic_boxes, atomic_rows = atomic_audit()
    phase_boxes, atlas_boxes, phase_rows = phase_audit()
    structural_boxes = structural_deepest_audit()
    print("CSD_REENTRY_HOSTILE_VALUE_V1")
    print(f"atomic_boxes={atomic_boxes}|atomic_n=1..9")
    print(f"phase_boxes={phase_boxes}|phase_n=0..4")
    print(f"atlas_target_boxes={atlas_boxes}|atlas_n=1..4")
    print(f"structural_boxes={structural_boxes}|structural_n=2..12")
    for row in atomic_rows:
        print(row)
    for row in phase_rows:
        print(row)
    print(f"assertions={A.assertions}")
    print("MATHEMATICS PASS")
    print("NEW_AXIS COMPLETE_SUPPORT_RESOLVED_DEEPEST_SHELL")
    print("DECISION GREEN_REENTRY_AFTER_CONTRACT_STRENGTHENING")
    print("COBATCH RTI_CEF_COMPATIBLE")
    print("EXTERNAL HOLD_EXTERNAL")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
