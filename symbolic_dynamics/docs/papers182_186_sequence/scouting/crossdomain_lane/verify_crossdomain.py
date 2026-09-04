#!/usr/bin/env python3
"""Exact, standard-library pilots for the P182--P186 cross-domain scout.

The program is deliberately exhaustive only on small carriers.  It writes no
files and emits a deterministic stdout transcript suitable for bytewise replay.
"""

from __future__ import annotations

from collections import Counter
from functools import lru_cache
from itertools import permutations, product
from math import factorial, gcd


class Audit:
    def __init__(self) -> None:
        self.assertions = 0

    def equal(self, left, right, label: str) -> None:
        self.assertions += 1
        if left != right:
            raise AssertionError(f"{label}: {left!r} != {right!r}")

    def true(self, condition: bool, label: str) -> None:
        self.assertions += 1
        if not condition:
            raise AssertionError(label)


AUDIT = Audit()


def stirling2(t: int, r: int) -> int:
    if t == 0:
        return int(r == 0)
    if r == 0:
        return 0
    table = [[0] * (r + 1) for _ in range(t + 1)]
    table[0][0] = 1
    for i in range(1, t + 1):
        for j in range(1, min(i, r) + 1):
            table[i][j] = table[i - 1][j - 1] + j * table[i - 1][j]
    return table[t][r]


def onto_words(t: int, r: int) -> int:
    return factorial(r) * stirling2(t, r)


# ---------------------------------------------------------------------------
# Pilot I: random incoming-copy symmetrization (RICS)


@lru_cache(maxsize=None)
def arcs(n: int) -> tuple[tuple[int, int], ...]:
    return tuple((i, j) for i in range(n) for j in range(n) if i != j)


@lru_cache(maxsize=None)
def arc_index(n: int) -> dict[tuple[int, int], int]:
    return {arc: k for k, arc in enumerate(arcs(n))}


def get_arc(state: int, n: int, i: int, j: int) -> int:
    return (state >> arc_index(n)[(i, j)]) & 1


def put_arc(state: int, n: int, i: int, j: int, value: int) -> int:
    bit = 1 << arc_index(n)[(i, j)]
    return (state | bit) if value else (state & ~bit)


def incoming_copy(state: int, n: int, v: int) -> int:
    out = state
    for u in range(n):
        if u != v:
            out = put_arc(out, n, v, u, get_arc(state, n, u, v))
    return out


def conflict_edges(state: int, n: int) -> frozenset[tuple[int, int]]:
    return frozenset(
        (i, j)
        for i in range(n)
        for j in range(i + 1, n)
        if get_arc(state, n, i, j) != get_arc(state, n, j, i)
    )


def conflict_representative(n: int, edges: frozenset[tuple[int, int]]) -> int:
    state = 0
    for i, j in edges:
        state = put_arc(state, n, i, j, 1)
    return state


def apply_vertex_word(state: int, n: int, word: tuple[int, ...]) -> int:
    for v in word:
        state = incoming_copy(state, n, v)
    return state


def independent_vertex_set(mask: int, edges: frozenset[tuple[int, int]]) -> bool:
    return all(not ((mask >> i) & 1 and (mask >> j) & 1) for i, j in edges)


def isolated_vertices(n: int, edges: frozenset[tuple[int, int]]) -> int:
    touched = {v for edge in edges for v in edge}
    return n - len(touched)


def order_endpoint(
    initial: int,
    n: int,
    edges: frozenset[tuple[int, int]],
    order: tuple[int, ...],
) -> int:
    """Closed endpoint from just the support's first-occurrence order."""
    rank = {v: k for k, v in enumerate(order)}
    out = initial
    infinity = n + 1
    for i, j in edges:
        ri, rj = rank.get(i, infinity), rank.get(j, infinity)
        if ri == rj == infinity:
            continue
        early, late = (i, j) if ri < rj else (j, i)
        value = get_arc(initial, n, late, early)
        out = put_arc(out, n, early, late, value)
        out = put_arc(out, n, late, early, value)
    return out


def verify_rics() -> list[str]:
    rows: list[str] = []
    for n in range(1, 5):
        state_count = 1 << (n * (n - 1))
        recurrent = 0
        labelled_in = Counter()
        source_sets: dict[int, set[int]] = {}
        for state in range(state_count):
            conflicts = conflict_edges(state, n)
            fixed = all(incoming_copy(state, n, v) == state for v in range(n))
            AUDIT.equal(fixed, not conflicts, f"RICS fixed criterion n={n} state={state}")
            recurrent += int(fixed)
            for v in range(n):
                target = incoming_copy(state, n, v)
                expected = frozenset(edge for edge in conflicts if v not in edge)
                AUDIT.equal(
                    conflict_edges(target, n),
                    expected,
                    f"RICS conflict deletion n={n} state={state} v={v}",
                )
                labelled_in[target] += 1
                source_sets.setdefault(target, set()).add(state)
        AUDIT.equal(recurrent, 1 << (n * (n - 1) // 2), f"RICS recurrent count n={n}")
        for target in range(state_count):
            k = isolated_vertices(n, conflict_edges(target, n))
            AUDIT.equal(
                labelled_in[target],
                k * (1 << (n - 1)),
                f"RICS labelled fibre n={n} target={target}",
            )
            AUDIT.equal(
                len(source_sets.get(target, set())),
                1 + k * ((1 << (n - 1)) - 1) if k else 0,
                f"RICS distinct fibre n={n} target={target}",
            )

        pair_edges = tuple((i, j) for i in range(n) for j in range(i + 1, n))
        endpoint_signal = 0
        complete = frozenset(pair_edges)
        complete_initial = conflict_representative(n, complete)
        for edge_mask in range(1 << len(pair_edges)):
            edges = frozenset(
                edge for k, edge in enumerate(pair_edges) if (edge_mask >> k) & 1
            )
            initial = conflict_representative(n, edges)
            for t in range(0, n + 1):
                literal = Counter()
                for word in product(range(n), repeat=t):
                    literal[apply_vertex_word(initial, n, word)] += 1
                by_order = Counter()
                for support_mask in range(1 << n):
                    support = tuple(v for v in range(n) if (support_mask >> v) & 1)
                    weight = stirling2(t, len(support))
                    if not weight:
                        continue
                    for order in permutations(support):
                        by_order[order_endpoint(initial, n, edges, order)] += weight
                AUDIT.equal(literal, by_order, f"RICS order kernel n={n} H={edge_mask} t={t}")
                absorbed = sum(count for state, count in literal.items() if not conflict_edges(state, n))
                predicted = sum(
                    onto_words(t, n - missing.bit_count())
                    for missing in range(1 << n)
                    if independent_vertex_set(missing, edges)
                )
                AUDIT.equal(absorbed, predicted, f"RICS absorption polynomial n={n} H={edge_mask} t={t}")
                if edges == complete and t == n:
                    endpoint_signal = len(literal)
        complete_absorbed = sum(
            1
            for word in product(range(n), repeat=n)
            if not conflict_edges(apply_vertex_word(complete_initial, n, word), n)
        )
        rows.append(
            "RICS "
            f"n={n} states={state_count} recurrent={recurrent} "
            f"max_distinct_fibre={1 + n * ((1 << (n - 1)) - 1)} "
            f"complete_H_absorbed_at_t=n={complete_absorbed} "
            f"complete_H_endpoint_support={endpoint_signal}"
        )
    return rows


# ---------------------------------------------------------------------------
# Pilot II: co-gcd translation (CGT)


def vp(x: int, p: int, a: int) -> int:
    if x == 0:
        return a
    value = 0
    while x % p == 0:
        x //= p
        value += 1
    return value


def cogcd_step(x: int, modulus: int) -> int:
    return (x + modulus // gcd(x, modulus)) % modulus


def orbit_tail_period(x: int, modulus: int) -> tuple[int, int]:
    first: dict[int, int] = {}
    time = 0
    while x not in first:
        first[x] = time
        x = cogcd_step(x, modulus)
        time += 1
    return first[x], time - first[x]


def predicted_tail_period(x: int, p: int, a: int) -> tuple[int, int]:
    value = vp(x, p, a)
    if 2 * value < a:
        return 0, p**value
    if 2 * value > a:
        return 1, p ** (a - value)
    h = a // 2
    unit = x // (p**h)
    run = p - (unit % p)
    landed_unit = unit + run
    extra = vp(landed_unit, p, h)
    return run + 1, p ** (h - extra)


def predicted_double_target(y: int, p: int, a: int) -> bool:
    if y == 1:
        return True
    value = vp(y, p, a)
    if 2 * value >= a:
        return False
    z = y // (p**value)
    scale = p ** (a - 2 * value)
    return (z - 1) % scale == 0 and ((z - 1) // scale) % p != 0


def verify_cgt() -> list[str]:
    rows: list[str] = []
    cases = (
        *((2, a) for a in range(1, 10)),
        *((3, a) for a in range(1, 8)),
        *((5, a) for a in range(1, 6)),
        *((7, a) for a in range(1, 5)),
    )
    for p, a in cases:
        modulus = p**a
        tails = Counter()
        periods = Counter()
        incoming = Counter()
        recurrent_states: set[int] = set()
        for x in range(modulus):
            actual = orbit_tail_period(x, modulus)
            expected = predicted_tail_period(x, p, a)
            AUDIT.equal(actual, expected, f"CGT orbit p={p} a={a} x={x}")
            tail, period = actual
            tails[tail] += 1
            periods[period] += 1
            if tail == 0:
                recurrent_states.add(x)
            incoming[cogcd_step(x, modulus)] += 1

        low_cut = (a - 1) // 2
        expected_recurrent = modulus - p ** (a // 2)
        AUDIT.equal(len(recurrent_states), expected_recurrent, f"CGT recurrent p={p} a={a}")
        expected_tails = Counter({0: expected_recurrent})
        if a % 2:
            expected_tails[1] = p ** (a // 2)
        else:
            h = a // 2
            expected_tails[1] = p ** (h - 1)
            for depth in range(2, p + 1):
                expected_tails[depth] = p ** (h - 1)
        AUDIT.equal(tails, expected_tails, f"CGT tail census p={p} a={a}")

        fibre_hist = Counter(incoming[y] for y in range(modulus))
        defect = p ** ((a - 1) // 2)
        AUDIT.equal(
            fibre_hist,
            Counter({1: modulus - 2 * defect, 0: defect, 2: defect}),
            f"CGT fibre histogram p={p} a={a}",
        )
        for y in range(modulus):
            AUDIT.true(incoming[y] <= 2, f"CGT fibre cap p={p} a={a} y={y}")
            AUDIT.equal(
                incoming[y] == 2,
                predicted_double_target(y, p, a),
                f"CGT double atlas p={p} a={a} y={y}",
            )

        unseen = set(recurrent_states)
        actual_cycles = Counter()
        while unseen:
            start = min(unseen)
            orbit: list[int] = []
            x = start
            while x not in orbit:
                orbit.append(x)
                x = cogcd_step(x, modulus)
            AUDIT.equal(x, start, f"CGT recurrent component p={p} a={a} start={start}")
            actual_cycles[len(orbit)] += 1
            unseen.difference_update(orbit)
        expected_cycles = Counter(
            {
                p**value: (p - 1) * p ** (a - 2 * value - 1)
                for value in range(low_cut + 1)
            }
        )
        AUDIT.equal(actual_cycles, expected_cycles, f"CGT cycle census p={p} a={a}")
        tail_text = ",".join(f"{depth}:{tails[depth]}" for depth in sorted(tails))
        cycle_text = ",".join(f"{length}:{actual_cycles[length]}" for length in sorted(actual_cycles))
        rows.append(
            "CGT "
            f"p={p} a={a} N={modulus} image={modulus - defect} "
            f"fibres_0_1_2={defect}/{modulus - 2 * defect}/{defect} "
            f"tails={tail_text} cycles={cycle_text}"
        )
    return rows


# ---------------------------------------------------------------------------
# Pilot III: random suffix-set compression (SSC)


def set_words(state: int):
    while state:
        low = state & -state
        yield low.bit_length() - 1
        state ^= low


def suffix_shift(state: int, d: int, bit: int) -> int:
    word_mask = (1 << d) - 1
    out = 0
    for word in set_words(state):
        image = ((word << 1) & word_mask) | bit
        out |= 1 << image
    return out


def apply_bit_history(state: int, d: int, history: int, t: int) -> int:
    for k in range(t - 1, -1, -1):
        state = suffix_shift(state, d, (history >> k) & 1)
    return state


def suffix_closed_form(state: int, d: int, history: int, t: int) -> int:
    if t >= d:
        return 1 << (history & ((1 << d) - 1))
    suffix_mask = (1 << (d - t)) - 1
    out = 0
    for word in set_words(state):
        out |= 1 << (((word & suffix_mask) << t) | history)
    return out


def common_suffix_length(state: int, d: int) -> int:
    length = 0
    words = tuple(set_words(state))
    for trial in range(1, d + 1):
        mask = (1 << trial) - 1
        if len({word & mask for word in words}) == 1:
            length = trial
        else:
            break
    return length


def verify_ssc() -> list[str]:
    rows: list[str] = []
    for d in range(1, 5):
        alphabet = 1 << d
        carrier = (1 << alphabet) - 1
        shells = Counter()
        incoming = Counter()
        image = set()
        for state in range(1, carrier + 1):
            predicted_depth = d - common_suffix_length(state, d)
            zero_state = state
            literal_depth = 0
            while zero_state.bit_count() > 1:
                zero_state = suffix_shift(zero_state, d, 0)
                literal_depth += 1
            AUDIT.equal(literal_depth, predicted_depth, f"SSC depth d={d} state={state}")
            shells[predicted_depth] += 1
            for bit in (0, 1):
                target = suffix_shift(state, d, bit)
                incoming[target] += 1
                image.add(target)
        cumulative_previous = 0
        expected_shells = Counter()
        for depth in range(d + 1):
            cumulative = (1 << (d - depth)) * ((1 << (1 << depth)) - 1)
            expected_shells[depth] = cumulative - cumulative_previous
            cumulative_previous = cumulative
        AUDIT.equal(shells, expected_shells, f"SSC shell census d={d}")
        AUDIT.equal(
            len(image),
            2 * ((1 << (1 << (d - 1))) - 1),
            f"SSC one-step image d={d}",
        )
        for target in range(1, carrier + 1):
            last_bits = {word & 1 for word in set_words(target)}
            expected = 3 ** target.bit_count() if len(last_bits) == 1 else 0
            AUDIT.equal(incoming[target], expected, f"SSC one-step fibre d={d} target={target}")

        if d <= 3:
            for t in range(0, d + 3):
                labelled_in = Counter()
                for state in range(1, carrier + 1):
                    for history in range(1 << t):
                        literal = apply_bit_history(state, d, history, t)
                        closed = suffix_closed_form(state, d, history, t)
                        AUDIT.equal(literal, closed, f"SSC closed image d={d} t={t} state={state} h={history}")
                        labelled_in[literal] += 1
                for target in range(1, carrier + 1):
                    if t <= d:
                        residues = {word & ((1 << t) - 1) for word in set_words(target)}
                        expected = (
                            ((1 << (1 << t)) - 1) ** target.bit_count()
                            if len(residues) == 1
                            else 0
                        )
                    else:
                        expected = carrier * (1 << (t - d)) if target.bit_count() == 1 else 0
                    AUDIT.equal(
                        labelled_in[target],
                        expected,
                        f"SSC time-t fibre d={d} t={t} target={target}",
                    )
            for singleton in (1 << word for word in range(alphabet)):
                endpoints = Counter(
                    apply_bit_history(singleton, d, history, d)
                    for history in range(1 << d)
                )
                AUDIT.equal(
                    endpoints,
                    Counter({1 << word: 1 for word in range(alphabet)}),
                    f"SSC recurrent de Bruijn mixing d={d} singleton={singleton}",
                )
        shell_text = ",".join(f"{depth}:{shells[depth]}" for depth in range(d + 1))
        rows.append(
            "SSC "
            f"d={d} states={carrier} recurrent={alphabet} shells={shell_text} "
            f"one_step_image={len(image)} max_one_step_fibre={3 ** (1 << (d - 1))}"
        )
    return rows


def main() -> None:
    print("P182_186_CROSSDOMAIN_BREADTH")
    for row in verify_rics():
        print(row)
    for row in verify_cgt():
        print(row)
    for row in verify_ssc():
        print(row)
    print("SYSTEMS_SCOUTED=16")
    print("PILOTS=3")
    print(f"ASSERTIONS={AUDIT.assertions}")
    print("OWNER_STATUS=BOUNDED_NONHIT_NOT_NOVELTY;HOLD_EXTERNAL")
    print("RESULT=PASS")


if __name__ == "__main__":
    main()
