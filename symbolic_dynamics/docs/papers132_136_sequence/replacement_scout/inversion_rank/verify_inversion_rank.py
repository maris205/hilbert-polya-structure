#!/usr/bin/env python3
"""Deterministic exact pilot for the inversion-rank replacement lane.

All carriers are the inversion-sequence boxes

    E_n = {e=(e_0,...,e_{n-1}) : 0 <= e_i <= i}.

There is no randomness and there are no third-party dependencies.  The main
candidate was S01, subsequently killed by the exact direct owner
arXiv:2608.24476v1.  S07 is retained only as a stated ascent/descent symmetry
control, and S16 is retained only to expose that the apparently different
Lehmer conversion S14 is exactly reverse-complement after decoding.  Neither
control is counted toward the distinct-system audit.
"""

from __future__ import annotations

from hashlib import sha256
from itertools import combinations, product
from math import comb
from typing import Callable, Iterable, Iterator

State = tuple[int, ...]
Map = Callable[[State], State]


ASSERTIONS = 0


def check(condition: bool, message: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def inversion_sequences(n: int) -> Iterator[State]:
    return product(*(range(i + 1) for i in range(n)))


def valid(e: State) -> bool:
    return all(0 <= x <= i for i, x in enumerate(e))


# ---------------------------------------------------------------------------
# Twenty-three literal maps.  Twenty-one are counted as genuinely distinct;
# S07 and S16 are explicit controls and are not counted.


def s01_strict_lower_rank(e: State) -> State:
    return tuple(sum(e[j] < e[i] for j in range(i)) for i in range(len(e)))


def s02_first_occurrence_position(e: State) -> State:
    return tuple(next(j for j in range(i + 1) if e[j] == e[i]) for i in range(len(e)))


def s03_first_appearance_rgf(e: State) -> State:
    labels: dict[int, int] = {}
    out: list[int] = []
    for x in e:
        if x not in labels:
            labels[x] = len(labels)
        out.append(labels[x])
    return tuple(out)


def s04_prior_occurrence_count(e: State) -> State:
    return tuple(sum(e[j] == e[i] for j in range(i)) for i in range(len(e)))


def s05_distinct_lower_rank(e: State) -> State:
    return tuple(len({e[j] for j in range(i) if e[j] < e[i]}) for i in range(len(e)))


def s06_prefix_descent_count(e: State) -> State:
    return tuple(sum(e[j - 1] > e[j] for j in range(1, i + 1)) for i in range(len(e)))


def s07_prefix_ascent_count_control(e: State) -> State:
    return tuple(sum(e[j - 1] < e[j] for j in range(1, i + 1)) for i in range(len(e)))


def s08_prefix_strict_record_count(e: State) -> State:
    out = [0]
    records = 0
    maximum = e[0]
    for x in e[1:]:
        if x > maximum:
            records += 1
            maximum = x
        out.append(records)
    return tuple(out)


def s09_prefix_distinct_minus_one(e: State) -> State:
    seen: set[int] = set()
    out: list[int] = []
    for x in e:
        seen.add(x)
        out.append(len(seen) - 1)
    return tuple(out)


def parent_root(e: State, i: int) -> int:
    while e[i] < i:
        i = e[i]
    return i


def s10_parent_root_label(e: State) -> State:
    return tuple(parent_root(e, i) for i in range(len(e)))


def s11_parent_depth(e: State) -> State:
    out: list[int] = []
    for i in range(len(e)):
        depth = 0
        while e[i] < i:
            i = e[i]
            depth += 1
        out.append(depth)
    return tuple(out)


def s12_grandparent_jump(e: State) -> State:
    return tuple(e[e[i]] for i in range(len(e)))


def s13_component_prior_count(e: State) -> State:
    roots = tuple(parent_root(e, i) for i in range(len(e)))
    return tuple(sum(roots[j] == roots[i] for j in range(i)) for i in range(len(e)))


def inversion_to_permutation(e: State) -> State:
    """Decode e_i=#{j<i:p_j>p_i}; permutation values are zero based."""
    available = list(range(len(e)))
    p = [0] * len(e)
    for i in range(len(e) - 1, -1, -1):
        p[i] = available.pop(len(available) - 1 - e[i])
    return tuple(p)


def permutation_to_inversion(p: State) -> State:
    return tuple(sum(p[j] > p[i] for j in range(i)) for i in range(len(p)))


def s14_reversed_right_lehmer(e: State) -> State:
    p = inversion_to_permutation(e)
    right_lehmer = tuple(sum(p[j] < p[i] for j in range(i + 1, len(p))) for i in range(len(p)))
    return tuple(reversed(right_lehmer))


def s15_inverse_permutation_code(e: State) -> State:
    p = inversion_to_permutation(e)
    inv = [0] * len(p)
    for i, x in enumerate(p):
        inv[x] = i
    return permutation_to_inversion(tuple(inv))


def s16_reverse_complement_control(e: State) -> State:
    p = inversion_to_permutation(e)
    n = len(p)
    rc = tuple(n - 1 - x for x in reversed(p))
    return permutation_to_inversion(rc)


def s17_permutation_square_code(e: State) -> State:
    p = inversion_to_permutation(e)
    return permutation_to_inversion(tuple(p[p[i]] for i in range(len(p))))


def stack_sort_permutation(p: State) -> State:
    stack: list[int] = []
    out: list[int] = []
    for x in p:
        while stack and stack[-1] < x:
            out.append(stack.pop())
        stack.append(x)
    out.extend(reversed(stack))
    return tuple(out)


def s18_stack_sort_code(e: State) -> State:
    return permutation_to_inversion(stack_sort_permutation(inversion_to_permutation(e)))


def pop_stack_sort_permutation(p: State) -> State:
    out: list[int] = []
    start = 0
    for i in range(1, len(p) + 1):
        if i == len(p) or p[i - 1] < p[i]:
            out.extend(reversed(p[start:i]))
            start = i
    return tuple(out)


def s19_pop_stack_sort_code(e: State) -> State:
    return permutation_to_inversion(pop_stack_sort_permutation(inversion_to_permutation(e)))


def s20_lis_ending_layer(e: State) -> State:
    p = inversion_to_permutation(e)
    layers: list[int] = []
    for i, x in enumerate(p):
        layers.append(max((layers[j] + 1 for j in range(i) if p[j] < x), default=0))
    return tuple(layers)


def s21_previous_occurrence_index(e: State) -> State:
    out: list[int] = []
    for i, x in enumerate(e):
        earlier = [j for j in range(i) if e[j] == x]
        out.append(earlier[-1] if earlier else 0)
    return tuple(out)


def s22_recency_gap_minus_one(e: State) -> State:
    out: list[int] = []
    for i, x in enumerate(e):
        earlier = [j for j in range(i) if e[j] == x]
        out.append(i - earlier[-1] - 1 if earlier else 0)
    return tuple(out)


def s23_prior_prefix_mex(e: State) -> State:
    out: list[int] = []
    seen: set[int] = set()
    for x in e:
        mex = 0
        while mex in seen:
            mex += 1
        out.append(mex)
        seen.add(x)
    return tuple(out)


SYSTEMS: tuple[tuple[str, str, Map, bool], ...] = (
    ("S01", "strict lower rank (PR1)", s01_strict_lower_rank, True),
    ("S02", "first-occurrence position", s02_first_occurrence_position, True),
    ("S03", "first-appearance RGF", s03_first_appearance_rgf, True),
    ("S04", "prior occurrence count", s04_prior_occurrence_count, True),
    ("S05", "distinct strict-lower rank", s05_distinct_lower_rank, True),
    ("S06", "prefix descent count", s06_prefix_descent_count, True),
    ("S07", "prefix ascent count (dual control)", s07_prefix_ascent_count_control, False),
    ("S08", "prefix strict-record count", s08_prefix_strict_record_count, True),
    ("S09", "prefix distinct count minus one", s09_prefix_distinct_minus_one, True),
    ("S10", "parent-root label", s10_parent_root_label, True),
    ("S11", "parent depth", s11_parent_depth, True),
    ("S12", "grandparent jump", s12_grandparent_jump, True),
    ("S13", "component prior count", s13_component_prior_count, True),
    ("S14", "reversed right-Lehmer conversion", s14_reversed_right_lehmer, True),
    ("S15", "inverse-permutation re-encoding", s15_inverse_permutation_code, True),
    ("S16", "reverse-complement (duplicate control)", s16_reverse_complement_control, False),
    ("S17", "permutation-square re-encoding", s17_permutation_square_code, True),
    ("S18", "stack-sort re-encoding", s18_stack_sort_code, True),
    ("S19", "pop-stack re-encoding", s19_pop_stack_sort_code, True),
    ("S20", "LIS-ending layer code", s20_lis_ending_layer, True),
    ("S21", "previous-occurrence index", s21_previous_occurrence_index, True),
    ("S22", "recency gap minus one", s22_recency_gap_minus_one, True),
    ("S23", "prior-prefix mex", s23_prior_prefix_mex, True),
)


# ---------------------------------------------------------------------------
# Exact finite dynamics and independent noncrossing-partition recognizer.


def orbit_profile(start: State, update: Map) -> tuple[int, int, tuple[State, ...]]:
    seen: dict[State, int] = {}
    orbit: list[State] = []
    x = start
    while x not in seen:
        seen[x] = len(orbit)
        orbit.append(x)
        x = update(x)
    mu = seen[x]
    return mu, len(orbit) - mu, tuple(orbit)


def census(n: int, update: Map) -> tuple[int, int, int, int, int]:
    states = tuple(inversion_sequences(n))
    images = {update(e) for e in states}
    fixed = sum(update(e) == e for e in states)
    profiles = [orbit_profile(e, update)[:2] for e in states]
    return len(states), len(images), fixed, max(mu for mu, _ in profiles), max(lam for _, lam in profiles)


def catalan(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


def is_noncrossing_min_code(code: State) -> bool:
    for label in set(code):
        positions = [i for i, x in enumerate(code) if x == label]
        if min(positions) != label:
            return False
    for a, b, c, d in combinations(range(len(code)), 4):
        if code[a] == code[c] and code[b] == code[d] and code[a] != code[b]:
            return False
    return True


def restricted_growth_words(n: int) -> Iterator[State]:
    if n == 0:
        yield ()
        return

    word = [0]

    def extend() -> Iterator[State]:
        if len(word) == n:
            yield tuple(word)
            return
        for x in range(max(word) + 2):
            word.append(x)
            yield from extend()
            word.pop()

    yield from extend()


def rgf_to_min_code(rgf: State) -> State:
    first: dict[int, int] = {}
    for i, x in enumerate(rgf):
        first.setdefault(x, i)
    return tuple(first[x] for x in rgf)


def is_ordinary_ascent_sequence(a: State) -> bool:
    if not a or a[0] != 0:
        return False
    for i in range(1, len(a)):
        ascents = sum(a[j] < a[j + 1] for j in range(i - 1))
        if not (0 <= a[i] <= 1 + ascents):
            return False
    return True


PR1_EXPECTED = {
    1: (1, 1, 1, 0, 1),
    2: (2, 2, 2, 0, 1),
    3: (6, 5, 5, 1, 1),
    4: (24, 15, 14, 2, 1),
    5: (120, 53, 42, 3, 1),
    6: (720, 217, 132, 4, 1),
    7: (5040, 1014, 429, 5, 1),
    8: (40320, 5335, 1430, 6, 1),
}

AUDIT_SHA256 = "fc2320357944180847fe4c8c2a34b475f93d27b0c9aa4c4fd87f78fc7acd829a"


def verify_pr1() -> None:
    fishburn = (1, 2, 5, 15, 53, 217, 1014, 5335)
    for n in range(1, 9):
        states = tuple(inversion_sequences(n))
        observed = census(n, s01_strict_lower_rank)
        check(observed == PR1_EXPECTED[n], f"S01 frozen census failed at n={n}: {observed}")
        check(observed[1] == fishburn[n - 1], f"S01 image/Fishburn finite match failed at n={n}")
        check(observed[2] == catalan(n), f"S01 fixed/Catalan count failed at n={n}")

        fixed = {e for e in states if s01_strict_lower_rank(e) == e}
        nc_from_partitions = {
            code
            for rgf in restricted_growth_words(n)
            for code in (rgf_to_min_code(rgf),)
            if is_noncrossing_min_code(code)
        }
        check(fixed == nc_from_partitions, f"S01 fixed points != NC minimum-block codes at n={n}")

        for e in states:
            nxt = s01_strict_lower_rank(e)
            check(valid(nxt), f"S01 left E_{n}: {e} -> {nxt}")
            check(all(x <= y for x, y in zip(e, nxt)), f"S01 inflation failed: {e} -> {nxt}")
            mu, period, orbit = orbit_profile(e, s01_strict_lower_rank)
            check(period == 1, f"S01 nontrivial cycle from {e}")
            check(mu <= max(0, n - 2), f"S01 depth bound failed from {e}: {mu}")
            terminal = orbit[-1]
            check(is_noncrossing_min_code(terminal), f"S01 terminal not NC code: {terminal}")
            # Once a coordinate pauses, the no-pause lemma says it is frozen.
            for t in range(len(orbit) - 1):
                for i in range(n):
                    if orbit[t][i] == orbit[t + 1][i]:
                        check(
                            all(orbit[u][i] == orbit[t][i] for u in range(t + 1, len(orbit))),
                            f"S01 coordinate resumed after pausing: {e}, i={i}, t={t}",
                        )

    for n in range(2, 13):
        witness = tuple(range(n - 2)) + (0, 1)
        mu, period, orbit = orbit_profile(witness, s01_strict_lower_rank)
        check(mu == n - 2 and period == 1, f"S01 sharp witness failed at n={n}")
        check(tuple(x[-1] for x in orbit) == tuple(range(1, n)), f"S01 witness trajectory failed at n={n}")

    counterexample = (0, 0, 1)
    image = s01_strict_lower_rank(counterexample)
    check(image == (0, 0, 2), "S01 ascent-sequence counterexample changed")
    check(not is_ordinary_ascent_sequence(image), "S01 image is not the ordinary ascent-sequence class")


def verify_audit() -> dict[str, tuple[tuple[int, int, int, int, int], ...]]:
    check(sum(counted for _, _, _, counted in SYSTEMS) == 21, "distinct audit count changed")
    snapshots: dict[str, tuple[tuple[int, int, int, int, int], ...]] = {}
    truth_tables: dict[str, tuple[State, ...]] = {}
    carrier6 = tuple(inversion_sequences(6))

    for sid, _, update, counted in SYSTEMS:
        rows = tuple(census(n, update) for n in range(1, 8))
        snapshots[sid] = rows
        for n in range(1, 8):
            for e in inversion_sequences(n):
                check(valid(update(e)), f"{sid} left E_{n}: {e} -> {update(e)}")
        if counted:
            truth_tables[sid] = tuple(update(e) for e in carrier6)

    ids = sorted(truth_tables)
    for i, sid in enumerate(ids):
        for other in ids[i + 1 :]:
            check(truth_tables[sid] != truth_tables[other], f"counted maps {sid} and {other} coincide on E_6")

    check(
        all(s14_reversed_right_lehmer(e) == s16_reverse_complement_control(e) for e in carrier6),
        "S14/S16 duplicate-control identity failed",
    )
    payload = "\n".join(
        f"{sid}:" + ";".join(",".join(map(str, row)) for row in snapshots[sid])
        for sid, _, _, _ in SYSTEMS
    )
    check(sha256(payload.encode()).hexdigest() == AUDIT_SHA256, "full audit census digest changed")
    return snapshots


def format_row(row: tuple[int, int, int, int, int]) -> str:
    return "/".join(map(str, row))


def main() -> None:
    verify_pr1()
    snapshots = verify_audit()

    print("PR1 columns=states/image/fixed/max_tail/max_period")
    print("PR1 " + " ".join(f"n={n}:{format_row(PR1_EXPECTED[n])}" for n in range(1, 9)))
    print("PR1 sharp_tail=n-2 verified_n=2..12")
    print("PR1 fixed=noncrossing_minimum_block_codes verified_n=1..8")
    print("PR1 image_counts=1,2,5,15,53,217,1014,5335 (finite Fishburn match only)")
    print("PR1 image_not_ordinary_ascent witness=(0,0,1)->(0,0,2)")
    print("VERDICT S01=KILL direct_owner=arXiv:2608.24476v1 promotions=0")
    print("AUDIT counted_distinct=21 controls=S07,S16 census_n=1..7")
    print(f"AUDIT sha256={AUDIT_SHA256}")
    for sid, _, _, _ in SYSTEMS:
        print(f"{sid} " + " ".join(format_row(row) for row in snapshots[sid]))
    print(f"ASSERTIONS {ASSERTIONS}")
    print("OK")


if __name__ == "__main__":
    main()
