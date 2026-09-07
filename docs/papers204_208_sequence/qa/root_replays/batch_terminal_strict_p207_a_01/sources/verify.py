#!/usr/bin/env python3
"""P207 manuscript A: standalone independent exact finite checks.

Reviewer batch197_lzk_gate, NOT a P207 mathematical author. This is a new
Python implementation of this reviewer's disclosed earlier UGR gate routes:
direct 13-height cones, a four-height overlap graph and the full TCSD sign
union. It is not blind, externally reviewed, or independent of that earlier
reviewer. No author/gate/old code is imported or executed; no files, canonical
data, network, randomness, third-party library or floating-point values are
used. The 81-state graph is not the author's eight-role implementation.
Fixed scopes are all 3^13 open words, exact graph powers 1..81, complete
cyclic source/target/sign words n=3..10, and only the stated seed n=4..64.
These finite boxes do NOT prove all-n bounds or literature novelty. The
13-site premise is the explicitly computer-assisted lemma of the proof.
"""

from collections import Counter
from hashlib import sha256
from itertools import product
import json


COUNTS = Counter()
RECORD = sha256()
SECTION = "initial"


def check(value, detail):
    COUNTS[SECTION] += 1
    if not value:
        raise AssertionError((SECTION, detail))


def record(value):
    RECORD.update(json.dumps(value, separators=(",", ":")).encode())
    RECORD.update(b"\n")


def upper_triple(a, b, c):
    return (a > b) + (c > b)


def open_update(row):
    return tuple((row[i - 1] > row[i]) + (row[i + 1] > row[i])
                 for i in range(1, len(row) - 1))


def extrema(row):
    center = len(row) // 2
    return {i - center for i in range(1, len(row) - 1)
            if row[i] < min(row[i - 1], row[i + 1])
            or row[i] > max(row[i - 1], row[i + 1])}


def local_lemma():
    global SECTION
    SECTION = "direct_thirteen_height_local_certificate"
    permanent = 0
    for row in product(range(3), repeat=5):
        if 0 in extrema(row):
            following = open_update(row)
            check(0 in extrema(following), ("permanent", row))
            check(following[1] == (2 if row[2] < row[1] else 0),
                  ("extremum flips type", row))
            permanent += 1
    equal, changed = 0, 0
    witness_counts = Counter()
    for word in product(range(3), repeat=13):
        rows = [word]
        for _ in range(4):
            rows.append(open_update(rows[-1]))
        if rows[4][2] == rows[2][4]:
            equal += 1
            record((word, None))
            continue
        changed += 1
        old = extrema(word)
        witness = None
        for time in range(1, 5):
            fresh = extrema(rows[time]) - old
            if fresh:
                witness = (time, min(fresh))
                break
        check(witness is not None, ("local implication", word))
        time, site = witness
        check(abs(site) <= 5 - time, ("computed extremum domain", word, witness))
        witness_counts[witness] += 1
        record((word, witness))
    check(equal + changed == 3 ** 13, "all 13-letter words exactly once")
    check(equal == 1427787 and changed == 166536, "independent full-cone census")
    return {"enumerated_complete_words": equal + changed, "length": 13,
            "height_comparison_not_edge_sign_implementation": True,
            "equal_centers": equal, "unequal_centers_with_witness": changed,
            "strict_center_cases_in_3_power_5": permanent,
            "first_witness_time_site_counts": [list(k) + [v] for k, v in sorted(witness_counts.items())],
            "no_inner_word_factorization": True}


def code(word, base=3):
    value = 0
    for x in word:
        value = base * value + x
    return value


def overlap_graph():
    global SECTION
    SECTION = "independent_81_height_overlap_graph"
    vertices = list(product(range(3), repeat=4))
    adjacency = [[] for _ in vertices]
    for i, (a, b, c, d) in enumerate(vertices):
        for e in range(3):
            middle = upper_triple(upper_triple(a, b, c),
                                  upper_triple(b, c, d), upper_triple(c, d, e))
            if middle == c:
                adjacency[i].append(code((b, c, d, e)))
    check(sum(map(len, adjacency)) == 137, "complete overlap edge count")
    power = [[int(i == j) for j in range(81)] for i in range(81)]
    traces, coefficients = [0], [1]
    for exponent in range(1, 82):
        following = [[0] * 81 for _ in range(81)]
        for i in range(81):
            for k in range(81):
                term = power[i][k]
                if term:
                    for j in adjacency[k]:
                        following[i][j] += term
        power = following
        traces.append(sum(power[i][i] for i in range(81)))
        numerator = sum(coefficients[i] * traces[exponent - i]
                        for i in range(exponent))
        check(numerator % exponent == 0, ("exact Newton division", exponent))
        coefficients.append(-numerator // exponent)
        record(("overlap_trace_and_Newton", exponent, traces[-1], coefficients[-1]))
    expected = [1, -1, -1, -3, 2, 2, 0, 0, 1, -1] + [0] * 72
    check(coefficients == expected, "entire 81-degree determinant, including every zero tail")
    check(traces[1:9] == [1, 3, 13, 11, 21, 63, 85, 155], "initial independent core counts")
    return {"vertices_four_heights": vertices, "adjacency": adjacency,
            "edges": 137, "trace_exponents_1_to_81": traces[1:],
            "det_I_minus_zR_coefficients_all_82": coefficients,
            "determinant_identity": "(1-z)*(1-z^2-4*z^3-2*z^4+z^8)",
            "arithmetic": "Python arbitrary-precision integers; no truncated characteristic polynomial"}


def upper(word):
    return tuple((word[i - 1] > word[i]) + (word[(i + 1) % len(word)] > word[i])
                 for i in range(len(word)))


def lower(word):
    return tuple((word[i - 1] < word[i]) + (word[(i + 1) % len(word)] < word[i])
                 for i in range(len(word)))


def cyclic_extrema(word):
    return {i for i in range(len(word))
            if word[i] < min(word[i - 1], word[(i + 1) % len(word)])
            or word[i] > max(word[i - 1], word[(i + 1) % len(word)])}


def language(word):
    if not any(word):
        return True
    if 0 not in word:
        return False
    n = len(word)
    start = next(i for i in range(n) if word[i] == 0 and word[i - 1] > 0)
    row = word[start:] + word[:start]
    zero_lengths, positives = [], []
    i = 0
    while i < n:
        j = i
        while i < n and row[i] == 0:
            i += 1
        zero_lengths.append(i - j)
        j = i
        while i < n and row[i] > 0:
            i += 1
        positives.append(row[j:i])
    allowed = {(2,), (1, 1), (1, 2), (2, 1), (1, 2, 1)}
    for i, word_part in enumerate(positives):
        if zero_lengths[i] not in (1, 2) or word_part not in allowed:
            return False
        if word_part in {(1, 2), (1, 2, 1)} and zero_lengths[i] != 1:
            return False
        if word_part in {(2, 1), (1, 2, 1)} and zero_lengths[(i + 1) % len(positives)] != 1:
            return False
    return True


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def sign_weight(signs):
    """The old TCSD theorem, reimplemented from its proof, not its code."""
    strict = tuple(s for s in signs if s)
    if not strict:
        return 3
    if len(set(strict)) == 1:
        return 0
    start = next(i for i in range(len(strict)) if strict[i] != strict[i - 1])
    strict = strict[start:] + strict[:start]
    runs, i = [], 0
    while i < len(strict):
        j = i
        while i < len(strict) and strict[i] == strict[j]:
            i += 1
        runs.append(i - j)
    if max(runs) >= 3:
        return 0
    doubled = [i for i, length in enumerate(runs) if length == 2]
    if not doubled:
        return lucas(len(strict))
    result = 1
    for j, run_position in enumerate(doubled):
        gap = (doubled[(j + 1) % len(doubled)] - run_position - 1) % len(runs)
        result *= fibonacci(gap + 1)
    return result


def orbit_data(successor):
    """Walk each previously unseen path, without assuming a period bound."""
    depth, period = [-1] * len(successor), [-1] * len(successor)
    cycles = []
    for source in range(len(successor)):
        if depth[source] != -1:
            continue
        path, position = [], {}
        current = source
        while depth[current] == -1 and current not in position:
            position[current] = len(path)
            path.append(current)
            current = successor[current]
        if current in position:
            beginning = position[current]
            cycle = path[beginning:]
            cycles.append(cycle)
            for vertex in cycle:
                depth[vertex], period[vertex] = 0, len(cycle)
            path = path[:beginning]
        for vertex in reversed(path):
            depth[vertex] = depth[successor[vertex]] + 1
            period[vertex] = period[successor[vertex]]
    return depth, period, cycles


def rotations(word):
    return {word[i:] + word[:i] for i in range(len(word))}


def claimed_maximizers(n):
    m = n // 2
    if n % 2 == 0:
        return rotations((0, 2) * m)
    result = rotations((0, 0) + (2, 0) * (m - 1) + (2,))
    result |= rotations((0, 1, 1) + (0, 2) * (m - 1))
    if n == 3:
        result.add((0, 0, 0))
    return result


def complete_cycles(graph):
    global SECTION
    SECTION = "complete_cyclic_sources_targets_and_sign_strata"
    reports, union_example = [], None
    for n in range(3, 11):
        states = list(product(range(3), repeat=n))
        size = len(states)
        successor = [code(upper(x)) for x in states]
        upper_sources = [[] for _ in states]
        lower_sources = [[] for _ in states]
        sign_sources = [[] for _ in states]
        for index, x in enumerate(states):
            upper_sources[successor[index]].append(index)
            lower_sources[code(lower(x))].append(index)
            signs = tuple((x[(i + 1) % n] > x[i]) - (x[(i + 1) % n] < x[i]) for i in range(n))
            sign_sources[code(tuple(s + 1 for s in signs))].append(index)
            check(upper(tuple(2 - value for value in x)) == lower(x), ("pointwise UJ=F", n, index))
            check(cyclic_extrema(x) <= cyclic_extrema(states[successor[index]]),
                  ("cyclic extrema permanence including repeated 13-site windows", n, index))
        depth, period, cycles = orbit_data(successor)
        check(set(period) <= {1, 2}, ("literal all-orbit periods", n))
        check([cycle for cycle in cycles if len(cycle) == 1] == [[0]], ("unique fixed source", n))
        check(sum(map(len, cycles)) == graph["trace_exponents_1_to_81"][n - 1], ("independent core graph", n))
        union_counts = [0] * size
        union_sources = [set() for _ in states]
        feasible_strata = [[] for _ in states]
        for sign_index, shifted in enumerate(states):
            signs = tuple(s - 1 for s in shifted)
            value = sign_weight(signs)
            check(value == len(sign_sources[sign_index]), ("entire TCSD stratum", n, signs))
            target = tuple((signs[i - 1] == -1) + (signs[i] == 1) for i in range(n))
            destination = code(target)
            check(not (union_sources[destination] & set(sign_sources[sign_index])),
                  ("unique labelled sign stratum", n, signs))
            union_sources[destination].update(sign_sources[sign_index])
            union_counts[destination] += value
            if value:
                feasible_strata[destination].append((signs, value, sign_sources[sign_index]))
            record(("full_sign_stratum", n, signs, value, sign_sources[sign_index]))
        attained, depths = [], Counter(depth)
        maximum = lucas(2 * (n // 2))
        for index, x in enumerate(states):
            second = successor[successor[index]]
            fourth = successor[successor[second]]
            is_core = second == index
            check(language(x) == is_core, ("core language iff", n, x))
            check((depth[index] == 0) == is_core, ("literal walk depth versus square", n, x))
            check(depth[index] <= 4 * n + 2, ("nonsharp finite bound", n, x))
            if cyclic_extrema(states[fourth]) == cyclic_extrema(x):
                check(fourth == second, ("four-step implication on every cyclic source", n, x))
            check(union_sources[index] == set(upper_sources[index]), ("complete labelled union source set", n, x))
            check(union_counts[index] == len(upper_sources[index]), ("whole aggregated target count", n, x))
            check({size - 1 - source for source in lower_sources[index]} == set(upper_sources[index]),
                  ("full inverse complement source set", n, x))
            check(union_counts[index] <= maximum, ("all target maximum", n, x))
            if union_counts[index] == maximum:
                attained.append(x)
            record(("whole_fibre_depth", n, x, union_counts[index], upper_sources[index], depth[index]))
        check(set(attained) == claimed_maximizers(n), ("all labelled equality cases", n))
        check(sum(union_counts) == size, ("partition of full carrier", n))
        if n == 3:
            check(max(depth) == 1, "H(3)=1")
        if n == 4:
            target = (0, 1, 0, 1)
            parts = feasible_strata[code(target)]
            check(len(parts) == 2 and sorted(v for _, v, _ in parts) == [3, 3], "union versus single stratum")
            union_example = {"target": target, "whole_count": union_counts[code(target)],
                             "parts": [{"signs": s, "count": v, "complete_sources": [states[t] for t in ids]}
                                       for s, v, ids in parts]}
        reports.append({"n": n, "sources_targets_sign_words_each": size,
                        "image_points": sum(bool(v) for v in upper_sources),
                        "core_points": sum(map(len, cycles)),
                        "cycles_by_period": sorted(Counter(map(len, cycles)).items()),
                        "states_by_eventual_period": sorted(Counter(period).items()),
                        "exact_depth_histogram": sorted(depths.items()),
                        "observed_height_not_all_n_formula": max(depth),
                        "fibre_size_histogram_including_empty": sorted(Counter(union_counts).items()),
                        "maximum_fibre": maximum, "all_labelled_maximizers": attained,
                        "feasible_sign_strata": sum(bool(v) for v in sign_sources),
                        "successor_vector_sha256": sha256(json.dumps(successor, separators=(",", ":")).encode()).hexdigest()})
    return reports, union_example


def seeds():
    global SECTION
    SECTION = "stated_seed_only_not_full_boxes"
    reports = []
    for n in range(4, 65):
        source = (0,) + (1,) * (n - 1)
        word = upper(source)
        meeting = n // 2
        check(word == (2,) + (0,) * (n - 1), ("one-hole to seed", n))
        check(upper(upper(source)) != source, ("source noncore", n))
        for time in range(meeting + 1):
            expected = []
            for i in range(n):
                distance = min(i, n - i)
                if time == meeting:
                    value = 1 if n % 2 and distance == meeting else 2 * int((time - distance) % 2 == 0)
                elif distance == 0 or distance < time:
                    value = 2 * int((time - distance) % 2 == 0)
                elif distance == time:
                    value = 1
                else:
                    value = 0
                expected.append(value)
            check(word == tuple(expected), ("entire wave formula", n, time))
            check((upper(upper(word)) == word) == (time == meeting), ("exact seed entrance", n, time))
            check(language(word) == (time == meeting), ("core boundary", n, time))
            record(("seed", n, time, word))
            word = upper(word)
        reports.append({"n": n, "seed_entrance": meeting, "source_entrance": meeting + 1})
    return reports


def main():
    local = local_lemma()
    graph = overlap_graph()
    cyclic, union_example = complete_cycles(graph)
    seed = seeds()
    print(json.dumps({"status": "PASS", "schema": "p207-manuscript-a-independent-v1",
                      "paper": "P207", "kind": "independent reviewer finite evidence, not all-n or source certification",
                      "same_reviewer_prior_gate_algorithm_reuse_disclosed": True,
                      "author_code_imports_or_execution": False, "input_file_reads": False,
                      "standard_library_only": True, "arbitrary_precision_integer_only": True,
                      "literal": "U(x)_i=[x_(i-1)>x_i]+[x_(i+1)>x_i], labelled ternary n>=3",
                      "local_certificate": local, "independent_overlap_core_graph": graph,
                      "complete_cyclic_boxes": cyclic, "full_union_counterexample": union_example,
                      "seed_only_n4_to_64": seed, "assertions_by_section": dict(sorted(COUNTS.items())),
                      "assertions": sum(COUNTS.values()), "ordered_checked_record_sha256": RECORD.hexdigest(),
                      "excluded_claims": ["global sharp height for n>=4", "global literature novelty",
                                          "source clearance", "external review", "new independent gate reviewer"]},
                     sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
