#!/usr/bin/env python3
"""Deterministic exact scouting controls for the P187--P191 root lane.

These finite checks pressure candidate formulae.  They are not proofs,
experiments, novelty checks, or counts of validated dynamical subclasses.
"""

from __future__ import annotations

from collections import Counter
from itertools import permutations, product
from math import comb, gcd, lcm


ASSERTIONS = 0


def check(condition: bool, message: str = "") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def orbit(update, state):
    seen = {}
    x = state
    while x not in seen:
        seen[x] = len(seen)
        x = update(x)
    return seen[x], len(seen) - seen[x], x


def matmul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def cdq_matrix_fibre(target, height):
    size = height + 1
    acc = [[int(i == j) for j in range(size)] for i in range(size)]
    for value in target:
        local = [[int(max(i - j, 0) == value) for j in range(size)]
                 for i in range(size)]
        acc = matmul(acc, local)
    return sum(acc[i][i] for i in range(size))


def independent_cycle(mask, n):
    if n == 1:
        return not (mask & 1)
    return all(not ((mask >> i) & 1 and (mask >> ((i + 1) % n)) & 1)
               for i in range(n))


def rc01_cdq():
    boxes = 0
    states_seen = 0
    deepest = []
    for m in range(2, 7):
        for height in range(1, 4):
            states = list(product(range(height + 1), repeat=m))
            update = lambda x: tuple(max(x[i] - x[(i + 1) % m], 0)
                                     for i in range(m))
            fibres = Counter(update(x) for x in states)
            fixed = 0
            max_tail = 0
            for x in states:
                y = update(x)
                check(all(0 <= z <= height for z in y), "CDQ closure")
                tail, period, endpoint = orbit(update, x)
                check(period == 1, "CDQ nonfixed recurrence")
                check(tail <= (1 if m == 2 else height), "CDQ clock")
                check(update(endpoint) == endpoint, "CDQ endpoint")
                is_fixed = all(not (x[i] and x[(i + 1) % m])
                               for i in range(m))
                check((y == x) == is_fixed, "CDQ fixed locus")
                fixed += is_fixed
                max_tail = max(max_tail, tail)
            predicted_fixed = sum(height ** mask.bit_count()
                                  for mask in range(1 << m)
                                  if independent_cycle(mask, m))
            check(fixed == predicted_fixed, "CDQ fixed census")
            check(max_tail == (1 if m == 2 else height), "CDQ sharp clock")
            for target in product(range(height + 1), repeat=m):
                check(fibres[target] == cdq_matrix_fibre(target, height),
                      "CDQ every-target fibre")
            boxes += 1
            states_seen += len(states)
            deepest.append((m, height, max_tail))
    return f"boxes={boxes} states={states_seen} last={deepest[-1]}"


def cyclic_longest_run(bits):
    n = len(bits)
    if not any(bits):
        return 0
    check(not all(bits), "run called on all-one cycle")
    doubled = bits + bits
    best = run = 0
    for value in doubled:
        run = run + 1 if value else 0
        best = max(best, run)
    return min(best, n - 1)


def rc02_cgs():
    boxes = states_seen = 0
    for m in range(2, 8):
        for height in range(1, 4):
            update = lambda x: tuple(min(x[i], x[(i + 1) % m])
                                     for i in range(m))
            terminal_counts = Counter()
            for x in product(range(height + 1), repeat=m):
                minimum = min(x)
                tail, period, endpoint = orbit(update, x)
                expected_tail = cyclic_longest_run(
                    tuple(value > minimum for value in x))
                check(period == 1, "CGS recurrence")
                check(tail == expected_tail, "CGS gap clock")
                check(endpoint == (minimum,) * m, "CGS endpoint")
                y = x
                for t in range(m):
                    expected = tuple(min(x[(i + j) % m]
                                         for j in range(t + 1))
                                     for i in range(m))
                    check(y == expected, "CGS window iterate")
                    y = update(y)
                terminal_counts[minimum] += 1
                states_seen += 1
            for b in range(height + 1):
                predicted = ((height - b + 1) ** m
                             - (height - b) ** m)
                check(terminal_counts[b] == predicted, "CGS terminal fibre")
            boxes += 1
    return f"boxes={boxes} states={states_seen}"


def prefix_mask(k):
    return (1 << k) - 1 if k else 0


def initial_run(mask, n):
    r = 0
    while r < n and (mask >> r) & 1:
        r += 1
    return r


def rc03_sct():
    states_seen = 0
    deepest_signature = []
    for n in range(0, 14):
        update = lambda mask: mask & prefix_mask(mask.bit_count())
        fibres = Counter(update(mask) for mask in range(1 << n))
        terminal = Counter()
        max_tail = 0
        deepest = []
        fixed = 0
        for mask in range(1 << n):
            tail, period, endpoint = orbit(update, mask)
            r = initial_run(mask, n)
            check(period == 1, "SCT recurrence")
            check(endpoint == prefix_mask(r), "SCT endpoint")
            check(tail <= max(0, n - 1), "SCT clock")
            fixed += update(mask) == mask
            terminal[r] += 1
            if tail > max_tail:
                max_tail, deepest = tail, [mask]
            elif tail == max_tail:
                deepest.append(mask)
            states_seen += 1
            k = mask.bit_count()
            y = update(mask)
            for _ in range(n + 1):
                check(y == mask & prefix_mask(k), "SCT rank iterate")
                k = (mask & prefix_mask(k)).bit_count()
                y = update(y)
        check(fixed == n + 1, "SCT fixed census")
        for target in range(1 << n):
            b = target.bit_count()
            maximum = target.bit_length()
            lo = max(b, maximum)
            hi = (n + b) // 2
            predicted = sum(comb(n - k, k - b) for k in range(lo, hi + 1))
            check(fibres[target] == predicted, "SCT one-step fibre")
        for r in range(n + 1):
            predicted = 1 if r == n else 1 << (n - r - 1)
            check(terminal[r] == predicted, "SCT terminal fibre")
        if n >= 2:
            expected = prefix_mask(n) ^ 1
            check(max_tail == n - 1 and deepest == [expected],
                  "SCT unique deepest state")
        else:
            check(max_tail == 0, "SCT small boundary")
        deepest_signature.append((n, max_tail, len(deepest)))
    return f"n=0..13 states={states_seen} last={deepest_signature[-1]}"


def reverse_bits(mask, n):
    out = 0
    for i in range(n):
        if (mask >> i) & 1:
            out |= 1 << (n - 1 - i)
    return out


def rc04_sce():
    states_seen = 0
    for n in range(0, 13):
        full = prefix_mask(n)
        involution = lambda x: reverse_bits(full ^ x, n)
        truncate = lambda x: x & prefix_mask(x.bit_count())
        expand = lambda x: x | prefix_mask(x.bit_count())
        for mask in range(1 << n):
            check(involution(expand(mask)) == truncate(involution(mask)),
                  "SCE conjugacy")
            check(involution(involution(mask)) == mask, "SCE involution")
            states_seen += 1
    return f"conjugacy_states={states_seen}"


def cyclic_group(n):
    return [[(i + j) % n for j in range(n)] for i in range(n)]


def symmetric_group_three():
    elems = list(permutations(range(3)))
    index = {p: i for i, p in enumerate(elems)}
    table = []
    for p in elems:
        row = []
        for q in elems:
            row.append(index[tuple(p[q[i]] for i in range(3))])
        table.append(row)
    return table


def dihedral_group(n):
    elems = [(r, s) for s in range(2) for r in range(n)]
    index = {x: i for i, x in enumerate(elems)}
    table = []
    for r, s in elems:
        row = []
        for u, v in elems:
            row.append(index[((r + (-1 if s else 1) * u) % n, (s + v) % 2)])
        table.append(row)
    return table


def subgroup_masks(table):
    n = len(table)
    identity = next(i for i in range(n)
                    if all(table[i][j] == j and table[j][i] == j
                           for j in range(n)))
    answer = []
    for mask in range(1 << n):
        if not ((mask >> identity) & 1):
            continue
        elements = [i for i in range(n) if (mask >> i) & 1]
        if all((mask >> table[i][j]) & 1 for i in elements for j in elements):
            answer.append(mask)
    return answer


def left_translate(mask, g, table):
    out = 0
    for x in range(len(table)):
        if (mask >> x) & 1:
            out |= 1 << table[g][x]
    return out


def left_stabilizer(mask, table):
    return sum(1 << g for g in range(len(table))
               if left_translate(mask, g, table) == mask)


def generated_subgroup(mask, table):
    n = len(table)
    identity = next(i for i in range(n)
                    if all(table[i][j] == j and table[j][i] == j
                           for j in range(n)))
    out = mask | (1 << identity)
    changed = True
    while changed:
        changed = False
        elems = [i for i in range(n) if (out >> i) & 1]
        for i in elems:
            for j in elems:
                value = table[i][j]
                if not ((out >> value) & 1):
                    out |= 1 << value
                    changed = True
    return out


def rc05_lss_and_rc15_sgc():
    groups = [(f"C{n}", cyclic_group(n)) for n in range(1, 9)]
    groups += [("S3", symmetric_group_three()), ("D8", dihedral_group(4))]
    lss_states = sgc_states = 0
    summaries = []
    for name, table in groups:
        n = len(table)
        subgroups = subgroup_masks(table)
        subgroup_set = set(subgroups)
        fibres = Counter()
        generated_fibres = Counter()
        for mask in range(1 << n):
            stabilizer = left_stabilizer(mask, table)
            check(stabilizer in subgroup_set, "LSS image subgroup")
            check(left_stabilizer(stabilizer, table) == stabilizer,
                  "LSS idempotence")
            fibres[stabilizer] += 1
            closure = generated_subgroup(mask, table)
            check(closure in subgroup_set, "SGC image subgroup")
            check(generated_subgroup(closure, table) == closure,
                  "SGC idempotence")
            generated_fibres[closure] += 1
            lss_states += 1
            sgc_states += 1
        exact = {}
        for h in sorted(subgroups, key=lambda z: z.bit_count(), reverse=True):
            fixed_by_h = 1 << (n // h.bit_count())
            exact[h] = fixed_by_h - sum(value for k, value in exact.items()
                                             if h & ~k == 0 and h != k)
            check(exact[h] == fibres[h], "LSS subgroup inversion")
        check(sum(fibres.values()) == 1 << n, "LSS fibre partition")
        check(sum(generated_fibres.values()) == 1 << n, "SGC fibre partition")
        summaries.append((name, n, len(subgroups), max(fibres.values())))
    return (f"LSS_states={lss_states} SGC_states={sgc_states} "
            f"last={summaries[-1]}")


def compose_permutation(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def permutation_cycle_lengths(p):
    seen = set()
    lengths = []
    for i in range(len(p)):
        if i in seen:
            continue
        j = i
        length = 0
        while j not in seen:
            seen.add(j)
            length += 1
            j = p[j]
        lengths.append(length)
    return lengths


def vtwo(n):
    answer = 0
    while n and n % 2 == 0:
        answer += 1
        n //= 2
    return answer


def order_two_mod(odd):
    if odd == 1:
        return 1
    value = 2 % odd
    answer = 1
    while value != 1:
        value = value * 2 % odd
        answer += 1
    return answer


def rc06_psq():
    total = 0
    max_period = 0
    for n in range(1, 8):
        update = lambda p: compose_permutation(p, p)
        for p in permutations(range(n)):
            lengths = permutation_cycle_lengths(p)
            two_tail = max(vtwo(length) for length in lengths)
            odd_lcm = 1
            for length in lengths:
                odd_lcm = lcm(odd_lcm, length >> vtwo(length))
            tail, period, _ = orbit(update, p)
            check(tail == two_tail, "PSQ tail")
            check(period == order_two_mod(odd_lcm), "PSQ period")
            max_period = max(max_period, period)
            total += 1
    return f"permutations={total} max_period={max_period}"


def compose_function(f, g):
    return tuple(f[g[i]] for i in range(len(f)))


def function_power(f, exponent):
    result = tuple(range(len(f)))
    base = f
    while exponent:
        if exponent & 1:
            result = compose_function(base, result)
        base = compose_function(base, base)
        exponent >>= 1
    return result


def rc07_efs():
    total = 0
    profiles = []
    for n in range(1, 6):
        update = lambda f: compose_function(f, f)
        maximum_tail = maximum_period = 0
        for f in product(range(n), repeat=n):
            y = f
            for t in range(7):
                check(y == function_power(f, 1 << t), "EFS dyadic power")
                y = update(y)
            tail, period, _ = orbit(update, f)
            check(tail >= 0 and period >= 1, "EFS functional graph")
            maximum_tail = max(maximum_tail, tail)
            maximum_period = max(maximum_period, period)
            total += 1
        profiles.append((n, maximum_tail, maximum_period))
    return f"endofunctions={total} profiles={profiles}"


def relation_compose(mask_a, mask_b, n):
    out = 0
    for i in range(n):
        for k in range(n):
            if not ((mask_a >> (i * n + k)) & 1):
                continue
            for j in range(n):
                if (mask_b >> (k * n + j)) & 1:
                    out |= 1 << (i * n + j)
    return out


def rc08_rtc_and_rc09_rsq():
    rtc_total = rsq_total = 0
    rtc_profiles = []
    for n in range(1, 5):
        tc_update = lambda r: r | relation_compose(r, r, n)
        max_tail = 0
        # Closing a directed cycle can first create a loop at path length n,
        # so the universal dyadic bound uses n rather than n-1.
        bound = 0 if n <= 1 else (n - 1).bit_length()
        for relation in range(1 << (n * n)):
            tail, period, endpoint = orbit(tc_update, relation)
            check(period == 1, "RTC recurrence")
            check(tail <= bound, "RTC dyadic clock")
            check(tc_update(endpoint) == endpoint, "RTC closure")
            max_tail = max(max_tail, tail)
            rtc_total += 1
        rtc_profiles.append((n, max_tail))
    rsq_profiles = []
    for n in range(1, 4):
        update = lambda r: relation_compose(r, r, n)
        max_tail = max_period = 0
        for relation in range(1 << (n * n)):
            y = update(relation)
            check(0 <= y < (1 << (n * n)), "RSQ closure")
            tail, period, _ = orbit(update, relation)
            max_tail = max(max_tail, tail)
            max_period = max(max_period, period)
            rsq_total += 1
        rsq_profiles.append((n, max_tail, max_period))
    return (f"RTC_relations={rtc_total} profiles={rtc_profiles}; "
            f"RSQ_relations={rsq_total} profiles={rsq_profiles}")


def rotate_mask(mask, amount, n):
    if n == 0:
        return mask
    amount %= n
    full = prefix_mask(n)
    return ((mask << amount) | (mask >> (n - amount))) & full


def rc10_cbe_and_rc14_hsr():
    boundary_total = shift_total = 0
    summaries = []
    for n in range(1, 16):
        full = prefix_mask(n)
        boundary = lambda x: x & ~(rotate_mask(x, n - 1, n)) & full
        max_shift_period = 0
        for mask in range(1 << n):
            y = boundary(mask)
            check(boundary(y) == y, "CBE idempotence")
            check(all(not ((y >> i) & 1 and (y >> ((i + 1) % n)) & 1)
                      for i in range(n)), "CBE independent image")
            shift = lambda x: rotate_mask(x, x.bit_count(), n)
            z = shift(mask)
            check(z.bit_count() == mask.bit_count(), "HSR cardinality")
            tail, period, _ = orbit(shift, mask)
            check(tail == 0, "HSR permutation")
            expected = n // gcd(n, mask.bit_count()) if mask.bit_count() else 1
            check(period <= expected and expected % period == 0,
                  "HSR orbit divisor")
            max_shift_period = max(max_shift_period, period)
            boundary_total += 1
            shift_total += 1
        summaries.append((n, max_shift_period))
    return (f"boundary_states={boundary_total} shift_states={shift_total} "
            f"last={summaries[-1]}")


def rc11_imn():
    total = 0
    profiles = []
    for n in range(1, 7):
        update = lambda word: tuple(word.count(j) % n for j in range(n))
        max_tail = max_period = 0
        cycle_lengths = set()
        for word in product(range(n), repeat=n):
            y = update(word)
            check(len(y) == n and all(0 <= z < n for z in y), "IMN closure")
            tail, period, _ = orbit(update, word)
            max_tail = max(max_tail, tail)
            max_period = max(max_period, period)
            cycle_lengths.add(period)
            total += 1
        profiles.append((n, max_tail, max_period, tuple(sorted(cycle_lengths))))
    return f"inventory_words={total} profiles={profiles}"


def rc12_ucd():
    total = 0
    for height in range(0, 65):
        update = lambda e: min(e, height - e)
        for exponent in range(height + 1):
            y = update(exponent)
            check(0 <= y <= height, "UCD closure")
            check(update(y) == y, "UCD idempotence")
            total += 1
    return f"primepower_exponents={total}"


def rc13_cpt():
    total = 0
    profiles = []
    for n in range(0, 17):
        update = lambda x: x ^ prefix_mask(x.bit_count())
        max_tail = max_period = 0
        periods = set()
        for mask in range(1 << n):
            y = update(mask)
            check(0 <= y < (1 << n if n else 1), "CPT closure")
            tail, period, _ = orbit(update, mask)
            max_tail = max(max_tail, tail)
            max_period = max(max_period, period)
            periods.add(period)
            total += 1
        profiles.append((n, max_tail, max_period, tuple(sorted(periods))))
    return f"prefix_toggle_states={total} last={profiles[-1]}"


def inverse_in_table(g, table):
    identity = next(i for i in range(len(table))
                    if all(table[i][j] == j and table[j][i] == j
                           for j in range(len(table))))
    return next(h for h in range(len(table))
                if table[g][h] == identity and table[h][g] == identity)


def conjugate_subset(mask, g, table):
    inv = inverse_in_table(g, table)
    out = 0
    for x in range(len(table)):
        if (mask >> x) & 1:
            out |= 1 << table[table[g][x]][inv]
    return out


def conjugation_stabilizer(mask, table):
    return sum(1 << g for g in range(len(table))
               if conjugate_subset(mask, g, table) == mask)


def rc16_cns():
    total = 0
    profiles = []
    for name, table in [("S3", symmetric_group_three()),
                        ("D8", dihedral_group(4))]:
        subs = set(subgroup_masks(table))
        update = lambda mask: conjugation_stabilizer(mask, table)
        max_tail = max_period = 0
        for mask in range(1 << len(table)):
            y = update(mask)
            check(y in subs, "CNS image subgroup")
            tail, period, _ = orbit(update, mask)
            check(period == 1, "CNS normalizer tower recurrence")
            max_tail = max(max_tail, tail)
            max_period = max(max_period, period)
            total += 1
        profiles.append((name, max_tail, max_period))
    return f"subset_states={total} profiles={profiles}"


def main():
    rows = [
        ("RC01_CDQ", rc01_cdq()),
        ("RC02_CGS", rc02_cgs()),
        ("RC03_SCT", rc03_sct()),
        ("RC04_SCE", rc04_sce()),
        ("RC05_LSS_RC15_SGC", rc05_lss_and_rc15_sgc()),
        ("RC06_PSQ", rc06_psq()),
        ("RC07_EFS", rc07_efs()),
        ("RC08_RTC_RC09_RSQ", rc08_rtc_and_rc09_rsq()),
        ("RC10_CBE_RC14_HSR", rc10_cbe_and_rc14_hsr()),
        ("RC11_IMN", rc11_imn()),
        ("RC12_UCD", rc12_ucd()),
        ("RC13_CPT", rc13_cpt()),
        ("RC16_CNS", rc16_cns()),
    ]
    print("P187-P191 ROOT COORDINATOR EXACT PILOT")
    print("scope=bounded_falsification_not_proof_not_novelty")
    print("candidate_denominator=16")
    for name, summary in rows:
        print(f"{name}: PASS {summary}")
    print(f"assertions={ASSERTIONS}")
    print("verdict=PASS")


if __name__ == "__main__":
    main()
