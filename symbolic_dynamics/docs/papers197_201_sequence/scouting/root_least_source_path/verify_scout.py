#!/usr/bin/env python3
"""Exact falsification controls for least-source path orientations."""

from collections import Counter


ASSERTIONS = 0


def check(condition, message="assertion failed"):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def step(mask, m):
    if m == 0:
        return 0
    if mask == 0:
        return 1 << (m - 1)
    low = mask & -mask
    i = low.bit_length() - 1
    if i == 0:
        return mask ^ 1
    return mask ^ (1 << i) ^ (1 << (i - 1))


def iterate(mask, m, t):
    for _ in range(t):
        mask = step(mask, m)
    return mask


def sites(mask, m):
    return [i + 1 for i in range(m) if (mask >> i) & 1]


def predicted_tail(mask, m):
    a = sites(mask, m)
    return sum(a[:-1]) if len(a) >= 2 else 0


def subset_sum_counts(s):
    out = [1]
    for i in range(1, s + 1):
        out += [0] * i
        for e in range(len(out) - 1, i - 1, -1):
            out[e] += out[e - i]
    return out


def q(qcache, s, e):
    if e < 0 or e >= len(qcache[s]):
        return 0
    return qcache[s][e]


def transient_fibre_formula(target, m, t, qcache):
    b = sites(target, m)
    check(len(b) >= 2)
    return sum(q(qcache, b[0] + r - 1, t - r)
               for r in range(b[1] - b[0]))


def core_index(mask):
    if mask == 0:
        return 0
    check(mask & (mask - 1) == 0)
    return mask.bit_length()


def core_fibre_formula(target, m, t, qcache):
    n = m + 1
    s = core_index(target)
    ans = 1
    for r in range(1, m + 1):
        for e in range(1, t + 1):
            if (s - (r + e - t)) % n == 0:
                ans += q(qcache, r - 1, e)
    return ans


def run():
    terminal_rows = []
    for n in range(1, 19):
        m = n - 1
        size = 1 << m
        qcache = [subset_sum_counts(s) for s in range(m + 1)]
        nexts = [step(x, m) for x in range(size)]

        # Literal least-source rule versus particle normal form.
        for mask in range(size):
            if m == 0:
                literal = 0
            else:
                b = [(mask >> i) & 1 for i in range(m)]
                source = None
                for v in range(n):
                    left_in = v > 0 and b[v - 1] == 1
                    right_in = v < m and b[v] == 0
                    if not left_in and not right_in:
                        source = v
                        break
                check(source is not None)
                literal = mask
                if source > 0:
                    literal ^= 1 << (source - 1)
                if source < m:
                    literal ^= 1 << source
            check(literal == nexts[mask], (n, mask, literal, nexts[mask]))

        core = {0} | {1 << i for i in range(m)}
        check(len(core) == n)
        if n == 1:
            check(nexts[0] == 0)
        else:
            cycle = []
            x = 0
            while x not in cycle:
                cycle.append(x)
                x = nexts[x]
            check(x == 0 and set(cycle) == core and len(cycle) == n)

        depth_hist = Counter()
        actual_tails = []
        for mask in range(size):
            t = predicted_tail(mask, m)
            if mask in core:
                check(t == 0)
            else:
                check(predicted_tail(nexts[mask], m) == t - 1,
                      (n, mask, t, nexts[mask]))
            actual_tails.append(t)
            depth_hist[t] += 1

            a = sites(mask, m)
            if n <= 12 and len(a) >= 2:
                prefix = 0
                for j in range(len(a) - 1):
                    for tt in range(prefix, prefix + a[j]):
                        expected = [a[j] - (tt - prefix)] + a[j + 1:]
                        got = sites(iterate(mask, m, tt), m)
                        check(got == expected, (n, mask, tt, got, expected))
                    prefix += a[j]

        expected_hist = Counter({0: 1})
        for r in range(1, m + 1):
            for e, count in enumerate(qcache[r - 1]):
                expected_hist[e] += count
        check(depth_hist == expected_hist, (n, depth_hist, expected_hist))
        expected_max = m * (m - 1) // 2
        check(max(actual_tails) == expected_max)
        if m >= 2:
            check(sum(t == expected_max for t in actual_tails) == 1)
        else:
            check(sum(t == expected_max for t in actual_tails) == size)

        fibres = Counter(nexts)
        if m >= 2:
            hist = Counter(fibres.get(y, 0) for y in range(size))
            check(hist == Counter({0: 1 << (m - 2),
                                   1: 1 << (m - 1),
                                   2: 1 << (m - 2)}), (n, hist))
            check(len(fibres) == 3 * (1 << (m - 2)))
            for y in range(size):
                nonimage = (y & 3) == 3
                check((fibres.get(y, 0) == 0) == nonimage)
        else:
            check(all(fibres[y] == 1 for y in range(size)))

        # Every-time inverse atlas in boxes whose complete time scan is cheap.
        if n <= 11:
            horizon = expected_max + 2 * n
            powers = list(range(size))
            for t in range(horizon + 1):
                direct = Counter(powers)
                for target in range(size):
                    if target in core:
                        predicted = core_fibre_formula(target, m, t, qcache)
                    else:
                        predicted = transient_fibre_formula(target, m, t, qcache)
                    check(direct.get(target, 0) == predicted,
                          (n, t, target, direct.get(target, 0), predicted))
                powers = [nexts[x] for x in powers]

        # Fixed iterates: one n-cycle and no transient periodic point.
        if n <= 12:
            powers = list(range(size))
            for t in range(1, 2 * n + 1):
                powers = [nexts[x] for x in powers]
                count = sum(y == x for x, y in enumerate(powers))
                check(count == (n if t % n == 0 else 0), (n, t, count))

        if n >= 14:
            terminal_rows.append((n, size, len(fibres), expected_max,
                                  max(fibres.values())))

    print("LEAST_SOURCE_PATH_OK")
    print(f"assertions={ASSERTIONS}")
    print("scope=all_path_orientations_n_1_through_18")
    print("every_time_fibres=complete_n_1_through_11")
    for n, states, image, tail, fibre in terminal_rows:
        print(f"n={n} states={states} image={image} max_tail={tail} max_fibre={fibre}")
    print("recurrent_core=single_n_cycle")
    print("tail=sum_of_all_particle_sites_except_rightmost")
    print("depth_polynomial=1_plus_sum_prefix_subset_products")
    print("one_step_fibre_histogram=quarter_half_quarter")
    print("external_status=HOLD_EXTERNAL")


if __name__ == "__main__":
    run()
