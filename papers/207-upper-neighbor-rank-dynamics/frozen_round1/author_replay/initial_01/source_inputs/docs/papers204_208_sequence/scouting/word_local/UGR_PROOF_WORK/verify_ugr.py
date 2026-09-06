#!/usr/bin/env python3
"""UGR author proof certificate, using edges rather than the pilot's rank code.

No input file reads, imports of repository code, or larger cyclic atlas.
The factored local proof covers every thirteen-letter initial word. Core
classification and generating functions are checked in local/role form.
"""
from collections import Counter
from hashlib import sha256
from itertools import permutations, product
import json


ASSERTIONS = 0
DIGEST = sha256()
ROLES = ("S0", "S1", "W0L", "W0R", "W1L", "W1R", "N01", "N10")
EMIT = (0, 2, 0, 0, 1, 1, 1, 1)
FLIP = (1, 0, 4, 5, 2, 3, 7, 6)
NEXT = ((1, 4, 6), (0, 2, 7), (3,), (1, 4), (5,), (0, 2), (1,), (0,))
Q = tuple(tuple(int(j in NEXT[i]) for j in range(8)) for i in range(8))


def check(condition, detail):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(detail)


def record(obj):
    DIGEST.update(json.dumps(obj, separators=(",", ":")).encode())
    DIGEST.update(b"\n")


def edges(row):
    return tuple((b > a) - (b < a) for a, b in zip(row, row[1:]))


def advance(row):
    signs = edges(row)
    return tuple(int(signs[i - 1] < 0) + int(signs[i] > 0)
                 for i in range(1, len(row) - 1))


def extreme_sites(row):
    signs = edges(row)
    offset = len(row) // 2
    return {i - offset for i in range(1, len(row) - 1)
            if signs[i - 1] * signs[i] == -1}


def cone(row):
    rows = [row]
    for _ in range(4):
        rows.append(advance(rows[-1]))
    original = extreme_sites(row)
    events = [(s, j) for s in range(1, 5)
              for j in sorted(extreme_sites(rows[s]) - original)]
    changed = rows[4][len(rows[4]) // 2] != rows[2][len(rows[2]) // 2]
    return rows, events, changed


def check_witness(rows, event):
    s, j = event
    first, last = rows[0], rows[s]
    i0, is_ = len(first) // 2 + j, len(last) // 2 + j
    a, b, c = first[i0 - 1:i0 + 2]
    was_extreme = b < min(a, c) or b > max(a, c)
    a, b, c = last[is_ - 1:is_ + 2]
    is_extreme = b < min(a, c) or b > max(a, c)
    check(not was_extreme and is_extreme, ("literal witness", rows[0], event))


def local_certificate():
    for triple in product(range(3), repeat=3):
        a, b, c = triple
        check(advance(triple) == (int(a > b) + int(c > b),), ("literal edge factor", triple))
    extreme_cases = 0
    for row in product(range(3), repeat=5):
        if 0 in extreme_sites(row):
            extreme_cases += 1
            nxt = advance(row)
            check(0 in extreme_sites(nxt), ("extremum permanence", row))
            old_min = row[2] < min(row[1], row[3])
            check(nxt[1] == (2 if old_min else 0), ("extremum flips type", row))
    classes = Counter()
    events_census = Counter()
    exceptions = []
    for inner in product(range(3), repeat=11):
        rows, events, changed = cone(inner)
        if not changed:
            classes["center_equal"] += 1
            record(("inner_equal", inner))
        elif events:
            classes["inner_witness"] += 1
            chosen = events[0]
            check_witness(rows, chosen)
            events_census[chosen] += 1
            record(("inner_witness", inner, chosen))
        else:
            classes["needs_outer_letters"] += 1
            nine = []
            for a, b in product(range(3), repeat=2):
                outer = (a,) + inner + (b,)
                full_rows, full_events, full_changed = cone(outer)
                check(full_changed, ("extension preserves changed center", inner, a, b))
                check(bool(full_events), ("four-step growth certificate", outer))
                chosen = full_events[0]
                check_witness(full_rows, chosen)
                events_census[chosen] += 1
                nine.append([a, b, *chosen])
                record(("outer_witness", outer, chosen))
            exceptions.append({"inner_word": inner, "all_nine_extensions_a_b_time_site": nine})
    check(sum(classes.values()) == 3 ** 11, "all inner windows covered")
    check(len(exceptions) == 204, "independent reproduction of exception count")
    return {"alphabet": [0, 1, 2], "initial_radius": 6, "updates": 4,
            "strict_extremum_local_cases": extreme_cases,
            "inner_words_checked": 3 ** 11, "inner_case_counts": dict(classes),
            "explicit_outer_extensions": 9 * len(exceptions),
            "thirteen_letter_words_covered_by_extension_argument": 3 ** 13,
            "first_witness_census": [list(k) + [v] for k, v in sorted(events_census.items())],
            "complete_inner_exception_and_extension_certificate": exceptions}


def literal_triple(a, b, c):
    return int(a > b) + int(c > b)


def classified_column_triplet(left, center, right):
    s0, s1, w0, w1, neutral = (0, 2), (2, 0), (0, 1), (1, 0), (1, 1)
    if center == s0:
        return left in (s1, w1, neutral) and right in (s1, w1, neutral)
    if center == s1:
        return left in (s0, w0, neutral) and right in (s0, w0, neutral)
    if center == w0:
        return ((left == w0 and right in (w1, s1))
                or (right == w0 and left in (w1, s1)))
    if center == w1:
        return ((left == w1 and right in (w0, s0))
                or (right == w1 and left in (w0, s0)))
    return (left, right) in ((s0, s1), (s1, s0))


def mm(a, b):
    m = len(a)
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(m))
                       for j in range(m)) for i in range(m))


def determinant_polynomial():
    # Leibniz formula for det(I-zQ), no symbolic-library dependency.
    out = [0] * 9
    terms = 0
    for perm in permutations(range(8)):
        degree = 0
        possible = True
        for i, j in enumerate(perm):
            if i == j:
                check(Q[i][i] == 0, "this determinant expansion has zero diagonal")
            elif Q[i][j]:
                degree += 1
            else:
                possible = False
                break
        if not possible:
            continue
        inversions = sum(perm[i] > perm[j] for i in range(8) for j in range(i + 1, 8))
        out[degree] += (-1) ** (inversions + degree)
        terms += 1
    return out, terms


def core_certificate():
    columns = ((0, 2), (2, 0), (0, 1), (1, 0), (1, 1))
    column_triples = []
    def literal_compatible(left, center, right):
        return (literal_triple(left[0], center[0], right[0]) == center[1]
                and literal_triple(left[1], center[1], right[1]) == center[0])
    for left, center, right in product(columns, repeat=3):
        actual = literal_compatible(left, center, right)
        classified = classified_column_triplet(left, center, right)
        check(not classified or actual, ("classified triples are compatible", left, center, right))
        if classified:
            column_triples.append([left, center, right])
    compatible_five_windows = 0
    for window in product(columns, repeat=5):
        # Excluding a neutral neighbour of a weak site uses that neighbour's
        # own equation, not only the center equation. Check all three centers.
        if all(literal_compatible(*window[i:i + 3]) for i in range(3)):
            compatible_five_windows += 1
            check(classified_column_triplet(*window[1:4]),
                  ("converse classification with both neighbours' equations", window))
    path_count = 0
    for i in range(8):
        for j in NEXT[i]:
            check(FLIP[j] in NEXT[FLIP[i]], ("phase-flip graph automorphism", i, j))
            for k in NEXT[j]:
                check(literal_triple(EMIT[i], EMIT[j], EMIT[k]) == EMIT[FLIP[j]],
                      ("role path literal dynamics", i, j, k))
                path_count += 1
    determinant, leibniz_terms = determinant_polynomial()
    check(determinant == [1, 0, -1, -4, -2, 0, 0, 0, 1], "eight-role determinant")
    power = tuple(tuple(int(i == j) for j in range(8)) for i in range(8))
    log_derivative_coefficients = [0]
    traces = []
    for n in range(1, 61):
        power = mm(power, Q)
        tr = sum(power[i][i] for i in range(8))
        dn = determinant[n] if n < len(determinant) else 0
        coeff = -n * dn - sum(determinant[k] * log_derivative_coefficients[n - k]
                              for k in range(1, min(8, n) + 1))
        log_derivative_coefficients.append(coeff)
        check(tr == coeff, ("rational trace generating function", n))
        check(tr % 2 == 0, ("all nonzero core points are paired", n))
        traces.append({"n": n, "nonzero_core_points": tr, "all_core_points": tr + 1,
                       "two_cycles": tr // 2})
        record(("trace", n, tr))
    old_counts = (13, 11, 21, 63, 85, 155, 373, 613)
    for n, expected in zip(range(3, 11), old_counts):
        check(traces[n - 1]["all_core_points"] == expected,
              ("comparison to existing root n3..10 observations, not a new cyclic atlas", n))
    return {"roles": ROLES, "emitted_height": EMIT, "phase_flip": FLIP,
            "adjacency": Q, "admissible_column_triples": column_triples,
            "compatible_five_column_windows": compatible_five_windows,
            "admissible_role_three_paths_checked": path_count,
            "det_I_minus_zQ_coefficients": determinant,
            "nonzero_Leibniz_terms": leibniz_terms, "exact_matrix_traces_n1_to_60": traces,
            "interpretation_scope": "ternary cycle theorem n>=3; n1,2 coefficients only formal graph values"}


def cycle_step(row):
    n = len(row)
    signs = tuple((row[(i + 1) % n] > row[i]) - (row[(i + 1) % n] < row[i])
                  for i in range(n))
    return tuple(int(signs[(i - 1) % n] < 0) + int(signs[i] > 0) for i in range(n))


def single_seed_profile(n, s):
    m = n // 2
    ans = []
    for i in range(n):
        d = min(i, n - i)
        if s == m:
            ans.append(1 if n % 2 and d == m else 2 * int((s - d) % 2 == 0))
        elif d == 0:
            ans.append(2 * int(s % 2 == 0))
        elif d < s:
            ans.append(2 * int((s - d) % 2 == 0))
        elif d == s:
            ans.append(1)
        else:
            ans.append(0)
    return tuple(ans)


def special_witness_checks():
    boxes = []
    for n in range(4, 11):
        source = (0,) + (1,) * (n - 1)
        row = cycle_step(source)
        m = n // 2
        check(row == (2,) + (0,) * (n - 1), ("one-hole source", n))
        for s in range(m + 1):
            check(row == single_seed_profile(n, s), ("closed finite-speed profile", n, s))
            check((cycle_step(cycle_step(row)) == row) == (s == m),
                  ("exact one-hole hitting time", n, s))
            record(("witness", n, s, row))
            row = cycle_step(row)
        boxes.append({"n": n, "source": source, "exact_hitting_time": m + 1,
                      "all_source_enumeration": False})
    max_height, small_core = 0, 0
    for source in product(range(3), repeat=3):
        image = cycle_step(source)
        check(cycle_step(cycle_step(image)) == image, ("n3 first image is core", source))
        in_core = cycle_step(cycle_step(source)) == source
        small_core += int(in_core)
        max_height = max(max_height, int(not in_core))
    check((max_height, small_core) == (1, 13), "all 27 n3 states")
    return {"one_hole_witnesses_within_original_cutoff": boxes,
            "n3_full_small_case": {"states": 27, "maximum_hitting_time": max_height,
                                    "core_points": small_core},
            "unproved_global_sharp_height_formula": "max(5, floor(n/2)+1) is NOT claimed",
            "proved_nonsharp_global_upper_bound": "4*n+2; at n=10 this is 42, not the measured sharp value 6"}


def main():
    local = local_certificate()
    core = core_certificate()
    witnesses = special_witness_checks()
    print(json.dumps({"status": "PASS", "kind": "author computer-assisted local proof certificate",
                      "source_disposition": "HANDOFF_WITH_SOURCE_HOLD; no admission",
                      "literal": "count of the two strictly greater cyclic neighbours",
                      "no_input_file_reads": True, "new_full_cyclic_enumeration_above_n3": False,
                      "local_growth_certificate": local, "core_certificate": core,
                      "special_checks": witnesses, "assertions": ASSERTIONS,
                      "ordered_record_sha256": DIGEST.hexdigest()}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
