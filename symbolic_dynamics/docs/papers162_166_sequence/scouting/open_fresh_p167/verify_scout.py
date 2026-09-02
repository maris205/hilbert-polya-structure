#!/usr/bin/env python3
"""Independent exact probes for the bounded open-fresh P167 lane.

The program is deterministic, standard-library only, and imports no paper or
earlier-scout code.  Enumeration is used as counterexample pressure; the
all-parameter arguments are recorded in SCOUT.md.
"""

from collections import Counter, defaultdict, deque
from functools import lru_cache


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


# ---------------------------------------------------------------------------
# GCM: greedy-complement dynamics on path matchings / 2 x n domino tilings.


@lru_cache(maxsize=None)
def compositions12(n):
    if n == 0:
        return ((),)
    ans = []
    for first in (1, 2):
        if first <= n:
            ans.extend((first,) + tail for tail in compositions12(n - first))
    return tuple(ans)


def tiling_update(comp):
    """Literal tiling rule, implemented run by run."""
    out = []
    i = 0
    while i < len(comp):
        if comp[i] == 2:
            out.extend((1, 1))
            i += 1
            continue
        j = i
        while j < len(comp) and comp[j] == 1:
            j += 1
        run = j - i
        out.extend((2,) * (run // 2))
        if run % 2:
            out.append(1)
        i = j
    return tuple(out)


def comp_to_matching(comp):
    pos = 1
    edges = []
    for tile in comp:
        if tile == 2:
            edges.append(pos)
        pos += tile
    return tuple(edges)


def matching_to_comp(edges, n):
    starts = set(edges)
    out = []
    i = 1
    while i <= n:
        if i in starts:
            out.append(2)
            i += 2
        else:
            out.append(1)
            i += 1
    return tuple(out)


def greedy_complement(edges, n):
    covered = {v for edge in edges for v in (edge, edge + 1)}
    out = []
    v = 1
    while v <= n:
        if v in covered:
            v += 1
        elif v < n and v + 1 not in covered:
            out.append(v)
            v += 2
        else:
            v += 1
    return tuple(out)


def first_even_edge(edges):
    return min((edge for edge in edges if edge % 2 == 0), default=None)


def functional_stats(start, update):
    seen = {}
    x = start
    while x not in seen:
        seen[x] = len(seen)
        x = update(x)
    return seen[x], len(seen) - seen[x]


def inverse_parser_count(target_comp):
    """Count inverse parses of A(r0) 11 A(r1) ... 11 A(rk).

    Here A(2j)=2^j and A(2j+1)=2^j 1.  This parser is independent
    of source enumeration and gives the every-target one-step fibre.
    """
    word = tuple(target_comp)

    @lru_cache(maxsize=None)
    def parse_a(pos):
        p = pos
        while p < len(word) and word[p] == 2:
            p += 1
        total = 0
        # Even source 1-run: A ends immediately after the forced 2-run.
        if p == len(word):
            total += 1
        elif p + 1 < len(word) and word[p : p + 2] == (1, 1):
            total += parse_a(p + 2)
        # Odd source 1-run: A consumes one further 1.
        if p < len(word) and word[p] == 1:
            q = p + 1
            if q == len(word):
                total += 1
            elif q + 1 < len(word) and word[q : q + 2] == (1, 1):
                total += parse_a(q + 2)
        return total

    return parse_a(0)


def maximal_matching_count(n):
    values = [1, 1, 1]
    if n <= 2:
        return values[n]
    for k in range(3, n + 1):
        values.append(values[k - 2] + values[k - 3])
    return values[n]


def run_gcm():
    rows = []
    for n in range(1, 19):
        comps = compositions12(n)
        states = tuple(comp_to_matching(comp) for comp in comps)
        check(len(states) == len(set(states)), f"GCM duplicate states n={n}")
        check(all(matching_to_comp(e, n) in comps for e in states),
              f"GCM carrier conversion n={n}")

        fibres = defaultdict(int)
        depths = Counter()
        periods = Counter()
        for comp, edges in zip(comps, states):
            target_comp = tiling_update(comp)
            target_edges = greedy_complement(edges, n)
            check(sum(target_comp) == n, f"GCM tiling closure n={n}")
            check(comp_to_matching(target_comp) == target_edges,
                  f"GCM independent literal implementations n={n}")
            fibres[target_edges] += 1

            bad = first_even_edge(edges)
            next_bad = first_even_edge(target_edges)
            if bad is not None:
                check(next_bad is None or next_bad > bad,
                      f"GCM leftmost defect failed n={n}, E={edges}")

            depth, period = functional_stats(
                edges, lambda e, size=n: greedy_complement(e, size)
            )
            depths[depth] += 1
            periods[period] += 1

        canonical = tuple(range(1, n, 2))
        recurrent = {
            edges
            for edges in states
            if functional_stats(edges, lambda e, size=n: greedy_complement(e, size))[0]
            == 0
        }
        expected_recurrent = set()
        for mask in range(1 << len(canonical)):
            expected_recurrent.add(
                tuple(edge for j, edge in enumerate(canonical) if mask & (1 << j))
            )
        check(recurrent == expected_recurrent, f"GCM recurrent locus n={n}")
        for edges in recurrent:
            check(greedy_complement(edges, n) ==
                  tuple(e for e in canonical if e not in edges),
                  f"GCM complement action n={n}")

        expected_periods = {1} if n == 1 else {2}
        check(set(periods) == expected_periods, f"GCM periods n={n}")
        sharp_depth = (n - 1) // 2
        check(max(depths) == sharp_depth, f"GCM sharp depth n={n}")
        witness = tuple(range(2, n, 4))
        check(functional_stats(witness,
              lambda e, size=n: greedy_complement(e, size))[0] == sharp_depth,
              f"GCM sharp witness n={n}")

        brute_fibres = Counter()
        for comp in comps:
            brute_fibres[tiling_update(comp)] += 1
        for target in comps:
            check(inverse_parser_count(target) == brute_fibres[target],
                  f"GCM target parser n={n}, target={target}")
        empty_target = tuple(1 for _ in range(n))
        check(brute_fibres[empty_target] == maximal_matching_count(n),
              f"GCM maximal-matching fibre n={n}")
        check(brute_fibres[empty_target] == max(brute_fibres.values()),
              f"GCM observed largest fibre n={n}")

        rows.append((n, len(states), len(fibres), len(recurrent),
                     max(depths), max(fibres.values()),
                     fibres[()]))

    print("GCM n/states/image/recurrent/maxdepth/maxfibre/empty-target-fibre")
    for row in rows:
        print("GCM", *row, sep=" ")


# ---------------------------------------------------------------------------
# SRW: a rooted star-switch walk on perfect matchings.


@lru_cache(maxsize=None)
def perfect_matchings(labels):
    labels = tuple(labels)
    if not labels:
        return ((),)
    a = labels[0]
    ans = []
    for index in range(1, len(labels)):
        b = labels[index]
        rest = labels[1:index] + labels[index + 1 :]
        for tail in perfect_matchings(rest):
            ans.append(tuple(sorted(((a, b),) + tail)))
    return tuple(ans)


def conjugate_star(matching, v):
    def swap(x):
        if x == 0:
            return v
        if x == v:
            return 0
        return x

    return tuple(sorted(tuple(sorted((swap(a), swap(b)))) for a, b in matching))


def root_partner(matching):
    for a, b in matching:
        if a == 0:
            return b
        if b == 0:
            return a
    raise AssertionError("root has no partner")


def run_srw():
    print("SRW n/states/distinct-neighbour-range/t3-support/t3-max-history")
    for n in range(1, 6):
        m = 2 * n
        states = perfect_matchings(tuple(range(m)))
        state_set = set(states)
        branch_counts = {}
        column_mass = Counter()
        for state in states:
            row = Counter(conjugate_star(state, v) for v in range(m))
            check(sum(row.values()) == m, f"SRW row mass n={n}")
            check(set(row) <= state_set, f"SRW closure n={n}")
            branch_counts[state] = row
            column_mass.update(row)
        check(all(column_mass[state] == m for state in states),
              f"SRW uniform stationarity n={n}")
        for state, row in branch_counts.items():
            for target, multiplicity in row.items():
                check(branch_counts[target][state] == multiplicity,
                      f"SRW reversibility n={n}")

        base = tuple((2 * j, 2 * j + 1) for j in range(n))
        reached = {base}
        queue = deque([base])
        while queue:
            state = queue.popleft()
            for target in branch_counts[state]:
                if target not in reached:
                    reached.add(target)
                    queue.append(target)
        check(reached == state_set, f"SRW irreducible n={n}")

        history = Counter({base: 1})
        initial_partner = root_partner(base)
        t3 = None
        for t in range(0, 6):
            partner_counts = Counter()
            for state, count in history.items():
                partner_counts[root_partner(state)] += count
            same_expected = (m ** t + m - 2) // (m - 1)
            other_expected = (m ** t - 1) // (m - 1)
            check(partner_counts[initial_partner] == same_expected,
                  f"SRW root return n={n}, t={t}")
            for partner in range(1, m):
                if partner != initial_partner:
                    check(partner_counts[partner] == other_expected,
                          f"SRW other partner n={n}, t={t}")
            check(sum(history.values()) == m ** t, f"SRW history mass n={n}, t={t}")
            if t == 3:
                t3 = (len(history), max(history.values()))
            nxt = Counter()
            for state, count in history.items():
                for target, multiplicity in branch_counts[state].items():
                    nxt[target] += count * multiplicity
            history = nxt

        neighbour_range = sorted({len(row) for row in branch_counts.values()})
        print("SRW", n, len(states),
              f"{neighbour_range[0]}..{neighbour_range[-1]}",
              t3[0], t3[1])


# ---------------------------------------------------------------------------
# OFP: orthogonal polarity on incident point-line flags of PG(2,q).


def inv_mod(a, q):
    return pow(a, q - 2, q)


def normalize_projective(vector, q):
    vector = tuple(x % q for x in vector)
    for x in vector:
        if x:
            scale = inv_mod(x, q)
            return tuple((scale * y) % q for y in vector)
    raise ValueError("zero vector has no projective class")


def projective_points(q):
    return tuple(sorted({
        normalize_projective((x, y, z), q)
        for x in range(q) for y in range(q) for z in range(q)
        if (x, y, z) != (0, 0, 0)
    }))


def dot(u, v, q):
    return sum(a * b for a, b in zip(u, v)) % q


def run_ofp():
    print("OFP q/points/flags/fixed-flags/two-cycles")
    for q in (3, 5, 7, 11):
        points = projective_points(q)
        check(len(points) == q * q + q + 1, f"OFP point count q={q}")
        flags = tuple((point, line) for point in points for line in points
                      if dot(point, line, q) == 0)
        check(len(flags) == (q * q + q + 1) * (q + 1),
              f"OFP flag count q={q}")
        flag_set = set(flags)
        fixed = 0
        visited = set()
        two_cycles = 0
        for flag in flags:
            target = (flag[1], flag[0])
            check(target in flag_set, f"OFP closure q={q}")
            check((target[1], target[0]) == flag, f"OFP involution q={q}")
            if target == flag:
                fixed += 1
            elif flag not in visited:
                visited.add(flag)
                visited.add(target)
                two_cycles += 1
        check(fixed == q + 1, f"OFP conic/absolute count q={q}")
        check(2 * two_cycles + fixed == len(flags), f"OFP orbit mass q={q}")
        print("OFP", q, len(points), len(flags), fixed, two_cycles)


def main():
    run_gcm()
    run_srw()
    run_ofp()
    print(f"ASSERTIONS {ASSERTIONS}")
    print("DECISIONS GCM=KILL_INTERNAL_TRAFFIC_TRANSDUCER "
          "SRW=KILL_DIRECT_MATCHING_REWIRING_OWNER "
          "OFP=KILL_DIRECT_POLARITY_INVOLUTION")
    print("FINAL KILL_ALL")
    print("HOLD_EXTERNAL")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
