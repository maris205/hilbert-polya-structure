#!/usr/bin/env python3
"""Independent Hostile Review A verifier for P166.

This program starts from the literal map

    T_n(x) = x + wt(x) * (1,...,1)  mod n

and does not import author, scout, or Gate-A code.  It combines exhaustive
literal functional graphs, exhaustive weak-composition phase maps, and a
separate labelled-bin coefficient calculation.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import product
from math import comb, factorial, isqrt


ASSERTIONS = 0


def check(condition: bool, message: str = "assertion failed") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def decode(code: int, n: int) -> tuple[int, ...]:
    out = []
    for _ in range(n):
        code, digit = divmod(code, n)
        out.append(digit)
    return tuple(out)


def encode(word: tuple[int, ...], n: int) -> int:
    code = 0
    place = 1
    for digit in word:
        code += digit * place
        place *= n
    return code


def literal_step(word: tuple[int, ...], n: int) -> tuple[int, ...]:
    weight = sum(a != 0 for a in word)
    return tuple((a + weight) % n for a in word)


def transition_table(n: int) -> list[int]:
    return [encode(literal_step(decode(code, n), n), n) for code in range(n**n)]


def functional_graph(next_state: list[int]) -> tuple[list[int], list[int]]:
    """Return preperiod and eventual exact period for every state."""
    size = len(next_state)
    depth = [-1] * size
    period = [0] * size
    for root in range(size):
        if depth[root] >= 0:
            continue
        path: list[int] = []
        position: dict[int, int] = {}
        v = root
        while depth[v] < 0 and v not in position:
            position[v] = len(path)
            path.append(v)
            v = next_state[v]
        if depth[v] >= 0:
            d = depth[v]
            p = period[v]
            for u in reversed(path):
                d += 1
                depth[u] = d
                period[u] = p
        else:
            start = position[v]
            p = len(path) - start
            for u in path[start:]:
                depth[u] = 0
                period[u] = p
            d = 0
            for u in reversed(path[:start]):
                d += 1
                depth[u] = d
                period[u] = p
    return depth, period


def stirling2_table(limit: int) -> list[list[int]]:
    s = [[0] * (limit + 1) for _ in range(limit + 1)]
    s[0][0] = 1
    for n in range(1, limit + 1):
        for k in range(1, n + 1):
            s[n][k] = s[n - 1][k - 1] + k * s[n - 1][k]
    return s


S2 = stirling2_table(64)


def period_formula(n: int, k: int) -> int:
    if k == 1:
        return 1 + (n - 1) ** n
    if 2 <= k <= n:
        return factorial(k) * S2[n][k]
    return 0


def recurrent_formula(n: int) -> int:
    return (n - 1) ** n + sum(factorial(k) * S2[n][k] for k in range(1, n + 1))


def depth_formula(n: int, d: int) -> int:
    if d == 0:
        return recurrent_formula(n)
    if d >= n - 1:
        return 0
    return factorial(d) * sum(
        comb(n, s) * S2[s][d] * (n - d - 1) ** (n - s)
        for s in range(d, n)
    )


def h_value(n: int) -> int:
    h = (isqrt(8 * n + 1) - 1) // 2
    while (h + 1) * (h + 2) // 2 <= n:
        h += 1
    while h * (h + 1) // 2 > n:
        h -= 1
    return h


def multiplicities(word: tuple[int, ...], n: int) -> tuple[int, ...]:
    m = [0] * n
    for a in word:
        m[a] += 1
    return tuple(m)


def phase_map(m: tuple[int, ...]) -> tuple[int, ...]:
    n = len(m)
    return tuple((j + m[j]) % n for j in range(n))


def phase_stats(g: tuple[int, ...], start: int) -> tuple[int, int]:
    seen: dict[int, int] = {}
    v = start
    time = 0
    while v not in seen:
        seen[v] = time
        time += 1
        v = g[v]
    return seen[v], time - seen[v]


def directed_cycles(g: tuple[int, ...]) -> list[tuple[int, ...]]:
    cycles: set[tuple[int, ...]] = set()
    for start in range(len(g)):
        trail: list[int] = []
        pos: dict[int, int] = {}
        v = start
        while v not in pos:
            pos[v] = len(trail)
            trail.append(v)
            v = g[v]
        cyc = trail[pos[v] :]
        anchor = min(range(len(cyc)), key=lambda i: cyc[i])
        canon = tuple(cyc[anchor:] + cyc[:anchor])
        cycles.add(canon)
    return sorted(cycles)


def multinomial_weight(m: tuple[int, ...]) -> int:
    out = factorial(sum(m))
    for a in m:
        out //= factorial(a)
    return out


def weak_compositions(total: int, parts: int):
    prefix = [0] * parts

    def rec(i: int, left: int):
        if i == parts - 1:
            prefix[i] = left
            yield tuple(prefix)
            return
        for value in range(left + 1):
            prefix[i] = value
            yield from rec(i + 1, left - value)

    yield from rec(0, total)


def fibre_formula(m: tuple[int, ...], is_zero_word: bool) -> int:
    n = len(m)
    return (
        int(is_zero_word)
        + int(m[0] == 0)
        + sum(m[k] == n - k for k in range(1, n))
    )


def expected_last_phases(m: tuple[int, ...]) -> set[int]:
    n = len(m)
    zeros = [j for j, a in enumerate(m) if a == 0]
    twos = [j for j, a in enumerate(m) if a == 2]
    ones = [j for j, a in enumerate(m) if a == 1]
    if n < 3 or len(zeros) != 1 or len(twos) != 1 or len(ones) != n - 2:
        return set()
    z, e = zeros[0], twos[0]
    if e == (z - 1) % n:
        return set()
    answer = {(z + 1) % n}
    if e == (z + 1) % n:
        answer.add((z + 2) % n)
    return answer


def coefficient_distribution(n: int) -> Counter[int]:
    """Independent labelled-bin DP for the marked EGF coefficients."""
    # State (used labels, number of triggered generic indicators) -> count.
    dp: dict[tuple[int, int], int] = {(0, 0): 1}
    for bin_index in range(n):
        nxt: dict[tuple[int, int], int] = defaultdict(int)
        for (used, degree), ways in dp.items():
            for count in range(n - used + 1):
                if bin_index == 0:
                    mark = count == 0
                else:
                    mark = count == n - bin_index
                nxt[(used + count, degree + int(mark))] += ways * comb(n - used, count)
        dp = nxt
    dist = Counter({degree: ways for (used, degree), ways in dp.items() if used == n})
    # The all-zero target has generic degree 0 but literal degree 1.
    dist[0] -= 1
    dist[1] += 1
    if dist[0] == 0:
        del dist[0]
    return dist


def check_literal_boxes() -> list[str]:
    lines = ["[literal functional graphs n=2..7]"]
    for n in range(2, 8):
        size = n**n
        nxt = transition_table(n)
        depth, period = functional_graph(nxt)
        indegree = [0] * size
        for image in nxt:
            indegree[image] += 1

        # The update preserves all coordinate differences.
        for code, image in enumerate(nxt):
            x = decode(code, n)
            tx = decode(image, n)
            for i in range(1, n):
                check((tx[i] - tx[0]) % n == (x[i] - x[0]) % n,
                      f"difference invariant n={n}, code={code}")

        pcount = Counter(period[i] for i in range(size) if depth[i] == 0)
        dcount = Counter(depth)
        for k in range(1, n + 1):
            check(pcount[k] == period_formula(n, k), f"period census n={n}, k={k}")
            check(pcount[k] % k == 0, f"cycle divisibility n={n}, k={k}")
        check(sum(pcount.values()) == recurrent_formula(n), f"recurrent n={n}")
        for d in range(0, n + 2):
            check(dcount[d] == depth_formula(n, d), f"depth census n={n}, d={d}")
        check(max(depth) == n - 2, f"sharp tail n={n}")

        # Fixed iterates and exact-period divisor conversion.
        current = list(range(size))
        for r in range(1, 2 * n + 1):
            current = [nxt[v] for v in current]
            fixed = sum(v == i for i, v in enumerate(current))
            expected = sum(period_formula(n, k) for k in range(1, n + 1) if r % k == 0)
            check(fixed == expected, f"fixed iterate n={n}, r={r}")

        # Every target one-step fibre, including separate weights 0 and n.
        target_fibre_dist = Counter()
        for code in range(size):
            word = decode(code, n)
            m = multiplicities(word, n)
            predicted = fibre_formula(m, code == 0)
            check(indegree[code] == predicted, f"one-step target n={n}, y={code}")
            target_fibre_dist[predicted] += 1
        check(sum(k * v for k, v in target_fibre_dist.items()) == size,
              f"global indegree mass n={n}")
        check(target_fibre_dist == coefficient_distribution(n), f"marked EGF n={n}")
        expected_max = 1 if n == 2 else 1 + h_value(n)
        check(max(indegree) == expected_max, f"maximum fibre n={n}")

        # Target-local all-time oracle.  Exhaust all targets through n=6;
        # use a deterministic 7,000-target slice at n=7.
        if n <= 6:
            targets = range(size)
        else:
            targets = ((137 * q + 19) % size for q in range(7000))
        for code in targets:
            y = decode(code, n)
            m = multiplicities(y, n)
            g = phase_map(m)
            phase_positions = list(range(n))
            literal_positions = [
                encode(tuple((a - j) % n for a in y), n) for j in range(n)
            ]
            for t in range(0, 2 * n + 1):
                phase_count = sum(j == 0 for j in phase_positions)
                literal_count = sum(v == code for v in literal_positions)
                check(phase_count == literal_count,
                      f"all-time oracle n={n}, y={code}, t={t}")
                if t == 0:
                    check(phase_count == 1, f"t=0 identity n={n}, y={code}")
                phase_positions = [g[j] for j in phase_positions]
                literal_positions = [nxt[v] for v in literal_positions]

        lines.append(
            f"n={n};states={size};recurrent={dcount[0]};"
            f"maxdepth={max(depth)};image={size-target_fibre_dist.get(0,0)};"
            f"maxfibre={max(indegree)}"
        )
    return lines


def check_composition_boxes() -> list[str]:
    lines = ["[independent weak-composition phase audit n=2..11]"]
    total_profiles = 0
    total_weight = 0
    for n in range(2, 12):
        weighted_period = Counter()
        weighted_depth = Counter()
        weighted_indegree = Counter()
        last_weight = 0
        profile_count = 0
        for m in weak_compositions(n, n):
            profile_count += 1
            total_profiles += 1
            weight = multinomial_weight(m)
            total_weight += weight
            g = phase_map(m)
            d0, p0 = phase_stats(g, 0)
            weighted_depth[d0] += weight
            if d0 == 0:
                weighted_period[p0] += weight

            cycles = directed_cycles(g)
            nontrivial = [c for c in cycles if len(c) > 1]
            check(len(nontrivial) <= 1, f"cycle uniqueness n={n}, m={m}")
            for cycle in nontrivial:
                cset = set(cycle)
                support = {j for j, a in enumerate(m) if a > 0}
                check(cset == support, f"cycle support n={n}, m={m}")
                check(sum(m[j] for j in cycle) == n, f"cycle mass n={n}, m={m}")
                for index, j in enumerate(cycle):
                    next_j = cycle[(index + 1) % len(cycle)]
                    check(m[j] == (next_j - j) % n, f"cycle gaps n={n}, m={m}")
            for j in range(n):
                if g[j] == j:
                    check(m[j] in (0, n), f"fixed phase classification n={n}, m={m}")

            phase_depths = {j: phase_stats(g, j)[0] for j in range(n)}
            check(max(phase_depths.values()) <= n - 2, f"tail cap n={n}, m={m}")
            got_last = {j for j, d in phase_depths.items() if d == n - 2 and n >= 3}
            want_last = expected_last_phases(m)
            check(got_last == want_last, f"last-shell phases n={n}, m={m}")

            # Degree of a target with profile m.  Only m=(n,0,...,0)
            # corresponds to the all-zero literal target.
            is_zero = m[0] == n
            direct_degree = sum(g[j] == 0 for j in range(n))
            predicted_degree = fibre_formula(m, is_zero)
            check(direct_degree == predicted_degree, f"phase fibre n={n}, m={m}")
            weighted_indegree[predicted_degree] += weight
            if d0 == n - 2 and n >= 3:
                last_weight += weight

            h = h_value(n)
            middle_hits = sum(m[k] == n - k for k in range(1, n))
            if n == 2:
                check(predicted_degree <= 1, f"binary permutation n=2, m={m}")
            else:
                equality_condition = m[0] == 0 and middle_hits == h
                check((predicted_degree == 1 + h) == equality_condition,
                      f"max-fibre equality n={n}, m={m}")

        check(sum(weighted_depth.values()) == n**n, f"profile mass n={n}")
        check(weighted_indegree == coefficient_distribution(n), f"profile EGF n={n}")
        for k in range(1, n + 1):
            check(weighted_period[k] == period_formula(n, k), f"profile periods n={n}, k={k}")
        for d in range(0, n + 2):
            check(weighted_depth[d] == depth_formula(n, d), f"profile depths n={n}, d={d}")
        expected_last = 0 if n == 2 else (n - 1) * factorial(n) // 2
        check(last_weight == expected_last, f"last shell n={n}")
        lines.append(
            f"n={n};profiles={profile_count};weighted={n**n};"
            f"last={last_weight};maxfibre={max(weighted_indegree)}"
        )
    lines.append(f"composition_profiles_total={total_profiles};weighted_total={total_weight}")
    return lines


def check_egf_and_boundaries() -> list[str]:
    lines = ["[marked-EGF and boundary extension]"]
    for n in range(2, 31):
        dist = coefficient_distribution(n)
        check(sum(dist.values()) == n**n, f"EGF total n={n}")
        check(sum(k * v for k, v in dist.items()) == n**n, f"EGF indegree mass n={n}")
        expected_max = 1 if n == 2 else 1 + h_value(n)
        check(max(dist) == expected_max, f"EGF maximum support n={n}")
        if n in (2, 3, 4, 6, 8, 9, 12, 16, 20, 24, 30):
            lines.append(
                f"n={n};support={','.join(map(str, sorted(dist)))};"
                f"image={n**n-dist.get(0,0)};maxfibre={max(dist)}"
            )

    # Explicit triangular-remainder construction across every boundary.
    for n in range(3, 257):
        h = h_value(n)
        triangular = h * (h + 1) // 2
        remainder = n - triangular
        check(0 <= remainder <= h, f"triangular remainder n={n}")
        check(triangular <= n < (h + 1) * (h + 2) // 2, f"h floor n={n}")
        m = [0] * n
        for r in range(1, h + 1):
            m[n - r] = r
        if remainder:
            check(m[1] == 0, f"remainder bin unused n={n}")
            m[1] = remainder
            check(remainder < n - 1, f"remainder nontrigger n={n}")
        check(sum(m) == n and m[0] == 0, f"witness mass n={n}")
        hits = sum(m[k] == n - k for k in range(1, n))
        check(hits == h, f"witness hit count n={n}")
        check(fibre_formula(tuple(m), False) == 1 + h, f"witness fibre n={n}")

    # Complete shape/phase boundary for moderate sizes and sampled large sizes.
    for n in range(3, 65):
        for z in range(n):
            for e in range(n):
                if e == z:
                    continue
                m = [1] * n
                m[z] = 0
                m[e] = 2
                g = phase_map(tuple(m))
                got = {j for j in range(n) if phase_stats(g, j)[0] == n - 2}
                check(got == expected_last_phases(tuple(m)), f"last witness n={n}, z={z}, e={e}")

    # The t=0 oracle, integer-weight 0/n split, and composite moduli get
    # dedicated visible sentinels in addition to the exhaustive checks.
    for n in (2, 4, 6, 8, 9, 10, 12, 15, 16, 20, 27, 32, 48, 64):
        zero = (0,) * n
        no_zero = (1,) * n
        check(literal_step(zero, n) == zero, f"weight-zero branch n={n}")
        check(literal_step(no_zero, n) == no_zero, f"weight-n branch n={n}")
        check(fibre_formula(multiplicities(zero, n), True) == 1, f"zero target n={n}")
        check(fibre_formula(multiplicities(no_zero, n), False) >= 1, f"full branch n={n}")
    lines.append("sentinels=t0,n2,composite,weight0/weightn,triangular,last-shell PASS")
    return lines


def main() -> None:
    output = ["P166 HAMMING-WEIGHT TRANSLATION -- INDEPENDENT HOSTILE REVIEW A"]
    output.extend(check_literal_boxes())
    output.extend(check_composition_boxes())
    output.extend(check_egf_and_boundaries())
    output.append(f"ASSERTIONS={ASSERTIONS}")
    output.append("RESULT=PASS")
    output.append("SEVERITY=0C/0M/0m")
    output.append("EXTERNAL_STATUS=HOLD_EXTERNAL")
    print("\n".join(output))


if __name__ == "__main__":
    main()
