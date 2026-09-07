#!/usr/bin/env python3
"""P207 standalone AUTHOR certificate and finite corroboration.

Authorship: batch197_fosp_gate, an UGR/LNR proof contributor. Adapted from
that author's verify_ugr.py and verify_inverse.py; no reviewer code is used.
Only Python's standard library is imported. There are NO input-file reads,
repository imports, canonical reads, network requests, or random choices.

Scopes fixed before this paper-local producer's initial execution:
  * all 3^11 inner words, with every one of the nine outer extensions for
    all exceptional inner words; a deductive overlap argument covers 3^13;
  * all five-type temporal-column triples and five-column windows;
  * exact eight-role determinant and graph traces through exponent 60;
  * every cyclic source AND target for n=3,...,10 (the existing gate cutoff);
  * every positive local source/target run through length 6;
  * every A/J/B matrix word of lengths 2,...,10 and identities through 100;
  * only the stated single-seed witnesses for n=4,...,64, NOT full boxes;
  * alternating-target independent-set adapters at n=4,6,8,10.

The local certificate is a stated computer-assisted proof dependency.
Finite cyclic/matrix checks do not prove an all-size theorem or a sharp
global clock. The proved global upper bound 4*n+2 is explicitly nonsharp.
This executable does not certify sources, independent review or completion.
"""

from collections import Counter, defaultdict, deque
from hashlib import sha256
from itertools import permutations, product
import json


ASSERTIONS = Counter()
RECORD = sha256()
SECTION = "setup"
SCOPE = {
    "cyclic_complete_source_and_target_lengths": [3, 10],
    "inner_window_length": 11,
    "outer_extension_alphabet_each_side": [0, 1, 2],
    "covered_window_length": 13,
    "local_growth_updates": 4,
    "positive_local_run_lengths": [1, 6],
    "all_A_J_B_word_lengths": [2, 10],
    "matrix_identity_exponents": [2, 100],
    "graph_trace_exponents": [1, 60],
    "single_seed_only_lengths": [4, 64],
    "independent_set_adapter_lengths": [4, 6, 8, 10],
}
ROLES = ("S0", "S1", "W0L", "W0R", "W1L", "W1R", "N01", "N10")
EMIT = (0, 2, 0, 0, 1, 1, 1, 1)
FLIP = (1, 0, 4, 5, 2, 3, 7, 6)
NEXT = ((1, 4, 6), (0, 2, 7), (3,), (1, 4), (5,), (0, 2), (1,), (0,))
Q = tuple(tuple(int(j in NEXT[i]) for j in range(8)) for i in range(8))
ZERO = ((0, 0, 0),) * 3
I3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
KERNELS = {
    (2,): ((2, 1, 0), (1, 1, 0), (0, 0, 0)),
    (1,): ((0, 1, 1), (1, 0, 1), (1, 1, 0)),
    (1, 1): ((2, 1, 1), (1, 1, 0), (1, 0, 0)),
    (1, 2): ((1, 1, 0), (0, 0, 0), (0, 0, 0)),
    (2, 1): ((1, 0, 0), (1, 0, 0), (0, 0, 0)),
    (1, 1, 1): ((2, 1, 0), (1, 0, 0), (0, 0, 0)),
    (1, 2, 1): ((1, 0, 0), (0, 0, 0), (0, 0, 0)),
    (1, 1, 1, 1): ((1, 0, 0), (0, 0, 0), (0, 0, 0)),
}
A, J, B = (KERNELS[w] for w in ((2,), (1,), (1, 1)))


def section(name):
    global SECTION
    SECTION = name


def check(condition, detail):
    ASSERTIONS[SECTION] += 1
    if not condition:
        raise AssertionError((SECTION, detail))


def record(obj):
    RECORD.update(json.dumps(obj, separators=(",", ":")).encode("utf-8"))
    RECORD.update(b"\n")


def matrix_multiply(a, b):
    n = len(a)
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(n))
                       for j in range(n)) for i in range(n))


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def encode(word):
    ans = 0
    for digit in word:
        ans = 3 * ans + digit
    return ans


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def edges(row):
    return tuple((b > a) - (b < a) for a, b in zip(row, row[1:]))


def open_step(row):
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
        rows.append(open_step(rows[-1]))
    original = extreme_sites(row)
    events = [(s, j) for s in range(1, 5)
              for j in sorted(extreme_sites(rows[s]) - original)]
    changed = rows[4][len(rows[4]) // 2] != rows[2][len(rows[2]) // 2]
    return rows, events, changed


def check_witness(rows, event):
    s, j = event
    radius = len(rows[0]) // 2
    check(1 <= s <= 4 and abs(j) <= radius - 1 - s,
          ("witness inside computed extremum domain", len(rows[0]), event))
    first, later = rows[0], rows[s]
    i0, it = radius + j, len(later) // 2 + j
    a, b, c = first[i0 - 1:i0 + 2]
    old_extreme = b < min(a, c) or b > max(a, c)
    a, b, c = later[it - 1:it + 2]
    new_extreme = b < min(a, c) or b > max(a, c)
    check(not old_extreme and new_extreme,
          ("direct-height witness, independent of sign test", first, event))


def local_growth_certificate():
    section("local_growth_certificate")
    for a, b, c in product(range(3), repeat=3):
        check(open_step((a, b, c)) == (int(a > b) + int(c > b),),
              ("edge-sign expression equals literal rule", a, b, c))
    extrema = 0
    for row in product(range(3), repeat=5):
        if 0 in extreme_sites(row):
            extrema += 1
            nxt = open_step(row)
            check(0 in extreme_sites(nxt), ("permanent strict extremum", row))
            old_minimum = row[2] < min(row[1], row[3])
            check(nxt[1] == (2 if old_minimum else 0),
                  ("extremum reverses type", row))
    classes, events_census = Counter(), Counter()
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
            record(("inner_witness_valid_for_all_nine_extensions", inner, chosen))
        else:
            classes["needs_outer_letters"] += 1
            nine = []
            for left, right in product(range(3), repeat=2):
                full = (left,) + inner + (right,)
                full_rows, full_events, full_changed = cone(full)
                check(full_changed, ("outer extension preserves both centers", full))
                check(bool(full_events), ("radius-six four-step growth", full))
                chosen = full_events[0]
                check_witness(full_rows, chosen)
                events_census[chosen] += 1
                nine.append([left, right, *chosen])
                record(("explicit_outer_extension_witness", full, chosen))
            check({tuple(item[:2]) for item in nine} == set(product(range(3), repeat=2)),
                  ("every outer-letter pair represented once", inner))
            exceptions.append({"inner_word": inner,
                               "all_nine_extensions_left_right_time_site": nine})
    check(classes == {"center_equal": 158643, "inner_witness": 18300,
                      "needs_outer_letters": 204}, "full inner classification")
    covered = sum(9 * count for count in classes.values())
    check(sum(classes.values()) == 3 ** 11, "all inner words covered")
    check(covered == 3 ** 13, "unique inner word times all nine extensions")
    check(len(exceptions) == classes["needs_outer_letters"], "complete exceptional list")
    return {
        "representation": "edge-sign evolution; witnesses rechecked by height inequalities",
        "initial_radius": 6, "updates": 4, "strict_center_cases_among_3_power_5": extrema,
        "inner_words_enumerated": 3 ** 11, "inner_case_counts": dict(classes),
        "explicit_outer_extensions": 9 * len(exceptions),
        "all_thirteen_letter_words_covered_by_proved_overlap_argument": covered,
        "direct_enumeration_of_all_3_power_13_words": False,
        "overlap_argument": [
            "Every 13-letter word has one inner 11-letter word and one of nine outer pairs.",
            "Both time-2/time-4 centers depend only on the inner cone.",
            "An inner witness at |j|<=4-s and its time-zero test use only the inner cone.",
            "Every exceptional inner word instead has all nine full witnesses at |j|<=5-s.",
            "Cyclic windows of every n>=3, including repeated coordinates for n<13, embed by locality.",
        ],
        "first_witness_census": [list(k) + [v] for k, v in sorted(events_census.items())],
        "complete_inner_exception_and_extension_certificate": exceptions,
    }


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


def determinant_polynomial():
    # Full exact 8-by-8 Leibniz expansion; no symbolic library or truncated fit.
    check(all(Q[i][i] == 0 for i in range(8)), "zero diagonal for expansion")
    out, terms = [0] * 9, 0
    for perm in permutations(range(8)):
        degree = 0
        for i, j in enumerate(perm):
            if i != j:
                if not Q[i][j]:
                    break
                degree += 1
        else:
            inversions = sum(perm[i] > perm[j] for i in range(8) for j in range(i + 1, 8))
            out[degree] += (-1) ** (inversions + degree)
            terms += 1
    return out, terms


def core_local_certificate():
    section("core_local_and_graph")
    columns = ((0, 2), (2, 0), (0, 1), (1, 0), (1, 1))

    def compatible(left, center, right):
        return (literal_triple(left[0], center[0], right[0]) == center[1]
                and literal_triple(left[1], center[1], right[1]) == center[0])

    triples = []
    for left, center, right in product(columns, repeat=3):
        classified = classified_column_triplet(left, center, right)
        check(not classified or compatible(left, center, right),
              ("sufficiency at center", left, center, right))
        if classified:
            triples.append([left, center, right])
    necessary_windows = 0
    for window in product(columns, repeat=5):
        if all(compatible(*window[i:i + 3]) for i in range(3)):
            necessary_windows += 1
            check(classified_column_triplet(*window[1:4]),
                  ("necessity includes both neighbors' own equations", window))
    paths = 0
    for i in range(8):
        for j in NEXT[i]:
            check(FLIP[j] in NEXT[FLIP[i]], ("phase-flip automorphism", i, j))
            for k in NEXT[j]:
                paths += 1
                check(literal_triple(EMIT[i], EMIT[j], EMIT[k]) == EMIT[FLIP[j]],
                      ("role path induces literal dynamics", i, j, k))
    determinant, terms = determinant_polynomial()
    check(determinant == [1, 0, -1, -4, -2, 0, 0, 0, 1], "full determinant polynomial")
    power = tuple(tuple(int(i == j) for j in range(8)) for i in range(8))
    coefficients, traces = [0], []
    for n in range(1, 61):
        power = matrix_multiply(power, Q)
        value = trace(power)
        dn = determinant[n] if n < 9 else 0
        coefficient = -n * dn - sum(determinant[k] * coefficients[n - k]
                                    for k in range(1, min(n, 8) + 1))
        coefficients.append(coefficient)
        check(value == coefficient, ("minus z D prime over D", n))
        check(value % 2 == 0, ("nonzero core pairing", n))
        traces.append({"n": n, "nonzero_core_points": value,
                       "all_core_points": value + 1, "two_cycles": value // 2})
        record(("core_trace", n, value))
    check([v["nonzero_core_points"] for v in traces[:8]] == [0, 2, 12, 10, 20, 62, 84, 154],
          "stated initial graph traces")
    return {"roles": ROLES, "emitted_height": EMIT, "phase_flip": FLIP,
            "adjacency": Q, "admissible_column_triples": triples,
            "compatible_five_column_windows": necessary_windows,
            "admissible_role_three_paths": paths,
            "det_I_minus_zQ_coefficients": determinant,
            "nonzero_Leibniz_terms": terms, "traces_n1_to_60": traces,
            "n1_and_n2_scope": "formal graph values only; original carrier is n>=3"}


def upper_step(x):
    n = len(x)
    return tuple(int(x[(i - 1) % n] > x[i]) + int(x[(i + 1) % n] > x[i])
                 for i in range(n))


def edge_ranks(x):
    # Independently award one unit to the smaller and to the larger endpoint.
    upper, lower = [0] * len(x), [0] * len(x)
    for i in range(len(x)):
        j = (i + 1) % len(x)
        if x[i] < x[j]:
            upper[i] += 1
            lower[j] += 1
        elif x[j] < x[i]:
            upper[j] += 1
            lower[i] += 1
    return tuple(upper), tuple(lower)


def split_target(b):
    # Only called on words with both a zero and a positive entry.
    n = len(b)
    start = next(i for i in range(n) if b[i] == 0 and b[(i - 1) % n] > 0)
    offset, zeros, positives, words = 0, [], [], []
    while offset < n:
        z, p = [], []
        while offset < n and b[(start + offset) % n] == 0:
            z.append((start + offset) % n)
            offset += 1
        while offset < n and b[(start + offset) % n] > 0:
            p.append((start + offset) % n)
            offset += 1
        zeros.append(tuple(z))
        positives.append(tuple(p))
        words.append(tuple(b[i] for i in p))
    return zeros, positives, words


def role_decode(x):
    if not any(x):
        return ()  # Distinct all-zero exception; not an eight-role word.
    if 0 not in x:
        return None
    zeros, positives, words = split_target(x)
    if any(len(z) not in (1, 2) for z in zeros):
        return None
    positive_roles = {(2,): (1,), (1, 1): (4, 5), (1, 2): (6, 1),
                      (2, 1): (1, 7), (1, 2, 1): (6, 1, 7)}
    roles = [-1] * len(x)
    for j, (z, p, w) in enumerate(zip(zeros, positives, words)):
        if w not in positive_roles:
            return None
        if w in ((1, 2), (1, 2, 1)) and len(z) != 1:
            return None
        if w in ((2, 1), (1, 2, 1)) and len(zeros[(j + 1) % len(zeros)]) != 1:
            return None
        for i, role in zip(z, (0,) if len(z) == 1 else (2, 3)):
            roles[i] = role
        for i, role in zip(p, positive_roles[w]):
            roles[i] = role
    return tuple(roles)


def local_source_list(w, a, b):
    out = []
    if w == (2,):
        if a == b == 0:
            out.append((1,))
        if a < 2 and b < 2:
            out.append((2,))
    elif w == (1,):
        if (a, b) in ((0, 1), (1, 0)):
            out.append((1,))
        if (a, b) in ((0, 2), (1, 2), (2, 0), (2, 1)):
            out.append((2,))
    elif w == (1, 1):
        if a == b == 0:
            out.append((1, 1))
        if a < 2 and b < 2:
            out.append((2, 2))
        if (a, b) == (0, 2):
            out.append((1, 2))
        if (a, b) == (2, 0):
            out.append((2, 1))
    elif w == (1, 2):
        if a == 0 and b < 2:
            out.append((1, 2))
    elif w == (2, 1):
        if a < 2 and b == 0:
            out.append((2, 1))
    elif w == (1, 1, 1):
        if a == 0 and b < 2:
            out.append((1, 2, 2))
        if a < 2 and b == 0:
            out.append((2, 2, 1))
    elif w == (1, 2, 1):
        if a == b == 0:
            out.append((1, 2, 1))
    elif w == (1, 1, 1, 1):
        if a == b == 0:
            out.append((1, 2, 2, 1))
    return tuple(out)


def local_inverse_tables():
    section("local_inverse_tables")
    boxes = []
    for m in range(1, 7):
        inventory, attempts = defaultdict(set), 0
        for a, b in product(range(3), repeat=2):
            for u in product((1, 2), repeat=m):
                attempts += 1
                if a > u[0] or b > u[-1]:
                    continue
                row = (a,) + u + (b,)
                w = tuple(int(row[i - 1] < row[i]) + int(row[i + 1] < row[i])
                          for i in range(1, m + 1))
                if all(w):
                    inventory[w, a, b].add(u)
            for w in product((1, 2), repeat=m):
                stated = local_source_list(w, a, b)
                check(len(stated) == len(set(stated)), ("local injection", w, a, b))
                check(set(stated) == inventory[w, a, b], ("complete local source list", w, a, b))
                check(len(stated) == KERNELS.get(w, ZERO)[a][b], ("kernel entry", w, a, b))
                record(("local_inverse", w, a, b, sorted(stated)))
        boxes.append({"positive_run_length": m, "boundary_source_attempts": attempts,
                      "nonempty_boundary_fibres": sum(bool(v) for v in inventory.values())})
    return boxes


def inverse_decoder(b):
    """Construct every U source by complementing the proven lower-rank decoder."""
    n = len(b)
    if 0 not in b:
        return set(), 0
    if not any(b):
        return {encode((v,) * n) for v in range(3)}, 3
    zeros, positives, words = split_target(b)
    matrix = I3
    for w in words:
        matrix = matrix_multiply(matrix, KERNELS.get(w, ZERO))
    evaluated = trace(matrix)
    if evaluated == 0:
        # Every summand is a nonnegative integer. This is an exact zero test,
        # not clipping, sampling or a relaxed decoder.
        return set(), 0
    count = len(words)
    sources = set()
    for heights in product(range(3), repeat=count):
        choices = [local_source_list(w, heights[j], heights[(j + 1) % count])
                   for j, w in enumerate(words)]
        if not all(choices):
            continue
        base = [-1] * n
        for j, sites in enumerate(zeros):
            for i in sites:
                base[i] = heights[j]
        for filling in product(*choices):
            x = base.copy()
            for sites, letters in zip(positives, filling):
                for i, letter in zip(sites, letters):
                    x[i] = letter
            check(all(0 <= value <= 2 for value in x), ("decoder fills every labelled site", b))
            code = encode(tuple(2 - value for value in x))
            check(code not in sources, ("complemented decoder injection", b, heights, filling))
            sources.add(code)
    return sources, evaluated


def rotations(x):
    return {x[i:] + x[:i] for i in range(len(x))}


def equality_targets(n):
    m = n // 2
    if n % 2 == 0:
        return rotations((0, 2) * m)
    out = rotations((0, 0) + (2, 0) * (m - 1) + (2,))
    out |= rotations((0, 1, 1) + (0, 2) * (m - 1))
    if n == 3:
        out.add((0, 0, 0))
    return out


def functional_graph(successors):
    nstates = len(successors)
    indegree = [0] * nstates
    for image in successors:
        indegree[image] += 1
    residue = indegree.copy()
    queue = deque(i for i, degree in enumerate(residue) if degree == 0)
    peeled = []
    while queue:
        current = queue.popleft()
        peeled.append(current)
        image = successors[current]
        residue[image] -= 1
        if residue[image] == 0:
            queue.append(image)
    visited, cycles = set(), []
    for i, degree in enumerate(residue):
        if degree and i not in visited:
            orbit, current = [], i
            while current not in visited:
                visited.add(current)
                orbit.append(current)
                current = successors[current]
            check(current == i, ("remaining graph consists of cycles", i))
            cycles.append(orbit)
    depth = [0] * nstates
    for current in reversed(peeled):
        depth[current] = depth[successors[current]] + 1
    return indegree, depth, cycles


def full_cycle_and_inverse_boxes(graph_traces):
    section("full_cyclic_sources_targets_n3_to_10")
    boxes = []
    for n in range(3, 11):
        states = list(product(range(3), repeat=n))
        inverse, lower_inverse = defaultdict(set), defaultdict(set)
        successors = []
        for code, x in enumerate(states):
            check(encode(x) == code, ("lexicographic base-three indexing", n, code))
            y = upper_step(x)
            upper, lower = edge_ranks(x)
            check(y == upper, ("direct and edge-oriented U agree", n, x))
            check(all(0 <= v <= 2 for v in y), ("carrier closure", n, x))
            image = encode(y)
            successors.append(image)
            inverse[image].add(code)
            lower_inverse[encode(lower)].add(code)
        indegree, depth, cycles = functional_graph(successors)
        check(all(len(cycle) in (1, 2) for cycle in cycles), ("finite periods one/two", n))
        check([cycle for cycle in cycles if len(cycle) == 1] == [[0]], ("unique zero fixed point", n))
        check(sum(len(cycle) for cycle in cycles) == graph_traces[n - 1]["all_core_points"],
              ("literal recurrent census matches independently encoded role graph", n))
        maximum = lucas(2 * (n // 2))
        equal = set()
        for code, target in enumerate(states):
            roles = role_decode(target)
            is_core = successors[successors[code]] == code
            check((roles is not None) == is_core, ("exact core run language", n, target))
            check((depth[code] == 0) == is_core, ("Kahn core agrees with literal U square", n, code))
            if roles:
                check(tuple(EMIT[r] for r in roles) == target, ("role inverse keeps labels", target))
                check(all(roles[(i + 1) % n] in NEXT[roles[i]] for i in range(n)),
                      ("role inverse is a closed walk", target))
                check(role_decode(states[successors[code]]) == tuple(FLIP[r] for r in roles),
                      ("literal U is role phase flip", target))
            if depth[code]:
                check(depth[code] == 1 + depth[successors[code]], ("exact transient recurrence", n, code))
            check(depth[code] <= 4 * n + 2, ("stated nonsharp bound in finite box", n, code))
            decoded, evaluated = inverse_decoder(target)
            actual = inverse.get(code, set())
            complemented_lower = {3 ** n - 1 - c for c in lower_inverse.get(code, set())}
            check(actual == complemented_lower, ("full labelled U inverse equals J F inverse", target))
            check(actual == decoded, ("full decoded source set, including empty targets", target))
            check(len(actual) == evaluated == indegree[code], ("kernel/count/graph indegree", target))
            check(evaluated <= maximum, ("all-target sharp maximum bound", target, evaluated))
            if evaluated == maximum:
                equal.add(target)
            record(("complete_fibre", n, code, sorted(actual), evaluated, depth[code]))
        check(equal == equality_targets(n), ("entire labelled equality classification", n))
        check(len(equal) == (7 if n == 3 else 2 if n % 2 == 0 else 2 * n),
              ("maximizer number", n))
        check(max(indegree) == maximum, ("maximum attained", n))
        check(sum(indegree) == 3 ** n, ("source partition identity", n))
        iterate = list(range(3 ** n))
        at_bound = None
        for t in range(1, 4 * n + 5):
            iterate = [successors[code] for code in iterate]
            if t == 4 * n + 2:
                at_bound = iterate.copy()
        check(iterate == at_bound, ("actual U^(4n+4)=U^(4n+2) throughout box", n))
        height = max(depth)
        if n == 3:
            check(height == 1, "complete n3 exact global height")
        deepest_code = depth.index(height)
        orbit = [deepest_code]
        for _ in range(height + 2):
            orbit.append(successors[orbit[-1]])
        boxes.append({
            "n": n, "complete_sources_and_targets_each": 3 ** n,
            "image_points": len(inverse), "core_points": sum(len(c) for c in cycles),
            "cycle_histogram_period_count": sorted(Counter(map(len, cycles)).items()),
            "observed_sharp_height_in_this_complete_box": height,
            "proved_nonsharp_global_bound": 4 * n + 2,
            "depth_histogram": sorted(Counter(depth).items()),
            "maximum_fibre": maximum, "all_labelled_maximizers": sorted(equal),
            "target_fibre_histogram_including_empty": sorted(Counter(indegree).items()),
            "first_deepest_witness_and_entrance_plus_cycle": [states[c] for c in orbit],
            "successor_index_vector_sha256": sha256(json.dumps(successors, separators=(",", ":")).encode()).hexdigest(),
        })
    return boxes


def matrix_word_checks():
    section("mixed_kernel_comparison")
    boxes = []
    for length in range(2, 11):
        counts = Counter()

        def visit(labels, value):
            if len(labels) < length:
                for label, matrix in enumerate((A, J, B)):
                    visit(labels + (label,), matrix_multiply(value, matrix))
                return
            k, j = labels.count(2), labels.count(1)
            actual, bound = trace(value), lucas(2 * (length + k // 2))
            check(actual <= bound, ("every mixed product bound", labels, actual))
            check((actual == bound) == (k <= 1 and j == 0),
                  ("mixed strictness and one-B equality", labels, actual))
            counts[k, j, actual == bound] += 1
            record(("mixed_word", labels, actual))

        visit((), I3)
        check(sum(counts.values()) == 3 ** length, ("all matrix words enumerated", length))
        check(sum(v for (k, j, equality), v in counts.items() if equality) == length + 1,
              ("exact mixed equality word count", length))
        boxes.append({"length": length, "all_words": 3 ** length, "equality_words": length + 1,
                      "by_B_count_J_count_equality": [list(k) + [v] for k, v in sorted(counts.items())]})
    power = A
    for r in range(2, 101):
        previous, power = power, matrix_multiply(power, A)
        check(trace(power) == lucas(2 * r), ("Lucas identity", r))
        check(trace(matrix_multiply(B, previous)) == trace(power), ("one-B identity", r))
        for w in ((1, 2), (2, 1), (1, 1, 1), (1, 2, 1), (1, 1, 1, 1)):
            check(trace(matrix_multiply(KERNELS[w], previous)) < trace(power),
                  ("strict dominated kernel", r, w))
    check(13 ** 2 < 3 * 13 * 5 - 5 ** 2, "13/5 below larger quadratic root lambda")
    check(169 ** 3 > 270 * 25 ** 3, "3*cuberoot(10)<(13/5)^2")
    check(13 ** 3 > 10 * 5 ** 3, "10<lambda^3")
    check(13 ** 4 > 30 * 5 ** 4, "30<lambda^4")
    check(13 ** 4 > 9 * 5 ** 4, "9<lambda^4")
    return {"matrix_word_boxes": boxes, "identity_range": [2, 100],
            "analytic_constant_checks": "exact integer/rational inequalities, no floating-point proof",
            "proof_scope": "finite corroboration of a separate all-parameter Holder/length-budget proof"}


def single_seed_profile(n, time):
    meeting = n // 2
    out = []
    for i in range(n):
        distance = min(i, n - i)
        if time == meeting:
            out.append(1 if n % 2 and distance == meeting else 2 * int((time - distance) % 2 == 0))
        elif distance == 0:
            out.append(2 * int(time % 2 == 0))
        elif distance < time:
            out.append(2 * int((time - distance) % 2 == 0))
        elif distance == time:
            out.append(1)
        else:
            out.append(0)
    return tuple(out)


def seed_checks():
    section("single_seed_only")
    boxes = []
    for n in range(4, 65):
        source = (0,) + (1,) * (n - 1)
        row, meeting = upper_step(source), n // 2
        check(row == (2,) + (0,) * (n - 1), ("one-hole source to single seed", n))
        check(upper_step(upper_step(source)) != source, ("source not already in core", n))
        for time in range(meeting + 1):
            check(row == single_seed_profile(n, time), ("exact wave at every premeeting/meeting time", n, time))
            check((upper_step(upper_step(row)) == row) == (time == meeting),
                  ("exact seed entrance", n, time))
            check((role_decode(row) is not None) == (time == meeting),
                  ("meeting profile and core-language converse", n, time))
            record(("single_seed", n, time, row))
            row = upper_step(row)
        boxes.append({"n": n, "single_seed_hitting_time": meeting,
                      "one_hole_source_hitting_time": meeting + 1,
                      "all_source_enumeration": False})
    return boxes


def classical_attainer_checks():
    section("deducted_classical_attainer_adapter")
    boxes = []
    for n in (4, 6, 8, 10):
        target = (0, 2) * (n // 2)
        literal_sources = {x for x in product(range(3), repeat=n) if upper_step(x) == target}
        reconstructed = set()
        independent_sets = 0
        for mask in product((0, 1), repeat=n):
            if any(mask[i] and mask[(i + 1) % n] for i in range(n)):
                continue
            independent_sets += 1
            lower_source = tuple(mask[i] if i % 2 == 0 else 2 - mask[i] for i in range(n))
            reconstructed.add(tuple(2 - v for v in lower_source))
        check(reconstructed == literal_sources, ("complete complemented independent-set adapter", n))
        check(independent_sets == lucas(n), ("classical Lucas value", n))
        boxes.append({"n": n, "independent_sets": independent_sets,
                      "full_labelled_source_bijection": True, "fresh_inverse_credit": 0})
    return boxes


def main():
    local = local_growth_certificate()
    core = core_local_certificate()
    inverse_tables = local_inverse_tables()
    cyclic = full_cycle_and_inverse_boxes(core["traces_n1_to_60"])
    mixed = matrix_word_checks()
    seeds = seed_checks()
    classical = classical_attainer_checks()
    print(json.dumps({
        "status": "PASS", "paper": "P207", "schema": "p207-author-certificate-v1",
        "kind": "author computer-assisted local proof certificate and finite corroboration",
        "literal": "U(x)_i=[x_(i-1)>x_i]+[x_(i+1)>x_i], labelled ternary n>=3",
        "code_provenance": "same author's UGR/LNR implementations adapted and combined; no gate code imported",
        "no_input_file_reads": True, "standard_library_only": True, "declared_scope": SCOPE,
        "local_growth_certificate": local, "core_certificate": core,
        "local_inverse_tables": inverse_tables, "complete_cyclic_source_target_boxes": cyclic,
        "mixed_kernel_checks": mixed, "single_seed_only_checks": seeds,
        "deducted_classical_attainer_checks": classical,
        "all_parameter_claim_boundaries": {
            "proved_global_upper_bound": "H(n)<=4*n+2, nonsharp",
            "proved_seed_height": "h(01^(n-1))=floor(n/2)+1 for n>=4; H(3)=1",
            "sharp_global_height_formula_for_n_ge_4": "NOT CLAIMED",
            "inverse_complement_transport_and_static_decoder": "zero additional contribution credit",
            "retained_shared_inverse_residual": "whole-target comparison and complete equality cases, used once",
            "source_or_independent_review_clearance": "NOT CERTIFIED BY THIS EXECUTABLE",
        },
        "assertions_by_section": dict(sorted(ASSERTIONS.items())),
        "assertions": sum(ASSERTIONS.values()),
        "ordered_checked_record_sha256": RECORD.hexdigest(),
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
