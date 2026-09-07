#!/usr/bin/env python3
"""P207 B: sign-lift quotient, two-time-column graph, source-pair inverse.

Standalone stdlib producer. No files are read and no author or A code/data
are imported. Fixed bounds are the original review bounds, not new atlases.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
import sys

assert sys.flags.optimize == 0 and __debug__
CHECKS = 0


def ck(ok, detail=None):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(detail)


def digest(value):
    return sha256(json.dumps(value, separators=(",", ":"), sort_keys=True).encode()).hexdigest()


def sign(z):
    return (z > 0) - (z < 0)


def update(x, upper=True):
    n = len(x)
    if upper:
        return tuple(int(x[(i-1) % n] > x[i]) + int(x[(i+1) % n] > x[i]) for i in range(n))
    return tuple(int(x[(i-1) % n] < x[i]) + int(x[(i+1) % n] < x[i]) for i in range(n))


def encode(x):
    r = 0
    for v in x:
        r = 3*r + v
    return r


def extrema(x):
    n = len(x)
    return {i for i in range(n) if (x[(i-1) % n]-x[i])*(x[(i+1) % n]-x[i]) > 0}


def local_certificate():
    census = Counter()
    all_hash = sha256()
    changed_records = []
    for edge in product((-1, 0, 1), repeat=12):
        # suffix[j][a] counts height lifts of edge[j:] beginning at a.
        suffix = [[0]*3 for _ in range(13)]
        suffix[12] = [1, 1, 1]
        for j in range(11, -1, -1):
            suffix[j] = [sum(suffix[j+1][b] for b in range(3) if sign(b-a) == edge[j]) for a in range(3)]
        weight = sum(suffix[0])
        census['sign_words'] += 1
        if weight == 0:
            census['unrealizable'] += 1
            continue
        census['realizable'] += 1
        census['height_lifts'] += weight
        a = next(a for a in range(3) if suffix[0][a])
        lift = [a]
        for j, e in enumerate(edge):
            a = next(b for b in range(3) if sign(b-a) == e and suffix[j+1][b])
            lift.append(a)
        ck(tuple(sign(lift[i+1]-lift[i]) for i in range(12)) == edge)
        initial_extrema = {j for j in range(-5, 6) if edge[j+5]*edge[j+6] == -1}
        rows = [tuple(lift)]
        sgn = edge
        for t in range(4):
            row = tuple(int(sgn[i-1] < 0)+int(sgn[i] > 0) for i in range(1, len(sgn)))
            prev = rows[-1]
            direct = tuple(int(prev[i-1] > prev[i])+int(prev[i+1] > prev[i]) for i in range(1, len(prev)-1))
            ck(row == direct)
            rows.append(row)
            sgn = tuple(sign(row[i+1]-row[i]) for i in range(len(row)-1))
        changed = rows[4][2] != rows[2][4]
        witness = None
        if changed:
            census['changed_classes'] += 1
            census['changed_height_lifts'] += weight
            for t in range(1, 5):
                row = rows[t]
                for j in range(-(5-t), 6-t):
                    p = j+6-t
                    if j not in initial_extrema and (row[p-1]-row[p])*(row[p+1]-row[p]) > 0:
                        witness = (t, j)
                        break
                if witness is not None:
                    break
            ck(witness is not None, (edge, lift, rows))
            t, j = witness
            p = j+6-t
            ck((lift[j+5]-lift[j+6])*(lift[j+7]-lift[j+6]) <= 0)
            ck((rows[t][p-1]-rows[t][p])*(rows[t][p+1]-rows[t][p]) > 0)
            changed_records.append([''.join(str(e+1) for e in edge), weight, t, j])
        else:
            census['equal_classes'] += 1
            census['equal_height_lifts'] += weight
        all_hash.update(json.dumps([edge, weight, rows[2][4], rows[4][2], witness], separators=(",", ":")).encode()+b'\n')
    ck(census['sign_words'] == 3**12)
    ck(census['height_lifts'] == 3**13)
    ck(census['equal_height_lifts'] + census['changed_height_lifts'] == 3**13)
    return {'census': dict(census), 'all_realizable_records_sha256': all_hash.hexdigest(),
            'changed_sign_classes': changed_records,
            'sign_encoding': 'character 0=-1,1=0,2=+1; record=[sign_word,lift_count,time,site]'}


def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matmul(a, b):
    n = len(a)
    c = [[0]*n for _ in range(n)]
    for i in range(n):
        for k, v in enumerate(a[i]):
            if v:
                for j, w in enumerate(b[k]):
                    if w:
                        c[i][j] += v*w
    return c


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def bareiss(a):
    a = [row[:] for row in a]
    n = len(a)
    prev = 1
    parity = 1
    for k in range(n-1):
        if a[k][k] == 0:
            swap = next((i for i in range(k+1, n) if a[i][k]), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            parity *= -1
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                num = a[i][j]*pivot-a[i][k]*a[k][j]
                ck(num % prev == 0)
                a[i][j] = num//prev
            a[i][k] = 0
        prev = pivot
    return parity*a[-1][-1]


def interpolate_integer(values):
    # Newton forward differences times binomial(z,k); no trace/Newton identities.
    delta = values[:]
    basis = [Fraction(1)]
    out = [Fraction(0)]*len(values)
    for k in range(len(values)):
        for i, v in enumerate(basis):
            out[i] += delta[0]*v
        delta = [delta[i+1]-delta[i] for i in range(len(delta)-1)]
        if k+1 < len(values):
            nxt = [Fraction(0)]*(len(basis)+1)
            for i, v in enumerate(basis):
                nxt[i] -= k*v/(k+1)
                nxt[i+1] += v/(k+1)
            basis = nxt
    ck(all(v.denominator == 1 for v in out))
    return [int(v) for v in out]


def core_graph():
    columns = [(0, 0), (0, 2), (2, 0), (0, 1), (1, 0), (1, 1)]
    pairs = list(product(range(6), repeat=2))
    pi = {v: i for i, v in enumerate(pairs)}
    adj = [[] for _ in pairs]
    triples = []
    for l, c, r in product(range(6), repeat=3):
        left, center, right = columns[l], columns[c], columns[r]
        if (center[1] == int(left[0] > center[0])+int(right[0] > center[0]) and
                center[0] == int(left[1] > center[1])+int(right[1] > center[1])):
            adj[pi[l, c]].append(pi[c, r])
            triples.append([l, c, r])
    matrix = [[int(j in adj[i]) for j in range(36)] for i in range(36)]
    values = [bareiss([[int(i == j)-z*matrix[i][j] for j in range(36)] for i in range(36)]) for z in range(37)]
    polynomial = interpolate_integer(values)
    d = [1, 0, -1, -4, -2, 0, 0, 0, 1]
    expected = [0]*37
    for i, v in enumerate(d):
        expected[i] += v
        expected[i+1] -= v
    ck(polynomial == expected, polynomial)
    power = identity(36)
    traces = []
    for n in range(1, 61):
        # Sparse right multiplication is a direct count of closed walks.
        nxt = [[0]*36 for _ in range(36)]
        for i in range(36):
            for k, val in enumerate(power[i]):
                if val:
                    for j in adj[k]:
                        nxt[i][j] += val
        power = nxt
        traces.append(trace(power))
    a = [v-1 for v in traces]
    ck(a[:8] == [0, 2, 12, 10, 20, 62, 84, 154])
    for n in range(9, 61):
        ck(a[n-1] == a[n-3]+4*a[n-4]+2*a[n-5]-a[n-9])
    return {'columns': columns, 'vertices': pairs, 'allowed_triples': triples,
            'integer_determinant_samples_z0_to36': values,
            'determinant_coefficients_degree0_to36': polynomial, 'closed_walk_traces_1_to60': traces}


def language(x):
    n = len(x)
    if not any(x):
        return True
    if 0 not in x:
        return False
    start = next(i for i in range(n) if x[i] == 0 and x[i-1] != 0)
    word = x[start:]+x[:start]
    zero = []
    positive = []
    p = 0
    while p < n:
        q = p
        while q < n and word[q] == 0:
            q += 1
        zero.append(q-p)
        p = q
        while q < n and word[q] != 0:
            q += 1
        positive.append(word[p:q])
        p = q
    if not all(v in (1, 2) for v in zero):
        return False
    allowed = {(2,), (1, 1), (1, 2), (2, 1), (1, 2, 1)}
    for i, w in enumerate(positive):
        if w not in allowed:
            return False
        if w in ((1, 2), (1, 2, 1)) and zero[i] != 1:
            return False
        if w in ((2, 1), (1, 2, 1)) and zero[(i+1) % len(zero)] != 1:
            return False
    return True


def lucas(n):
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a+b
    return a


def rotate_set(word):
    return {word[i:]+word[:i] for i in range(len(word))}


def equality_words(n):
    m = n//2
    if n == 3:
        return {(0, 0, 0)} | rotate_set((0, 0, 2)) | rotate_set((0, 1, 1))
    if n % 2 == 0:
        return rotate_set((0, 2)*m)
    return rotate_set((0, 0)+(2, 0)*(m-1)+(2,)) | rotate_set((0, 1, 1)+(0, 2)*(m-1))


def source_pair_machine():
    pairs = list(product(range(3), repeat=2))
    edges = [[[] for _ in range(9)] for _ in range(3)]
    for state, (a, b) in enumerate(pairs):
        for c in range(3):
            rank = int(a > b)+int(c > b)
            edges[rank][state].append(3*b+c)
    return pairs, edges


def all_target_traces(n, edges):
    values = []
    def descend(depth, p):
        if depth == n:
            values.append(trace(p))
            return
        for rank in range(3):
            q = [[0]*9 for _ in range(9)]
            for i in range(9):
                for k, v in enumerate(p[i]):
                    if v:
                        for j in edges[rank][k]:
                            q[i][j] += v
            descend(depth+1, q)
    descend(0, identity(9))
    return values


def decode_target(target, pairs, edges):
    n = len(target)
    out = []
    def descend(depth, state, initial, code):
        if depth == n:
            if state == initial:
                out.append(code)
            return
        code = 3*code+pairs[state][1]
        for nxt in edges[target[depth]][state]:
            descend(depth+1, nxt, initial, code)
    for initial in range(9):
        descend(0, initial, initial, 0)
    return sorted(out)


def cyclic_boxes(graph):
    pairs, edges = source_pair_machine()
    summaries = []
    for n in range(3, 11):
        words = list(product(range(3), repeat=n))
        successor = [encode(update(x)) for x in words]
        source_sets = [[] for _ in words]
        for i, x in enumerate(words):
            target = successor[i]
            source_sets[target].append(i)
            ck(update(tuple(2-v for v in x), False) == words[target])
            e0, e1 = extrema(x), extrema(words[target])
            ck(e0 <= e1)
            ck(all(words[target][j] == (2 if x[j] < x[j-1] else 0) for j in e0))
        current = list(range(len(words)))
        heights = [-1]*len(words)
        layers = []
        # Simultaneous time filtration, not Kahn peeling or per-orbit walks.
        for t in range(4*n+3):
            newly = 0
            for i, cur in enumerate(current):
                if heights[i] < 0 and successor[successor[cur]] == cur:
                    heights[i] = t
                    newly += 1
            layers.append(newly)
            if min(heights) >= 0:
                break
            current = [successor[cur] for cur in current]
        ck(min(heights) >= 0)
        for i, x in enumerate(words):
            core = successor[successor[i]] == i
            ck(core == language(x), (n, x))
            ck((successor[i] == i) == (i == 0))
            ck((heights[i] == 0) == core)
        trace_counts = all_target_traces(n, edges)
        inverse_hash = sha256()
        for target_code, target in enumerate(words):
            decoded = decode_target(target, pairs, edges)
            ck(decoded == source_sets[target_code], (n, target, decoded, source_sets[target_code]))
            ck(len(decoded) == trace_counts[target_code])
            inverse_hash.update(json.dumps([target_code, decoded], separators=(",", ":")).encode()+b'\n')
        counts = list(map(len, source_sets))
        maximum = max(counts)
        attaining = {words[i] for i, v in enumerate(counts) if v == maximum}
        ck(maximum == lucas(2*(n//2)))
        ck(attaining == equality_words(n), (n, attaining))
        ck(layers[0] == graph['closed_walk_traces_1_to60'][n-1])
        if n == 3:
            ck(max(heights) == 1 and heights[encode((0, 0, 1))] == 1)
        summaries.append({'n': n, 'states': len(words), 'image': sum(v > 0 for v in counts),
                          'core': layers[0], 'fixed': 1, 'period2_cycles': (layers[0]-1)//2,
                          'height_distribution': layers, 'max_height': max(heights),
                          'max_fibre': maximum, 'all_maximizers': sorted(attaining),
                          'successor_sha256': digest(successor), 'fibre_counts_sha256': digest(counts),
                          'every_labelled_inverse_set_sha256': inverse_hash.hexdigest()})
    return {'machine_pairs': pairs, 'machine_edges_by_target': edges, 'boxes': summaries}


def positive_kernels():
    expected = {(2,): [[2,1,0],[1,1,0],[0,0,0]], (1,): [[0,1,1],[1,0,1],[1,1,0]],
                (1,1): [[2,1,1],[1,1,0],[1,0,0]], (1,2): [[1,1,0],[0,0,0],[0,0,0]],
                (2,1): [[1,0,0],[1,0,0],[0,0,0]], (1,1,1): [[2,1,0],[1,0,0],[0,0,0]],
                (1,2,1): [[1,0,0],[0,0,0],[0,0,0]], (1,1,1,1): [[1,0,0],[0,0,0],[0,0,0]]}
    census = []
    local_hash = sha256()
    for length in range(1, 7):
        found = {}
        for a, b in product(range(3), repeat=2):
            for u in product((1, 2), repeat=length):
                v = (a,)+u+(b,)
                w = tuple(int(v[i-1] < v[i])+int(v[i+1] < v[i]) for i in range(1, length+1))
                if a <= u[0] and b <= u[-1] and all(w):
                    found.setdefault(w, [[0]*3 for _ in range(3)])[a][b] += 1
                    local_hash.update(json.dumps([a, b, u, w], separators=(",", ":")).encode()+b'\n')
        for w in product((1, 2), repeat=length):
            ck(found.get(w, [[0]*3 for _ in range(3)]) == expected.get(w, [[0]*3 for _ in range(3)]), w)
        census.append({'length': length, 'nonzero_words': len(found), 'local_strings': sum(sum(map(sum, m)) for m in found.values())})
    return expected, {'census': census, 'local_source_catalog_sha256': local_hash.hexdigest(),
                       'kernels': {''.join(map(str, w)): v for w, v in expected.items()}}


def matrix_pressure(kernels):
    a, j, b = kernels[2,], kernels[1,], kernels[1,1]
    matrices = [a, j, b]
    records = []
    power = identity(3)
    for r in range(1, 101):
        previous = power
        power = matmul(power, a)
        ck(trace(power) == lucas(2*r))
        if r >= 2:
            ck(trace(matmul(b, previous)) == trace(power))
            ck(trace(matmul(kernels[1,2], previous)) < trace(power))
            ck(trace(matmul(kernels[2,1], previous)) < trace(power))
        # Exact rational lower bounds used by the handwritten norm argument.
        if r >= 2:
            ck(Fraction(10,9)*3**r < Fraction(13,5)**(r+r//2))
    ck(Fraction(13,5)**2 > 6)
    ck(Fraction(13,5)**6 > 270)
    ck(Fraction(13,5)**3 > 10 and Fraction(13,5)**4 > 30)
    for r in range(2, 11):
        maximum = 0
        classes = Counter()
        word_hash = sha256()
        for w in product(range(3), repeat=r):
            p = identity(3)
            for letter in w:
                p = matmul(p, matrices[letter])
            value = trace(p)
            k, nj = w.count(2), w.count(1)
            if k <= 1:
                ck(value <= lucas(2*r))
                if nj:
                    ck(value < lucas(2*r))
                else:
                    ck(value == lucas(2*r))
            else:
                ck(value < lucas(2*(r+k//2)))
            maximum = max(maximum, value)
            classes[k, nj] += 1
            word_hash.update(json.dumps([w, value], separators=(",", ":")).encode()+b'\n')
        records.append({'length': r, 'words': 3**r, 'maximum_raw_trace': maximum,
                        'class_counts': [[k, j, v] for (k, j), v in sorted(classes.items())],
                        'all_product_traces_sha256': word_hash.hexdigest()})
    return records


def seed_checks():
    rows = []
    for n in range(4, 65):
        m = n//2
        z = (2,)+(0,)*(n-1)
        for t in range(m):
            expected = []
            for i in range(n):
                d = min(i, n-i)
                expected.append(2*int(t % 2 == 0) if d == 0 else 2*int((t-d) % 2 == 0) if d < t else 1 if d == t else 0)
            ck(z == tuple(expected), (n, t))
            ck(update(update(z)) != z)
            z = update(z)
        ck(update(update(z)) == z and language(z))
        source = (0,)+(1,)*(n-1)
        ck(update(source) == (2,)+(0,)*(n-1))
        ck(update(update(source)) != source)
        rows.append({'n': n, 'seed20_height': m, 'seed01_height': m+1, 'meeting_word': z})
    return rows


def independent_sets():
    records = []
    for n in (4, 6, 8, 10):
        target = (0, 2)*(n//2)
        mapped = set()
        for marks in product((0, 1), repeat=n):
            if any(marks[i] and marks[(i+1) % n] for i in range(n)):
                continue
            lower_source = tuple(1 if marks[i] else 0 if i % 2 == 0 else 2 for i in range(n))
            ck(update(lower_source, False) == target)
            ck(tuple(int(v == 1) for v in lower_source) == marks)
            mapped.add(lower_source)
        all_sources = {x for x in product(range(3), repeat=n) if update(x, False) == target}
        ck(mapped == all_sources and len(mapped) == lucas(n))
        records.append({'n': n, 'count': len(mapped), 'source_set_sha256': digest(sorted(mapped))})
    return records


def main():
    local = local_certificate()
    graph = core_graph()
    cyclic = cyclic_boxes(graph)
    kernels, kernel_report = positive_kernels()
    pressure = matrix_pressure(kernels)
    seeds = seed_checks()
    attainers = independent_sets()
    ck(update((0,2,0,2), False) == (0,2,0,2))
    ck(update((0,2,0,2)) == (2,0,2,0))
    # Equal center and neighbor sum are insufficient for the literal rank.
    ck(int(0 > 1)+int(2 > 1) != int(1 > 1)+int(1 > 1))
    print(json.dumps({'review': 'P207 actual manuscript B', 'status': 'PASS', 'assertions': CHECKS,
                      'local_sign_lift_certificate': local, 'two_time_column_pair_graph': graph,
                      'source_pair_inverse_and_time_filtration': cyclic, 'positive_kernels': kernel_report,
                      'mixed_matrix_pressure': pressure, 'single_seed_witnesses': seeds,
                      'deducted_independent_set_attainers': attainers,
                      'scope': 'original fixed bounds only; all-length arguments remain deductive; source access not closed by execution'},
                     sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
