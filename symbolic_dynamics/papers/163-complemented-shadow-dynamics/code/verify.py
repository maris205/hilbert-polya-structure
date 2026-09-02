#!/usr/bin/env python3
"""Independent exact verifier for P163 complemented-shadow dynamics.

Subsets and set families are represented by two nested levels of bit masks.
This standard-library program imports no scout or re-entry-gate implementation.
Finite enumeration is counterexample pressure, not an all-parameter proof.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
from math import comb


ASSERTIONS = 0


def check(condition: bool, label: object) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def equal(left: object, right: object, label: object) -> None:
    check(left == right, (label, left, right))


@lru_cache(maxsize=None)
def layer(n: int, k: int) -> tuple[int, ...]:
    return tuple(a for a in range(1 << n) if a.bit_count() == k)


def family_members(family: int) -> tuple[int, ...]:
    return tuple(a for a in range(family.bit_length()) if (family >> a) & 1)


def literal_atom_image(n: int, atom: int) -> int:
    if atom == 0:
        return 0
    full = (1 << n) - 1
    out = 0
    bits = atom
    while bits:
        chosen = bits & -bits
        bits ^= chosen
        target = full ^ (atom ^ chosen)
        out |= 1 << target
    return out


@lru_cache(maxsize=None)
def atom_images(n: int) -> tuple[int, ...]:
    return tuple(literal_atom_image(n, a) for a in range(1 << n))


def literal_step(n: int, family: int) -> int:
    out = 0
    images = atom_images(n)
    bits = family
    while bits:
        flag = bits & -bits
        bits ^= flag
        out |= images[flag.bit_length() - 1]
    return out


def literal_iterate(n: int, family: int, t: int) -> int:
    for _ in range(t):
        family = literal_step(n, family)
    return family


def kernel_formula(n: int, atom: int, t: int) -> int:
    if atom == 0:
        return 1 if t == 0 else 0
    k = atom.bit_count()
    out = 0
    if t % 2 == 0:
        radius = t // 2
        for target in layer(n, k):
            if k - (atom & target).bit_count() <= radius:
                out |= 1 << target
    else:
        radius = (t - 1) // 2
        for target in layer(n, n - k + 1):
            if (atom & target).bit_count() <= radius + 1:
                out |= 1 << target
    return out


def kernel_union(n: int, family: int, t: int) -> int:
    out = 0
    for atom in family_members(family):
        out |= kernel_formula(n, atom, t)
    return out


def orbit_data(n: int, family: int) -> tuple[int, int]:
    seen: dict[int, int] = {}
    t = 0
    current = family
    while current not in seen:
        seen[current] = t
        current = literal_step(n, current)
        t += 1
    return seen[current], t - seen[current]


def support_and_radii(n: int, family: int) -> tuple[int, int, int]:
    support = 0
    even: list[int] = []
    odd: list[int] = []
    for k in range(1, n + 1):
        source = tuple(a for a in layer(n, k) if (family >> a) & 1)
        if not source:
            continue
        support |= 1 << (k - 1)
        even.append(max(min(k - (a & b).bit_count() for a in source)
                        for b in layer(n, k)))
        dual = n - k + 1
        odd.append(max(min((a & c).bit_count() - 1 for a in source)
                       for c in layer(n, dual)))
    if not even:
        return support, -1, -1
    return support, max(even), max(odd)


def dual_support(n: int, support: int) -> int:
    out = 0
    for k in range(1, n + 1):
        if (support >> (k - 1)) & 1:
            out |= 1 << (n - k)
    return out


def clock_formula(n: int, family: int) -> tuple[int, int]:
    support, even, odd = support_and_radii(n, family)
    if support == 0:
        return (1, 1) if family & 1 else (0, 1)
    tail = min(2 * even, 2 * odd + 1)
    if family & 1:
        tail = max(1, tail)
    period = 1 if support == dual_support(n, support) else 2
    return tail, period


def recurrent_family(n: int, support: int) -> int:
    out = 0
    for k in range(1, n + 1):
        if (support >> (k - 1)) & 1:
            for a in layer(n, k):
                out |= 1 << a
    return out


def central_rank(n: int) -> int:
    return (n + 1) // 2


def atomic_depth(n: int, k: int) -> int:
    return min(2 * min(k, n - k), 2 * min(k - 1, n - k) + 1)


def atomic_rank_for_depth(n: int, depth: int) -> int:
    return n - depth // 2 if depth % 2 == 0 else (depth + 1) // 2


def deepest_total(n: int) -> int:
    if n == 2:
        return 12
    m = comb(n, central_rank(n))
    return m * 2 ** ((1 << n) - m)


def deepest_by_support(n: int, support: int) -> int:
    kstar = central_rank(n)
    if not ((support >> (kstar - 1)) & 1):
        return 0
    out = 2 * comb(n, kstar)
    for k in range(1, n + 1):
        if k != kstar and ((support >> (k - 1)) & 1):
            out *= 2 ** comb(n, k) - 1
    return out


def deepest_period_one(n: int) -> int:
    kstar = central_rank(n)
    out = 2 * comb(n, kstar)
    unseen = set(range(1, n + 1))
    while unseen:
        k = min(unseen)
        orbit = {k, n - k + 1}
        unseen -= orbit
        if kstar in orbit:
            for j in orbit - {kstar}:
                out *= 2 ** comb(n, j) - 1
        else:
            product_nonempty = 1
            for j in orbit:
                product_nonempty *= 2 ** comb(n, j) - 1
            out *= 1 + product_nonempty
    return out


def inverse_counts_formula(n: int, kernels: tuple[int, ...]) -> list[int]:
    """Cover inclusion-exclusion, retained only as a zero-credit control."""
    state_count = 1 << (1 << n)
    values = [0] * state_count
    for target in range(state_count):
        admissible = sum(1 for a in range(1, 1 << n)
                         if kernels[a] & ~target == 0)
        values[target] = 1 << admissible
    for atom in range(1 << n):
        bit = 1 << atom
        for target in range(state_count):
            if target & bit:
                values[target] -= values[target ^ bit]
    return [2 * x for x in values]


def audit_atomic() -> list[str]:
    rows: list[str] = []
    for n in range(1, 10):
        histogram: Counter[int] = Counter()
        for atom in range(1 << n):
            singleton = 1 << atom
            for t in range(2 * n + 3):
                direct = literal_iterate(n, singleton, t)
                formula = kernel_formula(n, atom, t)
                equal(direct, formula, ("atomic kernel", n, atom, t))
                if atom:
                    k = atom.bit_count()
                    if t % 2 == 0:
                        radius = min(t // 2, k, n - k)
                        volume = sum(comb(k, j) * comb(n - k, j)
                                     for j in range(radius + 1))
                    else:
                        radius = min((t + 1) // 2, k, n - k + 1)
                        volume = sum(comb(k, j) * comb(n - k, j - 1)
                                     for j in range(1, radius + 1))
                    equal(formula.bit_count(), volume,
                          ("kernel volume", n, atom, t))
            tail, period = orbit_data(n, singleton)
            if atom == 0:
                equal((tail, period), (1, 1), ("silent atom", n))
            else:
                k = atom.bit_count()
                depth = atomic_depth(n, k)
                equal(tail, depth, ("atomic depth", n, atom))
                check(period in (1, 2), ("atomic period", n, atom))
                histogram[depth] += 1
        expected = Counter({d: comb(n, (d + 1) // 2) for d in range(n)})
        equal(histogram, expected, ("atomic histogram", n))
        for d in range(n):
            k = atomic_rank_for_depth(n, d)
            equal(atomic_depth(n, k), d, ("depth inverse", n, d))
            equal(sum(1 for j in range(1, n + 1) if atomic_depth(n, j) == d),
                  1, ("unique depth rank", n, d))
        rows.append(
            f"atomic n={n} atoms={(1 << n)-1} depths="
            + ",".join(f"{d}:{histogram[d]}" for d in sorted(histogram))
        )
    return rows


def audit_phase_and_fibres() -> list[str]:
    rows: list[str] = []
    for n in range(5):
        state_count = 1 << (1 << n)
        next_map = [literal_step(n, family) for family in range(state_count)]
        iterates = [list(range(state_count))]
        for _ in range(n + 2):
            iterates.append([next_map[x] for x in iterates[-1]])

        depths: Counter[int] = Counter()
        periods: Counter[int] = Counter()
        recurrent = set()
        fixed = set()
        deep_support: Counter[int] = Counter()
        deep_period: Counter[int] = Counter()
        for family in range(state_count):
            actual = orbit_data(n, family)
            predicted = clock_formula(n, family)
            equal(actual, predicted, ("mixed clock", n, family))
            for t, mapping in enumerate(iterates):
                equal(mapping[family], kernel_union(n, family, t),
                      ("union kernel", n, family, t))
            depths[actual[0]] += 1
            periods[actual[1]] += 1
            if actual[0] == 0:
                recurrent.add(family)
            if next_map[family] == family:
                fixed.add(family)
            if n >= 3 and actual[0] == n - 1:
                support, _, _ = support_and_radii(n, family)
                deep_support[support] += 1
                deep_period[actual[1]] += 1
            if n >= 3:
                central_size = sum(1 for a in layer(n, central_rank(n))
                                   if (family >> a) & 1)
                equal(actual[0] == n - 1, central_size == 1,
                      ("central iff", n, family))

        expected_recurrent = {recurrent_family(n, r) for r in range(1 << n)}
        equal(recurrent, expected_recurrent, ("recurrent atlas", n))
        expected_fixed = {recurrent_family(n, r) for r in range(1 << n)
                          if dual_support(n, r) == r}
        equal(fixed, expected_fixed, ("fixed atlas", n))
        equal(len(recurrent), 1 << n, ("recurrent count", n))
        equal(len(fixed), 1 << ((n + 1) // 2), ("fixed count", n))

        if n in (0, 1):
            equal(max(depths), 1, ("excluded small height", n))
        elif n == 2:
            equal(max(depths), 1, "n=2 height")
            equal(depths[1], 12, "n=2 deepest total")
            by_pair = Counter(orbit_data(n, f) for f in range(state_count))
            equal(by_pair[(1, 1)], 6, "n=2 deepest period one")
            equal(by_pair[(1, 2)], 6, "n=2 deepest period two")
            central_selected = sum(
                sum(1 for a in layer(n, 1) if (f >> a) & 1) == 1
                for f in range(state_count)
            )
            equal(central_selected, 8, "n=2 central predicate shortfall")
            rows.append("deep n=2 total=12 period1=6 period2=6 central_selected=8")
        else:
            equal(max(depths), n - 1, ("height", n))
            equal(depths[n - 1], deepest_total(n), ("deepest total", n))
            for support in range(1 << n):
                equal(deep_support[support], deepest_by_support(n, support),
                      ("support refinement", n, support))
            equal(deep_period[1], deepest_period_one(n),
                  ("deepest period one", n))
            equal(deep_period[2], deepest_total(n) - deepest_period_one(n),
                  ("deepest period two", n))
            equal(sum(deepest_by_support(n, r) for r in range(1 << n)),
                  deepest_total(n), ("support sum", n))
            rows.append(
                f"deep n={n} kstar={central_rank(n)} total={deepest_total(n)} "
                f"period1={deepest_period_one(n)} "
                f"period2={deepest_total(n)-deepest_period_one(n)}"
            )

        image_sizes = [state_count]
        if n >= 1:
            for t in range(1, n + 3):
                actual_fibres = [0] * state_count
                for source in range(state_count):
                    actual_fibres[iterates[t][source]] += 1
                kernels = tuple(kernel_formula(n, a, t) for a in range(1 << n))
                predicted_fibres = inverse_counts_formula(n, kernels)
                for target in range(state_count):
                    equal(actual_fibres[target], predicted_fibres[target],
                          ("every-target fibre", n, t, target))
                    reconstructed = 0
                    for a in range(1, 1 << n):
                        if kernels[a] & ~target == 0:
                            reconstructed |= kernels[a]
                    equal(actual_fibres[target] > 0, reconstructed == target,
                          ("image criterion", n, t, target))
                equal(sum(actual_fibres), state_count, ("fibre mass", n, t))
                equal(actual_fibres[0], 2, ("empty target", n, t))
                image_sizes.append(sum(x > 0 for x in actual_fibres))
                if t >= n - 1:
                    equal({g for g, x in enumerate(actual_fibres) if x},
                          expected_recurrent, ("stable image", n, t))
                    for support in range(1 << n):
                        target = recurrent_family(n, support)
                        source_support = support if t % 2 == 0 else dual_support(n, support)
                        expected = 2
                        for k in range(1, n + 1):
                            if (source_support >> (k - 1)) & 1:
                                expected *= 2 ** comb(n, k) - 1
                        equal(actual_fibres[target], expected,
                              ("stable fibre product", n, t, support))
        rows.append(
            f"phase n={n} states={state_count} height={max(depths)} "
            f"recurrent={len(recurrent)} fixed={len(fixed)} "
            f"depths=" + ",".join(f"{d}:{depths[d]}" for d in sorted(depths))
            + " images=" + ",".join(map(str, image_sizes))
        )
    return rows


def audit_central_structure() -> list[str]:
    rows: list[str] = []
    for n in range(2, 13):
        kstar = central_rank(n)
        for k in range(1, n + 1):
            emax = min(k, n - k)
            omax = min(k - 1, n - k)
            check(emax <= n // 2, ("even cap", n, k))
            check(omax <= (n - 1) // 2, ("odd cap", n, k))
        for atom in layer(n, kstar):
            equal(atomic_depth(n, kstar), n - 1,
                  ("central singleton depth", n, atom))
        if n <= 8:
            central = layer(n, kstar)
            for i, left in enumerate(central):
                for right in central[i + 1:]:
                    family = (1 << left) | (1 << right)
                    support, even, odd = support_and_radii(n, family)
                    equal(support, 1 << (kstar - 1),
                          ("central pair support", n, left, right))
                    check(min(2 * even, 2 * odd + 1) < n - 1,
                          ("central pair not deepest", n, left, right))
        p1 = deepest_period_one(n) if n >= 3 else 6
        p2 = deepest_total(n) - p1
        check(p1 >= 0 and p2 >= 0 and p1 + p2 == deepest_total(n),
              ("period product partition", n))
        if n <= 6:
            split = f"total={deepest_total(n)} period1={p1} period2={p2}"
        else:
            payload = f"{deepest_total(n)}|{p1}|{p2}".encode("ascii")
            split = (
                f"total_digits={len(str(deepest_total(n)))} "
                f"split_sha256={sha256(payload).hexdigest()[:20]}"
            )
        rows.append(f"structure n={n} central={comb(n,kstar)} {split}")
    return rows


def main() -> None:
    rows: list[str] = []
    rows.extend(audit_atomic())
    rows.extend(audit_phase_and_fibres())
    rows.extend(audit_central_structure())
    blob = "\n".join(rows).encode("utf-8")
    print("P163 CSD independent exact verifier")
    for row in rows:
        print(row)
    print(f"ASSERTIONS {ASSERTIONS}")
    print(f"ROW_SHA256 {sha256(blob).hexdigest()}")
    print("DECISION GREEN_REENTRY_AFTER_CONTRACT_STRENGTHENING")
    print("EXTERNAL HOLD_EXTERNAL")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
