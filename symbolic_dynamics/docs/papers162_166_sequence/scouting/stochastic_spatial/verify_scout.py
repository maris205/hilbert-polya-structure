#!/usr/bin/env python3
"""Exact breadth falsifier for the P162--P166 stochastic/spatial lane.

The program is deliberately self-contained.  It imports no paper or earlier
scout code, uses no pseudorandomness, floating point, third-party package, or
network service, and checks sixteen literal systems with integer/Fraction
arithmetic.  Exhaustion is counterexample pressure, not a proof of novelty.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from functools import reduce
from itertools import combinations, product
from math import comb, factorial, gcd


ASSERTIONS = 0


def require(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def harmonic(n):
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))


def iterate_distribution(start, transition, steps):
    law = {start: Fraction(1)}
    for _ in range(steps):
        nxt = defaultdict(Fraction)
        for state, mass in law.items():
            for target, probability in transition(state).items():
                nxt[target] += mass * probability
        law = dict(nxt)
    return law


def rank_mod(rows, q):
    a = [list(row) for row in rows if any(x % q for x in row)]
    if not a:
        return 0
    columns = len(a[0])
    rank = 0
    for column in range(columns):
        pivot = next((i for i in range(rank, len(a)) if a[i][column] % q), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][column] % q, -1, q)
        a[rank] = [(x * inv) % q for x in a[rank]]
        for i in range(len(a)):
            if i != rank and a[i][column] % q:
                factor = a[i][column] % q
                a[i] = [(x - factor * y) % q for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def gaussian_binomial(n, k, q):
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    answer = 1
    for i in range(k):
        answer = answer * (q ** (n - i) - 1) // (q ** (k - i) - 1)
    return answer


def spanning_nonzero_tuples(q, dimension, length):
    total = 0
    for j in range(dimension + 1):
        codimension = dimension - j
        total += (
            gaussian_binomial(dimension, j, q)
            * (-1) ** codimension
            * q ** comb(codimension, 2)
            * (q**j - 1) ** length
        )
    return total


def spanning_all_tuples(q, dimension, length):
    total = 0
    for j in range(dimension + 1):
        codimension = dimension - j
        total += (
            gaussian_binomial(dimension, j, q)
            * (-1) ** codimension
            * q ** comb(codimension, 2)
            * q ** (j * length)
        )
    return total


# DCI: intersections of centralizers in odd dihedral groups.
def dihedral_mul(x, y, n):
    a, b = x
    c, d = y
    return ((a + (-1 if b else 1) * c) % n, (b + d) % 2)


def dci_checks():
    signature = None
    for n in (3, 5, 7, 9):
        group = tuple((a, b) for b in (0, 1) for a in range(n))
        identity = (0, 0)
        rotation_group = frozenset((a, 0) for a in range(n))
        centralizers = {}
        for x in group:
            centralizers[x] = frozenset(
                y for y in group if dihedral_mul(x, y, n) == dihedral_mul(y, x, n)
            )
        for length in range(1, 5):
            observed = Counter()
            for word in product(group, repeat=length):
                meet = frozenset(group)
                for x in word:
                    meet &= centralizers[x]
                if meet == frozenset(group):
                    key = "G"
                elif meet == rotation_group:
                    key = "A"
                elif meet == frozenset((identity,)):
                    key = "Z"
                else:
                    reflections = [x for x in meet if x[1]]
                    require(len(meet) == 2 and len(reflections) == 1, "DCI centralizer type")
                    key = f"C{reflections[0][0]}"
                observed[key] += 1
            require(observed["G"] == 1, "DCI whole-group fibre")
            require(observed["A"] == n**length - 1, "DCI rotation fibre")
            for j in range(n):
                require(observed[f"C{j}"] == 2**length - 1, "DCI reflection fibre")
            expected_center = (2 * n) ** length - n**length - n * (2**length - 1)
            require(observed["Z"] == expected_center, "DCI centre fibre")
            require(sum(observed.values()) == (2 * n) ** length, "DCI mass")
            survival = n**length + n * (2**length - 1)
            require(sum(v for k, v in observed.items() if k != "Z") == survival, "DCI survival")
            if n == 5 and length == 3:
                signature = (observed["G"], observed["A"], 2**length - 1, observed["Z"])
    require(signature == (1, 124, 7, 840), "DCI signature")
    return signature


# LSC: uniform lattice-simplex contraction.
def simplex_points(dimension, radius):
    return tuple(x for x in product(range(radius + 1), repeat=dimension) if sum(x) <= radius)


def simplex_weight(dimension, shell):
    return comb(shell + dimension - 1, dimension - 1)


def simplex_total(dimension, radius):
    return comb(radius + dimension, dimension)


def lsc_transition(dimension, radius):
    denominator = simplex_total(dimension, radius)
    return {k: Fraction(simplex_weight(dimension, k), denominator) for k in range(radius + 1)}


def lsc_pgf_formula(dimension, radius, z):
    answer = z
    for j in range(1, radius + 1):
        answer *= Fraction(j, 1) / (j + dimension * (1 - z))
    return answer


def lsc_checks():
    signature = None
    for dimension in range(1, 5):
        means = [Fraction(0)]
        for radius in range(1, 8):
            points = simplex_points(dimension, radius)
            shell_hist = Counter(map(sum, points))
            require(len(points) == simplex_total(dimension, radius), "LSC simplex size")
            for k in range(radius + 1):
                require(shell_hist[k] == simplex_weight(dimension, k), "LSC shell size")
            transition = lsc_transition(dimension, radius)
            require(sum(transition.values()) == 1, "LSC row mass")
            p_self = transition[radius]
            mean = (1 + sum(transition[k] * means[k] for k in range(radius))) / (1 - p_self)
            means.append(mean)
            require(mean == 1 + dimension * harmonic(radius), "LSC mean")
            for z in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
                pgfs = [Fraction(1)]
                for m in range(1, radius + 1):
                    row = lsc_transition(dimension, m)
                    value = z * sum(row[k] * pgfs[k] for k in range(m)) / (1 - z * row[m])
                    pgfs.append(value)
                require(pgfs[radius] == lsc_pgf_formula(dimension, radius, z), "LSC PGF")
        for target in range(1, 7):
            green = [Fraction(0)] * 8
            green[target] = Fraction(target + dimension, target)
            for radius in range(target + 1, 8):
                row = lsc_transition(dimension, radius)
                green[radius] = sum(row[k] * green[k] for k in range(radius)) / (1 - row[radius])
                require(green[radius] == Fraction(dimension, target), "LSC Green")
        if dimension == 2:
            signature = (means[3], lsc_pgf_formula(2, 3, Fraction(1, 2)), Fraction(2, 1))
    require(signature == (Fraction(14, 3), Fraction(1, 8), Fraction(2)), "LSC signature")
    return signature


# QHI: repeated random-hyperplane intersection over prime fields.
def qhi_checks():
    signature = None
    for q, dimension, max_length in ((2, 2, 4), (2, 3, 4), (2, 4, 4), (3, 2, 3), (3, 3, 3)):
        vectors = tuple(v for v in product(range(q), repeat=dimension) if any(v))
        for length in range(1, max_length + 1):
            observed = Counter()
            for rows in product(vectors, repeat=length):
                observed[rank_mod(rows, q)] += 1
            for rank in range(dimension + 1):
                expected = gaussian_binomial(dimension, rank, q) * spanning_nonzero_tuples(q, rank, length)
                require(observed[rank] == expected, "QHI rank distribution")
            require(sum(observed.values()) == len(vectors) ** length, "QHI mass")
            if (q, dimension, length) == (2, 3, 3):
                signature = tuple(observed[r] for r in range(4))
    require(signature == (0, 7, 168, 168), "QHI signature")
    return signature


# HCI: common centralizers in the finite Heisenberg group, projected to rank.
def hci_checks():
    signature = None
    for q in (2, 3, 5):
        vectors = tuple(product(range(q), repeat=2))
        vectors = tuple(vectors)
        for length in range(1, 5):
            observed = Counter(rank_mod(rows, q) for rows in product(vectors, repeat=length))
            for rank in range(3):
                expected = gaussian_binomial(2, rank, q) * spanning_all_tuples(q, rank, length)
                require(observed[rank] == expected, "HCI projected-rank law")
            require(sum(observed.values()) == q ** (2 * length), "HCI mass")
            if (q, length) == (3, 3):
                signature = tuple(observed[r] for r in range(3))
    require(signature == (1, 104, 624), "HCI signature")
    return signature


# ORW: random vertex replacement inside a finite-field orthocentric quartet.
def dot(u, v, p):
    return sum(a * b for a, b in zip(u, v)) % p


def sub(u, v, p):
    return tuple((a - b) % p for a, b in zip(u, v))


def orthocenter_bruteforce(a, b, c, p):
    answers = []
    for h in product(range(p), repeat=2):
        if dot(sub(h, a, p), sub(b, c, p), p) == 0 and dot(sub(h, b, p), sub(a, c, p), p) == 0:
            answers.append(h)
    require(len(answers) == 1, "ORW unique orthocenter")
    return answers[0]


def orw_checks():
    p = 7
    quartet = ((0, 0), (1, 0), (2, 1), (2, 5))
    for missing in range(4):
        triangle = tuple(quartet[i] for i in range(4) if i != missing)
        require(orthocenter_bruteforce(*triangle, p) == quartet[missing], "ORW quartet identity")
    law = [1, 0, 0, 0]
    signature = None
    for t in range(13):
        same = (3**t + 3 * (-1) ** t) // 4
        other = (3**t - (-1) ** t) // 4
        require(law[0] == same, "ORW return count")
        for value in law[1:]:
            require(value == other, "ORW off-diagonal count")
        require(sum(law) == 3**t, "ORW mass")
        if t == 4:
            signature = tuple(law)
        nxt = [0] * 4
        for i, count in enumerate(law):
            for j in range(4):
                if i != j:
                    nxt[j] += count
        law = nxt
    require(signature == (21, 20, 20, 20), "ORW signature")
    return signature


# KMP: iid-letter prefix-automaton hitting.
def prefix_transition(pattern, state, letter):
    word = pattern[:state] + (letter,)
    for length in range(min(len(pattern), len(word)), -1, -1):
        if word[-length:] == pattern[:length] if length else True:
            return length
    raise AssertionError("unreachable")


def solve_linear(matrix, rhs):
    n = len(rhs)
    a = [list(map(Fraction, matrix[i])) + [Fraction(rhs[i])] for i in range(n)]
    for column in range(n):
        pivot = next(i for i in range(column, n) if a[i][column])
        a[column], a[pivot] = a[pivot], a[column]
        scale = a[column][column]
        a[column] = [x / scale for x in a[column]]
        for row in range(n):
            if row != column and a[row][column]:
                scale = a[row][column]
                a[row] = [x - scale * y for x, y in zip(a[row], a[column])]
    return [a[i][-1] for i in range(n)]


def pattern_mean(pattern, alphabet_size):
    n = len(pattern)
    matrix = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    rhs = [Fraction(1) for _ in range(n)]
    for state in range(n):
        for letter in range(alphabet_size):
            target = prefix_transition(pattern, state, letter)
            if target < n:
                matrix[state][target] -= Fraction(1, alphabet_size)
    return solve_linear(matrix, rhs)[0]


def border_lengths(pattern):
    return [k for k in range(1, len(pattern) + 1) if pattern[:k] == pattern[-k:]]


def first_hit_counts(pattern, alphabet_size, horizon):
    n = len(pattern)
    active = Counter({0: 1})
    hits = []
    for _ in range(horizon):
        nxt = Counter()
        hit = 0
        for state, count in active.items():
            for letter in range(alphabet_size):
                target = prefix_transition(pattern, state, letter)
                if target == n:
                    hit += count
                else:
                    nxt[target] += count
        hits.append(hit)
        active = nxt
    return tuple(hits)


def kmp_checks():
    signature = None
    for alphabet_size, max_length in ((2, 5), (3, 4)):
        for length in range(1, max_length + 1):
            for pattern in product(range(alphabet_size), repeat=length):
                mean = pattern_mean(pattern, alphabet_size)
                expected_mean = sum((alphabet_size**k for k in border_lengths(pattern)), 0)
                require(mean == expected_mean, "KMP border mean")
                horizon = length + 4
                dynamic = first_hit_counts(pattern, alphabet_size, horizon)
                brute = []
                for t in range(1, horizon + 1):
                    count = 0
                    for word in product(range(alphabet_size), repeat=t):
                        first = next((i + length for i in range(t - length + 1) if word[i : i + length] == pattern), None)
                        if first == t:
                            count += 1
                    brute.append(count)
                require(dynamic == tuple(brute), "KMP first-hit distribution")
                if alphabet_size == 2 and pattern == (0, 1, 0):
                    signature = (mean, dynamic)
    require(signature[0] == 10, "KMP signature mean")
    return signature


# GSW: random star toggles on labelled graphs.
def star_mask(n, vertex):
    bit = 0
    index = 0
    for i in range(n):
        for j in range(i + 1, n):
            if i == vertex or j == vertex:
                bit |= 1 << index
            index += 1
    return bit


def parity_walk_count(n, t, x):
    numerator = 0
    for y in range(1 << n):
        sign = -1 if (x & y).bit_count() % 2 else 1
        numerator += sign * (n - 2 * y.bit_count()) ** t
    require(numerator % (1 << n) == 0, "GSW Fourier integrality")
    return numerator // (1 << n)


def gsw_checks():
    signature = None
    for n in range(2, 8):
        stars = [star_mask(n, v) for v in range(n)]
        require(len({reduce(int.__xor__, (stars[v] for v in range(n) if (s >> v) & 1), 0) for s in range(1 << n)}) == 1 << (n - 1), "GSW cut space")
        law = Counter({0: 1})
        for t in range(8):
            for subset in range(1 << (n - 1)):
                cut = reduce(int.__xor__, (stars[v + 1] for v in range(n - 1) if (subset >> v) & 1), 0)
                x = subset << 1
                expected = parity_walk_count(n, t, x) + parity_walk_count(n, t, x ^ ((1 << n) - 1))
                require(law[cut] == expected, "GSW endpoint count")
            require(sum(law.values()) == n**t, "GSW mass")
            if n == 5 and t == 4:
                signature = law[0]
            nxt = Counter()
            for state, count in law.items():
                for star in stars:
                    nxt[state ^ star] += count
            law = nxt
    require(signature == 65, "GSW signature")
    return signature


# TTW: random triangle-boundary toggles on graphs.
def complete_graph_edges(n):
    return {(i, j): k for k, (i, j) in enumerate(combinations(range(n), 2))}


def triangle_masks(n):
    edges = complete_graph_edges(n)
    masks = []
    for tri in combinations(range(n), 3):
        mask = 0
        for i, j in combinations(tri, 2):
            mask |= 1 << edges[min(i, j), max(i, j)]
        masks.append(mask)
    return masks


def graph_degree_parity(mask, n):
    edges = complete_graph_edges(n)
    parity = [0] * n
    for (i, j), bit in edges.items():
        if (mask >> bit) & 1:
            parity[i] ^= 1
            parity[j] ^= 1
    return tuple(parity)


def ttw_checks():
    signature = None
    for n in range(3, 7):
        triangles = triangle_masks(n)
        group = {0}
        for generator in triangles:
            group |= {x ^ generator for x in tuple(group)}
        dimension = comb(n - 1, 2)
        require(len(group) == 1 << dimension, "TTW cycle-space size")
        for state in group:
            require(not any(graph_degree_parity(state, n)), "TTW degree invariant")
        edges = complete_graph_edges(n)
        representatives = []
        free_edges = [edges[i, j] for i, j in combinations(range(1, n), 2)]
        for bits in range(1 << len(free_edges)):
            representatives.append(sum((1 << edge for k, edge in enumerate(free_edges) if (bits >> k) & 1), 0))
        law = Counter({0: 1})
        number_triangles = len(triangles)
        for t in range(6):
            for target in group:
                spectral_sum = 0
                for rep in representatives:
                    odd = sum(((rep & tri).bit_count() % 2) for tri in triangles)
                    sign = -1 if (rep & target).bit_count() % 2 else 1
                    spectral_sum += sign * (number_triangles - 2 * odd) ** t
                require(spectral_sum % len(group) == 0, "TTW Fourier integrality")
                require(law[target] == spectral_sum // len(group), "TTW Fourier endpoint")
            require(sum(law.values()) == number_triangles**t, "TTW mass")
            if n == 5 and t == 4:
                signature = law[0]
            nxt = Counter()
            for state, count in law.items():
                for tri in triangles:
                    nxt[state ^ tri] += count
            law = nxt
    require(signature is not None and signature > 0, "TTW signature")
    return signature


# PTW: plaquette-boundary toggles on a toroidal square cellulation.
def torus_plaquettes(rows, columns):
    # horizontal and vertical edge indices
    h = {(i, j): i * columns + j for i in range(rows) for j in range(columns)}
    offset = rows * columns
    v = {(i, j): offset + i * columns + j for i in range(rows) for j in range(columns)}
    faces = []
    for i in range(rows):
        for j in range(columns):
            mask = 0
            for edge in (h[i, j], v[i, (j + 1) % columns], h[(i + 1) % rows, j], v[i, j]):
                mask ^= 1 << edge
            faces.append(mask)
    return faces


def ptw_checks():
    signature = None
    for rows, columns in ((3, 3), (3, 4)):
        faces = torus_plaquettes(rows, columns)
        face_count = rows * columns
        require(reduce(int.__xor__, faces, 0) == 0, "PTW global face relation")
        span = {0}
        for face in faces:
            span |= {x ^ face for x in tuple(span)}
        require(len(span) == 1 << (face_count - 1), "PTW boundary-space rank")
        law = Counter({0: 1})
        parity_law = Counter({0: 1})
        for t in range(5):
            projected = Counter()
            for parity, count in parity_law.items():
                state = reduce(int.__xor__, (faces[i] for i in range(face_count) if (parity >> i) & 1), 0)
                projected[state] += count
            require(projected == law, "PTW face-parity conjugacy")
            require(sum(law.values()) == face_count**t, "PTW mass")
            if (rows, columns, t) == (3, 3, 4):
                signature = law[0]
            nxt = Counter()
            nxt_parity = Counter()
            for state, count in law.items():
                for face in faces:
                    nxt[state ^ face] += count
            for parity, count in parity_law.items():
                for i in range(face_count):
                    nxt_parity[parity ^ (1 << i)] += count
            law, parity_law = nxt, nxt_parity
    require(signature == 225, "PTW signature")
    return signature


# CDP: choose a forward/backward cyclic difference operator over F_2.
def rotate_left_bits(x, n, amount=1):
    amount %= n
    mask = (1 << n) - 1
    return ((x << amount) & mask) | (x >> (n - amount) if amount else 0)


def cyclic_difference(x, n, direction):
    return x ^ rotate_left_bits(x, n, direction)


def cdp_checks():
    signature = None
    for n in (2, 4, 8):
        for x in range(1 << n):
            plus_iterates = [x]
            for _ in range(n):
                plus_iterates.append(cyclic_difference(plus_iterates[-1], n, 1))
            require(plus_iterates[n] == 0, "CDP nilpotence")
            law = Counter({x: 1})
            for t in range(n + 1):
                expected = Counter()
                y = plus_iterates[t]
                for backward_count in range(t + 1):
                    target = rotate_left_bits(y, n, -backward_count)
                    expected[target] += comb(t, backward_count)
                require(law == expected, "CDP shift-binomial law")
                if n == 8 and x == 1 and t == 3:
                    signature = tuple(sorted(law.values()))
                nxt = Counter()
                for state, count in law.items():
                    nxt[cyclic_difference(state, n, 1)] += count
                    nxt[cyclic_difference(state, n, -1)] += count
                law = nxt
        for t in range(n + 1):
            images = Counter()
            for x in range(1 << n):
                y = x
                for _ in range(t):
                    y = cyclic_difference(y, n, 1)
                images[y] += 1
            require(len(images) == 1 << (n - t), "CDP image size")
            require(set(images.values()) == {1 << t}, "CDP uniform fibres")
    require(signature == (1, 1, 3, 3), "CDP signature")
    return signature


# UDC: uniform-divisor contraction in exponent coordinates.
def uniform_chain_matrix(maximum):
    matrix = [[Fraction(0) for _ in range(maximum + 1)] for _ in range(maximum + 1)]
    for state in range(maximum + 1):
        for target in range(state + 1):
            matrix[state][target] = Fraction(1, state + 1)
    return matrix


def matrix_multiply(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0)) for j in range(len(b[0]))] for i in range(len(a))]


def matrix_power(matrix, exponent):
    size = len(matrix)
    result = [[Fraction(int(i == j)) for j in range(size)] for i in range(size)]
    base = matrix
    while exponent:
        if exponent & 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        exponent //= 2
    return result


def udc_checks():
    signature = None
    profiles = ((1,), (2,), (2, 3), (1, 2, 3), (2, 2, 3, 4))
    for profile in profiles:
        matrices = [uniform_chain_matrix(e) for e in profile]
        state_space = tuple(product(*(range(e + 1) for e in profile)))
        start = profile
        def transition(state):
            denominator = 1
            for e in state:
                denominator *= e + 1
            return {target: Fraction(1, denominator) for target in product(*(range(e + 1) for e in state))}
        for t in range(6):
            literal = iterate_distribution(start, transition, t)
            powers = [matrix_power(matrix, t) for matrix in matrices]
            for target in state_space:
                expected = reduce(lambda x, y: x * y, (powers[i][profile[i]][target[i]] for i in range(len(profile))), Fraction(1))
                require(literal.get(target, Fraction(0)) == expected, "UDC target atlas")
            absorption = reduce(lambda x, y: x * y, (powers[i][profile[i]][0] for i in range(len(profile))), Fraction(1))
            require(literal.get(tuple(0 for _ in profile), Fraction(0)) == absorption, "UDC clock CDF")
            if profile == (2, 3) and t == 3:
                signature = absorption
    require(signature is not None, "UDC signature")
    return signature


# SBW: fair Calkin--Wilf/Stern--Brocot child walk.
def sb_children(pair):
    a, b = pair
    return ((a, a + b), (a + b, b))


def sb_inverse(pair):
    a, b = pair
    reverse_word = []
    while (a, b) != (1, 1):
        require(a != b and a > 0 and b > 0, "SBW inverse domain")
        if a > b:
            reverse_word.append(1)
            a -= b
        else:
            reverse_word.append(0)
            b -= a
    return tuple(reversed(reverse_word))


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def sbw_checks():
    signature = None
    states = {(1, 1): ()}
    for depth in range(13):
        require(len(states) == 1 << depth, "SBW distinct level")
        sums = []
        for pair, word in states.items():
            require(gcd(*pair) == 1, "SBW primitive pair")
            require(sb_inverse(pair) == word, "SBW inverse word")
            sums.append(sum(pair))
        require(min(sums) == depth + 2, "SBW minimum")
        require(max(sums) == fibonacci(depth + 3), "SBW Fibonacci maximum")
        if depth == 6:
            signature = (len(states), min(sums), max(sums))
        nxt = {}
        for pair, word in states.items():
            for choice, child in enumerate(sb_children(pair)):
                require(child not in nxt, "SBW child injectivity")
                nxt[child] = word + (choice,)
        states = nxt
    require(signature == (64, 8, 34), "SBW signature")
    return signature


# BSR: binary affine shift register x -> 2x+B modulo 2^h.
def bsr_checks():
    signature = None
    for height in range(1, 9):
        modulus = 1 << height
        for source in range(modulus):
            law = Counter({source: 1})
            for t in range(height + 3):
                for target in range(modulus):
                    if t < height:
                        residue = (target - (source << t)) % modulus
                        expected = int(residue < (1 << t))
                    else:
                        expected = 1 << (t - height)
                    require(law[target] == expected, "BSR target history")
                require(sum(law.values()) == 1 << t, "BSR mass")
                if height == 5 and source == 7 and t == 5:
                    signature = (len(law), min(law.values()), max(law.values()))
                nxt = Counter()
                for state, count in law.items():
                    nxt[(2 * state) % modulus] += count
                    nxt[(2 * state + 1) % modulus] += count
                law = nxt
        for x in range(modulus):
            for y in range(modulus):
                require(((1 << height) * (x - y)) % modulus == 0, "BSR synchronizing difference")
    require(signature == (32, 1, 1), "BSR signature")
    return signature


# ECR: Ewens/Chinese-restaurant cycle-shape growth.
def integer_partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    if maximum is None or maximum > n:
        maximum = n
    for first in range(maximum, 0, -1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def rising(x, n):
    answer = 1
    for i in range(n):
        answer *= x + i
    return answer


def z_lambda(partition):
    counts = Counter(partition)
    answer = 1
    for size, multiplicity in counts.items():
        answer *= size**multiplicity * factorial(multiplicity)
    return answer


def unsigned_stirling_first(n, k):
    table = [[0] * (n + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            table[i][j] = table[i - 1][j - 1] + (i - 1) * table[i - 1][j]
    return table[n][k]


def ecr_checks():
    signature = None
    for theta in range(1, 5):
        law = {(): Fraction(1)}
        for n in range(0, 8):
            if n:
                for partition in integer_partitions(n):
                    multiplicities = Counter(partition)
                    expected = Fraction(factorial(n) * theta ** len(partition), rising(theta, n) * z_lambda(partition))
                    require(law.get(partition, 0) == expected, "ECR Ewens shape")
                for cycles in range(1, n + 1):
                    observed = sum(prob for partition, prob in law.items() if len(partition) == cycles)
                    expected = Fraction(unsigned_stirling_first(n, cycles) * theta**cycles, rising(theta, n))
                    require(observed == expected, "ECR cycle-count law")
                require(sum(law.values()) == 1, "ECR mass")
                if theta == 2 and n == 5:
                    signature = tuple(sum(prob for part, prob in law.items() if len(part) == k) for k in range(1, 6))
            nxt = defaultdict(Fraction)
            for partition, mass in law.items():
                denominator = theta + n
                nxt[tuple(sorted(partition + (1,), reverse=True))] += mass * Fraction(theta, denominator)
                counts = Counter(partition)
                for size, multiplicity in counts.items():
                    grown = list(partition)
                    grown.remove(size)
                    grown.append(size + 1)
                    nxt[tuple(sorted(grown, reverse=True))] += mass * Fraction(size * multiplicity, denominator)
            law = dict(nxt)
    require(signature == (Fraction(1, 15), Fraction(5, 18), Fraction(7, 18), Fraction(2, 9), Fraction(2, 45)), "ECR signature")
    return signature


# PLU: two-colour Pólya reinforcement urn.
def rising_factorial(x, k):
    answer = 1
    for i in range(k):
        answer *= x + i
    return answer


def plu_checks():
    signature = None
    for alpha in range(1, 5):
        for beta in range(1, 5):
            law = {0: Fraction(1)}
            for t in range(9):
                for k in range(t + 1):
                    expected = Fraction(
                        comb(t, k) * rising_factorial(alpha, k) * rising_factorial(beta, t - k),
                        rising_factorial(alpha + beta, t),
                    )
                    require(law.get(k, 0) == expected, "PLU beta-binomial")
                require(sum(law.values()) == 1, "PLU mass")
                for word in product((0, 1), repeat=t):
                    reds = sum(word)
                    probability = Fraction(1)
                    r, b = alpha, beta
                    for draw in word:
                        probability *= Fraction(r if draw else b, r + b)
                        if draw:
                            r += 1
                        else:
                            b += 1
                    expected_word = Fraction(
                        rising_factorial(alpha, reds) * rising_factorial(beta, t - reds),
                        rising_factorial(alpha + beta, t),
                    )
                    require(probability == expected_word, "PLU path exchangeability")
                if alpha == 2 and beta == 3 and t == 4:
                    signature = tuple(law[k] for k in range(5))
                nxt = defaultdict(Fraction)
                for k, mass in law.items():
                    nxt[k + 1] += mass * Fraction(alpha + k, alpha + beta + t)
                    nxt[k] += mass * Fraction(beta + t - k, alpha + beta + t)
                law = dict(nxt)
    require(signature is not None, "PLU signature")
    return signature


# BGW: critical 0-or-2 Galton--Watson frontier.
def catalan(k):
    return comb(2 * k, k) // (k + 1)


def bgw_checks():
    law = {1: Fraction(1)}
    extinction = []
    for t in range(7):
        extinction.append(law.get(0, Fraction(0)))
        for s in (Fraction(0), Fraction(1, 3), Fraction(1, 2), Fraction(1)):
            observed = sum(probability * s**population for population, probability in law.items())
            value = s
            for _ in range(t):
                value = (1 + value * value) / 2
            require(observed == value, "BGW iterated PGF")
        require(sum(law.values()) == 1, "BGW mass")
        nxt = defaultdict(Fraction)
        for population, mass in law.items():
            for parents_with_two in range(population + 1):
                nxt[2 * parents_with_two] += mass * Fraction(comb(population, parents_with_two), 2**population)
        law = dict(nxt)
    progeny = []
    for k in range(9):
        value = Fraction(catalan(k), 2 ** (2 * k + 1))
        progeny.append(value)
        if k == 0:
            require(value == Fraction(1, 2), "BGW progeny base")
        else:
            rhs = Fraction(1, 2) * sum((progeny[i] * progeny[k - 1 - i] for i in range(k)), Fraction(0))
            require(value == rhs, "BGW Catalan progeny recursion")
    return extinction[4]


def main():
    results = [
        ("DCI", dci_checks()),
        ("LSC", lsc_checks()),
        ("QHI", qhi_checks()),
        ("HCI", hci_checks()),
        ("ORW", orw_checks()),
        ("KMP", kmp_checks()),
        ("GSW", gsw_checks()),
        ("TTW", ttw_checks()),
        ("PTW", ptw_checks()),
        ("CDP", cdp_checks()),
        ("UDC", udc_checks()),
        ("SBW", sbw_checks()),
        ("BSR", bsr_checks()),
        ("ECR", ecr_checks()),
        ("PLU", plu_checks()),
        ("BGW", bgw_checks()),
    ]
    print("P162-P166 STOCHASTIC/SPATIAL BREADTH SCOUT")
    print("systems=16")
    for name, signature in results:
        print(f"{name}={signature}")
    print(f"assertions={ASSERTIONS}")
    print("status=PASS")
    print("external=HOLD_EXTERNAL")


if __name__ == "__main__":
    main()
