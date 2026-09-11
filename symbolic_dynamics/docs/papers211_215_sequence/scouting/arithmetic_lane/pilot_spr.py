"""The sole preregistered SPR pilot. Author code; no scientific imports."""
import gzip
import hashlib
import itertools
import json
import pathlib
import sys

BASE = pathlib.Path(__file__).resolve().parent


def encode(obj):
    return (json.dumps(obj, sort_keys=True, separators=(',', ':')) + '\n').encode()


def emit(obj):
    sys.stdout.buffer.write(encode(obj))
    sys.stdout.buffer.flush()


def check(condition, *detail):
    if not condition:
        raise AssertionError(detail)


def direct(x):
    positive = sorted(v for v in x if v)
    if len(positive) <= 1:
        return x
    pivot = positive[1]
    return tuple(v % pivot for v in x)


def histogram_map(x, M):
    counts = [0] * (M + 1)
    for v in x:
        counts[v] += 1
    if len(x) - counts[0] <= 1:
        return x
    seen = 0
    pivot = None
    for value in range(1, M + 1):
        seen += counts[value]
        if seen >= 2:
            pivot = value
            break
    check(pivot is not None, 'missing histogram pivot', x)
    return tuple(v - pivot * (v // pivot) for v in x)


def support(x):
    return sum(v > 0 for v in x)


def reverse(a):
    a = tuple(sorted(a))
    m = a[-1]
    return (m, m + 1) + tuple(m + 1 + v for v in a[:-1])


def weak_le(a, b):
    aa, bb = sorted(a, reverse=True), sorted(b, reverse=True)
    sa = sb = 0
    for j in range(max(len(aa), len(bb))):
        sa += aa[j] if j < len(aa) else 0
        sb += bb[j] if j < len(bb) else 0
        if sa > sb:
            return False
    return True


def product(values):
    result = 1
    for value in values:
        result *= value
    return result


def fibre_formula(y, M):
    positive = [v for v in y if v]
    r, k = len(positive), len(y) - len(positive)
    total = int(r <= 1)
    for p in range(max(y) + 1, M + 1):
        B = M // p
        A = [(M - v) // p for v in positive]
        P = product(A)
        Q = sum(product(A[:i] + A[i+1:]) for i in range(r))
        D = (B + 1) ** k - B ** k
        E = D - k * B ** (k - 1) if k else 0
        total += D * Q + E * P
    return total


def zero_formula(n, M):
    return 1 + sum((M // p + 1) ** n - (M // p) ** n
                   - n * (M // p) ** (n - 1)
                   for p in range(1, M + 1))


def verify_decoder(x, y, M):
    if support(x) <= 1:
        check(x == y and support(y) <= 1, 'fixed decoder', x, y)
        return
    p = sorted(v for v in x if v)[1]
    check(max(y) < p <= M, 'pivot range', x, y, p)
    subpivot = 0
    equal_pivot = 0
    for source, target in zip(x, y):
        q, residue = divmod(source, p)
        check(residue == target, 'decoder residue', x, y)
        if target:
            check(0 <= q <= (M - target) // p, 'positive quotient', x, y)
            subpivot += q == 0
        else:
            check(0 <= q <= M // p, 'zero quotient', x, y)
            equal_pivot += q == 1
    check((subpivot == 1 and equal_pivot >= 1)
          or (subpivot == 0 and equal_pivot >= 2), 'inverse cases', x, y)


def runtime_surface():
    paths = {str(pathlib.Path(sys.executable).resolve())}
    modules = {}
    for name, module in sorted(sys.modules.items()):
        raw = getattr(module, '__file__', None)
        spec = getattr(module, '__spec__', None)
        origin = getattr(spec, 'origin', None)
        if raw and pathlib.Path(raw).is_file():
            resolved = str(pathlib.Path(raw).resolve())
            paths.add(resolved)
            modules[name] = resolved
        else:
            modules[name] = origin or 'no-file-no-spec'
    mappings = pathlib.Path('/proc/self/maps').read_text().splitlines()
    for line in mappings:
        parts = line.split(None, 5)
        if len(parts) == 6 and parts[5].startswith('/'):
            path = pathlib.Path(parts[5])
            if path.is_file():
                paths.add(str(path.resolve()))
    pins = {path: hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()
            for path in sorted(paths)}
    return {'module_origins': modules, 'visible_file_sha256': pins,
            'python': sys.version, 'executable': sys.executable,
            'sys_path': sys.path,
            'limitations': 'Declared sys.modules and mapped-file surface only; not hermetic closure.'}


def main():
    chain = {1: (1, 1)}
    for t in range(2, 5):
        chain[t] = reverse(chain[t - 1])
    emit({'kind': 'preregistered_scope', 'n': [1, 2, 3, 4, 5],
          'M': [0, 1, 2, 3, 4, 5, 6], 'reverse_chain': chain,
          'state_record_schema': ['x', 'T(x)', 'h(x)', 'indegree(x)']})
    states_total = 0
    records_digest = hashlib.sha256()
    records_path = BASE / 'sole_pilot' / 'state_records.jsonl.gz'
    with records_path.open('xb') as raw_records:
        with gzip.GzipFile(filename='', mode='wb', fileobj=raw_records,
                           compresslevel=9, mtime=0) as records:
            for n in range(1, 6):
                for M in range(7):
                    states = list(itertools.product(range(M + 1), repeat=n))
                    images = {}
                    incoming = dict.fromkeys(states, 0)
                    for x in states:
                        y = direct(x)
                        check(y == histogram_map(x, M), 'literal mismatch', n, M, x)
                        check(y in incoming, 'carrier', n, M, x, y)
                        check((y == x) == (support(x) <= 1), 'fixed', x, y)
                        if y != x:
                            check(support(y) < support(x), 'support', x, y)
                        if support(y) >= 2:
                            check(weak_le(reverse(tuple(v for v in y if v)), x),
                                  'reverse predecessor lemma', x, y)
                        verify_decoder(x, y, M)
                        images[x] = y
                        incoming[y] += 1
                    heights = {}
                    for x in states:
                        orbit_seen = set()
                        current = x
                        while images[current] != current:
                            check(current not in orbit_seen, 'nontrivial cycle', x)
                            orbit_seen.add(current)
                            current = images[current]
                        h = len(orbit_seen)
                        check(h <= max(0, support(x) - 1), 'support height', x, h)
                        heights[x] = h
                        for t in range(1, h + 1):
                            check(weak_le(chain[t], x), 'height majorization', x, t)
                    H = max(heights.values())
                    predicted_H = max([0] + [t for t, c in chain.items()
                                      if t + 1 <= n and max(c) <= M])
                    check(H == predicted_H, 'height threshold', n, M, H, predicted_H)
                    for t, c in chain.items():
                        if t + 1 <= n and max(c) <= M:
                            witness = c + (0,) * (n - len(c))
                            check(heights[witness] == t, 'attainment', n, M, t)
                    for y in states:
                        check(incoming[y] == fibre_formula(y, M), 'full fibre', n, M, y,
                              incoming[y], fibre_formula(y, M))
                    check(sum(incoming.values()) == len(states), 'mass', n, M)
                    degree_max = max(incoming.values())
                    maximizing_targets = [y for y in states if incoming[y] == degree_max]
                    zero = (0,) * n
                    check(incoming[zero] == zero_formula(n, M), 'zero formula', n, M)
                    if n >= 2 and M >= 1:
                        check(maximizing_targets == [zero], 'strict maximum', n, M)
                    else:
                        check(degree_max == 1 and len(maximizing_targets) == len(states),
                              'identity boundary', n, M)
                    height_histogram, fibre_histogram = {}, {}
                    digest = hashlib.sha256()
                    box_marker = encode({'box': [n, M]})
                    records.write(box_marker)
                    records_digest.update(box_marker)
                    for x in states:
                        h, d = heights[x], incoming[x]
                        height_histogram[h] = height_histogram.get(h, 0) + 1
                        fibre_histogram[d] = fibre_histogram.get(d, 0) + 1
                        record = encode([x, images[x], h, d])
                        records.write(record)
                        records_digest.update(record)
                        digest.update(record)
                    emit({'kind': 'box_pass', 'n': n, 'M': M, 'states': len(states),
                          'max_height': H, 'first_max_height_witness': next(x for x in states if heights[x] == H),
                          'height_histogram': height_histogram, 'fibre_histogram': fibre_histogram,
                          'max_fibre': degree_max, 'all_max_fibre_targets': maximizing_targets,
                          'per_state_records_sha256': digest.hexdigest()})
                    states_total += len(states)
    emit({'kind': 'all_checks_pass', 'boxes': 35, 'states': states_total,
          'records_uncompressed_sha256': records_digest.hexdigest(),
          'records_gzip_sha256': hashlib.sha256(records_path.read_bytes()).hexdigest(),
          'runtime_surface': runtime_surface()})


if __name__ == '__main__':
    main()
