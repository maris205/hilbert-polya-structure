#!/usr/bin/env python3
"""Deterministic exact pilots for the P157--P161 stochastic breadth scout.

All arithmetic is integral or Fraction arithmetic.  Exhaustive enumeration is
used only to attack stated finite consequences; it is not evidence for an
all-parameter theorem.
"""

from collections import Counter, defaultdict
from functools import lru_cache
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial


def fmt_counter(counter):
    return "{" + ",".join(f"{k}:{counter[k]}" for k in sorted(counter, key=str)) + "}"


def fmt_fractions(counter):
    return "{" + ",".join(
        f"{k}:{counter[k].numerator}/{counter[k].denominator}"
        for k in sorted(counter, key=str)
    ) + "}"


def add_scaled(out, source, scale):
    for key, value in source.items():
        out[key] += scale * value


def double_factorial_odd(m):
    if m <= 0:
        return 1
    out = 1
    for x in range(1, m + 1, 2):
        out *= x
    return out


def antipodal_avoiding_words(pair_count, length):
    return sum(
        (-1) ** (pair_count - j) * comb(pair_count, j) * (2 ** j) * (j ** length)
        for j in range(pair_count + 1)
    )


def pilot_cic():
    """Intersect K_n with t independent fair vertex cuts."""
    n, t = 4, 3
    edges = tuple(combinations(range(n), 2))
    states = Counter()
    for cuts in product(range(1 << n), repeat=t):
        kept = frozenset(
            e for e in edges
            if all(((cut >> e[0]) & 1) != ((cut >> e[1]) & 1) for cut in cuts)
        )
        states[kept] += 1
    edge_profile = Counter({len(state): count for state, count in states.items()})
    # Counter comprehension above overwrites equal sizes; aggregate explicitly.
    edge_profile = Counter()
    for state, count in states.items():
        edge_profile[len(state)] += count
    pair_count = 1 << (t - 1)
    empty_formula = antipodal_avoiding_words(pair_count, n)
    assert states[frozenset()] == empty_formula
    target = frozenset({(0, 2), (1, 2)})  # K_{2,1} plus labelled isolate 3.
    fibre_formula = pair_count * 2 * antipodal_avoiding_words(pair_count - 1, 1)
    assert states[target] == fibre_formula
    assert sum(edge_profile.values()) == (1 << n) ** t
    return (
        f"n={n},t={t},edges={fmt_counter(edge_profile)},"
        f"empty={empty_formula},K21+I_fibre={fibre_formula}"
    )


def all_matchings(vertices):
    vertices = tuple(vertices)
    if not vertices:
        return (frozenset(),)
    first = vertices[0]
    out = []
    for i in range(1, len(vertices)):
        second = vertices[i]
        rest = vertices[1:i] + vertices[i + 1 :]
        edge = (min(first, second), max(first, second))
        for matching in all_matchings(rest):
            out.append(frozenset((edge,)) | matching)
    return tuple(out)


def pilot_pmi():
    """Intersect t independent uniform perfect matchings of K_{2n}."""
    n, t = 3, 3
    matchings = all_matchings(range(2 * n))
    total = len(matchings) ** t
    brute = Counter()
    for sequence in product(matchings, repeat=t):
        common = set(sequence[0])
        for matching in sequence[1:]:
            common.intersection_update(matching)
        brute[len(common)] += 1
    assert len(matchings) == double_factorial_odd(2 * n - 1)
    binomial_moments = []
    for k in range(n + 1):
        partial_matchings = factorial(2 * n) // (
            (2 ** k) * factorial(k) * factorial(2 * n - 2 * k)
        )
        completions = double_factorial_odd(2 * n - 2 * k - 1)
        binomial_moments.append(partial_matchings * completions**t)
    inverted = Counter()
    for j in range(n + 1):
        inverted[j] = sum(
            (-1) ** (k - j) * comb(k, j) * binomial_moments[k]
            for k in range(j, n + 1)
        )
    assert brute == inverted and sum(brute.values()) == total
    return f"K{2*n},t={t},matchings={len(matchings)},common_edges={fmt_counter(brute)}"


def pilot_rii():
    """Intersect iid fixed-length intervals on a finite path."""
    n, ell, t = 7, 3, 3
    starts = range(n - ell + 1)
    lengths = Counter()
    target_counts = Counter()
    for seq in product(starts, repeat=t):
        lo, hi = max(seq), min(s + ell - 1 for s in seq)
        if lo <= hi:
            lengths[hi - lo + 1] += 1
            target_counts[(lo, hi)] += 1
        else:
            lengths[0] += 1
    m = n - ell + 1
    predicted = Counter()
    for d in range(m):
        range_count = m if d == 0 else (m - d) * (
            (d + 1) ** t - 2 * d**t + (d - 1) ** t
        )
        predicted[ell - d if d < ell else 0] += range_count
    assert lengths == predicted
    for (lo, hi), count in target_counts.items():
        d = ell - (hi - lo + 1)
        expected = 1 if d == 0 else (d + 1) ** t - 2 * d**t + (d - 1) ** t
        assert count == expected
    return f"path={n},ell={ell},t={t},intersection_length={fmt_counter(lengths)}"


def normalized_vectors(q):
    out = []
    for vec in product(range(q), repeat=3):
        if vec == (0, 0, 0):
            continue
        first = next(x for x in vec if x)
        inv = pow(first, -1, q)
        norm = tuple((x * inv) % q for x in vec)
        if norm not in out:
            out.append(norm)
    return tuple(sorted(out))


def projective_profile(q, t):
    points = normalized_vectors(q)
    lines = normalized_vectors(q)
    incidence = {
        line: frozenset(
            point for point in points
            if sum(a * b for a, b in zip(line, point)) % q == 0
        )
        for line in lines
    }
    brute = Counter()
    for seq in product(lines, repeat=t):
        common = set(points)
        for line in seq:
            common.intersection_update(incidence[line])
        brute[len(common)] += 1
    N = q * q + q + 1
    formula = Counter()
    formula[q + 1] = N
    formula[1] = N * ((q + 1) ** t - (q + 1))
    formula[0] = N**t - formula[q + 1] - formula[1]
    assert brute == formula
    return brute


def pilot_pli():
    """Intersect iid projective lines in PG(2,q), q prime in the pilot."""
    q2 = projective_profile(2, 3)
    q3 = projective_profile(3, 3)
    return f"q=2,t=3,sizes={fmt_counter(q2)};q=3,t=3,sizes={fmt_counter(q3)}"


@lru_cache(maxsize=None)
def ok_corral(a, b):
    if a == 0 or b == 0:
        return {(a, b): Fraction(1)}
    out = defaultdict(Fraction)
    add_scaled(out, ok_corral(a - 1, b), Fraction(b, a + b))
    add_scaled(out, ok_corral(a, b - 1), Fraction(a, a + b))
    return dict(out)


def pilot_okc():
    law = ok_corral(3, 3)
    assert sum(law.values()) == 1
    for (a, b), prob in law.items():
        assert law[(b, a)] == prob and (a == 0 or b == 0)
    survivors = Counter()
    for (a, b), prob in law.items():
        survivors[a + b] += prob
    return f"start=(3,3),survivors={fmt_fractions(survivors)}"


def pilot_cug():
    """Union iid cuts of K_n until vertex bit codes separate."""
    n, t = 4, 3
    edges = tuple(combinations(range(n), 2))
    profile = Counter()
    complete = 0
    for cuts in product(range(1 << n), repeat=t):
        state = {
            e for e in edges
            if any(((cut >> e[0]) & 1) != ((cut >> e[1]) & 1) for cut in cuts)
        }
        profile[len(state)] += 1
        complete += len(state) == len(edges)
    M = 1 << t
    predicted_complete = 1
    for j in range(n):
        predicted_complete *= M - j
    assert complete == predicted_complete
    return f"n={n},t={t},edges={fmt_counter(profile)},complete={complete}"


def prufer_tree(code, n):
    degree = [1] * n
    for x in code:
        degree[x] += 1
    edges = []
    for x in code:
        leaf = next(i for i, d in enumerate(degree) if d == 1)
        edges.append((min(leaf, x), max(leaf, x)))
        degree[leaf] -= 1
        degree[x] -= 1
    last = [i for i, d in enumerate(degree) if d == 1]
    edges.append((min(last), max(last)))
    return frozenset(edges)


def forest_component_sizes(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return None
        parent[ru] = rv
    sizes = Counter(find(i) for i in range(n))
    return tuple(sorted(sizes.values()))


def pilot_sti():
    """Intersect independent Cayley spanning trees."""
    n, t = 4, 2
    all_edges = tuple(combinations(range(n), 2))
    trees = tuple(prufer_tree(code, n) for code in product(range(n), repeat=n - 2))
    assert len(set(trees)) == n ** (n - 2)
    brute = Counter(len(a & b) for a in trees for b in trees)
    moments = []
    for k in range(n):
        total = 0
        for subset in combinations(all_edges, k):
            sizes = forest_component_sizes(n, subset)
            if sizes is None:
                continue
            c = len(sizes)
            if c == 1:
                extensions = 1
            else:
                extensions = n ** (c - 2)
                for size in sizes:
                    extensions *= size
            total += extensions**t
        moments.append(total)
    inverted = Counter()
    for j in range(n):
        inverted[j] = sum(
            (-1) ** (k - j) * comb(k, j) * moments[k]
            for k in range(j, n)
        )
    assert brute == inverted
    return f"K{n},t={t},trees={len(trees)},common_edges={fmt_counter(brute)}"


@lru_cache(maxsize=None)
def rsa_path(mask, n):
    active = [i for i in range(n - 1) if not (mask >> i) & 1 and not (mask >> (i + 1)) & 1]
    if not active:
        return {(mask, 0): Fraction(1)}
    out = defaultdict(Fraction)
    for i in active:
        child = rsa_path(mask | (1 << i) | (1 << (i + 1)), n)
        for (terminal, steps), prob in child.items():
            out[(terminal, steps + 1)] += prob / len(active)
    return dict(out)


def pilot_rsa():
    n = 7
    law = rsa_path(0, n)
    assert sum(law.values()) == 1
    dimers = Counter()
    for (terminal, steps), prob in law.items():
        assert all((terminal >> i) & 1 or (terminal >> (i + 1)) & 1 for i in range(n - 1))
        assert terminal.bit_count() == 2 * steps
        dimers[steps] += prob
    return f"path={n},jammed_dimers={fmt_fractions(dimers)},terminal_masks={len(law)}"


@lru_cache(maxsize=None)
def ksa_labeled(parts, visited, last):
    choices = [v for v, p in enumerate(parts) if not (visited >> v) & 1 and p != parts[last]]
    if not choices:
        return {(visited.bit_count(), parts[last]): Fraction(1)}
    out = defaultdict(Fraction)
    for v in choices:
        add_scaled(out, ksa_labeled(parts, visited | (1 << v), v), Fraction(1, len(choices)))
    return dict(out)


@lru_cache(maxsize=None)
def ksa_aggregated(rem, current_part, visited_count):
    available = sum(count for p, count in enumerate(rem) if p != current_part)
    if not available:
        return {(visited_count, current_part): Fraction(1)}
    out = defaultdict(Fraction)
    for p, count in enumerate(rem):
        if p == current_part or count == 0:
            continue
        nxt = list(rem)
        nxt[p] -= 1
        add_scaled(
            out,
            ksa_aggregated(tuple(nxt), p, visited_count + 1),
            Fraction(count, available),
        )
    return dict(out)


def pilot_kgt():
    sizes = (2, 2, 3)
    parts = tuple(p for p, size in enumerate(sizes) for _ in range(size))
    labeled = ksa_labeled(parts, 1, 0)
    rem = (sizes[0] - 1, sizes[1], sizes[2])
    aggregated = ksa_aggregated(rem, 0, 1)
    assert labeled == aggregated and sum(labeled.values()) == 1
    length_law = Counter()
    for (length, _), prob in labeled.items():
        length_law[length] += prob
    return f"K_(2,2,3),start_part=0,terminal_length={fmt_fractions(length_law)}"


@lru_cache(maxsize=None)
def equalize_path(state):
    active = [i for i in range(len(state) - 1) if abs(state[i] - state[i + 1]) >= 2]
    if not active:
        return {(state, 0): Fraction(1)}
    out = defaultdict(Fraction)
    for i in active:
        total = state[i] + state[i + 1]
        low, high = total // 2, (total + 1) // 2
        options = {(low, high)} if low == high else {(low, high), (high, low)}
        for pair in options:
            nxt = list(state)
            nxt[i], nxt[i + 1] = pair
            for (terminal, steps), prob in equalize_path(tuple(nxt)).items():
                out[(terminal, steps + 1)] += prob / (len(active) * len(options))
    return dict(out)


def pilot_ale():
    start = (4, 0, 3, 0)
    law = equalize_path(start)
    assert sum(law.values()) == 1
    step_law = Counter()
    for (terminal, steps), prob in law.items():
        assert sum(terminal) == sum(start)
        assert max(abs(a - b) for a, b in zip(terminal, terminal[1:])) <= 1
        step_law[steps] += prob
    return f"start={start},steps={fmt_fractions(step_law)},terminals={len(law)}"


def pilot_hfc():
    """Contract an anchored hypercube face to the sampled vertex hull."""
    d, t = 4, 3
    dimension = Counter()
    for rounds in product(range(1 << d), repeat=t):
        free = (1 << d) - 1
        for sampled_bits in rounds:
            free &= sampled_bits
        dimension[free.bit_count()] += 1
    predicted = Counter({k: comb(d, k) * (2**t - 1) ** (d - k) for k in range(d + 1)})
    assert dimension == predicted
    return f"d={d},t={t},face_dimension={fmt_counter(dimension)}"


def inversion_count(word):
    return sum(word[i] == "1" and word[j] == "0" for i in range(len(word)) for j in range(i + 1, len(word)))


@lru_cache(maxsize=None)
def tasep_histories(word):
    active = [i for i in range(len(word) - 1) if word[i : i + 2] == "10"]
    if not active:
        return 1
    total = 0
    for i in active:
        nxt = word[:i] + "01" + word[i + 2 :]
        assert inversion_count(nxt) == inversion_count(word) - 1
        total += tasep_histories(nxt)
    return total


def ferrers_syt_count(partition):
    cells = [(i, j) for i, row in enumerate(partition) for j in range(row)]
    hooks = 1
    for i, j in cells:
        right = partition[i] - j - 1
        below = sum(j < partition[ii] for ii in range(i + 1, len(partition)))
        hooks *= 1 + right + below
    return factorial(len(cells)) // hooks


def pilot_tas():
    word = "110100"
    partition = tuple(sum(c == "0" for c in word[i + 1 :]) for i, x in enumerate(word) if x == "1")
    inv = inversion_count(word)
    histories = tasep_histories(word)
    assert histories == ferrers_syt_count(partition)
    return f"word={word},clock={inv},shape={partition},histories={histories}"


def pilot_arc():
    n, ell, t = 7, 3, 3
    arcs = tuple(sum(1 << ((s + j) % n) for j in range(ell)) for s in range(n))
    coverage = Counter()
    full = 0
    for seq in product(arcs, repeat=t):
        state = 0
        for arc in seq:
            state |= arc
        coverage[state.bit_count()] += 1
        full += state == (1 << n) - 1
    ie_full = 0
    for missing in range(1 << n):
        allowed = sum((arc & missing) == 0 for arc in arcs)
        ie_full += (-1) ** missing.bit_count() * allowed**t
    assert full == ie_full
    return f"C{n},ell={ell},t={t},covered={fmt_counter(coverage)},full={full}"


def cycle_block_profile(n, contracted):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for edge in contracted:
        a, b = edge, (edge + 1) % n
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
    return tuple(sorted(Counter(find(i) for i in range(n)).values()))


def pilot_cec():
    n, k = 6, 3
    ordered = Counter(cycle_block_profile(n, seq) for seq in permutations(range(n), k))
    subsets = Counter(cycle_block_profile(n, seq) for seq in combinations(range(n), k))
    assert ordered == Counter({profile: count * factorial(k) for profile, count in subsets.items()})
    return f"C{n},k={k},block_profiles={fmt_counter(ordered)}"


def pilot_phg():
    n, start, t = 7, 3, 3
    targets = Counter()
    for seq in product(range(n), repeat=t):
        lo, hi = start, start
        for v in seq:
            lo, hi = min(lo, v), max(hi, v)
        targets[(lo, hi)] += 1
    full = targets[(0, n - 1)]
    predicted_full = n**t - 2 * (n - 1) ** t + (n - 2) ** t
    assert full == predicted_full
    for (lo, hi), count in targets.items():
        width = hi - lo + 1
        if lo < start < hi:
            predicted = width**t - 2 * (width - 1) ** t + (width - 2) ** t
        elif lo == start == hi:
            predicted = 1
        else:
            predicted = width**t - (width - 1) ** t
        assert count == predicted
    return f"path={n},start={start},t={t},targets={len(targets)},full={full}"


def bootstrap_close(mask, n):
    while True:
        add = 0
        for v in range(n):
            if (mask >> v) & 1:
                continue
            if (mask >> ((v - 1) % n)) & 1 and (mask >> ((v + 1) % n)) & 1:
                add |= 1 << v
        if not add:
            return mask
        mask |= add


@lru_cache(maxsize=None)
def bootstrap_seed_law(mask, n):
    full = (1 << n) - 1
    mask = bootstrap_close(mask, n)
    if mask == full:
        return {0: Fraction(1)}
    choices = [v for v in range(n) if not (mask >> v) & 1]
    out = defaultdict(Fraction)
    for v in choices:
        for steps, prob in bootstrap_seed_law(mask | (1 << v), n).items():
            out[steps + 1] += prob / len(choices)
    return dict(out)


def pilot_bpc():
    n = 7
    dp = bootstrap_seed_law(0, n)
    perm_counts = Counter()
    full = (1 << n) - 1
    for order in permutations(range(n)):
        mask, seeds = 0, 0
        while mask != full:
            v = next(v for v in order if not (mask >> v) & 1)
            mask = bootstrap_close(mask | (1 << v), n)
            seeds += 1
        perm_counts[seeds] += 1
    from_perms = {steps: Fraction(count, factorial(n)) for steps, count in perm_counts.items()}
    assert dp == from_perms and sum(dp.values()) == 1
    return f"C{n},threshold=2,seeds={fmt_fractions(Counter(dp))}"


def is_linear_extension(order, predecessors):
    position = {x: i for i, x in enumerate(order)}
    return all(position[p] < position[x] for x, preds in enumerate(predecessors) for p in preds)


def extension_probability(order, predecessors):
    remaining = set(range(len(order)))
    probability = Fraction(1)
    for chosen in order:
        sources = [x for x in remaining if predecessors[x].isdisjoint(remaining)]
        if chosen not in sources:
            return Fraction(0)
        probability /= len(sources)
        remaining.remove(chosen)
    return probability


def pilot_psd():
    predecessors = (frozenset(), frozenset({0}), frozenset({0}), frozenset({1, 2}), frozenset())
    laws = {}
    for order in permutations(range(5)):
        if is_linear_extension(order, predecessors):
            laws[order] = extension_probability(order, predecessors)
    assert sum(laws.values()) == 1
    multiplicities = Counter(laws.values())
    rendered = Counter({f"{p.numerator}/{p.denominator}": count for p, count in multiplicities.items()})
    return f"five_point_DAG,extensions={len(laws)},probability_multiplicity={fmt_counter(rendered)}"


@lru_cache(maxsize=None)
def rectangle_delete_law(rows, cols):
    if rows == 0:
        return {("R", cols, 0): Fraction(1)}
    if cols == 0:
        return {("C", rows, 0): Fraction(1)}
    out = defaultdict(Fraction)
    for (winner, survivors, steps), prob in rectangle_delete_law(rows - 1, cols).items():
        out[(winner, survivors, steps + 1)] += Fraction(rows, rows + cols) * prob
    for (winner, survivors, steps), prob in rectangle_delete_law(rows, cols - 1).items():
        out[(winner, survivors, steps + 1)] += Fraction(cols, rows + cols) * prob
    return dict(out)


def pilot_rcd():
    rows, cols = 3, 2
    dp = rectangle_delete_law(rows, cols)
    counts = Counter()
    labels = tuple(("R", i) for i in range(rows)) + tuple(("C", j) for j in range(cols))
    for order in permutations(labels):
        rleft, cleft = rows, cols
        for step, (kind, _) in enumerate(order, 1):
            if kind == "R":
                rleft -= 1
            else:
                cleft -= 1
            if rleft == 0 or cleft == 0:
                key = ("R", cleft, step) if rleft == 0 else ("C", rleft, step)
                counts[key] += 1
                break
    from_perms = {key: Fraction(count, factorial(rows + cols)) for key, count in counts.items()}
    assert dp == from_perms and sum(dp.values()) == 1
    marginal = Counter()
    for (winner, survivors, _), prob in dp.items():
        marginal[f"{winner}{survivors}"] += prob
    return f"{rows}x{cols},axis_survivors={fmt_fractions(marginal)}"


def one_dimensional_distribution(n, t):
    law = {n: Fraction(1)}
    for _ in range(t):
        nxt = defaultdict(Fraction)
        for state, prob in law.items():
            for target in range(1, state + 1):
                nxt[target] += prob / state
        law = dict(nxt)
    return law


def rectangle_distribution(a, b, t):
    law = {(a, b): Fraction(1)}
    for _ in range(t):
        nxt = defaultdict(Fraction)
        for (x, y), prob in law.items():
            for i in range(1, x + 1):
                for j in range(1, y + 1):
                    nxt[(i, j)] += prob / (x * y)
        law = dict(nxt)
    return law


@lru_cache(maxsize=None)
def green_visits(n, k):
    if n < k:
        return Fraction(0)
    if n == 1:
        return Fraction(0)
    immediate = Fraction(int(n == k))
    # Resolve the self-loop algebraically.
    lower = sum((green_visits(j, k) for j in range(1, n)), Fraction(0))
    return (immediate + lower / n) / (1 - Fraction(1, n))


def pilot_rcr():
    """Sample a cell and keep its origin-anchored subrectangle."""
    a, b, t = 4, 3, 4
    rect = rectangle_distribution(a, b, t)
    xlaw, ylaw = one_dimensional_distribution(a, t), one_dimensional_distribution(b, t)
    product_law = {(x, y): px * py for x, px in xlaw.items() for y, py in ylaw.items()}
    assert rect == product_law
    absorbed = rect[(1, 1)]
    assert absorbed == xlaw[1] * ylaw[1]
    green = tuple(green_visits(5, k) for k in range(2, 6))
    expected = Fraction(1) + sum(Fraction(1, j) for j in range(1, 5))
    # PGF z(n-1)!/prod_{k=2}^n(k-z) gives this mean at z=1.
    direct_expected = sum(green_visits(5, k) for k in range(2, 6))
    assert direct_expected == expected
    assert green == (Fraction(1), Fraction(1, 2), Fraction(1, 3), Fraction(5, 4))
    return (
        f"start={a}x{b},t={t},P_absorbed={absorbed.numerator}/{absorbed.denominator},"
        f"H5_mean={expected.numerator}/{expected.denominator},"
        f"Green5_to_2..5={','.join(str(x) for x in green)}"
    )


PILOTS = (
    ("CIC", pilot_cic, "SURVIVE_OWNER_THIN"),
    ("PMI", pilot_pmi, "SURVIVE_OWNER_AMBER"),
    ("RII", pilot_rii, "RESERVE_OWNER_THIN"),
    ("PLI", pilot_pli, "KILL_OWNER_RANK"),
    ("OKC", pilot_okc, "KILL_DIRECT_OWNER"),
    ("CUG", pilot_cug, "KILL_BIRTHDAY_REFINEMENT"),
    ("STI", pilot_sti, "KILL_DIRECT_OWNER_ENGINE"),
    ("RSA", pilot_rsa, "KILL_CLASSICAL_RSA"),
    ("KGT", pilot_kgt, "KILL_WEAK_SILHOUETTE"),
    ("ALE", pilot_ale, "KILL_WEAK_TEMPORAL_AXIS"),
    ("HFC", pilot_hfc, "KILL_BOOLEAN_PRODUCT"),
    ("TAS", pilot_tas, "KILL_TASEP_HOOK"),
    ("ARC", pilot_arc, "KILL_COVERAGE_ENGINE"),
    ("CEC", pilot_cec, "KILL_OCCUPIED_COALESCENCE"),
    ("PHG", pilot_phg, "KILL_SAMPLE_RANGE"),
    ("BPC", pilot_bpc, "KILL_BOOTSTRAP_CLOSURE"),
    ("PSD", pilot_psd, "KILL_LINEAR_EXTENSIONS"),
    ("RCD", pilot_rcd, "KILL_QUOTA_EXPOSURE"),
    ("RCR", pilot_rcr, "SURVIVE_OWNER_THIN"),
)


def main():
    print("P157-P161 STOCHASTIC/GRAPH/SPATIAL BREADTH SCOUT")
    print("MODE exact deterministic Fraction/integer arithmetic; enumeration=falsification only")
    passed = 0
    for index, (name, pilot, verdict) in enumerate(PILOTS, 1):
        signature = pilot()
        passed += 1
        print(f"[{index:02d} {name}] PASS {signature} | {verdict}")
    print(f"SUMMARY pilots={len(PILOTS)} pass={passed} survive=3 reserve=1 kill=15")
    print("BATCH_RULE CIC, PMI, and RII share an intersection engine: advance at most one without a separation proof")
    print("EVIDENCE_BOUNDARY finite enumeration attacks consequences; it proves no all-parameter claim")
    print("EXTERNAL_STATUS HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
