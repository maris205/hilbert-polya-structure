#!/usr/bin/env python3
"""Independent exact pilots for the P177--P181 combinatorial lane.

The program uses only Python's standard library.  Every phase space advertised
in stdout is exhausted; no random sample enters an assertion count.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from itertools import permutations, product
from math import comb, factorial, gcd


ASSERTIONS = 0


def check(condition: bool, message: str = "assertion failed") -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    p = 2
    sign = 1
    x = n
    while p * p <= x:
        if x % p == 0:
            x //= p
            sign = -sign
            if x % p == 0:
                return 0
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        sign = -sign
    return sign


def unsigned_stirling_first(n: int, k: int) -> int:
    if n == 0:
        return int(k == 0)
    row = [1]
    for m in range(1, n + 1):
        nxt = [0] * (m + 1)
        for j in range(1, m + 1):
            nxt[j] = (row[j - 1] if j - 1 < len(row) else 0) + (
                (m - 1) * row[j] if j < len(row) else 0
            )
        row = nxt
    return row[k] if 0 <= k < len(row) else 0


def bell(n: int) -> int:
    row = [1]
    for m in range(1, n + 1):
        nxt = [row[-1]]
        for j in range(1, m + 1):
            nxt.append(nxt[-1] + row[j - 1])
        row = nxt
    return row[0]


def falling(n: int, k: int) -> int:
    ans = 1
    for j in range(k):
        ans *= n - j
    return ans


def comp(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    """Composition p after q."""
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p: tuple[int, ...]) -> tuple[int, ...]:
    ans = [0] * len(p)
    for i, x in enumerate(p):
        ans[x] = i
    return tuple(ans)


def cycle_from(p: tuple[int, ...], start: int = 0) -> tuple[int, ...]:
    out = []
    x = start
    while not out or x != start:
        out.append(x)
        x = p[x]
    return tuple(out)


def cycle_count(p: tuple[int, ...]) -> int:
    seen: set[int] = set()
    ans = 0
    for i in range(len(p)):
        if i not in seen:
            ans += 1
            x = i
            while x not in seen:
                seen.add(x)
                x = p[x]
    return ans


def record_lows(word: tuple[int, ...]) -> int:
    best = len(word) + 2
    ans = 0
    for x in word:
        if x < best:
            ans += 1
            best = x
    return ans


def functional_signature(states, update):
    states = list(states)
    index = {x: i for i, x in enumerate(states)}
    check(len(index) == len(states), "duplicate state")
    nxt = []
    indegree = [0] * len(states)
    for x in states:
        y = update(x)
        check(y in index, "carrier not closed")
        j = index[y]
        nxt.append(j)
        indegree[j] += 1
    check(sum(indegree) == len(states), "indegree mass")

    depth = [-1] * len(states)
    period = [-1] * len(states)
    cycles = Counter()
    for root in range(len(states)):
        if depth[root] >= 0:
            continue
        path = []
        local = {}
        u = root
        while depth[u] < 0 and u not in local:
            local[u] = len(path)
            path.append(u)
            u = nxt[u]
        if depth[u] >= 0:
            d = depth[u]
            per = period[u]
            for v in reversed(path):
                d += 1
                depth[v] = d
                period[v] = per
        else:
            cut = local[u]
            cyc = path[cut:]
            per = len(cyc)
            cycles[per] += 1
            for v in cyc:
                depth[v] = 0
                period[v] = per
            d = 0
            for v in reversed(path[:cut]):
                d += 1
                depth[v] = d
                period[v] = per
    check(all(d >= 0 for d in depth), "unclassified depth")
    check(all(p >= 1 for p in period), "unclassified period")
    check(sum(length * count for length, count in cycles.items()) == sum(d == 0 for d in depth),
          "cycle-state mass")
    return {
        "states": len(states),
        "image": sum(v > 0 for v in indegree),
        "max_fibre": max(indegree) if indegree else 0,
        "indegree": indegree,
        "max_depth": max(depth) if depth else 0,
        "depth_hist": Counter(depth),
        "depth": depth,
        "period_points": Counter(period),
        "cycles": cycles,
        "fixed": cycles.get(1, 0),
        "nxt": nxt,
        "state_list": states,
    }


# ---------------------------------------------------------------------------
# C01: anchored minimum-cycle join on permutations


def mcj(p: tuple[int, ...]) -> tuple[int, ...]:
    n = len(p)
    anchored = set(cycle_from(p, 0))
    if len(anchored) == n:
        return p
    a = min(set(range(n)) - anchored)
    q = list(p)
    q[0], q[a] = q[a], q[0]
    return tuple(q)


def mcj_predicted_one_fibre(q: tuple[int, ...]) -> int:
    n = len(q)
    if n == 1:
        return 1
    cyc = cycle_from(q, 0)
    support = set(cyc)
    outside_min = min(set(range(n)) - support, default=n)
    best = n + 1
    cuts = 0
    for x in cyc[1:]:
        if x < best:
            if x < outside_min:
                cuts += 1
            best = x
    return cuts + int(len(cyc) == n)


def mcj_eligible_cuts(q: tuple[int, ...]) -> int:
    """Record-low cut sites that can be unmerged before the untouched cycles."""
    n = len(q)
    cyc = cycle_from(q, 0)
    support = set(cyc)
    outside_min = min(set(range(n)) - support, default=n)
    best = n + 1
    cuts = 0
    for x in cyc[1:]:
        if x < best:
            cuts += int(x < outside_min)
            best = x
    return cuts


def mcj_predicted_time_fibre(q: tuple[int, ...], t: int) -> int:
    """Closed all-target fibre of T^t, including absorption at an n-cycle."""
    ell = mcj_eligible_cuts(q)
    if len(cycle_from(q, 0)) == len(q):
        return sum(comb(ell, j) for j in range(min(t, ell) + 1))
    return comb(ell, t) if t <= ell else 0


def audit_mcj() -> None:
    print("C01 MCJ anchored minimum-cycle join")
    for n in range(1, 10):
        states = list(permutations(range(n)))
        one = Counter()
        basin = defaultdict(Counter)
        depths = Counter()
        for p in states:
            y = mcj(p)
            check(tuple(sorted(y)) == tuple(range(n)), "MCJ closure")
            expected_depth = cycle_count(p) - 1
            u = p
            t = 0
            while mcj(u) != u:
                u = mcj(u)
                t += 1
                check(t <= n - 1, "MCJ clock overflow")
            check(t == expected_depth, "MCJ point clock")
            check(len(cycle_from(u, 0)) == n, "MCJ endpoint")
            one[y] += 1
            basin[u][t] += 1
            depths[t] += 1

        for q in states:
            check(one[q] == mcj_predicted_one_fibre(q), "MCJ one-step fibre")
        check(len(one) == (1 if n == 1 else factorial(n) // 2), "MCJ image size")
        check(max(one.values()) == n, "MCJ maximum one-fibre")
        check(sum(v == n for v in one.values()) == 1, "MCJ unique one-fibre maximum")
        for t, count in depths.items():
            check(count == unsigned_stirling_first(n, t + 1), "MCJ depth Stirling layer")

        basin_sizes = Counter()
        for q, poly in basin.items():
            tail = cycle_from(q, 0)[1:]
            r = record_lows(tail)
            expected = Counter({j: comb(r, j) for j in range(r + 1)})
            check(poly == expected, "MCJ terminal basin polynomial")
            basin_sizes[sum(poly.values())] += 1
        expected_sizes = Counter(
            {2**r: unsigned_stirling_first(n - 1, r) for r in range(0, n)}
        )
        expected_sizes += Counter()  # delete zero entries
        check(basin_sizes == expected_sizes, "MCJ basin-size distribution")
        check(sum(size * count for size, count in basin_sizes.items()) == factorial(n),
              "MCJ basin mass")
        check(depths[n - 1] == 1, "MCJ unique deepest state")

        # A second, independently aggregated audit of every target at every time.
        current = states[:]
        for t in range(n + 1):
            fibres_t = Counter(current)
            for q in states:
                check(
                    fibres_t[q] == mcj_predicted_time_fibre(q, t),
                    "MCJ all-time every-target fibre",
                )
            if t < n:
                current = [mcj(p) for p in current]
        print(
            f"MCJ n={n} states={factorial(n)} image={len(one)} "
            f"max_depth={max(depths)} max_one_fibre={max(one.values())} "
            f"basin_sizes={dict(sorted(basin_sizes.items()))}"
        )
    print(
        "MCJ THEOREM_CHECK depth=cycles-1 recurrent=n-cycles "
        "all-time-fibres=record-cut-binomials terminal-basins=(1+u)^records"
    )


# ---------------------------------------------------------------------------
# C02: inversion followed by a fixed long cycle


def square_roots_of_uniform_cycles(n: int, power: int) -> int:
    d = gcd(n, power)
    length = n // d
    if length % 2 == 0:
        if d % 2:
            return 0
        j = d // 2
        return factorial(d) // (2**j * factorial(j)) * length**j
    return sum(
        factorial(d) // (factorial(d - 2 * j) * 2**j * factorial(j)) * length**j
        for j in range(d // 2 + 1)
    )


def iac_fixed_formula(n: int, m: int) -> int:
    if m % 2:
        return square_roots_of_uniform_cycles(n, m)
    k = m // 2
    d = gcd(n, k)
    length = n // d
    return length**d * factorial(d)


def audit_iac() -> None:
    print("C02 IAC inverse-anchor-cycle affine map")
    for n in range(1, 9):
        c = tuple(list(range(1, n)) + [0])

        def update(p):
            return comp(inverse(p), c)

        states = list(permutations(range(n)))
        sig = functional_signature(states, update)
        for p in states:
            check(update(update(p)) == comp(comp(inverse(c), p), c), "IAC square identity")
        check(sig["image"] == factorial(n), "IAC bijection")
        check(sig["max_fibre"] == 1, "IAC singleton fibres")
        check(all((2 * n) % period == 0 for period in sig["cycles"]), "IAC period divides 2n")
        for m in range(1, 2 * n + 1):
            literal = sum(length * count for length, count in sig["cycles"].items() if m % length == 0)
            check(literal == iac_fixed_formula(n, m), "IAC fixed-power formula")
        predicted_cycles = Counter()
        for r in range(1, 2 * n + 1):
            points = sum(mobius(r // d) * iac_fixed_formula(n, d) for d in divisors(r))
            check(points % r == 0, "IAC Mobius integrality")
            if points:
                predicted_cycles[r] = points // r
        check(predicted_cycles == sig["cycles"], "IAC complete cycle census")
        print(
            f"IAC n={n} states={factorial(n)} cycles={dict(sorted(sig['cycles'].items()))} "
            f"periods={sorted(sig['cycles'])}"
        )


# ---------------------------------------------------------------------------
# C03: conjugate a fixed long cycle by the current permutation


def audit_ctc() -> None:
    print("C03 CTC conjugate-to-cycle map")
    for n in range(1, 9):
        c = tuple(list(range(1, n)) + [0])

        def update(p):
            return comp(comp(inverse(p), c), p)

        states = list(permutations(range(n)))
        sig = functional_signature(states, update)
        check(sig["image"] == factorial(max(0, n - 1)), "CTC image is long cycles")
        for i, q in enumerate(states):
            is_long = len(cycle_from(q, 0)) == n
            check(sig["indegree"][i] == (n if is_long else 0), "CTC uniform front fibre")
        print(
            f"CTC n={n} states={factorial(n)} image={sig['image']} fibre={sig['max_fibre']} "
            f"max_depth={sig['max_depth']} periods={sorted(sig['cycles'])}"
        )


# ---------------------------------------------------------------------------
# C04: totalized prefix-mex word transducer


def prefix_mex(w: tuple[int, ...], q: int) -> tuple[int, ...]:
    seen = set()
    out = []
    for x in w:
        seen.add(x)
        out.append(next((a for a in range(q) if a not in seen), 0))
    return tuple(out)


def audit_pmx() -> None:
    print("C04 PMX totalized prefix-mex transducer")
    boxes = [(2, n) for n in range(1, 11)] + [(3, n) for n in range(1, 9)] + [
        (4, n) for n in range(1, 7)
    ]
    for q, n in boxes:
        states = list(product(range(q), repeat=n))
        sig = functional_signature(states, lambda w, q=q: prefix_mex(w, q))
        check(sig["fixed"] == 0, "PMX has no fixed word in audited boxes")
        check(set(sig["cycles"]) == {2}, "PMX audited recurrent core is period two")
        print(
            f"PMX q={q} n={n} states={q**n} image={sig['image']} "
            f"max_fibre={sig['max_fibre']} max_depth={sig['max_depth']}"
        )


# ---------------------------------------------------------------------------
# C05: cyclic next-occurrence-gap encoding


def equality_partition(w: tuple[int, ...]) -> tuple[int, ...]:
    labels = {}
    out = []
    for x in w:
        if x not in labels:
            labels[x] = len(labels)
        out.append(labels[x])
    return tuple(out)


def next_occurrence_gap(w: tuple[int, ...]) -> tuple[int, ...]:
    n = len(w)
    return tuple(
        next(d for d in range(1, n + 1) if w[(i + d) % n] == x) % n
        for i, x in enumerate(w)
    )


def audit_nog() -> None:
    print("C05 NOG cyclic next-occurrence-gap encoding")
    for n in range(1, 7):
        states = list(product(range(n), repeat=n))
        partition_code = {}
        fibres = Counter()
        blocks_for_code = {}
        for w in states:
            part = equality_partition(w)
            code = next_occurrence_gap(w)
            if part in partition_code:
                check(partition_code[part] == code, "NOG depends only on equality partition")
            else:
                partition_code[part] = code
            fibres[code] += 1
            blocks_for_code[code] = len(set(part))
        check(len(partition_code) == bell(n), "NOG Bell partition count")
        check(len(set(partition_code.values())) == bell(n), "NOG code injectivity")
        for code, count in fibres.items():
            check(count == falling(n, blocks_for_code[code]), "NOG labelled fibre")
        sig = functional_signature(states, next_occurrence_gap)
        print(
            f"NOG n={n} states={n**n} image={sig['image']} Bell={bell(n)} "
            f"max_fibre={sig['max_fibre']} max_depth={sig['max_depth']} "
            f"periods={sorted(sig['cycles'])}"
        )


# ---------------------------------------------------------------------------
# C06: an isolated-tail nonlinear feedback shift register


def tail_and_feedback(w: tuple[int, ...]) -> tuple[int, ...]:
    return w[1:] + (w[0] ^ int(all(w[1:])),)


def primitive_binary_necklaces(n: int) -> int:
    return sum(mobius(d) * 2 ** (n // d) for d in divisors(n)) // n


def audit_tan() -> None:
    print("C06 TAN tail-AND nonlinear feedback register")
    for n in range(2, 17):
        states = list(product((0, 1), repeat=n))
        sig = functional_signature(states, tail_and_feedback)
        check(sig["image"] == 2**n and sig["max_fibre"] == 1, "TAN nonsingular")
        exceptional = {w for w in states if sum(w) >= n - 1}
        check(len(exceptional) == n + 1, "TAN exceptional set size")
        for w in states:
            if sum(w) <= n - 2:
                check(tail_and_feedback(w) == w[1:] + (w[0],), "TAN ordinary necklace action")
            else:
                check(tail_and_feedback(w) in exceptional, "TAN exceptional orbit closure")
        predicted = Counter()
        for d in divisors(n):
            if d == 1:
                predicted[1] += 1
            else:
                predicted[d] += primitive_binary_necklaces(d) - int(d == n)
        predicted[n + 1] += 1
        predicted += Counter()
        check(predicted == sig["cycles"], "TAN complete cycle inventory")
        print(f"TAN n={n} cycles={dict(sorted(sig['cycles'].items()))}")


# ---------------------------------------------------------------------------
# C07: cyclic least-significant-digit radix pass


def rotate_bits_right(x: int, m: int) -> int:
    return (x >> 1) | ((x & 1) << (m - 1))


def cyclic_radix_pass(p: tuple[int, ...], m: int) -> tuple[int, ...]:
    return tuple(rotate_bits_right(x, m) for x in sorted(p, key=lambda x: x & 1))


def audit_crp() -> None:
    print("C07 CRP cyclic radix pass")
    for m in range(1, 4):
        n = 2**m
        states = list(permutations(range(n)))
        maps = {p: p for p in states}
        depth_hist = Counter()
        identity = tuple(range(n))
        cumulative_identity = {}
        for t in range(0, m + 1):
            fibres = Counter(maps.values())
            image_formula = factorial(n // (2**t)) ** (2**t)
            check(len(fibres) == image_formula, "CRP image tower")
            expected_fibre = factorial(n) // image_formula
            check(set(fibres.values()) == {expected_fibre}, "CRP uniform time fibre")
            cumulative_identity[t] = fibres[identity]
            if t < m:
                maps = {p: cyclic_radix_pass(q, m) for p, q in maps.items()}
        check(set(maps.values()) == {identity}, "CRP radix completion")
        for p in states:
            u = p
            t = 0
            while u != identity:
                u = cyclic_radix_pass(u, m)
                t += 1
                check(t <= m, "CRP clock overflow")
            depth_hist[t] += 1
        for t in range(m + 1):
            check(sum(depth_hist[j] for j in range(t + 1)) == cumulative_identity[t],
                  "CRP depth CDF")
        check(max(depth_hist) == m, "CRP sharp radix clock")
        print(
            f"CRP m={m} labels={n} states={factorial(n)} depth_hist={dict(sorted(depth_hist.items()))}"
        )


# ---------------------------------------------------------------------------
# C08: commuting-square row swap on complete binary automata


def dfa_commuting_swap(state):
    a, b = state
    n = len(a)
    mask = [a[b[i]] == b[a[i]] and a[i] != b[i] for i in range(n)]
    aa = list(a)
    bb = list(b)
    for i, active in enumerate(mask):
        if active:
            aa[i], bb[i] = bb[i], aa[i]
    return tuple(aa), tuple(bb)


def audit_dcs() -> None:
    print("C08 DCS DFA commuting-square row swap")
    for n in range(1, 5):
        transformations = list(product(range(n), repeat=n))
        states = list(product(transformations, transformations))
        sig = functional_signature(states, dfa_commuting_swap)
        print(
            f"DCS n={n} states={len(states)} image={sig['image']} fixed={sig['fixed']} "
            f"max_fibre={sig['max_fibre']} max_depth={sig['max_depth']} "
            f"periods={sorted(sig['cycles'])}"
        )


# ---------------------------------------------------------------------------
# C09: support-selection conjugation on permutations


def conjugate_transposition(p: tuple[int, ...], a: int, b: int) -> tuple[int, ...]:
    def tau(x):
        if x == a:
            return b
        if x == b:
            return a
        return x

    return tuple(tau(p[tau(i)]) for i in range(len(p)))


def css(p: tuple[int, ...]) -> tuple[int, ...]:
    n = len(p)
    support = set(cycle_from(p, 0))
    k = len(support)
    canonical = set(range(k))
    if support == canonical:
        return p
    a = min(canonical - support)
    b = max(support - canonical)
    return conjugate_transposition(p, a, b)


def css_depth(p: tuple[int, ...]) -> int:
    support = set(cycle_from(p, 0))
    return len(support - set(range(len(support))))


def audit_css() -> None:
    print("C09 CSS cycle-support selection conjugation")
    for n in range(1, 10):
        states = list(permutations(range(n)))
        basin = defaultdict(Counter)
        depth_hist = Counter()
        fixed = []
        one = Counter()
        for p in states:
            one[css(p)] += 1
            d = css_depth(p)
            u = p
            t = 0
            while css(u) != u:
                u = css(u)
                t += 1
                check(t <= n, "CSS clock overflow")
            check(t == d, "CSS point clock")
            support = set(cycle_from(u, 0))
            check(support == set(range(len(support))), "CSS canonical endpoint")
            basin[u][t] += 1
            depth_hist[t] += 1
        for q in states:
            if css(q) == q:
                fixed.append(q)
                k = len(cycle_from(q, 0))
                expected = Counter(
                    {
                        r: comb(k - 1, r) * comb(n - k, r)
                        for r in range(min(k - 1, n - k) + 1)
                    }
                )
                check(basin[q] == expected, "CSS terminal basin polynomial")
            else:
                check(q not in basin, "CSS nonfixed terminal")
        fixed_formula = sum(factorial(k - 1) * factorial(n - k) for k in range(1, n + 1))
        check(len(fixed) == fixed_formula, "CSS fixed census")
        check(max(depth_hist) == (n - 1) // 2, "CSS sharp clock")
        predicted_depth = Counter()
        for k in range(1, n + 1):
            multiplicity = factorial(k - 1) * factorial(n - k)
            for r in range(min(k - 1, n - k) + 1):
                predicted_depth[r] += multiplicity * comb(k - 1, r) * comb(n - k, r)
        check(depth_hist == predicted_depth, "CSS complete depth census")
        print(
            f"CSS n={n} states={factorial(n)} image={len(one)} fixed={len(fixed)} "
            f"max_depth={max(depth_hist)} max_one_fibre={max(one.values())}"
        )


# ---------------------------------------------------------------------------
# C10: first-descent follower to front (Project Euler's MTF / First Sort)


def first_descent_to_front(p: tuple[int, ...]) -> tuple[int, ...]:
    for i in range(len(p) - 1):
        if p[i] > p[i + 1]:
            return (p[i + 1],) + p[: i + 1] + p[i + 2 :]
    return p


def nonrecord_binary_potential(p: tuple[int, ...]) -> int:
    ans = 0
    record = 0
    for x in p:
        if x < record:
            ans += 1 << (x - 1)
        record = max(record, x)
    return ans


def first_descent_target_fibre(q: tuple[int, ...]) -> int:
    identity = tuple(range(1, len(q) + 1))
    x = q[0]
    eligible = 0
    for i, a in enumerate(q[1:]):
        if i and q[i] > a:
            break
        eligible += int(a > x)
    return eligible + int(q == identity)


def audit_fdf() -> None:
    print("C10 FDF first-descent follower-to-front / First Sort")
    for n in range(1, 9):
        states = list(permutations(range(1, n + 1)))
        sig = functional_signature(states, first_descent_to_front)
        identity = tuple(range(1, n + 1))
        deepest = (n,) + tuple(range(1, n)) if n > 1 else identity
        check(sig["cycles"] == Counter({1: 1}), "FDF unique recurrent state")
        check(sig["max_depth"] == 2 ** (n - 1) - 1, "FDF sharp binary clock")
        for p in states:
            v = first_descent_to_front(p)
            if v != p:
                check(nonrecord_binary_potential(v) < nonrecord_binary_potential(p),
                      "FDF binary potential descent")
        depth_by_state = dict(zip(states, sig["depth"]))
        check(depth_by_state[deepest] == 2 ** (n - 1) - 1, "FDF deepest witness")
        check(sum(t == 2 ** (n - 1) - 1 for t in depth_by_state.values()) == 1,
              "FDF unique deepest state")
        indegree = Counter(first_descent_to_front(p) for p in states)
        for q in states:
            check(indegree[q] == first_descent_target_fibre(q), "FDF every-target fibre")
        if n == 1:
            predicted_positive = Counter({1: 1})
        else:
            predicted_positive = Counter(
                {k: factorial(n) // factorial(k + 1) for k in range(1, n - 1)}
            )
            predicted_positive[n] = 1
        check(Counter(indegree.values()) == predicted_positive, "FDF positive fibre distribution")
        image_formula = sum(predicted_positive.values())
        check(len(indegree) == image_formula, "FDF image census")
        check(sum(k * v for k, v in predicted_positive.items()) == factorial(n),
              "FDF fibre mass")
        print(
            f"FDF n={n} states={factorial(n)} image={len(indegree)} "
            f"max_depth={sig['max_depth']} deepest={deepest} "
            f"positive_fibres={dict(sorted(predicted_positive.items()))}"
        )
    print("FDF OWNER_KILL Project_Euler_523_524 exact_literal")


def main() -> None:
    print("P177-P181 COMBINATORIAL LANE EXACT PILOT")
    print("HOLD_EXTERNAL")
    audit_mcj()
    audit_iac()
    audit_ctc()
    audit_pmx()
    audit_nog()
    audit_tan()
    audit_crp()
    audit_dcs()
    audit_css()
    audit_fdf()
    print("LITERAL_SYSTEMS 10")
    print(f"ASSERTIONS {ASSERTIONS}")
    print("DECISIONS 10_KILL 0_RESERVE 0_PROMOTE")
    print("STATUS PASS")


if __name__ == "__main__":
    main()
