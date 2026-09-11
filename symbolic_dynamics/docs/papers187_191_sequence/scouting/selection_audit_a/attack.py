#!/usr/bin/env python3
"""Process-separated hostile controls for five unnumbered scouting candidates.

This program re-encodes every update from its mathematical definition.  It
does not import any lane pilot or verifier.  Its finite enumerations are
counterexample pressure only: a PASS line is not a proof, novelty finding, or
ownership clearance.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
from math import comb, gcd
from pathlib import Path


ASSERTIONS = 0


def check(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def orbit(step, start):
    seen = {}
    x = start
    while x not in seen:
        seen[x] = len(seen)
        x = step(x)
    return seen[x], len(seen) - seen[x], x


SOURCE_BINDINGS = {
    "docs/papers187_191_sequence/scouting/algebra_lane/CANDIDATES.md":
        "9a556b2eeb0dbcf3d7ce97200dddfd920127b0edb977c2e49e33b7af14c01fb1",
    "docs/papers187_191_sequence/scouting/algebra_lane/KILL_LEDGER.md":
        "8bbca099fab07c941092a6411fb6c0f03cab27ce30081d72747b83bd82e8665b",
    "docs/papers187_191_sequence/scouting/algebra_lane/OWNER_SEARCH_LOG.md":
        "7f67238603b0d15f3eccea2c9fd31cec3fd24e195e61128c926fc62404235b6f",
    "docs/papers187_191_sequence/scouting/algebra_lane/THEOREM_SPIKES.md":
        "ad922463c85e0bfb87db143d6ade7ddba58363d46168fbdf16caca91169451b8",
    "docs/papers187_191_sequence/scouting/root_coordinator/CANDIDATES.md":
        "2e42d9c6122dbd130ff004d8ac5277dda197288f973dec429060009cb6b05768",
    "docs/papers187_191_sequence/scouting/root_coordinator/KILL_LEDGER.md":
        "e2e471f4f42e8340754b4971119cb59ba480433643b8b75443539dc44d6b30cf",
    "docs/papers187_191_sequence/scouting/root_coordinator/OWNER_SEARCH.md":
        "ae30d5ac50e485046233034efe021850e983c7227506ae02259217f425ada34d",
    "docs/papers187_191_sequence/scouting/root_coordinator/THEOREM_SPIKES.md":
        "cfcd47f804ea41a72aa048b4d2e1093395400ad25014e84a40eb6fb2eeae8dcf",
    "docs/papers172_176_sequence/scouting/algebra_arithmetic/SCOUT_AND_KILL_LEDGER.md":
        "2a8e024e6f6c8c6029b74387e4634141ed547d13cbfaf85bf50becab60a060a8",
}


def bind_sources() -> str:
    root = Path(__file__).resolve().parents[4]
    joined = sha256()
    for rel, expected in sorted(SOURCE_BINDINGS.items()):
        actual = sha256((root / rel).read_bytes()).hexdigest()
        check(actual == expected, f"source drift: {rel}")
        joined.update(f"{rel}\0{actual}\n".encode())
    return joined.hexdigest()


# A01: coordinates in each Jordan block run bottom to top.


def nil_shift(v, blocks, q):
    out = []
    offset = 0
    for length in blocks:
        block = v[offset:offset + length]
        out.extend(block[1:])
        out.append(0)
        offset += length
    return tuple(x % q for x in out)


def nil_height(v, blocks, q):
    if not any(v):
        return 0
    h = 0
    x = v
    while any(x):
        x = nil_shift(x, blocks, q)
        h += 1
    return h


def last_nonzero(v, blocks, q):
    h = nil_height(v, blocks, q)
    x = v
    for _ in range(max(0, h - 1)):
        x = nil_shift(x, blocks, q)
    return x


def kernel_targets(q, blocks):
    positions = []
    offset = 0
    for length in blocks:
        positions.append(offset)
        offset += length
    for values in product(range(q), repeat=len(blocks)):
        y = [0] * sum(blocks)
        for position, value in zip(positions, values):
            y[position] = value
        yield tuple(y)


def target_L(y, blocks):
    support_lengths = []
    offset = 0
    for length in blocks:
        if y[offset] != 0:
            support_lengths.append(length)
        offset += length
    return min(support_lengths) if support_lengths else 0


def attack_a01():
    boxes = ((2, (1,)), (2, (4, 2, 1)), (2, (2, 2)),
             (3, (3, 1)), (3, (2, 2)), (5, (2,)))
    states_total = 0
    unequal_signatures = []
    for q, blocks in boxes:
        states = tuple(product(range(q), repeat=sum(blocks)))
        step = lambda v, q=q, blocks=blocks: last_nonzero(v, blocks, q)
        fibres = Counter(step(v) for v in states)
        targets = tuple(kernel_targets(q, blocks))
        check(set(fibres) == set(targets), "A01 image is kernel")
        check(len(targets) == q ** len(blocks), "A01 kernel census")
        for v in states:
            y = step(v)
            check(step(y) == y, "A01 idempotence")
            tail, period, endpoint = orbit(step, v)
            check(period == 1 and tail in (0, 1), "A01 orbit silhouette")
            check(endpoint == y, "A01 endpoint")
            check((tail == 0) == (v in targets), "A01 depth/kernel")
        check(fibres.get((0,) * sum(blocks), 0) == 1, "A01 zero fibre")
        l_hist = Counter()
        for y in targets:
            if not any(y):
                continue
            ell = target_L(y, blocks)
            l_hist[ell] += 1
            predicted = 0
            for h in range(1, ell + 1):
                exponent = sum(min(h - 1, length) for length in blocks)
                stratum = sum(1 for v in states
                              if nil_height(v, blocks, q) == h and step(v) == y)
                check(stratum == q ** exponent, "A01 height-partition fibre")
                if h == 1:
                    check(stratum == 1, "A01 h=1 contribution")
                predicted += q ** exponent
            check(fibres[y] == predicted, "A01 total fibre formula")
        for ell in sorted(set(blocks)):
            ge_ell = sum(length >= ell for length in blocks)
            ge_next = sum(length >= ell + 1 for length in blocks)
            check(l_hist[ell] == q ** ge_ell - q ** ge_next,
                  "A01 support histogram")
        nonzero_values = {fibres[y] for y in targets if any(y)}
        max_fibre = max(nonzero_values, default=1)
        longest = max(blocks)
        for y in targets:
            if any(y):
                only_longest = target_L(y, blocks) == longest
                check((fibres[y] == max_fibre) == only_longest,
                      "A01 extremizer iff longest-block support")
        check(len(states) - len(targets) == sum(1 for v in states if step(v) != v),
              "A01 spectral zero multiplicity")
        if len(set(blocks)) > 1:
            unequal_signatures.append((q, blocks, tuple(sorted(nonzero_values))))
        states_total += len(states)
    return (f"boxes={len(boxes)} states={states_total} "
            f"unequal={unequal_signatures}")


# A02: direct multiplication/conjugation in the dihedral presentation.


def dmul(x, y, n):
    k, e = x
    ell, f = y
    return ((k + (-ell if e else ell)) % n, e ^ f)


def dinv(x, n):
    for y in ((k, e) for e in (0, 1) for k in range(n)):
        if dmul(x, y, n) == (0, 0) and dmul(y, x, n) == (0, 0):
            return y
    raise AssertionError("missing dihedral inverse")


def dpow(x, exponent, n):
    out = (0, 0)
    base = x
    while exponent:
        if exponent & 1:
            out = dmul(out, base, n)
        base = dmul(base, base, n)
        exponent //= 2
    return out


def class_size(x, n):
    group = tuple((k, e) for e in (0, 1) for k in range(n))
    return len({dmul(dmul(g, x, n), dinv(g, n), n) for g in group})


def vtwo(k):
    if k == 0:
        return 10 ** 9
    answer = 0
    while k % 2 == 0:
        answer += 1
        k //= 2
    return answer


def euler_phi(n):
    return sum(gcd(k, n) == 1 for k in range(1, n + 1))


def ord_two(odd):
    if odd == 1:
        return 1
    x = 2 % odd
    order = 1
    while x != 1:
        x = 2 * x % odd
        order += 1
    return order


def divisors(n):
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def attack_a02():
    regimes = Counter()
    pure_power_depths = []
    for n in range(3, 25):
        group = tuple((k, e) for e in (0, 1) for k in range(n))
        step = lambda x, n=n: dpow(x, class_size(x, n), n)
        nxt = {x: step(x) for x in group}
        fibres = Counter(nxt.values())
        a = 0
        m = n
        while m % 2 == 0:
            a += 1
            m //= 2
        regime = "odd" if a == 0 else ("two_mod_four" if a == 1 else "four_divides")
        regimes[regime] += 1
        for k in range(n):
            x = (k, 0)
            expected = x if k == 0 or (n % 2 == 0 and k == n // 2) else (2 * k % n, 0)
            check(nxt[x] == expected, "A02 rotation branch")
        for k in range(n):
            x = (k, 1)
            expected = x if n % 4 else (0, 0)
            check(nxt[x] == expected, "A02 reflection branch")

        recurrent = set()
        cycles = set()
        max_tail = 0
        for x in group:
            tail, period, endpoint = orbit(step, x)
            max_tail = max(max_tail, tail)
            y = x
            for _ in range(tail):
                y = step(y)
            recurrent.add(y)
            cycle = []
            z = y
            for _ in range(period):
                cycle.append(z)
                z = step(z)
            cycles.add(tuple(sorted(cycle)))
            if x[1] == 0 and a >= 1 and x not in ((0, 0), (n // 2, 0)):
                k = x[0]
                if k % m:
                    predicted_tail = a - min(a, vtwo(k))
                else:
                    u = (k // m) % (1 << a)
                    predicted_tail = a - 1 - vtwo(u)
                check(tail == predicted_tail, "A02 two-adic rotation tail")
            if x[1] == 1:
                check(tail == (1 if a >= 2 else 0), "A02 reflection tail")

        predicted_recurrent = (2 * n if a == 0 else
                               m + 1 + (n if a == 1 else 0))
        check(len(recurrent) == predicted_recurrent, "A02 recurrent census")
        rotation_cycles = sum(euler_phi(d) // ord_two(d) for d in divisors(n if a == 0 else m))
        predicted_cycles = rotation_cycles + (0 if a == 0 else 1)
        if n % 4:
            predicted_cycles += n
        check(len(cycles) == predicted_cycles, "A02 cycle census")
        expected_image = 2 * n if a == 0 else (3 * n // 2 + 1 if a == 1 else n // 2)
        check(len(fibres) == expected_image, "A02 image size")

        exceptional = {0} if n % 2 else {0, n // 2}
        for target in group:
            predicted = set()
            if target[1] == 0:
                j = target[0]
                predicted |= {(k, 0) for k in range(n)
                              if k not in exceptional and 2 * k % n == j}
                if j == 0:
                    predicted.add((0, 0))
                if n % 2 == 0 and j == n // 2:
                    predicted.add((n // 2, 0))
                if n % 4 == 0 and j == 0:
                    predicted |= {(k, 1) for k in range(n)}
            elif n % 4:
                predicted.add(target)
            actual = {x for x in group if nxt[x] == target}
            check(actual == predicted, "A02 exact predecessor set")
        expected_max = 1 if a == 0 else (2 if a == 1 else n + 1)
        check(max(fibres.values()) == expected_max, "A02 sharp fibre cap")
        if m == 1:
            pure_power_depths.append((n, max_tail))

    # The stated n>=3 hypothesis is essential: D_4 at n=2 is the Klein group,
    # so the literal map is the identity and the n=2 mod 4 cap would be 1, not 2.
    n = 2
    group = tuple((k, e) for e in (0, 1) for k in range(n))
    step = lambda x: dpow(x, class_size(x, n), n)
    check(all(step(x) == x for x in group), "A02 excluded n=2 boundary")
    return (f"n=3..24 regimes={dict(sorted(regimes.items()))} "
            f"pure2={pure_power_depths} excluded_n2=identity_cap1")


# RC01: direct cyclic constraint propagation, not lane matrix multiplication.


def positive_difference(word):
    m = len(word)
    return tuple(max(word[i] - word[(i + 1) % m], 0) for i in range(m))


def local_cycle_count(target, cap):
    m = len(target)
    total = 0
    for first in range(cap + 1):
        paths = {first: 1}
        for b in target[:-1]:
            following = Counter()
            for left, count in paths.items():
                if b:
                    right = left - b
                    if right >= 0:
                        following[right] += count
                else:
                    for right in range(left, cap + 1):
                        following[right] += count
            paths = dict(following)
        for left, count in paths.items():
            if max(left - first, 0) == target[-1]:
                total += count
    return total


def fixed_support(word):
    m = len(word)
    return all(not (word[i] > 0 and word[(i + 1) % m] > 0) for i in range(m))


def attack_rc01():
    boxes = 0
    states_total = 0
    sharp = []
    for m in range(1, 7):
        for cap in range(0, 5):
            states = tuple(product(range(cap + 1), repeat=m))
            fibres = Counter(positive_difference(x) for x in states)
            maximum_tail = 0
            witness = states[0]
            for x in states:
                y = positive_difference(x)
                check((y == x) == fixed_support(x), "RC01 fixed support")
                tail, period, endpoint = orbit(positive_difference, x)
                check(period == 1 and positive_difference(endpoint) == endpoint,
                      "RC01 recurrence/fixed")
                bound = 0 if cap == 0 else (1 if m <= 2 else cap)
                check(tail <= bound, "RC01 clock bound")
                if tail > maximum_tail:
                    maximum_tail, witness = tail, x
                height = max(x)
                if height:
                    first = positive_difference(x)
                    for i, value in enumerate(first):
                        if value == height:
                            check(first[(i - 1) % m] == 0 and first[(i + 1) % m] == 0,
                                  "RC01 top layer isolation")
                            check(positive_difference(first)[i] == height,
                                  "RC01 top layer freezes")
            expected_sharp = 0 if cap == 0 else (1 if m <= 2 else cap)
            check(maximum_tail == expected_sharp, "RC01 sharp clock")
            for target in states:
                check(fibres.get(target, 0) == local_cycle_count(target, cap),
                      "RC01 cyclic local-constraint trace")
            fixed_count = sum(fixed_support(x) for x in states)
            support_weight_count = 0
            for support in product((0, 1), repeat=m):
                if all(not (support[i] and support[(i + 1) % m]) for i in range(m)):
                    support_weight_count += cap ** sum(support)
            check(fixed_count == support_weight_count, "RC01 weighted independent census")
            if cap and m in (1, 2, 3):
                sharp.append((m, cap, witness))
            boxes += 1
            states_total += len(states)

    # Two-prime factorization is checked on joint exponent words rather than
    # inferred from separate histograms.
    for m in (1, 2, 3):
        left_states = tuple(product(range(2), repeat=m))
        right_states = tuple(product(range(3), repeat=m))
        joint = Counter((positive_difference(x), positive_difference(y))
                        for x in left_states for y in right_states)
        lf = Counter(positive_difference(x) for x in left_states)
        rf = Counter(positive_difference(y) for y in right_states)
        for target, count in joint.items():
            check(count == lf[target[0]] * rf[target[1]], "RC01 prime fibre product")
    return f"boxes={boxes} states={states_total} sharp_m123={sharp}"


# RC03: frozensets on a one-based ordered ground set, no bit encoding.


def subsets(n):
    ground = tuple(range(1, n + 1))
    return tuple(frozenset(c) for r in range(n + 1) for c in combinations(ground, r))


def truncate(A):
    return frozenset(x for x in A if x <= len(A))


def initial_prefix(A, n):
    r = 0
    while r < n and r + 1 in A:
        r += 1
    return r


def attack_rc03():
    total = 0
    depth_signature = []
    for n in range(0, 12):
        states = subsets(n)
        fibres = Counter(truncate(A) for A in states)
        terminal = Counter()
        deepest = []
        max_tail = -1
        for A in states:
            tail, period, endpoint = orbit(truncate, A)
            rho = initial_prefix(A, n)
            check(period == 1, "RC03 recurrence is fixed")
            check(endpoint == frozenset(range(1, rho + 1)), "RC03 endpoint")
            k = len(A)
            current = A
            for t in range(1, n + 3):
                expected = frozenset(x for x in A if x <= k)
                current = truncate(current)
                check(current == expected, "RC03 closed iterate")
                k = len(expected)
            terminal[rho] += 1
            if tail > max_tail:
                max_tail, deepest = tail, [A]
            elif tail == max_tail:
                deepest.append(A)
            total += 1
        for B in states:
            b = len(B)
            M = max(B, default=0)
            lo = max(b, M)
            hi = (n + b) // 2
            predicted = sum(comb(n - k, k - b) for k in range(lo, hi + 1))
            check(fibres.get(B, 0) == predicted, "RC03 labelled target fibre")
            check((B in fibres) == (lo <= hi), "RC03 exact first image")
        for r in range(n + 1):
            predicted = 1 if r == n else 2 ** (n - r - 1)
            check(terminal[r] == predicted, "RC03 terminal fibre")
        check(sum(fibres.values()) == 2 ** n, "RC03 fibre normalization")
        if n >= 2:
            expected = frozenset(range(2, n + 1))
            check(max_tail == n - 1 and deepest == [expected],
                  "RC03 unique maximum tail")
        else:
            check(max_tail == 0 and len(deepest) == len(states), "RC03 n=0/1 boundary")
        check(fibres.get(frozenset(), 0) ==
              sum(comb(n - k, k) for k in range(0, n // 2 + 1)),
              "RC03 empty-target fibre")
        check(fibres.get(frozenset(range(1, n + 1)), 0) == 1,
              "RC03 full-target fibre")
        depth_signature.append((n, max_tail, len(deepest)))
    return f"n=0..11 states={total} depths={depth_signature}"


# RC05: regular left action on explicit Cayley tables, including nonnormal H.


def cyclic_table(n):
    return tuple(tuple((i + j) % n for j in range(n)) for i in range(n))


def permutation_table_three():
    elems = tuple(product(range(3), repeat=3))
    elems = tuple(p for p in elems if len(set(p)) == 3)
    index = {p: i for i, p in enumerate(elems)}
    return tuple(tuple(index[tuple(p[q[i]] for i in range(3))] for q in elems)
                 for p in elems)


def dihedral_table(n):
    elems = tuple((k, e) for e in (0, 1) for k in range(n))
    index = {x: i for i, x in enumerate(elems)}
    return tuple(tuple(index[dmul(x, y, n)] for y in elems) for x in elems)


def identity_of(table):
    size = len(table)
    return next(e for e in range(size)
                if all(table[e][x] == x and table[x][e] == x for x in range(size)))


def subgroup_sets(table):
    size = len(table)
    identity = identity_of(table)
    answer = []
    universe = range(size)
    for r in range(1, size + 1):
        for combo in combinations(universe, r):
            H = frozenset(combo)
            if identity in H and all(table[x][y] in H for x in H for y in H):
                answer.append(H)
    return tuple(answer)


def group_subsets(size):
    universe = tuple(range(size))
    return tuple(frozenset(c) for r in range(size + 1)
                 for c in combinations(universe, r))


def left_stabilizer_set(A, table):
    return frozenset(g for g in range(len(table))
                     if {table[g][x] for x in A} == set(A))


def poset_mu(H, K, subgroups):
    @lru_cache(maxsize=None)
    def mu(X, Y):
        X, Y = frozenset(X), frozenset(Y)
        if X == Y:
            return 1
        between = [L for L in subgroups if X <= L < Y]
        return -sum(mu(tuple(sorted(X)), tuple(sorted(L))) for L in between)
    return mu(tuple(sorted(H)), tuple(sorted(K)))


def attack_rc05():
    groups = (("C1", cyclic_table(1)), ("C4", cyclic_table(4)),
              ("S3", permutation_table_three()), ("D8", dihedral_table(4)))
    signatures = []
    nonnormal_witness = None
    for name, table in groups:
        size = len(table)
        states = group_subsets(size)
        subgroups = subgroup_sets(table)
        subgroup_set = set(subgroups)
        fibres = Counter(left_stabilizer_set(A, table) for A in states)
        for A in states:
            H = left_stabilizer_set(A, table)
            check(H in subgroup_set, "RC05 image subgroup")
            check(left_stabilizer_set(H, table) == H, "RC05 idempotence")
        check(fibres.get(frozenset(), 0) == 0, "RC05 empty target has no source")
        G = frozenset(range(size))
        check(fibres[G] == 2, "RC05 full target has empty/full sources")
        for H in subgroups:
            predicted = sum(poset_mu(H, K, subgroups) * 2 ** (size // len(K))
                            for K in subgroups if H <= K)
            check(fibres[H] == predicted, "RC05 subgroup-poset inversion")
            invariant = sum(1 for A in states
                            if all({table[h][x] for x in A} == set(A) for h in H))
            check(invariant == 2 ** (size // len(H)), "RC05 invariant subset count")
        check(sum(fibres.values()) == 2 ** size, "RC05 fibre partition")
        signatures.append((name, size, len(subgroups), max(fibres.values())))

        if name == "S3":
            identity = identity_of(table)
            inverses = {g: next(h for h in range(size)
                                if table[g][h] == identity and table[h][g] == identity)
                        for g in range(size)}
            for H in subgroups:
                normal = all({table[table[g][h]][inverses[g]] for h in H} == set(H)
                             for g in range(size))
                if len(H) == 2 and not normal:
                    right_cosets = [{table[h][a] for h in H} for a in range(size)]
                    left_cosets = [{table[a][h] for h in H} for a in range(size)]
                    A = next(frozenset(C) for C in right_cosets
                             if C not in left_cosets)
                    check(left_stabilizer_set(A, table) == H,
                          "RC05 nonnormal right-coset stabilizer")
                    check(set(A) not in left_cosets,
                          "RC05 left/right coset wording counterexample")
                    nonnormal_witness = (tuple(sorted(H)), tuple(sorted(A)))
                    break
    check(nonnormal_witness is not None, "RC05 nonnormal witness exists")
    return f"groups={signatures} S3_right_not_left={nonnormal_witness}"


def main():
    binding = bind_sources()
    rows = (
        ("A01", attack_a01()),
        ("A02", attack_a02()),
        ("RC01", attack_rc01()),
        ("RC03", attack_rc03()),
        ("RC05", attack_rc05()),
    )
    print("P187-P191 PRESELECTION HOSTILE AUDIT A")
    print("scope=finite_counterexample_pressure_not_proof_not_novelty_not_owner_clearance")
    print(f"source_bindings={len(SOURCE_BINDINGS)} aggregate_sha256={binding}")
    for candidate, result in rows:
        print(f"{candidate} PASS {result}")
    print(f"assertions={ASSERTIONS}")
    print("status=PASS_FINITE_CONTROLS_OWNER_AMBER_HOLD_EXTERNAL_UNNUMBERED")


if __name__ == "__main__":
    main()
