#!/usr/bin/env python3
"""Independent hostile checker for P163 complemented-shadow dynamics."""

from collections import Counter, defaultdict
from math import comb
import hashlib


ASSERTIONS = 0
ROWS = []


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def atoms_of_family(family, atom_count):
    return [a for a in range(atom_count) if (family >> a) & 1]


def shadow_atom(n, atom):
    full = (1 << n) - 1
    image = 0
    for a in range(n):
        if (atom >> a) & 1:
            target = full ^ (atom ^ (1 << a))
            image |= 1 << target
    return image


def shadow_family(n, family):
    atom_count = 1 << n
    out = 0
    for atom in atoms_of_family(family, atom_count):
        out |= shadow_atom(n, atom)
    return out


def iterate(n, family, t):
    for _ in range(t):
        family = shadow_family(n, family)
    return family


def predicted_kernel(n, atom, t):
    if atom == 0:
        return (1 << 0) if t == 0 else 0
    k = atom.bit_count()
    s = t // 2
    out = 0
    for target in range(1 << n):
        rank = target.bit_count()
        intersection = (atom & target).bit_count()
        if t % 2 == 0:
            allowed = rank == k and k - intersection <= s
        else:
            allowed = rank == n - k + 1 and intersection <= s + 1
        if allowed:
            out |= 1 << target
    return out


def rank_union(n, support_mask):
    out = 0
    for atom in range(1 << n):
        rank = atom.bit_count()
        if rank and ((support_mask >> (rank - 1)) & 1):
            out |= 1 << atom
    return out


def phi_support(n, support_mask):
    out = 0
    for k in range(1, n + 1):
        if (support_mask >> (k - 1)) & 1:
            out |= 1 << ((n - k + 1) - 1)
    return out


def support_of(n, family):
    out = 0
    for atom in atoms_of_family(family, 1 << n):
        k = atom.bit_count()
        if k:
            out |= 1 << (k - 1)
    return out


def radius_tables(n):
    tables = {}
    full = (1 << n) - 1
    for k in range(1, n + 1):
        layer = [a for a in range(1 << n) if a.bit_count() == k]
        table = {}
        for selection in range(1, 1 << len(layer)):
            chosen = [layer[i] for i in range(len(layer)) if (selection >> i) & 1]
            e = max(
                min(k - (a & b).bit_count() for a in chosen)
                for b in layer
            )
            dual = [c for c in range(1 << n) if c.bit_count() == n - k + 1]
            o = max(
                min((a & c).bit_count() - 1 for a in chosen)
                for c in dual
            )
            check(e >= 0 and o >= 0)
            atom_mask = sum(1 << a for a in chosen)
            table[atom_mask] = (e, o)
        tables[k] = table
    return tables


def clock_formula(n, family, tables):
    if family == 0:
        return 0
    rank_support = support_of(n, family)
    if rank_support == 0:
        return 1
    e_values = []
    o_values = []
    for k in range(1, n + 1):
        layer_mask = 0
        for atom in range(1 << n):
            if atom.bit_count() == k and ((family >> atom) & 1):
                layer_mask |= 1 << atom
        if layer_mask:
            e, o = tables[k][layer_mask]
            e_values.append(e)
            o_values.append(o)
    clock = min(2 * max(e_values), 2 * max(o_values) + 1)
    return max(int(family & 1 != 0), clock)


def recurrent_set(n):
    return {rank_union(n, support) for support in range(1 << n)}


def literal_tail(n, family, recurrent):
    seen = set()
    t = 0
    while family not in recurrent:
        check(family not in seen, ("premature cycle", n, family))
        seen.add(family)
        family = shadow_family(n, family)
        t += 1
    return t, family


def atomic_checks():
    for n in range(1, 10):
        histogram = Counter()
        for atom in range(1, 1 << n):
            for t in range(0, n + 3):
                got = iterate(n, 1 << atom, t)
                expected = predicted_kernel(n, atom, t)
                check(got == expected, ("kernel", n, atom, t))
            k = atom.bit_count()
            depth = min(2 * min(k, n - k), 2 * min(k - 1, n - k) + 1)
            expected_rank = n - depth // 2 if depth % 2 == 0 else (depth + 1) // 2
            check(k == expected_rank)
            histogram[depth] += 1
        for depth in range(n):
            check(histogram[depth] == comb(n, (depth + 1) // 2),
                  ("atomic census", n, depth, histogram[depth]))
        ROWS.append(
            "atomic n={} depths={}".format(
                n, ",".join(f"{d}:{histogram[d]}" for d in sorted(histogram))
            )
        )


def phase_checks():
    for n in range(2, 5):
        atom_count = 1 << n
        phase_size = 1 << atom_count
        recurrent = recurrent_set(n)
        tables = radius_tables(n)
        depths = Counter()
        period1 = 0
        period2 = 0
        target_counts_by_t = []
        for t in range(0, n + 2):
            target_counts_by_t.append(Counter())

        for family in range(phase_size):
            tail, endpoint = literal_tail(n, family, recurrent)
            predicted_tail = clock_formula(n, family, tables)
            check(tail == predicted_tail, ("clock", n, family, tail, predicted_tail))
            depths[tail] += 1
            next_endpoint = shadow_family(n, endpoint)
            check(next_endpoint in recurrent)
            check(shadow_family(n, next_endpoint) == endpoint)
            if tail == n - 1:
                if next_endpoint == endpoint:
                    period1 += 1
                else:
                    period2 += 1
            for t in range(0, n + 2):
                target_counts_by_t[t][iterate(n, family, t)] += 1

        check(len(recurrent) == 2**n)
        fixed = {x for x in recurrent if shadow_family(n, x) == x}
        check(len(fixed) == 2 ** ((n + 1) // 2))
        check(max(depths) == n - 1)

        if n == 2:
            check(depths[1] == 12)
            check(period1 == 6 and period2 == 6)
        else:
            kstar = (n + 1) // 2
            middle_atoms = [a for a in range(atom_count) if a.bit_count() == kstar]
            deepest_by_condition = 0
            for family in range(phase_size):
                selected = sum((family >> a) & 1 for a in middle_atoms)
                if selected == 1:
                    deepest_by_condition += 1
                    check(literal_tail(n, family, recurrent)[0] == n - 1)
            total_formula = comb(n, kstar) * 2 ** (2**n - comb(n, kstar))
            check(depths[n - 1] == deepest_by_condition == total_formula)

        # Independently construct all inverse counts by optional atomic kernels.
        for t in range(1, n + 2):
            dp = {0: 1}
            for atom in range(1, atom_count):
                kernel = predicted_kernel(n, atom, t)
                new = defaultdict(int)
                for union, count in dp.items():
                    new[union] += count
                    new[union | kernel] += count
                dp = dict(new)
            predicted_counts = {target: 2 * count for target, count in dp.items()}
            observed_counts = target_counts_by_t[t]
            check(set(predicted_counts) == set(observed_counts), ("image", n, t))
            for target in set(predicted_counts) | set(observed_counts):
                check(predicted_counts.get(target, 0) == observed_counts.get(target, 0),
                      ("inverse", n, t, target))

            if t >= n - 1:
                for support in range(1 << n):
                    target = rank_union(n, support)
                    source_support = support if t % 2 == 0 else phi_support(n, support)
                    stable = 2
                    for k in range(1, n + 1):
                        if (source_support >> (k - 1)) & 1:
                            stable *= 2 ** comb(n, k) - 1
                    check(observed_counts[target] == stable,
                          ("stable", n, t, support))

        ROWS.append(
            f"phase n={n} states={phase_size} height={max(depths)} "
            f"deep={depths[n-1]} period={period1}/{period2}"
        )


def structural_formula_checks():
    for n in range(3, 13):
        kstar = (n + 1) // 2
        middle = comb(n, kstar)
        total = middle * 2 ** (2**n - middle)

        # Sum the endpoint-support refinement directly.
        support_total = 0
        period1 = 0
        for support in range(1 << n):
            if not ((support >> (kstar - 1)) & 1):
                continue
            term = 2 * middle
            for k in range(1, n + 1):
                if k != kstar and ((support >> (k - 1)) & 1):
                    term *= 2 ** comb(n, k) - 1
            support_total += term
            if phi_support(n, support) == support:
                period1 += term
        check(support_total == total)
        check(0 < period1 <= total)
        ROWS.append(
            f"structure n={n} central={middle} total_digits={len(str(total))} "
            f"period1_digits={len(str(period1))}"
        )


def main():
    print("P163 HOSTILE REVIEW A INDEPENDENT CHECK V1")
    atomic_checks()
    phase_checks()
    structural_formula_checks()
    for row in ROWS:
        print(row)
    print(f"ASSERTIONS {ASSERTIONS}")
    print("ROW_SHA256 " + hashlib.sha256("\n".join(ROWS).encode()).hexdigest())
    print("STATUS PASS")


if __name__ == "__main__":
    main()
